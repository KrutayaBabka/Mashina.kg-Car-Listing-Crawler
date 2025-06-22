from bs4 import BeautifulSoup
from bs4.element import Tag
from typing import List, Dict
from urllib.parse import urljoin
from config import BASE_URL

def extract_links_from_html(html: str) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    items: List[Tag] = soup.select('div.list-item.list-label')
    results = []

    for item in items:
        link_tag = item.find('a', href=True)
        if not link_tag:
            continue

        link = urljoin(BASE_URL, link_tag['href'])
        urgent_tag = item.select_one('.urgent-label')
        status = urgent_tag.get_text(strip=True) if urgent_tag else None

        features = set()
        for img in item.select('div.vip-list img[src]'):
            src = img['src']
            if 'vip' in src: features.add("vip")
            if 'premium' in src: features.add("premium")
            if 'color' in src: features.add("color")
            if 'autoup' in src: features.add("autoup")

        results.append({
            "link": link,
            "status": status,
            "features": list(features)
        })

    return results
