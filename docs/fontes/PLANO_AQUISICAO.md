# Plano consolidado de aquisição de dados — ITS-painel de rastreamento do câncer do colo do útero em Pernambuco

**Data da sondagem:** 01/08/2026 · **Coleta definitiva prevista:** 2027 · **Janela:** jan/2018–dez/2026 (108 meses) · **Unidade:** 185 unidades territoriais de PE (184 municípios + Distrito Estadual de Fernando de Noronha)

Oito fontes foram sondadas e cada sondagem foi submetida a uma verificação adversarial independente. Este documento consolida o que sobreviveu à verificação. **Onde sondador e verificador divergiram, o veredito do verificador prevalece** — em todos os casos de divergência o verificador reproduziu os bytes de forma independente e o sondador não.

---

## 1. Veredito por fonte

| Fonte | Disponível | Veredito | Papel no estudo |
|---|---|---|---|
| **SISCAN — TABNET nacional** (`cito_colo_residpe.def`, via `dhdat.exe` + `webtabx.exe`) | Sim | **CONFIRMADO** — reproduzido byte a byte, CSV idêntico ao do sondador | **PRIMÁRIA** — desfecho primário |
| **SISCAN — microdados CSV** (FTP `/dissemin/publicos/SISCAN/SISCAN/`) | Sim | **PARCIAL** — fonte real, comando de coleta quebrado | **Complementar** — enriquecimento e sensibilidade, não via canônica |
| **SIA-PA microdados DBC** (FTP `/dissemin/publicos/SIASUS/200801_/Dados/`) | Sim | **CONFIRMADO** — reproduzido dígito a dígito, inclusive teste de miolo (PAPE2001) | **Complementar** — validação cruzada obrigatória, nunca desfecho primário |
| **POPSVS** (FTP `/dissemin/publicos/IBGE/POPSVS/`) | Sim | **CONFIRMADO** — todos os 8 anos reproduzidos à unidade | **PRIMÁRIA** — denominador/offset |
| **ANS** (ANSTabNet POST + PDA-024) | Sim | **CONFIRMADO** — arquivo byte-idêntico (sha256 `1ac77846…`, 185.635 B) | **Complementar** — covariável de cobertura privada |
| **SISAB (indicador 4) / SIAPS (C7)** | Sim | **CONFIRMADO** — script rodou verbatim, fichas conferidas verbatim | **PRIMÁRIA para a análise documental**, inadequada para inferência |
| **Desfechos complementares** (SIM, Painel-Oncologia, CNES, cobertura APS, Base Territorial, SIDRA) | Sim (RCBP e IDHM: não) | **CONFIRMADO** | **Complementar** — covariáveis estruturais (Base Territorial e cobertura APS são obrigatórias) |
| **HPV / quebra de definição** (SIGTAP + SIA + PCDT) | Sim | **PARCIAL** — série de citologia do sondador estava errada por downloads truncados | **Complementar** — datação de ameaça, vigilância para 2027 |

### Divergências resolvidas a favor do verificador

**SISCAN microdados CSV — `PARCIAL`, não `disponivel/primaria`.** O sondador afirmou "12 meses completos" para 2025 e apresentou uma série mensal de PE 2018 (`201801=3781 … 201812=2611`) como fato empírico. O verificador rodou o comando publicado, obteve `exit 0` e um CSV bem-formado **com ~1/6 dos dados** — truncamento silencioso, sem sinal de erro. Mediu ainda que dez/2025 tem 7 registros contra ~730 de média nos meses anteriores (0,09% do esperado): o arquivo é censurado à direita, o último mês utilizável é ~out/2025. E os campos `CO_MUN_UNIDADE_SAUDE` / `CO_MUN_PREST_SERVICO`, que o sondador ofereceu para análise de fluxo, estão **0% preenchidos** em 335.887 registros. Prevalece o verificador porque ele mediu bytes lidos contra `SIZE` remoto; o sondador não validou nada.

**HPV — `PARCIAL`, e a manchete cai.** O sondador concluiu que "a citologia em PE está subindo (13,5 mil → 21,5 mil/mês), logo não há substituição tecnológica". O verificador conferiu o tamanho de cada `.dbc` contra o servidor: quatro dos oito arquivos estavam truncados em 33–41%. Com os arquivos íntegros a série é **estável/oscilante**, não ascendente:

| Competência | Sondador | Correto | Recife (correto) |
|---|---|---|---|
| 202510 | 13.486 | **22.769** | 1.006 |
| 202511 | 12.954 | **24.343** | 3.856 |
| 202512 | 16.869 | **25.879** | 4.471 |
| 202601 | 13.705 | **17.020** | 3.270 |
| 202602–202605 | idênticos | 17.253 / 20.904 / 21.499 / 21.519 | 3.054 / 3.585 / 3.956 / 4.632 |

A conclusão qualitativa (a citologia não desabou; zero produção de HPV no SIA) sobrevive. A quantitativa não: o dado corrigido é compatível com estabilidade e **não demonstra ausência de substituição**.

**SIA-PA — `CONFIRMADO`, com duas correções materiais.** O verificador confirmou tudo, mas acrescentou o que o sondador omitiu: (a) **não há identificador de paciente** em nenhuma das 60/61 colunas — o SIA conta exames, nunca mulheres; (b) os "~12% de faturamento retroativo" não são mensuráveis com arquivos não adjacentes, e variam de fato entre 4,2% e 11,4% conforme a competência.

**ANS — limitação refutada a favor da robustez.** O sondador afirmou que o TabNet limita ~17-18 arquivos por POST. O verificador testou 17/18/19/20/25/30/33 e **todos funcionam**: as 33 competências saem em um único POST. O que derruba o request é pedir um `.dbf` inexistente.

**SIAPS — esperança refutada.** O sondador recomendou "fortemente investigar" `/praticas-assistenciais` como possível fonte de contagem mensal de citopatológico por município. O verificador testou: o filtro `sigtap` devolve zero para todo código, inclusive códigos presentes no próprio catálogo. **Caminho morto.** Em compensação encontrou o que o sondador perdeu — ver §3, passo 9.

---

## 2. A decisão central: qual é o desfecho primário?

**Resposta: SISCAN, coletado via TABNET nacional (`SISCAN/cito_colo_residpe.def`). O SIA-PA entra como validação cruzada obrigatória, nunca como desfecho.**

### 2.1 Por que SISCAN e não SIA

A razão decisiva não é de engenharia — o SIA-PA é tecnicamente excelente e entrega tudo que o desenho pede, inclusive melhor que o SISCAN em faixa etária (idade simples vs quinquenal). A razão é de validade.

O SIA mede **faturamento de produção ambulatorial**. O SISCAN é o **sistema de informação do câncer** — registro do laudo citopatológico. Não são o mesmo universo, e a diferença foi medida: o SIA capta 78% (jan/2018), 86% (jan/2025) e 84% (mai/2026) do volume SISCAN na mesma UF, faixa e competência. Essa diferença não é ruído: é função de contratualização, glosa e regra de pagamento.

Três dos quatro change points do estudo são intervenções **financeiras** — τ1 (Previne Brasil), τ3 (componente financeiro Saúde Brasil 360) e τ4 (indicadores de qualidade, incluindo C7). Usar uma série de faturamento para medir efeito de mudanças no financiamento cria confundimento diferencial perfeitamente alinhado às datas de interrupção: um degrau no SIA em mai/2024 seria indistinguível entre "mais mulheres rastreadas" e "municípios passaram a faturar melhor porque agora vale dinheiro". Nenhuma especificação de GLMM resolve isso.

Confirmações empíricas que sustentam o SISCAN como primário, todas verificadas de forma independente:

| Requisito | SISCAN/TABNET | Evidência |
|---|---|---|
| Município de **residência** | Sim | O `.def` carrega SQL explícito `where FATO.CO_MUN_RESIDENCIA = …`; o def de atendimento usa **outra coluna** (`FATO.co_mun_prest_servico`) — são dados distintos, não a mesma tabela renomeada. Nota Técnica 3: "conforme cadastrado no Cartão Nacional de Saúde da paciente" |
| Mensal | Sim | `CO_ANO_MES_LIBERACAO`, 101 colunas de mês numa única requisição de 11,4 s |
| Faixa 25-64 | Sim, quinquenal | As 8 requisições isoladas somam 43579+43464+47573+48881+47247+43671+36776+26236 = **337.427 = exatamente** o filtro agregado 25-64 de 2024 |
| 185 unidades | Sim | 185 linhas de município, todas com contagem > 0; Fernando de Noronha (260545) presente |
| Série mensal real | Sim | jan/2018=22.563 ≠ fev=21.252 ≠ mar=28.174; queda COVID visível (2020=190.683 vs 2019=310.510) |
| Cobertura temporal hoje | 101 de 108 meses | jan/2018 a jun/2026, menos ago/2022 |
| Reprodutibilidade | curl puro, sem cookie/sessão/token/CAPTCHA | Verificador rodou verbatim em diretório limpo: exit 0, 15,3 s, CSV conteúdo-idêntico ao do sondador |
| Volume | < 5 MB para todo o estudo | 8 CSVs = 719.954 B em 120,5 s |

