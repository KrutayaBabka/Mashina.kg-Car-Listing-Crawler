"""
src/utils/parse_details/breadcrumbs.py — Extracts car breadcrumb navigation (brand, model, generation) from HTML.

Author: Danil  
Created: 2025-06-22  
Description:
    Parses breadcrumb elements from a car detail page HTML using schema.org markup.
    Extracts brand, model, and generation if present.

Usage:
    from utils.parse_details.breadcrumbs import extract_car_breadcrumbs
"""

from bs4 import BeautifulSoup, Tag
from typing import Dict, Optional


def extract_car_breadcrumbs(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    """
    Extract car brand, model, and generation from breadcrumb navigation.

    Args:
        soup (BeautifulSoup): Parsed HTML of a car detail page.

    Returns:
        Dict[str, Optional[str]]: Keys "brand", "model", "generation" with string values or None.
    """
    result: Dict[str, Optional[str]] = {"brand": None, "model": None, "generation": None}
    breadcrumb_items = soup.find_all("li", itemtype="https://schema.org/ListItem")

    if len(breadcrumb_items) >= 3:
        try:
            brand_tag: Optional[Tag] = breadcrumb_items[-3].find("span", itemprop="name")
            model_tag: Optional[Tag] = breadcrumb_items[-2].find("span", itemprop="name")
            generation_tag: Optional[Tag] = breadcrumb_items[-1].find("span", itemprop="name")

            result["brand"] = brand_tag.get_text(strip=True) if brand_tag else None
            result["model"] = model_tag.get_text(strip=True) if model_tag else None
            result["generation"] = generation_tag.get_text(strip=True) if generation_tag else None
        except Exception:
            # Log or pass silently depending on your logging strategy
            pass

    return result
