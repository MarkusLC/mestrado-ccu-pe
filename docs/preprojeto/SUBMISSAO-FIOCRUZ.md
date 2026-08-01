# IDENTIFICAÇÃO

**Candidata:** [preencher: nome completo, conforme documento de identidade]

**Programa:** Pós-Graduação em Saúde Pública — Mestrado Acadêmico (PPGSP/IAM/Fiocruz PE), turma 2027

**Área de concentração:** Políticas de Saúde

**Linha de pesquisa:** Avaliação de sistemas, programas e serviços de atenção e vigilância da saúde

**Orientador(a) pretendido(a):** [preencher: nome constante da relação do item 4.4 do edital]

**Título:** Produção de exames citopatológicos do câncer do colo do útero nos municípios de Pernambuco durante a transição Previne Brasil → Saúde Brasil 360: estudo ecológico de séries temporais interrompidas

---

# RESUMO

**Introdução.** O câncer do colo do útero é evitável em todos os elos de sua cadeia causal, mas persiste como quarta causa de morte por câncer em mulheres brasileiras. A coleta do citopatológico cabe à Atenção Primária, cujo financiamento federal foi reorganizado duas vezes em cinco anos, sem avaliação contrafactual. **Objetivo.** Estimar mudanças de nível e de tendência na produção mensal municipal de exames de rastreamento em mulheres de 25 a 64 anos em Pernambuco, associadas aos marcos normativos da transição, e documentar a intensidade efetiva da exposição a incentivo. **Métodos.** Séries temporais interrompidas em painel das 185 unidades municipais do estado, de 2018 a 2026, com extensão confirmatória a 2027. Desfecho do SISCAN, independente do sistema que aciona o pagamento. Modelo misto binomial negativo, offset log(população-alvo/36), efeitos aleatórios de município e de competência, AR(1) e Fourier. Estimando primário: maio de 2024, quando a revogação do Previne Brasil retira o incentivo. Reporte por STROBE e RECORD. **Resultados esperados.** Razões de taxas por marco, déficit acumulado, heterogeneidade municipal e matriz de (in)comparabilidade entre indicador nº 4 e C7 — todo efeito sendo produção, não cobertura.

**Palavras-chave:** Neoplasias do Colo do Útero; Detecção Precoce de Câncer; Atenção Primária à Saúde; Financiamento da Assistência à Saúde; Análise de Séries Temporais Interrompidas.

---

# 1 INTRODUÇÃO

O câncer do colo do útero é evitável em todos os elos de sua cadeia causal: há agente etiológico conhecido, imunização eficaz, lesão precursora detectável por exame barato e cura na fase pré-invasiva (INCA, 2016). Ainda assim, estimam-se 19.310 casos novos por ano em 2026-2028 e 6.983 óbitos em 2022 (INCA, 2025; INCA, 2026), com a maior carga no Norte e no Nordeste (INCA, 2026) e tendência secular de mortalidade em ascensão apenas nesta última macrorregião, entre 1980 e 2021 (FERRARI et al., 2025).

O determinante proximal é organizacional. O rastreamento é oportunístico, e o desperdício é mensurável: em 2021-2023 a cobertura nacional entre mulheres de 25 a 64 anos foi de 35,6%, contra razão de 47,4 exames por 100 mulheres, e a mesma produção redirecionada chegaria a 53,9% (RIBEIRO et al., 2025). A consequência aparece no estadiamento: metade dos diagnósticos em estádios III ou IV (INCA, 2025).

O financiamento federal da Atenção Primária foi reorganizado duas vezes em menos de um ciclo de gestão. A Portaria GM/MS nº 2.979/2019 instituiu capitação ponderada e pagamento por desempenho, no qual o rastreamento era o indicador nº 4, com meta de 40%, peso 1 em 10 e janela de 36 meses (BRASIL, 2022a). A Portaria GM/MS nº 3.493/2024 revogou o Previne Brasil (art. 7º, IV), com efeitos desde maio de 2024 (BRASIL, 2024a); a Portaria GM/MS nº 6.907/2025 incorporou os indicadores de qualidade (BRASIL, 2025a), e o rastreamento virou a boa prática (A) do C7, com 20 de 100 pontos, um de sete indicadores do componente (BRASIL, 2026a).

