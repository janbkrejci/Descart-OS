#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.10"
# dependencies = ["urllib3"]
# ///

import urllib.request
import urllib.parse
import re
import sys
import html

def search_ddg(query, num_results):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html_content = response.read().decode('utf-8')
            
        results = []
        pattern = re.compile(
            r'<a class="result__url" href="([^"]+)">(.*?)</a>.*?'
            r'<a class="result__snippet[^>]*>(.*?)</a>',
            re.IGNORECASE | re.DOTALL
        )
        
        matches = pattern.findall(html_content)
        for match in matches:
            link = html.unescape(match[0])
            if 'uddg=' in link:
                uddg_match = re.search(r'uddg=([^&]+)', link)
                if uddg_match:
                    link = urllib.parse.unquote(uddg_match.group(1))
            
            title = html.unescape(re.sub(r'<[^>]+>', '', match[1]).strip())
            snippet = html.unescape(re.sub(r'<[^>]+>', '', match[2]).strip())
            
            results.append({
                'title': title,
                'link': link,
                'snippet': snippet
            })
            if len(results) >= num_results:
                break
                
        return results
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 ddg_search.py <num_results> <query>")
        sys.exit(1)
        
    try:
        num_results = int(sys.argv[1])
    except ValueError:
        print("Error: num_results must be an integer.")
        sys.exit(1)
        
    query = " ".join(sys.argv[2:])
    
    results = search_ddg(query, num_results)
    
    if not results:
        print("No results found.")
    else:
        print("| Number | Result | Description |")
        print("|---|---|---|")
        for i, res in enumerate(results, 1):
            title = res['title'].replace('|', '\\|').replace('\n', ' ')
            link = res['link'].replace('|', '\\|')
            snippet = res['snippet'].replace('|', '\\|').replace('\n', ' ')
            print(f"| {i} | [{title}]({link}) | {snippet} |")
