"""
src/utils/parse_details/vin.py — Extract VIN code from the car detail page HTML.

Author: Danil
Created: 2025-06-23
Description:
    Parses the VIN (Vehicle Identification Number) code from the page,
    if available, and returns it in a dictionary.

"""

from typing import Dict, Optional
from bs4 import BeautifulSoup, Tag


def extract_vin_code(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    vin_link: Optional[Tag] = soup.find("a", class_="btn-product-modal", attrs={"data-vincode": True})
    vin_code: Optional[str] = vin_link.get("data-vincode", "").strip() if vin_link else None
    return {"vin_code": vin_code or None}
