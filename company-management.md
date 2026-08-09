# Company Management System

Run your telecom as a real business. You are the **CEO** — you don't micromanage employees. You give orders to your C‑suite executives, and they handle recruitment, training, and trading (buying/selling) of staff. As your company grows, more contracts from companies and countries appear — bigger contracts pay more but impose tougher demands.

---

## 4.1 Organizational Structure

You (CEO) → **C‑Suite Executives** → **Departments** → **Staff**

**You never directly access individual staff members.** You set budgets, approve strategies, and respond to crises. Your executives run the departments.

### C‑Suite Executives

| Executive | Unlock | Department(s) | What They Do For You |
|---|---|---|---|
| **CFO** (Finance) | Revenue Bonds (Era 2) | Finance & Admin | Manages budget, bonds, IPO. **Recruits & trains** finance/admin/legal staff. |
| **CTO** (Technology) | #1ESS (Era 3) | R&D Lab, Network Engineering | Runs R&D, speeds up research. **Recruits & trains** engineers & researchers. |
| **COO** (Operations) | DDD (Era 2) | NOC, Field Operations | Keeps network running. **Recruits & trains** NOC/field staff. Reduces churn. |
| **CMO** (Marketing) | Touch‑tone launch (Era 2) | Sales & Marketing, Customer Support | Drives subscriber growth. **Recruits & trains** sales & support staff. |

Each executive has **Level 1–20**. Leveling costs cash and improves their effectiveness:

| L1 | L5 | L10 | L15 | L20 |
|---|---|---|---|---|
| Base bonus | +50% bonus | +100% bonus | +200% bonus | +400% bonus |

### Department Staff (You Don't Touch These)
Staff are managed entirely by the responsible executive. You see aggregate numbers only:

| Department | Managed By | Staff Types | You See Only |
|---|---|---|---|
| Network Engineering | CTO | Line installer, Switch tech, RF engineer | "Avg build speed: +15%" |
| R&D Lab | CTO | Researcher, Scientist, Bell Labs fellow | "RP/s: +420" |
| NOC | COO | Tier‑1/2/3 engineers | "Uptime: 99.87%, MTTR: 142s" |
| Field Operations | COO | Field tech, Lineman, Tower climber | "Avg repair time: 8m" |
| Sales & Marketing | CMO | Telemarketer, Sales rep, Enterprise acct mgr | "Sub growth: +3%/mo" |
| Customer Support | CMO | Call center agent, Tech support, Billing | "Churn: 1.8%/mo" |
| Finance & Admin | CFO | Accountant, Auditor, Treasury analyst | "Opex reduction: 12%" |
| Regulatory & Legal | CFO | Lawyer, Compliance officer, Lobbyist | "Fine reduction: 30%" |
| Data Center Ops | CTO (Era 4+) | Server tech, Network admin, Security | "Cloud revenue: +$50K/mo" |

### How You Interact With Executives
- **Review** — See department performance reports (aggregate metrics only)
- **Order** — Tell an executive to focus on a goal (e.g. "increase sub growth" → CMO shifts strategy)
- **Budget** — Allocate cash per department (more budget = faster hiring, better equipment)
- **Replace** — Fire an executive (costs reputation, takes time to find replacement)

---

## 4.2 Staffing System (Executive Layer)

### How Executives Hire & Manage
- Each department has **slots** (start at 3, can be expanded with cash — you approve budget, CFO executes)
- Staff have **levels**: Junior → Senior → Lead → Manager → Director
- Staff have **skills** (0–100) — executives naturally hire higher skilled staff as they level up
- Salary is auto-managed. You only see the **total salary cost** per department.

| Level | Skill Range | Typical Role |
|---|---|---|
| Junior (L1) | 10–30 | Entry, training |
| Senior (L2) | 35–55 | Independent worker |
| Lead (L3) | 55–75 | Team lead |
| Manager (L4) | 70–85 | Manages 5–10 staff |
| Director (L5) | 82–95 | Department head |

