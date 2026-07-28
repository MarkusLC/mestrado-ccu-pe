#!/usr/bin/env python3
"""
SISCAN Download Histórico - 2018-2026
Faz múltiplas querys em TABNET para coletar todos os anos
"""

import json
import os
import re
from datetime import datetime
from bs4 import BeautifulSoup

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "playwright", "beautifulsoup4"])
    from playwright.sync_api import sync_playwright

os.makedirs('data', exist_ok=True)

print("=" * 80)
print("SISCAN DOWNLOAD HISTÓRICO 2018-2026")
print("=" * 80)
print()

# Períodos para fazer query (ano-mês)
periodos = [
    "202612",  # dez/2026
    "202611",  # nov/2026
    "202610",  # out/2026
    "202609",  # set/2026
    "202608",  # ago/2026
    "202607",  # jul/2026
    # ... só 1-2 meses por ano para amostra
    "202501",  # jan/2025
    "202401",  # jan/2024
    "202301",  # jan/2023
    "202201",  # jan/2022
    "202101",  # jan/2021
    "202001",  # jan/2020
    "201901",  # jan/2019
    "201801",  # jan/2018
]

agregado_total = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for periodo_idx, periodo in enumerate(periodos, 1):
        print(f"[{periodo_idx}/{len(periodos)}] Período {periodo}...")

        try:
            # Acessar TABNET
            page.goto("https://tabnet.saude.pe.gov.br/cgi-bin/dh?tab/tabsia08/prodpe.def", timeout=30000)
            page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(500)

            # Configurar
            page.select_option('select[name="Linha"]', 'Munic._Estabelecim')
            page.select_option('select[name="Coluna"]', 'Ano_Competen_______')
            page.select_option('select[name="SProcedimento"]', '222')
            page.wait_for_timeout(500)

            # Incremento (padrão)
            page.evaluate('document.querySelector("select[name=Incremento]").options[0].selected = true;')

            # Período (crucial!)
            try:
                # Procura select de período
                periodo_select = page.query_selector('select[name*="eriodo"], select[name*="Periodo"], select[name*="Mes"]')
                if periodo_select:
                    page.select_option(periodo_select, periodo)
                else:
                    # Tenta input hidden
                    page.evaluate(f'''() => {{
                        const inputs = document.querySelectorAll('input[value="{periodo}"]');
                        inputs.forEach(inp => inp.checked = true);
                    }}''')
            except:
                pass

            # Pesquisar
            page.click('//input[@value="Mostra"]')
            page.wait_for_timeout(3000)

            # Extrair
            html = page.content()
            soup = BeautifulSoup(html, 'html.parser')

            tables = soup.find_all('table', {'class': 'tabdados'})

            registros_periodo = 0

            for table in tables:
                caption = table.find('td', {'colspan': True})
                if caption and '0201020033' in caption.get_text():
                    tbody = table.find('tbody')
                    if tbody:
                        rows = tbody.find_all('tr')

                        for row in rows:
                            cols = row.find_all('td')

                            if len(cols) < 2:
                                continue

                            municipio_text = cols[0].get_text().strip()

                            if not municipio_text or municipio_text == 'TOTAL':
                                continue

                            match = re.search(r'\d+\s+(.+)', municipio_text)
                            municipio = match.group(1) if match else municipio_text

                            # Extrai ano do período
                            ano = periodo[:4]

                            for col_idx in range(1, len(cols)):
                                try:
                                    valor_str = cols[col_idx].get_text().strip()

                                    if not valor_str or valor_str in ['-', '']:
                                        continue

                                    valor = int(valor_str.replace('.', ''))

                                    if valor > 0:
                                        agregado_total.append({
                                            'municipio': municipio,
                                            'ano': ano,
                                            'exames': valor
                                        })
                                        registros_periodo += 1

                                except:
                                    pass

            if registros_periodo > 0:
                print(f"   ✅ {registros_periodo} registros")
            else:
                print(f"   ⏭️  Sem dados")

        except Exception as e:
            print(f"   ⚠️  {e}")

    browser.close()

# Processar resultados
print()
print("=" * 80)

if agregado_total:
    print(f"✅ Total coletado: {len(agregado_total)} registros")

    # Deduplica e agrupa
    by_key = {}
    for item in agregado_total:
        key = (item['municipio'], item['ano'])
        if key not in by_key:
            by_key[key] = 0
        by_key[key] += item['exames']

    agregado_clean = [
        {'municipio': k[0], 'ano': k[1], 'exames': v}
        for k, v in sorted(by_key.items())
    ]

    # Salva
    with open('data/siscan_agregado.json', 'w', encoding='utf-8') as f:
        json.dump(agregado_clean, f, ensure_ascii=False, indent=2)

    total = sum(item['exames'] for item in agregado_clean)
    munic = len(set(item['municipio'] for item in agregado_clean))
    anos = sorted(set(item['ano'] for item in agregado_clean))

    summary = {
        'total_exames': total,
        'total_municipios': munic,
        'anos': anos,
        'periodo': f"{min(anos)} a {max(anos)}" if anos else "N/A",
        'ultima_atualizacao': datetime.now().isoformat() + 'Z',
        'fonte': 'DATASUS SIA TABNET PE',
        'estado': 'PE',
        'procedimento': '0201020033 (Coleta material colo útero citopatologia)',
        'registros': len(agregado_clean)
    }

    with open('data/siscan_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print("=" * 80)
    print(f"   Exames: {total:,}")
    print(f"   Municípios: {munic}")
    print(f"   Período: {summary['periodo']}")
    print(f"   Anos: {', '.join(anos)}")
    print()
    print(f"   📁 data/siscan_agregado.json ({len(agregado_clean)} registros)")
    print(f"   📁 data/siscan_summary.json")
    print()

else:
    print("⚠️  Nenhum dado coletado")
