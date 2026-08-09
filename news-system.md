# News System — Historical & Industry Events

News events fire along the timeline to create a living world. Each event triggers at a specific in‑game year range, affects gameplay for a duration, and references real history. Events are **general** (not country‑specific) — drawn from global telecom, tech, and economic history.

## 5.1 Event Format

Each event:
```
[TYPE] Title — description
  Effect: gameplay impact
  Duration: how long it lasts (or instant)
  Trigger: ~year range
```

**TYPE icons:**
- 🏛️ **Regulation** — government / policy change
- 💥 **Crisis** — crash, scandal, disaster
- 🚀 **Breakthrough** — industry‑wide tech milestone
- 📈 **Boom** — market euphoria, growth
- 🏗️ **Infrastructure** — major build / cable / launch
- ⚔️ **Competition** — rivalry, M&A, new entrant
- 🔮 **Future** — speculative / futuristic events

## 5.2 News Trigger Mechanics — Two Layers with Priority

News has **two trigger layers**. Layer 1 fires immediately upon tech unlock. Layer 2 fires when the in‑game year matches. Layer 1 always fires **before** Layer 2.

```
[LAYER 1] Player completes Tech Node X
    → "Your company pioneers [technology]!"
    → Effect applies immediately

[LAYER 2] inGameYear == triggerYear
    → Historical news fires
    → Effect applies for Duration (or permanent)

Order: Layer 1 (tech unlock) → Layer 2 (year match) → Random pool
```

- **Layer 1 (tech‑triggered)** always fires at the exact moment the node completes — even if the player researched it ahead of the historical year
- **Layer 2 (year‑triggered)** skips if the player already unlocked that tech (no duplicate)
- **One‑time events** fire when the player first reaches that year
- **Persistent events** (wars, recessions) have a random chance to appear ±2 years of the trigger year
- Future events (Era 6) are **always** delayed until the player reaches that era

### Tech‑Triggered News Table (Layer 1)

When you complete a tech node, your company announces the achievement:

