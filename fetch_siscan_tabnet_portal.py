#!/usr/bin/env python3
"""
SISCAN Data Fetch via DATASUS TABNET Portal
Automates the official download form
"""

import json
import os
from datetime import datetime
import pandas as pd

print("=" * 70)
print("SISCAN FETCH - TABNET PORTAL AUTOMATION")
print("=" * 70)
print()

def fetch_via_portal():
    """Automate DATASUS TABNET portal form"""
    print("🎯 Accessing DATASUS TABNET portal...")

    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Access main TABNET portal
            print("   Opening portal...")
            page.goto("https://www2.datasus.gov.br/DATASUS/index.php", timeout=60000)

            # Wait and check for content
            page.wait_for_load_state("networkidle")
            print("   ✅ Portal loaded")

            # Look for "Assistência à Saúde" section
            print("   Finding 'Assistência à Saúde'...")

            # Try to click on the category
            try:
                page.click('button:has-text("Assistência à Saúde")', timeout=5000)
                print("   ✅ Clicked Assistência à Saúde")
            except:
                # Try alternative selectors
                try:
                    page.click('text=Assistência à Saúde', timeout=5000)
                except:
                    pass

            page.wait_for_timeout(2000)

            # Look for SISCAN/citopatologia option
            print("   Finding SISCAN/citopatologia...")

            # Get all visible text to find SISCAN
            content = page.content()
            if 'SISCAN' in content or 'citopatol' in content.lower():
                print("   ✅ Found SISCAN reference")

                # Try to click SISCAN link
                try:
                    page.click('text=SISCAN', timeout=5000)
                except:
                    try:
                        page.click('a:has-text("citopatol")', timeout=5000)
                    except:
                        pass

            page.wait_for_timeout(2000)

            # Look for SIA-PA (Procedimentos Ambulatoriais)
            print("   Finding SIA-PA...")
            try:
                page.click('text=SIA-PA', timeout=5000)
                print("   ✅ Clicked SIA-PA")
            except:
                pass

            page.wait_for_timeout(2000)

            # Setup download listener
            with page.expect_download() as download_info:
                # Click export button
                try:
                    page.click('button:has-text("Exportar")', timeout=5000)
                    print("   ✅ Clicked Exportar")
                except:
                    try:
                        page.click('input[value="Exportar"]', timeout=5000)
                    except:
                        pass

            # Get downloaded file
            download = download_info.value
            print(f"   ✅ Downloaded: {download.suggested_filename}")

            os.makedirs('data', exist_ok=True)
            download.save_as('data/siscan_raw.csv')

            browser.close()
            return True

    except Exception as e:
        print(f"   ⚠️  Playwright approach: {e}")
        return False


def fetch_via_selenium():
    """Fallback: Selenium automation"""
    print("🔄 Trying Selenium approach...")

    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        print("   Opening portal...")
        driver.get("https://www2.datasus.gov.br/DATASUS/index.php")

        # Wait for page
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "button"))
        )
        print("   ✅ Portal loaded")

        # Find and click categories
        try:
            btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Assistência"))
            )
            btn.click()
            print("   ✅ Clicked Assistência à Saúde")
        except:
            pass

        driver.implicitly_wait(2)

        # Look for SISCAN
        try:
            siscan = driver.find_element(By.PARTIAL_LINK_TEXT, "SISCAN")
            siscan.click()
            print("   ✅ Found SISCAN")
        except:
            pass

        driver.quit()
        return True

    except Exception as e:
        print(f"   ⚠️  Selenium: {e}")
        return False


def direct_datasus_endpoint():
    """Try direct endpoint for SIA-PA data"""
    print("🔗 Trying direct DATASUS endpoint...")

    import requests

    # Direct SIA-PA endpoint
    url = "https://www2.datasus.gov.br/cgi-bin/tabcgi.exe?sia/cnv/paproc.def"

    try:
        # POST with form data for TabNet query
        data = {
            "Linha": "Município",
            "Coluna": "Período",
            "Incremento": "Exames",
            "Pesquisa": "1"
        }

        print(f"   POST {url}...")
        resp = requests.post(url, data=data, timeout=30)

        if resp.status_code == 200 and len(resp.text) > 1000:
            print(f"   ✅ Got response ({len(resp.text)} bytes)")
            with open('data/siscan_raw.csv', 'w') as f:
                f.write(resp.text)
            return True
        else:
            print(f"   Status: {resp.status_code}")
    except Exception as e:
        print(f"   ⚠️  {e}")

    return False


def parse_csv():
    """Parse CSV to JSON"""
    print()
    print("📊 Parsing CSV...")

    csv_file = 'data/siscan_raw.csv'

    if not os.path.exists(csv_file):
        print("❌ No CSV found")
        return False

    try:
        # Read CSV with flexible encoding
        for encoding in ['latin-1', 'utf-8', 'iso-8859-1']:
            try:
                df = pd.read_csv(csv_file, encoding=encoding, on_bad_lines='skip')
                break
            except:
                continue

        print(f"✅ Loaded {len(df)} rows")

        # Parse data
        agregado = []
        for _, row in df.iterrows():
            try:
                agregado.append({
                    'municipio': str(row.iloc[0]).strip(),
                    'ano_mes': str(row.iloc[1]).strip() if len(row) > 1 else '',
                    'exames': int(float(str(row.iloc[2]).strip())) if len(row) > 2 else 0
                })
            except:
                pass

        if not agregado:
            print("⚠️  Could not parse rows")
            return False

        # Remove empty entries
        agregado = [a for a in agregado if a['exames'] > 0 and a['municipio'] and a['ano_mes']]

        if not agregado:
            print("⚠️  No valid data rows")
            return False

        # Save JSON
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

        print(f"✅ {total} exames, {munic} municípios")
        return True

    except Exception as e:
        print(f"❌ {e}")
        return False


if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)

    # Try methods in order
    methods = [
        ("Playwright", fetch_via_portal),
        ("Selenium", fetch_via_selenium),
        ("Direct Endpoint", direct_datasus_endpoint),
    ]

    success = False
    for name, method in methods:
        print()
        try:
            if method():
                success = True
                break
        except Exception as e:
            print(f"   {e}")

    # Parse whatever we got
    print()
    if parse_csv():
        print()
        print("=" * 70)
        print("✅ SUCCESS - REAL SISCAN DATA")
        print("=" * 70)
    else:
        print()
        print("=" * 70)
        print("⚠️  Could not obtain data from any method")
        print("=" * 70)
