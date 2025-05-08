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

# List of 5 URLs to scrape
ARTICLE_URLS = [
    "https://www.npr.org/2025/05/08/nx-s1-5382445/direct-democracy-ballot-measure-laws",
    "https://www.npr.org/2025/05/08/nx-s1-5383918/economists-trump-research-science-cuts-gdp-recession",
    "https://www.npr.org/2025/05/08/nx-s1-5391840/trump-ed-martin-withdraws-nomination-prosecutor",
    "https://www.npr.org/2025/05/07/nx-s1-5389973/trump-trade-deal-uk-tariffs",
    "https://www.npr.org/2025/05/06/nx-s1-5387465/trump-carney-canada-tariffs"
]

# Utility to sanitize filenames (no longer used, but kept for reference)
def sanitize_filename(s):
    s = re.sub(r'[^\w\-]+', '_', s)
    return s[:80]

def scrape_and_save(article_url: str, filename: str):
    """
    Scrapes a news article from the given URL using newspaper3k and saves as JSON.
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
            "text": article.text,
            "url": article_url
        }
        print(f"--- Title ---\n{data['title']}")
        print(f"--- Authors ---\n{data['authors']}")
        print(f"--- Publish Date ---\n{data['publish_date']}")
        print(f"--- Article Text (first 500 chars) ---\n{data['text'][:500]}...")
        print(f"\n--- Full Article Text Length ---\n{len(data['text'])} characters")

        if not data['text'].strip():
            print("\nWARNING: Scraped article text is empty or whitespace only.")

        # Save as JSON
        if not os.path.exists(POLITICAL_ARTICLES_DIR):
            os.makedirs(POLITICAL_ARTICLES_DIR)
        filepath = os.path.join(POLITICAL_ARTICLES_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved article JSON to: {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Only scrape the first URL for debugging
    url = ARTICLE_URLS[0]
    filename = "pol1.json"
    scrape_and_save(url, filename) 