"""
src/utils/parse_details/seller_comment.py — Extracts seller's comment from the car detail page HTML.

Author: Danil
Created: 2025-06-23
Description:
    Contains a function to parse the seller's comment text if present.
"""

from typing import Dict, Optional
from bs4 import BeautifulSoup, Tag

def extract_seller_comment(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    block: Optional[Tag] = soup.select_one("div.seller-comments span.original")
    if block:
        return {"seller_comment": block.get_text(strip=True, separator="\n")}
    return {"seller_comment": None}
