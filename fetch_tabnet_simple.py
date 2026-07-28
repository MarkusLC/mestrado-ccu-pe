#!/usr/bin/env python3
"""
SISCAN Data Fetch from TABNET - SIMPLEST APPROACH
Uses Playwright to access TABNET and download SISCOLO data for PE
"""

import json
import os
import subprocess
import sys
from datetime import datetime

print("=" * 80)
print("SISCAN FETCH FROM TABNET")
print("=" * 80)
print()

# Install playwright if needed
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("📦 Installing playwright...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-q",
        "playwright", "pandas"
    ])
    from playwright.sync_api import sync_playwright

os.makedirs('data', exist_ok=True)

print("🌐 Opening TABNET portal...")
print("   URL: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/")
print()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    try:
        # Navigate to TABNET
        page.goto("https://datasus.saude.gov.br/informacoes-de-saude-tabnet/", timeout=60000)
        page.wait_for_load_state("networkidle")
        print("✅ Portal loaded")

        # Look for Pernambuco TABNET
        page.goto("https://tabnet.saude.pe.gov.br/", timeout=60000)
        page.wait_for_load_state("networkidle")
        print("✅ PE TABNET loaded")
        print()
        print("📋 Available options on this portal:")

        # Get all available links
        links = page.locator("a").all()
        for i, link in enumerate(links[:20]):
            text = link.inner_text()
            if text.strip():
                print(f"   {i+1}. {text.strip()}")

        print()
        print("⚠️  Manual step required:")
        print()
        print("   1. Visit: https://tabnet.saude.pe.gov.br/")
        print("   2. Look for: SISCOLO / Câncer de Colo de Útero")
        print("   3. Configure:")
        print("      - Lines: Municipality")
        print("      - Columns: Year/Month")
        print("      - Filter: State=PE, Period=2018-2026")
        print("   4. Export as CSV")
        print("   5. Save as: data/siscan_manual.csv")
        print()

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        browser.close()

print()
print("Or try this command directly:")
print("  curl -o data/siscan_raw.html https://tabnet.saude.pe.gov.br/")
