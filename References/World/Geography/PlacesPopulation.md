# Places Population

> **Planning estimates** (unlocked digits). Method: `../Fauna/MonsterPopulation.md` worksheet + `../Society/Population.md`. Lean place list: `Places.md`. Fat notes: `PlacesDesign.md`.

Story locations sized for reference. Settlement **P** is people inside/around the named place. **Catchment** is the farm / forest / hunt ground that feeds that place. Round numbers on purpose. When a beat needs a hard count, pin it here and thin into `Places.md`.

**Shared Caldris defaults unless noted:** year 361; wage band 5–10 LC; G = 12 LC/kill; Bronze ≈ 75% of adventurers; `K = 100 × M`; Severe share ≈ 88% of standing stock; r_net = 2.3; predator share ≈ 30% of wild removal.

```
Hunters = Adventurers = 0.01 × L × M
L ≈ 0.59 × P
Hg ≈ Hunters + 0.75 × Adventurers
Hunter_kills_yr ≈ Hg × (150 to 300)     // w = 5–10 LC
Standing = f_held × K × Area_catchment
```

---

## Kingdom of Caldris (baseline)

| Input | Value |
|---|---|
| P | **1,000,000** (Population example) |
| Area | **~67,000 km²** |
| M | **1.5** |
| W | 1 peace (typical) |
| f_held | **0.10–0.20** crown-safe |
| C_amb | **1–1.5** lowland |

| Output | Low / high |
|---|---|
| L | ~590,000 |
| Hunters / adventurers | ~8,850 each |
| Hg (goblin-grade killers) | ~15,500 |
| Hunter kills/yr | **2.3–4.7M** |
| K | 150/km² |
| Standing at 10% K | **~1.0M** (≈880k Severe) |
| Standing at 20% K | **~2.0M** |
| Wild removals/yr at 10% K | ~2.1M |
| Dungeon kills needed (high wage, 10–20% K) | ~1.7–3.5M |

Neighbors (Alexandria, Bolia, Hatfordian Empire): not sized here.

---

## Arden estate / fief

Baron Wentworth knight house. Mansion, library, fields (Trox), mansion **training dungeon** (stocked goblins; not a public income dungeon).

| Input | Value |
|---|---|
| Estate household + servants | **~80–150** |
| Fief villages / farms (catchment people) | **~2,000–4,000** (use **3,000**) |
| Catchment Area | **~200 km²** (P/15) |
| M | **1.2** (mid-kingdom, watched lands) |
| f_held | **0.12** |
| C_amb | **1** |

| Output (P = 3,000) | Value |
|---|---|
| L | ~1,770 |
| Hunters / adventurers | ~21 each (few guild; mostly local hunters / men-at-arms) |
| Hg | ~37 |
| Hunter kills/yr | **~5,500–11,000** |
| K | 120/km² |
| Standing stock | ~0.12 × 120 × 200 ≈ **2,900** (≈2,500 Severe) |
| Training dungeon stock | **dozens** of pen goblins (story weekly clears); not part of wild standing |

**Nearby monsters:** farm-edge goblin packs, common wildlife, rare moderate threats. West/estate woods quieter than Carwen forest. Solo road still risky; caravan not required on short estate lanes.

---

## Lustile (named; not visited early)

Academy city (arts / weaponsmith / mage). Safe-path option.

| Input | Value |
|---|---|
| City P | **~30,000–40,000** (use **35,000**) |
| Catchment Area | **~2,300 km²** |
| M | **1.0** (safer heartland feel) |
| f_held | **0.10** |
| C_amb | **1** |

| Output (P = 35,000) | Value |
|---|---|
| L | ~20,700 |
| Hunters / adventurers | ~207 each |
| Hg | ~360 |
| Hunter kills/yr | **~54k–110k** |
| K | 100/km² |
| Standing at 10% K | **~23,000** (≈20k Severe) |

**Nearby monsters:** lowland flood at heartland density; academy city leans on hired clears and regional dungeons elsewhere. No story dungeon at Lustile.

---

## Carwen (walled adventurer town)

