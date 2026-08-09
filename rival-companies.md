# Rival Companies — Regional Competitors

You are not alone. Other telecom companies exist, each dominating **their home region**. To grow, you must squeeze into dominated markets, find niches, and out-compete them.

---

## How Rivals Work

At game start, **2–4 rival companies** are generated with randomized traits. Each owns a home region with >50% market share. You start in a **neutral or underserved region** and must expand into their territories.

### Rival Generation

| Aspect | Randomization |
|---|---|
| **Name** | Drawn from real defunct/absorbed telecom names |
| **Home region** | Assigned at game start (continent/country cluster) |
| **Specialty** | One quality domain they prioritize (Coverage/Speed/Reliability/Latency) |
| **Growth DNA** | How fast they invest in tech vs. finance across eras |
| **Risk profile** | Conservative → Aggressive (affects debt, pricing, expansion speed) |
| **Starting era quality** | Slightly below or at era baseline (±5 quality points) |

### Example Rivals

| Rival | Home Region | Specialty | DNA | Risk |
|---|---|---|---|---|
| **Nordic Telecom** | Scandinavia | Reliability | Tech‑first, slow financial growth | Conservative |
| **Mediterranean Cable** | Southern Europe | Coverage | Balanced | Moderate |
| **Continental Networks** | Central Europe | Speed | Financial‑first, fast expansion | Aggressive |
| **Eastern Telecom** | Eastern Europe | Latency | Tech‑follower, low cost | Conservative |
| **Colonial Wireless** | Southeast Asia | Coverage | Fast growth, high debt | Aggressive |
| **Island States Telecom** | Oceania/Islands | Latency (submarine) | Slow tech, high margin | Moderate |

Each playthrough generates a unique set. You never face the same combination twice.

---

## Region Market Share Model

Each region has a **market share pie**. Rivals own slices. You compete for the rest.

```
Region: Central Europe
─────────────────────────────────
 Continental Networks:  52%  (home dominant)
 Mediterranean Cable:   18%  (secondary)
 You:                    5%  (entering)
 Unserved / contested:  25%
─────────────────────────────────
```

### Starting Conditions

| Region Type | Player Start | Rival Dominance |
|---|---|---|
| **Neutral / underserved** | You start here. Weak or no rivals. | <15% each |
| **Rival home** | Must fight for every % point. | 40–60% one rival |
| **Contested** | 2–3 rivals battling. Opportunity. | 20–35% each |
| **Greenfield** (new era) | First mover advantage. | No rivals yet |

### Capturing Market Share

Your market share in a region changes based on:

```
marketShareChange = (yourQuality / rivalQuality) × investmentMultiplier × regionCapacity

yourQuality > rivalQuality → you gain share
yourQuality < rivalQuality → you lose share (or can't enter)
```

#### Quality Comparison Per Region
Your quality in a region = your network quality × (1 + regional infra bonus)

Rival's quality in their home region = base × (1 + home_advantage × 1.3)

To take share from a rival in their home region, your quality must be **~30% higher** than theirs. In neutral regions, the threshold is equal quality.

#### Investment Multiplier
- Running a price war: ×1.5 share gain (but reduces revenue)
- Advertising campaign: ×1.3
- Government contract: locks in 5–10% share for contract duration
- Regulatory barrier: ×0.5 if rival has local regulatory favor

---

## Rival Growth Patterns

Each rival follows a **growth DNA** that determines their tech speed and financial health across eras.

### Growth DNA Types

| DNA | Tech Speed | Financial Growth | Behavior |
|---|---|---|---|
| **Tech‑first** | Fast (1.5× RP/s) | Slow (0.7× revenue growth) | Invests heavily in R&D. May run debt. |
| **Financial‑first** | Slow (0.7× RP/s) | Fast (1.5× revenue growth) | Marketing, pricing, M&A focused. |
| **Balanced** | 1.0× | 1.0× | Steady performer. |
| **Tech‑follower** | 0.5× | 1.3× | Copies your tech with delay. Low R&D cost. |
| **Aggressive** | 1.2× (erratic) | 1.4× (high debt) | Boom/bust. Fast expansion, bankruptcy risk. |
| **Conservative** | 0.8× | 1.1× (low debt) | Slow but stable. Hard to dislodge from home region. |

### Era Affinity

Each rival has an era where they are **strongest** (their historical peak):