### Executive Recruitment Actions
As CEO, you see these options per executive. You can order the executive to:

| Action | Cost | Effect |
|---|---|---|
| **Hire push** | $10K–$1M (budget) | Executive fills open slots with best available talent |
| **Training program** | $5K–$500K (budget) | Raises avg department skill by 5–10 points |
| **Trade staff with subsidiary** | $50K–$2M | Exchange staff between departments |
| **Poach from competitor** | $100K–$5M | Hire a high-skill director away from rival |
| **Layoffs** | Reputation –5% | Cut salary cost but lose skill |

---

## 4.3 Operations Management

### NOC — Network Operations Center
Managed by COO. You see aggregate uptime and MTTR only. If NOC is understaffed, you get a warning: *"NOC queue: 12 alarms — recommend budget increase."*

**NOC Automation (tech tree dependent) — ordered by CTO:**

| Automation | Tech Prereq | Effect |
|---|---|---|
| Remote monitoring | T6 (Underground conduit) + S3 | Basic alarms from exchange |
| Automated diagnostics | S15 (#1ESS) | Self‑test on switch |
| Remote loopback test | A21 (ADSL) | Copper line test from CO |
| AI correlation | C33 (AI RIC) | Predicts failure before alarm |
| Zero‑touch healing | C35 (ZSM) | Auto‑resolves 60% of faults |

### Field Operations
Managed by COO. You see average repair time and total truck roll cost per month.

---

## 4.4 Customer Management

### Subscriber Tiers

| Tier | Typical ARPU | Churn Base | SLA | Unlock |
|---|---|---|---|---|
| Residential | $20–80/mo | 2%/mo | Best effort | Era 1 |
| Small Business | $100–300/mo | 1%/mo | 99.9% | Era 2 (PBX/Centrex) |
| Enterprise | $1,000–10,000/mo | 0.3%/mo | 99.99% + penalty | Era 3 (ISDN PRI) |
| Wholesale (other carriers) | Interconnect fees | Contract‑based | 99.99% | Era 3 (SS7) |
| Government | $500–5,000/mo | 0.1%/mo | 99.999% + security | Era 4 |

### Churn Formula
```
Monthly churn = baseChurn(tier)
               × (1 – 0.2 × customerSatisfaction)
               × (1 – 0.1 × supportStaffEffectiveness)
               × (1 – 0.05 × uptime)
               × (1 + 0.1 × competitorAggression)
               × pricePenalty
```

### Marketing Campaigns (Ordered by CMO)

| Campaign | Cost | Effect | Cooldown |
|---|---|---|---|
| Billboards / TV | $10k–$1M | +5% sub growth for 30s | 2 min |
| Promotional pricing | –20% ARPU for 30s | +15% sub growth for 30s | 5 min |
| Referral bonus | $5 per referral | +2% permanent growth | — |
| Enterprise roadshow | $100k | +10 enterprise leads | 10 min |

---

## 4.5 Contracts — Bigger Company, Bigger Demands

As your company grows, **external contracts** appear. These come from other companies or countries that want your telecom services. They pay well but impose **demands** you must meet — or lose the contract (and reputation).

### Contract Types

| Contract Source | Example | Typical Payout | Demand |
|---|---|---|---|
| **Small Business** | "Local bank needs dedicated line" | $5K–$50K one‑time | 99.5% uptime, 24h support response |
| **Enterprise** | "Retail chain wants nationwide MPLS VPN" | $50K–$500K/mo | 99.99% uptime, <30min fault response |
| **Carrier / Wholesale** | "Neighboring telco needs transit capacity" | $10K–$200K/mo | Latency <20ms, capacity 10Gbps |
| **Government** | "City hall wants fiber for 50 buildings" | $100K–$2M/mo | 99.999% uptime, security audit, local data |
| **Military** | "Ministry of defense — encrypted comms" | $1M–$10M/mo | Air‑gapped network, QKD, 24/7 dedicated NOC |
| **International** | "Foreign govt wants submarine cable access" | $5M–$50M one‑time | 5-year commitment, non‑discrimination clause |
| **Space Agency** | "Mars mission needs DTN relay" | $10M–$100M/mo | Interplanetary protocol, 99.9999% reliability |

### Contract Mechanics
- Contracts appear **automatically** based on your company size (sub count, regions, tech level)
- Each contract has a **deadline** — accept or ignore
- If you accept but **fail the demands** (e.g., uptime drops below SLA), you pay penalties and lose reputation
- **Multiple contracts** can run simultaneously — more revenue, more pressure
- **Renegotiation** — every 12 months the counterparty may demand better terms

### Demand Types

| Demand | What It Requires | Consequence If Failed |
|---|---|---|
| Uptime SLA | Your network uptime must stay above X% | Penalty fee + reputation loss |
| Latency cap | Average latency below Y ms | Contract cancelled |
| Capacity guarantee | Must maintain Z Gbps available bandwidth | Need to build more infra |
| Security compliance | Data must stay in‑country / encrypted | Government fine |
| Response time | NOC must acknowledge fault within N minutes | Penalty per missed SLA |
| Exclusivity | Cannot serve competitor in same region | Limits growth options (trade‑off) |

### Contract UI
```
┌──────────────────────────────────────────────────────────┐
│ 📄 NEW CONTRACT — Ministry of Defense                    │
│ Payout: $5M/mo  │  Deadline: 7 days to accept            │
│ Demands: 99.999% uptime, QKD encryption, 15s fault resp  │
│ Risk: Penalty $2M/event, Rep –10% if cancelled           │
│ [ACCEPT] [DECLINE]                                       │
└──────────────────────────────────────────────────────────┘
```

---

## 4.6 Corporate Finance

### Revenue Streams (beyond click revenue)

| Stream | Unlock | Contribution | Scalable By |
|---|---|---|---|
| Residential ARPU | Era 1 | 40–60% of revenue | More subscribers |
| Business ARPU | Era 2 | 15–25% | Enterprise sales staff |
| Interconnect / Termination | Era 2 (SS7) | 5–10% | Wholesale contracts |
| Data Center / Cloud | Era 4 | 5–15% | DC capacity |
| Content / TV Bundles | Era 3 | 5–10% | Content licensing |
| Tower / Infrastructure Lease | Era 5 | 3–8% | Tower count, REIT spin‑off |
| **Contracts** (see 4.5) | Era 2+ | 10–40% | Company size, reputation |

### Cost Structure (Opex)

| Cost Category | % of Revenue | Can Reduce By |
|---|---|---|
| Staff salaries | 15–30% | Automation (tech tree), outsourcing |
| Power & cooling | 5–15% | Energy‑efficient gear (tech), DC location |
| Spectrum lease / amortization | 5–20% | Efficient spectrum use (CA, MIMO) |
| Maintenance & repairs | 5–10% | Preventive maintenance, NOC automation |
| Interconnection (paying other carriers) | 3–8% | Peering agreements, IP transit negotiation |
| Customer acquisition cost (CAC) | 10–20% | Brand, word‑of‑mouth, organic growth |
| Regulatory & licensing | 2–5% | Compliance staff, lobbying |
| **Contract penalties** | 0–15% | Meeting SLA demands |

### CapEx Planning
You allocate cash between:
- **Build (infrastructure)** — growth CapEx (50–70% of total)
- **R&D (tech tree)** — innovation CapEx (10–20%)
- **Spectrum (auctions)** — strategic CapEx (0–30%, lumpy)
- **Data centers** — vertical expansion (5–15%)

---

## 4.7 Corporate Development (Era 3+)

### Mergers & Acquisitions

| Action | Cost | Effect | Prereq |
|---|---|---|---|
| Acquire rural ISP | $5M–$50M | Instantly unlocks region + subscriber base | IPO |
| Buy spectrum from another carrier | $100M–$1B | Gain spectrum license without auction | CEO L5 |
| Acquire content studio | $50M–$200M | Unlock TV/content bundle revenue | Era 4 |
| Merge with competitor | $1B+ | Eliminate competitor in region, gain subs | CEO L10 |
| Spin‑off tower assets (REIT) | — | Receive lump sum cash, lose tower lease revenue | Tower count >500 |

### Partnerships

| Partnership | Effect | Prereq |
|---|---|---|
| Roaming agreement | Your subscribers use partner towers → instant coverage in region | A18 (GSM) |
| Peering / IP transit | Reduced interconnection cost. No charge for mutual traffic. | C24 (BGP) |
| Wholesale MVNO | Sell network access to virtual operators. Low‑margin but volume. | A22 (3G) |
| Hyperscaler edge partnership | Colocate with AWS/Azure/GCP. DC revenue boost. | C29 (MEC) |

---

## 4.8 Regulatory & Compliance Events

Random events your CFO (via legal/compliance staff) can mitigate:

| Event | Effect | Mitigation |
|---|---|---|
| **Spectrum cap ruling** — regulator limits your holding | Forced sale of some licenses | Lobbyist reduces sale % |
| **Net neutrality fine** — zero‑rating ruled illegal | $1M–$50M fine | Compliance officer reduces by level |
| **Universal service obligation** — serve rural area | Cost ×$100k, revenue ×$1/mo | Delay with legal team (2 min) |
| **Data breach / privacy fine** | $5M–$100M + reputation | Security staff + encryption tech |
| **Local content rule** — host data locally | $500k per region | Data center in region = free |
| **Tax holiday ends** | +10% tax rate for 60s | CFO renegotiates (timed button) |

---

## 4.9 Company Dashboard

As CEO, you see this:

```
═══════════════════════════════════════════════
 CORP: AT&T-click  │ Tier: 3 (Digital)
 Your ownership: 68%    │ Staff total: 47
═══════════════════════════════════════════════
 Revenue:  $1.2M/mo     │ Opex:    $680K/mo
 Profit:   $520K/mo     │ Margin:  43%
═══════════════════════════════════════════════
 Subs:       48,203     │ Churn:   1.8%/mo
 ARPU:        $24.90    │ CAC:     $38
 Active contracts:  3   │ Contract rev: $150K/mo
═══════════════════════════════════════════════
 R&D:        +420 RP/s  │ Uptime: 99.87%
 NOC queue:  3 alarms   │ Field:   5 techs on shift
═══════════════════════════════════════════════

EXECUTIVES:
 CFO: L8  → "Finance healthy, bonds available"
 CTO: L6  → "R&D on track, network stable"
 COO: L5  → "NOC needs +2 T1 staff"
 CMO: L7  → "Sub growth +3%/mo, campaign available"
```

---

## 4.10 Company Progression Flow

```
Era 1:  You hire CFO & COO → they build first departments
  │
  v
Era 2:  CMO unlocks marketing → CTO unlocks R&D → contracts appear
  │
  v
Era 3:  IPO decision (stay private or go public) → big contracts
  │
  v
Era 4:  M&A possible → international contracts → more demands
  │
  v
Era 5:  AI reduces staff needs → executive levels matter more
  │
  v
Era 6:  Interstellar contracts → multi-planet operations
```

---

## 4.11 Cross‑System Interactions

| Executive | Tech Tree | Infrastructure | Market Investment |
|---|---|---|---|
| **CFO** | — | — | Unlocks bonds, IPO, reduces interest, manages buybacks |
| **CTO** | Accelerates RP, unlocks builds | Enables advanced infra (fiber, 5G) | Tech leadership → higher valuation |
| **COO** | NOC automation reduces opex | Uptime, repair speed, congestion relief | Higher uptime → stable stock, contract SLA |
| **CMO** | — | Faster penetration per region | Sub growth → revenue → stock price |
| **Contracts** | Some require specific tech (QKD, 5G) | Infrastructure capacity determines SLA feasibility | Contract revenue boosts quarterly results |
