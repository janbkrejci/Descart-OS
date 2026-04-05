---
name: search_internet
description: Tool for performing web searches via DuckDuckGo and returning results as a markdown table.
---

# Search Internet

This tool allows me to search the internet using DuckDuckGo. It invokes a built-in python script that parses DuckDuckGo HTML results and formats them into a markdown table.

## Procedure I must follow

1. Ascertain the search `query` and the desired number of results `num_results` (default is usually 5, but can be specified).
   * Note: If an exact match is required (e.g., a specific person's name like "Jan B. Krejčí" or a specific phrase), the query itself must contain double quotes to tell DuckDuckGo to search for the exact string. Otherwise, use a standard broad match query.
2. Execute the python script provided in this tool directory via the `bash` tool:
   ```bash
   # For broad match:
   tools/search_internet/ddg_search.py <num_results> "<query>"
   
   # For exact match (note the nested double quotes inside single quotes):
   tools/search_internet/ddg_search.py <num_results> '"<exact_query>"'
   ```
3. Read the output from the script which will be a standard markdown table with columns `Number`, `Result`, and `Description`.
4. Provide the table directly to the user or use it to compile an answer.
