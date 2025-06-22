"""
src/utils/__init__.py — Utility package initializer.

Author: Danil
Created: 2025-06-23

Description:
    This module re-exports key utility functions from the utils package:
    - fetch_html:       Fetches raw HTML content from a URL.
    - get_total_pages:  Retrieves total pagination page count from a URL.
    - build_page_links: Generates a list of paginated URLs based on the base URL.
    - extract_links_from_html: Extracts car listing links from a page's HTML.
    - extract_car_details: Parses detailed car information from a car page's HTML.
    - fetch_and_parse_car: Fetches a car detail page and parses its data asynchronously.

Usage:
    Import required utility functions directly from utils, for example:
        from utils import fetch_html, build_page_links, extract_links_from_html, fetch_and_parse_car

Project Structure:
    - fetch.py           : HTTP fetching utilities.
    - pagination.py      : Pagination link extraction and generation.
    - parse_listings.py  : Parsing car listing overview pages.
    - parse_details/     : Directory containing detailed car page parsers.
"""

from .fetch import fetch_html
from .pagination import get_total_pages, build_page_links
from .parse_listings import extract_links_from_html
from .parse_details import extract_car_details, fetch_and_parse_car
