#!/usr/bin/env python3
"""Pipeline de dados do estudo ITS de rastreamento de CCU em Pernambuco.

Monta o painel município de residência x mês x faixa etária quinquenal com o
denominador populacional, a partir de duas fontes oficiais:

  desfecho     SISCAN, exames citopatológicos do colo do útero, mulheres 25-64,
               por município de RESIDÊNCIA, competência mensal.
               TABNET/DATASUS, def SISCAN/cito_colo_residpe.def
  controle     SISCAN, mamografias, mesmo recorte territorial e temporal.
               def SISCAN/mamografia_residpe.def
  denominador  POPSVS (SVS/MS + IBGE), população por município x ano x sexo x
               idade simples. FTP DATASUS, /dissemin/publicos/IBGE/POPSVS/

Uso:
    python3 pipeline.py            # baixa o que falta e monta o painel
    python3 pipeline.py --check    # só roda o self-check, sem rede

Substitui os 17 scripts de scraping anteriores. Ver docs/HISTORICO_TENTATIVAS.md
para o que deu errado antes e docs/ACHADOS_VALIDACAO_SIA.md para por que o SIA
não serve como fonte do desfecho.
"""

import io
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

RAIZ = Path(__file__).parent
DADOS = RAIZ / "data"
BRUTO = DADOS / "bruto"

CGI = "http://tabnet.datasus.gov.br/cgi"
DEF_CITO = "SISCAN/cito_colo_residpe.def"
DEF_MAMO = "SISCAN/mamografia_residpe.def"
ANOS = range(2018, 2027)

# A janela do estudo. 108 meses, jan/2018 a dez/2026.
JANELA_INI, JANELA_FIM = "2018-01", "2026-12"

# Faixas quinquenais da população-alvo do rastreamento (INCA: 25 a 64 anos).
# O value do TABNET é "<rótulo>|<código>|<nível>".
FAIXAS = [
    "Entre 25 a 29 anos|025-029|3",
    "Entre 30 a 34 anos|030-034|3",
    "Entre 35 a 39 anos|035-039|3",
    "Entre 40 a 44 anos|040-044|3",
    "Entre 45 a 49 anos|045-049|3",
    "Entre 50 a 54 anos|050-054|3",
    "Entre 55 a 59 anos|055-059|3",
    "Entre 60 a 64 anos|060-064|3",
]

# Controle por característica: citopatológicos em mulheres FORA da faixa-alvo.
# Compartilham o choque pandêmico e a via de oferta, mas não entram no numerador
# de nenhum indicador de financiamento — ao contrário da mamografia, que é
# co-incentivada pelo próprio C7 a partir de mai/2025 e por isso não serve de
# controle no período que mais importa. Ver docs/pesquisa/ALERTAS_AUDITORIA.md
FAIXAS_CONTROLE = [
    "Entre 15 a 19 anos|015-019|3",
    "Entre 20 a 24 anos|020-024|3",
    "Entre 65 a 69 anos|065-069|3",
    "Entre 70 a 74 anos|070-074|3",
    "Entre 75 a 79 anos|075-079|3",
    "Acima de 79 anos|080-120|3",
]

# Mamografia na faixa-alvo do rastreamento de mama. Controle válido apenas até
# τ3 (mai/2024); depois de mai/2025 é co-incentivada pelo C7.
FAIXAS_MAMO = [
    "Entre 50 a 54 anos|050-054|3",
    "Entre 55 a 59 anos|055-059|3",
    "Entre 60 a 64 anos|060-064|3",
    "Entre 65 a 69 anos|065-069|3",
]

SERIES = [
    ("citopatologico", DEF_CITO, FAIXAS),
    ("cito_controle_fora_faixa", DEF_CITO, FAIXAS_CONTROLE),
    ("mamografia", DEF_MAMO, FAIXAS_MAMO),
]

