# Revenue Effects — Quick Reference

> Revenue follows: **regionRevenue = infrastructureBase × technologyMultiplier × regionalMarketMultiplier × prestigeMultiplier**
>
> See [quality-competition.md](quality-competition.md) for the full formula and per-node quality values.
> See [rival-companies.md](rival-companies.md) for the market share / competitor model.

## Two‑Factor Revenue

| Factor | What It Represents | How To Increase |
|---|---|---|
| **Infrastructure Base** | Your physical network capacity. $/s per asset. | Build more assets, level them up, prestige obsolete gear. |
| **Technology Multiplier** | How effectively your network runs. ×1.0–2.0+. | Research tech nodes to raise quality scores (Coverage, Speed, Reliability, Latency). |
| **Regional Market** | Foothold × competitive share in that region. | Raise foothold, improve quality, and out-compete local rivals. |

### Infrastructure Base Values (per asset per second)

| Era | Asset | Base Revenue |
|---|---|---|
| 1 | Copper Trunk | $0.01 |
| 1 | Manual Switchboard | $0.05 |
| 1 | Telegraph Line | $0.01 |
| 2 | Coaxial Backbone | $0.50 |
| 2 | Microwave Tower | $0.30 |
| 2 | Crossbar Exchange | $0.80 |
| 2 | Submarine Cable (TAT-1) | $2.00 |
| 2 | Mobile Tower (MTS) | $0.15 |
| 3 | Fiber Optic Cable | $5.00 |
| 3 | Digital CO (#5ESS/DMS) | $4.00 |
| 3 | Cell Tower (1G/2G) | $1.00 |
| 3 | Data Center | $2.00 |
| 3 | SONET Ring | $3.00 |
| 4 | FTTH OLT (GPON) | $8.00 |
| 4 | LTE eNodeB | $5.00 |
| 4 | DWDM Terminal | $12.00 |
| 4 | IP Core Router | $10.00 |
| 5 | 5G gNodeB (mmWave) | $15.00 |
| 5 | LEO Satellite Terminal | $20.00 |
| 5 | AI-NFV Core | $5.00 |
| 6 | Quantum Repeater | $100.00 |
| 6 | Lunar Relay Station | $500.00 |
| 6 | Neutrino Transceiver | $1,000.00 |
| 6 | Dyson Swarm Node | $5,000.00 |
| 6 | Interplanetary Gateway | $2,000.00 |

### Technology Quality → Multiplier

| Quality Score | Tech Multiplier |
|---|---|
| 0 | ×1.00 |
| 25 | ×1.25 |
| 50 | ×1.50 |
| 75 | ×1.75 |
| 100 | ×2.00 |
| 125 | ×2.25 |
| 150 | ×2.50 |

### Regional Market → Revenue Fraction

`regionalMarketMultiplier = footholdFraction × competitionMultiplier`

Competition is derived from your quality relative to rivals in that region. See `rival-companies.md`.

## Click Revenue

Each tap = **`$5.00 × technologyMultiplier × prestigeMultiplier`**. A brand-new run therefore starts at **$5 per click**. Cash only — no RP from clicking.
