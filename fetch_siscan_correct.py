#!/usr/bin/env python3
"""
SISCAN Data Fetch - CORRECT scraping
Selects: PA, all years, all months, PE (Pernambuco)
"""

import json, os, pandas as pd, time
from datetime import datetime
from playwright.sync_api import sync_playwright

print("🎯 SISCAN FETCH - CORRECT APPROACH")
print("=" * 70)
print()

os.makedirs('data', exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Show browser to verify
    page = browser.new_page()

    print("Opening portal...")
    page.goto("https://datasus.saude.gov.br/transferencia-de-arquivos/")
    page.wait_for_load_state("networkidle")
    time.sleep(3)

    print("✅ Portal loaded\n")

    # Step 1: Select Modalidade = "Dados"
    print("1️⃣  Selecting Modalidade = 'Dados'...")
    try:
        page.check('input[value="Dados"]')
        print("   ✅ Selected Dados")
    except:
        print("   ⚠️  Could not select Dados")

    time.sleep(1)

    # Step 2: Select Tipo de Arquivo = "PA"
    print("2️⃣  Selecting Tipo de Arquivo = 'PA'...")
    try:
        page.check('input[value="PA"]')
        print("   ✅ Selected PA (Produção Ambulatorial)")
    except:
        print("   ⚠️  Could not select PA")

    time.sleep(1)

    # Step 3: Select UF = "PE"
    print("3️⃣  Selecting UF = 'PE' (Pernambuco)...")
    try:
        page.check('input[value="PE"]')
        print("   ✅ Selected PE")
    except:
        print("   ⚠️  Could not select PE")

    time.sleep(1)

    # Step 4: Download for all years/months
    print("\n4️⃣  Downloading for years 2018-2026, all months...\n")

    anos = ['2026', '2025', '2024', '2023', '2022', '2021', '2020', '2019', '2018']
    meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

    downloaded = 0

    for ano in anos:
        for mes in meses:
            try:
                # Clear previous selections
                page.fill('input[name="ano"]', ano)
                page.fill('input[name="mes"]', mes)

                # Click Enviar with download listener
                with page.expect_download(timeout=30000) as dl:
                    page.click('button:has-text("Enviar")')

                download = dl.value
                filename = f'data/siscan_{ano}_{mes}.csv'
                download.save_as(filename)

                print(f"   ✅ {ano}-{mes}")
                downloaded += 1

            except Exception as e:
                print(f"   ⏭️  {ano}-{mes}: {str(e)[:40]}")

            if downloaded >= 50:  # Stop after 50 for initial test
                print(f"\n(Downloaded {downloaded} files - stopping for now)")
                break

        if downloaded >= 50:
            break

    browser.close()

print(f"\n✅ Downloaded {downloaded} files")

# Parse all CSVs
print("\nParsing CSV files...")

agregado = []
for f in os.listdir('data'):
    if f.startswith('siscan_') and f.endswith('.csv'):
        try:
            df = pd.read_csv(f'data/{f}', encoding='latin-1', on_bad_lines='skip')
            for _, row in df.iterrows():
                if len(row) >= 3:
                    try:
                        agregado.append({
                            'municipio': str(row.iloc[0]).strip(),
                            'ano_mes': str(row.iloc[1]).strip(),
                            'exames': int(float(str(row.iloc[2]).replace(',', '.')))
                        })
                    except:
                        pass
        except:
            pass

agregado = [a for a in agregado if a['exames'] > 0]

if agregado:
    with open('data/siscan_agregado.json', 'w') as f:
        json.dump(agregado, f, ensure_ascii=False, indent=2)

    summary = {
        'total_exames': sum(a['exames'] for a in agregado),
        'total_municipios': len(set(a['municipio'] for a in agregado)),
        'periodo': f"{min(a['ano_mes'] for a in agregado)} a {max(a['ano_mes'] for a in agregado)}",
        'ultima_atualizacao': datetime.now().isoformat() + 'Z'
    }

    with open('data/siscan_summary.json', 'w') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"✅ {summary['total_exames']:,} exames, {summary['total_municipios']} municípios")
else:
    print("❌ No valid data")
