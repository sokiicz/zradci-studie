# Dá se Turingovou metodou odhalit Zrádce?

**Kompletní studie · 27. 10. 2026 · přepočítáno 2. a 3. 11. 2026 po oponentuře · veřejná verze 5. 11. 2026**

Pokus o replikaci a rozšíření analýzy, kterou Hannah Fry předvedla na britských *The Traitors* ve videu „How would Alan Turing have played the Traitors?“, a ke které vydal vlastní video Matt Parker (Stand-up Maths): „Did Hannah Fry crack The Traitors?“. Její postup známe jen z rozborů a zpráv, ne z videa samotného (oddíl 8). Adresy obou videí a ostatních zdrojů jsou v oddílu 10.

Tohle je plná verze studie k našemu videu o Zrádcích. Je v ní i to, co se do videa nevešlo,
včetně chyb, které jsme cestou udělali (oddíly 7 a 7b), a toho, čemu se nedá věřit (oddíl 8).

> **Kdo studii připravil.** Nápad není náš: je Hannah Fry a lidí, se kterými ho připravovala.
> Otázky, námitky a rozhodnutí, co a jak měřit, jsou autorovy. Výpočty, kód a text studie
> připravila podle jeho zadání umělá inteligence (Claude od firmy Anthropic). Když píšeme
> „my", myslíme autora a AI, která pro něj počítala. Kritický posudek, kterému tu říkáme
> **oponentura**, napsala také AI (Claude), spuštěná zvlášť v roli oponenta s úkolem najít
> v projektu chyby. Není to lidský recenzent. I kontrolu textu před zveřejněním, na kterou
> se studie odvolává v oddílech 7b a 8, dělala AI v roli revizora. Kde chybu našel autor,
> oponentura nebo kontrola textu, píšeme to u ní. Komentář ve videu namluvila AI klonem
> autorova hlasu (ElevenLabs). Hudbu a zvuky ve videu složil program, který napsala AI.
> Upozornění: studie prozrazuje, kolik hráčů a Zrádců zbývalo ve 3. české řadě po 6. a 7. dílu. Jména žádná.

> **Co se změnilo 2. 11. 2026.** Oponentura celý projekt zkritizovala a autor zadal opravy:
> opravit hlasy, doplnit konec britské série, znovu změřit, kde v dílu je kulatý stůl
> (bývá i dřív než v druhé půlce), a předělat zbytek. Hlavní změny:
> - parser Wikipedie přehlédl čtyři naverbované Zrádce, jejich hlasy z doby, kdy byli Věrní,
>   se počítaly jako hlasy Zrádců (oddíl 7, chyba 8);
> - Fryina série je teď celá (10 dílů, skončila 30. 10.);
> - „poslední čtvrtina dílu" se už nevydává za kulatý stůl; skutečné okno stolu je změřené
>   z titulků a závěr o konkláve (scénách Zrádců mezi sebou) je **opačný** než dřív (oddíl 8);
> - všechna čísla jsou z jednoho společného přepočtu, výpisy mají v hlavičce datum
>   a otisk dat.
> Hlavní závěry studie se tím nemění. Mění se několik čísel a jeden dílčí závěr.

Studie má tři části, které vznikly postupně a každá odpovídá na jinou otázku:

1. **Hlasování** — dá se Zrádce poznat podle toho, jak hlasuje? *(20 sérií z pěti zemí)*
2. **Zmínky v titulcích** — dá se poznat podle toho, kolik se o něm mluví? *(3 české řady)*
3. **Hlavní test** — naučit se obojí na českých řadách 1 a 2 a pustit to na řadu 3 (slepé pro váhy, ne pro návrh měření; oddíl 8),
   kterou model nikdy neviděl. Včetně Fryiných „vesmírů", tedy celých skupin Zrádců.

---

## Shrnutí na jednu stránku

| Co | Výsledek |
|---|---|
| **Hlasování** | Signál v datech je, ale **mimo trénink je bezcenný** a v Česku míří u plané volby obráceně |
| **Zmínky v titulcích** | **Funguje.** Mimo trénink AUC 0,81–0,90, a to ve všech třech řadách |
| **Oslovení (5. pád)** | **Nic.** AUC 0,54, p = 0,68 |
| **Vesmíry (skupiny)** | **Nestabilní.** Na 3. řadě dvojice 1. z 91 a po 7. dílu znovu 1. z 66, na 1. řadě ale 67. ze 78 (vše se zmínkami; bez zmínek 72. ze 78, oddíl 6) |
| **Kde v dílu** | U samotného kulatého stolu je signál zmínek slabý a neprůkazný, nejsilnější je **po stole** (kde je i noční scéna Zrádců) |
| **Celkový verdikt** | Jako nástroj pro hráče **ne**. Jako postřeh o tom, komu pořad dává prostor, **ano** |

**Nejdůležitější jediná věta:** to, co v našem provedení funguje, není Turingova matematika na hlasování —
je to prosté „o kom se mluví". A ani u toho nevíme jistě, jestli měříme hru, nebo střih.

---

## 1. Data

### Hlasovací část

| | |
|---|---|
| Zdroj | tabulky hlasování na Wikipedii (cs i en), `Special:Export` |
| Rozsah | **20 sérií z pěti zemí** — Británie 1–4 a Celebrity 1–2, USA 1–4, Austrálie 1–3, Kanada 1–4, Česko 1–3 |
| Objem | 438 hráčů, 2 689 hlasů ve 202 kolech (kola s aspoň šesti hlasujícími) |
| Stav | Fryina série (Celebrity 2) celá, 10 dílů, stažená znovu 2. 11. 2026; česká 3. řada do 7. dílu |
| Naverbovaní Zrádci | 28 v 17 sériích (a 61 Zrádců od začátku); do naverbování se počítají jako Věrní. Parser od 2. 11. hlásí poznámku o naverbování, ke které nenašel hráče |
| Chybí | Nový Zéland (na anglické Wikipedii nemá samostatné stránky) |

### Zmínky z titulků

| | |
|---|---|
| Zdroj | skryté titulky pro neslyšící k dílům zveřejněným na iprima.cz (Prima+), formát WebVTT |
| Rozsah | **české řady 1–3, 31 epizod** (12 + 12 + 7), 69 hráčů, 14 Zrádců |
| Objem | asi 2 MB textu, **26 835 titulků** |

**Video dílů jsme nestahovali a žádnou ochranu jsme neobcházeli.** Použili jsme jen text titulků pro neslyšící, obraz ani zvuk dílů jsme nezpracovávali.

---

## 2. Metoda

### Turingův „ban"

Váha jednoho signálu je `log₁₀( P(signál | Zrádce) / P(signál | Věrný) )`. Jeden ban znamená
„desetkrát pravděpodobnější u Zrádce". Váhy se sčítají, protože se sčítají logaritmy — to je
celý Turingův trik z Bletchley Parku.

**Pozor na jednotku.** Fryiny zveřejněné body (+0,47 za planou volbu, −1,28 za to, že někdo nehlasoval
na odhaleného Zrádce, −1,73 za snídani s ním) nejsou v banech. Podle rozboru jejího videa
(Ed Jefferson) počítá přirozený logaritmus poměru, ne logaritmus o základu 10. Sedí to na
jejích vlastních číslech: `ln(23,5 / 14,6) = 0,476`. Přepočteno na bany je jejích +0,47
rovno **+0,204 banu**. Starší verze téhle studie obě jednotky porovnávala přímo, a tím
rozdíl proti našim váhám zhruba ztrojnásobila.

