# -*- coding: utf-8 -*-
"""Postavi index.html ze studie.md. Markdown se prevadi mistne, nic se nestahuje.

   python -I build.py

Potrebuje markdown-it-py (pip install markdown-it-py). Stranka nema zadne skripty,
pisma ani mereni navstevnosti z cizich serveru: vsechno je v teto slozce.

studie.md je kopie verejne verze studie (Apps/_docs/zradci-analyza/STUDIE-verejna.md),
ktera prosla branou B2. Text se upravuje tam a sem se jen kopiruje.
"""
import html
import io
import os
import re
import unicodedata

from markdown_it import MarkdownIt

ZDE = os.path.dirname(os.path.abspath(__file__))
ADRESA = "https://sokiicz.github.io/zradci-studie/"
TITULEK = "Dá se Turingovou metodou odhalit Zrádce? Kompletní studie"
POPIS = ("Dá se Zrádce najít počítáním? Pokus o replikaci postupu Hannah Fry na 20 sériích Zrádců "
         "z pěti zemí: data, metoda, výsledky, naše chyby a čemu se nedá věřit.")
OBRAZEK = ADRESA + "assets/nahled.png"
OBRAZEK_POPIS = "Dá se Zrádce spočítat? 20 sérií, 5 zemí"
AUTOR_IG = "https://www.instagram.com/johny_plesh/"

# holá adresa v textu se stane odkazem; tečka nebo čárka za ní do adresy nepatří
URL = re.compile(r"(?<![<\w])(https?://[^\s<>()]*[^\s<>().,;:!?“”\"'])")

SABLONA = """<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulek}</title>
<meta name="description" content="{popis}">
<link rel="canonical" href="{adresa}">
<meta property="og:title" content="{titulek}">
<meta property="og:description" content="{popis}">
<meta property="og:type" content="article">
<meta property="og:url" content="{adresa}">
<meta property="og:image" content="{obrazek}">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="720">
<meta property="og:image:alt" content="{obrazek_popis}">
<meta property="og:site_name" content="Zrádci: kompletní studie">
<meta property="og:locale" content="cs_CZ">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{titulek}">
<meta name="twitter:description" content="{popis}">
<meta name="twitter:image" content="{obrazek}">
<meta name="twitter:image:alt" content="{obrazek_popis}">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<main class="studie">
{obsah}
</main>
<footer class="paticka">
<p>Autor na Instagramu: <a href="{autor_ig}">@johny_plesh</a></p>
</footer>
</body>
</html>
"""


def slug(text):
    s = unicodedata.normalize("NFD", text.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-") or "oddil"


def odkazy(text):
    """Holé adresy na odkazy (<adresa>), ale ne uvnitř `kódu`."""
    casti = text.split("`")
    if len(casti) % 2 == 0:
        raise SystemExit("lichý počet zpětných apostrofů ve studie.md, kód by se rozbil")
    for i in range(0, len(casti), 2):
        casti[i] = URL.sub(r"<\1>", casti[i])
    return "`".join(casti)


def main():
    text = io.open(os.path.join(ZDE, "studie.md"), encoding="utf-8").read()
    md = MarkdownIt("commonmark").enable("table")
    env = {}
    tokeny = md.parse(odkazy(text), env)

    # nadpisy dostanou kotvy, oddíly (h2) jdou do obsahu
    pouzite, obsah = set(), []
    for i, t in enumerate(tokeny):
        if t.type != "heading_open":
            continue
        nazev = tokeny[i + 1].content
        kotva, n = slug(nazev), 2
        while kotva in pouzite:
            kotva, n = "%s-%d" % (slug(nazev), n), n + 1
        pouzite.add(kotva)
        t.attrSet("id", kotva)
        if t.tag == "h2":
            obsah.append((kotva, nazev))

    telo = md.renderer.render(tokeny, md.options, env)
    telo = telo.replace("<table>", '<div class="tabulka"><table>').replace("</table>", "</table></div>")
    # tabulky typu „klíč | hodnota“ mají ve studii prázdnou hlavičku; prázdný pruh nezobrazovat
    telo = re.sub(r"<thead>\s*<tr>\s*(?:<th></th>\s*)+</tr>\s*</thead>\s*", "", telo)

    # obsah za podtitul (první odstavec pod hlavním nadpisem)
    nav = ['<nav class="obsah" aria-label="Obsah"><p class="obsah-nadpis">Obsah</p><ul>']
    for kotva, nazev in obsah:
        nav.append('<li><a href="#%s">%s</a></li>' % (kotva, html.escape(nazev)))
    nav.append("</ul></nav>")
    konec_h1 = telo.index("</h1>")
    za_podtitulem = telo.index("</p>", konec_h1) + len("</p>")
    telo = telo[:za_podtitulem] + "\n" + "\n".join(nav) + telo[za_podtitulem:]

    stranka = SABLONA.format(
        titulek=html.escape(TITULEK), popis=html.escape(POPIS), adresa=ADRESA, obrazek=OBRAZEK,
        obrazek_popis=html.escape(OBRAZEK_POPIS), autor_ig=AUTOR_IG, obsah=telo)
    io.open(os.path.join(ZDE, "index.html"), "w", encoding="utf-8", newline="\n").write(stranka)
    print("zapsano index.html (%d oddílů, %d znaků)" % (len(obsah), len(stranka)))


if __name__ == "__main__":
    main()
