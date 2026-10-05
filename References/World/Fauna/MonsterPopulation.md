# Monster Population

Hub: `../World.md`. Human demography: `../Society/Population.md`. Prices: `../Society/Economy.md`. Mana `C`/`A`: `../Science/Energy/ManaConcentration.md`. Dungeons: `../Geography/Dungeons.md`. Species cards: `Creatures.md`. Story place fill: `../Geography/PlacesPopulation.md`.

Caldris-scale ecology and loot demand. World totals below are unlocked reference only. **Given-area worksheet** is at the end.

---

## Part 1. Premise

Terra is Earth-sized, 24-hour day, two moons, **361-day year**. Magic, status screens, monsters and dungeons are normal. Personal power is easy enough that many kingdoms exist instead of one empire.

**Caldris** (start): human-majority, temperate, medieval social structure + early industrial magitech (steam, rail, airships). No practical teleport. Solo road travel is dangerous; caravans are normal. Church of Solaria is the main faith.

Conflict drivers: politics, monsters, dungeons, villains.

Wild monsters ≠ dungeon-spawned monsters. Dungeon cores absorb dead things and respawn foes; countries treat dungeons as income engines. Damaging a core is forbidden.

### Population foundation

| Symbol | Meaning | Scale |
|---|---|---|
| **P** | People | Example Caldris: **1,000,000** |
| **M** | Monster pressure (socio-ecological, not mana) | 0.5 safe → 1 normal → **1.5 Caldris** → 2 frontier → 3 dungeon region |
| **W** | War | 1 peace → 2 border → 3 full war |

- ~25% urban, ~75% villages
- Workforce **L ≈ 59%** of non-noble/non-villain remainder; farmers ≈ half of L
- **Adventurers** and **hunters** are separate, same size each: `0.01 × L × M`
- At Caldris example: **~8,850 adventurers + ~8,850 hunters**
- **~4% of L are monster tamers/herders** (~23,600)
- Villains scale with **M** (they skim loot; they do not cull)
- Guild ranks fall off hard (factor 4 across 8 ranks). Most kill capacity is Bronze/Steel trash clears.

Full human formulas: `../Society/Population.md`.

### Monster-supply demand

Coin ladder is ×10: **1 LC = 10 SC**, **1 SS = 10 LC**.

| Kill component | Value |
|---|---|
| Ear (locked) | 5 LC = 50 SC |
| Rice stone share (2 SS × 1/5 drop, locked) | 4 LC = 40 SC |
| Parts H (locked) | 3 LC = 30 SC |
| **Kill value G** | **12 LC = 120 SC** |

```
Kills_per_hunter_yr = 361 × w ÷ G
Hg = Hunters + Bronze_adventurers
Hunter_kills_yr = Hg × Kills_per_hunter_yr
```

Unskilled wage **w** = 5–10 LC/day → about **150–300** kills/hunter/yr.

| Caldris (1M people) | Low wage | High wage |
|---|---|---|
| Goblin-grade killers (hunters + Bronze adventurers) | ~15,500 | ~15,500 |
| **Required hunter kills / year** | **~2.3 million** | **~4.7 million** |
| Stones / year (~1/5 drop) | ~0.47M | ~0.93M |

**Demand is a loot-economy ceiling.** Part-time hunters, mixed income and edible meat lower sold goblin kills. Soldiers, militia, caravan guards and farmers raise total removals. This file solves for **sold hunter kills** and treats other removals separately.

**H = 30 SC** is carried mostly by goblin blood (low-grade conduction ink, rune priming, stone-socket paste). Undead parts sit below that. Edible monsters add meat on top of H.

### Locked ecology rules

- **Never eaten:** goblins / goblin-kin, undead. Edible low monsters: meat good, **spoils fast**
- Stones: **size = level**; wild drop ~1/5; evolved always
- Kill XP: `50 × L × RaceMult` (goblin = 1.0 baseline)
- Mana law: concentration **C**, absorption **A = √C**
- **Most monsters breed very fast and need constant culling (quelling) to avoid disaster**

---

## Part 2. World frame (unlocked reference)

