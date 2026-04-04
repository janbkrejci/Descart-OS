---
name: search_internet
description: Skill to search the internet for information to answer user's questions or fulfill their requests.
---

# Search Internet Skill

This skill allows me to proactively search the internet whenever the user asks for current information, facts I am not sure about, or explicitly asks me to search the web.

## Usage

When I identify that I need to search the internet:

1. I will formulate a concise and effective search query.
2. I will decide on the number of results I need (usually between 3 and 10).
3. I will invoke the `search_internet` tool via the `bash` tool by running the script:
   ```bash
   python3 tools/search_internet/ddg_search.py <num_results> "<query>"
   ```
4. I will wait for the output, which will be formatted as a markdown table containing the columns `Number`, `Result`, and `Description`.
5. I will present the markdown table to the user or use the information in the `Description` column to construct a comprehensive answer, always citing the links.
