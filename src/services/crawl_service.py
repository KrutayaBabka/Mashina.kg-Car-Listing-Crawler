"""
src/services/crawl_service.py — Core asynchronous crawling service for Mashina.kg car listings.

Author: Danil
Created: 2025-06-22
Description:
    Contains the main crawling workflow that:
    - Builds the list of search result pages
    - Fetches and extracts car listing links from all pages asynchronously
    - Fetches and parses detailed information for each car listing asynchronously
    - Aggregates all results and saves them to a JSON file

Usage:
    Import and call `main_crawl()` from an async context or run via an entry script.

Dependencies:
    - asyncio
    - tqdm (for async progress bars)
    - utils.pagination: page link builder
    - utils.fetch: async-compatible HTML fetcher
    - utils.parse_listings: extract car links from listing pages
    - utils.parse_details: parse detailed car info
    - config: logger instance

"""

import asyncio
import json
from typing import Any, Dict, List
from tqdm.asyncio import tqdm
from utils.pagination import build_page_links
from utils.fetch import fetch_html
from utils.parse_listings import extract_links_from_html
from utils.parse_details import fetch_and_parse_car
from config import logger


async def fetch_and_extract_links(url: str) -> List[Dict[str, Any]]:
    """
    Fetch HTML content for a given URL asynchronously,
    then extract car listing links from the page.

    Args:
        url (str): URL of the listings page.

    Returns:
        List[Dict[str, Any]]: List of dictionaries with link info.
    """
    html: str = await asyncio.to_thread(fetch_html, url)
    return extract_links_from_html(html)


async def main_crawl() -> None:
    """
    Main crawling function that orchestrates the full crawling workflow:
    - Builds page links
    - Fetches car listing URLs from all pages asynchronously
    - Parses car details asynchronously
    - Saves all collected data to 'full_results.json'

    Returns:
        None
    """
    base_url: str = "https://m.mashina.kg/search/all/?page=1"
    links: List[str] = build_page_links(base_url)

    logger.info(f"Start fetching link lists from {len(links)} pages")

    # Fetch all listing pages and extract car links with progress bar
    tasks_links: List[asyncio.Future[List[Dict[str, Any]]]] = [fetch_and_extract_links(link) for link in links]
    all_results: List[List[Dict[str, Any]]] = []
    for coro in tqdm(asyncio.as_completed(tasks_links), total=len(tasks_links), desc="Fetching car links"):
        result: List[Dict[str, Any]] = await coro
        all_results.append(result)

    # Flatten list of lists into a single list of car link dicts
    flat_results: List[Dict[str, Any]] = [item for sublist in all_results for item in sublist]
    logger.info(f"Total car links found: {len(flat_results)}")

    results: List[Dict[str, Any]] = [None] * len(flat_results)

    async def worker(i: int, url: str) -> None:
        """
        Worker coroutine to fetch and parse car details for a single URL.

        Args:
            i (int): Index to store results.
            url (str): URL of the car details page.

        Returns:
            None
        """
        try:
            details: Dict[str, Any] = await fetch_and_parse_car(url)
            results[i] = details
        except Exception as e:
            logger.warning(f"Error parsing {url}: {e}")
            results[i] = {}

    tasks = [worker(i, item["link"]) for i, item in enumerate(flat_results)]

    # Parse car details asynchronously with progress bar
    for f in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Parsing car details"):
        await f

    # Attach parsed details back to the car listing dictionaries
    for i, item in enumerate(flat_results):
        item["car_details"] = results[i]

    # Save results to JSON file
    with open("full_results.json", "w", encoding="utf-8") as f:
        json.dump(flat_results, f, ensure_ascii=False, indent=2)

    logger.info(f"Saved {len(flat_results)} car details to full_results.json")
    print(f"Saved {len(flat_results)} car details to full_results.json")
