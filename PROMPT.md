# General Prompt — Recreate Telecom Clicker From Scratch

This is the master prompt used to create this game. Feed it to any capable
coding agent (or a fresh session) together with the `.md` design documents in
this repository to rebuild the whole project.

---

**Project:** Telecom Clicker — a mobile clicker/idle game where the player
builds a telecom empire from 1880 to the interspace era.

**Goal:** Build a complete, balanced, playable game from the design documents
in this repo (`tech-tree.md`, `market-investment.md`, `infrastructure.md`,
`company-management.md`, `rival-companies.md`, `news-system.md`,
`revenue-effects.md`, `quality-competition.md`, `rebirth+start.md`,
`gameplay-loop.md`).

**Deliverables:**

1. **Web game** — single-file `game/index.html` (HTML/CSS/JS, no build step,
   no external libraries, mobile-first touch UI):
   - Click page: big tap zone, revenue + quality cards, click-earn hint,
     ripple effect on tap.
   - Research page: 4 branches (Transmission/Switching/Access/Core) × 6 eras,
     87+ tech nodes with prerequisites, SVG dependency graph, long-press
     tooltips, RP production with R&D budget slider and laboratory upgrades.
   - Expand page: 12 world regions, foothold %, rivals per region, new-region
     expansion, pending regions.
   - Infra page: era-gated infrastructure assets per region, bulk buy
     (×1/×5/×10/×25), income breakdown (base × tech × market × prestige).
   - Finance page: IPO (needs ANI + revenue), share buyback, bank credit
     (limit = revenue/s × 1800, 3-month rate resets, borrow/repay).
   - Ads subpage: 10 channels (newspaper → streaming), spend % of revenue,
     subscriber growth; contracts subpage: monthly-payment offers that boost
     foothold.
   - Local progress saved to localStorage every ~10s and on exit; session
     restores on reload.
   - EN + KO language packs with a language switcher in the settings menu.
   - Era pacing: ~6–7 hours of play per era on the fastest legal tech path
     (era RP cap carries over at most 30 minutes into the next era).

2. **Text edition** — `game/telecom_clicker.py` (Python 3, stdlib only,
   real-time background income thread, JSON save/load): same economy and
   systems as the web game, driven by commands (`click`, `research`,
   `build`, `expand`, `contracts`, `ads`, `bank`, `ipo`, `wait`, `save`).

3. **Android shell** (optional, kept out of git): WebView wrapper loading the
   game file, immersive mode, DOM storage enabled for persistence.

**Constraints:**
- Keep every page/tab to one job; no shared page functions.
- No new external libraries — reuse what the project already has.
- No personal information in any production file.
- Balance so a player clears each era in ~6–7 simulated hours; quality score
  (coverage/speed/reliability/latency) drives the revenue multiplier; rivals
  apply regional pressure; rebirth gives 30% carryover with stacking bonuses.

Use the `.md` files as the source of truth for numbers, events, and systems;
use `game/tech-nodes.json` as the canonical tech tree data.
