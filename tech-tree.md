# Tech Tree — Technology Development

## Overview
4 parallel branches, 6 eras, ≈161 unlockable nodes. Most nodes require **multiple prerequisites** from different branches — representing real technical dependencies where advances in one domain enabled progress in another.

### Branch Notation
- **T** = Transmission, **S** = Switching, **A** = Access, **C** = Core Network
- Each node: `[Branch][#]` e.g. T1, S5, A12, C3
- Unlock conditions: `req: T1 + S2` means both T1 and S2 must be researched

### Era Structure
Each era has a **Gateway Tech** — a major cross-branch milestone that triggers a "Network Upgrade" prestige, giving a permanent multiplier and unlocking the next era's nodes for research.

### Research Pacing
- RP production starts at 5 RP/s and can grow through company investment and productive infrastructure.
- Each era has an RP/s ceiling: **8, 12, 18, 27, 40** for Eras 1–5 in the current implementation.
- Node costs preserve their RP weights but are scaled by era so the **fastest legal route takes about 7 simulated hours at the RP cap**.
- At most 30 minutes of the next era's capped RP production carries across an era transition, keeping the fastest post-Era-1 progression above **6.5 hours per era** without a timer gate.

---

## Era 1: Analog Dawn (1880–1920)

### TRANSMISSION

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| T1 | Twisted-pair copper trunk | 1881 | — | 1 voice circuit per pair. Basic connectivity. |
| T2 | Pupin loading coil | 1900 | T1 | Inductive coils every 1.8 km. Range ×1.5 on copper. |
| T3 | Phantom circuit | 1902 | T1 + T2 | Superimpose 3rd circuit on 2 pairs. +50% capacity on existing copper. |
| T4 | Open-wire FDM (frequency multiplex) | 1918 | T3 | 4 voice channels on 1 pair. First spectral efficiency. |
| T5 | First transcontinental line (NY→SF) | 1915 | T1 + T2 | Open-wire across USA. Enables national network. |
| T6 | Underground cable conduit | 1887 | T1 | Urban trenching. Protects wires from weather. |
| T7 | Duplex telegraph | 1872 | — | Send+receive on same wire simultaneously. Doubles telegram throughput. |

**Era 1 Gateway:** T4 (Open-wire FDM) — unlocks trunk capacity sufficient for next era

### SWITCHING

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| S1 | Manual cord switchboard | 1878 | T1 | Operator patches calls via cords. 100–200 lines. |
| S2 | Magneto crank signaling | 1878 | S1 | Hand-crank AC to alert operator. No local battery needed. |
| S3 | Common battery exchange | 1894 | S2 | Central battery at exchange. Longer loops, reliable signaling. |
| S4 | Strowger Step-by-Step switch | 1892 | S3 | Rotary dial pulses drive vertical/horizontal selector. First automatic switch. |
| S5 | Strowger trunk hunting | 1902 | S4 + T3 | Cascade Strowger banks. Scales to 10,000 lines. |
| S6 | Panel switch (Bell System) | 1915 | S4 + T1 | 100,000+ line capacity for big cities. Flat architecture. |
| S7 | Multi-office trunking (prefix codes) | 1904 | S5 | Each exchange gets 3-digit prefix. Inter-office routing. |

**Era 1 Gateway:** S4 (Strowger Step-by-Step) — automatic dialing, mass adoption begins

### ACCESS

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| A1 | Telephone set (carbon mic) | 1878 | S1 | First commercial phone. Carbon microphone amplifies signal. |
| A2 | Party line (shared line) | 1881 | T1 + A1 | 2–8 subscribers share 1 copper pair. Lower cost/sub. |
| A3 | Rotary dial (Strowger-compatible) | 1896 | S4 | Pulse dialing. Finger wheel sends pulses to step the switch. |
| A4 | Wall/Candlestick phone | 1890 | A1 | Standardized form factors. Rugged, reliable. |
| A5 | PBX — Private Branch Exchange | 1884 | S1 | Business internal switchboard. Share trunk lines among offices. |
| A6 | Bridging bell (ringer) | 1884 | A1 | Loud mechanical bell for long-loop signaling. |
| A7 | Lineman's test set | 1886 | A1 | Portable phone for installers. Enables maintenance reliability. |

