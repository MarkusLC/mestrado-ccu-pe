# IDENTIFICAÇÃO

**Candidata:** [VERIFICAR: nome completo da candidata, conforme documento de identidade]

**Programa:** Programa de Pós-Graduação em Saúde Pública — Mestrado Acadêmico (PPGSP/IAM/Fiocruz PE), Turma 2027

**Área de concentração:** Políticas de Saúde

**Linha de pesquisa:** Avaliação de sistemas, programas e serviços de atenção e vigilância da saúde

**Orientador(a) pretendido(a):** [VERIFICAR: nome do orientador, conferido na relação nominal do item 4.4 do edital vigente. A indicação é requisito de homologação (item 7.1.3) e a coerência com a linha do orientador vale 1,5 ponto no Anexo VII]

**Ano:** 2026 (ingresso em 2027)

**Título:** Cobertura de exames citopatológicos do câncer do colo do útero nos municípios de Pernambuco durante a transição Previne Brasil → Saúde Brasil 360: estudo ecológico de séries temporais interrompidas

---

# RESUMO

**Introdução.** O câncer do colo do útero é evitável em todos os elos de sua cadeia causal, mas persiste como quarta causa de morte por câncer em mulheres brasileiras, com a única tendência de mortalidade em ascensão no Nordeste. A coleta do citopatológico é atribuição da Atenção Primária, cujo financiamento federal foi reorganizado duas vezes em cinco anos, sem que exista avaliação com contrafactual dessas transições sobre o rastreamento. **Objetivo.** Estimar mudanças de nível e de tendência na produção mensal municipal de exames citopatológicos de rastreamento em mulheres de 25 a 64 anos em Pernambuco, associadas aos pontos de mudança normativos da transição, e caracterizar documentalmente a intensidade efetiva da exposição a incentivo. **Métodos.** Estudo ecológico de séries temporais interrompidas em painel das 185 unidades municipais de Pernambuco, janeiro de 2018 a dezembro de 2026, com extensão confirmatória a dezembro de 2027. Desfecho extraído do SISCAN por município de residência, base independente do sistema que aciona o pagamento. Modelo linear generalizado misto binomial negativo, offset log(população-alvo/36), efeitos aleatórios de município e de competência, AR1 intramunicipal e harmônicos de Fourier. Estimando primário: nível e tendência em maio de 2024, quando a revogação do Previne Brasil retira o incentivo financeiro específico ao rastreamento. Controle por característica: citopatológicos fora da faixa-alvo. Reporte por STROBE e RECORD; protocolo congelado antes da coleta definitiva. **Resultados esperados.** Razões de taxas por ponto de mudança, déficit acumulado em exames, heterogeneidade municipal e matriz de (in)comparabilidade entre o indicador nº 4 e o C7. Todo efeito estimado é resposta de produção, não ganho de cobertura.

**Palavras-chave:** Neoplasias do Colo do Útero; Detecção Precoce de Câncer; Atenção Primária à Saúde; Financiamento da Assistência à Saúde; Análise de Séries Temporais Interrompidas; Pernambuco.

---

# 1 INTRODUÇÃO

## 1.1 Uma neoplasia evitável em todos os elos da cadeia causal

O câncer do colo do útero ocupa posição singular entre as neoplasias de alta incidência: coexistem para ele agente etiológico necessário conhecido, imunização primária eficaz, lesão precursora detectável por exame de baixo custo e tratamento curativo na fase pré-invasiva. A infecção persistente por tipos oncogênicos do papilomavírus humano é condição necessária da doença, e os tipos 16 e 18 respondem por cerca de 70% dos casos; a história natural é lenta, com 15 a 20 anos entre a alteração celular inicial e o carcinoma invasivo em mulheres imunocompetentes (INCA, 2016). Sobre essa base a Organização Mundial da Saúde fixou o limiar de eliminação em 4 ou menos casos por 100 mil mulheres por ano e as metas 90-70-90 para 2030 (WHO, 2020).

O Brasil está distante desse patamar. Para cada ano do triênio 2026-2028 estimam-se 19.310 casos novos, taxa ajustada de 14,76 por 100 mil, terceiro câncer mais incidente em mulheres (INCA, 2026); em 2022 foram 6.983 óbitos, taxa ajustada de 4,79 (INCA, 2025). A taxa ajustada brasileira é cerca de 3,7 vezes o limiar de eliminação, e a modelagem disponível projeta que, mantido o rastreamento citológico oportunístico, o país só o alcançaria entre 2070 e 2075 (CORRÊA et al., 2022). Que uma doença com essas características permaneça como quarta causa de morte por câncer entre mulheres brasileiras não é resultado que a biologia explique.

## 1.2 A persistência é organizacional, e sua distribuição o demonstra

A evidência de que o determinante proximal é organizacional está na distribuição do dano. Norte e Nordeste concentram a maior carga estimada de incidência (taxas brutas de 22,79 e 20,76 por 100 mil, contra 14,06 no Sudeste) (INCA, 2026), e a análise de 171.793 óbitos entre 1980 e 2021 mostra tendência estacionária no país (AAPC −0,3%; IC95% −1,0; 0,4), declinante no Sudeste e no Centro-Oeste, e crescente apenas no Nordeste (AAPC +0,6%; IC95% 0,3; 0,8) — a única macrorregião em ascensão (FERRARI et al., 2025).

O elo organizacional é mensurável em cada etapa. O rastreamento brasileiro é oportunístico: o exame é ofertado quando a mulher procura o serviço por outra razão, e não por convocação de população definida. Já em 2016 o INCA registrava que 20% a 25% dos exames ocorriam fora do grupo etário recomendado e cerca de metade com intervalo de um ano ou menos, produzindo simultaneamente mulheres sobrerrastreadas e mulheres sem qualquer exame (INCA, 2016). A desduplicação por mulher no Sistema de Informação do Câncer quantificou o padrão: no triênio 2021-2023 a cobertura nacional entre mulheres de 25 a 64 anos usuárias exclusivas do SUS foi de 35,6%, contra razão de 47,4 exames por 100 mulheres — superestimação de cerca de um terço, coerente com a média de 1,3 exames por mulher rastreada — e cerca de 3,5 milhões de exames excedentes; redirecionada a mesma produção conforme as diretrizes, a cobertura possível chegaria a 53,9% (RIBEIRO et al., 2025). Parte substancial do déficit não é de recursos, mas de organização da oferta. A consequência clínica aparece no estadiamento: nos Registros Hospitalares de Câncer de 2016 a 2020, excluídos os casos in situ, 49,9% dos diagnósticos ocorreram em estádios III ou IV no país, com o Nordeste em 52,2% (INCA, 2025); na série de 2006 a 2015, a prevalência de estádio avançado foi de 48,4% no país, e a menor cobertura estadual de exame citológico associou-se, em nível contextual, ao diagnóstico tardio (RP 1,08; IC95% 1,01-1,14) (OLIVEIRA et al., 2024).

## 1.3 A Atenção Primária foi refinanciada duas vezes em cinco anos

A coleta do citopatológico é atribuição da Atenção Primária, e o financiamento federal desse nível foi reorganizado duas vezes em menos de um ciclo de gestão. A Portaria GM/MS nº 2.979, de 12 de novembro de 2019, substituiu o custeio por capitação ponderada, pagamento por desempenho e incentivo para ações estratégicas, extinguindo o PAB fixo, o PAB variável e o PMAQ-AB; o desempenho foi consolidado em um Indicador Sintético Final aferido quadrimestralmente no SISAB, no qual o rastreamento do colo do útero figurava como indicador nº 4, com meta de 40%, peso 1 em 10, janela de 36 meses e granularidade municipal (BRASIL, 2022a).

A Portaria GM/MS nº 3.493, de 10 de abril de 2024, instituiu nova metodologia de cofinanciamento do Piso de Atenção Primária, revogou o Previne Brasil (art. 7º, IV) e produziu efeitos financeiros a partir da parcela de maio de 2024 (BRASIL, 2024a). O repasse passou a organizar-se em seis componentes: fixo de manutenção das eSF e eAP; vínculo e acompanhamento territorial; qualidade; implantação e manutenção de programas e serviços; atenção à saúde bucal; e per capita com base populacional. A substituição da capitação por cadastro por um componente fixo por equipe somado a um componente per capita populacional, com estratificação pelo Indicador de Equidade e Dimensionamento, **responde parcialmente à crítica central dirigida ao arranjo de 2019** — a extinção da transferência de base populacional universal (DE SETA; OCKÉ-REIS; RAMOS, 2021). A endogeneidade do cadastro, porém, não desaparece: reaparece no denominador do indicador de qualidade, que é a população vinculada e acompanhada por equipe (BRASIL, 2025c). O deslocamento é de plano — do município para a equipe —, não de natureza. A Portaria GM/MS nº 6.907, de 29 de abril de 2025, incorporou os indicadores de qualidade a partir do segundo quadrimestre de 2025 (BRASIL, 2025a), e o rastreamento do colo do útero deixou de ser indicador próprio: passou a constituir a boa prática (A) do indicador C7, com peso de 20 pontos em 100, sendo o C7 um de sete indicadores do componente de qualidade (BRASIL, 2026a).

*Nota de delimitação.* A designação **Saúde Brasil 360** é adotada na comunicação oficial para um conjunto de iniciativas mais amplo que o financiamento da atenção primária. O objeto deste estudo é estritamente a metodologia de cofinanciamento instituída pela Portaria GM/MS nº 3.493/2024 e suas alterações, à qual o nome é aqui aplicado por economia de referência.

## 1.4 A intensidade do sinal financeiro, em números, e a cronologia que a limita

A intensidade do incentivo é quantificável, e a aritmética é parte do argumento. Sob o Previne Brasil, o indicador nº 4 tinha peso 1 na escala de 10 do ISF, e o ISF de 100% correspondia, em 2022, a R$ 3.225,00 mensais por equipe de Saúde da Família (BRASIL, 2022a): o valor máximo mensal por equipe atribuível ao desempenho em rastreamento do colo do útero era, portanto, da ordem de **R$ 322,50**, sobre um custeio federal por equipe de magnitude muito superior. Sob o novo modelo, a boa prática (A) responde por 20 de 100 pontos de um indicador que é um entre sete do componente de qualidade, o que situa a fração do componente sensível à citologia em cerca de **2,9%** (Apêndice E, item 5).

Duas observações normativas delimitam o que o estudo pode estimar. A primeira: dentro da janela de janeiro de 2018 a dezembro de 2026 o C7 **nunca carregou risco financeiro de perda**. Pela Portaria GM/MS nº 10.994, de 13 de maio de 2026, a classificação "bom" foi garantida até o primeiro quadrimestre de 2026 e, no segundo, a implantação é parcial e assimétrica — apenas equipes "ótimo" recebem valor diferenciado, enquanto "bom", "suficiente" e "regular" recebem todas o valor de "bom" —, com implementação integral só a partir do primeiro quadrimestre de 2027 (BRASIL, 2026b). A segunda: maio de 2025 é marco de mensuração do C7 e de remuneração por desempenho do componente de **vínculo**, não de exposição financeira ao C7 (BRASIL, 2024b; BRASIL, 2025a).

Há ainda razão de desenho, anterior à cronologia. Gurgel et al. (2023), comparando o arranjo brasileiro ao Quality and Outcomes Framework inglês, identificam quatro fragilidades: o pagamento é feito ao município e não ao prestador, tornando o incentivo contingente à decisão local de repasse; há ênfase em qualidade estrutural em lugar de processo; o número de indicadores é maior, o que dilui o foco; e a aferição é menos regular — donde a conclusão de que os incentivos teoricamente gerados eram pouco claros. Russo et al. (2024) mostram, no caso do PMAQ, que a resposta depende do tamanho, da frequência e do destinatário do bônus, com o efeito mais forte associado à periodicidade mensal do repasse ao trabalhador. Os marcos do novo modelo situados na janela transferem recurso ao fundo municipal, sob apuração quadrimestral, sobre fração diluída de um indicador composto: **as condições que a literatura associa a resposta forte estão todas ausentes.**

## 1.5 A resposta documentada é de registro, e a expectativa de efeito sobre a oferta é contida

Reorganizações de financiamento incidem simultaneamente sobre todos os municípios e têm data de vigência em ato normativo — são, no sentido técnico, intervenções de nível populacional, e a resposta documentada é sobretudo de registro. O próprio formulador do Previne Brasil registrou o salto do cadastro de 81 para 103 milhões de pessoas após o anúncio do programa (HARZHEIM, 2020), enquanto a crítica publicada no mesmo fascículo sustentou que cadastro não equivale a acesso (MASSUDA, 2020); o cadastro nacional passou de 98,9 para 154,2 milhões entre o terceiro quadrimestre de 2019 e o de 2021, com o menor crescimento do país no Nordeste (SELLERA et al., 2023). Do lado do numerador, a subnotificação é da ordem de grandeza do fenômeno medido: 108.511 exames citopatológicos realizados e pagos pelo SUS não foram registrados no SISAB no biênio 2021-2022 em uma única área programática do município do Rio de Janeiro (CASTRO-NUNES et al., 2024).

Quanto à oferta, a expectativa a priori é contida. Revisão sistemática de 18 estudos concluiu que incentivos financeiros produziram efeitos parciais ou nulos sobre o rastreamento de mama e de colo do útero (MAURO; ROTUNDO; GIANCOTTI, 2019). A síntese mais atual do QOF registra ganho mediano de 6,1 pontos percentuais em um ano na **introdução** do incentivo, que cai a 0,7 ponto em três anos, contra quedas de 10,7 pontos em um ano e 12,8 em três após a **retirada** (HO et al., 2025) — assimetria coerente com a queda imediata nos doze indicadores desincentivados em 2014 (MINCHIN et al., 2018). Essa assimetria é decisiva aqui, porque maio de 2024 é, dentro da janela, **o único evento cujo mecanismo é retirada de incentivo**.

## 1.6 O que a literatura nacional não respondeu, e por quê

A produção nacional sobre o Previne Brasil é descritiva. Nenhuma unidade federativa alcançou a meta de 40% do indicador de citopatológico, cuja média nacional foi de 14,2% (SCHÖNHOLZER et al., 2023), e os estudos estaduais dedicados ao indicador nº 4 cobrem Sul e Sudeste (CELLA; CORREA; BARANCELLI, 2025). A varredura sistemática não localizou nenhum estudo de séries temporais interrompidas, diferenças-em-diferenças ou controle sintético aplicado ao Previne Brasil — ausência que não decorre de inviabilidade metodológica, uma vez que o desenho quase-experimental já foi aplicado ao PMAQ em 2.346 municípios pareados (FARDOUSI et al., 2022). Sobre o modelo de 2024 a escassez é mais severa: o único texto revisado por pares localizado é um **ensaio** sobre a variação dos repasses em municípios paulistas, sem tocar indicadores nem rastreamento (TOCCILLO et al., 2025). Não há publicação sobre o C7, sobre qualquer indicador do componente de qualidade, sobre a migração SISAB→SIAPS ou sobre rastreamento de câncer no novo modelo.