O sinal financeiro é fraco: sob o Previne Brasil, o máximo mensal por equipe atribuível ao desempenho em citologia era da ordem de R$ 322,50; sob o novo modelo, a fração do componente de qualidade sensível à citologia é de cerca de 2,9%. Acresce que, na janela deste estudo, **o C7 nunca carregou risco financeiro de perda**: a classificação "bom" foi garantida até o primeiro quadrimestre de 2026 e, no segundo, só equipes "ótimo" recebem valor diferenciado, com implementação integral a partir de 2027 (BRASIL, 2026b). As condições associadas a resposta forte — pagamento ao prestador, alta frequência, poucos indicadores — faltam ao arranjo brasileiro (GURGEL et al., 2023). Não há estudo quase-experimental sobre o Previne Brasil e, sobre o modelo de 2024, há apenas um ensaio sobre repasses (TOCCILLO et al., 2025). A escassez é ela própria objeto de investigação: numerador, denominador, fonte e público-alvo mudaram de uma vez (BRASIL, 2022a; BRASIL, 2026a), sem tabela de equivalência.

# 2 JUSTIFICATIVA

Este projeto não reivindica ineditismo temático: Cella, Correa e Barancelli (2025) já trataram da cobertura do citopatológico sob o Previne Brasil, em corte transversal restrito ao Sul e ao Sudeste. A contribuição é de **desenho**, ao estimar mudanças de nível e de tendência em marcos datados, com contrafactual explícito; de **unidade de análise**, mensal e municipal; de **fonte**, ao usar contagens do SISCAN com offset demográfico independente, contra um indicador de numerador subnotificado (CASTRO-NUNES et al., 2024) e denominador movido pelo próprio incentivo (SELLERA et al., 2023); e de **recorte**, ao deslocar a análise para o Nordeste e alcançar 2024.

Pernambuco tem incidência ajustada estimada de 11,96 por 100 mil, inferior à nacional de 14,76, e mortalidade ajustada de 6,23 em 2022, superior à nordestina (5,94) e à nacional (4,79) (INCA, 2025; INCA, 2026). Menor incidência com maior mortalidade é a assinatura de detecção tardia e de falha nos elos posteriores do cuidado, corroborada por apenas 51,54% de laudos liberados em até 30 dias (INCA, 2023). Somam-se cobertura de 32,5%, contra 35,6% no país (RIBEIRO et al., 2025), e 27% dos municípios acima de 5% de insatisfatoriedade, o maior percentual nacional (INCA, 2023). O estado abriga ainda, desde 2021, programa de rastreamento organizado em nove municípios, sem avaliação publicada, avaliável pelo desenho proposto.

---

# 3 PERGUNTAS CONDUTORAS, PREMISSA NORMATIVA E HIPÓTESES

**Perguntas condutoras.** (i) Em que medida a razão mensal de exames citopatológicos de rastreamento por população-alvo feminina de 25 a 64 anos anualizada — dividida por três, conforme a Resolução CIT nº 2/2016 (BRASIL, 2016) — muda de nível e de tendência nos marcos da transição Previne Brasil → Saúde Brasil 360, nas 185 unidades municipais de Pernambuco entre 2018 e 2026? (ii) Como essas mudanças se distribuem entre os municípios, e a que características municipais se associam? (iii) O indicador nº 4 do Previne Brasil e a boa prática (A) do C7 são comparáveis a ponto de permitirem leitura contínua do rastreamento na transição?

**Premissa normativa P1**, documental e não testada: na janela, nenhum município esteve exposto a risco financeiro de perda por desempenho em rastreamento, pois a implementação integral do componente de qualidade só começa em 2027 (BRASIL, 2026b). H2 a H4 são condicionais a P1, e todas as hipóteses tratam de **produção**, não de cobertura.

