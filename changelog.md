# Changelog

## 2025-05-02 - Friday
### Changed
- **RandomTextBox.svelte**:
  - Complete overhaul: Replaced paragraph generation with a dynamic grid of randomly appearing letters.
  - Implemented dynamic grid sizing based on container dimensions.
  - Added character fade-in using CSS transitions triggered by JavaScript `setTimeout` with randomized delay.
  - Added individual character fade-out after a configurable `holdDuration`.
  - Modified update logic to only fill empty cells, preventing overwrites.
  - Adjusted styling for fixed cell size (e.g., 20x20), fonts (serif), and colors (using CSS variables).
- **LoadingDots.svelte**:
  - Added a rotating square element with CSS transition.
  - Removed original dot animation, text, associated logic, and styles.
  - Added absolute positioning to center the component on the screen.
- **+layout.svelte**:
  - Added four `RandomTextBox` components (two in left column, two in right), appearing conditionally during `phase2_components`.
  - Reordered `UrlInput.svelte` and `UrlInfo.svelte` in the right column, placing input above info.

### Added
- `LoadingDots.svelte` component for visual feedback during loading.
- `UrlInfo.svelte` component to display static instructions for URL input.
- `.module-dark` and `.module-light` CSS classes to `app.css` for themeable modules.
- Loading state logic (`isLoadingPhase2`) to `+layout.svelte` with a 5-second delay before showing phase 2 components.

### Changed
- **Component Loading Logic (`+layout.svelte`)**:
  - Refactored component loading into two phases controlled by `phase1_components` and `phase2_components` state variables.
  - Phase 1 (Header, NavMenu, UrlInput, About, UrlInfo) loads immediately after splash screen dismissal.
  - Phase 2 (ContentViewer, RandomTextBox) loads after Enter is pressed in `UrlInput` and a 5-second loading state (showing `LoadingDots`).
- **Component Styling & Placement (`+layout.svelte`, `NavMenu.svelte`, `app.css`)**:
  - Applied `.module-dark` / `.module-light` classes to relevant module wrappers in `+layout.svelte`.
  - Moved `About.svelte` component from right column to main column.
  - Refactored `NavMenu.svelte` styling:
    - Removed inline `style:` directives for color/background.
    - Removed JavaScript-based hover state (`hoveredIndex`).
    - Defined default, selected, and hover states using CSS classes and `:hover` pseudo-class in the `<style>` block.
    - Corrected text color for non-selected items to inherit from `.module-dark` parent.
  - Removed default background/color from base `.module` class in `app.css`.
- **Component Content (`About.svelte`, `UrlInfo.svelte`)**:
  - Added more detailed content sections (What, Why, How) to `About.svelte`.
  - Updated `UrlInfo.svelte` to display static instructions instead of dynamic URL info.
- **Transitions (`+layout.svelte`)**:
  - Added `out:fade` transition to `About.svelte` wrapper so it fades out when phase 2 components load.
  - Added `in:fade`/`out:fade` to `LoadingDots.svelte` wrapper.
- **LoadingDots.svelte**:
  - Implemented sequential dot animation using `setInterval`.
  - Added descriptive text ("Analyzing URL").
  - Removed `{#key}` block to prevent blinking during dot updates.
  - Adjusted styling (padding, font, size).
- **+layout.svelte**:
  - Corrected conditional logic for `<About>` component to ensure it fades out when loading starts (`{#if !isLoadingPhase2 && !phase2_components}`).
  - Removed unused `.module` class from `LoadingDots` wrapper.

### Fixed
- Corrected usage of Svelte state (`$state`) in `+layout.svelte` and `NavMenu.svelte` to use standard `let` for reactivity, resolving linter errors.
- Added missing component exports (`UrlInfo`, `LoadingDots`) to `frontend/src/components/index.ts` to resolve import errors.
- Fixed `NavMenu.svelte` text color inheritance issue by adjusting inline styles and later refactoring to use CSS classes.
- Typed the `event` parameter in `loadOtherComponents` in `+layout.svelte` to resolve TypeScript error.
- Prevented blinking effect in `LoadingDots.svelte` by removing the `{#key}` block around the animated dots.

