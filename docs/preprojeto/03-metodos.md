# 3. MÉTODOS

## 3.1 Delineamento

Trata-se de estudo ecológico de séries temporais interrompidas (ITS) em painel de municípios, com componente de análise documental comparativa. O desfecho é a contagem mensal de exames citopatológicos do colo do útero realizados em mulheres de 25 a 64 anos, por município de residência, e as interrupções são datas de vigência de atos normativos federais de cofinanciamento da atenção primária, declaradas a priori.

A escolha do delineamento decorre da natureza da exposição. Mudanças de regra de financiamento federal da atenção primária incidem simultaneamente sobre todos os municípios brasileiros; não existe, portanto, conjunto de unidades não expostas que possa servir de contrafactual em um desenho de alocação. Nessa condição — intervenção populacional, implantação universal, desfecho mensurado de forma rotineira e repetida antes e depois de datas conhecidas — a ITS é o delineamento quase-experimental mais robusto disponível, porque o próprio comportamento pré-intervenção da série fornece a projeção contra a qual o período pós-intervenção é comparado (WAGNER et al., 2002; LOPEZ BERNAL; CUMMINS; GASPARRINI, 2017). A especificação segue a versão corrigida do tutorial canônico (LOPEZ BERNAL; CUMMINS; GASPARRINI, 2021), cuja errata corrigiu uma definição algébrica do modelo segmentado que podia induzir interpretação errônea dos parâmetros.

Descartam-se explicitamente as alternativas próximas, pelas razões que Lopez Bernal et al. (2019) delimitam: diferenças-em-diferenças exige grupo não exposto e tendências paralelas, e controle sintético exige um doador de unidades não tratadas. Nenhuma das duas premissas se sustenta diante de uma alteração de regra de cofinanciamento federal que atinge todas as unidades de Pernambuco na mesma competência. A ITS dispensa unidade de comparação não exposta, admitindo, porém, séries-controle quando estas existam e sejam defensáveis (LOPEZ BERNAL et al., 2018) — questão tratada na seção 3.9.

### 3.1.1 Por que painel de municípios e não série estadual agregada

A decisão de manter as 185 unidades como séries individuais, em vez de somá-las em uma única série estadual, é a decisão de desenho com maior consequência sobre a precisão das estimativas, e precisa ser justificada em três planos.

**Plano da informação disponível.** A agregação estadual reduz o conjunto de dados a, no máximo, 108 observações — uma por competência da janela. Com quatro blocos de interrupção, cada um consumindo dois parâmetros (nível e tendência), somados a intercepto, tendência basal, quatro parâmetros de sazonalidade e um parâmetro de dispersão, o modelo agregado consumiria em torno de quinze graus de liberdade sobre cem observações efetivas, com segmentos curtos entre interrupções. O painel preserva, para a mesma estrutura de efeitos fixos, o produto 185 × 100 competências efetivamente publicadas, isto é, cerca de 18,5 mil observações município-mês. O poder para detectar mudanças de nível e de tendência vem dessa replicação entre unidades, não do comprimento da série.

**Plano estatístico.** Ewusie et al. (2020) demonstram, em ITS multicêntrico, que a regressão segmentada convencional aplicada a dados previamente agregados entre participantes e sítios não é ótima, e que incorporar explicitamente a variabilidade intra e entre unidades produz estimativas mais precisas e maior poder. Agregar 185 municípios em uma soma estadual descarta a variância entre unidades, que é informação, e faz o resultado ser dominado pelos municípios de maior volume — em Pernambuco, sobretudo Recife e as sedes de região de saúde que concentram laboratórios de citopatologia. O painel com efeitos aleatórios de intercepto e de inclinação por município recupera essa informação e, adicionalmente, permite estimar a heterogeneidade da resposta, que é objeto substantivo e não apenas ruído.

**Plano substantivo.** A hipótese de penalização diferencial de municípios com menor capacidade administrativa só é testável em painel, por termos de interação entre os indicadores de interrupção e características municipais. Em série agregada, essa pergunta é inexprimível. Precedentes brasileiros publicados sustentam a viabilidade da opção: Maia, Campos e Castanheira (2024) publicaram ITS em painel de 5.569 municípios em periódico nacional de primeira linha; Rasella et al. (2013), Hone et al. (2020) e Russo et al. (2021) empregaram painéis municipais com modelos de contagem para avaliar políticas federais; e Costa-Ribeiro et al. (2026) executaram ITS ecológico em painel municipal brasileiro com desfecho de contagem e offset, que é a combinação exata aqui proposta.

O custo da opção é declarado: o painel exige tratamento explícito da dependência serial dentro de cada município e da eventual dependência espacial entre municípios contíguos, ambos endereçados nas seções 3.8.3 e 3.8.4.

## 3.2 Área de estudo

O estudo abrange o estado de Pernambuco, região Nordeste do Brasil. O frame territorial adotado é o conjunto das 185 unidades municipais reconhecidas pelo Instituto Brasileiro de Geografia e Estatística para a Unidade da Federação de código 26, correspondentes aos 184 municípios e ao Distrito Estadual de Fernando de Noronha, unidade territorial sem estatuto municipal mas dotada de código de município no cadastro do IBGE e de registro autônomo nos sistemas de informação do SUS. Registra-se que parte da literatura estadual refere 184 unidades, por excluir Fernando de Noronha; a inclusão é adotada aqui por coerência com o frame canônico da fonte territorial e porque nenhum estudo localizado sobre indicadores de atenção primária inclui o Distrito Estadual, o que faz dessa inclusão um ganho marginal de completude.

A rede de atenção do estado está organizada em 12 regiões de saúde agrupadas em 4 macrorregiões de saúde [VERIFICAR: Plano Diretor de Regionalização vigente da SES-PE — confirmar número de regiões e macrorregiões e o ato que as institui, dado não disponível no dossiê depurado]. Essa estratificação é utilizada exclusivamente como variável de agrupamento em análises descritivas e de heterogeneidade, e não como nível hierárquico adicional do modelo principal, a fim de não multiplicar componentes de variância em um desenho que já é computacionalmente exigente.

A pertinência do recorte é epidemiológica e organizacional. Pernambuco tem 850 casos novos de câncer do colo do útero estimados por ano para o triênio 2026-2028, com taxa bruta de 16,99 e ajustada de 11,96 por 100 mil mulheres (INCA, 2026), e registrou 402 óbitos em 2022, com taxa ajustada de 6,23 por 100 mil, acima da média nordestina (INCA, 2025). A cobertura de rastreamento medida por mulher rastreada foi de 32,5% no triênio 2021-2023, contra 35,6% no Brasil (RIBEIRO et al., 2025). O estado responde por cerca de 20% dos exames citopatológicos do Nordeste (SILVA et al., 2023) e apresenta heterogeneidade interna documentada em qualidade laboratorial — 27% dos municípios com insatisfatoriedade acima de 5% em 2023, o maior percentual do país (INCA, 2025) — e em organização da oferta, com programa estadual de rastreamento organizado em cooperação com a Organização Pan-Americana da Saúde operando em Recife e em oito municípios desde dezembro de 2021 (OPAS; SES-PE, 2021). Essa heterogeneidade é condição de possibilidade do painel: é ela que fornece a variação entre unidades da qual o modelo extrai precisão.

## 3.3 População e unidade de análise

**Unidade de análise:** o município de residência, observado mensalmente. A unidade estatística elementar do painel é a célula município × competência mensal; em especificações estratificadas, município × faixa etária quinquenal × competência.

**População de referência:** mulheres residentes em Pernambuco com idade entre 25 e 64 anos, faixa etária-alvo do rastreamento citopatológico segundo as diretrizes nacionais vigentes durante a quase totalidade da janela (INCA, 2016) e faixa que define o Indicador 5 do Caderno de Diretrizes, Objetivos, Metas e Indicadores 2016, pactuado pela Resolução CIT nº 2, de 16 de agosto de 2016 (BRASIL, 2016). A faixa etária não é convenção analítica da pesquisadora: é a recomendação clínica e a definição normativa do indicador.

**Critérios de inclusão:** todos os registros de exame citopatológico do colo do útero no Sistema de Informação do Câncer (SISCAN) cujo município de residência da usuária pertença ao frame de 185 unidades de Pernambuco, cuja idade se situe entre 25 e 64 anos completos e cuja competência esteja compreendida na janela do estudo.

**Critérios de exclusão:** registros com município de residência ignorado ou não identificado, que serão contabilizados e reportados como perda, mas não redistribuídos; e registros de residentes em outras unidades da Federação atendidos em Pernambuco, excluídos por construção pelo uso do recorte por residência.

Não há amostragem: trata-se de censo dos registros disponíveis nas bases secundárias, o que dispensa cálculo de tamanho amostral no sentido clássico e desloca a questão do poder para a magnitude de efeito detectável, tratada na seção 3.10.

## 3.4 Período e marcos temporais

A janela do estudo é de janeiro de 2018 a dezembro de 2026, 108 competências mensais, com coleta definitiva prevista para 2027, quando a competência de dezembro de 2026 estiver consolidada. A extração-piloto executada em 1º de agosto de 2026 recuperou 100 das 108 competências, encerrando-se em junho de 2026. O período pré-primeira-interrupção compreende 24 competências (janeiro de 2018 a dezembro de 2019), extensão suficiente para caracterizar nível, tendência e ao menos dois ciclos sazonais completos antes da primeira ruptura.

Os pontos de mudança são definidos normativamente, por data de vigência ou de produção de efeitos financeiros de atos oficiais, e declarados a priori no protocolo. Nenhum ponto de mudança é obtido por busca de quebras nos dados. Essa exigência decorre de dois fatos: cada interrupção adicional consome graus de liberdade e encurta os segmentos disponíveis para caracterizar cada regime; e a comparação empírica de seis métodos estatísticos em 190 séries publicadas recomenda a pré-especificação do método no protocolo, acompanhada de análises de sensibilidade (TURNER; KARAHALIOS; FORBES et al., 2021b).

### 3.4.1 Os marcos

**Tabela 1 — Pontos de mudança, mecanismo e tratamento no modelo**

