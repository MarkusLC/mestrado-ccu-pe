# Exploração dos dados — o que aparece quando se olha de outros ângulos

Painel de 339.660 linhas, 185 municípios, 2018-01 a 2026-06. Duas rodadas de exploração
(01/08/2026): a primeira cobriu falsificação e consistência; a segunda cobriu sazonalidade,
estrutura etária, desigualdade entre municípios, recuperação pós-COVID e validade da série-controle.
Cada ângulo da segunda rodada foi submetido a um refutador que reproduziu os cálculos. **Onde
explorador e refutador divergiram, prevalece o refutador**, e a divergência está registrada.

Scripts: `scratchpad/falsificacao.py`, `scratchpad/consistencia.py`, `scratchpad/sazonalidade.py`,
`scratchpad/estrutura_etaria.py`, `scratchpad/desigualdade_completo.py`,
`scratchpad/covid_municipal.py`, `scratchpad/controle.py`, e os scripts de refutação
(`refuta_recuperacao.py`, `refuta2.py`, `ref1.py`–`ref8.py`, `rep2.py`–`rep7.py`, `atk1.py`–`atk7.py`).

A postura das duas rodadas foi procurar **anomalias antes de padrões**. O achado principal continua
sendo negativo, e continua sendo o mais importante do documento.

---

## 1. O teste de falsificação: o estimando primário não se distingue de ruído

A banca apontou a ausência de um teste de falsificação como problema grave. Ele foi feito.

Método: para cada marco, comparar a média da razão de exames nos 12 meses anteriores com a dos 12
posteriores. Depois, fazer exatamente o mesmo em **dez datas-placebo** — competências sem nenhum
evento normativo, distribuídas ao longo da janela. Competências ausentes e provisórias excluídas.

### Marcos reais

| Marco | Competência | Pré | Pós | Δ |
|-------|-------------|-----|-----|---|
| τ1 | jan/2020 | 0,3610 | 0,2195 | **−39,2%** |
| τ2 | mar/2020 | 0,3550 | 0,2060 | **−42,0%** |
| τ2b | jan/2021 | 0,2195 | 0,3347 | **+52,5%** |
| **τ3** | **mai/2024** | 0,4090 | 0,3558 | **−13,0%** |
| τ4 | mai/2025 | 0,3558 | 0,3685 | +3,6% ⚠ |

### Datas-placebo

Dez datas sem evento normativo produziram variações de **+0,4% a +45,3%**, com mediana de
**14,2%** em valor absoluto e desvio-padrão de 19,7 pontos percentuais. Algumas amostras:
set/2019 → −30,8%; jul/2021 → +45,3%; mar/2022 → +14,7%; nov/2024 → −13,4%.

### Veredito

| Marco | Δ | Placebos tão grandes ou maiores | p aproximado | Leitura |
|-------|---|--------------------------------|--------------|---------|
| τ1 | −39,2% | 1 de 10 | 0,18 | limítrofe |
| τ2 | −42,0% | 1 de 10 | 0,18 | limítrofe |
| τ2b | +52,5% | 0 de 10 | 0,09 | distinguível (ver correção abaixo) |
| **τ3** | **−13,0%** | **6 de 10** | **0,64** | **indistinguível de ruído** |
| τ4 | +3,6% ⚠ | 8 de 10 | 0,82 | indistinguível de ruído |

**τ3 é o estimando primário do estudo.** Uma variação de −13% depois de maio de 2024 é menor que a
mediana das variações que datas escolhidas ao acaso produzem nesta série. Seis dos dez placebos
produziram degraus iguais ou maiores.

Só a recuperação pós-pandêmica (τ2b) se destacava. τ1 e τ2 aparecem como limítrofes, mas são
inseparáveis um do outro e o que se mede ali é o choque da pandemia, não o Previne Brasil.

### Três correções que a segunda rodada impôs a esta tabela

**(a) O valor de τ4 está errado por truncamento sazonal, e o sinal se inverte.** A janela pós-τ4
vai de mai/2025 a abr/2026, mas jan–abr/2026 são provisórios e são excluídos. Sobram 8 meses
(mai–dez/2025) comparados contra 12 meses completos. Os meses 5 a 12 rodam sistematicamente acima
da média anual — fator sazonal 1,056 em 2024-25, 1,050 em 2022-23, 1,037 em 2018-19 — contra 0,888
nos meses 1 a 4. O viés é de +5,6%. Com meses casados (mai–dez/2025 contra mai–dez/2024) o degrau
bruto de τ4 é **−5,4%**, não +3,6%. Dois ângulos independentes chegaram ao mesmo número (controle e
desigualdade). τ1, τ2, τ2b e τ3 têm 12 meses de cada lado e não sofrem disso. Aplicada a mesma regra
a τ3, a janela mai–dez pareada dá **−11,3%** em vez de −13,0%.

**(b) O estimador bem especificado dá nulo para todos os cinco marcos, inclusive τ2b.** Estimando o
degrau no gap log(cito) − log(controle) com tendência específica de grupo mais dois harmônicos
(24 meses pré / 12 pós) e construindo a distribuição nula empírica sobre as 65 datas elegíveis:

| Marco | Degrau | Fração das 65 datas com \|degrau\| maior |
|-------|--------|------------------------------------------|
| τ1 | +4,19% | 34% |
| τ2 | +3,69% | 38% |
| τ2b | −4,27% | 32% |
| τ3 | **+0,32%** | **92%** |
| τ4 | +4,83% | 22% (17% excluindo o biênio COVID) |

Nada é distinguível de ruído. **Isto contradiz a leitura de "τ2b distinguível" da primeira rodada** e
a divergência precisa ser reportada: o resultado da primeira rodada usa a série bruta sem tendência
nem sazonalidade e com contagem de excedências contra dez placebos; o segundo modela a deriva e a
sazonalidade e usa randomização sobre 65 datas. O segundo é o teste correto.

**(c) Os dois marcos mais recentes têm pré-tendência contaminada.** Não é ruído genérico:

- **τ3 (mai/2024)** — a quebra regional da Mata Meridional começa em **dez/2023–jan/2024**
  (§2.1), ou seja, **cinco dos doze meses do braço PRÉ já estão colapsados**. Isso não é
  co-intervenção contemporânea (que uma covariável resolveria), é violação da suposição de tendência
  pré-estável.
- **τ4 (mai/2025)** — a razão estadual de jan–abr cai de 0,3488 (2024) para 0,2884 (2025), −17,3%,
  contra −5,4% em mai–dez. Jan/2025 = 0,211 é o mês mais baixo das 102 competências fora do vale da
  COVID. São 13.611 exames a menos no primeiro quadrimestre, 7.795 deles em 12 municípios grandes
  (Jaboatão −1.275, Olinda −873, Caruaru −831, Recife −830, Cabo −779). Um ITS com degrau de nível em
  τ4 ancora o pré nesse buraco e lê o retorno ao normal como efeito positivo do marco.

### O que isto significa, e o que não significa

**Não significa** que o estudo esteja errado ou seja inviável. A comparação da tabela é descritiva e
grosseira. O GLMM proposto controla tendência, sazonalidade e autocorrelação, e tem mais poder.

**Significa** quatro coisas concretas:

1. **O efeito, se existir, é pequeno diante da variabilidade natural da série.** Os dois erros-padrão
   de τ3 estimados na segunda rodada (0,125 e 0,157 em log) põem o nulo confortavelmente dentro do
   intervalo em qualquer especificação.
2. **O teste de falsificação precisa ir para o protocolo, com placebos pré-especificados**, com
   janelas casadas em meses do calendário e com inferência de randomização — não contagem de
   excedências contra zero, e não erro-padrão i.i.d. (§3.2).
3. **A hipótese nula deixa de ser um resultado decepcionante e passa a ser o resultado esperado.**
   Isso é coerente com a cronologia normativa e com o fato, agora estabelecido por caminho
   independente, de que **não existe periodicidade quadrimestral na série** (§2.12): se a gestão
   estivesse otimizando produção contra o ciclo de apuração do C7, o traço mais óbvio seria um pico
   quadrimestral, e ele não está lá.
4. **A análise de poder por simulação deixa de ser formalidade.** Ela precisa dizer qual é a menor
   mudança detectável com 80% de poder, declarada antes da coleta definitiva.

---

## 2. Achados sobre o rastreamento em Pernambuco

Ordenados por relevância. Cada um traz o cálculo e a hipótese de artefato que foi testada contra ele.

### 2.1 O maior evento da série não é a pandemia: a Mata Meridional inteira parou de fazer citologia em dez/2023

Dos 173 municípios elegíveis (≥20 exames/mês em 2022-23), **os 21 da microrregião Mata Meridional
Pernambucana estão todos no grupo do colapso — 100%, sem uma exceção**. No resto do estado, 14 de
152. Fisher exato **p = 4,2 × 10⁻¹⁸**. Não é a cauda inferior de uma distribuição ruidosa; é uma
microrregião apagando junto.

Série mensal agregada da microrregião: nov/2023 = 1.940 → dez/2023 = 1.110 → jan/2024 = 720, e
**nunca mais passa de 1.016**. A datação em "meados de 2024" da versão original é artefato de uma
estatística por município ("último mês ≥50% da própria base"); a quebra é dez/2023–jan/2024.

Grupo ampliado (35 municípios com nível de 2025 abaixo de 40% do de 2022-23; 242.455 mulheres, 8,9%
do estado): média mensal de citopatológicos 2.948 (2022) · 3.052 (2023) · 1.394 (2024) · 474 (2025),
**−84,2%**. Razão de exames do bloco: 0,453 (2023) → 0,070 (2025), contra 0,368 no resto do estado.
Volume perdido: 36.619 (2023) → 5.693 (2025) = **30.926 exames/ano**.

**Não há realocação.** Os outros 150 municípios também caem, de 339.930 (2023) para 303.120 (2025).
Simulação nula (queda uniforme de −12,4% mais ruído de Poisson, 2.000 réplicas): os 35 piores
selecionados ex-post explicariam 12% do degrau de τ3 (IC95 10–16%); o observado é 45%, p < 0,001. A
seleção na cauda não produz o achado.

**O que NÃO sustenta o achado:** o argumento da mamografia, como foi apresentado, não funciona. A
mamografia sobe +25,2% nos 35 municípios, mas sobe +10,6% no resto do estado — a alta é
majoritariamente tendência estadual. Pior, a mamografia praticamente não tem cauda de consolidação
(2026H1 = 10.277/mês contra 10.331/mês em 2025, −0,5%) enquanto o citopatológico cai 13,8% no mesmo
recorte; séries com lag de fechamento tão diferente não se controlam mutuamente contra atraso de
registro. O que sustenta o achado é o padrão 21/21 e o Fisher.

**Há dois eventos empilhados no grupo de 35.** Mata Meridional (21): 1.399 (2019) · 1.891 (2021) ·
1.900 (2022) · 1.891 (2023) — platô, e então queda. Os outros 14: 518 (2019) · 874 (2021) · 1.047
(2022) · 1.160 (2023) — trajetória de alta, e então queda. Fenômenos distintos que o critério de 40%
agregou.

**A explicação concorrente que estes dados não descartam** é migração para outro código de
procedimento SIA/SISCAN fora do painel. Verificação obrigatória: CNES dos laboratórios de
citopatologia que atendiam a microrregião, e se houve descredenciamento ou troca de prestador entre
out/2023 e jan/2024.

### 2.2 O vazio do Sertão do São Francisco: subnotificação geral de ~40%, com supressão adicional específica da citologia

Bloco Petrolina / Cabrobó / Orocó / Santa Maria da Boa Vista / Lagoa Grande / Dormentes / Afrânio /
Parnamirim. Razão anual de citopatológico: 0,047 (2018) · 0,197 · 0,029 · 0,136 · 0,105 · 0,105 ·
0,025 · 0,138 (2025), contra 0,432 · 0,369 · 0,231 · 0,346 · 0,334 · 0,445 · 0,400 · 0,351 no resto
de PE. **Petrolina, 2ª maior população-alvo do estado (113.692 mulheres em 2024), registrou 624
exames no ano inteiro — razão 0,016.**

**Correção importante à versão original.** A afirmação de que "a mamografia dos mesmos municípios
está em nível estadual ou acima" não se sustenta: medida no mesmo grão de bloco, a razão de
mamografia SF/resto é 0,70 · 0,60 · 0,85 · 0,49 · 0,61 · 0,77 · 0,46 · 0,38 nos oito anos —
**abaixo do resto de PE em todos eles, média ~0,61**. O número original vem de escolher 3 dos 8
municípios em 1 dos 8 anos, e mesmo assim 2 dos 3 estão abaixo do estado. Os outros cinco em 2018:
Cabrobó 58,2 · Orocó 53,1 · Afrânio 59,1 · Parnamirim 75,5 · Lagoa Grande 78,8 mamografias/1.000,
contra 144,7 do estado.

Leitura correta: **o bloco subnotifica tudo em ~40% e a citologia em ~76%. O diferencial é de 2,5×**,
não "buraco contra linha de base normal". O contrafactual deve usar a propensão a registrar do
próprio município (mamografia) e não a razão do resto de PE — os ~104 mil exames acumulados de
déficit caem para ~60 mil.

O rótulo geográfico também é falso e o bloco é definido pelo desfecho: Parnamirim não é da VIII GERES
(é da região de Salgueiro), e Terra Nova, que é da VIII GERES, tem razão média 0,752 — o dobro do
estado. Reportar como lista selecionada pelo desfecho, ou usar a composição oficial da GERES e então
explicar Terra Nova.

**Os exames não reaparecem em lugar nenhum.** O déficit anual do bloco (7.405 a 18.939) tem a mesma
ordem de grandeza do excedente do Pajeú (7.669 a 11.490), mas a correlação temporal entre os dois ao
longo dos 8 anos é **−0,15**. Como as somas municipais fecham com o estadual, eles simplesmente não
existem no SIA.

### 2.3 Sessenta e dois municípios estão hoje abaixo do patamar pré-pandemia — 1.094.146 mulheres, 40,4% do estado