Only Caldris-scale figures feed the story.

| Layer | Area |
|---|---|
| Total land | 149M km² |
| Ice caps | ~16M km² |
| Extreme terrain | ~33M km² |
| **Usable land** | **~100M km²** |

- World population ~800M → ~800 kingdoms at 1M each
- Human density ~15 people/km²
- Caldris area ~67,000 km²
- Held kingdoms ~55M km²; unclaimed usable wildland ~45M km²

---

## Part 3. Kill demand by M

```
Hg_per_M = 10,333 per million people   // 15,500 ÷ 1.5 at Caldris
Hunter_kills_yr ≈ Hg_per_M × M × (P / 1e6) × (150 to 300)
```

| Zone | M | Hunter kills/yr per 1M people | Kills/km²/yr (at 15 people/km²) |
|---|---|---|---|
| Heartland | 0.5 | 0.78–1.55M | 12–23 |
| Normal | 1.0 | 1.55–3.1M | 23–46 |
| **Caldris** | **1.5** | **2.3–4.7M** | **35–70** |
| Frontier | 2.0 | 3.1–6.2M | 46–93 |
| Dungeon region | 3.0 | 4.65–9.3M | 70–139 |

---

## Part 4. The Breeder's Bargain

A creature can keep its **strength**, its **wits** or its **numbers**. It cannot keep all three.

- **Mana can pay for a body.** Dense mana builds bone and muscle fast.
- **Mana cannot pay for a mind.**
- **Mana-built strength is borrowed.** It lasts only while the creature stays in dense mana or eats mana-rich food.

| Tier | Strength (no mana) | Wits kept | Gestation | Young per birth | Births/yr | First breeding | λ ideal | r ideal |
|---|---|---|---|---|---|---|---|---|
| None | Full | 100% | ~165 days | 1 | ~0.7 | ~5 yr | 1.17 | 0.16 |
| Slight | ~80% | ~75% | ~120 days | 1–2 | 1 | ~3 yr | 1.35 | 0.30 |
| Moderate | ~50% | ~50% | ~90 days | 2–3 | 2 | ~1 yr | 2.6 | 0.96 |
| Severe | ~20% | ~25% | 30–45 days | 4–6 | 4–6 | ~0.5 yr | ~18 | 2.9 |

- Strength and wits are **percentages of the ancestor** (monkey 25% ≈ rabbit; near-human 25% ≈ crude tool user).
- **Working Severe rate in held land: r_net = 2.3** (λ ≈ 10). Ideal r 2.9 minus natural death ~0.6/yr. Predators and hunting are separate removals.
- Bargain strength does **not** map to RaceMult.

Only **Severe** needs constant quelling. Moderate held by predators + ordinary hunting. Slight / None barely move in one bad season.

### Mana refund

**One strength step per doubling of A = √C** (C ×4 per step). Wits never refund.

| C | A | Refund steps | Severe strength | Where |
|---|---|---|---|---|
| 1 | 1 | 0 | 20% | Lowland, open sky |
| 1.5 | 1.2 | 0.3 | ~28% | Caldris hills |
| 2 | 1.4 | 0.5 | ~35% | High passes |
| 4 | 2 | 1 | 50% | Highest Earth-like peaks |
| 16 | 4 | 2 | 80% | Thick ground (spiritual, dungeon mouth, bloom + altitude, mid floors) |
| 64 | 8 | 3 | Full | Local anomalies (Albrook fire), deep floors |

Open-sky altitude tops out near **C ≈ 4**. Above that needs a thickener. Dungeon `C` from `../Geography/Dungeons.md` plugs in directly.

**Dispersal (unlocked default):**

```
Refund_steps_lost_per_week = 0.5 × (carried_steps − local_steps)
```

Dungeon-only monsters use a faster rate (≥1.5).

---

## Part 5. Containment

### Carrying capacity and M

**Lock: M is the chosen input** (`Population.md`). Bridge one way:

```
K = 100 × M          // goblin-grade carrying capacity per km²
```

Consistency check (not a second knob):

```
K_food × A × E  must equal  100 × M
```