Všechny pravděpodobnosti jsou vyhlazené Jeffreysovým `α = 0,5`, aby nulový počet nedělal
nekonečné váhy.

### Hlasovací signály

Každý hlas se zařadí do jedné ze čtyř kategorií podle toho, co se v kole stalo:

| Kategorie | Kdy |
|---|---|
| A | hlas na člověka, který byl vyhoštěn a ukázal se jako Zrádce |
| B | hlas na člověka, který byl vyhoštěn a byl Věrný |
| C | planá volba — terč dostal nejvýš jeden hlas, zatímco jiný měl tři a víc |
| D | ostatní |

Kola s méně než šesti hlasujícími se vynechávají jako endgame, ne kulatý stůl.

### Zmínkový signál

Pro každou epizodu: podíl zmínek hráče na všech zmínkách lidí, kteří jsou v té epizodě
ještě ve hře, dělený rovnoměrným podílem `1/n`. **Hodnota 1,00 = mluví se o něm přesně
tolik, kolik vychází náhodou.** Poměr se zařadí do jednoho ze čtyř pásem (hranice 0,5 / 1 / 2,
dané předem) a pásmu se přiřadí váha v banech.

Skóre hráče je **průměr** banů na epizodu, ne součet — jinak by vyhrával ten, kdo přežil déle.

### Vesmíry (Banburismus)

Místo hodnocení jednotlivců se vyjmenují **všechny možné skupiny Zrádců** mezi aktivními
hráči a každá se ohodnotí věrohodností. Z toho se spočítá, jak pravděpodobné je u každého
jednotlivce, že je Zrádce. Je to přesně to, co dělala Fry a co dělal Turing s možnými
nastaveními Enigmy.

Věrohodnost jednoho vesmíru = hlasovací váhy jeho členů + párový člen (jak často míří hlas
na Zrádce proti náhodě) + zmínkové bany jeho členů.

---

## 3. Výsledky: hlasování (20 sérií)

| Zjištění | Číslo |
|---|---|
| Věrní vyhostili Zrádce | **63 ze 180 hlasování** (35,0 %), náhoda dává 39,0 (21,7 %), p = 0,0001 |
| Zrádci hlasují na Zrádce | **1,52×** častěji, než dovoluje nabídka terčů |
| Věrní hlasují na Zrádce | 1,20× |
| Nejsilnější váha našeho modelu | **+0,076 banu** (Fryino +0,47 je +0,204 banu, viz jednotky) |
| Nejsilnější váha vůbec, v našem čtení Fryiny definice plané volby | **+0,281 banu** na britských řadách, p = 0,145 |
| Křížové ověření (nauč na 19, testuj na vynechané) | AUC **0,554**, lepší než náhoda u 13 z 20 sérií (náhodou čekáme 10; znaménkový test p ≈ 0,26) |
| Vesmíry přes všech 20 sérií | skutečná skupina v horních **49,7 %** (náhoda 50 %) |

**Výklad.** Signál v datech prokazatelně je — Věrní vyhostili Zrádce výrazně častěji, než by
dávala náhoda, a to není sporné. Nejsilnější váha našeho čtyřkategoriového modelu je
+0,076 banu; Fryino nejsilnější zveřejněné kladné číslo je po přepočtu +0,204 banu, tedy
**skoro třikrát víc**. Když se její definice plané volby zreplikuje tak, jak ji čteme
(oddíl 3b), vyjde na britských řadách +0,281 banu, tedy ještě o něco víc než u ní — jenže
na 208 hlasech a s p = 0,145. Žádné z těch čísel nestačí na rozhodnutí o konkrétním
člověku. AUC 0,554 je skoro náhoda.

> **Opraveno 2. 11. 2026.** Před opravou naverbovaných Zrádců a doplněním Fryiny série tu
> stálo AUC 0,573 a lepší než náhoda u 15 z 20 sérií. Fryina série sama klesla z 0,507 na
> 0,400. Tehdejší „p = 0,04" výpis neuvádí; sedí na oboustranný znaménkový test pro 15 z 20
> (0,041), tedy nejspíš vznikl tak. Pro 13 z 20 dává tentýž test 0,26.

**Zrádci jedou s davem.** Hlas na toho, kdo u stolu nakonec odejde, dají v **50,9 %**
případů, Věrní v **44,9 %** (p = 0,013, permutace hlasů uvnitř kola). Je to menší rozdíl než
u předchozího řádku, ale vyšel průkazně a dává smysl: Zrádce si nemůže dovolit být jediný, kdo
hlasuje jinak, tak se přidá k většině a nechá ostatní vybrat za sebe. (Pozor na počet testů,
oddíl 8: tenhle by přísnou opravu na mnohonásobné testování nepřežil.)

> **Opraveno 30. 10. 2026 po vlastním auditu.** Dřív tu stálo 46,0 % proti 41,0 % (p = 0,040),
> protože se signál počítal přes všech 200 kol včetně **23 kol, ve kterých nikdo vyhoštěn
> nebyl** (266 hlasů). Takový hlas ale není netrefa, je to jiná situace, a obě procenta
> stlačoval dolů. Po omezení na kola s vyhoštěním vychází nález **silněji**, ne slaběji.

**Vedlejší zjištění, u kterého je potřeba dát pozor na sílu:** dvojice dvou Zrádců na sebe
hlasuje v **20,8 %** případů, smíšená ve 14,4 % a dva Věrní v 11,3 %. Na českých řadách je
rozdíl nejvýraznější (26,0 % proti 10,8 %). Směr tedy jde proti představě, že se Zrádci
kryjí. **Průkazné to ale není:** p = 0,23 přes všech 20 sérií a p = 0,26 na českých řadách,
kde je dvojic dvou Zrádců jen 50 (přes všech 20 sérií 504). Je to zajímavý směr, ne doložený
nález, a tak se o něm má mluvit. (Před opravou dat 2. 11. tu stálo p = 0,103.)

---

## 3b. Fryiných šest signálů, replikovaných

Autor 29. 10. 2026: *„nemyslím si, že to byl jediný faktor, který zohledňovala.. projeď to
její původní video a to dodatečné vysvětlující video od stand up math ještě jedou a zcheckni,
co reálně řeší"*

Měl pravdu a starší verze téhle studie to měla zjednodušené. Podle rozboru videa
*How would Alan Turing have played the Traitors?* (rozbor Eda Jeffersona a zpravodajství,
zdroje v oddílu 10) boduje Fry **šest** věcí, ne jednu:

| # | Co Fry boduje | Umíme změřit? |
|---|---|---|
| 1 | planá volba | ano |
| 2 | hlas na Zrádce v kole, kdy byl vyhoštěn | ano |
| 3 | …a nikdy předtím na něj nehlasoval | ano |
| 4 | nehlasování na Zrádce v kole, kdy byl vyhoštěn | ano |
| 5 | v minulosti na hráče hlasoval Zrádce, který už je vyhoštěný | ano |
| 6 | byl v poslední skupině u snídaně se Zrádcem, který byl později vyhoštěn | **ne** |

Šestý se z veřejných tabulek hlasování spočítat nedá; kdo s kým seděl u snídaně, je jen ve
vysílání. Zbylých pět jsme spočítali.

### Replikace její plané volby

Fry planou volbu nepočítá přes celý pořad. Jak přesně ji vymezuje, víme jen z druhé ruky
(zdroje v oddílu 10): **jen první tři kulaté stoly** a 23,5 % proti 14,6 % na 205 hlasech uvádí
rozbor Eda Jeffersona, **jen kola, ve kterých odešel Věrný** píše jen novinářka The Tab
(22. 10. 2026) a sama Fry podle PinkNews mluví o „prvních třech epizodách". Říkáme tomu
proto „naše čtení její definice". Když se to vezme takhle:

