# Projekt: Elections Scraper
Třetí projekt pro Engeto Python Akademii

## Popis projektu
Tento projekt umožňuje automaticky stahovat a ukládat výsledky voleb do Poslanecké sněmovny Parlamentu České republiky konaných v roce 2017. Data jsou získávána přímo z oficiálního volebního portálu volby.cz (konkrétně zde: https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) a ukládána do CSV souboru vhodného pro další analýzu.

Skript umožňuje vybrat libovolný územní celek (okres či obec) a stáhne výsledky všech obcí daného území, včetně:
- počtu registrovaných voličů,
- počtu vydaných obálek,
- počtu platných hlasů,
- výsledků jednotlivých politických stran.

## Struktura projektu
- main.py – hlavní skript pro stahování volebních výsledků
- requirements.txt – seznam knihoven potřebných pro běh skriptu
- README.md – dokumentace projektu
- *.csv – výstupní soubor s výsledky voleb

## Instalace knihoven
Soupis všech knihoven, včetně jejich verzí, potřebných pro běh skriptu je uveden v souboru requirements.txt.

## Použití a spuštění skriptu
Skript main.py se spouští z příkazového řádku a vyžaduje 2 argumenty:

> python main.py <URL_uzemniho_celku> <vystupni_soubor.csv>
>
> <URL_uzemniho_celku> = odkaz na vybraný okres nebo obec na portálu volby.cz
> 
> <vystupni_soubor.csv> = název souboru, do kterého se uloží výsledky

Po úspěšném spuštění skript vytvoří CSV soubor s kompletními výsledky voleb pro všechny obce daného územního celku.

## Ukázka projektu
Výsledky pro okres Příbram:
> 1. argument -> https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111
> 2. argument -> vysledky_pribram.csv

Spuštění programu:
> python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111" vysledky_pribram.csv

Průběh stahování:
>STAHUJI DATA Z URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111
>STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=529672&xvyber=2111
>STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=564559&xvyber=2111
>STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=539953&xvyber=2111
>STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=539970&xvyber=2111
>STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=539988&xvyber=2111 
> ...
> UKLÁDÁM DATA DO SOUBORU: vysledky_pribram.csv
> UKONČUJI: main.py

Částečný výstup:
```
Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
529672,Bezděkov pod Třemšínem,134,105,103,11,65 %,0,00 %,0,00 %,9,70 %,0,00 %,31,06 %,0,00 %,0,97 %,2,91 %,0,00 %,0,00 %,0,97 %,0,00 %,4,85 %,0,00 %
564559,Bohostice,167,108,108,11,11 %,0,00 %,0,00 %,8,33 %,0,00 %,34,25 %,0,00 %,0,00 %,3,70 %,0,00 %,0,00 %,0,92 %,0,00 %,4,62 %,0,00 %
539953,Bohutín,1 417,925,920,10,10 %,0,10 %,0,21 %,5,43 %,0,00 %,37,82 %,0,10 %,0,21 %,3,26 %,0,10 %,0,76 %,0,21 %,0,00 %,9,56 %,0,10 %
539970,Borotice,302,202,202,8,91 %,0,49 %,0,00 %,9,90 %,0,00 %,32,17 %,0,00 %,0,00 %,7,42 %,0,00 %,1,98 %,0,00 %,0,49 %,7,92 %,0,49 %
539988,Bratkovice,252,167,166,17,46 %,0,00 %,0,00 %,6,62 %,0,00 %,24,09 %,0,00 %,0,00 %,5,42 %,0,00 %,4,21 %,0,00 %,0,00 %,13,25 %,0,00 %
```







