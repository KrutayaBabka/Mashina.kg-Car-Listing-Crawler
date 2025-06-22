"""
src/utils/parse_details/images.py — Extractor module for car image URLs from Mashina.kg detail pages.

Author: Danil
Created: 2025-06-23
Description:
    This module contains functions to parse and extract all image URLs
    from the car detail page HTML content using BeautifulSoup.

Usage:
    Import `extract_image_links` and pass a BeautifulSoup-parsed HTML document.

Dependencies:
    - beautifulsoup4

"""

from typing import Dict, List
from bs4 import BeautifulSoup, Tag


def extract_image_links(soup: BeautifulSoup) -> Dict[str, List[str]]:
    """
    Extracts image URLs from the car detail page soup.

    Args:
        soup (BeautifulSoup): Parsed HTML of the car detail page.

    Returns:
        Dict[str, List[str]]: Dictionary with key 'image_links' and list of image URLs as value.
    """
    image_div: List[Tag] = soup.select("div.fotorama-details a[data-full]")
    links: List[str] = [tag["data-full"].strip() for tag in image_div if tag.has_attr("data-full")]
    return {"image_links": links}
