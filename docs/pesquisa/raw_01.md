{
  "eixo": "Séries temporais interrompidas em painel aplicadas à avaliação de políticas de saúde: precedentes brasileiros, múltiplos pontos de mudança, modelos de contagem (GLMM binomial negativo com AR1), sazonalidade harmônica, dependência espacial, série-controle e reporte",
  "sintese": "A literatura metodológica de séries temporais interrompidas (ITS) está consolidada em torno de um núcleo pequeno e bem definido, e o projeto deve ancorar-se nele explicitamente. Wagner et al. (2002) formalizou a regressão segmentada em avaliação de políticas; Lopez Bernal, Cummins e Gasparrini (2017) é o tutorial canônico. Um detalhe que blinda a banca: esse tutorial recebeu **corrigendum em 2020** porque a definição algébrica original do modelo segmentado induzia interpretação errônea dos coeficientes de nível e de tendência. Citar a versão corrigida — e não apenas o artigo de 2017 — sinaliza leitura de primeira mão. Os dois artigos irmãos completam o arcabouço: Lopez Bernal et al. (2018) tipifica seis classes de controle para ITS (localidade, característica, comportamento, coorte histórica, **desfecho-controle** e **período-controle**), e Lopez Bernal et al. (2019) delimita as fronteiras entre DiD, ITS controlado e controle sintético.\n\nSobre o **estado da prática**, três revisões dão munição para justificar escolhas por exclusão. Hudson, Fielding e Ramsay (2019) mostram, em 116 estudos, reporte incompleto sistemático (mudança de inclinação relatada em 84%, de nível em 70%, efeitos de longo prazo em apenas 21%). Turner et al. (2020) documenta o mesmo hiato em 200 estudos de saúde pública. E Turner et al. (2021), comparando seis métodos em 190 séries reais, produz o número mais útil ao projeto: estimativas de autocorrelação só convergem entre métodos em séries com **≥100 pontos** (medianas de 0,20 com REML contra 0,04–0,05 com ARIMA/Prais-Winsten). Com 108 meses, a janela jan/2018–dez/2026 está exatamente no limiar em que a autocorrelação é estimável com credibilidade — argumento direto para **especificar AR1 a priori** em vez de aplicar correção post hoc, e para pré-registrar o método com análises de sensibilidade, como os autores recomendam.\n\nO **precedente brasileiro** divide-se em duas tradições que o projeto propõe cruzar. A primeira usa séries agregadas nacionais ou macrorregionais com regressão segmentada, Prais-Winsten, ARIMA ou Joinpoint: Nascimento et al. (2020) sobre mortalidade prematura por CCU e o Pacto pela Saúde; Pinto et al. (2022) sobre sífilis congênita; Ferreira et al. (2023) sobre rastreamentos mamário e cervical; Maia, Campos e Castanheira (2024) sobre austeridade fiscal e gasto municipal em saúde. A segunda usa **painel de municípios com modelos de contagem e efeitos fixos**: Rasella et al. (2013), no Lancet, com binomial negativo de efeitos fixos em painel nacional de municípios para o Bolsa Família; Hone et al. (2020), em 5.565 municípios, para o Mais Médicos; Russo et al. (2021), painel de efeitos fixos com binomial negativo em análise de sensibilidade, para o PMAQ-AB. Essas duas últimas são especialmente instrutivas por trazerem, além do modelo, **testes de desfecho-placebo** — Russo et al. usam internações por acidente de transporte como controle negativo, precisamente a lógica do \"desfecho-controle\" de Lopez Bernal et al. (2018).\n\nO cruzamento das tradições — ITS com múltiplos pontos de mudança **em painel municipal de contagens** — é raro na literatura brasileira e constitui a contribuição metodológica do projeto. Para heterogeneidade entre unidades, Ewusie et al. (2020) formaliza ITS multicêntrico com ponderação por variabilidade intra e entre sítios. Para o modelo em si, Brooks et al. (2017) é a citação obrigatória do glmmTMB, que suporta binomial negativo (NB1/NB2), offset e estruturas AR1. Sobre sobredispersão e excesso de zeros em contagens municipais pequenas, Campbell (2021) é a referência crítica: testar-e-então-selecionar zero-inflação ou sobredispersão infla falsos positivos em amostras pequenas. A recomendação prática é **pré-especificar NB2**, comparar com NB1 e zero-inflado por AIC, e reportar resíduos quantílicos (DHARMa) em vez de encadear testes de hipótese. Para poder estatístico, Green e MacLeod (2016) é a âncora do simr, mas há uma restrição honesta a declarar: **simr é construído sobre lme4 e não cobre glmmTMB nem AR1** — a via viável é simular diretamente do objeto ajustado via `simulate()`, tomando Liu et al. (2019) como referência de arcabouço de poder para ITS de contagens (com n=48 e efeito ±1,0 na escala log, poder ≈0,92 em Poisson e ≈0,96 em binomial negativo).\n\nSazonalidade por harmônicos de Fourier tem em Bhaskaran et al. (2013) a âncora conceitual — confirmada — e em Duarte, Argenton e Carvalheira (2022) o precedente aplicado quase perfeito: ITS com GLM quasi-Poisson, harmônicos pareados para sazonalidade mensal e bootstrap de Monte Carlo para contrafactuais, aplicado exatamente a contagens de Papanicolaou e mamografia em São Paulo durante a pandemia.\n\nDependência espacial deve ser tratada como diagnóstico escalonado, não como premissa. Riebler et al. (2016) é a referência do BYM2 (reparametrização escalada do BYM, com precisão e mistura separáveis); Costa-Ribeiro et al. (2026) demonstra a via prática em um painel municipal de ITS no Paraná — Poisson com offset de casos esperados, efeitos temporais por local, INLA. O protocolo defensável é: ajustar o GLMM, calcular I de Moran sobre resíduos agregados por município e escalar para BYM2 apenas se houver autocorrelação residual detectada.\n\nPor fim, o achado mais consequente deste eixo é negativo. **A mamografia de rastreamento não é série-controle defensável.** A nota metodológica do indicador C7 do Saúde Brasil 360 mostra que ele agrega quatro boas práticas ponderadas, incluindo simultaneamente citopatológico (25–64 anos, 36 meses) **e rastreamento mamário (50–69 anos, 24 meses)**, além de vacina HPV (9–14 anos) e consulta de saúde sexual e reprodutiva (14–69 anos). De τ4 em diante, mamografia é co-incentivada pelo mesmo indicador — contaminação no sentido exato de Lopez Bernal et al. (2018). A saída é dupla: manter a mamografia como controle **apenas para τ1–τ3** (o indicador nº 4 do Previne Brasil não contemplava mamografia) e adotar, para τ3–τ4, um controle por característica — citopatológicos em mulheres **fora** da faixa 25–64 anos, que partilham choque pandêmico e via de oferta mas não entram no numerador de nenhum indicador de financiamento.",
  "referencias": [
    {
      "autores": "Lopez Bernal J, Cummins S, Gasparrini A",
      "ano": "2017",
      "titulo": "Interrupted time series regression for the evaluation of public health interventions: a tutorial",
      "veiculo": "International Journal of Epidemiology, 46(1):348-355",
      "localizador": "10.1093/ije/dyw098 — https://academic.oup.com/ije/article/46/1/348/2622842",
      "achado": "Tutorial canônico de ITS: especificação da regressão segmentada, tratamento de autocorrelação, sazonalidade, período de transição e contrafactual. ATENÇÃO: recebeu corrigendum publicado em 2021 (Int J Epidemiol 50(3):1045-1046, https://academic.oup.com/ije/article/50/3/1045/5900884) porque a definição algébrica original do modelo podia levar a interpretação errônea dos parâmetros estimados. Código R/Stata e dados públicos em github.com/gasparrini/2017_lopezbernal_IJE_codedata.",
      "uso_no_projeto": "métodos — âncora principal do delineamento ITS; citar obrigatoriamente com o corrigendum",
      "confianca": "verificada-metadados"
    },
    {
      "autores": "Lopez Bernal J, Cummins S, Gasparrini A",
      "ano": "2018",
      "titulo": "The use of controls in interrupted time series studies of public health interventions",
      "veiculo": "International Journal of Epidemiology, 47(6):2082-2093",
      "localizador": "10.1093/ije/dyy135 — https://academic.oup.com/ije/article/47/6/2082/5049576",
      "achado": "Tipifica seis classes de controle em ITS: localidade, característica da população, comportamento, coorte histórica, desfecho-controle e período-controle. Recomenda definir a priori quais eventos confundidores concorrentes podem existir, ajustar simultaneamente ITS simples e ITS controlado, e interpretar com cautela quando divergem. Alerta explicitamente para contaminação (a intervenção afeta o controle indiretamente) e para mudanças diferenciais de composição populacional ao longo do tempo.",
      "uso_no_projeto": "métodos — fundamenta a escolha (e o descarte) da mamografia como série-controle; base para o controle por característica (mulheres fora de 25-64 anos)",
      "confianca": "verificada-texto-completo"
    },
    {
      "autores": "Lopez Bernal J, Cummins S, Gasparrini A",
      "ano": "2019",
      "titulo": "Difference in difference, controlled interrupted time series and synthetic controls",
      "veiculo": "International Journal of Epidemiology, 48(6):2062-2063",
      "localizador": "10.1093/ije/dyz050 — https://academic.oup.com/ije/article/48/6/2062/5419048",
      "achado": "Carta metodológica que delimita as fronteiras conceituais entre diferenças-em-diferenças, ITS controlado e controle sintético, esclarecendo que não são sinônimos e quais premissas cada um exige.",
      "uso_no_projeto": "métodos — justificar por que ITS em painel (e não DiD ou controle sintético) é o delineamento adequado",
      "confianca": "verificada-metadados"
    },
    {
      "autores": "Wagner AK, Soumerai SB, Zhang F, Ross-Degnan D",
      "ano": "2002",
      "titulo": "Segmented regression analysis of interrupted time series studies in medication use research",
      "veiculo": "Journal of Clinical Pharmacy and Therapeutics, 27(4):299-309",
      "localizador": "10.1046/j.1365-2710.2002.00430.x — https://onlinelibrary.wiley.com/doi/abs/10.1046/j.1365-2710.2002.00430.x",
      "achado": "Formalização clássica da regressão segmentada para avaliação de intervenções de política e educação, com decomposição em mudança de nível e mudança de tendência. Clássico-âncora conceitual do desenho.",
      "uso_no_projeto": "introdução e métodos — âncora histórica da regressão segmentada",
      "confianca": "verificada-metadados"
    },
    {
      "autores": "Turner SL, Karahalios A, Forbes AB, Taljaard M, Grimshaw JM, McKenzie JE",
      "ano": "2021",
      "titulo": "Comparison of six statistical methods for interrupted time series studies: empirical evaluation of 190 published series",
      "veiculo": "BMC Medical Research Methodology, 21:134",
      "localizador": "10.1186/s12874-021-01306-w — https://pmc.ncbi.nlm.nih.gov/articles/PMC8235830/",
      "achado": "Compara OLS, OLS com erros Newey-West, Prais-Winsten, REML, REML-Satterthwaite e ARIMA em 190 séries publicadas. Mudanças de nível padronizadas medianas variaram de 1,22 a 1,49 entre métodos; mudanças de inclinação foram estáveis em 0,13. Erros-padrão do ARIMA foram sistematicamente maiores (limites de concordância de 61% menores a 460% maiores vs Newey-West). Concordância na significância dicotomizada a 5%: 79,3% a 97,1%. CRUCIAL: estimativas de autocorrelação divergem entre métodos (mediana 0,20 em REML vs 0,04-0,05 em ARIMA/PW) e só convergem em séries com ≥100 pontos. Recomenda pré-especificar o método no protocolo e conduzir análises de sensibilidade.",
      "uso_no_projeto": "métodos — justifica AR1 especificado a priori e o valor dos 108 meses; justifica pré-especificação e sensibilidade; discussão de limitações",
      "confianca": "verificada-texto-completo"
    },
    {
      "autores": "Turner SL, Karahalios A, Forbes AB, Taljaard M, Grimshaw JM, Korevaar E, Cheng AC, Bero L, McKenzie JE",
      "ano": "2020",
      "titulo": "Design characteristics and statistical methods used in interrupted time series studies evaluating public health interventions: a review",
      "veiculo": "Journal of Clinical Epidemiology (revisão de 200 estudos indexados no PubMed, 2013-2017)",
      "localizador": "https://www.jclinepi.com/article/S0895-4356(19)30724-3/abstract — PII S0895-4356(19)30724-3",
      "achado": "Revisão de 200 estudos de ITS avaliando intervenções e exposições de saúde pública, documentando heterogeneidade e lacunas nas características de delineamento e nos métodos estatísticos empregados. Confirma hiato persistente entre a orientação metodológica e a prática publicada.",
      "uso_no_projeto": "métodos e discussão — sustentar que o rigor proposto (AR1 explícito, harmônicos, offset, múltiplos τ) está acima da prática média",
      "confianca": "verificada-metadados"
    },
    {
      "autores": "Hudson J, Fielding S, Ramsay CR",
      "ano": "2019",
      "titulo": "Methodology and reporting characteristics of studies using interrupted time series design in healthcare",
      "veiculo": "BMC Medical Research Methodology, 19:137",
      "localizador": "10.1186/s12874-019-0777-x — https://ncbi.nlm.nih.gov/pmc/articles/PMC6609377",
      "achado": "Revisão de 116 estudos de ITS publicados em 2015 (mínimo de 2 pontos pré e 1 pós). Estimativas de efeito reportadas como mudança de inclinação em 84%, mudança de nível em 70%, e mudança de nível de longo prazo em apenas 21%. Conclui que há problemas no reporte de características de delineamento e de resultados, e defende explicitamente a necessidade de desenvolver diretrizes formais de reporte para ITS.",
      "uso_no_projeto": "métodos (plano de reporte) e discussão — documenta a ausência de diretriz consolidada de reporte para ITS até 2019",
      "confianca": "verificada-resumo"
    },
    {
      "autores": "Turner SL, Forbes AB, Karahalios A, Taljaard M, McKenzie JE",
      "ano": "2021",
      "titulo": "Creating effective interrupted time series graphs: review and recommendations",
      "veiculo": "Research Synthesis Methods, 12(1):106-117 (online 2020)",
      "localizador": "10.1002/jrsm.1435 — https://onlinelibrary.wiley.com/doi/10.1002/jrsm.1435 (também https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7818488/)",
      "achado": "Revisão e recomendações para representação gráfica de ITS: gráficos eficazes devem incluir os pontos de dados observados, linhas de tendência por segmento com quebras nítidas nos pontos de interrupção, estimativa de sazonalidade, e intervalos de confiança em torno da tendência ajustada e do contrafactual. Boa visualização permite extração digital dos dados para revisões sistemáticas.",
      "uso_no_projeto": "métodos (plano de apresentação de resultados) — especificar os elementos das figuras de ITS na dissertação",
      "confianca": "verificada-metadados"
    },
    {
      "autores": "Ewusie JE, Thabane L, Beyene J, Straus SE, Hamid JS",
      "ano": "2020",
      "titulo": "MultiCenter Interrupted Time Series Analysis: Incorporating Within and Between-Center Heterogeneity",
      "veiculo": "Clinical Epidemiology, 12:625-636",
      "localizador": "10.2147/CLEP.S231843 — https://pubmed.ncbi.nlm.nih.gov/32606988/",
      "achado": "Propõe regressão segmentada ponderada (wSR) para ITS multicêntrico, incorporando pesos que refletem variabilidade tanto em nível de participante quanto de sítio. A wSR produziu as estimativas mais precisas (ICs 95% mais estreitos) e maior poder que a regressão segmentada convencional e a análise agrupada. Análise agrupada e wSR foram comparáveis com ≤4 sítios e heterogeneidade moderada-alta entre sítios. Argumenta que a regressão segmentada convencional não é ótima quando os dados são agregados entre participantes e cenários.",
      "uso_no_projeto": "métodos — justificar efeitos aleatórios por município em vez de agregar a série estadual; heterogeneidade intra e entre unidades",
      "confianca": "verificada-resumo"
    },
    {
      "autores": "Liu W, Ye S, Barton BA, Fischer MA, Lawrence C, Rahn EJ, Danila MI, Saag KG, Harris PA, Lemon SC, Allison JJ, Zhang B",
      "ano": "2019",
      "titulo": "Simulation-based power and sample size calculation for designing interrupted time series analyses of count outcomes in evaluation of health policy interventions",
      "veiculo": "Contemporary Clinical Trials Communications, 17:100474",
      "localizador": "10.1016/j.conctc.2019.100474 — https://pmc.ncbi.nlm.nih.gov/articles/PMC6920506/",
      "achado": "Arcabouço de cálculo de poder e tamanho amostral por simulação para ITS com desfechos de contagem, em modelos log-lineares observation-driven de baixa ordem (LL(0,1)) sob Poisson e binomial negativo (para sobredispersão). Poder cresce com tamanho amostral e magnitude do efeito. Sob Poisson o poder cresce monotonicamente com a autocorrelação (γ1 de -0,9 a 0,9); sob binomial negativo o padrão é não-monotônico, especialmente para efeitos maiores. Com n=48 observações e β2+β3=±1,0, poder ≈0,92 (Poisson) e ≈0,96 (BN). Poder difere substancialmente entre testar mudança de nível, de tendência, ou o efeito combinado. Pacote R tscount; código de simulação no apêndice.",
      "uso_no_projeto": "métodos — arcabouço de poder estatístico específico para ITS de contagem, a ser adaptado ao painel municipal",
      "confianca": "verificada-texto-completo"
    },
    {
      "autores": "Green P, MacLeod CJ",
      "ano": "2016",
      "titulo": "SIMR: an R package for power analysis of generalized linear mixed models by simulation",
      "veiculo": "Methods in Ecology and Evolution, 7(4):493-498",
      "localizador": "10.1111/2041-210X.12504 — https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.12504",
      "achado": "Apresenta o pacote simr para análise de poder de GLMM por simulação de Monte Carlo em três passos (simular resposta a partir do modelo ajustado, reajustar, aplicar teste), com curvas de poder para avaliar trade-off entre poder e tamanho amostral. RESTRIÇÃO PRÁTICA A DECLARAR: o simr é construído sobre modelos lme4/glmer e não suporta objetos glmmTMB nem estruturas de covariância AR1 — para o desenho proposto será necessário simular diretamente do objeto glmmTMB ajustado (método simulate()) e replicar a lógica de três passos manualmente.",
      "uso_no_projeto": "métodos — âncora bibliográfica do poder por simulação em GLMM, com ressalva explícita sobre incompatibilidade com glmmTMB/AR1",
      "confianca": "verificada-metadados"
    },
    {
      "autores": "Brooks ME, Kristensen K, van Benthem KJ, Magnusson A, Berg CW, Nielsen A, Skaug HJ, Maechler M, Bolker BM",
      "ano": "2017",
      "titulo": "glmmTMB balances speed and flexibility among packages for zero-inflated generalized linear mixed modeling",
      "veiculo": "The R Journal, 9(2):378-400",
      "localizador": "10.32614/RJ-2017-066 — https://journal.r-project.org/archive/2017/RJ-2017-066/",
      "achado": "Apresenta o glmmTMB para GLMM com contagens correlacionadas, sobredispersão e excesso de zeros, mostrando que é mais rápido que glmmADMB, MCMCglmm e brms, e mais flexível que INLA e mgcv para modelagem zero-inflada. O pacote implementa binomial negativo (nbinom1 com variância linear na média e nbinom2 com variância quadrática), offset, e estruturas de covariância estruturadas incluindo AR1 de primeira ordem (ar1 homogêneo e hetar1 heterogêneo) — documentado nas vinhetas oficiais do pacote (cran.r-project.org/web/packages/glmmTMB/vignettes/glmmTMB.pdf).",
      "uso_no_projeto": "métodos — citação obrigatória do software; fundamenta a viabilidade de BN + offset + AR1 intra-município na mesma especificação",
      "confianca": "verificada-metadados"
    },
    {
      "autores": "Campbell H",
      "ano": "2021",
      "titulo": "The consequences of checking for zero-inflation and overdispersion in the analysis of count data",
      "veiculo": "Methods in Ecology and Evolution, 12(4):665-680",
      "localizador": "10.1111/2041-210X.13559 — https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13559 (preprint arXiv:1911.00115)",
      "achado": "Demonstra que, com tamanhos amostrais pequenos, a seleção de modelo baseada em testes de escore preliminares ou em critérios de informação (AIC, BIC) para decidir sobre zero-inflação e sobredispersão pode inflar substancialmente a taxa de falsos positivos. Recomenda cautela ao rejeitar a hipótese nula de ausência de associação após tal seleção sequencial.",
      "uso_no_projeto": "métodos — justificar pré-especificação de binomial negativo (NB2) em vez de estratégia testar-e-selecionar; sustentar uso de resíduos quantílicos (DHARMa) em lugar de cadeia de testes",
      "confianca": "verificada-metadados"
    },
    {
      "autores": "Bhaskaran K, Gasparrini A, Hajat S, Smeeth L, Armstrong B",
      "ano": "2013",
      "titulo": "Time series regression studies in environmental epidemiology",
      "veiculo": "International Journal of Epidemiology, 42(4):1187-1195",
      "localizador": "10.1093/ije/dyt092 — https://academic.oup.com/ije/article/42/4/1187/657875",
      "achado": "Tutorial de referência para regressão de séries temporais com desfechos de contagem em epidemiologia: modelos Poisson/quasi-Poisson e binomial negativo, controle de tendência de longo prazo e de sazonalidade por splines e por termos harmônicos (senos e cossenos de Fourier), tratamento de sobredispersão e de autocorrelação residual, e defasagens. Código R e dados em github.com/gasparrini/2013_bhaskaran_IJE_codedata.",
      "uso_no_projeto": "métodos — âncora conceitual dos harmônicos de Fourier para sazonalidade mensal e da escolha da família de contagem",
      "confianca": "verificada-metadados"
    },
    {
      "autores": "Duarte MBO, Argenton JLP, Carvalheira JBC",
      "ano": "2022",
      "titulo": "Impact of COVID-19 in Cervical and Breast Cancer Screening and Systemic Treatment in São Paulo, Brazil: An Interrupted Time Series Analysis",
      "veiculo": "JCO Global Oncology, 8:e2100371",
      "localizador": "10.1200/GO.21.00371 — https://pmc.ncbi.nlm.nih.gov/articles/PMC9225667/",
      "achado": "ITS de jan/2017 a nov/2021 em São Paulo com GLM quasi-Poisson ajustando tempo, início da pandemia, termo de interação e HARMÔNICOS PAREADOS para sazonalidade mensal; contrafactual por bootstrap de Monte Carlo com IC 95%. Estimou aproximadamente 1.149.727 preventivos (Papanicolaou), 713.616 mamografias e 2.693 conizações perdidos ou atrasados. Redução de 25% no início de terapia adjuvante em estádios I/II de mama; excesso de 156 pacientes iniciando cuidado paliativo em CCU avançado. Rastreamento mostrou-se mais vulnerável que tratamento sistêmico, com recuperação lenta que se estendeu além de julho/2020 (revogação das recomendações oficiais de suspensão).",
      "uso_no_projeto": "métodos (precedente aplicado quase idêntico: harmônicos + contagem + citopatológico e mamografia) e discussão (magnitude do choque pandêmico e recuperação lenta)",
      "confianca": "verificada-texto-completo"
    },
    {
      "autores": "Rasella D, Aquino R, Santos CAT, Paes-Sousa R, Barreto ML",
      "ano": "2013",
      "titulo": "Effect of a conditional cash transfer programme on childhood mortality: a nationwide analysis of Brazilian municipalities",
      "veiculo": "The Lancet, 382(9886):57-64",
      "localizador": "10.1016/S0140-6736(13)60715-1 — https://pubmed.ncbi.nlm.nih.gov/23683599/",
      "achado": "Análise de painel nacional de municípios brasileiros com modelos BINOMIAL NEGATIVO DE EFEITOS FIXOS para avaliar o Bolsa Família sobre mortalidade em menores de 5 anos. A mortalidade em menores de 5 anos, global e por causas relacionadas à pobreza (desnutrição, diarreia, infecções respiratórias), diminuiu conforme aumentou a cobertura do programa. Marco do desenho ecológico de painel municipal com contagem em periódico de altíssimo impacto.",
      "uso_no_projeto": "métodos e justificativa — precedente maior de painel municipal com contagem binomial negativa em avaliação de política brasileira; demonstra aceitação do desenho",
      "confianca": "verificada-metadados"
    },
    {
      "autores": "Hone T, Powell-Jackson T, Santos LMP, Soares RS, Oliveira FP, Sanchez MN, Harris M, Santos FOS, Millett C",
      "ano": "2020",
      "titulo": "Impact of the Programa Mais Médicos (more doctors Programme) on primary care doctor supply and amenable mortality: quasi-experimental study of 5565 Brazilian municipalities",
      "veiculo": "BMC Health Services Research, 20(Suppl 2):873",
      "localizador": "10.1186/s12913-020-05716-2 — https://pmc.ncbi.nlm.nih.gov/articles/PMC7491024/",
      "achado": "Painel de 5.565 municípios brasileiros, 2008-2017, com diferenças-em-diferenças e efeitos fixos longitudinais (efeitos fixos de município, de estado-trimestre-ano, e confundidores socioeconômicos variantes no tempo). O PMM associou-se a +5,7 médicos de atenção primária por 100 mil habitantes (IC95% 5,1-6,4), embora 15,1 médicos PMM tenham sido parcialmente compensados por 9,4 médicos não-PMM a menos. Mortalidade evitável reduziu 1,06 óbitos por 100 mil por ano (IC95% -1,78 a -0,34), cerca de 1,3%. Efeitos heterogêneos concentrados em municípios prioritários e naqueles com baixa densidade médica inicial.",
      "uso_no_projeto": "métodos e justificativa — precedente de painel municipal com escalonamento temporal de política e efeitos fixos; modelo de reporte de heterogeneidade",
      "confianca": "verificada-texto-completo"
    },
    {
      "autores": "Russo LX, Powell-Jackson T, Maia Barreto JO, Borghi J, Kovacs R, Gurgel Junior GD, Rasella D, Hone T",
      "ano": "2021",
      "titulo": "Pay for performance in primary care: the contribution of the Programme for Improving Access and Quality of Primary Care (PMAQ) on avoidable hospitalisations in Brazil, 2009-2018",
      "veiculo": "BMJ Global Health, 6(7):e005429",
      "localizador": "10.1136/bmjgh-2021-005429 — https://pmc.ncbi.nlm.nih.gov/articles/PMC8273460/",
      "achado": "Painel de efeitos fixos de 5.564 municípios, 2009-2018, com análise de sensibilidade em regressão BINOMIAL NEGATIVA reportando razões de taxa de incidência (IRR). Cada ponto percentual de aumento na participação no PMAQ reduziu a taxa de internação por condições sensíveis à atenção primária em 0,0356 por 10 mil habitantes de 0-64 anos (p=0,004), cerca de 60.829 internações evitadas em 2018; em menores de 5 anos, -0,0940 por 10 mil (p=0,012), ~11.936 internações. IMPORTANTE: TESTE DE PLACEBO com internações por acidente de transporte foi não significativo, sustentando a validade — precedente direto do uso de desfecho-controle.",
      "uso_no_projeto": "métodos — precedente de pagamento por desempenho em painel municipal com binomial negativo E de teste de desfecho-placebo (modelo para o controle não equivalente)",
      "confianca": "verificada-texto-completo"
    },
    {
      "autores": "Maia LR, Campos MR, Castanheira D",
      "ano": "2024",
      "titulo": "Fiscal austerity and municipal health spending: an interrupted time series study",
      "veiculo": "Revista de Saúde Pública, 58:42",
      "localizador": "10.11606/s1518-8787.2024058005772 — https://pmc.ncbi.nlm.nih.gov/articles/PMC11548907/",
      "achado": "ITS com modelagem ARIMA em painel de 5.569 municípios brasileiros, dados semestrais 2010-2019, intervenção no 1º semestre de 2015 (política de ajuste fiscal), estratificando municípios por porte (≤100 mil; 100.001-400.000; >400.000). Fonte: SIOPS. Impacto imediato: queda média nacional de ~6,70 per capita no gasto total em saúde, chegando a 10,39 nos municípios pequenos. Na tendência 2015-2019, apenas municípios grandes mantiveram impactos negativos sustentados, com redução significativa de transferências federais e de recursos próprios/estaduais.",
      "uso_no_projeto": "métodos (precedente de ITS em painel municipal publicado em RSP) e discussão (contexto de subfinanciamento concorrente na janela do estudo)",
      "confianca": "verificada-texto-completo"
    },
    {
      "autores": "Arato CVDB, Guerra LM, Probst LF, Pereira AC",
      "ano": "2025",
      "titulo": "Association of Previne Brasil Program with prenatal care and maternal-child mortality",
      "veiculo": "Revista de Saúde Pública, 59:e28",
      "localizador": "10.11606/s1518-8787.2025059006735 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12520718/",
      "achado": "Estudo ecológico nacional com 5.570 municípios comparando períodos pré (2016-2018) e pós (2019-2022) implantação do Previne Brasil. NÃO usa ITS: emprega regressão logística sobre a variação dicotomizada dos indicadores. Pré-natal aumentou em 86,7% dos municípios; mortalidade materna caiu em apenas 30,9% e mortalidade infantil em 42,6%. Sem associação significativa entre aumento do pré-natal e redução da mortalidade materna (OR=0,92; IC95% 0,78-1,09) ou infantil (OR=1,14; IC95% 0,97-1,34). Região, cobertura de atenção primária e porte populacional associaram-se às variações.",
      "uso_no_projeto": "justificativa e discussão — evidencia que a avaliação existente do Previne Brasil em painel municipal usa desenho antes-depois dicotomizado, não ITS; lacuna que o projeto preenche",
      "confianca": "verificada-texto-completo"
    },
    {
      "autores": "Nascimento MI, Massahud FC, Barbosa NG, Lopes CD, Rodrigues VC",
      "ano": "2020",
      "titulo": "Premature mortality due to cervical cancer: study of interrupted time series",
      "veiculo": "Revista de Saúde Pública, 54:139",
      "localizador": "10.11606/s1518-8787.2020054002528 — https://www.scielo.br/j/rsp/a/KnmjZZMDJzZKyrCXmPpGYBN/?lang=en",
      "achado": "ITS com regressão segmentada avaliando o efeito do Pacto pela Saúde sobre mortalidade prematura (30-69 anos) por CCU no Brasil e macrorregiões; pré-Pacto 1998-2006 e pós-Pacto 2010-2018, excluindo 2007-2009 como fase de implantação (período de transição). Mais de 119.000 óbitos na faixa-alvo. Brasil: aumento progressivo (coeficiente 0,513; IC95% 0,430-0,596). Nordeste foi a única região com redução imediata de nível (-0,635; IC95% -1,177 a -0,092) e tendência decrescente. Norte com maiores taxas absolutas (>20/100 mil). Conclui que a ITS não conseguiu demonstrar efetividade das iniciativas do Pacto pela Saúde.",
      "uso_no_projeto": "introdução, justificativa e métodos — precedente brasileiro de ITS aplicada a CCU; modelo de exclusão de período de transição em torno do ponto de mudança",
      "confianca": "verificada-resumo"
    },
    {
      "autores": "Ferreira HNC, Capistrano GN, Morais TNB, et al.",
      "ano": "2023",
      "titulo": "Screening and hospitalization of breast and cervical cancer in Brazil from 2010 to 2022: A time-series study",
      "veiculo": "PLOS ONE, 18(10):e0278011",
      "localizador": "10.1371/journal.pone.0278011 — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0278011",
      "achado": "Série temporal 2010-2022 por regressão Joinpoint, unidade nacional e por macrorregião, analisando EM PARALELO citopatológico (25-69 anos) e mamografia (50-69 anos), além de internações. Mamografia variou de 36 a 71 exames por 1.000 mulheres, com pico em 2019; citopatológico variou de 126 a 226 por 1.000. Ambos com maior oferta até 2019 e queda no período pandêmico. Internações com pico em 2019 (colo do útero 48/100 mil; mama 147/100 mil) e declínio 2020-2022 em todas as regiões. IMPORTANTE: analisa as duas séries em paralelo, mas NÃO usa uma como controle da outra.",
      "uso_no_projeto": "introdução e discussão — magnitude nacional das razões de exames; evidencia que o paralelismo mama/colo é descritivo na literatura, não explorado como ITS controlado",
      "confianca": "verificada-texto-completo"
    },
    {
      "autores": "Pinto R, Valentim R, Fernandes da Silva L, Fontoura de Souza G, Góis Farias de Moura Santos Lima T, Pereira de Oliveira CA, Marques dos Santos M, Espinosa Miranda A, Cunha-Oliveira A, Kumar V, Atun R",
      "ano": "2022",
      "titulo": "Use of Interrupted Time Series Analysis in Understanding the Course of the Congenital Syphilis Epidemic in Brazil",
      "veiculo": "The Lancet Regional Health – Americas, 7:100163",
      "localizador": "10.1016/j.lana.2021.100163 — https://www.sciencedirect.com/science/article/pii/S2667193X21001599",
      "achado": "Aplicação de ITS a dados de vigilância brasileiros para compreender a trajetória da epidemia de sífilis congênita, publicada em periódico internacional de alto impacto regional. Demonstra a aceitação do desenho ITS com dados de sistemas de informação do SUS em veículo internacional.",
      "uso_no_projeto": "métodos e justificativa — precedente de ITS com dados de sistema de informação brasileiro em periódico internacional",
      "confianca": "verificada-metadados"
    },
    {
      "autores": "Costa-Ribeiro MCV, Krainski ET, Mello AM, Carvalho DS, Luhm KR, Diaz-Quijano FA, Raboni SM, Silva LR, Buffon MCM, Maluf EMCP, Graef G, Almeida GA, Preto C, Shimakura SE",
      "ano": "2026",
      "titulo": "Dengue Incidence Following Mass Vaccination: An Interrupted Time Series Study in Paraná, Brazil",
      "veiculo": "Tropical Medicine and Infectious Disease, 11(1):11 (publicado online 30/12/2025)",
      "localizador": "10.3390/tropicalmed11010011 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12846613/",
      "achado": "ITS ecológico de 15 anos em PAINEL DE MUNICÍPIOS: 30 municípios vacinados mais 10 grupos de municípios-controle não vacinados, em 3 faixas de idade, gerando 120 séries semanais. Modelo Poisson com OFFSET de casos esperados (y_ikt ~ Poisson(E_ikt × λ_ikt)), com variação temporal específica por local (efeitos por município) em lugar de estrutura sazonal paramétrica; ajuste por sorotipo, faixa de idade e cobertura vacinal variante no tempo; covariável climática (proporção de tempo com temperatura mínima horária >21°C nas 9-12 semanas anteriores). Estimado via INLA (R-INLA v22.04.16) com estratégia CCD. Redução relativa de 8,2% na incidência para a cobertura de 3 doses efetivamente alcançada; 17% para cobertura hipotética de 90% e 18,7% para 100%.",
      "uso_no_projeto": "métodos — precedente brasileiro mais próximo do desenho proposto: ITS em painel municipal, contagem com offset, efeitos por município, controle por localidade e via INLA; referência para o caminho espacial",
      "confianca": "verificada-texto-completo"
    },
    {
      "autores": "Riebler A, Sørbye SH, Simpson D, Rue H",
      "ano": "2016",
      "titulo": "An intuitive Bayesian spatial model for disease mapping that accounts for scaling",
      "veiculo": "Statistical Methods in Medical Research, 25(4):1145-1165",
      "localizador": "10.1177/0962280216660421 — https://journals.sagepub.com/doi/10.1177/0962280216660421 (preprint arXiv:1601.01180)",
      "achado": "Apresenta a reparametrização BYM2 do modelo Besag-York-Mollié. No BYM clássico, a componente espacialmente estruturada (ICAR) não pode ser vista independentemente da componente não estruturada, o que torna a definição de prioris para os hiperparâmetros dos dois efeitos aleatórios problemática. O BYM2 escala a componente espacial e reduz o modelo a UM parâmetro de precisão e UM parâmetro de mistura, permitindo prioris penalizadoras de complexidade (PC) interpretáveis e controle independente dos hiperparâmetros. Implementado em R-INLA.",
      "uso_no_projeto": "métodos — âncora para a extensão espacial (CAR/BYM2) caso o I de Moran nos resíduos indique autocorrelação espacial residual",
      "confianca": "verificada-metadados"
    },
    {
      "autores": "von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP (STROBE Initiative)",
      "ano": "2007",
      "titulo": "The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies",
      "veiculo": "PLOS Medicine, 4(10):e296 (publicado também em BMJ, The Lancet e Epidemiology em out/nov 2007); documento companheiro de explicação e elaboração em PLOS Medicine 4(10):e297",
      "localizador": "10.1371/journal.pmed.0040296 — https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0040296",
      "achado": "Recomendações para reporte completo e acurado de estudos observacionais, cobrindo os delineamentos de coorte, caso-controle e transversal. Documento base ao qual as extensões (incluindo RECORD) se ancoram.",
      "uso_no_projeto": "métodos (plano de reporte) — diretriz base a ser declarada na dissertação e no artigo",
      "confianca": "verificada-metadados"
    },
    {
      "autores": "Benchimol EI, Smeeth L, Guttmann A, Harron K, Moher D, Petersen I, Sørensen HT, von Elm E, Langan SM (RECORD Working Committee)",
      "ano": "2015",
      "titulo": "The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) Statement",
      "veiculo": "PLOS Medicine, 12(10):e1001885",
      "localizador": "10.1371/journal.pmed.1001885 — https://pmc.ncbi.nlm.nih.gov/articles/PMC4595218/",
      "achado": "Extensão do STROBE para estudos observacionais com dados de saúde coletados rotineiramente, motivada por itens não cobertos pelo STROBE. Checklist de 13 itens relativos a título, resumo, introdução, métodos, resultados e discussão, além de informações complementares exigidas nesses relatos. O documento de métodos de consenso foi publicado separadamente (PubMed 25965407). NÃO foi localizada atualização posterior do RECORD original; existe extensão irmã para farmacoepidemiologia (RECORD-PE, Langan et al. 2018), não aplicável a este projeto.",
      "uso_no_projeto": "métodos (plano de reporte) — diretriz específica para dados de sistemas de informação (SISCAN, SIA/SUS, SISAB, SIAPS)",
      "confianca": "verificada-resumo"
    },
    {
      "autores": "McKenzie JE et al. (core group, School of Public Health and Preventive Medicine, Monash University; financiamento NHMRC Austrália)",
      "ano": "2023",
      "titulo": "CARITS – Complete and Accurate Reporting of Interrupted Time Series studies (diretriz de reporte em desenvolvimento, registrada na EQUATOR Network)",
      "veiculo": "EQUATOR Network — Reporting guidelines under development for observational studies. Registro em 09/05/2023",
      "localizador": "https://www.equator-network.org/library/reporting-guidelines-under-development/reporting-guidelines-under-development-for-observational-studies/",
      "achado": "ACHADO CENTRAL PARA O EIXO: NÃO existe, até a verificação, diretriz de reporte específica para ITS publicada. A CARITS está registrada como em desenvolvimento na EQUATOR desde 09/05/2023, sob liderança de Joanne McKenzie (Monash University), com previsão de publicação como documento de explicação e elaboração de acesso aberto em torno de 2025-2026. Escopo declarado: delineamentos de ITS que avaliam efeitos de intervenções em populações ou impactos de exposições (ex.: desastres naturais), com ênfase no reporte completo de detalhes de delineamento, métodos estatísticos e medidas de efeito.",
      "uso_no_projeto": "métodos (plano de reporte) — declarar STROBE+RECORD como diretrizes aplicáveis e registrar que a CARITS deve ser consultada na redação final (2026-2027), quando provavelmente já estará publicada",
      "confianca": "verificada-texto-completo"
    },
    {
      "autores": "Ministério da Saúde, Secretaria de Atenção Primária à Saúde (Brasil); material de divulgação do CONASEMS",
      "ano": "2025",
      "titulo": "Nota Metodológica C7 — Cuidado da mulher na prevenção do câncer (indicador do componente Qualidade do Saúde Brasil 360, Portaria GM/MS nº 3.493, de 10 de abril de 2024)",
      "veiculo": "gov.br/saude — Fichas técnicas de indicadores para equipe de Atenção Primária e Saúde da Família; e CONASEMS, Websérie dos Indicadores de Cofinanciamento Federal da APS (13º episódio)",
      "localizador": "https://www.gov.br/saude/pt-br/composicao/saps/publicacoes/fichas-tecnicas/equipe-de-atencao-primaria-e-saude-da-familia/nota-metodologica-c7-cuidado-da-mulher-na-prevencao-do-cancer — verificado em https://portal.conasems.org.br/noticias/1235_indicador-c7-de-cofinanciamento-da-aps-cuidado-da-mulher-na-prevencao-do-cancer",
      "achado": "ACHADO QUE ALTERA O DELINEAMENTO: o indicador C7 é COMPOSTO por quatro boas práticas ponderadas, e inclui SIMULTANEAMENTE (i) ao menos um exame de rastreamento de câncer do colo do útero em mulheres de 25 a 64 anos nos últimos 36 meses; (ii) ao menos uma dose de vacina HPV em meninas e adolescentes de 9 a 14 anos; (iii) atendimento com foco em saúde sexual e reprodutiva em adolescentes e mulheres de 14 a 69 anos nos últimos 12 meses; e (iv) AO MENOS UM EXAME DE RASTREAMENTO DE CÂNCER DE MAMA EM MULHERES DE 50 A 69 ANOS NOS ÚLTIMOS 24 MESES. O cálculo é a soma das ponderações das boas práticas realizadas para meninas e mulheres de 9 a 69 anos sobre o total de pessoas de cada público-alvo vinculado à equipe. Monitoramento mensal com avaliação quadrimestral; cerca de 54% das equipes em classificação suficiente. Registro via e-SUS APS / SIAPS, procedimentos referenciados na SIGTAP. A Portaria GM/MS nº 3.493/2024 vincula as transferências federais à organização do cuidado no território; a SAPS publicou em maio/2025 a lista de 15 indicadores do componente Qualidade.",
      "uso_no_projeto": "métodos (INVALIDA a mamografia como série-controle a partir de τ4, por co-incentivo direto — contaminação no sentido de Lopez Bernal 2018) e componente documental (matriz de incomparabilidade indicador nº 4 SISAB vs C7 SIAPS: o C7 é composto e ponderado, o indicador nº 4 era simples)",
      "confianca": "verificada-texto-completo"
    }
  ],
  "lacunas": [
    "NENHUM estudo localizado aplica ITS em painel de municípios com GLMM de contagem e offset para avaliar o Previne Brasil sobre cobertura de citopatológico. A única avaliação encontrada do Previne Brasil em painel municipal (Arato et al., 2025, Rev Saúde Pública 59:e28) usa regressão logística sobre variação dicotomizada antes-depois em 5.570 municípios, sem estrutura de série temporal, sem contagem, sem offset e sem ponto de mudança formal. Esta é a lacuna central que justifica o delineamento proposto.",
    "NENHUMA avaliação publicada do Saúde Brasil 360 ou da Portaria GM/MS nº 3.493/2024 foi localizada — nem sobre financiamento, nem sobre o indicador C7, nem sobre qualquer desfecho de rastreamento. A literatura disponível é exclusivamente normativa (portarias, notas técnicas SAPS/CONASS/CONASEMS, material de capacitação). Isso é esperado pela recência, mas precisa ser afirmado explicitamente como ineditismo.",
    "NENHUM estudo localizado analisa a (in)comparabilidade entre o indicador nº 4 do Previne Brasil (SISAB) e o indicador C7 do Saúde Brasil 360 (SIAPS). A confirmação de que o C7 é um indicador COMPOSTO e PONDERADO de quatro boas práticas — contra um indicador nº 4 simples — reforça que a descontinuidade de série é estrutural e não apenas de sistema de informação. O componente documental do projeto não tem antecedente na literatura.",
    "NENHUM precedente localizado usa formalmente a mamografia de rastreamento como série-controle não equivalente para o citopatológico em ITS controlado. Ferreira et al. (2023) e Duarte et al. (2022) analisam as duas séries EM PARALELO, mas nenhum dos dois estabelece uma como contrafactual da outra. Adicionalmente — e este é o achado mais importante do eixo — a nota metodológica do C7 mostra que o indicador agrega explicitamente o rastreamento mamário (50-69 anos, 24 meses) junto ao citopatológico (25-64 anos, 36 meses). A mamografia é portanto CO-INCENTIVADA a partir de τ4 (mai/2025), configurando contaminação no sentido exato de Lopez Bernal et al. (2018). RECOMENDAÇÃO: (a) manter a mamografia como controle apenas para τ1-τ3, verificando documentalmente que o indicador nº 4 do Previne Brasil não contemplava mamografia; (b) para τ3-τ4, adotar controle por característica — citopatológicos em mulheres FORA da faixa 25-64 anos (por exemplo <25 e >64 anos), que compartilham o mesmo choque pandêmico e a mesma via de oferta mas não integram o numerador de nenhum indicador de financiamento; (c) reportar ITS simples e ITS controlado simultaneamente, como recomendam Lopez Bernal et al. (2018).",
    "NENHUMA aplicação publicada em saúde pública brasileira foi localizada usando glmmTMB com binomial negativo E estrutura AR1 em painel municipal de contagens. O precedente mais próximo (Costa-Ribeiro et al., 2026, painel de municípios do Paraná) usa Poisson com offset de casos esperados via INLA, não glmmTMB, e trata a dependência temporal por efeitos temporais específicos de local em vez de AR1 explícito. A escolha por glmmTMB precisará ser justificada pela flexibilidade (Brooks et al., 2017) e não por precedente aplicado nacional.",
    "NÃO há literatura de poder estatístico para ITS com MÚLTIPLOS pontos de mudança em painel de contagens. Liu et al. (2019) é o arcabouço disponível, mas trata de UMA série, UMA interrupção e modelos log-lineares observation-driven (pacote tscount), não de GLMM em painel com quatro τ. Além disso, o simr (Green & MacLeod, 2016) é construído sobre lme4/glmer e NÃO suporta glmmTMB nem estruturas AR1 — não foi localizada nenhuma orientação publicada para poder por simulação em GLMM binomial negativo com AR1 em painel. Solução a documentar no protocolo: simular diretamente do objeto glmmTMB ajustado (método simulate()) replicando a lógica de três passos do simr, com curvas de poder por magnitude de efeito e por número de municípios.",
    "NÃO existe diretriz de reporte específica para ITS publicada. Hudson et al. (2019) recomendava explicitamente desenvolvê-la; a CARITS (Complete and Accurate Reporting of Interrupted Time Series studies) está registrada na EQUATOR desde 09/05/2023 sob liderança de Joanne McKenzie (Monash), com previsão de publicação em 2025-2026. Como a coleta do projeto é em 2027, a CARITS provavelmente estará publicada na redação final e DEVE ser reconsultada. Até então: STROBE + RECORD (13 itens) como diretrizes declaradas, complementadas pelas recomendações de Turner et al. (2021) para as figuras e por Turner et al. (2021, seis métodos) para pré-especificação e sensibilidade.",
    "NENHUM estudo brasileiro localizado modela CONJUNTAMENTE múltiplos pontos de mudança E dependência espacial em painel municipal de contagens. Costa-Ribeiro et al. (2026) usa INLA em painel municipal mas com uma única interrupção e sem componente CAR/BYM2 explícito; os estudos de mapeamento espacial de CCU no Brasil (mortalidade, 2000-2021) usam BYM sem estrutura de ITS. Não foi localizada nenhuma referência aplicada em saúde no Brasil que combine I de Moran em resíduos de GLMM de painel como critério de escalonamento para BYM2 — o protocolo de diagnóstico escalonado proposto será uma escolha do projeto, ancorada teoricamente em Riebler et al. (2016), não copiada de um precedente.",
    "NÃO foi localizado tutorial ou revisão metodológica dedicada especificamente a ITS com MÚLTIPLOS pontos de mudança e EVENTOS CONCORRENTES próximos no tempo — o caso crítico do projeto, com τ1 (jan/2020) e τ2 (mar/2020) separados por dois meses. A literatura disponível trata o problema de forma dispersa: Lopez Bernal et al. (2018) via classes de controle, Turner et al. (2021) via pré-especificação e sensibilidade, Nascimento et al. (2020) via exclusão de período de transição. Não há orientação canônica sobre identificabilidade quando duas interrupções são quase simultâneas. IMPLICAÇÃO PRÁTICA: os efeitos de τ1 e τ2 são provavelmente NÃO SEPARÁVEIS empiricamente e isso deve ser declarado a priori no protocolo — a estratégia defensável é modelar τ1-τ2 como um bloco único e, em análise de sensibilidade, deslocar τ1 para jan/2019 (publicação da Portaria GM/MS 2.979/2019 e período de adaptação) para testar a robustez.",
    "Há um preprint relevante mas NÃO revisado por pares: Waken RJ, Wang F, Eisenstein SA, McBride T, Johnson K, Joynt-Maddox K. 'Multilevel non-linear interrupted time series analysis'. arXiv:2511.05725 (07/11/2025). Propõe combinar modelos aditivos generalizados para efeitos não lineares de interrupção com modelos bayesianos multinível de séries temporais, com partial pooling e pós-estratificação, demonstrado em três aplicações em saúde (diagnóstico de câncer de próstata por raça/idade, internações por AVC por ruralidade durante a COVID-19, expansão do Medicaid). É o trabalho metodológico mais próximo do desenho de painel proposto, mas NÃO deve ser citado como âncora de métodos enquanto for preprint. Reverificar publicação em periódico até 2027.",
    "NENHUM estudo de tendência temporal ou ITS sobre cobertura/razão de exames citopatológicos nos MUNICÍPIOS DE PERNAMBUCO foi localizado. A literatura brasileira sobre cobertura de citopatológico é nacional (Ferreira et al., 2023), por macrorregião, ou por estados agregados de Sul e Nordeste (Cad Saúde Pública), com estudos locais em PE restritos a análise laboratorial descritiva (por exemplo, LACIAN/Caruaru). Não há linha de base publicada específica para PE em nível municipal — o que reforça o ineditismo mas também significa que os números de incidência e cobertura para PE precisarão vir diretamente de INCA/SISCAN/TABNET, não de literatura secundária."
  ],
  "numeros_chave": [
    "Autocorrelação em ITS: estimativas divergem entre métodos (mediana 0,20 com REML vs 0,04-0,05 com ARIMA/Prais-Winsten) e só convergem em séries com ≥100 pontos temporais (Turner SL et al., BMC Med Res Methodol 2021;21:134, avaliação empírica de 190 séries publicadas). A janela do projeto tem 108 meses — exatamente no limiar, argumento direto para AR1 especificado a priori.",
    "Concordância entre métodos de ITS na significância dicotomizada a 5%: 79,3% a 97,1% conforme o par de métodos; erros-padrão do ARIMA sistematicamente maiores (limites de concordância de 61% menores a 460% maiores vs Newey-West) (Turner SL et al., BMC Med Res Methodol 2021;21:134).",
    "Reporte incompleto em ITS: em 116 estudos de saúde publicados em 2015, mudança de inclinação foi relatada em 84%, mudança de nível em 70% e mudança de nível de longo prazo em apenas 21% (Hudson J, Fielding S, Ramsay CR. BMC Med Res Methodol 2019;19:137).",
    "Poder estatístico em ITS de contagem: com 48 observações e efeito combinado β2+β3 = ±1,0 na escala log, poder ≈0,92 sob Poisson e ≈0,96 sob binomial negativo; sob binomial negativo o poder é NÃO-MONOTÔNICO na autocorrelação (Liu W et al., Contemp Clin Trials Commun 2019;17:100474).",
    "Impacto pandêmico em São Paulo: ~1.149.727 exames de Papanicolaou, 713.616 mamografias e 2.693 conizações perdidos ou atrasados; redução de 25% no início de terapia adjuvante em mama estádio I/II; excesso de 156 pacientes iniciando cuidado paliativo por CCU avançado (Duarte MBO, Argenton JLP, Carvalheira JBC. JCO Glob Oncol 2022;8:e2100371, ITS quasi-Poisson com harmônicos pareados, jan/2017-nov/2021).",
    "Razões nacionais de exames, Brasil 2010-2022: citopatológico de 126 a 226 exames por 1.000 mulheres; mamografia de 36 a 71 por 1.000 mulheres; ambos com pico em 2019 e queda no período pandêmico. Internações com pico em 2019: colo do útero 48/100 mil e mama 147/100 mil (Ferreira HNC et al., PLOS ONE 2023;18(10):e0278011, regressão Joinpoint).",
    "Mortalidade prematura por CCU (30-69 anos), Brasil 1998-2018: mais de 119.000 óbitos; coeficiente de tendência pós-Pacto pela Saúde no Brasil 0,513 (IC95% 0,430-0,596) indicando aumento progressivo; Nordeste foi a única macrorregião com redução imediata de nível (-0,635; IC95% -1,177 a -0,092); Norte com maiores taxas absolutas (>20/100 mil) (Nascimento MI et al., Rev Saúde Pública 2020;54:139).",
    "Precedente de painel municipal com binomial negativo: PMAQ-AB reduziu internações por condições sensíveis à atenção primária em 0,0356 por 10 mil habitantes de 0-64 anos por ponto percentual de participação (p=0,004), ~60.829 internações evitadas em 2018; em menores de 5 anos -0,0940 por 10 mil (p=0,012); teste de placebo com internações por acidente de transporte NÃO significativo (Russo LX et al., BMJ Glob Health 2021;6(7):e005429, painel de 5.564 municípios, 2009-2018).",
    "Precedente de painel municipal com efeitos fixos: Mais Médicos associou-se a +5,7 médicos de atenção primária por 100 mil habitantes (IC95% 5,1-6,4) e a redução de 1,06 óbitos evitáveis por 100 mil por ano (IC95% -1,78 a -0,34), cerca de 1,3%, em 5.565 municípios, 2008-2017 (Hone T et al., BMC Health Serv Res 2020;20(Suppl 2):873).",
    "Precedente de ITS em painel municipal com offset e INLA: 30 municípios vacinados + 10 grupos-controle × 3 faixas de idade = 120 séries semanais em 15 anos; redução relativa de 8,2% na incidência de dengue para a cobertura de 3 doses alcançada, 17% para cobertura hipotética de 90% e 18,7% para 100% (Costa-Ribeiro MCV et al., Trop Med Infect Dis 2026;11(1):11).",
    "Precedente de ITS em painel de 5.569 municípios publicado em Rev Saúde Pública: queda imediata média nacional de 6,70 per capita no gasto total em saúde após a política de austeridade de 2015, chegando a 10,39 nos municípios de pequeno porte (Maia LR, Campos MR, Castanheira D. Rev Saúde Pública 2024;58:42, ARIMA, dados semestrais 2010-2019).",
    "Previne Brasil em 5.570 municípios (2016-2018 vs 2019-2022): pré-natal aumentou em 86,7% dos municípios, mortalidade materna caiu em apenas 30,9% e infantil em 42,6%; sem associação entre aumento do pré-natal e redução da mortalidade materna (OR=0,92; IC95% 0,78-1,09) ou infantil (OR=1,14; IC95% 0,97-1,34) (Arato CVDB et al., Rev Saúde Pública 2025;59:e28 — desenho antes-depois, NÃO ITS).",
    "Composição do indicador C7 (Saúde Brasil 360): quatro boas práticas ponderadas — citopatológico em mulheres de 25 a 64 anos nos últimos 36 meses; ≥1 dose de vacina HPV em meninas de 9 a 14 anos; atendimento em saúde sexual e reprodutiva em mulheres de 14 a 69 anos nos últimos 12 meses; e rastreamento de câncer de mama em mulheres de 50 a 69 anos nos últimos 24 meses. Denominador: público-alvo de 9 a 69 anos vinculado à equipe. Monitoramento mensal, avaliação quadrimestral; ~54% das equipes em classificação suficiente (Nota Metodológica C7, SAPS/MS; CONASEMS).",
    "Diretriz RECORD: checklist de 13 itens como extensão do STROBE para estudos com dados de saúde coletados rotineiramente (Benchimol EI et al., PLOS Med 2015;12(10):e1001885).",
    "Diretriz de reporte específica para ITS: NÃO publicada. CARITS registrada na EQUATOR Network em 09/05/2023 (Joanne McKenzie, Monash University, financiamento NHMRC), com publicação prevista para 2025-2026 — reconsultar na redação final."
  ]
}