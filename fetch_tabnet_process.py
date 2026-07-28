#!/usr/bin/env python3
"""
Process SISCAN CSV from TABNET into aggregated JSON
Run this after downloading CSV manually from TABNET portal
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

print("=" * 80)
print("SISCAN TABNET CSV → JSON PROCESSOR")
print("=" * 80)
print()

os.makedirs('data', exist_ok=True)

# Check if raw CSV exists
csv_files = [
    'data/siscan_manual.csv',
    'data/siscan_raw.csv',
    'data/siscan.csv'
]

csv_file = None
for f in csv_files:
    if Path(f).exists():
        csv_file = f
        break

if not csv_file:
    print("❌ No CSV found in data/ directory")
    print()
    print("To get data:")
    print("  1. Visit: https://tabnet.saude.pe.gov.br/")
    print("  2. Select: SISCOLO (Câncer de Colo de Útero)")
    print("  3. Configure:")
    print("     - Lines (Linhas): Municipality (Município)")
    print("     - Columns (Colunas): Year/Month (Ano/Mês)")
    print("     - Filter to: State=PE, Period=2018-2026")
    print("  4. Export as CSV")
    print("  5. Save as: data/siscan_manual.csv")
    print()
    sys.exit(1)

print(f"📂 Found: {csv_file}")
print()

try:
    # Read CSV with multiple encoding attempts
    df = None
    for encoding in ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']:
        try:
            df = pd.read_csv(csv_file, encoding=encoding, on_bad_lines='skip')
            print(f"✅ Loaded with encoding: {encoding}")
            break
        except:
            continue

    if df is None:
        print("❌ Could not read CSV with any encoding")
        sys.exit(1)

    print(f"   Rows: {len(df)}")
    print(f"   Columns: {list(df.columns)}")
    print()

    # Parse into aggregated format
    agregado = []

    for _, row in df.iterrows():
        try:
            row_dict = row.to_dict()

            # Try to infer column positions/names
            # Typical TABNET format:
            # Col 1: Municipality
            # Col 2: Year-Month or Year/Month
            # Col 3+: Values (exams count)

            cols = [str(v).strip() for v in row]

            if len(cols) >= 3:
                municipio = cols[0]
                ano_mes = cols[1]

                # Get first numeric value as exams count
                exames = 0
                for val in cols[2:]:
                    try:
                        exames = int(float(val.replace(',', '.')))
                        if exames > 0:
                            break
                    except:
                        pass

                if municipio and exames > 0:
                    # Normalize ano_mes format to YYYY-MM
                    if '-' in ano_mes:
                        ano_mes = ano_mes.replace('-', '-')
                    elif '/' in ano_mes:
                        parts = ano_mes.split('/')
                        if len(parts) == 2:
                            ano_mes = f"{parts[0]}-{parts[1]:0>2}"

                    agregado.append({
                        'municipio': municipio,
                        'ano_mes': ano_mes,
                        'exames': exames
                    })
        except Exception as e:
            pass

    # Remove duplicates and invalid records
    agregado = [a for a in agregado if a['exames'] > 0 and a['municipio']]

    if not agregado:
        print("❌ No valid data parsed")
        sys.exit(1)

    print(f"✅ Aggregated: {len(agregado)} records")
    print()

    # Save JSON
    with open('data/siscan_agregado.json', 'w', encoding='utf-8') as f:
        json.dump(agregado, f, ensure_ascii=False, indent=2)

    total = sum(a['exames'] for a in agregado)
    munic = len(set(a['municipio'] for a in agregado))
    periodo_min = min(a['ano_mes'] for a in agregado)
    periodo_max = max(a['ano_mes'] for a in agregado)

    summary = {
        'total_exames': total,
        'total_municipios': munic,
        'periodo': f"{periodo_min} a {periodo_max}",
        'ultima_atualizacao': datetime.now().isoformat() + 'Z',
        'fonte': 'DATASUS TABNET SISCOLO',
        'estado': 'PE'
    }

    with open('data/siscan_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print("=" * 80)
    print("✅ SUCCESS - SISCAN DATA PROCESSED")
    print("=" * 80)
    print(f"   Total exames: {total:,}")
    print(f"   Municipalities: {munic}")
    print(f"   Period: {summary['periodo']}")
    print()
    print(f"   Output files:")
    print(f"   - data/siscan_agregado.json")
    print(f"   - data/siscan_summary.json")
    print()

except Exception as e:
    print(f"❌ Error processing CSV: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
