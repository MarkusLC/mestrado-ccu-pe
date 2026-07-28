#!/usr/bin/env python3
"""
SISCAN Mensal - Download CORRETO de série temporal real
Faz query POR MÊS (não por ano) para capturar variação real
"""

import json
import os
import re
import time
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
print("SISCAN MENSAL - SÉRIE TEMPORAL REAL")
print("=" * 80)
print()

# Querys mensais de interesse
# (período_code, label_display)
meses_query = [
    ("202601", "Jun/2026"),
    ("202605", "Mai/2026"),
    ("202604", "Abr/2026"),
    ("202603", "Mar/2026"),
    ("202602", "Fev/2026"),
    ("202601", "Jan/2026"),
    ("202512", "Dez/2025"),
    ("202511", "Nov/2025"),
    ("202510", "Out/2025"),
    ("202509", "Set/2025"),
    # ... continuando para trás
    ("202401", "Jan/2024"),
    ("202301", "Jan/2023"),
    ("202201", "Jan/2022"),
    ("202101", "Jan/2021"),
    ("202001", "Jan/2020"),
    ("201901", "Jan/2019"),
    ("201801", "Jan/2018"),
]

agregado_total = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    for idx, (periodo_code, label) in enumerate(meses_query, 1):
        print(f"[{idx}/{len(meses_query)}] {label}...", end=" ", flush=True)

        page = browser.new_page()

        try:
            page.goto("https://tabnet.saude.pe.gov.br/cgi-bin/dh?tab/tabsia08/prodpe.def", timeout=30000)
            page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(800)

            # Config
            page.select_option('select[name="Linha"]', 'Munic._Estabelecim')
            page.select_option('select[name="Coluna"]', 'Ano_Competen_______')
            page.select_option('select[name="SProcedimento"]', '222')
            page.wait_for_timeout(800)

            page.evaluate('document.querySelector("select[name=Incremento]").options[0].selected = true;')

            # Período CORRETO
            page.evaluate(f'''() => {{
                const opts = document.querySelectorAll('option');
                opts.forEach(o => {{
                    if (o.value === "{periodo_code}") {{
                        o.selected = true;
                        o.parentElement?.dispatchEvent(new Event('change', {{bubbles: true}}));
                    }}
                }});
            }}''')

            page.click('//input[@value="Mostra"]')
            page.wait_for_timeout(4000)

            html = page.content()
            soup = BeautifulSoup(html, 'html.parser')

            tables = soup.find_all('table', {'class': 'tabdados'})

            registros = 0

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

                            for col_idx in range(1, len(cols)):
                                try:
                                    valor_str = cols[col_idx].get_text().strip()

                                    if not valor_str or valor_str in ['-', '']:
                                        continue

                                    valor = int(valor_str.replace('.', ''))

                                    if valor > 0:
                                        # Extrai ano-mês do label
                                        ano_mes = periodo_code
                                        ano = ano_mes[:4]
                                        mes = ano_mes[4:6] if len(ano_mes) >= 6 else "01"

                                        agregado_total.append({
                                            'municipio': municipio,
                                            'ano': ano,
                                            'ano_mes': f"{ano}-{mes}",
                                            'exames': valor
                                        })
                                        registros += 1

                                except:
                                    pass

            print(f"✅ {registros}")

        except Exception as e:
            print(f"⚠️")

        finally:
            page.close()
            time.sleep(0.5)

    browser.close()

# Processar
print()
print("=" * 80)

if agregado_total:
    print(f"✅ Total: {len(agregado_total)} registros")

    # Deduplica
    by_key = {}
    for item in agregado_total:
        key = (item['municipio'], item['ano_mes'])
        if key not in by_key:
            by_key[key] = 0
        by_key[key] += item['exames']

    agregado_clean = [
        {
            'municipio': k[0],
            'ano': k[1][:4],
            'ano_mes': k[1],
            'exames': v
        }
        for k, v in sorted(by_key.items())
    ]

    # Salva
    with open('data/siscan_agregado.json', 'w', encoding='utf-8') as f:
        json.dump(agregado_clean, f, ensure_ascii=False, indent=2)

    total = sum(item['exames'] for item in agregado_clean)
    munic = len(set(item['municipio'] for item in agregado_clean))
    anos = sorted(set(item['ano'] for item in agregado_clean))
    meses = sorted(set(item['ano_mes'] for item in agregado_clean))

    summary = {
        'total_exames': total,
        'total_municipios': munic,
        'anos': anos,
        'meses_coletados': len(meses),
        'periodo': f"{min(meses)} a {max(meses)}" if meses else "N/A",
        'ultima_atualizacao': datetime.now().isoformat() + 'Z',
        'fonte': 'DATASUS SIA TABNET PE',
        'estado': 'PE',
        'procedimento': '0201020033 (Coleta material colo útero citopatologia)',
        'registros': len(agregado_clean),
        'nota': 'Série mensal real (não agregada)'
    }

    with open('data/siscan_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print()
    print("=" * 80)
    print("✅ SISCAN MENSAL (SÉRIE REAL)")
    print("=" * 80)
    print(f"   Exames: {total:,}")
    print(f"   Municípios: {munic}")
    print(f"   Período: {summary['periodo']}")
    print(f"   Meses: {len(meses)}")
    print(f"   Registros: {len(agregado_clean)}")
    print()

else:
    print("⚠️ Nenhum dado")
