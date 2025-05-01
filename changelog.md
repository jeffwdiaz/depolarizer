# Changelog

## 2025-04-30 - Wednesday
### Changed
- Modified splash grid animation:
  - Reduced grid cell size from 100x100 to 50x50 pixels
  - Adjusted font size to 2rem for better readability in smaller cells
  - Improved animation consistency between static and dynamic letters
  - Removed redundant splash title text
  - Static "deconstructed" text now animates in with the grid
### Fixed
- Removed cached .svelte-kit directory from git tracking
- Added .svelte-kit to .gitignore for better version control

## 2025-04-29 - Tuesday
### Added
- FastAPI backend now supports LLM-powered analysis of articles.
- `/analyze` endpoint accepts:
  - `article_filename`: the name of the article in `backend/articles` to analyze.
  - `text`: the user's question or instruction.
- Loads all context files from `backend/context` and builds a structured prompt for the LLM (OpenRouter API).
- Returns a generic error if the article file is not found.
- Changelog entry for today per documentation rules.
- Added archive/** to .gitignore for better project organization
### Changed
- Documentation and changelog updated to follow project documentation rules.
- README.md updated to reflect FastAPI backend, OpenRouter LLM integration, and new folder structure.
- To-do list updated to include LLM integration and future URL scraping.
- Backend overview updated for new API and folder structure.
### Fixed
- Documentation files reviewed and validated for compliance with project standards
### Planned
- Add support for scraping article content from a URL for analysis using the same context mechanism.

## 2025-04-27 - Sunday
### Changed
- Splash grid animation now reveals letters in a randomized order for a more dynamic effect.
- Explicitly set Garamond font for grid letters to ensure consistent typography.
- Improved animation timing and style consistency in SplashOverlay.

## 2025-04-24 - Thursday
### Changed
- Restructured project file organization:
  - Moved components from `src/lib` to `src/components`
  - Updated all import paths to reflect new structure
  - Relocated animations.ts to components directory
  - Updated component imports to use relative paths
- Fixed remaining path references after lib folder removal:
  - Updated import path in app.css from './lib/styles/fonts.css' to './styles/fonts.css'
  - Updated README.md folder structure to reflect current organization
  - Updated path aliases in .svelte-kit/tsconfig.json to use new directory structure
  - Removed outdated lib directory references

## 2025-04-23 - Wednesday
### Added
- Created new FillerImageBlock component with:
  - Random height and width generation
  - Shine animation effect
  - Smooth transitions
  - Customizable dimensions through props
- Created new FillerTextBlock component with:
  - Random paragraph and line generation
  - Different width ranges for last lines
  - Smooth transitions
  - Customizable ranges through props
### Changed
- Centralized all component styles in app.css:
  - Moved FillerImageBlock styles to app.css
  - Moved FillerTextBlock styles to app.css
  - Added clear section comments for each component's styles
- Improved code organization by separating component logic from styling
- Updated header styling:
  - Set header height to 100px
  - Changed font size to 60px
  - Reduced underline height to 5px
  - Removed redundant full-width-header class
  - Consolidated header grid styles
  - Fixed align-items typo in header
  - Updated header underline comment to reflect new height
- Repositioned left sidebar:
  - Moved sidebar below header and underline
  - Adjusted sidebar height to account for header space
  - Updated positioning to align with grid margins
- Fixed component structure:
  - Added missing article-body wrapper in Article component
- Improved CSS organization:
  - Moved component styles from Header.svelte to app.css
  - Enhanced CSS selector specificity for better style application
  - Consolidated all styles in the global CSS file
  - Renamed sidebar classes for clarity:
    - .sidebar → .left-sidebar
    - .grid-sidebar → .grid-left-sidebar
  - Removed unused classes:
    - .main-flex-layout
    - .text-center
    - .mt-24
  - Reorganized app.css into logical sections:
    - Theme Variables
    - Base Styles
    - Layout & Grid
    - Component-specific styles
    - Utility classes
    - Removed redundant rules and comments

## 2025-04-22 - Tuesday
### Added
- Migrated the project to use Svelte for the frontend framework.
- Added a 10px solid black line under the main header that spans the full 12-column grid.
  - Implemented via a new `<div class="header-underline"></div>` in `Header.svelte`.
  - Added `.header-underline` CSS class in `app.css` with clear section comments and grid alignment.
### Changed
- Updated documentation and comments for header and underline styling for clarity and maintainability.

## 2025-04-21 - Monday
### Added
- Initial changelog file created in the process folder.
- Frontend layout and styling for deconstructed implemented.
- Article section and polarizing-language markup added.
- Project summary added to header description.
### Changed
- Switched main layout to a 5-column CSS grid: fixed-width sidebars and a 3-column center.
- Updated `.main-content` to use a minimal, grid-friendly style and removed excess padding/margins.
- Header and URL input now span all 3 columns; header description appears top-right.
- Article section spans all 3 columns.
- Restored `.header h1` CSS for prominent heading.
### Removed
- Old flexbox and max-width layout styles from `.main-content`.
- Redundant/legacy header description and main-content column markup.
