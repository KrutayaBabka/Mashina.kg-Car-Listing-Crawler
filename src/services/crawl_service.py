import asyncio
import json
from tqdm.asyncio import tqdm
from utils.pagination import build_page_links
from utils.fetch import fetch_html
from utils.parse_listings import extract_links_from_html
from utils.parse_details import fetch_and_parse_car
from config import logger


async def fetch_and_extract_links(url: str):
    html = await asyncio.to_thread(fetch_html, url)
    return extract_links_from_html(html)


async def main_crawl():
    base_url = "https://m.mashina.kg/search/all/?page=1"
    links = build_page_links(base_url)

    logger.info(f"Start fetching link lists from {len(links)} pages")

    tasks_links = [fetch_and_extract_links(link) for link in links]
    all_results = []
    for coro in tqdm(asyncio.as_completed(tasks_links), total=len(tasks_links), desc="Fetching car links"):
        result = await coro
        all_results.append(result)

    flat_results = [item for sublist in all_results for item in sublist]
    logger.info(f"Total car links found: {len(flat_results)}")

    results = [None] * len(flat_results)

    async def worker(i: int, url: str):
        try:
            details = await fetch_and_parse_car(url)
            results[i] = details
        except Exception as e:
            logger.warning(f"Error parsing {url}: {e}")
            results[i] = {}

    tasks = [worker(i, item["link"]) for i, item in enumerate(flat_results)]
    for f in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Parsing car details"):
        await f

    for i, item in enumerate(flat_results):
        item["car_details"] = results[i]

    with open("full_results.json", "w", encoding="utf-8") as f:
        json.dump(flat_results, f, ensure_ascii=False, indent=2)

    logger.info(f"Saved {len(flat_results)} car details to full_results.json")
    print(f"Saved {len(flat_results)} car details to full_results.json")