Essa escassez tem causa que é, ela própria, objeto legítimo de investigação: os instrumentos oficiais de aferição foram substituídos em série. Ainda na vigência do Previne Brasil, a Portaria GM/MS nº 102/2022 alterou denominação, numerador — que passou a exigir coleta realizada na atenção primária — e denominador, de mulheres cadastradas para cadastradas e vinculadas. Na transição para o novo modelo mudaram simultaneamente sete dimensões: numerador, códigos SIGTAP aceitos, denominador, fonte, granularidade, métrica e público-alvo (BRASIL, 2022a; BRASIL, 2026a). A ruptura de sistema foi formalizada pela Portaria GM/MS nº 7.639/2025, que instituiu o SIAPS como sistema vigente para fins de financiamento (BRASIL, 2025b), e soma-se a incorporação, em janeiro de 2026, do exame molecular de HPV à boa prática do C7, com janela de 60 meses (BRASIL, 2026a). **Não existe série retrocalculada, fator de conversão nem tabela de equivalência.** A fragilidade não é só normativa: os sistemas de informação do câncer perderam 20% da informação do citopatológico entre 2008 e 2019 (TOMAZELLI; RIBEIRO; DIAS, 2022), a cobertura por mulher rastreada não pôde ser calculada para quatro unidades federativas por implantação insuficiente do SISCAN (INCA, 2025), e a análise regional das Américas atribui explicitamente a baixa cobertura brasileira à não consolidação desse sistema (FERNÁNDEZ-DEAZA et al., 2024).

# 2 JUSTIFICATIVA

## 2.1 Por que este desenho, contra os precedentes

Este projeto **não reivindica ineditismo temático**. Cella, Correa e Barancelli (2025) já trataram da progressão da cobertura do citopatológico sob o Previne Brasil, em estudo transversal cobrindo 2018-2023, com recorte na 7ª Regional de Saúde do Paraná e nas regiões Sul e Sudeste, encontrando aumento progressivo da cobertura, ainda abaixo da meta, e correlação positiva entre acesso e detecção. A coincidência de tema é assumida sem rodeios. A contribuição é de outra ordem, em quatro planos. É de **desenho**, ao adotar séries temporais interrompidas em painel, com contrafactual explícito e estimativa de mudança de nível e de tendência em pontos normativos datados, contra corte transversal correlacional sem controle de tendência pré-intervenção, e ao tratar sazonalidade, autocorrelação e sobredispersão. É de **unidade de análise**, ao operar em base mensal e municipal, contra agregados anuais por regional. É de **fonte**, ao usar contagens do SISCAN com offset demográfico independente, contra o indicador da atenção primária, cujo numerador é subnotificado em magnitude documentada (CASTRO-NUNES et al., 2024) e cujo denominador é movido pelo próprio incentivo (SELLERA et al., 2023). E é de **recorte e período**, ao deslocar a análise para o Nordeste e ao alcançar a transição de 2024. Não se trata de responder a uma pergunta nova sobre um objeto novo, mas de responder com contrafactual a uma pergunta que a literatura disponível só pôde descrever — e de fazê-lo na região cuja tendência de mortalidade é a única em ascensão no país.

## 2.2 Por que Pernambuco

Pernambuco apresenta taxa de incidência estimada ajustada de 11,96 por 100 mil, **inferior** à média nacional de 14,76, e ao mesmo tempo mortalidade ajustada de 6,23 por 100 mil em 2022, superior tanto à média nordestina (5,94) quanto à nacional (4,79) (INCA, 2025; INCA, 2026). A combinação de menor incidência estimada com maior mortalidade não é argumento contra o recorte, mas a favor dele: é a assinatura esperada de detecção tardia e de falha nos elos posteriores da linha de cuidado, corroborada pelos 62,5% de casos diagnosticados em estádio avançado no estado — percentual praticamente idêntico ao de Alagoas (62,4%), o que situa Pernambuco no patamar nordestino e não como caso extremo isolado (OLIVEIRA et al., 2024) — e pelos 51,54% de laudos liberados em até 30 dias em 2022 (INCA, 2023). O recorte não se justifica, portanto, por magnitude de incidência, e sim pela conjunção de mortalidade elevada, cobertura baixa (32,5% no triênio 2021-2023, contra 35,6% no país; RIBEIRO et al., 2025), qualidade laboratorial deficiente — índice de positividade entre 1,9 e 2,2 de 2019 a 2023, permanentemente em faixa inaceitável ou de aprimoramento, razão HSIL/satisfatórios de 0,31% abaixo do parâmetro de 0,4%, e 27% dos municípios com insatisfatoriedade acima de 5%, o maior percentual do país (INCA, 2023; INCA, 2025) — e heterogeneidade intraestadual suficiente para sustentar um painel municipal.

Essa heterogeneidade é documentada em todas as dimensões relevantes. Na organização da oferta, o gargalo é estrutural e antigo, descrito em município de grande porte da Região Metropolitana do Recife, onde a média de 18 mil citologias em quatro anos correspondia ao volume necessário para um único mês (SANTOS; SILVA; SILVA, 2012). Na capacidade de registro, o Nordeste teve o menor crescimento de cadastro do país sob a capitação ponderada — precisamente a dimensão que o denominador do C7 torna determinante (SELLERA et al., 2023). O estado abriga, desde dezembro de 2021, programa estadual de rastreamento organizado em cooperação com a OPAS, em Recife e em oito municípios (OPAS; SES-PE, 2021), o que introduz variação de exposição dentro do próprio painel. As 185 unidades municipais oferecem contraste suficiente em cobertura de atenção primária, oferta laboratorial e capacidade administrativa para testar se o efeito de uma mudança nacional de regra é homogêneo no território.

---

# 3 PERGUNTA DE PESQUISA, PREMISSA NORMATIVA E HIPÓTESES

## 3.1 Pergunta

Em que medida a razão mensal de exames citopatológicos de rastreamento do colo do útero por população feminina-alvo de 25 a 64 anos anualizada — população dividida por três, conforme a Resolução CIT nº 2/2016 —, nas 185 unidades municipais de Pernambuco (184 municípios e o Distrito Estadual de Fernando de Noronha) entre janeiro de 2018 e dezembro de 2026, apresenta mudanças de nível e de tendência associadas aos pontos de mudança normativos e sanitários da transição Previne Brasil → Saúde Brasil 360, e como essas mudanças se distribuem entre municípios e regiões de saúde?

## 3.2 Premissa normativa P1

**P1 é estabelecida pelo componente documental e não é submetida a teste estatístico.** Dentro da janela de janeiro de 2018 a dezembro de 2026, nenhum município de Pernambuco esteve exposto a risco financeiro de perda associado ao desempenho em rastreamento do colo do útero: a implementação integral do componente de qualidade só se inicia no primeiro quadrimestre de 2027 (BRASIL, 2026b). As hipóteses H2 a H4 são formuladas condicionalmente a P1. A observação de resposta de produção relevante em τ4 ou τ5, apesar de P1, indicaria mecanismos não financeiros de indução — efeito de mensuração, pactuação regional, reorganização de processos de trabalho — e constituiria achado a investigar em desenho próprio.

## 3.3 Hipóteses

As hipóteses são formuladas a priori, antes do ajuste dos modelos, e ancoradas na cronologia normativa da Tabela 1. Todas se referem à **produção** de exames registrada no SISCAN por município de residência, e não à cobertura populacional.

**H1 — Bloco τ1–τ2 (mar/2020), com retomada em τ2b (jan/2021).** Espera-se redução abrupta e de grande magnitude no nível da razão de exames, seguida de recuperação parcial e incompleta. A hipótese trata os dois marcos como bloco único, por não serem empiricamente separáveis com dois meses de intervalo, e **não** atribui a queda à implantação do Previne Brasil: a evidência sobre o colapso do rastreamento no Brasil em 2020 (RIBEIRO; CORRÊA; MIGOWSKI, 2022) e o padrão da série pernambucana são compatíveis com efeito predominantemente pandêmico. *Ressalva:* se a apuração do desempenho do Previne Brasil esteve suspensa durante a Emergência de Saúde Pública de Importância Nacional, τ1 não constitui marco de exposição financeira ao indicador nº 4, e o bloco deve ser interpretado integralmente como choque pandêmico sobre a oferta, com a exposição financeira datada da primeira competência de repasse por ISF efetivamente apurado (S21).

**H2 — τ3 (mai/2024): retirada de incentivo.** A Portaria GM/MS nº 3.493/2024 revoga o Previne Brasil (art. 7º, IV) e extingue o pagamento por desempenho vinculado ao indicador nº 4, sem que o componente de qualidade que o substituiria produza diferenciação financeira antes do segundo quadrimestre de 2026. Entre maio de 2024 e abril de 2026, portanto, o rastreamento do colo do útero **não é objeto de nenhum incentivo financeiro específico** — configuração de retirada de incentivo, e não de choque de recurso. A literatura de pagamento por desempenho registra que a retirada produz efeitos maiores e mais persistentes que a introdução (MINCHIN et al., 2018; HO et al., 2025). Espera-se, por isso, **mudança de nível ou de tendência de sinal negativo em τ3, de magnitude maior que a esperada em τ4 e τ5**. Esta é a única hipótese direcional forte do estudo, e é falsificável: efeito nulo em τ3 indicaria que o incentivo do Previne Brasil sobre a citologia jamais foi financeiramente operante — leitura convergente com P1 e com a ressalva de H1.

**H3 — τ4 (mai/2025): mensuração sem consequência financeira.** Espera-se efeito nulo ou de magnitude desprezível. Maio de 2025 é marco de início da apuração do C7, não de exposição financeira a ele: quem passa a ser remunerado por classificação de desempenho nessa competência é o componente de vínculo. Acrescente-se a diluição do sinal (2,9% do componente de qualidade) e a janela de acumulação retrospectiva de 36 meses, que dilui o retorno marginal de qualquer exame individual. A confirmação do efeito nulo é resultado informativo. Advertência interpretativa obrigatória: **efeito nulo não distingue ausência de resposta de resposta eficiente** (seção 5.6.1).

**H4 — τ5 (mai/2026): exposição unilateral concentrada na margem.** Espera-se efeito de baixa intensidade e, se existente, de sinal positivo. A Portaria GM/MS nº 10.994/2026 instituiu diferenciação apenas para equipes classificadas como "ótimo". A exposição é unilateral: há ganho potencial e nenhum risco de perda. A assimetria implica gradiente: a intensidade é nula para equipes distantes do limiar de 75 pontos e positiva apenas em sua vizinhança; espera-se, por consequência, que eventual resposta se concentre nos municípios cujas equipes se situem próximas ao corte [VERIFICAR: disponibilidade das classificações do C7 por INE no e-Gestor APS]. **τ5 é estimado apenas como mudança de nível, sem mudança de tendência, e é declaradamente exploratório por dispor de poucas competências pós-interrupção dentro da janela principal.**

**H5 — τ6 (jan/2027): o único regime de risco bilateral.** Na extensão confirmatória da janela a dezembro de 2027, espera-se que a implementação integral do componente de qualidade, com risco bilateral, produza efeito de magnitude superior ao de τ4 e τ5. O contraste entre o regime de incentivo de baixa intensidade (τ3–τ5) e o regime de risco bilateral (τ6) é o contraste teoricamente informativo do estudo.

**H6 — Heterogeneidade.** Espera-se variabilidade substantiva entre municípios na magnitude da queda pandêmica e na mudança de nível em τ3, associada ao porte populacional, à cobertura de Estratégia Saúde da Família e à região de saúde. Não se formula hipótese direcional quanto ao gradiente de vulnerabilidade, dada a inexistência de estudo empírico sobre o novo modelo — o único texto revisado por pares localizado é ensaio sobre variação de repasses em municípios paulistas, sem indicadores nem rastreamento (TOCCILLO et al., 2025).

Não se formula hipótese de que o C7 tenha gerado incentivo por ameaça de perda de repasse, nem de que a mamografia sirva como série-controle a partir de τ4: a primeira é refutada pela cronologia normativa; a segunda, pela agregação de ambos os rastreamentos oncológicos na mesma fórmula ponderada do C7.

---

# 4 OBJETIVOS

## 4.1 Objetivo geral

Estimar as mudanças de nível e de tendência na razão mensal de exames citopatológicos de rastreamento do colo do útero em mulheres de 25 a 64 anos, por município de residência, nas 185 unidades municipais de Pernambuco entre janeiro de 2018 e dezembro de 2026, associadas aos pontos de mudança da transição Previne Brasil → Saúde Brasil 360, interpretando-as à luz da intensidade efetiva da exposição a incentivo documentada na análise normativa.

## 4.2 Objetivos específicos

1. **Descrever** a série mensal municipal e estadual de exames citopatológicos em mulheres de 25 a 64 anos, com o painel completado por zero-fill contra o frame canônico do IBGE, e caracterizar sua estrutura sazonal, sobredispersão e autocorrelação intramunicipal antes da especificação do modelo, incluindo a composição por motivo do exame (rastreamento, repetição, seguimento) ao longo da janela.

2. **Estimar** as mudanças de nível e de tendência da razão de exames nos blocos τ1–τ2 (com retomada em τ2b), τ3 e τ4, e a mudança de **nível** em τ5, esta declaradamente exploratória, por modelo linear generalizado misto binomial negativo com offset log(população-alvo/36), efeitos aleatórios de município e de competência, AR1 intramunicipal e harmônicos de Fourier, reportando razões de taxas com intervalos de 95%. O **estimando primário é o par (δ₃, γ₃)**.

3. **Quantificar** o efeito por comparação com contrafactual, estimando, para cada segmento pós-interrupção, a diferença entre produção observada e projetada, em exames absolutos e em variação percentual, com incerteza propagada por simulação.

4. **Estimar e mapear** a variância entre municípios das mudanças de nível associadas ao bloco pandêmico e a τ3, e examinar sua associação com porte populacional, cobertura de Estratégia Saúde da Família e região de saúde por termos de interação, com apresentação cartográfica.

5. **Estimar** a associação entre a variação municipal do repasse federal de custeio da APS na transição de maio de 2024 e a resposta de produção, tratando a exposição a τ3 como **dose contínua** (variação real per capita do repasse, deflacionada pelo IPCA, entre a média mensal de 2023 e a média das parcelas de maio a dezembro de 2024) interagida com o indicador pós-τ3, à maneira do procedimento aplicado por Toccillo et al. (2025) aos municípios paulistas.

6. **Estimar** a discordância entre o volume de citopatológicos registrado no SISCAN e o volume total registrado no SIA/SUS, por município e competência, como medida de completude relativa dos canais de registro, e verificar se essa discordância apresenta descontinuidade nos pontos de mudança — condição necessária para atribuir qualquer efeito estimado à oferta e não ao registro.

7. **Verificar** se as mudanças de nível e de tendência na produção foram acompanhadas de variação proporcional na detecção de lesão intraepitelial de alto grau ou mais grave (HSIL+), distinguindo parcialmente captação de mulheres não rastreadas de repetição sobre mulheres já rastreadas.

8. **Construir a matriz de (in)comparabilidade** entre o indicador nº 4 do Previne Brasil e o indicador C7, a partir das fontes normativas primárias, confrontando numerador, denominador, faixa etária, janela de acumulação, sistema de origem, granularidade, periodicidade e **valor máximo em risco por equipe**, e registrando as rupturas internas a cada regime — em particular a Portaria GM/MS nº 102/2022 e a incorporação do exame molecular de HPV na competência de janeiro de 2026.

9. **Avaliar a robustez** das estimativas por análises de sensibilidade e testes de falsificação pré-especificados no protocolo, congelados antes da coleta definitiva, nenhum deles substituível ou suprimível em função do resultado (Apêndice B).

---

# 5 MÉTODOS

