# backend/news_api.py
# This file will contain functions to interact with the News API.

import os
import httpx
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_BASE_URL = "https://newsapi.org/v2/everything"  # Example: get everything, adjust as needed

async def fetch_news(query: str, sources: str | None = None, domains: str | None = None, language: str = "en", sortBy: str = "publishedAt"):
    """
    Fetches news articles from the News API based on a query and other optional parameters.

    Args:
        query (str): The search query for articles.
        sources (str, optional): A comma-seperated string of identifiers for the news sources or blogs you want headlines from.
        domains (str, optional): A comma-seperated string of domains (e.g. bbc.co.uk, techcrunch.com) to restrict the search to.
        language (str, optional): The language of the articles. Defaults to "en".
        sortBy (str, optional): The order to sort the articles in. Defaults to "publishedAt". 
                                Possible values: "relevancy", "popularity", "publishedAt".

    Returns:
        dict: The JSON response from News API or an error message.
    """
    if not NEWS_API_KEY:
        return {"error": "NEWS_API_KEY not found in environment variables."}

    params = {
        "q": query,
        "apiKey": NEWS_API_KEY,
        "language": language,
        "sortBy": sortBy,
    }
    if sources:
        params["sources"] = sources
    if domains:
        params["domains"] = domains
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(NEWS_API_BASE_URL, params=params)
            response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
            return response.json()
        except httpx.HTTPStatusError as exc:
            return {"error": f"HTTP error occurred: {exc.response.status_code} - {exc.response.text}"}
        except httpx.RequestError as exc:
            return {"error": f"An error occurred while requesting {exc.request.url!r}: {exc}"}

# Example usage (optional, for testing directly)
# if __name__ == "__main__":
#     import asyncio
#     async def main_test():
#         # Ensure you have NEWS_API_KEY in your .env file at the project root
#         # or set it as an environment variable directly.
#         news = await fetch_news(query="technology")
#         if "error" in news:
#             print(f"Error fetching news: {news['error']}")
#         else:
#             print(f"Fetched {len(news.get('articles', []))} articles.")
#             for article in news.get('articles', [])[:2]: # Print first 2 articles
#                 print(f"  Title: {article['title']}")
#                 print(f"  Source: {article['source']['name']}")
#                 print(f"  URL: {article['url']}")
#                 print("-" * 20)
#
#     asyncio.run(main_test()) 