O critério original ("nunca alcançou média móvel de 12 meses ≥90% do pré em nenhum momento entre 2020
e 2025") responde à pergunta errada: é um critério de "nunca encostou", e deixa de fora quem encostou
uma vez e depois desabou. Ele devolve 13 municípios e 285.642 mulheres.

Contando **quem está abaixo hoje** (nível médio de 2024-25 contra a base de 2018-19): **62
municípios, 1.094.146 mulheres 25-64, 40,4% do estado**. Só em 2025 são 75 municípios. Os 13 da lista
original são 13 dos 62.

Entre os 49 que faltavam estão os maiores casos operacionais do estado: **Jaboatão dos Guararapes**
(206.364 mulheres, nível 2025 = 0,73), **Caruaru** (119.353, nível 0,73), Petrolina, Abreu e Lima
(0,45), Bezerros (0,68), Escada (0,28), Carpina (0,13), Paudalho (0,14), Salgueiro, Pesqueira.
Escada é o caso didático: figura entre os maiores "superávits" acumulados do estado — porque um pico
de lote de 2.701 exames em ago/2021 inflou o acumulado — e está em razão 0,062 em 2025.

Os 13 da lista original **não** são artefato de base 2018 inflada: refazendo com base = só 2019 (o ano
mais baixo do pré), 12 dos 13 permanecem abaixo de 0,90. O que muda com a base é o tamanho da lista:
62 com base 2018-19, 56 com base 2019.

Os quatro maiores déficits absolutos: Recife 81.106, Olinda 26.327, Jaboatão 15.775, Paulista 18.290.
Os 10 maiores somam 198.953 de 296.566 do déficit bruto = **67%** (não 75%; ver §4, erro de
`min_count`).

### 2.4 Déficit acumulado: robusto na fase aguda (145–176 mil), indeterminado no saldo

Janela 2020-03 a 2025-12, 68 competências observadas. Observado: 1.742.673 exames. Quatro
contrafactuais:

| Contrafactual | Déficit | % |
|---|---|---|
| A — platô da média mensal 2018-19 (27.320) | **+115.056** | 6,2% |
| B — tendência linear ajustada em 2018-19 (slope −35/mês) | +587 | 0,0% |
| C — platô só de 2019 (25.876) | +16.884 | 1,0% |
| D — platô A escalado pelo crescimento da população-alvo | +183.744 | 9,5% |

A **fase aguda** (mar/2020 a dez/2021, 22 meses) é o único número robusto: +164.382 / +145.093 /
+132.620 / +176.481 pelos quatro contrafactuais. Escala: o pico acumulado de +178.635 em jul/2021
equivale a 19,8% de uma meta anual INCA (903.557 exames/ano).

**A narrativa da trajetória não sobrevive à troca de contrafactual.** Sob A: pico +178.635 (jul/2021)
→ +105.627 (dez/2023) → +115.056 (dez/2025), "repagou 36% e voltou a acumular em 2025". Sob C, que é
igualmente defensável: pico +154.092 → +42.104 → +16.884, **"repagou 89% e a dívida é residual"**.
Como o próprio pré não é platô (§4), não há base para preferir A a C. **A frase "voltou a acumular em
2025" é artefato da escolha de base e deve ser retirada.**

O contrafactual B é indefensável: extrapola por seis anos uma queda de −10,0% observada entre 2018 e
2019, que é ela própria uma anomalia não explicada.

### 2.5 Cento e onze de 185 municípios têm ao menos um degrau sustentado de registro — e cinco ligam entre mai e jul/2025

Critério: média dos 6 meses seguintes ÷ média dos 6 anteriores ≥5× ou ≤1/5, com ≥30 exames na janela
e ≥200 na série; um degrau por município. Resultado: **111 municípios**, 62 desligamentos
(−101.868 exames/ano) e 49 ligamentos (+78.744/ano). Distinto dos picos transitórios: aqui o novo
patamar permanece.

**O argumento estatístico original é inválido e foi substituído.** "45 meses distintos para 111
degraus, esperado 1,3/mês sob uniformidade" pressupõe independência entre municípios. Simulando 40
réplicas de um processo com sazonalidade estadual, tendência estadual e ruído NB, **com zero degraus
verdadeiros**, o detector acha 58 degraus e um cluster máximo de 17,9 num único ano-mês (p95 = 22,1)
— maior que os 14 reais de mar/2019. O agrupamento por mês-calendário também é artefato (o nulo
produz 15,3 em março e 14,3 em abril, contra 20 e 24 reais). A estatística de agrupamento é
ininterpretável.

**O que sustenta o mecanismo é o contraste com a mamografia.** Nos 23 municípios dos blocos de
mar-abr/2019, a citologia cai para **12,1%** do patamar anterior (2.931 → 354/mês) enquanto a
mamografia dos mesmos municípios fica em **84,5%** (estado inteiro: 88,5%) e o controle fora-de-faixa
cai igual, para 11,4%. Nos 5 que ligam em mai-jul/2025: citologia 97 → 1.040/mês (10,7×) enquanto a
mamografia **cai**, 222 → 169. É chaveamento de registro específico da citologia.

**Contaminação de τ4:** com todos os municípios, janela mai–dez pareada, 0,3895 → 0,3685 (−5,4%);
excluindo os 5 que ligaram, 0,4065 → 0,3753 (−7,7%). Contribuição de **+2,3 pontos percentuais**. Só
Petrolina já leva a −7,1% (39 exames em jun/2025 → 533, 820, 701, 887, 778, 698, sustentado a
~500/mês). A composição da lista dos cinco não é estável a W: com W=4 saem Cedro e Saloá no lugar de
Flores e Santa Filomena; com W=9 sobram só Cabrobó e Orocó. A direção da correção é estável, a lista
não.

**τ3 é limpo quanto a este mecanismo específico:** −13,0% com todos, −12,5% sem os mesmos 5, −13,2%
sem os 8 (5 + Vitória de Santo Antão, Goiana, Escada). O que contamina τ3 é a Mata Meridional (§2.1),
que é outro evento.

### 2.6 Em 2025 há tantos municípios "vazios" quanto no ano da pandemia

Municípios com razão anual abaixo de 0,1: 17 (2018) · 19 · **34 (2020)** · 7 · 7 · 10 · 13 ·
**33 (2025)**. Em 2020 o volume estadual caiu 46% e havia 34 vazios; em 2025 caiu 19% e há 33. Não é
queda de produção, é colapso de cobertura do registro.

Persistentes ao longo da janela: Triunfo em 8 dos 8 anos (25 exames em 2025 para 4.155 mulheres),
Afrânio 7, Santa Cruz da Baixa Verde 7, Lagoa Grande 7, Santa Maria da Boa Vista 6, Dormentes 6,
Orocó 6, Cabrobó 5, Moreilândia 4, Petrolina 4. Ao todo 63 municípios (23,9% da população-alvo)
têm razão <0,1 em pelo menos um ano.

Isto é o dado que mais compromete usar 2025 como período pós de qualquer marco.

### 2.7 Desigualdade entre municípios: a pandemia elevou o Gini, a recuperação o baixou ao mínimo, e a alta de 2025 é metade registro

Gini de concentração ponderado pela população-alvo (Lorenz: municípios ordenados pela razão, eixo x =
fração acumulada de mulheres 25-64, eixo y = fração acumulada de exames), verificado com duas
implementações independentes:

| 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| 0,2771 | 0,2885 | **0,3367** | 0,3060 | **0,2601** | 0,2903 | 0,2906 | 0,3234 |

A narrativa fácil — "a pandemia aumentou a desigualdade e ela nunca voltou" — é **falsa**. 2022 é o
ano mais equitativo da série de oito anos; a recuperação pós-pandêmica foi igualizadora. A alta de
2025 é um evento posterior e independente.

Bootstrap pareado de 2.000 réplicas: Δ(2025 − 2022) = **+0,0633**, IC95 [+0,0331; +0,0995]. Mas
**metade da alta é município caindo em buraco de registro**: excluindo os 33 municípios com razão
<0,1 no próprio ano, 2022 = 0,2493 e 2025 = 0,2798, **Δ = +0,031**. A direção sobrevive, a magnitude
não. Duas alternativas foram testadas e caem: reprojeção populacional não explica nada (Gini 2025 com
denominador de 2023 = 0,3239) e 2025 não parece truncado (razão de nov/2025 = 0,355 e dez/2025 =
0,358, acima de dez/2024 = 0,310).

A leitura de gestão "quando o sistema cai, cai mais onde já era pior" **não pode ser afirmada**
enquanto metade do efeito for falha administrativa.

Nota metodológica: o Gini **não** ponderado das contagens brutas fica em 0,59–0,70 e é inútil — mede
o tamanho dos municípios (Recife tem 480.781 mulheres, Fernando de Noronha 1.069), não desigualdade
de acesso.

### 2.8 A atividade fora da diretriz encolheu 2,6× mais rápido que a atividade dentro — e 88% do movimento é um só lado

Variação da razão de exames 2019→2025, com denominador específico de cada faixa:

| Fora (jovens) | | Dentro da faixa-alvo 25-64 | | Fora (idosas) | |
|---|---|---|---|---|---|
| 015-019 | −36,8% | 025-029 | −1,3% | 065-069 | −22,9% |
| 020-024 | −26,9% | 030-034 | −10,2% | 070-074 | −36,9% |
| | | 035-039 | −6,5% | 075-079 | −48,0% |
| | | 040-044 | −8,0% | 080-120 | −62,0% |
| | | 045-049 | −7,7% | | |
| | | 050-054 | −5,0% | | |
| | | 055-059 | +0,5% | | |
| | | 060-064 | −0,9% | | |

Dentro do alvo: média −4,9%, maior salto entre faixas adjacentes 8,9 pp. Nas bordas da diretriz:
salto 020-024 → 025-029 = **+25,6 pp**; salto 060-064 → 065-069 = **−22,0 pp**. Ambos ~3× o maior
salto interno.

A geometria sobrevive a tudo que foi jogado nela:

- **Decomposição numerador/denominador:** o salto 24/25 é +28,3 pp de numerador −4,2 pp de
  denominador (denominador só 17%); o salto 64/65 é −27,4 +1,1 (denominador 5%).
- **Teste de descontinuidade honesto:** regredir a variação numa cúbica no ponto médio da idade dá
  R² = 0,866; acrescentar indicador dentro/fora sobe para R² = 0,931, com degrau de **+17,3 pp**
  (+20,8 pp excluindo a faixa aberta 080-120).
- **Mudança de regra de validação do SISCAN — descartada.** O share mensal fora-de-faixa cai numa
  reta de −0,84 pp/ano, R² = 0,947, com dp das primeiras diferenças de 0,42 pp e máximo de 1,49 pp em
  96 meses. Não há degrau em mês nenhum; uma trava de sistema teria produzido salto.
- **Contrafactual demográfico:** congelando a razão de cada faixa em 2019 e movendo só a população, o
  share fora-de-faixa iria de 20,51% para 19,77% — a demografia explica **−0,75 pp dos −5,19 pp
  observados, 14%**. 86% é comportamental.
- **Picos de lote:** excluindo as 36 células município-mês, o salto 24/25 vai de +25,6 para +25,7 pp.
  Zero contaminação.
- **Generalidade municipal:** em 175 municípios com dado utilizável, o salto 24/25 é positivo em 142
  (81%) e o salto 64/65 é negativo em 127 (73%), medianas +20,5 pp e −12,8 pp.

**Três ressalvas que mudam a leitura.**

1. **A simetria é enganosa quanto ao peso.** Decompondo a queda do share fora-de-faixa (20,51% →
   15,32%, −5,19 pp): o lado jovem entrega −4,56 pp (**88%**) e o lado 65+ apenas −0,63 pp (12%). A
   proporção é 7:1. "O sistema convergiu para a diretriz" é, na prática, "o sistema parou de rastrear
   menores de 25".
2. **O ano-base é carga oculta.** "A razão dentro da faixa caiu ~5%" é −5,3% com base 2019 e −15,7%
   com base 2018 — e 2018→2019 sozinho já foi −11,0%, antes de qualquer marco. O salto 24/25 é
   +20,2 pp (base 2018), +25,6 (2019), +20,0 (2021), +15,5 (2022), +8,4 (2023). A versão original
   reporta o máximo da série.
3. **A direção substantiva é ambígua.** "Convergência à diretriz" e "racionamento do rastreamento
   oportunístico" são observacionalmente equivalentes aqui: num sistema que encolhe, a atividade
   discricionária cai primeiro. Formulação agnóstica recomendada: *a atividade fora da diretriz
   encolheu 2,6× mais rápido que a dentro*.

**A hipótese concorrente mais provável não foi testada:** citopatológico em 15-24 no Brasil é
majoritariamente oportunístico em consulta de pré-natal e planejamento familiar, e a fecundidade de
15-24 em PE caiu fortemente na janela. Menos contatos por mulher produz exatamente esta queda sem
nenhuma mudança de conformidade. A população 015-019 caiu só 9,5% enquanto os exames caíram 42,8%,
então não é população — mas *contatos por mulher* não é população. Exige SINASC por faixa etária
materna para ser afastada.

**Correção necessária ao vocabulário de "vale":** 060-064 é a faixa de menor razão do alvo em todos
os oito anos, mas entre 2019 e 2025 seus **exames cresceram +20,0%** enquanto a população cresceu
+21,1%; e 065-069 teve queda de exames de apenas −7,4% com população crescendo +20,0%. A queda das
razões nessas duas faixas é dominada por crescimento populacional de ~20%, não por desmobilização do
serviço. Chamar 060-064 de "faixa desassistida, exatamente onde a mortalidade é maior" inverte o
quadro operacional.

### 2.9 Trinta e sete mil exames por ano em mulheres de 15 a 24 anos — 13,0% do volume acumulado

Em 2025: **37.636 exames citopatológicos em mulheres de 15 a 24 anos** (11.256 em 015-019 e 26.380 em
020-024), faixa em que o rastreamento é contraindicado pelo INCA. Razões de 0,098 e 0,218. Acumulado
2018-2025: 389.293 exames em menores de 25 anos = **13,0% de todos os 2.995.895 citopatológicos da
janela**.

**Dois números da versão original foram refutados e não devem ser usados.**

- **O "96,2% do déficit" é artefato da referência escolhida.** A conta fixa como alvo a faixa mais
  rastreada de 2025 (050-054, razão 0,385) — a única escolha da grade que produz um déficit da ordem
  de 37,6 mil. Variando a referência: 2ª maior (0,360) → cobertura 190%; mediana do alvo (0,345) →
  319%; média (0,341) → 369%; nível médio de 2019 (0,360) → 194%; referência 0,40 → 71,5%; 0,45 →
  38,5%; 0,50 → 26,3%; **meta INCA 1,0 → 6,3%**. O intervalo vai de 6% a 369%. É numerologia.
- **Os "18,4% fora da diretriz" misturam estatutos normativos diferentes.** Dos 550.177 exames,
  389.293 (13,0%) são <25 — contraindicação dura. Mas 160.884 (5,4%) são 65+, e o INCA encerra o
  rastreamento aos 64 **somente** para mulheres com dois exames normais consecutivos nos últimos
  cinco anos. Sem dado de histórico — que este painel não tem — chamar os 5,4% de "fora da diretriz"
  é errado. "Quase um em cada cinco" vira **"um em cada oito"**.

A falsificação séria continua não testável nestes arquivos: os exames em <25 podem ser seguimento ou
investigação de sintoma. As três tabulações de qualidade de `dashboard.json` cobrem apenas a faixa
25-64 (confirmado: somam exatamente ao painel 25-64 em 8 dos 9 anos). Extrair `motivo do exame`
estratificado por faixa no TABNET é pré-requisito para levar o número à gestão.

### 2.10 O seguimento colapsou em 2020 e nunca voltou, enquanto o rastreamento voltou a superar 2018

Tabulação `motivo` do `dashboard.json` (faixa 25-64), índice base 2018 = 100:

| Motivo | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| Rastreamento | 100 | 89,8 | 55,7 | 86,1 | 92,7 | **111,1** | 99,3 | 90,7 |
| Seguimento | 100 | 97,9 | 40,7 | 49,1 | 40,8 | 42,4 | 41,5 | **46,3** |
| Repetição por exame alterado | 100 | 69,6 | 27,3 | 44,4 | 36,2 | 59,7 | **105,5** | 70,9 |

Em absoluto, o seguimento cai de 9.286 (2018) para 3.776 (2020) e fica entre 3.786 e 4.303 até 2025 —
nunca passa de 47% do patamar pré-pandemia, num período em que o rastreamento chegou a 111% dele. A
participação do seguimento no total despenca de 2,69% (2018) para 1,05% (2023) e 1,39% (2025).

**A hipótese de artefato de preenchimento fica enfraquecida com o dado disponível**, por um teste
discriminante que a versão original não rodou: se o campo `motivo` tivesse passado a marcar
"Rastreamento" por padrão a partir de 2020, teria matado as duas categorias igualmente. Matou uma e
poupou a outra — **a Repetição recuperou acima de 2018 em 2024** (909 exames contra 862). Além disso,
`motivo` não tem categoria "Ignorado" e as três somam exatamente o total do painel em 8 dos 9 anos,
então não há resíduo de não-preenchimento onde um campo abandonado se esconderia (por contraste,
`interv_coleta` tem "Ignorado", e ele vale 0 em todos os anos exceto 3 em 2020).

Os outros dois testes continuam impossíveis com estes arquivos, porque as tabulações de qualidade só
existem no agregado estadual: (a) verificar se a queda é simultânea em todos os municípios e
laboratórios — mudança de sistema é simultânea, mudança assistencial é escalonada; (b) cruzar com o
número de exames alterados do período.

Se for real, é mais grave que qualquer coisa que o estimando primário mede: seguimento de lesão
detectada é o elo que efetivamente previne câncer invasivo, e rastrear mais enquanto se acompanha
menos piora o desfecho mesmo com a razão de exames subindo. É o exemplo mais forte do alerta
"contagem de exames não é cobertura".

### 2.11 Janeiro é o mês mais baixo do ano (−20,0%), e o efeito é monótono na idade

No perfil sazonal com efeito fixo de ano, anos não-COVID, janeiro é **−20,0%** — o menor dos doze
meses, contra fevereiro −16,4% e outubro +14,4%. F(mês) = 6,22, p = 1,9 × 10⁻⁶. E **não é dia útil**:
janeiro tem 21,6 dias úteis, acima da média mensal de 20,9; controlando por log(dias úteis) o efeito
piora para −23,0%. O contraste com fevereiro fecha o argumento: fevereiro tem 18,7 dias úteis e seu
efeito sobe de −16,4% para −9,2% ao controlar — fevereiro é quase inteiramente calendário, janeiro
não é nada.

A hipótese de arraste de virada de ano (janeiro inflado por lançamento retroativo de dezembro) está
**refutada na direção oposta**: a razão janeiro/dezembro-anterior é 0,846 · 0,853 · 0,808 · 0,819 ·
0,846 · 0,755 · 0,685 nos anos de 2019 a 2025 — todos abaixo de 0,86, média 0,802. Não há acúmulo
empurrado para janeiro; há uma parada.

**Duas afirmações da versão original caem.**

*"Está se aprofundando"* — refutado. A razão jan/dez-anterior é a estatística errada: mistura
numerador e denominador e inclui três pares que cruzam a pandemia. Decompondo, o desvio de janeiro em
relação ao nível do próprio ano tem tendência −0,0348 log/ano (p = 0,176) e o de dezembro −0,0180
(p = 0,409); nenhum é significativo, e o p = 0,030 da razão nasce de somar dois ruídos. O teste
correto — interação mês × tendência linear, anos não-COVID — dá janeiro −0,0332 log/ano com
**p = 0,066**, o menor dos doze meses, mas junho dá +0,0319 com p = 0,078 na direção oposta, e
**Bonferroni sobre 12 testes leva o menor p a 0,787**. Leave-one-out: tirando 2025, a tendência cai
para −0,0132/ano com p = 0,145. Toda a significância mora num único ano.

*"É parada do processamento laboratorial"* — contrariado pelo gradiente etário, que nunca fora
testado apesar de os dados terem 14 faixas prontas. Coeficiente de janeiro, faixa a faixa:

| 015-019 | 020-024 | 025-029 | 030-034 | 035-039 | 040-044 | 045-049 |
|---|---|---|---|---|---|---|
| −20,1% | −19,9% | −22,6% | −20,6% | −20,7% | −19,7% | −20,3% |

| 050-054 | 055-059 | 060-064 | 065-069 | 070-074 | 075-079 | 080-120 |
|---|---|---|---|---|---|---|
| −18,9% | −18,1% | −17,5% | −16,8% | −9,1% | **−5,4%** | −9,3% |

Spearman idade × efeito de janeiro **rho = 0,864, p = 0,0001**. Fevereiro faz o contrário (−12,3% nas
jovens, −19,4% em 60-64), então não é escala. O mesmo laboratório processa todas as lâminas; um
gradiente de 17 pontos entre 25-29 e 75-79 não sai de parada de processamento. Isso responde, de
passagem, a pergunta que a primeira rodada deixou aberta sobre faixas jovens e idosas terem dinâmicas
opostas: elas não têm — mas o efeito de janeiro **é** monótono na idade.

**E nov/2024 a mar/2025 é uma depressão de cinco meses, não um janeiro.** Desvio de cada mês em
relação ao nível do próprio ano: nov/2024 −5%, dez/2024 −17%, jan/2025 −37%, fev/2025 −10%, mar/2025
−23%, contra out/2024 +17% e abr/2025 +13%. Dez/2024 é o dezembro mais baixo da série (os outros: +2,
+8, +21, +11, −7, +7) e mar/2025 o março mais baixo (−1, −9, +3, +5, +2, +4). Goiana é um pedaço
identificável: 164 / 98 / 20 / 13 exames de out/2024 a jan/2025 e depois 3.089 em fev/2025, num
município que roda 200-450/mês. Ajustar um dummy mensal a isso é ler quebra de nível como
sazonalidade.

### 2.12 Sazonalidade: dois harmônicos bastam, não há ciclo quadrimestral, e o Outubro Rosa só aparece na mamografia

**Perfil mensal** (log-exames com efeito fixo de ano, anos não-COVID, n = 70; o efeito fixo remove
tendência sem absorver sazonalidade — uma spline de 8 nós engole o sinal e derruba F(mês) de 6,22
para 1,70):

| jan | fev | mar | abr | mai | jun | jul | ago | set | out | nov | dez |
|---|---|---|---|---|---|---|---|---|---|---|---|
| −20,0% | −16,4% | −4,5% | +4,9% | +9,0% | −2,8% | −4,1% | +9,5% | +8,1% | +14,4% | +8,6% | −0,1% |

Amplitude pico-vale 43,1%. F(mês) = 6,22, p = 1,9 × 10⁻⁶.

**Não existe periodicidade quadrimestral.** Este é o teste que a primeira rodada pediu, e o resultado
é negativo por quatro caminhos independentes:

- Na janela limpa 2022-2025, a frequência de 3 ciclos/ano responde por **1,47% da potência espectral,
  rank 14 de 24**. Bootstrap paramétrico de 4.000 réplicas sob a nula de K=2 harmônicos estáveis mais
  AR(1) — portanto com sinal quadrimestral exatamente zero por construção — dá mediana 1,38% e IC90%
  0,11–6,07%. O observado cai praticamente na mediana do nulo: **p = 0,479**.
- Dummies de fim de quadrimestre, com as três defasagens declaradas: abr/ago/dez **+6,1%** (p =
  0,152); mai/set/jan −3,1% (p = 0,456); jun/out/fev −2,8% (p = 0,487). Nenhum sobrevive. E o +6,1%
  vem inteiro de agosto (abr +4,9%, ago +9,5%, **dez −0,1%**) — dezembro, mês de fechamento do
  terceiro quadrimestre, é um dos mais baixos do ano. Um ciclo de apuração genuíno não pularia
  dezembro.
- **Desenho pré/pós-Previne, que é o teste com o desenho correto** e não estava na versão original:
  pré-Previne (2018-2019) dá abr/ago/dez +5,1% (p = 0,448); pós-Previne (2022-2025) dá +6,7%
  (p = 0,231). O DiD é **+1,6 pp**. A elevação de fim de quadrimestre já existia dois anos antes de
  existir quadrimestre.
- Bloco F do harmônico k=3, nulo em toda janela: 2018-2025 F = 1,84 p = 0,168; 2020-2025 F = 0,55
  p = 0,582; 2022-2025 F = 1,39 p = 0,261. Amplitude do k=3 no perfil estadual: **3,7%**.
- Robustez aos picos de lote: substituindo cada pico pela mediana vizinha, a potência quadrimestral
  fica em 0,6% com e sem.

⚠ **Correção a um erro da versão original.** O teste municipal reportava "fases uniformemente
distribuídas (Rayleigh R = 0,028, p = 0,888)" como evidência positiva. O número está errado (provável
bug de unidade ao reaproveitar a convenção do k=1 num harmônico de período 4 meses). Refeito: R =
0,388, Z = 23,79 (2018-2025) e R = 0,454, Z = 34,02 (2022-2025), **p < 10⁻¹⁰ nas duas janelas — as
fases estão fortemente alinhadas**, e a fase média coloca os picos nos meses 4,5 / 8,5 / 12,5
(municipal) e 4,8 / 8,8 / 12,8 (estadual): abril, agosto e dezembro, com meio mês de atraso. Isso
**não** ressuscita a hipótese — com amplitude de 3,7% e detecção no acaso (6–8% de municípios
significativos contra 5% esperados), o alinhamento é explicado por vazamento do formato anual
não-senoidal para dentro do k=3 num modelo que só ajusta K=2. Mas a afirmação de uniformidade tem de
sair do texto: quem refizer o teste encontra picos em abr/ago/dez.

