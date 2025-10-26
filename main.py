import sys
import csv
import requests
import bs4
from typing import List, Tuple


def get_html(link: str) -> bs4.BeautifulSoup:
    """
    Stáhne HTML obsah z daného odkazu a vrátí ho jako objekt BeautifulSoup.
    Přidán print pro indikaci stahování.
    """
    print("STAHUJI DATA Z VYBRANÉHO URL:", link)
    response = requests.get(link)
    html = bs4.BeautifulSoup(response.text, "html.parser")
    return html


def get_towns(html: bs4.BeautifulSoup) -> List[str]:
    """Vrací seznam názvů obcí z HTML tabulky."""
    return [t.text for t in html.find_all("td", "overflow_name")]


def get_links(html: bs4.BeautifulSoup) -> List[str]:
    """Vrací seznam URL odkazů na detailní výsledky obcí."""
    links = []
    for cell in html.find_all("td", "cislo"):
        a_tag = cell.find("a")
        if a_tag and "href" in a_tag.attrs:
            links.append(f"https://volby.cz/pls/ps2017nss/{a_tag['href']}")
    return links


def get_ids(html: bs4.BeautifulSoup) -> List[str]:
    """Vrací seznam identifikačních kódů obcí z tabulky."""
    return [i.text for i in html.find_all("td", "cislo")]


def collect_parties(first_link: str) -> List[str]:
    """Vrací seznam všech kandidujících politických stran pro daný okres."""
    html = get_html(first_link)
    return [p.text for p in html.find_all("td", "overflow_name")]


def get_voters_data(links: List[str]) -> Tuple[List[str], List[str], List[str]]:
    """
    Vrací tři seznamy: počet voličů, účast, platné hlasy pro každou obec.
    """
    voters, attendance, valid_ones = [], [], []
    for link in links:
        html = get_html(link)
        voters.extend(
            [v.text.replace("\xa0", " ") for v in html.find_all("td", headers="sa2")]
        )
        attendance.extend(
            [a.text.replace("\xa0", " ") for a in html.find_all("td", headers="sa3")]
        )
        valid_ones.extend(
            [c.text.replace("\xa0", " ") for c in html.find_all("td", headers="sa6")]
        )
    return voters, attendance, valid_ones


def collect_votes(links: List[str]) -> List[List[str]]:
    """
    Vrací procentuální výsledky hlasů pro všechny strany a obce.
    """
    votes = []
    for link in links:
        html = get_html(link)
        votes_cells = html.find_all("td", "cislo", headers=["t1sb4", "t2sb4"])
        votes.append([v.text + " %" for v in votes_cells])
    return votes


def create_rows(html: bs4.BeautifulSoup) -> List[List[str]]:
    """
    Sestaví seznam řádků pro CSV. Každý řádek obsahuje všechny potřebné údaje.
    """
    links = get_links(html)
    if not links:
        return []
    voters, attendance, valid_ones = get_voters_data(links)
    towns = get_towns(html)
    ids = get_ids(html)
    votes = collect_votes(links)

    return [
        [i, t, v, a, vo] + vs
        for i, t, v, a, vo, vs in zip(ids, towns, voters, attendance, valid_ones, votes)
    ]


def election2017(link: str) -> Tuple[List[str], List[List[str]]]:
    """
    Připraví data pro CSV a vrací header a rows.
    """
    html = get_html(link)
    links = get_links(html)
    if not links:
        return [], []
    rows = create_rows(html)
    parties = collect_parties(links[0])
    header = [
        "Kód obce",
        "Název obce",
        "Voliči v seznamu",
        "Vydané obálky",
        "Platné hlasy",
    ] + parties
    return header, rows


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Zadal jsi chybný počet argumentů. Musí být 3: "
            "název skriptu, url adresa v uvozovkách a jméno výstupního .csv souboru."
        )
        sys.exit(1)
    address = sys.argv[1]
    file_name = sys.argv[2]

    header, rows = election2017(address)
    if not rows:
        print("Chyba: Nenalezeny žádné data.")
        sys.exit(1)
    # Výpis před uložením souboru

    print("UKLÁDÁM DATA DO SOUBORU:", file_name)
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    # Výpis při ukončení skriptu

    print("UKONČUJI elections-scraper")