**H1 — bloco τ1–τ2, com retomada em τ2b.** Espera-se redução abrupta e de grande magnitude no nível, com recuperação parcial. Os marcos entram como bloco único, por não serem separáveis, e a queda **não** é atribuída ao Previne Brasil: o padrão é compatível com efeito pandêmico (RIBEIRO; CORRÊA; MIGOWSKI, 2022).

**H2 — τ3: retirada de incentivo.** A revogação extingue o pagamento por desempenho sobre o indicador nº 4 sem substituto, e a retirada produz efeitos maiores e mais persistentes que a introdução (MINCHIN et al., 2018; HO et al., 2025). Espera-se mudança de **sinal negativo, maior que em τ4 e τ5** — única hipótese direcional forte, e falsificável: efeito nulo indicaria que o incentivo jamais foi operante.

**H3 — τ4: mensuração sem consequência financeira.** Espera-se efeito nulo ou desprezível, pois maio de 2025 inicia a apuração do C7, não a exposição financeira a ele. Efeito nulo é informativo, mas não distingue ausência de resposta de resposta eficiente: o numerador do C7 é de pessoas, e o desfecho, de eventos.

**H4 — τ5: exposição unilateral na margem.** Espera-se efeito baixo e, se existente, positivo: há ganho potencial para equipes "ótimo" e nenhum risco de perda (BRASIL, 2026b), com resposta esperada concentrada nos municípios próximos ao corte de classificação, gradiente estimável se as classificações do C7 por equipe estiverem publicadas no e-Gestor APS. **τ5 é estimado apenas como mudança de nível, sem mudança de tendência, e é declaradamente exploratório.**

**H5 — τ6: único regime de risco bilateral.** Na extensão confirmatória, espera-se efeito superior ao de τ4 e τ5; o contraste entre incentivo de baixa intensidade e risco bilateral é o teoricamente informativo do estudo.

**H6 — heterogeneidade.** Espera-se variabilidade entre municípios na queda pandêmica e na mudança de nível em τ3, associada a porte, cobertura de ESF e região.

---

# 4 OBJETIVOS

**Geral.** Estimar as mudanças de nível e de tendência na razão mensal de exames citopatológicos de rastreamento em mulheres de 25 a 64 anos, por município de residência, nas 185 unidades municipais de Pernambuco entre 2018 e 2026, associadas aos marcos da transição Previne Brasil → Saúde Brasil 360, à luz da intensidade efetiva da exposição a incentivo documentada.

**Específicos.** (1) Descrever a série mensal municipal, com sazonalidade, sobredispersão, autocorrelação e composição por motivo. (2) Estimar as mudanças de nível e de tendência nos blocos τ1–τ2 (com retomada em τ2b), τ3 e τ4, e a de nível em τ5, exploratória, em razões de taxas com intervalos de 95%, sendo o estimando primário o par (δ₃, γ₃), e quantificar por segmento a diferença entre produção observada e contrafactual. (3) Estimar e mapear a variância entre municípios das mudanças de nível em τ3, e sua associação com porte, cobertura de ESF e região. (4) Estimar a discordância entre os volumes do SISCAN e do SIA/SUS nos marcos, condição para atribuir efeito à oferta e não ao registro. (5) Construir a matriz de (in)comparabilidade entre o indicador nº 4 e o C7. (6) Avaliar a robustez por sensibilidades e falsificações congeladas antes da coleta.

---

# 5 METODOLOGIA

