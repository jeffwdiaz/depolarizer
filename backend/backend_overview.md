# Backend Overview

The backend is built using **Python** with the **FastAPI** framework and integrates with the OpenRouter LLM API.

## Current Implementation
- **Articles to analyze** are placed in `backend/articles/` as Markdown files.
- **Context files** are placed in `backend/context/` as Markdown files.
- The `/analyze` endpoint accepts:
  - `article_filename`: the name of the article in `backend/articles` to analyze.
  - `text`: the user's question or instruction.
- The backend loads all context files, builds a structured prompt (with clear separation between context and main article), and sends it to the LLM for analysis.
- If the article file is not found, a generic error is returned.

## Planned/Future Work
- Add the ability to scrape article content from a URL and analyze it using the same context mechanism.

