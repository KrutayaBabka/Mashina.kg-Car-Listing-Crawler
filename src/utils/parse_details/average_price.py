"""
src/utils/parse_details/average_price.py — Extracts average market price block from a car detail page.

Author: Danil  
Created: 2025-06-22  
Description:
    Parses the "Средняя цена по рынку" section of mashina.kg car detail page.
    Extracts:
    - Description (e.g., "Средняя цена аналогичных автомобилей")
    - Average price in USD

Usage:
    from utils.parse_details.average_price import extract_average_price
"""

from typing import Dict, Optional
from bs4 import BeautifulSoup, Tag


def extract_average_price(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    """
    Extracts the average market price block from the given car detail soup.

    Args:
        soup (BeautifulSoup): Parsed HTML of the car detail page.

    Returns:
        Dict[str, Optional[str]]: A dictionary containing:
            - 'average_price_desc': Description of average pricing (if available)
            - 'average_price_usd': Extracted USD price (if available)
    """
    block: Optional[Tag] = soup.select_one("div.details-stat")
    if not block:
        return {"average_price_desc": None, "average_price_usd": None}

    desc_tag: Optional[Tag] = block.select_one("p b")
    description: Optional[str] = desc_tag.get_text(" ", strip=True) if desc_tag else None

    price_tag: Optional[Tag] = block.select_one("span.formatted-anal")
    price_usd: Optional[str] = price_tag.get_text(strip=True) if price_tag else None

    return {
        "average_price_desc": description,
        "average_price_usd": price_usd,
    }
