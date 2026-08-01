# Validação empírica do SIA-SUS (TABNET-PE) como fonte do desfecho

Testes executados em 01/08/2026 contra `tabnet.saude.pe.gov.br/cgi-bin/tabnet?tab/tabsia08/prodpe.def`,
por POST direto (sem navegador), procedimento `0203010019` (exame citopatológico cérvico-vaginal),
incremento `Qtd.Apresentada____`.

Scripts de teste: `scratchpad/teste_residencia.py`, `teste_desfecho.py`, `teste_bpac.py`,
`teste_filtros.py`, `calibra_idade.py`.

## 1. Município de residência resolve o problema de cobertura

A metodologia exige agregação por município de **residência**. O pipeline antigo usava
`Munic._Estabelecim`. A diferença é grande e explica o sintoma de "só 15 municípios":

| Linha | Municípios com exame (jan–mar/2026) | Total |
|-------|-------------------------------------|-------|
| `Munic._Estabelecim` | 43 | 21.830 |
| `Munic_Resid_Pac` | **179** | 21.202 |

Por estabelecimento aparecem apenas os municípios que sediam laboratório de citopatologia — em PE,
algumas dezenas. Por residência aparecem quase todos os 184, que é o painel que o estudo precisa.
Em 2025, `Munic_Resid_Pac` devolveu 186 linhas (inclui a linha `Total` e o código de município
ignorado), com 3,2% da produção sem município de residência identificado.

## 2. O código de procedimento estava errado

| Código | SProcedimento (índice) | Municípios (jan–mar/2026, residência) | Total |
|--------|------------------------|----------------------------------------|-------|
| `0201020033` coleta de material | 222 | 127 | 5.488 |
| `0203010019` exame citopatológico | 766 | **179** | **21.202** |
| `0203010060` | 771 | erro de aplicação | — |

O pipeline antigo usava `0201020033`, que é o **ato de coleta na APS**, não a análise laboratorial.
O exame propriamente dito é `0203010019`, com quatro vezes o volume e cobertura municipal muito maior.
O índice 771 devolve página de erro — o mapeamento posicional herdado do histórico está furado nesse ponto.

Observação: `SProcedimento` usa **índice posicional dentro do `.def`**, não o código SIGTAP. O índice
muda se o `.def` for republicado — é um ponto de fragilidade que precisa de verificação a cada extração.

## 3. A série temporal funciona — o parâmetro de período era o bug

O período é `Arquivos`, multivalorado, com valor `papeYYMM.dbf`. Todos os scripts antigos usaram o
formato `"202601"`, que não existe entre as opções; por isso toda consulta retornava a competência
default e a "série" era a mesma competência repetida.

Com o valor correto, a variação mensal real aparece (mulheres 25–64, residência):

```
2018: 174 municípios · total 9.863
      742 629 1003 1097 1189 790 775 797 554 891 664 732
2025: 178 municípios · total 5.021
      456 492 389 443 459 467 468 497 331 327 187 505
```

`Coluna=Mês_Competen_______` devolve uma coluna por competência em uma única requisição.
A última coluna da resposta é o **Total da linha** e precisa ser descartada — foi contá-la como
dado que fez os valores versionados valerem o dobro do real.

## 4. Correção ao mapeamento do filtro de idade

O `HISTORICO_TENTATIVAS.md` registra a regra `value = idade + 2`. A calibração empírica mostra
**`value = idade + 1`**:

```
SIdade=26 -> "25 anos"      SIdade=42 -> "41 anos"
SIdade=27 -> "26 anos"      SIdade=65 -> "64 anos"
SIdade=66 -> "65 anos"
```

Logo, a faixa 25–64 anos corresponde aos values **26 a 65** (40 valores), e não 26 a 65 pela regra +2.
O intervalo numérico coincide por acidente, mas a regra documentada está errada em um ano.

## 5. Achado que inviabiliza o SIA como fonte do desfecho

A distribuição por idade da produção de `0203010019` em PE, 2025, é biologicamente implausível:

| Faixa | Exames | % |
|-------|--------|---|
| 10–14 | 428 | 0,7 |
| 15–19 | 10.405 | 18,0 |
| **20–24** | **24.615** | **42,6** |
| 25–64 (faixa-alvo do rastreamento) | **5.171** | **9,0** |
| **65–69** | **10.916** | **18,9** |
| 70–74 | 4.242 | 7,3 |
| 75+ | 1.967 | 3,4 |

O rastreamento de CCU no Brasil é indicado para 25 a 64 anos. Uma distribuição em que 43% da produção
recai em 20–24 anos, 19% em 65–69, e apenas 9% na faixa-alvo inteira não descreve um programa de
rastreamento — descreve um campo de idade corrompido. O padrão bimodal, com picos simétricos logo
antes e logo depois da faixa-alvo, sugere erro sistemático de preenchimento ou de conversão do campo
`PA_IDADE` do SIA, não comportamento clínico.

Toda a produção de 2025 está registrada como **BPA-I** (individualizado); não há BPA-C, então a
ausência de identificação do paciente não explica o problema. O campo existe e está preenchido —
está preenchido errado.

### Consequência metodológica

O SIA-SUS via TABNET-PE **não serve como fonte do desfecho primário**. Não por instabilidade de
definição, mas porque a estratificação por faixa etária — que é constitutiva do desfecho — é
inutilizável. Filtrar 25–64 no SIA descartaria 91% da produção sem que se saiba o que se está
descartando.

Isso reforça empiricamente o Ponto-Chave 4 da metodologia (SISCAN como único desfecho inferencial),
por uma razão que o parecer metodológico não previa. O parecer justificava a escolha do SISCAN pela
estabilidade da definição operacional ao longo da janela; acrescenta-se agora que o SIA sequer
permite construir o desfecho tal como definido.

O SIA permanece útil como:
- **validação cruzada de volume total** por município (sem estratificação etária)
- fonte de covariável de oferta, via CNES cruzado com produção laboratorial

## 6. Notas operacionais para o pipeline

- POST direto funciona; Playwright é desnecessário. Corpo `urlencode` em **latin-1** (nomes de campo
  são acentuados), `formato=prn` devolve CSV separado por `;` dentro de `<pre>`.
- **Entidades HTML colidem com o separador**: `&Aacute;guas Belas` contém `;`. É obrigatório aplicar
  `html.unescape()` **antes** do `split(";")`, ou os nomes de municípios acentuados quebram em duas
  colunas e deslocam os valores.
- `Linha=--Não-Ativa--` devolve resultado vazio: não há como pedir o total sem uma linha. Para obter
  totais, agregar a partir de uma linha real.
- O TABNET responde **HTTP 200 em erro de aplicação**, devolvendo página HTML. Qualquer cliente
  precisa validar a presença do bloco `<pre>` antes de aceitar a resposta — foi essa ausência de
  validação que gravou uma página de erro como `data/siscan_raw.csv`.
- Limite prático: até 60 competências por requisição; 101 aborta a resposta. Usar lotes de 12 a 24.
