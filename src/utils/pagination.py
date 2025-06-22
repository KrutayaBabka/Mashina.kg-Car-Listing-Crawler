from bs4 import BeautifulSoup
import requests
from typing import List
from config import logger

def get_total_pages(url: str) -> int:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch URL: {e}")
        raise Exception(f"Failed to fetch URL: {e}")

    soup = BeautifulSoup(response.text, "html.parser")
    all_links = soup.select('ul.pagination a[data-page]')

    for link in reversed(all_links):
        if link.text.strip().lower() == "последняя":
            page_number = link.get("data-page")
            if page_number and page_number.isdigit():
                logger.info(f"Total pages found: {page_number}")
                return int(page_number)

    logger.error("Pagination element with 'Последняя' not found.")
    raise Exception("Pagination element with 'Последняя' not found.")


def build_page_links(base_url: str) -> List[str]:
    total_pages = get_total_pages(base_url)
    return [f"https://m.mashina.kg/search/all/?page={i}" for i in range(1, total_pages + 1)]