## 2025-05-01 - Thursday
### Added
- Barrel file (`frontend/src/components/index.ts`) for centralized component exports.
- Focus styling and keyboard accessibility (`role`, `tabindex`, `on:keydown`) for static letters in `SplashOverlay.svelte`.
- Svelte 5 Runes (`$state`) for reactive state management in `SplashOverlay.svelte`.

### Changed
- **Component Refactoring & CSS Organization**:
  - Refactored `SplashOverlay.svelte`:
    - Click handler now only triggers on static "deconstructed" letters.
    - Overlay dismissal requires clicking specific letters or using keyboard (Enter/Space).
    - Removed click handler from main overlay container.
  - Refactored `RandomTextBox.svelte`:
    - Changed from character grid to generating realistic-looking random text paragraphs.
    - Simplified to generate static text by default, with optional `refreshInterval` prop.
    - Scoped styles directly in the component using `<style>` block.
    - Corrected props definition to use standard `export let` and added `refreshInterval` typing.
  - Updated CSS organization across components (`Header.svelte`, `About.svelte`, `ContentViewer.svelte`, `RandomTextBox.svelte`):
    - Moved component-specific styles from `app.css` into respective component files.
    - Ensured components use global `.module` class for container styling.
    - Ensured components utilize global theme variables (e.g., `var(--font-serif)`, `var(--main-bg)`).
- **Imports & Structure**:
  - Standardized component imports in `frontend/src/routes/+layout.svelte` to use the barrel file.
  - Updated `frontend/src/components/index.ts` to export all relevant components.
- **Layout & Styling**:
  - Updated `Header.svelte` styling:
    - Corrected underline visibility (`background: var(--main-bg)`).
    - Added smooth opacity transition on mount.
    - Ensured proper `grid-area: header;` is set.
  - Updated `frontend/src/routes/+layout.svelte` grid definition for clarity.
- Refactored CSS variable usage:
  - Replaced instances of `--main-bg` with `--color-light`.
  - Replaced instances of `--main-text` with `--color-dark`.
  - Replaced instances of `--accent` with `--color-highlight`.
  - Replaced instances of `--polarizing` with `--color-highlight`.
  - Replaced instances of `--text-secondary` with `--color-dark`.
  - Replaced instances of `--primary` / `--color-primary` with `--color-dark`.

### Fixed
- Corrected props syntax in `Header.svelte` (removed `$props()` and `$state()`).
- Resolved potential import issues by ensuring all used components are exported from `frontend/src/components/index.ts`.
- Fixed reactivity issues in `RandomTextBox.svelte` when `refreshInterval` is used.

### Removed
- Unused `frontend/src/components/RandomTextBox.css` file.
- Redundant styles from `app.css` (styles now scoped within components).
- Duplicated CSS rule blocks in `frontend/src/styles/app.css`.
- Unused `--module-bg`, `--sidebar-text`, `--sidebar-selected` CSS variables and associated rules from `frontend/src/styles/app.css` (due to user edits).
- Unused `.left-sidebar` CSS rules from `frontend/src/styles/app.css`.

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

## 2025-05-07 - Wednesday
### Added
- Tested and validated full-article scraping from NPR using `newspaper3k` with custom user-agent.
- Confirmed NPR as a scraper-friendly source for politics articles.
- Set groundwork for a new component based on NPR article: https://www.npr.org/2025/05/06/nx-s1-5387465/trump-carney-canada-tariffs

### Fixed
- Resolved `lxml.html.clean` ImportError by installing `lxml[html_clean]` for compatibility with `newspaper3k`.

### Changed
- **PoliticalNewsExample.svelte**:
  - Removed dropdown menu for article selection; now always loads and displays the first available article automatically.
  - Fixed Svelte duplicate key error in paragraph rendering by using the index as the key.
  - Improved error handling and loading state.
- **Vite Proxy Config**:
  - Updated proxy in `vite.config.ts` to rewrite `/backend` to `/` for correct backend API routing.

### Fixed
- Resolved 404 errors and proxy issues between frontend and backend.
- Ensured FastAPI backend and Svelte frontend communicate seamlessly for article loading.

### Documentation
- Updated README to reflect new workflow, proxy setup, and dynamic article loading.
