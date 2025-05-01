# deconstructed

## Project Overview

`deconstructed` is a web application designed to combat division and distrust by presenting news content in a neutral, emotion-free manner. It fetches articles, analyzes them using an LLM backend (integrated with OpenRouter), and displays the deconstructed content through a SvelteKit frontend.

## Project Goal

The primary goal is to provide users with a tool that helps them understand news events without the emotional charge often found in standard reporting. By stripping away polarizing language and focusing on factual content, the project aims to foster more informed and rational public discourse.

## Tech Stack

### Frontend Components

- **Framework**: SvelteKit (with Svelte 5 Runes)
- **Language**: TypeScript
- **Styling**: CSS with CSS Variables (component-scoped and global styles defined in `src/styles`)
- **Fonts**: Google Fonts (imported via `src/styles/fonts.css`)
- **Animations**: Svelte built-in transitions and custom animations (`src/components/animations.ts`)

### Backend Components

- **Framework**: FastAPI (Python)
- **LLM Integration**: OpenRouter API
- **HTTP Client**: httpx
- **Environment Management**: python-dotenv

### Development Environment

- **Version Control**: Git
- **IDE**: VS Code with Cursor
- **Package Manager**: npm (frontend), pip (backend)

## Folder Structure

```text
destructured/
├── backend/          # FastAPI backend (Python, LLM integration)
│   ├── articles/     # Example articles for analysis (Markdown)
│   ├── context/      # Context files for LLM analysis (Markdown)
│   ├── __pycache__/  # Python cache (ignored)
│   ├── main.py       # FastAPI app entry point
│   └── requirements.txt # Python dependencies
├── frontend/         # SvelteKit frontend
│   ├── src/
│   │   ├── components/ # Reusable Svelte components
│   │   │   └── index.ts  # Barrel file for component exports
│   │   ├── routes/     # SvelteKit page routes (+layout.svelte, +page.svelte)
│   │   └── styles/     # Global CSS files (app.css, colors.css, fonts.css)
│   ├── static/       # Static assets (e.g., favicon)
│   ├── node_modules/ # Node.js dependencies (ignored)
│   ├── .svelte-kit/  # SvelteKit build files (ignored)
│   ├── package.json
│   ├── package-lock.json
│   ├── svelte.config.js
│   ├── tsconfig.json
│   └── vite.config.ts
├── .cursor/          # Cursor configuration/rules
├── .venv/            # Python virtual environment (ignored)
├── archive/          # Archived files (ignored)
├── .env              # Environment variables (ignored)
├── .gitignore        # Git ignore configuration
├── .npmrc            # Npm configuration
├── changelog.md      # Project changelog
├── LICENSE           # Project license
├── README.md         # This file
└── to-do.md          # Project to-do list
```

## Getting Started

### Prerequisites

- Node.js and npm
- Python and pip
- Git

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd deconstructed
    ```
2.  **Backend Setup:**
    ```bash
    cd backend
    python -m venv ../.venv # Create virtual env in root .venv folder
    # Activate the virtual environment (adjust for your OS/shell)
    # Windows (Git Bash/Linux Subsystem):
    source ../.venv/Scripts/activate
    # Windows (Command Prompt):
    ..\.venv\Scripts\activate.bat
    # Windows (PowerShell):
    ..\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    # Create a .env file in the *project root* (/) and add your OPENROUTER_API_KEY
    # Example .env:
    # OPENROUTER_API_KEY=sk-or-...
    cd ..
    ```
3.  **Frontend Setup:**
    ```bash
    cd frontend
    npm install
    cd ..
    ```

### Running the Application

1.  **Start the Backend Server:**
    *(Ensure your virtual environment is activated)*
    ```bash
    cd backend
    uvicorn main:app --reload
    # Server runs at http://localhost:8000
    cd ..
    ```
2.  **Start the Frontend Dev Server:**
    ```bash
    cd frontend
    npm run dev -- --open
    # App runs at http://localhost:5173 (or next available port)
    ```

## Backend LLM Integration Details

- Uses **FastAPI**.
- Integrates with **OpenRouter LLM API** (requires `OPENROUTER_API_KEY` in root `.env` file).
- Analyzes articles from `backend/articles/` using context from `backend/context/`.
- `/analyze` endpoint takes `article_filename` and user `text` (question/instruction).
- Constructs a prompt for the LLM, combining context and the article content.
- Handles file not found errors.
- **Planned:** Support scraping articles directly from URLs.

## Core Features

- Responsive grid layout using CSS Grid.
- Component-based architecture (Svelte 5 Runes) with barrel file exports.
- Centralized CSS theming (`src/styles/colors.css`, `src/styles/fonts.css`).
- Scoped component styles alongside global styles (`src/styles/app.css`).
- Type-safe development with TypeScript.
- LLM-powered article analysis via FastAPI backend.
- Interactive splash screen on load.
- Standardized CSS variable naming and usage.

## Project Outline (Original)

A tool that scrapes and deconstructs news content from multiple sources. Users can select news categories like Political, Financial, or World news. Initially supporting Political news only. The system scrapes predetermined sites for popular stories, processes them through the deconstructor, and presents neutral, fact-based content.

### System Features (Original)

- Multi-source news aggregation
- Political bias detection
- Emotional language filtering
- Fact-based content generation
- Source diversity (left/center/right)

## Implementation Steps (Original)

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

## Development Status (Legacy - See `to-do.md`)

### Frontend Implementation (Legacy)

#### Initial Setup
- [x] Initialize project
- [x] Set up TypeScript
- [x] Configure dev environment
- [x] Set up version control

#### Project Organization (Legacy)
- [x] Create directory structure
- [x] Configure project
- [x] Set up Git
- [x] Add gitignore

#### Component Development (Legacy)
- [x] Build header
- [x] Create navigation
- [x] Add content viewer
- [x] Create URL input
- [x] Add placeholders

#### Visual Design (Legacy)
- [x] Implement grid layout
- [x] Set up CSS system
- [x] Add fonts
- [x] Create animations

#### User Interface (Legacy)
- [x] Add category selector
- [ ] Show loading states
- [ ] Create feedback system
- [ ] Ensure accessibility

### Backend Implementation (Legacy)

#### LLM Integration
- [x] Set up FastAPI backend
- [x] Integrate OpenRouter LLM API
- [x] Load context files from backend/context
- [x] Analyze a specified article from backend/articles using context
- [ ] [Future] Support analyzing articles scraped from URLs

#### Data Configuration (Legacy)
- [ ] Set up news sources
- [ ] Add source categories
- [ ] Configure metadata
- [ ] Validate sources

#### Content Management (Legacy)
- [ ] Extract articles
- [ ] Clean content
- [ ] Detect duplicates
- [ ] Validate content

### Quality Assurance (Legacy)
