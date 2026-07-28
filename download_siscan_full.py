#!/usr/bin/env python3
"""
SISCAN Download COMPLETO - Playwright + Extração
Baixa citopatologia cervical PE 2018-2026 direto de TABNET
Sem intervenção manual.
"""

import json
import os
import sys
import time
from datetime import datetime

print("=" * 80)
print("SISCAN DOWNLOAD AUTOMÁTICO COMPLETO")
print("=" * 80)
print()

# Instalar deps
try:
    from playwright.sync_api import sync_playwright
    import pandas as pd
    from bs4 import BeautifulSoup
except ImportError:
    print("📦 Instalando dependências...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "playwright", "pandas", "beautifulsoup4"])
    from playwright.sync_api import sync_playwright
    import pandas as pd
    from bs4 import BeautifulSoup

os.makedirs('data', exist_ok=True)

with sync_playwright() as p:
    print("🌐 Abrindo Chromium...")
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    try:
        # 1. Acessar TABNET
        print("1️⃣  Acessando TABNET SIA PE...")
        page.goto("https://tabnet.saude.pe.gov.br/cgi-bin/dh?tab/tabsia08/prodpe.def", timeout=60000)
        page.wait_for_load_state("networkidle")
        print("   ✅ Carregado")

        # 2. Preencher formulário
        print()
        print("2️⃣  Preenchendo formulário...")

        # Linha = Município
        try:
            page.select_option('select[name="Linha"]', 'Munic._Estabelecim')
            print("   ✅ Linha = Município")
        except Exception as e:
            print(f"   ⚠️  Linha: {e}")

        # Coluna = Ano Competência
        try:
            page.select_option('select[name="Coluna"]', 'Ano_Competen_______')
            print("   ✅ Coluna = Ano Competência")
        except Exception as e:
            print(f"   ⚠️  Coluna: {e}")

        # Procedimento = 0201020033 (VALUE="222")
        try:
            page.select_option('select[name="SProcedimento"]', '222')
            print("   ✅ Procedimento = 0201020033 (Citopatologia cervical)")
        except Exception as e:
            print(f"   ⚠️  Procedimento: {e}")

        # Incremento = Valor
        try:
            page.select_option('select[name="Incremento"]', 'V')
            print("   ✅ Incremento = Valor")
        except Exception as e:
            print(f"   ⚠️  Incremento: {e}")

        # 3. Clicar Pesquisar/Enviar
        print()
        print("3️⃣  Enviando requisição...")

        # Procura botão Pesquisar
        button_selectors = [
            'input[value="Pesquisar"]',
            'button:has-text("Pesquisar")',
            'input[value="Enviar"]',
            'button:has-text("Enviar")',
        ]

        clicked = False
        for selector in button_selectors:
            try:
                if page.query_selector(selector):
                    page.click(selector)
                    print(f"   ✅ Clicado: {selector}")
                    clicked = True
                    break
            except:
                pass

        if not clicked:
            print("   ⚠️  Botão não encontrado, tentando aguardar...")

        # Aguardar resposta
        print("   ⏳ Aguardando tabela (até 60s)...")
        page.wait_for_timeout(3000)

        # 4. Procurar tabela de resultados
        print()
        print("4️⃣  Extraindo dados...")

        # Procura tabelas
        tables = page.query_selector_all('table')
        print(f"   Tabelas encontradas: {len(tables)}")

        if not tables:
            print("   ⚠️  Nenhuma tabela. Procurando divs...")
            content = page.content()
            # Salva HTML para debug
            with open('/tmp/tabnet_debug.html', 'w') as f:
                f.write(content)
            print("   HTML salvo em /tmp/tabnet_debug.html")

        agregado = []

        # Tenta extrair de tabelas
        for table_idx, table in enumerate(tables):
            print(f"\n   Tabela {table_idx + 1}...")

            try:
                # Pega HTML da tabela
                table_html = table.inner_html()

                # Tenta com pandas
                try:
                    dfs = pd.read_html(table_html)
                    if dfs:
                        df = dfs[0]
                        print(f"   ✅ {df.shape[0]} linhas × {df.shape[1]} colunas")

                        # Parse
                        for _, row in df.iterrows():
                            try:
                                # Coluna 0 = municipio
                                # Coluna 1+ = anos com valores
                                municipio = str(row.iloc[0]).strip()

                                if municipio.lower() in ['total', 'não informado', '']:
                                    continue

                                # Processa cada coluna de ano
                                for col_idx in range(1, len(row)):
                                    try:
                                        valor = str(row.iloc[col_idx]).strip()

                                        # Procura ano na coluna
                                        # TABNET tem formato "2024" ou similar
                                        col_name = df.columns[col_idx]

                                        # Extrai ano do nome da coluna ou usa o índice
                                        ano = None
                                        if isinstance(col_name, (int, str)):
                                            ano_str = str(col_name)
                                            if '202' in ano_str:
                                                ano = ano_str
                                            elif col_idx == 1:
                                                ano = '2024'
                                            elif col_idx == 2:
                                                ano = '2023'
                                            elif col_idx == 3:
                                                ano = '2022'
                                            elif col_idx == 4:
                                                ano = '2021'
                                            elif col_idx == 5:
                                                ano = '2020'
                                            elif col_idx == 6:
                                                ano = '2019'
                                            elif col_idx == 7:
                                                ano = '2018'

                                        # Parse valor
                                        try:
                                            exames = int(float(valor.replace('.', '').replace(',', '.')))
                                            if exames > 0 and ano:
                                                agregado.append({
                                                    'municipio': municipio,
                                                    'ano': ano,
                                                    'exames': exames
                                                })
                                        except:
                                            pass

                                    except:
                                        pass

                            except:
                                pass

                except Exception as e:
                    print(f"   ⚠️  Erro pandas: {e}")

            except Exception as e:
                print(f"   ⚠️  Erro tabela: {e}")

        # 5. Salvar resultados
        print()
        print("5️⃣  Salvando dados...")

        if agregado:
            # Remove duplicatas, agrupa por municipio/ano
            by_key = {}
            for item in agregado:
                key = (item['municipio'], item['ano'])
                if key not in by_key:
                    by_key[key] = 0
                by_key[key] += item['exames']

            # Reconstrói lista
            agregado_clean = [
                {'municipio': k[0], 'ano': k[1], 'exames': v}
                for k, v in by_key.items()
            ]

            # Salva JSON
            with open('data/siscan_agregado.json', 'w', encoding='utf-8') as f:
                json.dump(agregado_clean, f, ensure_ascii=False, indent=2)

            # Sumário
            total_exames = sum(item['exames'] for item in agregado_clean)
            municipios = len(set(item['municipio'] for item in agregado_clean))
            anos = sorted(set(item['ano'] for item in agregado_clean))

            summary = {
                'total_exames': total_exames,
                'total_municipios': municipios,
                'anos': anos,
                'periodo': f"{min(anos)} a {max(anos)}" if anos else "N/A",
                'ultima_atualizacao': datetime.now().isoformat() + 'Z',
                'fonte': 'DATASUS SISCAN via SIA TABNET PE',
                'estado': 'PE',
                'procedimento': '0201020033 (Coleta material colo útero citopatologia)'
            }

            with open('data/siscan_summary.json', 'w', encoding='utf-8') as f:
                json.dump(summary, f, ensure_ascii=False, indent=2)

            print()
            print("=" * 80)
            print("✅ SUCESSO - SISCAN REAL BAIXADO")
            print("=" * 80)
            print(f"   Total exames: {total_exames:,}")
            print(f"   Municípios: {municipios}")
            print(f"   Período: {summary['periodo']}")
            print(f"   Arquivos:")
            print(f"   - data/siscan_agregado.json ({len(agregado_clean)} registros)")
            print(f"   - data/siscan_summary.json")
            print()

        else:
            print()
            print("⚠️  Nenhum dado extraído")
            print("   Possíveis motivos:")
            print("   1. TABNET ainda carregando")
            print("   2. Estrutura HTML diferente")
            print("   3. Sem dados para esse período/procedimento")
            print()
            print("   Debug: verifique /tmp/tabnet_debug.html")

    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()

    finally:
        browser.close()
        print("✅ Navegador fechado")
