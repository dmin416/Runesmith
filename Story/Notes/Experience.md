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
| **7** | Last estate-pen goblins (already Mage; not pre-class) | Post-ascension |

Ch 6: weekly one-on-ones after the 9th birthday. Locked count **55** estate L1s after bravery (year of weeks plus a few extras) so the half-bank lands L3 under `500 × L`.

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
| 7 | Last estate training goblins (Mana Bolt + sword) | not shown | Already Mage; clears the pen |
| 9 | Forest goblins L3/L4/L5 | 52 / 53 / 53 / 54 | On-page; Mage L5→L6 |
