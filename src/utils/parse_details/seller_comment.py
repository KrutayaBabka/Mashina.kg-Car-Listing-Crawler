from typing import Dict, Optional
from bs4 import BeautifulSoup


def extract_seller_comment(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    block = soup.select_one("div.seller-comments span.original")
    if block:
        return {"seller_comment": block.get_text(strip=True, separator="\n")}
    return {"seller_comment": None}