**Era 1 Gateway:** A3 (Rotary dial) — enables mass automatic calling via Strowger

### CORE NETWORK

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| C1 | Point-to-point Morse telegraph | 1844 | — | First electrical telecom. Binary relay. Railroad dispatch. |
| C2 | Stock telegraph ticker (Edison) | 1867 | C1 | High-volume burst messages on shared wire. |
| C3 | Telex (teleprinter network) | 1910 | C1 + S1 | Typewriter message exchange. Store-and-forward. |
| C4 | Operator numbering plan (NPA-NXX) | 1904 | S7 | 3-digit office code + 4-digit subscriber. Foundation of all routing. |
| C5 | Trunk super group (12‑channel) | 1918 | T4 | Group FDM channels for routing efficiency. |
| C6 | Manual toll board | 1885 | S1 | Separates long-distance operators. |
| C7 | Toll cord circuit (built-in test) | 1892 | C6 | Operator can test trunk quality before connecting. |

**Era 1 Gateway:** C4 (Numbering plan) — foundation for Direct Distance Dialing

---

## Era 2: Electromechanical & Radio (1930–1960)

### TRANSMISSION

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| T8 | L-carrier coaxial cable | 1941 | T4 + T5 + S7 | 600 voice circuits on 1 coax pair. High-capacity backbone. |
| T9 | TD-2 microwave relay | 1950 | T5 + T8 | 4 GHz, 30‑50 km hops, 480 circuits/hop. |
| T10 | TAT-1 transatlantic submarine | 1956 | T8 + S9 | 36 voice circuits across Atlantic. Vacuum-tube repeaters every 70 km. |
| T11 | N-carrier short‑haul FDM | 1952 | T4 | 12 channels on 2 pairs. Cheap rural interoffice trunking. |
| T12 | Troposcatter (over‑the‑horizon) | 1955 | T9 | 300 km hop, 120 circuits. Military + remote area. |
| T13 | TASI (Time Assignment Speech Interpolation) | 1960 | T10 | Detect pauses in speech, fill gaps → capacity ×2.1 on submarine cables. |
| T14 | Submarine cable rigid repeater | 1950 | T8 | Deep-sea pressure-rated vacuum-tube amplifier. Enables TAT-1. |

**Era 2 Gateway:** T8 (L‑carrier coaxial) → nationwide backbone capacity

### SWITCHING

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| S8 | #1 Crossbar (Bell Labs) | 1938 | S5 + T6 | Electromechanical matrix. 1/10th moving parts. 10,000 lines. |
| S9 | #4 Crossbar toll tandem | 1943 | S8 + C4 | Long-distance-only switch. 50,000 trunks. |
| S10 | #5 Crossbar (local office) | 1950 | S8 | 20,000 lines. Ubiquitous in Bell System. |
| S11 | DDD — Direct Distance Dialing | 1951 | S10 + C4 + C7 | Customer dials long-distance without operator. |
| S12 | XBT — Crossbar Tandem | 1941 | S8 + C5 | Regional trunk concentration. 1,000 trunk capacity. |
| S13 | Rotary switch (WE machine) | 1938 | S5 | Urban multi-exchange switching. |
| S14 | IDDD — International DDD | 1963 | S11 + T10 | 10-digit international dialing. Modified #5 Crossbar. |

