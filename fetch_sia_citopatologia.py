#!/usr/bin/env python3
"""
Fetch citopatologia data from SIA TABNET PE via Playwright
Procedimento: 0201020033 - Coleta material colo útero para exame citopatológico
Period: 2018-2026, State: PE, Aggregation: by Municipality
"""

import json
import os
import sys
from datetime import datetime

try:
    from playwright.sync_api import sync_playwright
    import pandas as pd
except ImportError:
    print("📦 Installing dependencies...")
    import subprocess
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-q",
        "playwright", "pandas"
    ])
    from playwright.sync_api import sync_playwright
    import pandas as pd

os.makedirs('data', exist_ok=True)

print("=" * 80)
print("SISCAN CITOPATOLOGIA - SIA TABNET PE")
print("=" * 80)
print()
print("📊 Objetivo: Exames citopatológicos cervical PE 2018-2026")
print("   Procedimento: 0201020033 (Coleta material colo útero)")
print("   Agregação: por Município")
print()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Mostrar browser
    page = browser.new_page()

    try:
        # 1. Abrir TABNET SIA PE
        print("1️⃣  Abrindo TABNET SIA PE...")
        page.goto("https://tabnet.saude.pe.gov.br/cgi-bin/dh?tab/tabsia08/prodpe.def", timeout=60000)
        page.wait_for_load_state("networkidle")
        print("   ✅ Carregado")
        print()

        # 2. Selecionar Linha = Município
        print("2️⃣  Configurando: Linha = Município...")
        page.select_option('select[name="Linha"]', 'Munic._Estabelecim')
        print("   ✅ Selecionado")
        print()

        # 3. Selecionar Coluna = Ano Competência
        print("3️⃣  Configurando: Coluna = Ano Competência...")
        page.select_option('select[name="Coluna"]', 'Ano_Competen_______')
        print("   ✅ Selecionado")
        print()

        # 4. Selecionar Procedimento = 0201020033
        print("4️⃣  Selecionando procedimento citopatologia...")
        page.select_option('select[name="SProcedimento"]', '222')  # VALUE=222
        print("   ✅ 0201020033 selecionado")
        print()

        # 5. Selecionar Incremento = Valores
        print("5️⃣  Selecionando incremento = Valores...")
        page.select_option('select[name="Incremento"]', 'V')
        print("   ✅ Selecionado")
        print()

        # 6. Clicar Pesquisar
        print("6️⃣  Clicando 'Pesquisar'...")
        page.click('button:has-text("Pesquisar"), input[value="Pesquisar"]')
        page.wait_for_load_state("networkidle", timeout=60000)
        print("   ✅ Resultados carregados")
        print()

        # 7. Procurar por botão de export/download
        print("7️⃣  Procurando opção de export...")

        # Tenta diferentes seletores para botão de export
        export_selectors = [
            'a:has-text("Exportar")',
            'a:has-text("Arquivo")',
            'input[value="Arquivo"]',
            'button:has-text("Exportar")',
        ]

        exported = False
        for selector in export_selectors:
            try:
                if page.query_selector(selector):
                    print(f"   Tentando: {selector}")
                    page.click(selector)
                    page.wait_for_timeout(2000)
                    exported = True
                    print(f"   ✅ Clicado")
                    break
            except:
                pass

        if not exported:
            print("   ⚠️  Botão export não encontrado")
            print("   Alternativa: selecione formato (CSV) e clique manualmente")

        # 8. Procurar por dados na página
        print()
        print("8️⃣  Procurando dados de municípios...")
        content = page.content()

        municipios_encontrados = []
        for m in ['Recife', 'Olinda', 'Caruaru', 'Jaboatao', 'Pernambuco']:
            if m in content:
                municipios_encontrados.append(m)

        if municipios_encontrados:
            print(f"   ✅ Encontrados: {', '.join(municipios_encontrados)}")
        else:
            print("   ⚠️  Nenhum município detectado em HTML")

        # 9. Tentar extrair tabela
        print()
        print("9️⃣  Tentando extrair dados da tabela...")

        tables = page.query_selector_all('table')
        if tables:
            print(f"   ✅ Encontradas {len(tables)} tabela(s)")

            # Tenta extrair primeira tabela
            try:
                # Lê HTML da tabela
                table_html = tables[0].inner_html()

                if len(table_html) > 500:
                    print(f"   ✅ Tabela tem {len(table_html)} bytes de conteúdo")

                    # Tenta com pandas
                    try:
                        df = pd.read_html(table_html)[0]
                        print(f"   ✅ DataFrame: {df.shape[0]} linhas × {df.shape[1]} colunas")

                        # Salva CSV
                        df.to_csv('data/siscan_citopatologia_raw.csv', index=False)
                        print(f"   ✅ Salvo: data/siscan_citopatologia_raw.csv")

                    except:
                        print("   ⚠️  Não conseguiu fazer parse automaticamente")
            except:
                pass

        print()
        print("=" * 80)
        print("✅ TABNET ABERTO - Agora:")
        print("   1. Escolha formato de arquivo (CSV/Excel)")
        print("   2. Clique 'Arquivo'/'Exportar'")
        print("   3. Salve como: data/siscan_manual.csv")
        print("=" * 80)

        # Manter navegador aberto
        print()
        print("⏳ Navegador aberto para ação manual...")
        print("   Pressione ENTER para fechar")
        input()

    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()

    finally:
        browser.close()
        print("✅ Fechado")