**5.1 Delineamento e unidade.** Estudo ecológico de séries temporais interrompidas em painel municipal, com componente documental comparativo. Como a regra incide sobre todos os municípios ao mesmo tempo, não há unidades não expostas: diferenças-em-diferenças e controle sintético estão descartados, e o pré-intervenção é o contrafactual (WAGNER et al., 2002; LOPEZ BERNAL; CUMMINS; GASPARRINI, 2017, 2018). Como o indicador de interrupção é idêntico para as 185 unidades (EWUSIE et al., 2020), a identificação dos efeitos permanece ancorada no comprimento da série, não no produto N×T: o painel compra estrutura e heterogeneidade, não graus de liberdade sobre a exposição. A unidade é o município de residência observado mensalmente; a população de referência são mulheres de 25 a 64 anos (INCA, 2016; BRASIL, 2016).

**5.2 Período e marcos.** Janela principal de janeiro de 2018 a dezembro de 2026, 108 competências, 24 delas anteriores ao primeiro marco, com extensão confirmatória a dezembro de 2027. Os marcos são pré-especificados (TURNER et al., 2021) e datados pela competência de produção de efeitos, distinguindo vigência, apuração e repasse. São: **τ1** (jan/2020), capitação ponderada e indicador nº 4, único marco sem âncora normativa própria de efeitos financeiros; **τ2** (mar/2020), emergência sanitária; **τ2b** (jan/2021), **ponto de recuperação epidemiológica e não marco normativo** (RIBEIRO; CORRÊA; MIGOWSKI, 2022), sem atribuição de efeito de política; **τ3** (mai/2024), retirada de incentivo e estimando primário; **τ4** (mai/2025), mensuração do C7 e não exposição financeira a ele; **τ5** (mai/2026), implantação parcial, **estimado somente como mudança de nível, sem mudança de tendência, e declaradamente exploratório**; e **τ6** (jan/2027), risco bilateral, na extensão confirmatória. τ1 e τ2 distam dois meses e são quase colineares: entram como bloco único ancorado em τ1, e o estudo **não** separa o efeito do Previne Brasil do da pandemia. Como um par único de parâmetros não descreveria o V pandêmico, τ2b é acrescentado a priori, para que o contrafactual de τ3 não extrapole um segmento mal ajustado.

**5.3 Fontes, desfecho e denominador.** O desfecho vem do SISCAN, por TABNET/DATASUS, que não alimenta a aferição do pagamento, feita em outros sistemas (BRASIL, 2022a; BRASIL, 2026a): usar a base que aciona o pagamento tornaria qualquer efeito indistinguível de mudança de registro (MINCHIN et al., 2018; CASTRO-NUNES et al., 2024).

*Defasagem entre coleta e liberação do laudo.* O campo de competência é a data de liberação do laudo: a série é datada pelo laboratório, não pela atenção primária, e apenas 51,54% dos laudos saíram em até 30 dias em 2022 (INCA, 2023). A discordância entre o nadir nacional por data de atendimento, maio de 2020 (RIBEIRO; CORRÊA; MIGOWSKI, 2022), e o desta série, junho de 2020, estima a defasagem em cerca de um mês. Como três dos quatro marcos caem em maio, a ameaça atinge o estimando: o efeito de maio de 2024 pode refletir a fila do laboratório em abril. Sensibilidade desloca todos os τ em +1, +2 e +3.

O **desfecho primário** é a contagem mensal de exames com motivo "rastreamento" em mulheres de 25 a 64 anos, por município de residência; repetição e seguimento respondem à coleta insatisfatória e ao gargalo diagnóstico, não ao incentivo. O parâmetro de interesse é a razão dessa contagem pela população-alvo anualizada, como offset **log(N/36)**, em que **36 é a operacionalização mensal do fator de divisão 3 da Resolução CIT nº 2/2016**; a escolha entre /3 e /36 desloca apenas o intercepto e não altera efeito algum. São secundários os exames fora da faixa-alvo, de repetição, de seguimento e com HSIL+; o denominador é interpolado para competência mensal.

*Contagem de exames não é cobertura.* A razão de exames tem numerador de eventos e denominador de pessoas; a cobertura tem ambos de pessoas (DIAS et al., 2022; RIBEIRO et al., 2025). **Todo efeito estimado é resposta de produção de exames, não ganho de cobertura populacional nem proteção contra o câncer invasor.** Elevação da razão é compatível com captação de nunca rastreadas, que aumenta cobertura, e com encurtamento de intervalo em já rastreadas, que não aumenta; sem desduplicação por mulher, a ambiguidade é irredutível.