**Era 2 Gateway:** S10 (#5 Crossbar) → scale nationwide

### ACCESS

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| A8 | Touch-tone DTMF keypad | 1963 | S10 + A3 | Push-button. 4×3 matrix. Faster call setup. |
| A9 | Desk phone (500/2500 set) | 1950 | A4 | Universal design. Standardized everything. |
| A10 | MTS — Mobile Telephone Service | 1946 | T8 | Car phone. Manual operator. 3 channels. 0G. |
| A11 | IMTS — Improved MTS | 1964 | A10 + S8 | Automatic, full-duplex. 11 channels. |
| A12 | Bellboy pager (AT&T) | 1962 | S10 | Tone-only, 1-way pager. 15 km range. |
| A13 | Business line hunt group | 1951 | S8 | Auto-route to next available line. |
| A14 | Centrex (central office PBX) | 1963 | S10 + A5 | PBX at central office. |

**Era 2 Gateway:** A8 (Touch-tone) → subscriber convenience boom

### CORE NETWORK

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| C8 | SF (Single‑Frequency) in‑band signaling | 1948 | T8 | 2600 Hz tone for trunk supervision. |
| C9 | MF (Multi‑Frequency) signaling | 1950 | C8 + S9 | KP+ST+toll digits. Faster call setup. |
| C10 | ANI — Automatic Number Identification | 1952 | C9 + S11 | Identify calling party. Enables automated billing. |
| C11 | ONI — Operator Number Identification | 1944 | C6 | Manual backup for ANI. |
| C12 | Traffic routing plan (Class 1–5) | 1946 | S9 + C4 | Hierarchical switch levels. |
| C13 | DTL — Direct Trunk Line | 1954 | C12 | High-usage trunk bypassing intermediate switches. |
| C14 | AMA — Automatic Message Accounting | 1952 | C10 + S11 | Punched tape billing for DDD calls. |

**Era 2 Gateway:** C9 (MF signaling) → automated nationwide call routing

---

## Era 3: Digital & Satellite (1970–1990)

### TRANSMISSION

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| T15 | Single-mode fiber optic (Corning) | 1970 | T8 + C17 | 20 dB/km (later 0.2 dB/km). 40 Gbps theoretical. |
| T16 | T‑carrier (T1, DS1) | 1962 | S15 | 1.544 Mbps, 24 voice channels on 2 copper pairs. |
| T17 | TAT‑8 fiber submarine cable | 1988 | T15 + T18 | 280 Mbps across Atlantic. 40,000 simultaneous calls. |
| T18 | SONET (OC‑3/12/48) | 1988 | T15 + S15 | Synchronous frame. Self-healing rings. OC‑48 = 2.5 Gbps. |
| T19 | EDFA optical amplifier | 1992 | T18 | All‑optical amplification. Undersea game‑changer. |
| T20 | DWDM (dense wavelength division) | 1995 | T15 + T18 | 40+ λ × 10 Gbps = 400 Gbps per fiber. |
| T21 | HFC — Hybrid Fiber‑Coax | 1989 | T15 + A19 | Fiber to node + coax to home. 2000 homes/node. |

**Era 3 Gateway:** T15 (Fiber optic) → digital backbone, analog dominance ends

### SWITCHING

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| S15 | #1ESS (Electronic Switching System) | 1965 | S10 + C9 | Stored‑program control. 65,000 lines, 16,000 trunks. |
| S16 | #4ESS (Digital Toll Switch) | 1976 | S15 + C15 | Time‑division digital. 100,000 trunks. |
| S17 | DACS — Digital Access Cross‑Connect | 1981 | S15 | DS0‑level grooming. Remote provisioning. |
| S18 | #5ESS (Distributed Modular) | 1982 | S15 + T16 | Modular: 100–100,000 lines. |
| S19 | DMS‑10 / DMS‑100 (Nortel) | 1977/79 | S15 | DMS‑10: rural. DMS‑100: metro. |
| S20 | #1EAX (GTE Automatic Electric) | 1976 | S15 | Analog matrix, digital control. |
| S21 | RSM — Remote Switching Module | 1982 | S18 + T15 | Remote cabinet via fiber. 200–2,000 rural lines. |

**Era 3 Gateway:** S15 (#1ESS) → software‑controlled switching

### ACCESS

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| A15 | ISDN BRI (Basic Rate) | 1988 | S18 + A8 | 2B + D = 128 kbps. Digital voice + data. |
| A16 | ISDN PRI (Primary Rate) | 1988 | S16 + A15 | 23B + D = 1.544 Mbps. Business trunk. |
| A17 | 1G — AMPS | 1983 | A11 + T15 | Analog cellular. 800 MHz. No encryption. |
| A18 | 2G — GSM | 1991 | A17 + C16 | Digital voice, TDMA, SMS. SIM card. |
| A19 | Cable modem DOCSIS 1.0 | 1997 | A17 + T21 | 38/10 Mbps on coax. |
| A20 | 2.5G — GPRS | 2000 | A18 + C17 | Packet data over GSM. 114 kbps. |
| A21 | ADSL | 1988 | S18 + T15 | 8/1 Mbps on copper. 3.5 km loop limit. |

**Era 3 Gateway:** A18 (GSM) → digital mobile everywhere

### CORE NETWORK

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| C15 | SS7 — Signaling System 7 | 1975 | C9 + S15 | Out‑of‑band signaling. ISUP, TCAP, MAP. |
| C16 | IN — Intelligent Network | 1980 | C15 + S18 | SCP databases for 800#, LNP. |
| C17 | ARPANET / TCP/IP | 1969/81 | T16 + S15 | Packet switching. IPv4, TCP. Internet foundation. |
| C18 | X.25 packet switching | 1976 | C17 | First public data network. 64 kbps. |
| C19 | ATM — Asynchronous Transfer Mode | 1993 | T18 + C17 | 53‑byte cells. QoS guarantees. 155/622 Mbps. |
| C20 | DNS — Domain Name System | 1983 | C17 | Name → IP mapping. |
| C21 | SCP — Service Control Point | 1981 | C15 + S18 | Centralized databases for routing. |

**Era 3 Gateway:** C15 (SS7) + C17 (TCP/IP) → intelligent network + internet

---

## Era 4: Broadband & IP (2000–2015)

### TRANSMISSION

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| T22 | 40 Gbps DWDM | 2005 | T20 + C25 | 100 × 10G. C+L band. 250+ wavelengths. |
| T23 | 100G coherent optics (DP‑QPSK) | 2010 | T22 | Coherent receiver with DSP. 100G per λ. |
| T24 | TPE transpacific cable | 2008 | T22 + A25 | 5.12 Tbps Asia→US. 10,000 km direct route. |
| T25 | 400G / 800G (16QAM, shaping) | 2020 | T23 | 400–800G per λ. Probabilistic shaping. |
| T26 | GPON (2.5G/1.25G) | 2004 | T15 + A21 | Fiber to home. 1:32 passive splitter. |
| T27 | NG‑PON2 (TWDM‑PON) | 2015 | T26 | 4–8 λ × 10G = 40 Gbps aggregate. |
| T28 | G.fast (212 MHz copper) | 2014 | T26 + A27 | 1 Gbps over 100 m copper. Vectoring. |

**Era 4 Gateway:** T22 (40G DWDM) + T26 (GPON) → global broadband capacity

### SWITCHING

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| S22 | MPLS — Multi‑Protocol Label Switching | 1999 | C25 + C19 | Traffic engineering, VPNs, fast reroute. |
| S23 | Softswitch (MGC architecture) | 1998 | S18 + C17 | Separate call control from media. |
| S24 | SIP — Session Initiation Protocol | 1999 | C17 + S23 | Text‑based call setup. VoIP interop. |
| S25 | MGW — Media Gateway | 1998 | S23 + S16 | TDM↔IP conversion. G.711↔G.729. |
| S26 | SIGTRAN — SS7 over IP | 2000 | C15 + C17 | M3UA, M2PA. SS7 over IP. |
| S27 | LTE EPC (MME, SGW, PGW, HSS) | 2012 | A25 + C25 | All‑IP core for LTE. |
| S28 | Diameter AAA protocol | 2005 | C15 + C17 | Replaces RADIUS. LTE/IMS auth. |

**Era 4 Gateway:** S22 (MPLS) + S23 (Softswitch) → IP convergence

### ACCESS

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| A22 | 3G UMTS (WCDMA) | 2004 | A20 + C15 | 5 MHz channels. 2 Mbps peak. |
| A23 | 3.5G HSDPA / HSPA+ | 2006 | A22 | 14.4 → 42 Mbps. |
| A24 | FTTH (GPON / EPON) | 2005–10 | T26 + A21 | Fiber to home. Symmetric 1G/2.5G/10G. |
| A25 | 4G LTE (OFDMA, MIMO) | 2012 | A23 + S27 | OFDMA, 20 MHz, 2×2 MIMO. 150 Mbps. All‑IP. |
| A26 | 4.5G LTE‑Advanced | 2015 | A25 | 5×20 MHz CA. 4×4 MIMO. 1 Gbps peak. |
| A27 | VDSL2 + Vectoring | 2010 | A21 + T26 | 100 Mbps at 500 m. Crosstalk cancellation. |
| A28 | WiMAX (802.16e) | 2005 | A22 | OFDMA fixed wireless. 40 Mbps. |

**Era 4 Gateway:** A25 (4G LTE) → all‑IP mobile era

### CORE NETWORK

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| C22 | Frame Relay | 1984 | C18 + T16 | 1.5 Mbps PVCs. Cheaper than leased lines. |
| C23 | ATM backbone (B‑ISDN) | 1993 | C19 + T18 | 622 Mbps core. ISP backbone. |
| C24 | BGP — Border Gateway Protocol | 1989 | C17 | Inter‑domain routing. |
| C25 | IP/MPLS backbone | 1999 | C17 + C24 | Carrier‑grade IP. Replaces FR/ATM. |
| C26 | IMS — IP Multimedia Subsystem | 2002 | S24 + C25 | SIP converged core. HSS, CSCF. |
| C27 | GGSN / SGSN (GPRS core) | 2000 | A20 + C17 | Tunnels mobile data to internet. |
| C28 | NFV — Network Functions Virtualization | 2012 | C25 + C20 | Virtualized EPC/IMS on COTS. |

**Era 4 Gateway:** C26 (IMS) + C25 (IP/MPLS) → single converged network

---

## Era 5: Autonomous & Software-Defined (2015–2030)

### TRANSMISSION

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| T29 | 1.6 Tbps coherent (single carrier) | 2025 | T25 + C30 | Probabilistic shaping. 1.6 Tbps per λ. |
| T30 | Flex‑grid DWDM | 2015 | T25 | 12.5 GHz slot granularity. |
| T31 | Hollow‑core NANF fiber | 2024 | T29 | 99.7% speed of light. 3× lower latency. |
| T32 | Free‑Space Optics (FSO) backhaul | 2018 | A30 + T30 | 10 Gbps laser. License‑free. |
| T33 | EDFA + Raman hybrid amplification | 2012 | T19 + T25 | 10,000 km reach. No regeneration. |
| T34 | Space‑Division Multiplexing (SDM) | 2020 | T25 | Multi‑core fiber. ×7 capacity. |
| T35 | Distributed Acoustic Sensing (DAS) | 2018 | T31 + C35 | Cable‑cut prevention. |

**Era 5 Gateway:** T31 (Hollow‑core fiber) → latency‑minimized global transport

### SWITCHING

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| S29 | SDN — Software‑Defined Networking | 2011 | C25 + C28 | Control/data plane separation. |
| S30 | Network Slicing (5G SA) | 2020 | A30 + C31 | eMBB, URLLC, mMTC slices. |
| S31 | Service mesh (Istio, Cilium) | 2018 | C28 + S29 | Sidecar proxy. mTLS. |
| S32 | P4 programmable data plane | 2016 | S29 | Protocol‑independent programming. |
| S33 | Segment Routing (SR‑MPLS, SRv6) | 2015 | S22 | Source‑routed MPLS. |
| S34 | 5G UPF — User Plane Function | 2020 | S30 + C31 | Distributed user plane. 10 Gbps. |
| S35 | ZTP — Zero‑Touch Provisioning | 2018 | S29 + C28 | Auto‑configure from DHCP. |

**Era 5 Gateway:** S29 (SDN) → fully programmable network

### ACCESS

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| A29 | 5G NR Non‑Standalone (FR1) | 2019 | A26 + A25 | sub‑6 GHz. 1–2 Gbps. |
| A30 | 5G NR Standalone (FR2, mmWave) | 2020 | A29 + S34 | 28/39 GHz. 4 Gbps. 200 m. |
| A31 | 5G‑Advanced (AI/ML RAN) | 2024 | A30 + C33 | AI/ML RAN. eRedCap. ISAC. |
| A32 | LEO satellite (Starlink v2) | 2023 | A29 + T24 | 7,500+ sats. 220 Gbps per sat. |
| A33 | Direct‑to‑cell satellite | 2024 | A32 + A30 | Standard phone to satellite. |
| A34 | FWA — Fixed Wireless Access (5G) | 2020 | A30 | CPE on window. 300–500 Mbps. |
| A35 | Wi‑Fi 6/6E (802.11ax) | 2020 | A29 | OFDMA, MU‑MIMO. Carrier offload. |

**Era 5 Gateway:** A30 (5G SA mmWave) → ubiquitous high‑speed wireless

### CORE NETWORK

| Node | Tech | Year | Prereqs | Effect |
|---|---|---|---|---|
| C29 | MEC — Mobile Edge Computing | 2020 | S34 + C31 | Compute at 5G base station. <10 ms. |
| C30 | SDN optical transport (GMPLS) | 2015 | C25 + T25 | Multi‑layer optimization. |
| C31 | 5GC SBA (Service‑Based Architecture) | 2020 | A30 + C28 | HTTP/2, RESTful, cloud‑native. |
| C32 | NWDAF — Network Data Analytics | 2020 | C31 | AI/ML analytics in 5GC. |
| C33 | AI RIC — RAN Intelligent Controller | 2024 | C31 + C32 | xApps/rApps. Real‑time optimization. |
| C34 | QKD — Quantum Key Distribution | 2020s | C31 + T31 | Entanglement‑based key exchange. |
| C35 | ZSM — Zero‑Touch Network Management | 2020 | C31 + C32 | Closed‑loop automation. |

**Era 5 Gateway:** C31 (5GC SBA) → autonomous network operations

---

## Era 6: Interspace & Beyond (2050+)

### TRANSMISSION

| Node | Tech | Prereqs | Effect |
|---|---|---|---|
| T36 | Quantum entanglement relay | T31 + T34 + S37 | Instant correlation at any distance. |
| T37 | Neutrino beam link | T36 + C36 | Penetrates planets. 0.1 bit/s through 10,000 km rock. |
| T38 | Gravity‑wave antenna array | T37 + C39 | Galactic‑scale communication. |
| T39 | Lunar laser comm | T36 + A38 | 10 Gbps Earth↔Moon. |
| T40 | Orbital Angular Momentum (OAM) mux | T36 | ∞ states per photon. Unlimited capacity. |
| T41 | Mars DTN backbone | T39 + C39 | Bundle protocol across planets. |

### SWITCHING

| Node | Tech | Prereqs | Effect |
|---|---|---|---|
| S36 | Quantum router (entanglement swap) | T36 + C34 | Swap entanglement across nodes. |
| S37 | Quantum memory buffer | S36 | Store entangled state 1 hour. |
| S38 | Photonic on‑chip switch | S36 + T36 | 100 Tbps, zero idle power. |
| S39 | Interplanetary routing (IPN gateway) | S38 + C39 | Bundle bridge, Sol system mesh. |
| S40 | Causal‑structure‑aware routing | T38 + S39 | Routes through spacetime curvature. |

### ACCESS

| Node | Tech | Prereqs | Effect |
|---|---|---|---|
| A36 | Biological neural interface | A35 + C38 | Direct brain↔network. 1 Gbps. |
| A37 | Holographic antenna array | A30 + T34 | Programmable EM surface. 10 Tbps/user. |
| A38 | Lunar base station | A30 + T31 | Network on the Moon. 100 km radius. |
| A39 | Dyson‑swarm relay | T41 + S39 | Thousands of statites around Sun. |
| A40 | Multi‑planet SIM / identity | S39 + C36 | Universal identity, seamless roaming. |

### CORE NETWORK

| Node | Tech | Prereqs | Effect |
|---|---|---|---|
| C36 | Universal quantum internet | T36 + S36 + C34 | End‑to‑end quantum state transmission. |
| C37 | Post‑quantum crypto protocol | C34 + C31 | NIST Kyber/Dilithium. |
| C38 | AI mesh protocol (swarm routing) | C35 + A36 | Trillions of self‑forming devices. |
| C39 | Interstellar data bundling | T36 + T41 | Deep‑space FEC. >1 ly distance. |
| C40 | Dispersed ledger inter‑carrier settlement | C36 + S39 | Blockchain for planetary clearing. |

---

### Full Dependency Graph Summary

```
Era 1:  7+7+7+7 = 28 nodes, mostly linear within branch
Era 2:  7+7+7+7 = 28 nodes, first cross-branch prereqs (e.g. T10←S9, S11←C4)
Era 3:  7+7+7+7 = 28 nodes, heavy cross-branch (e.g. A20←C17, S15←C9)
Era 4:  7+7+7+7 = 28 nodes, IP convergence (S22←C25+C19, A25←S27)
Era 5:  7+7+7+7 = 28 nodes, SDN/5G interdependence (A30←S34, C31←A30+C28)
Era 6:  6+5+5+5 = 21 nodes, quantum+interplanetary
Total: ≈161 unlockable nodes
```
