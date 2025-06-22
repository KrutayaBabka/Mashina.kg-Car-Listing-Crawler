"""
src/config.py — Global configuration for the Mashina.kg crawler project.

Author: Danil
Created: 2025-06-22
Description:
    This module contains project-wide configuration constants and logging setup,
    including:
    - Base URL for mashina.kg
    - Standard HTTP headers for requests
    - Logging configuration (writes to app.log)

Usage:
    Import `BASE_URL`, `HEADERS`, and `logger` wherever needed.

Project Notes:
    - `BASE_URL` and `HEADERS` are used in both synchronous and asynchronous requests
    - Logging is configured globally and will write to `app.log` in append mode
"""

from typing import Dict


BASE_URL: str = "https://m.mashina.kg"

HEADERS: Dict[str, str] = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/114.0.0.0 Safari/537.36"
    )
}

import logging
logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)
logger: logging.Logger = logging.getLogger(__name__)