| Node | Company News Headline | Layer 1 Effect |
|---|---|---|
| **T1** | "Our first copper trunk line connects two buildings!" | +$50 instant revenue |
| **T4** | "We multiplex 4 calls on one wire — capacity soars!" | +10% capacity on all copper trunks |
| **T5** | "We string the first cross-country line!" | New region: long-distance unlocked |
| **T8** | "Our coaxial backbone carries 600 calls at once!" | +20% backbone capacity |
| **T10** | "We lay a cable across the ocean!" | Intercontinental region unlocked |
| **T15** | "Our first fiber optic line — light, not electricity!" | +50% capacity, future-proof |
| **T16** | "We digitize transport — 24 calls on 2 copper pairs!" | +10% digital revenue multiplier |
| **T18** | "Our network now heals itself — SONET ring live!" | -50% outage impact |
| **T19** | "Light amplified without electricity — EDFA deployed!" | +30% fiber range, -20% repeater cost |
| **T20** | "40 colors of light on one fiber — DWDM live!" | +20% backbone capacity |
| **T22** | "We push 40 Gbps per wavelength!" | +15% capacity per fiber |
| **T26** | "Fiber to the home — our first GPON subscriber!" | +$50 ARPU for fiber subs |
| **T29** | "1.6 Tbps on a single laser — new record!" | +10% capacity, industry recognition |
| **T31** | "Hollow-core fiber slashes latency to near light speed!" | -30% latency penalty in all regions |
| **T36** | "We entangle two particles 1,000 km apart!" | Interstellar research path opens |
| **S1** | "Our first switchboard — operators ready!" | +100 subscriber capacity |
| **S4** | "We install the first automatic switch!" | -50% labor cost for local calls |
| **S8** | "Crossbar switch live — 1/10th the moving parts!" | +50% switching capacity, -30% maintenance |
| **S10** | "#5 Crossbar deployed — the workhorse of our network!" | +20% subscriber capacity per exchange |
| **S11** | "Customers can now dial anywhere — DDD is live!" | +15% long-distance revenue |
| **S15** | "Software-defined switching — our #1ESS is live!" | +30% flexibility, OAM cost -20% |
| **S16** | "All-digital toll switch handles 100,000 trunks!" | +50% toll capacity |
| **S18** | "Modular #5ESS — scales from village to metropolis!" | -15% switching cost per sub |
| **S22** | "MPLS network live — traffic engineering now possible!" | +10% core efficiency |
| **S23** | "Softswitch replaces circuit switch — VoIP ready!" | -20% voice opex |
| **S27** | "All-IP core for LTE — EPC deployed!" | +20% data revenue |
| **S29** | "Our network is now software-defined — SDN controller live!" | -30% provisioning time |
| **S30** | "Network slicing live — dedicated lanes for every service!" | +$100 per enterprise slice |
| **S33** | "Segment routing simplifies our core — RSVP retired!" | -15% core opex |
| **S36** | "Quantum router swaps entanglement — first quantum call!" | Quantum network revenue unlocked |
| **A3** | "Rotary dial phones shipped to every subscriber!" | +10% call completion rate |
| **A8** | "Touch-tone — push a button, not a wheel!" | +15% call setup speed |
| **A10** | "Our first mobile phone service — car phones!" | +$200/mo per mobile user (niche) |
| **A15** | "ISDN BRI — 128 kbps to every home!" | +$30/mo ARPU per business line |
| **A17** | "Our cellular network goes live — 1G!" | +500 mobile subscribers instantly |
| **A18** | "GSM network live — digital, encrypted, roaming-ready!" | +20% mobile margin, roaming revenue |
| **A20** | "Always-on mobile data — GPRS launched!" | +$5/mo per mobile sub |
| **A22** | "3G network — mobile video is here!" | +$10/mo ARPU boost |
| **A25** | "4G LTE live — 150 Mbps to your phone!" | +$15/mo ARPU, -20% churn |
| **A27** | "100 Mbps over copper — VDSL2 vectoring deployed!" | +10% copper lifespan |
| **A29** | "5G NR — 1 Gbps wireless!" | +$20/mo ARPU, new enterprise revenue |
| **A30** | "5G mmWave — 4 Gbps at 28 GHz!" | +$30/mo ARPU, dense urban capacity |
| **A32** | "We connect to the LEO constellation — global coverage!" | Global region unlocked |
| **A36** | "Neural interface approved — thought-to-network!" | +$500/mo ARPU (premium) |
| **C4** | "Our numbering plan — every subscriber has a unique code!" | Routing efficiency +20% |
| **C9** | "Multi-frequency signaling — calls set up in seconds!" | -50% call setup time |
| **C15** | "SS7 network live — intelligent signaling!" | +10% network intelligence, IN services |
| **C17** | "We connect to the ARPANET — packet switching arrives!" | +5% data revenue, internet foundation |
| **C24** | "BGP routing — we become an ISP!" | +5% interconnection revenue |
| **C25** | "IP/MPLS backbone live — Frame Relay retired!" | -15% transport opex |
| **C26** | "IMS core live — voice, video, messaging on one platform!" | +10% service revenue |
| **C28** | "NFV — network functions virtualized on COTS servers!" | -25% opex, +50% deployment speed |
| **C31** | "5G core SBA — cloud-native, stateless, containerized!" | +20% automation, -30% core opex |
| **C33** | "AI RIC optimizes our RAN in real-time!" | +10% capacity from same spectrum |
| **C36** | "Quantum internet operational — unhackable links!" | +$100K/mo per quantum link |

## 5.3 Era 1: Analog Dawn (1880–1920)

