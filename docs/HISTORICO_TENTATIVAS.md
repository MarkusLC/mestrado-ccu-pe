# Histórico de tentativas — coleta de dados de rastreamento do câncer do colo do útero (DATASUS/TABNET)

Documento de arqueologia técnica. Consolida o conhecimento operacional embutido nos 17 scripts
Python, 2 scripts R e 1 shell script escritos em 2026-07-28 para baixar dados de citopatologia
cervical de Pernambuco. Os scripts serão deletados; este documento existe para que ninguém
precise redescobrir os parâmetros do TABNET por tentativa e erro.

Escopo original pretendido: exames citopatológicos cervicais, 184 municípios de PE, série
mensal 2018–2026, para um estudo de série temporal interrompida (ITS) multinível.

**Aviso central:** os dados que ficaram versionados em `data/siscan_agregado.json` são
**artefatuais** — não são uma série temporal real. A seção
[10. Veredito](#10-veredito-e-o-que-de-fato-funciona) explica por quê, com prova numérica.

---

## 1. Sumário executivo

| Item | Conclusão |
|---|---|
| Fonte correta | TABNET estadual de PE (`tabnet.saude.pe.gov.br`), tabulação SIA/PA `tab/tabsia08/prodpe.def` |
| Fontes erradas testadas | `tabnet.datasus.gov.br/cgi/tabcgi.exe?sia/cnv/paproc.def` (DEF inexistente), portal de transferência de arquivos, APIs REST inventadas, `microdatasus`, `pysus`, `datasus-fetcher` |
| Automação necessária | **Nenhum browser.** Um `POST` HTTP form-urlencoded resolve tudo (descoberta desta análise, nunca alcançada pelos 17 scripts) |
| Parâmetro que quebrou todas as tentativas | `Arquivos` — o período. Valor é `papeYYMM.dbf`, não `YYYYMM` |
| Código SIGTAP usado | `0201020033` (coleta de material do colo do útero), via `SProcedimento=222` |
| Encoding | Tudo `ISO-8859-1` (latin-1) **com entidades HTML** (`Afr&acirc;nio`) |
| Tentativa que chegou mais perto | `download_siscan_final.py` (20:21) — única que extraiu números reais do TABNET |

---

## 2. Cronologia reconstruída

Todo o trabalho aconteceu em **2026-07-28**, entre 16:08 e 21:10 (mtimes do filesystem; o
`git log` datou tudo no mesmo dia e não desambigua). A ordem abaixo vem dos mtimes, que são
mais precisos que os commits.

| Hora | Arquivo | Abordagem | O que tentou corrigir da anterior |
|---|---|---|---|
| 16:08 | `fetch_siscan.R` (v1), `.github/workflows/update-siscan.yml`, `SETUP.md` | R + `microdatasus::fetch_datasus(information_system="SIA")` | — (ponto de partida) |
| 17:21 | `fetch_local.sh`, `SETUP_LOCAL.md` | Wrapper `Rscript fetch_siscan.R` para rodar fora do CI | GitHub Actions falhava instalando `microdatasus` (commits `1f0a0f6`, `b41d157`) |
| 17:34 | `debug_siscan.R` | Inspeção de colunas do `SIA-PA` (1 ano, checar `PA_DT_PROC`) | Não se sabia o schema retornado |
| 17:36 | `fetch_siscan.py` | Primeiro Python; chutes de endpoint TABNET + APIs REST inexistentes | Abandonar dependência de R |
| 17:38 | `fetch_siscan_playwright.py` | Playwright em `paproc.def`, clicar "Exportar" | POST cego não retornava CSV |
| 17:39 | `DOWNLOAD_REAL_DATA.md` | Instruções manuais (abrir `paproc.def`, exportar CSV) | Aceitar passo manual |
| 17:43 | `fetch_siscan.R` (v2, atual) | `SIA-PA` + filtro `grepl("^0201", PA_PROC_ID)` | `SIA` genérico não trazia procedimento |
| 17:46 | `fetch_siscan_complete.py` | 5 estratégias em cascata (GitHub mirrors, Playwright, Selenium, API, curl) | Força bruta multiestratégia |
| 17:46 | `data/siscan_raw.csv` | **Artefato de falha** gravado pela estratégia curl | — |
| 17:49 | `fetch_siscan_tabnet_portal.py` | Portal `www2.datasus.gov.br` + `cgi-bin/tabcgi.exe` | `tabnet.datasus.gov.br` retornava erro |
| 17:53 | `fetch_siscan_form.py` | Portal de transferência de arquivos; `select[name=tipo_arquivo]="PA"` | Baixar DBC bruto em vez de tabular |
| 17:55 | `fetch_siscan_correct.py` | Mesmo portal, `input[value="Dados"]/"PA"/"PE"`, `headless=False` | Seletores `select` não existiam; eram checkboxes |
| 18:03 | `fetch_siscan_real.py` | Bibliotecas `datasus-fetcher` e `pysus` (`SISCOLO`) | Abandonar scraping por biblioteca pronta |
| 18:05 | `fetch_tabnet_process.py` | Só processa CSV baixado à mão | Aceitar que o download é manual |
| 18:05 | `fetch_tabnet_simple.py` | Playwright só para *listar* links do TABNET PE | Descobrir a estrutura do portal estadual |
| 18:05–18:06 | `DOWNLOAD_TABNET.md`, `DADOS_REAIS.md` | Documenta o compromisso manual + automação | — |
| **18:14** | **`fetch_sia_citopatologia.py`** | **Descoberta do endpoint e dos campos reais do TABNET PE** | **Virada de chave do projeto** |
| 18:16 | `download_siscan_full.py` | Headless + `pandas.read_html` na tabela | Remover o passo manual do anterior |
| **20:21** | **`download_siscan_final.py`** | **BeautifulSoup + `table.tabdados` + `//input[@value="Mostra"]`** | `pandas.read_html` não achava a tabela; botão era `Mostra`, não `Pesquisar` |
| 20:21 | `download_siscan_historico.py` | Loop de 15 períodos (`"202612"`, `"202501"`, …) | Só o mês corrente vinha |
| 20:30 | `expand_siscan_full.py` | 1 query por ano (janeiro de cada ano) | Reduzir número de requisições |
| 20:52 | `expand_siscan_mensal.py` | 1 query por mês | Série anual saiu "lisa" (idêntica) |
| 20:54 | `ACHADO_DADOS_ESTRANHOS.md` | Diagnóstico da série lisa (**causa-raiz errada**) | — |
| 20:57 | `expand_siscan_completo.py` | Múltiplas dimensões (sexo, idade, região, financiamento) | Enriquecer o dataset |
| 20:59 | `expand_sexo.py` | Só sexo (M/F), 11 meses | Versão enxuta do anterior |
| 21:10 | `dashboard_mestrado.html` (final) | Consome o JSON | — |

Padrão de nomes como pista cronológica: `fetch_siscan.py` → `_playwright` → `_complete` →
`_tabnet_portal` → `_form` → `_correct` → `_real` → `download_..._full` → `download_..._final`
→ `_historico` → `expand_..._full` → `_mensal` → `_completo`. Cada adjetivo mais enfático
sinaliza que o anterior não resolveu.

---

## 3. Endpoints e URLs testados

### 3.1 O endpoint que funciona

```
Página do formulário (GET):
  https://tabnet.saude.pe.gov.br/cgi-bin/dh?tab/tabsia08/prodpe.def

Alvo da submissão (POST) — note que o CGI muda de "dh" para "tabnet":
  https://tabnet.saude.pe.gov.br/cgi-bin/tabnet?tab/tabsia08/prodpe.def
```

Título da tabulação: *Produção Ambulatorial de Procedimentos da Tabela Unificada* (TabNet Linux 2.7).

O HTML da página do formulário declara literalmente:

```html
<FORM ACTION="/cgi-bin/tabnet?tab/tabsia08/prodpe.def" METHOD=POST>
```

**Nenhum dos 17 scripts usou o alvo `/cgi-bin/tabnet?...` diretamente.** Todos abriram
`/cgi-bin/dh?...` num browser headless e clicaram no botão de submit. Esse foi o custo
principal de complexidade do projeto: 10 dos 17 scripts existem só para automatizar um clique
que um `POST` de 10 linhas resolve.

Verificado nesta análise (2026-08-01): `GET` na página do formulário retorna HTTP 200, ~1,2 MB.
`POST` no alvo retorna HTTP 200 com os dados.

### 3.2 Endpoints que não funcionam

| URL | Usada por | Resultado |
|---|---|---|
| `http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sia/cnv/paproc.def` | `fetch_siscan.py`, `fetch_siscan_playwright.py`, `fetch_siscan_complete.py`, `DOWNLOAD_REAL_DATA.md` | **Erro do servidor:** `Arquivo DEF não encontrado: sia/cnv/paproc.def`. O DEF `paproc.def` não existe nesse caminho. Ver §9.1 |
| `https://www2.datasus.gov.br/cgi-bin/tabcgi.exe?sia/cnv/paproc.def` | `fetch_siscan_tabnet_portal.py` (`direct_datasus_endpoint`) | Mesmo problema; host/caminho errados |
| `https://www2.datasus.gov.br/DATASUS/index.php` | `fetch_siscan_tabnet_portal.py` | Portal institucional; navegação por texto ("Assistência à Saúde", "SISCAN") frágil, não chegou a dados |
| `https://datasus.saude.gov.br/transferencia-de-arquivos/` | `fetch_siscan_form.py`, `fetch_siscan_correct.py` | Página existe, mas entrega **DBC bruto** (microdados), não CSV tabulado. Os seletores assumidos (`select[name="tipo_arquivo"]`, `select[name="ano"]`, `select[name="mes"]`, `input[value="Dados"]`, `input[value="PA"]`, `input[value="PE"]`, `button:has-text("Enviar")`) nunca casaram |
| `https://datasus.saude.gov.br/informacoes-de-saude-tabnet/` | `fetch_tabnet_simple.py` | Índice de tabulações; usada só como ponto de partida de navegação |
| `https://tabnet.saude.pe.gov.br/` | `fetch_tabnet_simple.py`, `DOWNLOAD_TABNET.md` | Raiz do TABNET PE — correta, mas sem o `.def` específico não leva a nada automatizável |
| `https://api.datasus.gov.br/v1/siscan/exames` | `fetch_siscan.py` | **Não existe.** URL inventada |
| `https://apis.saude.gov.br/siscan/exames` | `fetch_siscan_complete.py` | **Não existe.** URL inventada |
| `https://datasus.saude.gov.br/api/v1/siscan` | `fetch_siscan_complete.py` | **Não existe.** URL inventada |
| `https://www.datasusb.saude.gov.br/sia/exportar` | `fetch_siscan.py` | **Não existe.** Domínio inventado (`datasusb`) |
| `https://datasus.saude.gov.br/transferencia-de-arquivos/publicos/SISCAN` | `fetch_siscan.py` | Só `HEAD`; nunca produziu dados |
| `https://raw.githubusercontent.com/rfsaldanha/pysus/master/pysus/data/`, `https://datasus-mirrors.github.io/data/`, `https://api.github.com/search/code?q=SISCAN+filetype:csv` | `fetch_siscan_complete.py` (`strategy_github_mirrors`) | Busca especulativa por espelhos; nenhum dado |

**Não existe API REST pública do DATASUS/SISCAN.** Toda URL do tipo `api.*/siscan` nos scripts
é invenção. TABNET é CGI com formulário HTML; é essa a interface programática disponível.

### 3.3 Bibliotecas testadas

| Biblioteca | Chamada exata | Resultado |
|---|---|---|
| `microdatasus` (R) | `fetch_datasus(year_start=2018, year_end=2026, information_system="SIA-PA")` | Baixa microdados SIA-PA (arquivos `PA*.dbc`). Volume enorme para PE × 9 anos; falhou repetidamente no GitHub Actions na etapa de instalação (`remotes::install_github('rfsaldanha/microdatasus')`) |
| `microdatasus` (R), v1 | `information_system = "SIA"` | Valor inválido/insuficiente; corrigido para `"SIA-PA"` no commit `1dba86e` |
| `pysus` | `from pysus.online_data import SISCOLO; SISCOLO().download(state='PE', year=2024)` | API imaginada. `pysus` não expõe `SISCOLO` dessa forma |
| `datasus-fetcher` | `Fetcher(system='SISCOLO').download(state='PE', years=range(2018,2027))` | API imaginada. Não existe construtor `Fetcher(system=...)` com esse contrato |

Colunas do SIA-PA que os scripts R usavam (úteis se algum dia se voltar a microdados):
`PA_PROC_ID` (procedimento SIGTAP, 10 dígitos), `PA_MUNOFN` (município), `PA_DT_PROC`
(data de processamento, formato `%d%m%Y`). O filtro aplicado era `grepl("^0201", PA_PROC_ID)`
— note que `^0201` captura todo o subgrupo "0201 Coleta de material", não só citopatologia
cervical.

---

## 4. Parâmetros do formulário TABNET (referência canônica)

Todos os nomes e valores abaixo foram extraídos do HTML de
`https://tabnet.saude.pe.gov.br/cgi-bin/dh?tab/tabsia08/prodpe.def` e **validados por POST real**
em 2026-08-01. Onde um script usou valor divergente, isso está marcado.

### 4.1 Estrutura geral do formulário

| Campo | Tipo | Obrigatório | Observação |
|---|---|---|---|
| `Linha` | `select` (51 opções) | sim | Dimensão das linhas |
| `Coluna` | `select` (29 opções) | sim | Dimensão das colunas; default `--Não-Ativa--` |
| `Incremento` | `select` (8 opções) | sim | Métrica |
| `Arquivos` | `select` **múltiplo** (221 opções) | sim | **O período.** Aceita repetição do campo |
| `S<Dimensão>` | `select` múltiplo (36 campos) | não | Filtros. Prefixo `S` + nome da dimensão |
| `formato` | `radio` | sim | `table` (default) \| `pre` \| `prn` |
| `opcoes` | `checkbox` | não | Único valor conhecido: `ordenar` |
| `mostre` | `submit` | **sim** | Valor literal `Mostra` |

Campo de reset: `<INPUT TYPE="reset" VALUE=Limpa>` (irrelevante para POST).

Encoding do corpo do POST: **latin-1**. Nomes de campo contêm acentos e caracteres não-ASCII
(`Mês_Competen_______`, `SForma_Organização`, `SRaça/Cor_Paciente__`) — se codificados em UTF-8
o CGI não os reconhece.

### 4.2 `Linha` — valores (51 opções)

Preservar os underscores de padding: eles fazem parte do valor literal.

```
Mês_Competen_______     (SELECIONADO por default)
Ano_Competen_______
Mês_Atendimento____
Ano_Atendimento____
BPA-C/BPA-I/APAC___
Procedimento
Grupo_proced.
SubGrup_proced
Forma_Organização
Complex.procedim.
Carater_de_Atendim.
Motivo_Saida/Perman
Motivo_Saida-Alta__
Motivo_Saida-Óbito_
Mot.Saida-Encerram.
Mot.Saida-Permanên.
Mot.Saida-Transfer.
Tp.Financiamento
Profissional-CBO___
Tipo_de_Gestão______
Estabel-CNES_PE
REDE_Psicossocial
Natureza_estab_OUT/15
Natureza_Jurídica
Munic._Estabelecim        <-- município do ESTABELECIMENTO (usado pelos scripts)
RD_Estab
Região_Saude-Estab
Macrorreg_Estab
Microrreg_Estab
Sexo_do_Paciente___
Idade_do_Paciente__
Raça/Cor_Paciente__
Etnia______________
Munic_Resid_Pac_BR
Munic_Resid_Pac           <-- município de RESIDÊNCIA do paciente
RD_Resid_Pac
Reg_Saude-Resid_Pac
Macrorreg_Resid_Pac
Microrreg_Resid
Hosp.Regionais
Seis_Grandes_Hosp
Proced_Cons.Méd.Bás
Causas_Sensivei
Rede_Complementar__
Diag_CID10_(capit)
Diag_CID10_(grupo)
Diag_CID10_(categ)
SAMU
CEO
UPA
UPAE
```

Atenção metodológica: `Munic._Estabelecim` (com ponto depois de "Munic") agrega pelo município
onde o procedimento foi *faturado*; `Munic_Resid_Pac` (sem ponto) agrega pela residência da
paciente. Para cobertura populacional de rastreamento com denominador municipal, o correto em
geral é **residência**. Todos os scripts usaram `Munic._Estabelecim`.

### 4.3 `Coluna` — valores (29 opções)

```
--Não-Ativa--             (SELECIONADO por default; produz coluna única)
Mês_Competen_______       <-- série mensal em UMA requisição
Ano_Competen_______       <-- usado pelos scripts
Mês_Atendimento____
Ano_Atendimento____
BPA-C/BPA-I/APAC___
Grupo_proced.
Forma_Organização
Complex.procedim.
Carater_de_Atendim.
Tp.Financiamento
Tipo_de_Gestão______
Tipo_Estabelecim
Natureza_estab_OUT/15
Natureza_Jurídica
Região_Saude-Estab
Macrorreg_Estab
Microrreg_Estab
Sexo_do_Paciente___
Idade_do_Paciente__
Raça/Cor_Paciente__
Etnia______________
Munic_Resid_Pac
RD_Resid_Pac
Reg_Saude-Resid_Pac
Macrorreg_Resid_Pac
Microrreg_Resid
UPA
UPAE
```

`Coluna` não repete todos os valores de `Linha` (não há `Munic._Estabelecim` em `Coluna`, por exemplo).

### 4.4 `Incremento` — valores (8 opções, lista completa)

```
Frequencia_______        (SELECIONADO por default) - contagem de registros
Vl.Aprovado________
Qtd.Apresentada____      - quantidade de procedimentos apresentada
Vl.Apresentado_____
Vl.Complem._Federal
Vl.Complem._Local__
Vl.Incremento______
DIF.VALOR__________
```

Valores usados pelos scripts e que **não existem**: `"Exames"` (`fetch_siscan.py`,
`fetch_siscan_tabnet_portal.py`), `"V"` (`fetch_sia_citopatologia.py`,
`download_siscan_full.py`). Por isso os scripts posteriores passaram a forçar
`options[0].selected = true` via JavaScript, isto é, ficaram presos no default `Frequencia`.

Para contagem de exames o semanticamente correto é `Qtd.Apresentada____`. Em verificação
pontual (Mar/2026, procedimento 0201020033) `Frequencia` e `Qtd.Apresentada` retornaram valores
idênticos, mas são conceitos distintos (registros BPA vs. quantidade de procedimentos) e podem
divergir. `Vl.Aprovado________` retornou vazio para esse procedimento.

### 4.5 `Arquivos` — o período (221 opções) — PARÂMETRO CRÍTICO

Formato do valor: **`papeYYMM.dbf`** (nome do arquivo DBF de competência), rótulo `Mmm/AAAA`.

```
pape2605.dbf  ->  Mai/2026    (SELECIONADO por default)
pape2604.dbf  ->  Abr/2026
pape2603.dbf  ->  Mar/2026
pape2602.dbf  ->  Fev/2026
pape2601.dbf  ->  Jan/2026
pape2512.dbf  ->  Dez/2025
...
pape1801.dbf  ->  Jan/2018
...
pape0801.dbf  ->  Jan/2008    (mais antigo disponível)
```

Cobertura: **Jan/2008 a Mai/2026** (221 competências) — bem mais que o intervalo 2018–2026
pretendido pelo estudo.

O select é **múltiplo**: repetir `Arquivos=...` no corpo do POST seleciona várias competências
de uma vez. Combinado com `Coluna=Mês_Competen_______`, isso devolve uma coluna por mês em
uma única requisição.

**Este é o parâmetro que quebrou todo o projeto.** Todos os scripts que tentaram variar o
período usaram valores no formato `"202601"`, `"201801"`, `"202612"`:

- `download_siscan_historico.py`: lista `periodos = ["202612", "202611", ..., "201801"]`
- `expand_siscan_full.py`: `[("201801","2018"), ..., ("202601","2026")]`
- `expand_siscan_mensal.py`: `[("202601","Jun/2026"), ("202605","Mai/2026"), ...]`
- `expand_siscan_completo.py`: `['202603','202202','202102','202002','201902','201802']`
- `expand_sexo.py`: `['202603','202602','202601','202512', ...]`

Nenhum desses valores existe entre as `<option>`. O truque JavaScript usado
(`opts.forEach(o => { if (o.value === "202601") o.selected = true })`) nunca casava, e o
`select` permanecia no default `pape2605.dbf` (Mai/2026). **Toda "série temporal" coletada é a
mesma competência Mai/2026 repetida, com rótulo de mês fabricado a partir da variável do loop.**

`expand_sexo.py` tem uma tentativa reveladora — a única que menciona o nome certo do campo,
mas em código que não faz nada:

```python
page.evaluate(f'document.querySelector("select[name*=Arquivos]") && document.querySelector("select[name*=Arquivos]").value === "{periodo}"')
```

É uma comparação (`===`), não uma atribuição; e o valor comparado está no formato errado.

Limite prático de competências por requisição (medido em 2026-08-01, procedimento 222,
`Coluna=Mês_Competen`):

| Competências | Tempo | Resultado |
|---|---|---|
| 3 | ~5 s | OK |
| 12 (1 ano) | ~17 s | OK |
| 24 (2 anos) | ~28 s | OK |
| 60 (5 anos) | ~56 s | OK |
| 101 (2018–mai/2026) | — | `IncompleteRead` — servidor aborta a resposta |

Recomendação: lotes de 12 a 24 competências, com pausa entre requisições.

### 4.6 `SProcedimento` — filtro de procedimento (5.673 opções)

O `value` é um **índice posicional dentro deste `.def`**, não o código SIGTAP. O texto da
`<option>` é `"<código SIGTAP 10 dígitos> <DESCRIÇÃO>"`.

```
222  =  0201020033 COLETA DE MATERIAL DO COLO DE UTERO PARA EXAME CITOPATOLOGICO
```

Confirmado: `SProcedimento=222` retorna cabeçalho
`Procedimento: 0201020033 COLETA DE MATERIAL DO COLO DE UTERO PARA EXAME CITOPATOLOGICO`.

**Fragilidade:** o índice `222` desloca quando novos procedimentos entram na SIGTAP e o `.def`
é regerado. Um pipeline robusto deve baixar o formulário, procurar a `<option>` cujo texto
começa com o código SIGTAP desejado e ler o `value` daquela opção — nunca hardcodar `222`.

Todos os campos de filtro seguem o padrão `S` + nome da dimensão, e todos aceitam o valor
especial `TODAS_AS_CATEGORIAS__` (equivalente a "sem filtro"):

```
SBPA-C/BPA-I/APAC___   SProcedimento          SGrupo_proced.        SSubGrup_proced
SForma_Organização     SComplex.procedim.     SCarater_de_Atendim.  STp.Financiamento
SProfissional-CBO___   STipo_de_Gestão______  SEstabel-CNES_PE      SNatureza_estab_OUT/15
SNatureza_Jurídica     SMunic.Estabelecim     SRD_Estab             SRegião_Saude-Estab
SMacrorreg_Estab       SMicrorreg_Estab       SSexo_do_Paciente___  SIdade_do_Paciente__
SRaça/Cor_Paciente__   SEtnia______________   SMunic_Resid_Pac      SRD_Resid_Pac
SReg_Saude-Resid_Pac   SMacrorreg_Resid_Pac   SMicrorreg_Resid      SDiag_CID10_(capit)
SDiag_CID10_(grupo)    SDiag_CID10_(categ)    SSAMU                 SCEO
SUPA                   SUPAE
```

Note a inconsistência de pontuação entre `Linha` e o filtro correspondente:
`Linha=Munic._Estabelecim` mas filtro `SMunic.Estabelecim` (sem underscore).

### 4.7 Valores dos filtros usados pelos scripts (com correções)

**`SSexo_do_Paciente___`** (4 opções) — valores usados em `expand_sexo.py` e
`expand_siscan_completo.py` estão **corretos**:

```
TODAS_AS_CATEGORIAS__  Todas as categorias
1                      Masculino
2                      Feminino
3                      (rótulo vazio — provável "não informado")
```

**`SIdade_do_Paciente__`** (134 opções) — valores usados em `expand_siscan_completo.py` estão
**errados**. O `value` é índice sequencial, não a idade:

```
TODAS_AS_CATEGORIAS__  Todas as categorias
1                      Menos que 1 ano de idade
2                      1 ano
3                      2 anos
...                    (regra: value = idade + 2, para idade >= 1)
6                      5 anos          <- o script mapeava "5" para "5 anos"; 5 é 4 anos
16                     15 anos         <- o script mapeava "15" para "15 anos"; 15 é 14 anos
21                     20 anos
26                     25 anos
31                     30 anos
41                     40 anos
51                     50 anos
61                     60 anos
132                    Idade não exigida (BPA-C)
133                    Idade informada com erro
```

Faixa etária-alvo do rastreamento de CCU (25 a 64 anos) = `value` de `26` a `65`.

**`STp.Financiamento`** (7 opções) — os rótulos assumidos em `expand_siscan_completo.py`
(`'1'='PAB'`, `'4'='Estratégico'`) estão parcialmente errados:

```
TODAS_AS_CATEGORIAS__  Todas as categorias
1                      01 Atenção Básica (PAB)                                <- correto no script
2                      02 Assistência Farmacêutica
3                      04 Fundo de Ações Estratégicas Compensações FAEC       <- este é o "Estratégico"
4                      05 Incentivo - MAC                                     <- o script chamava de "Estratégico"
5                      06 Média e Alta Complexidade (MAC)
6                      07 Vigilância em Saúde
```

**`SReg_Saude-Resid_Pac`** (14 opções) — as 4 primeiras assumidas em
`expand_siscan_completo.py` estão **corretas**; lista completa das 12 regiões de saúde de PE:

```
TODAS_AS_CATEGORIAS__  Todas as categorias
1   2601 Recife                 7   2607 Salgueiro
2   2602 Limoeiro               8   2608 Petrolina
3   2603 Palmares               9   2609 Ouricuri
4   2604 Caruaru                10  2610 Afogados da Ingazeira
5   2605 Garanhuns              11  2611 Serra Talhada
6   2606 Arcoverde              12  2612 Goiana
13  2600 Município ignorado - PE
```

**`SMacrorreg_Resid_Pac`** (17 opções) — hierárquico, com cabeçalhos de macrorregião
intercalados (I a IV) e regiões prefixadas por `...`. Cabeçalhos são selecionáveis e agregam
as filhas:

```
1   I MACRORREGIÃO   (2601 Recife, 2602 Limoeiro, 2603 Palmares, 2612 Goiana)
6   II MACRORREGIÃO  (2604 Caruaru, 2605 Garanhuns)
9   III MACRORREGIÃO (2606 Arcoverde, 2610 Afogados da Ingazeira, 2611 Serra Talhada)
13  IV MACRORREGIÃO  (2607 Salgueiro, 2608 Petrolina, 2609 Ouricuri)
```

**`SMunic.Estabelecim`** (186 opções = `TODAS_AS_CATEGORIAS__` + 185 municípios). Rótulo é
`"<código IBGE 6 dígitos> <Nome>"`:

```
1   260005 Abreu e Lima
2   260010 Afogados da Ingazeira
3   260020 Afrânio
4   260030 Agrestina
5   260040 Água Preta
...
```

185 = 184 municípios de PE + Fernando de Noronha (distrito estadual), consistente com os
"184 municípios" da metodologia do dashboard.

**`SBPA-C/BPA-I/APAC___`** (6 opções) — relevante para separar produção consolidada de individualizada:

```
TODAS_AS_CATEGORIAS__  Todas as categorias
1   BPA-C
2   BPA-I
3   APAC
4   ..APAC - Procedimento Principal
5   ..APAC - Procedimento Secundário
```

**`SGrupo_proced.`** / **`SSubGrup_proced`** / **`SForma_Organização`** — alternativa a filtrar
procedimento individual:

```
SGrupo_proced.:     2 = "02 Procedimentos com finalidade diagnostica"
SSubGrup_proced:    3 = "0201 Coleta de material"
                    5 = "0203 Diagnostico por anatomia patologica e citopatologi"
SForma_Organização: 8 = "020101 Coleta de material por meio de puncao/biopsia"
                    9 = "020102 Outras formas de coleta de material"
```

### 4.8 Botão de submissão

```
<INPUT NAME="mostre" TYPE="submit" VALUE=Mostra>
```

Ou seja: `mostre=Mostra`. Os scripts iniciais procuraram botões `"Pesquisar"`, `"Enviar"`,
`"Exportar"`, `"Arquivo"` — nenhum existe. Só em `download_siscan_final.py` (20:21) aparece o
seletor certo, via XPath `//input[@value="Mostra"]`.

### 4.9 Formato de saída — `formato`

```
formato=table   (default)  tabela HTML com class="tabdados"
formato=pre                texto pré-formatado, alinhado por espaços
formato=prn                CSV com ";" e campos entre aspas, dentro de <PRE>
```

**`formato=prn` é o achado que dispensa todo o parsing de HTML.** Nenhum dos 17 scripts o
descobriu; todos raspavam a tabela HTML.

### 4.10 Parâmetros inventados nos scripts (não existem no TABNET)

Registrados para que ninguém os reintroduza:

```
Tema=SIA            pesquisa=1          Pesquisa=1        cgi=sidratbr.def
tabela=2005         region=PE           Linha=Município   Coluna=Período
Incremento=Exames   Incremento=V        Incremento=Valores
```

---

## 5. Receita reproduzível validada

Sem browser, sem Playwright, sem BeautifulSoup. Validado em 2026-08-01.

```python
import urllib.request, urllib.parse, re, html

URL = "https://tabnet.saude.pe.gov.br/cgi-bin/tabnet?tab/tabsia08/prodpe.def"

def consulta(competencias, sprocedimento="222", incremento="Qtd.Apresentada____",
             linha="Munic._Estabelecim", coluna="Mês_Competen_______"):
    """competencias: lista de nomes de arquivo, ex. ['pape2601.dbf', 'pape2602.dbf']"""
    campos = [("Linha", linha), ("Coluna", coluna), ("Incremento", incremento)]
    campos += [("Arquivos", c) for c in competencias]
    campos += [("SProcedimento", sprocedimento), ("formato", "prn"), ("mostre", "Mostra")]

    # ATENÇÃO: latin-1, não UTF-8 — nomes de campo têm acentos
    corpo = urllib.parse.urlencode(campos, encoding="latin-1").encode("latin-1")
    req = urllib.request.Request(URL, data=corpo,
                                 headers={"User-Agent": "Mozilla/5.0"})
    texto = urllib.request.urlopen(req, timeout=180).read().decode("latin-1")

    bloco = re.search(r"<PRE>(.*?)</PRE>", texto, re.S | re.I)
    if not bloco:
        return []  # sem dados para o filtro/período

    # só linhas que começam com aspas são dados; o TABNET emite um "&" solto no fim
    linhas = [html.unescape(l) for l in bloco.group(1).strip().splitlines()
              if l.startswith('"')]
    return [l.split(";") for l in linhas]
```

Resposta real (`Arquivos` = Jan, Fev, Mar/2026; `SProcedimento=222`):

```
Qtd.Apresentada     por Mês Competen        segundo Munic. Estabelecim
Procedimento: 0201020033 COLETA DE MATERIAL DO COLO DE UTERO PARA EXAME CITOPATOLOGICO
Período: Jan-Mar/2026
<PRE>
"Munic. Estabelecim";"Jan/2026";"Fev/2026";"Mar/2026";"Total"
"260020 Afrânio";85;69;74;228
"260120 Arcoverde";23;104;11;138
"260150 Belém de Maria";122;123;121;366
"260290 Cabo de Santo Agostinho";196;104;258;558
"260345 Camaragibe";2;5;4;11
...
&
</PRE>
```

Os valores **variam mês a mês** — confirmação de que o parâmetro `Arquivos` é o que faltava.

Pontos de atenção no parsing do `prn`:

1. A **última coluna é `"Total"`** — precisa ser descartada, não somada (ver §10).
2. O bloco `<PRE>` termina com uma linha contendo só `&`. Filtrar por `startswith('"')`.
3. O texto vem com **entidades HTML** dentro de conteúdo latin-1: `"260020 Afr&acirc;nio"`.
   Ordem correta: `decode("latin-1")` e depois `html.unescape()`.
4. Pode haver linha `"TOTAL"` agregada; descartar por nome.

---

## 6. Códigos SIGTAP relevantes

Extraídos do `<select name="SProcedimento">` (5.673 opções). A coluna `value` é o índice do
`.def` de PE em **mai/2026** — reconfirmar sempre pelo texto da opção.

### 6.1 Usado pelos scripts

| SIGTAP | `value` | Descrição | Uso |
|---|---|---|---|
| `0201020033` | `222` | COLETA DE MATERIAL DO COLO DE UTERO PARA EXAME CITOPATOLOGICO | **Único código usado.** Presente em `fetch_sia_citopatologia.py` e em todos os `download_*`/`expand_*` |
| `^0201` (prefixo) | — | subgrupo "0201 Coleta de material" | `fetch_siscan.R`: `grepl("^0201", PA_PROC_ID)` — captura muito mais que citopatologia cervical |
| `020101`, `020102`, `020103` | — | citados em comentários de `fetch_siscan.py` e `fetch_siscan.R` como "códigos de citopatologia" | Atribuição incorreta: são *formas de organização*, não procedimentos |

### 6.2 Cascata completa do rastreamento de CCU (mapeada nesta análise)

Rastreamento / coleta:

| SIGTAP | `value` | Descrição |
|---|---|---|
| `0201020033` | `222` | Coleta de material do colo de útero para exame citopatológico |
| `0201020076` | `226` | Coleta de material do colo do útero para exame molecular de detecção de HPV |
| `0201020084` | `227` | Entrega de material obtido por autocoleta para exame molecular de HPV no colo do útero |

Exame citopatológico (diagnóstico laboratorial):

| SIGTAP | `value` | Descrição |
|---|---|---|
| `0203010019` | `766` | Exame citopatológico cérvico-vaginal/microflora |
| `0203010060` | `771` | Exame citopatológico cérvico vaginal — **rastreamento** |
| `0203010086` | `773` | Exame citopatológico cérvico vaginal/microflora — rastreamento |
| `0203010027` | `767` | Exame citopatológico hormonal seriado (mínimo 3 coletas) |
| `0203010051` | `770` | Controle externo de qualidade do exame citopatológico cérvico vaginal |
| `0203010078` | `772` | Controle de qualidade do exame citopatológico cérvico vaginal |

Confirmação diagnóstica:

| SIGTAP | `value` | Descrição |
|---|---|---|
| `0201010666` | `219` | Biópsia do colo uterino |
| `0211040029` | `1054` | Colposcopia |
| `0203020081` | `781` | Exame anatomopatológico do colo uterino — biópsia |
| `0203020022` | `775` | Exame anatomopatológico do colo uterino — peça cirúrgica |

Tratamento de lesões precursoras:

| SIGTAP | `value` | Descrição |
|---|---|---|
| `0409060089` | `3609` | Excisão tipo I do colo uterino |
| `0409060305` | `3631` | Excisão tipo 2 do colo uterino |
| `0409060038` | `3604` | Excisão tipo 3 do colo uterino |
| `0309030048` | `2198` | Criocauterização / eletrocoagulação de colo de útero |
| `0416060013` | `4038` | Amputação cônica do colo do útero em oncologia |

Ofertas de Cuidado Integrado (OCI, novas na SIGTAP):

| SIGTAP | `value` | Descrição |
|---|---|---|
| `0901010057` | `5640` | OCI investigação diagnóstica de câncer de colo do útero |
| `0901010065` | `5641` | OCI avaliação diagnóstica e terapêutica de câncer de colo do útero |
| `0901010111` | `5646` | OCI avaliação diagnóstica e terapêutica de câncer de colo do útero — I |
| `0901010120` | `5647` | OCI avaliação diagnóstica e terapêutica de câncer de colo do útero — II |

Gestão / habilitação de serviços:

| SIGTAP | `value` | Descrição |
|---|---|---|
| `0102010331` | `106` | Cadastro de serviços de diagnóstico e tratamento do câncer de colo de útero e mama |
| `0102010340` | `107` | Inspeção sanitária desses serviços |
| `0102010358` | `108` | Licenciamento sanitário desses serviços |

### 6.3 Cobertura empírica por código (PE, Jan–Mar/2026, `Linha=Munic._Estabelecim`)

| Código | `value` | Municípios com registro |
|---|---|---|
| `0201020033` (coleta) | `222` | **24** |
| `0203010019` (exame cito/microflora) | `766` | **45** |
| `0203010060` (exame cito — rastreamento) | `771` | **0** (sem dados no SIA de PE) |

Achado metodológico relevante: o código escolhido pelos scripts (`0201020033`) tem a **menor**
cobertura municipal dos três. Uma série municipal de rastreamento em PE provavelmente precisa
somar `0201020033` + `0203010019`, ou usar o subgrupo `0203` inteiro. Cobrir 184 municípios com
um único código de procedimento não parece viável — vale validar contra outra fonte (SISCAN
próprio, ou painéis do INCA) antes de fechar a metodologia.

---

## 7. Trechos de código reaproveitáveis

### 7.1 Encoding — o problema mais recorrente

`data/siscan_raw.csv` **não é UTF-8 e não é CSV**: é uma página HTML de erro em
**ISO-8859-1**. Conteúdo íntegro (317 bytes):

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" ...>
<html lang="pt-BR">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<head><h1>ERRO:</h1></head>
<html><body>
<h3>Arquivo DEF não encontrado: sia/cnv/paproc.def</h3>
</body></html>
```

Verificável com `file -I data/siscan_raw.csv` → `text/html; charset=iso-8859-1`.

Foi gravado às 17:46 pela `strategy_curl_direct` de `fetch_siscan_complete.py`, que faz
`curl -s -o data/siscan_raw.csv <url>` e aceita como sucesso qualquer arquivo com
`os.path.getsize(...) > 1000` — a página de erro tem 317 bytes, então essa estratégia
retornou `False`, mas o arquivo lixo ficou no disco e passou a ser lido pelos scripts
seguintes (`fetch_tabnet_process.py` procura `data/siscan_raw.csv` na lista de candidatos).

Como os scripts lidaram (evolução):

```python
# fetch_siscan_playwright.py (17:38) — encoding fixo
df = pd.read_csv(csv_file, encoding='latin-1')

# fetch_siscan_complete.py (17:46) — + tolerância a linhas ruins
df = pd.read_csv(csv_file, encoding='latin-1', on_bad_lines='skip')

# fetch_siscan_tabnet_portal.py (17:49) — cascata de encodings
for encoding in ['latin-1', 'utf-8', 'iso-8859-1']:
    try:
        df = pd.read_csv(csv_file, encoding=encoding, on_bad_lines='skip'); break
    except: continue

# fetch_tabnet_process.py (18:05) — cascata mais completa (a melhor das versões)
for encoding in ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']:
    try:
        df = pd.read_csv(csv_file, encoding=encoding, on_bad_lines='skip')
        print(f"Loaded with encoding: {encoding}"); break
    except: continue
```

Observação: a cascata é enganosa. `latin-1` **nunca falha** (todo byte é válido), então tentar
`utf-8` primeiro e cair em `latin-1` funciona, mas colocar `latin-1` primeiro mascara
silenciosamente arquivos UTF-8 (mojibake). Para TABNET a resposta é sempre `iso-8859-1` —
não há ambiguidade e a cascata é desnecessária.

Regra correta para o TABNET, em duas etapas:

```python
texto = resposta_bytes.decode("latin-1")   # o TABNET declara iso-8859-1
texto = html.unescape(texto)               # e ainda emite &acirc;, &eacute;, &ccedil;...
```

Sem o `html.unescape`, nomes de municípios saem como `Afr&acirc;nio`, `Bel&eacute;m de Maria`,
`Jaboat&atilde;o dos Guararapes`. Nenhum dos 17 scripts fez `unescape` — usavam
`get_text()` do BeautifulSoup, que resolve entidades automaticamente. Ao migrar para `formato=prn`
(texto puro), o `unescape` passa a ser obrigatório.

Curiosidade documental: no `<select name="SProcedimento">` alguns rótulos vêm com mojibake
já na origem (`1¶Ý LINHA` em vez de `1ª LINHA`) — corrupção no próprio `.def` do servidor,
não no cliente. Não tentar consertar.

### 7.2 Normalização de nome de município

Formato do rótulo TABNET: `"<código IBGE 6 dígitos><espaços><Nome>"`, ex. `260020 Afrânio`.

O regex usado (idêntico em `download_siscan_final.py`, `download_siscan_historico.py`,
`expand_siscan_full.py`, `expand_siscan_mensal.py`, `expand_siscan_completo.py`, `expand_sexo.py`):

```python
match = re.search(r'\d+\s+(.+)', municipio_text)
municipio = match.group(1) if match else municipio_text
```

Funciona, mas **descarta o código IBGE** — que é justamente a chave estável para join com
população (denominador do estudo) e com malhas geográficas. Preservar ambos:

```python
m = re.match(r'(\d{6})\s+(.+)', municipio_text.strip())
cod_ibge, nome = (m.group(1), m.group(2).strip()) if m else (None, municipio_text.strip())
```

Filtro de linhas agregadas (usado em todos os scripts):

```python
if not municipio_text or municipio_text == 'TOTAL':
    continue
# download_siscan_full.py usava versão mais ampla:
if municipio.lower() in ['total', 'não informado', '']:
    continue
```

Deve incluir também `Município ignorado - PE` (código `2600`) quando aparecer.

### 7.3 Parsing da tabela HTML do TABNET (`formato=table`)

Se por algum motivo for necessário manter o parsing de HTML, o padrão de
`download_siscan_final.py` é o que funcionou:

```python
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table', {'class': 'tabdados'})   # class canônica do TabNet
if not tables:
    tables = soup.find_all('table')                       # fallback

for table in tables:
    # identifica a tabela certa pelo código SIGTAP no caption
    caption = table.find('td', {'colspan': True})
    if caption and '0201020033' in caption.get_text():
        tbody = table.find('tbody')
        for row in tbody.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) < 2:
                continue
            municipio_text = cols[0].get_text().strip()
            ...
