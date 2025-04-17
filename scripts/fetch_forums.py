import requests
from bs4 import BeautifulSoup
import os
import json
import time

BASE_URL = "https://www.psychforums.com"
BOARD_PATHS = {
    "depression": "/depression/",
    "anxiety": "/anxiety/",
    "ptsd": "/post-traumatic-stress/",
    "ocd": "/obsessive-compulsive/"
}
HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_page(url):
    response = requests.get(url, headers=HEADERS)
    return BeautifulSoup(response.text, "html.parser")

def get_thread_links(board_url, pages=2):
    thread_links = []
    for page_num in range(pages):
        url = f"{board_url}?start={page_num * 50}"
        print(f"📄 Fetching board page: {url}")
        soup = fetch_page(url)
        links = soup.select("a.topictitle")
        for a in links:
            thread_url = a['href']
            # Ensure the thread URL is absolute
            if thread_url.startswith("http"):
                thread_links.append(thread_url)  # If the link is absolute, use it directly
            else:
                thread_links.append(BASE_URL + thread_url)  # If it's relative, append to BASE_URL
        time.sleep(1)
    return thread_links


def scrape_thread(url):
    soup = fetch_page(url)
    try:
        title = soup.select_one("h2.topic-title").text.strip()
    except:
        title = "No Title"
    
    posts = []
    post_divs = soup.select("div.postbody div.content")
    for post in post_divs:
        text = post.get_text(separator=" ", strip=True)
        posts.append(text)

    return {
        "thread_url": url,
        "title": title,
        "posts": posts
    }

def scrape_multiple_boards(board_paths, pages=2):
    all_data = []
    for category, path in board_paths.items():
        print(f"\n📘 Scraping category: {category.upper()}")
        board_url = BASE_URL + path
        thread_urls = get_thread_links(board_url, pages)

        for url in thread_urls:
            print(f"🔍 {category.upper()} thread: {url}")
            thread_data = scrape_thread(url)
            thread_data["category"] = category
            all_data.append(thread_data)
            time.sleep(1)
    return all_data

# --- Run the Scraper ---
data = scrape_multiple_boards(BOARD_PATHS, pages=3)

# Save to your project path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
output_dir = os.path.join(project_root, "raw_data", "forums")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "psychforums_data.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Scraped {len(data)} threads from PsychForums. Saved to {output_path}")
