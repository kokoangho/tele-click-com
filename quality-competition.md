# Quality & Competition — The Real Revenue Driver

Revenue is driven by **infrastructure × technology**, moderated by **competition** with rival companies in each region. If you ignore either infrastructure or technology, your revenue suffers regardless of the other.

---

## Revenue Formula

```
regionRevenue = infrastructureBase × technologyMultiplier × marketShare
totalRevenue  = sum of all regionRevenue
```

### Infrastructure Base
Infrastructure provides the **capacity** to earn. More and better infrastructure = higher base.

| Factor | How It Scales |
|---|---|
| **Infrastructure count** | Each asset contributes a base value (see `infrastructure.md` for per-asset base) |
| **Infrastructure level** | Each asset can be leveled 1–100. Level 50 = 50× base value. |
| **Era relevance** | Obsolete assets (e.g., copper in Era 4) contribute 0×. Prestige multiplier compensates. |

### Technology Multiplier
Technology **multiplies** the value of infrastructure. Better quality = each infrastructure unit earns more.

```
technologyMultiplier = 1.0 + (yourQuality / 100)
```

- Quality is the weighted average of 4 domains (Coverage, Speed, Reliability, Latency)
- At quality 0 → ×1.0 (base)
- At quality 50 → ×1.5
- At quality 100 → ×2.0
- Quality above 100 still scales (diminishing returns past 100)

### Market Share
Rivals split each region. Your share is determined by relative quality. See [rival-companies.md](rival-companies.md).

| Your Quality vs. Rival | Market Share Outcome |
|---|---|
| Your quality > rival by 20+ | You dominate. 50%+ share, rival shrinks. |
| Your quality > rival by 10–20 | You lead. 35–50% share. |
| Your quality ≈ rival (±10) | Split. 15–35% share each. |
| Your quality < rival by 10–20 | You trail. 5–15% share. |
| Your quality < rival by 20+ | You barely exist. <5% share, losing money. |

In the region you **start** in (neutral/underserved), no rival has >30% share. You can grow without fighting.

---

## 4 Quality Domains

Every tech node and infrastructure asset improves one or more of these domains:

| Domain | What It Measures | Max Score | Visible As |
|---|---|---|---|
| **Coverage** | Reach, regions, subscriber capacity | 0–100 | Serviceable population, new regions |
| **Speed** | Data throughput per subscriber | 0–100 | Mbps, plan tiers |
| **Reliability** | Uptime, fault tolerance | 0–100 | Uptime %, MTTR |
| **Latency** | Responsiveness, delay | 0–100 | ms ping |

### Domain Weight by Subscriber Tier

| Tier | Coverage | Speed | Reliability | Latency |
|---|---|---|---|---|
| Residential | 30% | 30% | 20% | 20% |
| Small Business | 20% | 35% | 25% | 20% |
| Enterprise | 5% | 25% | 50% | 20% |
| Wholesale | 15% | 30% | 40% | 15% |
| Government | 5% | 15% | 60% | 20% |

Your **overall quality** for a region = weighted average across tiers × infrastructure coverage in that region.

---

## Competitor Quality

Rivals increase their quality over time. See [rival-companies.md](rival-companies.md) for per-rival growth rates.

### Base Competitor Quality by Era

| Era | Base Quality | Description |
|---|---|---|
| 1 (Analog Dawn) | 10 | Very basic. Copper phone works. |
| 2 (Electromechanical) | 25 | DDD, crossbar, basic mobile. |
| 3 (Digital & Satellite) | 45 | Digital switching, fiber, cellular. |
| 4 (Broadband & IP) | 65 | LTE, FTTH, IP core, MPLS. |
| 5 (Autonomous) | 85 | 5G, SDN, LEO, AI operations. |
| 6 (Interspace) | 95 | Quantum, interplanetary. |

Each year within an era, rival quality creeps **+1 point** (simulating their investments).

Rivals with **Tech‑first** DNA grow +1.5 per year. **Tech‑follower** DNA grows +0.5 per year.

### Regional Quality Variation

