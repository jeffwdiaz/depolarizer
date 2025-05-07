import sys
import os
import json
from newspaper import Article
from newspaper import Config
from datetime import datetime
import re

# Set up a custom user-agent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

POLITICAL_ARTICLES_DIR = os.path.join(os.path.dirname(__file__), "political_articles")

# Utility to sanitize filenames
def sanitize_filename(s):
    s = re.sub(r'[^\w\-]+', '_', s)
    return s[:80]

def scrape_article(article_url: str):
    """
    Scrapes a news article from the given URL using newspaper3k and prints key information.
    Also saves the article as a JSON file in the articles directory.
    """
    try:
        print(f"Scraping: {article_url}")
        article = Article(article_url, config=config)
        article.download()
        article.parse()
        data = {
            "title": article.title,
            "authors": article.authors,
            "publish_date": article.publish_date.isoformat() if article.publish_date else None,
            "top_image": article.top_image,
            "text": article.text,
            "url": article_url
        }
        print(f"--- Title ---\n{data['title']}")
        print(f"--- Authors ---\n{data['authors']}")
        print(f"--- Publish Date ---\n{data['publish_date']}")
        print(f"--- Top Image ---\n{data['top_image']}")
        print(f"--- Article Text (first 500 chars) ---\n{data['text'][:500]}...")
        print(f"\n--- Full Article Text Length ---\n{len(data['text'])} characters")

        if not data['text'].strip():
            print("\nWARNING: Scraped article text is empty or whitespace only.")

        # Save as JSON
        if not os.path.exists(POLITICAL_ARTICLES_DIR):
            os.makedirs(POLITICAL_ARTICLES_DIR)
        # Use title or fallback to date for filename
        base = sanitize_filename(data['title'] or 'article')
        if not base:
            base = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{base}.json"
        filepath = os.path.join(POLITICAL_ARTICLES_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved article JSON to: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scrape_article.py <article_url>")
        sys.exit(1)
    url = sys.argv[1]
    scrape_article(url) 