#!/usr/bin/env python3
"""
SISCAN Data Fetch - REAL DATA via datasus-fetcher
Download SISCOLO exams from DATASUS for Pernambuco (PE) 2018-2026
Source: https://pypi.org/project/datasus-fetcher/
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

print("=" * 80)
print("SISCAN REAL DATA FETCH - DATASUS FETCHER")
print("=" * 80)
print()

# Ensure data dir exists
os.makedirs('data', exist_ok=True)

# Step 1: Install datasus-fetcher if not present
print("📦 Checking datasus-fetcher installation...")
try:
    import datasus_fetcher
    print("   ✅ datasus-fetcher already installed")
except ImportError:
    print("   📥 Installing datasus-fetcher...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "datasus-fetcher"])
    print("   ✅ datasus-fetcher installed")

print()

# Step 2: Fetch SISCOLO data for PE
print("🔍 Fetching SISCOLO exams for Pernambuco (PE)...")
print("   Period: 2018-2026")
print()

try:
    from datasus_fetcher import Fetcher

    # Create fetcher
    fetcher = Fetcher(system='SISCOLO')

    # Download for PE state, years 2018-2026
    print("   Downloading... (this may take 1-2 minutes)")

    df = fetcher.download(
        state='PE',
        years=list(range(2018, 2027))  # 2018-2026
    )

    print(f"   ✅ Downloaded: {len(df)} records")

    # Show sample
    if len(df) > 0:
        print(f"\n   Columns: {list(df.columns)}")
        print(f"\n   Sample:")
        print(df.head(2).to_string())

except Exception as e:
    print(f"   ❌ datasus-fetcher error: {e}")
    print()
    print("   🔄 Trying alternative: PySUS...")

    try:
        from pysus.online_data import SISCOLO

        siscolo = SISCOLO()
        df = siscolo.download(state='PE', year=2024)  # Test with one year first

        print(f"   ✅ PySUS downloaded: {len(df)} records")

    except Exception as e2:
        print(f"   ❌ PySUS also failed: {e2}")
        print()
        print("   ⚠️  Could not fetch SISCOLO via automated tools.")
        print()
        print("   FALLBACK: Manual download")
        print("   1. Visit: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/")
        print("   2. Select: Epidemiológicas e Morbidade → SISCOLO/SISMAMA")
        print("   3. Filter: State=PE, Period=2018-2026")
        print("   4. Export CSV → Save as data/siscan_manual.csv")
        print()
        sys.exit(1)

print()

# Step 3: Aggregate data
print("📊 Aggregating SISCOLO data...")

if df is not None and len(df) > 0:
    # Rename columns to match our schema (depends on SISCOLO structure)
    # Typical columns: MUNICIPIO, ANO, MES, EXAMES_CITO

    agregado = []

    # Infer column names (they might vary)
    col_municipio = next((col for col in df.columns if 'munic' in col.lower()), None)
    col_ano = next((col for col in df.columns if 'ano' in col.lower()), None)
    col_mes = next((col for col in df.columns if 'mes' in col.lower()), None)
    col_exames = next((col for col in df.columns if 'exam' in col.lower() or 'cito' in col.lower()), None)

    if all([col_municipio, col_ano, col_mes, col_exames]):
        for _, row in df.iterrows():
            try:
                agregado.append({
                    'municipio': str(row[col_municipio]).strip(),
                    'ano_mes': f"{int(row[col_ano])}-{int(row[col_mes]):02d}",
                    'exames': int(row[col_exames])
                })
            except:
                pass

        # Remove invalid records
        agregado = [a for a in agregado if a['exames'] > 0 and a['municipio']]

        print(f"   ✅ Aggregated: {len(agregado)} records")

        # Save JSON
        with open('data/siscan_agregado.json', 'w', encoding='utf-8') as f:
            json.dump(agregado, f, ensure_ascii=False, indent=2)

        total = sum(a['exames'] for a in agregado)
        munic = len(set(a['municipio'] for a in agregado))

        summary = {
            'total_exames': total,
            'total_municipios': munic,
            'periodo': f"{min(a['ano_mes'] for a in agregado)} a {max(a['ano_mes'] for a in agregado)}",
            'ultima_atualizacao': datetime.now().isoformat() + 'Z',
            'fonte': 'DATASUS SISCOLO',
            'estado': 'PE'
        }

        with open('data/siscan_summary.json', 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        print()
        print("=" * 80)
        print("✅ SUCCESS - REAL SISCAN DATA")
        print("=" * 80)
        print(f"   Total exames: {total:,}")
        print(f"   Municipalities: {munic}")
        print(f"   Period: {summary['periodo']}")
        print(f"   Files: data/siscan_agregado.json + data/siscan_summary.json")
        print()
    else:
        print(f"   ⚠️  Could not infer columns from fetched data")
        print(f"   Available columns: {list(df.columns)}")
