"""
src/utils/parse_details/configuration.py — Extracts configuration options section from a car detail page.

Author: Danil  
Created: 2025-06-22  
Description:
    Parses the "configuration" block of the car detail HTML page,
    extracting sections with lists of options.

Usage:
    from utils.parse_details.configuration import extract_configuration_options
"""

from typing import Dict, List, Optional
from bs4 import BeautifulSoup, Tag


def extract_configuration_options(soup: BeautifulSoup) -> Dict[str, Optional[Dict[str, List[str]]]]:
    """
    Extracts configuration options from the given BeautifulSoup object.

    Args:
        soup (BeautifulSoup): Parsed HTML of the car detail page.

    Returns:
        Dict[str, Optional[Dict[str, List[str]]]]: 
            A dictionary with key 'configuration' that maps to another dictionary,
            where keys are section names and values are lists of option strings.
            Returns {'configuration': None} if the configuration block is not found.
    """
    config_block: Optional[Tag] = soup.select_one("div.configuration")
    if not config_block:
        return {"configuration": None}

    configuration: Dict[str, List[str]] = {}
    names: Optional[Tag] = config_block.select("div.name")
    values: Optional[Tag] = config_block.select("div.value")

    for name_div, value_div in zip(names, values):
        section_name: str = name_div.get_text(strip=True)
        options: List[str] = [
            p.get_text(strip=True) 
            for p in value_div.select("p") 
            if p.get_text(strip=True)
        ]
        configuration[section_name] = options

    return {"configuration": configuration}
