"""
src/utils/parse_details/head_info.py — Extracts main header information from a car detail page.

Author: Danil  
Created: 2025-06-22  
Description:
    Parses title, model info, location, update times, views, favorites, and prices in different currencies.

Usage:
    from utils.parse_details.head_info import extract_head_info
"""

from typing import Dict, Optional
from bs4 import BeautifulSoup, Tag


def extract_head_info(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    """
    Extract main header info from the page.

    Args:
        soup (BeautifulSoup): Parsed HTML of a car detail page.

    Returns:
        Dict[str, Optional[str]]: Dictionary with keys:
            - title
            - model_info
            - location
            - updated
            - posted
            - views
            - favorites
            - price_usd
            - price_kgs
            - price_rub
            - price_kzt
    """
    wrapper: Optional[Tag] = soup.select_one("div.head-wrapper-main")
    if wrapper is None:
        return {k: None for k in (
            "title", "model_info", "location", "updated", "posted",
            "views", "favorites", "price_usd", "price_kgs",
            "price_rub", "price_kzt"
        )}

    title_tag: Optional[Tag] = wrapper.select_one("div.head-left h1")
    model_input: Optional[Tag] = wrapper.select_one("div.head-left input.ad-title-value")
    location_link: Optional[Tag] = wrapper.select_one("div.head-left .location a")
    updated_span: Optional[Tag] = wrapper.select_one("div.head-left .upped-at .arrow-up")
    posted_span: Optional[Tag] = wrapper.select_one("div.head-left .upped-at span:nth-of-type(2)")
    views_span: Optional[Tag] = wrapper.select_one("div.head-left .counters .views")
    favorites_span: Optional[Tag] = wrapper.select_one("div.head-left .counters .heart")
    price_usd_span: Optional[Tag] = wrapper.select_one("div.head-right .prices-block .main .price-dollar span")
    price_kgs_div: Optional[Tag] = wrapper.select_one("div.head-right .prices-block .main .price-som")
    price_rub_div: Optional[Tag] = wrapper.select_one("div.head-right .prices-block .addit .price-som:nth-of-type(1)")
    price_kzt_div: Optional[Tag] = wrapper.select_one("div.head-right .prices-block .addit .price-som:nth-of-type(2)")

    return {
        "title": title_tag.get_text(strip=True) if title_tag else None,
        "model_info": model_input["value"].strip() if model_input else None,
        "location": location_link.get_text(strip=True) if location_link else None,
        "updated": updated_span.get_text(strip=True) if updated_span else None,
        "posted": posted_span.get_text(strip=True) if posted_span else None,
        "views": views_span.get_text(strip=True) if views_span else None,
        "favorites": favorites_span.get_text(strip=True) if favorites_span else None,
        "price_usd": price_usd_span.get_text(strip=True) if price_usd_span else None,
        "price_kgs": price_kgs_div.get_text(strip=True) if price_kgs_div else None,
        "price_rub": price_rub_div.get_text(strip=True) if price_rub_div else None,
        "price_kzt": price_kzt_div.get_text(strip=True) if price_kzt_div else None,
    }
