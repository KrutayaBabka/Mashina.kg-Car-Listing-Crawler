````markdown
# 🚗 Mashina.kg Car Listing Crawler

A fast and modular asynchronous crawler that collects detailed car listings from [m.mashina.kg](https://m.mashina.kg), extracts structured vehicle data, and saves it as JSON for further analysis or integration.

**Author:** Danil  
**Created:** 2025-06-22  
**Python version:** 3.8+

---

## 📌 Features

- ✅ Collects all paginated car listing links from Mashina.kg  
- ✅ Parses individual car detail pages asynchronously  
- ✅ Extracts brand, model, year, mileage, prices, configuration, seller info, VIN, etc.  
- ✅ Aggregates results and saves to `full_results.json`  
- ✅ Modular extractor system: easy to test, maintain, extend

---

## 🛠 Installation

```bash
git clone https://github.com/your-username/mashina-kg-crawler.git
cd mashina-kg-crawler
python -m venv venv
venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate     # On Linux/Mac

pip install -r requirements.txt
````

---

## 🚀 Usage

Run the crawler:

```bash
python src/main.py
```

Output:

* Scraped data will be saved to:
  `full_results.json`
* Logs will be written to:
  `app.log`

---

## 📁 Project Structure

```
src/
│
├── main.py                    # Entry point for the crawler
├── config.py                  # Global configuration and logging setup
│
├── services/
│   └── crawl_service.py       # Orchestrates crawling and data saving
│
├── utils/
│   ├── __init__.py            # Re-exports key functions
│   ├── fetch.py               # HTML fetcher using requests
│   ├── pagination.py          # Total pages & page URL builder
│   ├── parse_listings.py      # Parses overview listing cards
│   └── parse_details/         # All individual field extractors
│       ├── __init__.py
│       ├── average_price.py
│       ├── breadcrumbs.py
│       ├── configuration.py
│       ├── contact.py
│       ├── credit.py
│       ├── head_info.py
│       ├── history.py
│       ├── images.py
│       ├── seller_comment.py
│       ├── specs.py
│       └── vin.py
│
└── data/
    └── reference_data/        # Optional: example raw HTML & expected JSON output
```

---

## 🧪 Reference Data (Optional)

You can find sample HTML and JSON output in:

```
data/reference_data/
```

These files are useful for:

* Debugging changes to extractors
* Validating output format
* Unit tests or future dataset development

---

## 🧩 Dependencies

* `requests`
* `aiohttp`
* `tqdm`
* `beautifulsoup4`

Install all from:

```
requirements.txt
```

---

## ✅ Logging

* Log file: `app.log`
* Format: `[YYYY-MM-DD HH:MM:SS] LEVEL: message`
* Configured globally via `logging` in `config.py`

---

## 📄 License

This project is licensed for educational and research purposes. Please respect the terms of use of the mashina.kg website.

---

## 🙌 Contributing

Pull requests, bug reports, and suggestions are welcome!

---