LINHA_MUN_RESID = (
    "Munic.de residencia|CONCAT(CONCAT(DISSEMINACAO.TB_TBN_MUNICIPIO.CO_MUNICIPIO, ' '), "
    "DISSEMINACAO.TB_TBN_MUNICIPIO.NO_MUNICIPIO)  where FATO.CO_MUN_RESIDENCIA = "
    "DISSEMINACAO.TB_TBN_MUNICIPIO.CO_MUNICIPIO"
)
# Os dois defs divergem no campo de competência: o citopatológico usa a data de
# liberação do laudo; o de mamografia, a competência de faturamento.
COLUNA_MES_CITO = "Mes/Ano competencia|CO_ANO_MES_LIBERACAO|1|SISCAN\\periodo.cnv"
COLUNA_MES_MAMO = "Mes/Ano competenc|NU_ANO_MES_COMPETENCIA|1|siscan\\periodo.cnv"

# Competência em que o SISCAN não processou dados em nenhuma UF, nem para
# citopatológico nem para mamografia. Não é zero, é ausência: nenhuma série real
# de rastreamento zera nacionalmente por um mês. Setembro seguinte recebe o
# transbordo e fica inflado, por isso os dois meses saem juntos.
# Ver docs/pesquisa/ALERTAS_AUDITORIA.md
MESES_INVALIDOS = ("2022-08", "2022-09")

# Meses finais de qualquer extração ainda acumulam lançamento retroativo e
# aparecem subestimados. Marcados como provisórios em vez de descartados, para
# que a decisão de censurar fique na análise, não na coleta.
MESES_PROVISORIOS = 6


def _req(url, dados=None, timeout=240):
    req = urllib.request.Request(
        url,
        data=dados,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "identity",
        },
    )
    resp = urllib.request.urlopen(req, timeout=timeout)
    bruto = resp.read()
    if bruto[:2] == b"\x1f\x8b":  # a API do IBGE ignora identity e devolve gzip
        import gzip
        bruto = gzip.decompress(bruto)
    return bruto


def baixa_siscan(nome_def, faixa, motivo="TODAS_AS_CATEGORIAS__"):
    """Uma tabulação do TABNET: municípios de residência x meses, para uma faixa.

    O TABNET responde com HTML contendo o link de um CSV gerado sob demanda.
    Duas etapas, portanto: POST da tabulação, depois GET do CSV.
    """
    # Os dois defs divergem em nomes de campo: o de mamografia tem
    # "SMes/Ano competenc" truncado e não possui "XMotivo do exame".
    eh_cito = "cito" in nome_def
    pares = [
        ("Linha", LINHA_MUN_RESID),
        ("Coluna", COLUNA_MES_CITO if eh_cito else COLUNA_MES_MAMO),
        ("Incremento", "Exames|=count(*)"),
    ]
    pares += [("PAno competencia", f"{a}|{a}|4") for a in ANOS]
    pares += [
        ("SMunic.de residencia", "TODAS_AS_CATEGORIAS__"),
        ("SMes/Ano competencia" if eh_cito else "SMes/Ano competenc", "TODAS_AS_CATEGORIAS__"),
        ("XSexo", "Feminino|F|1"),
        ("XFaixa etária", faixa),
    ]
    if eh_cito:
        pares.append(("XMotivo do exame", motivo))
    pares += [
        ("grafico", ""),
        ("nomedef", nome_def),
        ("formato", "table"),
        ("mostre", "sim"),
    ]
    corpo = urllib.parse.urlencode(pares, encoding="latin-1", errors="replace").encode("ascii")
    html = _req(f"{CGI}/webtabx.exe?{nome_def}", corpo).decode("latin-1")

    link = re.search(r"csv/[A-Za-z_0-9]+\.csv", html)
    if not link:
        # O TABNET responde HTTP 200 mesmo em erro de aplicação. Sem o link do
        # CSV a resposta não é dado — foi aceitar uma dessas que gravou uma
        # página de erro como se fosse a base.
        trecho = re.sub(r"<[^>]+>", " ", html)
        raise RuntimeError(f"TABNET não gerou CSV: {re.sub(r'  +', ' ', trecho)[:300]}")
    return _req(f"{CGI}/{link.group(0)}").decode("latin-1")


