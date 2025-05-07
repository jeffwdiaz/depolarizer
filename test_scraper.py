from newspaper import Article
from newspaper import Config

# Set up a custom user-agent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

article_url = "https://www.npr.org/2025/05/06/nx-s1-5387465/trump-carney-canada-tariffs"

try:
    print(f"Attempting to scrape: {article_url}")
    article = Article(article_url, config=config)
    article.download()
    article.parse()
    print(f"--- Title ---\n{article.title}")
    print(f"--- Authors ---\n{article.authors}")
    print(f"--- Publish Date ---\n{article.publish_date}")
    print(f"--- Top Image ---\n{article.top_image}")
    print(f"--- Article Text (first 500 chars) ---\n{article.text[:500]}...")
    print(f"\n--- Full Article Text Length ---\n{len(article.text)} characters")

    if not article.text.strip():
        print("\nWARNING: Scraped article text is empty or whitespace only.")

except Exception as e:
    print(f"An error occurred: {e}")