O SISCAN entrega ainda, de graça: `Motivo do exame` (Rastreamento / Repetição / Seguimento — 98,6% dos 25-64 em PE em 2024 são rastreamento puro), a nomenclatura brasileira de laudos completa, e o def "por pacientes" com `count(distinct co_paciente)`.

### 2.2 As duas vias de SISCAN são consistentes entre si — e isso é a validação mais forte disponível

Nenhum dos oito agentes cruzou as duas vias de SISCAN. Cruzando aqui, com os números que ambos os verificadores produziram (microdados: extração parcial de 54% dos bytes do arquivo nacional de 2018; TABNET: extração completa):

| Mês/2018 | Microdados (parcial) | TABNET (completo) | Razão |
|---|---|---|---|
| jan | 17.713 | 22.563 | 78,5% |
| fev | 16.262 | 21.252 | 76,5% |
| mar | 21.635 | 28.174 | 76,8% |
| abr | 24.732 | 32.222 | 76,8% |
| mai | 24.786 | 32.128 | 77,1% |
| jun | 19.348 | 25.382 | 76,2% |
| jul | 22.532 | 29.409 | 76,6% |
| ago | 25.257 | 32.666 | 77,3% |
| set | 21.445 | 28.004 | 76,6% |
| out | 24.896 | 32.447 | 76,7% |
| nov | 24.518 | 31.966 | 76,7% |
| dez | 22.195 | 28.946 | 76,7% |

A razão é **76,2%–78,5%, praticamente constante**. Isso é exatamente o padrão de uma leitura parcial que perdeu uma fração aproximadamente uniforme dos registros — não de duas fontes que discordam. Ou seja: **microdados e TABNET medem o mesmo universo**, e a completude da extração parcial foi de ~77%. Esta conciliação deve ser refeita com download íntegro (passo 4 do plano) e reportada na dissertação como validação interna da fonte.

### 2.3 Por que TABNET e não os microdados CSV, se os microdados são individuais

| Critério | TABNET | Microdados CSV FTP |
|---|---|---|
| Última competência hoje | **jun/2026** | dez/2025, mas utilizável só até ~out/2025 (dez/2025 tem 7 registros na amostra de cauda) |
| Volume | 720 KB | 12,5 GB (cito) + 6,3 GB (mamografia) nacionais para extrair ~5% de PE |
| Tempo | ~2 min | dias (throughput despenca; um único ano não terminou em 3h30 no teste do verificador) |
| Risco de coleta | baixo | **alto — truncamento silencioso comprovado** |
| Idade | quinquenal | anos simples |
| Motivo do exame | Sim (dimensão) | Sim (`TP_MOTIVO_EXAME`, 100% preenchido) |
| Laudo / adequabilidade | Sim (Incremento) | Sim (`CO_LAUDO_CITOPATOLOGICO`, sem dicionário oficial) |
| Dedup de mulheres | Só anual (`cito_colo_pacpe.def`) | Só nos arquivos `_PACNT_`, e a dedup é **anual** |
| Fluxo/evasão | não | **não** (campos de estabelecimento 0% preenchidos) |

O ganho real dos microdados sobre o TABNET é a idade simples. O custo é 20 GB, dias de download, um modo de falha invisível e três meses a menos de cobertura. Não compensa como via canônica. Compensa como fonte de sensibilidade para dois anos-âncora.

### 2.4 Como cruzar SISCAN × SIA e o que esperar

Construa **duas séries paralelas** município × mês × faixa 25-64, jan/2018–dez/2026:

- `y_siscan` = TABNET, `Incremento = Exames`, `Coluna = Mes/Ano competencia`
- `y_sia` = SIA-PA, `PA_PROC_ID = '0203010086'`, agregado por **`PA_CMP`** (competência do atendimento, nunca `PA_MVM`), `PA_MUNPCN` prefixo 26, `PA_IDADE` 25-64, somando **`PA_QTDAPR`** (declarar a escolha; `PA_QTDPRO` como sensibilidade)

Produtos obrigatórios do cruzamento:

1. **Razão SISCAN/SIA por município-ano.** É o único denominador de completude disponível — o TABNET nacional do SISCAN está vazio, então não há tabulação oficial contra a qual auditar os microdados. Sem essa razão não é possível separar aumento de exames de aumento de captura do SISCAN, e a implantação do SISCAN é contemporânea a τ1.
2. **Modelo replicado nas duas séries, coeficiente a coeficiente por change point.** Concordância reforça a inferência. **Divergência concentrada em τ3/τ4 é, em si, o achado**: significa que o efeito observado é de registro/faturamento e não de cobertura. Isso é resultado publicável, não fracasso.

Expectativa quantitativa, com base no já medido: razão SIA/SISCAN entre 78% e 86%, crescente ao longo da janela. Se essa razão **saltar em mai/2024 ou mai/2025**, o salto é a assinatura do artefato de faturamento.

---

## 3. Plano de aquisição — ordem de execução

Todos os comandos abaixo foram executados e verificados em 01/08/2026. Onde a versão original do sondador falhou, está a versão corrigida pelo verificador.

### Passo 0 — Convenções e higiene, antes de qualquer download

Três regras não negociáveis, derivadas de falhas reais nesta sondagem:

1. **Nunca use `curl` contra o FTP do DATASUS para listar.** `curl --list-only` truncou 234 arquivos SIGTAP em 15, e 130 arquivos SISCAN em 18, **sem erro**. Use `ftplib` + `NLST`.
2. **Nunca aceite um download sem validar tamanho contra `SIZE` remoto.** Quatro agentes produziram dados errados por causa disso; um publicou uma série temporal falsa.
3. **Congele e hasheie tudo.** As bases são retroativamente mutáveis e sem versionamento. Registre data de extração e sha256 de cada CSV. Exemplo já registrado: `pe_benef_f2564_trimestral.csv`, sha256 `1ac77846…`, 185.635 B, 2026-08-01.

```bash
source /Users/markuscorgosinho/projects/Juliana/mestrado-ccu-pe/venv/bin/activate
mkdir -p dados/{siscan,sia,pop,cov,doc}
```

### Passo 1 — Frame canônico das 185 unidades territoriais

Sem isso, o zero-fill do passo 2 é impossível e joins geram linhas órfãs.

```bash
curl -s "https://servicodados.ibge.gov.br/api/v1/localidades/estados/26/municipios" -o dados/municipios_PE.json
# n = 185, inclui id 2605459 Fernando de Noronha
curl -s "https://servicodados.ibge.gov.br/api/v3/malhas/estados/26?intrarregiao=municipio&formato=application/vnd.geo+json&qualidade=intermediaria" -o dados/malha_PE_mun.geojson
# HTTP 200, 223.489 B, 185 features, properties.codarea = codigo IBGE 7 digitos
# ATENCAO: qualidade aceita apenas minima|intermediaria|maxima. Valores 1-4 retornam HTTP 400.
```

O IBGE e o DATASUS tratam Fernando de Noronha como unidade territorial equivalente a município (diferença simétrica entre os dois conjuntos: **vazia**). O N do painel é **185 × 108 = 19.980** observações município-mês. Redação correta na dissertação: "185 unidades territoriais (184 municípios e o Distrito Estadual de Fernando de Noronha)".

### Passo 2 — Desfecho primário: SISCAN TABNET, 8 requisições

Sempre parseie o formulário da etapa 1 antes de montar o POST — os nomes de campo são acentuados e **truncados de forma diferente entre defs** (o cito usa `SMes/Ano competencia`, a mamografia usa `SMes/Ano competenc`).

```bash
CGI=http://tabnet.datasus.gov.br/cgi
DEF=SISCAN/cito_colo_residpe.def
# etapa 1 - metadados (59.653 B; declara "Data de atualizacao dos dados: 20/07/2026")
curl -s "$CGI/dhdat.exe?$DEF" | iconv -f latin1 -t utf-8 > dados/siscan/form_residpe.html
```

