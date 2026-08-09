# UI Redesign

The interface was refreshed without changing the game's simulation or economy logic.

## Main changes

- Added a clearer mobile dashboard with a central connection button and live metric cards.
- Reworked the visual system with consistent colors, spacing, typography, borders, and cards.
- Improved the top status bar and bottom navigation for mobile use.
- Redesigned the research screen with readable node names, branch legends, larger nodes, and richer tooltips.
- Added consistent page headers to expansion, infrastructure, and IPO screens.
- Restyled contracts, advertisements, buttons, sliders, menus, and region controls.
- Kept `game/index.html` and `android/app/src/main/assets/index.html` synchronized.

## Validation

- JavaScript syntax checked with Node.js.
- Runtime tested at 360×800, 390×844, and 768×1024.
- All five main tabs rendered without page errors.
- The connect action, research graph, and horizontal tree scrolling were verified.