**5.4 Processamento e especificação.** O zero-fill contra frame canônico repõe a linha do município que zera, omitida pelo TABNET: sem ela, o zero vira dado faltante, viés para cima máximo no período pandêmico e portanto correlacionado com as interrupções.

A especificação é um modelo misto binomial negativo NB2 da contagem mensal, com offset log(N/36), intercepto e tendência basais, um par de nível e tendência por bloco — com o de tendência de τ5 imposto igual a zero — e harmônicos de Fourier. A estrutura aleatória tem três camadas: intercepto e inclinação por município; AR(1) intramunicipal, especificada a priori; e, decisivamente, **um efeito aleatório de competência, v_t, compartilhado por todos os municípios**. Como o indicador de interrupção é idêntico para as 185 unidades, qualquer choque estadual comum não modelado moveria os resíduos de todos na mesma direção, e **um modelo que os supusesse condicionalmente independentes leria um único choque estadual como 185 evidências independentes**; é v_t que impede essa leitura, e por isso se reportam também erros-padrão por wild cluster bootstrap no nível da competência.

As mudanças de tendência acumulam-se, e reporta-se a soma vigente em cada segmento. A NB2 é pré-especificada por sobredispersão (BROOKS et al., 2017) e, como testes preliminares inflam falsos positivos (CAMPBELL, 2021), famílias alternativas entram só como sensibilidade. A sazonalidade por harmônicos é crítica, pois três marcos caem em maio (DUARTE et al., 2022).

**5.5 Poder e série-controle.** O poder é avaliado por simulação **com v_t ativo**, sem o qual as curvas ficariam otimistas. A mamografia foi descartada como controle, pois o C7 agrega colo e mama na mesma fórmula (BRASIL, 2026a); o controle é por característica da população — exames fora da faixa-alvo —, com viés anticonservador no cenário nulo.

**5.6 Componente documental, vieses e reprodutibilidade.** O componente documental confronta, nas fontes normativas primárias, numerador, denominador, faixa etária, janela, sistema e valor em risco por equipe dos dois indicadores, em dupla conferência. A subnotificação por implantação incompleta do SISCAN é a ameaça mais grave: se a cobertura do sistema cresceu na janela, parte da tendência ascendente é artefato de consolidação (TOMAZELLI; RIBEIRO; DIAS, 2022), talvez da ordem do efeito procurado no bloco pandêmico. A razão entre canais de registro **não** entra no preditor, por endogeneidade — seu numerador é o próprio desfecho —, e é reportada como teste de falsificação; mitiga-se restringindo o painel a municípios com produção estável. Conversão ao DNA-HPV, cointervenção estadual e não separabilidade de τ1 e τ2 completam as ameaças declaradas. O reporte segue o STROBE (VON ELM et al., 2007) e o RECORD (BENCHIMOL et al., 2015), com repositório público. O protocolo, com interrupções-placebo em maio de 2019, 2022 e 2023, é congelado antes da extração; a pré-especificação é anterior ao ajuste de qualquer modelo, não à visualização dos dados.

**5.7 Aspectos éticos.** O estudo usa apenas dados secundários agregados, públicos e sem identificação individual, sem contato com participantes nem *linkage*, e enquadra-se em tese na hipótese de não registro e não avaliação do art. 1º, parágrafo único, da Resolução CNS nº 510/2016. **A dispensa não será presumida.** Conduta declarada: consulta formal prévia ao CEP-IAM; reprodução integral da manifestação obtida, qualquer que seja o teor; e submissão via Plataforma Brasil se assim orientado ou se não houver manifestação em prazo. A extração de agosto de 2026 foi teste de acesso a dados públicos; a coleta de pesquisa é posterior ao parecer.