```python
# dados/siscan/post_siscan.py  — 8 requisicoes, ~120 s, 720 KB
import urllib.request, urllib.parse, re, pandas as pd, json

BASE  = "http://tabnet.datasus.gov.br/cgi/webtabx.exe?SISCAN/cito_colo_residpe.def"
LINHA = ("Munic.de residencia|CONCAT(CONCAT(DISSEMINACAO.TB_TBN_MUNICIPIO.CO_MUNICIPIO, ' '), "
         "DISSEMINACAO.TB_TBN_MUNICIPIO.NO_MUNICIPIO)  where FATO.CO_MUN_RESIDENCIA = "
         "DISSEMINACAO.TB_TBN_MUNICIPIO.CO_MUNICIPIO")
COL    = "Mes/Ano competencia|CO_ANO_MES_LIBERACAO|1|SISCAN\\periodo.cnv"
FAIXAS = [f"Entre {a} a {a+4} anos|{a:03d}-{a+4:03d}|3" for a in range(25, 65, 5)]

def baixa(faixa, anos=range(2018, 2027), motivo="TODAS_AS_CATEGORIAS__"):
    p  = [("Linha", LINHA), ("Coluna", COL), ("Incremento", "Exames|=count(*)")]
    p += [("PAno competencia", f"{a}|{a}|4") for a in anos]
    p += [("SMunic.de residencia", "TODAS_AS_CATEGORIAS__"),
          ("SMes/Ano competencia", "TODAS_AS_CATEGORIAS__"),
          ("XSexo", "Feminino|F|1"), ("XFaixa etária", faixa),
          ("XMotivo do exame", motivo),
          ("SAno Resultado", "TODAS_AS_CATEGORIAS__"), ("SMes Resultado", "TODAS_AS_CATEGORIAS__"),
          ("grafico", ""), ("nomedef", "SISCAN/cito_colo_residpe.def"),
          ("formato", "table"), ("mostre", "sim")]
    body = urllib.parse.urlencode(p, encoding="latin-1", errors="replace").encode("ascii")
    req  = urllib.request.Request(BASE, data=body, headers={
        "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=180).read().decode("latin-1")
    m = re.search(r"csv/[A-Za-z_0-9]+\.csv", html)
    if not m:                                   # falha e ruidosa: ORA-xxxxx ou pagina de erro
        raise RuntimeError("TABNET nao devolveu link .csv — inspecionar resposta")
    return urllib.request.urlopen("http://tabnet.datasus.gov.br/cgi/" + m.group(0), timeout=240).read()

frames = []
for f in FAIXAS:
    fx = f.split("|")[1]
    fn = f"dados/siscan/cito_colo_residpe_{fx}_2018-2026.csv"
    open(fn, "wb").write(baixa(f))
    df = pd.read_csv(fn, sep=";", encoding="latin-1", dtype=str)
    df = df[~df.iloc[:, 0].str.contains("Total", na=False)]
    df = df.drop(columns=[c for c in df.columns if c.strip() == "Total"])
    lg = df.melt(id_vars=df.columns[0], var_name="mes_ano", value_name="exames")
    lg.columns = ["municipio", "mes_ano", "exames"]; lg["faixa"] = fx
    frames.append(lg)

p = pd.concat(frames)
p["exames"]   = pd.to_numeric(p.exames, errors="coerce")
p["cod_ibge"] = p.municipio.str.slice(0, 6)

# ---- ZERO-FILL OBRIGATORIO contra o frame canonico de 185 -------------------
canon = [str(m["id"])[:6] for m in json.load(open("dados/municipios_PE.json"))]
meses = sorted(p.mes_ano.unique())
idx   = pd.MultiIndex.from_product([canon, meses, sorted(p.faixa.unique())],
                                   names=["cod_ibge", "mes_ano", "faixa"])
p = (p.set_index(["cod_ibge", "mes_ano", "faixa"])["exames"]
       .reindex(idx, fill_value=0).reset_index())
assert p.cod_ibge.nunique() == 185, p.cod_ibge.nunique()
p.to_csv("dados/siscan/painel_siscan_cito_pe_25a64_2018_2026.csv", index=False)
print(p.shape, p.cod_ibge.nunique(), p.mes_ano.nunique(), int(p.exames.sum()))
# esperado hoje: (149480, 4) 185 101 2610409
```

**Por que o zero-fill é obrigatório e não cosmético.** O painel de janela completa é balanceado por acidente: cada faixa devolve os 185 municípios com zeros explícitos. Mas em recortes mais estreitos o TABNET **dropa municípios silenciosamente** — só em 2024, a faixa 060-064 devolveu 183 municípios e quatro outras faixas devolveram 184. Qualquer estratificação adicional (faixa × motivo, faixa × resultado) perde municípios sem aviso, e o `melt` não repõe nada. Zeros verdadeiros virando ausências enviesam o modelo de contagem para cima.

**Ago/2022 não existe** — o TABNET omite a coluna. Verificado em três consultas independentes: PE filtrado, PE sem nenhum filtro, e o def nacional (`cito_colo_residbr.def`, 5.568 municípios). O zero-fill acima criaria 185 zeros falsos nesse mês se ele estivesse no eixo; como o TABNET omite a coluna, ele simplesmente não entra em `meses`. **Trate como missing, não como zero**, e não o reintroduza.

Teste de existência de def (não use HTTP 404 — def inexistente devolve **HTTP 200** com traceback Python de ~270 B):

```bash
curl -s "http://tabnet.datasus.gov.br/cgi/dhdat.exe?SISCAN/<def>.def" | grep -q '<SELECT' \
  && echo EXISTE || echo NAO_EXISTE
```

### Passo 3 — Série-controle: **não use mamografia**

A série-controle prevista no protocolo está invalidada. A ficha oficial do C7 (Portaria vigente, SEI 0054641718, assinada 19-22/06/2026) define a **boa prática (D) = (g/h) × 20** — rastreamento de câncer de mama em mulheres de 50-69 anos, últimos 24 meses, aceitando os SIGTAP **02.04.03.003-0** (Mamografia) e **02.04.03.018-8** (Mamografia bilateral para rastreamento). O verificador conferiu isso verbatim no PDF. A mamografia recebe o mesmo incentivo financeiro que o citopatológico em τ3/τ4 — viola a premissa de controle não tratado.

Agravante independente: o buraco de ago/2022 **também atinge a mamografia** no SISCAN (PE 2022 pula de JULHO/2022 para SETEMBRO/2022). Desfecho e controle perdem o mesmo `t`, o que impede diagnosticar o buraco por contraste entre séries.

**Substituto recomendado: citologia fora da faixa de rastreamento (20-24 e 65+), no mesmo def SISCAN.** É controle interno: mesma fonte, mesmo município, mesma infraestrutura de coleta, mesmo lag coleta→liberação — mas fica fora do numerador do C7 (boa prática A é 25-64) e fora do numerador do indicador 4 do Previne (25-64). Isola τ1, τ3 e τ4.

```python
# mesma funcao baixa(), trocando as faixas
FAIXAS_CTRL = ["Entre 20 a 24 anos|020-024|3",
               "Entre 65 a 69 anos|065-069|3", "Entre 70 a 74 anos|070-074|3",
               "Entre 75 a 79 anos|075-079|3", "80 anos e mais|080-999|3"]
# conferir os values exatos no <SELECT NAME="XFaixa etária"> do form baixado no passo 2
```

**Para τ2 (mar/2020, COVID) não existe série-controle válida** em nenhuma das fontes sondadas: qualquer rastreamento ofertado pela mesma rede sofre o mesmo choque. Declare isso, não invente controle.

Como o SIA mostra que o código 0203010019 é usado majoritariamente **fora** da faixa (jan/2018: 4.107 registros <25 anos, 1.583 >64, contra apenas 757 em 25-64), essa série também mede **sobrerrastreio** — ambas as pontas contraindicadas pela diretriz do INCA. Vale como desfecho secundário de qualidade, dialogando diretamente com o C7.

### Passo 4 — Sensibilidade: microdados SISCAN para dois anos-âncora

Faça isto **apenas** para 2019 (pré-τ2) e 2024 (pós-τ3), não para os nove anos. Objetivo: (a) conciliar contra o TABNET conforme §2.2; (b) obter idade simples e `TP_MOTIVO_EXAME` em nível individual; (c) medir a distribuição do lag coleta→liberação.

```python
# extrator resumivel — o comando com `curl | awk` do sondador NAO deve ser usado
# uso: python3 stream_pe_resumable.py SISCAN_CITO_COLO_2019.csv '"26"'
import sys, time
from ftplib import FTP
HOST, DIR = 'ftp.datasus.gov.br', '/dissemin/publicos/SISCAN/SISCAN/'
FNAME = sys.argv[1]; UF = (sys.argv[2] if len(sys.argv) > 2 else '"26"').encode()
out = open(FNAME.replace('.csv', '_PE.csv'), 'wb')
off = pe = 0; buf = b''; first = True; tent = 0
f = FTP(HOST, timeout=300); f.login(); size = f.size(DIR + FNAME)
while off < size:
    try:
        if f is None: f = FTP(HOST, timeout=300); f.login()
        conn = f.transfercmd('RETR ' + DIR + FNAME, off)      # REST no offset exato
        while True:
            ch = conn.recv(1 << 20)
            if not ch: break
            off += len(ch); parts = (buf + ch).split(b'\n'); buf = parts.pop()
            for ln in parts:
                if first: out.write(ln + b'\n'); first = False; continue
                fl = ln.split(b';', 4)
                if len(fl) > 3 and fl[2] == UF: pe += 1; out.write(ln + b'\n')
        conn.close(); f.voidresp(); tent = 0
    except Exception as e:
        tent += 1; print('QUEDA em', off, repr(e), flush=True)
        try: f.close()
        except Exception: pass
        f = None
        if tent > 40: break
        time.sleep(min(10 * tent, 60))
out.close()
assert off == size, f'INCOMPLETO {off}/{size} - descartar saida'   # a linha que faltava
print('COMPLETO', off, size, 'linhas PE =', pe)
```

Campos confirmados (84 colunas, ordem verificada): campo 3 `CO_UF_RESIDENCIA`, 6 `CO_MUN_RESIDENCIA`, 11 `CO_ANO_MES_LIBERACAO`, 14 `CO_IDADE_PACIENTE` (anos simples, zero-padded), 31 `TP_MOTIVO_EXAME`, 81 `CO_LAUDO_CITOPATOLOGICO`, 84 `SG_SEXO`. Na mamografia o campo de competência é `NU_ANO_MES_COMPETENCIA`.