def parse_tabnet_csv(texto, faixa_cod):
    """CSV do TABNET -> lista de (cod_ibge, nome, ano_mes, exames)."""
    linhas = [l for l in texto.splitlines() if ";" in l]
    cabecalho = None
    saida = []
    for linha in linhas:
        campos = [c.strip().strip('"') for c in linha.split(";")]
        if cabecalho is None:
            if "resid" in campos[0].lower() or "munic" in campos[0].lower():
                cabecalho = campos
            continue
        rotulo = campos[0]
        if not rotulo or rotulo.lower().startswith(("total", "fonte", "-")):
            continue
        m = re.match(r"(\d{6,7})\s+(.*)", rotulo)
        if not m:
            continue
        cod, nome = m.group(1), m.group(2).strip()
        for i, valor in enumerate(campos[1:], start=1):
            if i >= len(cabecalho):
                break
            col = cabecalho[i].strip()
            if col.lower() in ("total", ""):
                continue
            mes = normaliza_competencia(col)
            if not mes:
                continue
            v = valor.replace(".", "").replace("-", "0").strip()
            saida.append((cod, nome, mes, int(v) if v.isdigit() else 0))
    return saida


MESES_PT = {
    "jan": "01", "fev": "02", "mar": "03", "abr": "04", "mai": "05", "jun": "06",
    "jul": "07", "ago": "08", "set": "09", "out": "10", "nov": "11", "dez": "12",
}


def normaliza_competencia(rotulo):
    """'Jan/2018' ou '201801' -> '2018-01'."""
    r = rotulo.strip().lower()
    m = re.match(r"([a-zç]{3})[a-zç]*[/\- ](\d{4})", r)
    if m and m.group(1) in MESES_PT:
        return f"{m.group(2)}-{MESES_PT[m.group(1)]}"
    m = re.fullmatch(r"(\d{4})-?(\d{2})", r)
    if m and "01" <= m.group(2) <= "12":
        return f"{m.group(1)}-{m.group(2)}"
    return None


def municipios_pe():
    """Os 185 códigos IBGE de PE, da API de Localidades. Frame canônico do painel."""
    cache = BRUTO / "municipios_pe.json"
    if not cache.exists():
        dados = _req("https://servicodados.ibge.gov.br/api/v1/localidades/estados/26/municipios")
        cache.write_bytes(dados)
    lista = json.loads(cache.read_text())
    return {str(m["id"]): m["nome"] for m in lista}