**5.8 Produtos.** Dois manuscritos em periódicos indexados de saúde coletiva em acesso aberto, um com as estimativas em painel e outro com a matriz de (in)comparabilidade; nota técnica à SES-PE e ao COSEMS-PE, com rotina reprodutível de extração, painel público municipal e critério para separar queda de produção de queda de registro, no 17º mês; e repositório de código.

---

# 6 VIABILIDADE

A etapa mais incerta de um estudo com dados secundários — obter e tratar os dados — já foi cumprida em agosto de 2026. Estão disponíveis 2.578.890 exames citopatológicos de mulheres de 25 a 64 anos, por município de residência, de 2018 a junho de 2026, cobrindo 100 das 108 competências; seis ausentes virão na coleta definitiva e duas são ausências de protocolo. O painel está montado, o denominador cobre 100% das células do offset e a série-controle já existe. O sinal é mensurável: a razão anual cai de 0,405 em 2018 a 0,219 em 2020, sobe a 0,423 em 2023 e cai a 0,342 em 2025. Não há dados identificados, convênio a firmar nem sujeitos a recrutar, e o ajuste é factível em equipamento pessoal.

**Aderência institucional.** O projeto se insere na linha *Avaliação de sistemas, programas e serviços de atenção e vigilância da saúde*, por avaliar a efetividade de um programa federal de indução financeira sobre um serviço de rastreamento oncológico com dados de sistemas nacionais de informação. As estruturas institucionais disponíveis bastam, pois o estudo não requer laboratório, campo nem convênio de cessão de dados.

---

# 7 CRONOGRAMA

Matrícula em fevereiro de 2027, integralização em 24 meses. **2027.1:** disciplinas obrigatórias; depósito do protocolo congelado; consulta ao CEP-IAM; levantamento documental — nenhuma extração de pesquisa antes da manifestação do comitê. **2027.2:** disciplinas eletivas e de produtos; coleta definitiva no segundo semestre, estratificada por motivo e resultado; análise exploratória e matriz de (in)comparabilidade; qualificação no 11º mês. **2028.1:** modelagem definitiva, sensibilidades e falsificação; extração de fechamento de 2027 para τ6; primeiro manuscrito no 15º mês e produto técnico no 17º. **2028.2:** revisão final; segundo manuscrito; oficina de devolução à SES-PE; defesa no 22º mês, depósito no 23º.

---

# REFERÊNCIAS

BENCHIMOL, E. I. et al. The RECORD Statement. **PLOS Medicine**, v. 12, n. 10, e1001885, 2015. DOI: 10.1371/journal.pmed.1001885.

BRASIL. Ministério da Saúde. Comissão Intergestores Tripartite. **Resolução nº 2, de 16 de agosto de 2016**: dispõe sobre os indicadores do processo nacional de pactuação interfederativa relativos ao ano de 2016. Anexo: Caderno de Diretrizes, Objetivos, Metas e Indicadores 2016, Indicador 5, p. 14-15. Brasília, DF, 2016. Disponível em: https://saude.rs.gov.br/upload/arquivos/201703/28151749-caderno-de-diretrizes-objetivos-metas-e-indicadores-2016.pdf. Acesso em: 1 ago. 2026.

BRASIL. Ministério da Saúde. **Nota Técnica nº 3/2022-DESF/SAPS/MS**: indicadores de pagamento por desempenho do Programa Previne Brasil. Brasília, DF, 2022a. Disponível em: https://www.conasems.org.br/wp-content/uploads/2022/01/NT-Alteracao-Indicadores-de-Desempenho-Previne-Brasil-1.pdf. Acesso em: 1 ago. 2026.

BRASIL. **Portaria GM/MS nº 3.493, de 10 de abril de 2024**. **DOU**, Brasília, DF, ed. 70, seção 1, p. 100, 11 abr. 2024a. Disponível em: https://bvsms.saude.gov.br/bvs/saudelegis/gm/2024/prt3493_11_04_2024.html. Acesso em: 1 ago. 2026.