Validação obrigatória por ano: (a) bytes lidos == `SIZE`; (b) 12 competências presentes; (c) 185 municípios distintos; (d) nenhum mês >50% abaixo da mediana (censura à direita → descartar o mês).

### Passo 5 — Denominador e offset: POPSVS

Baixe **também 2017** — sem o ponto de 1º/jul/2017 não há âncora à esquerda para interpolar jan–jun/2018, que são os 6 primeiros meses do painel.

```bash
for y in 17 18 19 20 21 22 23 24 25; do
  curl -sS -O "ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/POPSVS/POPSBR$y.zip"
  unzip -o -q POPSBR$y.zip -d dados/pop/popsvs$y
done
```

```python
from dbfread import DBF
import pandas as pd, glob, numpy as np

out = []
for f in sorted(glob.glob('dados/pop/popsvs*/[Pp][Oo][Pp]*.dbf')):
    # lowernames=True e OBRIGATORIO: a caixa dos campos muda de maiuscula (2018-2024)
    # para minuscula (2025), e a largura de idade vai de C(3) para C(5)
    d = pd.DataFrame(iter(DBF(f, encoding='latin-1', lowernames=True)))
    d['cod_mun'] = d.cod_mun.astype(str).str.strip()
    d['idade']   = pd.to_numeric(d.idade, errors='coerce')
    d['pop']     = pd.to_numeric(d.pop, errors='coerce')
    out.append(d[d.cod_mun.str.startswith('26')])
pe = pd.concat(out)
den = (pe[(pe.sexo.astype(str).str.strip() == '2') & (pe.idade.between(25, 64))]
       .groupby(['cod_mun', 'ano']).pop.sum().reset_index(name='pop_fem_25_64'))
den['cod_ibge6'] = den.cod_mun.str[:6]          # join com DATASUS/SISCAN
den.to_csv('dados/pop/pop_PE_fem_25_64_2017_2025.csv', index=False)
```

Valores de referência já validados à unidade: PE fem 25-64 = 2.554.215 (2018) … 2.710.671 (2025); total PE 2024 = 9.539.029 e 2025 = 9.562.007, **coincidindo à unidade** com o SIDRA 6579.

**Extrapolação de 2026** (`POPSBR26` não existe em 01/08/2026; esperado entre out/2026 e jan/2027):

```python
p  = den.pivot(index='cod_mun', columns='ano', values='pop_fem_25_64').loc[:, 2021:2025]
X  = np.arange(2021, 2026); Y = np.log(p.values)
b  = ((X - X.mean()) * (Y - Y.mean(1, keepdims=True))).sum(1) / ((X - X.mean())**2).sum()
a  = Y.mean(1) - b * X.mean()
p2026 = np.exp(a + b * 2026).round().astype(int)   # total PE = 2.733.601 (+0,846%)
```

**Correção do offset.** A coluna `pop/3` entregue na sondagem é a contagem esperada **anual** sob periodicidade trienal. O desfecho é **mensal**. O offset correto é:

```
offset_it = log( pop_fem_25_64[i, ano(t)] / 3 / 12 )
```

Como é fator constante, os coeficientes de nível e tendência não mudam — mas qualquer cobertura reportada a partir de `pop/3` sai **12× errada**. Renomeie a coluna para `denom_anual_trienal` e derive `offset_mensal` explicitamente.

**Interpolação para 108 meses:** interpole linearmente entre pontos de 1º/jul de anos consecutivos, **não** use degrau anual. O degrau cairia em janeiro — mesmo mês de τ1 (jan/2020) — e seria lido como efeito de intervenção. Declare a escolha no método.

Sensibilidade obrigatória com denominador censitário: a razão POPSVS/Censo 2022 por município tem média 1,0215 e DP 0,0138, mas **três municípios têm razão < 1** (Pombos 0,9501, Tupanatinga 0,9686, Itaíba 0,9848) — o que é incompatível com "ajuste de cobertura uniforme" e indica diferença de alocação municipal. Recife tem razão 1,0552 e carrega ~18% do denominador.

```bash
curl -s "https://apisidra.ibge.gov.br/values/t/9514/n6/in%20n3%2026/v/93/p/2022/c2/5/c287/93088,93089,93090,93091,93092,93093,93094,93095/c286/113635" \
  -o dados/pop/censo2022_9514_PE_fem2564.json   # 1.480 registros = 185 x 8 faixas
```

**Não use** SIDRA 6579 como série (faltam 2022 e 2023, e 2018-2021 são valores pré-censo — a série teria salto artificial de −1,4% entre 2021 e 2024, sobre τ1/τ2), nem SIDRA 7358 (não desce a município e é a revisão 2018, pré-censo), nem POPTBR/POPTCU (sem sexo e sem idade).

### Passo 6 — Validação cruzada: SIA-PA

```python
# download resumavel e idempotente — o retrbinary sem retry do sondador
# estourou TimeoutError em 600 s deixando arquivo PARCIAL sem aviso
from ftplib import FTP
import os, time
DIR = '/dissemin/publicos/SIASUS/200801_/Dados/'
def conecta():
    f = FTP('ftp.datasus.gov.br', timeout=120); f.login(); f.cwd(DIR); return f

def baixa(fn, tentativas=12):
    f = conecta(); alvo = f.size(fn); f.quit()
    for t in range(tentativas):
        have = os.path.getsize(fn) if os.path.exists(fn) else 0
        if have == alvo: return alvo
        if have > alvo: os.remove(fn); have = 0
        try:
            f = conecta()
            with open(fn, 'ab') as h:
                f.retrbinary('RETR ' + fn, h.write, 65536, rest=have)   # rest= retoma
            f.quit()
        except Exception as e:
            print(' retry %d em %s: %s' % (t + 1, fn, type(e).__name__)); time.sleep(5)
    raise IOError('%s incompleto' % fn)

for ano in range(18, 27):
    for mes in range(1, 13):
        fn = 'dados/sia/PAPE%02d%02d.dbc' % (ano, mes)
        try: print('OK', fn, baixa(fn))
        except Exception as e: print('PULADO', fn, e)   # >=202606 ainda nao publicado
```

```python
import pyreaddbc, os, glob, csv
from dbfread import DBF
from collections import Counter
import json
canon = {str(m["id"])[:6] for m in json.load(open("dados/municipios_PE.json"))}
painel = Counter()
for dbc in sorted(glob.glob('dados/sia/PAPE*.dbc')):
    dbf = dbc[:-4] + '.dbf'
    pyreaddbc.dbc2dbf(dbc, dbf)                       # DBF e 13-17x maior; apagar depois
    for r in DBF(dbf, encoding='latin-1', load=False):
        if (r['PA_PROC_ID'] or '').strip() != '0203010086': continue
        mun = str(r['PA_MUNPCN']).strip()
        if mun not in canon: continue                 # valida contra IBGE, nao startswith('26')
        if r['PA_SEXO'] != 'F': continue
        idade = int(r['PA_IDADE'])                    # PA_IDADE em ANOS (PA_FLIDADE='1')
        if not 25 <= idade <= 64: continue
        painel[(mun, str(r['PA_CMP']).strip())] += int(r['PA_QTDAPR'] or 0)
    os.remove(dbf)                                    # pico de disco ~0,8 GB
```

Regras que valem como método, não como detalhe:

- **`PA_CMP`, nunca `PA_MVM`.** `PAPE1801` contém competências 201801 (23.534 reg), 201712 (2.687), 201711 (519) e 201710 (89). Uma série montada por arquivo produz artefato de queda no fim.
- **`PA_MUNPCN` é residência; `PA_UFMUN` é estabelecimento.** Divergem em 42% (2018) e 49% (2026) dos registros, e a divergência bate exatamente com as flags oficiais `PA_UFDIF`/`PA_MNDIF` — `{('0','0'):15542, ('0','1'):10821, ('1','1'):466}` em 2018. Este foi o erro nº 2 do pipeline atual do repositório.
- **Os campos de idade do procedimento chamam-se `IDADEMIN` e `IDADEMAX`, sem prefixo `PA_`.** `PA_IDADEMIN` não existe e causa `KeyError`.
- **`0203010086` é autovalidado**: o SIGTAP impõe 300-779 meses e o SIA rejeita fora disso. 100% dos 20.382 registros de jan/2018 e dos 23.031 de mai/2026 caem em 25-64, zero exceções.
- **Fuga interestadual medida**: 37 exames de residentes de PE faturados na PB e 34 em AL em mai/2026 = 0,32% do total. Não vale baixar 27 UFs (~120 GB). Reporte o número; se quiser corrigir, PE+PB+AL+BA+PI cobre quase tudo por ~15 GB.
- **Contagem vs quantidade**: `PA_QTDAPR` (aprovada) ≠ nº de linhas ≠ `PA_QTDPRO` (apresentada). Em jan/2018, 26.829 apresentados vs 26.630 aprovados (0,7% de glosa). Padronize e declare — a diferença é exatamente a glosa, que pode variar no tempo e entre municípios.

### Passo 7 — Estratificação territorial (obrigatória para os efeitos aleatórios aninhados)

```bash
curl -sS -o dados/cov/base_territorial_jun26.zip \
  "ftp://ftp.datasus.gov.br/territorio/tabelas/2026/06-base_territorial_jun26.zip"
unzip -o -q dados/cov/base_territorial_jun26.zip -d dados/cov/bt2606
```

