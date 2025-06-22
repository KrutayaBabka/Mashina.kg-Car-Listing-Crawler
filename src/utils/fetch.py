"""
src/utils/fetch.py — Utility function for synchronous HTML fetching.

Author: Danil  
Created: 2025-06-22  
Description:
    Provides a helper function to fetch raw HTML content from a given URL using
    the `requests` library. Standard headers and logging are applied globally.

Usage:
    from utils.fetch import fetch_html
    html = fetch_html("https://example.com/page")

Dependencies:
    - requests
    - config.HEADERS for HTTP headers
    - config.logger for logging

Returns:
    - str: Raw HTML content if successful, or empty string on failure.
"""

import requests
from requests import Response
from config import HEADERS, logger


def fetch_html(url: str) -> str:
    """
    Fetch HTML content from the given URL using synchronous requests.

    Args:
        url (str): The target URL to fetch HTML content from.

    Returns:
        str: The HTML content of the page, or an empty string if the request fails.
    """
    try:
        response: Response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        logger.info(f"Fetched: {url}")
        return response.text
    except Exception as e:
        logger.error(f"Failed to fetch {url}: {e}")
        return ""
