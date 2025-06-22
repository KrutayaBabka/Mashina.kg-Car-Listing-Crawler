import re
from typing import Any, Dict, Optional
from bs4 import BeautifulSoup


def extract_history_records(soup: BeautifulSoup) -> Dict[str, Optional[Dict[str, Any]]]:
    vin_report = {}

    name_block = soup.find("div", class_="car-name lw")
    if name_block:
        vin_report["car_name_and_year_vin"] = name_block.get_text(strip=True)

    record_sources = []

    for span in soup.find_all("span", class_="green"):
        record_text = span.get_text(strip=True)

        match = re.search(r"Найден[ао]?\s+(\d+)\s+запис", record_text, re.IGNORECASE)
        if match:
            count = int(match.group(1))
            title = None

            link_div = span.find_parent("div", class_="link")

            if link_div:
                title_block = link_div.find_previous_sibling("div", class_="title")
                if title_block:
                    title = title_block.get_text(strip=True)
                else:
                    parent = link_div
                    for _ in range(3):
                        parent = parent.find_parent("div")
                        if parent:
                            title_block = parent.find("div", class_="title")
                            if title_block:
                                title = title_block.get_text(strip=True)
                                break

            if title:
                record_sources.append({
                    "source": title,
                    "record_count": count
                })

    if record_sources:
        vin_report["history_records"] = record_sources

    return {"vin_report": vin_report if vin_report else None}