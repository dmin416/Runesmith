# Experience

Running XP log. Kill formula and curve: `References/Levels.md`. Status screens: `Status.md`.

**Common goblin:** `49 + level` (RaceMult 1.0). Other races: `(49 + level) × RaceMult`.

**Pre-class bank:** XP before first ascension banks and applies later with a **½ penalty**. One-time only (first class). Does not refill for later class changes.

## Where it sits in the chapters

| Ch | On-page | XP / bank |
|---|---|---|
| **4** | Bravery test: Goblin L1 kill + First Kill | **50 + 200 = 250** banked |
| **4→5** | Off-page (named in Ch 6): estate one-on-one Goblin L1 fights after age 9 (**55** kills) | **55 × 50 = 2750** |
| **5** | Ascension → **Mage L1**. Bank not applied on-page yet | Still banked |
| **6** | Bank applied (½) → **Mage L3** empty | **1500** spent |
| **6→7** | Post-Mage estate weeks: fights escalate to **2× L1**; ~**3 months** | **25 × 50 = 1250** toward L4 |
| **7** | Last estate-pen pair (already Mage; counted in the 25) | Still L3; bar **1250 / 1500** |
| **8** | Guild registration; no fights | Still Mage L3; bar unchanged |
| **9** | Forest hunt; levels on the **54** kill | **1250 + 263** → L4 overflow **13**; +**105** → **118 / 2000** |
| **9.5** | Not written yet | — |
| **10** | **Timeskip** ~3 months of Carwen goblin grind → **Mage L20** | Off-page levels; live sheet at the inn |

Ch 6: weekly one-on-ones after the 9th birthday. Locked count **55** estate L1s after bravery (year of weeks plus a few extras) so the half-bank lands L3 empty under `500 × L`. After Mage, weekly continues and turns to **two** L1s at a time for ~**3 months** (**25** kills including the Ch 7 finale) so the first Carwen hunt can finish L3→L4.

## Pre-class bank

| Ch | Source | XP | Bank after | Notes |
|---|---|---|---|---|
| 4 | Goblin L1 kill (49+1) | **50** | 50 | On-page; kill #1 |
| 4 | First Kill achievement | **+200** | **250** | On-page |
| 4–5 | Estate Goblin L1 × **55** | **2750** | **3000** | After bravery; total L1 kills **56** |
| 5–6 | Ascension + **½** → Mage L3 | **1500** applied | **0** | Empty bar at L3 |

**Full pre-class bank:** **3000 XP** → **1500** after half.

## Linear constant (locked)

```
XP_to_next(L) = 500 × L
```

| Step | Cost |
|---|---|
| L1→L2 | **500** |
| L2→L3 | **1000** |
| **Sum** | **1500** |

Curve tables: `Levels.md`.

## Post-ascension

| Ch | Source | XP | Notes |
|---|---|---|---|
| 6→7 | Estate weekly **2× Goblin L1** over ~3 months (**25** kills incl. Ch 7 pair) | **1250** | Fills L3 bar to **1250 / 1500**; no level-up yet |
| 7 | Last estate training pair (Mana Bolt eye + sword throat) | in the 1250 | Already Mage; clears the pen; no level-up line. **+1** rice-grain mana stone from the second |
| 9 | Forest goblins L3/L4/L2 then L4/L5 then L3/L4 | 52 / 53 / 51 / 53 / 54 / 52 / 53 | On-page; **1250 + 263** crosses 1500 on the **54** (Mage **L3→L4**, overflow **13 / 2000**); +**105** noise kills → **118 / 2000** |
| 9.5 | Not written yet | — | — |
| 10 | Carwen goblin grind timeskip (~3 months) | off-page | Ends **Mage L20** on the inn sheet |

`XP_to_next(3) = 1500`. Entering Ch 9 with **1250** keeps the level-up on the **54** XP kill. Overflow after level-up is **(1250 + 263) − 1500 = 13** into the L4 bar (`XP_to_next(4) = 2000`).
