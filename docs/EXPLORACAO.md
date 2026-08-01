# Exploração dos dados — o que aparece quando se olha de outros ângulos

Análises de 01/08/2026 sobre o painel de 339.660 linhas. Scripts em
`scratchpad/falsificacao.py` e `scratchpad/consistencia.py`.

Esta rodada procurou **anomalias antes de padrões**. O achado principal é negativo, e é o mais
importante do documento.

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
| τ4 | mai/2025 | 0,3558 | 0,3685 | +3,6% |

### Datas-placebo

Dez datas sem evento normativo produziram variações de **+0,4% a +45,3%**, com mediana de
**14,2%** em valor absoluto e desvio-padrão de 19,7 pontos percentuais. Algumas amostras:
set/2019 → −30,8%; jul/2021 → +45,3%; mar/2022 → +14,7%; nov/2024 → −13,4%.

### Veredito

| Marco | Δ | Placebos tão grandes ou maiores | p aproximado | Leitura |
|-------|---|--------------------------------|--------------|---------|
| τ1 | −39,2% | 1 de 10 | 0,18 | limítrofe |
| τ2 | −42,0% | 1 de 10 | 0,18 | limítrofe |
| τ2b | +52,5% | 0 de 10 | 0,09 | distinguível |
| **τ3** | **−13,0%** | **6 de 10** | **0,64** | **indistinguível de ruído** |
| τ4 | +3,6% | 8 de 10 | 0,82 | indistinguível de ruído |

**τ3 é o estimando primário do estudo.** Uma variação de −13% depois de maio de 2024 é menor que a
mediana das variações que datas escolhidas ao acaso produzem nesta série. Seis dos dez placebos
produziram degraus iguais ou maiores.

τ4 é ainda mais claro: +3,6% é menor que oito dos dez placebos — o que, aliás, é coerente com a
premissa normativa de que o C7 nunca carregou risco financeiro de perda dentro da janela.

Só a recuperação pós-pandêmica (τ2b) se destaca inequivocamente. τ1 e τ2 aparecem como limítrofes,
mas são inseparáveis um do outro e o que se mede ali é o choque da pandemia, não o Previne Brasil.

### O que isto significa, e o que não significa

**Não significa** que o estudo esteja errado ou seja inviável. A comparação acima é descritiva e
grosseira: usa a série estadual agregada, ignora tendência pré-existente, sazonalidade,
autocorrelação e toda a informação do painel municipal. O GLMM proposto controla tudo isso e tem
mais poder para separar um degrau de uma flutuação.

**Significa** três coisas concretas:

1. **O efeito, se existir, é pequeno diante da variabilidade natural da série.** Qualquer estimativa
   que o modelo produza para τ3 precisa vir acompanhada de intervalo de confiança honesto, e a
   discussão precisa antecipar que o intervalo provavelmente conterá o nulo.
2. **O teste de falsificação precisa ir para o protocolo, com placebos pré-especificados**, e o
   resultado precisa ser reportado seja qual for. Fazê-lo depois de ver o resultado do modelo é
   pesca.
3. **A hipótese nula deixa de ser um resultado decepcionante e passa a ser o resultado esperado.**
   Isso é coerente com a cronologia normativa: o componente de qualidade foi prorrogado, e não
   houve risco financeiro sobre o C7 no período. Um estudo que prevê ausência de efeito e a
   encontra, com poder documentado para detectar efeitos de determinada magnitude, é um estudo
   bem-sucedido. Um que promete detectar efeito e não encontra parece fracasso.

A conclusão operacional é que a **análise de poder por simulação deixa de ser formalidade**. Ela
precisa dizer qual é a menor mudança detectável com 80% de poder, e essa magnitude precisa ser
declarada antes da coleta definitiva.

## 2. Lançamento retroativo em lote

Trinta e seis competências municipais têm volume superior a quatro vezes a mediana dos seis meses
vizinhos, com excesso acima de 200 exames, e voltam ao patamar normal no mês seguinte. São despejos
de registro acumulado, não atividade real.

| Município | Competência | Mediana vizinha | Pico | Razão |
|-----------|-------------|-----------------|------|-------|
| Ipojuca | jan/2021 | 28 | 827 | 29× |
| Maraial | mai/2021 | 12 | 361 | 29× |
| Belo Jardim | nov/2020 | 9 | 236 | 26× |
| **Goiana** | **fev/2025** | 157 | **3.089** | 20× |
| Vitória de Santo Antão | jun/2020 | 24 | 440 | 18× |
| Escada | ago/2021 | 202 | 2.921 | 14× |