| Term | Meaning | Typical |
|---|---|---|
| K_food | Food capacity, temperate farm/forest | ~100/km² |
| A | √C | ≥1 |
| E | Wildland edge exposure | 1.0 interior; 1.3–2.0 border |

Caldris: M = 1.5 → **K = 150/km²**. Check: 100 × 1.2 × 1.25 = 150.

### Holding density

```
N_star = K × (1 − C_cull / r)     // density held (/km²)
Removals_yr = C_cull × N_star × Area_km2
Max_wild_production = (r × K / 4) × Area_km2   // at 50% of K
```

Use **r = r_net = 2.3** for Severe in held land.

| Cull (C_cull ÷ r) | Density held | Share of K | Caldris standing (67k km²) | Wild removal/yr |
|---|---|---|---|---|
| 0.9 | 15/km² | 10% | 1.0M | 2.1M |
| 0.8 | 30/km² | 20% | 2.0M | 3.7M |
| 0.7 | 45/km² | 30% | 3.0M | 4.9M |
| 0.5 | 75/km² | 50% | 5.0M | 5.8M |

**Knife edge:** ~11% drop in removal effort ≈ doubles density and hunter haul. Guilds profit from under-hunting; crown needs over-hunting. Ear bounty (5 LC = 42% of G) is a crown policy lever.

**Predators** take ~20–40% of total **wild** removal, on top of hunter kills. Wage demand fixes hunter kills. Held density is an output of hunters + predators (+ dungeon income).

**Dungeons** let the crown keep density low while hunters still earn. At 10–20% of K and high wage, dungeons supply **28–73%** of hunter income.

### Lapse (culling stops)

r = 2.3 from 10% of K: ~17% at 3 months, ~26% at 6 months, ~53% at 1 year, ~92% at 2 years. War that cuts 20% of removal effort settles near ~28% of K within about a year.

---

## Part 6. Tier composition (held land at 10% of K)

| Tier | Typical | Share | Caldris count | Density |
|---|---|---|---|---|
| Severe | Goblin, dungeon rat | ~88% | ~1.0M | ~15/km² |
| Moderate | Spiked boar, mid beasts | ~10% | ~115,000 | ~1.7/km² |
| Slight | Wereboar, elite | ~1% | ~11,500 | ~1 per 6 km² |
| None (apex, risen) | Apex, evolved leaders | ~0.1% | ~1,100 | ~1 per 60 km² |

Named wild vs dungeon:

| Monster | Wild density | Dungeon role |
|---|---|---|
| Spiked boar | ~0.3/km² | Floor-1 trash |
| Wereboar | ~1 per 75 km² | Floor-3 elite |

### Evolution

Evolution moves one bargain tier up: permanent strength, wits back, slower breeding, always drops a stone. Held land ~0.1% evolved; wildlands ~0.5%. Quelling is evolution control.

### Goblin society

Severe goblin ≈ 25% of a near-human mind: crude weapons, nests, ambush, pack follow; no planning past the day. Pack leader ~1/20–40 (veteran). Chief/shaman evolved ~1/500–1,000.

---

## Part 7. Dungeons

Core pays build cost. No womb. Fully mana-built; weaken fastest outside. Stable kill volume vs wild flood.

```
Y = parties_per_day × kills_per_party_visit × 361
Dungeon_count ≈ Dungeon_kills_needed ÷ Y
```

**Pin Y from Carwen / Albrook chapter traffic first.** Count follows Y.

---

## Part 8. Species placement

| Monster | Tier | Mana | Notes |
|---|---|---|---|
| Dungeon rat (wild) | Severe | C 1 | Pure flood |
| Goblin | Severe | C 1–1.5 → 20–30% strength | Veterans + evolved chiefs |
| Mountain goblin | Severe | C 2–4 → 35–50% (80% on thick C≈16) | Weakens in ~10 days downhill |
| Spiked boar | Moderate | C 1–4 | ~0.3/km² wild |
| Wereboar | Slight | Varies | ~1/75 km² wild |
| Needle worm/moth | Egg-layer | n/a | Beyond table |
| Myrmeke | Eusocial | n/a | Colony bypasses bargain |
| Albrook fire types | Zone-tied | C 64+ anomaly | Collapse in 2–3 weeks elsewhere |