| τ | Evento e ato normativo | Competência | Mecanismo | Tratamento no modelo |
|---|---|---|---|---|
| τ1 | Previne Brasil — Portaria GM/MS nº 2.979, de 12/11/2019 | jan/2020 | Substituição do PAB fixo e variável por capitação ponderada, pagamento por desempenho e incentivo para ações estratégicas. O rastreamento do colo do útero constitui o indicador nº 4, com meta de 40%, parâmetro de referência de 80%, peso 1, janela de 36 meses, apuração quadrimestral em SISAB e granularidade municipal (BRASIL, 2022a) | Modelado em **bloco único com τ2** (ver 3.4.2) |
| τ2 | Emergência de Saúde Pública de Importância Nacional, COVID-19 | mar/2020 | Interrupção abrupta da oferta eletiva e da demanda por procedimentos de rastreamento. Choque exógeno, não intervenção de interesse | Modelado em **bloco único com τ1** |
| τ3 | Componente financeiro do modelo Saúde Brasil 360 — Portaria GM/MS nº 3.493, de 10/04/2024, art. 8º | mai/2024 | Reestruturação do repasse federal em seis componentes e revogação do Previne Brasil (art. 7º, IV). Efeitos financeiros "a partir da parcela maio de 2024", confirmados no material oficial da SAPS (BRASIL, 2024a; BRASIL, 2024b). O art. 3º da redação original garante, por doze meses, o valor da classificação "bom" nos componentes de vínculo e qualidade. **É marco de reestruturação do fluxo financeiro, não de exposição a risco de perda por desempenho em rastreamento** | Ponto de mudança próprio |
| τ4 | Incorporação dos indicadores de qualidade, inclusive o C7 — Portaria GM/MS nº 6.907, de 29/04/2025, art. 3º, §1º | mai/2025 | Início da apuração dos sete indicadores de qualidade das eSF e eAP a partir do 2º quadrimestre de 2025. **Marco de mensuração do C7, não de exposição financeira a ele.** Em maio de 2025 quem passa a ser remunerado por classificação de desempenho é o componente de **vínculo e acompanhamento territorial**, não o de qualidade (BRASIL, 2024b; BRASIL, 2025a) | Ponto de mudança próprio, com hipótese de efeito de mensuração |
| τ5 | Implantação parcial e assimétrica da qualidade — Portaria GM/MS nº 10.994, de 13/05/2026 | mai/2026 | A classificação "bom" é mantida na qualidade até o 1º quadrimestre de 2026; a partir do 2º quadrimestre de 2026, apenas equipes classificadas como "ótimo" recebem o valor correspondente, enquanto "bom", "suficiente" e "regular" recebem indistintamente o valor de "bom" (BRASIL, 2026b) | Ponto de mudança próprio, com interpretação restrita a **ganho potencial**, sem risco de perda |

### 3.4.2 A não separabilidade de τ1 e τ2 e a estratégia de bloco único

τ1 e τ2 estão separados por dois meses. Com dados mensais, o segmento entre as duas interrupções contém duas observações. Nessas condições, as colunas da matriz de delineamento correspondentes às duas interrupções são quase colineares, e os coeficientes de nível e de tendência atribuíveis a cada uma delas são, com alta probabilidade, não separáveis empiricamente: qualquer partição do efeito entre τ1 e τ2 seria determinada pela especificação, não pelos dados.

Não foi localizado tutorial, revisão ou recomendação metodológica dedicada a esse caso. A literatura trata o problema de forma dispersa e indireta — por classes de controle (LOPEZ BERNAL et al., 2018), por pré-especificação e análise de sensibilidade (TURNER; KARAHALIOS; FORBES et al., 2021b) e por exclusão de período de transição (NASCIMENTO et al., 2020) — mas não oferece orientação canônica sobre identificabilidade quando duas interrupções são quase simultâneas.

A estratégia adotada, declarada a priori no protocolo, é modelar τ1 e τ2 como **bloco único de interrupção**, com um único par de parâmetros de nível e de tendência, renunciando explicitamente à pretensão de atribuir efeito próprio a cada um. O bloco é interpretado como a transição conjunta entre o regime de financiamento anterior e o período pandêmico, e **não** como o efeito isolado do Previne Brasil. Essa renúncia é substantiva e será reafirmada na discussão: o estudo não estima o efeito do Previne Brasil sobre a produção de exames de forma separada do efeito da pandemia, e nenhuma leitura dos resultados pode fazê-lo.

Três providências acompanham essa decisão. Primeira, análise de sensibilidade deslocando τ1 para janeiro de 2019, data associada ao período de publicação e de adaptação municipal que antecede a vigência, o que amplia o segmento intermediário e permite avaliar se as conclusões sobre τ3, τ4 e τ5 são robustas à escolha do ponto inicial. Segunda, análise de sensibilidade com exclusão de período de transição pandêmico, à maneira de Nascimento et al. (2020), removendo da estimação as competências de março a agosto de 2020 — intervalo que compreende o nadir documentado e o início da retomada (RIBEIRO; CORRÊA; MIGOWSKI, 2022). Terceira, reporte lado a lado de todas as especificações, com a divergência entre elas apresentada como incerteza do desenho e não resolvida por seleção post hoc.

A magnitude do choque pandêmico na própria série do estudo justifica esse cuidado. A extração-piloto registra 23.593 exames em janeiro de 2020, 7.951 em abril, 2.279 em maio e 1.576 em junho de 2020 — nadir correspondente a redução de aproximadamente 93% frente a janeiro do mesmo ano —, com recuperação a 25.848 em novembro de 2020. Um choque dessa amplitude domina qualquer variação atribuível a um incentivo financeiro instituído dois meses antes.

### 3.4.3 Rupturas de mensuração adicionais

Além dos cinco pontos de mudança de política, a janela contém rupturas na definição operacional dos instrumentos oficiais de aferição. Elas **não** são modeladas como interrupções da série do desfecho, porque o desfecho provém do SISCAN e não do sistema que alimenta a aferição do indicador de pagamento; integram, porém, o componente documental (seção 3.11) e a discussão das limitações. São três, no mínimo:

1. **jan/2022 — Portaria GM/MS nº 102/2022**, que alterou simultaneamente denominação, numerador (passando a exigir coleta realizada na atenção primária) e denominador (de mulheres cadastradas para cadastradas e vinculadas) do indicador nº 4, **dentro da vigência do Previne Brasil** (BRASIL, 2022a).
2. **mai/2024 a mai/2025 — transição do indicador nº 4 para a boa prática (A) do indicador C7**, com mudança simultânea de sete dimensões: numerador, códigos SIGTAP aceitos, denominador, fonte, granularidade, métrica e público-alvo (BRASIL, 2022a; BRASIL, 2026a).
3. **jan/2026 — incorporação do procedimento SIGTAP 02.02.10.025-1** (exame molecular de detecção de HPV) à boa prática (A) do C7, com janela de acumulação de 60 meses, distinta dos 36 meses aplicáveis aos demais procedimentos (BRASIL, 2026a).

Registra-se ainda, como pendência de fonte primária, a redefinição atribuída a julho de 2022 da regra de cálculo do denominador dos indicadores do Previne Brasil, pela qual o limiar de 85% teria passado a incidir sobre a população-alvo identificada de cada indicador. Essa ruptura só foi localizada em fonte secundária e **não será usada como referência normativa** enquanto não recuperada em fonte oficial, por Wayback Machine, comparação das versões da nota técnica no repositório do Ministério da Saúde ou solicitação via Lei de Acesso à Informação. A comparação das duas versões da nota é evidência primária mais forte que o comunicado.

## 3.5 Fontes de dados e variáveis

### 3.5.1 Desfecho: SISCAN

A fonte do desfecho é o Sistema de Informação do Câncer (SISCAN), acessado por meio do TABNET/DATASUS, definição `SISCAN/cito_colo_residpe.def`. A escolha decorre de três argumentos, dos quais o terceiro é empírico e específico deste projeto.

**Argumento de independência.** O SISCAN não alimenta a aferição do indicador de pagamento por desempenho. O indicador nº 4 do Previne Brasil era apurado no SISAB; a boa prática (A) do C7 é apurada em SIAPS, SCNES e RNDS (BRASIL, 2022a; BRASIL, 2026a). Usar como desfecho a mesma base que aciona o pagamento faria com que qualquer efeito estimado fosse indistinguível de mudança de comportamento de registro — problema central da avaliação de incentivos (MINCHIN et al., 2018) e documentado no Brasil em magnitude comparável ao próprio fenômeno medido: 108.511 exames realizados e pagos pelo SUS ausentes do SISAB no biênio 2021-2022 em uma única área programática do município do Rio de Janeiro (CASTRO-NUNES et al., 2024). O uso do SISCAN contorna estruturalmente essa contaminação e é argumentado como força de desenho, não como conveniência.

**Argumento de estabilidade da definição operacional.** O registro do exame citopatológico no SISCAN mantém, ao longo da janela, numerador de exames com laudo, faixa etária derivada da data de nascimento da usuária e município de residência declarado, sem as mudanças de numerador, denominador, fonte e granularidade que atingiram o indicador oficial ao menos três vezes no período (seção 3.4.3).

**Argumento empírico: por que o SIA/SUS foi descartado.** A alternativa natural seria o Sistema de Informações Ambulatoriais (SIA/SUS), fonte declarada do Indicador 5 do Caderno 2016 (BRASIL, 2016) pelos procedimentos 02.03.01.001-9 e 02.03.01.008-6. Testes de validação executados em 1º de agosto de 2026 contra o TABNET estadual de Pernambuco, por requisição POST direta ao procedimento 0203010019 (exame citopatológico cérvico-vaginal), incremento de quantidade apresentada, com estratificação por município de residência e por idade simples, produziram a seguinte distribuição etária da produção de 2025:

**Tabela 2 — Distribuição etária da produção de exame citopatológico no SIA/SUS, Pernambuco, 2025**

| Faixa etária | Exames | % |
|---|---|---|
| 10 a 14 anos | 428 | 0,7 |
| 15 a 19 anos | 10.405 | 18,0 |
| 20 a 24 anos | 24.615 | **42,6** |
| 25 a 64 anos (faixa-alvo do rastreamento) | 5.171 | **9,0** |
| 65 a 69 anos | 10.916 | **18,9** |
| 70 a 74 anos | 4.242 | 7,3 |
| 75 anos ou mais | 1.967 | 3,4 |

Essa distribuição é biologicamente implausível para um programa de rastreamento. O rastreamento de câncer do colo do útero no Brasil é indicado dos 25 aos 64 anos, e o rastreamento antes dos 25 anos é explicitamente desaconselhado (INCA, 2016). A literatura registra que de 20% a 25% dos exames são realizados fora do grupo etário recomendado (INCA, 2016) e que, em Pernambuco, a proporção de exames na faixa-alvo passou de 78,80% em 2018 para 81,43% em 2022 (INCA, 2023). Uma distribuição em que 42,6% da produção recai na faixa de 20 a 24 anos, 18,9% na faixa de 65 a 69 e apenas 9,0% na faixa-alvo inteira não descreve um programa oportunístico com má aderência às diretrizes — está a mais de setenta pontos percentuais do padrão documentado pela fonte oficial para o mesmo estado. O padrão bimodal, com picos simétricos imediatamente antes e imediatamente depois dos limites da faixa-alvo, é assinatura de erro sistemático de preenchimento ou de conversão do campo de idade, não de comportamento clínico. Verificou-se ainda que toda a produção de 2025 está registrada como Boletim de Produção Ambulatorial Individualizado, de modo que a ausência de identificação do paciente não explica o problema: o campo existe, está preenchido e está preenchido errado.

A consequência metodológica é terminante. Como a estratificação etária é constitutiva do desfecho, filtrar a faixa de 25 a 64 anos no SIA descartaria 91% da produção sem que se saiba o que está sendo descartado. O SIA/SUS **não serve como fonte do desfecho primário** deste estudo. Permanece útil, e será usado, para dois fins auxiliares: validação cruzada do volume total por município, sem estratificação etária; e construção da covariável de substituição tecnológica pelo teste molecular de DNA-HPV, descrita em 3.5.4.