**Quantos harmônicos.** Anos completos não-COVID (n = 60): K=1 AIC −66,0 BIC −51,3; **K=2 AIC −87,3
BIC −68,5**; K=3 AIC −85,7 BIC −62,6. AIC e BIC concordam em K=2; k=3 acrescenta F = 0,98 p = 0,381,
e k=4 a k=6 nada. Falta de ajuste de K=2 contra o modelo saturado de 11 dummies: F = 0,87, gl(7,44),
p = 0,541 — indistinguível do saturado. Sob binomial negativa o AIC também escolhe K=2 (1165,8 /
1138,9 / 1140,7 / 1143,4 para K=1..4), então não é artefato do OLS em log. Resíduos de K=2 ainda têm
autocorrelação (Ljung-Box lag 6 p = 0,022): o que falta ao modelo é um termo AR(1) (rho 0,11 na
janela limpa, 0,31 na não-COVID inteira), não mais harmônicos.

⚠ **"O segundo par é o dominante" está refutado.** O F = 13,39 contra F = 8,31 é artefato do teste
sequencial (cada par testado contra o MSE do modelo em que entrou). Testando os dois contra o mesmo
modelo cheio: k=1 F = 12,19, k=2 F = 13,39 — empate; amplitudes ajustadas |k=1| = 0,0984 e |k=2| =
0,1031, razão 1,05. E a razão só passa de 1 na amostra empilhada: 0,83 em 2018-2019 e 0,94 em
2023-2025, com o harmônico **anual** dominando nos dois. A razão >1 no pool é assinatura de atenuação
do anual por deriva de fase entre períodos. O argumento espectral também não é estável: 2022-2025 dá
semestral 32,7% contra anual 19,6%, mas essa janela contém ago/set-2022 preenchidos por interpolação
errada (§4); em 2023-2025, sem nenhum mês interpolado, a ordem se inverte — **anual 35,4%, semestral
29,7%**; em 2018-2019, anual 11,1% e semestral 21,5%.

**A sazonalidade do desfecho é indistinguível da do controle.** Perfis com efeito fixo de ano, anos
não-COVID: jan −20,0 vs −18,1; fev −16,4 vs −15,2; mai +9,0 vs +9,0; ago +9,5 vs +9,2; out +14,4 vs
+12,0; dez −0,1 vs −2,3. Correlação dos doze pontos r = 0,9937; teste F de interação mês × série
F = 0,06, gl(11,106), p = 1,00. **Isso não é evidência de igualdade** — um F de 0,06 está 16 vezes
abaixo do esperado sob a nula, e partindo o próprio desfecho ao meio (25-29 contra 30-64) o mesmo
teste dá F = 0,34, p = 0,976: o controle agregado sai mais parecido com o desfecho do que o desfecho
é consigo mesmo. F = 0,06 é o que a estatística faz quando as duas séries compartilham choque de
registro e o resíduo comum infla o denominador. Desagregando por faixa, cada banda isolada dá F entre
0,51 e 1,51 — valores ordinários (15-19 F = 0,74; 20-24 F = 0,51; 65-69 F = 1,35; 70-74 F = 1,51;
75+ F = 1,31). O controle agregado é dominado por 20-24 (272.982 de 571.866 exames, 48%).

**A mamografia, sim, difere:** F = 4,15, gl(11,106), p = 4,3 × 10⁻⁵, correlação r = 0,628, com
outubro **+44,4%** e novembro +27,1% — a assinatura do Outubro Rosa. No citopatológico outubro é
+14,4% e o controle tem +12,0% no mesmo mês: é o mesmo outubro de todo mundo, não campanha. Quando
existe campanha, ela aparece com +44% num mês; no citopatológico não aparece nada parecido.

**Estabilidade da amplitude: não se sabe, e com 70 meses não dá para saber.** Dois testes formais não
rejeitam — desenho balanceado 2018-19 contra 2023-25 F(mês × período) = 1,03, gl(11,33), p = 0,444; e
interação Fourier × tempo F = 1,51, gl(4,58), p = 0,211. Mas os pontos se movem: dezembro −10,7 pp,
novembro −11,1 pp, maio +16,1 pp, junho +16,3 pp, correlação entre perfis 0,66, e a amplitude
pico-vale **vai de 37,0% para 55,2%** (cresce, não encolhe). Três indícios fracos independentes
apontam para deriva de fase: a concentração espectral em f=1 é 0,536 contra mediana 0,827 no
bootstrap (p = 0,044); a razão |k=2|/|k=1| é 0,83 / 0,94 / 1,05 por janela; e o teste balanceado tem
só ~6 observações por mês do ano. **Não se pode declarar a suposição validada porque p = 0,21.**

### 2.13 Um harmônico único para os 185 municípios é restrição forte — e não é ruído de Poisson

Ajustando K=2 mais tendência quadrática em cada município, apenas **34%** têm o bloco de quatro
termos de Fourier significativo a 5%. As fases estão alinhadas no agregado (Rayleigh R = 0,42,
p = 3,4 × 10⁻¹²), mas a dispersão é larga: P10-P90 do mês de pico vai de 2,1 a 10,4 — de fevereiro a
outubro.

O confundidor óbvio — municípios pequenos têm contagem baixa, e ruído de Poisson sozinho produz baixa
detectabilidade e fases aleatórias — **foi testado e não explica**:

| Corte de volume | n | % significativos | Pico P10-P90 | Rayleigh R |
|---|---|---|---|---|
| ≥ 3.000 | 130 | 34% | 2,1 – 10,4 | 0,42 |
| ≥ 10.000 | 37 | 35% | 4,3 – 10,9 | 0,49 |
| ≥ 20.000 | 17 | 35% | 3,9 – 10,6 | 0,43 |
| ≥ 50.000 | 6 | 67% | 7,4 – 10,2 | 0,77 |

A proporção de significativos é 34-35% e não se move em três ordens de corte; a dispersão de fase
continua cobrindo de abril a outubro nos municípios com mais de 20 mil exames acumulados. Só no corte
de 50 mil, com n = 6 (Recife e mais cinco), ela encolhe. A amplitude mediana **cai** com o volume
(21% → 20% → 14%), que é a assinatura esperada de ruído inflando amplitude nos pequenos — mas a
detectabilidade não melhora, e é isso que importa. **A heterogeneidade é real.**

### 2.14 O choque de 2020 foi universal; a recuperação é que separou — e não separou por idade

Vale das três séries: cito 1.576 em jun/2020 (−94,2% da base pré), controle fora-faixa 405 em jun/2020
(−94,3%), mamografia 430 em abr/2020 (−96,1%). Município a município, a mediana de abr-jul/2020 é
−86,5%, o p95 é −61,9%, e **183 de 185 caíram ≥50%**; 11 municípios registraram zero exames em
abr+mai+jun/2020 somados. Os dois "resilientes" (Exu e Santa Cruz) são artefato de sub-registro no
pré: bases de 3,7 e 11,6 exames/mês, razões pré de 0,016 e 0,043, e níveis posteriores de 39× e 5,5×
o "pré". **Não houve resiliência municipal em 2020.**

**Uniformidade por faixa, medida no fundo do choque** (abr-jul/2020 contra abr-jul/2019): dentro do
alvo as quedas vão de −79,6% (025-029) a −82,1% (060-064) — amplitude de **2,5 pp em oito faixas**; e
fora do alvo, de −82,2% a −84,1%. No agregado anual a amplitude é 2,9 pp. A regressão da queda no
ponto médio da faixa dá coeficiente +0,042 pp por ano de idade, R² = 0,25. **Não há iniquidade etária
escondida no agregado.**

Foi a **recuperação** que separou, e separou por conformidade à diretriz, não por idade: em 2023 vs
2019, todas as oito faixas-alvo acima de 2019 (+13,5% a +22,6%), enquanto fora do alvo nenhuma voltou
exceto 065-069 (+4,0%): 015-019 −7,1%, 070-074 −6,8%, 075-079 −20,4%, 080-120 −26,6%. Ressalva: a
monotonicidade "na distância à diretriz" não é estrita — 015-019 (−44,4%) cai mais que 070-074
(−43,2%), que está mais longe. É quase-monótona dentro de cada lado, não através deles.

⚠ **"Puro choque de oferta, sem componente de demanda" não se sustenta como inferência.** O argumento
compara mínimos em meses diferentes (cito jun/2020, mamografia abr/2020) — mês a mês a mamografia
lidera: mar/2020 mamo −40,8% contra cito −21,3%; abr/2020 mamo −96,1% contra cito −70,9%. Isso é a
assinatura do lag de liberação do laudo, não de choque diferencial. E a inferência pressupõe que
existe uma série exposta só à demanda; não existe nenhuma aqui. Em lockdown, as três sofrem
simultaneamente choque de oferta e de demanda. Formulação honesta: *o colapso é universal e
simultâneo nas três séries; estes dados não permitem separar oferta de demanda*.

⚠ **O "gradiente etário da recuperação" está refutado — é composição do denominador.** Variação de
2025 contra a média de 2018-19:

| Faixa | Contagem | pop_alvo | **Razão** |
|---|---|---|---|
| 025-029 | −10,6% | −2,2% | **−8,6%** |
| 030-034 | −20,2% | −5,9% | −15,3% |
| 035-039 | −14,8% | −2,9% | −12,2% |
| 040-044 | −5,3% | +9,0% | −13,1% |
| 045-049 | −0,2% | +14,0% | −12,5% |
| 050-054 | −1,1% | +10,0% | −10,1% |
| 055-059 | +9,6% | +14,0% | −3,8% |
| 060-064 | +13,8% | +23,0% | −7,5% |

O gradiente monotônico da coluna de contagem é a coluna de pop_alvo. Normalizado, **não há
gradiente**: todas as faixas caem entre −3,8% e −15,3%, e a mais jovem cai menos que quatro das mais
velhas. "As mulheres mais velhas do alvo voltaram, as mais jovens não" está invertido em termos per
capita.

### 2.15 Municípios pequenos rastreiam mais, e o gradiente não é instabilidade de denominador

Razão **ponderada pela população** dentro de cada quintil de porte (2023-2025) — a medida imune ao
argumento de números pequenos, que a versão original não usou: **0,582 → 0,493 → 0,469 → 0,413 →
0,346**, monotônica. Médias não ponderadas por quintil: Q1 (mediana 2.450 mulheres) 0,609 · Q2 0,496
· Q3 0,475 · Q4 0,412 · Q5 (24.126) 0,422. Spearman porte × razão em 2025: rho = −0,174, p = 0,018.

Testes contra artefato, todos negativos:

- **Instabilidade de contagem:** o CV temporal intramunicipal (2023-2025) é praticamente plano entre
  quintis — 0,221 · 0,197 · 0,209 · 0,187 · 0,184. Variação de 20%, insuficiente para gerar um
  gradiente de 1,6× nas médias.