BRASIL. **Portaria GM/MS nº 6.907, de 29 de abril de 2025**. **DOU**, Brasília, DF, 8 maio 2025a. Disponível em: https://bvsms.saude.gov.br/bvs/saudelegis/gm/2025/prt6907_08_05_2025.html. Acesso em: 1 ago. 2026.

BRASIL. Ministério da Saúde. **Nota Metodológica C7 — Cuidado da mulher na prevenção do câncer**. Brasília, DF, 2026a. Disponível em: https://www.gov.br/saude/pt-br/composicao/saps/publicacoes/fichas-tecnicas/equipe-de-atencao-primaria-e-saude-da-familia/nota-metodologica-c7-cuidado-da-mulher-na-prevencao-do-cancer. Acesso em: 1 ago. 2026.

BRASIL. **Portaria GM/MS nº 10.994, de 13 de maio de 2026**. **DOU**, Brasília, DF, ed. 89, seção 1, p. 1105, 14 maio 2026b. Disponível em: https://www.in.gov.br/web/dou. Acesso em: 1 ago. 2026.

BROOKS, M. E. et al. glmmTMB balances speed and flexibility among packages for zero-inflated GLMM. **The R Journal**, v. 9, n. 2, p. 378-400, 2017. DOI: 10.32614/RJ-2017-066.

CAMPBELL, H. The consequences of checking for zero-inflation and overdispersion in count data. **Methods in Ecology and Evolution**, v. 12, n. 4, p. 665-680, 2021. DOI: 10.1111/2041-210X.13559.

CASTRO-NUNES, P. de et al. Effects of pay for performance in primary care in an under-registration scenario. **Revista de Saúde Pública**, v. 58, p. 44, 2024. DOI: 10.11606/s1518-8787.2024058005812.

CELLA, E. N.; CORREA, L. D.; BARANCELLI, A. J. A análise da progressão da cobertura do citopatológico e da incidência de câncer de colo de útero pela implementação do Programa Previne Brasil. **Revista Brasileira de Medicina de Família e Comunidade**, v. 20, n. 47, art. 4480, 2025. DOI: 10.5712/rbmfc20(47)4480.

DIAS, M. B. K. et al. Rastreamento do câncer do colo do útero em mulheres de 25 a 64 anos: indicadores do Siscolo, 2007-2013. **Revista Brasileira de Cancerologia**, v. 68, n. 1, 2022. DOI: 10.32635/2176-9745.RBC.2022v68n1.1520.

DUARTE, M. B. O.; ARGENTON, J. L. P.; CARVALHEIRA, J. B. C. Impact of COVID-19 in cervical and breast cancer screening in São Paulo: an interrupted time series analysis. **JCO Global Oncology**, v. 8, e2100371, 2022. DOI: 10.1200/GO.21.00371.

EWUSIE, J. E. et al. Multicenter interrupted time series analysis. **Clinical Epidemiology**, v. 12, p. 625-636, 2020. DOI: 10.2147/CLEP.S241568.

FERRARI, Y. A. C. et al. Tendência secular de mortalidade por câncer do colo do útero no Brasil e regiões. **Ciência & Saúde Coletiva**, v. 30, n. 3, e09962023, 2025. DOI: 10.1590/1413-81232025303.09962023.

GURGEL, G. D. et al. Pay-for-performance for primary health care in Brazil: a comparison with England's Quality Outcomes Framework. **Health Policy**, v. 128, p. 62-68, 2023. DOI: 10.1016/j.healthpol.2022.11.004.

HO, L. et al. Effect of the UK Quality and Outcomes Framework on quality of primary care: systematic review. **BMJ**, v. 389, e083424, 2025. DOI: 10.1136/bmj-2024-083424.

