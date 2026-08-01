# Pendências e build — versão FIOCRUZ

**Este arquivo NÃO entra no PDF submetido.** Ele é o arquivo irmão de controle de
`SUBMISSAO-FIOCRUZ.md`, que é a única fonte do PDF. Nada daqui deve ser colado no corpo.

---

## 1. Decisões humanas — bloqueiam a submissão

Três informações dependem de decisão ou consulta da candidata e **não podem ser preenchidas por
conjectura**. Duas delas permanecem como marcador `[preencher: …]` no bloco de identificação do
corpo, que é onde a banca espera vê-las preenchidas.

1. **Nome completo da candidata** (linha 3 do corpo). Grafia idêntica à do documento de identidade,
   da inscrição no SIEF e do Lattes.
2. **Orientador(a) pretendido(a)** (linha 11 do corpo). Indicar nome da relação nominal do item 4.4
   do edital vigente. **A omissão é causa de não homologação da inscrição pelo item 7.1.3** — o
   projeto sequer é lido. Além disso, os 1,5 ponto de Viabilidade Operacional do Anexo VII são
   pontuados pela coerência com a linha do orientador proposto. Conferir Lattes e ARCA/Fiocruz e
   contatar o orientador **antes de 31/08/2026**.
   Atenção: Cesse, Mendes e Albuquerque (LABSIS, Lam-Saúde, RIS-AcesSUS — as estruturas mais
   aderentes ao objeto) **não constam** da lista com vaga em 2027, conforme `parte6-editais.md`
   §6.3. A escolha não é trivial e não pode ser feita na véspera.
3. **Frase de aderência à produção do orientador.** Depois de definido o orientador, acrescentar ao
   final do parágrafo "Aderência institucional" (seção 6 do corpo) uma frase citando **dois
   trabalhos concretos** do Lattes dele que dialoguem com avaliação de política de financiamento da
   APS, séries temporais interrompidas ou sistemas de informação em saúde. O parágrafo atual está
   íntegro e submissível sem essa frase — ela é ganho de pontuação, não remendo de lacuna.

## 2. Consultas à secretaria

4. **Norma bibliográfica exigida** — ABNT ou Vancouver. O edital não especifica.
   Consultar `inscricaospacad.iam@fiocruz.br`. As referências estão hoje em **ABNT NBR 6023
   abreviada**, com DOI nos artigos indexados e `Disponível em` / `Acesso em: 1 ago. 2026` na
   literatura cinzenta e nos atos normativos. Se a resposta for Vancouver, converter o bloco
   inteiro.
5. **Anexo VI** — baixar pelo SIEF e conferir se os cabeçalhos são livres ou se é formulário de
   campos fixos. Nesse segundo caso, verter o conteúdo no template oficial em vez de entregar o
   Markdown convertido. `parte6-editais.md` §6.5 item 7 alerta que a extração pública dos anexos vem
   com marca d'água que fragmenta o texto.
6. **Alíneas de BRASIL** — reconferir uma a uma após a padronização definitiva da norma. Hoje o
   corpo usa 2022a, 2024a, 2025a, 2026a e 2026b. Só o par de 2026 tem homônimo real; se a norma
   adotada seguir NBR 6023 à risca, 2022a/2024a/2025a viram 2022/2024/2025 (corrigir corpo e lista
   juntos).

## 3. Verificações de fonte

7. **BRASIL, 2026b — Portaria GM/MS nº 10.994, de 13 de maio de 2026.** É a única fonte que sustenta
   sozinha a Premissa normativa P1, H4 e H5 — ou seja, a correção nº 7 da banca (o C7 nunca carregou
   risco financeiro de perda dentro da janela). Conferir número, data, teor e **vigência** no DOU
   (ed. 89, seção 1, p. 1105, 14 maio 2026) e substituir o localizador genérico
   `https://www.in.gov.br/web/dou` pelo permalink específico da matéria.
   **Se norma posterior tiver alterado a garantia de classificação "bom" até o 1º quadrimestre de
   2026, P1 cai e H2–H4 caem com ela.**
8. **BRASIL, 2016 — Resolução CIT nº 2, de 16 de agosto de 2016.** A entrada foi trocada: antes
   apontava para o Caderno de Diretrizes 2016, que é o **anexo**, não o ato. O corpo cita a
   Resolução em dois pontos (perguntas condutoras e §5.3, offset log(N/36) — correção nº 4 da
   banca), e agora citação e entrada casam. Falta ainda o localizador do ato em si: o URL atual é o
   do Caderno hospedado pela SES-RS. Buscar o texto da Resolução no repositório da CIT/MS e
   substituir, mantendo o Caderno como nota de anexo.
9. **Classificações do C7 por INE no e-Gestor APS.** Condição para operacionalizar o gradiente de
   proximidade ao corte em H4. A hipótese já está redigida de modo a sobreviver à indisponibilidade
   ("gradiente estimável se as classificações … estiverem publicadas"), então isto não bloqueia a
   submissão — mas confirmar antes da qualificação.

## 4. Resolvido nesta rodada (registro)

- **FERRARI et al. (2025) deixou de ser citação órfã.** Os dados bibliográficos foram recuperados
  em fonte primária no dossiê de pesquisa (`docs/pesquisa/raw_14.md` e `parte1-epidemiologia.md`,
  ambos com verificação verbatim registrada em `raw_10.md`): FERRARI, Y. A. C. et al. *Tendência
  secular de mortalidade por câncer do colo do útero no Brasil e regiões*. Ciência & Saúde
  Coletiva, v. 30, n. 3, e09962023, 2025. DOI: 10.1590/1413-81232025303.09962023. A entrada foi
  incluída na lista e o argumento regional do parágrafo de abertura foi preservado inteiro.
