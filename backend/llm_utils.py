import os
import httpx
from fastapi import HTTPException
from dotenv import load_dotenv
import glob

# Load environment variables from .env file
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = "openai/gpt-3.5-turbo"  # You can change this to another model if desired

# Utility to load all .md context files from backend/context/
CONTEXT_DIR = os.path.join(os.path.dirname(__file__), "context")
def load_all_context() -> str:
    context_files = sorted(glob.glob(os.path.join(CONTEXT_DIR, "*.md")))
    contexts = []
    for path in context_files:
        try:
            with open(path, "r", encoding="utf-8") as f:
                contexts.append(f"--- {os.path.basename(path)} ---\n" + f.read())
        except Exception:
            continue
    return "\n\n".join(contexts)

def list_context_filenames() -> str:
    context_files = sorted(glob.glob(os.path.join(CONTEXT_DIR, "*.md")))
    return ', '.join(os.path.basename(f) for f in context_files)

async def call_openrouter(prompt: str) -> str:
    """
    Calls the OpenRouter LLM API with the given prompt and returns the response content.
    Raises HTTPException on error.
    """
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
        return result["choices"][0]["message"]["content"]

async def highlight_polarizing_language(text: str) -> str:
    """
    Calls the LLM to highlight polarizing or emotionally charged language in the article text.
    References all .md files in backend/context/ as @context (by filename) for background knowledge. Returns the article text with highlights and paragraph breaks.
    """
    context_filenames = list_context_filenames()
    prompt = (
        "You are an expert in media analysis. Carefully read the following news article. "
        f"You have access to the following context files for background knowledge: {context_filenames}. "
        "Refer to these as @context in your analysis. "
        "Highlight all words, phrases, or sentences in the article that are polarizing, emotionally charged, or likely to provoke strong reactions, "
        "by wrapping them in <span class='polarizing-language'>...</span>. "
        "Preserve the original text and structure, but format the output so that each paragraph is wrapped in <p>...</p> tags. "
        "Do not add any commentary or explanation—return only the full article text with highlights and paragraph breaks.\n\n"
        "Refer to @context for definitions and examples of polarizing language.\n\n"
        "=== ARTICLE START ===\n"
        f"{text}\n"
        "=== ARTICLE END ==="
    )
    return await call_openrouter(prompt) 