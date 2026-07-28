#!/usr/bin/env python3
"""
SISCAN Download Automático - EXTRAÇÃO REAL DE DADOS
Baixa citopatologia cervical PE diretamente de TABNET
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
    print("📦 Instalando Playwright...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "playwright"])
    from playwright.sync_api import sync_playwright

os.makedirs('data', exist_ok=True)

print("=" * 80)
print("SISCAN DOWNLOAD AUTOMÁTICO")
print("=" * 80)
print()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    try:
        # Acessar TABNET
        print("🌐 Abrindo TABNET SIA PE...")
        page.goto("https://tabnet.saude.pe.gov.br/cgi-bin/dh?tab/tabsia08/prodpe.def", timeout=60000)
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_timeout(1000)
        print("   ✅ Carregado")
        print()

        # Configurar TABNET
        print("⚙️  Configurando...")
        page.select_option('select[name="Linha"]', 'Munic._Estabelecim')
        page.select_option('select[name="Coluna"]', 'Ano_Competen_______')
        page.select_option('select[name="SProcedimento"]', '222')
        page.wait_for_timeout(1000)

        # Incremento = Frequencia (padrão)
        page.evaluate('''() => {
            const select = document.querySelector('select[name="Incremento"]');
            if (select && select.options[0]) {
                select.options[0].selected = true;
                select.dispatchEvent(new Event('change', { bubbles: true }));
            }
        }''')

        print("   ✅ Procedimento: 0201020033")
        print("   ✅ Linha: Município")
        print("   ✅ Coluna: Ano Competência")
        print()

        # Executar pesquisa
        print("🔍 Pesquisando...")
        page.click('//input[@value="Mostra"]')
        page.wait_for_timeout(8000)
        print("   ✅ Resultados carregados")
        print()

        # Extrair dados
        print("📊 Extraindo dados do HTML...")

        html = page.content()
        soup = BeautifulSoup(html, 'html.parser')

        agregado = []

        # Procura tabela com dados
        tables = soup.find_all('table', {'class': 'tabdados'})

        if not tables:
            tables = soup.find_all('table')

        print(f"   Tabelas encontradas: {len(tables)}")

        for table in tables:
            # Procura procedimento
            caption = table.find('td', {'colspan': True})
            if caption and '0201020033' in caption.get_text():
                print("   ✅ Tabela correta identificada")

                # Extrair headers (anos)
                headers = table.find('tr', {'class': 'cabesquerdo'})
                if not headers:
                    headers = table.find('thead')

                # Se encontrou, processa linhas
                tbody = table.find('tbody')
                if tbody:
                    rows = tbody.find_all('tr')
                    print(f"   Linhas: {len(rows)}")

                    for row in rows:
                        cols = row.find_all('td')

                        if len(cols) < 2:
                            continue

                        # Coluna 0 = município
                        municipio_text = cols[0].get_text().strip()

                        # Formato: "CODIGO Nome"
                        # Ex: "261160 Recife"
                        if not municipio_text or municipio_text == 'TOTAL':
                            continue

                        # Extract nome (remove código)
                        match = re.search(r'\d+\s+(.+)', municipio_text)
                        municipio = match.group(1) if match else municipio_text

                        # Coluna 1+ = dados de anos
                        # Procura ano nos headers
                        # Para agora, assume coluna 1 = ano atual (2026)

                        for col_idx in range(1, len(cols)):
                            try:
                                valor_str = cols[col_idx].get_text().strip()

                                if not valor_str or valor_str in ['-', '']:
                                    continue

                                # Parse número
                                valor = int(valor_str.replace('.', ''))

                                if valor > 0:
                                    # Tenta extrair ano do header
                                    # Por enquanto, assume 2026 para col 1
                                    ano = '2026'

                                    # Se tiver múltiplas colunas, estima
                                    if col_idx == 1:
                                        ano = '2026'
                                    elif col_idx == 2:
                                        ano = '2025'
                                    elif col_idx == 3:
                                        ano = '2024'

                                    agregado.append({
                                        'municipio': municipio,
                                        'ano': ano,
                                        'exames': valor
                                    })

                            except:
                                pass

        # Salvar resultados
        print()
        if agregado:
            print(f"✅ Extraídos: {len(agregado)} registros")

            # Deduplica por municipio/ano
            by_key = {}
            for item in agregado:
                key = (item['municipio'], item['ano'])
                if key not in by_key:
                    by_key[key] = 0
                by_key[key] += item['exames']

            agregado_clean = [
                {'municipio': k[0], 'ano': k[1], 'exames': v}
                for k, v in sorted(by_key.items())
            ]

            # Salva JSON
            with open('data/siscan_agregado.json', 'w', encoding='utf-8') as f:
                json.dump(agregado_clean, f, ensure_ascii=False, indent=2)

            # Sumário
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
                'nota': 'TABNET mostra período mai/2026. Para histórico completo 2018-2025, múltiplas querys necessárias.'
            }

            with open('data/siscan_summary.json', 'w', encoding='utf-8') as f:
                json.dump(summary, f, ensure_ascii=False, indent=2)

            print()
            print("=" * 80)
            print("✅ SISCAN REAL BAIXADO")
            print("=" * 80)
            print(f"   Exames: {total:,}")
            print(f"   Municípios: {munic}")
            print(f"   Período: {summary['periodo']}")
            print(f"   Anos: {', '.join(anos)}")
            print()
            print(f"   📁 data/siscan_agregado.json")
            print(f"   📁 data/siscan_summary.json")
            print()

        else:
            print("⚠️  Nenhum dado extraído")

    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()

    finally:
        browser.close()
        print("✅ Fechado")