- **Rival home region**: rival gets +30% quality bonus (home advantage)
- **Neutral region**: baseline
- **Greenfield region** (new era): no rivals exist for the first 2 years of the era → 100% market share

---

## How Tech & Infrastructure Affect Quality

Each tech node and infrastructure asset contributes points to specific domains.

### Tech Nodes → Quality Points

| Node | Coverage | Speed | Reliability | Latency |
|---|---|---|---|---|
| **Transmission** | | | | |
| T1 Twisted-pair copper | +3 | +1 | 0 | 0 |
| T2 Pupin loading coil | +2 | 0 | 0 | +2 |
| T3 Phantom circuit | 0 | +2 | 0 | 0 |
| T4 Open-wire FDM | 0 | +5 | 0 | 0 |
| T5 Transcontinental line | +8 | 0 | +2 | –1 |
| T6 Underground conduit | 0 | 0 | +5 | 0 |
| T8 L-carrier coaxial | 0 | +8 | +2 | 0 |
| T9 TD-2 microwave relay | +5 | +3 | 0 | +3 |
| T10 TAT-1 submarine | +10 | +2 | +3 | –2 |
| T11 N-carrier short-haul | +2 | +2 | 0 | 0 |
| T12 Troposcatter | +5 | +1 | 0 | –1 |
| T13 TASI | 0 | +3 | 0 | –1 |
| T14 Submarine repeater | 0 | 0 | +5 | 0 |
| T15 Single-mode fiber | 0 | +15 | +3 | +5 |
| T16 T-carrier (T1) | 0 | +5 | +3 | 0 |
| T17 TAT-8 fiber submarine | +8 | +5 | +5 | +2 |
| T18 SONET | 0 | +3 | +15 | 0 |
| T19 EDFA | 0 | +5 | +5 | +2 |
| T20 DWDM | 0 | +15 | 0 | 0 |
| T21 HFC | +3 | +8 | –1 | 0 |
| T22 40G DWDM | 0 | +8 | 0 | 0 |
| T23 100G coherent | 0 | +10 | 0 | 0 |
| T24 TPE transpacific | +8 | +5 | +3 | +2 |
| T25 400G/800G optics | 0 | +12 | 0 | 0 |
| T26 GPON | 0 | +10 | +2 | +2 |
| T27 NG-PON2 | 0 | +8 | 0 | 0 |
| T28 G.fast | 0 | +5 | 0 | 0 |
| T29 1.6T coherent | 0 | +10 | 0 | 0 |
| T30 Flex-grid DWDM | 0 | +5 | 0 | 0 |
| T31 Hollow-core fiber | 0 | +5 | +2 | +15 |
| T32 Free-Space Optics | 0 | +5 | –2 | +5 |
| T33 EDFA+Raman hybrid | 0 | 0 | +8 | +2 |
| T34 Space-Division Mux | 0 | +10 | 0 | 0 |
| T35 DAS (fiber sensing) | 0 | 0 | +5 | 0 |
| T36 Quantum entanglement | +5 | +3 | +10 | +20 |
| T37 Neutrino beam | +15 | +1 | +10 | 0 |
| T38 Gravity-wave array | +20 | +1 | +5 | 0 |
| T39 Lunar laser comm | +10 | +5 | +5 | +8 |
| T40 OAM multiplexing | 0 | +15 | 0 | 0 |
| T41 Mars DTN backbone | +15 | +2 | +5 | –5 |
| | | | | |
| **Switching** | | | | |
| S1 Manual switchboard | +1 | 0 | –3 | –1 |
| S2 Magneto crank | 0 | 0 | 0 | –2 |
| S3 Common battery | +1 | 0 | +3 | 0 |
| S4 Strowger step-by-step | +3 | +1 | +2 | +3 |
| S5 Strowger trunk hunting | +2 | 0 | +1 | +1 |
| S6 Panel switch | +5 | 0 | +2 | 0 |
| S7 Multi-office trunking | +3 | 0 | +1 | +1 |
| S8 #1 Crossbar | +3 | 0 | +5 | +2 |
| S9 #4 Crossbar toll | +5 | 0 | +3 | +2 |
| S10 #5 Crossbar | +5 | +1 | +5 | +1 |
| S11 DDD | +3 | 0 | +2 | +5 |
| S12 XBT Crossbar Tandem | +3 | 0 | +2 | +1 |
| S13 Rotary switch | +2 | 0 | +1 | 0 |
| S14 IDDD | +3 | 0 | +2 | +3 |
| S15 #1ESS electronic | +3 | +2 | +8 | +3 |
| S16 #4ESS digital | +3 | +3 | +10 | +5 |
| S17 DACS | 0 | 0 | +5 | 0 |
| S18 #5ESS modular | +5 | +2 | +8 | +2 |
| S19 DMS-10/100 | +5 | +2 | +8 | +2 |
| S20 #1EAX | +2 | +1 | +5 | +1 |
| S21 RSM remote module | +8 | 0 | +3 | –1 |
| S22 MPLS | 0 | +3 | +8 | +5 |
| S23 Softswitch | 0 | +2 | +5 | +5 |
| S24 SIP | 0 | +2 | +3 | +3 |
| S25 Media Gateway | 0 | +2 | +3 | +2 |
| S26 SIGTRAN | 0 | 0 | +5 | 0 |
| S27 LTE EPC | 0 | +8 | +8 | +5 |
| S28 Diameter AAA | 0 | 0 | +3 | +1 |
| S29 SDN | 0 | +5 | +10 | +3 |
| S30 Network Slicing | 0 | +8 | +8 | +5 |
| S31 Service mesh | 0 | 0 | +5 | +2 |
| S32 P4 programmable | 0 | +3 | +3 | +3 |
| S33 Segment Routing | 0 | +2 | +5 | +3 |
| S34 5G UPF | 0 | +5 | +5 | +5 |
| S35 ZTP | 0 | 0 | +5 | 0 |
| S36 Quantum router | +5 | +3 | +10 | +15 |
| S37 Quantum memory | 0 | 0 | +8 | +5 |
| S38 Photonic chip switch | 0 | +10 | +5 | +5 |
| S39 IPN interplanetary | +10 | +2 | +5 | +3 |
| S40 Causal-structure routing | +5 | 0 | +5 | +15 |
| | | | | |
| **Access** | | | | |
| A1 Telephone set | +1 | 0 | 0 | 0 |
| A2 Party line | +5 | –2 | –2 | 0 |
| A3 Rotary dial | 0 | 0 | +1 | +2 |
| A4 Wall/Candlestick phone | 0 | 0 | +1 | 0 |
| A5 PBX | +2 | 0 | +2 | +1 |
| A6 Bridging bell | 0 | 0 | +2 | 0 |
| A7 Lineman's test set | 0 | 0 | +3 | 0 |
| A8 Touch-tone DTMF | 0 | +1 | +2 | +3 |
| A9 Desk phone (500/2500) | 0 | 0 | +2 | 0 |
| A10 MTS (car phone) | +3 | –2 | –3 | –3 |
| A11 IMTS | +3 | 0 | +2 | +1 |
| A12 Bellboy pager | +2 | –1 | 0 | 0 |
| A13 Business hunt group | +1 | 0 | +2 | +1 |
| A14 Centrex | +2 | +1 | +3 | +1 |
| A15 ISDN BRI | 0 | +5 | +3 | +2 |
| A16 ISDN PRI | 0 | +8 | +5 | +2 |
| A17 1G AMPS | +8 | –1 | –2 | –2 |
| A18 2G GSM | +10 | +3 | +5 | +3 |
| A19 Cable modem DOCSIS | +3 | +8 | –1 | 0 |
| A20 2.5G GPRS | +3 | +3 | +2 | –1 |
| A21 ADSL | +3 | +8 | +1 | 0 |
| A22 3G UMTS | +8 | +8 | +5 | +3 |
| A23 3.5G HSPA+ | +3 | +10 | +3 | +3 |
| A24 FTTH | +2 | +15 | +5 | +3 |
| A25 4G LTE | +10 | +15 | +8 | +8 |
| A26 4.5G LTE-Advanced | +3 | +10 | +5 | +5 |
| A27 VDSL2 + Vectoring | +2 | +8 | +2 | +2 |
| A28 WiMAX | +3 | +3 | –1 | +2 |
| A29 5G NR (FR1) | +8 | +15 | +8 | +10 |
| A30 5G NR (FR2 mmWave) | +3 | +20 | +8 | +12 |
| A31 5G-Advanced | +3 | +10 | +10 | +8 |
| A32 LEO satellite | +20 | +8 | +5 | +5 |
| A33 Direct-to-cell sat | +10 | +2 | +3 | +2 |
| A34 FWA (fixed wireless) | +5 | +8 | +3 | +3 |
| A35 Wi-Fi 6/6E | +3 | +8 | +2 | +3 |
| A36 Neural interface | +1 | +10 | +3 | +15 |
| A37 Holographic antenna | +3 | +20 | +5 | +8 |
| A38 Lunar base station | +15 | +5 | +8 | +5 |
| A39 Dyson-swarm relay | +25 | +8 | +10 | +5 |
| A40 Multi-planet SIM | +10 | 0 | +5 | +3 |
| | | | | |
| **Core Network** | | | | |
| C1 Morse telegraph | +2 | 0 | –1 | –3 |
| C2 Stock ticker | 0 | 0 | 0 | 0 |
| C3 Telex | +2 | 0 | +1 | 0 |
| C4 Numbering plan | +5 | 0 | +3 | +3 |
| C5 Trunk super group | 0 | +3 | +1 | 0 |
| C6 Manual toll board | +3 | 0 | –2 | –2 |
| C7 Toll cord test | 0 | 0 | +3 | 0 |
| C8 SF signaling | 0 | 0 | +2 | 0 |
| C9 MF signaling | 0 | 0 | +3 | +3 |
| C10 ANI | 0 | 0 | +3 | +2 |
| C11 ONI (manual) | 0 | 0 | –1 | –2 |
| C12 Routing plan (Class 1–5) | +5 | 0 | +5 | +3 |
| C13 DTL | +2 | 0 | +2 | +2 |
| C14 AMA billing | 0 | 0 | +2 | 0 |
| C15 SS7 | 0 | 0 | +10 | +5 |
| C16 IN (Intelligent Network) | +3 | 0 | +8 | +3 |
| C17 ARPANET / TCP/IP | 0 | +3 | +5 | +3 |
| C18 X.25 | 0 | +1 | +3 | 0 |
| C19 ATM | 0 | +5 | +5 | +3 |
| C20 DNS | 0 | +1 | +3 | +2 |
| C21 SCP | 0 | 0 | +5 | +2 |
| C22 Frame Relay | 0 | +2 | +3 | 0 |
| C23 ATM backbone | 0 | +5 | +5 | +2 |
| C24 BGP | 0 | +1 | +5 | +1 |
| C25 IP/MPLS backbone | 0 | +8 | +10 | +5 |
| C26 IMS | 0 | +3 | +8 | +5 |
| C27 GGSN/SGSN | 0 | +3 | +5 | +2 |
| C28 NFV | 0 | +3 | +5 | +3 |
| C29 MEC | 0 | +3 | +3 | +10 |
| C30 SDN optical (GMPLS) | 0 | +5 | +8 | +3 |
| C31 5GC SBA | 0 | +5 | +10 | +5 |
| C32 NWDAF | 0 | 0 | +8 | +3 |
| C33 AI RIC | 0 | +5 | +10 | +5 |
| C34 QKD | 0 | 0 | +10 | –1 |
| C35 ZSM | 0 | 0 | +15 | +3 |
| C36 Universal quantum internet | +3 | +8 | +15 | +15 |
| C37 Post-quantum crypto | 0 | 0 | +10 | –1 |
| C38 AI mesh protocol | +5 | +3 | +10 | +8 |
| C39 Interstellar bundling | +5 | +2 | +8 | –3 |
| C40 Inter-carrier ledger | +3 | 0 | +5 | 0 |

