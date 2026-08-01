# Defasagem do eixo temporal e composição do desfecho

Medições feitas em 01/08/2026 contra `SISCAN/cito_colo_residpe.def`, mulheres de 25 a 64 anos,
Pernambuco, competências de 2018 a jun/2026 (2.610.409 exames antes da exclusão de ago e set/2022).

Respondem a dois apontamentos da banca avaliadora: o eixo temporal do desfecho (apontado como fatal
pelo epidemiologista) e a composição do desfecho por motivo do exame (apontado como grave).

## 1. Não existe data de coleta no TABNET agregado

As únicas variáveis temporais expostas pelo `.def` são:

| Variável | Campo | O que data |
|----------|-------|-----------|
| Mes/Ano competencia | `CO_ANO_MES_LIBERACAO` | liberação do laudo pelo prestador — **o eixo em uso** |
| Mes Resultado | `CO_ANO_MES_RESULTADO` | mês em que o laudo recebeu resultado |

A data da **coleta** — o ato que a política incentiva — não é exposta como dimensão de tabulação.
A recomendação da banca de adotá-la como eixo principal, caso existisse, não é executável pela via
agregada. Duas saídas permanecem abertas:

1. **Microdados CSV do SISCAN** no FTP do DATASUS (`/dissemin/publicos/SISCAN/SISCAN/`) trazem
   `CO_INTERVALO_COLETA`, `CO_INTERVALO_EXAME` e `CO_TEMPO_EXAME` por exame, o que permitiria
   reconstruir a data de coleta individualmente. Custo: cerca de 14 GB de transferência.
2. **Declarar a limitação e quantificar a defasagem**, que é o que as medições abaixo permitem.

## 2. A defasagem, medida

O `.def` expõe o intervalo entre coleta e recebimento no laboratório (`Interv Coleta`) e o tempo
total do exame (`Tempo Exame`). Distribuição para PE, mulheres de 25 a 64 anos, 2018–2026:

**Intervalo entre a coleta e o laboratório**

| Faixa | Exames | % |
|-------|--------|---|
| 0 a 10 dias | 1.806.781 | 69,2 |
| 11 a 20 dias | 450.803 | 17,3 |
| 21 a 30 dias | 169.300 | 6,5 |
| mais de 30 dias | 183.522 | 7,0 |
| ignorado | 3 | 0,0 |

**Tempo total do exame, da coleta à liberação do laudo**

| Faixa | Exames | % |
|-------|--------|---|
| até 30 dias | 1.424.209 | 54,6 |
| 31 a 60 dias | 905.839 | 34,7 |
| mais de 60 dias | 280.361 | 10,7 |

### O que isso significa para o desenho

**A defasagem mediana está entre 30 e 60 dias.** Pouco mais da metade dos exames é liberada em até
30 dias; 45,4% levam mais que isso, e 10,7% passam de 60 dias. A série datada por liberação está,
portanto, deslocada para a frente em relação ao ato de coleta por algo entre um e dois meses, com
uma cauda relevante.

Três consequências, todas a declarar no protocolo:

1. **Choques abruptos aparecem suavizados e atrasados.** O nadir da série de PE cai em jun/2020
   (1.576 exames), enquanto a literatura nacional documenta o nadir do rastreamento em mai/2020.
   A discordância de um mês é consistente com a defasagem medida e serve como estimativa empírica
   dela.
2. **Três dos marcos normativos caem em maio** (τ3 mai/2024, τ4 mai/2025, τ5 mai/2026). Se o efeito
   de uma mudança de incentivo sobre a coleta leva de um a dois meses para aparecer na competência
   de liberação, a mudança de nível estimada em τ é atenuada e parte do efeito vaza para o segmento
   seguinte.
3. **Análise de sensibilidade obrigatória**: reestimar com todos os τ deslocados em +1, +2 e +3
   competências. Se as estimativas mudarem de sinal ou de significância, o eixo temporal é o fator
   dominante e a conclusão precisa ser condicionada a ele.

## 3. Composição do desfecho por motivo do exame

O `.def` expõe `TP_MOTIVO_EXAME`, o que permite separar rastreamento de repetição e seguimento —
distinção que a banca cobrou, porque um desfecho de rastreio não deveria incluir exames de
acompanhamento de lesão já detectada.

| Motivo | Exames | % |
|--------|--------|---|
| Rastreamento | 2.561.489 | **98,1** |
| Seguimento | 44.185 | 1,7 |
| Repetição (exame alterado ASCUS/baixo grau) | 4.735 | 0,2 |

### O que isso significa

A contaminação é de **1,9%**. O desfecho agregado é, para efeitos práticos, uma série de
rastreamento. Isso enfraquece a crítica, mas não a dispensa: o correto é restringir o numerador a
`TP_MOTIVO_EXAME = Rastreamento` na especificação principal, porque a definição do desfecho é de
rastreio e porque a proporção de seguimento pode não ser estável ao longo da janela — se a detecção
de lesões aumentou, o seguimento aumenta junto, e essa parcela responde a um mecanismo diferente
do incentivo estudado.

O `pipeline.py` já expõe o parâmetro `motivo` em `baixa_siscan()`. Trocar a especificação principal
custa uma linha e uma recoleta de oito requisições.

