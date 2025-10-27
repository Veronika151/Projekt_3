# 🗳️ Elections Scraper
*Třetí projekt pro Engeto kurz: Datový analytik s Pythonem*  

## 📘 Popis projektu
Cílem projektu je **zpracování a získání výsledků voleb do Poslanecké sněmovny Parlamentu České republiky, které se konaly v roce 2017**.  
Data pocházejí z oficiálního volebního portálu **[volby.cz](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)** a ukládají se do **CSV souboru**, vhodného pro další analýzu.  

Skript umožňuje vybrat **libovolný územní celek** (okres nebo obec) a stáhne:  
- počet registrovaných voličů  
- počet vydaných obálek  
- počet platných hlasů  
- výsledky všech kandidujících stran  

---

## 🧩 Struktura projektu
| Soubor | Popis |
|:--------|:-------|
| `main.py` | Hlavní skript pro stahování volebních výsledků |
| `requirements.txt` | Seznam knihoven potřebných pro běh skriptu |
| `README.md` | Dokumentace projektu |
| `*.csv` | Výstupní soubor s výsledky voleb |

---

## ⚙️ Instalace knihoven
Seznam použitých knihoven třetích stran (včetně verzí) je uveden v souboru `requirements.txt`.  
Nainstalovat potřebné knihovny ve vytvořeném virtuálním prostředí je možné příkazem:
```bash
pip install -r requirements.txt
```

---

## ▶️ Použití a spuštění skriptu
Skript `main.py` se spouští z příkazového řádku a vyžaduje **dva argumenty**:

```bash
python main.py <URL_uzemniho_celku> <vystupni_soubor.csv>
```

**Parametry:**
- `<URL_uzemniho_celku>` – odkaz na vybraný okres nebo obec 
- `<vystupni_soubor.csv>` – název souboru, kam se výsledky uloží  

Po úspěšném spuštění skript vytvoří **CSV soubor** s kompletními výsledky všech obcí vybraného území.

---

## 💡 Ukázka použití
Příklad pro okres **Příbram**:

### Spuštění:
```bash
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111" vysledky_pribram.csv
```

### Průběh:
```
STAHUJI DATA Z VYBRANÉHO URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111
STAHUJI DATA Z VYBRANÉHO URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=529672&xvyber=2111
STAHUJI DATA Z VYBRANÉHO URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=564559&xvyber=2111
...
UKLÁDÁM DATA DO SOUBORU: vysledky_pribram.csv
UKONČUJI elections-scraper
```

---

## 🧾 Ukázka výstupu (CSV)
```csv
Kód obce;Název obce;Voliči v seznamu;Vydané obálky;Platné hlasy;Občanská demokratická strana;Řád národa - Vlastenecká unie;CESTA ODPOVĚDNÉ SPOLEČNOSTI;Česká str.sociálně demokrat.;...
529672;Bezděkov pod Třemšínem;134;105;103;12;0;0;10;32;3;0;9;8;5;3;1;0
564559;Bohostice;167;108;108;12;0;0;9;37;4;0;7;6;5;2;1;0
539953;Bohutín;1417;925;920;93;1;2;50;348;30;11;79;61;88;17;4;4
539970;Borotice;302;202;202;18;1;0;20;65;15;2;12;11;16;3;0;0
539988;Bratkovice;252;167;166;29;0;0;11;40;9;1;17;13;22;4;0;0
...
```

---

