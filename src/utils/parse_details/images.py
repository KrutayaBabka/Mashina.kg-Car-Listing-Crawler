from typing import Dict, List
from bs4 import BeautifulSoup


def extract_image_links(soup: BeautifulSoup) -> Dict[str, List[str]]:
    image_div = soup.select("div.fotorama-details a[data-full]")
    links = [tag["data-full"].strip() for tag in image_div if tag.has_attr("data-full")]
    return {"image_links": links}