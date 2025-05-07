# To-Do List

## Key Features Implemented / Tasks Completed

- [x] Set up basic project structure (Frontend: SvelteKit, Backend: FastAPI)
- [x] Implement animated splash overlay (`SplashOverlay.svelte`).
- [x] Implement multi-phase component loading (`+layout.svelte`):
    - Phase 1: Header, Nav, About, URL Input/Info
    - Loading state with `LoadingDots.svelte`
    - Phase 2: Content Viewer, Random Text
- [x] Create core UI components (`Header`, `NavMenu`, `About`, `UrlInput`, `UrlInfo`, `ContentViewer`, `LoadingDots`).
- [x] Add placeholder components (`RandomTextBox`).
- [x] Implement basic CSS theming (`.module-light`, `.module-dark`) in global `app.css`.
- [x] Set up FastAPI backend (`backend/main.py`).
- [x] Basic LLM Integration (Backend):
    - Integrate OpenRouter LLM API.
    - Load context files from `backend/context`.
    - Analyze a specified article from `backend/articles` using context via `/analyze` endpoint.
- [x] Successfully scraped and parsed full NPR article using `newspaper3k` (2025-05-07).

## Next Steps / In Progress

- [ ] **URL Submission Logic:**
    - [ ] Connect `UrlInput` submission (Enter key) to backend `/analyze` endpoint (or a new URL scraping endpoint).
    - [ ] Pass the submitted URL from `+layout.svelte` (in `loadOtherComponents`) to the relevant component or function that will call the backend.
- [ ] **Display Analysis Results:**
    - [ ] Modify `ContentViewer.svelte` to display the neutral, deconstructed content received from the backend.
    - [ ] Handle potential errors from the backend API call.
- [ ] **Web Scraping Implementation:**
    - [ ] Add ability to scrape article content from a submitted URL (backend).
    - [ ] Create a new backend endpoint (e.g., `/scrape_and_analyze`) that takes a URL.
- [ ] **Frontend NPR Article Component:**
    - [ ] Create a new Svelte component to display the NPR article (https://www.npr.org/2025/05/06/nx-s1-5387465/trump-carney-canada-tariffs) using the scraped content.
    - [ ] Integrate this component into the main UI for demonstration/testing.
- [ ] **Refine UI/UX:**
    - [ ] Make `NavMenu.svelte` interactive (allow selecting different sources/views).
    - [ ] Replace `RandomTextBox.svelte` with actual content related to the selected Nav item or analysis.
    - [ ] Improve styling and transitions further.

## Future / Nice-to-Haves

- [ ] Database Setup (PostgreSQL?): Store sources, articles, analysis results.
- [ ] User Authentication / Preferences.
- [ ] Testing (Unit, Integration).
- [ ] Deployment configuration.

---

*(Below is the original, more granular list for reference)*

# To-Do List (Original Granular)

## Tomorrow
- [ ] web scraper
- [ ] Add hover effects to grid letters
- [ ] Consider adding color transitions for static letters

## Project Setup

- [ ] Set up Node.js environment
- [ ] Install required npm packages
- [ ] Configure development tools (ESLint, Prettier)
- [ ] Set up testing framework (Vitest/Jest)

## Project Structure

- [x] Create basic directory structure
- [x] Set up configuration files
- [x] Initialize Git repository
- [x] Create .gitignore file

## Database Setup

- [ ] Design database schema
- [ ] Set up PostgreSQL database
- [ ] Create tables for:
  - News sources
  - Articles
  - Depolarized content
  - User preferences

## News Source Management

- [ ] Create JSON configuration for news sources
- [ ] Categorize sources (left, center, right)
- [ ] Add source metadata (URLs, categories, reliability scores)
- [ ] Implement source validation system

## Web Scraping Implementation

- [ ] Set up web scraping infrastructure
- [ ] Implement rate limiting and quotas
- [ ] Create retry logic for failed requests
- [ ] Implement content validation and cleaning
- [ ] **[Planned] Add ability to scrape article content from a URL and analyze it**
    - [ ] **1. Update Dependencies:** Add `requests` and `beautifulsoup4` to backend `requirements.txt`.
    - [ ] **2. Install Dependencies:** Run `pip install -r backend/requirements.txt` (or equivalent).
    - [ ] **3. Create Scraping Module/Function:** Decide location (e.g., `backend/scraping.py`) and create `scrape_article_text(url: str)`.
    - [ ] **4. Implement Scraping Logic:**
        - [ ] Use `requests.get()` with a User-Agent.
        - [ ] Handle HTTP errors (`response.raise_for_status()`).
        - [ ] Parse HTML with `BeautifulSoup(response.content, 'html.parser')`.
        - [ ] Identify and select HTML elements containing article text (e.g., using `soup.select()`).
        - [ ] Extract and return text (`.get_text()`).
    - [ ] **5. Create Backend Endpoint:** Define a new FastAPI endpoint (e.g., `/scrape/`) in `backend/main.py` accepting a URL.
    - [ ] **6. Connect Endpoint to Logic:** Call `scrape_article_text` from the endpoint handler and return the result.
    - [ ] **7. Refine and Test:** Test with various URLs, refine selectors, add error handling.

## Depolarization Algorithm

- [ ] Research and implement sentiment analysis
- [ ] Create algorithm for identifying emotionally charged language
- [ ] Develop fact cross-referencing system
- [ ] Implement neutral summary generation

## LLM Integration (Backend)

- [x] Set up FastAPI backend
- [x] Integrate OpenRouter LLM API
- [x] Load context files from backend/context
- [x] Analyze a specified article from backend/articles using context
- [ ] [Future] Support analyzing articles scraped from URLs

## User Interface

- [x] Design and implement basic UI
- [x] Implement animated splash overlay with randomized grid reveal and Garamond font
- [x] Implement interactive splash overlay requiring click on static letters
- [ ] Create news category selection
- [ ] Implement results display
- [ ] Add source attribution display

## Testing and Quality Assurance

- [ ] Write unit tests
- [ ] Implement integration tests
- [ ] Set up continuous integration
- [ ] Create monitoring system

## Deployment

- [ ] Set up production environment
- [ ] Configure security measures
- [ ] Implement backup system
- [ ] Create deployment documentation
