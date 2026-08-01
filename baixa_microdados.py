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

import os
import sys
import time
import urllib.request
from pathlib import Path

BASE = "ftp://ftp.datasus.gov.br/dissemin/publicos/SISCAN/SISCAN"
DESTINO = Path(__file__).parent / "data" / "microdados"
ANOS = range(2018, 2027)
UF_PE = b'"26"'
CAMPO_UF = 2  # CO_UF_RESIDENCIA é o 3º campo (índice 2)


def baixa_ano(ano, base_nome="SISCAN_CITO_COLO"):
    """Baixa um ano e grava só as linhas de PE. Idempotente e retomável."""
    saida = DESTINO / f"{base_nome}_{ano}_PE.csv"
    parcial = saida.with_suffix(".parcial")

    if saida.exists():
        return "já existe", saida.stat().st_size

    url = f"{BASE}/{base_nome}_{ano}.csv"
    linhas_pe = lidas = 0
    t0 = time.monotonic()

    try:
        with urllib.request.urlopen(url, timeout=120) as fonte, \
             open(parcial, "wb") as fh:
            cabecalho = fonte.readline()
            fh.write(cabecalho)
            for linha in fonte:
                lidas += 1
                # split posicional: o 3º campo é a UF de residência, e o valor
                # vem entre aspas. Evita instanciar um parser de CSV por linha.
                partes = linha.split(b";", CAMPO_UF + 2)
                if len(partes) > CAMPO_UF and partes[CAMPO_UF] == UF_PE:
                    fh.write(linha)
                    linhas_pe += 1
                if lidas % 2_000_000 == 0:
                    mb = fh.tell() / 1e6
                    print(f"    {lidas / 1e6:.0f}M linhas lidas, "
                          f"{linhas_pe:,} de PE ({mb:.0f} MB)", flush=True)
    except Exception as e:
        parcial.unlink(missing_ok=True)
        return f"falhou: {type(e).__name__}: {e}", 0

    parcial.rename(saida)
    dt = time.monotonic() - t0
    return f"{linhas_pe:,} linhas de PE em {dt / 60:.1f} min", saida.stat().st_size


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