```

Outras classes CSS do TabNet observadas nos scripts: `cabesquerdo` (linha de cabeçalho).

O parsing de números usa separador de milhar brasileiro:

```python
valor = int(valor_str.replace('.', ''))                             # "1.380" -> 1380
# variante em download_siscan_full.py, para valores com decimal:
exames = int(float(valor.replace('.', '').replace(',', '.')))        # "1.380,00" -> 1380
```

Valores ausentes vêm como `-` ou string vazia:

```python
if not valor_str or valor_str in ['-', '']:
    continue
```

**Não replicar** o laço de colunas desses scripts — é a origem do bug de duplicação (§10).

### 7.4 Deduplicação / agregação

Padrão repetido em todos os `download_*` e `expand_*`:

```python
by_key = {}
for item in agregado:
    key = (item['municipio'], item['ano_mes'])
    by_key[key] = by_key.get(key, 0) + item['exames']

agregado_clean = [{'municipio': k[0], 'ano': k[1][:4], 'ano_mes': k[1], 'exames': v}
                  for k, v in sorted(by_key.items())]
```

Somar em `by_key` é exatamente o que transformou dois bugs de coleta em números plausíveis
mas errados. Se a chave já deveria ser única, **detectar colisão e falhar**, não somar.

Bug residual em `expand_sexo.py` (linha 141): `'ano': k[0][:4]` — usa `k[0]`, que é o
*município*, produzindo campo `ano` com as 4 primeiras letras do nome do município. Deveria
ser `k[1][:4]`.

### 7.5 Formato de saída consolidado

Contrato de dados estabilizado nos últimos scripts (`data/siscan_agregado.json`):

```json
[{"municipio": "Recife", "ano": "2026", "ano_mes": "2026-05", "exames": 5610}]
```

E `data/siscan_summary.json`:

```json
{
  "total_exames": 157930, "total_municipios": 15,
  "anos": ["2018", "...", "2026"], "meses_coletados": 16,
  "periodo": "2018-01 a 2026-05",
  "ultima_atualizacao": "2026-07-28T20:55:04.147621Z",
  "fonte": "DATASUS SIA TABNET PE", "estado": "PE",
  "procedimento": "0201020033 (Coleta material colo útero citopatologia)",
  "registros": 240, "nota": "Série mensal real (não agregada)"
}
```

Histórico de dores no `summary.json` (visível nos commits `e71c573`, `05e8683`, `422aa74`):
`jsonlite::write_json` do R serializa escalares como arrays de 1 elemento; a solução final foi
montar o JSON com `sprintf` e `writeLines` em vez de usar a biblioteca.

---

## 8. Automação GitHub Actions

`.github/workflows/update-siscan.yml`, na forma final:

- gatilhos: cron `0 12 15 * *` (dia 15, 12h UTC), `workflow_dispatch`, e `push` em `data/siscan_*.csv`
- `permissions: contents: write` (adicionado no commit `ca7f6ed` — faltava e o push falhava)
- roda `python3 fetch_tabnet_process.py` com `continue-on-error: true`, isto é, **falha silenciosa**
- commita `data/siscan_*.json` se houve diff

Evolução: a versão inicial rodava `fetch_siscan.R` com `microdatasus`. Commits `1f0a0f6`
("adicionar remotes na lista de dependências R") e `b41d157` ("simplificar script R para
evitar problemas de instalação de microdatasus") mostram a batalha; o resultado foi abandonar R
no CI e passar a apenas processar um CSV que alguém subiria à mão.

Com a receita da §5 (POST direto, sem browser), o workflow pode voltar a coletar de fato — não
precisa de R, Playwright, Selenium nem Chromium; só `urllib` da stdlib.

---

## 9. O que falhou e por quê

### 9.1 `paproc.def` não existe (17:36–17:49)

`http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sia/cnv/paproc.def` retorna
`Arquivo DEF não encontrado: sia/cnv/paproc.def`. Essa URL foi usada por 4 scripts e por
`DOWNLOAD_REAL_DATA.md`. O erro só ficou visível porque foi salvo como `data/siscan_raw.csv` —
nenhum script inspecionou o conteúdo, todos tentaram lê-lo como CSV. A resposta HTTP era **200**,
o que derrubou toda verificação baseada em status code.

Lição: TABNET responde 200 para erros de aplicação. Validar o **corpo** (procurar `ERRO:`,
`Arquivo DEF não encontrado`, ausência de `<PRE>`), nunca só o status.

### 9.2 APIs REST inventadas (17:36–17:46)

`api.datasus.gov.br`, `apis.saude.gov.br`, `datasusb.saude.gov.br`, `datasus-mirrors.github.io`.
Cinco URLs que não existem, todas dentro de `try/except: pass`, portanto falhando em silêncio.
Não existe API REST pública do DATASUS/SISCAN.

### 9.3 Bibliotecas com APIs imaginadas (18:03)

`Fetcher(system='SISCOLO').download(state='PE', years=...)` e
`pysus.online_data.SISCOLO().download(state='PE', year=2024)` não correspondem ao contrato real
de `datasus-fetcher` nem de `pysus`. `fetch_siscan_real.py` termina caindo no fallback manual.

### 9.4 Portal de transferência de arquivos (17:53–17:55)

`datasus.saude.gov.br/transferencia-de-arquivos/` serve microdados **DBC**, não CSV tabulado.
Os dois scripts assumiram widgets diferentes para a mesma página — `fetch_siscan_form.py` usou
`select[name="tipo_arquivo"]`, `fetch_siscan_correct.py` usou `input[value="PA"]` — sinal de que
ninguém inspecionou o DOM. Além disso o laço tenta até 20/50 downloads e limita "para teste",
o que jamais cobriria 2018–2026.

### 9.5 Automação de browser por adivinhação de seletor (17:38–18:16)

Padrão comum: listas de seletores candidatos dentro de `try/except: continue`.

```python
export_selectors = ['button:has-text("Exportar")', 'input[value="Exportar"]',
                    'a:has-text("CSV")', 'button[title*="Exportar"]']