O mesmo conjunto de testes documentou três decisões operacionais que passam a integrar o protocolo de extração. Primeira, a agregação deve usar o campo de município de residência da paciente, e não o de município do estabelecimento: por estabelecimento aparecem apenas as poucas dezenas de municípios que sediam laboratório de citopatologia, ao passo que por residência aparecem 179 das 185 unidades já em um trimestre isolado. Segunda, o código correto do exame laboratorial é 02.03.01.001-9, e não o de coleta de material na atenção primária, que corresponde ao ato de coleta e apresenta cerca de um quarto do volume. Terceira, o campo de idade do TABNET obedece à regra `valor = idade + 1`, calibrada empiricamente, e não `idade + 2` como registrado na documentação herdada.

### 3.5.2 Acesso programático ao SISCAN

A extração é integralmente programática, sem uso de navegador, por requisição HTTP POST ao CGI do TABNET/DATASUS, e é reprodutível a partir de um único script versionado. Os elementos do protocolo que precisam constar do reporte, por exigência do item de acesso a dados e códigos do RECORD (BENCHIMOL et al., 2015), são:

- **Definição:** `SISCAN/cito_colo_residpe.def`, para o desfecho e para a série-controle; `SISCAN/mamografia_residpe.def`, para a série descartada como controle e mantida apenas como descritivo.
- **Linha:** município de residência, por expressão que concatena código e nome do município a partir da tabela de disseminação, com junção pelo campo de município de residência do fato.
- **Coluna:** mês/ano de competência. Os dois arquivos de definição divergem no campo de competência — o citopatológico usa a data de liberação do laudo e a mamografia usa a competência de faturamento —, divergência que precisa ser declarada e que impede tratar as duas séries como comensuráveis competência a competência.
- **Estratificação etária:** faixas quinquenais, oito para a faixa-alvo (25-29 a 60-64) e seis para a série-controle (15-19, 20-24, 65-69, 70-74, 75-79 e 80 anos ou mais).
- **Codificação e parsing:** corpo da requisição codificado em latin-1, porque os nomes de campo do TABNET são acentuados; formato de resposta `prn`, que devolve texto separado por ponto e vírgula dentro de bloco `<pre>`.

Quatro armadilhas do TABNET foram identificadas e são tratadas por verificação obrigatória em cada extração:

1. **A última coluna da resposta é o total da linha**, e contá-la como dado duplica os valores.
2. **Entidades HTML colidem com o separador**: nomes de município acentuados são devolvidos como entidades que contêm ponto e vírgula, de modo que a decodificação de entidades deve preceder a separação de campos, sob pena de deslocamento de colunas.
3. **O TABNET responde HTTP 200 em erro de aplicação**, devolvendo página HTML; a presença do bloco `<pre>` deve ser validada antes de aceitar a resposta.
4. **O índice de procedimento é posicional dentro do arquivo de definição**, não o código SIGTAP, e muda se a definição for republicada; a correspondência deve ser reverificada a cada extração. Há ainda limite prático de cerca de 60 competências por requisição, o que impõe lotes de 12 a 24.

A extração-piloto executada em 1º de agosto de 2026 recuperou 2.578.890 exames citopatológicos em mulheres de 25 a 64 anos, por município de residência, em 100 competências mensais, nas 185 unidades. As séries-controle recuperadas somam 571.866 exames citopatológicos fora da faixa de 25 a 64 anos e 976.947 mamografias na faixa de 50 a 69 anos.

### 3.5.3 Denominador: POPSVS

O denominador é a população feminina residente, por município, ano e faixa etária quinquenal, obtida da base POPSVS (Secretaria de Vigilância em Saúde do Ministério da Saúde, a partir de estimativas do IBGE), disponível no repositório de disseminação do DATASUS em arquivos anuais. A extração agrega a população feminina por município de Pernambuco, ano e faixa quinquenal, a partir de registros de idade simples. A cobertura obtida na extração-piloto foi de 100% das células município × ano × faixa do painel.

Três decisões sobre o denominador são declaradas:

**Especificidade de faixa.** O offset de cada célula do painel utiliza a população da faixa quinquenal correspondente, e não a população agregada de 25 a 64 anos, sempre que a especificação for estratificada por idade. Na especificação principal, agregada, o denominador é a soma das oito faixas quinquenais da faixa-alvo no município e ano.

**Defasagem do último ano.** A base POPSVS pode não ter publicado o último ano da janela no momento da coleta. Nesse caso, adota-se a estimativa do ano mais recente disponível, com sinalização explícita da célula defasada, e a decisão entre repetir, interpolar linearmente ou censurar é tomada na análise e submetida a sensibilidade, não na coleta.

**População total versus população SUS-dependente.** Ribeiro et al. (2025) utilizam, para estimar cobertura, a população feminina de 25 a 64 anos usuária exclusivamente do SUS, apurada no Censo 2022. Adotar a população total no offset produz razão sistematicamente menor que a obtida com denominador SUS-dependente; adotar o denominador SUS-dependente exige fonte municipal de cobertura de saúde suplementar. A decisão adotada é usar a **população feminina total** por município e faixa quinquenal na especificação principal, por três razões: é o denominador da definição normativa do Indicador 5 (BRASIL, 2016); é estável e disponível em série anual para toda a janela, ao passo que a fração SUS-dependente municipal só é apurável em ano censitário; e, sendo o objeto de interesse a mudança de nível e de tendência ao longo do tempo, um denominador multiplicado por fator aproximadamente constante por município é absorvido pelo intercepto aleatório de município e não desloca as estimativas de efeito. A alternativa é submetida a análise de sensibilidade (S6, seção 3.8.5).

### 3.5.4 Covariáveis

As covariáveis são poucas e cada uma tem função declarada, evitando o inflacionamento de termos em um modelo já denso.

| Variável | Definição operacional | Fonte | Função |
|---|---|---|---|
| Porte populacional | População total do município, em estratos | POPSVS/IBGE | Estratificação e interação com os indicadores de interrupção |
| Região e macrorregião de saúde | Pertencimento territorial | [VERIFICAR: PDR/SES-PE] | Descrição e heterogeneidade |
| Exposição ao programa estadual de rastreamento organizado | Indicador binário para Recife e os oito municípios da fase inicial (Amaraji, Barreiros, Cortês, Lagoa dos Gatos, Ribeirão, Primavera, São Benedito do Sul e Tamandaré), a partir de dezembro de 2021 | OPAS; SES-PE (2021) | Cointervenção; estratificação e sensibilidade |
| Substituição tecnológica pelo teste molecular | Registro municipal do procedimento de teste molecular de HPV, por competência | SIA/SUS, sem estratificação etária | Covariável de confundimento a partir de 2024; sensibilidade por censura |
| Competência inválida | Indicador binário para agosto e setembro de 2022 | Construída (ver 3.7.2) | Exclusão da estimação |
| Competência provisória | Indicador binário para as últimas competências da extração | Construída (ver 3.7.3) | Censura ou sensibilidade |

## 3.6 Definição dos desfechos

**Desfecho primário.** Contagem mensal de exames citopatológicos do colo do útero realizados em mulheres de 25 a 64 anos, por município de residência, competência mensal, fonte SISCAN. O parâmetro de interesse é a razão entre essa contagem e a população-alvo dividida por três, isto é, a versão mensalizada do Indicador 5 do Caderno de Diretrizes, Objetivos, Metas e Indicadores 2016 (BRASIL, 2016), operacionalizada como offset log(população-alvo ÷ 3) no modelo de contagem. O fator de divisão 3 é a operacionalização aritmética da periodicidade trienal recomendada: sob adesão perfeita às diretrizes, em um ano apenas um terço da população-alvo deveria ser examinado, de modo que a razão esperada em regime estacionário é 1,0. O offset tem, portanto, lastro normativo, e não apenas conveniência estatística. Registra-se que o instrumento correto de pactuação é a Resolução CIT nº 2, de 16 de agosto de 2016, e não a Portaria GM/MS nº 3.388/2013, que redefine a Qualificação Nacional em Citopatologia e não contém o indicador.

**Desfechos secundários.**

1. Contagem mensal de exames citopatológicos em mulheres **fora** da faixa de 25 a 64 anos, por município de residência (série-controle por característica da população, seção 3.9).
2. Contagem mensal de exames citopatológicos estratificada por faixa etária quinquenal, para verificar se eventual resposta ao incentivo se concentra em faixas específicas.
3. Contagem mensal de mamografias em mulheres de 50 a 69 anos, mantida como série descritiva e como controle **restrito ao período anterior a τ3**, pelas razões expostas em 3.9.
4. Produto documental: matriz de (in)comparabilidade entre os instrumentos oficiais de aferição (seção 3.11).

### 3.6.1 Declaração obrigatória: contagem de exames não é cobertura

A razão de exames tem numerador de eventos e denominador de pessoas; a cobertura tem numerador e denominador de pessoas. São medidas de naturezas distintas, que só coincidiriam sob a hipótese, empiricamente falsa, de que cada mulher realiza no máximo um exame no período. Dias et al. (2022) registraram que a razão de exames não mede cobertura; Ribeiro et al. (2025) quantificaram a discrepância, estimando cobertura de 35,6% no Brasil contra razão de 47,4 exames por 100 mulheres no SISCAN — superestimação de aproximadamente 35% —, com média de 1,3 exames por mulher no triênio e cerca de 3,5 milhões de exames excedentes. Em Pernambuco, foram 965.206 exames para 687.199 mulheres examinadas, correspondendo a cobertura de 32,5% e razão de 45,7 por 100.

A implicação para a inferência é direta e é declarada aqui, e não ao final como confissão: **todo efeito estimado neste estudo é resposta de produção de exames, não ganho de cobertura populacional nem proteção contra o câncer invasor.** Uma elevação da razão é compatível com dois processos causais distintos — captação de mulheres nunca rastreadas, que aumenta a cobertura, e encurtamento do intervalo entre exames em mulheres já rastreadas, que não aumenta cobertura alguma e ainda consome capacidade laboratorial e de seguimento. Sem desduplicação por mulher em série mensal, que não é possível com dados agregados de acesso público, a ambiguidade entre captação e repetição é irredutível neste desenho. Os coeficientes serão nomeados por aquilo que estimam.

## 3.7 Procedimentos de coleta e processamento

A coleta é executada por script único, versionado em repositório público, que baixa o que falta, monta o painel e roda um autoteste sem rede. Três tratamentos de dados são obrigatórios e não negociáveis, porque cada um deles, se omitido, enviesa as estimativas em direção conhecida.

### 3.7.1 Zero-fill contra frame canônico de 185 municípios

O TABNET **omite a linha do município que zera no estrato consultado**. Se um município não registrou nenhum exame em determinada faixa quinquenal e determinada competência, ele simplesmente não aparece na resposta. Sem reposição, um zero verdadeiro é lido pelo software estatístico como observação ausente, e o painel deixa de ser balanceado. Em um modelo de contagem, a consequência é direta: a média condicional é estimada apenas sobre as células em que houve produção, e o efeito é enviesar as estimativas **para cima**, tanto no nível quanto — de forma mais grave — nos segmentos em que a produção colapsa, precisamente o período pandêmico, em que a proporção de municípios com produção nula é máxima. O viés é, portanto, diferencial no tempo e correlacionado com as interrupções de interesse.

