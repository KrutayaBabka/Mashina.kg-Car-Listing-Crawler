from typing import Dict, Optional
from bs4 import BeautifulSoup


def extract_main_specs(soup: BeautifulSoup) -> Dict[str, Optional[str]]:
    label_map = {
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

    rows = soup.select("div.tab-content div.field-row.clr")

    for row in rows:
        label_tag = row.select_one("div.field-label")
        value_tag = row.select_one("div.field-value")

        if not label_tag or not value_tag:
            continue

        raw_label = label_tag.get_text(strip=True).lower()
        key = label_map.get(raw_label)

        if not key:
            continue  

        if raw_label == "пробег":
            hidden_span = value_tag.select_one("span.mileage-source")
            value = hidden_span.get_text(strip=True) + " км" if hidden_span else value_tag.get_text(strip=True)
        else:
            value = value_tag.get_text(strip=True)

        specs[key] = value

    return specs