```python
import pandas as pd
B = 'dados/cov/bt2606/'
mr  = pd.read_csv(B+'rl_municip_regsaud.csv', sep=';', dtype=str)
rs  = pd.read_csv(B+'tb_regsaud.csv', sep=',', dtype=str)[['CO_REGSAUD','DS_NOME']].rename(columns={'DS_NOME':'NO_REGSAUD'})
rm  = pd.read_csv(B+'rl_regsaud_macsaud.csv', sep=';', dtype=str)
mac = pd.read_csv(B+'tb_macsaud.csv', sep=';', dtype=str)[['CO_MACSAUD','DS_NOME']].rename(columns={'CO_MACSAUD':'CO_MACRORREGIONAL','DS_NOME':'NO_MACSAUD'})
mun = pd.read_csv(B+'tb_municip.csv', sep=';', dtype=str)[['CO_MUNICIP','CO_MUNICDV','DS_NOME','UF','IN_SEMIAR','NU_AREA']]
pe = (mr[mr.CO_MUNICIP.str.startswith('26')].merge(mun, on='CO_MUNICIP')
        .merge(rs, on='CO_REGSAUD').merge(rm, on='CO_REGSAUD').merge(mac, on='CO_MACRORREGIONAL'))
pe.sort_values('CO_MUNICIP').to_csv('dados/cov/PE_municipio_regsaude_macro.csv', index=False)
print(len(pe), pe.CO_REGSAUD.nunique(), pe.CO_MACRORREGIONAL.nunique())   # 185 12 4
```

Resultado verificado célula a célula: **185 municípios / 12 Regiões de Saúde / 4 Macrorregiões**. Fernando de Noronha e Recife ambos em I Região de Saúde / METROPOLITANA.

**Checagem barata que ninguém fez:** o diretório `/territorio/tabelas/<ano>/` tem versões mensais desde 2023. Baixe `2023/02-base_territorial_*.zip` e compare `rl_municip_regsaud` com jun/2026 para saber se a composição mudou por deliberação CIB/CIR dentro da janela. Como os efeitos aleatórios são aninhados em região de saúde, uma mudança não detectada torna a estratificação anacrônica.

### Passo 8 — Covariáveis tempo-variantes

**8a. Cobertura de APS (mensal, 185 municípios).**

```bash
# AB (jan/2018 a dez/2020) e APS (jan/2021 a mai/2026) — API publica, sem auth
curl -sS "https://relatorioaps-prd.saude.gov.br/cobertura/aps?unidadeGeografica=MUNICIPIO&coUf=26&nuCompInicio=202405&nuCompFim=202405"
curl -sS "https://relatorioaps-prd.saude.gov.br/cobertura/ab?unidadeGeografica=MUNICIPIO&coUf=26&nuCompInicio=201801&nuCompFim=201801"
```

Três armadilhas verificadas: (i) a métrica **muda em jan/2021** — "Cobertura AB" (nº de eSF + carga horária, teto de 100%) vs "Cobertura APS" (capacidade de cadastro, **sem teto**: Abreu e Lima 05/2024 = 120,36%); (ii) `qtCobertura` da APS usa **denominador congelado por ano** (`nuAnoReferencia="2023"` em `nuComp=05/2024`), criando degrau artificial em toda virada de janeiro — que colide com τ1 (janeiro/2020); (iii) no bloco AB a **vírgula é separador de milhar e de decimal no mesmo registro**: `qtPopulacao:"99,364"` (=99364 pessoas), `qtCoberturaSf:"96,600"` (=96,6%), `pcCoberturaSf:"97.22"`. Um `replace(',','')` global transforma 96,6% em 96600. Na API APS os mesmos campos já vêm numéricos.

Contagem de 185 linhas não prova completude — municípios com zero equipes também retornam linha. Cheque `qtEsf==0 & qtPopulacao>0`.

**8b. Cobertura de saúde suplementar (ANS, trimestral).** Um único POST, 34 competências (Dez/17 a Mar/26):

```python
ARQS = [a for a in competencias_disponiveis() if a[6:10] >= "1712"]   # inclui Dez/17
hdr, body = parse(post(ARQS))                                          # UM post, nao dois lotes
```

`SUF=17` (Pernambuco), `SSexo=2` (Feminino), `SFaixa_etária` 7..14 (25-29 … 60-64). Use **apenas "Assistência Médica"** (`NR_BENEF_M` / `COBERTURA_ASSIST_PLAN='Médico-hospitalar'`) — plano exclusivamente odontológico não desloca rastreamento de colo.

`cobertura_mun_ano = benef_F25-64_assistência_médica(Dez do ano) / pop_F25-64_POPSVS(ano)`.

**Nunca como denominador.** A ANS conta **vínculos, não pessoas** (nota oficial: um beneficiário com dois planos aparece duas vezes), e há viés de endereço de plano coletivo (63,3% dos vínculos F 25-64 de PE são Coletivo Empresarial; Recife concentra 45,4% do estado com ~16% da população). `pop − beneficiárias` é denominador viesado e potencialmente negativo em municípios pequenos.

**Cuidado com pós-tratamento em τ2**: a cobertura caiu de 430.467 (Mar/18) para 423.025 (Set/20) e recuperou para 459.725 (Dez/25). Se caiu **por causa** da COVID (desemprego → perda de plano coletivo), é mediadora de τ2, não confundidora. Use tempo-variante para τ1/τ3/τ4; para τ2 fixe no valor pré-pandêmico (média 2018-2019 por município) e reporte as duas especificações.

**8c. Oferta laboratorial (CNES, mensal).** `SERV_ESP=120` (Serviço de Diagnóstico por Anatomia Patológica e/ou Citopatologia), com `CLASS_SR`: `001` anatomopatológico, `002` **exames citopatológicos**, `003` **MEQ do colo do útero**.

```python
# SRPE1801.dbc .. SRPE2606.dbc em /dissemin/publicos/CNES/200508_/Dados/SR
# Filtrar AMB_SUS=='1' — sem esse filtro, 26% dos CNES contados sao rede nao-SUS
d = d[(d.SERV_ESP.astype(str).str.strip()=='120') & (d.AMB_SUS.astype(str).str.strip()=='1')]
```

Série 120/002 com filtro SUS em jun/2026: **188 CNES / 81 municípios** (sem filtro: 253/89). `CODUFMUN` é o município do **estabelecimento**, não de residência — agregue por Região de Saúde (o campo `REGSAUDE` já vem no próprio SR). Contagem de estabelecimentos ignora volume: triangule com a produção do SIA.

**8d. Intensidade financeira do incentivo (mensal, em reais) — a covariável mais forte encontrada.**

```bash
curl -s "https://relatorioaps-prd.saude.gov.br/financiamento/pagamento?unidadeGeografica=MUNICIPIO&coUf=26&nuParcelaInicio=202601&nuParcelaFim=202605&tipoRelatorio=COMPLETO" -o dados/cov/pag.json
```

A chave `resumosPlanosOrcamentarios` vem agregada por UF (`coMunicipioIbge: null`) — foi só isso que o sondador viu. A resposta tem uma segunda chave, **`pagamentos`**, com 925 registros = 185 municípios × 5 parcelas **mensais**, cada um com `coMunicipioIbge`, `nuParcela`, `dsFaixaIndiceEquidadeEsfEap`, `dsClassificacaoQualidadeEsfEap`, `qtEsf100pcPgto/75pc/50pc/25pc`, `vlFixoEsf`, `vlVinculoEsf`, `vlQualidadeEsf`, `vlTotalEsf`.

Isto é município × mês, em reais, com classificação de qualidade. **É a única série mensal municipal desta família de fontes** e permite trocar a dummy binária de τ3/τ4 por uma exposição contínua dose-resposta. **Verificar antes de assumir:** só foi testado o intervalo 202601–202605; a retroação de `nuParcela` não foi medida.

### Passo 9 — Análise documental: indicador 4 do Previne × C7

Esta é a única parte do bloco SISAB/SIAPS que é **primária**. Extraia e arquive **agora**: o painel SISAB rotula os três últimos quadrimestres como "(DESCONTINUADO)" e **os quadrimestres de 2020-2021 já sumiram** do painel, apesar de o Previne Brasil ter começado em 2020.

```bash
# C7 (SIAPS) — API publica com OpenAPI, sem auth
curl -s -H 'Content-Type: application/json' -X POST \
  'https://apisiaps.saude.gov.br/api/public/componente/indicador-quadrimestre/filtro' \
  -d '{"uf":["PE"],"nuQuadrimestre":["2025Q1","2025Q2","2025Q3","2026Q1"]}' -o dados/doc/pe_c7.json
# filtrar coTipoIndicador == 109  -> 878 linhas, 185 municipios

# Indicador 4 (SISAB) — formulario JSF, sem login apesar do "acessoRestrito" no path
python3 baixa_sisab_ind4.py PE dados/doc/sisab_ind4_PE.csv   # 1.850 linhas = 185 x 10 quadrimestres

# Fichas oficiais
curl -sL -o dados/doc/ficha_C7.pdf 'https://www.gov.br/saude/pt-br/composicao/saps/publicacoes/fichas-tecnicas/equipe-de-atencao-primaria-e-saude-da-familia/nota-metodologica-c7-cuidado-da-mulher-na-prevencao-do-cancer/@@download/file'
curl -sL -o dados/doc/qualificadores_previne.pdf 'https://sisab.saude.gov.br/resource/file/qualificadores_indicades_Thrift.pdf'
curl -sL -o dados/doc/NT_30_2025.pdf 'https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/notas-tecnicas/2025/nota-tecnica-no-30-2025-cgesco-desco-saps-ms.pdf'
```

