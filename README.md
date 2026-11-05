# Zrádci: kompletní studie

Dá se Zrádce najít počítáním? Kompletní studie k videu o Zrádcích: pokus o replikaci
postupu Hannah Fry na 20 sériích pořadu z pěti zemí, data, metoda, výsledky, naše chyby
a čemu se nedá věřit.

Stránka: https://sokiicz.github.io/zradci-studie/

Výpočty, kód a text připravila AI (Claude) podle autorových otázek a rozhodnutí. Podrobně
to popisuje rámeček „Kdo studii připravil“ na začátku studie. Neoficiální analýza, která
s pořadem, s televizí Prima ani s BBC nesouvisí.

## Jak se stránka staví

Text studie je v `studie.md`. Stránku `index.html` z něj postaví:

```bash
pip install markdown-it-py
python -I build.py
```

Stránka nemá skripty ani měření návštěvnosti a nenačítá písma, obrázky ani kód z cizích serverů. Hostuje ji GitHub Pages, který jako každý hosting vidí adresy (IP) návštěvníků. Odkazy na jiné weby (Instagram, YouTube, zdroje) se načtou, až když na ně kliknete.

## Licence

Zatím neurčena. Všechna práva vyhrazena, dokud autor nezvolí licenci.
