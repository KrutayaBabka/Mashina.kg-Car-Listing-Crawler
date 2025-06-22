"""
src/main.py — Entry point of the Mashina.kg car listing crawler.

Author: Danil
Created: 2025-06-22
Description:
    This script launches the asynchronous crawling process that:
    - Collects car listing links from all pages of mashina.kg
    - Parses each individual car's detail page
    - Aggregates and saves the full data to a JSON file

Usage:
    Run directly with Python:
        python main.py

Dependencies:
    - Python 3.8+
    - aiohttp, requests, BeautifulSoup4, tqdm, etc.

Project Structure:
    - services/crawl_service.py   : core crawling and parsing logic
    - utils/parse_details/        : individual detail extractors
    - config.py                   : configuration and logging setup
    - data/reference_data/        : sample HTML pages and expected JSON output
                                     (useful for tests and quick inspection)

"""

import asyncio
from services.crawl_service import main_crawl

if __name__ == "__main__":
    asyncio.run(main_crawl())