| | Zrádci | Věrní | poměr | nat | ban | příležitostí | p |
|---|---|---|---|---|---|---|---|
| britské řady, naše čtení Fryiny definice | **24,3 %** | 12,9 % | 1,89 | +0,648 | +0,281 | 208 | 0,145 |
| britské řady, naše širší definice | 17,0 % | 13,2 % | 1,29 | +0,257 | +0,112 | 926 | 0,291 |
| **české řady, naše čtení Fryiny definice** | 5,0 % | 10,9 % | 0,46 | −0,454 | −0,197 | 139 | 0,515 |
| **české řady, jen kola s vyhoštěným Věrným** | **2,4 %** | 11,6 % | 0,21 | −1,196 | −0,519 | 256 | **0,036** |

**Fryinu číslu jsme blízko.** Ona podle Jeffersona uvádí 23,5 % u Zrádců na 205 hlasech,
nám vychází 24,3 % na 208 hlasech. U Věrných uvádí 14,6 %, nám vyšlo 12,9 %. Jefferson sám
napočítal 24 % proti 15,6 %. (Před opravou naverbovaných Zrádců 2. 11. nám vycházelo 23,7 %.)

Z toho plynou tři věci, a žádná z nich není, že by počítala špatně:

1. **Na definici záleží víc než na datech.** Tatáž data, jen širší definice, a poměr spadne
   z 1,89 na 1,29.
2. **Ani v její definici to není průkazné.** Po obou zúženích zbývá 208 hlasů a p = 0,145.
3. **Na českých řadách to jde na opačnou stranu, a tam průkazně.** V kolech, kde odešel
   Věrný, dělají naši Zrádci planou volbu skoro pětkrát méně často než Věrní (p = 0,036).
   Průkazné je to ale jen u tohoto jednoho způsobu počítání a jen na 256 hlasech.

### Zbylé čtyři signály

| signál | Británie | Česko | všech 20 sérií | p (20 sérií) |
|---|---|---|---|---|
| 2 hlas na odhaleného Zrádce | −0,068 | −0,113 | −0,074 | 0,109 |
| 3 …a až teď poprvé | −0,053 | −0,096 | −0,068 | 0,219 |
| 4 nehlasoval na odhaleného Zrádce | +0,033 | +0,153 | +0,060 | 0,153 |
| 5 v minulosti na něj hlasoval Zrádce | −0,149 | **+0,242** | +0,120 | 0,439 |

(v banech; kladné číslo = častější u Zrádců)

**Žádný z nich nevyšel průkazně.** Signál 5 míří v Česku na opačnou stranu než v Británii.
U signálu 4 je **znaménko nejisté**. Fry podle zpravodajství dává za nehlasování na
odhaleného Zrádce −1,28 bodu. Jestli záporný bod znamená „spíš Věrný", žádný zdroj u tohoto
bodu výslovně neříká; Jefferson píše jen obecně, že víc bodů znamená spíš Zrádce
(oddíl 10). **Pokud** to tak je, vychází nám opačné znaménko: u nás je
nehlasování slabě na stranu viny, na britských řadách nejslabší (+0,033).

**Výhrada k tomuhle oddílu.** Signály 2 až 5 jsou definované pomocí role, která se odhalí až
vyhoštěním. Permutační test proto prohazuje nálepky mezi hráči a definici signálu nechává
být; je to standardní label-permutation, ale není to totéž co test na předpovědi dopředu.

---

## 4. Výsledky: zmínky v titulcích (3 české řady)

| | Zrádci | Věrní | v banech | AUC | p |
|---|---|---|---|---|---|
| celá epizoda | **1,58** | 0,89 | +0,25 | 0,72 | 0,024 |
| poslední čtvrtina epizody | **1,92** | 0,83 | **+0,36** | 0,75 | 0,047 |
| oslovení (5. pád) | 1,13 | 0,98 | +0,06 | 0,54 | 0,68 |

Po řadách (poslední čtvrtina):

| řada | Zrádci | Věrní | AUC |
|---|---|---|---|
| 1. řada (12 epizod, 5 Zrádců) | 1,50 | 0,91 | 0,71 |
| 2. řada (12 epizod, 6 Zrádců) | 2,23 | 0,77 | 0,77 |
| 3. řada (7 epizod, 3 Zrádci) | 2,11 | 0,82 | 0,80 |

**Poslední čtvrtina není kulatý stůl.** Do 2. 11. tu stálo „poslední čtvrtina (kulatý
stůl)". Oponentura ukázala, že na konci dílu je i noční scéna Zrádců a že kulatý stůl bývá
i v první polovině dílu. Skutečné okno stolu z titulků je v oddílu 8.

Čísla se po opravě titulků 2. 11. (oddíl 7, chyba 10) pohnula jen v setinách.

**Zmínkový signál je skoro pětkrát silnější než nejsilnější váha našeho hlasovacího modelu**
(+0,364 proti +0,076 banu) a zhruba o třetinu silnější než planá volba v našem čtení Fryiny
definice na britských řadách (+0,281 banu). Opakuje se ve všech třech řadách; první řada je
slabší než zbylé dvě.

### Sonda: oslovení 5. pádem, a proč je jeho selhání důležité

Chtěli jsme „kdo koho obviňuje". Na to titulky nestačí: **nemají jmenovky mluvčích.**
Střídání mluvčích značené je (asi třetina titulků začíná pomlčkou), ale to říká jen
„promluvil někdo jiný", ne kdo.

Čeština ale nabízí náhradu. Když někdo použije jméno v 5. pádě, tedy v tvaru, kterým se
v češtině volá, je to **přímé oslovení** — kontakt tváří v tvář, ne zmínka za zády.

**Výsledek je nula.** AUC 0,54, p = 0,68; po vyloučení epizody odchodu jsou Zrádci v 1. řadě
dokonce *pod* Věrnými.

**Jak silný ten test vlastně je.** Autor 29. 10. 2026: *„myslím si, že se hráči navzájem
velmi oslovují, i zrádce, prootže spolu furt mluví. otázka ale je, jak se to dostane do
střihu"*. Je to správná námitka a nula sama o sobě neznamená, že se to neděje. Oslovení je
v titulcích vzácné: **639 oslovení na 4 728 zmínek** (13,5 %) a **u 479 ze 713 řádků
hráč-epizoda (67 %) nepadne ani jedno**. (Níž v textu stojí 53 % — to je tentýž jev
měřený na jiném jmenovateli: jen na hráčích, kteří v dané epizodě ještě hráli,
a v epizodách, kde vůbec nějaké oslovení padlo.)

Proto jsme spočítali sílu testu: nasimulovali jsme efekt dané velikosti na skutečném
rozdělení počtů a zjistili, jak často ho permutační test při našem vzorku zachytí.

| skutečný efekt | test ho najde (p < 0,05) |
|---|---|
| žádný rozdíl | 4 % (to je hladina testu, sedí) |
| o pětinu víc | 15 % |
| o polovinu víc | 36 % |
| **jako u zmínek (1,58 / 0,90, tedy 1,76×)** | **46 %** |
| dvojnásobek | 60 % |
| dva a půl násobek | 80 % |

(Přepočteno 2. 11. s pevným pořadím hráčů, oddíl 7, chyba 11; dřív 6, 16, 33, 49, 66, 81 %.)

