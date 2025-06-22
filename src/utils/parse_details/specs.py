"""
src/utils/parse_details/specs.py — Extract main specifications of a car from the detail page HTML.

Author: Danil
Created: 2025-06-23
Description:
    Parses key car specification fields such as year, mileage, color, engine, etc.
    Maps Russian labels to standardized English keys.

"""

from typing import Dict, Optional
from bs4 import BeautifulSoup, Tag


def extract_main_specs(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    label_map: Dict[str, str] = {
        "год выпуска": "year",
        "пробег": "mileage",
        "кузов": "body_type",
        "цвет": "color",
        "двигатель": "engine",
        "коробка": "transmission",
        "привод": "drive_type",
        "руль": "steering_wheel",
        "состояние": "condition",
        "таможня": "customs_cleared",
        "обмен": "exchange",
        "наличие": "availability",
        "регион, город": "car_location",
        "учёт": "registration_country",
        "прочее": "other_info",
        "vin": "vin",
    }

    specs: Dict[str, Optional[str]] = {v: None for v in label_map.values()}

    rows: list[Tag] = soup.select("div.tab-content div.field-row.clr")

    for row in rows:
        label_tag: Optional[Tag] = row.select_one("div.field-label")
        value_tag: Optional[Tag] = row.select_one("div.field-value")

        if not label_tag or not value_tag:
            continue

        raw_label: str = label_tag.get_text(strip=True).lower()
        key: Optional[str] = label_map.get(raw_label)

        if not key:
            continue  

        if raw_label == "пробег":
            hidden_span: Optional[Tag] = value_tag.select_one("span.mileage-source")
            value: str = (hidden_span.get_text(strip=True) + " км") if hidden_span else value_tag.get_text(strip=True)
        else:
            value: str = value_tag.get_text(strip=True)

        specs[key] = value

    return specs
