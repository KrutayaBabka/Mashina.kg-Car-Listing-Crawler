from typing import Dict, Optional
from urllib.parse import urljoin
from bs4 import BeautifulSoup

from config import BASE_URL


def extract_contact_info(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    contact_div = soup.select_one("div.personal-info.details-phone-wrap")
    if not contact_div:
        return {
            "user_name": None,
            "user_profile_url": None,
            "phone_number": None
        }

    user_name_tag = contact_div.select_one("span.i-name")
    user_name = user_name_tag.get_text(strip=True) if user_name_tag else None

    profile_link_tag = contact_div.select_one("a[href^='/user/']")
    profile_url = urljoin(BASE_URL, profile_link_tag['href']) if profile_link_tag else None

    phone_tag = contact_div.select_one("div.number")
    phone_number = phone_tag.get_text(strip=True) if phone_tag else None

    return {
        "user_name": user_name,
        "user_profile_url": profile_url,
        "phone_number": phone_number
    }