Dois ajustes obrigatórios no script do SISAB:

```python
# 1) `header` e sobrescrito a cada quadrimestre: o CSV rotula a coluna de percentual
#    com o rotulo do ULTIMO quadrimestre em TODAS as 1850 linhas
header_fix = [h if not h.endswith("(%)") else "percentual_indicador" for h in header]

# 2) fixar a visao de equipe — "" != regra de pagamento
VISAO_EQUIPE = "|HM|NC|"    # apenas eSF/eAP validas para o componente de desempenho
                            # rodar tambem com "" e comparar (sensibilidade obrigatoria)
```

**Matriz de incomparabilidade com cinco eixos, toda documentada em fonte primária:**

| Eixo | Previne, indicador 4 | C7, boa prática (A) |
|---|---|---|
| Numerador | **um único** código: SIGTAP 02.01.02.003-3 / ABPG010 (a **coleta**) | **sete** códigos, incluindo os exames 02.03.01.008-6 e 02.03.01.001-9, dois de HPV molecular, mais ABEX001/ABP022 |
| Evento contado | coletado | coletado **ou solicitado ou avaliado** |
| Denominador | mulheres **cadastradas** no município | pessoas **vinculadas à equipe** sob NT 30/2025 (exige cadastro MICI completo, **exclui** cadastro rápido) |
| População | sexo = 1 (feminino) | mulheres **e homens transgênero**; exclui mulheres transgênero das boas práticas |
| Estrutura | indicador simples | composto de 4 boas práticas — **rastreamento de colo vale 20 de 100 pontos** |
| Janela | 36 meses | 36 meses, **exceto** 60 meses para 02.02.10.025-1, regra que entrou em jan/2026 |
| Publicação | numerador + denominador + % por município | apenas contagem de equipes em 4 categorias ordinais |

Conclusão documental defensável: **não formam série histórica contínua e não são comparáveis nem após harmonização.** Sobreposição temporal: só 2025Q1 (Previne: 2022Q1–2025Q1, 10 pontos; C7: 2025Q1–2026Q1, 4 pontos). Impossível calibrar fator de conversão.

**Abra o pedido de LAI agora** para os quadrimestres 2020-2021 do indicador 4, que já não estão públicos. O prazo é longo e a coleta é em 2027.

### Passo 10 — Desfechos secundários (opcionais, mas baratos)

**Mortalidade (SIM).** `DOPE<AAAA>.dbc` em `/dissemin/publicos/SIM/CID10/DORES/` (2018-2024) e `/SIM/PRELIM/DORES/` (2025-2026, até maio). 3.841 óbitos C53+C55 residentes em PE na janela. **Não use como desfecho do GLMM mensal**: apenas 2.071 de 19.240 células município×mês têm ≥1 óbito (10,8% não-zero). E a latência rastreamento→mortalidade é de 5-15 anos: a mortalidade **não é interpretável para nenhum dos quatro change points** dentro de uma janela que acaba em 2026. Use agregada por região de saúde/ano, como contextualização. Redistribua o C55 por município/ano/faixa, nunca com fator global — a proporção de C55 caiu de 23,9% (2018) para 15,5% (2024), o que significa que parte do "aumento" de C53 é melhoria de codificação.

**Painel-Oncologia.** `POBR<AAAA>.dbc` em `/dissemin/publicos/painel_oncologia/Dados/`, 2013-2026, com `MUN_RESID`, `ANOMES_DIA`, `IDADE`, `ESTADIAM`, `TEMPO_TRAT`. **O CID está em `DIAG_DETH`, não em `DIAGNOSTIC`** (que só assume 01/02/03/04 — filtrar por ela retorna zero casos). Ressalva séria não levantada pelo sondador: mais rastreamento gera mais diagnósticos detectados, e a base só captura quem foi tratado no SUS — um "efeito de τ3 sobre estadiamento precoce" é parcialmente a própria exposição se re-manifestando (*detection bias*). Some-se `ESTADIAM=9` em 33,3% dos C53 de PE em 2024. `TEMPO_TRAT` usa 99999 para "sem tratamento" e tem valores negativos (mín −50): sem limpeza, qualquer média é lixo (a média bruta é 29.599 dias).

**Razão exames/mulher (teste empírico do pressuposto do offset).** O def `SISCAN/cito_colo_pacpe.def` usa `Incremento = Pacientes distintos|=count(distinct co_paciente)`, mas só oferece dimensão **anual**. Isso permite calcular exames/mulher por município-ano — proxy direto de repetição indevida (rastreamento oportunístico anual em vez de trienal). Como o offset assume periodicidade trienal, essa razão **testa** o pressuposto em vez de assumi-lo. O indicador 4 do Previne remunera cobertura, criando incentivo exatamente para inflar exames sem ampliar mulheres cobertas.

---

## 4. Códigos SIGTAP definitivos

Vigência varrida em 56 competências reais entre 201801 e 202607 (`tb_procedimento.txt` posicional: `CO_PROCEDIMENTO` pos 1-10, `NO_PROCEDIMENTO` 11-260, `TP_SEXO` 262, `VL_IDADE_MINIMA` 275-278, `VL_IDADE_MAXIMA` 279-282, idades em **meses**).

| Código | Descrição oficial | Vigência 2018-2026 | Idade SIGTAP | Papel |
|---|---|---|---|---|
| **0203010086** | EXAME CITOPATOLÓGICO CERVICO VAGINAL/MICROFLORA-RASTREAMENTO | 56/56 competências, **estável** | 0300-0779 meses = **25-64 anos exatos** | **Desfecho no SIA** (validação cruzada). Autovalidado: 100% dos registros caem em 25-64 |
| **0203010019** | EXAME CITOPATOLÓGICO CERVICO-VAGINAL/MICROFLORA | 56/56, **estável** | 0120-1571 meses (10-130 anos) | **Sensibilidade** (+ ~4% no desfecho) e **série-controle interna**: é o complemento etário, usado majoritariamente fora de 25-64 |
| **0204030188** | MAMOGRAFIA BILATERAL PARA RASTREAMENTO | 56/56, estável | — | **NÃO usar como controle** — está na boa prática (D) do C7 |
| **0204030030** | MAMOGRAFIA | 56/56, estável | — | **NÃO usar como controle** — idem |
| **0201020033** | COLETA DE MATERIAL DO COLO DE ÚTERO P/ EXAME CITOPATOLÓGICO | 56/56, estável | — | **NÃO usar.** É o erro nº 1 do pipeline atual. 514 registros em jan/2018 em PE contra 26.829 do exame (1:52) — a coleta é registrada no e-SUS APS, não faturada no SIA |
| **0203010078** | CONTROLE DE QUALIDADE DO EXAME CITOPATOLÓGICO | 56/56 | — | **Excluir** — não é exame |
| **0203010027** | EXAME CITOPATOLÓGICO HORMONAL SERIADO | 56/56 | — | **Excluir** — não é rastreio de CCU |
| **0201020076** | COLETA DE MATERIAL DO COLO DO ÚTERO PARA EXAME MOLECULAR DE DETECÇÃO DE HPV | ⚠ **CRIADO em 202405** | — | Registro **10 (e-SUS APS)**, financiamento 01 — **não aparece no SIA**. Monitorar via SISAB |
| **0201020084** | ENTREGA DE MATERIAL OBTIDO POR AUTO COLETA PARA EXAME MOLECULAR DE HPV | ⚠ **CRIADO em 202405** | — | Idem |
| **0202100251** | EXAME MOLECULAR DE DETECÇÂO DE HPV *(grafia original)* | ⚠ **CRIADO em 202511** | 0300-0779 meses = 25-64 | **Produção ZERO** em PE, PR e DF em todas as competências até mai/2026. Registro 02 (BPA-I), `VL_SA = R$ 0,00`, grupo 02/subgrupo 02/forma 10 (Exames de genética) |
| ~~0203010045~~ | — | **NÃO EXISTE** em nenhuma das 56 competências | — | Código citado no projeto que não existe |
| ~~0203010070~~ | — | **NÃO EXISTE** em nenhuma das 56 competências | — | Idem |
| ~~0202030300~~ | PESQUISA DE ANTICORPOS ANTI-HIV-1 + HIV-2 (ELISA) | presente em 201801, **ausente** em 202607 | — | **Não tem relação com HPV.** Candidato errado no enunciado |
| ~~0214010104~~ | TESTE RÁPIDO PARA DETECÇÃO DE INFECÇÃO PELO HBV | presente em 201801, **ausente** em 202607 | — | Idem |

### Quebras de série a declarar explicitamente

