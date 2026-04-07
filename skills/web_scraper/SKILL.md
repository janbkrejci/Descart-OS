---
name: web_scraper
description: Skill for autonomously visiting webpages via URL to extract information, read articles, or pull content in markdown format.
---

# Web Scraper Skill

This skill allows me to dive deeper into the web. When standard search results (from `search_internet`) do not provide enough context, or when the user explicitly provides a URL for me to read, I use this skill to fetch the page's actual content.

## Usage

When I identify that I need to read the contents of a specific URL:

1. I will invoke the `web_scraper` tool via the `bash` tool by running the script:
   ```bash
   python3 tools/web_scraper/scrape_to_md.py "<url>"
   ```
2. The script handles all missing dependencies on its own through a local virtual environment, so I don't need to install anything manually beforehand.
3. I will wait for the output, which will be the webpage's main text converted to clean markdown format.
4. I will process the markdown text to answer the user's question, summarize the article, or extract the requested information.
5. If the extracted markdown is very long, it will be automatically truncated or saved by my bash tool wrapper. In such cases, I'll work with the saved file as needed.