## 5.1 Delineamento, área e unidade de análise

Estudo ecológico de séries temporais interrompidas (ITS) em painel de municípios, com componente de análise documental comparativa. As interrupções são datas de produção de efeitos de atos normativos federais, declaradas a priori. Mudanças de regra de financiamento incidem simultaneamente sobre todos os municípios: não há unidades não expostas que sirvam de contrafactual por alocação, o que descarta diferenças-em-diferenças e controle sintético (LOPEZ BERNAL; CUMMINS; GASPARRINI, 2019) e torna a ITS o delineamento quase-experimental mais robusto disponível, porque o comportamento pré-intervenção fornece a projeção contra a qual o período posterior é comparado (WAGNER et al., 2002; LOPEZ BERNAL; CUMMINS; GASPARRINI, 2017). Séries-controle são admitidas quando defensáveis (LOPEZ BERNAL; CUMMINS; GASPARRINI, 2018), questão tratada em 5.6.

**O painel, e o que ele efetivamente compra.** Ewusie et al. (2020) mostram que a regressão segmentada sobre dados previamente agregados entre sítios não é ótima. Este projeto assume, porém, uma qualificação decisiva: **o indicador de interrupção é idêntico para as 185 unidades**, de modo que a exposição não varia entre municípios, apenas no tempo. O painel ganha precisão para os parâmetros basais e sazonais, permite estimar heterogeneidade e torna testável a hipótese de penalização diferencial — mas **a identificação de δₖ e γₖ permanece ancorada no comprimento da série, não no produto N×T**. O ganho é de estrutura e de heterogeneidade, não de multiplicação de graus de liberdade sobre a exposição. Daí decorrem duas exigências: o efeito aleatório de competência (5.4) e o reporte de erros-padrão agrupados por competência (S20). Precedentes brasileiros sustentam a viabilidade da opção (RUSSO et al., 2021; COSTA-RIBEIRO et al., 2026).

O frame territorial é o conjunto das 185 unidades municipais reconhecidas pelo IBGE para a UF 26 — 184 municípios e o Distrito Estadual de Fernando de Noronha, sem estatuto municipal mas com código próprio no cadastro do IBGE e registro autônomo nos sistemas do SUS. As regiões e macrorregiões definidas pelo Plano Diretor de Regionalização vigente da SES-PE são variável de agrupamento em análises descritivas e de heterogeneidade, não nível hierárquico do modelo. A unidade de análise é o município de residência observado mensalmente; a célula elementar é município × competência e, em especificações estratificadas, município × faixa quinquenal × competência. A população de referência são mulheres residentes com 25 a 64 anos, faixa que é simultaneamente recomendação clínica (INCA, 2016) e definição normativa do Indicador 5 (BRASIL, 2016). Excluem-se registros com município de residência ignorado, contabilizados e reportados como perda sem redistribuição. Não há amostragem — é censo dos registros disponíveis —, o que desloca a questão do poder para a magnitude de efeito detectável (5.7).

## 5.2 Período e marcos temporais

A janela principal é de janeiro de 2018 a dezembro de 2026, 108 competências, com **extensão confirmatória** a dezembro de 2027 para acomodar τ6. O período anterior ao bloco de interrupção compreende **26 competências (janeiro de 2018 a fevereiro de 2020)**, suficiente para caracterizar nível, tendência e dois ciclos sazonais.

Nenhum ponto de mudança é obtido por busca de quebras nos dados: cada interrupção adicional consome graus de liberdade, e a comparação de seis métodos em 190 séries publicadas recomenda a pré-especificação no protocolo com sensibilidades (TURNER et al., 2021). A revisão de 200 estudos de saúde pública mostra por que a disciplina importa: regressão linear simples em 31% das séries, método indeterminável em 17% e reconhecimento explícito de autocorrelação em apenas 63% (TURNER et al., 2020).

**Três relógios que não coincidem.** Os marcos são datados pela competência em que o ato produz efeitos, distinguindo-se vigência normativa, abertura da janela de apuração e parcela de repasse. τ3 é data de parcela (art. 8º); τ4 e τ5 são datas de abertura de janela quadrimestral, cujo repasse correspondente só ocorre após o fechamento do quadrimestre. Como a resposta a um marco de mensuração é imediata à publicação e a resposta a um marco financeiro é diferida, ambas as datações são declaradas a priori e submetidas a sensibilidade (S17).

**Tabela 1 — Pontos de mudança, mecanismo e tratamento no modelo**

| τ | Ato | Competência | Mecanismo | Tratamento |
|---|---|---|---|---|
| τ1 | Portaria GM/MS nº 2.979/2019 | jan/2020 | Capitação ponderada e pagamento por desempenho; rastreamento do colo do útero como indicador nº 4, peso 1, meta 40%, janela de 36 meses, SISAB, granularidade municipal (BRASIL, 2022a). **Único marco sem âncora normativa própria de produção de efeitos financeiros** (Apêndice E, item 4) | Bloco único com τ2; D_B = 1[t ≥ mar/2020] |
| τ2 | Emergência de Saúde Pública, COVID-19 | mar/2020 | Interrupção abrupta da oferta eletiva e da demanda. Choque exógeno | Bloco único com τ1 |
| τ2b | Retomada pós-nadir | jan/2021 | **Ponto de recuperação epidemiológica, não marco normativo**, ancorado no retorno da produção estadual em nov/2020 e no padrão nacional (RIBEIRO; CORRÊA; MIGOWSKI, 2022). Nenhum efeito de política lhe é atribuído | Par próprio de nível e tendência |
| τ3 | Portaria GM/MS nº 3.493/2024, art. 8º | mai/2024 | Revogação do Previne Brasil (art. 7º, IV) e **extinção do pagamento por desempenho sobre o indicador nº 4**, sem diferenciação substitutiva antes do 2º quadrimestre de 2026: **retirada de incentivo** (BRASIL, 2024a; BRASIL, 2024b) | **Estimando primário** (δ₃, γ₃) |
| τ4 | Portaria GM/MS nº 6.907/2025, art. 3º, §1º | mai/2025 | Início da apuração dos indicadores de qualidade. **Marco de mensuração do C7, não de exposição financeira a ele** (BRASIL, 2024b; BRASIL, 2025a) | Par próprio; hipótese de efeito de mensuração |
| τ5 | Portaria GM/MS nº 10.994/2026 | mai/2026 | Implantação parcial e assimétrica: só equipes "ótimo" recebem valor diferenciado (BRASIL, 2026b) | **Somente δ₅, sem γ₅; exploratório** |
| τ6 | Implementação integral (BRASIL, 2026b) | jan/2027 | Primeiro regime com **risco bilateral** sobre o desempenho em rastreamento | Par próprio, apenas na extensão confirmatória |

**Não separabilidade de τ1 e τ2, e a forma funcional do bloco.** As duas datas distam dois meses; o segmento entre elas contém duas observações e as colunas correspondentes da matriz de delineamento são quase colineares. A estratégia declarada é modelá-las como **bloco único**, com renúncia explícita à atribuição de efeito próprio a cada uma: o estudo **não** estima o efeito do Previne Brasil separadamente do da pandemia, e nenhuma leitura dos resultados pode fazê-lo. Um único par de parâmetros, contudo, não tem forma para descrever um segmento de quatro anos que contém queda a 1.576 exames em junho de 2020 e retorno a 25.848 em novembro; o ajuste produziria resíduos sistemáticos e — o que é decisivo — o contrafactual usado para estimar δ₃ seria a extrapolação de um segmento mal ajustado. Acrescenta-se, por isso, o ponto de recuperação **τ2b = jan/2021**, declarado a priori, de modo que período agudo e retomada tenham parâmetros próprios. Acompanham a decisão S1, S1b, S2, S2b e a inspeção do resíduo médio por competência dentro do segmento.

**Rupturas de mensuração adicionais** — jan/2022 (Portaria GM/MS nº 102/2022), a transição do indicador nº 4 para a boa prática (A) do C7 e jan/2026 (SIGTAP 02.02.10.025-1, com janela de 60 meses) — **não** são modeladas como interrupções do desfecho, porque este provém do SISCAN e não do sistema que alimenta a aferição do pagamento; integram o componente documental (5.8). A redefinição atribuída a julho de 2022 da regra do denominador de 85% foi localizada apenas em fonte secundária e **não é usada como referência normativa** enquanto não recuperada em fonte oficial.

## 5.3 Fontes, desfechos e denominador

**Fonte do desfecho: SISCAN**, por TABNET/DATASUS, definição `SISCAN/cito_colo_residpe.def`, com dois argumentos suficientes. *Independência:* o SISCAN não alimenta a aferição do pagamento — o indicador nº 4 era apurado no SISAB e a boa prática (A) do C7 é apurada em SIAPS, SCNES e RNDS (BRASIL, 2022a; BRASIL, 2026a). Usar como desfecho a base que aciona o pagamento tornaria qualquer efeito indistinguível de mudança de registro (MINCHIN et al., 2018; CASTRO-NUNES et al., 2024). Registre-se o limite da proteção: o SISCAN é imune à contaminação por registro **induzido pelo incentivo**, não a efeitos de registro em geral, pois é sistema administrativo com implantação heterogênea. *Estabilidade:* o registro mantém, ao longo da janela, numerador de exames com laudo, faixa etária derivada da data de nascimento e município de residência declarado, sem as mudanças que atingiram o indicador oficial ao menos três vezes.

**O SIA/SUS e uma discrepância a explicar.** A alternativa natural seria o Sistema de Informações Ambulatoriais, fonte declarada do Indicador 5 (BRASIL, 2016). Testes executados em 1º de agosto de 2026 contra o TABNET estadual produziram, para 2025, **duas anomalias e não uma**: distribuição etária biologicamente implausível, com 42,6% da produção em 20 a 24 anos e apenas 9,0% na faixa-alvo — padrão bimodal com picos simétricos junto aos limites da faixa, assinatura de erro no campo de idade ou de deslocamento posicional do eixo etário; e volume total de 57.744 exames em todas as idades, contra produção do SISCAN da ordem de 310 mil por ano no mesmo estado, **discrepância de quase seis vezes que nenhum erro de faixa explica**. Ambas são incompatíveis com o que o INCA publica para o mesmo estado a partir do mesmo SIA — 82,6% dos exames na faixa-alvo em 2023 (INCA, 2025) e 420.927 a 410.378 exames anuais por residência entre 2018 e 2022 (INCA, 2023). As hipóteses de campo corrompido e de armadilha de extração não foram discriminadas. **Conduta pré-especificada:** antes da coleta definitiva executa-se e reporta-se um **teste de reconciliação** contra os totais anuais por faixa publicados pelo INCA (2023); se reproduzirem, o erro era da extração e o descarte é reescrito como registro de armadilha, mantendo-se o SISCAN pelos dois argumentos anteriores, que bastam; se não, a validação externa passa a ser feita contra a série do SISCAN publicada em INCA (2025), declarando-se o sistema de origem de cada série comparada. Em qualquer cenário o SIA permanece utilizável **naquilo que não depende da estratificação etária** — volume total e presença do procedimento molecular —, porque o erro é de alocação entre faixas, não de contagem. Protocolo de extração, armadilhas do TABNET e verificações obrigatórias no Apêndice F.

**Defasagem entre coleta e liberação do laudo.** O campo de competência do citopatológico é a **data de liberação do laudo** (`CO_ANO_MES_LIBERACAO`): a série é datada pelo laboratório, não pela atenção primária. Em Pernambuco apenas 51,54% dos laudos saíram em até 30 dias em 2022 (INCA, 2023), fração que varia entre municípios e no tempo. A discordância entre o nadir nacional por data de atendimento, maio de 2020 (RIBEIRO; CORRÊA; MIGOWSKI, 2022), e o nadir desta série, junho de 2020, é estimativa empírica direta dessa defasagem, de cerca de um mês. Como três dos quatro marcos caem em maio, a ameaça atinge o estimando: o δ de maio de 2024 pode refletir a fila do laboratório em abril. Providências: verificar se a data de coleta existe como coluna alternativa na definição — se existir, é ela o eixo temporal correto e a série por liberação passa a ser a sensibilidade; S16, com todos os τ deslocados em +1, +2 e +3 competências; e o percentual de laudos em até 30 dias (QualiCito/INCA) como modificador de efeito.

**Desfecho primário.** Contagem mensal de exames citopatológicos com **motivo "rastreamento"**, em mulheres de 25 a 64 anos, por município de residência. A restrição é substantiva: exames de repetição são acoplados à insatisfatoriedade da coleta — 3,38% em Pernambuco em 2022, com 27% dos municípios acima de 5% (INCA, 2023; INCA, 2025) e repetição prescrita em 6 a 12 semanas (INCA, 2016) — e exames de seguimento, ao gargalo diagnóstico; nenhum dos dois é o objeto do incentivo, cuja boa prática (A) é rastreamento. A extração-piloto agregou todas as categorias; a coleta definitiva estratifica, e o percentual de motivo ignorado será reportado por ano.

O parâmetro de interesse é a razão entre essa contagem e a população-alvo anualizada, operacionalizada como offset **log(N/36)** — o fator 36 é a mensalização do fator de divisão 3 da Resolução CIT nº 2/2016 (3 anos × 12 meses), de modo que exp(β₀) fica na mesma escala das razões anuais reportadas descritivamente. A escolha entre /3 e /36 desloca apenas o intercepto por log 12 e **não altera δₖ, γₖ nem qualquer razão de taxas**: é decisão de interpretabilidade, não de estimação. O valor de referência 1,0 sob adesão perfeita é aproximação — com dois exames anuais iniciais e periodicidade trienal subsequente, a adesão estrita corresponde a cerca de 1,05. A partir da 3ª edição das Diretrizes (INCA, 2025) o intervalo recomendado sob teste molecular passa a cinco anos, de modo que, nos municípios que migrarem, o denominador normativo passaria a N/5 e a razão deixaria de ser comparável ao regime anterior — razão adicional para tratar a substituição tecnológica como ameaça, e não como ruído.

**Desfechos secundários:** (1) citopatológicos **fora** da faixa de 25 a 64 anos, série-controle por característica; (2) citopatológicos por faixa quinquenal; (3) exames de **repetição**, indicador de qualidade de coleta e não de esforço de rastreamento; (4) exames de **seguimento**, proxy invertida da capacidade de investigação; (5) exames com diagnóstico **HSIL+** e razão HSIL+/satisfatórios, medida de rendimento; (6) mamografias de 50 a 69 anos, série descritiva e controle restrito ao período anterior a τ3; (7) matriz de (in)comparabilidade.

**Denominador.** População feminina residente por município, ano e faixa quinquenal (POPSVS/SVS-MS a partir de estimativas do IBGE), com cobertura de 100% das células na extração-piloto; na especificação principal, a **soma das oito faixas quinquenais** da faixa-alvo, **interpolada linearmente para competência mensal** para evitar nove degraus artificiais de offset, todos em janeiro e vizinhos de τ1 (a versão em escada é S15). Adota-se a **população total**, por ser o denominador da definição normativa (BRASIL, 2016) e estar disponível em série anual para toda a janela, ao passo que a fração SUS-dependente só é apurável em ano censitário (RIBEIRO et al., 2025). O argumento de que um fator multiplicativo constante por município é absorvido pelo intercepto aleatório **pressupõe invariância temporal dessa fração, o que a variação da cobertura suplementar entre 2018 e 2026 não sustenta** — e essa variação ocorre justamente em torno das interrupções; a estabilidade será verificada e, se a variação intramunicipal exceder cinco pontos percentuais, a razão beneficiários/população entra como covariável tempo-variante (S6; Apêndice E, item 6). As dez covariáveis, com definição operacional, fonte e função, constam do Apêndice F. O **Indicador de Equidade e Dimensionamento** é usado apenas como variável descritiva, e **não** como estratificador dos efeitos: é construto da própria Portaria 3.493/2024, endógeno ao arranjo cuja exposição se avalia, e anacrônico para todo o período anterior a τ3.