```

Nenhum existe no TABNET. O botão certo é `input[value="Mostra"]` e só aparece em
`download_siscan_final.py`. O padrão `try/except: pass` em torno de cada interação faz o script
"terminar com sucesso" tendo configurado zero campos.

### 9.6 `Incremento` nunca configurado (18:14 em diante)

`Incremento="V"` (e `"Valores"`, `"Exames"`) não existem. `fetch_sia_citopatologia.py` e
`download_siscan_full.py` capturavam a exceção e seguiam. Os scripts posteriores desistiram e
forçaram `options[0].selected = true`, ficando no default `Frequencia_______`. Funcionou por
acidente — `Frequencia` retorna valores plausíveis — mas foi escolha involuntária.

### 9.7 `Arquivos` nunca configurado — a falha estrutural (20:21 em diante)

Detalhado em §4.5. Todo script que variava período usava `YYYYMM`; o valor real é
`papeYYMM.dbf`. Consequência: **toda consulta retornou a competência default (Mai/2026)**,
com o rótulo de mês vindo da variável do loop Python. `download_siscan_final.py` chegou a
registrar a suspeita no próprio JSON:

```
"nota": "TABNET mostra período mai/2026. Para histórico completo 2018-2025,
         múltiplas querys necessárias."
```

A suspeita estava certa; o diagnóstico (fazer mais queries) estava errado — faltava
**setar o parâmetro**, não repetir a requisição.

### 9.8 Diagnóstico errado em `ACHADO_DADOS_ESTRANHOS.md` (20:54)

O documento registra corretamente o sintoma (Afrânio 74, Arcoverde 258, Caruaru 80 idênticos
em 2018–2026) e conclui:

> "TABNET não diferencia mês-a-mês — quando você pede 'janeiro/2018', ele retorna dados
> AGREGADOS do período todo."

**Isso é falso.** O TABNET diferencia mês a mês perfeitamente (§5 mostra 85/69/74 para Afrânio
em Jan/Fev/Mar 2026). O problema era o valor do parâmetro `Arquivos`. Como o diagnóstico errou
a causa, a "solução" (`expand_siscan_mensal.py`, queries mensais) reproduziu exatamente o mesmo
defeito — e ainda o piorou, ao introduzir uma duplicata na lista de períodos.

### 9.9 Fabricação de rótulo de ano a partir do índice da coluna

`download_siscan_full.py` e `download_siscan_final.py` chutam o ano pela posição da coluna:

```python
if col_idx == 1: ano = '2026'
elif col_idx == 2: ano = '2025'
elif col_idx == 3: ano = '2024'
```

Metadado inventado. Com `Coluna=Mês_Competen_______` e `formato=prn`, o cabeçalho traz o
rótulo real de cada coluna (`"Jan/2026";"Fev/2026";...`) — basta lê-lo.

---

## 10. Veredito: e o que de fato funciona

### 10.1 Qual tentativa chegou mais perto

**`download_siscan_final.py`** (2026-07-28 20:21). É a única que combina todos os elementos
certos e extrai números reais do TABNET:

- endpoint correto (`tabnet.saude.pe.gov.br/cgi-bin/dh?tab/tabsia08/prodpe.def`);
- `Linha=Munic._Estabelecim` e `Coluna=Ano_Competen_______` válidos;
- `SProcedimento=222` válido, e verificação de que a tabela retornada contém `0201020033`;
- botão de submit correto (`//input[@value="Mostra"]`);
- parsing via `table.tabdados` + BeautifulSoup, com regex de município.

