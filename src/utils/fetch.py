import requests
from requests import Response
from config import HEADERS, logger

def fetch_html(url: str) -> str:
    try:
        response: Response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        logger.info(f"Fetched: {url}")
        return response.text
    except Exception as e:
        logger.error(f"Failed to fetch {url}: {e}")
        return ""