### 5.3.1 Declaração obrigatória: contagem de exames não é cobertura

A razão de exames tem numerador de eventos e denominador de pessoas; a cobertura tem numerador e denominador de pessoas (DIAS et al., 2022; RIBEIRO et al., 2025). Só coincidiriam sob a hipótese, empiricamente falsa, de um exame por mulher no período: a cobertura nacional de 35,6% contrasta com razão de 47,4 por 100, superestimação de cerca de um terço, com 1,3 exames por mulher rastreada. **Todo efeito estimado neste estudo é resposta de produção de exames, não ganho de cobertura populacional nem proteção contra o câncer invasor.** Uma elevação da razão é compatível com captação de mulheres nunca rastreadas, que aumenta cobertura, e com encurtamento do intervalo em mulheres já rastreadas, que não aumenta cobertura alguma. Sem desduplicação por mulher em série mensal, impossível com dados agregados públicos, a ambiguidade é irredutível; a decomposição por rendimento diagnóstico é substituto **parcial**, não equivalente.

Há assimetria adicional entre o desfecho e o objeto do incentivo. O numerador da boa prática (A) do C7 é de **pessoas**; este desfecho é de **eventos**. Segue-se que a resposta programaticamente desejável — redirecionar capacidade instalada de mulheres já rastreadas para mulheres nunca rastreadas, sem aumento de volume — eleva o indicador incentivado e produz **efeito nulo sobre o desfecho aqui medido**. A não rejeição da hipótese nula, portanto, **não distingue ausência de resposta de resposta eficiente**, e nenhuma leitura pode converter efeito nulo em evidência de inércia.

## 5.4 Processamento e especificação do modelo

Três tratamentos são obrigatórios, porque cada um, se omitido, enviesa em direção conhecida; o detalhamento e as asserções do autoteste constam do Apêndice F. **Zero-fill contra frame canônico:** o TABNET omite a linha do município que zera no estrato, e sem reposição o zero verdadeiro é lido como ausente e a média condicional é estimada só sobre células com produção — viés **para cima**, máximo no período pandêmico e portanto **diferencial no tempo e correlacionado com as interrupções**. Toda célula ausente recebe zero **desde que a competência já tenha sido publicada**, e o critério operacional dessa distinção, sem o qual a regra é inexequível, é que *uma competência é considerada publicada quando o total estadual retornado é maior que zero*. **Agosto, setembro e outubro de 2022:** nas duas primeiras o SISCAN não processou dados em nenhuma unidade da Federação e **outubro** recebeu o transbordo, aparecendo inflado; as **três** são codificadas como ausentes, porque excluir apenas as duas vazias deixaria um pico de produção acumulada de três meses que o componente sazonal interpretaria como estrutura (S9). **Cauda provisória:** as seis últimas competências são marcadas na coleta e censuradas na análise principal (S10 as reincorpora); para que a censura não elimine o segmento pós-τ5, **a coleta definitiva é executada no segundo semestre de 2027**, de modo que dezembro de 2026 tenha ao menos oito meses de maturação, conservando oito competências pós-τ5 — suficientes para δ₅ exploratório, insuficientes para γ₅.

**Especificação.** Seja Y_it a contagem de exames de rastreamento no município i na competência t e N_it a população-alvo interpolada. Adota-se modelo linear generalizado misto binomial negativo NB2, Var(Y) = μ + μ²/θ, com preditor linear

log μ_it = log(N_it/36) + β₀ + β₁t + Σ_{k∈K} [δ_k D_kt + γ_k (t − τ_k) D_kt] + Σ_{h=1}^{2} [a_h sen(2πht/12) + b_h cos(2πht/12)] + **x**_it′**φ** + u_0i + u_1i t + **v_t** + ε_it,

em que K = {B, 2b, 3, 4, 5}, D_Bt = 1[t ≥ mar/2020] e γ₅ = 0 por imposição. Os termos aleatórios são (u_0i, u_1i)′ ~ N(0, Σ_u) por município; ε_i ~ N(0, σ²_ε R(φ)), com R(φ) de estrutura AR(1) e independente entre municípios; e — este é o termo cuja ausência produziria falsa precisão — **v_t ~ N(0, σ²_v), efeito aleatório de competência compartilhado por todos os municípios**. Como D_kt é idêntico para as 185 unidades, qualquer choque comum estadual não modelado — contrato laboratorial, campanha da SES-PE, falha do SISCAN, calendário — moveria os resíduos de todos os municípios na mesma direção, e um modelo que os supusesse condicionalmente independentes leria um choque único como 185 evidências independentes. É v_t que impede essa leitura, e é por isso que S20 reporta erros-padrão robustos por wild cluster bootstrap no nível da competência. O coeficiente do offset é fixado em 1. O glossário completo dos termos está no Apêndice A.

Três esclarecimentos que o reporte deve conter. **Os γ_k acumulam-se**: a inclinação vigente no segmento posterior a τ_k é β₁ + Σ_{j⪯k} γ_j, e é essa soma, não γ_k isoladamente, que será reportada por segmento. **σ²_ε e θ competem pela mesma sobredispersão**, e a identificação conjunta é potencialmente frágil em municípios pequenos com muitos zeros; declara-se a fragilidade e compara-se, em S3b, com Poisson mais AR1 e com NB2 sem AR1. **O fator de competência é construído com todos os 108 níveis da janela**, inclusive os das competências excluídas, para que a AR1 preserve as distâncias temporais corretas na presença de lacunas. Para que o objetivo 4 seja executável, inclui-se **coeficiente aleatório** para os indicadores do bloco pandêmico e de τ3 — `(1 + t + D_B + D_3 | município)` —, com redução por ordem pré-especificada em caso de não convergência; se a estrutura ampliada não for adotada, o objetivo 4 restringe-se a interações de efeitos fixos e reajustes estratificados (S12), retirando-se a promessa de extrair heterogeneidade dos efeitos a partir dos efeitos aleatórios. A especificação estratificada por idade e a do contrafactual constam do Apêndice A; registre-se aqui que o contrafactual anula δ_k e γ_k de todos os blocos com τ_k ≥ τ_{k*}, fixa os efeitos aleatórios nos valores preditos condicionais, propaga a incerteza por 10.000 extrações da distribuição assintótica conjunta dos efeitos fixos e reporta **dois** intervalos — o de confiança para a produção contrafactual esperada, base do déficit acumulado, e o de predição para a contagem.

**Família, dependência e diagnósticos.** NB2 é pré-especificada, porque contagens municipais mensais têm variância muito superior à média. Registra-se, por rigor de atribuição, que o tutorial de Bhaskaran et al. (2013), frequentemente invocado nesse contexto, **não trata da binomial negativa**; a justificativa apoia-se em Brooks et al. (2017) e Campbell (2021). Como decidir sobre zero-inflação e sobredispersão por testes preliminares infla a taxa de falsos positivos nas inferências subsequentes (CAMPBELL, 2021), as famílias alternativas entram **apenas como sensibilidade reportada** (S3). A AR1 é especificada a priori, e não por diagnóstico post hoc, porque as estimativas de autocorrelação divergem entre métodos e só convergem em séries com pelo menos 100 pontos (TURNER et al., 2021). A sazonalidade usa dois pares de harmônicos de Fourier, decisão crítica porque três dos quatro marcos caem em maio, com precedente aplicado quase idêntico (DUARTE; ARGENTON; CARVALHEIRA, 2022). Os diagnósticos (Apêndice F) incluem resíduos quantílicos simulados em **duas versões**, condicional e **marginal** com re-simulação dos efeitos aleatórios, usando-se apenas a segunda para julgar adequação da média condicional, já que a condicional aparece quase uniforme por construção; autocorrelação residual por **rotação pela matriz de covariância estimada**, e não pela função de autocorrelação bruta, inválida em resíduos de modelo com AR1; **resíduos médios por competência**, diagnóstico direto de má especificação da forma temporal; e o modelo espacial BYM2 (RIEBLER et al., 2016) ajustado **incondicionalmente** (S11), com o I de Moran reportado como descritivo e não como porta de entrada, para não reintroduzir a seleção guiada por dados que o protocolo rejeita.

**Pré-especificação.** O protocolo — pontos de mudança, estrutura do modelo, famílias comparadas e as vinte e uma análises do Apêndice B — é **congelado e depositado em repositório com carimbo de data antes da extração definitiva de 2027**. Declara-se, por transparência, que a série descritiva da extração-piloto já foi inspecionada na fase de elaboração: a pré-especificação é anterior ao ajuste de qualquer modelo, **não** anterior à visualização dos dados, e a distinção é declarada por exigência de honestidade metodológica. Duas classes merecem destaque: **S13, interrupções-placebo** em maio de 2019, 2022 e 2023, no mesmo mês do calendário dos marcos reais para não confundir placebo com sazonalidade — qualquer δ placebo de magnitude comparável invalida a interpretação causal do coeficiente correspondente —, e **S14, desfecho-placebo** à maneira de Russo et al. (2021), sobre a série de mamografias anterior a τ3.

## 5.5 Poder, série-controle e componente documental

**Poder.** Não existe literatura de poder para ITS com múltiplos pontos de mudança em painel de contagens; Liu et al. (2019) servem de balizamento e Green e MacLeod (2016) de âncora do método por simulação. **O `simr` não suporta `glmmTMB` nem AR1**, de modo que se simula do objeto ajustado por `simulate()`, com **v_t ativo** — omiti-lo produziria curvas grosseiramente otimistas. A grade é reduzida e declarada: δ ∈ {0; 0,05; 0,10; 0,20} e γ ∈ {0,005; 0,010}, 500 réplicas, cerca de 25 células e 12.500 ajustes, **incluindo a célula δ = 0 para verificação empírica da taxa de erro tipo I**; réplicas não convergentes entram no denominador do poder e o percentual é reportado; o teste é o de Wald a 5% bilateral. **O item computacionalmente oneroso do projeto é o estudo de poder, não o ajuste individual** (Apêndice G).

**Série-controle.** A **mamografia foi descartada**: o C7 agrega, na mesma fórmula ponderada, os rastreamentos de colo e de mama (BRASIL, 2026a), o que a torna objeto do mesmo incentivo — contaminação no sentido de Lopez Bernal et al. (2018). A restrição adotada é conservadora e vai até **τ3**. O controle é **por característica da população**: citopatológicos fora da faixa de 25 a 64 anos, mesma rede, mesmos laboratórios, mesmo sistema e mesmo choque pandêmico, sem integrar o numerador de nenhum indicador de cofinanciamento. ITS simples e ITS controlado são reportados lado a lado. **A direção do viés depende do sinal do efeito**: se o efeito no grupo-alvo for positivo, uma queda autônoma do controle é conservadora; se for nulo ou negativo — cenário que H2 a H4 tornam mais provável —, é **anticonservadora**. Sob capacidade laboratorial limitada, documentada no estado (SANTOS; SILVA; SILVA, 2012; INCA, 2023), a resposta ao incentivo é realocar exames de fora para dentro da faixa a volume constante, e o contraste é inflado; o diagnóstico pré-especificado verifica se a **soma** das duas séries permanece estável em torno de cada τ, caso em que o ITS controlado é reportado como **limite superior** do efeito. Especificação completa e S19 no Apêndice H.

**Componente documental.** Em um campo em que o gestor federal reformulou duas vezes o instrumento de aferição sem publicar ponte de comparabilidade, documentar a (in)comparabilidade é resultado de pesquisa. O corpus soma, à camada normativa federal, resoluções da CIB de Pernambuco, posicionamentos de CONASS, CONASEMS e ABRASCO, e as tabelas de valores de incentivo por classificação e tipo de equipe — sem as quais a matriz compara definições de indicador e não intensidades de exposição. A dupla conferência é feita pela pesquisadora em dois momentos separados por, no mínimo, quinze dias, com registro de discordâncias e arbitragem pelo orientador. O produto é a matriz do Apêndice C; corpus e procedimento no Apêndice I.

## 5.8 Vieses, reprodutibilidade e aspectos éticos

As quinze ameaças à validade constam do Apêndice D. Cinco exigem registro no corpo do texto.

**(1) Subnotificação por implantação incompleta do SISCAN — residual alto, ameaça de maior gravidade do estudo.** Se a cobertura do sistema cresceu ao longo da janela, parte da tendência ascendente é artefato de consolidação (TOMAZELLI; RIBEIRO; DIAS, 2022; INCA, 2025), e o problema é máximo justamente na travessia de τ1–τ2: **uma parte não desprezível da mudança de nível estimada no bloco pode ser artefato de consolidação do SISCAN, e a magnitude dessa parte é da mesma ordem do efeito procurado.** A mitigação inicialmente considerada — incluir no preditor a razão entre volume do SISCAN e volume do SIA — foi **descartada por endogeneidade**: o numerador dessa razão *é* o desfecho, e condicionar em função da variável dependente enviesa δ_k e γ_k de forma imprevisível; acresce que o denominador seria o SIA, cuja discrepância de volume está por explicar. A conduta adotada: (a) a razão entre canais de registro é **reportada como resultado descritivo e como verificação de falsificação**, pois descontinuidade da própria razão nos pontos de mudança é condição necessária para atribuir efeito ao registro e não à oferta (objetivo 6), à maneira da comparação entre sistemas de Tomazelli, Ribeiro e Dias (2022); (b) a covariável de implantação entra no preditor por fonte **exógena** ao desfecho, o número de estabelecimentos com citopatologia habilitada no SCNES; (c) a mitigação principal é a **restrição do painel** aos municípios com produção não nula e estável desde 2018; (d) declara-se que a implantação diferencial não é integralmente mensurável com fontes públicas e constitui limitação residual alta.

**(2) Substituição tecnológica pelo DNA-HPV — moderado a alto.** Num município integralmente convertido a citologia não cai um pouco: colapsa para a fração de triagem reflexa em mulheres HPV-positivas, e o intervalo passa de três para cinco anos. A assinatura é verificável — queda abrupta e sustentada da citologia **de rastreamento** concomitante ao aparecimento do SIGTAP 02.02.10.025-1, com preservação relativa de repetição e seguimento —, e municípios que a apresentem são sinalizados e excluídos em S5b; a verificação só é operável porque o desfecho é estratificado por motivo. **(3) Cointervenção estadual — moderado:** programa de rastreamento organizado em nove unidades desde dez/2021, sem avaliação publicada (OPAS; SES-PE, 2021); indicador binário, estratificação e S7. **(4) Contagem interpretada como cobertura — irredutível:** declarada no desenho, nos objetivos, nos desfechos e na discussão (5.3.1). **(5) Não separabilidade de τ1 e τ2 — limitação de desenho assumida:** bloco único a priori, τ2b para a forma funcional, S1, S1b, S2 e S2b.