- **§5.2, aritmética das competências.** "26 delas pré-interrupção" estava errado: com τ1 em
  jan/2020 e série iniciando em jan/2018, o segmento pré tem **24** competências. Corrigido para 24,
  e o bloco τ1–τ2 foi explicitado como **ancorado em τ1**.
- **Perguntas condutoras no plural**, como pede a rubrica do Anexo VII: a pergunta única foi
  desdobrada em três, correspondentes aos objetivos específicos 2, 3 e 5.
- **Seção 5 renomeada** de "MÉTODOS" para "METODOLOGIA", conforme nomenclatura do Anexo VI.
- **Título**: "Cobertura de exames citopatológicos…" passou a "**Produção** de exames
  citopatológicos…". O título anterior contradizia frontalmente a correção nº 6 da banca, enunciada
  em §5.3 e no resumo ("todo efeito é resposta de produção, não ganho de cobertura").
  **Propagar para `PRE-PROJETO.md` e `SUBMISSAO-UPE.md`**, que carregam o mesmo título.
- **Os sete ajustes da banca foram conferidos um a um após a edição** e permanecem no corpo: v_t e a
  frase das "185 evidências independentes" (§5.4); τ2b como ponto de recuperação epidemiológica e
  não marco normativo (§5.2); τ5 só como mudança de nível, exploratório (§5.2, H4 e objetivo 2);
  offset log(N/36) com a nota do fator de divisão 3 (§5.3); defasagem entre coleta e liberação do
  laudo (§5.3); contagem de exames não é cobertura (§5.3 e resumo); C7 sem risco financeiro de perda
  na janela (§1, P1, H4).

## 5. Extensão — medida, não estimada

Contagem real por `wc -w` sobre o arquivo submissível, com marcação `**` e separadores `---`
removidos:

| Bloco | Palavras |
|---|---|
| Corpo (identificação → cronograma, linhas 1-113) | 3.174 |
| Referências (linhas 115-fim) | 952 |
| **Total** | **4.126** |

Caracteres (sem quebras de linha, sem `**`): **28.062** em 90 blocos.

O total anterior a esta rodada era 3.880 (3.159 + 721). O acréscimo de 246 palavras é **quase
inteiramente localizador**: 21 DOIs e 10 pares `Disponível em` / `Acesso em` exigidos pela NBR 6023
na literatura cinzenta e nos atos normativos, mais a entrada de FERRARI. O corpo cresceu apenas 15
palavras líquidas (as perguntas condutoras adicionais, descontados os três `[VERIFICAR]` removidos).

**Isto é risco de página, e o limite que vincula é de páginas, não de palavras.** O edital fixa 10
páginas em Times New Roman 12, espaçamento 1,5, **incluindo as referências** e sem capa. Com 28.062
caracteres, a ~75 caracteres por linha e ~38 linhas por página, a projeção é de ~11 páginas com 6 pt
de espaço entre parágrafos e ~10 páginas com espaçamento zerado. `parte6-editais.md` §6.2 registra
indeferimento documentado por excesso de páginas no edital irmão da UPE.

**Ordem de corte, se o PDF estourar** (só executar depois de medir o PDF real, nunca antes):

1. **RESUMO inteiro** (~190 palavras). Não é exigido pelo Anexo VI e é o único bloco integralmente
   redundante.
2. **Compressão de §5.6** (componente documental, vieses e reprodutibilidade), preservando as
   correções 5 e 6 da banca.
3. **§5.5** (poder e série-controle), mantendo a menção a `v_t` ativo na simulação — ela é parte da
   correção nº 1.

Não cortar: v_t e a frase das 185 evidências independentes; a nota do fator de divisão 3; a
defasagem do laudo; o parágrafo "Contagem de exames não é cobertura"; a ausência de risco financeiro
no C7. São as sete correções da banca.

## 6. Build do PDF

Fonte única: `docs/preprojeto/SUBMISSAO-FIOCRUZ.md`. Este arquivo (`PENDENCIAS-FIOCRUZ.md`) **não
entra no pipeline** — não incluir em `input-files`, não concatenar, não passar ao Pandoc/Quarto.

```bash
cd docs/preprojeto
pandoc SUBMISSAO-FIOCRUZ.md -o SUBMISSAO-FIOCRUZ.pdf \
  --pdf-engine=xelatex \
  -V mainfont="Times New Roman" -V fontsize=12pt \
  -V geometry:a4paper -V geometry:margin=2.5cm \
  -V linestretch=1.5 -V lang=pt-BR
```

Checklist pós-build, na prova em PDF e não no editor:

- [ ] Contar as páginas. Limite: 10, referências incluídas, sem capa.
- [ ] Conferir a renderização de **τ, δ₃, γ₃, v_t** e da seta **→** do título.
- [ ] Conferir que os dois marcadores `[preencher: …]` do bloco de identificação foram substituídos.
- [ ] Buscar "VERIFICAR", "Pendência" e "Contagem:" no PDF — devem retornar zero ocorrências.
- [ ] Limpar metadados do PDF (autor, título, produtor) se a versão for usada em avaliação cega.
- [ ] Revisão profissional de língua portuguesa antes do envio.