### Infrastructure → Quality Contribution

Each infrastructure asset contributes recurring quality points while it operates:

| Asset | Coverage | Speed | Reliability | Latency | Base Revenue Value |
|---|---|---|---|---|---|
| Copper Trunk | +5 | +2 | –1 | 0 | $0.01/s per circuit |
| Manual Switchboard | +2 | 0 | –3 | –1 | $0.05/s per 100 subs |
| Coaxial Backbone | +3 | +8 | +2 | 0 | $0.50/s per 600 circuits |
| Microwave Tower | +5 | +3 | +1 | +3 | $0.30/s per 480 circuits |
| Crossbar Exchange | +5 | +2 | +5 | +2 | $0.80/s per 10k subs |
| Submarine Cable (TAT-1) | +8 | +2 | +2 | –2 | $2.00/s per 36 circuits |
| Fiber Optic Cable | +3 | +15 | +3 | +5 | $5.00/s per 10 Gbps |
| Digital CO | +5 | +3 | +8 | +3 | $4.00/s per 100k subs |
| Cell Tower (1G/2G) | +8 | +2 | –1 | –1 | $1.00/s per 500 subs |
| Data Center | 0 | +5 | +5 | +3 | $2.00/s |
| FTTH OLT | +2 | +15 | +3 | +2 | $8.00/s per 32 subs |
| LTE eNodeB | +8 | +12 | +5 | +8 | $5.00/s per 500 subs |
| DWDM Terminal | 0 | +15 | +2 | 0 | $12.00/s per 40×10G |
| IP Core Router | 0 | +5 | +8 | +3 | $10.00/s per Tbps |
| 5G gNodeB (mmWave) | +3 | +20 | +5 | +12 | $15.00/s per user |
| LEO Satellite Terminal | +20 | +5 | +3 | +5 | $20.00/s global |
| Quantum Repeater | +3 | +3 | +8 | +15 | $100.00/s |
| Lunar Relay Station | +15 | +5 | +8 | +5 | $500.00/s |
| Neutrino Transceiver | +15 | +1 | +10 | 0 | $1,000.00/s |
| Dyson Swarm Node | +25 | +8 | +10 | +5 | $5,000.00/s |
| Interplanetary Gateway | +10 | +2 | +5 | +3 | $2,000.00/s |