**Reprodutibilidade e reporte.** Extração e montagem em Python 3 com biblioteca padrão, em script único versionado com autoteste sem rede; modelagem em R com `glmmTMB` (BROOKS et al., 2017), `DHARMa`, `spdep` e `INLA`. Repositório público com dados brutos como retornados pelo TABNET, painel montado, scripts, registro de sessão e sementes fixadas; a data de cada extração é registrada, pois o TABNET é base viva sujeita a lançamento retroativo. O reporte segue o STROBE (VON ELM et al., 2007) e a extensão RECORD (BENCHIMOL et al., 2015), diretamente aplicável a dados coletados rotineiramente, somados à pré-especificação e às sensibilidades recomendadas para ITS (TURNER et al., 2021); a diretriz CARITS, em desenvolvimento na EQUATOR Network, será reconsultada e, se publicada, adotada.

**Aspectos éticos.** O estudo usa exclusivamente dados secundários, agregados, de domínio público e sem possibilidade de identificação individual, sem contato com participantes, coleta primária, acesso a prontuário ou microdado identificado, nem *linkage*. Em consonância com as Resoluções CNS nº 466/2012 e nº 510/2016, enquadra-se em tese na hipótese de não registro e não avaliação do parágrafo único do art. 1º desta última. **A dispensa não será presumida**, porque o comitê da instituição de vínculo não dispõe de política pública explícita de dispensa para bases secundárias agregadas de acesso público. Conduta declarada: consulta formal prévia ao comitê; reprodução integral da manifestação obtida, qualquer que seja o teor; submissão via Plataforma Brasil se assim orientado, ou se não houver manifestação em prazo compatível, com os prazos regimentais — dez dias para conferência documental, trinta para parecer e trinta para pendências — incorporados ao caminho crítico; declaração de ausência de conflito de interesses e de financiamento vinculado às partes da política avaliada; e consulta quanto à eventual exigência de manifestação específica sobre a Lei nº 13.709/2018. Registra-se, para afastar leitura de coleta anterior à apreciação ética, que **a extração de agosto de 2026 constituiu teste de reprodutibilidade do procedimento de acesso a dados agregados de domínio público**, conduzido na fase de elaboração do projeto; nenhuma modelagem analítica foi realizada, e a coleta de pesquisa propriamente dita é a extração definitiva, posterior à manifestação do comitê.

---

# 6 RESULTADOS ESPERADOS E CONTRIBUIÇÃO PARA A GESTÃO

O produto analítico central é o conjunto de razões de taxas com intervalos de 95% para o bloco τ1–τ2 e τ2b, para τ3 — o estimando primário — e para τ4, mais a mudança de nível exploratória em τ5, cada uma acompanhada da série contrafactual e do déficit acumulado em número absoluto de exames, que é a métrica que interessa ao gestor. τ6 é estimado na extensão confirmatória e é o único coeficiente da série exposto a risco financeiro bilateral. Somam-se as estimativas estratificadas e de dose contínua, a decomposição por motivo do exame e por rendimento diagnóstico, e a matriz documental de (in)comparabilidade.

Para a **SES-PE**, o estudo entrega o que os instrumentos federais hoje não entregam: uma série municipal mensal de produção, contínua ao longo de nove anos, imune às rupturas de definição do indicador oficial porque extraída de fonte que não alimenta a apuração do C7. Isso permite (i) identificar municípios cuja produção assistencial de rastreamento permanece abaixo do patamar pré-pandemia — informação que a apuração do C7 não fornece, por ser construída sobre população vinculada à equipe e não sobre população residente; (ii) dimensionar o déficit acumulado em números absolutos, insumo para pactuação de metas na Comissão Intergestores Bipartite e para o planejamento da capacidade laboratorial; (iii) avaliar, com contrafactual, o programa estadual de rastreamento organizado, que não possui avaliação publicada; e (iv) delimitar, por análise de limites, o conjunto de municípios cuja produção observada é insuficiente para alcançar o patamar de classificação "ótimo" sob qualquer denominador plausível de população vinculada — exercício de contorno, e **não** de predição do escore, uma vez que a matriz de (in)comparabilidade estabelece que a produção medida no SISCAN não é convertível no numerador do C7.

Para as **secretarias municipais**, o produto técnico oferece um procedimento de monitoramento local que não depende do desempenho de cadastro da equipe. Registre-se o limite da promessa: a série do SISCAN é independente do sistema que aciona o pagamento, o que a torna imune à contaminação por registro induzido pelo incentivo, **mas não a efeitos de registro em geral**. A distinção entre queda de produção e queda de registro só é abordável por discordância entre canais independentes de registro (objetivo 6) e é oferecida como análise exploratória, não como produto garantido.

**Produtos.** *Científicos:* dois manuscritos originais submetidos a periódicos indexados de saúde coletiva em acesso aberto — um com as estimativas de ITS em painel municipal, outro com a matriz de (in)comparabilidade. *Técnico-tecnológico:* nota técnica de monitoramento do rastreamento citopatológico por fonte independente do sistema que aciona o pagamento, dirigida à SES-PE e ao COSEMS-PE, contendo (a) rotina reprodutível de extração mensal do SISCAN por município de residência, (b) a matriz de (in)comparabilidade com orientação de leitura das séries antes e depois de cada ruptura, (c) painel público de acompanhamento municipal e (d) critério operacional para distinguir queda de produção de queda de registro; entrega no 17º mês, com oficina de devolução à SES-PE e a gestores municipais e classificação segundo a taxonomia de produção técnica da CAPES na área de Saúde Coletiva. *Repositório reprodutível* com código de extração, tratamento e modelagem, dicionário de variáveis e registro de versões das extrações.

---

# 7 VIABILIDADE

A exequibilidade em 24 meses não é projeção: a etapa habitualmente mais incerta de um estudo com dados secundários — a obtenção e o tratamento dos dados — já foi executada e verificada em agosto de 2026, na fase de elaboração deste projeto.

1. **Os dados já foram coletados.** Estão disponíveis 2.578.890 exames citopatológicos de mulheres de 25 a 64 anos, por município de residência, em Pernambuco, de janeiro de 2018 a junho de 2026, extraídos por requisição programática e conferidos dígito a dígito contra a interface pública. Cobrem-se **100 das 108 competências** da janela. Das oito ausentes, **seis** correspondem a julho a dezembro de 2026, a serem obtidas na coleta definitiva de 2027 quando estiverem consolidadas; as outras **duas** são agosto e setembro de 2022, competências em que o SISCAN não processou dados em nenhuma unidade da Federação e que são tratadas como ausentes por decisão de protocolo (5.7.2), e não como lacuna de coleta.

2. **O painel está montado e é completo**, com as 185 unidades e preenchimento de zeros verdadeiros contra frame canônico do IBGE.

3. **O denominador está resolvido**, com cobertura de 100% das células do offset.

4. **As séries-controle já existem**: 571.866 citopatológicos fora da faixa-alvo e 976.947 mamografias de 50 a 69 anos, estas utilizáveis apenas até τ3.

5. **A série tem sinal mensurável.** A razão anual varia de 0,405 em 2018 a 0,219 em 2020, com recuperação a 0,423 em 2023 e nova queda a 0,342 em 2025. O colapso pandêmico está inteiramente capturado, **com nadir em junho de 2020, correspondente a redução de aproximadamente 93% frente a janeiro do mesmo ano** (1.576 contra 23.593 exames), e retorno a 25.848 em novembro de 2020.

6. **O pipeline é reprodutível.** A coleta definitiva consiste em reexecutar o mesmo procedimento sobre a janela completa, acrescida da estratificação por motivo do exame e por resultado citológico.

7. **Não há barreira de acesso nem de campo**: não há dados identificados, acesso restrito, convênio a firmar, instrumento a validar nem sujeitos a recrutar.

8. **O método é executável com os recursos disponíveis.** O ajuste do modelo é factível em equipamento pessoal, com tempo da ordem de dezenas de minutos por especificação; o risco de convergência marginal em modelos com AR1 e inclinações aleatórias é reconhecido e endereçado pelo protocolo de 5.8.2. A **análise de poder por simulação**, por exigir alguns milhares de reajustes, é executada em lote paralelizado, com semente fixada, e é o item computacionalmente oneroso — distinção que separa o custo de um ajuste, trivial, do custo do estudo de poder, não trivial.

9. **Aderência institucional.** [VERIFICAR: parágrafo a redigir após a leitura da relação nominal do item 4.4 do edital vigente, no seguinte molde — "O projeto se insere na linha *Avaliação de sistemas, programas e serviços de atenção e vigilância da saúde*, da área de concentração *Políticas de Saúde*, por avaliar a efetividade de um programa federal de indução financeira sobre um serviço de rastreamento oncológico em recorte municipal. A aderência à produção de [orientador] manifesta-se em [dois trabalhos concretos do Lattes, por método ou por objeto]. As estruturas institucionais disponíveis à execução — biblioteca, infraestrutura computacional e acesso a bases do DATASUS — são suficientes, dado que o estudo não requer laboratório, campo nem convênio."]

Os riscos remanescentes são de interpretação, não de execução, e estão declarados: não separabilidade de τ1 e τ2, implantação diferencial do SISCAN, difusão não observada do teste molecular, cointervenção estadual, defasagem entre coleta e liberação do laudo e, sobretudo, a impossibilidade de converter contagem de exames em cobertura populacional.

---

# 8 CRONOGRAMA

Referência: matrícula em fevereiro de 2027, integralização em 24 meses.

| Período | Atividades |
|---|---|
| **2027.1** (meses 1–6) | Disciplinas obrigatórias. Fev–mar: **congelamento e depósito do protocolo analítico com carimbo de data** — pontos de mudança, estrutura do modelo, famílias e as vinte e uma sensibilidades — e **consulta formal ao CEP** com submissão via Plataforma Brasil se orientado. Abr–jul: aguardo do parecer, levantamento documental normativo e consolidação da revisão. **O pré-registro precede a coleta definitiva; nenhuma extração de pesquisa ocorre antes da manifestação do comitê** |
| **2027.2** (meses 7–12) | Disciplinas eletivas e disciplina de desenvolvimento de produtos. **Coleta definitiva** — reextração integral de jan/2018 a dez/2026, com estratificação por motivo do exame e por resultado citológico, denominadores e séries-controle —, executada no segundo semestre para que dez/2026 disponha de ao menos oito meses de maturação; teste de reconciliação do SIA; comparação com a extração de 2026 e estimativa da curva de maturação; análise exploratória e diagnósticos; construção da matriz de (in)comparabilidade. **Exame de qualificação no 11º mês** |
| **2028.1** (meses 13–18) | Modelagem definitiva (ITS simples e controlado), análises estratificadas, dose contínua, sensibilidades e testes de falsificação; **extração de fechamento de jan a dez/2027** para a análise confirmatória de τ6; redação de resultados e discussão. **Submissão do primeiro manuscrito com o orientador no 15º mês**, atendendo à exigência de produção técnico-científica em até 20 meses. **Entrega do produto técnico-tecnológico e publicação do painel no 17º mês** |
| **2028.2** (meses 19–24) | Redação e revisão final; submissão do segundo manuscrito; oficina de devolução à SES-PE e a gestores municipais; **defesa no 22º mês**; depósito no 23º, dentro do limite de 24 meses |

---

# 9 ORÇAMENTO

**Não há custo de coleta de dados.** Todas as fontes são públicas e de acesso irrestrito, todo o processamento emprega software livre e o equipamento é próprio. Não há trabalho de campo, entrevistas, deslocamento para coleta, contratação de auxiliares nem aquisição de bases restritas.

| Item | Especificação | Valor (R$) |
|---|---|---|
| Acesso a dados e licenças | Bases públicas; R, glmmTMB, Quarto, Git, QGIS | 0,00 |
| Infraestrutura computacional | Equipamento próprio; hospedagem do painel em serviço gratuito | 0,00 |
| Material de consumo | Suprimentos, mídias, encadernação das vias da dissertação | 800,00 |
| Obtenção de documentos | Atos normativos, comutação bibliográfica, literatura sem acesso aberto | 400,00 |
| Congresso nacional da área | Inscrição, passagem, quatro diárias e alimentação | 4.900,00 |
| Evento estadual/regional | Inscrição e deslocamento | 700,00 |
| Revisão de língua portuguesa | Dois manuscritos e dissertação | 1.200,00 |
| Contingência de taxa de publicação | Os periódicos nacionais prioritários não cobram APC | 1.000,00 |
| Oficina de devolução a gestores | Material de apoio e logística | 800,00 |
| Reserva técnica (10%) | — | 980,00 |
| **Total** | | **10.780,00** |

A rubrica de versão para o inglês foi suprimida por coerência com o alvo declarado dos manuscritos, que são periódicos nacionais indexados em acesso aberto. As despesas serão custeadas com recursos próprios, com possibilidade de apoio pelo Programa de Apoio à Pós-Graduação. Eventual concessão de bolsa não é pressuposto de execução: **nenhuma rubrica é condição para a produção dos resultados analíticos.**

---

# REFERÊNCIAS

BENCHIMOL, E. I.; SMEETH, L.; GUTTMANN, A. et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) Statement. **PLOS Medicine**, v. 12, n. 10, e1001885, 2015. DOI: 10.1371/journal.pmed.1001885.

BHASKARAN, K.; GASPARRINI, A.; HAJAT, S.; SMEETH, L.; ARMSTRONG, B. Time series regression studies in environmental epidemiology. **International Journal of Epidemiology**, v. 42, n. 4, p. 1187-1195, 2013. DOI: 10.1093/ije/dyt092.

BRASIL. Ministério da Saúde. **Caderno de Diretrizes, Objetivos, Metas e Indicadores 2016**. Brasília, DF: Ministério da Saúde, 2016. Indicador 5, p. 14-15. (Pactuado pela Resolução CIT nº 2, de 16 de agosto de 2016.)

BRASIL. Ministério da Saúde. Secretaria de Atenção Primária à Saúde. Departamento de Saúde da Família. **Nota Técnica nº 3/2022-DESF/SAPS/MS**: indicadores de pagamento por desempenho do Programa Previne Brasil. Brasília, DF: Ministério da Saúde, 2022a. SEI nº 0024999684, processo nº 25000.012850/2020-33.

BRASIL. Ministério da Saúde. Gabinete do Ministro. **Portaria GM/MS nº 3.493, de 10 de abril de 2024**. Institui nova metodologia de cofinanciamento federal do Piso de Atenção Primária à Saúde. Diário Oficial da União, Brasília, DF, ed. 70, seção 1, p. 100, 11 abr. 2024a.

BRASIL. Ministério da Saúde. Secretaria de Atenção Primária à Saúde. **Perguntas frequentes — Novo Modelo de Cofinanciamento Federal da Atenção Primária à Saúde**. Brasília, DF: Ministério da Saúde, 2024b. Disponível em: https://aps.saude.gov.br/. Acesso em: 1 ago. 2026.

BRASIL. Ministério da Saúde. Gabinete do Ministro. **Portaria GM/MS nº 6.907, de 29 de abril de 2025**. Altera a Portaria de Consolidação GM/MS nº 6/2017 e a Portaria GM/MS nº 3.493/2024. Diário Oficial da União, Brasília, DF, 8 maio 2025a.

BRASIL. Ministério da Saúde. Gabinete do Ministro. **Portaria GM/MS nº 7.639, de 18 de julho de 2025**. Institui o Sistema de Informação para a Atenção Primária à Saúde. Diário Oficial da União, Brasília, DF, ed. 136, seção 1, p. 128, 22 jul. 2025b.

