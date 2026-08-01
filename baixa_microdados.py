#!/usr/bin/env python3
"""Baixa os microdados do SISCAN e extrai Pernambuco em streaming.

Motivo: a via agregada do TABNET data a série pela liberação do laudo, e a data
da coleta — o ato que a política incentiva — não existe como dimensão de
tabulação. Os microdados trazem CO_INTERVALO_COLETA e CO_TEMPO_EXAME por exame,
o que permite reconstruir a data de coleta e reestimar a série no eixo certo.

Ver docs/ACHADOS_EIXO_TEMPORAL_E_MOTIVO.md para a medição que motivou isto.

Os arquivos nacionais somam cerca de 14 GB e o FTP entrega 130 a 265 KB/s por
conexão, então isto leva horas. O filtro roda em streaming: o arquivo nacional
nunca toca o disco, só as linhas de PE (cerca de 5%).

Uso:
    python3 baixa_microdados.py                 # todos os anos
    python3 baixa_microdados.py 2018            # um ano, para validar
    python3 baixa_microdados.py --status        # o que já foi baixado
"""

import ftplib
import json
import sys
import time
from pathlib import Path

HOST = "ftp.datasus.gov.br"
DIR = "/dissemin/publicos/SISCAN/SISCAN"
DESTINO = Path(__file__).parent / "data" / "microdados"
ANOS = range(2018, 2027)
UF_PE = b'"26"'
CAMPO_UF = 2  # CO_UF_RESIDENCIA é o 3º campo (índice 2)

# O FTP do DATASUS derruba conexões longas — um arquivo de 1,7 GB a 200 KB/s
# leva mais de duas horas e não sobrevive inteiro. A retomada por REST é o que
# torna o download viável; sem ela nenhum ano completa.
TENTATIVAS = 40
ESPERA = 20


def baixa_ano(ano, base_nome="SISCAN_CITO_COLO"):
    """Baixa um ano e grava só as linhas de PE. Idempotente e retomável.

    Retoma de onde parou usando REST do FTP. O estado (offset de bytes na
    origem) fica num sidecar .estado, para que uma interrupção no meio não
    obrigue a recomeçar do zero.
    """
    saida = DESTINO / f"{base_nome}_{ano}_PE.csv"
    parcial = saida.with_suffix(".parcial")
    estado_f = saida.with_suffix(".estado")

    if saida.exists():
        with open(saida, "rb") as fh:
            return f"já existe, {sum(1 for _ in fh) - 1:,} linhas", saida.stat().st_size

    nome = f"{base_nome}_{ano}.csv"
    est = json.loads(estado_f.read_text()) if estado_f.exists() else {"offset": 0, "pe": 0}
    offset, linhas_pe = est["offset"], est["pe"]
    t0 = time.monotonic()

    # Tamanho na origem, para conferir no final. O FTP do DATASUS encerra a
    # transferência limpa quando trunca: o cliente vê fim de arquivo e sai com
    # sucesso, deixando um CSV bem-formado com uma fração dos dados. Sem esta
    # conferência o truncamento passa silencioso — foi assim que uma sondagem
    # anterior concluiu coisas erradas a partir de um sexto dos registros.
    try:
        ftp_meta = ftplib.FTP(HOST, timeout=60)
        ftp_meta.login()
        ftp_meta.cwd(DIR)
        ftp_meta.voidcmd("TYPE I")
        tamanho_origem = ftp_meta.size(nome)
        ftp_meta.quit()
    except Exception as e:
        return f"não consegui o tamanho na origem: {type(e).__name__}: {e}", 0

    for tentativa in range(1, TENTATIVAS + 1):
        buffer = bytearray()
        fh = open(parcial, "ab" if offset else "wb")
        try:
            ftp = ftplib.FTP(HOST, timeout=90)
            ftp.login()
            ftp.cwd(DIR)
            ftp.voidcmd("TYPE I")
            if offset == 0:
                print(f"    {tamanho_origem / 1e9:.2f} GB na origem", flush=True)

            primeira = offset == 0

            def consome(bloco):
                nonlocal offset, linhas_pe, primeira
                offset += len(bloco)
                buffer.extend(bloco)
                # processa só linhas completas; o resto fica no buffer para o
                # próximo bloco — é isso que permite cortar em qualquer byte
                if b"\n" not in bloco:
                    return
                *linhas, resto = buffer.split(b"\n")
                del buffer[:]
                buffer.extend(resto)
                for linha in linhas:
                    if not linha:
                        continue
                    if primeira:  # a primeira linha do arquivo é o cabeçalho
                        fh.write(linha + b"\n")
                        primeira = False
                        continue
                    partes = linha.split(b";", CAMPO_UF + 2)
                    if len(partes) > CAMPO_UF and partes[CAMPO_UF] == UF_PE:
                        fh.write(linha + b"\n")
                        linhas_pe += 1

            ftp.retrbinary(f"RETR {nome}", consome, blocksize=1 << 16, rest=offset)
            ftp.quit()
            # o que sobrou no buffer é a última linha, sem quebra final
            if buffer:
                partes = bytes(buffer).split(b";", CAMPO_UF + 2)
                if len(partes) > CAMPO_UF and partes[CAMPO_UF] == UF_PE:
                    fh.write(bytes(buffer) + b"\n")
                    linhas_pe += 1
            fh.close()

            # a conferência que impede o truncamento silencioso
            if offset < tamanho_origem:
                falta = tamanho_origem - offset
                estado_f.write_text(json.dumps({"offset": offset, "pe": linhas_pe}))
                raise IOError(
                    f"transferência encerrou cedo: {offset:,} de {tamanho_origem:,} bytes "
                    f"({100 * offset / tamanho_origem:.1f}%), faltam {falta / 1e6:.0f} MB"
                )

            parcial.rename(saida)
            estado_f.unlink(missing_ok=True)
            dt = time.monotonic() - t0
            return (f"{linhas_pe:,} linhas de PE em {dt / 60:.1f} min "
                    f"({offset:,} bytes, íntegro)"), saida.stat().st_size

        except Exception as e:
            fh.close()
            estado_f.write_text(json.dumps({"offset": offset, "pe": linhas_pe}))
            if tentativa == TENTATIVAS:
                return f"falhou após {TENTATIVAS} tentativas: {type(e).__name__}: {e}", 0
            print(f"    [{tentativa}/{TENTATIVAS}] {type(e).__name__} em "
                  f"{offset / 1e9:.2f} GB, {linhas_pe:,} de PE — retomando", flush=True)
            time.sleep(ESPERA)


def status():
    DESTINO.mkdir(parents=True, exist_ok=True)
    print(f"{'arquivo':44s} {'tamanho':>10s}  linhas")
    total = 0
    for f in sorted(DESTINO.glob("*_PE.csv")):
        tam = f.stat().st_size
        total += tam
        with open(f, "rb") as fh:
            n = sum(1 for _ in fh) - 1
        print(f"{f.name:44s} {tam / 1e6:9.1f}M  {n:,}")
    print(f"{'TOTAL':44s} {total / 1e6:9.1f}M")


if __name__ == "__main__":
    if "--status" in sys.argv:
        status()
        sys.exit(0)

    DESTINO.mkdir(parents=True, exist_ok=True)
    alvo = [int(a) for a in sys.argv[1:] if a.isdigit()] or list(ANOS)

    for ano in alvo:
        print(f"[{ano}] baixando…", flush=True)
        msg, tam = baixa_ano(ano)
        print(f"[{ano}] {msg}", flush=True)