O excesso soma **18.804 exames, 0,73% do total** — pequeno no agregado estadual, devastador na série
do município afetado. Escada passa de 220 para 2.921 e volta a 241 no mês seguinte.

**O que preocupa não é o volume, é a localização: 14 dos 36 picos caem a menos de três meses de
algum marco.** Goiana, o quarto maior, ocorre em fevereiro de 2025 — três meses antes de τ4.

### Tratamento necessário

Isto não estava previsto no protocolo e precisa entrar. Três opções, em ordem de preferência:

1. **Modelar como observação influente**, identificando os picos por critério pré-especificado (o
   usado aqui serve: mais de quatro vezes a mediana móvel de seis meses, com excesso absoluto acima
   de um limiar) e verificando a estabilidade das estimativas com e sem eles.
2. **Winsorizar** as competências identificadas ao percentil da própria série municipal.
3. **Redistribuir** o excesso pelos meses anteriores — tecnicamente mais correto, já que é isso que
   de fato aconteceu, mas exige suposição sobre o período de acúmulo.

A opção 1 é a mais defensável porque não altera o dado, apenas documenta a sensibilidade a ele.

## 3. O que foi verificado e está correto

| Verificação | Resultado |
|-------------|-----------|
| Códigos municipais | 185, todos de PE — nenhum fora do estado, nenhum de município ignorado |
| Soma dos municípios × total estadual | Confere em todas as competências testadas |
| Denominador total | 2.710.671 mulheres de 25 a 64 anos em PE (2025) — compatível com a população estadual |
| Municípios com denominador zero | Nenhum |
| Menor denominador | Fernando de Noronha, 1.069 mulheres — pequeno, mas não zero |
| Zeros no painel | 395 de 18.500 células (2,1%), concentrados em municípios pequenos |
| Maior sequência de zeros | Fernando de Noronha, 8 meses seguidos |
| Séries com valores repetidos | Seis municípios com poucos valores distintos — todos pequenos, onde valores baixos naturalmente se repetem. **Não é o bug do pipeline anterior**, que replicava a mesma competência em todos os anos |

Os zeros são plausíveis: concentram-se onde a população-alvo é de poucas centenas de mulheres e
alguns meses sem nenhum exame é o esperado. Nenhum município grande tem sequência de zeros.

## 4. Correção a um erro desta própria análise

A primeira versão do script de consistência reportou "225.805 mulheres de 25 a 64 anos em PE", o
que teria sido um problema gravíssimo de denominador. Era erro do script de verificação, que
dividia por doze um valor que não estava replicado por competência. O valor correto é 2.710.671.

Fica registrado porque ilustra o risco destas análises: **um script de verificação com bug produz
um alarme falso tão convincente quanto um achado real.** Todo número deste documento foi conferido
contra uma segunda fonte ou recalculado por caminho independente.

## 5. O que ainda não foi olhado

Esta rodada cobriu falsificação e consistência. Ficaram de fora, por interrupção do processamento:

- **Sazonalidade**: se o padrão é estável ao longo dos anos, quantos harmônicos são necessários, e
  sobretudo se existe periodicidade **quadrimestral** — que seria achado forte, por coincidir com o
  ciclo de apuração dos indicadores de pagamento.
- **Estrutura etária**: deslocamento entre faixas ao longo da janela, resposta diferencial à
  pandemia por faixa, e sobrerrastreamento em mulheres abaixo de 25 anos.
- **Desigualdade**: Gini entre municípios e sua evolução; quantos municípios superam a razão de 1,0
  e se isso é sobrerrastreamento ou artefato de denominador pequeno.
- **Recuperação pós-COVID por município**: quantos nunca voltaram ao patamar pré-pandemia, e o
  déficit acumulado de exames — que é o número mais útil para a gestão estadual.
- **Validade do controle**: se a série de mulheres fora da faixa de 25 a 64 acompanha o desfecho no
  período pré-intervenção, e se as faixas jovens e idosas têm dinâmicas opostas que se cancelam ao
  serem agregadas num controle único.