| Year | Type | Event | Effect |
|---|---|---|---|
| 1880 | 🚀 | **First telephone directory published.** 30,000 people now own telephones. | +10% subscriber growth for 30s |
| 1881 | 🏗️ | **First telephone line between two cities** — Boston to Providence. | Unlock region expansion (first time) |
| 1884 | 🚀 | **PBX invented** — businesses can now have internal phone networks. | Unlock Business tier |
| 1887 | ⚔️ | **Patent wars erupt** — Bell vs. competitors. | RP cost +20% for 60s |
| 1891 | 🚀 | **Strowger patents the automatic telephone switch.** | S4 research cost –15% |
| 1892 | 🏗️ | **First automatic exchange opens** — La Porte, Indiana. | Unlock S4 faster if researching |
| 1895 | 📈 | **Telephone adoption boom** — 250,000 phones in use. | +15% subscriber growth for 45s |
| 1900 | 💥 | **Great Fire / natural disaster** destroys telephone infrastructure. | –20% capacity in 2 regions |
| 1901 | 🚀 | **Marconi transmits first transatlantic wireless signal.** | +10% RP generation |
| 1904 | 🏛️ | **International Telegraph Convention revised** — first global standards. | Unlock C4 at –20% cost |
| 1906 | 💥 | **Earthquake** — telegraph/phone lines destroyed. | Revenue –50% for 30s |
| 1910 | 🏗️ | **First transcontinental telephone line proposed.** | T5 research accelerated |
| 1914 | ⚔️ | **World War I begins** — governments take control of networks. | Revenue +20%, RP –10% |
| 1915 | 🚀 | **First transcontinental phone call** — NY to San Francisco. | +10% reputation, new region |
| 1918 | 🏛️ | **Post‑war reconstruction** — governments invest in networks. | Infra cost –15% for 60s |
| 1920 | 📈 | **Radio broadcasting begins** — commercial stations go live. | C3 gets +RP boost |

## 5.4 Era 2: Electromechanical & Radio (1930–1960)

| Year | Type | Event | Effect |
|---|---|---|---|
| 1927 | 🚀 | **First commercial radiotelephone service** — London to New York. | Unlock international ambition |
| 1929 | 💥 | **Great Depression begins** — telecom investment collapses. | Revenue –30% for 120s |
| 1933 | 🏛️ | **Spectrum licensing introduced** — communications regulation established. | First auction event |
| 1934 | 🏗️ | **Coaxial cable demonstrated** — first 240‑channel system. | T8 research cost –20% |
| 1938 | 🚀 | **#1 Crossbar switch installed** in Brooklyn. | S8 unlock –15% cost |
| 1939 | ⚔️ | **World War II begins** — massive military demand. | Revenue +30%, RP +20% |
| 1941 | 🏗️ | **L‑carrier coaxial system operational** — 600 circuits. | T8 unlocked |
| 1945 | 🚀 | **ENIAC computer unveiled** — digital computing begins. | +5% RP permanently |
| 1946 | 🚀 | **First mobile telephone service (MTS)** in St. Louis. | A10 unlocked |
| 1947 | 🚀 | **Transistor invented** at Bell Labs. | +15% RP permanently |
| 1948 | 🚀 | **Shannon publishes "A Mathematical Theory of Communication".** | RP +10% permanently |
| 1950 | 📈 | **Suburban boom** — new housing needs telephone lines. | +10% sub growth for 90s |
| 1951 | 🚀 | **Direct Distance Dialing (DDD)** begins. | S11 unlock event |
| 1953 | 🏛️ | **Hush‑a‑Phone ruling** — FCC allows non‑Bell equipment. | +5% RP |
| 1956 | 🏗️ | **TAT‑1 submarine cable operational** — 36 circuits across Atlantic. | T10 unlocked |
| 1956 | 🚀 | **SONY sells first commercial transistor radio.** | Consumer electronics begins |
| 1957 | 🚀 | **Sputnik launched** — space age begins. | Satellite research possible |
| 1958 | 🏗️ | **First communications satellite (Score)** — broadcasts Eisenhower's voice. | Previews satellite era |
| 1960 | 🚀 | **Laser demonstrated** (Theodore Maiman). | Future fiber optic foundation |

## 5.5 Era 3: Digital & Satellite (1970–1990)

