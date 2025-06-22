"""
src/utils/parse_listings.py — Extracts car listing links from mashina.kg listing HTML.

Author: Danil  
Created: 2025-06-22  
Description:
    Parses the search result page HTML to extract:
    - URLs of individual car listings
    - 'Срочно' status if available
    - Feature tags (e.g., VIP, Premium, Colored, AutoUp)

Usage:
    from utils.parse_listings import extract_links_from_html
    links = extract_links_from_html(html_content)

Dependencies:
    - BeautifulSoup4
    - config.BASE_URL for absolute URL joining
"""

from bs4 import BeautifulSoup
from bs4.element import Tag
from typing import List, Dict, Optional, Set
from urllib.parse import urljoin
from config import BASE_URL


def extract_links_from_html(html: str) -> List[Dict[str, str]]:
    """
    Extracts car listing links and metadata from the HTML of a search result page.

    Args:
        html (str): Raw HTML content of a search results page.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing:
            - 'link': Full URL to the car listing
            - 'status': 'Срочно' label if present
            - 'features': List of paid features (vip, premium, etc.)
    """
    soup: BeautifulSoup = BeautifulSoup(html, "html.parser")
    items: List[Tag] = soup.select('div.list-item.list-label')
    results: List[Dict[str, str]] = []

    for item in items:
        link_tag = item.find('a', href=True)
        if not link_tag:
            continue

        # Build full link to car detail page
        link: str = urljoin(BASE_URL, link_tag['href'])

        # Check if listing is marked as 'Срочно'
        urgent_tag: Optional[Tag] = item.select_one('.urgent-label')
        status: Optional[str] = urgent_tag.get_text(strip=True) if urgent_tag else None

        # Detect features like VIP, Premium, etc. based on image src
        features: Set[str] = set()
        for img in item.select('div.vip-list img[src]'):
            src = img['src']
            if 'vip' in src:
                features.add("vip")
            if 'premium' in src:
                features.add("premium")
            if 'color' in src:
                features.add("color")
            if 'autoup' in src:
                features.add("autoup")

        results.append({
            "link": link,
            "status": status,
            "features": list(features)
        })

    return results
