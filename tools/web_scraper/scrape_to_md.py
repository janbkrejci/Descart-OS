#!/usr/bin/env python3
import os
import sys
import subprocess
import venv

# Directory for the virtual environment
VENV_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".venv")

def in_venv():
    return sys.prefix != sys.base_prefix

def setup_and_run():
    # Create venv if it doesn't exist
    if not os.path.exists(VENV_DIR):
        print(f"Creating virtual environment in {VENV_DIR}...", file=sys.stderr)
        venv.create(VENV_DIR, with_pip=True)
    
    # Path to python executable inside venv
    if os.name == 'nt':
        venv_python = os.path.join(VENV_DIR, "Scripts", "python.exe")
    else:
        venv_python = os.path.join(VENV_DIR, "bin", "python")
    
    # Install dependencies
    print("Ensuring dependencies are installed...", file=sys.stderr)
    subprocess.check_call(
        [venv_python, "-m", "pip", "install", "-q", "requests", "beautifulsoup4", "markdownify", "trafilatura", "certifi"],
        stdout=sys.stderr
    )
    
    # Re-run this script using the venv's python
    sys.exit(subprocess.call([venv_python] + sys.argv))

# If we are not in the venv, set it up and switch to it
if not in_venv():
    setup_and_run()

# From here on, we are safely inside the virtual environment
import ssl
import urllib3

# Disable SSL verification globally to bypass local issuer certificate issues (common on macOS)
try:
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except Exception:
    pass

import certifi
import os
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
os.environ['SSL_CERT_FILE'] = certifi.where()

import requests
from bs4 import BeautifulSoup
import trafilatura
from markdownify import markdownify as md

def scrape_url(url):
    try:
        # Fetch the content using requests to easily bypass SSL issues if needed
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=15, verify=False)
        response.raise_for_status()
        html_content = response.content

        # Try Trafilatura first, as it's excellent for extracting main article content
        result = trafilatura.extract(html_content, output_format="markdown")
        
        # If trafilatura returns something substantial, use it. 
        # For homepages, trafilatura often fails or returns very little text, so we fallback if length is small.
        if result and len(result) > 500:
            return result

        # Fallback to beautifulsoup + markdownify for homepages and pages where trafilatura misses content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove script, style, header, footer, and nav elements to clean up the text
        for element in soup(["script", "style", "noscript", "header", "footer", "nav", "aside"]):
            element.extract()
            
        markdown_text = md(str(soup), heading_style="ATX", escape_asterisks=False)
        return markdown_text.strip()
        
    except Exception as e:
        print(f"Error scraping {url}: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scrape_to_md.py <url>", file=sys.stderr)
        sys.exit(1)
        
    url = sys.argv[1]
    markdown_content = scrape_url(url)
    
    if markdown_content:
        print(markdown_content)
    else:
        print(f"Failed to extract readable content from {url}.", file=sys.stderr)
        sys.exit(1)