1. **202405 — dois códigos de HPV nascem exatamente em τ3.** `0201020076` e `0201020084` foram criados na competência mai/2024, o mesmo mês do change point financeiro. Não é coincidência: a incorporação do teste de HPV faz parte do mesmo pacote. **τ3 não é só uma mudança de financiamento, é também uma mudança de tecnologia de rastreamento**, e o coeficiente de τ3 tem de ser interpretado com essa co-intervenção declarada.
2. **202511 — o exame molecular de HPV nasce dentro da janela.** Produção zero até mai/2026, mas a meta do MS é cobertura nacional até dez/2026 — dentro da janela.
3. **`TP_SEXO` de 0203010086 mudou de `F` (2018) para `I` (2026)**, e apareceram 34 registros com `PA_SEXO='M'` em mai/2026. Filtrar `PA_SEXO='F'` descarta esses casos. Volume desprezível, mas a regra de filtro muda de significado ao longo da janela.
4. **`0203010086` é estável no resto**: descrição, faixa etária e tipo de registro idênticos de 201501 a 202607. Não há quebra de codificação no desfecho.

Confirmação de vigência de qualquer código, em qualquer competência:

```python
from ftplib import FTP; import zipfile, io
f = FTP('ftp2.datasus.gov.br', timeout=120); f.login()
f.cwd('/public/sistemas/tup/downloads')
alvo = sorted(f.nlst('TabelaUnificada_*'))[-1]     # NUNCA adivinhar o nome: tem sufixo de versao
buf = io.BytesIO(); f.retrbinary('RETR ' + alvo, buf.write); f.quit()
z = zipfile.ZipFile(buf)
for line in z.open('tb_procedimento.txt'):
    co = line[0:10].decode('latin-1')
    if co in {'0203010086','0203010019','0201020033','0202100251','0204030188'}:
        print(co, line[10:260].decode('latin-1').strip()[:60],
              '| sexo', chr(line[261]), '| idade(meses)', line[274:278].decode(), '-', line[278:282].decode())
```

---

## 5. Ameaças de validade descobertas nesta sondagem

Ordenadas por gravidade para o desenho. Todas com evidência empírica, não conjectura.

**1. A série-controle prevista no protocolo está invalidada.** Mamografia de rastreamento **é** parte do C7: boa prática (D), 20 pontos, SIGTAP 02.04.03.003-0 e 02.04.03.018-8, mulheres de 50-69 anos, janela de 24 meses — verbatim na ficha oficial, conferido por dois agentes independentes. O mesmo incentivo financeiro atua sobre controle e desfecho. Ver §3 passo 3 para o substituto.

**2. Ago/2022 é zero nacional no SISCAN, e não está documentado em nenhuma publicação.** Verificado em PE filtrado, PE sem filtro e no def nacional com 5.568 municípios; e **também na mamografia** (PE 2022 pula de julho para setembro nas duas séries). Set/2022 vem inflado (31.519 contra 24.758 em julho), sugerindo transbordo. São 185 observações faltantes em t=56, num ponto que não coincide com nenhum τ. Tratar como *missing*, jamais como zero — e note que tratar só ago/2022 como missing deixa set/2022 inflado; considere agregar o bimestre nas duas séries.

**3. τ3 é uma intervenção dupla, não financeira pura.** Os códigos de coleta e auto-coleta de HPV foram criados na competência SIGTAP 202405, exatamente τ3.

**4. Duas das quatro datas de change point estão sob suspeita.** (a) A Portaria GM/MS 3.493 pode ser de **10/04/2024**, não maio — mas isso **não foi confirmado em fonte primária**: `in.gov.br`, `bvsms.saude.gov.br` e a página de normativas do SIAPS estavam inacessíveis, e a ficha C7 cita a portaria sem o dia. **Não altere o protocolo com base nisso** até conferir no DOU de outra rede. (b) O primeiro quadrimestre com C7 efetivamente apurado e publicado é **2025Q1 (jan-abr/2025)**, verificado empiricamente (2024Q1/Q2/Q3 retornam zero linhas) — τ4 posto em mai/2025 pode estar atrasado em relação à entrada em vigor.

**5. τ1 e τ2 podem ser empiricamente inseparáveis.** Estão a dois meses de distância, e a competência do SISCAN é o mês em que o exame foi **liberado e faturado pelo prestador** (Nota Técnica 3, verbatim), não o mês da coleta. Um lag heterogêneo entre municípios da ordem de 1-2 meses embaralha os dois. Pior: a distribuição do atraso **mudou no tempo** (a COVID travou laboratórios), então o operador de suavização é não-estacionário — desloca e **deforma** τ2 de modo dependente do próprio choque. A sensibilidade com `CO_ANO_MES_RESULTADO` não resolve, porque resultado também é pós-coleta. Considere declarar τ1/τ2 como um único choque composto.

**6. Censura à direita não reconhecida.** Os últimos 3-6 meses de qualquer extração são provisórios. Hoje: jun/2026 = 20.379 contra mai/2026 = 24.924 (−18%) — padrão clássico de competência ainda acumulando, não queda real. No SIA, o faturamento retroativo é de 4,2% a 11,4% conforme a competência, chegando até 3 meses depois. Não interprete inflexão no fim da série como efeito de τ4; censure a cauda ou modele-a como provisória.

**7. Erro de unidade no offset.** `pop/3` é a contagem esperada **anual**; o desfecho é mensal. O offset correto é `log(pop/3/12)`. Os coeficientes não mudam (é constante), mas qualquer cobertura reportada a partir dele sai 12× errada.

**8. O denominador não contém o choque demográfico da COVID.** As taxas de crescimento do POPSVS para fem 25-64 em PE desaceleram monotonicamente (+1,042% → +0,671%) **sem nenhuma perturbação em 2020-2021**, porque 2018-2023 são rebaseamento/interpolação entre os Censos 2010 e 2022. Exatamente em τ2 o denominador é contrafactualmente liso. O efeito é pequeno para mulheres de 25-64 e conservador (denominador levemente superestimado pós-2020 → taxa subestimada → atenua a queda detectada), mas tem de ser declarado.

**9. As taxas desta dissertação não serão comparáveis aos painéis oficiais.** O denominador do indicador 4 do Previne é população **cadastrada** na eSF/eAP; o do C7 é população **vinculada à equipe** sob a NT 30/2025. Nenhum dos dois é população residente do IBGE. Como o estudo compara justamente indicador 4 vs C7, isso tem de ser tratado no método, não assumido como resolvido.

**10. A cobertura de APS tem um degrau artificial em janeiro.** `qtCobertura` usa denominador congelado por ano (`nuAnoReferencia`), atualizado na virada de janeiro. τ1 é **janeiro**/2020. Um change point de janeiro sobreposto a um artefato de janeiro na covariável é confundimento de calendário. Reconstrua a cobertura com denominador próprio (o mesmo POPSVS) ou inclua dummy de ano-de-referência.

**11. O instrumento de medição da APS mudou junto com a política.** "Cobertura AB" termina em dez/2020 e "Cobertura APS" começa em jan/2021 — a quebra fica entre τ1 e τ2. As duas não são comparáveis (a segunda não tem teto de 100%). Trate como duas covariáveis distintas ou padronize dentro de cada regime.

**12. A cobertura ANS é pós-tratamento para τ2** (ver §3 passo 8b).

**13. Subregistro do SISCAN pode ser diferencial e crescente dentro da janela.** A caixa de ATENÇÃO da Nota Técnica fala de implantação heterogênea **entre municípios**, não só no tempo. Num painel com AR1 intra-município, subregistro persistente é absorvido pelo efeito aleatório — mas se a implantação continuou avançando em municípios pequenos dentro da janela, isso vira tendência espúria correlacionada com τ1, que por sua vez premia registro. Precisa de teste explícito (tendência pré-τ1 por porte municipal), não de frase na discussão. Métrica operacional: razão SISCAN/SIA por município-ano (§2.4).

**14. O desfecho conta exames, não mulheres, e o offset assume mulheres.** Não há identificador de paciente no SIA, e no SISCAN a dedup só existe em base anual. Recoletas por amostra insatisfatória contam duas vezes no numerador e zero no denominador — e a taxa de amostra insatisfatória é ela própria um indicador de qualidade que pode mudar em τ4. Decida e defenda: ou o desfecho é "volume de exames" (e `pop/3` vira só escala populacional, não interpretação literal de periodicidade), ou se testa o pressuposto com a razão exames/mulher do def por pacientes (§3 passo 10).

**15. `TP_MOTIVO_EXAME='01'` não é filtro neutro.** 97,3–98,6% dos registros já são rastreamento, e a proporção de repetição/seguimento pode ela própria mudar com as intervenções — filtrar por motivo é condicionar em variável pós-tratamento. Rode como sensibilidade, nunca como especificação principal.

**16. Fernando de Noronha é zero estrutural.** 1.069 mulheres de 25-64 em 2025 contra 480.781 em Recife (450×). No SIA: 0 exames em jan/2018, 2 em mai/2026. Com offset dessa magnitude e periodicidade trienal, a maioria das 108 competências terá contagem zero, e o binomial negativo com AR1 terá problema de convergência nessa unidade. Decida a priori: manter, tratar como estrato próprio, ou excluir com justificativa — e reporte a decisão. Mesmo raciocínio, em menor grau, para os municípios do sertão com menos de 2.000 mulheres na faixa.

