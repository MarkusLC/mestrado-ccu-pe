#!/usr/bin/env python3
"""Mede a extensão real em páginas das versões de submissão.

O que vincula nos editais é página, não palavra: 10 páginas na Fiocruz
incluindo as referências, 6 na UPE excluída a capa — em A4, Times New Roman 12,
espaçamento 1,5. Contar palavras é proxy; isto renderiza e conta.

Uso:
    python3 conta_paginas.py
"""

import sys
from pathlib import Path

from markdown_it import MarkdownIt
from playwright.sync_api import sync_playwright

DIR = Path(__file__).parent / "docs" / "preprojeto"
SAIDA = Path("/tmp/preprojeto_pdf")

# A formatação que os editais especificam. Margens de 2,5 cm são o padrão ABNT
# para trabalhos acadêmicos; nenhum dos dois editais as fixa, então esta é a
# hipótese conservadora.
CSS = """
@page { size: A4; margin: 2.5cm; }
body {
  font-family: "Times New Roman", Times, serif;
  font-size: 12pt;
  line-height: 1.5;
  text-align: justify;
  color: #000;
}
h1 { font-size: 14pt; margin: 18pt 0 10pt; }
h2 { font-size: 13pt; margin: 15pt 0 8pt; }
h3 { font-size: 12pt; margin: 12pt 0 6pt; }
p { margin: 0 0 8pt; text-indent: 1.25cm; }
li { margin-bottom: 4pt; }
table { border-collapse: collapse; width: 100%; font-size: 10pt; margin: 8pt 0; }
th, td { border: 1px solid #999; padding: 3pt 5pt; text-align: left; }
code { font-family: "Courier New", monospace; font-size: 10pt; }
"""

# `corta_capa`: o edital da UPE exclui a capa da contagem, então o bloco antes
# da primeira seção numerada sai antes de medir. O da Fiocruz conta tudo.
ALVOS = [
    ("SUBMISSAO-FIOCRUZ.md", 10, False, "Fiocruz — 10 páginas incluindo referências"),
    ("SUBMISSAO-UPE.md", 6, True, "UPE anônima — 6 páginas excluída a capa"),
    ("SUBMISSAO-UPE-IDENTIFICADA.md", 6, True, "UPE identificada — 6 páginas excluída a capa"),
]


def mede(md_path, pw, corta_capa=False):
    texto = md_path.read_text(encoding="utf-8")
    if corta_capa:
        marca = texto.find("\n## ")
        if marca > 0:
            texto = texto[marca:]
    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    html = f"<style>{CSS}</style>\n" + md.render(texto)
    pdf = SAIDA / (md_path.stem + ".pdf")

    pg = pw.new_page()
    pg.set_content(html, wait_until="load")
    pg.pdf(path=str(pdf), format="A4", print_background=False,
           margin={"top": "2.5cm", "bottom": "2.5cm", "left": "2.5cm", "right": "2.5cm"})
    pg.close()

    # contagem de páginas direto do PDF: cada página é um objeto /Type /Page
    dados = pdf.read_bytes()
    n = dados.count(b"/Type /Page") - dados.count(b"/Type /Pages")
    return n, pdf


if __name__ == "__main__":
    SAIDA.mkdir(exist_ok=True)
    problema = False
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context()
        print(f"{'arquivo':34s} {'páginas':>8s} {'limite':>7s}  situação")
        for nome, limite, corta, desc in ALVOS:
            caminho = DIR / nome
            if not caminho.exists():
                print(f"{nome:34s} {'—':>8s} {limite:>7d}  arquivo ausente")
                continue
            n, pdf = mede(caminho, ctx, corta)
            ok = n <= limite
            problema |= not ok
            print(f"{nome:34s} {n:>8d} {limite:>7d}  {'ok' if ok else f'EXCEDE em {n - limite}'}")
        ctx.close()
        b.close()
    print(f"\nPDFs em {SAIDA}")
    sys.exit(1 if problema else 0)