BRASIL. Ministério da Saúde. Secretaria de Atenção Primária à Saúde. **Nota Técnica nº 30/2025-CGESCO/DESCO/SAPS/MS** — Componente Vínculo e Acompanhamento Territorial. Brasília, DF: Ministério da Saúde, 23 set. 2025c. SEI nº 0049700833, processo nº 25000.178857/2024-41.

BRASIL. Ministério da Saúde. Secretaria de Atenção Primária à Saúde. **Nota Metodológica C7 — Cuidado da mulher e do homem transgênero na prevenção do câncer na Atenção Primária à Saúde**. Brasília, DF: Ministério da Saúde, 2026a. SEI nº 0054641718, processo nº 25000.137969/2025-22.

BRASIL. Ministério da Saúde. Gabinete do Ministro. **Portaria GM/MS nº 10.994, de 13 de maio de 2026**. Dispõe sobre o período de implementação da metodologia de cofinanciamento federal do Piso de Atenção Primária à Saúde. Diário Oficial da União, Brasília, DF, ed. 89, seção 1, p. 1105, 14 maio 2026b.

BROOKS, M. E.; KRISTENSEN, K.; VAN BENTHEM, K. J. et al. glmmTMB balances speed and flexibility among packages for zero-inflated generalized linear mixed modeling. **The R Journal**, v. 9, n. 2, p. 378-400, 2017. DOI: 10.32614/RJ-2017-066.

CAMPBELL, H. The consequences of checking for zero-inflation and overdispersion in the analysis of count data. **Methods in Ecology and Evolution**, v. 12, n. 4, p. 665-680, 2021. DOI: 10.1111/2041-210X.13559.

CASTRO-NUNES, P. de; PALMIERI, P.; BELLAS, H. et al. Effects of pay for performance in primary care in an under-registration scenario. **Revista de Saúde Pública**, v. 58, p. 44, 2024. DOI: 10.11606/s1518-8787.2024058005812.

CELLA, E. N.; CORREA, L. D.; BARANCELLI, A. J. A análise da progressão da cobertura do citopatológico e da incidência de câncer de colo de útero pela implementação do Programa Previne Brasil. **Revista Brasileira de Medicina de Família e Comunidade**, v. 20, n. 47, art. 4480, 2025. DOI: 10.5712/rbmfc20(47)4480.

CORRÊA, F. M. et al. [Estudo de modelagem sobre rastreamento oportunístico e projeção do limiar de eliminação do câncer do colo do útero no Brasil], 2022. [VERIFICAR: completar autoria, título, periódico, volume, páginas e DOI — a referência é usada no dossiê depurado sem dados bibliográficos completos.]

COSTA-RIBEIRO, M. C. V.; KRAINSKI, E. T.; MELLO, A. M. et al. Dengue incidence following mass vaccination: an interrupted time series study in Paraná, Brazil. **Tropical Medicine and Infectious Disease**, v. 11, n. 1, art. 11, 2026.

DE SETA, M. H.; OCKÉ-REIS, C. O.; RAMOS, A. L. P. Programa Previne Brasil: o ápice das ameaças à Atenção Primária à Saúde? **Ciência & Saúde Coletiva**, v. 26, supl. 2, p. 3781-3786, 2021. DOI: 10.1590/1413-81232021269.2.01072020.

DIAS, M. B. K.; ALCÂNTARA, L. L. M.; GIRIANELLI, V. R. et al. Rastreamento do câncer do colo do útero em mulheres de 25 a 64 anos: indicadores do primeiro exame citopatológico informado no Siscolo, 2007-2013. **Revista Brasileira de Cancerologia**, v. 68, n. 1, 2022. DOI: 10.32635/2176-9745.RBC.2022v68n1.1520.

DUARTE, M. B. O.; ARGENTON, J. L. P.; CARVALHEIRA, J. B. C. Impact of COVID-19 in cervical and breast cancer screening and systemic treatment in São Paulo, Brazil: an interrupted time series analysis. **JCO Global Oncology**, v. 8, e2100371, 2022. DOI: 10.1200/GO.21.00371.

EWUSIE, J. E.; THABANE, L.; BEYENE, J.; STRAUS, S. E.; HAMID, J. S. Multicenter interrupted time series analysis: incorporating within and between-center heterogeneity. **Clinical Epidemiology**, v. 12, p. 625-636, 2020. DOI: 10.2147/CLEP.S241568.

FARDOUSI, N.; NUNES DA SILVA, E.; KOVACS, R. et al. Performance bonuses and the quality of primary health care delivered by family health teams in Brazil: a difference-in-differences analysis. **PLOS Medicine**, v. 19, n. 7, e1004033, 2022. DOI: 10.1371/journal.pmed.1004033.

FERNÁNDEZ-DEAZA, G. et al. [Análise regional da cobertura de rastreamento do câncer do colo do útero nas Américas: 37 países; cobertura trienal de 60%; ausência de associação com mortalidade; baixa cobertura brasileira atribuída à não consolidação do SISCAN], 2024. [VERIFICAR: completar autoria, título, periódico e DOI.]

FERRARI, A. J. S. et al. [Tendência da mortalidade por câncer do colo do útero no Brasil e macrorregiões, 1980-2021: 171.793 óbitos; AAPC nacional −0,3% (IC95% −1,0; 0,4); Nordeste +0,6% (IC95% 0,3; 0,8)], 2025. [VERIFICAR: completar autoria, título, periódico, volume e DOI.]

GREEN, P.; MACLEOD, C. J. SIMR: an R package for power analysis of generalized linear mixed models by simulation. **Methods in Ecology and Evolution**, v. 7, n. 4, p. 493-498, 2016. DOI: 10.1111/2041-210X.12504.

GURGEL, G. D.; KRISTENSEN, S. R.; DA SILVA, E. N. et al. Pay-for-performance for primary health care in Brazil: a comparison with England's Quality Outcomes Framework and lessons for the future. **Health Policy**, v. 128, p. 62-68, 2023. DOI: 10.1016/j.healthpol.2022.11.004.

HARZHEIM, E. "Previne Brasil": bases da reforma da Atenção Primária à Saúde. **Ciência & Saúde Coletiva**, v. 25, n. 4, p. 1189-1196, 2020. DOI: 10.1590/1413-81232020254.01552020.

HO, L.; MERCER, S. W.; HENDERSON, D.; DONAGHY, E.; GUTHRIE, B. Effect of UK Quality and Outcomes Framework pay-for-performance programme on quality of primary care: systematic review with quantitative synthesis. **BMJ**, v. 389, e083424, 2025. DOI: 10.1136/bmj-2024-083424.

INSTITUTO NACIONAL DE CÂNCER (INCA). **Diretrizes brasileiras para o rastreamento do câncer do colo do útero**. 2. ed. rev. atual. Rio de Janeiro: INCA, 2016. 114 p.

INSTITUTO NACIONAL DE CÂNCER (INCA). **Dados e números sobre câncer do colo do útero: relatório anual 2023**. Rio de Janeiro: INCA, out. 2023. Disponível em: https://www.gov.br/inca/. Acesso em: 1 ago. 2026.

INSTITUTO NACIONAL DE CÂNCER (INCA). **Controle do câncer do colo do útero no Brasil: dados e números 2025**. Rio de Janeiro: INCA, 2025. Disponível em: https://www.gov.br/inca/. Acesso em: 1 ago. 2026.

INSTITUTO NACIONAL DE CÂNCER (INCA). **Estimativa 2026: incidência de câncer no Brasil**. Rio de Janeiro: INCA, 2026.

LIU, W.; YE, S.; BARTON, B. A. et al. Simulation-based power and sample size calculation for designing interrupted time series analyses of count outcomes in evaluation of health policy interventions. **Contemporary Clinical Trials Communications**, v. 17, art. 100474, 2019. DOI: 10.1016/j.conctc.2019.100474.

LOPEZ BERNAL, J.; CUMMINS, S.; GASPARRINI, A. Interrupted time series regression for the evaluation of public health interventions: a tutorial. **International Journal of Epidemiology**, v. 46, n. 1, p. 348-355, 2017. DOI: 10.1093/ije/dyw098.

LOPEZ BERNAL, J.; CUMMINS, S.; GASPARRINI, A. The use of controls in interrupted time series studies of public health interventions. **International Journal of Epidemiology**, v. 47, n. 6, p. 2082-2093, 2018. DOI: 10.1093/ije/dyy135.

LOPEZ BERNAL, J.; CUMMINS, S.; GASPARRINI, A. Difference in difference, controlled interrupted time series and synthetic controls. **International Journal of Epidemiology**, v. 48, n. 6, p. 2062-2063, 2019. DOI: 10.1093/ije/dyz050.

MASSUDA, A. [Artigo-companheiro crítico à reforma do financiamento da APS]. **Ciência & Saúde Coletiva**, v. 25, n. 4, 2020. [VERIFICAR: completar título, páginas e DOI. **Atenção:** não confundir com HARZHEIM (2020), que defende a reforma — a auditoria registrou troca de autoria com inversão de posição argumentativa entre os dois textos, publicados no mesmo fascículo.]

MAURO, M.; ROTUNDO, G.; GIANCOTTI, M. Effect of financial incentives on breast, cervical and colorectal cancer screening delivery rates: results from a systematic literature review. **Health Policy**, v. 123, n. 12, p. 1210-1220, 2019. DOI: 10.1016/j.healthpol.2019.09.012.

MINCHIN, M.; ROLAND, M.; RICHARDSON, J.; ROWARK, S.; GUTHRIE, B. Quality of care in the United Kingdom after removal of financial incentives. **New England Journal of Medicine**, v. 379, n. 10, p. 948-957, 2018. DOI: 10.1056/NEJMsa1801495.

NASCIMENTO, M. I.; MASSAHUD, F. C.; BARBOSA, N. G.; LOPES, C. D.; RODRIGUES, V. C. Premature mortality due to cervical cancer: study of interrupted time series. **Revista de Saúde Pública**, v. 54, art. 139, 2020. DOI: 10.11606/s1518-8787.2020054002528.

OLIVEIRA, M. M. de et al. [Diagnóstico em estádio avançado de câncer do colo do útero no Brasil, RHC 2006-2015: 125.356 casos registrados; 54.344 nas análises inferenciais, excluído SP; 48,4% em estádio avançado; RP 1,08 (IC95% 1,01-1,14) para menor cobertura estadual], 2024. [VERIFICAR: completar autoria, título, periódico e DOI.]

ORGANIZAÇÃO PAN-AMERICANA DA SAÚDE (OPAS/OMS); SECRETARIA ESTADUAL DE SAÚDE DE PERNAMBUCO (SES-PE). **Estado brasileiro de Pernambuco e OPAS lançam programa para prevenir e tratar câncer de colo de útero (Programa Útero é Vida)**. Notícia institucional, 16 dez. 2021. Disponível em: https://www.paho.org/pt/brasil. Acesso em: 1 ago. 2026.

RIBEIRO, C. M.; CLARO, I. B.; TOMAZELLI, J. G.; DIAS, M. B. K. Rastreamento do câncer do colo do útero no Brasil: análise da cobertura a partir do Sistema de Informação do Câncer. **Cadernos de Saúde Pública**, v. 41, n. 8, e00152224, 2025. DOI: 10.1590/0102-311XPT152224.

RIBEIRO, C. M.; CORRÊA, F. M.; MIGOWSKI, A. Efeitos de curto prazo da pandemia de COVID-19 na realização de procedimentos de rastreamento, investigação diagnóstica e tratamento do câncer no Brasil: estudo descritivo, 2019-2020. **Epidemiologia e Serviços de Saúde**, v. 31, n. 1, e2021405, 2022. DOI: 10.1590/S1679-49742022000100010.

RIEBLER, A.; SØRBYE, S. H.; SIMPSON, D.; RUE, H. An intuitive Bayesian spatial model for disease mapping that accounts for scaling. **Statistical Methods in Medical Research**, v. 25, n. 4, p. 1145-1165, 2016. DOI: 10.1177/0962280216660421.

RUSSO, L. X.; POWELL-JACKSON, T.; MAIA BARRETO, J. O. et al. Pay for performance in primary care: the contribution of the Programme for Improving Access and Quality of Primary Care (PMAQ) on avoidable hospitalisations in Brazil, 2009-2018. **BMJ Global Health**, v. 6, n. 7, e005429, 2021. DOI: 10.1136/bmjgh-2021-005429.

RUSSO, L. X.; POWELL-JACKSON, T.; BORGHI, J. et al. Does pay-for-performance design matter? Evidence from Brazil. **Health Policy and Planning**, v. 39, n. 6, p. 593-602, 2024. DOI: 10.1093/heapol/czae025.

SANTOS, [.]; SILVA, [.]; SILVA, [.] [Estudo em município de grande porte da Região Metropolitana do Recife: média de 18 mil citologias em quatro anos, equivalente ao volume necessário para um único mês], 2012. [VERIFICAR: completar autoria, título, periódico, volume e páginas.]

SCHÖNHOLZER, T. E.; ZACHARIAS, F. C. M.; AMARAL, G. G. et al. Performance indicators of Primary Care of the Previne Brasil Program. **Revista Latino-Americana de Enfermagem**, v. 31, e4007, 2023. DOI: 10.1590/1518-8345.6640.4007.

SELLERA, P. E. G.; SILVA, M. R. M.; MENDONÇA, A. V. M.; GINANI, V. C.; SOUSA, M. F. Incentivo de capitação ponderada (Programa Previne Brasil): impactos na evolução do cadastro populacional na APS. **Ciência & Saúde Coletiva**, v. 28, n. 9, p. 2743-2750, 2023. DOI: 10.1590/1413-81232023289.20142022.

TOCCILLO, G. L.; CARNUT, L.; MENDES, Á.; MELO, M. A. O novo modelo de alocação de recursos federais da APS 2024: variação dos repasses nos municípios paulistas. **Saúde em Debate**, v. 49, n. 147, e10205, 2025. Ensaio. DOI: 10.1590/2358-2898202514710205P.

TOMAZELLI, J.; RIBEIRO, C. M.; DIAS, M. B. K. Cobertura dos sistemas de informação dos cânceres do colo do útero e de mama no Brasil, 2008-2019. **Revista Brasileira de Cancerologia**, v. 68, n. 1, e-121544, 2022. DOI: 10.32635/2176-9745.RBC.2022v68n1.1544.

TURNER, S. L.; KARAHALIOS, A.; FORBES, A. B. et al. Design characteristics and statistical methods used in interrupted time series studies evaluating public health interventions: a review. **Journal of Clinical Epidemiology**, v. 122, p. 1-11, 2020. DOI: 10.1016/j.jclinepi.2020.02.006.

TURNER, S. L.; KARAHALIOS, A.; FORBES, A. B. et al. Comparison of six statistical methods for interrupted time series studies: empirical evaluation of 190 published series. **BMC Medical Research Methodology**, v. 21, art. 134, 2021. DOI: 10.1186/s12874-021-01306-w.

VON ELM, E.; ALTMAN, D. G.; EGGER, M. et al. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. **PLOS Medicine**, v. 4, n. 10, e296, 2007. DOI: 10.1371/journal.pmed.0040296.

WAGNER, A. K.; SOUMERAI, S. B.; ZHANG, F.; ROSS-DEGNAN, D. Segmented regression analysis of interrupted time series studies in medication use research. **Journal of Clinical Pharmacy and Therapeutics**, v. 27, n. 4, p. 299-309, 2002. DOI: 10.1046/j.1365-2710.2002.00430.x.

