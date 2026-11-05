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

Stránka nemá skripty ani měření návštěvnosti a nenačítá nic z cizích serverů.

## Licence

Zatím neurčena. Text i kód jsou chráněné autorským právem, dokud autor nezvolí licenci.