**A nejspíš to ani neměří hráče.** Autor 29. 10. 2026: *„btw hodně oslovení v 5. pádu
bude od hradního pána“*. Je to oprávněná námitka. Vzorek z titulků ji dokládá:
„(jméno), předstup“, „(jméno), pokračuješ“, „(jméno), řada je na tobě“ (jména hráčů
vynechána) — to všechno říká moderátor, když u stolu vyvolává. Rozlišit to nejde, protože
titulky nemají jmenovky mluvčích; hrubý odhad z kontextu najde formuli moderátora
u 14 % oslovení a řeč hráče u 12 %, zbytek nerozhodne. Měřeno tedy není podezření, ale
z velké části pořad sám.

Zkusili jsme to podepřít i druhou cestou: kdyby moderátor rozdával oslovení podle pořadí,
měla by mít rovnoměrnější rozdělení než zmínky. **Nevyšlo to** — oslovení mají rozptyl
větší (směrodatná odchylka 1,73 proti 0,94 u zmínek v celé epizodě), protože 53 % hodnot je
nula. Hypotéza tedy neplatí a jako doklad se nepoužívá.

**Takže nulový výsledek u 5. pádu nedokazuje, že se nic neděje.** I efekt stejně velký jako
u zmínek bychom tímhle testem zachytili v méně než polovině případů. Je to málo dat, ne nález.
Tvrzení dřívější verze, že *„kdyby hráči Zrádce podezírali, muselo by se to projevit právě
tam"*, neplatí a je odtud pryč.

---

## 5. Hlavní test: naučit na řadách 1 a 2, pustit na řadu 3 (slepé pro váhy, ne pro návrh měření; oddíl 8)

Všechno předchozí bylo buď popisné, nebo křížově ověřené jen na hlasování. **Tohle je jediný
poctivý test celého postupu**: váhy se učí výhradně na českých řadách 1 a 2 a pak se bez
jakékoli úpravy pustí na řadu 3.

### Co se model naučil (jen z řad 1 a 2)

**Hlasovací váhy** — všechny mizivé, žádná nepřesahuje desetinu banu:

| kategorie | Zrádci | Věrní | banů |
|---|---|---|---|
| A, hlas na vyhoštěného Zrádce | 10 | 58 | **−0,084** |
| B, hlas na vyhoštěného Věrného | 20 | 85 | +0,042 |
| C, planá volba | 4 | 27 | −0,124 |
| D, ostatní | 16 | 67 | +0,051 |

Párový násobitel: Zrádce 2,82×, Věrný 1,73×.

**Zmínkové váhy** — řádově silnější:

| pásmo | Zrádci | Věrní | banů | 95% interval (bootstrap přes hráče) |
|---|---|---|---|---|
| pod 0,5 | 7 | 110 | **−0,503** | −0,80 až −0,26 |
| 0,5–1 | 9 | 66 | −0,179 | −0,63 až +0,06 |
| 1–2 | 25 | 58 | +0,305 | +0,05 až +0,48 |
| nad 2 | 14 | 28 | **+0,372** | +0,14 až +0,64 |

Všimněte si té asymetrie: **nejsilnější je negativní váha.** „Skoro se o něm nemluví" je
silnější důkaz, že je Věrný (−0,50), než „mluví se o něm hodně" je důkazem, že je Zrádce
(+0,37). Model je lepší ve vylučování než v obviňování.

**Jak pevné to je.** Oponentura upozornila, že pásmo „pod 0,5" má jen 7 pozorování
Zrádce a že jsou to opakovaná pozorování týchž lidí. Bootstrap přes hráče (44 lidí, 2 000
běhů) dává intervaly v tabulce: oba konce se překrývají a záporná váha je
silnější než kladná v **78 %** běhů. Platí to tedy většinou, ne jistě. (Na zbylých dvou
trénincích z kontroly níž vychází 92 % a 85 %.)

### Test na 3. řadě (stav po 6. epizodě)

| Co | AUC | p |
|---|---|---|
| jen hlasování | **0,351** | 0,79 |
| jen zmínky, celá epizoda | 0,895 | 0,019 |
| jen zmínky, celá epizoda, bez epizody odchodu | **0,947** | 0,005 |
| hlasování + zmínky | 0,912 | 0,008 |
| jen zmínky, poslední čtvrtina | 0,930 | 0,008 |
| jen zmínky, poslední čtvrtina, bez epizody odchodu | **0,947** | 0,004 |
| jen zmínky, skutečné okno kulatého stolu | 0,465 | 0,57 |
| jen zmínky, okno stolu, bez epizody odchodu | 0,490 | 0,55 |

**Hlasovací model je horší než náhoda** (0,351). Na zbylých dvou řadách vychází 0,431
a 0,649, tedy jednou pod náhodou a jednou nad ní. (Do 2. 11. tu stálo 0,403 a 0,684, čísla
z běhu před přidáním 7. dílu; našla to oponentura.)

**Měřeno jen u kulatého stolu, signál na 3. řadě mizí** (0,465). Zmínky tedy na 3. řadě
fungují v celém dílu a v poslední čtvrtině, ne v samotném okně stolu. Oddíl 8 to rozebírá. Tři hodnoty na nic neukážou
spolehlivě; co se z nich dá říct, je, že hlasování mimo trénink nedrží, a že přidání
k zmínkám výsledek spíš zhoršuje.

Vyloučení epizody, ve které hráč odešel, výsledek **zlepšilo** (0,895 → 0,947). To je
důležité: znamená to, že signál netáhne pozornost věnovaná odcházejícím, ta ho naopak ředí.

### Kontrola: každá řada jednou jako testovaná

| testovaná řada | hlasování | zmínky | zmínky, bez epizody odchodu | zmínky, jen okno stolu |
|---|---|---|---|---|
| 1. řada | 0,649 (p 0,22) | 0,895 (p 0,014) | 0,895 (p 0,014) | 0,825 (p 0,049) |
| 2. řada | 0,431 (p 0,67) | 0,812 (p 0,026) | 0,701 (p 0,13) | 0,674 (p 0,16) |
| 3. řada | 0,351 (p 0,79) | 0,895 (p 0,019) | 0,947 (p 0,005) | 0,465 (p 0,57) |

**Zmínkový signál obstál třikrát ze tří** na mírnějším měření a dvakrát ze tří na přísném
(u 2. řady p = 0,13, tedy neprůkazně). Měřený jen v okně kulatého stolu obstál jednou ze
tří. Hlasování neobstálo ani jednou.

> **Opraveno 2. 11. 2026 (na podnět oponentury).** Tabulka dřív nesouhlasila s uloženým
> výpisem: u 1. a 2. řady byla čísla z běhu před přidáním 7. dílu a u 3. řady stálo
> v posledním sloupci číslo z „poslední čtvrtiny". Teď jsou všechna z uloženého výpisu
> jednoho společného přepočtu.

---

## 6. Vesmíry: jednou trefa, jednou katastrofa

Tady je výsledek nejzajímavější a zároveň nejvarovnější.

| testovaná řada | aktivních / hledaných | bez zmínek | se zmínkami |
|---|---|---|---|
| 1. řada | 13 / 2 | 72. ze 78 (92 %) | 67. ze 78 (86 %) |
| 2. řada | 14 / 1 | 4. ze 14 (29 %) | 2. ze 14 (14 %) |
| 3. řada | 14 / 2 | 21. z 91 (23 %) | **1. z 91 (1 %)** |

(U 2. řady bez zmínek tu do 2. 11. chybně stálo „6. ze 14". Uložený výpis už tehdy říkal
4. ze 14; byla to stejná chyba přepisu, jakou oponentura našla v tabulce kontroly
v oddílu 5.)