O tratamento é o zero-fill contra frame canônico: constrói-se o produto cartesiano completo de 185 municípios × faixas etárias × competências publicadas, e toda célula ausente na resposta do TABNET recebe valor zero, desde que a competência já tenha sido publicada. Células de competências ainda não publicadas **não** recebem zero e permanecem fora do painel, porque ausência de publicação não é ausência de produção. O frame canônico é obtido da API de localidades do IBGE para a Unidade da Federação 26, e sua cardinalidade (185) é verificada por asserção no autoteste do script.

### 3.7.2 Agosto e setembro de 2022 como ausentes, não como zeros

Nas competências de agosto e setembro de 2022, o SISCAN não processou dados em nenhuma unidade da Federação, nem para citopatológico nem para mamografia. Nenhuma série real de rastreamento zera nacionalmente por um mês inteiro: trata-se de falha de processamento do sistema, não de interrupção da assistência. O mês de setembro seguinte recebeu o transbordo dos registros retidos e aparece inflado, razão pela qual as duas competências são tratadas em conjunto.

O tratamento é a codificação de ambas as competências como **ausentes** (`NA`), e não como zeros, com exclusão da estimação. Codificá-las como zero introduziria dois erros simultâneos: um vale artificial de dois meses em todas as 185 séries, e um pico compensatório imediatamente posterior — configuração que um modelo de contagem com termos sazonais interpretaria como estrutura, e não como artefato. Como a exclusão ocorre em um segmento intermediário (entre τ2 e τ3), longe de qualquer ponto de mudança, seu custo em graus de liberdade é baixo. Uma análise de sensibilidade alternativa (S9) reestima o modelo com as duas competências agregadas em um único bimestre e, separadamente, com imputação por média dos harmônicos.

### 3.7.3 Censura ou marcação da cauda provisória

As últimas competências de qualquer extração do SISCAN ainda acumulam lançamento retroativo e aparecem sistematicamente subestimadas, com o grau de subestimação decrescendo à medida que a competência envelhece. Tratar a cauda provisória como dado consolidado produziria uma queda espúria ao final da série — exatamente o segmento em que se situam τ4 e τ5, os marcos de maior interesse substantivo.

O tratamento adotado tem duas camadas. Na coleta, as seis últimas competências disponíveis são **marcadas** como provisórias, e não descartadas, de modo que a decisão de censura permaneça na análise e seja auditável. Na análise, a especificação principal **censura** as competências provisórias, e uma análise de sensibilidade (S11) as reincorpora, permitindo quantificar o impacto da decisão sobre os coeficientes de τ5. Na coleta definitiva de 2027, o intervalo de maturação será recalibrado empiricamente pela comparação entre a extração-piloto de agosto de 2026 e a extração definitiva, para as competências comuns às duas — procedimento que produz, como subproduto, uma estimativa direta da curva de maturação do SISCAN em Pernambuco.

### 3.7.4 Demais procedimentos

- **Registros sem município de residência identificado** são contabilizados e reportados como perda, com o percentual apresentado por ano. Na extração-piloto do SIA, essa perda foi de 3,2% em 2025; o percentual correspondente no SISCAN será reportado. Não há redistribuição proporcional.
- **Verificação de integridade** por reprodução independente da extração e comparação dígito a dígito dos totais por competência e por município, procedimento já executado na extração-piloto.
- **Consistência do denominador** por verificação de que a soma das faixas quinquenais reproduz a população feminina total do município e ano, e por inspeção de descontinuidades entre anos censitários e intercensitários.
- **Reprodutibilidade da série descritiva** por comparação dos totais anuais estaduais com os valores publicados pelo INCA para Pernambuco (INCA, 2023), como verificação externa de ordem de grandeza.

## 3.8 Análise estatística

### 3.8.1 Especificação do modelo

Seja $Y_{it}$ a contagem de exames citopatológicos em mulheres de 25 a 64 anos residentes no município $i$ ($i = 1, \dots, 185$) na competência $t$ ($t = 1, \dots, T$, com $t = 1$ em janeiro de 2018), e seja $N_{it}$ a população feminina de 25 a 64 anos do município $i$ no ano correspondente a $t$.

Adota-se o modelo linear generalizado misto com distribuição binomial negativa na parametrização NB2:

$$Y_{it} \mid \boldsymbol{u}_i,\ \varepsilon_{it} \;\sim\; \text{NB2}(\mu_{it},\ \theta), \qquad \operatorname{Var}(Y_{it}) = \mu_{it} + \frac{\mu_{it}^{2}}{\theta}$$

com preditor linear na escala logarítmica:

$$
\log \mu_{it} \;=\; \underbrace{\log\!\left(\frac{N_{it}}{3}\right)}_{\text{offset}}
\;+\; \beta_0 \;+\; \beta_1 t
\;+\; \sum_{k \in \mathcal{K}} \left[ \delta_k D_{kt} \;+\; \gamma_k (t - \tau_k) D_{kt} \right]
\;+\; \sum_{h=1}^{H} \left[ a_h \sin\!\left(\tfrac{2\pi h t}{12}\right) + b_h \cos\!\left(\tfrac{2\pi h t}{12}\right) \right]
\;+\; \mathbf{x}_{it}^{\top}\boldsymbol{\varphi}
\;+\; u_{0i} \;+\; u_{1i} t \;+\; \varepsilon_{it}
$$

em que:

- $\mathcal{K} = \{B,\ 3,\ 4,\ 5\}$ é o conjunto dos blocos de interrupção, com $B$ designando o bloco único τ1–τ2 (ponto de referência: março de 2020), e 3, 4 e 5 designando τ3 (maio de 2024), τ4 (maio de 2025) e τ5 (maio de 2026);
- $D_{kt} = \mathbb{1}[t \geq \tau_k]$ é o indicador de pós-interrupção;
- $\delta_k$ é a mudança **de nível** associada à interrupção $k$, e $\exp(\delta_k)$ é a razão de taxas imediata;
- $\gamma_k$ é a mudança **de tendência** (inclinação) associada à interrupção $k$, e $\exp(\gamma_k)$ é o fator multiplicativo mensal adicional sobre a taxa;
- $H$ é o número de pares harmônicos de Fourier, pré-especificado em $H = 2$;
- $\mathbf{x}_{it}$ é o vetor de covariáveis da seção 3.5.4, com coeficientes $\boldsymbol{\varphi}$;
- $(u_{0i},\ u_{1i})^{\top} \sim \mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma}_u)$ são o intercepto e a inclinação aleatórios do município $i$, com $\boldsymbol{\Sigma}_u$ irrestrita (variâncias $\sigma_{u_0}^2$ e $\sigma_{u_1}^2$ e correlação $\rho_u$);
- $\varepsilon_{it}$ é o termo de dependência serial intra-município, com estrutura autorregressiva de primeira ordem: $\operatorname{Cor}(\varepsilon_{it},\ \varepsilon_{i,t+s}) = \phi^{|s|}$, $|\phi| < 1$, independente entre municípios.

O coeficiente do offset é **fixado em 1**, não estimado, o que faz do modelo um modelo de razão de exames por população-alvo anualizada, e não de contagem bruta.

O contrafactual para o segmento posterior a uma interrupção $k^{*}$ é obtido por predição do mesmo modelo com $\delta_k = \gamma_k = 0$ para todo $k \geq k^{*}$, mantidos os demais termos, incluindo sazonalidade e efeitos aleatórios. Os intervalos de confiança do contrafactual são obtidos por simulação da distribuição preditiva a partir da matriz de covariância dos parâmetros estimados, com 10.000 réplicas.

### 3.8.2 Justificativa da família e da parametrização

Contagens municipais mensais de exames apresentam variância muito superior à média, por concentração de oferta, mutirões e efeitos de calendário administrativo, o que torna a distribuição de Poisson inadequada. Adota-se a binomial negativa na parametrização NB2, com variância quadrática na média, pré-especificada no protocolo. Registra-se, por rigor de atribuição, que o tutorial de Bhaskaran et al. (2013), frequentemente invocado nesse contexto, **não trata da binomial negativa** — sua contribuição a este desenho é restrita ao tratamento de tendência de longo prazo, sazonalidade por harmônicos de Fourier e splines, sobredispersão em Poisson por ajuste dos erros-padrão e autocorrelação residual. A justificativa da família apoia-se em Brooks et al. (2017), em Campbell (2021) e nos precedentes aplicados brasileiros (RASELLA et al., 2013; RUSSO et al., 2021).

Municípios pequenos, com poucas centenas de mulheres na faixa-alvo, produzirão competências com contagem zero, o que levanta a questão da zero-inflação. Campbell (2021) demonstra que decidir sobre zero-inflação e sobredispersão por meio de testes preliminares ou de critérios de informação em amostras pequenas infla substancialmente a taxa de falsos positivos nas inferências subsequentes. A conduta adotada é, por isso, pré-especificar NB2, comparar de forma declarada com NB1 e com a variante zero-inflada **apenas como sensibilidade reportada** (S3), e avaliar o ajuste por resíduos quantílicos simulados, em vez de encadear testes de hipótese sequenciais.

### 3.8.3 Estrutura de dependência

A estrutura de efeitos aleatórios por município responde ao argumento de Ewusie et al. (2020) contra a agregação e permite que nível e tendência basais variem entre unidades. A dependência serial intra-município é tratada por estrutura AR1, especificada **a priori** e não introduzida por diagnóstico post hoc. Turner, Karahalios, Forbes et al. (2021b) fornecem o argumento: as estimativas de autocorrelação divergem substancialmente entre métodos — mediana de 0,20 sob REML contra 0,04 sob ARIMA e 0,05 sob Prais-Winsten — e só convergem em séries com pelo menos 100 pontos temporais. A janela de 108 meses situa-se logo acima desse limiar, o que torna a autocorrelação estimável, mas não recomenda correções guiadas por diagnóstico.

A sazonalidade é modelada por $H = 2$ pares de harmônicos de Fourier, e não por onze indicadores mensais, por parcimônia: quatro parâmetros em vez de onze, em um modelo que já consome muitos com quatro blocos de interrupção e efeitos aleatórios. Ignorar a sazonalidade em ITS mensal confunde variação cíclica com mudança de nível, sobretudo quando um ponto de interrupção coincide com vale ou pico sazonal — e três dos quatro blocos deste estudo caem em maio. O precedente aplicado é quase idêntico ao caso em questão: Duarte, Argenton e Carvalheira (2022) analisaram contagens mensais de Papanicolaou e mamografia em São Paulo entre janeiro de 2017 e novembro de 2021 por ITS com modelo linear generalizado quasi-Poisson, dois pares de harmônicos para sazonalidade mensal e contrafactual por bootstrap de Monte Carlo. O número de pares é pré-especificado e sua adequação verificada pelos resíduos (S4).

### 3.8.4 Diagnósticos

