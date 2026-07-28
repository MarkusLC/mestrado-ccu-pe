#!/usr/bin/env python3
"""
Expand SISCAN - Download COMPLETO 2018-2026
Faz 1 query por ano para coletar série histórica
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
print("SISCAN EXPANSION 2018-2026")
print("=" * 80)
print()

# Um mês por ano (janeiro de cada ano)
anos = [
    ("201801", "2018"),
    ("201901", "2019"),
    ("202001", "2020"),
    ("202101", "2021"),
    ("202201", "2022"),
    ("202301", "2023"),
    ("202401", "2024"),
    ("202501", "2025"),
    ("202601", "2026"),
]

agregado_total = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    for idx, (periodo_code, ano_label) in enumerate(anos, 1):
        print(f"[{idx}/{len(anos)}] {ano_label} ({periodo_code})...", end=" ", flush=True)

        page = browser.new_page()

        try:
            # Acessar
            page.goto("https://tabnet.saude.pe.gov.br/cgi-bin/dh?tab/tabsia08/prodpe.def", timeout=30000)
            page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(800)

            # Configurar
            page.select_option('select[name="Linha"]', 'Munic._Estabelecim')
            page.select_option('select[name="Coluna"]', 'Ano_Competen_______')
            page.select_option('select[name="SProcedimento"]', '222')
            page.wait_for_timeout(800)

            # Incremento padrão
            page.evaluate('document.querySelector("select[name=Incremento]").options[0].selected = true;')

            # Período - tenta diferentes seletores
            periodo_set = False

            # Tenta select direto
            try:
                selects_periodo = page.query_selector_all('select')
                for sel in selects_periodo:
                    name = sel.get_attribute('name') or ''
                    if any(x in name.lower() for x in ['periodo', 'mes', 'data']):
                        try:
                            page.select_option(sel, periodo_code)
                            periodo_set = True
                            break
                        except:
                            pass
            except:
                pass

            # Se não achou select, tenta input
            if not periodo_set:
                try:
                    page.evaluate(f'''() => {{
                        const opts = document.querySelectorAll('option');
                        opts.forEach(o => {{
                            if (o.value === "{periodo_code}" || o.textContent.includes("{periodo_code}")) {{
                                o.selected = true;
                                o.parentElement?.dispatchEvent(new Event('change', {{bubbles: true}}));
                            }}
                        }});
                    }}''')
                    periodo_set = True
                except:
                    pass

            # Pesquisar
            page.click('//input[@value="Mostra"]')
            page.wait_for_timeout(4000)

            # Extrair
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

                            # Extrai nome do município
                            match = re.search(r'\d+\s+(.+)', municipio_text)
                            municipio = match.group(1) if match else municipio_text

                            # Pega valores
                            for col_idx in range(1, len(cols)):
                                try:
                                    valor_str = cols[col_idx].get_text().strip()

                                    if not valor_str or valor_str in ['-', '']:
                                        continue

                                    valor = int(valor_str.replace('.', ''))

                                    if valor > 0:
                                        agregado_total.append({
                                            'municipio': municipio,
                                            'ano': ano_label,
                                            'exames': valor
                                        })
                                        registros += 1

                                except:
                                    pass

            print(f"✅ {registros} registros")

        except Exception as e:
            print(f"⚠️ {str(e)[:30]}")

        finally:
            page.close()
            time.sleep(1)  # Respeitar servidor

    browser.close()

# Processar
print()
print("=" * 80)

if agregado_total:
    print(f"✅ Total: {len(agregado_total)} registros")

    # Deduplica
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
        'registros': len(agregado_clean),
        'nota': '1 mês por ano (janeiro). Para granularidade mensal completa, execute múltiplas querys.'
    }

    with open('data/siscan_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print()
    print("=" * 80)
    print("✅ SISCAN EXPANDIDO")
    print("=" * 80)
    print(f"   Exames: {total:,}")
    print(f"   Municípios: {munic}")
    print(f"   Período: {summary['periodo']}")
    print(f"   Anos: {', '.join(anos)}")
    print(f"   Registros: {len(agregado_clean)}")
    print()

else:
    print("⚠️ Nenhum dado")
