"""
src/utils/pagination.py — Utilities for pagination handling on mashina.kg.

Author: Danil  
Created: 2025-06-22  
Description:
    Provides functions to:
    - Determine the total number of pages in search results
    - Build full list of paginated search result URLs

Usage:
    from utils.pagination import build_page_links
    links = build_page_links("https://m.mashina.kg/search/all/?page=1")

Dependencies:
    - requests
    - BeautifulSoup4
    - config.logger for logging
"""

from bs4 import BeautifulSoup, Tag
import requests
from typing import List
from config import logger


def get_total_pages(url: str) -> int:
    """
    Determine the total number of pages in the search result pagination.

    Args:
        url (str): A URL pointing to the first page of search results.

    Returns:
        int: Total number of pages available.

    Raises:
        Exception: If the pagination structure is not found or request fails.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch URL: {e}")
        raise Exception(f"Failed to fetch URL: {e}")

    soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
    all_links: List[Tag] = soup.select('ul.pagination a[data-page]')

    for link in reversed(all_links):
        if link.text.strip().lower() == "последняя":
            page_number = link.get("data-page")
            if page_number and page_number.isdigit():
                logger.info(f"Total pages found: {page_number}")
                return int(page_number)

    logger.error("Pagination element with 'Последняя' not found.")
    raise Exception("Pagination element with 'Последняя' not found.")


def build_page_links(base_url: str) -> List[str]:
    """
    Build a list of paginated search result URLs based on total pages.

    Args:
        base_url (str): A base URL starting from page 1 of the search results.

    Returns:
        List[str]: List of full URLs for each page of the search results.
    """
    total_pages: int = get_total_pages(base_url)
    return [f"https://m.mashina.kg/search/all/?page={i}" for i in range(1, total_pages + 1)]