Small walled town, gate, city lord castle road, guild, inn, train station. Goblin forest + farms. Active public dungeon.

| Input | Value |
|---|---|
| Town P | **~8,000–12,000** (use **10,000**) |
| Catchment (farms + goblin forest) | **~400–600 km²** (use **500 km²**) |
| Catchment people (incl. town) | **~7,500–10,000** rural + town ≈ treat hunt math on **P = 10,000** town-centered |
| M | **1.5** |
| f_held | **0.15** (dungeon + hunters keep it middling) |
| C_amb | **1–1.2** |
| Working dungeons | **1** (Carwen Dungeon) |

| Output (P = 10,000) | Value |
|---|---|
| L | ~5,900 |
| Hunters / adventurers | ~89 each |
| Hg | ~155 |
| Hunter kills/yr | **~23k–47k** |
| K | 150/km² |
| Standing stock | 0.15 × 150 × 500 ≈ **11,000** (≈9,700 Severe / goblin-grade) |
| Spiked boar wild (forest edge ~100 km²) | ~30 |
| Wereboar wild | ~7 in whole catchment (rare event) |
| Evolved / chiefs | ~10 Severe-evolved in catchment |
| Wild removals/yr | ~2.3 × 0.15 × 0.85 × 150 × 500 ≈ **22,000** |
| Hunter wild share (~70%) | ~15,000 |
| Dungeon kills needed | **~8k–32k**/yr depending on wage |
| Implied Y if 1 dungeon fills the gap | **~20k–50k**/yr (pin from chapter traffic) |

### Carwen cabin fringe (~30 min coach)

| Input | Value |
|---|---|
| Residents | **1** (Roland) + occasional visitors |
| Patch Area | **~20–40 km²** of forest/farm edge (use **30 km²**) |
| M | **1.5** |
| f_held | **0.18** (less patrol than town wall) |
| C_amb | **1** |

| Output | Value |
|---|---|
| Standing on patch | 0.18 × 150 × 30 ≈ **800** (≈700 Severe) |
| Feel | Goblin packs common; spring/animals west; few scavengers in west woods (story). Cabin is not safe solo long-term without culling. |

### Carwen Dungeon (spawn, not wild)

| Floor band | Standing feel (planning) | Notes |
|---|---|---|
| Entry maze | **dozens** of dungeon rats cycling | Filter; weaker than goblin |
| Floor 1 Emerald Wilderness | **hundreds** of Spiked Boars on routes (km-scale biome) | Steel hunting ground; artificial sun |
| Floor 2 | Boar packs + **Needle Worms** (dozens–hundreds) | Higher multi-spawn |
| Floor 3 | **Wereboars** (scarce elites) + Needle Moths | Vicious multi-type |
| Floors 4–9 | Unsized early | |
| Floor 10 boss | **1** + adds; week respawn | Guild appointment |

Dungeon standing is core-budgeted and respawns; do not add to wild `Standing`. Upper floors crowded with Bronze/Steel parties.

---

## Edelgard (craft / mountain city)

No local public dungeon. Mines, gorge, dwarves/gnomes, merchant council. Adventurers as hired muscle / wild clears. Colder altitude.

| Input | Value |
|---|---|
| City P | **~45,000–70,000** (use **55,000**) |
| Catchment Area | **~3,000–4,000 km²** mountain/valley (use **3,500 km²**) |
| M | **1.7** (wild work without a town dungeon) |
| f_held | **0.12** |
| C_amb | **1.5–2.5** (altitude; peaks toward 4) |

| Output (P = 55,000) | Value |
|---|---|
| L | ~32,500 |
| Hunters / adventurers | ~550 each |
| Hg | ~960 |
| Hunter kills/yr | **~145k–290k** |
| K | 170/km² |
| Standing stock | 0.12 × 170 × 3500 ≈ **71,000** (≈62k Severe) |
| Mountain goblin strength | **~35–50%** at C 2–4; **~80%** only on thick ground |
| Wild wereboar-scale elites | ~50 in catchment |
| Dungeon kills needed | **high** (no local dungeon) → met by **hired expeditions**, regional clears, imported stone/loot economy |

