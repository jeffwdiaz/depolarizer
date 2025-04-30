import os
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import glob
import httpx
from dotenv import load_dotenv

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
ARTICLES_DIR = os.path.join(os.path.dirname(__file__), "articles")

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
    file_path = os.path.join(ARTICLES_DIR, filename)
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