INCA. **Diretrizes brasileiras para o rastreamento do câncer do colo do útero**. 2. ed. Rio de Janeiro: INCA, 2016. Disponível em: https://www.inca.gov.br/sites/ufu.sti.inca.local/files/media/document/diretrizesparaorastreamentodocancerdocolodoutero_2016_corrigido.pdf. Acesso em: 1 ago. 2026.

INCA. **Dados e números sobre câncer do colo do útero 2023**. Rio de Janeiro: INCA, 2023. Disponível em: https://www.inca.gov.br/sites/ufu.sti.inca.local/files/media/document/dados_e_numeros_colo_22marco2023.pdf. Acesso em: 1 ago. 2026.

INCA. **Controle do câncer do colo do útero no Brasil 2025**. Rio de Janeiro: INCA, 2025. Disponível em: https://ninho.inca.gov.br/jspui/handle/123456789/17304. Acesso em: 1 ago. 2026.

INCA. **Estimativa 2026: incidência de câncer no Brasil**. Rio de Janeiro: INCA, 2026. Disponível em: https://ninho.inca.gov.br/jspui/handle/123456789/17914. Acesso em: 1 ago. 2026.

LOPEZ BERNAL, J.; CUMMINS, S.; GASPARRINI, A. Interrupted time series regression for the evaluation of public health interventions. **International Journal of Epidemiology**, v. 46, n. 1, p. 348-355, 2017. DOI: 10.1093/ije/dyw098.

LOPEZ BERNAL, J.; CUMMINS, S.; GASPARRINI, A. The use of controls in interrupted time series studies. **International Journal of Epidemiology**, v. 47, n. 6, p. 2082-2093, 2018. DOI: 10.1093/ije/dyy135.

MINCHIN, M. et al. Quality of care in the United Kingdom after removal of financial incentives. **New England Journal of Medicine**, v. 379, n. 10, p. 948-957, 2018. DOI: 10.1056/NEJMsa1801495.

RIBEIRO, C. M. et al. Rastreamento do câncer do colo do útero no Brasil: análise da cobertura a partir do Sistema de Informação do Câncer. **Cadernos de Saúde Pública**, v. 41, n. 8, e00152224, 2025. DOI: 10.1590/0102-311XPT152224.

RIBEIRO, C. M.; CORRÊA, F. M.; MIGOWSKI, A. Efeitos de curto prazo da pandemia de COVID-19 no rastreamento e tratamento do câncer no Brasil, 2019-2020. **Epidemiologia e Serviços de Saúde**, v. 31, n. 1, e2021405, 2022. DOI: 10.1590/S1679-49742022000100010.

SELLERA, P. E. G. et al. Incentivo de capitação ponderada: impactos na evolução do cadastro populacional na APS. **Ciência & Saúde Coletiva**, v. 28, n. 9, p. 2743-2750, 2023. DOI: 10.1590/1413-81232023289.20142022.

TOCCILLO, G. L. et al. O novo modelo de alocação de recursos federais da APS 2024. **Saúde em Debate**, v. 49, n. 147, e10205, 2025. DOI: 10.1590/2358-2898202514710205P.

TOMAZELLI, J.; RIBEIRO, C. M.; DIAS, M. B. K. Cobertura dos sistemas de informação dos cânceres do colo do útero e de mama, 2008-2019. **Revista Brasileira de Cancerologia**, v. 68, n. 1, e-121544, 2022. DOI: 10.32635/2176-9745.RBC.2022v68n1.1544.

TURNER, S. L. et al. Comparison of six statistical methods for interrupted time series studies. **BMC Medical Research Methodology**, v. 21, art. 134, 2021. DOI: 10.1186/s12874-021-01306-w.

VON ELM, E. et al. The STROBE statement. **PLOS Medicine**, v. 4, n. 10, e296, 2007. DOI: 10.1371/journal.pmed.0040296.

WAGNER, A. K. et al. Segmented regression analysis of interrupted time series studies. **Journal of Clinical Pharmacy and Therapeutics**, v. 27, n. 4, p. 299-309, 2002. DOI: 10.1046/j.1365-2710.2002.00430.x.
