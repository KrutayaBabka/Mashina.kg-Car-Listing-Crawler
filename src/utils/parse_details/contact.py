"""
src/utils/parse_details/contact.py — Extracts contact information from a car detail page.

Author: Danil  
Created: 2025-06-22  
Description:
    Parses user name, profile URL, and phone number from the contact block of the page.

Usage:
    from utils.parse_details.contact import extract_contact_info
"""

from typing import Dict, Optional
from urllib.parse import urljoin
from bs4 import BeautifulSoup, Tag

from config import BASE_URL


def extract_contact_info(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    """
    Extract user contact information.

    Args:
        soup (BeautifulSoup): Parsed HTML of a car detail page.

    Returns:
        Dict[str, Optional[str]]: Dictionary with keys:
            - "user_name": name of the seller or None
            - "user_profile_url": full URL to the user profile or None
            - "phone_number": seller's phone number or None
    """
    contact_div: Optional[Tag] = soup.select_one("div.personal-info.details-phone-wrap")
    if not contact_div:
        return {
            "user_name": None,
            "user_profile_url": None,
            "phone_number": None
        }

    user_name_tag: Optional[Tag] = contact_div.select_one("span.i-name")
    user_name: Optional[str] = user_name_tag.get_text(strip=True) if user_name_tag else None

    profile_link_tag: Optional[Tag] = contact_div.select_one("a[href^='/user/']")
    profile_url: Optional[str] = urljoin(BASE_URL, profile_link_tag['href']) if profile_link_tag else None

    phone_tag: Optional[Tag] = contact_div.select_one("div.number")
    phone_number: Optional[str] = phone_tag.get_text(strip=True) if phone_tag else None

    return {
        "user_name": user_name,
        "user_profile_url": profile_url,
        "phone_number": phone_number
    }
