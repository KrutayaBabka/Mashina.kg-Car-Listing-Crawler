from bs4 import BeautifulSoup
from typing import Dict, Optional

def extract_car_breadcrumbs(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    result = {"brand": None, "model": None, "generation": None}
    breadcrumb_items = soup.find_all("li", itemtype="https://schema.org/ListItem")

    if len(breadcrumb_items) >= 3:
        try:
            result["brand"] = breadcrumb_items[-3].find("span", itemprop="name").get_text(strip=True)
            result["model"] = breadcrumb_items[-2].find("span", itemprop="name").get_text(strip=True)
            result["generation"] = breadcrumb_items[-1].find("span", itemprop="name").get_text(strip=True)
        except Exception:
            pass
    return result