Em segundo lugar, **`fetch_sia_citopatologia.py`** (18:14): descobriu o endpoint e os nomes dos
campos — sem esse script nada depois teria funcionado —, mas dependia de intervenção manual
(`input()` no fim) e usava `Incremento='V'` inválido.

Os `expand_*.py` posteriores **regrediram**: adicionaram dimensões e loops sobre um parâmetro
de período que nunca foi aplicado, gerando volume de dados falsos com aparência de série
temporal.

### 10.2 Os dados versionados são artefatuais — prova

`data/siscan_summary.json` declara 157.930 exames, 15 municípios, 16 meses, 240 registros,
com a nota `"Série mensal real (não agregada)"`. Reconsultando o TABNET hoje para a competência
**Mai/2026** (a default do formulário), `SProcedimento=222`, `Incremento=Frequencia_______`:

| Município | Valor no JSON (todo mês) | TABNET Mai/2026 | Razão |
|---|---|---|---|
| Recife | 5610 | 2805 | 2,0 |
| Olinda | 1380 | 690 | 2,0 |
| Cabo de Santo Agostinho | 542 | 271 | 2,0 |
| Garanhuns | 328 | 164 | 2,0 |
| Jaboatão dos Guararapes | 308 | 154 | 2,0 |
| Arcoverde | 258 | 129 | 2,0 |
| Belém de Maria | 234 | 117 | 2,0 |
| Caruaru | 130 | 65 | 2,0 |
| Gravatá | 130 | 65 | 2,0 |
| Goiana | 98 | 49 | 2,0 |
| Paulista | 80 | 40 | 2,0 |
| Afrânio | 74 | 37 | 2,0 |
| Petrolina | 66 | 33 | 2,0 |
| Moreno | 48 | 24 | 2,0 |
| Camaragibe | 4 | 2 | 2,0 |