1. **Resíduos quantílicos simulados** (abordagem de simulação a partir do modelo ajustado), com inspeção de uniformidade, de dispersão e de excesso de zeros, e teste de desvio de uniformidade. Substituem a bateria de testes sequenciais desaconselhada por Campbell (2021).
2. **Autocorrelação residual**: funções de autocorrelação e autocorrelação parcial dos resíduos por município, agregadas, para verificar se a estrutura AR1 é suficiente.
3. **Dependência espacial**: protocolo escalonado em três passos. Ajusta-se o modelo; agregam-se os resíduos quantílicos por município; calcula-se o índice I de Moran sobre essa distribuição, com matriz de vizinhança por contiguidade. Havendo autocorrelação espacial residual, escala-se para modelo com componente espacialmente estruturada, adotando a reparametrização BYM2 de Riebler et al. (2016), que escala a componente estruturada e reduz o modelo a um parâmetro de precisão e um de mistura, permitindo prioris penalizadoras de complexidade interpretáveis — vantagem decisiva sobre o BYM clássico, no qual as duas componentes não podem ser especificadas independentemente. Costa-Ribeiro et al. (2026) demonstram a via prática de estimação bayesiana em painel municipal brasileiro de ITS. Registra-se que o protocolo de escalonamento é escolha deste projeto, ancorada teoricamente, e não replicação de precedente aplicado nacional.
4. **Influência**: identificação de municípios com influência desproporcional sobre os coeficientes de interrupção, por reajuste com exclusão sequencial dos dez municípios de maior volume.
5. **Convergência**: verificação do gradiente e da matriz hessiana do ajuste, com reajuste sob otimizadores alternativos em caso de convergência marginal.

### 3.8.5 Análises de sensibilidade pré-especificadas

Todas as análises abaixo são declaradas no protocolo antes da coleta definitiva. Nenhuma será substituída ou suprimida em função do resultado, e as divergências entre especificações serão reportadas como incerteza do desenho, não resolvidas por seleção post hoc.

| # | Análise | O que testa |
|---|---|---|
| S1 | τ1 deslocado de jan/2020 para jan/2019 (publicação e adaptação), ampliando o segmento intermediário | Robustez das conclusões sobre τ3, τ4 e τ5 à escolha do ponto inicial e à hipótese de antecipação |
| S2 | Exclusão do período de transição pandêmico (mar–ago/2020) da estimação, à maneira de Nascimento et al. (2020) | Contaminação das estimativas de nível pelo período de implantação e colapso |
| S3 | Famílias alternativas: NB1, binomial negativa zero-inflada e quasi-Poisson | Dependência dos resultados da hipótese distribucional, sem seleção por teste preliminar (CAMPBELL, 2021) |
| S4 | Sazonalidade com $H = 1$, $H = 3$ e com onze indicadores mensais | Adequação da parcimônia dos harmônicos e confusão entre ciclo e nível |
| S5 | Censura da série em dez/2024 e, alternativamente, em jun/2025; e inclusão da covariável de teste molecular de HPV | Substituição tecnológica pelo teste de DNA-HPV como explicação alternativa de queda pós-2024 |
| S6 | Denominador alternativo: população feminina SUS-dependente, por aplicação da fração municipal apurada no Censo 2022 | Sensibilidade do offset à escolha do denominador (RIBEIRO et al., 2025) |
| S7 | Exclusão dos nove municípios do programa estadual de rastreamento organizado; e, alternativamente, termo de interação com o indicador de exposição a partir de dez/2021 | Cointervenção estadual não mensurada (OPAS; SES-PE, 2021) |
| S8 | Exclusão de Recife e exclusão de Fernando de Noronha | Influência do município de maior volume e da unidade de menor população |
| S9 | Agosto e setembro de 2022 agregados em bimestre; e, alternativamente, imputados pelos harmônicos | Robustez ao tratamento da falha de processamento do SISCAN |
| S10 | Reinclusão das competências provisórias censuradas | Impacto da maturação da série sobre os coeficientes de τ5 |
| S11 | Modelo com componente espacial BYM2, condicional à detecção de I de Moran significativo | Dependência espacial residual entre municípios contíguos |
| S12 | Reestimação em subamostras por porte populacional e por estrato de vulnerabilidade | Heterogeneidade da resposta e hipótese de penalização diferencial por capacidade administrativa |

## 3.9 Série-controle

Lopez Bernal et al. (2018) tipificam seis classes de controle em ITS — localidade, característica da população, comportamento, coorte histórica, desfecho-controle e período-controle — e recomendam definir a priori os confundidores concorrentes, ajustar simultaneamente ITS simples e ITS controlado e interpretar com cautela quando as duas estimativas divergirem. Alertam ainda para dois riscos: contaminação, quando a intervenção afeta indiretamente a série-controle, e mudança diferencial de composição populacional ao longo do tempo. A prática brasileira já incorpora a lógica: Russo et al. (2021) usam internações por acidente de transporte como desfecho-controle, e Pinto et al. (2022) constroem ITS controlado por estratificação de municípios prioritários.

### 3.9.1 Por que a mamografia foi descartada

O candidato natural seria a mamografia de rastreamento, que compartilha com o citopatológico a via de oferta, o público feminino, o sistema de informação e o choque pandêmico. Ferreira et al. (2023) e Duarte, Argenton e Carvalheira (2022) analisam as duas séries em paralelo, mas nenhum dos dois estabelece uma como contrafactual da outra.

Esse controle deixa de ser válido a partir de maio de 2025. A Nota Metodológica do indicador C7 mostra que o indicador agrega, **na mesma fórmula ponderada**, o rastreamento do colo do útero em pessoas de 25 a 64 anos, com janela de 36 meses e peso de 20 pontos, e o rastreamento de câncer de mama em pessoas de 50 a 69 anos, com janela de 24 meses, peso igualmente de 20 pontos e procedimentos SIGTAP 02.04.03.003-0 e 02.04.03.018-8 (BRASIL, 2026a). A mamografia passa a ser **co-incentivada pelo mesmo indicador** de cofinanciamento que incentiva o citopatológico. Trata-se de contaminação no sentido exato de Lopez Bernal et al. (2018): a intervenção cujo efeito se quer estimar atua diretamente sobre a série que serviria de controle, tornando-a inservível como contrafactual a partir dessa data — precisamente o período de maior interesse substantivo do estudo.

Acrescente-se uma razão técnica independente: as duas definições do TABNET divergem no campo de competência, com o citopatológico usando a data de liberação do laudo e a mamografia usando a competência de faturamento, o que impede tratar as séries como comensuráveis mês a mês sem uma correção de defasagem que não é estimável com dados públicos.

A mamografia é, portanto, mantida como **série descritiva** e como controle **restrito ao período anterior a τ3**, condicionado à verificação documental de que o indicador nº 4 do Previne Brasil não contemplava mamografia em nenhuma de suas versões — verificação que integra o componente documental.

### 3.9.2 O controle adotado: por característica da população

A alternativa adotada é o controle por característica da população, uma das seis classes tipificadas por Lopez Bernal et al. (2018): a série de exames citopatológicos realizados em mulheres **fora** da faixa de 25 a 64 anos, extraída da mesma definição do TABNET, com as mesmas faixas quinquenais complementares (15-19, 20-24, 65-69, 70-74, 75-79 e 80 anos ou mais) e o mesmo recorte por município de residência.

A justificativa é estrutural. Essas mulheres são atendidas pela mesma rede, pelos mesmos profissionais e pelos mesmos laboratórios; seus exames são registrados no mesmo sistema, com o mesmo campo de competência; e sofreram o mesmo choque pandêmico. Não integram, porém, o numerador de nenhum indicador de cofinanciamento — nem do indicador nº 4 do Previne Brasil, restrito à faixa de 25 a 64 anos, nem da boa prática (A) do C7, igualmente restrita a essa faixa. O contraste isola, portanto, o componente da variação atribuível ao incentivo financeiro daquele atribuível a determinantes comuns de oferta.

O modelo controlado acrescenta ao preditor linear um indicador de grupo $G$ (alvo *versus* controle) e suas interações com os termos de interrupção, de modo que $\delta_k^{\text{dif}}$ e $\gamma_k^{\text{dif}}$ estimam a diferença de mudança de nível e de tendência entre as duas séries. Seguindo a recomendação dos próprios autores, **ITS simples e ITS controlado são estimados e reportados lado a lado**, e a divergência entre eles é tratada como informação, não como problema a ser suprimido.

Três limitações são declaradas. Primeira, a série-controle é substancialmente menor em volume — 571.866 exames contra 2.578.890 na série-alvo, na extração-piloto —, o que reduz sua precisão. Segunda, ela é potencialmente mais sensível a mudanças de composição populacional, o que exige verificação da estabilidade do denominador etário ao longo da janela. Terceira, é possível que uma política de qualificação do rastreamento reduza deliberadamente os exames fora da faixa etária, caso em que a série-controle não seria estritamente não exposta — hipótese que será examinada à luz da evolução da proporção de exames na faixa-alvo, documentada para Pernambuco entre 2018 e 2022 (INCA, 2023), e que, se confirmada, atenua e não anula o contraste, por atuar em direção oposta à do incentivo.

## 3.10 Poder estatístico

Não existe literatura de cálculo de poder para ITS com múltiplos pontos de mudança em painel de contagens. O arcabouço disponível mais próximo é Liu et al. (2019), que desenvolvem cálculo de poder e tamanho amostral por simulação para ITS com desfechos de contagem em modelos log-lineares *observation-driven* sob Poisson e binomial negativo. Seus resultados servem como referência de ordem de grandeza: com 48 observações, efeito combinado $\beta_2 + \beta_3 = -1{,}0$ na escala logarítmica e ausência de autocorrelação ($\gamma_1 = 0$), o poder estimado é 0,92 sob Poisson e 0,96 sob binomial negativo; para $\beta_2 + \beta_3 = +1{,}0$ nas mesmas condições, o poder é 0,99 em ambas as famílias, chegando a 1,0 com $\gamma_1 = 0{,}7$. Os autores observam que, sob binomial negativo, o poder é não monotônico na autocorrelação, crescendo e depois decrescendo à medida que $\gamma_1$ aumenta. O arcabouço trata, contudo, de uma série, uma interrupção e modelos *observation-driven*, e não de modelo misto em painel com múltiplos pontos de mudança — de modo que esses valores não são transferíveis ao desenho aqui proposto, servindo apenas de balizamento.

A âncora bibliográfica para poder por simulação em modelos mistos generalizados é Green e MacLeod (2016), que formalizam a lógica de três passos — simular a resposta a partir do modelo ajustado, reajustar o modelo aos dados simulados, aplicar o teste — e a produção de curvas de poder por magnitude de efeito e tamanho amostral. **Há, porém, uma restrição prática que precisa ser declarada: o pacote `simr` é construído sobre modelos `lme4`/`glmer` e não suporta objetos `glmmTMB` nem estruturas de covariância AR1.** Não é possível, portanto, executar a análise de poder deste desenho com essa ferramenta.

A via adotada é simular diretamente do objeto `glmmTMB` ajustado, por meio do método `simulate()`, replicando manualmente a lógica de três passos de Green e MacLeod (2016). Isso preserva, na geração dos dados sintéticos, a família binomial negativa, o offset, os efeitos aleatórios por município e a estrutura AR1. O procedimento é o seguinte:

