---
name: web_scraper
description: Tool for scraping a web page from a given URL and converting its readable content into markdown.
---

# Web Scraper Tool

This tool allows me to visit a webpage via its URL and extract the main content converted into human-readable markdown.

## Dependencies and Setup

The included Python script (`scrape_to_md.py`) is completely self-contained. It strictly follows the dependency management rule:
- It automatically creates an isolated Python Virtual Environment (`.venv`) inside its directory.
- It installs all required external libraries (`trafilatura`, `requests`, `beautifulsoup4`, `markdownify`) on the fly.
- It guarantees that the global Python environment remains clean.

## Procedure I must follow

1. Ascertain the `url` to be scraped.
2. Execute the python script via the `bash` tool:
   ```bash
   python3 tools/web_scraper/scrape_to_md.py "<url>"
   ```
3. Read the standard output (stdout), which will contain the markdown representation of the webpage's main content.
4. If there are any setup messages or errors, they will be printed to standard error (stderr), keeping the markdown output clean.
