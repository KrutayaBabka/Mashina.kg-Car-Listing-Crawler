from typing import Dict, Optional
from bs4 import BeautifulSoup


def extract_credit_title(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    block = soup.find("div", id="details-actions-block")
    if not block:
        return {"credit_offer": None}

    title_div = block.select_one("div.credit-button-top .content .title")
    if title_div:
        return {"credit_offer": title_div.get_text(strip=True)}
    return {"credit_offer": None}