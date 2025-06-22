"""
src/utils/parse_details/__init__.py — High-level car detail extractor and parser.

Author: Danil  
Created: 2025-06-22  
Description:
    This module provides:
    - `extract_car_details(html: str)`: parses all structured blocks from raw car detail HTML
    - `fetch_and_parse_car(url: str)`: fetches HTML from a given car detail URL and parses it

    The module aggregates individual extractors (breadcrumbs, specs, pricing, images, etc.)
    and composes a full dictionary of car information.

Usage:
    from utils.parse_details import fetch_and_parse_car

Dependencies:
    - asyncio
    - BeautifulSoup4
    - config.logger
    - utils.fetch.fetch_html
"""

import asyncio
from bs4 import BeautifulSoup
from typing import Dict, Optional

from utils.fetch import fetch_html

from .breadcrumbs import extract_car_breadcrumbs
from .head_info import extract_head_info
from .credit import extract_credit_title
from .contact import extract_contact_info
from .images import extract_image_links
from .specs import extract_main_specs
from .average_price import extract_average_price
from .seller_comment import extract_seller_comment
from .configuration import extract_configuration_options
from .history import extract_history_records
from .vin import extract_vin_code

from config import logger


def extract_car_details(html: str) -> Dict[str, Optional[str]]:
    """
    Extract structured car data from a single detail page's HTML.

    Args:
        html (str): Raw HTML content of a car detail page.

    Returns:
        Dict[str, Optional[str]]: Parsed fields including specs, prices, contacts, VIN, etc.
    """
    soup: BeautifulSoup = BeautifulSoup(html, "html.parser")
    details: Dict[str, Optional[str]] = {}

    details.update(extract_car_breadcrumbs(soup))
    details.update(extract_head_info(soup))
    details.update(extract_credit_title(soup))
    details.update(extract_contact_info(soup))
    details.update(extract_image_links(soup))
    details.update(extract_main_specs(soup))
    details.update(extract_average_price(soup))
    details.update(extract_seller_comment(soup))
    details.update(extract_configuration_options(soup))
    details.update(extract_history_records(soup))
    details.update(extract_vin_code(soup))

    return details


async def fetch_and_parse_car(url: str) -> Dict[str, Optional[str]]:
    """
    Asynchronously fetch a car detail page and extract all relevant data.

    Args:
        url (str): The full URL of a car detail page.

    Returns:
        Dict[str, Optional[str]]: Dictionary of extracted fields or empty dict on failure.
    """
    html: str = await asyncio.to_thread(fetch_html, url)
    if not html:
        logger.warning(f"No HTML content fetched for {url}")
        return {}

    details: Dict[str, Optional[str]] = extract_car_details(html)
    logger.info(f"Parsed details for {url}")
    return details