- **Seleção por crescimento:** quintis definidos pela população de 2018 dão o mesmo (0,614 · 0,504 ·
  0,455 · 0,418 · 0,422).
- **Deriva de denominador:** a pop-alvo cresce 3,8% (Q1) a 8,1% (Q3) entre 2018 e 2025, ordens de
  grandeza abaixo do gradiente.

Excluindo os 63 municípios com razão <0,1 em algum ano, o gradiente **fortalece** (rho = −0,413,
p = 2,3 × 10⁻⁶, n = 122). Ressalva: essa exclusão é pelo desfecho e corta a cauda inferior, então a
afirmação de que "os buracos de registro estavam atenuando o gradiente" não é evidência limpa. O
gradiente é real; a demonstração não.

**A hipótese que pode derrubá-lo continua não testável nestes dados:** o denominador do estudo é
população total feminina, não população SUS-dependente. Recife tem ~30% de cobertura suplementar,
municípios do Sertão <5%. A conta grosseira sugere que o gradiente encolheria de 1,63 para ~1,19 (ou
seja, ~70% explicado) se o denominador fosse corrigido. É um join público por `cod_ibge` (TABNET/ANS)
e vale a pena.

### 2.16 Razão acima de 1,0: sobrerrastreamento persistente em cinco a sete municípios, e um bloco regional que faz o dobro do estado

Trinta e nove município-anos com razão >1,0, em 18 municípios distintos: 3 (2018) · 2 · 0 · 6 · 2 ·
**13 (2023)** · 8 · 5 (2025). Em 2025 somam 5,9% dos exames do estado com 2,4% da população-alvo.

**Não é instabilidade de denominador pequeno nem despejo retroativo** — o teste caso a caso, que a
versão original deixou em aberto, é inequívoco:

| Município | 2023 | 2024 | 2025 |
|---|---|---|---|
| Brejão | 1,35 | 1,06 | 1,34 |
| Ingazeira | 1,44 | 1,19 | 1,25 |
| Terezinha | 1,44 | 1,16 | 1,22 |
| Carnaíba | 1,20 | 1,24 | 1,13 |
| Machados | 0,97 | 1,10 | 1,02 |

Três anos consecutivos acima de 1,0 não é ruído: um lote inflaria um ano e deprimiria os vizinhos. Na
média trienal são 7 municípios, não 5. Em termos crus, esses municípios fazem entre 0,341 e 0,448
exames por mulher 25-64 por ano — intervalo efetivo de 2,2 a 2,9 anos em vez dos 3 preconizados.
Plausível operacionalmente (ESF com cobertura alta chamando anualmente), e é **sobrerrastreamento**,
que é problema de qualidade, não meta atingida.

**A hipótese de "mulheres de municípios vizinhos" está falsificada no nível do bloco.** Agregando os
19 municípios do Sertão do Pajeú (98.892 mulheres, incluindo os três mais vazios do estado — Triunfo
0,018, Calumbi 0,021, Santa Cruz da Baixa Verde 0,025), o bloco inteiro tem razão **0,656** em 2025
contra 0,330 no resto de PE. Se fosse redistribuição interna, fecharia no nível estadual; fecha ao
dobro. Robusto à composição da lista: microrregião IBGE sem Betânia e Carnaubeira 0,678; sem Serra
Talhada 0,635. Resta a hipótese de fluxo interestadual (Itapetim, Tuparetama e São José do Egito
fazem divisa com a Paraíba), não testável com estes dados.

Duas ressalvas. **(a)** 13 dos 39 município-anos caem em 2023, o ano de razão estadual máxima, e a
contagem de >1,0 acompanha a razão estadual (corr = 0,579), com 0 casos em 2020 — o limiar de 1,0 é
em parte um efeito de ano. **(b)** Machados e Vertente do Lério aparecem simultaneamente na lista de
desligamentos de mar/2019 (§2.5) e aqui como sobrerrastreamento. A mesma série não pode ser
"disponibilidade de registro" num achado e "atividade assistencial" no outro; municípios que aparecem
nas duas listas devem sair desta.

O teste da hipótese de "indicação frouxa" (rastrear fora da faixa e registrar dentro) está mal
especificado na versão original: compara **participação** de exames fora da faixa (15,76% nos 18
contra 16,47% do estado), não a **taxa** por mulher. Num município que rastreia o dobro, a
participação pode ficar igual com a taxa fora da faixa dobrada. Refazer com taxa por 1.000 mulheres
15-24 e 65+.

### 2.17 Diferença de 6,5× entre regiões contíguas, e ninguém sabe por quê

Sertão do Pajeú 0,656 contra Sertão do São Francisco ~0,10 em 2025 — **6,5×** entre blocos
geograficamente vizinhos, sem nenhum marco normativo da janela que chegue perto de explicar. E o
déficit do São Francisco não reaparece no Pajeú (correlação temporal −0,15). É o achado mais
acionável do painel e o que mais claramente aponta para infraestrutura de registro/laboratório, não
para política.

Complemento do lado metropolitano: o déficit acumulado da RMR é **+141.786 (17,6%)** contra
superávit de −26.731 (−2,5%) no interior. O interior já estava acima do pré em 2021 (+2,1%) e a RMR
ainda estava −27,1%. O achado é robusto à base: com base = só 2019, RMR ainda +102.825 (+13,4%) e o
superávit do interior **aumenta** para −85.942 (−8,6%) — mais robusto que o déficit estadual, que
despenca de +115.056 para +16.884 na mesma troca. Hipótese de migração para Recife descartada: Recife
é o maior déficit individual e o bloco RMR inteiro está em déficit; não há sumidouro nem fonte.

### 2.18 Dias úteis explicam fevereiro e mais nada

Média de dias úteis por mês (feriados nacionais e móveis, Consciência Negra a partir de 2024): jan
21,6 · fev 18,7 · mar 21,2 · abr 20,1 · mai 21,1 · jun 20,6 · jul 22,2 · ago 22,1 · set 20,8 · out
21,6 · nov 19,8 · dez 21,4. Correlação com o perfil sazonal: **0,22**. Incluindo log(dias úteis) no
modelo, o coeficiente é 0,86 (ep 0,27, p = 0,002) — quase proporcional, como esperado mecanicamente —
mas o perfil quase não se move e a amplitude pico-vale **sobe** de 43,1% para 48,7%. A única mudança
grande é fevereiro (−16,4% → −9,2%); janeiro **piora** (−20,0% → −23,0%). O modelo pode incluir o
offset por higiene, mas isso não muda o que a sazonalidade significa. A lista de feriados usada é
nacional e ignora os estaduais e municipais de PE; corrigi-la empurraria fevereiro ainda mais para o
lado do calendário, reforçando a conclusão.

### 2.19 Só cinco municípios atingem a meta INCA, e o estado opera a um terço dela

Razão de 2025: estado **0,342**; RMR 0,307; interior 0,369. Cinco municípios com razão ≥1,0
(população mediana 2.450 mulheres). Nos 13 que nunca voltaram ao pré, a razão de 2025 vai de 0,025
(Santa Cruz da Baixa Verde) a 0,561 (Alagoinha); **Paulista está em 0,127 com 111.693 mulheres**.

Contagem de exames não é cobertura: nada aqui distingue uma mulher rastreada quatro vezes de quatro
mulheres rastreadas uma vez — e §2.16 mostra que a primeira hipótese é a mais provável nos municípios
que "batem a meta".

### 2.20 O agregado 25-64 não esconde mudança de perfil etário

A população-alvo envelheceu de verdade entre 2018 e 2025 (015-019 −10,9%, 020-024 −6,3%, 030-034
−6,4%, contra 060-064 +25,0%, 070-074 +25,1%, 075-079 +26,7%; idade média 25-64 de 42,17 para 43,11
anos). Mas a padronização direta pela estrutura de 2018 move a razão de 2025 de **0,3418 para
0,3409** — 0,09 pp, **0,26% relativo**, e em nenhum ano da janela o efeito passa de 0,10 pp.
Invertendo a padronização (padrão 2025), o efeito máximo é 0,045 pp. A razão mecânica: a razão é
quase plana entre as oito faixas do alvo (0,299 a 0,385 em 2025, máx/mín 1,29), então redistribuir
peso entre elas quase não move o agregado.

Deslocamento etário de quem é rastreada: a idade média da mulher rastreada sobe 1,12 ano, mas a da
população sobe 0,94 ano no mesmo período — **o deslocamento líquido é 0,18 ano em sete anos**, 84% do
movimento é demografia pura.

**A dispensa vale só para o agregado 25-64 e não se estende ao agregado que inclui as faixas de
controle**, onde a heterogeneidade entre faixas vai de 0,010 a 0,385.

### 2.21 Uma anomalia não explicada, anterior a tudo: a queda de 2018 para 2019

Média mensal estadual: citopatológico 28.763 (2018) → 25.876 (2019), **−10,0%**; controle 7.607 →
6.678, −12,2%; mas a mamografia **sobe** 8,2% (10.716 → 11.592). A queda da citologia é concentrada
num vale de mar a jul de 2019 (22.885/mês contra 30.573 no segundo semestre de 2018), com recuperação
parcial no segundo semestre (27.965). Entre os 160 municípios com base ≥20 exames/mês, a mediana da
variação 2018→2019 é −15,2%, com 114 caindo e 45 subindo.

Como a mamografia sobe no mesmo período, não é mudança geral de registro do SISCAN — é específico da
citologia. **Não há explicação para isto no material disponível**, e ela é a razão pela qual o
período pré-intervenção não pode ser tratado como platô nem como reta (§3.5).

### 2.22 E o ano de referência que ninguém nomeou: 2023 é o máximo histórico da série

Volume anual estadual: 345.159 (2018) · 310.510 · 190.683 · 293.341 · 283.236 (10 meses) ·
**376.549 (2023)** · 337.427 · 308.813 (2025). 2023 está 21% acima de 2018 e 33% acima de 2022.

Isto importa porque os relatórios ancoram a série ora em 2018-19, ora em 2022-23, e a referência mais
alta é a que faz 2024-25 parecer declínio. **Se 2023 for pico de recuperação represada** (lançamento
do estoque de 2020-21 chegando ao registro), a "queda de 2024-25" é em parte regressão à média — e
isso não foi testado em lugar nenhum. Fixar uma referência única e justificá-la é pré-requisito de
qualquer número que saia deste documento.

---

## 3. Achados sobre o desenho do estudo

### 3.1 A série-controle: manter, mas não como contrafactual de nível ou tendência

Esta é a decisão de desenho mais consequente da segunda rodada. **A recomendação não é trocar o
controle nem abandoná-lo — é mudar o papel que ele tem no modelo.**

**Dos três argumentos que sustentam a escolha, dois se confirmam e o terceiro falha.**

*Confirmado — mesmo choque pandêmico.* Fundo no mesmo mês (jun/2020) para desfecho e controle, com
magnitudes indistinguíveis (−93,9% e −93,8%), trajetória mensal sobreposta de mar a ago/2020. A
mamografia, por contraste, tem fundo em abr/2020 e já estava −44% em março. Ressalva não removível:
as duas séries são datadas pela liberação do laudo, então o fundo comum é compatível com parada do
laboratório (via de oferta compartilhada) e não **prova** choque de demanda compartilhado. Reportar
como premissa não-falsificável com estes dados.

*Confirmado — mesma via de oferta.* R²(dlog cito ~ dlog ctrl) = **0,990** sobre toda a série; 0,967
excluindo o biênio COVID; 0,955 só em 2018-19; 0,975 em 2022-25. O co-movimento é estrutural, não
pandêmico. Prova direta: dos 28 picos de lançamento retroativo detectados no desfecho, **100%
coincidem com pico >2× no controle no mesmo município-mês** e 93% com pico >4×, razão mediana 7,1×
(Goiana fev/2025: cito 3.089 sobre mediana 216, controle 581 sobre 39). A amplificação é praticamente
igual nas duas séries (7,1× e 6,7×), ou seja, o lote entra proporcional e o DiD o cancela de forma
limpa. **Este é o valor real do controle e é o motivo para mantê-lo.**

*Falha — "não integram o numerador de nenhum indicador de financiamento".* Não integram o numerador,
mas competem pelo mesmo denominador de capacidade da equipe. **O controle não é neutro ao incentivo:
é o que o incentivo desloca.**

**A deriva, medida.** O gap log(razão_cito) − log(razão_ctrl) sobe monotonicamente nos oito anos:
0,624 (2018) · 0,645 · 0,715 · 0,741 · 0,772 · 0,838 · 0,892 · 0,981 (2025), acelerando por
sub-período: +0,196 → +0,276 → +0,480 → +0,664 %/mês. Na janela cheia de 94 meses com HAC/Newey-West:
**+0,422 ± 0,020 %/mês, p < 10⁻¹⁶**; ADF com tendência rejeita raiz unitária (p = 0,024). O termo
quadrático é altamente significativo (p < 10⁻⁴), com inclinação instantânea indo de +0,212 %/mês
(jan/2018) a +0,543 %/mês (abr/2024).

Quatro explicações alternativas foram testadas e descartadas: **demografia** (a diferença de
crescimento populacional explica 3,8%; em contagem bruta sem denominador a deriva é +0,597 %/mês);
**recomposição entre municípios** (dentro de município a mediana é +0,557 %/mês, 66,3% positivos,
Wilcoxon p < 10⁻⁵); **picos retroativos** (excluindo os 28, a deriva vai a +0,597 %/mês — aumenta);
**cauda provisória** (todas as janelas terminam em dez/2025).

O mecanismo está visível no share fora-de-faixa, que cai monotonicamente há nove anos sem uma única
reversão: 20,91% (2018) · 20,51 · 19,21 · 18,88 · 18,32 · 17,32 · 16,54 · 15,32 (2025) · 14,01 (2026
parcial).

**Tendências paralelas são rejeitadas em todas as janelas — e o teste que "passa" está mal
especificado.** A regressão empilhada (duas séries como observações independentes) dá, na janela
pré-τ3, interação +0,578 %/mês com ep 0,713, p = 0,422 → "paralelo". A mesma janela no **pareado** —
inclinação de log(cito) − log(ctrl), que é literalmente o que o DiD estima — dá coeficiente idêntico
(identidade FWL verificada em 3 casas) e ep 0,088, **p = 4,7 × 10⁻⁶**. O ep empilhado infla 8 a 10×
porque ignora que os resíduos das duas séries correlacionam a r = 0,996. Rodando o empilhado com
erros agrupados por competência, ele reproduz o ep pareado. Em três janelas: 2018-19 +0,196 %/mês
(empilhado p = 0,754, pareado p = 0,0065); pré-τ3 +0,578 (0,422 vs 4,7e-6); pré-τ4 +0,519 (0,488 vs
~0).

**O placebo-DiD não é centrado em zero.** Aplicando o DiD (12m pré vs 12m pós) nas dez datas-placebo:
+2,1 · +3,1 · +3,6 · +0,6 · +4,5 · +7,2 · +5,9 · +5,0 · +7,7 · +9,5%. **Dez de dez positivos**, média
+4,94%, sd 2,72%. O mesmo padrão em todas as agregações (jovem 10/10, +4,79%; fronteira 10/10,
+3,58%; distante 10/10, +7,26%). Ampliando para as 33 datas elegíveis: média +4,97%, dp 2,00, mínimo
+1,01, **33 de 33 positivas**. O estimador mede a deriva.

**Mas o alarme de "falso positivo" não se materializa — e este é o ponto que decide a recomendação.**

- A deriva pré-τ3 extrapolada por 12 meses dá +7,2%; o DiD observado em τ3 é +6,0%; residual −1,2%.
  Em τ4, esperado +6,4%, observado +9,5%, residual +3,1% — dentro de 1,1 desvio-padrão da dispersão
  dos placebos. Sob contrafactual quadrático, τ3 esperado +6,7% contra observado +6,0%.
- O t = +5,74 (p = 0,0003) que testa "média dos placebos = 0" é inválido: são dez janelas de 24 meses
  sobre um span de 77, sobrepostas, sobre **uma** série tendenciosa e autocorrelacionada. Está
  redescobrindo a deriva com graus de liberdade emprestados.
- Centrar os placebos não muda τ4 (p = 0,09 antes e depois) e torna τ3 **mais** conservador (0,36 →
  0,73). O que move τ4 é casar os meses (§1a): com janela 8/8, τ4 = +11,04% contra placebos de média
  +4,93% e sd 3,30%, **z = +1,85, p = 0,18**.
- **Estimando o degrau com tendência específica de grupo mais harmônicos e inferência de randomização
  sobre as 65 datas elegíveis, τ3 = +0,32% com 92% das datas produzindo mais** (§1b). Não há falso
  positivo. Quando a deriva é modelada, ela some do estimando em vez de virar efeito.