1. Ajustar o modelo completo aos dados observados da extração-piloto, obtendo estimativas de $\beta_0$, $\beta_1$, $\theta$, $\boldsymbol{\Sigma}_u$, $\phi$ e dos parâmetros sazonais.
2. Fixar os coeficientes de interrupção em valores de uma grade pré-especificada: $\delta_k \in \{0{,}02;\ 0{,}05;\ 0{,}10;\ 0{,}15;\ 0{,}20;\ 0{,}30\}$ em valor absoluto na escala logarítmica, e $\gamma_k \in \{0{,}002;\ 0{,}005;\ 0{,}010;\ 0{,}015\}$ por mês.
3. Para cada ponto da grade, gerar 1.000 conjuntos de dados sintéticos, reajustar o modelo e registrar a proporção de réplicas em que o coeficiente correspondente é declarado significativo ao nível de 5%.
4. Repetir a grade para números decrescentes de municípios efetivamente analisáveis (185, 150, 100, 50) e para comprimentos de série de 108, 100 e 84 competências, de modo a quantificar o custo de eventual censura.

As curvas de poder são construídas e **reportadas separadamente para mudança de nível e para mudança de tendência**, distinção necessária porque, como mostram Liu et al. (2019), o poder difere substancialmente entre os dois alvos e o efeito combinado. Reporta-se também o efeito mínimo detectável com poder de 80% em cada configuração. A semente do gerador de números aleatórios é fixada e registrada. Trata-se de escolha metodológica do projeto, documentada no protocolo por ausência de orientação publicada para o caso, e não de aplicação de procedimento padronizado.

## 3.11 Análise documental comparativa

O componente documental não é acessório: em um campo em que o gestor federal reformulou duas vezes o instrumento de aferição sem publicar ponte de comparabilidade, documentar sistematicamente a (in)comparabilidade é resultado de pesquisa.

**Corpus.** Atos normativos federais (portarias GM/MS, portarias de consolidação, resoluções CIT), notas técnicas e notas metodológicas da SAPS/MS com identificador SEI, fichas de qualificação de indicadores, material oficial de orientação e notas técnicas conjuntas tripartites, todos com localizador (DOU com edição, seção e página; ou número SEI e processo). Fontes sem localizador verificável são excluídas do corpus e registradas como pendência.

**Procedimento.** Extração dirigida por matriz de dimensões, com dupla conferência do texto integral do ato e registro literal dos trechos que sustentam cada célula. Divergências entre o texto normativo e o material secundário de orientação são registradas como tais, com prevalência do texto normativo.

**Produto: matriz de (in)comparabilidade.** A matriz confronta as dimensões operacionais do instrumento oficial de aferição do rastreamento antes e depois de cada ruptura.

**Tabela 3 — Matriz de (in)comparabilidade: dimensões e rupturas**

| Dimensão | Indicador nº 4, versão original (2020-2021) | Ruptura 1 — Portaria GM/MS nº 102/2022 (jan/2022) | Ruptura 2 — transição para o C7 (mai/2024 a mai/2025) | Ruptura 3 — Nota Metodológica C7 vigente (jan/2026) |
|---|---|---|---|---|
| Denominação | Indicador nº 4 do Previne Brasil | Alterada | Boa prática (A) do indicador C7 | Mantida |
| Numerador | Coleta de citopatológico registrada | Passa a exigir coleta **realizada na APS** | Passa a admitir exame **coletado, solicitado ou avaliado** | Incorpora o teste molecular de HPV |
| Códigos aceitos | Um procedimento SIGTAP | Um procedimento SIGTAP | Seis procedimentos SIGTAP mais dois códigos ABEX/ABP | Acresce SIGTAP 02.02.10.025-1 |
| Janela de acumulação | 36 meses | 36 meses | 36 meses | 36 meses, **exceto 60 meses** para o teste molecular |
| Denominador | Mulheres **cadastradas**, com piso ancorado em estimativa do IBGE | Mulheres **cadastradas e vinculadas** | Pessoas de 25 a 64 anos **vinculadas à equipe**, nos termos da NT nº 30/2025 | Mantido |
| Fonte | SISAB | SISAB | SIAPS, SCNES e RNDS | Mantida |
| Granularidade | Município | Município | Identificador Nacional de Equipe (INE) | Mantida |
| Métrica | Percentual, meta de 40%, parâmetro de 80%, peso 1 | Percentual | Pontuação: 20 de 100 pontos do C7, que é 1 de 7 indicadores do componente de qualidade | Mantida |
| Público-alvo | Mulheres de 25 a 64 anos | Mulheres de 25 a 64 anos | Ampliado (mulheres e homens transgênero) | Mantido |
| Periodicidade de avaliação | Quadrimestral | Quadrimestral | Quadrimestral, com extração no 20º dia útil | Mantida |
| Consequência financeira | Pagamento por desempenho, com risco de perda | Idem | Classificação "bom" garantida na transição; sem risco de perda dentro da janela | Idem |

**Análise.** Para cada dimensão, classifica-se a ruptura em três níveis — comparabilidade preservada, comparabilidade condicionada a ajuste explicitado, e incomparabilidade — e registra-se a existência ou inexistência de fator de conversão, série retrocalculada ou tabela de equivalência publicada pelo gestor federal. A ausência desses instrumentos, se confirmada, é ela própria o achado.

**Articulação com o componente quantitativo.** A matriz cumpre três funções: fundamenta a decisão de não usar o indicador oficial como desfecho; delimita quais rupturas devem ser tratadas como ameaças à validade do desfecho do SISCAN (nenhuma delas diretamente, por independência de fonte) e quais afetam apenas a interpretação da exposição; e sustenta a formulação da hipótese de exposição a incentivo de **baixa intensidade**, discutida a seguir.

**Consequência central sobre a hipótese.** Dentro da janela de janeiro de 2018 a dezembro de 2026, o indicador C7 **nunca carregou risco financeiro de perda**. A Portaria GM/MS nº 10.994, de 13 de maio de 2026, manteve a classificação "bom" no componente de qualidade até o 1º quadrimestre de 2026 e instituiu, no 2º quadrimestre de 2026, implantação parcial e assimétrica, em que apenas equipes classificadas como "ótimo" recebem valor diferenciado, enquanto "bom", "suficiente" e "regular" recebem indistintamente o valor de "bom"; a implementação integral, com risco bilateral, só se inicia no 1º quadrimestre de 2027, fora da janela (BRASIL, 2026b). A hipótese do estudo deve, portanto, ser formulada como **exposição a incentivo de baixa intensidade**, e a assimetria da implantação é, ela própria, achado relevante para a gestão. Nenhuma leitura dos resultados pode atribuir eventual variação pós-2024 a resposta a risco de perda financeira. O estudo não estima o efeito do pagamento por desempenho do novo modelo: estima o efeito da mudança de arranjo de financiamento e de regime de mensuração.

## 3.12 Recursos computacionais e reprodutibilidade

**Extração e montagem do painel.** Python 3, biblioteca padrão, sem dependência de navegador automatizado, em script único versionado que baixa o que falta, monta o painel e executa autoteste sem rede. O autoteste verifica, por asserção, os pontos que quebraram tentativas anteriores: descarte da coluna de total da linha, decodificação de entidades HTML antes da separação de campos, validação do bloco `<pre>` na resposta, cardinalidade 185 do frame canônico, e presença das competências de agosto e setembro de 2022 na lista de competências inválidas.

**Modelagem.** R, com `glmmTMB` para o modelo misto binomial negativo com offset e estrutura AR1 (BROOKS et al., 2017), `DHARMa` para resíduos quantílicos simulados, `spdep` para o índice I de Moran e a matriz de contiguidade, e `INLA` para o modelo BYM2, se o diagnóstico espacial o exigir. Registra-se que não foi localizada aplicação publicada em saúde pública brasileira que combine `glmmTMB`, binomial negativo e AR1 em painel municipal, de modo que a escolha computacional se justifica pela flexibilidade documentada do software e não por precedente aplicado nacional.

**Reprodutibilidade.** Repositório público com histórico de versões contendo: o script de extração; os dados brutos como retornados pelo TABNET, sem edição manual; o painel montado; os scripts de modelagem; e o registro da sessão de execução com versões de linguagem e de pacotes. Sementes de números aleatórios fixadas e registradas em toda simulação. A data de cada extração é registrada, dado que o TABNET é base viva sujeita a lançamento retroativo, e a extração definitiva de 2027 será comparada à extração-piloto de agosto de 2026 nas competências comuns, com a diferença reportada como medida empírica de maturação da série.

**Diretrizes de reporte.** O reporte segue o STROBE (VON ELM et al., 2007) como arcabouço geral para estudos observacionais e o RECORD (BENCHIMOL et al., 2015) como extensão diretamente aplicável, por se tratar de estudo conduzido com dados de saúde coletados rotineiramente — cobrindo explicitamente a descrição da população extraída dos bancos, os códigos e algoritmos de seleção, a validação e o acesso aos dados e ao código. A esses somam-se duas recomendações operacionais específicas de ITS: a pré-especificação do método no protocolo com apresentação de análises de sensibilidade (TURNER; KARAHALIOS; FORBES et al., 2021b) e os critérios de representação gráfica — pontos observados, linhas de tendência por segmento com quebras nítidas nas interrupções, representação da sazonalidade estimada e intervalos de confiança em torno da tendência ajustada e do contrafactual (TURNER; KARAHALIOS; FORBES et al., 2021a), critérios que apenas 33% dos gráficos revisados por aqueles autores atendiam conjuntamente. Não existe, até o momento, diretriz de reporte específica para ITS publicada; a iniciativa CARITS está registrada como em desenvolvimento na EQUATOR Network, e deverá ser reconsultada e, se publicada, adotada na redação final.

## 3.13 Vieses potenciais e mitigação

**Tabela 4 — Ameaças à validade, direção esperada e mitigação**