**Districts (people shares of city, rough):**

| District | Share | People (at 55k) |
|---|---|---|
| Hightown | ~10% | ~5,500 |
| Craft / market core | ~40% | ~22,000 |
| Southtown / lower | ~25% | ~14,000 |
| Other (temple, yards, rail) | ~25% | ~13,500 |

Rat Plaza / Thieves Guild: hundreds of actives, not a census district.

### Manstos Grotto (near Edelgard)

Iron mine + Myrmeke breach. Not a continuous wild standing stock.

| Item | Planning |
|---|---|
| Mine workers (when open) | **~100–300** |
| Expedition (Ch 27–32) | **~20** adventurers under Wells |
| Myrmeke workers | **swarm: hundreds–thousands** in nest |
| Soldiers (horse-sized, past L50) | **dozens** in a mature nest |
| Queen | **1** (L163 story) |

Colony bypasses Breeder's Bargain; treat as eusocial flood until collapsed.

---

## Luden (southern port city)

Caravan / sail hub to Dragnis.

| Input | Value |
|---|---|
| City P | **~35,000–55,000** (use **45,000**) |
| Catchment Area | **~2,500 km²** coast/plain |
| M | **1.4** |
| f_held | **0.12** |
| C_amb | **1–1.3** |

| Output (P = 45,000) | Value |
|---|---|
| L | ~26,600 |
| Hunters / adventurers | ~370 each |
| Hg | ~650 |
| Hunter kills/yr | **~98k–195k** |
| K | 140/km² |
| Standing stock | 0.12 × 140 × 2500 ≈ **42,000** (≈37k Severe) |

**Nearby monsters:** coastal/plain goblin-grade flood; bandit pressure on roads (story Ch 65). Sail gaps > monster density for island hop.

---

## Dragnis Island

Large southern Caldris island, aristocrat Duke, central volcano, S-rank main dungeon, side dungeons, export boom.

| Input | Value |
|---|---|
| Island P | **~80,000–150,000** (use **120,000**) |
| Island Area | **~8,000–15,000 km²** (use **12,000 km²**) |
| M | **2.0–2.5** average (dungeon-region pull; coast milder) |
| f_held | **0.15** coasts/valleys; wild interior higher |
| C_amb | Coast **1–1.5**; volcanic / dungeon **4–64** local |

| Output (P = 120,000, M = 2.2) | Value |
|---|---|
| L | ~71,000 |
| Hunters / adventurers | ~1,560 each |
| Hg | ~2,700 |
| Hunter kills/yr | **~405k–810k** |
| K | 220/km² |
| Standing if 15% held on half the island (6,000 km²) | 0.15 × 220 × 6000 ≈ **200,000** |
| Wildland remainder | saturated; spillover into valleys |
| Working side dungeons | **several** toward main Infernal Dragon dungeon |
| Main dungeon | **1** S-rank (dragon unbeaten); magus-tower barrier |

### Unnamed closest island port (Ch 67)

| Input | Value |
|---|---|
| Town P | **~3,000–6,000** (use **4,000**) |
| M | **1.8** |
| Guild | **none** (travel agency) |

Overnight stop; caravan inland to Albrook. Monsters: coastal Severe flood + road risk; no local guild cull engine.

---

## Albrook (boom town)

Valley by months-old volcanic side dungeon. Wall going up; absentee noble; commoner mayor. Early vs ~1 year later (Ch 77).

| Input | Early (Ch 68–73) | Mature (~Ch 77) |
|---|---|---|
| Town P | **~2,500–4,000** (use **3,500**) | **~6,000–10,000** (use **8,000**) |
| Valley catchment | **~250 km²** | **~300 km²** |
| M | **2.5–3.0** (dungeon region) | **2.5** |
| f_held | **0.20** (boom cull + dungeon) | **0.15** |
| C_amb valley | **1.5–3** | same |
| C at dungeon / fire site | **16–64+** anomaly | same |
| Working dungeons | **1** (Albrook) + link risk to main | same |

