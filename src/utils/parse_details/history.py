"""
src/utils/parse_details/history.py — Extracts history records related to a car's VIN report.

Author: Danil  
Created: 2025-06-23  
Description:
    Parses the VIN report section on the car detail page to extract
    the car's name, year, and associated history record counts
    from various sources.

Usage:
    from utils.parse_details.history import extract_history_records
"""

import re
from typing import Any, Dict, List, Optional
from bs4 import BeautifulSoup, Tag


def extract_history_records(soup: BeautifulSoup) -> Dict[str, Optional[Dict[str, Any]]]:
    """
    Extract VIN-related history records from the parsed HTML soup.

    Args:
        soup (BeautifulSoup): Parsed HTML of a car detail page.

    Returns:
        Dict[str, Optional[Dict[str, Any]]]: Dictionary with key "vin_report" containing:
            - "car_name_and_year_vin" (str): car name and year info
            - "history_records" (List[Dict[str, Any]]): list of sources and record counts
            or None if no data found.
    """
    vin_report: Dict[str, Any] = {}

    name_block: Optional[BeautifulSoup] = soup.find("div", class_="car-name lw")
    if name_block:
        vin_report["car_name_and_year_vin"] = name_block.get_text(strip=True)

    record_sources: List[Dict[str, Any]] = []

    for span in soup.find_all("span", class_="green"):
        record_text: str = span.get_text(strip=True)

        match: Optional[re.Match[str]] = re.search(r"Найден[ао]?\s+(\d+)\s+запис", record_text, re.IGNORECASE)
        if not match:
            continue

        count: int = int(match.group(1))
        title: Optional[str] = None

        link_div: Optional[BeautifulSoup] = span.find_parent("div", class_="link")
        if link_div:
            title_block: Optional[BeautifulSoup] = link_div.find_previous_sibling("div", class_="title")
            if title_block:
                title: str = title_block.get_text(strip=True)
            else:
                parent: Optional[BeautifulSoup] = link_div
                for _ in range(3):
                    parent: Optional[Tag] = parent.find_parent("div")
                    if not parent:
                        break
                    title_block: Optional[Tag] = parent.find("div", class_="title")
                    if title_block:
                        title: str = title_block.get_text(strip=True)
                        break

        if title:
            record_sources.append({
                "source": title,
                "record_count": count
            })

    if record_sources:
        vin_report["history_records"] = record_sources

    return {"vin_report": vin_report if vin_report else None}