**Exatamente 2× para os 15 municípios.** Dois bugs independentes se somam:

1. **Período nunca aplicado** (§4.5/§9.7): todas as 16 "competências" são Mai/2026. Daí a série
   perfeitamente lisa.
2. **Coluna "Total" somada como se fosse dado**: o laço
   `for col_idx in range(1, len(cols))` percorre a coluna de dados **e** a coluna `Total`. Com
   `Coluna=Ano_Competen_______` e uma única competência selecionada, há 1 coluna de dado +
   1 de total, ambas com o mesmo número — daí o fator exato 2×.

Prova adicional do bug 1: `expand_siscan_mensal.py` tem `"202601"` duas vezes na lista
(`("202601","Jun/2026")` e `("202601","Jan/2026")`, linhas 32 e 37). No JSON, `2026-01` de
Afrânio é **148** = 4 × 37 — duas passagens somadas pelo `by_key`. Nada disso seria possível se
o período estivesse sendo aplicado.

Conclusão: `data/siscan_agregado.json`, `data/siscan_summary.json` e todo número exibido no
`dashboard_mestrado.html` **não devem ser usados**. Também não são utilizáveis como valores de
referência: são o dobro do real, para um único mês, com rótulos temporais fabricados, e cobrem
15 municípios de 184.

