# Rastreamento do câncer do colo do útero em Pernambuco

Dados e pipeline de um **estudo ecológico de séries temporais interrompidas** sobre a cobertura de
exames citopatológicos do colo do útero nos municípios de Pernambuco, durante a transição do modelo
de cofinanciamento federal da Atenção Primária: **Previne Brasil → Saúde Brasil 360**.

Painel público: **https://markuslc.github.io/mestrado-ccu-pe/**

## O que está aqui

| Arquivo | Conteúdo |
|---------|----------|
| `pipeline.py` | Coleta e monta o painel município × mês × faixa etária, com denominador populacional |
| `index.html` | Painel de dados, sem dependências externas, consome `data/dashboard.json` |
| `data/dashboard.json` | Agregado que alimenta o painel (24 KB) |
| `data/resumo.json` | Metadados da extração: totais, cobertura, competências |
| `data/populacao_pe.json` | Denominador: população feminina por município, ano e faixa quinquenal |
| `docs/` | Documentação metodológica e histórico técnico |

## Rodar

```bash
python3 -m venv venv && source venv/bin/activate
pip install dbfread
python3 pipeline.py          # baixa o que falta e monta o painel
python3 pipeline.py --check  # só o self-check, sem rede
```

A primeira execução baixa cerca de 240 MB do DATASUS (estimativas populacionais) e leva alguns
minutos. As seguintes reaproveitam o cache em `data/bruto/`, que não é versionado.

Saída: `data/painel_ccu_pe.csv` (340 mil linhas, o painel para análise em R) mais os agregados
versionados.

## Desenho do estudo

- **Delineamento**: ecológico, séries temporais interrompidas em painel de municípios
- **Unidade de análise**: município — 185 unidades de PE, incluindo Fernando de Noronha
- **Janela**: jan/2018 a dez/2026 (108 meses); coleta definitiva em 2027
- **Desfecho**: contagem mensal de exames citopatológicos em mulheres de 25 a 64 anos, por município
  de **residência**
- **Offset**: log(população feminina da faixa ÷ 3) — fator de divisão trienal da Resolução CIT nº 2/2016
- **Modelo**: GLMM binomial negativo (`glmmTMB`), efeitos aleatórios por município, AR1
  intra-município, harmônicos de Fourier

### Marcos temporais modelados

| τ | Competência | Evento |
|---|-------------|--------|
| τ1 | jan/2020 | Previne Brasil — Portaria GM/MS 2.979 de 12/11/2019 |
| τ2 | mar/2020 | Emergência de Saúde Pública, COVID-19 |
| τ3 | mai/2024 | Componente financeiro do Saúde Brasil 360 — Portaria GM/MS 3.493/2024, art. 8º |
| τ4 | mai/2025 | Mensuração do indicador C7 — Portaria GM/MS 6.907/2025 |
| τ5 | mai/2026 | Implantação parcial e assimétrica da qualidade — Portaria GM/MS 10.994/2026 |

τ1 e τ2 estão separados por dois meses e provavelmente não são separáveis empiricamente; a
estratégia declarada a priori é modelá-los como bloco único, com sensibilidade deslocando τ1 para
jan/2019.

## Fontes

| Fonte | Papel | Acesso |
|-------|-------|--------|
| SISCAN | Desfecho | TABNET/DATASUS, `SISCAN/cito_colo_residpe.def`, por POST |
| POPSVS (SVS/MS + IBGE) | Denominador | FTP DATASUS, `/dissemin/publicos/IBGE/POPSVS/` |
| IBGE Localidades | Frame territorial | API de localidades, UF 26 |
| SISCAN mamografia | Série-controle | `SISCAN/mamografia_residpe.def` |

## Três coisas que não são óbvias

**O SIA-SUS não serve como fonte do desfecho.** A distribuição etária da produção de citopatológico
no SIA em PE aloca 43% dos exames em mulheres de 20 a 24 anos e apenas 9% na faixa-alvo de 25 a 64 —
um programa indicado para 25 a 64 anos não produz essa distribuição. O campo de idade está
inutilizável para o recorte que o desfecho exige. Detalhes em
[`docs/ACHADOS_VALIDACAO_SIA.md`](docs/ACHADOS_VALIDACAO_SIA.md).

**Agosto e setembro de 2022 são ausências, não zeros.** O SISCAN não processou dados em nenhuma
unidade da federação em agosto de 2022, e setembro recebeu o transbordo. Nenhuma série real de
rastreamento zera nacionalmente por um mês.

**O TABNET omite a linha do município que zera no estrato.** Sem preencher zeros contra um frame
canônico de 185 códigos, um zero verdadeiro vira ausência e o modelo de contagem enviesa para cima.

## Documentação

- [`docs/ACHADOS_VALIDACAO_SIA.md`](docs/ACHADOS_VALIDACAO_SIA.md) — validação empírica das fontes
- [`docs/HISTORICO_TENTATIVAS.md`](docs/HISTORICO_TENTATIVAS.md) — parâmetros do TABNET e o que deu
  errado no pipeline anterior
- [`docs/pesquisa/`](docs/pesquisa/) — dossiê de literatura auditado e alertas normativos
- [`docs/preprojeto/`](docs/preprojeto/) — pré-projeto de mestrado

## Licença

Dados públicos do DATASUS e do IBGE. Código sob licença MIT.