WORLD HEALTH ORGANIZATION (WHO). **Global strategy to accelerate the elimination of cervical cancer as a public health problem**. Geneva: WHO, 2020. 56 p. ISBN 9789240014107.

---

# APÊNDICES

> **Nota.** Os Apêndices A a E constituem material de protocolo, depositado no repositório público do estudo junto com o pré-registro. **Não integram o corpo submetido a nenhum dos dois editais**, cujos limites de extensão são atendidos pelas seções 1 a 9 mais as referências.

## Apêndice A — Glossário dos termos do modelo

| Termo | Significado |
|---|---|
| Y_it | Contagem de exames de rastreamento no município i, competência t |
| N_it | População feminina-alvo de 25 a 64 anos, interpolada para competência mensal |
| log(N_it/36) | Offset; coeficiente fixado em 1; o fator 36 é a mensalização do fator de divisão 3 da Resolução CIT nº 2/2016 |
| β₀, β₁ | Intercepto e tendência mensal basal |
| K = {B, 2b, 3, 4, 5} | Blocos de interrupção; B com referência mar/2020; γ₅ = 0 por imposição |
| D_kt = 1[t ≥ τ_k] | Indicador de pós-interrupção, **idêntico para as 185 unidades** |
| δ_k | Mudança de nível; exp(δ_k) é a razão de taxas imediata |
| γ_k | Mudança de inclinação; a inclinação vigente no segmento posterior a τ_k é β₁ + Σ_{j⪯k} γ_j |
| a_h, b_h (h = 1, 2) | Harmônicos de Fourier, período 12 |
| **x**_it, **φ** | Covariáveis (Tabela 2) e coeficientes |
| (u_0i, u_1i)′ ~ N(0, Σ_u) | Intercepto e inclinação aleatórios de município; Σ_u irrestrita |
| **v_t ~ N(0, σ²_v)** | **Efeito aleatório de competência compartilhado por todos os municípios; impede que um choque estadual comum seja contado 185 vezes** |
| ε_i ~ N(0, σ²_ε R(φ)) | Dependência serial intramunicipal, R(φ) com estrutura AR(1), independente entre municípios |
| θ | Parâmetro de dispersão NB2; identificação conjunta com σ²_ε declarada como potencialmente frágil (S3b) |

## Apêndice B — Análises de sensibilidade e testes de falsificação pré-especificados

| # | Análise | O que testa |
|---|---|---|
| S1 | τ1 deslocado de jan/2020 para jan/2019 | Antecipação por publicação e adaptação municipal |
| S1b | D_B recodificado com início em jan/2020 | Escolha do ponto de referência do bloco |
| S2 | Exclusão de mar–ago/2020 (NASCIMENTO et al., 2020) | Contaminação pelo período agudo |
| S2b | Bloco pandêmico sem τ2b (par único) | Necessidade do ponto de recuperação |
| S3 | NB1, nbinom1 (variância proporcional à média, análogo em máxima verossimilhança do ajuste quasi-Poisson) e NB2 zero-inflada | Hipótese distribucional, sem seleção por teste preliminar |
| S3b | Poisson com termo AR1; e NB2 sem AR1 | Identificação conjunta de σ²_ε e θ |
| S4 | Sazonalidade com H = 1, H = 3 e onze indicadores mensais | Parcimônia dos harmônicos |
| S5 | Censura em dez/2024 e em jun/2025; covariável de teste molecular | Substituição tecnológica |
| S5b | Exclusão de municípios com assinatura de conversão a DNA-HPV | Conversão versus retração |
| S6 | Denominador SUS-dependente **tempo-variante** | Invariância temporal da fração SUS-dependente |
| S7 | Exclusão dos nove municípios do programa estadual; e interação a partir de dez/2021 | Cointervenção estadual |
| S8 | Exclusão de Recife; exclusão de Fernando de Noronha | Influência de volume e de população mínima |
| S9 | Imputação das três competências de 2022 pelos harmônicos e tendência local; e retenção de out/2022 com indicador de transbordo | Tratamento da falha de processamento |
| S10 | Reinclusão das competências provisórias censuradas | Maturação da série sobre δ₅ |
| S11 | Componente espacial BYM2, ajustado **incondicionalmente** | Dependência espacial residual |
| S12 | Reestimação por porte populacional, cobertura de ESF e estrato de vulnerabilidade | Penalização diferencial por capacidade |
| **S13** | **Interrupções-placebo em mai/2019, mai/2022 e mai/2023** | Mudanças de nível espúrias na ausência de política |
| **S14** | **Desfecho-placebo: modelo completo sobre mamografias 50–69 antes de τ3** (RUSSO et al., 2021) | Especificidade do efeito |
| S15 | População mensal em escada versus interpolada | Degraus artificiais de offset em janeiro |
| S16 | Todos os τ deslocados em +1, +2 e +3 competências | Defasagem entre coleta e liberação do laudo |
| S17 | τ4 e τ5 deslocados um quadrimestre à frente; τ4 na competência de publicação da Portaria 6.907/2025 | Datação por apuração versus por repasse |
| S18 | Série total, sem restrição por motivo do exame | Comparabilidade com a literatura que não estratifica |
| S19 | Controle restrito a 15–24 anos, excluindo 65 anos ou mais | Ligação programática da faixa 65–69 à faixa-alvo |
| S20 | Erros-padrão por wild cluster bootstrap no nível da competência (108 clusters) | Choques comuns estaduais não modelados |
| S21 | τ1 deslocado para a primeira competência de repasse por ISF efetivamente apurado | Suspensão da apuração do desempenho durante a ESPIN |

## Apêndice C — Matriz de (in)comparabilidade: dimensões e rupturas

| Dimensão | Indicador nº 4, versão original (2020-2021) | Ruptura 1 — Portaria 102/2022 | Ruptura 2 — transição para o C7 (2024-2025) | Ruptura 3 — Nota Metodológica C7 (jan/2026) |
|---|---|---|---|---|
| Denominação | Indicador nº 4 do Previne Brasil | Alterada | Boa prática (A) do C7 | Mantida |
| Numerador | Coleta de citopatológico registrada | Exige coleta **realizada na APS** | Admite exame **coletado, solicitado ou avaliado** | Incorpora o teste molecular de HPV |
| Códigos aceitos | Um procedimento SIGTAP | Um procedimento SIGTAP | Seis SIGTAP mais dois códigos ABEX/ABP | Acresce SIGTAP 02.02.10.025-1 |
| Janela de acumulação | 36 meses | 36 meses | 36 meses | 36 meses, **exceto 60** para o teste molecular |
| Denominador | Mulheres **cadastradas**, piso em estimativa IBGE | Mulheres **cadastradas e vinculadas** | Pessoas de 25 a 64 anos **vinculadas à equipe** (NT 30/2025) | Mantido |
| Fonte | SISAB | SISAB | SIAPS, SCNES e RNDS | Mantida |
| Granularidade | Município | Município | Identificador Nacional de Equipe | Mantida |
| Métrica | Percentual, meta 40%, parâmetro 80%, peso 1 | Percentual | 20 de 100 pontos do C7, 1 de 7 indicadores da qualidade | Mantida |
| Público-alvo | Mulheres de 25 a 64 anos | Idem | Ampliado (mulheres e homens transgênero) | Mantido |
| Consequência financeira | Desempenho remunera componente **adicional** sobre a capitação; a não obtenção da nota máxima é **ganho não auferido** em relação ao teto do ISF, não redução do repasse-base | Idem | Classificação "bom" garantida; **sem risco de perda dentro da janela** | Exposição **unilateral**, concentrada na margem entre "bom" e "ótimo" (limiar de 75 pontos) |
| **Valor máximo mensal em risco por eSF** | **Da ordem de R$ 322,50 (2022): peso 1/10 sobre ISF de R$ 3.225,00** | Idem | **Zero** | **Fração de 2,9% do componente de qualidade** [VERIFICAR: conversão em reais] |

## Apêndice D — Ameaças à validade não detalhadas no corpo

| # | Ameaça | Direção | Mitigação | Residual |
|---|---|---|---|---|
| 6 | Zero-fill omitido | Superestimação, diferencial no tempo | Zero-fill contra frame canônico, com asserção | Eliminado se aplicado |
| 7 | Cauda provisória | Queda espúria ao final | Marcação, censura, S10, coleta em 2027.2 | Baixo a moderado |
| 8 | Município de residência ignorado | Subestimação não diferencial | Reporte anual do percentual; verificação de estabilidade | Baixo, se estável |
| 9 | Índice posicional do TABNET | Erro de extração silencioso | Reverificação a cada extração; reprodução independente | Baixo |
| 10 | Denominador defasado | Deslocamento de nível | Sinalização das células; S6, S15 | Moderado até a verificação da fração SUS-dependente |
| 11 | Falácia ecológica | Inferência indevida sobre mulheres | Restrição explícita das conclusões ao nível municipal | Controlado por escopo |
| 12 | Heterogeneidade de qualidade laboratorial | Ruído entre unidades | Efeitos aleatórios absorvem heterogeneidade estável; variação temporal não mensurável | Moderado, não mensurável |
| 13 | Defasagem coleta–liberação do laudo | Deslocamento dos coeficientes no tempo | Subseção 5.4.1; S16; covariável QualiCito | Moderado |
| 14 | Composição e exposição da série-controle | **Sinal do viés depende do sinal do efeito**; realocação torna o contraste anticonservador | Diagnóstico da soma das séries; S19; reporte como limite superior quando houver assinatura de realocação | Moderado |
| 15 | Múltiplas comparações | Falsos positivos | Estimando primário declarado; hierarquia de desfechos; ênfase em magnitude e intervalo, não em dicotomia | Controlado por disciplina de reporte |

## Apêndice E — Pendências de verificação anteriores à submissão

1. Relação nominal de orientadores com vaga em 2027 (item 4.4 do edital do PPGSP/IAM) e redação do parágrafo de aderência institucional (seção 7, item 9).
2. Norma bibliográfica exigida por cada programa: nenhum dos dois editais especifica ABNT ou Vancouver, e na Fiocruz a formatação das referências é item pontuado. Consultar as duas secretarias.
3. Número de regiões e macrorregiões de saúde e ato instituidor, no Plano Diretor de Regionalização vigente da SES-PE.
4. Ato(s) que suspenderam ou postergaram a apuração e o pagamento do componente de desempenho do Previne Brasil durante a ESPIN, e competência do primeiro repasse por ISF apurado (Tabela 1, τ1; H1; S21).
5. Valores de incentivo do componente de qualidade por classificação e tipo de equipe, para converter a fração de 2,9% em reais por equipe/mês (Apêndice C).
6. Disponibilidade e granularidade da série mensal municipal de beneficiários de planos privados na ANS (S6). Se não se confirmar, mover a ameaça para o Apêndice D como não testável.
7. Disponibilidade da série mensal municipal de repasses do Fundo Nacional de Saúde / e-Gestor APS, 2018-2026 (objetivo 5).
8. Disponibilidade das classificações do C7 por INE no e-Gestor APS (H4).
9. Comunicado SAPS de julho de 2022 sobre a regra do denominador de 85%: recuperar por Wayback Machine, comparação de versões da nota técnica ou pedido via Lei de Acesso à Informação. Enquanto não recuperado, não usar como referência normativa.
10. Publicação da diretriz CARITS na EQUATOR Network, a reconsultar na redação final.
11. **Dados bibliográficos incompletos em seis entradas.** CORRÊA et al. (2022), FERNÁNDEZ-DEAZA et al. (2024), FERRARI et al. (2025), MASSUDA (2020), OLIVEIRA et al. (2024) e SANTOS, SILVA e SILVA (2012) são usadas no dossiê depurado por seus achados, sem que a referência completa esteja registrada. **Nenhum dado bibliográfico foi inferido ou completado por conjectura.** Recuperar autoria, título, periódico, volume, páginas e DOI em fonte primária antes da submissão; se alguma não se confirmar, retirar a afirmação correspondente do corpo do texto em vez de manter a citação. Cuidado específico com MASSUDA (2020), objeto de troca de autoria documentada com HARZHEIM (2020).

## Apêndice F — Protocolo operacional: extração, covariáveis e diagnósticos

**Extração.** POST ao CGI do TABNET/DATASUS, corpo em latin-1 (os nomes de campo são acentuados), resposta em formato `prn` dentro de bloco `<pre>`. Linha: município de residência, por expressão que concatena código e nome a partir da tabela de disseminação. Coluna: mês/ano de competência. Estratificação etária em faixas quinquenais, oito para a faixa-alvo e seis para a série-controle. Quatro armadilhas, verificadas em toda extração: (i) **a última coluna da resposta é o total da linha**, e contá-la duplica os valores; (ii) **entidades HTML colidem com o separador** — nomes acentuados são devolvidos como entidades que contêm ponto e vírgula, de modo que a decodificação deve preceder a separação de campos; (iii) **o TABNET responde HTTP 200 em erro de aplicação**, devolvendo página HTML, e a presença do bloco `<pre>` deve ser validada antes de aceitar a resposta; (iv) **o índice de procedimento é posicional dentro do arquivo de definição**, não o código SIGTAP, e muda se a definição for republicada. Limite prático de cerca de 60 competências por requisição, em lotes de 12 a 24.

**Asserções do autoteste (sem rede).** Descarte da coluna de total; decodificação de entidades antes da separação; validação do bloco `<pre>`; cardinalidade 185 do frame canônico obtido da API de localidades do IBGE para a UF 26; presença de agosto, setembro **e outubro** de 2022 na lista de competências inválidas; ausência de zero-fill em todas as 185 unidades numa mesma competência; e **nlevels(competência) = 108 após a exclusão das linhas**, para que a AR1 preserve as distâncias temporais.

**Covariáveis**

| Variável | Definição operacional | Fonte | Função |
|---|---|---|---|
| Porte populacional | População total do município, em estratos | POPSVS/IBGE | Estratificação e interação |
| Região e macrorregião de saúde | Pertencimento territorial | PDR vigente/SES-PE | Descrição e heterogeneidade |
| Cobertura de Estratégia Saúde da Família | Proporção da população coberta por eSF, por município e competência | e-Gestor APS/SISAB | Estratificação e interação |
| Estrato de vulnerabilidade | Quintis do Índice de Vulnerabilidade Social municipal, ano-base declarado | Ipea | Estratificação e interação |
| Variação do repasse federal em τ3 | Variação real per capita, deflacionada pelo IPCA, entre a média mensal de 2023 e a média das parcelas mai–dez/2024 | Apêndice E, item 7 | **Dose contínua** da exposição a τ3 (objetivo 5) |
| Implantação do SISCAN | Estabelecimentos com serviço de citopatologia habilitado, por município e competência | SCNES | Proxy **exógena** de completude de registro |
| Exposição ao programa estadual | Indicador binário para Recife e os oito municípios da fase inicial, a partir de dez/2021 | OPAS; SES-PE (2021) | Cointervenção; estratificação e S7 |
| Substituição tecnológica | Registro municipal do procedimento molecular de HPV, por competência | SIA/SUS, sem estratificação etária | Confundimento a partir de 2024; S5, S5b |
| Tempo de liberação de laudo | Percentual de laudos liberados em até 30 dias, por UF e ano | QualiCito/INCA | Modificador de efeito |
| Fração SUS-dependente | Razão beneficiários de planos privados / população, se tempo-variante disponível | Apêndice E, item 6 | S6 |
| Competência inválida / provisória | Indicadores binários | Construídos | Exclusão ou censura |