### 10.3 Checklist para o pipeline novo

1. `POST` em `https://tabnet.saude.pe.gov.br/cgi-bin/tabnet?tab/tabsia08/prodpe.def`,
   corpo `application/x-www-form-urlencoded` em **latin-1**, `formato=prn`, `mostre=Mostra`.
   Sem browser.
2. Resolver `SProcedimento` **dinamicamente**: baixar o formulário, casar o texto da `<option>`
   com o código SIGTAP desejado, usar o `value` encontrado. Não hardcodar `222`.
3. `Arquivos` com valores `papeYYMM.dbf`, um por competência, em lotes de 12–24
   (101 de uma vez estoura o servidor). Enumerar as opções reais do formulário em vez de gerar
   os nomes por regra — o TABNET pode ter lacunas de competência.
4. `Coluna=Mês_Competen_______` para obter uma coluna por mês e **ler o rótulo real do
   cabeçalho**; nunca derivar o mês do índice da coluna nem da variável do loop.
5. **Descartar a coluna `Total`** e as linhas agregadas (`TOTAL`, `Município ignorado - PE`).
6. `Incremento=Qtd.Apresentada____` (declarar explicitamente qual métrica está em uso).
7. Decidir e documentar `Munic._Estabelecim` (faturamento) vs. `Munic_Resid_Pac` (residência).
   Para cobertura populacional, residência.
