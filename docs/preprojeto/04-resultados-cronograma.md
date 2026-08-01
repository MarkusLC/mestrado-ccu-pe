# Resultados esperados, cronograma, orçamento e viabilidade

## 1. Resultados esperados

O estudo deve produzir quatro conjuntos de resultados, correspondentes aos objetivos específicos.

**1.1 Estimativas de mudança de nível e de tendência na produção de exames.** O produto analítico central é o conjunto de razões de taxas de incidência (IRR) com intervalos de confiança de 95%, estimadas por GLMM binomial negativo com efeitos aleatórios por município, estrutura AR1 intramunicipal e harmônicos de Fourier, para cada ponto de mudança declarado a priori: o bloco τ1–τ2 (Previne Brasil e emergência de saúde pública, jan.–mar. 2020, modelado conjuntamente por não separabilidade), τ3 (componente financeiro do novo modelo de cofinanciamento, maio de 2024), τ4 (incorporação dos indicadores de qualidade, maio de 2025) e τ5 (implantação parcial e assimétrica da qualidade, maio de 2026). Cada estimativa será acompanhada da série contrafactual projetada a partir do segmento anterior e da diferença absoluta acumulada entre exames observados e esperados, em número de exames — a métrica que interessa ao gestor. Espera-se, adicionalmente, a estimativa do déficit acumulado do choque pandêmico, cujo nadir já está caracterizado nos dados coletados (1.576 exames em junho de 2020, contra 23.593 em janeiro do mesmo ano).

**1.2 Estimativas estratificadas e teste da hipótese de penalização diferencial.** Termos de interação entre os pontos de mudança e características municipais (porte populacional, cobertura de Estratégia Saúde da Família, estrato do Indicador de Equidade e Dimensionamento, macrorregião de saúde) devem indicar se a resposta de produção foi homogênea ou se se concentrou nos municípios de maior capacidade administrativa. Esta é a lacuna 7 do dossiê e é o resultado de maior consequência distributiva.

**1.3 Matriz documental de (in)comparabilidade.** O componente de análise documental deve entregar uma matriz que confronte, dimensão a dimensão — denominação, numerador, códigos de procedimento aceitos, denominador, fonte de dados, granularidade de apuração, métrica, público-alvo e janela de acumulação —, três estados normativos do indicador de rastreamento: o indicador nº 4 original do Previne Brasil, sua redefinição pela Portaria GM/MS nº 102/2022 e a boa prática (A) do indicador C7. A matriz é o instrumento que sustenta a afirmação, hoje não publicada, de que não existe série comparável entre os dois modelos e de que nenhuma ponte de conversão foi divulgada pelo gestor federal.

**1.4 Caracterização da exposição efetiva ao incentivo.** Da auditoria normativa decorre um resultado que reorienta a interpretação de todo o restante: dentro da janela de janeiro de 2018 a dezembro de 2026, o indicador C7 nunca carregou risco financeiro de perda. A classificação "bom" foi garantida até o primeiro quadrimestre de 2026; no segundo quadrimestre de 2026 apenas as equipes classificadas como "ótimo" passaram a receber valor diferenciado; a implementação integral inicia-se no primeiro quadrimestre de 2027, fora da janela. O estudo, portanto, não estima o efeito do pagamento por desempenho do novo modelo — estima o efeito da mudança de arranjo de financiamento e de regime de mensuração, sob exposição a incentivo de baixa intensidade. A própria assimetria da implantação é achado relevante para a gestão e deve ser reportada como tal.

Todos os efeitos estimados são respostas de **produção** de exames, não de cobertura populacional. Sem desduplicação por mulher, permanece irredutível a ambiguidade entre captação de mulheres nunca rastreadas e repetição sobre as já rastreadas. Essa qualificação acompanhará cada resultado.

### 1.5 Produtos de disseminação

| Produto | Descrição | Prazo |
|---|---|---|
| Dissertação | Documento completo, redigido conforme STROBE e extensão RECORD | 2028.2 |
| Artigo original | Estimativas de ITS em painel municipal; alvo em periódico nacional de saúde coletiva ou de cancerologia indexado, em acesso aberto | Submissão até 2028.2 |
| Artigo/nota metodológica | Matriz de (in)comparabilidade entre os indicadores de rastreamento dos dois modelos | Submissão até 2028.2 |
| Produto técnico-tecnológico | Nota técnica com protocolo de monitoramento do rastreamento por fonte independente do sistema que aciona o pagamento, dirigida a gestores municipais e à SES-PE (exigência do mestrado profissional da UPE) | 2028.1 |
| Painel público de dados | Aplicação web com a série mensal de exames por município, razões por população-alvo, séries-controle e filtros por macrorregião e período; código e dados versionados em repositório público | Protótipo já operante; versão pública em 2028.1 |
| Repositório reprodutível | Código de extração, tratamento e modelagem, com dicionário de variáveis e registro de versões das extrações | Contínuo |

