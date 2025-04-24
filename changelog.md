# Changelog

- All notable changes to this project will be documented in this file.
- Each day, create a new version of the project. The first version will be day 32, which is the current state of the project. The next day will be day 33, and so on.
- Check today's date.
- If nothing has been done on the day, create an empty entry.

## [Day 34] - 2025-04-23

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

## [Day 33] - 2025-04-22

### Added

- Migrated the project to use Svelte for the frontend framework.
- Added a 10px solid black line under the main header that spans the full 12-column grid.
  - Implemented via a new `<div class="header-underline"></div>` in `Header.svelte`.
  - Added `.header-underline` CSS class in `app.css` with clear section comments and grid alignment.

### Changed

- Updated documentation and comments for header and underline styling for clarity and maintainability.

## [Day 32] - 2025-04-21

### Added

- Initial changelog file created in the process folder.
- Frontend layout and styling for Depolarizer implemented.
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
