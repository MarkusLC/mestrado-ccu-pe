# 📥 Download Dados REAIS do DATASUS (3 min)

## Passo 1: Abrir TabNet (30 seg)

```bash
open "http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sia/cnv/paproc.def"
```

Ou copie/cola no navegador.

## Passo 2: Selecionar Citopatologia (1 min)

Na página que abrir:

1. **Linha:** Município
2. **Coluna:** Período  
3. **Incremento:** Exames
4. **Períodos:** Clique em "2018-01" até "2026-12" (ou quanto tiver)
5. **Tema:** SIA
6. Clique em **Mostrar**

## Passo 3: Exportar CSV (30 seg)

Após carregar os dados:

1. Clique no botão **Exportar**
2. Escolha **CSV** (ou qualquer formato)
3. Salve como `siscan_raw.csv` em `/Users/markuscorgosinho/projects/Juliana/mestrado-ccu-pe/data/`

## Passo 4: Rodar Parser (30 seg)

```bash
cd /Users/markuscorgosinho/projects/Juliana/mestrado-ccu-pe
python3 -c "
import pandas as pd, json, os
from datetime import datetime

csv_file = 'data/siscan_raw.csv'
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file, encoding='latin-1')
    # Adjust column names based on DATASUS export
    # Usually: Município, Período, Exames
    agregado = []
    for _, row in df.iterrows():
        try:
            agregado.append({
                'municipio': str(row.iloc[0]) if len(row) > 0 else '',
                'ano_mes': str(row.iloc[1]) if len(row) > 1 else '',
                'exames': int(row.iloc[2]) if len(row) > 2 else 0
            })
        except:
            pass
    
    with open('data/siscan_agregado.json', 'w') as f:
        json.dump(agregado, f, ensure_ascii=False, indent=2)
    
    total = sum(d['exames'] for d in agregado)
    munic = len(set(d['municipio'] for d in agregado))
    
    summary = {
        'total_exames': total,
        'total_municipios': munic,
        'periodo': f'{min(d[\"ano_mes\"] for d in agregado)} a {max(d[\"ano_mes\"] for d in agregado)}',
        'ultima_atualizacao': datetime.now().isoformat() + 'Z'
    }
    
    with open('data/siscan_summary.json', 'w') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f'✅ {total} exames, {munic} municípios')
else:
    print('❌ siscan_raw.csv not found')
"
```

## Passo 5: Push (30 seg)

```bash
git add data/siscan_*.json
git commit -m "data: SISCAN real data from DATASUS"
git push
```

**PRONTO!** Dashboard tem dados REAIS! 🎉

---

**Nota:** Se o CSV tiver outro formato, ajuste os nomes das colunas no parser Python acima.
