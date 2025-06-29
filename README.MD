````markdown
# 🚗 Mashina.kg Car Listing Crawler

A fast, **asynchronous** crawler that collects detailed car listings from  
[m.mashina.kg](https://m.mashina.kg), extracts structured vehicle data, and saves the
results as JSON for further analysis or integration.

**Author:** Danil  
**Created:** 2025-06-22  
**Python version:** 3.8 +

---

## 📌 Features

| Feature                                                                      | Status |
|------------------------------------------------------------------------------|--------|
|Collect links from **all** paginated search pages                             |   ✅   |
|Parse each car-detail page **concurrently**                                   |   ✅   |
|Extract brand, model, year, mileage, prices, configuration, seller info, VIN …|   ✅   |
|Save aggregated data to `full_results.json`                                   |   ✅   |
|Modular extractor system — easy to test & extend                              |   ✅   |

---

## 🛠 Installation

```bash
git clone https://github.com/KrutayaBabka/Mashina.kg-Car-Listing-Crawler.git
cd Mashina.kg-Car-Listing-Crawler

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
# source venv/bin/activate

pip install -r requirements.txt
````

---

## 🚀 Usage

```bash
python src/main.py
```

**Output**

* Parsed listings → `full_results.json`
* Logs      → `app.log`

---

## 📁 Project Structure

```
src/
│
├── main.py                    # Entry point
├── config.py                  # Global constants & logging
│
├── services/
│   └── crawl_service.py       # Orchestrates crawling & data saving
│
├── utils/
│   ├── __init__.py            # Re-exports key helpers
│   ├── fetch.py               # Synchronous HTML fetcher
│   ├── pagination.py          # Page-count & URL builder
│   ├── parse_listings.py      # Extracts links from listing cards
│   └── parse_details/         # Fine-grained extractors
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
    └── reference_data/        # Sample HTML pages & expected JSON output
                               # Handy for tests / debugging
```

---

## 🧪 Reference Data (Optional)

Directory `data/reference_data/` contains **paired** samples:

| File     | Purpose                                   |
| -------- | ----------------------------------------- |
| `*.html` | Raw HTML saved from real Mashina.kg pages |
| `*.json` | Expected structured output for that HTML  |

Use them to ⬇️

* Validate individual extractors without hitting the live site
* Write unit-tests / regression tests (fixtures)
* Debug new extraction logic quickly

---

## 🧩 Dependencies

Core libraries (see `requirements.txt` for exact versions):

* `requests`
* `tqdm`
* `beautifulsoup4`
* `urllib3` (dependency of requests)
* `certifi` (dependency of requests)

---

## ✅ Logging

| File      | Details                                          |
| --------- | ------------------------------------------------ |
| `app.log` | All crawl events, warnings, errors (append mode) |
| Format    | `[YYYY-MM-DD HH:MM:SS] LEVEL: message`           |
| Config    | Defined once in **`src/config.py`**              |

---

## 📄 License

Licensed for **educational and research** purposes.
Respect the terms of service of mashina.kg and scrape responsibly.

---

## 🙌 Contributing

*Found a bug?* *Have an idea?* — PRs and issues are welcome!
Please follow conventional commit messages and keep functions type-annotated.

---