---

## Complete Revenue Formula

```
For each region:
  infraValue = sum of (asset_count × base_revenue_per_asset × level_multiplier)
               only active-era assets contribute
  
  techMultiplier = 1.0 + (weightedQualityScore / 100)
  
  marketShare = f(yourQuality, rivalQuality)  — see rival-companies.md
  
  regionRevenue = infraValue × techMultiplier × marketShare

totalRevenue = sum of all regionRevenue
```

### Example
```
Region: Central Europe
  Infra: 10 Fiber cables (10 × $5 = $50/s), 2 Digital COs (2 × $4 = $8/s)
  Infra value: $58/s
  
  Quality: Coverage 60, Speed 80, Reliability 50, Latency 40
  Weighted (residential weights 30/30/20/20): 60×0.3 + 80×0.3 + 50×0.2 + 40×0.2 = 60
  Tech multiplier: 1.0 + 60/100 = 1.6×
  
  Market share: your quality 60 vs rival 72 → you have ~15% share
  
  Revenue: $58 × 1.6 × 0.15 = $13.92/s
```

---

## Era Transition — Prestige

When you trigger a Network Upgrade:

1. **Obsolete assets** stop contributing `infraValue` (copper in Era 3+, etc.)
2. **Prestige multiplier** ×1.5–4.0 multiplies all remaining `infraValue`
3. New-era infrastructure you build benefits from the multiplier too

| Transition | Obsolete | Multiplier |
|---|---|---|
| Era 1 → 2 | Copper, Manual Switchboard, Telegraph | ×1.5 |
| Era 2 → 3 | Coaxial, Crossbar, MTS Tower | ×2.0 |
| Era 3 → 4 | Legacy Fiber, 1G/2G towers, pre-#5ESS | ×2.5 |
| Era 4 → 5 | GPON (non-NG), LTE (non-LTE-A) | ×3.0 |
| Era 5 → 6 | 5G (non-Advanced), NFV (non-SBA) | ×4.0 |
