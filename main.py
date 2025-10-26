import sys
import csv
import requests
import bs4
from typing import List, Tuple


def get_html(link: str) -> bs4.BeautifulSoup:
    """Načte HTML stránku zadané adresy a vrátí ji jako objekt BeautifulSoup."""
    response = requests.get(link)
    html = bs4.BeautifulSoup(response.text, "html.parser")
    print("STAHUJI DATA Z URL:", link)
    return html


def get_towns(html: bs4.BeautifulSoup) -> List[str]:
    """Vrátí seznam názvů obcí spadajících do vybraného okresu."""
    return [t.text for t in html.find_all("td", "overflow_name")]


def get_links(html: bs4.BeautifulSoup) -> List[str]:
    """Získá seznam odkazů na detailní výsledky jednotlivých obcí v daném okrese."""
    links = []
    for cell in html.find_all("td", "cislo"):
        a_tag = cell.find("a")
        if a_tag and "href" in a_tag.attrs:
            links.append(f"https://volby.cz/pls/ps2017nss/{a_tag['href']}")
    return links


def get_ids(html: bs4.BeautifulSoup) -> List[str]:
    """Vrátí seznam identifikačních kódů všech obcí v aktuálním okrese."""
    return [i.text for i in html.find_all("td", "cislo")]


def collect_parties(first_link: str) -> List[str]:
    """Vrací seznam všech politických stran, které kandidují v tomto okrese."""
    html = get_html(first_link)
    return [p.text for p in html.find_all("td", "overflow_name")]


def get_voters_data(links: List[str]) -> Tuple[List[str], List[str], List[str]]:
    """
    Získá počet zapsaných voličů, účastníků voleb a platných hlasů pro každou obec.
    Vrací tři seznamy: voters, attendance, valid_ones.
    """
    voters, attendance, valid_ones = [], [], []
    for link in links:
        html = get_html(link)
        voters.extend([v.text.replace('\xa0', ' ') for v in html.find_all("td", headers="sa2")])
        attendance.extend([a.text.replace('\xa0', ' ') for a in html.find_all("td", headers="sa3")])
        valid_ones.extend([c.text.replace('\xa0', ' ') for c in html.find_all("td", headers="sa6")])
    return voters, attendance, valid_ones


def collect_votes(links: List[str]) -> List[List[str]]:
    """
    Vrací dvourozměrný seznam, kde jsou pro každou obec uvedeny
    procentuální výsledky všech politických stran.
    """
    votes = []
    for link in links:
        html = get_html(link)
        votes_cells = html.find_all("td", "cislo", headers=["t1sb4", "t2sb4"])
        votes.append([v.text + ' %' for v in votes_cells])
    return votes


def create_rows(html: bs4.BeautifulSoup) -> List[List[str]]:
    """
    Sestaví datovou strukturu pro CSV.
    Každý řádek obsahuje ID obce, její název, počet registrovaných a zúčastněných voličů,
    počet platných hlasů a procentuální výsledky všech kandidujících stran.
    """
    links = get_links(html)
    if not links:
        print("Chyba: Nenalezeny žádné odkazy na obce. Struktura HTML se možná změnila.")
        quit()

    voters, attendance, valid_ones = get_voters_data(links)
    towns = get_towns(html)
    ids = get_ids(html)
    votes = collect_votes(links)

    return [[i, t, v, a, vo] + vs for i, t, v, a, vo, vs in zip(ids, towns, voters, attendance, valid_ones, votes)]


def election2017(link: str, file: str) -> None:
    """
    Hlavní funkce, která vygeneruje CSV soubor s kompletními výsledky voleb
    v daném okrese.
    """
    html = get_html(link)
    links = get_links(html)
    if not links:
        print("Chyba: Nenalezeny žádné odkazy na obce. Struktura HTML se možná změnila.")
        quit()

    rows = create_rows(html)
    parties = collect_parties(links[0])

    header = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy']
    header.extend(parties)

    print("UKLÁDÁM DATA DO SOUBORU:", file)
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print("UKONČUJI:", sys.argv[0])


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Zadal jsi chybný počet argumentů. Musí být 3: '
              'název skriptu, url adresa v uvozovkách a jméno výstupního .csv souboru.')
        quit()

    address = sys.argv[1]
    file_name = sys.argv[2]
    election2017(address, file_name)