---

## Part 9. Stone flow (Caldris)

0.47–0.93M rice stones/yr ≈ 0.5–0.9 per person/yr ≈ **~1% of labor income**. Consumable sink (lamps, rail, ink), not a flood.

---

## Part 10. Field notes

### The Breeder's Bargain

Among the beasts that have made the bargain, the pattern holds so reliably it may as well be law. A creature can keep its strength, its wits or its numbers. It cannot keep all three.

The price is paid first in the womb. A large brain is the slowest thing a mother builds and no amount of hunger or urgency can hurry it. Heavy bone and dense muscle come next. Strip those away and the body no longer needs to carry its young for half a year. It builds smaller, simpler offspring and pushes them into the world unfinished.

The measure is always the ancestor, never the beast beside it. A trade that leaves a monkey as dim as a hare leaves the goblin, whose forebears were nearly as clever as men, with a quarter of a man's mind. That is enough to lash a blade to a stick, dig a warren and follow whoever has lived longest. It is not enough to plan past nightfall or to teach anything the next litter will keep.

| Degree of trade | Strength kept | Wits kept | Troop monkey | Goblin | Gestation | Young/birth | Births/yr |
|---|---|---|---|---|---|---|---|
| None | Full | Full | Full primate | Near-human ancestor | ~165 d | 1 | ~0.7 |
| Slight | ~80% | ~75% | Dull monkey | Chief / shaman band | ~120 d | 1–2 | 1 |
| Moderate | ~50% | ~50% | Goat-like | Cunning raider | ~90 d | 2–3 | 2 |
| Severe | ~20% | ~25% | Rabbit-like | Crude tool user | 30–45 d | 4–6 | 4–6 |

### The Mana Debt

Where the air runs thick with mana a breeder can borrow back the strength it gave away. The loan buys flesh only. Wits never refund. Bring a mountain goblin to the lowlands and it sickens within days; by the second week it matches valley kin. High tribes raid in short seasons and fight each other for thick ground harder than they fight men. The risen escape the bargain by surviving long enough to keep mana; every risen began as one face in a flood a Bronze hunter failed to thin.

---

# Given area worksheet

Use this to size **any patch** (barony, forest, dungeon region, whole kingdom).

## Inputs

| Symbol | Meaning | How to pick |
|---|---|---|
| Area | km² of the patch | Map / estimate |
| P | People living in the patch | See human population below |
| M | Monster pressure | 0.5 / 1 / 1.5 / 2 / 3 (or interpolate) |
| W | War state | 1 peace, 2 border, 3 full |
| f_held | Fraction of K actually held | Crown safe **0.10–0.20**; neglected **0.30+** |
| C_amb | Ambient mana concentration | Open sky 1–4; thickeners / dungeon from `ManaConcentration` + `Dungeons` |
| pred | Predator share of **wild** removal | Default **0.30** (band 0.20–0.40) |
| w | Unskilled day wage LC | 5–10 |
| Y | Dungeon kills/yr per working dungeon | Pin from story traffic; default planning **50,000** |
| N_dung | Working dungeons in the patch | Count, or solve for later |

## A. Human population

Pick **one**:

```
// Density method (Caldris-like held land)
P = 15 × Area

// Share of a known kingdom
P = P_kingdom × (Area / Area_kingdom)

// Direct census / story number
P = given
```

Then run `../Society/Population.md` on **P, M, W**, or the compact band below (peace, Caldris-like nobility/villain share):

```
L ≈ 0.59 × P
Hunters = Adventurers = 0.01 × L × M
Bronze_adventurers ≈ 0.75 × Adventurers
Hg = Hunters + Bronze_adventurers
Tamers ≈ 0.04 × L
Villains ≈ 0.004 × (P − nobility) × M ≈ 0.004 × 0.99 × P × M
Under_arms_peace ≈ 0.0082 × P     // knights+army+guard+royal at W=1, Caldris-like
```

For exact nobility, army, mage and rank tables, use the full Population file on P.