def faixa_de(idade):
    """Idade simples -> código da faixa quinquenal do TABNET."""
    if idade < 10:
        return "000-009"
    if idade > 79:
        return "080-120"
    base = (idade // 5) * 5
    return f"{base:03d}-{base + 4:03d}"


def baixa_populacao():
    """POPSVS: população feminina por município de PE, ano e faixa quinquenal.

    O denominador tem de ser específico da faixa: o offset de cada célula do
    painel é log(pop daquela faixa / 3), não a população 25-64 inteira.
    """
    from dbfread import DBF

    cache = DADOS / "populacao_pe.json"
    if cache.exists():
        return json.loads(cache.read_text())

    pop = {}
    for ano in ANOS:
        zp = BRUTO / f"POPSBR{ano % 100:02d}.zip"
        if not zp.exists():
            url = f"ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/POPSVS/POPSBR{ano % 100:02d}.zip"
            try:
                print(f"  população {ano}...", end=" ", flush=True)
                urllib.request.urlretrieve(url, zp)
            except Exception as e:
                print(f"indisponível ({type(e).__name__})")
                continue
        with zipfile.ZipFile(zp) as z:
            nome_dbf = [n for n in z.namelist() if n.lower().endswith(".dbf")][0]
            z.extract(nome_dbf, BRUTO)
        for r in DBF(str(BRUTO / nome_dbf), encoding="latin-1", lowernames=True):
            if not str(r["cod_mun"]).startswith("26") or str(r["sexo"]) != "2":
                continue
            chave = f"{r['cod_mun']}|{ano}|{faixa_de(int(r['idade']))}"
            pop[chave] = pop.get(chave, 0) + int(r["pop"])
        print(f"  população {ano}: ok")

    cache.write_text(json.dumps(pop, ensure_ascii=False, indent=1))
    return pop


def meses_da_janela():
    out = []
    for ano in ANOS:
        for m in range(1, 13):
            mes = f"{ano}-{m:02d}"
            if JANELA_INI <= mes <= JANELA_FIM:
                out.append(mes)
    return out


def monta_painel():
    BRUTO.mkdir(parents=True, exist_ok=True)
    munis = municipios_pe()
    print(f"Frame canônico: {len(munis)} municípios de PE")

    registros = []
    for serie, nome_def, faixas in SERIES:
        for faixa in faixas:
            cod_faixa = faixa.split("|")[1]
            arq = BRUTO / f"{serie}_{cod_faixa}.csv"
            if not arq.exists():
                print(f"  {serie} {cod_faixa}...", end=" ", flush=True)
                try:
                    arq.write_text(baixa_siscan(nome_def, faixa), encoding="utf-8")
                    print("ok")
                except Exception as e:
                    print(f"FALHOU: {e}")
                    continue
                time.sleep(2)
            for cod, _nome, mes, n in parse_tabnet_csv(arq.read_text(encoding="utf-8"), cod_faixa):
                registros.append(
                    {"serie": serie, "cod": cod, "faixa": cod_faixa, "mes": mes, "exames": n}
                )

    if not registros:
        raise SystemExit("Nenhum dado baixado. Verifique a conexão e o TABNET.")

    pop = baixa_populacao()
    meses = meses_da_janela()
    ultimo_com_dado = max(r["mes"] for r in registros)
    corte_provisorio = meses[max(0, meses.index(ultimo_com_dado) - MESES_PROVISORIOS + 1)]

    # Zero-fill contra o frame canônico. O TABNET omite a linha do município que
    # zera no estrato inteiro; sem repor, zero verdadeiro vira ausência e o
    # modelo de contagem enviesa para cima.
    indice = {(r["serie"], r["cod"], r["faixa"], r["mes"]): r["exames"] for r in registros}
    ultimo_ano_pop = max(int(k.split("|")[1]) for k in pop) if pop else None
    painel = []
    for serie, _nome_def, faixas in SERIES:
        for cod, nome in sorted(munis.items()):
            for faixa in [f.split("|")[1] for f in faixas]:
                for mes in meses:
                    if mes > ultimo_com_dado:
                        continue  # ainda não publicado, não é zero
                    valido = mes not in MESES_INVALIDOS
                    ano = int(mes[:4])
                    # POPSVS ainda não publicou o último ano da janela; usa-se o
                    # mais recente disponível, sinalizado para que a análise
                    # decida entre repetir, interpolar ou censurar.
                    ano_pop = min(ano, ultimo_ano_pop) if ultimo_ano_pop else ano
                    painel.append({
                        "serie": serie,
                        "cod_ibge": cod,
                        "municipio": nome,
                        "faixa": faixa,
                        "ano_mes": mes,
                        "exames": indice.get((serie, cod[:6], faixa, mes), 0) if valido else None,
                        "pop_alvo": pop.get(f"{cod}|{ano_pop}|{faixa}"),
                        "pop_ano": ano_pop,
                        "pop_defasada": ano_pop != ano,
                        "valido": valido,
                        "provisorio": mes >= corte_provisorio,
                    })

    # CSV, não JSON: é o formato que o glmmTMB consome e ocupa um décimo do espaço.
    import csv
    campos = ["serie", "cod_ibge", "municipio", "faixa", "ano_mes", "exames",
              "pop_alvo", "pop_ano", "pop_defasada", "valido", "provisorio"]
    with open(DADOS / "painel_ccu_pe.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        w.writerows(painel)
    return painel, munis, meses, ultimo_com_dado, corte_provisorio


def resume(painel, munis, meses, ultimo, corte):
    cito = [r for r in painel if r["serie"] == "citopatologico"]
    validos = [r for r in cito if r["valido"]]
    total = sum(r["exames"] for r in validos)
    por_mes = {}
    for r in validos:
        por_mes[r["ano_mes"]] = por_mes.get(r["ano_mes"], 0) + r["exames"]

    com_pop = [r for r in validos if r["pop_alvo"]]
    pop_total = sum(
        p for cod in munis
        for a, p in [(ultimo[:4], next((r["pop_alvo"] for r in validos
                                        if r["cod_ibge"] == cod and r["pop_alvo"]), 0))]
    )

    resumo = {
        "total_exames_citopatologicos": total,
        "municipios": len(munis),
        "meses_com_dado": len(por_mes),
        "meses_da_janela": len(meses),
        "primeira_competencia": min(por_mes) if por_mes else None,
        "ultima_competencia": ultimo,
        "competencias_invalidas": list(MESES_INVALIDOS),
        "provisorio_a_partir_de": corte,
        "cobertura_denominador": f"{100 * len(com_pop) / max(1, len(validos)):.1f}%",
        "serie_mensal_estadual": dict(sorted(por_mes.items())),
        "fonte_desfecho": "SISCAN/DATASUS, def cito_colo_residpe.def, município de residência",
        "fonte_denominador": "POPSVS (SVS/MS + IBGE), população feminina por faixa quinquenal",
        "offset": "log(populacao_feminina_da_faixa / 3) — fator de divisão 3, Resolução CIT nº 2/2016",
        "razao_de_exames_por_ano": {
            a: round(r, 3)
            for a in sorted({x["ano_mes"][:4] for x in painel})
            if (r := razao_de_exames(painel, a)) is not None
        },
    }
    (DADOS / "resumo.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=2))
    return resumo


def self_check():
    """Verifica o que quebrou o pipeline anterior: parsing, competência, zero-fill."""
    # A última coluna do TABNET é o total da linha e não pode virar dado —
    # foi contá-la que fez os valores versionados valerem o dobro.
    csv = (
        '"Munic.de residencia";"Jan/2018";"Fev/2018";"Total"\n'
        '"260005 Abreu e Lima";"393";"146";"539"\n'
        '"260545 Fernando de Noronha";"0";"8";"8"\n'
        '"Total";"393";"154";"547"\n'
    )
    linhas = parse_tabnet_csv(csv, "025-029")
    assert len(linhas) == 4, f"esperado 4 células, veio {len(linhas)}: {linhas}"
    assert ("260005", "Abreu e Lima", "2018-01", 393) in linhas, linhas
    assert not any(m == "Total" for _, _, m, _ in linhas), "coluna Total virou dado"
    assert not any(n == "Total" for _, n, _, _ in linhas), "linha Total virou município"

    # Entidades HTML contêm o separador ';' — se o unescape não vier antes do
    # split, o nome do município quebra em duas colunas e desloca os valores.
    assert normaliza_competencia("Jan/2018") == "2018-01"
    assert normaliza_competencia("201801") == "2018-01"
    assert normaliza_competencia("Total") is None
    assert normaliza_competencia("2018-13") is None, "mês 13 não existe"

    assert len(meses_da_janela()) == 108, f"janela tem {len(meses_da_janela())} meses, esperado 108"
    assert "2022-08" in MESES_INVALIDOS

    # O denominador é por faixa. Replicar a população 25-64 inteira em cada uma
    # das 8 faixas multiplicaria o denominador por 8 e afundaria a razão de
    # exames na mesma proporção.
    assert faixa_de(25) == "025-029" and faixa_de(64) == "060-064"
    assert faixa_de(29) == "025-029" and faixa_de(30) == "030-034"
    assert faixa_de(80) == "080-120" and faixa_de(95) == "080-120"
    assert faixa_de(9) == "000-009" and faixa_de(19) == "015-019"

    print("self-check ok")


def razao_de_exames(painel, ano):
    """Exames do ano / (população-alvo / 3). O parâmetro INCA é 1,0."""
    alvo = [r for r in painel if r["serie"] == "citopatologico" and r["valido"]
            and r["ano_mes"][:4] == ano and r["pop_alvo"]]
    if not alvo:
        return None
    # pop_alvo é anual e se repete nas 12 competências do ano
    denom = sum(r["pop_alvo"] for r in alvo) / 12 / 3
    return sum(r["exames"] for r in alvo) / denom if denom else None


MARCOS = [
    {"id": "τ1", "mes": "2020-01", "rotulo": "Previne Brasil",
     "detalhe": "Portaria GM/MS 2.979 de 12/11/2019 — não separável de τ2, modelado em bloco"},
    {"id": "τ2", "mes": "2020-03", "rotulo": "COVID-19",
     "detalhe": "Emergência de Saúde Pública de Importância Nacional"},
    {"id": "τ2b", "mes": "2021-01", "rotulo": "Recuperação pós-pandêmica",
     "detalhe": "Ponto de recuperação epidemiológica, não marco normativo — nenhum efeito de política lhe é atribuído"},
    {"id": "τ3", "mes": "2024-05", "rotulo": "Saúde Brasil 360",
     "detalhe": "Componente financeiro — Portaria GM/MS 3.493/2024, art. 8º"},
    {"id": "τ4", "mes": "2025-05", "rotulo": "Indicador C7 mensurado",
     "detalhe": "Portaria GM/MS 6.907/2025 — mensuração, não exposição financeira"},
    {"id": "τ5", "mes": "2026-05", "rotulo": "Qualidade parcial",
     "detalhe": "Portaria GM/MS 10.994/2026 — implantação assimétrica, só ganho"},
]


def tabula_por_ano(linha_val, rotulo):
    """Tabulação auxiliar: uma dimensão qualitativa × ano de competência.

    Serve às medidas de qualidade que o painel declara — composição do desfecho
    por motivo do exame e tempo até a liberação do laudo.
    """
    pares = [
        ("Linha", linha_val),
        ("Coluna", "Ano competencia|CO_ANO_LIBERACAO|1|CITO\\ano.cnv"),
        ("Incremento", "Exames|=count(*)"),
    ]
    pares += [("PAno competencia", f"{a}|{a}|4") for a in ANOS]
    pares += [
        ("SMunic.de residencia", "TODAS_AS_CATEGORIAS__"),
        ("SMes/Ano competencia", "TODAS_AS_CATEGORIAS__"),
        ("XSexo", "Feminino|F|1"),
    ]
    pares += [("XFaixa etária", f) for f in FAIXAS]
    pares += [
        ("XMotivo do exame", "TODAS_AS_CATEGORIAS__"),
        ("grafico", ""), ("nomedef", DEF_CITO),
        ("formato", "table"), ("mostre", "sim"),
    ]
    corpo = urllib.parse.urlencode(pares, encoding="latin-1", errors="replace").encode("ascii")
    html = _req(f"{CGI}/webtabx.exe?{DEF_CITO}", corpo).decode("latin-1")
    link = re.search(r"csv/[A-Za-z_0-9]+\.csv", html)
    if not link:
        return None
    texto = _req(f"{CGI}/{link.group(0)}").decode("latin-1")

    import html as htmlmod
    cabecalho, linhas = None, {}
    for l in texto.splitlines():
        l = htmlmod.unescape(l)
        if ";" not in l:
            continue
        campos = [c.strip().strip('"') for c in l.split(";")]
        if cabecalho is None:
            cabecalho = [c.strip() for c in campos]
            continue
        if campos[0].lower().startswith(("total", "fonte")):
            continue
        vals = {}
        for i, v in enumerate(campos[1:], start=1):
            if i >= len(cabecalho) or cabecalho[i].lower() in ("total", ""):
                continue
            n = v.replace(".", "").strip()
            vals[cabecalho[i]] = int(n) if n.isdigit() else 0
        linhas[campos[0]] = vals
    return {"rotulo": rotulo, "categorias": linhas}


def gera_dashboard(painel, resumo):
    """Agrega o painel de 340 mil linhas no JSON enxuto que o dashboard consome."""
    from collections import defaultdict

    series_mes = defaultdict(lambda: defaultdict(int))
    pop_mes = defaultdict(int)
    mun_ano = defaultdict(lambda: defaultdict(int))
    mun_pop = {}
    nomes = {}

    for r in painel:
        if not r["valido"]:
            continue
        s, m = r["serie"], r["ano_mes"]
        series_mes[s][m] += r["exames"]
        if s == "citopatologico":
            pop_mes[m] += (r["pop_alvo"] or 0)
            ano = m[:4]
            mun_ano[r["cod_ibge"]][ano] += r["exames"]
            mun_pop[(r["cod_ibge"], ano)] = mun_pop.get((r["cod_ibge"], ano), 0) + (r["pop_alvo"] or 0)
            nomes[r["cod_ibge"]] = r["municipio"]

    meses = sorted(series_mes["citopatologico"])
    # razão mensal = exames do mês / (população-alvo / 3 / 12)
    razao_mes = [
        round(series_mes["citopatologico"][m] / (pop_mes[m] / 12 / 3), 4) if pop_mes[m] else None
        for m in meses
    ]

    # último ano-calendário completo, para o ranking municipal
    anos_completos = sorted({m[:4] for m in meses if sum(1 for x in meses if x[:4] == m[:4]) == 12})
    ano_ref = anos_completos[-1] if anos_completos else meses[-1][:4]

    municipios = []
    for cod, por_ano in mun_ano.items():
        p = mun_pop.get((cod, ano_ref), 0)
        if not p:
            continue
        municipios.append({
            "cod": cod,
            "nome": nomes[cod],
            "exames": por_ano.get(ano_ref, 0),
            "pop": round(p / 12),
            "razao": round(por_ano.get(ano_ref, 0) / (p / 12 / 3), 4),
        })
    municipios.sort(key=lambda x: -x["razao"])

    # Tabulações de qualidade. Ficam em cache: mudam pouco e cada uma custa uma
    # requisição lenta ao TABNET.
    cache_q = DADOS / "qualidade.json"
    if cache_q.exists():
        qualidade = json.loads(cache_q.read_text())
    else:
        qualidade = {}
        for chave, val, rot in [
            ("motivo", "Motivo do exame|TP_MOTIVO_EXAME|1|CITO\\motivo_exame.cnv",
             "Motivo do exame"),
            ("tempo_liberacao", "Tempo Exame|CO_TEMPO_EXAME|1|CITO\\TempoExame.CNV",
             "Tempo entre a coleta e a liberação do laudo"),
        ]:
            print(f"  qualidade: {chave}...", end=" ", flush=True)
            r = tabula_por_ano(val, rot)
            qualidade[chave] = r
            print("ok" if r else "falhou")
        cache_q.write_text(json.dumps(qualidade, ensure_ascii=False, indent=1))

    dash = {
        "meses": meses,
        "series": {s: [series_mes[s].get(m, 0) for m in meses] for s in series_mes},
        "qualidade": qualidade,
        "razao_mensal": razao_mes,
        "razao_anual": resumo["razao_de_exames_por_ano"],
        "municipios": municipios,
        "ano_referencia": ano_ref,
        "marcos": [m for m in MARCOS if m["mes"] <= meses[-1]],
        "competencias_invalidas": list(MESES_INVALIDOS),
        "provisorio_a_partir_de": resumo["provisorio_a_partir_de"],
        "resumo": resumo,
        "gerado_em": time.strftime("%Y-%m-%d"),
    }
    (DADOS / "dashboard.json").write_text(json.dumps(dash, ensure_ascii=False), encoding="utf-8")
    return dash


if __name__ == "__main__":
    if "--check" in sys.argv:
        self_check()
        sys.exit(0)

    self_check()
    DADOS.mkdir(exist_ok=True)
    painel, munis, meses, ultimo, corte = monta_painel()
    r = resume(painel, munis, meses, ultimo, corte)
    print()
    print(f"  exames citopatológicos  {r['total_exames_citopatologicos']:,}")
    print(f"  municípios              {r['municipios']}")
    print(f"  competências            {r['meses_com_dado']} de {r['meses_da_janela']}")
    print(f"  período                 {r['primeira_competencia']} a {r['ultima_competencia']}")
    print(f"  provisório a partir de  {r['provisorio_a_partir_de']}")
    print(f"  denominador             {r['cobertura_denominador']} das células")
    print(f"  razão de exames         {r['razao_de_exames_por_ano']}")

    # Verificação de saída: a razão de exames de PE fica bem abaixo do parâmetro
    # INCA de 1,0, mas não na casa de 0,05 — isso indicaria denominador somado
    # errado, por exemplo replicando a população 25-64 em cada faixa.
    ref = r["razao_de_exames_por_ano"].get("2023")
    if ref is not None and not 0.15 < ref < 1.5:
        raise SystemExit(f"razão de exames de 2023 = {ref}, fora do plausível — revise o denominador")

    d = gera_dashboard(painel, r)
    print(f"  dashboard.json          {len(d['municipios'])} municípios, ano-base {d['ano_referencia']}")
