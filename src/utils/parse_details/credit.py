"""
src/utils/parse_details/credit.py — Extracts credit offer title from a car detail page.

Author: Danil  
Created: 2025-06-22  
Description:
    Parses the credit offer title from the details actions block of the page.

Usage:
    from utils.parse_details.credit import extract_credit_title
"""

from typing import Dict, Optional
from bs4 import BeautifulSoup, Tag


def extract_credit_title(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    """
    Extract credit offer title from the given BeautifulSoup object.

    Args:
        soup (BeautifulSoup): Parsed HTML of a car detail page.

    Returns:
        Dict[str, Optional[str]]: Dictionary with key 'credit_offer' and the offer title or None.
    """
    block: Optional[Tag] = soup.find("div", id="details-actions-block")
    if not block:
        return {"credit_offer": None}

    title_div: Optional[Tag] = block.select_one("div.credit-button-top .content .title")
    if title_div:
        return {"credit_offer": title_div.get_text(strip=True)}
    return {"credit_offer": None}
