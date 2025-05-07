# backend/fetch_latest_article.py
# This script fetches the latest 'politics' article from NewsAPI
# and saves it as a Markdown file in the backend/articles/ directory.

import os
import asyncio
import datetime
import re

# Attempt to import fetch_news from news_api.py, assuming it's in the same directory
# and this script is run in an environment where 'backend' is a discoverable package
# or the PYTHONPATH is set up accordingly (e.g., run from project root).
try:
    from .news_api import fetch_news
except ImportError:
    print("Error: Could not import 'fetch_news' from '.news_api'.")
    print("Ensure '.news_api.py' is in the same directory or backend module is accessible.")
    print("You might need to run this script from the project root, e.g., using:")
    print("python -m backend.fetch_latest_article")
    exit(1)

ARTICLES_DIR = os.path.join(os.path.dirname(__file__), "articles")

def sanitize_filename(name):
    """Sanitizes a string to be used as a filename."""
    # Remove invalid characters
    name = re.sub(r'[^a-zA-Z0-9_\s-]', '', name)
    # Replace spaces with underscores
    name = name.replace(' ', '_')
    # Truncate to a reasonable length
    return name[:100]

def save_article_to_md(article_data, filename):
    """Saves article data to a Markdown file in the ARTICLES_DIR."""
    if not os.path.exists(ARTICLES_DIR):
        try:
            os.makedirs(ARTICLES_DIR)
            print(f"Created directory: {ARTICLES_DIR}")
        except OSError as e:
            print(f"Error creating directory {ARTICLES_DIR}: {e}")
            return
    
    filepath = os.path.join(ARTICLES_DIR, filename)

    title = article_data.get('title', 'No Title Provided')
    source_name = article_data.get('source', {}).get('name', 'No Source Provided')
    url = article_data.get('url', '#')
    published_at = article_data.get('publishedAt', '')
    description = article_data.get('description', '')
    content = article_data.get('content', '')
    
    # Use content if available and not just a short stub, otherwise use description.
    # NewsAPI 'content' often ends with "[+XYZ chars]".
    article_body = description # Default to description
    if content:
        # Check if content is significantly longer or more complete than description
        # A simple check: if content is longer and doesn't seem to be just a prefix of description
        if len(content) > len(description) or not description.startswith(content.split('[+')[0].strip()):
            article_body = content

    # Clean up the common NewsAPI content truncation
    if article_body and "[+" in article_body and article_body.endswith("chars]"):
        article_body = article_body.split("[+")[0].strip() + "..."
    
    if not article_body: # Fallback if both description and content are empty
        article_body = "No content available for this article."

    md_content = f"# {title}\n\n"
    md_content += f"**Source:** {source_name}\n"
    if published_at:
        try:
            # Format date nicely if possible
            parsed_date = datetime.datetime.fromisoformat(published_at.replace('Z', '+00:00'))
            md_content += f"**Published:** {parsed_date.strftime('%Y-%m-%d %H:%M:%S %Z')}\n"
        except ValueError:
            md_content += f"**Published:** {published_at}\n" # Fallback to raw string
    md_content += f"**URL:** [{url}]({url})\n\n"
    md_content += "---\n\n"
    md_content += f"{article_body}\n"

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"Successfully saved article to: {filepath}")
    except IOError as e:
        print(f"Error: Could not write article to file {filepath}. Reason: {e}")

async def main_fetch_and_save():
    """Fetches the latest politics article and saves it."""
    print("Fetching the latest 'politics' article from NewsAPI...")
    
    # fetch_news sorts by publishedAt by default if sortBy is not overridden for relevance/popularity
    news_data = await fetch_news(query="politics", sortBy="publishedAt")

    if not news_data:
        print("Error: No data received from fetch_news. This could be an issue with the function itself.")
        return

    if "error" in news_data:
        print(f"API Error: {news_data['error']}")
        if "NEWS_API_KEY not found" in news_data['error']:
            print("Please ensure your NEWS_API_KEY is correctly set in the .env file in the project root.")
        return

    articles = news_data.get('articles', [])
    if not articles:
        print("No articles found for the query 'politics'.")
        return

    latest_article = articles[0] # First article is the latest due to sortBy="publishedAt"
    
    article_title = latest_article.get('title', 'Untitled_Article')
    sanitized_title = sanitize_filename(article_title)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_slug = f"politics_{sanitized_title}"
    filename = f"{filename_slug}_{timestamp}.md"
    
    print(f"Processing article: '{article_title}'")
    save_article_to_md(latest_article, filename)

if __name__ == "__main__":
    # To run this script successfully:
    # 1. Ensure you are in the project root directory (006_deconstructed).
    # 2. Run as a module: python -m backend.fetch_latest_article
    # This ensures that 'from news_api import fetch_news' works correctly
    # and that 'load_dotenv()' in news_api.py can find the .env file in the project root.
    asyncio.run(main_fetch_and_save()) 