## 2. Contribuição esperada para a gestão

Para a **SES-PE**, o estudo entrega o que os instrumentos federais hoje não entregam: uma série municipal mensal de produção de exames, contínua ao longo de nove anos, imune às três rupturas de definição do indicador oficial, porque extraída de fonte que não alimenta a apuração do C7. Isso permite (i) identificar municípios cuja produção não recuperou o patamar pré-pandemia, distinguindo-os daqueles cujo indicador oficial apenas mudou de régua; (ii) dimensionar o déficit acumulado de exames em números absolutos, insumo direto para pactuação de metas na Comissão Intergestores Bipartite e para o planejamento da capacidade laboratorial; (iii) avaliar, com contrafactual, o programa estadual de rastreamento organizado em cooperação com a OPAS, que opera em Recife e em oito municípios desde dezembro de 2021 e não possui avaliação publicada; e (iv) antecipar quais municípios tendem a ser penalizados quando a implementação integral do componente de qualidade começar, em 2027 — precisamente o período em que o estudo estará em curso.

Para as **secretarias municipais**, o produto técnico oferece um procedimento de monitoramento local que não depende do desempenho de cadastro da equipe. A distinção entre queda de produção e queda de registro é operacionalmente decisiva: no primeiro caso a resposta é logística e assistencial; no segundo, é de qualificação do registro no sistema de informação da atenção primária. O painel público torna essa distinção verificável município a município, sem intermediação analítica.

## 3. Cronograma

Referência: ingresso em 2027 (matrícula em fevereiro, início das atividades em fevereiro na UPE e em março na Fiocruz), integralização em 24 meses.

| Semestre | Atividades |
|---|---|
| **2027.1** | Cumprimento das disciplinas obrigatórias (metodologia, epidemiologia, política e financiamento em saúde); consulta e, se for o caso, submissão ao CEP; **coleta definitiva** — reextração integral da série jan./2018–dez./2026 do SISCAN, com fechamento das oito competências pendentes de 2026, e reextração dos denominadores e das séries-controle; verificação de retroalimentação retroativa da base por comparação com a extração de 2026; consolidação da revisão de literatura |
| **2027.2** | Disciplinas eletivas e disciplina de desenvolvimento de produtos (UPE, 60 h); conclusão do levantamento documental normativo e construção da matriz de (in)comparabilidade; análise exploratória do painel, diagnósticos de sobredispersão, sazonalidade e autocorrelação; especificação e pré-registro do modelo; **exame de qualificação** |
| **2028.1** | Modelagem definitiva (ITS simples e ITS controlado por característica), análises estratificadas e análises de sensibilidade (deslocamento de τ1 para jan./2019, exclusão do período de transição pandêmico, censura da série a partir da difusão do teste molecular de HPV, especificações alternativas de offset); redação dos capítulos de resultados e discussão; **entrega do produto técnico** e publicação do painel; submissão do primeiro manuscrito |
| **2028.2** | Redação e revisão final da dissertação; submissão do segundo manuscrito; oficina de devolução dos resultados à SES-PE e a gestores municipais; **defesa**; depósito e correções |

O cronograma atende às duas exigências institucionais: 60 créditos com produto técnico-tecnológico obrigatório e produção técnico-científica com o orientador em até 20 meses, no caso do mestrado profissional da UPE; integralização em até 24 meses em regime presencial de tempo integral, no caso do mestrado acadêmico do IAM/Fiocruz.

## 4. Orçamento

**Declara-se que não há custo de coleta de dados.** Todas as fontes são públicas e de acesso irrestrito — TABNET/DATASUS para o desfecho e para as séries-controle, POPSVS/IBGE para os denominadores, Diário Oficial da União e repositórios do Ministério da Saúde para o corpus documental. Todo o processamento e a modelagem empregam software livre (R, glmmTMB, Quarto, Git), sem licenças. O equipamento computacional é próprio e suficiente. Não há trabalho de campo, entrevistas, deslocamento para coleta, contratação de auxiliares de pesquisa nem aquisição de bases restritas.

| Item | Especificação | Valor (R$) |
|---|---|---|
| Acesso a dados | Bases públicas; nenhuma taxa | 0,00 |
| Licenças de software | R, glmmTMB, Quarto, Git, Zotero, QGIS — todos livres | 0,00 |
| Infraestrutura computacional | Equipamento próprio; hospedagem do painel em serviço gratuito de páginas estáticas | 0,00 |
| Material de consumo | Papel, suprimentos de impressão, mídias, encadernação das vias da dissertação | 800,00 |
| Obtenção de documentos | Cópias de atos normativos, comutação bibliográfica, literatura sem acesso aberto | 400,00 |
| Participação em congresso nacional da área | Inscrição, passagem aérea, quatro diárias e alimentação | 4.900,00 |
| Participação em evento estadual/regional | Inscrição e deslocamento | 700,00 |
| Revisão de língua portuguesa e versão para o inglês | Um manuscrito | 2.500,00 |
| Taxa de processamento em acesso aberto (APC) | Contingência: os periódicos nacionais prioritários não cobram APC; a rubrica cobre a hipótese de submissão a periódico internacional | 3.000,00 |
| Oficina de devolução a gestores | Material de apoio e apoio logístico | 800,00 |
| Reserva técnica (10%) | — | 1.310,00 |
| **Total** | | **14.410,00** |

