# Telecom Clicker

A mobile clicker/idle game where you build a telecom empire from scratch. Start in 1880 with hand-crank switchboards, expand through every real technological era, and reach interspace communication.

## Repository Layout

| Path | Contents |
|---|---|
| `game/index.html` | Canonical web game (single-file HTML/CSS/JS, EN/KO language packs, localStorage save) |
| `game/tech-nodes.json` | Tech tree data: 87 nodes across 4 branches × 6 eras (shared by web + text versions) |
| `game/telecom_clicker.py` | Text edition of the game (Python 3, stdlib only, real-time, saves to `telecom_clicker_save.json`) |
| `*.md` | Design/plan documents used to build the game (see below) |
| `output/` | Release artifacts (`.aab` app bundles) |

> `android/` (native WebView shell) is intentionally **not** committed to this repository.

## Running the Text Game

```bash
cd game
python telecom_clicker.py
```

Type `help` inside the game. Core loop: click to earn → research tech → build infrastructure → expand regions → fight rivals → contracts/ads/bank/IPO.

## Design Documents (the plan)

The game was designed bottom-up with these documents:

| File | Contents |
|---|---|
| [gameplay-loop.md](gameplay-loop.md) | Core clicker loop, currencies, mobile design |
| [tech-tree.md](tech-tree.md) | Full tech tree: 4 branches (T/S/A/C) × 6 eras, ~161 nodes with prereqs |
| [market-investment.md](market-investment.md) | IPO, bonds, spectrum auctions, quarterly reports, M&A |
| [infrastructure.md](infrastructure.md) | 40+ asset types by era, region/grid system, upgrades & redundancy |
| [company-management.md](company-management.md) | 9 departments, C-suite, staffing, NOC, customer tiers |
| [rival-companies.md](rival-companies.md) | Regional competitors, growth DNAs, market share mechanics |
| [news-system.md](news-system.md) | 140+ historical events, tech-triggered + year-triggered layers |
| [revenue-effects.md](revenue-effects.md) | Which techs/infra boost which quality domains |
| [quality-competition.md](quality-competition.md) | Quality model: 4 domains, competitor quality, revenue formula |
| [rebirth+start.md](rebirth+start.md) | Getting kicked out, hostile takeover, rebirth with 30% stacking |

Plus change logs from the tuning passes: `CHANGES-UI-PASS-2.md`, `CHANGES-ECONOMY-PASS-3.md`, `CHANGES-FINANCE-PASS-4.md`, `UI-REDESIGN.md`, `ANDROID-UPDATE.md`.

## How This Game Was Made

1. Basic plan with GPT-5.6 Luna; a basic Python text game was built to test the plan.
2. DeepSeek-V4-Flash and GPT-5.6 Sol balanced the game and produced the concrete design (all `.md` files here).
3. The concrete web game (`game/index.html`) implements the final design; the text game remains as a playable test harness.

See [PROMPT.md](PROMPT.md) for a general prompt that can recreate the whole game from scratch.
