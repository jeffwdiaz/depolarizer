# Depolarizer

## Project Structure

```
depolarizer/
  backend/      # FastAPI backend (Python, LLM integration)
    main.py
    requirements.txt
    articles/   # Articles to analyze (Markdown files)
    context/    # Context files (Markdown files)
    ...
  frontend/     # SvelteKit frontend
    src/
    static/
    package.json
    ...
  README.md
  ...
```

## Getting Started

### Frontend

1. Install dependencies:
   ```sh
   cd frontend
   npm install
   ```
2. Run the development server:
   ```sh
   npm run dev
   ```

### Backend

1. Install dependencies:
   ```sh
   cd backend
   pip install -r requirements.txt
   ```
2. Start the backend server:
   ```sh
   uvicorn main:app --reload
   ```

The backend will run on port 8000 by default. The frontend will run on its configured port (usually 5173).

---

## Backend LLM Integration

- The backend is built with **FastAPI** (Python) and integrates with the **OpenRouter LLM API**.
- **Articles to analyze** are placed in `backend/articles/` as Markdown files.
- **Context files** are placed in `backend/context/` as Markdown files.
- The `/analyze` endpoint accepts:
  - `article_filename`: the name of the article in `backend/articles` to analyze.
  - `text`: the user's question or instruction.
- The backend loads all context files, builds a structured prompt (with clear separation between context and main article), and sends it to the LLM for analysis.
- If the article file is not found, a generic error is returned.
- **Planned:** Add support for scraping article content from a URL for analysis using the same context mechanism.

---

## Notes
- Adjust ports and proxy settings as needed for integration.
- Add your backend API routes in `backend/main.py` or split into separate files as your backend grows.
- For shared code, create a `shared/` directory at the root.

## Problem Statement

Our society is facing a growing crisis of division and distrust, fueled in part by the emotionally charged content that dominates our news landscape. Millennials and older Americans, who are active participants in our democracy, are constantly bombarded with news that evokes anger, fear, hatred, and outrage. This constant barrage of negativity makes it difficult for them to form balanced, well-informed opinions and engage in constructive dialogue. The potential impact of addressing this problem is huge. By providing access to neutral, emotion-free news, we can promote a more informed and rational public discourse, foster greater understanding and empathy between different groups, and ultimately strengthen our democracy.

## Tech Stack

### Frontend Components

- **Framework**: SvelteKit (with Svelte 5 Runes)
- **Language**: TypeScript
- **Styling**: CSS with CSS Variables (component-scoped and global)
- **Fonts**: Google Fonts (EB Garamond)
- **Animations**: Svelte built-in transitions

### Backend Components

- **Framework**: FastAPI (Python)
- **LLM Integration**: OpenRouter API
- **HTTP Client**: httpx
- **Environment Management**: python-dotenv

### Development Environment

- **Version Control**: Git
- **IDE**: VS Code with Cursor
- **Package Manager**: npm (frontend), pip (backend)

### Core Features

- Responsive grid layout
- Component-based architecture (using barrel file for imports)
- Centralized animation system (`animations.ts`)
- Type-safe development
- Modern CSS practices (global theme, scoped component styles)
- LLM-powered article analysis (Backend)
- Interactive splash screen

### Directory Structure

```text
src/
├── components/       # Reusable components
├── routes/           # Page routes
└── styles/           # Global styles and theme
```

## Project Outline

A tool that scrapes and deconstructs news content from multiple sources. Users can select news categories like Political, Financial, or World news. Initially supporting Political news only. The system scrapes predetermined sites for popular stories, processes them through the deconstructed, and presents neutral, fact-based content.

### System Features

- Multi-source news aggregation
- Political bias detection
- Emotional language filtering
- Fact-based content generation
- Source diversity (left/center/right)

## Implementation Steps

### 1. User Selection and Processing

1. Category Selection
   - Select news category
   - Validate selection
   - Initialize session

2. Source Management
   - Load source configuration
   - Check source health
   - Manage source rotation
   - Set rate limits

3. Content Gathering
   - Scan websites
   - Handle request failures
   - Clean content
   - Store articles

4. Article Analysis
   - Group similar stories
   - Calculate popularity
   - Check source diversity
   - Select top stories

5. Content Processing
   - Find related content
   - Verify relevance
   - Group by perspective
   - Extract key facts

6. Depolarization
   - Analyze sentiment
   - Filter charged language
   - Verify facts
   - Generate summary
   - Add attribution

7. Quality Assurance
   - Validate content
   - Check facts
   - Ensure balance
   - Verify clarity

8. Content Delivery
   - Format content
   - Add metadata
   - Generate output
   - Update UI

9. System Monitoring
   - Track metrics
   - Monitor sources
   - Collect feedback
   - Update scores

10. Error Management
    - Log errors
    - Recover gracefully
    - Use cache
    - Alert admins

## Development Status

### Frontend Implementation

#### Initial Setup
- [x] Initialize project
- [x] Set up TypeScript
- [x] Configure dev environment
- [x] Set up version control

#### Project Organization
- [x] Create directory structure
- [x] Configure project
- [x] Set up Git
- [x] Add gitignore

#### Component Development
- [x] Build header
- [x] Create navigation
- [x] Add content viewer
- [x] Create URL input
- [x] Add placeholders

#### Visual Design
- [x] Implement grid layout
- [x] Set up CSS system
- [x] Add fonts
- [x] Create animations

#### User Interface
- [x] Add category selector
- [ ] Show loading states
- [ ] Create feedback system
- [ ] Ensure accessibility

### Backend Implementation

#### LLM Integration
- [x] Set up FastAPI backend
- [x] Integrate OpenRouter LLM API
- [x] Load context files from backend/context
- [x] Analyze a specified article from backend/articles using context
- [ ] [Future] Support analyzing articles scraped from URLs

#### Data Configuration
- [ ] Set up news sources
- [ ] Add source categories
- [ ] Configure metadata
- [ ] Validate sources

#### Content Management
- [ ] Extract articles
- [ ] Clean content
- [ ] Detect duplicates
- [ ] Validate content

### Quality Assurance

#### Testing Implementation
- [ ] Add component tests
- [ ] Test integration
- [ ] Add E2E tests
- [ ] Test performance

#### Documentation Management
- [x] Document technical details
- [ ] Write user guide
- [ ] Document API
- [ ] Create deployment guide