| # | Viés / ameaça | Mecanismo | Direção esperada | Mitigação | Residual |
|---|---|---|---|---|---|
| 1 | **Subnotificação por implantação incompleta do SISCAN** | Se a cobertura do SISCAN em Pernambuco cresceu ao longo da janela, parte da tendência ascendente é artefato de implantação do sistema, e não aumento de produção. A cobertura dos sistemas de informação do câncer perdeu 20% no período 2008-2019 para o citopatológico (TOMAZELLI; RIBEIRO; DIAS, 2022), e a cobertura por mulher rastreada sequer pôde ser calculada para quatro unidades da Federação por implantação insuficiente do SISCAN (INCA, 2025) | Superestimação da tendência basal e, criticamente, **possível confusão com τ1**, cuja data coincide com o período de consolidação do sistema | (a) Reconstruir a série de completude do SISCAN em Pernambuco por município, pela razão entre o volume do SISCAN e o volume total do SIA sem estratificação etária, competência a competência; (b) incluir essa razão como covariável de completude no preditor linear; (c) análise de sensibilidade restringindo o painel aos municípios com razão estável desde 2018 | **Alto.** É a ameaça de maior gravidade do estudo e não é eliminável com fontes secundárias. Deve constar dos resultados, e não apenas das limitações |
| 2 | Substituição tecnológica pelo teste de DNA-HPV | A partir de 2024-2025, queda na contagem de citopatológicos pode expressar substituição de método, não desinvestimento. Não há dado público sobre data e ritmo de implantação por município em Pernambuco | Subestimação da produção pós-τ3 e pós-τ4 | Covariável construída a partir do registro do procedimento molecular no SIA/SUS por município; análises de sensibilidade S5 com censura em dez/2024 e jun/2025 | Moderado a alto. Não eliminável |
| 3 | Cointervenção estadual não mensurada | Programa estadual de rastreamento organizado em Recife e oito municípios desde dez/2021, sem avaliação publicada nem dados divulgados (OPAS; SES-PE, 2021) | Superestimação do efeito em nove das 185 unidades | Indicador binário de exposição, estratificação e sensibilidade S7 | Moderado |
| 4 | Zero-fill omitido | O TABNET omite a linha do município que zera no estrato; zero verdadeiro lido como ausente | Superestimação da média condicional, com viés **diferencial no tempo**, máximo no período pandêmico | Zero-fill obrigatório contra frame canônico de 185 unidades, com asserção no autoteste (seção 3.7.1) | Eliminado, se o procedimento for aplicado |
| 5 | Falha de processamento do SISCAN em ago/2022 | Duas competências sem processamento nacional, com transbordo em setembro | Vale artificial seguido de pico compensatório | Codificação como ausentes e exclusão da estimação; sensibilidade S9 | Baixo |
| 6 | Cauda provisória da série | Lançamento retroativo subestima as últimas competências | Queda espúria ao final, justamente onde estão τ4 e τ5 | Marcação na coleta, censura na análise principal, sensibilidade S10, recalibração empírica da curva de maturação na coleta de 2027 | Baixo a moderado |
| 7 | Município de residência ignorado | Perda de registros sem identificação do município | Subestimação não diferencial, salvo se a perda variar no tempo | Contabilização e reporte do percentual por ano; verificação de estabilidade temporal da perda | Baixo, se estável |
| 8 | Fragilidade do índice posicional do TABNET | O índice de procedimento é posicional no arquivo de definição e muda se este for republicado | Erro de extração, potencialmente catastrófico e silencioso | Reverificação da correspondência a cada extração e validação do bloco `<pre>`; reprodução independente com conferência dígito a dígito | Baixo |
| 9 | Denominador defasado e escolha entre população total e SUS-dependente | POPSVS pode não publicar o último ano; a fração SUS-dependente só é apurável em ano censitário | Deslocamento de nível, aproximadamente constante por município | Sinalização das células defasadas; sensibilidade S6; absorção do fator constante pelo intercepto aleatório | Baixo |
| 10 | Contagem de exames interpretada como cobertura | Numerador de eventos sobre denominador de pessoas; 1,3 exames por mulher no triênio (RIBEIRO et al., 2025) | Superestimação da proteção populacional inferida | Declaração no desenho, nos objetivos, nos resultados e na discussão (seção 3.6.1); nomeação dos coeficientes como resposta de produção | **Irredutível** neste desenho |
| 11 | Falácia ecológica | Unidade de análise é o município; não se inferem relações individuais | Inferência indevida sobre mulheres | Restrição explícita das conclusões ao nível municipal; ausência de qualquer afirmação individual | Controlado por restrição de escopo |
| 12 | Não separabilidade de τ1 e τ2 | Duas interrupções a dois meses de distância; colunas quase colineares | Atribuição arbitrária de efeito entre política e pandemia | Bloco único declarado a priori; renúncia explícita à separação; sensibilidades S1 e S2 | Assumido como limitação de desenho |
| 13 | Heterogeneidade de qualidade laboratorial entre municípios | Sensibilidade da citologia depende de coleta e leitura locais, com variação documentada entre centros (RAMÍREZ et al., 2023); 27% dos municípios de PE com insatisfatoriedade acima de 5% em 2023 (INCA, 2025) | Ruído adicional entre unidades; possível confusão com volume | Efeitos aleatórios por município absorvem heterogeneidade estável; a variação temporal da qualidade não é mensurável por município e é declarada | Moderado, não mensurável |
| 14 | Mudança de composição da série-controle | Exames fora da faixa-alvo podem cair por qualificação do rastreamento, e não por ausência de incentivo | Atenuação do contraste controlado | Verificação da estabilidade do denominador etário; reporte simultâneo de ITS simples e controlado | Baixo, e em direção conservadora |
| 15 | Múltiplas comparações | Quatro blocos × dois parâmetros × múltiplos desfechos e sensibilidades | Falsos positivos | Hierarquia de desfechos declarada a priori (primário, secundários, sensibilidades); sensibilidades reportadas como robustez, não como testes independentes; ênfase em magnitude e intervalo, não em dicotomia de significância | Controlado por disciplina de reporte |

## 3.14 Aspectos éticos

O estudo utiliza exclusivamente dados secundários, agregados, de domínio público e sem qualquer possibilidade de identificação individual: contagens municipais mensais de procedimentos, disponibilizadas pelo DATASUS por interface pública de tabulação, e estimativas populacionais publicadas pelo Ministério da Saúde e pelo IBGE. Não há contato com participantes, não há coleta de dados primários, não há acesso a prontuário, a registro nominal ou a microdado identificado, e não há linkage entre bases.

Nessas condições, a pesquisa se enquadra, em tese, na hipótese de não registro e não avaliação pelo sistema CEP/CONEP prevista no parágrafo único do art. 1º da Resolução CNS nº 510, de 7 de abril de 2016, que exclui do âmbito de apreciação ética as pesquisas com bancos de dados cujas informações são agregadas, sem possibilidade de identificação individual, e as pesquisas com informações de acesso público.

**Ressalva expressa.** A dispensa **não será presumida**. O Comitê de Ética em Pesquisa do Instituto Aggeu Magalhães não dispõe de política pública explícita de dispensa para bases secundárias agregadas e de acesso público; sua página institucional remete genericamente às resoluções do Conselho Nacional de Saúde e exige submissão via Plataforma Brasil, sem enunciar hipótese de não submissão. Em um programa em que a adequação ética integra a avaliação do projeto, presumir dispensa é risco desnecessário e assimétrico.

Adota-se, por isso, a seguinte conduta, declarada no projeto:

1. **Consulta formal prévia ao CEP-IAM**, por meio do endereço institucional do comitê, solicitando manifestação sobre a necessidade de apreciação ética do desenho tal como descrito, com anexação do resumo do protocolo e da descrição das fontes.
2. **Reprodução integral da manifestação obtida** nesta seção do projeto e, posteriormente, na dissertação, qualquer que seja o teor.
3. **Submissão via Plataforma Brasil** caso a manifestação indique necessidade de apreciação, ou caso não haja manifestação em prazo compatível com o cronograma. Os prazos institucionais informados pelo comitê — conferência documental em até dez dias, parecer em trinta dias contados da aceitação integral e trinta dias para atendimento de pendências — são incorporados ao cronograma do projeto como caminho crítico.
4. **Ausência de conflito de interesses** e ausência de financiamento com vínculo a qualquer das partes envolvidas na política avaliada, ambos declarados.

Registra-se, por fim, que a natureza agregada e pública dos dados dispensa Termo de Consentimento Livre e Esclarecido e não enseja tratamento de dados pessoais na acepção legal, uma vez que nenhuma informação relativa a pessoa natural identificada ou identificável é acessada ou processada [VERIFICAR: confirmar, na consulta ao CEP-IAM, se o comitê exige manifestação específica sobre a Lei Geral de Proteção de Dados para bases agregadas de acesso público].

---

## Referências desta seção

BENCHIMOL, E. I.; SMEETH, L.; GUTTMANN, A. et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) Statement. **PLOS Medicine**, v. 12, n. 10, e1001885, 2015.

BHASKARAN, K.; GASPARRINI, A.; HAJAT, S.; SMEETH, L.; ARMSTRONG, B. Time series regression studies in environmental epidemiology. **International Journal of Epidemiology**, v. 42, n. 4, p. 1187-1195, 2013.

BRASIL. Conselho Nacional de Saúde. **Resolução nº 510, de 7 de abril de 2016.** Dispõe sobre as normas aplicáveis a pesquisas em Ciências Humanas e Sociais. Diário Oficial da União, Brasília, DF, 24 maio 2016.

BRASIL. Ministério da Saúde. **Caderno de Diretrizes, Objetivos, Metas e Indicadores 2016.** Brasília, DF: Ministério da Saúde, 2016. Indicador 5 — Razão de exames citopatológicos do colo do útero em mulheres de 25 a 64 anos e a população da mesma faixa etária, p. 14-15. (Indicadores pactuados por meio da Resolução CIT nº 2, de 16 de agosto de 2016.)

BRASIL. Ministério da Saúde. Secretaria de Atenção Primária à Saúde. Departamento de Saúde da Família. **Nota Técnica nº 3/2022-DESF/SAPS/MS**: indicadores de pagamento por desempenho do Programa Previne Brasil. Brasília, DF: Ministério da Saúde, 2022a. SEI nº 0024999684, processo nº 25000.012850/2020-33.

BRASIL. Ministério da Saúde. Gabinete do Ministro. **Portaria GM/MS nº 3.493, de 10 de abril de 2024.** Altera a Portaria de Consolidação GM/MS nº 6, de 28 de setembro de 2017, para instituir nova metodologia de cofinanciamento federal do Piso de Atenção Primária à Saúde no âmbito do Sistema Único de Saúde (SUS). Diário Oficial da União, Brasília, DF, ed. 70, seção 1, p. 100, 11 abr. 2024a.

BRASIL. Ministério da Saúde. Secretaria de Atenção Primária à Saúde. **Perguntas frequentes — Novo Modelo de Cofinanciamento Federal da Atenção Primária à Saúde.** Brasília, DF: Ministério da Saúde, 2024b.

BRASIL. Ministério da Saúde. Gabinete do Ministro. **Portaria GM/MS nº 6.907, de 29 de abril de 2025.** Altera a Portaria de Consolidação GM/MS nº 6, de 28 de setembro de 2017, e a Portaria GM/MS nº 3.493, de 10 de abril de 2024, referentes à metodologia de cofinanciamento federal do Piso de Atenção Primária à Saúde. Diário Oficial da União, Brasília, DF, 8 maio 2025a.

BRASIL. Ministério da Saúde. Gabinete do Ministro. **Portaria GM/MS nº 7.639, de 18 de julho de 2025.** Altera a Portaria de Consolidação GM/MS nº 1, de 28 de setembro de 2017. Diário Oficial da União, Brasília, DF, ed. 136, seção 1, p. 128, 22 jul. 2025b.

BRASIL. Ministério da Saúde. Secretaria de Atenção Primária à Saúde. Coordenação-Geral de Saúde da Família e Comunidade. **Nota Técnica nº 30/2025-CGESCO/DESCO/SAPS/MS** — Componente Vínculo e Acompanhamento Territorial. Brasília, DF: Ministério da Saúde, 23 set. 2025c. SEI nº 0049700833, processo nº 25000.178857/2024-41.

BRASIL. Ministério da Saúde. Secretaria de Atenção Primária à Saúde. **Nota Metodológica C7 — Cuidado da mulher e do homem transgênero na prevenção do câncer na Atenção Primária à Saúde.** Brasília, DF: Ministério da Saúde, 2026a. SEI nº 0054641718, processo nº 25000.137969/2025-22.

