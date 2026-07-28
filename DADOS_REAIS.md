# 🔴 COMO USAR DADOS REAIS DE SISCOLO

## O Problema

DATASUS (TABNET) **é uma interface web**, não uma API. Por isso:
- ❌ Não dá pra automatar 100% sem ser frágil
- ✅ Mas **dados reais agregados** dão pro download manual

## A Solução: Manual + Automação

### 1️⃣ Você Faz (Manual)

**Baixe CSV uma vez de TABNET:**

1. Acesse: https://tabnet.saude.pe.gov.br/
2. Procure: **SISCOLO** ou **Câncer de Colo de Útero**
3. Configure:
   - **Linhas:** Município
   - **Colunas:** Ano/Mês
   - **Período:** 2018-2026
   - **Estado:** PE
   - **Indicador:** Citopatologia Cervical
4. **Exporte:** CSV
5. **Salve em:** `data/siscan_manual.csv` (ou qualquer .csv na pasta `data/`)

### 2️⃣ GitHub Faz (Automático)

Quando você faz **push do CSV**:

```bash
git add data/siscan_manual.csv
git commit -m "Upload SISCAN CSV"
git push
```

**GitHub Actions roda automaticamente:**
- ✅ Processa CSV
- ✅ Gera JSON agregado
- ✅ Atualiza dashboard
- ✅ Faz commit dos dados processados

### 3️⃣ Dashboard Fica Vivo

O arquivo `data/siscan_agregado.json` alimenta:
- 📊 Gráficos (Plotly)
- 📈 Série temporal
- 🗺️ Municípios
- 📋 Metodologia

## 🚀 Workflow Completo

```
Manual (você)          Automático (GitHub)
    ↓                         ↓
Baixa CSV TABNET    →    Roda fetch_tabnet_process.py
    ↓                         ↓
Salva em data/      →    Gera JSON agregado
    ↓                         ↓
git push            →    Commit dos JSON
                         ↓
                    Dashboard já mostra novos dados!
```

## 📌 Arquivos-chave

| Arquivo | Você Cria | GitHub Cria |
|---------|-----------|------------|
| `data/siscan_manual.csv` | ✅ Download de TABNET | — |
| `data/siscan_agregado.json` | — | ✅ Processado |
| `data/siscan_summary.json` | — | ✅ Metadados |
| `fetch_tabnet_process.py` | — | ✅ Script (no repo) |

## ✅ Primeiro Teste

```bash
# 1. Baixe CSV manualmente (acima)
# 2. Salve como data/siscan_manual.csv
# 3. Execute localmente:

python3 fetch_tabnet_process.py

# Resultado esperado:
# ✅ data/siscan_agregado.json
# ✅ data/siscan_summary.json
```

## 🔄 Atualizações Periódicas

- **Mensalmente:** Baixe novo CSV de TABNET
- **Push:** `git push` → GitHub Actions processa automaticamente
- **Dashboard:** Atualiza com novos dados

## ❓ FAQ

**P: Preciso fazer isso todo mês?**
- A: Sim, se quiser dados sempre atualizados. Ou quando quiser.

**P: Pode ser ano todo junto?**
- A: Sim! Baixe período 2018-2026, salve, processa tudo.

**P: Se algo der errado no GitHub Actions?**
- A: Execute localmente: `python3 fetch_tabnet_process.py`

**P: Já temos dados "fake" no repo?**
- A: Sim, em `data/siscan_*.json`. Quando você subir um CSV real, substitui automaticamente.

## 🎯 Resumo para Mestrado

- ✅ Dados **reais de DATASUS**
- ✅ Processo **reproduzível** (está no repo)
- ✅ Dashboard **sempre atualizado**
- ✅ GitHub Pages **público e gratuito**
- ✅ Pipeline **completamente automatizada** após o push do CSV

É isso. Nada de fake data. Dados vivos.
