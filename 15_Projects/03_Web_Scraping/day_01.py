"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# You will be getting 403 Forbidden because many large sites (including Wikipedia, LinkedIn, Amazon, etc.) block requests that look like automated scraping if you just use requests.get() without headers.

# 👉 For Wikipedia specifically:

# The URL you tried is correct:
# https://en.wikipedia.org/wiki/Python_(programming_language)
# But you need to add a User-Agent header so it looks like a normal browser request.

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

def get_h2_headers(url):
    try:
        global headers
        response = requests.get(url, headers=headers, timeout=10)
        # print(response.status_code)
        # print(response.text[:500]) # print first 500 chars
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    print(h2_tags)
    headers = []
    for tag in h2_tags:
        header_text = tag.get_text(strip=True)
        if header_text and header_text.lower() != "contents":
            headers.append(header_text)
    print(headers)

get_h2_headers(URL)