from typing import Dict, Optional
from bs4 import BeautifulSoup


def extract_vin_code(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    vin_link = soup.find("a", class_="btn-product-modal", attrs={"data-vincode": True})
    vin_code = vin_link.get("data-vincode", "").strip() if vin_link else None
    return {"vin_code": vin_code or None}