**E a deriva agregada não é o viés do estimador de painel.** O desvio-padrão da deriva **entre
municípios** é 1,717 %/mês — três vezes a própria média de 0,553 — com IQR [−0,312; +1,364], p10
−1,077, p90 +2,242, e **22,1% do volume estadual em municípios com deriva negativa**. A crítica
inteira vive em ~100 pontos do agregado estadual, mas o desenho é um painel de 185 municípios: uma
inclinação aleatória por município absorve essa heterogeneidade por construção.

**Ambiguidade declarada, e ela não é resolúvel com estes dados.** Se a de-implementação do
rastreamento fora da faixa é *causada* pelo próprio incentivo (substituição de capacidade), então a
deriva não é ruído de tendência: é efeito de tratamento sobre o controle, com sinal invertido. Nesse
caso o termo de tendência específico de grupo **não corrige viés — remove efeito real e enviesa o DiD
para zero**. A tentativa de decidir por quebra de inclinação em τ1 (+0,259 %/mês, p = 0,0039) falha:
10 de 10 datas-placebo produzem quebras igualmente significativas sob pré-tendência linear, porque a
deriva acelera continuamente. **Isto vai para o protocolo como ambiguidade declarada, não como
recomendação metodológica.**

**Não trocar por mamografia.** Ela é pior em correlação (r de 1ª diferença +0,510 contra +0,977; na
janela τ1–τ3 r(dlog) +0,592 contra +0,997), em erro de acompanhamento (sd 0,346 contra 0,028), em
variância de placebo (sd 12,88% contra 2,72%), tem pré-tendência de sinal oposto (+1,239 %/mês contra
−0,161 em 2018-19) e choque pandêmico em mês diferente. O argumento de que "é a única com placebos
centrados em zero, e isso é diagnóstico" **não vale**: com sd 12,88% e n = 10, o IC95 da média dos
placebos é [−10,4%; +8,1%], o poder para detectar exatamente o viés de +4,94% do controle é 0,19, e o
menor viés detectável com 80% de poder é 11,8%. A mamografia não está centrada em zero — ela é
incapaz de dizer onde está.

**Desagregar o controle: sim, mas não no eixo proposto.** Jovens (015-024) e idosas (065+) **não** têm
dinâmicas opostas: r de nível +0,703, r de 1ª diferença +0,680 (IC95 +0,37 a +0,85), r durante COVID
+0,97, e índices de 2025 base 2018 praticamente iguais (61,9 e 59,3). Não há cancelamento — o sd da
variação mensal do agregado é igual ao de cada metade. O que precisa ser pré-especificado é **quais
faixas entram**, porque o DiD de τ4 varia de +0,3% (065-069) a +10,4% (020-024) a +13,5% (075-079) a
+32,6% (080-120); agregados: fronteira +7,4%, distante +13,5%, controle inteiro +9,5%.

Ressalva sobre o "gradiente por distância à faixa": em contagem bruta, sem denominador, a correlação
distância × índice 2025 cai de −0,989 para **−0,786** e a simetria que dava força ao argumento
evapora (015-019 e 070-074 são 54,6 e 54,5 em razão, mas 48,6 e 68,2 em contagem). E distância é
quase colinear com o tamanho da faixa (corr log N × distância = −0,930), com n = 6 pontos e 4 valores
distintos de distância. **"Faixas pequenas caíram mais" ajusta os dados tão bem quanto "faixas
distantes caíram mais"**, e não implica dose-resposta a incentivo. A implicação prática sobrevive; a
leitura mecanicista, não.

**Cegueira mecanicista, registrada e não testável.** Se o mecanismo do incentivo for melhoria de
**registro** e não aumento de exames — o mecanismo mais provável de um indicador pago por exame
lançado — o controle o remove por construção e o DiD estima zero necessariamente. Com apenas 1,0% de
variância residual (sd do resíduo 0,0281 contra sd bruto 0,2796), o sinal que sobra é menor que o
viés de tendência. O teste proposto (comparar a distribuição de tempo de liberação do laudo entre
desfecho e controle antes e depois de τ3) **não pode ser rodado**: a tabulação
`qualidade/tempo_liberacao` de `dashboard.json` é apenas anual, três categorias, sem quebra por série.
Exige tabulação do SISCAN estratificada por faixa etária — isso é prazo, não análise.

**Recomendação consolidada:**

1. Manter `cito_controle_fora_faixa` no modelo **como covariável de nuisance variando no tempo**
   (absorve choque comum de notificação e lote retroativo, para o que ele é comprovadamente bom),
   **nunca como contrafactual de nível ou de tendência**.
2. Pré-especificar **quais faixas** compõem o controle, antes de ver o resultado.
3. Incluir **inclinação aleatória por município** — é o que transporta o argumento do agregado para o
   painel.
4. Reportar o degrau com **tendência específica de grupo** e inferência de randomização, e declarar
   a ambiguidade sobre o que essa tendência absorve.
5. **Não** usar controle e harmônicos de Fourier ao mesmo tempo como fontes concorrentes de
   sazonalidade: os perfis sazonais das duas séries são idênticos (r = 0,9937) e os dois termos
   competem pelo mesmo sinal, inflando os erros-padrão da parte que interessa. Escolher uma rota e
   justificar.

### 3.2 Inferência: nem empilhado i.i.d., nem pareado i.i.d.

O ep empilhado está morto (§3.1). Mas **o ep pareado i.i.d. também é anticonservador**: os resíduos
do gap são serialmente correlacionados (rho = +0,59, Durbin-Watson 0,79 na janela pré-τ3). Na
regressão de degrau com tendência de grupo e harmônicos, o ep i.i.d. dá 1,38% e p = 0,0005 para τ4,
contra sd 3,50% da distribuição de randomização — **anticonservador por 2,3×**.

Segundo alerta: os p pequenos de janelas curtas são teatro. Simulando 2.000 random walks sem drift
com o mesmo sd de inovação (0,0232) e n = 22, **73,2% rejeitam a 5% com ep i.i.d. e 66,9% com HAC**.
Em 22 meses não se separa tendência de passeio aleatório. O que sustenta a deriva é a janela de 94
meses com HAC e o ADF-com-tendência, não o p = 2 × 10⁻⁶ da janela de 22.

**O protocolo deve usar HAC ou inferência de randomização.** Sem isso troca-se um erro tipo II por um
tipo I.

### 3.3 Sazonalidade no modelo: K=2, harmônicos interagidos com o período pandêmico, e inclinações aleatórias

**(a) K=2 pares, e isso é firme.** AIC e BIC concordam, o teste de falta de ajuste contra o saturado
não rejeita (F = 0,87, p = 0,541), e sob binomial negativa o AIC escolhe K=2 também. **Não** descrever
o segundo par como "dominante" (§2.12): as duas amplitudes são indistinguíveis (0,0984 e 0,1031) e o
ranking espectral não é estável à janela. Não acrescentar K=3 para limpar resíduo — o que falta é um
termo AR(1) (rho 0,11 a 0,31).

**(b) Estimar os harmônicos com interação por período pandêmico é obrigatório, não sensibilidade.**
Poolar 2020-21 desloca o coeficiente sazonal de **maio em −23,4 pontos percentuais** (−14,4% com a
pandemia dentro, +9,0% sem) e o de junho em −22,8 pp. A escala do perfil sazonal de 2020 é 4,66 vezes
a dos demais anos, com amplitude pico-vale de 1.426% contra 33-92% nos anos normais. **Maio de 2024 é
τ3 e maio de 2025 é τ4** — a contaminação incide exatamente no mês de início dos dois marcos
recentes.

