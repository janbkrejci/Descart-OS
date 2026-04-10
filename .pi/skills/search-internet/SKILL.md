---
name: search-internet
description: Skill to search the internet for information to answer user's questions or fulfill their requests.
---

# Search Internet Skill

This skill allows me to proactively search the internet whenever the user asks for current information, facts I am not sure about, or explicitly asks me to search the web.

## Usage

When I identify that I need to search the internet:

1. I will formulate a concise and effective search query.
2. I will decide whether the search should be a **broad match** or an **exact match**. 
   * For broad concepts, I will use regular keywords. 
   * For specific names, error messages, or exact phrases (e.g. `Jan B. Krejčí`), I will enclose the query in double quotes to force an exact match in DuckDuckGo.
3. I will decide on the number of results I need (usually between 3 and 10).
4. I will invoke the `./ddg_search.py` executable script via the `bash` tool by running the command:
   ```bash
   # For broad match:
   ./ddg_search.py <num_results> "<query>"
   
   # For exact match (note the nested double quotes inside single quotes):
   ./ddg_search.py <num_results> '"<exact_query>"'
   ```
5. I will wait for the output, which will be formatted as a markdown table containing the columns `Number`, `Result`, and `Description`.
6. I will present the markdown table to the user or use the information in the `Description` column to construct a comprehensive answer, always citing the links.