| Year | Type | Event | Effect |
|---|---|---|---|
| 1962 | 🚀 | **Telstar satellite launched** — first live TV across Atlantic. | +10% reputation, satellite confidence |
| 1963 | 🚀 | **Touch‑tone introduced** in Carnegie & Greensburg, PA. | A8 unlock faster |
| 1965 | 🚀 | **#1ESS goes live** — first electronic switching. | S15 unlocked |
| 1968 | 🏛️ | **Carterfone decision** — FCC allows non‑Bell devices. | Innovation surge |
| 1969 | 🚀 | **ARPANET first nodes** — UCLA, Stanford, UCSB, Utah. | C17 foundation event |
| 1970 | 🚀 | **Corning produces first low‑loss fiber optic cable.** | T15 research starts |
| 1971 | 🚀 | **Intel 4004 microprocessor** — first CPU on a chip. | RP +5% permanently |
| 1972 | 🚀 | **Email invented** (Ray Tomlinson). | Internet's killer app born |
| 1973 | 🚀 | **Motorola DynaTAC — first handheld mobile phone call.** | Mobile future begins |
| 1975 | 🚀 | **SS7 protocol defined** — out‑of‑band signaling. | C15 foundation |
| 1976 | 🏗️ | **#4ESS digital toll switch** — 100,000 trunks. | S16 unlocked |
| 1977 | 🏗️ | **First fiber optic telephone installation** — Chicago. | T15 proven in real network |
| 1978 | 🏛️ | **ITU allocates spectrum for cellular** (800/900 MHz). | Mobile spectrum available |
| 1979 | 💥 | **Oil shock / recession** — telecom CapEx frozen. | Build cost +25% for 60s |
| 1981 | 🚀 | **IBM PC launched** — personal computing mainstream. | Data connectivity demand surges |
| 1982 | ⚔️ | **Bell System breakup announced** — AT&T to divest. | +20% market opportunity |
| 1983 | 🚀 | **First commercial 1G cellular (AMPS)** in Chicago. | A17 unlocked |
| 1984 | 🏛️ | **Bell System broken up** — 7 Baby Bells created. | Competition: revenue –10%, growth +15% |
| 1985 | 🚀 | **First .com domain registered** — symbolics.com. | Internet commercial potential |
| 1987 | 🚀 | **GSM standard agreed** — 13 countries sign MoU. | A18 foundation |
| 1988 | 🏛️ | **First spectrum auction** — New Zealand experiment. | Auction mechanic unlocked |
| 1988 | 🏗️ | **TAT‑8 fiber cable operational** — 280 Mbps. | T17 unlocked |
| 1989 | 🚀 | **World Wide Web invented** (Tim Berners‑Lee). | Internet revolution begins |

## 5.6 Era 4: Broadband & IP (2000–2015)

| Year | Type | Event | Effect |
|---|---|---|---|
| 1991 | 🚀 | **First GSM call** — Nokia / Radiolinja in Finland. | A18 unlocked |
| 1992 | 🚀 | **First SMS sent** — "Merry Christmas" | Mobile messaging begins |
| 1993 | 🚀 | **Mosaic browser** — first graphical web browser. | Internet goes mainstream |
| 1994 | 🏛️ | **FCC begins PCS spectrum auctions** — $7.7B raised. | Auction mechanic for all |
| 1995 | 📈 | **Internet goes commercial** — Netscape IPO, Amazon, eBay. | +20% subscriber growth |
| 1995 | 🏛️ | **WTO Telecom Agreement** — 69 countries open markets. | New regions cost –20% |
| 1996 | 🏛️ | **Telecommunications Act** — deregulation, cable/telco cross‑entry. | New competition + new opportunities |
| 1997 | 🚀 | **Wi‑Fi (802.11) standard approved.** | Future wireless LAN revolution |
| 1998 | 📈 | **Internet bubble inflates** — massive fiber investment. | Infra cost –30% (warning signs) |
| 1998 | 🚀 | **Iridium satellite phone network launches** — 66 satellites. | First global mobile coverage |
| 1999 | 🚀 | **MPLS standardized** — IP converges with telecom. | S22 unlocked |
| 1999 | ⚔️ | **WorldCom buys MCI** for $37B. | Consolidation wave |
| 2000 | 💥 | **Dot‑com bubble bursts** — NASDAQ crashes. | Revenue –15% |
| 2000 | 💥 | **3G spectrum auctions (Europe)** — £22.5B in UK alone. | Spectrum +50% for 60s |
| 2001 | 💥 | **Telecoms crash** — 60+ bankruptcies, fiber overcapacity. | Revenue –20% for 90s |
| 2001 | 💥 | **WorldCom fraud** — $11B scandal, largest bankruptcy. | Reputation –15% for 60s |
| 2001 | 💥 | **Nortel collapses** — worth $300B to near zero. | Build cost –20% for 30s |
| 2002 | 🏛️ | **Sarbanes‑Oxley Act** — tighter financial controls. | Compliance +5% permanently |
| 2003 | 🚀 | **Skype launched** — VoIP goes mainstream. | Voice ARPU –5% |
| 2004 | 🚀 | **3G commercial launches (UMTS).** | A22 unlocked |
| 2005 | 🚀 | **YouTube launched** — user‑generated video. | Bandwidth demand explodes |
| 2005 | 📈 | **Broadband penetration passes 50%** in developed markets. | +10% sub growth |
| 2006 | 📈 | **AWS launches** — cloud computing begins. | Unlock DC/cloud revenue stream |
| 2007 | 🚀 | **iPhone launched** — mobile internet becomes real. | A25 research +20% boost |
| 2007 | 💥 | **Subprime crisis begins** — financial sector freezes. | Debt unavailable for 60s |
| 2008 | 💥 | **Global Financial Crisis** — telecom hit. | Revenue –15% for 120s |
| 2009 | 🚀 | **First commercial LTE** (TeliaSonera, Stockholm/Oslo). | A25 unlocked |
| 2009 | 🏛️ | **EU roaming regulation** — mobile roaming price caps. | Roaming revenue –10% |
| 2010 | 📈 | **Smartphone penetration hits 20%** — mobile data doubles yearly. | Bandwidth demand +20% annually |
| 2011 | 🚀 | **iPhone overtakes Nokia** — mobile data dominates. | Voice becomes secondary |
| 2012 | 🚀 | **LTE becomes mainstream** — 100+ networks. | A25 costs –20% |
| 2013 | 🚀 | **Google Fiber launches** — 1 Gbps to home. | FTTH costs –10% |
| 2014 | 💥 | **Heartbleed bug** — internet security crisis. | Security costs +5% |
| 2015 | 🏛️ | **Net neutrality rules strengthened** (FCC Title II). | Zero‑rating restricted |
| 2015 | 📈 | **AWS‑3 spectrum auction (US)** — $81B raised. | Auctions more expensive |