| Output | Early (P=3,500, M=2.8) | Mature (P=8,000, M=2.5) |
|---|---|---|
| L | ~2,070 | ~4,720 |
| Hunters / adventurers | ~58 each | ~118 each |
| Hg | ~100 | ~205 |
| Hunter kills/yr | **~15k–30k** | **~31k–62k** |
| K | 280/km² | 250/km² |
| Standing stock | 0.20 × 280 × 250 ≈ **14,000** | 0.15 × 250 × 300 ≈ **11,000** |
| Farmhouse patch (~½ acre + 40 min out) | local standing on ~10 km² ≈ **hundreds** of Severe-grade if unculled | wall + shed; still fringe risk |

**Nearby monsters:** Fire Slimes, Fiery Skeletons, Baby Salamanders (dungeon); valley wild Severe flood under volcanic pressure; thieves in town as boom crime (not monster census).

### Albrook Dungeon

| Band | Planning standing / traffic |
|---|---|
| Safe hub | No monsters leaving bounds |
| Floors 1–3 | Crowded Bronze/Steel; Fire Slimes, Fiery Skeletons (cap ~L10), Baby Salamanders; **hundreds** cycling |
| Mid (~4–6) | Crimson Giant Rats, harder salamanders; **hundreds** |
| Floor 7 | Trap rooms + Lesser Troglodytes |
| Toward 10 | ~L50 / some T2; mining section |
| Link risk | Spill from Infernal Dragon dungeon if connection real |

Pin **Y** from party traffic before locking Caldris-wide dungeon counts.

---

## Hatfordian–Caldris border fortress (Ch 67)

Black-stone fortress between peaks. Ceasefire. Not a civilian town.

| Input | Value |
|---|---|
| Garrison | **~500–2,000** (use **1,000** rotating) |
| Catchment | mountain pass **~100 km²** watched |
| M | **2.0** frontier |
| f_held | **0.25** on the pass only |
| C_amb | **2–4** |

| Output | Value |
|---|---|
| Standing on watched pass | 0.25 × 200 × 100 ≈ **5,000** |
| Feel | Mountain goblin / frontier flood; patrols and war leftovers matter more than hunter wage math |

---

## Stegend (named only)

City on a convoy-protection listing (too far for early Roland). No chapter visit.

| Input | Planning placeholder |
|---|---|
| P | **~20,000–40,000** |
| M | **1.3–1.6** |
| Role | Inland city on a trade road; size when a beat goes there |

---

## Quick comparison

| Place | P (use) | M | Catchment km² | Standing (f_held band) | Hunter kills/yr | Local dungeon |
|---|---|---|---|---|---|---|
| Caldris | 1,000,000 | 1.5 | 67,000 | 1.0–2.0M | 2.3–4.7M | many |
| Arden fief | 3,000 | 1.2 | 200 | ~3k | 6–11k | training pen only |
| Lustile | 35,000 | 1.0 | 2,300 | ~23k | 54–110k | none on-page |
| Carwen | 10,000 | 1.5 | 500 | ~11k | 23–47k | yes |
| Carwen cabin patch | 1 | 1.5 | 30 | ~800 | n/a | no |
| Edelgard | 55,000 | 1.7 | 3,500 | ~71k | 145–290k | none (wild/mine) |
| Luden | 45,000 | 1.4 | 2,500 | ~42k | 98–195k | none on-page |
| Dragnis Island | 120,000 | 2.2 | 12,000 | ~200k held valleys | 405–810k | main + sides |
| Island port | 4,000 | 1.8 | ~250 | ~10k | 10–20k | no guild |
| Albrook early | 3,500 | 2.8 | 250 | ~14k | 15–30k | yes |
| Albrook mature | 8,000 | 2.5 | 300 | ~11k | 31–62k | yes |
| Border fortress | ~1,000 garrison | 2.0 | 100 | ~5k on pass | garrison cull | no |

---

## Open

- Pin Carwen / Albrook **Y** and town **P** when a chapter gives a harder cue (guild lines, gate counts, map scale)
- Absorb chosen digits into lean `Places.md` only when a beat needs them
- Stegend / capital / Duke seat remain placeholders
