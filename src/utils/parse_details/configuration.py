from typing import Dict, List, Optional
from bs4 import BeautifulSoup


def extract_configuration_options(soup: BeautifulSoup) -> Dict[str, Optional[Dict[str, List[str]]]]:
    config_block = soup.select_one("div.configuration")
    if not config_block:
        return {"configuration": None}

    configuration: Dict[str, List[str]] = {}
    names = config_block.select("div.name")
    values = config_block.select("div.value")

    for name_div, value_div in zip(names, values):
        section_name = name_div.get_text(strip=True)
        options = [p.get_text(strip=True) for p in value_div.select("p") if p.get_text(strip=True)]
        configuration[section_name] = options

    return {"configuration": configuration}