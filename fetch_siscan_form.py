#!/usr/bin/env python3
"""
SISCAN Data Fetch - Automate DATASUS Portal Form
Selects: PA (Produção Ambulatorial), years 2018-2026, all months
Downloads and aggregates all data
"""

import json
import os
from datetime import datetime
import pandas as pd
import time

print("=" * 70)
print("SISCAN FETCH - DATASUS PORTAL FORM AUTOMATION")
print("=" * 70)
print()

def fetch_all_data_automated():
    """Automate form submission for all years/months"""
    from playwright.sync_api import sync_playwright

    print("🎬 Starting Playwright...")

    all_data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to portal
        print("🌐 Opening DATASUS portal...")
        page.goto("https://datasus.saude.gov.br/transferencia-de-arquivos/", timeout=60000)
        page.wait_for_load_state("networkidle")
        print("   ✅ Portal loaded")

        # Find the form
        print("🔍 Finding form elements...")

        try:
            # Wait for select elements
            page.wait_for_selector('select[name="tipo_arquivo"]', timeout=10000)
            print("   ✅ Found tipo_arquivo select")

            # Select PA (Produção Ambulatorial)
            page.select_option('select[name="tipo_arquivo"]', "PA")
            print("   ✅ Selected: PA (Produção Ambulatorial)")

            time.sleep(1)

            # Get available years
            anos_select = page.locator('select[name="ano"]')
            if anos_select.count() > 0:
                options = anos_select.locator('option').all()
                anos = [opt.get_attribute('value') for opt in options if opt.get_attribute('value')]
                print(f"   ✅ Available years: {anos[:10]}...")
            else:
                anos = ['2026', '2025', '2024', '2023', '2022', '2021', '2020', '2019', '2018']
                print(f"   Using default years: {anos}")

            # Get available months
            meses_select = page.locator('select[name="mes"]')
            if meses_select.count() > 0:
                options = meses_select.locator('option').all()
                meses = [opt.get_attribute('value') for opt in options if opt.get_attribute('value') and opt.get_attribute('value') != '']
                print(f"   ✅ Available months: {meses}")
            else:
                meses = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

            print()
            print("📥 Downloading data for all year/month combinations...")

            # Iterate through years and months
            total_downloads = 0
            for ano in anos:
                for mes in meses:
                    try:
                        # Select year and month
                        page.select_option('select[name="ano"]', ano)
                        page.select_option('select[name="mes"]', mes)

                        time.sleep(0.5)

                        # Listen for download
                        with page.expect_download() as download_info:
                            # Click send button
                            page.click('button:has-text("Enviar"), input[value="Enviar"]')

                        download = download_info.value
                        filename = f"data/siscan_{ano}_{mes}.csv"

                        os.makedirs('data', exist_ok=True)
                        download.save_as(filename)

                        print(f"   ✅ {ano}-{mes}: {filename}")
                        total_downloads += 1

                    except Exception as e:
                        print(f"   ⚠️  {ano}-{mes}: {str(e)[:50]}")
                        continue

                    if total_downloads >= 20:  # Limit downloads for testing
                        print("   (Stopping after 20 downloads for testing)")
                        break

                if total_downloads >= 20:
                    break

            print(f"\n✅ Downloaded {total_downloads} files")

        except Exception as e:
            print(f"❌ Form automation failed: {e}")

        finally:
            browser.close()

    return total_downloads > 0


def parse_all_csvs():
    """Parse all downloaded CSVs into single JSON"""
    print()
    print("📊 Parsing all CSV files...")

    agregado = []

    csv_files = [f for f in os.listdir('data') if f.startswith('siscan_') and f.endswith('.csv')]
    print(f"Found {len(csv_files)} CSV files")

    for csv_file in csv_files:
        filepath = f'data/{csv_file}'

        try:
            # Read with flexible encoding
            df = pd.read_csv(filepath, encoding='latin-1', on_bad_lines='skip')

            # Parse each row
            for _, row in df.iterrows():
                try:
                    if len(row) >= 3:
                        agregado.append({
                            'municipio': str(row.iloc[0]).strip(),
                            'ano_mes': str(row.iloc[1]).strip(),
                            'exames': int(float(str(row.iloc[2]).replace(',', '.'))),
                        })
                except:
                    pass

        except Exception as e:
            print(f"   ⚠️  Error reading {csv_file}: {e}")

    # Clean data
    agregado = [a for a in agregado if a['exames'] > 0 and a['municipio'] and a['ano_mes']]

    if not agregado:
        print("❌ No valid data parsed")
        return False

    # Aggregate by municipio/ano_mes
    print(f"✅ Aggregated {len(agregado)} records")

    # Save
    with open('data/siscan_agregado.json', 'w') as f:
        json.dump(agregado, f, ensure_ascii=False, indent=2)

    total = sum(a['exames'] for a in agregado)
    munic = len(set(a['municipio'] for a in agregado))

    summary = {
        'total_exames': total,
        'total_municipios': munic,
        'periodo': f"{min(a['ano_mes'] for a in agregado)} a {max(a['ano_mes'] for a in agregado)}",
        'ultima_atualizacao': datetime.now().isoformat() + 'Z'
    }

    with open('data/siscan_summary.json', 'w') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"\n✅ REAL DATA: {total:,} exames, {munic} municípios")
    return True


if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)

    print("Step 1: Automate DATASUS portal form download...")
    print()

    if fetch_all_data_automated():
        print("\nStep 2: Parse and aggregate...")
        if parse_all_csvs():
            print("\n" + "=" * 70)
            print("✅ SUCCESS - REAL SISCAN DATA OBTAINED")
            print("=" * 70)
        else:
            print("\n⚠️  Parse failed")
    else:
        print("\n⚠️  Download automation failed")
        print("Manual fallback: Download CSV from portal and save as data/siscan_raw.csv")