**Verificação adicional recomendada**: tabular motivo × competência anual, para confirmar que a
proporção de 1,9% é estável e não cresce ao longo da janela. Se crescer, a restrição deixa de ser
refinamento e passa a ser necessária para evitar tendência espúria.

## 4. A defasagem não é constante — e isso é uma ameaça nova

Tabulação de `Tempo Exame` por ano de liberação, PE, mulheres de 25 a 64 anos:

| Tempo até a liberação | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026\* |
|---|---|---|---|---|---|---|---|---|---|
| até 30 dias | 58,9% | 59,0% | 62,7% | **65,7%** | 50,7% | **46,3%** | 53,0% | 47,4% | 49,8% |
| 31 a 60 dias | 29,7% | 30,2% | 28,5% | 27,2% | 39,3% | 41,2% | 36,0% | 41,6% | 35,0% |
| mais de 60 dias | 11,4% | 10,9% | 8,8% | **7,0%** | 10,0% | 12,5% | 11,0% | 11,0% | **15,2%** |

\* 2026 vai até junho e ainda não acumulou os laudos de liberação lenta.

**Há uma quebra entre 2021 e 2022.** A proporção de exames liberados em até 30 dias cai de 65,7%
para 50,7% — quinze pontos percentuais num único ano — e não volta ao patamar anterior. A cauda
acima de 60 dias mais que dobra entre 2021 e 2026, de 7,0% para 15,2%.

Isto é mais grave que a defasagem em si. A defasagem constante desloca a série inteira e é
absorvida por uma análise de sensibilidade que empurra os τ para frente. Uma defasagem **que muda
ao longo da janela** deforma a série de modo não uniforme: quando o processamento desacelera,
exames coletados no período são empurrados para competências posteriores, o que **deprime
artificialmente a competência corrente e infla a seguinte**. A tendência estimada entre τ2 e τ3
absorve essa deformação como se fosse variação de produção.

A quebra de 2021 para 2022 não coincide com nenhum marco normativo do estudo — τ3 é mai/2024 — o
que é uma sorte: ela não se confunde diretamente com um efeito de interesse. Mas cai dentro do
segmento que serve de base para extrapolar o contrafactual de τ3, e é justamente a inclinação desse
segmento que define o contrafactual contra o qual o efeito do Saúde Brasil 360 será medido.

### Onde está o gargalo: no laboratório, não no transporte

O `.def` expõe duas medidas temporais distintas, e compará-las localiza a etapa que desacelerou.
`Interv Coleta` mede da coleta até a chegada ao laboratório; `Tempo Exame` mede o percurso completo,
até a liberação do laudo.

Proporção com intervalo **coleta → laboratório** de até 10 dias, por ano de liberação:

| 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| 69,6% | 73,9% | 70,2% | 70,2% | 69,1% | 68,4% | 64,9% | 68,4% | 69,0% |

Essa etapa é **estável**. A logística de transporte da amostra não mudou de forma material em nove
anos. Como o tempo total caiu de 65,7% para 50,7% entre 2021 e 2022, a desaceleração está
inteiramente na etapa seguinte: o **processamento dentro do laboratório**.

Isso é útil por dois motivos. Primeiro, restringe a explicação: não é falha de coleta na atenção
primária nem de transporte, é capacidade laboratorial. Segundo, a covariável a construir fica mais
precisa — o que importa é o tempo de processamento, e ele é uma característica da rede de
laboratórios, não do comportamento das equipes de APS.

### Encaminhamento

1. **Incluir a composição do tempo de liberação como covariável variante no tempo** no nível
   município-competência, ou ao menos a proporção liberada em até 30 dias. Diferentemente da
   covariável de completude do SISCAN — que a banca rejeitou por endogeneidade, já que o numerador
   é o próprio desfecho —, esta é uma característica do **processamento laboratorial**, não do
   volume de exames, e não é função da variável dependente.
2. **Pré-especificar a análise de sensibilidade com a série datada por `CO_ANO_MES_RESULTADO`**,
   que é o eixo alternativo disponível na fonte agregada.
3. A reconstrução da data de coleta por exame, a partir dos microdados individuais, permanece como
   o desempate definitivo — mas **não é executável hoje**. O FTP do DATASUS entregou 12,5 KB/s na
   medição de 01/08/2026, o que dá 38 horas para um único ano-calendário e mais de 300 horas para a
   janela completa. O script `baixa_microdados.py` fica no repositório, é idempotente e retomável, e
   deve ser executado quando o servidor estiver responsivo, ou a partir de uma rede com melhor
   trânsito até o DATASUS. A via agregada acima responde à maior parte da pergunta a um custo de
   segundos.

## 5. O que ainda não foi medido

- Se a proporção de seguimento varia entre municípios de forma correlacionada com a capacidade
  laboratorial — o que faria a contaminação de 1,9% ser diferencial, não uniforme.
- Se a desaceleração de 2022 é homogênea entre municípios ou concentrada em alguns laboratórios.
  Se for concentrada, os municípios atendidos por eles têm séries deformadas de modo específico, e
  o efeito aleatório de município não basta para absorver isso — seria preciso um termo de
  laboratório, que a fonte agregada não expõe.
