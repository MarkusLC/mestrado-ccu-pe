#!/usr/bin/env python3
"""
Fetch SISCAN data from DATASUS TabNet using Playwright
Automates the entire download process
"""

import json
import os
import time
from pathlib import Path
from datetime import datetime
import pandas as pd

async def fetch_datasus():
    from playwright.async_api import async_playwright

    print("🎬 Starting Playwright automation for DATASUS...")
    print("🌐 Opening TabNet...")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        try:
            # Navigate to DATASUS TabNet SIA
            url = "http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sia/cnv/paproc.def"
            await page.goto(url, wait_until="networkidle", timeout=60000)

            print("⏳ Page loaded, waiting for interface...")
            await page.wait_for_timeout(3000)

            # Click on data selection (varies by interface)
            # This is a generic approach - adapt based on actual TabNet structure

            print("🔍 Looking for export option...")

            # Try to find and click export button
            # DATASUS uses various interfaces, so we'll try multiple selectors
            export_selectors = [
                'button:has-text("Exportar")',
                'input[value="Exportar"]',
                'a:has-text("CSV")',
                'button[title*="Exportar"]',
            ]

            export_clicked = False
            for selector in export_selectors:
                try:
                    await page.click(selector, timeout=5000)
                    print(f"✅ Clicked export with selector: {selector}")
                    export_clicked = True
                    break
                except:
                    continue

            if not export_clicked:
                print("⚠️  Could not find export button, trying download event...")

                # Listen for download events
                async def handle_download(download):
                    await download.save_as("data/siscan_raw.csv")
                    print(f"✅ Downloaded: {download.suggested_filename}")

                page.on("download", handle_download)

                # Try alternative export methods
                await page.evaluate("""
                    () => {
                        // Try to trigger download via JavaScript
                        const btn = document.querySelector('[value="Exportar"]') ||
                                   document.querySelector('button:contains("Exportar")');
                        if (btn) btn.click();
                    }
                """)

                await page.wait_for_timeout(5000)

            # Wait for file download
            print("⏳ Waiting for download...")
            await page.wait_for_timeout(10000)

            print("✅ Download should be complete")

        except Exception as e:
            print(f"❌ Error: {e}")
            print("This is expected if TabNet structure changed")
            print("Fallback: Use manual download or alternative method")

        finally:
            await browser.close()


def parse_siscan_csv():
    """Parse downloaded CSV to JSON"""

    csv_file = "data/siscan_raw.csv"

    if not Path(csv_file).exists():
        print(f"⚠️  {csv_file} not found")
        print("Manual download required from:")
        print("  http://tabnet.datasus.gov.br/")
        print("  → SIA → Procedimentos Ambulatoriais")
        print("  → Filtrar: Citopatologia (020101)")
        print("  → Exportar CSV")
        return False

    print(f"📖 Parsing {csv_file}...")

    try:
        # Read CSV (adjust encoding if needed)
        df = pd.read_csv(csv_file, encoding='latin-1')

        print(f"Loaded: {len(df)} rows, {len(df.columns)} columns")
        print(f"Columns: {list(df.columns)}")

        # Aggregate by municipality and month
        # Column names vary; adjust based on actual DATASUS export
        required_cols = ['Município', 'Período', 'Exames']  # Portuguese

        # Try alternative column names
        col_map = {}
        for required in required_cols:
            found = None
            for col in df.columns:
                if required.lower() in col.lower():
                    found = col
                    break
            if found:
                col_map[required] = found

        if len(col_map) < 2:
            print("⚠️  Could not find expected columns")
            print(f"Available: {df.columns.tolist()}")
            return False

        # Rename columns
        df = df.rename(columns={v: k for k, v in col_map.items()})

        # Ensure numeric data
        df['Exames'] = pd.to_numeric(df['Exames'], errors='coerce').fillna(0).astype(int)

        # Format: municipio, ano_mes, exames
        agregado = df[['Município', 'Período', 'Exames']].copy()
        agregado.columns = ['municipio', 'ano_mes', 'exames']
        agregado = agregado[agregado['exames'] > 0]

        print(f"✅ Aggregated: {len(agregado)} records")
        print(f"   Municipalities: {agregado['municipio'].nunique()}")
        print(f"   Months: {agregado['ano_mes'].nunique()}")

        # Save as JSON
        os.makedirs("data", exist_ok=True)

        with open("data/siscan_agregado.json", 'w', encoding='utf-8') as f:
            json.dump(agregado.to_dict('records'), f, ensure_ascii=False, indent=2)

        print("✓ Saved: data/siscan_agregado.json")

        # Save summary
        summary = {
            "total_exames": int(agregado['exames'].sum()),
            "total_municipios": int(agregado['municipio'].nunique()),
            "periodo": f"{agregado['ano_mes'].min()} a {agregado['ano_mes'].max()}",
            "ultima_atualizacao": datetime.now().isoformat() + "Z"
        }

        with open("data/siscan_summary.json", 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        print(f"✓ Summary: {summary['total_exames']} exames, {summary['total_municipios']} municípios")

        return True

    except Exception as e:
        print(f"❌ Parse error: {e}")
        return False


if __name__ == "__main__":
    import asyncio

    print("=" * 60)
    print("SISCAN Data Fetch - DATASUS TabNet via Playwright")
    print("=" * 60)
    print()

    # Try Playwright automation
    try:
        asyncio.run(fetch_datasus())
    except Exception as e:
        print(f"⚠️  Playwright failed: {e}")
        print("   This is normal if Playwright dependencies are incomplete")

    # Parse CSV (works if download succeeded)
    print()
    print("Parsing CSV...")
    if parse_siscan_csv():
        print("\n✅ SUCCESS: Real SISCAN data from DATASUS!")
    else:
        print("\n⚠️  Could not process. Manual download required.")
        print("See instructions above.")