## 5.7 Era 5: Autonomous & Software-Defined (2015–2030)

| Year | Type | Event | Effect |
|---|---|---|---|
| 2015 | 🏛️ | **EU eliminates roaming charges** (from 2017). | Roaming revenue gone, satisfaction +10% |
| 2016 | 💥 | **Net neutrality repeal (US)** — FCC reverses Title II. | Zero‑rating allowed, +10% revenue |
| 2017 | 🚀 | **First 5G NR specification (3GPP R15).** | A29 research path opens |
| 2017 | ⚔️ | **T‑Mobile / Sprint merger proposed.** | Consolidation wave |
| 2018 | 📈 | **Starlink first test satellites launched.** | A32 becomes real |
| 2018 | 🚀 | **First 5G commercial launches.** | 5G era begins |
| 2019 | 🏛️ | **Huawei ban** — US restricts Chinese equipment. | Equipment cost +15% |
| 2019 | 🚀 | **Starlink operational beta.** | A32 unlocked |
| 2020 | 💥 | **COVID‑19 pandemic** — WFH drives bandwidth demand. | +30% sub growth, NOC stressed |
| 2020 | 📈 | **5G SA launches** — network slicing real. | S30 unlocked |
| 2021 | 💥 | **Global chip shortage** — network equipment delayed. | Build time +30% for 90s |
| 2021 | 🏛️ | **O‑RAN Alliance grows** — open hardware ecosystem. | Equipment cost –15% |
| 2022 | 💥 | **Russia‑Ukraine war** — Starlink critical connectivity. | Satellite revenue +15% |
| 2022 | 💥 | **Energy crisis** — power costs +30%. | Opex +10% for 60s |
| 2023 | 🚀 | **Direct‑to‑phone satellite demo.** | A33 unlocked |
| 2023 | 📈 | **AI explosion** — ChatGPT 100M users in 2 months. | Edge compute demand surges |
| 2024 | 🚀 | **5G‑Advanced (3GPP R18)** — AI/ML in RAN. | A31 unlocked |
| 2024 | 🏛️ | **EU Cyber Resilience Act.** | Compliance +3% |
| 2025 | 📈 | **6G vision articulated** — ITU IMT‑2030. | Future era preview |
| 2025 | 🚀 | **LEO mega‑constellations reach global coverage.** | A32 fully operational |
| 2026 | 💥 | **AI‑generated fraud / deepfake scams.** | Security opex +5% |
| 2026 | 🏗️ | **Quantum internet demo** — 3 nodes entangled. | C34, T36 precursor |
| 2027 | 🚀 | **6G initial spec (3GPP R22).** | 6G research path opens |
| 2028 | 💥 | **Massive solar storm** — satellite disruption. | LEO capacity –10% |
| 2029 | 🚀 | **Hollow‑core fiber deployed at scale.** | T31 commercially available |
| 2030 | 📈 | **6G commercial launch** — 1 Tbps target. | Era 6 begins |

