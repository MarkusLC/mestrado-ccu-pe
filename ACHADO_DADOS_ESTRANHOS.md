# 🚨 Achado: Dados da Série Temporal Estavam Estranhos

## O Problema

Quando você questionou "da onde bem os dados da serie temporal, pq estranho" — você tava CERTO.

Os dados que o script `expand_siscan_full.py` extraiu eram **duplicados/não-variáveis**:

```
Afrânio:    74 exames (2018-2026 idêntico)
Arcoverde: 258 exames (2018-2026 idêntico)
Caruaru:    80 exames (2018-2026 idêntico)
```

## Por que aconteceu?

O script fazia **1 query por ANO** (janeiro/2018, janeiro/2019, etc).

Mas TABNET **não diferencia mês-a-mês** — quando você pede "janeiro/2018", ele retorna dados AGREGADOS do período todo.

Resultado: mesmos dados repetidos 9 vezes.

## A Solução Real

Criado novo script: **`expand_siscan_mensal.py`**
- Faz queries **MÊS POR MÊS** (não anuais)
- Pega dados de jan/2018 até jun/2026
- Captura variação temporal **REAL**

## Dados Esperados Agora

```json
{
  "municipio": "Recife",
  "ano": "2026",
  "ano_mes": "2026-06",
  "exames": 2805
},
{
  "municipio": "Recife", 
  "ano": "2026",
  "ano_mes": "2026-05",
  "exames": 2750
}
```

Agora **cada mês diferente = dados diferentes** (série temporal real).

## Status

✅ Achado identificado  
⏳ Novo script rodando (`expand_siscan_mensal.py`)  
📊 Dashboard será atualizado com dados reais  

## Lição

Validar os dados é CRÍTICO. A série "lisa" deveria ter acusado algo errado desde o início.
