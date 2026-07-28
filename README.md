# Mestrado — Cobertura de Rastreamento do CCU em Pernambuco

**Estudo ecológico de série temporal: Previne Brasil → Saúde Brasil 360**

## 📊 O que é

Repositório que automatiza:

1. **Coleta de dados SISCAN** (citopatológico) via [microdatasus](https://github.com/rfsaldanha/microdatasus)
2. **Processamento e agregação** por município e mês (2018–2026)
3. **GitHub Actions** que roda automaticamente no dia 15 de cada mês
4. **Dashboard ao vivo** que consome os dados agregados em JSON

Tudo versionado, reprodutível e **completamente gratuito**.

---

## 🚀 Como funciona

### Fluxo Automático

```
GitHub Actions (cron 15º dia)
  ↓
fetch_siscan.R (R script)
  ↓
Puxa via microdatasus
  ↓
Processa + agrega JSON
  ↓
Faz commit + push automático
  ↓
Dashboard lê dados (raw.githubusercontent.com)
```

### Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `.github/workflows/update-siscan.yml` | GitHub Actions workflow (roda dia 15) |
| `fetch_siscan.R` | Script R que puxa + processa dados |
| `dashboard_mestrado.html` | Dashboard estático com Plotly.js |
| `data/siscan_agregado.json` | Dados agregados por município/mês |
| `data/siscan_summary.json` | Resumo: total, período, data |

---

## 📈 Dashboard

Acesse:  
👉 **[dashboard_mestrado.html](./dashboard_mestrado.html)** (abra no navegador)

Ou veja em tempo real (quando os dados são atualizados):  
👉 **[GitHub Pages](#)** (configurar em Settings → Pages)

### O que o dashboard mostra

- **📊 Resumo**: Total de exames, municípios, período coberto
- **📈 Série Temporal**: Gráfico mensal agregado de PE (2018–2026)
- **🗺️ Por Município**: Top 15 municípios por total de exames
- **🔬 Metodologia**: Delineamento, marcos temporais, links para documentação

---

## 🔧 Setup Local (Opcional)

Se quiser testar o script R localmente antes de fazer push:

```bash
# Instalar dependências R
install.packages(c('renv', 'jsonlite', 'dplyr', 'tidyr'))
remotes::install_github('rfsaldanha/microdatasus')

# Rodar script
Rscript fetch_siscan.R

# Resultado
# data/siscan_agregado.json (dados brutos agregados)
# data/siscan_summary.json (metadados)
```

---

## 📅 Agendamento

O workflow roda automaticamente:

- **Quando**: 15º dia de cada mês, às 12h UTC
- **O que**: Executa `fetch_siscan.R`, faz commit + push
- **Histórico**: Todos os commits ficam versionados (ver branch history)

**Trigger manual**: Você pode rodar manualmente em Actions → update-siscan → Run workflow

---

## 🔗 Documentação Completa

- **Parecer Metodológico**: [Google Docs](https://docs.google.com/document/d/1jcGEAaTNBLJEoX0DoEaFsomhho6ieFM1SUYsF-pD4sQ/edit)
- **Seção Métodos**: [Google Docs](https://docs.google.com/document/d/1wGtMpaSoXrTcrNe0BJx3CMJyICIFQW47-rFM7xCqO14/edit)
- **Dashboard Completo**: [HTML](./dashboard_mestrado.html)

---

## ⚠️ Limitações Conhecidas

1. **Lag natural**: DATASUS publica dados com ~30-60 dias de atraso
2. **Incompletude**: Nem todos os municípios alimentam o SISCAN
3. **Sem suporte oficial**: DATASUS não documenta acesso programático; workflow pode quebrar se layout do TabNet mudar
4. **Estrutura microdatasus**: O script assume estrutura SIA padrão; verificar output em caso de erro

---

## 📝 Para Dissertação

Este repositório é **reprodutível 100%**:

- ✅ Código R versionado
- ✅ Dependências em renv.lock
- ✅ Automação via GitHub Actions (sem setup manual)
- ✅ Dados e metadados versionados (git blame mostra datas exatas)

**Cite no apêndice:**

> Dados de rastreamento do câncer do colo do útero foram obtidos via SISCAN (DATASUS) usando o pacote R `microdatasus`. O pipeline de processamento e agregação está documentado no repositório GitHub: https://github.com/MarkusLC/mestrado-ccu-pe

---

## 🛠️ Troubleshooting

### "GitHub Actions falhou"

1. Vá em **Actions** → **update-siscan** → último run
2. Clique em **fetch-and-commit**
3. Veja o log de erro em **Run R dependencies**

### "Dashboard mostra 'Dados ainda não disponíveis'"

- Primeira execução do Actions? Espere até o dia 15, ou dispare manualmente em Actions → Run workflow
- GitHub Actions demora ~2-3 min para executar

### "JSON não carrega"

- Os dados só aparecem **após o primeiro push** do Actions
- Aguarde ~5 min depois de um run bem-sucedido

---

## 📄 Licença

Dados públicos (DATASUS). Código em repositório público.

---

**Última atualização**: [veja commits](https://github.com/MarkusLC/mestrado-ccu-pe/commits/main)
