from typing import Dict, Optional
from bs4 import BeautifulSoup


def extract_average_price(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    block = soup.select_one("div.details-stat")
    if not block:
        return {"average_price_desc": None, "average_price_usd": None}

    desc_tag = block.select_one("p b")
    description = (
        desc_tag.get_text(" ", strip=True) if desc_tag else None
    )

    price_tag = block.select_one("span.formatted-anal")
    price_usd = price_tag.get_text(strip=True) if price_tag else None

    return {
        "average_price_desc": description,
        "average_price_usd": price_usd,
    }