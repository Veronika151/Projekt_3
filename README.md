# 🗳️ Elections Scraper
*Třetí projekt pro Engeto Datový analytik s Pythonem*  

## 📘 Popis projektu
Tento projekt automaticky **stahuje a ukládá výsledky voleb do Poslanecké sněmovny ČR (2017)**.  
Data pocházejí z oficiálního volebního portálu **[volby.cz](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)**  
a ukládají se do **CSV souboru**, vhodného pro další analýzu.  

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
Potřebné knihovny (včetně verzí) jsou uvedeny v souboru `requirements.txt`.  
Nainstaluj je příkazem:
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
- `<URL_uzemniho_celku>` – odkaz na vybraný okres nebo obec z portálu [volby.cz](https://www.volby.cz)  
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
STAHUJI DATA Z URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111
STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=529672&xvyber=2111
...
UKLÁDÁM DATA DO SOUBORU: vysledky_pribram.csv
UKONČUJI: main.py
```

---

## 🧾 Ukázka výstupu (CSV)
```csv
Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,ANO 2011,KDU-ČSL,SPD,ČSSD,...
529672,Bezděkov pod Třemšínem,134,105,103,11,31,06 %,0,97 %,4,85 %,9,70 %,...
564559,Bohostice,167,108,108,11,34,25 %,3,70 %,4,62 %,8,33 %,...
539953,Bohutín,1417,925,920,10,37,82 %,3,26 %,9,56 %,5,43 %,...
```

---

## 🧠 Shrnutí  
**Elections Scraper** je praktický nástroj pro automatizované zpracování a analýzu výsledků voleb v ČR.  
Díky jednoduchému použití a univerzálnímu výstupu (CSV) se snadno integruje do dalších analytických projektů.