**Demais procedimentos.** Registros sem município de residência identificado são contabilizados e reportados por ano, sem redistribuição proporcional. A integridade é verificada por reprodução independente da extração e comparação dígito a dígito dos totais por competência e por município. A consistência do denominador é verificada pela soma das faixas quinquenais contra a população feminina total do município e ano. A série descritiva é validada externamente contra os totais publicados pelo INCA para Pernambuco, com o sistema de origem de cada série comparada declarado no reporte.

**Diagnósticos completos.** (1) Resíduos quantílicos simulados em duas versões, condicional e marginal, usando-se apenas a marginal para julgar adequação da média condicional. (2) Autocorrelação residual por rotação pela matriz de covariância estimada. (3) Resíduos médios por competência, inspecionados em particular dentro do segmento τ2–τ3. (4) Índice I de Moran sobre resíduos agregados por município, com matriz de contiguidade, reportado como descritivo; modelo BYM2 ajustado incondicionalmente (S11). (5) Influência, por reajuste com exclusão sequencial dos dez municípios de maior volume. (6) Convergência, por verificação de gradiente e hessiana, com reajuste sob otimizadores alternativos e reparametrização por padronização do eixo temporal.

**Especificação estratificada por idade.** Unidade município × faixa quinquenal × competência, offset log(N_ijt/36) da faixa j, efeito fixo de faixa, interações faixa × D_kt para os blocos de interesse, e estrutura `(1 + t | município)` mais `(1 | município:faixa)`. Os contrastes de interesse são as interações faixa × D₃.

## Apêndice G — Poder estatístico por simulação

Não existe literatura de poder para ITS com múltiplos pontos de mudança em painel de contagens. Liu et al. (2019) oferecem balizamento para uma série e uma interrupção em modelos *observation-driven*: com 48 observações, efeito combinado −1,0 na escala logarítmica e ausência de autocorrelação, o poder é 0,92 sob Poisson e 0,96 sob binomial negativa; para +1,0 nas mesmas condições, 0,99 em ambas. Os valores não são transferíveis a este desenho. A âncora para poder por simulação em modelos mistos é Green e MacLeod (2016); **o pacote `simr` é construído sobre `lme4`/`glmer` e não suporta `glmmTMB` nem estruturas AR1**, de modo que a via adotada é simular do objeto ajustado por `simulate()`, preservando família, offset, efeitos aleatórios de município **e de competência** e AR1. A geração inclui **v_t ativo**; omiti-lo produziria curvas grosseiramente otimistas.

A grade é deliberadamente reduzida por restrição computacional e declarada como tal: δ ∈ {0; 0,05; 0,10; 0,20} e γ ∈ {0,005; 0,010}, com 500 réplicas por célula na configuração principal de 185 municípios e 108 competências, mais duas configurações reduzidas avaliadas apenas em δ = 0,10 — cerca de 25 células e 12.500 ajustes. **Inclui-se a célula δ = 0 para verificação empírica da taxa de erro tipo I**, obrigatória quando o modelo de trabalho pode ser mal especificado. Réplicas não convergentes são contabilizadas no denominador do poder e o percentual é reportado. O teste é o de Wald sobre o coeficiente, a 5% bilateral. As curvas são reportadas separadamente para nível e para tendência, com o efeito mínimo detectável a 80%. A execução é em lote paralelizado, com semente fixada, e o tempo estimado é da ordem de dias de processamento: **o item computacionalmente oneroso do projeto é o estudo de poder, não o ajuste individual do modelo**.

## Apêndice H — Série-controle: descarte da mamografia e controle por característica

A **mamografia foi descartada** como controle: a Nota Metodológica agrega, na mesma fórmula ponderada do C7, o rastreamento do colo do útero (25 a 64 anos, 36 meses, 20 pontos) e o de mama (50 a 69 anos, 24 meses, 20 pontos) (BRASIL, 2026a), o que faz da série de controle objeto do mesmo incentivo — contaminação no sentido exato de Lopez Bernal et al. (2018). A contaminação financeira efetiva começa em τ4, mas a restrição adotada é mais conservadora e vai até **τ3**, porque a arquitetura do C7 é instituída pela Portaria 3.493/2024 e pode ter induzido antecipação de reorganização da oferta antes do início da apuração. Acresce razão técnica independente: as definições do TABNET divergem no campo de competência, com o citopatológico usando a data de liberação do laudo e a mamografia a competência de faturamento.

O controle adotado é **por característica da população**: citopatológicos em mulheres fora da faixa de 25 a 64 anos, da mesma definição, com faixas quinquenais complementares e o mesmo recorte por residência. Essas mulheres são atendidas pela mesma rede, pelos mesmos profissionais e laboratórios, registradas no mesmo sistema e com o mesmo campo de competência, e sofreram o mesmo choque pandêmico, mas não integram o numerador de nenhum indicador de cofinanciamento. O modelo controlado acrescenta indicador de grupo G e suas interações com os termos de interrupção, sendo δ_k^dif o contraste de interesse; o offset é log da população feminina complementar da faixa correspondente, a estrutura aleatória é `(1 + t | município:grupo)`, a AR1 é estimada **separadamente por grupo** e v_t é compartilhado. ITS simples e ITS controlado são reportados lado a lado.

Três limitações. A série-controle é menor em volume — 571.866 exames contra 2.578.890 na série-alvo —, o que reduz sua precisão. É mais sensível a mudanças de composição populacional. E, sobretudo, **não é estritamente não exposta, sendo a direção do viés dependente do sinal do efeito**: se o efeito no grupo-alvo for positivo, uma queda autônoma do controle por qualificação da oferta é conservadora; se for nulo ou negativo — cenário que H2 a H4 tornam mais provável —, é **anticonservadora** e pode gerar diferença espúria. Pior: sob capacidade laboratorial limitada, com evidência direta disso no estado (SANTOS; SILVA; SILVA, 2012; INCA, 2023), a resposta ao incentivo é realocar exames de fora para dentro da faixa a volume total constante, caso em que a série-alvo sobe pela mesma causa que faz a série-controle cair e o contraste é inflado. Diagnóstico pré-especificado: verificar se a **soma** das duas séries permanece estável em torno de cada τ; estabilidade da soma com movimento oposto das partes é assinatura de realocação, e nesse caso o ITS controlado é reportado como **limite superior** do efeito. Acrescenta-se S19, controle restrito a 15 a 24 anos, excluindo 65 anos ou mais, dado que exames em 65–69 podem decorrer do critério de encerramento aos 64 anos com dois exames negativos, o que os torna programaticamente ligados à faixa-alvo. O sinal do viés será declarado ao interpretar cada coeficiente controlado.

## Apêndice I — Análise documental comparativa: corpus e procedimento

Em um campo em que o gestor federal reformulou duas vezes o instrumento de aferição sem publicar ponte de comparabilidade, documentar sistematicamente a (in)comparabilidade é resultado de pesquisa. O corpus reúne atos normativos federais, notas técnicas e metodológicas da SAPS/MS com identificador SEI e fichas de qualificação de indicadores, todos com localizador, acrescidos de três componentes que a camada federal isolada não cobre: **resoluções da Comissão Intergestores Bipartite de Pernambuco** sobre cofinanciamento da APS no período; **posicionamentos públicos de CONASS, CONASEMS e ABRASCO** sobre os dois modelos; e as **tabelas de valores de incentivo por componente, classificação e tipo de equipe**, sem as quais a matriz compara definições de indicador e não intensidades de exposição. Fontes sem localizador verificável são excluídas e registradas como pendência. A extração é dirigida por matriz de dimensões, com registro literal dos trechos que sustentam cada célula; a **dupla conferência é realizada pela pesquisadora em dois momentos separados por, no mínimo, quinze dias, com registro das discordâncias e arbitragem pelo orientador**; divergências entre texto normativo e material secundário prevalecem em favor do primeiro.

O produto é a matriz do Apêndice C, que classifica cada dimensão em comparabilidade preservada, condicionada a ajuste explicitado, ou incomparabilidade, e registra a existência ou inexistência de fator de conversão, série retrocalculada ou tabela de equivalência publicada pelo gestor federal — cuja ausência, se confirmada, é ela própria o achado. Registra-se ainda, como achado documental de interesse próprio, a assimetria entre o volume de crítica institucional dirigido ao Previne Brasil em 2019-2020 e a ausência de posicionamento institucional localizado sobre o modelo de 2024, asseveração que a busca sistemática no corpus permite confirmar ou refutar.


---

# NOTA DE DERIVAÇÃO EDITORIAL E ORÇAMENTO DE PALAVRAS

Este é o **documento-mãe: não é submetível como está**, e a razão é de extensão. O corpo (Identificação a Orçamento) tem cerca de **11.400 palavras**, as referências cerca de **2.150** em **57 entradas**, e os apêndices cerca de **3.300**. O limite da Fiocruz é de 10 páginas **incluindo as referências**; o da UPE, 6 páginas excluída a capa. Em A4 com espaçamento 1,5, isso corresponde a aproximadamente **3.900 e 2.400 palavras**. O corte não é aparo: é reescrita contra orçamento, e o orçamento é o seguinte.

| Seção | Mãe | **Fiocruz (meta 3.900)** | **UPE (meta 2.400)** |
|---|---:|---:|---:|
| Identificação / capa | 121 | 120 | fora da contagem |
| Resumo e palavras-chave | 303 | 200 | 150 |
| 1 Introdução | 2.076 | 620 | Introdução única com problema, justificativa e objetivos: **800** |
| 2 Justificativa | 634 | 450 | — |
| 3 Pergunta, premissa e hipóteses | 1.002 | 400 | 150 (pergunta e premissa; hipóteses cortadas) |
| 4 Objetivos | 573 | 300 | (no bloco de 800 acima) |
| 5 Métodos | 4.700 | 1.100 | 700 |
| 5.x Produtos científico e técnico | (em 6) | 60 | **250** (subseção obrigatória, item 3.5.k) |
| 6 Resultados esperados e gestão | 537 | 0 (realocado) | 200 (dentro da Justificativa) |
| 7 Viabilidade | 595 | 250 | 0 (suprimida) |
| 8 Cronograma | 283 | 180 | 120 |
| 9 Orçamento | 266 | **0 (suprimido)** | 120 |
| Referências | 2.154 (57 entradas) | **700 (30 entradas)** | **400 (18 entradas)** |
| Apêndices | 3.289 | 0 | 0 |
| **Total contado** | **≈ 16.900** | **≈ 3.880** | **≈ 2.390** |

**Cortes que recuperam páginas sem perder rubrica.** A equação em display de 5.4 sai e vira três linhas em prosa, retendo obrigatoriamente a menção ao efeito aleatório de competência. A discussão do SIA em 5.3 reduz-se a duas frases, com remessa ao documento de apoio. As tabelas de covariáveis, sensibilidades, (in)comparabilidade e vieses saem do corpo — a matriz de (in)comparabilidade é substituída por um parágrafo que enuncia as três rupturas e a inexistência de ponte de conversão. A seção 6 é dissolvida: o que ela promete já está nos objetivos 2, 4 e 8, e apenas os Produtos e o parágrafo de contribuição para a gestão sobrevivem, realocados. **Os Apêndices A a I constituem material de protocolo, depositado no repositório público junto com o pré-registro, e não acompanham nenhuma das duas submissões.**

**Referências.** Preservar obrigatoriamente: LOPEZ BERNAL (2017; 2018), WAGNER (2002), TURNER (2021), EWUSIE (2020), BROOKS (2017), CAMPBELL (2021), BENCHIMOL (2015), VON ELM (2007), RIBEIRO et al. (2025), DIAS et al. (2022), RIBEIRO, CORRÊA e MIGOWSKI (2022), CASTRO-NUNES et al. (2024), INCA (2016; 2023; 2025; 2026), BRASIL (2016; 2022a; 2024a; 2025a; 2026a; 2026b), CELLA, CORREA e BARANCELLI (2025), TOCCILLO et al. (2025), HO et al. (2025), MINCHIN et al. (2018), GURGEL et al. (2023), SELLERA et al. (2023), TOMAZELLI, RIBEIRO e DIAS (2022) e DUARTE, ARGENTON e CARVALHEIRA (2022). Sacrificar, nesta ordem: SANTOS, SILVA e SILVA (2012), BHASKARAN et al. (2013), TURNER et al. (2020), FERNÁNDEZ-DEAZA et al. (2024), CORRÊA et al. (2022), MAURO, ROTUNDO e GIANCOTTI (2019), SCHÖNHOLZER et al. (2023), FARDOUSI et al. (2022), RIEBLER et al. (2016), GREEN e MACLEOD (2016), LIU et al. (2019), NASCIMENTO et al. (2020), COSTA-RIBEIRO et al. (2026) e RUSSO et al. (2021; 2024), com remissão em bloco onde o argumento exigir ("a literatura de pagamento por desempenho na atenção primária converge para efeitos parciais ou nulos sobre rastreamento — ver HO et al., 2025, para a síntese mais recente"). **Antes de padronizar, confirmar com as duas secretarias se a norma exigida é ABNT ou Vancouver** (Apêndice E, item 2): nenhum dos dois editais a especifica, e na Fiocruz a formatação das referências é item pontuado.

**Divergências que impõem dois arquivos, e não um.** *Fiocruz:* mantém o bloco de Identificação com orientador nominal e linha de pesquisa; mantém Introdução e Justificativa como itens distintos, na ordem do Anexo VI; mantém Viabilidade como seção autônoma; mantém as hipóteses formalmente enunciadas, que valem 2,0 pontos no Anexo VII e que o edital da UPE sequer menciona; **suprime o Orçamento**. *UPE:* **suprime toda menção a docente, linha de orientador, Fiocruz, IAM e ao comitê de ética daquela instituição** — a seção de ética passa a referir "o Comitê de Ética em Pesquisa da instituição de vínculo", com os prazos regimentais do comitê correspondente; **mantém o Orçamento**; converte os Produtos em subseção obrigatória dentro dos procedimentos metodológicos, onde o item 3.5.k os exige e 2,0 dos 10,0 pontos os medem; move a contribuição para a gestão para dentro da Justificativa, onde outros 2,0 pontos medem articulação e aplicabilidade ao SUS; **suprime Viabilidade** como bloco autônomo, redistribuindo seus itens em duas frases nos métodos. Antes do envio, executar varredura de anonimização: nome da candidata, "Fiocruz", "IAM", "Aggeu", nomes de docentes, URL de repositório pessoal e metadados de autor do PDF.

**Em ambas as versões.** Gerar o PDF por Quarto ou LaTeX, com tipografia real — nunca colar Markdown em processador de texto —, conferindo visualmente a equação, os símbolos τ, δ, γ, φ e σ e as tabelas na prova impressa. Conferir uma a uma as alíneas de BRASIL, que são seis anos com múltiplas entradas. Resolver as onze pendências do Apêndice E, **sem as quais os marcadores [VERIFICAR] não podem ser removidos e não devem ser preenchidos por conjectura**. Passar revisão profissional de língua portuguesa, rubrica já prevista no orçamento. Conferir fonte, corpo, espaçamento, margens e contagem de páginas antes do envio: "projeto de pesquisa ultrapassou limite de páginas" consta nominalmente entre os motivos de indeferimento do ciclo anterior da UPE.