### Třetí řada: model trefil přesně

Po 6. epizodě zbývali dva neodhalení Zrádci mezi čtrnácti lidmi, tedy 91 možných dvojic.
Model naučený jen na řadách 1 a 2 dal **skutečnou dvojici Zrádců na první místo z 91.**
Marginální pravděpodobnosti (3. řada se v době psaní ještě vysílá, proto místo jmen hráčů
uvádíme písmena a role píšeme v mužském rodě bez ohledu na pohlaví):

| hráč | model | skutečnost |
|---|---|---|
| Zrádce A | 54,5 % | **ZRÁDCE** |
| Zrádce B | 26,2 % | **ZRÁDCE** |
| hráč C | 19,0 % | Věrný |
| hráč D | 18,8 % | Věrný |
| hráč E | 17,3 % | Věrný |
| … | … | … |
| hráč F | 0,0 % | Věrný |

### Potvrzení po 7. epizodě

Sedmá epizoda se odvysílala **až po dokončení analýzy** (29. 10. 2026). Model se od té doby
nikam neučil, dostal jen o jednu epizodu dat navíc. Vyhoštěn byl jeden Věrný a další Věrný
byl zavražděn, takže ve hře zůstalo 12 lidí a oba neodhalení Zrádci.

| | po 6. epizodě | po 7. epizodě |
|---|---|---|
| možných dvojic | 91 | 66 |
| skutečná dvojice podle zmínek (celá epizoda) | **1.** | **1.** |
| skutečná dvojice podle zmínek (poslední čtvrtina) | 1. | 2. |
| skutečná dvojice podle zmínek (jen okno kulatého stolu) | 17. | 13. |
| skutečná dvojice bez zmínek (jen hlasování) | 21. z 91 | 15. z 66 |
| Zrádce A / Zrádce B | 54,5 % / 26,2 % | 56,3 % / 27,6 % |

**Je to slabší důkaz, než vypadá.** Pole se zmenšilo z 91 dvojic na 66, takže je to snazší
úloha, a u měření z poslední čtvrtiny dvojice spadla na druhé místo. Měřeno jen u kulatého
stolu je skutečná dvojice až 17., resp. 13. Zároveň je to ale
zkouška, kterou nešlo dopředu ovlivnit: data vznikla až po tom, co byl model hotový.

### První řada: model se spletl, jak nejvíc mohl

Skutečná dvojice Zrádců 1. řady skončila **72. ze 78**, tedy mezi nejméně pravděpodobnými.
AUC marginálů **0,182** — výrazně *horší* než náhoda. Zmínky to posunuly jen na 67. místo.

**Tohle je ta nejdůležitější tabulka v celé studii.** Jedna řada vypadá jako průlom, druhá
jako naprosté selhání. Průměr přes tři řady je se zmínkami **34 %** proti náhodným 50 %
(bez zmínek 48 %, tedy prakticky náhoda; do 2. 11. tu stálo 53 %, spočtené z chybně
přepsaného 6. místa 2. řady) — rozptyl je tak obrovský, že jediný výsledek nic neznamená.

Kdybychom studii zastavili u třetí řady, napsali bychom „metoda funguje" a byli bychom vedle.

### Proč vesmíry selhávají

Vesmírový model sčítá mnoho slabých, nezávisle odhadnutých členů přes všechny dvojice
hráčů. Když je každý člen skoro nulový a jeden z nich je systematicky obrácený (párový
násobitel 2,82× se na 1. řadě zřejmě nechová jako na ostatních), výsledek se převrátí
celý. Je to křehká konstrukce: **sčítáním slabých signálů nevznikne silný, vznikne jen
nestabilní.**

---

## 7. Chyby, které jsme v průběhu udělali

Čtyři z nich, body 4, 5, 8 a 9, prokazatelně dělaly výsledek lepším, než byl. To je samo
o sobě poučení: chyba, která výsledek zhorší, se najde sama, protože netěší. Body 8 až 11
jsme navíc nenašli sami, našla je oponentura.

1. **Přezdívky v titulcích jsme nedohledali do konce.** Titulky 3. řady píšou jedno jméno
   s „y“ místo „i“ (37×) a jiné s „i“ místo „y“ (7×). Ani jedno se bez diakritiky nesloučí
   se základním tvarem jména, takže se ty zmínky nepočítaly. Našli jsme to až při zpracování
   7. epizody výpisem nezařazených slov s velkým písmenem. **Dopad:** všech 37 a 7 výskytů
   je v 7. epizodě (lidé v ní probírají odhaleného Zrádce a podezírají dalšího hráče), takže
   se výsledky za epizody 1 až 6 nezměnily ani o řádek (ověřeno porovnáním tabulky zmínek
   před opravou a po ní: 0 změněných řádků). Bez opravy by ale byl špatně test po 7. epizodě.
   Poučení: výpis nezařazených slov nestačí pustit jednou na začátku, patří ke každé nové
   epizodě.

2. **Stahovací skript přepsal hotová data.** Při rate limitu Wikipedie uložil prázdné
   soubory a korpus spadl z 20 sérií na 12. Opraveno: stahuje se do dočasného souboru a
   původní se přepíše, až když se stažení povedlo.
3. **Zkrácená varianta „Tom" u jednoho jména** se chytala na běžné české „o tom" a „k tomu".
   Nafoukla počet zmínek toho hráče ze 48 na 192.
4. **Za „ve hře" jsme brali každého, kdo má řádek v tabulce kola** — tedy i dávno vyřazené
   hráče. Ti mají skoro nula zmínek a sráželi průměr Věrných dolů, takže model vypadal lépe.
5. **Permutační test prohazoval role uvnitř epizody**, jako by 452 řádků bylo 452 nezávislých
   pozorování. Nejsou: jsou to pořád titíž lidé v řadě epizod. Efektivní vzorek je počet
   *lidí*, ne řádků. Po opravě spadlo p z 0,0001 na 0,03.
6. **Filtr velkých písmen byl rozbitý.** Znaková třída `[A-ZÁ-Ž]` v Unicode obsahuje i malá
   písmena s háčkem, takže nefiltrovala nic. Opraveno přes `isupper()`.

Chyby 8 až 11 našla oponentura 31. 10. 2026, opravené jsou od 2. 11. (Chyba 7 je v oddílu 7b.)

8. **Parser tiše přehlédl čtyři naverbované Zrádce.** Jméno v poznámce „X was recruited as
   a Traitor in Episode N" se neshodovalo se jménem v tabulce hlasování (Fryina série:
   zkrácené jméno s iniciálou příjmení proti celému jménu a kratší přezdívka proti delší;
   americká 1. řada: tabulka soutěžících skončila předčasně na šabloně Wikipedie pro
   řazení jmen; britská 1. řada: v poznámce stálo „became a Traitor", ne „was recruited").
   Jejich hlasy z doby, kdy byli Věrní, se počítaly jako hlasy Zrádců. **Dopad:** Fryina
   série v křížovém ověření 0,507 → 0,400 (zároveň s doplněním jejích posledních dílů),
   průměr 0,573 → 0,554. Výsledek tedy chyba **vylepšovala**. Parser teď spáruje i zkratku
   a podmět poznámky a nahlas hlásí poznámku, ke které hráče nenašel.
9. **„Poslední čtvrtina dílu = kulatý stůl" neplatilo.** Na konci dílu je i noční scéna
   Zrádců a kulatý stůl bývá i v první polovině dílu. Na tom stál závěr, že signál nežije
   na konkláve. Po změření skutečného okna stolu vyšel **opak** (oddíl 8). I tahle chyba
   vylepšovala výsledek, protože dávala uklidňující výklad.