8. Preservar o **código IBGE de 6 dígitos** junto do nome do município.
9. `decode("latin-1")` e depois `html.unescape()`.
10. Validar o corpo da resposta, não o status HTTP: exigir `<PRE>`, rejeitar
    `Arquivo DEF não encontrado` / `ERRO:`.
11. Reavaliar a escolha de procedimento: `0201020033` cobre 24 municípios em Jan–Mar/2026;
    `0203010019` cobre 45; `0203010060` cobre 0. Um único código não cobre 184 municípios.
12. Teste de sanidade obrigatório antes de publicar: se a variância intramunicipal da série for
    zero, o período não foi aplicado. Esse teste teria evitado todo o retrabalho de 20:21–21:10.

---

## 11. Inventário dos arquivos documentados

Scripts (a serem removidos):

```
Python (17):
  fetch_siscan.py                 17:36   endpoints/APIs inventados
  fetch_siscan_playwright.py      17:38   Playwright em paproc.def
  fetch_siscan_complete.py        17:46   5 estratégias; gerou data/siscan_raw.csv (lixo)
  fetch_siscan_tabnet_portal.py   17:49   www2.datasus.gov.br
  fetch_siscan_form.py            17:53   portal transferência (select)
  fetch_siscan_correct.py         17:55   portal transferência (checkbox)
  fetch_siscan_real.py            18:03   datasus-fetcher / pysus
  fetch_tabnet_process.py         18:05   processa CSV manual (usado no CI)
  fetch_tabnet_simple.py          18:05   lista links do TABNET PE
  fetch_sia_citopatologia.py      18:14   DESCOBERTA do endpoint e dos campos
  download_siscan_full.py         18:16   headless + pandas.read_html
  download_siscan_final.py        20:21   MELHOR TENTATIVA
  download_siscan_historico.py    20:21   loop de períodos (formato errado)
  expand_siscan_full.py           20:30   1 query/ano
  expand_siscan_mensal.py         20:52   1 query/mês (gerou o JSON versionado)
  expand_siscan_completo.py       20:57   multidimensional
  expand_sexo.py                  20:59   sexo M/F

R (2):
  fetch_siscan.R                  17:43   microdatasus SIA-PA + filtro ^0201
  debug_siscan.R                  17:34   inspeção de colunas do SIA-PA

Shell (1):
  fetch_local.sh                  17:21   wrapper de Rscript
```

Markdowns de diagnóstico:

```
SETUP.md                     16:08   assume automação que nunca existiu; descreve dados de exemplo
SETUP_LOCAL.md               17:21   instalação de R + microdatasus
DOWNLOAD_REAL_DATA.md        17:39   instruções manuais com o endpoint paproc.def (errado)
DOWNLOAD_TABNET.md           18:05   instruções manuais via TABNET PE; formato esperado do CSV
DADOS_REAIS.md               18:06   racionaliza o compromisso "download manual + CI processa"
ACHADO_DADOS_ESTRANHOS.md    20:54   sintoma correto, causa-raiz errada (ver §9.8)
```

Artefatos de dados:

```
data/siscan_raw.csv        317 B   HTML de erro em iso-8859-1 (NÃO é CSV) — descartar
data/siscan_agregado.json  24 KB   240 registros artefatuais (2x, mês único) — descartar
data/siscan_summary.json   490 B   metadados dos dados artefatuais — descartar
```

---

*Documento produzido em 2026-08-01 por análise estática dos scripts, do `git log`, dos mtimes
do filesystem e de consultas de verificação ao TABNET PE.*
