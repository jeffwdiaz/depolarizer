import os
from fastapi import FastAPI, HTTPException, Query, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import glob
import httpx
from dotenv import load_dotenv
from .news_api import fetch_news
from fastapi.responses import PlainTextResponse, JSONResponse
import json
from .HighlightLang import highlight_article
import subprocess

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Allow CORS for local development (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CONTEXT_DIR = os.path.join(os.path.dirname(__file__), "context")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = "openai/gpt-3.5-turbo"  # You can change this to another model if desired
POLITICAL_ARTICLES_DIR = os.path.join(os.path.dirname(__file__), "political_articles")

class AnalyzeRequest(BaseModel):
    article_filename: str
    text: str

class AnalyzeResponse(BaseModel):
    result: str


def load_articles() -> List[str]:
    article_files = glob.glob(os.path.join(CONTEXT_DIR, "*.md"))
    articles = []
    for file_path in article_files:
        with open(file_path, "r", encoding="utf-8") as f:
            articles.append(f.read())
    return articles

def load_article(filename: str) -> Optional[str]:
    file_path = os.path.join(POLITICAL_ARTICLES_DIR, filename)
    if not os.path.isfile(file_path):
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

async def call_openrouter(prompt: str) -> str:
    if not OPENROUTER_API_KEY:
        raise HTTPException(status_code=500, detail="OpenRouter API key not set.")
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that uses the following articles as context."},
            {"role": "user", "content": prompt}
        ]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(OPENROUTER_API_URL, headers=headers, json=data)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"OpenRouter API error: {response.text}")
        result = response.json()
        # Extract the LLM's reply
        return result["choices"][0]["message"]["content"]

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    article = load_article(request.article_filename)
    if article is None:
        raise HTTPException(status_code=400, detail="Article not found or cannot be read.")
    context_articles = load_articles()
    formatted_context = "\n\n".join([
        f"Context Article {i+1}:\n{a.strip()}" for i, a in enumerate(context_articles)
    ])
    prompt = (
        "You are an expert analyst. Using the following context articles and the main article, answer the user's question or perform the requested analysis as clearly and concisely as possible.\n"
        "=== CONTEXT ARTICLES START ===\n"
        f"{formatted_context}\n"
        "=== CONTEXT ARTICLES END ===\n\n"
        "=== MAIN ARTICLE START ===\n"
        f"{article.strip()}\n"
        "=== MAIN ARTICLE END ===\n\n"
        "User request:\n"
        f"{request.text}"
    )
    try:
        llm_response = await call_openrouter(prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing your request.")
    return AnalyzeResponse(result=llm_response)

@app.get("/news")
async def get_news(
    query: str = Query(..., description="Search query for articles"),
    sources: Optional[str] = Query(None, description="Comma-separated string of news sources (e.g., bbc-news,cnn)"),
    domains: Optional[str] = Query(None, description="Comma-separated string of domains (e.g., bbc.co.uk,techcrunch.com)"),
    language: Optional[str] = Query("en", description="Language of the articles (e.g., en, de, fr)"),
    sortBy: Optional[str] = Query("publishedAt", description="Sort order (relevancy, popularity, publishedAt)")
):
    valid_sort_by = ["relevancy", "popularity", "publishedAt"]
    if sortBy not in valid_sort_by:
        raise HTTPException(status_code=400, detail=f"Invalid sortBy parameter. Allowed values are: {', '.join(valid_sort_by)}")

    news_data = await fetch_news(
        query=query,
        sources=sources,
        domains=domains,
        language=language,
        sortBy=sortBy
    )
    if "error" in news_data:
        if "NEWS_API_KEY not found" in news_data["error"]:
             raise HTTPException(status_code=500, detail="News API key not configured on the server.")
        raise HTTPException(status_code=502, detail=f"Error fetching news from provider: {news_data['error']}")
    return news_data

@app.get("/article", response_class=PlainTextResponse)
async def get_article(filename: str):
    content = load_article(filename)
    if content is None:
        raise HTTPException(status_code=404, detail="Article not found.")
    return content

@app.get("/article_json", response_class=JSONResponse)
async def get_article_json(filename: str):
    file_path = os.path.join(POLITICAL_ARTICLES_DIR, filename)
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="Article not found.")
    with open(file_path, 'r', encoding='utf-8') as f:
        return JSONResponse(content=json.load(f))

@app.get("/list_articles")
async def list_articles():
    files = [f for f in os.listdir(POLITICAL_ARTICLES_DIR) if f.endswith('.json')]
    return {"files": files}

@app.get("/highlight_article", response_class=JSONResponse)
async def highlight_article_endpoint(filename: str):
    """
    Returns the article JSON with an additional 'highlighted_text' field,
    where polarizing language is highlighted by the LLM.
    """
    file_path = os.path.join(POLITICAL_ARTICLES_DIR, filename)
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="Article not found.")
    try:
        result = await highlight_article(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Highlighting failed: {e}")
    return JSONResponse(content=result)

@app.post("/scrape_politics")
async def scrape_politics(background_tasks: BackgroundTasks):
    """
    Triggers scraping of 5 politics articles by running scrape_article.py as a subprocess.
    Returns immediately with a success message; scraping runs in the background.
    """
    def run_scraper():
        try:
            result = subprocess.run([
                "python", os.path.join(os.path.dirname(__file__), "scrape_article.py")
            ], capture_output=True, text=True)
            print("Scraper output:", result.stdout)
            if result.stderr:
                print("Scraper error output:", result.stderr)
        except Exception as e:
            print(f"Error running scraper: {e}")
    background_tasks.add_task(run_scraper)
    return {"success": True, "message": "Scraping started in background."} 