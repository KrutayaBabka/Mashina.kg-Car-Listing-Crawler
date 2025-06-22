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
    soup = BeautifulSoup(html, "html.parser")
    details = {}
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


async def fetch_and_parse_car(url: str) -> dict:
    html = await asyncio.to_thread(fetch_html, url)
    if not html:
        logger.warning(f"No HTML content fetched for {url}")
        return {}
    details = extract_car_details(html)
    logger.info(f"Parsed details for {url}")
    return details
