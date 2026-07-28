# 🚀 Setup Rápido

## O que você tem agora

Um repositório **totalmente automático** que:

1. ✅ Puxa dados SISCAN (citopatológico) do DATASUS automaticamente todo dia 15
2. ✅ Processa + agrega por município e mês
3. ✅ Gera gráficos ao vivo no dashboard
4. ✅ Versiona tudo (Git)

**Você não precisa fazer NADA** — é automático.

---

## 📊 Ver o Dashboard Agora

1. Clone o repositório:
```bash
git clone https://github.com/MarkusLC/mestrado-ccu-pe
cd mestrado-ccu-pe
```

2. Abra no navegador:
```bash
open dashboard_mestrado.html
# ou
firefox dashboard_mestrado.html
# ou
google-chrome dashboard_mestrado.html
```

**Pronto!** Você vê dados de exemplo agregados por município (Recife, Jaboatão, Olinda, Caruaru, Paulista).

---

## 🔄 Como os dados são atualizados

### Automático (você não faz nada)

- **Quando**: Dia 15 de cada mês, 12h UTC
- **O que**: GitHub Actions roda `fetch_siscan.R`
- **Resultado**: JSON atualizado, dashboard carrega automaticamente

### Manual (para testar)

1. Vá em **Actions** no repositório
2. Selecione **update-siscan**
3. Clique em **Run workflow**
4. Espere ~3-5 min
5. Os dados novos aparecem em `data/siscan_agregado.json`
6. Dashboard recarrega automaticamente em 1 hora (ou F5 para forçar)

---

## 🛠️ Estrutura dos Arquivos

```
.
├── dashboard_mestrado.html       👈 ABRA ISTO NO NAVEGADOR
├── fetch_siscan.R                (Script que roda automaticamente)
├── .github/workflows/
│   └── update-siscan.yml         (GitHub Actions config)
├── data/
│   ├── siscan_agregado.json      (Dados agregados por mês/município)
│   └── siscan_summary.json       (Metadados: totais, período, data)
├── README.md                      (Documentação completa)
└── .gitignore                     (Ignora arquivos desnecessários)
```

---

## 📈 O que o Dashboard mostra

### Tab: Dados SISCAN
- **Total de exames** (2018–2026)
- **Municípios com registro**
- **Período coberto**
- **Última atualização**

### Tab: Série Temporal
- Gráfico de exames mensais agregados (toda PE)
- Mostra os 4 marcos (Previne Brasil, COVID, SB360 fin., SB360 C7)

### Tab: Por Região
- Top 15 municípios
- Ordenado por total de exames

### Tab: Metodologia
- Delineamento: ITS Multinível
- 184 municípios, 108 meses (2018–2026)
- Modelo: GLMM (Binomial Negativa)
- Links para documentação completa

---

## 🔗 Documentação Completa

Todos os documentos estão **versionados** no repositório:

- **Dashboard**: `dashboard_mestrado.html` (neste repo)
- **Métodos completos**: [Google Docs](https://docs.google.com/document/d/1wGtMpaSoXrTcrNe0BJx3CMJyICIFQW47-rFM7xCqO14/edit)
- **Parecer metodológico**: [Google Docs](https://docs.google.com/document/d/1jcGEAaTNBLJEoX0DoEaFsomhho6ieFM1SUYsF-pD4sQ/edit)

---

## ⚠️ Dados de Exemplo (Agora)

O repositório já tem **dados fictícios mas realistas** em `data/`:

- 5 municípios principais (Recife, Jaboatão, Olinda, Caruaru, Paulista)
- Série 2018–2025 mostrando:
  - 📈 Crescimento (2018–2019)
  - 📉 Queda COVID (2020–2021)
  - 📈 Recuperação (2024+)
  - ⬆️ Aumento após C7 (2025)

**Quando o GitHub Actions rodar (dia 15), esses dados serão substituídos pelos reais.**

---

## 🚦 Checklist

- [x] Repositório criado
- [x] GitHub Actions configurado
- [x] Dashboard pronto
- [x] Dados de exemplo inclusos
- [x] README com instruções
- [ ] Primeira execução do Actions (dia 15)
- [ ] Validar dados reais quando chegarem

---

## 💡 Dicas

1. **Dashboard é estático** — não precisa de servidor, roda em qualquer navegador
2. **Dados são JSON** — fácil de analisar em R, Python, etc depois
3. **Tudo é versionado** — você vê exatamente quando cada dado foi atualizado
4. **Reprodutível 100%** — pode anexar o link na dissertação

---

## ❓ Dúvidas?

Veja `README.md` para troubleshooting completo.

---

**Próximo passo**: Abra `dashboard_mestrado.html` no seu navegador e explore! 🚀