As despesas serão custeadas com recursos próprios, com possibilidade de apoio pelo Programa de Apoio à Pós-Graduação para a participação em eventos e para a publicação. Eventual concessão de bolsa não é pressuposto de execução: nenhuma rubrica do orçamento é condição para a produção dos resultados analíticos.

## 5. Viabilidade

A exequibilidade em 24 meses não é projeção: a etapa habitualmente mais incerta de um estudo com dados secundários — a obtenção e o tratamento dos dados — já foi executada e verificada, em agosto de 2026, na fase de elaboração deste projeto.

1. **Os dados já foram coletados.** Estão disponíveis 2.578.890 exames citopatológicos de mulheres de 25 a 64 anos, por município de residência, em Pernambuco, no período de janeiro de 2018 a junho de 2026, extraídos do TABNET/DATASUS por requisição programática sobre a definição `SISCAN/cito_colo_residpe.def` e conferidos dígito a dígito contra a interface pública. Cobrem-se 100 das 108 competências da janela; as oito restantes correspondem ao segundo semestre de 2026 e serão obtidas na coleta definitiva de 2027, quando estiverem consolidadas.

2. **O painel está montado e é completo.** As 185 unidades municipais de Pernambuco, incluído o Distrito Estadual de Fernando de Noronha, compõem painel balanceado, com preenchimento de zeros verdadeiros contra frame canônico do IBGE, o que elimina a confusão entre ausência de registro e ausência de produção.

3. **O denominador está resolvido.** A população feminina por município, ano e faixa quinquenal foi obtida do POPSVS (SVS/MS e IBGE), com cobertura de 100% das células necessárias ao offset log(população-alvo ÷ 3), cujo fator de divisão tem lastro na Resolução CIT nº 2, de 16 de agosto de 2016.

4. **As séries-controle já existem.** Foram coletados 571.866 exames citopatológicos em mulheres fora da faixa de 25 a 64 anos — o controle por característica adotado, por compartilhar o choque pandêmico e a via de oferta sem integrar o numerador de qualquer indicador de financiamento — e 976.947 mamografias na faixa de 50 a 69 anos, utilizáveis apenas até τ3, uma vez que a partir de maio de 2025 a mamografia passa a ser co-incentivada pelo mesmo indicador C7.

5. **A série tem sinal, e o sinal é mensurável.** A razão de exames por população-alvo varia de 0,405 em 2018 a 0,219 em 2020, com recuperação parcial a 0,423 em 2023 e nova queda a 0,342 em 2025. O colapso pandêmico está inteiramente capturado, com nadir de 93% em junho de 2020. A variação necessária para estimar mudanças de nível e de tendência está presente nos dados, o que remove o risco de um desenho sem potência.

6. **O pipeline é reprodutível.** A extração, o tratamento e a construção do painel estão codificados, versionados e documentados; a coleta definitiva de 2027 consiste em reexecutar o mesmo procedimento sobre a janela completa, e não em reconstruir o processo. O protótipo do painel público já opera sobre esses dados.

7. **Não há barreira de acesso nem de campo.** Não há dados identificados, nem acesso restrito a solicitar, nem convênio a firmar, nem instrumento a validar, nem sujeitos a recrutar. Ainda assim, e por não haver política pública explícita de dispensa para bases secundárias agregadas de acesso público, será feita consulta prévia ao comitê de ética da instituição de vínculo, com submissão para registro se assim for orientado — providência alocada em 2027.1, compatível com os prazos regimentais de conferência documental e emissão de parecer.

8. **O método está definido e é executável com os recursos disponíveis.** O ajuste de GLMM binomial negativo com efeitos aleatórios, estrutura AR1 e harmônicos de Fourier sobre painel de 185 unidades e 108 períodos é computacionalmente trivial em equipamento pessoal. O poder será avaliado por simulação a partir do próprio objeto ajustado, e não por pacote incompatível com a estrutura de covariância adotada.

Os riscos remanescentes são de interpretação, não de execução, e estão declarados nas limitações: não separabilidade de τ1 e τ2, difusão não observada do teste molecular de HPV a partir de 2026, cointervenção do programa estadual de rastreamento organizado e, sobretudo, a impossibilidade de converter contagem de exames em cobertura populacional.
