#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telecom Clicker — Text Edition
================================
Real-time text version of the Telecom Clicker game design.
Start in 1880 with hand-crank switchboards, research 4 tech branches
(Transmission / Switching / Access / Core) across 6 eras, build
infrastructure, fight rivals, take contracts, run ads, borrow from the
bank, and take the company public.

Canonical web game: game/index.html  |  Tech data: game/tech-nodes.json
"""

import json
import math
import os
import random
import sys
import threading
import time

# ─────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────

ERA_NAMES = [
    "Analog Dawn (1880-1920)",
    "Electromechanical & Radio (1930-1960)",
    "Digital & Satellite (1970-1990)",
    "Broadband & IP (2000-2015)",
    "Autonomous & SDN (2015-2030)",
    "Interspace (2030+)",
]

WORLD_REGIONS = [
    "North America", "Latin America", "Western Europe", "Eastern Europe",
    "East Asia", "Southeast Asia", "South Asia", "Middle East",
    "Africa", "Oceania", "Central Asia", "Arctic/Nordic",
]

BRANCH_NAMES = {"T": "Transmission", "S": "Switching", "A": "Access", "C": "Core"}
BRANCH_ORDER = ["T", "S", "A", "C"]

RIVAL_NAMES_A = ['Northstar', 'Continental', 'Horizon', 'Frontier', 'Summit',
                 'Pioneer', 'United', 'Metro', 'National', 'Regional', 'Allied',
                 'Civic', 'Atlas', 'Evergreen', 'Signal', 'Vertex', 'Gateway',
                 'Commonwealth']
RIVAL_NAMES_B = ['Telecom', 'Communications', 'Networks', 'Wireless', 'Broadband',
                 'Telephone', 'Connectivity', 'Fiber', 'Mobile', 'Link', 'Systems',
                 'Services', 'Infrastructure', 'Digital', 'Exchange', 'Data']
RIVAL_DNA = {'tech-first': 1.5, 'financial-first': 0.7, 'balanced': 1.0,
             'tech-follower': 0.5, 'aggressive': 1.3, 'conservative': 0.8}

# Infrastructure: era -> [(name, $/sec per unit, cost multiplier)]
INFRA_ASSETS = {
    0: [["Copper Trunk", 0.03, 1.00], ["Manual Switchboard", 0.05, 1.20],
        ["Telegraph", 0.025, 0.90], ["Carrier Terminal", 0.08, 1.60],
        ["Underground Conduit", 0.06, 1.40], ["Automatic Exchange", 0.10, 2.00],
        ["Panel Exchange", 0.14, 2.80], ["Private Branch Exchange", 0.07, 1.50],
        ["Toll Office", 0.12, 2.30]],
    1: [["Coaxial Backbone", 0.50, 1], ["Microwave Tower", 0.30, 1],
        ["Crossbar Exchange", 0.80, 1], ["Submarine Cable", 2.00, 1]],
    2: [["Fiber Cable", 5.00, 1], ["Digital CO", 4.00, 1],
        ["Cell Tower", 1.00, 1], ["Data Center", 2.00, 1]],
    3: [["FTTH OLT", 8.00, 1], ["LTE eNodeB", 5.00, 1],
        ["DWDM Terminal", 12.00, 1], ["IP Core Router", 10.00, 1]],
    4: [["5G gNodeB", 15.00, 1], ["LEO Terminal", 20.00, 1],
        ["AI-NFV Core", 5.00, 1], ["MEC Node", 4.00, 1]],
}

AD_PRODUCTS = [
    {"id": "newspaper", "name": "Newspaper Ads", "year": 1880, "era": 0,
     "growth": 0.25, "cost": 0.15},
    {"id": "billboard", "name": "Billboard Ads", "year": 1880, "era": 0,
     "growth": 0.20, "cost": 0.20},
    {"id": "radio", "name": "Radio Spots", "year": 1922, "era": 1,
     "growth": 0.40, "cost": 0.30},
    {"id": "tv", "name": "TV Commercials", "year": 1941, "era": 2,
     "growth": 0.55, "cost": 0.50},
    {"id": "web-banner", "name": "Web Banner Ads", "year": 1994, "era": 3,
     "growth": 0.35, "cost": 0.30},
    {"id": "search", "name": "Search Ads", "year": 2000, "era": 3,
     "growth": 0.60, "cost": 0.60},
    {"id": "social", "name": "Social Feed Ads", "year": 2007, "era": 4,
     "growth": 0.75, "cost": 0.80},
    {"id": "video", "name": "Video/Stories Ads", "year": 2010, "era": 4,
     "growth": 0.90, "cost": 1.00},
    {"id": "programmatic", "name": "Programmatic Ads", "year": 2012, "era": 5,
     "growth": 1.00, "cost": 1.25},
    {"id": "streaming", "name": "Streaming/CTV Ads", "year": 2016, "era": 5,
     "growth": 1.20, "cost": 1.50},
]

CONTRACT_TYPES = ["Govt broadband", "Enterprise VPN", "Military comms",
                  "Smart city", "Cable landing"]

START_FOOTHOLD = 20
NEW_REGION_FOOTHOLD = 15
USER_GROWTH_RATE = 0.47
EXPANSION_BASE_COST = 350
FOOTHOLD_BASE_COST = 35
LAB_COST_BASE = 150

GAME_YEAR_SECONDS = 3600        # 1 in-game year per real hour
GAME_DAY_SECONDS = GAME_YEAR_SECONDS / 365
MONTH_SECONDS = GAME_YEAR_SECONDS / 12

BANK_RATE_CENTER = 0.03
BANK_RATE_MIN = 0.027
BANK_RATE_MAX = 0.033
BANK_RATE_MONTHS = 3
BANK_CREDIT_PER_REVENUE_PER_SEC = 1800
INCOME_SCALE = 100

CLICK_BASE_REVENUE = 5
AD_SUBSCRIBERS_PER_DOLLAR_PER_SEC = 1
RP_BASE_RATE = 5
RP_GAUGE_BONUS = 0.5
LAB_RP_BONUS = 0.25
ERA_RP_CAPS = [8, 12, 18, 27, 40]
TARGET_ERA_SECONDS = 7 * 60 * 60   # ~7h of play to clear an era on the fast path
ERA_MIN_PATH_WEIGHTS = [239, 581, 815, 1058, 960]
ERA_RP_CARRY_SECONDS = 30 * 60     # at most 30 min of RP carries into next era

MAX_PENDING_CONTRACTS = 2
MAX_ACTIVE_CONTRACTS = 3
CONTRACT_OFFER_TTL = 180
MAX_RIVALS_PER_REGION = 5
MAX_RIVAL_SPAWNS_PER_YEAR = 1
WEAK_RIVAL_FOOTHOLD = 0.05
WEAK_RIVAL_EXIT_MIN_CHANCE = 0.20
WEAK_RIVAL_EXIT_MAX_CHANCE = 0.50

SAVE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "telecom_clicker_save.json")
TECH_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "tech-nodes.json")

# ─────────────────────────────────────────────
# TECH TREE (from tech-nodes.json)
# ─────────────────────────────────────────────

TECH_NODES = {}
if os.path.exists(TECH_FILE):
    try:
        with open(TECH_FILE, encoding="utf-8") as f:
            TECH_NODES = json.load(f)
    except Exception:
        TECH_NODES = {}

TECH_TREE = {}
for nid, node in TECH_NODES.items():
    TECH_TREE[nid] = [
        node.get("name", nid),
        int(node.get("era", 0)),
        list(node.get("prerequisite", [])),
        int(node.get("quality", {}).get("coverage", 0)),
        int(node.get("quality", {}).get("speed", 0)),
        int(node.get("quality", {}).get("reliability", 0)),
        int(node.get("quality", {}).get("latency", 0)),
        int(node.get("RP", 10)),
    ]

INFRA_UNLOCKS = {}
for nid, node in TECH_NODES.items():
    infra = node.get("infra")
    if not infra:
        continue
    for era, assets in INFRA_ASSETS.items():
        for idx, asset in enumerate(assets):
            if asset[0] == infra:
                INFRA_UNLOCKS.setdefault(era, {})[idx] = nid

# ─────────────────────────────────────────────
# GAME STATE
# ─────────────────────────────────────────────


class State:
    def __init__(self):
        self.cash = 100.0
        self.rp = 5.0
        self.clicks = 0
        self.era = 0
        self.year = 1880.0
        self.researched = set()
        self.regions = {WORLD_REGIONS[0]: []}
        self.footholds = {WORLD_REGIONS[0]: START_FOOTHOLD}
        self.contracts = []
        self.active_contracts = []
        self.rivals = []
        self.rival_spawn_year = int(self.year)
        self.rival_spawns_this_year = 0
        self.contract_timer = 0.0
        self.is_public = False
        self.owned_shares = 1.0
        self.prestige_mult = 1.0
        self.bank_debt = 0.0
        self.bank_rate = BANK_RATE_CENTER
        self.bank_months_at_rate = 0
        self.last_bank_interest = 0.0
        self.users = 100
        self.ad_products = {}
        self.lab_level = 1
        self.tech_investment = 0.0
        self.tech_investment_max = 200.0
        self.research_budget = 10
        self.selected_region = WORLD_REGIONS[0]
        self.bulk_qty = 1
        self.notice = "Welcome to Telecom Clicker! Type 'help' for commands."

    def to_dict(self):
        return {
            "v": 1, "cash": self.cash, "rp": self.rp, "clicks": self.clicks,
            "era": self.era, "year": self.year,
            "researched": sorted(self.researched),
            "regions": self.regions, "footholds": self.footholds,
            "contracts": self.contracts, "active_contracts": self.active_contracts,
            "rivals": self.rivals, "is_public": self.is_public,
            "owned_shares": self.owned_shares, "prestige_mult": self.prestige_mult,
            "bank_debt": self.bank_debt, "bank_rate": self.bank_rate,
            "bank_months_at_rate": self.bank_months_at_rate,
            "last_bank_interest": self.last_bank_interest, "users": self.users,
            "ad_products": self.ad_products, "lab_level": self.lab_level,
            "tech_investment": self.tech_investment,
            "tech_investment_max": self.tech_investment_max,
            "research_budget": self.research_budget,
            "selected_region": self.selected_region, "bulk_qty": self.bulk_qty,
        }

    def from_dict(self, d):
        self.cash = float(d.get("cash", 100))
        self.rp = float(d.get("rp", 5))
        self.clicks = int(d.get("clicks", 0))
        self.era = max(0, min(5, int(d.get("era", 0))))
        self.year = float(d.get("year", 1880))
        self.researched = set(d.get("researched", []))
        self.regions = dict(d.get("regions", {}) or {})
        self.footholds = dict(d.get("footholds", {}) or {})
        self.contracts = list(d.get("contracts", []))
        self.active_contracts = list(d.get("active_contracts", []))
        self.rivals = list(d.get("rivals", []))
        self.is_public = bool(d.get("is_public", False))
        self.owned_shares = float(d.get("owned_shares", 1.0))
        self.prestige_mult = float(d.get("prestige_mult", 1.0))
        self.bank_debt = float(d.get("bank_debt", 0))
        self.bank_rate = float(d.get("bank_rate", BANK_RATE_CENTER))
        self.bank_months_at_rate = int(d.get("bank_months_at_rate", 0))
        self.last_bank_interest = float(d.get("last_bank_interest", 0))
        self.users = float(d.get("users", 100))
        self.ad_products = dict(d.get("ad_products", {}) or {})
        self.lab_level = int(d.get("lab_level", 1))
        self.tech_investment = float(d.get("tech_investment", 0))
        self.tech_investment_max = float(d.get("tech_investment_max", 200))
        self.research_budget = int(d.get("research_budget", 10))
        self.selected_region = d.get("selected_region", WORLD_REGIONS[0])
        self.bulk_qty = int(d.get("bulk_qty", 1))
        if WORLD_REGIONS[0] not in self.regions:
            self.regions[WORLD_REGIONS[0]] = []
            self.footholds.setdefault(WORLD_REGIONS[0], START_FOOTHOLD)


STATE = State()

# ─────────────────────────────────────────────
# ECONOMIC HELPERS
# ─────────────────────────────────────────────


def fmt(n):
    n = float(n)
    if n >= 1e12:
        return f"${n/1e12:.2f}T"
    if n >= 1e9:
        return f"${n/1e9:.2f}B"
    if n >= 1e6:
        return f"${n/1e6:.2f}M"
    if n >= 1e3:
        return f"${n/1e3:.1f}K"
    return f"${n:.2f}"


def fmt_int(n):
    return f"${int(n):,}"


def game_date():
    year = int(STATE.year)
    day = int((STATE.year - year) * 365)
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        months[1] += 1
    month = 0
    while day >= months[month]:
        day -= months[month]
        month += 1
    return f"{year:04d}/{month+1:02d}/{day+1:02d}"


def quality_score():
    cov = spd = rel = lat = 0
    for nid in STATE.researched:
        d = TECH_TREE.get(nid)
        if d:
            cov += d[3]
            spd += d[4]
            rel += d[5]
            lat += d[6]
    for r in STATE.regions:
        for era, idx, qty in STATE.regions[r]:
            if era <= STATE.era and INFRA_ASSETS.get(era) and \
                    idx < len(INFRA_ASSETS[era]):
                pct = min(10, qty)
                spd += pct
                rel += pct
    return min(100, cov * 0.3 + spd * 0.3 + rel * 0.2 + lat * 0.2)


def region_infra_ips(region):
    ips = 0.0
    for era, idx, qty in STATE.regions.get(region, []):
        if era <= STATE.era and INFRA_ASSETS.get(era) and \
                idx < len(INFRA_ASSETS[era]):
            ips += INFRA_ASSETS[era][idx][1] * qty
    return ips


def total_infra_ips():
    return sum(region_infra_ips(r) for r in STATE.regions)


def infra_unlocked(era, idx):
    if STATE.era < era:
        return False
    req = INFRA_UNLOCKS.get(era, {}).get(idx)
    if not req or req in STATE.researched:
        return True
    return any(True for invs in STATE.regions.values()
               for inv in invs if inv[0] == era and inv[1] == idx)


def total_foothold_mult():
    vals = [min(0.8, STATE.footholds.get(r, 0) / 100) for r in STATE.regions]
    return (sum(vals) / len(vals)) if vals else 0.1


def rival_pressure():
    if not STATE.regions:
        return 1.0
    total = 0.0
    my_q = quality_score()
    for region in STATE.regions:
        rivals = [r for r in STATE.rivals if r["region"] == region]
        if rivals:
            share = sum(rival_market_share(r, my_q) for r in rivals)
            total += max(0.05, 1 - min(0.95, share))
        else:
            total += 1.0
    return total / len(STATE.regions)


def region_competition_mult(region):
    rivals = [r for r in STATE.rivals if r["region"] == region]
    if not rivals:
        return 1.0
    pressure = sum(rival_market_share(r, quality_score()) for r in rivals)
    return max(0.05, 1 - min(0.95, pressure))


def technology_revenue_mult():
    return 1 + quality_score() / 100


def region_market_mult(region):
    fh = max(0.05, min(1.0, STATE.footholds.get(region, 0) / 100))
    return fh * region_competition_mult(region)


def region_network_ips(region):
    return (region_infra_ips(region) * technology_revenue_mult()
            * region_market_mult(region) * STATE.prestige_mult * INCOME_SCALE)


def network_income_ips():
    return sum(region_network_ips(r) for r in STATE.regions)


def rp_rate():
    gauge = (STATE.tech_investment / STATE.tech_investment_max
             if STATE.tech_investment_max else 0)
    lab_mult = 1 + max(0, STATE.lab_level - 1) * LAB_RP_BONUS
    budget_mult = 1 + STATE.research_budget / 100
    network_boost = 1 + min(1, math.log2(1 + max(0, network_income_ips())) / 8)
    raw = (RP_BASE_RATE * lab_mult * budget_mult
           * (1 + gauge * RP_GAUGE_BONUS) * network_boost)
    cap = ERA_RP_CAPS[min(STATE.era, len(ERA_RP_CAPS) - 1)]
    return min(cap, raw)


def research_cost(nid):
    d = TECH_TREE.get(nid)
    if not d:
        return 0
    era = max(0, min(len(ERA_RP_CAPS) - 1, d[1]))
    scale = ERA_RP_CAPS[era] * TARGET_ERA_SECONDS / ERA_MIN_PATH_WEIGHTS[era]
    return max(1, math.ceil(max(1, d[7]) * scale))


def can_research(nid):
    d = TECH_TREE.get(nid)
    if nid in STATE.researched:
        return "owned"
    if not d or d[1] > STATE.era:
        return "locked"
    for p in d[2]:
        if p not in STATE.researched:
            return "locked"
    return "avail"


def era_requirement(branch):
    total = sum(1 for nid in TECH_TREE
                if nid[0] == branch and TECH_TREE[nid][1] == STATE.era)
    return min(4, total)


# ─────────────────────────────────────────────
# RIVALS
# ─────────────────────────────────────────────


def rival_name():
    return (random.choice(RIVAL_NAMES_A) + " " + random.choice(RIVAL_NAMES_B))


def spawn_rival():
    candidates = [r for r in WORLD_REGIONS
                  if len([x for x in STATE.rivals if x["region"] == r])
                  < MAX_RIVALS_PER_REGION]
    if not candidates:
        return False
    region = candidates[0]
    tech = min(5, max(STATE.era, int((STATE.year - 1880) / 20)))
    infra = max((tech + 1) * 2, total_infra_ips() * (0.55 + random.random() * 0.35))
    STATE.rivals.append({
        "name": rival_name(), "region": region, "tech": tech, "infra": infra,
        "quality": min(100, 42 + tech * 7 + random.random() * 10),
        "home_share": 0.02 + random.random() * 0.06,
        "dna": random.choice(list(RIVAL_DNA)),
    })
    STATE.notice = f"New rival entered {region}"
    return True


def init_rivals():
    STATE.rivals = []
    STATE.rival_spawn_year = int(STATE.year)
    STATE.rival_spawns_this_year = 0
    for _ in range(min(3, len(WORLD_REGIONS))):
        spawn_rival()
    STATE.rival_spawns_this_year = 0


def rival_market_share(rival, my_quality):
    tech_bonus = (rival.get("tech", 0) or 0) * 7
    infra_bonus = math.log10(1 + (rival.get("infra", 0) or 0)) * 6
    pressure = ((rival.get("quality", 50) + tech_bonus + infra_bonus + 20)
                / (my_quality + 20) * 1.25)
    return min(0.9, rival.get("home_share", 0.05)
               * max(0.45, min(1.4, pressure)))


def rival_tick(dt):
    for rival in STATE.rivals:
        rate = RIVAL_DNA.get(rival.get("dna"), 1.0)
        rival["tech"] = min(5, rival.get("tech", 0) + 0.0008 * rate * dt)
        rival["infra"] = max(0, rival.get("infra", 0)
                             + (0.03 + rival.get("tech", 0) * 0.015) * rate * dt)
        rival["quality"] = min(100, rival.get("quality", 50)
                               + 0.55 * rate * (1 + STATE.era * 0.12) * dt / 60)
        rival["home_share"] = min(0.75, rival.get("home_share", 0.05)
                                  + 0.0012 * rate * dt / 60)
        fh = STATE.footholds.get(rival["region"], 0)
        if fh > 1:
            gap = max(0, rival["quality"] - quality_score())
            STATE.footholds[rival["region"]] = max(
                1, fh - gap / 100 * 0.0015 * dt)


def rival_monthly_industry_update():
    year = int(STATE.year)
    if STATE.rival_spawn_year != year:
        STATE.rival_spawn_year = year
        STATE.rival_spawns_this_year = 0
    departed = []
    keep = []
    for rival in STATE.rivals:
        foothold = max(0, float(rival.get("home_share", 0)))
        if foothold >= WEAK_RIVAL_FOOTHOLD:
            keep.append(rival)
            continue
        weakness = 1 - min(1, foothold / WEAK_RIVAL_FOOTHOLD)
        chance = (WEAK_RIVAL_EXIT_MIN_CHANCE
                  + weakness * (WEAK_RIVAL_EXIT_MAX_CHANCE
                                - WEAK_RIVAL_EXIT_MIN_CHANCE))
        if random.random() < chance:
            departed.append(rival["name"])
        else:
            keep.append(rival)
    STATE.rivals = keep
    if (STATE.rival_spawns_this_year < MAX_RIVAL_SPAWNS_PER_YEAR
            and random.random() < _rival_entry_chance(year)):
        if spawn_rival():
            STATE.rival_spawns_this_year += 1
    if departed:
        STATE.notice = ", ".join(departed) + " left the market"


def _rival_entry_chance(year):
    if year < 1900:
        return 0.03
    if year < 1915:
        return 0.05
    if year < 1930:
        return 0.08
    if year < 1950:
        return 0.12
    if year < 1980:
        return 0.16
    return 0.20


# ─────────────────────────────────────────────
# ADS / USERS / CONTRACTS / BANK
# ─────────────────────────────────────────────


def ad_state(pid):
    return STATE.ad_products.setdefault(pid, {"spend": 0})


def ad_unlocked(product):
    return STATE.era >= product["era"] and STATE.year >= product["year"]


def ad_spend_ratio(product):
    return max(0, min(100, float(ad_state(product["id"]).get("spend", 0)))) / 100


def gross_income_ips():
    return max(0, network_income_ips())


def ad_cost_per_tick(product):
    if not ad_unlocked(product):
        return 0
    return gross_income_ips() * 0.01 * ad_spend_ratio(product)


def ad_growth_per_tick(product):
    return ad_cost_per_tick(product) * AD_SUBSCRIBERS_PER_DOLLAR_PER_SEC


def ad_cost_total():
    return sum(ad_cost_per_tick(p) for p in AD_PRODUCTS)


def organic_user_growth():
    saturation = max(0.05, 1 - STATE.users / 1_000_000)
    return (USER_GROWTH_RATE * (1 + quality_score() / 200)
            * max(0.1, total_foothold_mult()) * rival_pressure() * saturation)


def user_growth():
    return organic_user_growth() + sum(ad_growth_per_tick(p)
                                       for p in AD_PRODUCTS)


def generate_contract():
    if (len(STATE.contracts) >= MAX_PENDING_CONTRACTS
            or len(STATE.active_contracts) >= MAX_ACTIVE_CONTRACTS):
        return
    candidates = [r for r in WORLD_REGIONS if STATE.footholds.get(r, 0) < 50]
    if not candidates:
        return
    region = random.choice(candidates)
    STATE.contracts.append({
        "name": random.choice(CONTRACT_TYPES), "region": region,
        "monthly_payment": 100 + random.randint(0, 400),
        "months_total": 6 + random.randint(0, 6),
        "months_paid": 0, "boost": 30 + random.randint(0, 29),
        "offer_age": 0,
        "offer_ttl": CONTRACT_OFFER_TTL + random.randint(0, CONTRACT_OFFER_TTL),
    })


def pay_contracts():
    completed = []
    keep = []
    for ct in STATE.active_contracts:
        STATE.cash += ct["monthly_payment"]
        ct["months_paid"] += 1
        if ct["months_paid"] >= ct["months_total"]:
            completed.append(ct["name"])
        else:
            keep.append(ct)
    STATE.active_contracts = keep
    if completed:
        STATE.notice = "Contract complete: " + ", ".join(completed)


def bank_credit_limit():
    return max(0, gross_income_ips() * BANK_CREDIT_PER_REVENUE_PER_SEC)


def bank_available_credit():
    return max(0, bank_credit_limit() - STATE.bank_debt)


def process_bank_month():
    interest = STATE.bank_debt * STATE.bank_rate / 12 if STATE.bank_debt > 0 else 0
    STATE.bank_debt += interest
    STATE.last_bank_interest = interest
    STATE.bank_months_at_rate += 1
    if STATE.bank_months_at_rate >= BANK_RATE_MONTHS:
        STATE.bank_months_at_rate = 0
        STATE.bank_rate = BANK_RATE_MIN + random.random() * (BANK_RATE_MAX - BANK_RATE_MIN)


# ─────────────────────────────────────────────
# TIME SIMULATION (real-time background thread)
# ─────────────────────────────────────────────

_tick_lock = threading.Lock()
_running = True


def simulate_seconds(seconds):
    remaining = max(0, seconds)
    while remaining > 0:
        dt = min(60, remaining)
        with _tick_lock:
            income_rate = gross_income_ips()
            ad_cost = ad_cost_total() * dt
            scale = min(1, max(0, STATE.cash) / ad_cost) if ad_cost > 0 else 1
            STATE.cash -= ad_cost * scale
            STATE.users = max(1, STATE.users
                              + (organic_user_growth()
                                 + sum(ad_growth_per_tick(p) for p in AD_PRODUCTS)
                                 * scale) * dt)
            income = (gross_income_ips() + income_rate) / 2 * dt
            STATE.cash += income
            net = max(0, income - ad_cost * scale)
            STATE.tech_investment = min(
                STATE.tech_investment_max,
                STATE.tech_investment + net * STATE.research_budget / 100)
            STATE.rp += rp_rate() * dt
            rival_tick(dt)
            for ct in STATE.contracts:
                ct["offer_age"] = ct.get("offer_age", 0) + dt
            STATE.contracts = [ct for ct in STATE.contracts
                               if ct["offer_age"] < ct.get("offer_ttl",
                                                           CONTRACT_OFFER_TTL)]
            STATE.year += dt / 3600
            STATE.contract_timer += dt
            while STATE.contract_timer >= MONTH_SECONDS:
                STATE.contract_timer -= MONTH_SECONDS
                pay_contracts()
                process_bank_month()
                rival_monthly_industry_update()
        remaining -= dt


def _background_tick():
    last = time.monotonic()
    while _running:
        now = time.monotonic()
        dt = min(60, now - last)
        last = now
        simulate_seconds(dt)
        time.sleep(0.2)


# ─────────────────────────────────────────────
# ACTIONS
# ─────────────────────────────────────────────


def do_click():
    val = CLICK_BASE_REVENUE * technology_revenue_mult() * STATE.prestige_mult
    STATE.cash += val
    STATE.clicks += 1
    return f"+{fmt(val)}"


def do_research(nid):
    nid = nid.upper()
    if nid in STATE.researched:
        return "Already researched."
    if can_research(nid) != "avail":
        return f"{nid} is locked (era or prerequisites)."
    cost = research_cost(nid)
    if STATE.rp < cost:
        return f"Need {cost:.0f} RP, have {STATE.rp:.0f}."
    STATE.rp -= cost
    STATE.researched.add(nid)
    if STATE.era < 5:
        counts = {b: sum(1 for n in STATE.researched
                         if TECH_TREE.get(n, [None, 99])[1] == STATE.era
                         and n[0] == b)
                  for b in BRANCH_ORDER}
        if all(counts[b] >= era_requirement(b) for b in BRANCH_ORDER):
            STATE.era += 1
            cap = ERA_RP_CAPS[min(STATE.era, len(ERA_RP_CAPS) - 1)]
            STATE.rp = min(STATE.rp, cap * ERA_RP_CARRY_SECONDS)
            STATE.prestige_mult *= 1 + STATE.era * 0.3
            STATE.notice = f"ERA ADVANCED → {ERA_NAMES[STATE.era]}"
    return f"Researched {nid} ({TECH_TREE[nid][0]})"

def infra_cost(era, idx, n, region):
    owned = [inv for inv in STATE.regions.get(region, [])
             if inv[0] == era and inv[1] == idx]
    qty = owned[0][2] if owned else 0
    asset = INFRA_ASSETS.get(era, [None] * 10)[idx] if idx < len(INFRA_ASSETS.get(era, [])) else None
    cost_mult = float(asset[2]) if asset and asset[2] > 0 else 1
    base = 10 * (era + 1) * (1 + era * 2) * cost_mult
    return int(base * n * (2 * qty + n + 1) / 2)


def do_build(era, idx, n=1):
    era, idx = int(era), int(idx)
    if not infra_unlocked(era, idx):
        return "Locked — research the required node first."
    region = STATE.selected_region
    cost = infra_cost(era, idx, n, region)
    if STATE.cash < cost:
        return f"Need {fmt(cost)}, have {fmt(STATE.cash)}."
    STATE.cash -= cost
    owned = [inv for inv in STATE.regions.get(region, [])
             if inv[0] == era and inv[1] == idx]
    if owned:
        owned[0][2] += n
    else:
        STATE.regions.setdefault(region, []).append([era, idx, n])
    return (f"Built ×{n} {INFRA_ASSETS[era][idx][0]} in {region} "
            f"({fmt(cost)})")


def do_expand(region):
    if region in STATE.regions:
        return "Already present."
    cost = EXPANSION_BASE_COST * (len(STATE.regions) + 1)
    if STATE.cash < cost:
        return f"Need {fmt(cost)}, have {fmt(STATE.cash)}."
    STATE.cash -= cost
    STATE.regions[region] = []
    STATE.footholds[region] = NEW_REGION_FOOTHOLD
    STATE.selected_region = region
    return (f"Expanded to {region}! Foothold {NEW_REGION_FOOTHOLD}% "
            f"({fmt(cost)})")


def do_boost(region):
    if region not in STATE.regions:
        return "Not present in that region."
    fh = STATE.footholds.get(region, 0)
    if fh >= 100:
        return "Foothold already maxed (100%)."
    cost = FOOTHOLD_BASE_COST * (int(fh) + 1)
    if STATE.cash < cost:
        return f"Need {fmt(cost)}, have {fmt(STATE.cash)}."
    STATE.cash -= cost
    STATE.footholds[region] = min(100, fh + 1)
    return f"Boosted {region} to {STATE.footholds[region]:.1f}%"


def do_accept_contract(idx):
    if len(STATE.active_contracts) >= MAX_ACTIVE_CONTRACTS:
        return f"Contract limit reached ({MAX_ACTIVE_CONTRACTS})."
    if idx >= len(STATE.contracts):
        return "No such contract."
    ct = STATE.contracts.pop(idx)
    if ct["region"] not in STATE.regions:
        STATE.regions[ct["region"]] = []
        STATE.footholds[ct["region"]] = NEW_REGION_FOOTHOLD
    STATE.footholds[ct["region"]] = max(STATE.footholds.get(ct["region"], 0),
                                        ct["boost"])
    ct["months_paid"] = 0
    STATE.active_contracts.append(ct)
    return (f"Accepted: {ct['name']} — {ct['region']} "
            f"${ct['monthly_payment']}/mo × {ct['months_total']}mo")


def do_borrow(share):
    amount = int(bank_available_credit() * max(0, min(1, share)))
    if amount < 1:
        return "No credit available."
    STATE.bank_debt += amount
    STATE.cash += amount
    return f"Borrowed {fmt_int(amount)} (debt {fmt(STATE.bank_debt)})"


def do_repay(share):
    if STATE.bank_debt <= 0 or STATE.cash <= 0:
        return "Nothing to repay."
    target = STATE.bank_debt if share >= 1 else STATE.bank_debt * max(0, share)
    amount = min(STATE.cash, target)
    STATE.cash -= amount
    STATE.bank_debt = max(0, STATE.bank_debt - amount)
    return f"Repaid {fmt_int(amount)} (debt {fmt(STATE.bank_debt)})"


def do_ipo():
    annual = gross_income_ips() * GAME_YEAR_SECONDS
    if STATE.is_public:
        return "Already public."
    if annual < 500 or "C10" not in STATE.researched:
        return "Need ANI (C10) and >$500/year revenue."
    val = int(annual * 24 * 30 * 2)
    sell = int(val * 0.3)
    STATE.cash += sell
    STATE.owned_shares = 0.7
    STATE.is_public = True
    return f"IPO! Sold 30% for {fmt_int(sell)}. Valuation {fmt_int(val)}."


def do_buyback():
    if not STATE.is_public:
        return "Not public."
    cost = int(gross_income_ips() * GAME_YEAR_SECONDS * 24 * 30 * 0.5)
    if STATE.cash < cost:
        return f"Need {fmt_int(cost)}."
    STATE.cash -= cost
    STATE.owned_shares = min(1.0, STATE.owned_shares + 0.1)
    return f"Bought back 10% (now {STATE.owned_shares*100:.0f}% owned)"


def do_upgrade_lab():
    cost = LAB_COST_BASE * STATE.lab_level * STATE.lab_level
    if STATE.cash < cost:
        return f"Need {fmt(cost)}."
    progress = (STATE.tech_investment / STATE.tech_investment_max
                if STATE.tech_investment_max else 0)
    STATE.cash -= cost
    STATE.lab_level += 1
    STATE.tech_investment_max = STATE.lab_level * 200
    STATE.tech_investment = progress * STATE.tech_investment_max
    return f"Laboratory upgraded to Lv.{STATE.lab_level} ({fmt(cost)})"


def save_game():
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(STATE.to_dict(), f, ensure_ascii=False, indent=1)
        return "Saved."
    except Exception as e:
        return f"Save failed: {e}"


def load_game():
    try:
        with open(SAVE_FILE, encoding="utf-8") as f:
            STATE.from_dict(json.load(f))
        return f"Loaded. ({game_date()})"
    except Exception as e:
        init_rivals()
        return f"No valid save — fresh start. ({e})"


# ─────────────────────────────────────────────
# RENDERING
# ─────────────────────────────────────────────


def print_status():
    s = STATE
    print("=" * 62)
    print(f"  {game_date()}  |  {ERA_NAMES[s.era]}")
    print(f"  Cash {fmt(s.cash)}   RP {s.rp:.1f} ({rp_rate():.1f}/s)"
          f"   Users {int(s.users)}   Quality {quality_score():.1f}")
    print(f"  Network income {fmt(gross_income_ips())}/s"
          f"  (click +{fmt(CLICK_BASE_REVENUE * technology_revenue_mult() * s.prestige_mult)})")
    print(f"  Regions {len(s.regions)}   Rivals {len(s.rivals)}"
          f"   Contracts {len(s.active_contracts)}/{MAX_ACTIVE_CONTRACTS}"
          f"   Debt {fmt(s.bank_debt)}"
          + ("   PUBLIC" if s.is_public else ""))
    if s.notice:
        print(f"  >> {s.notice}")
        s.notice = ""


def print_research():
    print("=" * 62)
    print("AVAILABLE RESEARCH (era requirement per branch: "
          + ", ".join(f"{BRANCH_NAMES[b]} {era_requirement(b)}"
                      for b in BRANCH_ORDER) + ")")
    rows = []
    for nid in sorted(TECH_TREE.keys(),
                      key=lambda x: (TECH_TREE[x][1], x)):
        d = TECH_TREE[nid]
        if d[1] > STATE.era + 1:
            continue
        status = can_research(nid)
        mark = {"owned": "[x]", "avail": "[ ]", "locked": "[#]"}[status]
        rows.append(f"  {mark} {nid:<5} {d[0]:<26} era {d[1]}"
                    f"  RP {research_cost(nid):>5}  "
                    + ("prereq: " + ",".join(d[2]) if d[2] else ""))
    print("\n".join(rows))


def print_infra():
    print("=" * 62)
    print(f"INFRASTRUCTURE — {STATE.selected_region} "
          f"(foothold {STATE.footholds.get(STATE.selected_region, 0):.1f}%)")
    print("  [era] [idx]  name                     $/s/unit")
    for era in range(0, STATE.era + 1):
        for idx, asset in enumerate(INFRA_ASSETS.get(era, [])):
            if not infra_unlocked(era, idx):
                continue
            owned = [inv for inv in STATE.regions.get(STATE.selected_region, [])
                     if inv[0] == era and inv[1] == idx]
            qty = owned[0][2] if owned else 0
            print(f"  {era}    {idx:<3} {asset[0]:<26} {asset[1]:>7}/s"
                  f"   ×{qty}   cost {fmt(infra_cost(era, idx, 1, STATE.selected_region))}")


def print_expand():
    print("=" * 62)
    print("EXPANSION — owned regions:")
    for rn in STATE.regions:
        print(f"  {rn:<18} foothold {STATE.footholds.get(rn, 0):.1f}%"
              f"  income {fmt(region_network_ips(rn))}/s")
    print("New regions:")
    for rn in [r for r in WORLD_REGIONS if r not in STATE.regions]:
        cost = EXPANSION_BASE_COST * (len(STATE.regions) + 1)
        print(f"  {rn:<18} cost {fmt(cost)}  start foothold {NEW_REGION_FOOTHOLD}%")


def print_rivals():
    print("=" * 62)
    if not STATE.rivals:
        print("  No rivals yet.")
        return
    my_q = quality_score()
    for rn in [r for r in WORLD_REGIONS
               if any(x["region"] == r for x in STATE.rivals)]:
        rivals = [r for r in STATE.rivals if r["region"] == rn]
        print(f"  {rn} ({len(rivals)} rival(s)):")
        for r in rivals:
            share = rival_market_share(r, my_q) * 100
            print(f"    {r['name']:<28} tech {int(r['tech'])}"
                  f"  infra {r['infra']:.0f}  q {r['quality']:.0f}"
                  f"  pressure {share:.0f}%")


def print_contracts():
    print("=" * 62)
    print(f"CONTRACTS (pending {len(STATE.contracts)},"
          f" active {len(STATE.active_contracts)}/{MAX_ACTIVE_CONTRACTS})")
    for i, ct in enumerate(STATE.contracts):
        ttl = ct["offer_ttl"] - ct["offer_age"]
        print(f"  [{i}] {ct['name']} — {ct['region']}"
              f"  ${ct['monthly_payment']}/mo × {ct['months_total']}"
              f"  foothold +{ct['boost']}%  offer {ttl:.0f}s left")
    for ct in STATE.active_contracts:
        print(f"  [*] {ct['name']} — {ct['region']}"
              f"  ${ct['monthly_payment']}/mo  paid {ct['months_paid']}/"
              f"{ct['months_total']}")


def print_ads():
    print("=" * 62)
    print(f"ADS — spend % of network revenue per channel "
          f"(total {fmt(ad_cost_total())}/s → "
          f"+{sum(ad_growth_per_tick(p) for p in AD_PRODUCTS):.2f} users/s)")
    for p in AD_PRODUCTS:
        spend = int(ad_spend_ratio(p) * 100)
        gate = ("OK" if ad_unlocked(p)
                else f"needs {ERA_NAMES[p['era']]} / {p['year']}")
        print(f"  {p['id']:<13} {p['name']:<22} spend {spend:>3}%  {gate}")


def print_bank():
    print("=" * 62)
    print(f"BANK — debt {fmt(STATE.bank_debt)}"
          f"  rate {STATE.bank_rate*100:.2f}%/yr"
          f"  credit {fmt(bank_credit_limit())}"
          f"  available {fmt(bank_available_credit())}")
    print(f"  monthly interest {fmt(STATE.last_bank_interest)}"
          f"  (rate resets in {BANK_RATE_MONTHS - STATE.bank_months_at_rate} mo)")


def print_ipo():
    print("=" * 62)
    annual = gross_income_ips() * GAME_YEAR_SECONDS
    val = int(annual * 24 * 30 * 2)
    if STATE.is_public:
        print(f"  PUBLIC — you own {STATE.owned_shares*100:.0f}%"
              f"  valuation {fmt_int(val)}")
        if STATE.owned_shares < 0.2:
            print("  DANGER: shareholders may remove you!")
    elif "C10" in STATE.researched and annual > 500:
        print(f"  Private — valuation {fmt_int(val)}"
              f"  sell 30% → {fmt_int(int(val*0.3))}")
    else:
        print("  Private. Need ANI (C10) and >$500/year revenue"
              f" (currently {fmt(annual)}/yr)")


def print_help():
    print("=" * 62)
    print("""COMMANDS:
  click, c                      Click (earn cash)
  status, s                     Current situation
  research, r                   List tech tree (available first)
  research <ID>                 Research a node, e.g. research T1
  infra, i                      List buildable infrastructure
  build <era> <idx> [qty]       Build infrastructure
  expand                        List new regions
  expand <region>               Enter a new region
  boost <region>                +1% foothold in owned region
  contracts, ct                 List contracts
  accept <n>                    Accept pending contract n
  ads                           List ad channels
  ad <id> <0-100>               Set ad spend %, e.g. ad newspaper 50
  bank                          Bank status
  borrow <0-1>                  Borrow fraction of credit, e.g. borrow .5
  repay <0-1>                   Repay fraction of debt (1 = all)
  ipo                           Go public (needs C10 + revenue)
  buyback                       Buy back 10% of shares
  lab                           Upgrade laboratory
  budget <0-20>                 Set R&D budget %
  wait <months>                 Fast-forward N months
  save / load                   Save / load progress
  quit, q                       Exit (progress is saved automatically)""")

# ─────────────────────────────────────────────
# REPL
# ─────────────────────────────────────────────


def cmd_research_args(args):
    if not args:
        print_research()
        return
    nid = args[0].upper()
    if nid not in TECH_TREE:
        print(f"Unknown node {nid}. See 'research'.")
        return
    print(do_research(nid))
    save_game()


def cmd_build(args):
    if len(args) < 2:
        print("Usage: build <era> <idx> [qty]")
        return
    try:
        era, idx = int(args[0]), int(args[1])
        n = int(args[2]) if len(args) > 2 else STATE.bulk_qty
    except ValueError:
        print("Usage: build <era> <idx> [qty]")
        return
    print(do_build(era, idx, n))
    save_game()


def cmd_expand(args):
    if not args:
        print_expand()
        return
    region = " ".join(args)
    if region not in WORLD_REGIONS:
        print(f"Unknown region '{region}'. Regions: {', '.join(WORLD_REGIONS)}")
        return
    print(do_expand(region))
    save_game()


def cmd_ad(args):
    if not args:
        print_ads()
        return
    pid = args[0]
    if pid not in [p["id"] for p in AD_PRODUCTS]:
        print("Unknown ad id. See 'ads'.")
        return
    try:
        spend = int(args[1])
    except (IndexError, ValueError):
        print("Usage: ad <id> <0-100>")
        return
    spend = max(0, min(100, spend))
    ad_state(pid)["spend"] = spend
    print(f"{pid} spend set to {spend}%")
    save_game()


def cmd_wait(args):
    try:
        months = float(args[0]) if args else 1
    except ValueError:
        print("Usage: wait <months>")
        return
    seconds = months * MONTH_SECONDS
    print(f"Fast-forwarding {months:.0f} month(s)...")
    simulate_seconds(seconds)
    print_status()


def main():
    global _running
    try:
        with open(TECH_FILE, encoding="utf-8") as f:
            if not TECH_NODES:
                print("WARNING: tech-nodes.json not found or empty — "
                      "tech tree will be empty.")
    except Exception:
        print("WARNING: could not read tech-nodes.json.")
    print("=" * 62)
    print("  TELECOM CLICKER — Text Edition")
    print("  Build a telecom empire from 1880 to the interspace era.")
    print("  Type 'help' for commands. 'quit' exits (autosaves).")
    print("=" * 62)
    load_game()
    ticker = threading.Thread(target=_background_tick, daemon=True)
    ticker.start()
    try:
        while True:
            try:
                line = input("> ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if not line:
                continue
            parts = line.split()
            cmd = parts[0].lower()
            args = parts[1:]
            if cmd in ("quit", "q", "exit"):
                break
            elif cmd in ("help", "h", "?"):
                print_help()
            elif cmd in ("click", "c"):
                print(do_click())
            elif cmd in ("status", "s"):
                print_status()
            elif cmd in ("research", "r"):
                cmd_research_args(args)
            elif cmd in ("infra", "i"):
                print_infra()
            elif cmd == "build":
                cmd_build(args)
            elif cmd == "expand":
                cmd_expand(args)
            elif cmd == "boost":
                if not args:
                    print("Usage: boost <region>")
                else:
                    print(do_boost(" ".join(args)))
                    save_game()
            elif cmd in ("contracts", "ct"):
                print_contracts()
            elif cmd == "accept":
                try:
                    print(do_accept_contract(int(args[0])))
                    save_game()
                except (IndexError, ValueError):
                    print("Usage: accept <n>")
            elif cmd == "ads":
                print_ads()
            elif cmd == "ad":
                cmd_ad(args)
            elif cmd == "bank":
                print_bank()
            elif cmd == "borrow":
                try:
                    print(do_borrow(float(args[0])))
                    save_game()
                except (IndexError, ValueError):
                    print("Usage: borrow <0-1>")
            elif cmd == "repay":
                try:
                    print(do_repay(float(args[0])))
                    save_game()
                except (IndexError, ValueError):
                    print("Usage: repay <0-1>")
            elif cmd == "ipo":
                print(do_ipo())
                save_game()
            elif cmd == "buyback":
                print(do_buyback())
                save_game()
            elif cmd == "lab":
                print(do_upgrade_lab())
                save_game()
            elif cmd == "budget":
                try:
                    STATE.research_budget = max(0, min(20, int(args[0])))
                    print(f"R&D budget set to {STATE.research_budget}%")
                    save_game()
                except (IndexError, ValueError):
                    print("Usage: budget <0-20>")
            elif cmd == "wait":
                cmd_wait(args)
            elif cmd == "save":
                print(save_game())
            elif cmd == "load":
                print(load_game())
            elif cmd == "rivals":
                print_rivals()
            else:
                print(f"Unknown command '{cmd}'. Type 'help'.")
    finally:
        _running = False
        save_game()
        print("Progress saved. Goodbye!")


if __name__ == "__main__":
    main()