## 5.8 Era 6: Interspace & Beyond (2050+)

| Year | Type | Event | Effect |
|---|---|---|---|
| 2032 | 🏗️ | **First permanent lunar base communications hub.** | A38 unlocked, Lunar region opens |
| 2035 | 🚀 | **Quantum entanglement repeater at 1,000 km.** | T36 breakthrough |
| 2038 | 💥 | **LEO orbit congestion crisis** — collision risk. | Satellite opex +10% |
| 2040 | 🏛️ | **Interplanetary spectrum allocated.** | S39 foundation |
| 2042 | 🚀 | **Neutrino communication test** — signal through 1 km rock. | T37 proof of concept |
| 2045 | 💥 | **AI‑managed network resolves 99.9% of faults.** | NOC staffing –80% |
| 2048 | 🏗️ | **Interplanetary internet backbone** — Earth↔Mars. | T41 unlocked |
| 2050 | 🚀 | **First commercial quantum internet service.** | C36 unlocked |
| 2055 | 💥 | **Dyson‑swarm prototype** — 1,000 relay statites. | A39 unlocked |
| 2060 | 🚀 | **Biological neural interface approved.** | A36 unlocked |
| 2070 | 🏛️ | **Interstellar communications treaty** — ITU renamed. | Universal standard |
| 2080 | 🔮 | **Gravity‑wave communication demonstrated.** | T38 unlocked |
| 2090 | 🔮 | **Multi‑planet SIM roaming.** | A40 unlocked |
| 2100 | 🔮 | **Causal‑structure routing operational.** | S40 unlocked |

## 5.9 Random Events Pool (non‑year specific)

| Era | Event | Effect |
|---|---|---|
| 1–2 | **Lightning strike damages exchange.** | Repair cost $500 |
| 1–2 | **Operator strike** — switchboard staff walk out. | Revenue –20% for 15s |
| 2–3 | **Microwave interference** — rain fade. | Capacity –20% for 10s |
| 3–4 | **Backhoe cuts fiber.** | –50% capacity in 1 region for 30s |
| 3–4 | **Computer virus hits SS7 network.** | New connections blocked for 15s |
| 4–5 | **DDoS attack on core routers.** | Data revenue –30% for 20s |
| 4–5 | **Fierce price war** — competitor drops rates 30%. | Churn +3% for 45s |
| 5 | **Drone hits cell tower.** | Repair +50%, 30s outage |
| 5–6 | **Solar flare disrupts satellite service.** | LEO capacity –40% for 60s |
| 5–6 | **Quantum‑hack attempt detected.** | Security opex +10% for 30s |

## 5.10 News UI

Events appear as a scrolling ticker at the top of the screen + a **NEWS** button that opens a log.

Tech unlocks appear with a distinct **company achievement** style:
```
┌──────────────────────────────────────────────────┐
│ 🏆 YOUR COMPANY  │ 1963: #1ESS Deployed!         │
│                  │ Software-defined switching.    │
│                  │ +30% flexibility, -20% OAM     │
└──────────────────────────────────────────────────┘
```

Historical events appear as:
```
┌─────────────────────────────────────────────────┐
│ 📰 NEWS  │ 1982: Bell System breakup announced! │
│           │ AT&T to divest local companies.     │
│           │ Effect: new long‑distance markets.  │
└─────────────────────────────────────────────────┘
```

The news log preserves all past events with the year they fired, so players can scroll through the history of their playthrough.

### Cross‑System Integration

| News Event Type | Affects |
|---|---|
| 📈 Booms / 💥 Crashes | Market Investment — stock price, debt availability |
| 🚀 Breakthroughs | Tech Tree — research cost or RP boost |
| 🏗️ Infrastructure | Infrastructure — build cost, new regions |
| 🏛️ Regulation | Company Management — compliance, new mechanics |
| ⚔️ Competition | All — price pressure, growth opportunity |
| 🔮 Future | RP boost toward that branch |
