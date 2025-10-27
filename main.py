import sys
import csv
import requests
import bs4
from typing import List, Tuple


def get_html(link: str) -> bs4.BeautifulSoup:
    """Stáhne HTML obsah z daného odkazu a vrátí ho jako objekt BeautifulSoup."""
    print("STAHUJI DATA Z VYBRANÉHO URL:", link)
    response = requests.get(link)
    response.raise_for_status()
    return bs4.BeautifulSoup(response.text, "html.parser")


def get_towns(html: bs4.BeautifulSoup) -> List[str]:
    """Vrací seznam názvů obcí z HTML tabulky."""
    return [t.text.strip() for t in html.find_all("td", "overflow_name")]


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
    return [i.text.strip() for i in html.find_all("td", "cislo")]


def collect_parties(first_link: str) -> List[str]:
    """Vrací seznam všech kandidujících politických stran pro daný okres."""
    html = get_html(first_link)
    return [p.text.strip() for p in html.find_all("td", "overflow_name")]


def get_voters_data(links: List[str]) -> Tuple[List[str], List[str], List[str]]:
    """Vrací počty voličů, vydaných obálek a platných hlasů pro každou obec."""
    voters, envelopes, valid_ones = [], [], []
    for link in links:
        html = get_html(link)
        voters.append(html.find("td", headers="sa2").text.replace("\xa0", " "))
        envelopes.append(html.find("td", headers="sa3").text.replace("\xa0", " "))
        valid_ones.append(html.find("td", headers="sa6").text.replace("\xa0", " "))
    return voters, envelopes, valid_ones


def collect_votes(links: List[str]) -> List[List[str]]:
    """Vrací počty hlasů pro všechny strany a obce."""
    votes = []
    for link in links:
        html = get_html(link)
        # Hlasy jsou ve sloupcích t1sb3 a t2sb3

        votes_cells = html.find_all("td", "cislo", headers=["t1sb3", "t2sb3"])
        votes.append([v.text.strip().replace("\xa0", " ") for v in votes_cells])
    return votes


def create_rows(html: bs4.BeautifulSoup) -> List[List[str]]:
    """Sestaví seznam řádků pro CSV. Každý řádek obsahuje všechny potřebné údaje."""
    links = get_links(html)
    if not links:
        return []
    voters, envelopes, valid_ones = get_voters_data(links)
    towns = get_towns(html)
    ids = get_ids(html)
    votes = collect_votes(links)

    # Každý řádek: [Kód, Název, Voliči, Obálky, Platné hlasy, hlasy pro strany...]

    return [
        [i, t, v, e, val] + vs
        for i, t, v, e, val, vs in zip(ids, towns, voters, envelopes, valid_ones, votes)
    ]


def election2017(link: str) -> Tuple[List[str], List[List[str]]]:
    """Připraví data pro CSV a vrací header a rows."""
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
        print("Použití: python elections_scraper.py <URL> <vystupni_soubor.csv>")
        sys.exit(1)
    address = sys.argv[1]
    file_name = sys.argv[2]

    header, rows = election2017(address)
    if not rows:
        print("Chyba: Nenalezeny žádné údaje.")
        sys.exit(1)
    print("UKLÁDÁM DATA DO SOUBORU:", file_name)
    with open(file_name, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header)
        writer.writerows(rows)
    print("UKONČUJI elections-scraper")