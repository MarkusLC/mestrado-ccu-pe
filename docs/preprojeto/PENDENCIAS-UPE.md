# Pendências — submissão PPGSC/FCM/UPE (mestrado profissional)

**Este arquivo é controle interno. NÃO converter para PDF nem anexar à submissão.**
Os arquivos que vão à banca são `SUBMISSAO-UPE.md` (anônima) e `SUBMISSAO-UPE-IDENTIFICADA.md`.

## 1. Decisões que dependem da candidata (marcadores em branco nos arquivos)

| # | Onde | O que preencher |
|---|------|-----------------|
| 1 | `SUBMISSAO-UPE-IDENTIFICADA.md`, campo **Candidata** (linha de sublinhado na capa) | Nome completo conforme documento de identidade. **Não** preencher na versão anônima. |
| 2 | Ambos os arquivos, campo **Linha de pesquisa** (linha de sublinhado na capa) | Denominação da linha conforme o edital e o Anexo I. A ementa vigente deve ser confirmada em `ppgsaudecoletiva.fcm@upe.br` — as páginas do portal retornam conteúdo vazio. Como a indicação de orientador é vedada (item 3.8), a linha é o único instrumento de direcionamento: enviar com o campo em branco desperdiça o direcionamento. |

Nenhum dos dois pode ser preenchido por conjectura.

## 2. Verificações obrigatórias antes de gerar o PDF

3. **Contagem de páginas na prova impressa.** O teto do edital é de **6 páginas em A4, excluída a capa**, e inclui as referências. "Projeto de pesquisa ultrapassou limite de páginas" consta nominalmente entre os indeferimentos do ciclo anterior. A extensão atual (corpo 1.996 + referências 455 = **2.451 palavras**, medidas com `wc -w` sobre o texto sem markup) fica em torno de 5,5 a 6 páginas conforme o renderizador. Conferir **no PDF final**, nunca na contagem do editor. Se estourar, o ajuste é tipográfico (fonte, entrelinha, margens, espaço entre parágrafos), não mais corte de conteúdo — o corte já consumiu 647 palavras.

4. **Geração tipográfica** por Quarto ou LaTeX, com conferência visual dos símbolos `τ2b`, `v_t` e da expressão `log(N/36)` na prova impressa. Nunca colar Markdown em processador de texto.

5. **Metadados do PDF.** Limpar autor, título e produtor no PDF da **versão anônima** — não são visíveis no texto e persistem à exportação. A varredura textual já foi feita e está limpa (ver seção 4).

6. **Norma bibliográfica.** O edital não especifica ABNT ou Vancouver. As 17 entradas estão em ABNT (NBR 6023) com títulos de periódico por extenso. O Modelo de Projeto oficial do PPGSC adota NBR 14724/2024, NBR 6023 e NBR 10520 — indício forte de que ABNT é o esperado. Confirmar com a secretaria.

7. **Revisão profissional de língua portuguesa**, rubrica já prevista no orçamento.

## 3. Registro das alterações desta rodada

- **Natureza do programa corrigida** na capa: mestrado **profissional**, sigla completa PPGSC/FCM/UPE. O enquadramento profissional foi explicitado na §1.2 ("o produto principal é de gestão").
- **Título reescrito**: "Cobertura de exames citopatológicos…" → "**Produção** de exames citopatológicos…", eliminando a contradição frontal com a §3.4 ("Contagem de exames não é cobertura").
- **"Revisão preliminar da literatura" criada como seção nomeada** (§2), exigida pelo item 3.5.k. O conteúdo é o que já existia diluído na introdução — reorganização, não texto novo.
- **Cronograma reancorado** no calendário da UPE: matrícula em dezembro de 2026, aulas a partir de fevereiro de 2027. O anterior usava fevereiro de 2027 como matrícula, que é o calendário da outra instituição.
- **Afirmação sem referência removida**: a "análise nacional de 171.793 óbitos entre 1980 e 2021" e o marcador `[VERIFICAR]` que a acompanhava saíram da §1.1. Nenhuma das referências disponíveis a sustenta; a afirmação foi retirada em vez de receber citação por conjectura. Se a fonte primária for recuperada (autoria, título, periódico, volume, DOI), a frase pode voltar com a citação — é ganho argumentativo, não requisito.
- **Resumo suprimido.** A estrutura do item 3.5.k não prevê resumo, e o teto é de páginas. As palavras-chave foram mantidas na capa.
- **Referência a BROOKS et al. (2017)** removida junto com a citação do pacote `glmmTMB`, por espaço; o pacote segue nomeado no texto.
- **Alíneas de BRASIL corrigidas**: `2022a` → `2022` e `2024a` → `2024`, já que só há homônimos em 2026 (a/b).
- **Entrada órfã resolvida**: a Resolução CIT nº 2/2016 agora é citada como `(BRASIL, 2016)` na §1.3.
- **Extensão**: de 3.098 para 2.451 palavras (corpo + referências), corte de 647.

## 4. Varredura de anonimização — resultado

Executada sobre `SUBMISSAO-UPE.md` com `grep -in`. Termos buscados: fiocruz, IAM, aggeu, magalhães, arca, e nomes de docentes (pauliana, galvão, ulisses, montarroyos, cesse, eduarda, antonio da cruz, gouveia, mendes, paulette, albuquerque, almerice). **Zero ocorrências.** A seção de ética diz "Comitê de Ética em Pesquisa da instituição de vínculo", sem CEP nominal nem e-mails. Não há nome de pessoa na capa nem no corpo. Resta apenas a limpeza de metadados do PDF (item 5).

## 5. Pendências que não bloqueiam a submissão

Atos que suspenderam a apuração do desempenho durante a Emergência de Saúde Pública de Importância Nacional, valores de incentivo por classificação de equipe, séries de repasse do Fundo Nacional de Saúde e classificações do C7 por equipe permanecem no material depositado no repositório.