O critério para decidir se isso é problema teórico ou real foi declarado ("se a diferença for menor
que um décimo do erro-padrão, vai para apêndice") e o teste foi rodado: ITS na janela completa com
degrau e inclinação em τ3, mais indicador pandêmico de nível e inclinação.

| Especificação | τ3 (log) | τ3 (%) | ep |
|---|---|---|---|
| Fourier global | −0,0331 | −3,3% | 0,157 |
| Fourier × período pandêmico | −0,0949 | −9,1% | 0,125 |

Diferença = 0,0618 log = **0,49 erro-padrão**, quase cinco vezes o limiar, e a estimativa pontual
quase triplica. **Vai para a especificação principal.** (Ressalva honesta: os dois erros-padrão são
enormes e nenhuma das duas estimativas chega perto de significância — a conclusão substantiva não
muda, o que muda é que a magnitude reportada depende de uma escolha que precisa ser pré-declarada.)

**(c) Inclinações aleatórias no primeiro par de Fourier por município são obrigatórias.** Apenas
34-35% dos municípios têm sazonalidade detectável, em todos os cortes de volume até 20 mil exames
acumulados, e a dispersão de fase cobre de abril a outubro (§2.13). Um harmônico de efeito fixo impõe
o mesmo perfil a Recife e a Fernando de Noronha; isso subestima a variância e infla a precisão
aparente de τ3, que é justamente o ponto frágil apontado pelo teste de falsificação.

**(d) A estabilidade da amplitude não é testável com poder** (~6 observações por mês do ano). Rodar
o modelo principal com Fourier fixo e reportar como sensibilidade **pré-especificada** a versão com
interação Fourier × período, mostrando o efeito sobre τ3. Se concordarem, a discussão fica livre; se
discordarem, isso é resultado.

**(e) O modelo não precisa de offset por dias úteis** (§2.18) — pode incluí-lo por higiene, mas não
muda nada.

### 3.4 Família de distribuição: Poisson está descartada, e o teste indica zero-inflação

No grão município × faixa × mês (o grão do GLMM), 2018-2025 sem provisórios: 139.120 células,
**17.659 zeros (12,7%)**. Os 2,1% da primeira rodada são de um grão mais agregado; os dois números
são compatíveis e o que importa para o modelo de contagem é este.

Zeros por faixa: 9,8% (25-29) crescendo monotonicamente até 20,2% (60-64). Por quintil de porte:
21,5% · 17,8% · 12,0% · 9,3% · 2,9%.

**A variância marginal de 5× a 173× a média é um número enganoso** e não deve ser reportado: mistura
variação entre municípios, faixas e meses, e não diz nada sobre a superdispersão **condicional** que
o GLMM com offset e efeito aleatório enfrenta. Condicionando em taxa municipal × índice de faixa ×
índice de mês, a dispersão de Pearson cai de 172,7 para **14,5** no Q5 e de 5,0 para **3,4** no Q1 —
o número de manchete superestima o Q5 em 12×.

⚠ **"Os municípios grandes são proporcionalmente mais superdispersos" é artefato matemático.** A
estatística usada, CV_obs / (1/√μ) = CV·√μ, é monótona em μ sempre que o CV é aproximadamente
constante. Aplicando o CV mediano estadual (0,652) a todos os quintis, o "excesso" previsto iria de
3,89 a 10,34; o observado vai de 4,10 a 8,74 — **menos** que o artefato prevê. O CV de fato **cai**
com o porte (Spearman −0,297, p = 4,0 × 10⁻⁵).

⚠ **A conclusão "NB2 basta, ZINB não é necessário" falha no teste que ela própria definiu como
decisivo.** Sob NB2 condicional com α ajustado por momentos, o P(0) observado excede o predito em
todos os quintis: Q1 0,215 vs 0,168 · Q2 0,178 vs 0,113 · Q3 0,120 vs 0,066 · Q4 0,093 vs 0,036 ·
Q5 0,029 vs 0,004. Ajustando de verdade (offset log(pop/3), faixa + taxa municipal + tendência,
n = 25.000): **NB2 AIC = 159.056,6 contra ZINB AIC = 158.396,3, ΔAIC = 660 a favor do ZINB**.
Ressalva: esse ajuste não tem intercepto aleatório de município, que poderia absorver parte do
excesso; mas a checagem por momentos já condiciona na taxa municipal e dá o mesmo sinal.

**Recomendação:** Poisson descartada; **pré-especificar a comparação NB2 vs ZINB com efeito aleatório
de município**, e reportar rootograma além de AIC/BIC. Não presumir NB2.

Nota correlata: os municípios com CV > 1,5 coincidem quase inteiramente com os que têm degrau de
registro (Afrânio 2,265 · Lagoa Grande 2,181 · Santa Cruz da Baixa Verde 2,068 · Maraial 2,027 ·
Escada 2,015 · Cabrobó 1,975 · Orocó 1,933 · Dormentes 1,763 · Goiana 1,626 — bloco São Francisco
mais os dois picos retroativos). **O efeito aleatório vai absorver falha administrativa e chamá-la de
heterogeneidade municipal**, inflando a variância residual e reduzindo o poder para detectar τ3. Daí
a recomendação do indicador de "registro ativo" (§4).

### 3.5 A forma da tendência: nem platô, nem reta, e o estimador piecewise carrega viés fixo

O período pré-intervenção **não é platô** (§2.21: −10,0% de 2018 para 2019) e **não é reta** (a queda
é um vale de mar-jul/2019 com recuperação parcial). Extrapolar uma tendência linear ajustada em
2018-19 por seis anos é indefensável, e é exatamente por isso que o contrafactual B produz déficit
~zero (§2.4).

**E todo estimador de quebra piecewise-linear nesta série carrega viés fixo por curvatura.** Ajustando
uma quadrática à própria série de log(fora/alvo) — zero ruído, zero competência ausente — e rodando o
estimador de quebra de inclinação: **−1,02 %/ano em toda data, com desvio-padrão exatamente 0,000**.
Ajustar duas retas a uma curva convexa devolve quebra negativa em qualquer nó. Isso invalida a leitura
"os placebos negativos vêm do buraco de ago/set 2022" (§5) e obriga a especificar tendência quadrática
ou spline pré-especificada antes do nó.

**Duas violações concretas de tendência pré-estável nos marcos recentes**, já listadas em §1c e §2.1:
a quebra da Mata Meridional dentro do braço pré de τ3, e o colapso de jan-abr/2025 dentro do braço pré
de τ4. Nenhuma das duas é tratável como covariável contemporânea.

### 3.6 Denominador, unidade e grão

- **Padronização etária não é necessária** para o agregado 25-64 (efeito de composição 0,26%, §2.20).
  Escrever isso explicitamente na dissertação como verificação feita — é a objeção óbvia de banca a um
  estudo ecológico de série longa com população envelhecendo. **Não estender ao agregado que inclui as
  faixas de controle.**
- **A mamografia carrega o mesmo `pop_alvo` da citologia** — verificado em **4.995 de 4.995** linhas
  com (município, faixa, ano) comuns, não é coincidência de uma célula. Mamografia é bienal
  (denominador pop/2) e citologia trienal (pop/3); aplicar a fórmula do painel à mamografia
  subestimaria a razão em 33%. Hoje o `dashboard.json` publica só a contagem bruta de mamografia, então
  o erro está **latente, não cometido**. Correção barata: coluna `periodicidade` (2 ou 3) no painel.
- **Cobertura suplementar (ANS) como covariável de nível 2.** Se a hipótese de §2.15 se confirmar, boa
  parte do gradiente de porte — e da variabilidade que o modelo atribuiria a efeito aleatório — é
  misspecificação do denominador. Join público por `cod_ibge`.
- **Termo aleatório de GERES/região, além do de município.** O bloco Mata Meridional (§2.1) e o bloco
  São Francisco (§2.2) são fenômenos regionais; um intercepto aleatório municipal absorve o nível mas
  não a estrutura de correlação espacial nem a alternância liga/desliga dentro do bloco (Petrolina
  varia 0,016 → 0,260 entre anos, 16×).
- **A faixa 080-120 é heterogênea** (40 anos de amplitude, 137.264 mulheres em 2025 contra 114.563 em
  075-079, apenas 437 exames em 2025). Mas ⚠ **o impacto foi superestimado**: ela é 1,04% do controle,
  e removê-la move o DiD de τ4 de +9,50% para +9,04% (0,46 pp) e o de τ3 de +6,01% para +5,62%
  (0,39 pp). É **gravidade menor**, uma linha de sensibilidade no apêndice — não um parágrafo no
  protocolo. Se alguma faixa merecesse destaque por peso, seria 020-024, que sozinha é 47,7% do
  controle. Excluí-la, sim, das regressões de gradiente etário, onde é ponto de alta alavancagem com
  ponto médio arbitrário.

### 3.7 Regras de janela e de pré-especificação

1. **Janelas pré/pós com o mesmo número de meses E os mesmos meses-calendário.** A amplitude sazonal é
   de ~40% (média da razão por mês: jan 0,299 · fev 0,314 · jun 0,315 · jul 0,321 contra out 0,419 ·
   nov 0,407 · set 0,388 · ago 0,389) e τ4 é o único marco cuja janela pós é truncada pelo fim dos
   dados — logo é o único cujo placebo da primeira rodada não é comparável. Reportar sensibilidade a
   janelas de 6/9/12 meses.
2. **Todo estimando reportado vem com sua distribuição de placebo**, com janelas simétricas e
   pré-especificadas. Duas vezes em duas rodadas uma especificação plausível produziu significância
   que o placebo derrubou; isso precisa virar regra, não hábito.
3. **Não usar "distância mínima a ago/set 2022" como critério** — ver §5, o problema é curvatura, e a
   regra custaria o terço central da janela sem comprar nada.
4. **Fixar o critério de identificação dos picos de lote no protocolo** com janela explícita (número
   de meses vizinhos, se inclui o próprio mês, mediana ou média aparada, limiar absoluto ou relativo
   ao mês). A escolha muda o conjunto de 26 para 61 picos e muda qual mês é o modal (§5).
5. **Fixar uma referência única** para todo o documento e justificá-la (§2.22). Trocar base 2018-19
   por base 2019 muda o déficit estadual de +115.056 para +16.884, o "repagamento" de 36% para 89%, o
   superávit do interior de −26.731 para −85.942, e a lista de municípios abaixo do pré de 62 para 56.
6. **Verificação obrigatória:** a soma dos 185 municípios tem de fechar com o agregado estadual em
   toda métrica derivada. Foi essa checagem, e só ela, que expôs o erro de `min_count` (§4).

### 3.8 Desfechos secundários que os dados sustentam

- **Proporção de exames dentro da faixa 25-64 sobre o total** — medida de conformidade com a diretriz,
  com sinal muito maior que a razão (−5,19 pp em oito anos, deriva de −0,84 pp/ano com R² = 0,947) e
  sem degrau em mês nenhum. Ressalva de §2.8: 88% do movimento é o lado <25, e a interpretação
  ("convergência" vs "racionamento") é ambígua.
- **Contagem absoluta de exames em mulheres de 15 a 24 anos** — 37.636/ano, 13,0% do volume acumulado.
  Interpretação clínica direta (exames contraindicados) em vez de uma razão adimensional. **Não** usar
  a versão "cobre 96% do déficit" (§2.9).
- **Gini de concentração ponderado pela população-alvo** — defensável como desfecho secundário anual,
  **mas só depois de separar desligamento de registro de queda de produção** (§2.7).
- **Razão de seguimento sobre rastreamento** — se sobreviver à verificação de artefato de preenchimento
  (§2.10), é o desfecho mais próximo do que efetivamente previne câncer invasivo.

---

## 4. Problemas de dado a tratar

Tabela única, ordenada por gravidade. As duas rodadas estão integradas.

| # | Problema | Evidência | Gravidade | Tratamento |
|---|---|---|---|---|
| 1 | **A Mata Meridional inteira para de registrar citologia em dez/2023, dentro do braço pré de τ3** | 21 de 21 municípios elegíveis da microrregião no grupo do colapso, Fisher p = 4,2e-18. Série do bloco: nov/23 1.940 → dez/23 1.110 → jan/24 720, nunca mais acima de 1.016. Cinco dos doze meses do pré de τ3 já colapsados | compromete-análise | Tratar como **quebra estrutural datada em dez/2023**, não como covariável. Rodar o teste de falsificação de dez placebos sobre a série sem a microrregião. Reportar τ3 com e sem. Ir ao CNES: descredenciamento ou troca de prestador entre out/2023 e jan/2024 |
| 2 | **Ago e set de 2022 não estão vazios no TABNET — 31.519 exames existem na fonte** | `qualidade.json` (mesma `tabula_por_ano` do pipeline, sem excluir competências inválidas) soma 314.755 em 2022 contra 283.236 do painel. Reconcilia ao dígito nos outros 8 anos; a diferença total das 9 tabulações é exatamente 31.519. Média dos 4 meses vizinhos = 29.613/mês, esperado 59.226 — os 31.519 são **53,2%**, ou 15.760/mês | compromete-análise | Reextrair ago e set de 2022 do TABNET. Se for competência parcial, reclassificar de `valido=False` para uma terceira categoria (parcial/subnotificado) e tratar como **censura**, não exclusão listwise. Enquanto isso: nunca cruzar tabulações de qualidade com o painel dentro de 2022 sem reconciliar (os 45,4% de laudos >30 dias estão sobre base de 12 meses em 2022 e 10 no painel); e não anualizar 2022 por ×12/10 (superestima em 8,0%: 339.883 contra 314.755) |
| 3 | **Degraus sustentados de disponibilidade de registro em 111 de 185 municípios** | 62 desligamentos (−101.868 exames/ano) e 49 ligamentos (+78.744/ano), critério 6m antes vs 6m depois, razão ≥5× ou ≤1/5. Nos 23 do bloco mar-abr/2019 a citologia cai a **12,1%** enquanto a mamografia fica em **84,5%**. Nos 5 de mai-jul/2025 a citologia sobe 10,7× enquanto a mamografia cai | compromete-análise | Indicador binário pré-especificado de **"registro ativo"** por município-mês (média móvel de 6 meses acima de um piso, ou ausência de degrau ≥5× nos 6 meses adjacentes), (a) como covariável e (b) como critério de exclusão, reportando as duas versões. Fixar o critério antes de olhar o modelo. ⚠ Não usar a estatística de agrupamento por mês: o nulo com choque comum produz clusters maiores que os reais |
| 4 | **τ4 é contaminado pelos ligamentos de mai-jul/2025** | Janela mai-dez pareada: com todos 0,3895 → 0,3685 (−5,4%); sem os 5 (Flores, Parnamirim, Santa Filomena, Orocó, Petrolina, +12.392 exames/ano) 0,4065 → 0,3753 (−7,7%). Contribuição **+2,3 pp**. Só Petrolina leva a −7,1% | compromete-análise | Reportar τ4 sempre em duas versões, pré-especificadas. Reportar Petrolina isolada, porque a lista dos cinco é instável a W (W=4 troca dois deles; W=9 sobram dois) |
| 5 | **Citologia quase ausente em 8 municípios do São Francisco durante toda a janela, incluindo Petrolina** | Razão do bloco 0,025 a 0,197 contra 0,231 a 0,445 no resto de PE, em todos os 8 anos. Petrolina: 624 exames em 2024 para 113.692 mulheres. A mamografia do bloco também está abaixo (SF/resto ~0,61 em média) — **subnotificação geral de ~40% mais supressão específica da citologia de fator ~2,5** | compromete-análise | Sensibilidade obrigatória excluindo os 8; termo aleatório de GERES/região. Contrafactual pela mamografia do próprio município, não pela razão do resto de PE (déficit acumulado cai de ~104 mil para ~60 mil). Verificar no CNES se há laboratório habilitado na VIII GERES e sob qual CNES fatura; verificar SISCAN por **residência** |
| 6 | **O controle está sob de-implementação ativa: nove anos de queda monótona do share fora-de-faixa** | 20,91% (2018) · 20,51 · 19,21 · 18,88 · 18,32 · 17,32 · 16,54 · 15,32 (2025) · 14,01 (2026 parcial). Sem uma reversão. Deriva do gap: +0,422 ± 0,020 %/mês (HAC, 94 meses), acelerando de +0,212 a +0,543 %/mês | compromete-análise | Não há tratamento estatístico que conserte um controle tratado por outra política. Modelar a deriva explicitamente com tendência específica de grupo + inclinação aleatória por município (§3.1), **e declarar a ambiguidade**: se a deriva for causada pelo incentivo, o termo remove efeito real e enviesa para zero |
| 7 | **Colapso de jan-abr/2025, dentro do braço pré de τ4** | Razão estadual jan-abr: 0,3488 (2024) → 0,2884 (2025), −17,3%, contra −5,4% em mai-dez. Jan/2025 = 0,211 é o mês mais baixo das 102 competências fora do vale da COVID. −13.611 exames no trimestre, 7.795 em 12 municípios grandes | compromete-análise | Nomear o evento e datá-lo antes de estimar τ4. Um ITS com degrau de nível em τ4 lê o retorno ao normal como efeito positivo do marco — que é o mecanismo que produziu o +3,6% original |
| 8 | **Em 2025 há 33 municípios com razão anual <0,1 — tantos quanto em 2020 (34), com volume caindo 19% em vez de 46%** | 17 · 19 · 34 · 7 · 7 · 10 · 13 · 33. Persistentes: Triunfo 8/8 anos, Afrânio 7, Santa Cruz da Baixa Verde 7, Lagoa Grande 7 | compromete-análise | Distinguir persistentes (falha estrutural — tratar como **dado faltante**, não zero de produção) de episódicos (indicador de registro ativo). Razão <0,1 sustentada é a versão municipal do erro de ler ausência como zero. Compromete usar 2025 como período pós de qualquer marco |
| 9 | **`groupby().sum()` converte as duas ausências documentadas em zeros reais** | `d[d.serie=='citopatologico'].groupby('dt').exames.sum()` devolve **0.0** em 2022-08 e 2022-09 (todas as células NaN). log(0) = −inf, e um GLMM Poisson leria "zero exames em Pernambuco inteiro". No painel municipal o mesmo erro inflou o déficit em **54.639** exames (= 2 × 27.320), 47% da estimativa líquida | compromete-análise | `sum(min_count=1)` em toda agregação, ou máscara explícita pela coluna `valido`. ✔ **Verificado: `pipeline.py` (linha 599, `None if m in invalidas else ...`) e `dashboard.json` estão corretos** — trazem `null` em 2022-08 e 2022-09 em `series.citopatologico` e em `razao_mensal`. A armadilha é dos scripts de análise, não do pipeline |
| 10 | **Petrolina tem série não interpretável e seu déficit não pode ser reportado** | Volume anual: 1.767 · 8.480 · 1.129 · 3.395 · 3.470 · 4.379 · **624** · 4.627. Em 2024, 30-40 exames/mês numa cidade com 97.951 mulheres 25-64. Degrau abrupto: jun/2025 = 39 → jul/2025 = 533 → 820, 701, 887. A mamografia, no mesmo município e período, é estável (2.755 · 2.585 · 2.139 · 1.683 · 2.065 · 3.620 · 2.244 · 1.774) | compromete-análise | Excluir ou tratar como observação influente declarada. **A razão cito/mamografia por município é um detector objetivo de integridade de registro** e deve substituir o julgamento caso a caso — rodá-la nos 185 produz a lista de municípios com série de citologia não interpretável |
| 11 | **Quatorze municípios têm sub-registro quase certo no pré-pandemia, invalidando o contrafactual neles** | Razão 2018-19 abaixo de 0,10: Belo Jardim 0,099, Exu 0,016 (33 exames em todo 2018), Cabrobó 0,038, Lagoa Grande 0,038, Afrânio 0,022, Dormentes 0,028, Triunfo 0,054, Santa Filomena 0,032, Moreilândia 0,021 e mais 5. Juntos contribuem **−26.454** de superávit fictício | exige-tratamento | Limiar pré-especificado de plausibilidade da linha de base (razão pré ≥0,10) e déficit reportado com e sem: +115.056 → +141.509 (sem <0,10) → +154.210 (sem <0,20). Nunca apresentar o superávit deles como recuperação |
| 12 | **Estimar um único perfil sazonal sobre a janela inteira transfere o colapso pandêmico para maio e junho** | Maio: −14,4% com 2020-21 dentro, +9,0% sem — **23,4 pp**. Junho −25,6% vs −2,8%, 22,8 pp. Escala do perfil de 2020 = 4,66× a dos demais anos. τ3 é maio/2024 e τ4 é maio/2025 | exige-tratamento | Harmônicos interagidos com indicador de período pandêmico (mar/2020–dez/2021). Verificado que muda τ3 de −3,3% para −9,1%, diferença de **0,49 ep** — entra na especificação principal, não em apêndice (§3.3b) |
| 13 | **Picos de lançamento retroativo em lote** | 36 competências município-mês acima de 4× a mediana dos seis vizinhos com excesso >200, voltando ao normal em seguida; **18.804 exames, 0,73% do total**. Ipojuca jan/2021 28→827 (29×); Maraial mai/2021 12→361; Belo Jardim nov/2020 9→236; **Goiana fev/2025 157→3.089**; Vitória de Santo Antão jun/2020 24→440; Escada ago/2021 202→2.921→241. **14 dos 36 caem a menos de três meses de algum marco** | exige-tratamento | Modelar como **observação influente** com critério pré-especificado e reportar estabilidade com e sem (preferível a winsorizar ou redistribuir, porque não altera o dado). ⚠ O critério muda tudo: mediana móvel de 7 meses dá 26 picos e 13.619 exames; limiar relativo ao mesmo mês em outros anos dá **61 picos** e muda o mês modal de dezembro para **maio**. Fixar janela, referência e limiar no protocolo antes de rodar |
| 14 | **Picos retroativos produzem superávits municipais fictícios que escondem municípios em colapso** | Excesso no pós: 9.774 exames em 15 competências. Goiana concentra 2.873 e aparece com superávit de −11.647; **Escada** concentra 2.701, aparece entre os maiores superávits do estado e tem razão de **0,062** em 2025. Removendo o excesso, o déficit líquido sobe de +115.056 para +124.830 | exige-tratamento | Classificação recuperado/não-recuperado sobre série winsorizada, com **"razão do último ano firme" como segundo critério obrigatório** ao lado do déficit acumulado |
| 15 | **O período pré-intervenção não é platô nem reta** | Média mensal: cito 28.763 (2018) → 25.876 (2019), −10,0%; controle −12,2%; **mamografia +8,2%**. Vale concentrado em mar-jul/2019 (22.885/mês contra 30.573 no 2º semestre de 2018). Mediana municipal −15,2%, 114 caindo e 45 subindo | exige-tratamento | Investigar o que ocorreu na citologia em PE no 1º semestre de 2019 antes de fixar o baseline. Não extrapolar tendência linear de 2018-19 (é o que produz o contrafactual B com déficit ~zero). Declarar e testar a suposição do segmento pré no ITS |
| 16 | **O valor de τ4 na tabela de falsificação é artefato de janela sazonalmente truncada** | Pós-τ4 tem 8 meses (mai-dez/2025) contra 12 no pré, e os meses 5-12 têm fator sazonal 1,056 contra 0,888 dos meses 1-4. Viés de +5,6%. Com meses casados, **−5,4%** em vez de +3,6% | exige-tratamento | Corrigir a tabela. Janelas casadas em meses do calendário sempre que a cauda provisória truncar o pós. No DiD o viés **não** cancela: τ4 sobe de +9,50% (truncado) para +11,04% (casado 8/8) e os dez placebos precisam ser recalculados com a mesma janela |
| 17 | **A janela útil para estimar sazonalidade não-pandêmica tem 70 meses — ~6 observações por mês do ano** | 2018 (12) + 2019 (12) + 2022 (10) + 2023 (12) + 2024 (12) + 2025 (12). Os testes de estabilidade (F = 1,03 p = 0,444; F = 1,51 p = 0,211) são não-rejeições de baixo poder, enquanto os pontos estimados se movem 10 a 16 pp | exige-tratamento | Ou estender para 2014-2017 (existe no SIA e triplicaria o pré-pandemia), ou declarar no protocolo que a suposição de sazonalidade estável **não pode ser testada com poder** e reportar a versão com deriva como sensibilidade obrigatória |
| 18 | **2022 tem 10 competências observadas; comparações de nível anual precisam de anualização, o Gini não** | `n_meses` = 10 em 2022 para os 185 municípios, 12 nos demais. Como o fator é comum a todas as unidades, cancela nas frações acumuladas da Lorenz. Sem anualizar, a razão de 2022 seria 0,3205 em vez de 0,3846 | exige-tratamento | Preferível: grão mensal com os dois meses como faltantes, nunca como zero. Se anualizar, ⚠ o fator correto **não é 12/10** — sob a hipótese de que ago/set tiveram 53% do volume (item 2), o fator é 314.755/283.236 = **1,111**, e a razão de 2022 vai de 0,385 para ~0,357 |
| 19 | **O critério de retorno "3 meses consecutivos ≥90%" confunde volatilidade com nível** | Jupi tem nível 2024-25 = 0,914 do pré e nunca atinge 3 meses consecutivos. Concordância entre critérios: 7 nunca recuperam pelos dois, 2 só por A, 6 só por B. Pior: "nunca encostou" ≠ "está abaixo hoje" — o primeiro dá 13 municípios, o segundo dá **62** (§2.3) | exige-tratamento | Usar **nível médio de 2024-25 contra a base pré** como definição principal (responde à pergunta de gestão). Declarar o critério antes de olhar o resultado |
| 20 | **A cauda provisória de 2026 tem numerador subestimado E denominador congelado** | Média mensal jan-jun/2026 = 22.195 contra base pré de 27.320 (−18,8%), ascendente dentro da própria cauda (jan 19.993, mar 22.988, mai 24.924). `pop_defasada=True` marca exatamente as linhas de 2026, que carregam `pop_ano=2025` — a pirâmide de 2026 é idêntica à de 2025 nas 14 faixas, superestimando a razão em ~0,85%. Vieses opostos, o do numerador é uma ordem de grandeza maior. **A mamografia não tem cauda** (2026H1 = 10.277/mês contra 10.331 em 2025, −0,5%), enquanto o cito cai 13,8% — medida direta do lag de liberação | menor | Excluir 2026 de toda estatística. Marcar visualmente como parcial no dashboard (hoje publica `razao_anual` 2026 = 0,295 ao lado dos anos completos). ⚠ **Anomalia a registrar:** em 2026 a categoria "mais de 60 dias" de `tempo_liberacao` é 20.280 de 133.172 = **15,2%**, o máximo da série (2025: 11,0%; 2021: 7,0%). Numa cauda truncada isso é o inverso do esperado, e é evidência direta de que 2026 é backlog de 2025, não atividade de 2026 — a cauda deve ser excluída por **composição**, não só por volume |
| 21 | **A faixa 080-120 é aberta (40 anos) e entra no controle junto com faixas quinquenais** | 137.264 mulheres em 2025 contra 114.563 em 075-079; apenas 437 exames (razão 0,010); variação 2019→2025 de −62,0%, a maior da grade, sobre base de centenas | menor | ⚠ Impacto superestimado na versão original: é **1,04% do controle** e removê-la move o DiD de τ4 em 0,46 pp e o de τ3 em 0,39 pp. Uma linha de sensibilidade no apêndice. Excluí-la, sim, das regressões de gradiente etário, onde é ponto de alta alavancagem com ponto médio arbitrário (90) |
| 22 | **A série de mamografia carrega o `pop_alvo` das faixas de citologia** | Verificado em **4.995 de 4.995** linhas com (município, faixa, ano) comuns. Mamografia é bienal (pop/2), citologia trienal (pop/3): aplicar a fórmula do painel subestimaria em 33%. `dashboard.json` publica só contagem bruta, então o erro está latente | menor | Coluna `periodicidade` (2 ou 3) no painel, para a fórmula não depender de quem escreve o script lembrar |
| 23 | **O Gini não ponderado das contagens brutas mede tamanho de município, não desigualdade de acesso** | 0,652 (2018) · 0,642 (2020) · 0,642 (2025) — praticamente constante e sem relação com o ponderado (0,260 a 0,337). Dominado por Recife ter 480.781 mulheres e Fernando de Noronha 1.069 | menor | Reportar apenas o Gini ponderado pela população-alvo, com os eixos da Lorenz explicitados, e dizer no texto por que o bruto foi descartado |
| 24 | **Divergência de critério na contagem dos picos: 36 na primeira rodada, 26 na segunda** | Critério da segunda: mediana móvel centrada de 7 meses (min_periods=5), razão >4, excesso >200, dentro de competências válidas → 26 picos, 13.619 exames, 0,53%. Os oito maiores coincidem (Goiana, Escada, Ipojuca), então é definição de vizinhança, não dado | menor | Coberto pelo item 13. Nenhuma conclusão de robustez muda com 26 ou 36 |

### 4.1 Advertência: os erros das próprias análises

Cinco erros foram cometidos e corrigidos **dentro** destas duas rodadas. Ficam registrados porque
ilustram o risco do gênero: **um script de verificação com bug produz um alarme falso tão convincente
quanto um achado real.**

1. **Denominador de 225.805 mulheres** (rodada 1). A primeira versão do script de consistência
   reportou esse número, o que teria sido um problema gravíssimo. Era erro do script, que dividia por
   doze um valor que não estava replicado por competência. **O valor correto é 2.710.671.**
2. **`aggfunc='sum'` transformando ausência em zero** (rodada 2). Inflou o déficit municipal em
   54.639 exames — 47% da estimativa líquida. Só foi pego porque a soma municipal não fechava com a
   estadual. **Alguns números publicados carregam esse erro**: o déficit de Recife é 81.106 e não
   91.676; Jaboatão 15.775 e não 18.487; os 10 maiores somam 198.953 (67%) e não 223 mil (75%). O
   casamento é exato à casa decimal (81.106 + 2 × 5.284,75 = 91.675,5), o que confirma o diagnóstico.
   Pior: a mesma frase usava numerador com bug e denominador corrigido.
3. **Spline cúbica de 8 nós absorvendo a sazonalidade** (rodada 2). Produzia escalas de amplitude de
   0,78 → 2,53 → 0,18 → 0,25 por biênio, "colapso da sazonalidade após a pandemia", F de escalas
   iguais p = 0,0001. Era artefato duplo: a spline com um nó a cada dez meses absorve o sinal (o F das
   dummies de mês cai de 6,22 para 1,70 quando ela entra) e a média móvel 2×12 perde os seis primeiros
   e últimos meses. No desenho balanceado a amplitude **cresce**, de 37,0% para 55,2%.
4. **Janela assimétrica no teste de quebra** (rodada 2). Uma versão dava −3,80 %/ano com t = −3,33,
   "significante", e teria sido o único achado a contradizer a conclusão nula. A janela era 38 meses
   antes e 20 depois. Corrigida, o placebo derrubou (p = 0,36). E a correção **ainda estava errada**:
   com `iloc` numa série de 94 pontos, a janela de τ3 é 24/20 enquanto os 25 placebos recebem 24/24 —
   o mesmo defeito que dizia ter consertado. Com janela genuinamente simétrica τ3 é −4,72 a −5,09
   %/ano, 50-70% **maior** que os −3,00 reportados, e o p continua 0,32.
5. **Rayleigh do harmônico quadrimestral** (rodada 2). Reportado como R = 0,028, p = 0,888, "fases
   uniformes", e usado como evidência positiva. O valor correto é R = 0,388-0,454, **p < 10⁻¹⁰, fases
   fortemente alinhadas em abr/ago/dez** — provável bug de unidade. O achado sobrevive por outros
   caminhos, mas a afirmação de uniformidade teria sido derrubada por qualquer membro da banca que
   refizesse o teste.

**Regra que sai daí:** todo número que for para a dissertação precisa ser recalculado por caminho
independente, e todo bloco reportado na prosa precisa estar no script reprodutível. Dois blocos da
rodada 2 estavam só na prosa — e um deles era exatamente o do erro nº 5.

### 4.2 O que foi verificado e está correto

| Verificação | Resultado |
|---|---|
| Códigos municipais | 185, todos de PE — nenhum fora do estado, nenhum de município ignorado |
| Soma dos municípios × total estadual | Confere em todas as competências testadas |
| Denominador total | 2.710.671 mulheres de 25 a 64 anos em PE (2025), e 4.968.722 mulheres no total (IBGE ~4,96M), 19,0% em 0-14 e 12,2% em 65+ |
| Pirâmide etária | Coerente. O crescimento diferencial por faixa (−10,9% em 015-019, +25,0% em 060-064) é onda de coorte esperada para a transição demográfica pernambucana |
| Municípios com denominador zero | Nenhum. Menor: Fernando de Noronha, 1.069 mulheres |
| `pop_alvo` | Constante em (município, faixa, ano) — verificado por asserção |
| Zeros no painel, grão agregado | 395 de 18.500 células (2,1%), concentrados em municípios pequenos; maior sequência é Fernando de Noronha, 8 meses. **No grão município × faixa × mês são 12,7%** (§3.4) — os dois números são compatíveis, e o que importa para o modelo de contagem é o segundo |
| Séries com valores repetidos | Seis municípios com poucos valores distintos, todos pequenos. **Não é o bug do pipeline anterior**, que replicava a mesma competência em todos os anos |
| `pipeline.py` e `dashboard.json` nas competências ausentes | Corretos: `null` em 2022-08 e 2022-09 em `series.citopatologico` e `razao_mensal` (linha 599, `None if m in invalidas else ...`) |
| Reconciliação `qualidade.json` × painel | Bate ao dígito em 8 dos 9 anos. A única divergência é 2022, e é o achado do item 2 da tabela acima |
| `pop_defasada` | `True` apenas nas linhas de 2026, que carregam `pop_ano = 2025` |
| Reconferência por caminho independente | Os headlines de estrutura etária foram recalculados com leitor CSV puro, sem pandas, com asserções (razão 015-019 em 2018 = 0,1793; 060-064 em 2025 = 0,2987; 050-054 em 2025 = 0,3851; exames <25 em 2025 = 37.636) |
| Gini ponderado | Recalculado com duas implementações independentes (Lorenz por trapézio e diferença média par-a-par ponderada) — bate nas quatro casas |

---

## 5. O que foi refutado

Para que ninguém persiga a mesma miragem duas vezes. Cada item traz o número que o mata.

### Sobre o fenômeno

| Hipótese | Veredito |
|---|---|
| **Existe periodicidade quadrimestral (ciclo de apuração do C7) na produção** | **Não existe.** 1,47% da potência espectral, rank 14 de 24, p = 0,479 contra bootstrap sob nula de zero sinal quadrimestral. Dummy abr/ago/dez +6,1% (p = 0,152) vem inteiro de agosto; **dezembro, mês de fechamento do 3º quadrimestre, é −0,1%**. DiD pré/pós-Previne: +1,6 pp. Amplitude do k=3: 3,7% |
| Elevação no fim do quadrimestre como sinal fraco | Descartada. Um ciclo de apuração genuíno não pularia dezembro |
| **Arraste de virada de ano: janeiro inflado por lançamento retroativo de dezembro** | **Refutado na direção oposta.** jan/dez-anterior é 0,802 em média, abaixo de 0,86 nos sete anos, e janeiro tem 21,6 dias úteis (acima da média). Não há acúmulo empurrado para janeiro; há uma parada |
| O vale de janeiro está se aprofundando | Refutado. Interação mês × tendência dá janeiro p = 0,066, o menor dos doze, mas junho dá p = 0,078 na direção oposta e **Bonferroni leva o menor p a 0,787**. Tirando 2025, a tendência cai para p = 0,145. E nov/2024–mar/2025 é uma depressão de cinco meses, não um janeiro |
| A queda de janeiro é parada do processamento laboratorial | Contrariado. O efeito de janeiro é **monótono na idade** (−22,6% em 25-29 a −5,4% em 75-79, Spearman rho = 0,864, p = 0,0001). O mesmo laboratório processa todas as lâminas |
| A sazonalidade do citopatológico reflete demanda por rastreamento | Falso. É indistinguível da do controle (r = 0,9937). Quando existe campanha, ela aparece: mamografia tem outubro **+44,4%** e novembro +27,1%; o citopatológico tem +14,4% e o controle +12,0% no mesmo mês |
| A amplitude sazonal encolheu depois da pandemia | Artefato de spline de 8 nós mais bordas de média móvel. No desenho balanceado a amplitude **cresce**, de 37,0% para 55,2% |
| Pico espectral em 10,67 meses (o ciclo não seria anual) | Vazamento espectral do transiente da COVID no meio da série. Na janela limpa o pico é semestral e anual; 1,25 ciclos/ano cai para 10,9% |
| Deriva monotônica da fase do ciclo anual, de dezembro para julho | Rebaixado de achado a indício. Janelas móveis se sobrepõem e as iniciais são dominadas pelo colapso de 2020; a regressão do mês de pico ano a ano dá −0,28 mês/ano com p = 0,534, e o teste de interação Fourier × tempo p = 0,211 |
| Dias úteis explicam a sazonalidade | Correlação 0,22; controlando, a amplitude **sobe** de 43,1% para 48,7%. Explica fevereiro e nada mais |
| **Jovens (015-024) e idosas (065+) têm dinâmicas opostas que se cancelam no controle** | **Testado e falso.** r de nível +0,703, r de 1ª diferença +0,680, r durante COVID +0,97; índices de 2025 base 2018 praticamente iguais (61,9 e 59,3); o sd da variação mensal do agregado é igual ao de cada metade. A heterogeneidade existe, mas o eixo é outro (§3.1) |
| A pandemia revelou iniquidade etária dentro da faixa-alvo | Não há. No fundo do choque (abr-jul/2020) a amplitude entre as oito faixas é de **2,5 pp**; no agregado anual, 2,9 pp; a regressão no ponto médio da idade dá coeficiente +0,042 pp/ano, R² = 0,25 |
| **O gradiente etário da recuperação (velhas voltaram, jovens não)** | **Refutado — é composição do denominador.** Em razão, todas as faixas caem entre −3,8% e −15,3% e a mais jovem cai **menos** que quatro das mais velhas. O gradiente da coluna de contagem é a coluna de pop_alvo (060-064 cresceu 23,0%, 025-029 encolheu 2,2%) |
| O agregado 25-64 esconde mudança de perfil etário | Descartado com número: padronização direta move a razão de 2025 de 0,3418 para 0,3409 — **0,26% relativo**, nunca acima de 0,10 pp em ano nenhum. Padronização invertida: máximo 0,045 pp |
| Houve deslocamento etário substantivo do rastreamento | 84% é demografia pura. A idade média da rastreada sobe 1,12 ano, a da população 0,94 — **deslocamento líquido de 0,18 ano em sete anos** |
| A composição etária quebra em τ3 | Descartado após placebo, e é autocorreção. Janela simétrica dá −3,00 (ou −4,72 corrigindo o bug de `iloc`) com 9 de 25 placebos iguais ou maiores, **p = 0,32-0,36** |
| **A queda dos exames em menores de 25 cobre 96% do déficit da faixa-alvo ("realocação de custo zero")** | **Refutado.** O 96,2% é artefato da referência (a faixa mais rastreada de 2025). Variando: 6% (meta INCA 1,0) a 369% (média do alvo). O número defensável é o absoluto: 37.636 exames/ano em 15-24, 13,0% do volume acumulado |
| 18,4% dos exames estão fora da diretriz | Errado. 13,0% são <25 (contraindicação dura); os 5,4% em 65+ têm indicação condicional ao histórico, que este painel não tem. "Um em cada cinco" vira "um em cada oito" |
| 060-064 é a faixa desassistida, onde a mortalidade é maior | Inverte o quadro. Em **contagem**, 060-064 cresceu +20,0% entre 2019 e 2025 e 065-069 caiu só −7,4%; a queda das razões é dominada por crescimento populacional de ~20% |
| **Houve municípios resilientes à pandemia** | Não houve. Só Exu e Santa Cruz ficam acima de −50% em abr-jul/2020, com bases pré de 3,7 e 11,6 exames/mês (razões 0,016 e 0,043) e níveis posteriores de 39× e 5,5× o "pré". É sub-registro no denominador da comparação |
| O choque de 2020 foi puro choque de oferta, sem componente de demanda | Não se sustenta como inferência. Os mínimos comparados estão em meses diferentes (mamografia lidera por 1-2 meses, que é o lag de liberação), e nenhuma das três séries é exógena a nenhum dos dois choques |
| **A pandemia aumentou a desigualdade entre municípios e ela nunca voltou** | Falso. O Gini ponderado cai para **0,2601 em 2022, o menor da série de oito anos**. A recuperação foi igualizadora. A alta de 2025 é evento posterior e independente — e metade dela é registro (Δ cai de +0,063 para +0,031 excluindo os 33 municípios com razão <0,1) |
| Municípios pequenos têm razão maior porque a razão é instável neles | Falso. O CV temporal é plano entre quintis (0,221 a 0,184). E a razão **ponderada pela população** por quintil cai monotonicamente, 0,582 → 0,346 — imune ao argumento de números pequenos |
| Os municípios com razão >1,0 registram mulheres de municípios vizinhos | Falsificado no nível do bloco. Os 19 municípios do Pajeú, incluindo os três mais vazios do estado, fecham em **0,656** contra 0,330 no resto. Se fosse redistribuição interna, fecharia no nível estadual; fecha ao dobro. Robusto à composição da lista |
| Os >1,0 são instabilidade de denominador pequeno ou despejo retroativo | Refutado. Cinco municípios estão acima de 1,0 em **três anos consecutivos** (Brejão 1,35/1,06/1,34; Ingazeira 1,44/1,19/1,25; Terezinha; Carnaíba; Machados). Um lote inflaria um ano e deprimiria os vizinhos |
| Os >1,0 rastreiam fora da faixa e registram dentro | Sem evidência — mas o teste está mal especificado (compara participação, não taxa por mulher). Refazer |
| Co-rastreamento com mamografia explica o pico em 050-054 e o excesso em 065-069 | Descartado. Spearman da propensão municipal fora-de-faixa com intensidade de mamografia: 065-069 (coberta) +0,218 e +0,308; 070-074 (**não** coberta) +0,240 e +0,179. Praticamente iguais. É "municípios que fazem mais de tudo fazem mais de tudo" |
| Os exames que faltam no São Francisco migraram para o Pajeú, ou os dos 35 municípios em colapso migraram para vizinhos | Não migraram. Déficit SF e excedente Pajeú têm a mesma ordem de grandeza mas correlação temporal **−0,15**; e o volume dos outros 150 municípios cai de 339.930 (2023) para 303.120 (2025). Não há sumidouro nem fonte |
| Os exames da RMR passaram a ser atribuídos a Recife | Recife é o maior déficit individual do estado e o bloco RMR inteiro está em déficit de +141.786 |
| A queda de 2025 é a cauda provisória chegando antes | Não é. A cauda começa em jan/2026, o resto do estado mantém 26.483 exames em dez/2025, e a razão de nov e dez/2025 (0,355 e 0,358) está acima de dez/2024 (0,310) |
| A queda do rastreamento em <25 é um movimento estadual homogêneo | Descartado como afirmação de magnitude: Recife responde por parte grande da queda e 71 dos 185 municípios **aumentaram**. O que é estadual é o diferencial dentro-vs-fora (sobrevive à exclusão das 5 maiores e é positivo em 142 de 175 municípios) |
| A pirâmide etária do denominador tem problema | Descartada por verificação: 4.968.722 mulheres em PE em 2025 (IBGE ~4,96M), 19,0% em 0-14, 12,2% em 65+, e o total 25-64 de 2.710.671 bate entre o JSON e o painel |
| A "convergência à diretriz" é movimento bilateral | Não é. 88% da queda do share fora-de-faixa é o lado <25 (−4,56 pp de −5,19 pp); o lado 65+ entrega 12%. A proporção é 7:1 |

### Sobre o desenho e a inferência

| Hipótese | Veredito |
|---|---|
| **Os picos de lançamento em lote são sazonais (metade em nov/dez/jan)** | **Refutado por dois caminhos.** (a) A janela de 3 meses foi escolhida depois de ver o histograma; Monte Carlo com 20.000 réplicas tomando o máximo entre as 12 janelas leva p de 0,0052 para **0,0513**. (b) Com detector de limiar relativo ao mesmo mês em outros anos saem 61 picos com nov+dez+jan = 17 de 61 (28% contra 25%), **p = 0,348**, e o mês modal passa a ser **maio** |
| **O buraco de ago/set 2022 fabrica quebras estruturais espúrias** | **Refutado.** (a) Interpolando os dois meses, as duas maiores quebras depois de 2022-07 são exatamente **os meses interpolados** (−4,90 e −4,88); meses inventados não podem liderar o ranking se o buraco fosse a causa. (b) Removendo ago/set de 2020 em vez de 2022, as maiores continuam em 2022. (c) Uma **quadrática pura** (zero ruído, zero buraco) devolve quebra de **−1,02 %/ano em toda data, dp exatamente 0,000** — o viés é curvatura, não competência ausente. A concentração em 2022 é mecânica: com win=24 numa série de 94, os nós elegíveis vão de 2020-01 a 2023-12 e as datas de 2022 são as de maior alavancagem. **O tratamento proposto era pior que o problema**: proibir nós a menos de 12 meses de ago/set 2022 amputaria 25 meses, o terço central da série |
| A igualdade sazonal desfecho-controle (F = 0,06, p = 1,00) é "ausência total de diferença" | Não é. Um F de 0,06 com 11 gl está 16× abaixo do esperado sob a nula. Partindo o **próprio desfecho** ao meio (25-29 contra 30-64) o mesmo teste dá F = 0,34, p = 0,976 — o controle sai mais parecido com o desfecho do que o desfecho é consigo mesmo. É sinal de denominador inflado por resíduo comum, não evidência de igualdade |
| O segundo par de harmônicos é dominante | Refutado. O F = 13,39 vs 8,31 é artefato do teste sequencial; contra o mesmo modelo cheio dá 12,19 vs 13,39, amplitudes 0,0984 e 0,1031. Dentro de cada período o harmônico **anual** domina (razão 0,83 e 0,94) |
| A deriva do controle é uma reta suave (R² = 0,934), não degrau | Falso. Por biênio: −2,35 → −3,31 → −5,76 → −7,97 %/ano — **triplica**. Spline com nó em τ1 dá −2,68 %/ano, t = −3,43. R² alto de uma reta ajustada a uma curva convexa não é prova de linearidade |
| A deriva do controle é secular e não atribuível a marco específico | Contradito pela aceleração: metade da deriva total é posterior a jan/2020. Mas o teste de quebra é indecidível — 10 de 10 placebos produzem quebras igualmente significativas sob pré-tendência linear, porque a deriva acelera continuamente |
| A deriva do controle é demografia, recomposição municipal, picos retroativos ou cauda provisória | Os quatro descartados: 3,8%; mediana intramunicipal +0,557 %/mês com Wilcoxon p < 10⁻⁵; +0,597 %/mês excluindo os 28 picos (aumenta); todas as janelas terminam em dez/2025 |
| O controle fabrica falso positivo no teste de falsificação | **Não se materializa.** Centrar os placebos não muda τ4 (p = 0,09 nos dois) e torna τ3 mais conservador (0,36 → 0,73). O que move τ4 é casar os meses (p = 0,18). Com tendência de grupo e randomização, τ3 = +0,32% com 92% das datas produzindo mais |
| A mamografia seria melhor controle | Pior em correlação, erro de acompanhamento, variância de placebo e pré-tendência, com choque pandêmico em mês diferente. O único quesito em que ganha — placebos centrados em zero — é um **teste sem poder** (IC95 da média [−10,4%; +8,1%]; poder 0,19 para detectar o viés observado) |
| O controle atual é inútil | Não é esse o achado. Ele remove com eficiência o ruído de remessa retroativa (100% dos 28 picos aparecem nas duas séries, com amplificação praticamente igual) e compartilha o choque pandêmico |
| A correlação desfecho-mamografia "vira negativa" ao remover sazonalidade (r = −0,421) | Artefato de dummies de mês com ~12 gl efetivos. Com harmônicos: +0,254 (K=1), −0,157 (K=2), −0,176 (K=3). A afirmação honesta é que **vai a zero**, não que se inverte |
| Os municípios grandes são proporcionalmente mais superdispersos | Artefato matemático: CV·√μ é monótona em μ quando o CV é constante. O CV de fato **cai** com o porte (Spearman −0,297, p = 4,0e-5) |
| Os 12,7% de zeros não exigem modelo zero-inflado (a NB gera zeros sozinha) | Falha no teste que a própria hipótese definiu como decisivo: P(0) observado excede o predito sob NB2 em todos os quintis, e **ZINB vence NB2 por ΔAIC = 660** |
| "A variância é 5× a 173× a média" | Número marginal e enganoso. A dispersão de Pearson **condicional** (que é o que o GLMM enfrenta) é 3,4 no Q1 e 14,5 no Q5 |
| O bloco do São Francisco registra mamografia em nível estadual | Falso. SF/resto de PE em mamografia é ~0,61 em média e **abaixo do estado nos oito anos**. O número original vem de 3 dos 8 municípios em 1 dos 8 anos |
| A recuperação de τ2b é artefato do bloco São Francisco ligando em out-nov/2020 | Descartado: o resto de PE também sobe de 0,231 para 0,346, e o bloco contribui com 6.641 exames em 2021 |
| A recuperação foi mais lenta nos municípios menores | **Não há padrão aparente**, com todas as letras. Spearman de log(pop) contra tempo de retorno: −0,051 (p = 0,50) por um critério e +0,176 (p = 0,021) por outro — **sinais opostos**. Nível 2024-25 −0,059 (p = 0,42); déficit relativo +0,115 (p = 0,12); queda de abr-jul/2020 −0,058 (p = 0,44). Cinco nulos e um marginal com R² de 3% |
| Os municípios menores caíram mais fundo em 2020 | Artefato de piso. rho = +0,430 usando o **mínimo** de 2020, mas 81 municípios registram algum mês com zero e chegar a zero com base de 30/mês é ruído de contagem. Usando a média de abr-jul/2020: **rho = −0,058, p = 0,44** |
| O filtro base ≥60 exames/mês "elimina o artefato" no teste de porte | Não elimina artefato, elimina poder. Bootstrap do rho no subgrupo filtrado dá IC95 [−0,251; +0,191], que **contém** o +0,176 original; subamostras aleatórias do mesmo n dão rho médio +0,173 e só atingem p<0,05 em 34% das vezes. E o único sinal significativo da tabela diz que os **maiores** demoraram mais — consistente com o déficit metropolitano, não com a hipótese testada |
| "Treze municípios nunca voltaram ao patamar pré-pandemia" | Subestima em cinco vezes. É um critério de "nunca encostou". Quem **está abaixo hoje** são **62 municípios e 1.094.146 mulheres** (40,4% do estado), encabeçados por Jaboatão e Caruaru |
| O estado "repagou 36% do déficit e voltou a acumular em 2025" | Artefato da escolha de base. Com base = só 2019 o repagamento é **89%** e a dívida é residual (+16.884). O único número robusto é o da fase aguda (145-176 mil) |
| A recuperação foi mais lenta nos municípios mais pobres | **Não testável com este painel.** Não há renda, IDHM, PIB per capita nem cobertura de ESF nos dados; só porte populacional. Exige join externo por `cod_ibge` |
| "45% do degrau de τ3 é o colapso laboratorial" | Enfraquecido: a fração varia de **31% a 77%** conforme o mês de corte (2023-11 → 77%; 2024-05 → 51%; 2024-11 → 31%; 2025-01 → 41%). E a data está errada — o evento começa em dez/2023 e contamina **ambos** os braços |
| A concentração de 111 degraus em poucos meses é evidência de choque administrativo comum | A estatística é ininterpretável. Um nulo com sazonalidade e tendência estaduais e **zero degraus verdadeiros** produz 58 degraus e cluster máximo de 17,9 num único mês, contra os 14 reais de mar/2019. O que sustenta o mecanismo é o contraste com a mamografia |

---

## 6. O que ainda não foi olhado

Os cinco ângulos que a primeira rodada listou como pendentes foram cobertos. O que resta são coisas
que **exigem dado que não está nestes arquivos**, ou testes que só fazem sentido depois de decisões
de protocolo. Em ordem de retorno esperado.

### 6.1 Exige extração nova do TABNET/SISCAN

1. **Reextrair ago e set de 2022.** É a pendência mais barata e a mais consequente: 31.519 exames
   existem na fonte (§4, item 2) e o estudo os descarta sem saber. A resposta muda o tratamento de
   exclusão listwise para censura.
2. **`Motivo do exame` estratificado por faixa etária.** As três tabulações de qualidade cobrem só
   25-64. Sem isso não se pode afirmar que os 37.636 exames/ano em 15-24 são rastreamento
   contraindicado, e não seguimento ou investigação de sintoma (§2.9). Se as <25 seguirem a
   distribuição das 25-64 (97,1% rastreamento), o achado se mantém quase inteiro — mas isso precisa
   ser verificado, não suposto.
3. **`Tempo de liberação` estratificado por série (desfecho vs controle) e por município.** É o único
   teste da "cegueira mecanicista" do controle (§3.1): se a distribuição de defasagem mudar após τ3 no
   desfecho mas não no controle, o mecanismo de registro é separável. A tabulação atual é anual, três
   categorias, sem quebra por série — o teste **não pode ser rodado** com o que existe.
4. **SISCAN por município de RESIDÊNCIA, não por local de atendimento.** Decide três coisas de uma
   vez: se o vazio do São Francisco é assistência ou atribuição (§2.2); se a razão >1,0 do Pajeú é
   sobrerrastreamento ou fluxo de vizinhos (§2.16); e se os achados municipais precisam de ressalva
   geral. Verificar primeiro qual é a atribuição do painel atual.
5. **Rol completo de procedimentos SIA/SISCAN de citopatologia.** A única explicação concorrente que
   estes dados não descartam para o colapso da Mata Meridional é migração para outro código
   (0203010086 vs 0201020033, ou outro). Um único cruzamento resolve.
6. **Série de 2014-2017, que existe no SIA.** Triplicaria o pré-pandemia e é a única forma de dar
   poder real ao teste de estabilidade da amplitude sazonal (§4, item 17). Sem isso, qualquer
   afirmação sobre estabilidade é opinião com p-valor.
7. **Um extrato posterior das competências de 2024-2025.** Testa duas coisas: se jan/2025 sobe (então
   é maturação de lançamento, não parada) e se dez/2025 ainda cresce (a cauda de consolidação do
   citopatológico pode ser mais longa que os seis meses declarados — a mamografia não tem cauda
   nenhuma e o cito cai 13,8% em 2026H1).

### 6.2 Exige join externo por `cod_ibge`

8. **CNES: laboratórios de citopatologia habilitados, por município e por período.** Datas de
   habilitação, descredenciamento e troca de prestador entre out/2023 e jan/2024 (Mata Meridional) e
   ao longo de 2019 (blocos de mar-abr/2019). É a verificação decisiva de três achados e não é
   análise — é consulta.
9. **Cobertura de planos de saúde (ANS).** Recife ~30%, Sertão <5%. Decide se o gradiente de porte é
   real ou misspecificação do denominador (§2.15), e é candidata a covariável de nível 2 no GLMM. Dado
   público, join trivial.
10. **SINASC por faixa etária materna.** A hipótese concorrente mais provável para a queda dos exames
    em 15-24 é redução de contatos de pré-natal e planejamento familiar, não conformidade à diretriz
    (§2.8). É a única explicação não-política sobre a mesa e não foi afastada.
11. **Indicadores socioeconômicos municipais (IDHM, PIB per capita, cobertura de ESF).** A pergunta
    "a recuperação foi mais lenta nos municípios mais pobres" é **não testável** com este painel —
    não há nenhuma variável socioeconômica nele, só porte populacional.
12. **Microrregião, mesorregião e GERES a partir de `data/bruto/municipios_pe.json`.** O arquivo já
    tem os quatro níveis para os 185 municípios e não foi usado: toda a análise geográfica das duas
    rodadas foi feita com listas de nomes escritas à mão. Foi assim que "22 da Zona da Mata Sul"
    escondeu o 21 de 21 com Fisher p = 4,2e-18, e que Parnamirim entrou numa GERES a que não pertence.

### 6.3 Testes que os dados permitem e ninguém rodou

13. **Detector de integridade de registro pela razão cito/mamografia, aplicado aos 185 municípios.**
    Petrolina é o caso limpo (citologia caótica, mamografia estável, mesma população e mesma rede) e o
    detector existe implicitamente em vários achados. Rodá-lo de forma sistemática produziria uma
    lista objetiva de municípios com série de citologia não interpretável, no lugar do julgamento caso
    a caso.
14. **Ajustar os três modelos de contagem no grão real** (município × faixa × mês, offset
    log(pop_alvo/3), efeito aleatório de município): Poisson, NB2, ZINB, comparados por AIC/BIC **e
    por rootograma**. O teste sem efeito aleatório já indica ZINB por ΔAIC = 660 (§3.4); falta refazer
    com a estrutura completa.
15. **Testar inclinação aleatória no primeiro par de Fourier por município.** Se a variância do efeito
    aleatório for significativa, os erros-padrão de τ3 mudam e o IC honesto fica mais largo — o que é
    exatamente o que o teste de falsificação pediu (§3.3c).
16. **Rodar o teste de falsificação de dez placebos sobre a série sem a Mata Meridional e sem o bloco
    São Francisco**, e ver se algum marco muda de veredito. Foi recomendado duas vezes e não foi feito.
17. **Testar se 2023 é pico de recuperação represada.** 2023 é o máximo histórico (376.549, 21% acima
    de 2018) e nenhuma rodada tratou disso. Se for lançamento do estoque de 2020-21, a "queda de
    2024-25" é em parte regressão à média (§2.22).
18. **Refazer o gradiente por distância à faixa dentro de municípios grandes isoladamente**, e testar
    se ele muda de inclinação em τ1/τ3. É o que separa "dose-resposta a incentivo" de "faixas pequenas
    caíram mais" (§3.1).
19. **Cruzar os municípios com razão >1,0 contra a tabulação de intervalo de coleta.** Se o intervalo
    mediano for menor que o do estado, o sobrerrastreamento fica demonstrado e o achado vira
    substantivo em vez de descritivo (§2.16).
20. **Repetir a escolha de K e o perfil sazonal com a razão em vez da contagem, e com GLMM
    Poisson/NB em vez de OLS em log.** O denominador é anual e não deveria mudar nada dentro do ano —
    se mudar, há erro na construção do denominador. E a escolha de K pode mudar se a variância não for
    proporcional ao quadrado da média.
21. **Cruzar o CNES dos estabelecimentos que produzem exames dentro e fora da faixa 25-64.** Se a
    sobreposição for perto de 100%, a igualdade sazonal desfecho-controle vira "os mesmos laboratórios
    processam tudo" — afirmação mais fraca, mas que ainda mata a leitura comportamental (§2.12).

### 6.4 O que provavelmente não vale a pena

- **Trocar o controle por mamografia.** Já respondido: pior em tudo menos num quesito, e esse quesito
  é um teste sem poder (§3.1).
- **Acrescentar K=3 harmônicos.** O que falta ao modelo é AR(1), não mais harmônicos (§2.12).
- **Regra de distância mínima a ago/set 2022 nos testes de quebra.** Custaria o terço central da
  janela para corrigir um efeito que não existe (§5).
- **Refinar o critério dos picos de lote para achar "o número certo".** Ele varia de 26 a 61 conforme
  a definição e nenhuma conclusão muda; o que importa é fixá-lo antes, não acertá-lo (§4, item 13).