| Era Affinity | Peak Performance | Weakness |
|---|---|---|
| **Analog** (Era 1–2) | Excellent with copper/electromechanical | Struggles with digital transition |
| **Digital** (Era 3) | Master of switching, fiber, GSM | Misses internet revolution |
| **Broadband** (Era 4) | Dominates IP, LTE, FTTH | Weak in early eras, struggles with 5G |
| **Autonomous** (Era 5) | AI/software‑defined native | Weak physical infrastructure |
| **Future** (Era 6) | Quick adopter of quantum/space | Neglects current revenue |
| **Generalist** | No peak, steady throughout | No weakness, no exceptional strength |

### Rival Events (Random)

Rivals generate their own in-game news events:

| Event | Effect on Them | Effect on You |
|---|---|---|
| **Rival builds new submarine cable** | +5% Coverage in their region | Threat: they might encroach on your region |
| **Rival secures government contract** | Locks 5% share in their home region | Harder to enter that region |
| **Rival wins spectrum auction** | +3% Speed quality | Next auction more expensive for you |
| **Rival suffers major outage** | –10% Reliability, –5% share | Opportunity: run ads targeting their customers |
| **Rival acquired by larger entity** | +20% financial but –10% flexibility | More powerful but slower competitor |
| **Rival goes bankrupt** | They dissolve. Region opens up. | Opportunity to acquire their assets |
| **Rival starts price war** | Revenue –15% (theirs, short‑term) | Revenue –10% (yours, must respond) |
| **Rival merges with another rival** | Combined entity, stronger | Tougher competitor, but regulatory scrutiny |

---

## Strategic Implications

### Surviving in Dominated Regions
1. **Find their weakness** — a Coverage‑specialist rival likely has lower Latency. Exploit that.
2. **Target neutral/greenfield regions first** — build a revenue base before fighting home rivals.
3. **Use contracts** — a government contract can give you protected share even in rival territory.
4. **Timing is everything** — a rival in their "weak era" is vulnerable. Attack during their transition.
5. **Bankruptcy** — an aggressive rival may collapse. Be ready to acquire their assets.

### Squeezing Into Niche Markets
- Niche = a specific subscriber tier (enterprise, government, wholesale) or specific quality domain
- You can achieve high quality in 1 domain even if your overall is lower
- Example: if a rival has Coverage 80 but Latency 40, you can offer low‑latency service to their enterprise customers without beating them on coverage

### Rival Intelligence
As you invest in Core Network tech, you unlock **intelligence** on rivals:

| Tech | Intel Unlocked |
|---|---|
| C4 (Numbering plan) | Know rival names and home regions |
| C9 (MF signaling) | See rival subscriber count |
| C15 (SS7) | See rival quality scores |
| C17 (TCP/IP) | See rival financial health |
| C24 (BGP) | See rival contract portfolio |
| C33 (AI RIC) | Predict rival's next move |

---

## Rival UI

```
┌──────────────────────────────────────────────────────────┐
│ COMPETITORS — Central Europe                             │
├────────────┬───────┬──────┬──────┬────────┬──────┬───────┤
│ Rival      │ Home  │ Shr  │ Qual │ Tech   │ Fin  │ Risk  │
├────────────┼───────┼──────┼──────┼────────┼──────┼───────┤
│ Continental│ 52%   │ Own  │ 72   │ 3.2 RP │ $45M │ Med   │
│ Nordic Tel │ 12%   │ NE   │ 68   │ 2.1 RP │ $28M │ Low   │
│ You        │  5%   │ —    │ 55   │ 1.8 RP │ $12M │ —     │
│ Unserved   │ 25%   │ —    │ —    │ —      │ —    │ —     │
├────────────┴───────┴──────┴──────┴────────┴──────┴───────┤
│ Intel: SS7 active — you see all quality scores.          │
│ Opportunity: Nordic Tel has Latency 45 (your specialty). │
└──────────────────────────────────────────────────────────┘
```

---

## Rival Company Name Bank

Generated names are drawn from this list of defunct/absorbed telecom companies (kept general):

| Pool A | Pool B | Pool C |
|---|---|---|
| Mercury | BellSouth | Pacific Bell |
| One2One | Telenor | Telia |
| Orange | TIM | KPN |
| Mobilcom | E‑Plus | O2 |
| Colt | Energis | Thus |
| Cable & Wireless | Global Crossing | FLAG Telecom |
| WorldCom | MCI | Sprint |
| GTE | NYNEX | US West |
| Telus | Bell Canada | Manitoba Tel |
| Télécom | France Câbles | Genérale |

Two names are combined to form rival identity: `{Pool A name} {Pool B name}` → "Mercury Telenor", "Cable & Wireless Telenor", "WorldCom BellSouth", etc.
