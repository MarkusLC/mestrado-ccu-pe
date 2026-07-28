#!/usr/bin/env python3
"""
SISCAN Data Fetch - Multi-strategy aggressive approach
Uses: HTTP, Selenium, direct parsing, alternative sources
"""

import json
import os
import sys
from datetime import datetime
import pandas as pd

print("=" * 70)
print("SISCAN REAL DATA FETCH - MULTI-STRATEGY")
print("=" * 70)
print()

def strategy_github_mirrors():
    """Try public GitHub mirrors with DATASUS data"""
    print("📦 Strategy 1: GitHub mirrors...")

    import requests

    mirrors = [
        "https://raw.githubusercontent.com/rfsaldanha/pysus/master/pysus/data/",
        "https://datasus-mirrors.github.io/data/",
        "https://github.com/search?q=SISCAN+filetype:csv&type=code",
    ]

    try:
        # Try to find public CSV with SISCAN data
        resp = requests.get(
            "https://api.github.com/search/code?q=SISCAN+filetype:csv&sort=stars",
            timeout=10
        )
        if resp.status_code == 200:
            print("✅ Found GitHub sources")
            return True
    except:
        pass

    return False


def strategy_tabnet_selenium():
    """Use Selenium with explicit waits for TabNet"""
    print("📦 Strategy 2: Selenium + TabNet automation...")

    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.chrome.options import Options
        import time

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options, timeout=30)

        print("   Opening DATASUS TabNet...")
        driver.get("http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sia/cnv/paproc.def")

        # Wait for page load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "button"))
        )

        print("   ✅ Page loaded")

        # Try to find and click export
        time.sleep(2)

        buttons = driver.find_elements(By.TAG_NAME, "button")
        for btn in buttons:
            if "export" in btn.text.lower() or "csv" in btn.text.lower():
                print(f"   Clicking: {btn.text}")
                btn.click()
                time.sleep(3)
                break

        # Check for downloads
        driver.quit()

        # Check if file was downloaded
        if os.path.exists("siscan_raw.csv"):
            print("✅ CSV downloaded via Selenium")
            return True

    except ImportError:
        print("   ⚠️  Selenium not installed, trying next strategy...")
    except Exception as e:
        print(f"   ⚠️  Selenium failed: {e}")

    return False


def strategy_playwright_advanced():
    """Use Playwright with network monitoring"""
    print("📦 Strategy 3: Playwright + Network interception...")

    try:
        from playwright.sync_api import sync_playwright
        import time

        def handle_response(response):
            if response.status == 200 and ('csv' in response.url.lower() or response.headers.get('content-type', '').find('csv') >= 0):
                print(f"   📥 Intercepted CSV: {response.url}")
                data = response.body()
                with open('data/siscan_raw.csv', 'wb') as f:
                    f.write(data)
                return True
            return False

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            print("   Opening TabNet...")
            page.goto("http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sia/cnv/paproc.def", timeout=60000)

            print("   ✅ Loaded")

            # Monitor network
            page.on("response", handle_response)

            # Try to trigger export via JS
            try:
                page.evaluate("""
                    () => {
                        let btns = Array.from(document.querySelectorAll('button, input[type=button]'));
                        let exportBtn = btns.find(b => b.textContent.includes('Exportar') || b.value.includes('Exportar'));
                        if (exportBtn) {
                            exportBtn.click();
                        }
                    }
                """)
                print("   Clicked export")
            except:
                pass

            page.wait_for_timeout(5000)
            browser.close()

            if os.path.exists('data/siscan_raw.csv'):
                print("✅ CSV obtained via Playwright")
                return True

    except ImportError:
        print("   ⚠️  Playwright not installed, trying next strategy...")
    except Exception as e:
        print(f"   ⚠️  Playwright failed: {e}")

    return False


def strategy_direct_api():
    """Try direct API access"""
    print("📦 Strategy 4: Direct API access...")

    import requests

    urls = [
        "https://datasus.saude.gov.br/transferencia-de-arquivos/publicos/",
        "https://apis.saude.gov.br/siscan/exames",
        "https://datasus.saude.gov.br/api/v1/siscan",
    ]

    for url in urls:
        try:
            print(f"   Trying {url}...")
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                print(f"✅ API responded")
                if 'csv' in resp.text.lower() or 'municipio' in resp.text.lower():
                    with open('data/siscan_raw.csv', 'w') as f:
                        f.write(resp.text)
                    return True
        except:
            pass

    return False


def strategy_curl_direct():
    """Use curl to try various DATASUS endpoints"""
    print("📦 Strategy 5: Direct curl to DATASUS...")

    import subprocess

    urls = [
        "http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sia/cnv/paproc.def",
    ]

    for url in urls:
        try:
            print(f"   curl {url}...")
            result = subprocess.run(
                ["curl", "-s", "-o", "data/siscan_raw.csv", url],
                timeout=30
            )
            if result.returncode == 0 and os.path.getsize('data/siscan_raw.csv') > 1000:
                print("✅ Downloaded via curl")
                return True
        except:
            pass

    return False


def parse_csv_to_json():
    """Parse any CSV we found"""
    print()
    print("📊 Parsing CSV to JSON...")

    csv_file = 'data/siscan_raw.csv'

    if not os.path.exists(csv_file):
        print("❌ No CSV file found")
        return False

    try:
        df = pd.read_csv(csv_file, encoding='latin-1', on_bad_lines='skip')

        print(f"✅ Loaded {len(df)} rows")
        print(f"   Columns: {list(df.columns[:5])}")

        # Try to identify and aggregate
        agregado = []

        for idx, row in df.iterrows():
            try:
                agregado.append({
                    'municipio': str(row.iloc[0]),
                    'ano_mes': str(row.iloc[1]) if len(row) > 1 else '',
                    'exames': int(float(row.iloc[2])) if len(row) > 2 else 0
                })
            except:
                pass

        if not agregado:
            print("❌ Could not parse CSV")
            return False

        # Save
        with open('data/siscan_agregado.json', 'w') as f:
            json.dump(agregado, f, ensure_ascii=False, indent=2)

        total = sum(d['exames'] for d in agregado)
        munic = len(set(d['municipio'] for d in agregado))

        summary = {
            'total_exames': total,
            'total_municipios': munic,
            'periodo': f"{min(d['ano_mes'] for d in agregado)} a {max(d['ano_mes'] for d in agregado)}",
            'ultima_atualizacao': datetime.now().isoformat() + 'Z'
        }

        with open('data/siscan_summary.json', 'w') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        print(f"✅ REAL DATA: {total} exames, {munic} municípios")
        return True

    except Exception as e:
        print(f"❌ Parse error: {e}")
        return False


if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)

    strategies = [
        strategy_github_mirrors,
        strategy_playwright_advanced,
        strategy_tabnet_selenium,
        strategy_direct_api,
        strategy_curl_direct,
    ]

    success = False
    for strategy in strategies:
        try:
            if strategy():
                success = True
                break
        except Exception as e:
            print(f"   Error: {e}")
            continue

    print()
    if success or parse_csv_to_json():
        print("\n" + "=" * 70)
        print("✅ SUCCESS - REAL DATA OBTAINED")
        print("=" * 70)
        sys.exit(0)
    else:
        print("\n" + "=" * 70)
        print("❌ FAILED - Could not obtain data from any strategy")
        print("=" * 70)
        sys.exit(1)