10. **Kontrola jmen hledala jen chybějící zmínky, ne falešné.** Jméno titulkářky
    v závěrečném titulku se počítalo jako zmínka jedné hráčky, jméno jiné osoby v titulcích
    jako zmínka jednoho hráče a popisky mluvčích („JMÉNO: …") jako zmínky. Oprava změnila
    22 řádků ze 713. Ruční kontrola 90 náhodných zmínek je popsaná v oddílu 8.
11. **Výpisy nešly zopakovat a studie citovala staré běhy.** Pořadí hráčů před náhodným
    prohazováním záviselo na pořadí množiny, které se mezi spuštěními Pythonu mění, takže
    tentýž výpočet dával pokaždé trochu jiné p. Tabulka kontroly v oddílu 5 citovala běh
    před přidáním 7. dílu. Opraveno řazením a jedním skriptem, který přepočítá všechny
    výpisy naráz a zapíše do nich datum a otisk dat.

---

## 7b. Poslední hlas Zrádce, a průměr, který lhal

Obojí vzniklo na autorovo upozornění 30. 10. 2026 a obojí stojí za zapsání: první jako
otevřený nález pro druhý díl, druhé jako chyba, která se málem dostala
do videa.

### Signál, který mají Fry i Majda: koho označí Zrádce v kole, kde jde ven

**Není to náš nález.** Autor 30. 10. 2026 upozornil, že ho ve svých seznamech mají
jak Fry, tak Majda (vědkyně, hráčka 3. české řady, která své ukazatele zveřejňuje), a že
bychom ho měli změřit:

> „velký signál, který používá minimálně majda, je, že zrádce, který je
> vyhlasovaný, tak na tom kulatým stolu, kde je vyhlasovaný, označí dalšího
> zrádce […]"

(Z citace jsme vynechali příklady se jmény hráčů.)

A týž den o něco později, když jsme signál omylem podali jako náš nález:

> „není to můj nález, mluví o tom i Fry i Majda. my to jen chtěli přidat a potvrdit
> a zmínit"

Že ho má i Fry, víme tedy od autora a z napasování na její signál 5 (níž). Ten je širší
(hlas vyhoštěného Zrádce kdykoli v minulosti, ne jen při odchodu) a jak s ním Fry přesně
počítá, ze zdrojů nevíme (oddíl 10). Video proto říká jen „podobné má i Fry"
(na podnět kontroly textu).

Majdina vlastní definice, jak ji autor téhož dne ocitoval: *„hráč co je při odchodu
označen vyhlasovaným zrádcem, má 2,7x vyšší šanci, že je také zrádce"*. Je to její
nejsilnější ukazatel („Označení zrádcem", 2,7×). Její číslo a naše 1,93× dělí každé něco
jiného, srovnává se jen směr.

Na Fryin seznam to sedí: je to její **signál 5** z oddílu 3b, *„v minulosti na hráče
hlasoval Zrádce, který už je vyhoštěný"*. Ona se dívá na terč, tohle měří hlasujícího,
ale je to tentýž jev z druhé strany. **Naše je na tom jen to měření.**

Spočítáno napříč 20 sériemi:

| | podíl |
|---|---|
| vyhoštěný Zrádce označil jiného Zrádce | **33,3 %** (20 z 60) |
| Zrádce v kole, kde vyhoštěn nebyl | 21,8 % (105 z 482) |
| vyhoštěný Věrný označil Zrádce | 27,4 % (29 ze 106) |

**Směr sedí: poměr 1,53× proti běžnému kolu.** Na českých řadách 1,38×, ale
tam je to jen 3 případy z 9.

**Námitka a jak ji to přežilo.** Kontrolní řádek (vyhoštěný Věrný, 27,4 %) ukazoval,
že část rozdílu může dělat prostá skutečnost, že ke konci hry je mezi zbývajícími
Zrádců poměrně víc. Autor se zeptal, jestli se to dá zohlednit. Dá, a přesněji než
dělením na půlky hry: každý hlas se porovná s tím, kolik Zrádců bylo **v tom kole**
mezi možnými terči:

| kdo hlasuje | pozorováno z očekávaného | poměr | p |
|---|---|---|---|
| **Zrádce v kole, kde jde sám ven** | 20 z 10,4 | **1,93×** | **0,004** |
| Zrádce v kole, kde ven nejde | 105 z 72,7 | 1,44× | 0,157 |
| Věrný v kole, kde jde sám ven | 29 z 22,7 | 1,28× | 0,201 |

Po očištění signál **obstál a je průkazný**. Dvě kontroly ho drží: u Věrného v jeho
posledním kole se nic takového neděje, takže to není efekt „posledního kola" obecně;
a v první polovině hry vychází 2,07× (p = 0,018), takže to není ani efekt konce hry.
Těch 20 případů je 20 různých lidí, pseudo-opakování tu není. **Ve videu je to část
o posledním hlasu Zrádce**, s tím, že vodítko sledují Fry i Majda a naše je jen měření.

**Proč to Zrádce dělá, data neříkají.** Pracovní verze videa do 2. 11. říkala „Nekryjí se,
ukazují na své". To je výklad motivu, ne měření (upozornila na to oponentura). Netestovaná
zůstává i obyčejnější možnost: odcházející Zrádce dá hlas tomu, kdo byl u stolu druhý
nejpodezřelejší, a ten bývá Zrádcem. Video teď říká jen směr.

Na českých řadách samotných to průkazné není (3 z 9, p = 0,117) — je to málo případů.

### Chyba, kterou chytil autor: průměr s opačným znaménkem

Pracovní verze videa chvíli tvrdila: *„kdo označí skutečného Zrádce, je spíš Věrný"*, na
základě toho, že hlas na odhaleného Zrádce dalo 42,9 % Zrádců proti 49,7 %
Věrných, tedy 0,86× (po opravě dat 2. 11.: 40,9 % proti 48,7 %, 0,84×). Autor:

> „ve chvíli, kdy je jasný, že bude zrádce vyhlasovaný, tak se k hlasování pro
> něj přidají i další zrádci."

Po rozdělení podle toho, jak jednoznačné to hlasování bylo:

| jak jasné to bylo | Zrádci | Věrní | poměr |
|---|---|---|---|
| těsné (pod 40 % hlasů) | 8,6 % (35) | 14,2 % (204) | **0,60×** |
| střední (40 až 60 %) | 80,0 % (30) | 52,2 % (159) | **1,53×** |
| jasné (nad 60 % hlasů) | 93,5 % (46) | 76,6 % (231) | **1,22×** |

**Ve dvou pásmech ze tří platí opak toho, co říkal průměr.** Zrádci drží
zpátky, dokud je výsledek nejistý, a jakmile je jasno, přidají se k většině
*ochotněji* než Věrní. Průměr přes všechna kola to smíchal a vyšlo z toho
opačné znaménko — učebnicový Simpsonův paradox.

Tvrzení je z videa pryč a scéna, která na něm stála, zrušená. **Zapsáno jako
chyba číslo 7**, i když se do zveřejněné verze nedostala: právě proto, že
průměr vypadal věrohodně a kontrolu vyžádal až autor, ne ten, kdo počítal.

---

## 8. Čemu se nedá věřit

- **Nevíme, jestli měříme hru, nebo střih.** Tvůrci vědí, kdo je Zrádce, a mohou mu (i bez
  záměru) dávat víc prostoru. **Hráč uvnitř hry ten signál použít nemůže** — konkláve Zrádců nevidí a střih
  nezná. Divák role zná z vysílání, takže jemu nic nového neprozradí; ukazuje hlavně, komu
  pořad dává prostor (upozornila na to oponentura). Oslovení nám tenhle výklad nepotvrdí ani nevyvrátí: test je na něj
  příliš slabý (oddíl 4).
  - **Konkláve Zrádců vyloučit nejde. Do 2. 11. 2026 tu stálo opak.** Otázka zní, jestli
    signál nevzniká hlavně tím, že se Zrádci jmenují mezi sebou na konkláve a v noci.
    Podle mluvčích scény rozdělit nejde, podle času ano.
    - **Staré měření** bralo poslední čtvrtinu dílu jako kulatý stůl a vyšlo, že signál je
      tam silnější než vepředu. Oponentura ukázala, že v poslední čtvrtině je i noční
      scéna Zrádců a že kulatý stůl bývá i v první polovině dílu (autor 2. 11.: „někdy se
      stane, že je kulatý stůl i dřív, než v druhé půlce").
    - **Nové měření** bere skutečné okno stolu z titulků: od přivítání moderátorem („Hráči,
      vítejte zpět u kulatého stolu") po odhalení role vyhoštěného. 17 dílů se našlo
      automaticky (u každého máme zapsanou větu, kterou okno končí), 14 je určených ručně,
      každý se zapsaným zdůvodněním: tři první díly bez vyhnanství (bez okna), dvě finále
      (bráno jen poslední kulatý stůl, ne hlasování u ohně), pět dílů bez obvyklé věty
      moderátora nebo výzvy k odhalení role a čtyři díly, ve kterých vyhoštěný odhalil roli
      volnou větou („A Bůh je věrný jako já"). Okno je odhad podle titulků bez jmenovek
      mluvčích, ne přesná hranice.
      (3. 11. opraveno dvakrát, obě chyby našla kontrola textu před zveřejněním: tu chybně
      stálo 22 a 9; a výraz pro odhalení role neznal „jsem byl věrný" a podobné, takže
      u sedmi dílů okno skončilo už na výzvě a uřízlo loučení. Čísla níž jsou po obou
      opravách.)
      Díl se pak dělí na tři části. Jen díly se stolem, p je permutace rolí mezi hráči
      uvnitř řady:

      | část dílu | Zrádci | Věrní | AUC | p |
      |---|---|---|---|---|
      | před stolem (ráno, mise, zpovědnice, začátek s konkláve) | 1,67 | 0,86 | 0,69 | 0,003 |
      | **u kulatého stolu** | 1,33 | 0,93 | 0,59 | **0,26** |
      | **po stole** (rozhovory po vyhlášení, noční scéna Zrádců, upoutávka) | **2,21** | 0,75 | **0,77** | **0,0002** |
      | poslední čtvrtina (staré měření) | 1,76 | 0,84 | 0,73 | 0,025 |

    - **Výsledek:** u samotného stolu je rozdíl malý a neprůkazný. Nejsilnější je po stole,
      kde je mimo jiné noční scéna Zrádců, a silný je i před stolem. Ve slepém testu na
      3. řadě (oddíl 5) zmínky jen z okna stolu nefungují vůbec (AUC 0,465).
    - **Co z toho plyne:** výklad „Zrádci se jmenují mezi sebou" vyloučit nejde, data ho
      spíš podporují. Dokázaný ale není: „po stole" obsahuje i rozhovory o vyhoštěném
      a upoutávku na další díl. Noční scénu samotnou jsme neoddělili, protože ji titulky
      spolehlivě neohraničí. Pro hráče z toho nic neplyne: u stolu, kde jediné slyší všechny,
      je rozdíl malý a neprůkazný (na 1. řadě ve slepém testu průkazný byl, na 3. ne).
  - **Druhou výhradu vyloučit nejde taky.** Kulatý stůl je sestříhaný stejně jako zbytek
    dílu. Rozdíl mezi „hráči ho podezírají" a „tvůrci mu dali prostor" z našich dat
    nevyčteme a nebudeme předstírat, že ano.
- **Tři řady jsou málo.** Vesmíry to ukazují nejlépe: jeden skvělý výsledek a jeden
  katastrofální.
- **Jako nástroj na konkrétního člověka je to k ničemu.** Zrádci jsou v pořadí svých řad na
  místech 4, 5, 8, 17, 21 / 1, 4, 5, 9, 13, 15 / 1, 5, 14 z 23.
- **Rozpoznávání jmen je ověřené jen vzorkem.** České pády se generují podle pravidla, ne ze
  slovníku; přezdívky jsme doplnili ručně podle výpisu nejčastějších nezařazených slov.
  Ruční kontrola 90 náhodných zachycených zmínek (30 na řadu) našla 90 správných,
  takže falešných je s 95% jistotou pod 3,3 %. Chybějící zmínky tím ověřené nejsou.
- **Rekapitulace na začátku dílu se počítá dvakrát.** Tatáž scéna je v dílu, kde se stala,
  i v rekapitulaci dalšího dílu. Týká se to všech hráčů; měření to nemění, je to šum.
- **Ve 2. řadě hrají muž a žena se jmény, která se liší jen koncovkou -a.** Ženské jméno má
  tedy stejný tvar jako 2. pád mužského, takže se tento tvar zahazuje oběma (56 výskytů).
  Oba jsou Věrní, takže to výsledek nenaklání, ale obě čísla jsou podstřelená.
- **Měření „poslední čtvrtina" jsme vybrali až po tom, co jsme viděli výsledky 3. řady.**
  Proto se jako hlavní uvádí „celá epizoda". Rozdíl mezi nimi je malý, ale je to výběr po
  faktu a patří to přiznat.
- **Slepý test na 3. řadě je slepý pro váhy, ne pro návrh měření** (upozornila na to
  oponentura). Model se učil jen na 1. a 2. řadě. Seznam přezdívek, opravy chyb a výběr
  „poslední čtvrtiny" ale vznikaly při pohledu i na 3. řadu. Skutečně slepé budou až díly
  8 až 12. Kód a data, ze kterých se model učí, jsme pro ně 2. 11. zmrazili; jedinou opravu
  chyby (okno kulatého stolu, oddíl 8) jsme udělali 3. 11., ještě než vyšel 8. díl. Odhady
  k dílům 8 až 12 během vysílání nezveřejňujeme.
- **Zkoušeli jsme hodně věcí** (upozornila na to oponentura). Studie prošla zhruba 40 variant:
  definice plané volby, Fryiny signály ve třech skupinách, dav, dvojice, poslední hlas, fáze
  hry, varianty zmínek, oslovení, části dílu. Bez opravy na mnohonásobné testování. Při
  přísné Bonferroniho opravě (0,05 / 40 ≈ 0,0013) by z „tří věcí o hře" obstálo jen „Věrní
  nehádají naslepo" (p = 0,0001). „Zrádci jdou s davem" (p = 0,013) a poslední hlas Zrádce
  (p = 0,004) ne. Nemusí to znamenat, že neplatí, ale jsou méně jisté, než by se zdálo, a
  patří ověřit na nových datech. Video je proto podává jako „dobré tipy, ne jistotu".
- **Tohle není předpověď.** Všechny role jsou známé z vysílání. Ověřuje se metoda, nic se
  nehádá dopředu.
- **Fryiny váhy (+0,47, −1,28, −1,73)** jsou ze zpravodajství o jejím videu (The Tab,
  20. a 22. 10. 2026), ne z videa samotného, a ona svou přesnou metodu nezveřejnila. Do
  výpočtu nevstupují. Že jsou v přirozeném logaritmu, je rekonstrukce Eda Jeffersona, ne
  její údaj — sedí ale na jejích vlastních procentech. Co znamená znaménko u konkrétního
  bodu, žádný zdroj výslovně neříká (zdroje v oddílu 10).
- **Naše replikace její definice je naše čtení jejího popisu.** „První tři kulaté stoly"
  a 23,5 % / 14,6 % jsou z Jeffersonova rozboru, „jen kola, kde odešel Věrný" jen z jednoho
  článku The Tab. Kdyby to myslela jinak, čísla v oddílu 3b se posunou. Obsah obou videí
  známe jen z rozborů a zpravodajství; ověřené jsou jejich adresy a popisy.
- **Zdrojem hlasovací části je Wikipedie, ne vysílání.** Nikdo ji neověřoval proti epizodám.

---

## 9. Závěr

**Fryin postup postavený na Turingově myšlence se na hlasovacích datech v našem provedení nepotvrdil.** Signál tam je a je statisticky prokazatelný, ale mimo trénink padá pod náhodu. Na sérii, ve které hrála sama Fry, vychází
0,40, tedy hůř než mince. Není to tím, že by Fry měřila špatně: její planou volbu jsme
v našem čtení její definice replikovali blízko (24,3 % proti jejím 23,5 %). Je to tím, že
ten rozdíl stojí na 208 hlasech, neudrží se mimo britské řady a na českých jde na opačnou
stranu. Na rozhodnutí o konkrétním člověku to nestačí ani omylem.

**To, co funguje, je mnohem hloupější signál: kolik se o kom mluví.** Mimo trénink drží
AUC kolem 0,85 a obstálo to ve všech třech českých řadách. Je to skoro pětkrát silnější než
nejsilnější váha našeho hlasovacího modelu a zhruba o třetinu silnější než planá volba
v našem čtení Fryiny definice.

**Ale Fryina hlavní myšlenka — vesmíry — se nepotvrdila.** Jednou dala dokonalý výsledek,
jednou výsledek horší než náhoda. Sčítání mnoha slabých signálů nevyrobí silný signál,
vyrobí nestabilní.

**A i to, co funguje, nejspíš neměří hru.** Dvě vysvětlení vyloučit neumíme: že pořad
dává Zrádcům víc prostoru, protože tvůrci vědí, kdo to je, a že se Zrádci jmenují mezi
sebou na konkláve a v noci. Signál je nejsilnější po kulatém stole, kde je i noční scéna
Zrádců, a u samotného stolu je slabý a neprůkazný. Divák role zná z vysílání, takže jemu to
nic nového neprozradí; ukazuje to hlavně, komu pořad dává prostor. Hráči u kulatého stolu
je to k ničemu — ten konkláve Zrádců nevidí a slyší jen to, co se řekne nahlas. A právě
v tom, co se řekne nahlas, je signál slabý: u stolu malý a neprůkazný, v přímém oslovení
jsme žádný **nezměřili** (ten test je ale slabý, oddíl 4).

Nejhezčí číslo celé studie je nakonec to nejnudnější: **−0,50 banu za to, že se o někom
skoro nemluví.** Nejsilnější věc, kterou se o Zrádcích dá zjistit, je spíš to, kdo jimi
*není* (většinou: tak to vyšlo v 78 % bootstrapových běhů, oddíl 5).

---

## 10. Jak si to ověřit

**Skripty a zpracovaná data zatím zveřejněné nejsou.** Nenajdete tu proto návod ke
spuštění, jen popis postupu a zdroje, ze kterých vychází. Zdrojová data jsou veřejná:
tabulky hlasování na Wikipedii a díly českých řad zveřejněné na iprima.cz.

### Postup

1. **Hlasování.** Tabulky hlasování 20 sérií z anglické a české Wikipedie (export přes
   `Special:Export`), převedené na hráče, role, kola a hlasy. Parser zvládá obě rozložení
   tabulek (cs i en); naverbované Zrádce počítá do naverbování jako Věrné (oddíl 1).
2. **Titulky.** Skryté titulky pro neslyšící k 31 dílům českých řad 1–3: zmínky jmen hráčů
   (české pády podle pravidla, přezdívky doplněné ručně), oslovení v 5. pádě a okno
   kulatého stolu v každém dílu (oddíl 8).
3. **Výpočty.** Turingovy váhy z hlasování, křížové ověření a permutace (oddíl 3), Fryiny
   signály (3b), zmínkový signál s permutací na úrovni hráčů a síla testu u oslovení (4),
   hlavní test s učením na 1. a 2. české řadě, slepým testem na 3. a bootstrapem vah (5),
   vesmíry (6), poslední hlas Zrádce (7b), zmínky před stolem, u stolu a po stole a ruční
   kontrola vzorku 90 zmínek (8).

Všechny výpisy přepočítá naráz jeden skript. Každý výpis přepíše celý a do hlavičky zapíše
datum, otisk skriptu a otisk vstupních dat.

Čistý Python 3.10, žádné instalované knihovny. Všechna náhodná čísla mají pevné semínko
a od 2. 11. 2026 i pevné pořadí hráčů, takže běh je opakovatelný: dva běhy hlavního testu
za sebou dávají shodný výpis (ověřeno 2. 11.). Do té doby to neplatilo (oddíl 7, chyba 11).

### Zdroje

**K metodě Hannah Fry.** Obsah obou videí známe jen z rozborů a zpravodajství (oddíl 8).

- Hannah Fry: „How would Alan Turing have played the Traitors?", YouTube:
  https://www.youtube.com/watch?v=twDvxNooI_4
- Matt Parker (Stand-up Maths): „Did Hannah Fry crack The Traitors?", YouTube, 22. 10. 2026:
  https://www.youtube.com/watch?v=KxHKrbfnmTU
- Ed Jefferson: „Could Hannah Fry have predicted what would happen in The Traitors using
  data?", 19. 10. 2026 (přirozený logaritmus, první tři kulaté stoly, 23,5 % / 14,6 %):
  https://edjefferson.com/blog/could-hannah-fry-have-predicted-what-would-happen-in-the-traitors-using-data/
- The Tab, 20. 10. 2026 (body se znaménkem):
  https://thetab.com/2026/10/20/if-you-apply-hannah-frys-celebrity-traitors-formula-to-the-show-its-so-clear-she-wouldve-won
- The Tab, 22. 10. 2026 (šest bodů, „jen kola, kde odešel Věrný"):
  https://thetab.com/2026/10/22/hannah-frys-celebrity-traitors-spreadsheet-updated-to-reveal-who-looks-most-suspicious
- PinkNews, 16. 10. 2026 („první tři epizody"):
  https://www.thepinknews.com/2026/10/16/hannah-fry-celebrity-traitors-theory/

**K Majdě.** Označení „vědkyně“: Kinotip2.cz, 17. 9. 2026: https://www.kinotip2.cz/clanky/zradci-3-pritvrzuji-vedkyne-si-vede-tabulku-novinarka-je-zvykla-na-manipulaci-kdo-ma-nejlepsi-taktiku-20260917-18010.html. Své ukazatele zveřejňuje na Instagramu (https://www.instagram.com/majdabohutinska/); její definici jsme převzali z přepisu, který udělal autor, profil jsme sami neotevřeli.

**Data.**

- Wikipedie (anglická a česká): stránky jednotlivých sérií pořadu *The Traitors* a *Zrádci*
  s tabulkami hlasování.
- iprima.cz: zveřejněné díly českých řad 1–3 pořadu *Zrádci* a jejich skryté titulky pro
  neslyšící.