BRASIL. Ministério da Saúde. Gabinete do Ministro. **Portaria GM/MS nº 10.994, de 13 de maio de 2026.** Altera a Portaria GM/MS nº 3.493, de 10 de abril de 2024, para dispor sobre o período de implementação da metodologia de cofinanciamento federal do Piso de Atenção Primária à Saúde — APS no âmbito do Sistema Único de Saúde — SUS. Diário Oficial da União, Brasília, DF, ed. 89, seção 1, p. 1105, 14 maio 2026b.

BROOKS, M. E.; KRISTENSEN, K.; VAN BENTHEM, K. J. et al. glmmTMB balances speed and flexibility among packages for zero-inflated generalized linear mixed modeling. **The R Journal**, v. 9, n. 2, p. 378-400, 2017.

CAMPBELL, H. The consequences of checking for zero-inflation and overdispersion in the analysis of count data. **Methods in Ecology and Evolution**, v. 12, n. 4, p. 665-680, 2021.

CASTRO-NUNES, P. de; PALMIERI, P.; BELLAS, H.; SOARES, A.; VIANA, J.; CARVALHO, P. V. R. de; JATOBÁ, A. Effects of pay for performance in primary care in an under-registration scenario. **Revista de Saúde Pública**, v. 58, p. 44, 2024. DOI: 10.11606/s1518-8787.2024058005812.

COSTA-RIBEIRO, M. C. V.; KRAINSKI, E. T.; MELLO, A. M. et al. Dengue incidence following mass vaccination: an interrupted time series study in Paraná, Brazil. **Tropical Medicine and Infectious Disease**, v. 11, n. 1, art. 11, 2026.

DIAS, M. B. K.; ALCÂNTARA, L. L. M.; GIRIANELLI, V. R.; MIGOWSKI, A.; RIBEIRO, C. M.; TOMAZELLI, J. G. Rastreamento do câncer do colo do útero em mulheres de 25 a 64 anos: indicadores do primeiro exame citopatológico informado no Siscolo, 2007-2013. **Revista Brasileira de Cancerologia**, v. 68, n. 1, 2022. DOI: 10.32635/2176-9745.RBC.2022v68n1.1520.

DUARTE, M. B. O.; ARGENTON, J. L. P.; CARVALHEIRA, J. B. C. Impact of COVID-19 in cervical and breast cancer screening and systemic treatment in São Paulo, Brazil: an interrupted time series analysis. **JCO Global Oncology**, v. 8, e2100371, 2022.

EWUSIE, J. E.; THABANE, L.; BEYENE, J.; STRAUS, S. E.; HAMID, J. S. Multicenter interrupted time series analysis: incorporating within and between-center heterogeneity. **Clinical Epidemiology**, v. 12, p. 625-636, 2020.

FERREIRA, H. N. C.; CAPISTRANO, G. N.; MORAIS, T. N. B. et al. Screening and hospitalization of breast and cervical cancer in Brazil from 2010 to 2022: a time-series study. **PLOS ONE**, v. 18, n. 10, e0278011, 2023.

GREEN, P.; MACLEOD, C. J. SIMR: an R package for power analysis of generalized linear mixed models by simulation. **Methods in Ecology and Evolution**, v. 7, n. 4, p. 493-498, 2016.

HONE, T.; POWELL-JACKSON, T.; SANTOS, L. M. P. et al. Impact of the Programa Mais Médicos on primary care doctor supply and amenable mortality: quasi-experimental study of 5565 Brazilian municipalities. **BMC Health Services Research**, v. 20, supl. 2, art. 873, 2020.

HUDSON, J.; FIELDING, S.; RAMSAY, C. R. Methodology and reporting characteristics of studies using interrupted time series design in healthcare. **BMC Medical Research Methodology**, v. 19, art. 137, 2019.

INSTITUTO NACIONAL DE CÂNCER JOSÉ ALENCAR GOMES DA SILVA (INCA). **Diretrizes brasileiras para o rastreamento do câncer do colo do útero.** 2. ed. rev. atual. Rio de Janeiro: INCA, 2016. 114 p.

INSTITUTO NACIONAL DE CÂNCER (INCA). **Dados e números sobre câncer do colo do útero: relatório anual 2023.** Rio de Janeiro: INCA, out. 2023.

INSTITUTO NACIONAL DE CÂNCER (INCA). **Dados e números sobre câncer do colo do útero: relatório anual 2025.** Rio de Janeiro: INCA, 2025.

INSTITUTO NACIONAL DE CÂNCER (INCA). **Estimativa 2026: incidência de câncer no Brasil.** Rio de Janeiro: INCA, 2026.

LIU, W.; YE, S.; BARTON, B. A. et al. Simulation-based power and sample size calculation for designing interrupted time series analyses of count outcomes in evaluation of health policy interventions. **Contemporary Clinical Trials Communications**, v. 17, art. 100474, 2019.

LOPEZ BERNAL, J.; CUMMINS, S.; GASPARRINI, A. Interrupted time series regression for the evaluation of public health interventions: a tutorial. **International Journal of Epidemiology**, v. 46, n. 1, p. 348-355, 2017.

LOPEZ BERNAL, J.; CUMMINS, S.; GASPARRINI, A. The use of controls in interrupted time series studies of public health interventions. **International Journal of Epidemiology**, v. 47, n. 6, p. 2082-2093, 2018.

LOPEZ BERNAL, J.; CUMMINS, S.; GASPARRINI, A. Difference in difference, controlled interrupted time series and synthetic controls. **International Journal of Epidemiology**, v. 48, n. 6, p. 2062-2063, 2019.

LOPEZ BERNAL, J.; CUMMINS, S.; GASPARRINI, A. Corrigendum to: Interrupted time series regression for the evaluation of public health interventions: a tutorial. **International Journal of Epidemiology**, v. 50, n. 3, p. 1045, 2021.

MAIA, L. R.; CAMPOS, M. R.; CASTANHEIRA, D. Fiscal austerity and municipal health spending: an interrupted time series study. **Revista de Saúde Pública**, v. 58, art. 42, 2024.

MINCHIN, M.; ROLAND, M.; RICHARDSON, J.; ROWARK, S.; GUTHRIE, B. Quality of care in the United Kingdom after removal of financial incentives. **New England Journal of Medicine**, v. 379, n. 10, p. 948-957, 2018. DOI: 10.1056/NEJMsa1801495.

NASCIMENTO, M. I.; MASSAHUD, F. C.; BARBOSA, N. G.; LOPES, C. D.; RODRIGUES, V. C. Premature mortality due to cervical cancer: study of interrupted time series. **Revista de Saúde Pública**, v. 54, art. 139, 2020.

ORGANIZAÇÃO PAN-AMERICANA DA SAÚDE (OPAS/OMS); SECRETARIA ESTADUAL DE SAÚDE DE PERNAMBUCO (SES-PE). **Estado brasileiro de Pernambuco e OPAS lançam programa para prevenir e tratar câncer de colo de útero (Programa Útero é Vida).** Notícia institucional, 16 dez. 2021. [Lançamento em 15 dez. 2021.]

PINTO, R.; VALENTIM, R.; FERNANDES DA SILVA, L. et al. Use of interrupted time series analysis in understanding the course of the congenital syphilis epidemic in Brazil. **The Lancet Regional Health – Americas**, v. 7, art. 100163, 2022.

RAMÍREZ, A. T.; VALLS, J.; BAENA, A. et al. (ESTAMPA study group). Performance of cervical cytology and HPV testing for primary cervical cancer screening in Latin America: an analysis within the ESTAMPA study. **The Lancet Regional Health – Americas**, v. 26, 100593, 2023. DOI: 10.1016/j.lana.2023.100593.

RASELLA, D.; AQUINO, R.; SANTOS, C. A. T.; PAES-SOUSA, R.; BARRETO, M. L. Effect of a conditional cash transfer programme on childhood mortality: a nationwide analysis of Brazilian municipalities. **The Lancet**, v. 382, n. 9886, p. 57-64, 2013.

RIBEIRO, C. M.; CLARO, I. B.; TOMAZELLI, J. G.; DIAS, M. B. K. Rastreamento do câncer do colo do útero no Brasil: análise da cobertura a partir do Sistema de Informação do Câncer. **Cadernos de Saúde Pública**, v. 41, n. 8, e00152224, 2025. DOI: 10.1590/0102-311XPT152224.

RIBEIRO, C. M.; CORRÊA, F. M.; MIGOWSKI, A. Efeitos de curto prazo da pandemia de COVID-19 na realização de procedimentos de rastreamento, investigação diagnóstica e tratamento do câncer no Brasil: estudo descritivo, 2019-2020. **Epidemiologia e Serviços de Saúde**, v. 31, n. 1, e2021405, 2022. DOI: 10.1590/S1679-49742022000100010.

RIEBLER, A.; SØRBYE, S. H.; SIMPSON, D.; RUE, H. An intuitive Bayesian spatial model for disease mapping that accounts for scaling. **Statistical Methods in Medical Research**, v. 25, n. 4, p. 1145-1165, 2016.

RUSSO, L. X.; POWELL-JACKSON, T.; MAIA BARRETO, J. O. et al. Pay for performance in primary care: the contribution of the Programme for Improving Access and Quality of Primary Care (PMAQ) on avoidable hospitalisations in Brazil, 2009-2018. **BMJ Global Health**, v. 6, n. 7, e005429, 2021.

SILVA, E. G. A.; LIMA, D. M.; MEIRA, B. S.; COSTA, D. N. Rastreamento do câncer de colo do útero na Bahia: avaliação da cobertura, adesão, adequabilidade e positividade das citopatologias realizadas entre 2017 e 2021. **Revista Brasileira de Análises Clínicas**, v. 58, n. 1, 2023. DOI: 10.21877/2448-3877.202300059.

TOMAZELLI, J.; RIBEIRO, C. M.; DIAS, M. B. K. Cobertura dos sistemas de informação dos cânceres do colo do útero e de mama no Brasil, 2008-2019. **Revista Brasileira de Cancerologia**, v. 68, n. 1, e-121544, 2022. DOI: 10.32635/2176-9745.RBC.2022v68n1.1544.

TURNER, S. L.; KARAHALIOS, A.; FORBES, A. B. et al. Design characteristics and statistical methods used in interrupted time series studies evaluating public health interventions: a review. **Journal of Clinical Epidemiology**, v. 122, p. 1-11, 2020.

TURNER, S. L.; KARAHALIOS, A.; FORBES, A. B. et al. Creating effective interrupted time series graphs: review and recommendations. **Research Synthesis Methods**, v. 12, n. 1, p. 106-117, 2021a.

TURNER, S. L.; KARAHALIOS, A.; FORBES, A. B. et al. Comparison of six statistical methods for interrupted time series studies: empirical evaluation of 190 published series. **BMC Medical Research Methodology**, v. 21, art. 134, 2021b.

VON ELM, E.; ALTMAN, D. G.; EGGER, M. et al. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. **PLOS Medicine**, v. 4, n. 10, e296, 2007.

WAGNER, A. K.; SOUMERAI, S. B.; ZHANG, F.; ROSS-DEGNAN, D. Segmented regression analysis of interrupted time series studies in medication use research. **Journal of Clinical Pharmacy and Therapeutics**, v. 27, n. 4, p. 299-309, 2002.
