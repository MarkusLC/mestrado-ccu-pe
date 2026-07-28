# Como Baixar Dados SISCAN de TABNET

## 🎯 Objetivo
Baixar dados reais de **SISCOLO** (câncer de colo de útero) para Pernambuco (PE) de **2018-2026** e processar em JSON para o dashboard.

## 📋 Passo a Passo

### 1️⃣ Acesse TABNET do Pernambuco

Abra em seu navegador:
```
https://tabnet.saude.pe.gov.br/
```

Ou acesse via portal DATASUS:
```
https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
```

### 2️⃣ Procure por SISCOLO/Câncer de Colo

Dentro do portal, você vai encontrar uma seção chamada:
- **"SISCOLO"** ou
- **"Câncer de Colo de Útero"** ou  
- **"Epidemiológicas e Morbidade"** → **"SISCOLO/SISMAMA"**

### 3️⃣ Configure a Tabulação

Na interface de consulta, configure:

**Linhas (Rows):**
- ✅ Município (município quer dizer "municipality")

**Colunas (Columns):**
- ✅ Ano/Mês (ou Year/Month)

**Períodos (Filter - Período):**
- ✅ De: 2018
- ✅ Até: 2026

**Unidade Federada (UF/State):**
- ✅ Selecione: **PE (Pernambuco)**

**Indicador/Procedimento:**
- ✅ **Citopatologia Cervical** (exames de citologia)

### 4️⃣ Exporte como CSV

Botão "Exportar" ou "Export":
- Formato: **CSV**
- Opção: **Com quebras de linha** (se oferecer)

### 5️⃣ Salve o Arquivo

Salve como:
```
data/siscan_manual.csv
```

Ou mova o arquivo baixado para essa pasta.

## ✅ Processe os Dados

Depois que o CSV estiver em `data/siscan_manual.csv`, execute:

```bash
pip install pandas
python3 fetch_tabnet_process.py
```

Isso vai gerar:
- `data/siscan_agregado.json` — dados agregados
- `data/siscan_summary.json` — sumário (total, período, etc)

## 📊 Resultado Esperado

O arquivo `siscan_agregado.json` deve ter este formato:

```json
[
  {
    "municipio": "Recife",
    "ano_mes": "2024-07",
    "exames": 1250
  },
  {
    "municipio": "Olinda",
    "ano_mes": "2024-07",
    "exames": 340
  },
  ...
]
```

## 🔄 Processo de Atualização

1. Você baixa o CSV manualmente **uma vez** (ou mensalmente)
2. Salva em `data/siscan_manual.csv`
3. Roda `fetch_tabnet_process.py`
4. Os JSON ficam prontos para o dashboard

Alternativamente, se quiser automatizar:
- GitHub Actions pode rodar o script após você fazer upload do CSV
- Ou você pode rodar mensalmente no seu próprio computador

## ❓ Dúvidas

**P: Por que não automático?**
- A: TABNET é uma interface web com muitos estados. Automação é frágil.

**P: Posso usar os dados antigos?**
- A: Sim, o dashboard mostra período, dados, e última atualização. Dados históricos são válidos.

**P: Qual é o formato exato do CSV?**
- A: TABNET exporta com:
  - Coluna 1: Município
  - Coluna 2: Ano-Mês (formato: 2024-07 ou 202407)
  - Coluna 3+: Valores numéricos (exames)

**P: Posso usar um ano só para testar?**
- A: Sim! Configure período 2024-2024 primeiro, teste, depois expanda para 2018-2026.