**Settlements (same shares as Population):**

```
Urban U = 0.25 × P
Villages_pop = 0.75 × P
N_cities ≈ max(1, round(0.10 × P / 40000))   // skip if P small; use size ranges in Population
N_towns  ≈ max(1, round(0.11 × P / 10000))
N_villages ≈ max(1, round(0.75 × P / 500))
```

## B. Monster carrying capacity and standing stock

```
K = 100 × M                         // /km²
A_mana = √C_amb
// consistency: K_food × A_mana × E ≈ K  (K_food~100, E from border)

Standing_total = f_held × K × Area   // all tiers, goblin-grade mass units
```

**Tier breakdown (held land):**

```
N_severe   = 0.88  × Standing_total
N_moderate = 0.10  × Standing_total
N_slight   = 0.01  × Standing_total
N_apex     = 0.001 × Standing_total
N_evolved  ≈ 0.001 × N_severe       // held land; use 0.005 in wildlands
```

**Named wild densities (optional overlay; do not double-count Severe):**

```
N_spiked_boar_wild ≈ 0.3 × Area_forest_edge
N_wereboar_wild    ≈ Area / 75
```

**Severe strength at this ambient:**

```
Refund_steps = log2(A_mana) = 0.5 × log2(C_amb)
Strength_severe ≈ 0.20 × 2^Refund_steps   // cap at 1.0; use Part 4 table
```

## C. Kill demand and presence feel

```
G = 12                         // LC per goblin-grade kill
Kills_per_hunter = 361 × w / G
Hunter_kills_yr = Hg × Kills_per_hunter
Stones_yr ≈ Hunter_kills_yr / 5
```

**Wild removal at held density** (Severe r_net = 2.3):

```
C_cull = r_net × (1 − f_held)
Wild_removals_yr = C_cull × (f_held × K) × Area
// equivalent: Wild_removals_yr = r_net × f_held × (1 − f_held) × K × Area
```

**Split:**

```
Predator_kills_yr = pred × Wild_removals_yr
Hunter_wild_yr = (1 − pred) × Wild_removals_yr
Dungeon_kills_needed = max(0, Hunter_kills_yr − Hunter_wild_yr)
N_dung_needed = Dungeon_kills_needed / Y
```

**Presence readouts (use in prose):**

| Metric | Formula | Feel |
|---|---|---|
| Standing density | `f_held × K` | Goblin-grade bodies/km² |
| Hunter pressure | `Hunter_kills_yr / Area` | Sold kills/km²/yr |
| Wild kill pressure | `Wild_removals_yr / Area` | Total wild deaths/km²/yr |
| Road danger | rises with M and f_held | Solo travel unsafe when M≥1 outside walls |
| Strength feel | Strength_severe from C_amb | Valley soft flood vs mountain hard flood |

## D. Worked micro-examples

### Carwen farm-forest fringe (planning sketch)

```
Area = 200 km², M = 1.5, f_held = 0.15, C_amb = 1.2, w = 5, pred = 0.3
P = 15 × 200 = 3,000
L ≈ 1,770
Hunters = Adventurers ≈ 0.01 × 1770 × 1.5 ≈ 27 each
Hg ≈ 27 + 0.75×27 ≈ 47
Hunter_kills_yr ≈ 47 × 150 ≈ 7,050
K = 150
Standing_total = 0.15 × 150 × 200 = 4,500
N_severe ≈ 3,960
Wild_removals_yr = 2.3 × 0.15 × 0.85 × 150 × 200 ≈ 8,800
Hunter_wild ≈ 6,200
Dungeon_kills_needed ≈ max(0, 7050 − 6200) ≈ 850
```

### Whole Caldris check

```
Area = 67,000, P = 1e6, M = 1.5, f_held = 0.10–0.20, w = 5–10
→ Hunter_kills_yr = 2.3–4.7M (matches Population)
→ K = 150, Standing at 10% = 1.0M Severe-dominated
```

## Open

- Pin Carwen / Albrook **Y** from chapter traffic
- World-frame digits stay unlocked
- Dispersal rate stays unlocked default