**17. Recife está perdendo população feminina 25-64** (484.131 em 2018 → 480.781 em 2025, −0,7%) enquanto PE cresce 6,1%, e concentra ~18% do denominador. O offset por município-ano resolve, **mas só se estiver entrando como offset de coeficiente fixado em 1**, não como covariável. Vale um teste explícito.

**18. Recife oferta teste DNA-HPV desde 12/09/2022** (piloto "Útero é Vida", 1.500 mulheres, expansão prevista para 60 mil), no pré-período de τ3 e τ4, **sem qualquer rastro em base aberta**. A exposição real em PE é sistematicamente subestimada por qualquer fonte pública. Rode sensibilidade excluindo Recife e a RMR — não porque a série de Recife caia (ela sobe), mas para demonstrar que foi testado.

**19. O município de residência vem do cadastro do CNS, e o Previne Brasil induziu cadastramento massivo na APS.** Se a qualidade do campo melhorou em τ1, o desenho confunde melhora de registro com melhora de desfecho. Testável: comparar a distribuição de municípios de residência antes/depois de jan/2020 contra a distribuição populacional do IBGE e ver se a aderência salta.

**20. O erro nº 1 do pipeline atual tem origem rastreável.** O SIGTAP 02.01.02.003-3 não foi escolhido por engano arbitrário: é **exatamente e apenas** o código do numerador do indicador 4 do Previne Brasil. Alguém transportou a definição de um indicador de **pagamento** para um desfecho **epidemiológico**. Vale como achado metodológico na dissertação, porque explica por que estudos que usam o código da coleta não medem produção de exames.

---

## 6. Riscos operacionais e mitigação

| Risco | Evidência | Mitigação |
|---|---|---|
| **FTP DATASUS trunca downloads em silêncio** | Quatro arquivos `PAPE` vieram com 33-41% faltando e o `pyreaddbc` converteu sem erro; um agente publicou uma série temporal falsa por causa disso. O `curl \| awk` do SISCAN devolveu `exit 0` com 1/6 dos dados | Validar `os.path.getsize()` contra `FTP.size()` **em todo download**; retomar com `rest=`/`REST`; `assert off == size` antes de usar a saída |
| **`curl --list-only` trunca listagens** | 15 de 234 arquivos SIGTAP; 18 de 130 arquivos SISCAN; ~40 linhas no diretório do SIA — **sem erro** | `ftplib` + `NLST` + glob. Nunca conclua "o arquivo não existe" a partir de `curl` |
| **HTTP/HTTPS de `ftp.datasus.gov.br` fora do ar** | Portas 80 e 443 dão timeout em 01/08/2026 (IP 189.28.143.164); só a 21 responde | Usar FTP porta 21. Escrever o downloader com fallback entre FTP e HTTPS — pode inverter até 2027 |
| **TABNET só em HTTP, charset iso-8859-1** | Porta 443 dá ECONNREFUSED | Corpo do POST em `urlencode(..., encoding='latin-1')`; ler resposta com `.decode('latin-1')` |
| **`deftohtm.exe` devolve stub para os defs do SISCAN** | 2.379 B com "Nenhum dado disponível" — foi isso que levou o pipeline atual ao TABNET estadual/SIA | Usar `dhdat.exe` para o formulário e `webtabx.exe` para a tabulação |
| **Nomes de campo do TABNET variam entre defs** | cito usa `SMes/Ano competencia`; mamografia usa `SMes/Ano competenc` e `NU_ANO_MES_COMPETENCIA` (com `siscan` minúsculo no path do cnv) | Sempre parsear o `<SELECT>` do form da etapa 1. Nunca hardcodar |
| **Def inexistente devolve HTTP 200** | Traceback Python de ~270 B, não 404 | Testar por `grep -q '<SELECT'`, não por código HTTP |
| **Falha entre defs é ruidosa, não silenciosa** | `ORA-00904: "CO_ANO_LIBERACAO": identificador inválido` em página visível | Tratar ausência de link `.csv` como erro fatal (`raise`, não `AttributeError`) |
| **TABNET dropa municípios em recortes estreitos** | Faixa 060-064 em 2024 devolveu 183 municípios; quatro faixas devolveram 184 | Zero-fill contra frame canônico de 185 (§3 passo 2) |
| **Dados retroativamente mutáveis, sem versionamento** | O formulário só informa "Data de atualização: 20/07/2026". O arquivo SISCAN de 2023 foi atualizado em 26/01/2026, quatro meses depois dos demais. O SIB/ANS permite correção de meses anteriores | Congelar snapshot, registrar data de extração e sha256 de cada CSV, fixar a versão para a análise final |
| **Painel SISAB em desativação** | Três últimos quadrimestres rotulados "(DESCONTINUADO)"; 2020-2021 já sumiram | Extrair e arquivar **agora**; abrir LAI ao MS para 2020-2021 imediatamente |
| **APIs internas sem contrato público** | `relatorioaps-prd.saude.gov.br` e `apisiaps.saude.gov.br` não são documentadas nem versionadas | Congelar os CSVs e versioná-los no repositório do estudo |
| **`pysus` 2.7.0 quebrado no venv** | `pysus.ftp`, `pysus.online_data`, `pysus.preprocessing` → `ModuleNotFoundError`; só existem `api`, `cli`, `data`, `utils`, `web` | `pyreaddbc.dbc2dbf()` + `dbfread.DBF(encoding='latin-1')`. Validado contra `read.dbc` do R: 751.636 registros idênticos nos três leitores |
| **`microdatasus::process_sia` quebrado** | Falha com subset (`Problem with PA_CBOCOD`) e com as 60 colunas (`PA_REGCT ... Can't convert from <character> to <factor>`) | `fetch_datasus` funciona para download; fazer o pré-processamento à mão |
| **Layout do DBF POPSVS mudou em 2025** | Nomes de campo de maiúscula para minúscula; largura de `idade` de C(3) para C(5); nome do arquivo dentro do zip varia de caixa | `lowernames=True`; ler via `ZipFile.namelist()`; nunca assumir nome fixo |
| **`POPSBR26` não publicado** | Último é `POPSBR25.zip` (29/10/2025). Rótulo do `.DEF` diz "2000-2024" mas o dado de 2025 existe | Extrapolar log-linear; refazer quando sair (out/2026 a jan/2027). Confirmar sempre pela **listagem FTP**, nunca pelo `.DEF` |
| **Espaço em disco no SIA** | DBF é 13-17× o DBC: 298 MB (jan/2018) a 793 MB (mai/2026); 108 competências sem apagar = ~67 GB | Descomprimir, filtrar e deletar **arquivo a arquivo** (pico ~0,8 GB) |
| **Tempo de download do SIA** | 4,17 GB para 101 competências, ~235 KB/s medidos; ~5-6 h | Rodar em background com retomada; o script pula arquivos já validados |
| **Nome do zip SIGTAP não é adivinhável** | `TabelaUnificada_202607.zip` → curl 78; o real é `TabelaUnificada_202607_v2607101010.zip` | `sorted(f.nlst('TabelaUnificada_*'))[-1]` |
| **Não segurar conexão FTP durante conversão** | 102 ciclos de download+`dbc2dbf` na mesma conexão → 421 por idle | Baixar tudo, fechar a conexão, converter depois |
| **Últimas competências ainda não publicadas** | Hoje faltam jul-dez/2026 no SISCAN e jun-dez/2026 no SIA | Lag de publicação de ~2-3 meses. **Coletar a partir de abr/2027**, para que dez/2026 já tenha absorvido o faturamento retroativo |
| **`bvsms`, `in.gov.br`, `ses.sp.bvs.br` inacessíveis** | HTTP 000 / ECONNRESET desta rede | Textos integrais das Portarias 2.979/2019, 3.493/2024, 7.639/2025 e da que criou 0202100251 (pista: SAES/MS nº 3.223, DOU 08/10/2025) precisam ser obtidos de outra rede. **Não citar sem conferir** |
| **`ls` e `find` retornaram vazio** para diretórios com arquivos | Artefato do hook RTK nesta sessão; um agente concluiu erradamente que downloads tinham sido apagados | Verificar arquivos com Python (`os.walk`, `os.path.getsize`) ou `wc -c` |

---

## Resumo executivo em cinco linhas

1. **Desfecho primário: SISCAN via TABNET** (`SISCAN/cito_colo_residpe.def`), 8 requisições, 720 KB, 2 minutos, verificado byte a byte. Corrige os seis defeitos do pipeline atual.
2. **SIA-PA é validação cruzada obrigatória**, nunca desfecho — mede faturamento, e três dos quatro change points são financeiros.
3. **Denominador: POPSVS** (`ftp.datasus.gov.br/dissemin/publicos/IBGE/POPSVS/`), idade simples, 185/185 municípios, coerente de 2000 a 2025. Offset mensal = `log(pop/3/12)`, interpolado a partir de 1º/jul, incluindo o ponto de 2017.
4. **A série-controle do protocolo está morta** (mamografia é boa prática D do C7). Substituto: citologia fora da faixa 25-64, no mesmo SISCAN. Para τ2 não há controle válido.
5. **Colete a partir de abr/2027**, congele o snapshot com hash, e re-execute a varredura de produção de 0202100251 no SIA para as competências 202606-202612 — é a prova empírica direta de que a substituição tecnológica ainda não contaminou o desfecho.