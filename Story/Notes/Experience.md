# Experience

Running XP log. Kill formula and curve: `References/Levels.md`. Status screens: `Status.md`. Coin / stones: `Items.md`, `References/Economy.md`.

**Common goblin:** `49 + level` (RaceMult 1.0). **Dungeon rat:** `9 + level`. **Needle Worm:** `24 + level`. **Needle Moth:** `99 + level`. **Spiked Boar:** `499 + level`. **Wereboar:** `999 + level`. **People** (classed races): `50 × overall level` (Ch 14 L55 pool **2750**; Roland **479**). Other monster races: `(49 + level) × RaceMult`.

**Pre-class bank:** XP before first ascension banks and applies later with a **½ penalty**. One-time only (first class). Does not refill for later class changes.

## Goblin kill totals (locked)

| Span | Kills | Running |
|---|---|---|
| Ch 4 bravery | **1** | 1 |
| Ch 4→5 estate 1v1s | **55** | **56** |
| Ch 6→7 estate Mage pairs | **25** | **81** |
| Ch 9 forest day | **7** | **88** |
| Ch 9.5 Carwen grind | **1,481** | **1,569** |
| Ch 10 nest opener | **7** | **1,576** |

Ch 9.5 = L4→L20 kill volume at matched-goblin pace (~**16–17**/day over ~**90** days). Spell/skill rank XP still lands (~**13.4k** after kill XP) but does **not** cut the kill count.

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
| **9.5** | **1,481** matched goblins → **Mage L20** | Month beats **M1 ~L11–12**, **M2 ~L16–17**, **M3 → L20**. Kill XP ~**78.5k**; spell/skill ranks fill the rest (~**13.4k**) |
| **10** | Nest opener + present day → **Mage L20** | **+7** kills (**1** matched / **6** slightly lower); **+2** rice-grain stones; ear turn-in **+35 LC** → pouch **6,035**; inn sheet |
| **11** | First dungeon day + trial weeks | On-page idle Spiked Boar **+5 XP** (**1%**). Day lock: **4** boars → **380** XP; share **+128** → pouch **6,163**. Trial **7** days: kill **+1,820** + Hands **L5→L6** (**~+100**) → bar **~2,774/10k** / pouch **~6,818** |
| **12** | Floor-2 Needle Worm pocket clear before tame | **12** worms **L16–L18** → **+492 XP** (**24 + level**); bar **~3,266 / 10,000**; still L20. Core worm kept alive for tame |
| **13** | Half-year Floor-3 → **Mage L25** | **1,102** kills; kill XP **48,726** + skill **3,608** = **52,334**; haul share **+9,116**; living+kit **−4,248** → pouch **11,641**; Calligraphy **L9**; **Basic Dodging → Dodging L6** |

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
| 9.5 | **1,481** matched forest goblins | ~**78,493** kill XP (×53 avg) | Enter **118 / 2000** at L4; need ~**91,882** to L20; spell/skill ranks supply ~**13,389**. Month beats M1 ~L11–12 / M2 ~L16–17 / **L20**. Goblin Hunter in M3 (past **1000** kills into the skip). Named late kill: **Goblin Shaman L23** (inside the 1,481) |
| 10 | Nest opener then inn sheet | at **L20** | **7** kills: **1×** matched (**69** XP) + **6×** slightly lower (~**L18–19**, ~**67–68** each) → ~**471–477** XP into the L20 bar. **+2** rice-grain stones (**286→288**; leaders stay **16**); ears **+35 LC** → pouch **6,035 LC**; boar leg (underseasoned, gamey). Plans last five to Mage cap then Mana Scribe |
| 11 | Dungeon rat + Spiked Boars (Emerald Wilderness) | at **L20** | On-page: idle first boar **+5 XP** (**1%**). Rat XP popup not shown. **Lock:** day **4** boars → **380** XP; share **+128 LC** → **6,163 LC**. Trial weeks (**7** more days / **28** boars): kill **+1,820 XP**; idle **Mana Hands** + Absorption + Sense while waiting → Hands **L5→L6** (**~+100** skill XP) → bar **~2,774 / 10,000**; share **+921** − living **266** → pouch **~6,818 LC**. Still L20. Shield L3 / Incantation L6 unchanged |
| 12 | Needle Worm pocket clear (before tame) | at **L20** | **12×** Floor-2 worms **L16–L18**; formula **24 + level**. On-page pops **41 / 42 / 40**; pocket total **+492 XP** → bar **~3,266 / 10,000**. One core-bearing worm left alive; taming begins |
| 13 | Half-year Floor-3 | **L20 → L25** | **1,102** kills (WB **120** / SB **78** / moth **228** / worm **416** / rat **260**); kill **48,726** + skill **3,608** = **52,334**; haul **+9,116**; living+kit **−4,248** → pouch **11,641 LC**. Skill ranks: `Skills.md` |

`XP_to_next(3) = 1500`. Entering Ch 9 with **1250** keeps the level-up on the **54** XP kill. Overflow after level-up is **(1250 + 263) − 1500 = 13** into the L4 bar (`XP_to_next(4) = 2000`).

## Ch 9.5 money / stones (locked with kills)

Goblin stone law: leaders **1/30** of kills; leader stone **1/3** of leaders (**5×** rice volume, **10 SS**); common rice-grain **1/5** of non-leaders (**2 SS**).

| Item | Amount |
|---|---|
| Enter pouch (end Ch 9) | **875 LC** |
| Ear bounty (**1,481 × 5 LC**) | **+7,405 LC** |
| Leaders in grind (**1,481 ÷ 30**) | **49** |
| Leader stones (**49 ÷ 3**) | **16** (kept; **10 SS** each if sold) |
| Non-leader kills | **1,432** |
| Rice-grain stones (**1,432 ÷ 5**) | **286** (kept; **2 SS** each if sold) |
| Lodging (**252 LC × 3** months) | **−756 LC** |
| Food (**breakfast 5 + dinner 5** × **90**; **3** jerky @ ~**2**) | **−906 LC** |
| Thick wool cloak (nice-ish, mattress/comforter) | **−300 LC** |
| Repairs / spare robe / early food-hunt tastes | **−318 LC** |
| **End pouch (into Ch 10)** | **6,000 LC** (**6 SG**) |
| Stones on person | **286** rice-grain + **16** leader |

Stone bank value if sold: rice **286 × 20 = 5,720 LC**; leader **16 × 100 = 1,600 LC**; total **7,320 LC** (~**7.3 SG**). Not sold in Ch 9.5.

## Ch 10 money / stones (nest opener)

| Item | Amount |
|---|---|
| Enter pouch (end Ch 9.5) | **6,000 LC** |
| Nest ear bounty (**7 × 5 LC**) | **+35 LC** |
| Nest stones | **+2** rice-grain (kept; no leader stone this nest) |
| **End pouch (into Ch 11)** | **6,035 LC** |
| Stones on person | **288** rice-grain + **16** leader |

## Ch 11 money (first party dungeon day)

On-page: equal money split after sales (no total printed). Locked with `Economy.md` Spiked Boar mat table (mid all-mats **78** LC/boar; leader stone **100** LC). Prose says “more” boars + “another” stone; day locked at **4** / **2**.

| Item | Amount |
|---|---|
| Enter pouch (end Ch 10) | **6,035 LC** |
| **4** Spiked Boars, mid mats | **~312 LC** team |
| **2** dungeon chest stones (sold) | **+200 LC** team |
| Team haul | **~512 LC** |
| Equal 4-way share (Roland) | **+128 LC** |
| **End pouch (after day 1)** | **6,163 LC** |
| Stones on person | **288** rice-grain + **16** leader (dungeon stones sold with the haul; personal bank unchanged) |

## Ch 11→12 trial weeks (locked)

**Span:** ~**2 weeks** between first dungeon day and the Iron Flagon binge (Ch 12). **7** more Floor-1 dive days (every other day). Still Emerald Wilderness Spiked Boars only (no deeper floors yet).

**Pace (per day, same butcher volume as day 1):** **4** Spiked Boars. Roland chips in less often than a full backline mage: **2** active (Mana Shield / real help → **125 XP** each) + **2** low/idle (**5 XP** each) → **260 XP**/day.

| Item | Amount |
|---|---|
| Dive days | **7** |
| Boars | **28** |
| Boar XP | **7 × 260 = 1,820 XP** |
| Enter L20 bar (after Ch 10 nest ~**474** + Ch 11 day **380**) | **~854 / 10,000** |
| End L20 bar (into Ch 12) | **~2,774 / 10,000** (kill **1,820** + Hands rank **~100**) |
| Class | Still **Mage L20** (no level-up; need **10,000** to L21) |

**Money** (mid mats **78**/boar; stone pace mid of Steel **5–10**/week × **2** weeks = **15** stones sold):

| Item | Amount |
|---|---|
| Enter pouch (after Ch 11 day 1) | **6,163 LC** |
| Mats (**28 × ~78**) | **~2,184 LC** team |
| Stones (**15 × 100**) | **+1,500 LC** team |
| Team haul | **~3,684 LC** |
| Equal 4-way share (Roland) | **+921 LC** |
| Lodging (**~9 LC**/day × **14**) | **−126 LC** |
| Food (**breakfast+dinner 10**/day × **14**) | **−140 LC** |
| **End pouch (into Ch 12 tavern)** | **~6,818 LC** |
| Stones on person | **288** rice + **16** leader (unchanged) |

**Skills:** While waiting on butcher / travel beats he keeps working mana: **Mana Hands** casts, **Mana Absorption**, **Mana Sense**. Shield stays **L3** (~**+14** combat casts; need **~105** for L4). Incantation stays **L6**. Sense and Absorption already **L9** (capped; still used). Mana Hands: idle waiting ~**25**/day × **7** ≈ **175** finished → **L5 → L6** (need **35×5 = 175** from L5). Hands rank popup **~+100 XP** (spell ranks beat trash goblins) → L20 bar **~2,774 / 10,000**. Combat acting still light vs solo goblins; idle mana practice is the real skill tick.

## Ch 12 money / XP (Iron Flagon + Floor-2 pocket)

| Item | Amount |
|---|---|
| Enter pouch (tavern) | **~6,818 LC** |
| Iron Flagon first round | **−45 LC** |
| **End pouch (after drink; into dungeon)** | **~6,773 LC** |
| Enter L20 bar | **~2,774 / 10,000** |
| Needle Worm pocket (**12× L16–L18**, **24 + level**) | **+492 XP** |
| **End L20 bar (after pocket / into tame)** | **~3,266 / 10,000** |
| Class | Still **Mage L20** |
| Stones on person | **288** rice + **16** leader (party bag takes tiny worm stones; personal bank unchanged on-page) |
| Pet | Core-bearing Needle Worm kept alive (**Basic Taming** L1) |

## Ch 13 half-year (Floor 3 → Mage L25 / Not bad)

**Span:** **26** weeks (**182** days; **~3** dives/week). Enter **Mage L20** bar **3,266 / 10,000**. Need **52,334 XP** to **Mage L25** empty.

**Kill XP:** Roland active **1/4** on L1 shares (Wereboar **250**, Spiked Boar **125**, Needle Moth **25**, Needle Worm **6**, dungeon rat **3**).

| Mob | Count | His XP |
|---|---:|---:|
| Wereboar | **120** | **30,000** |
| Spiked Boar | **78** | **9,750** |
| Needle Moth | **228** | **5,700** |
| Needle Worm | **416** | **2,496** |
| Dungeon rat | **260** | **780** |
| **Kill total** | **1,102** | **48,726** |

**Skill XP:** **3,608** (**36** ranks × **100** + **8** overflow). Ranks in `Skills.md` Ch 13.

**Bar:** kill **48,726** + skill **3,608** = **52,334** → **Mage L25**.

**Loot (team sale → equal 4-way):**

| Piece | Team LC |
|---|---:|
| Wereboar stones (**60** × **100**; **50%** of **120**) | **6,000** |
| Spiked Boar stones (**39** × **100**; **50%** of **78**) | **3,900** |
| Spiked Boar mats (**78** × **78**) | **6,084** |
| Wereboar mats (**120** × **156**) | **18,720** |
| Moth rice (**46** × **20**; ~**1/5** of **228**) | **920** |
| Worm tiny (**84** × **10**; ~**1/5** of **416**) | **840** |
| **Team** | **36,464** |
| **Roland share** | **9,116** |

**Money (Not bad count):**

| Item | Amount |
|---|---|
| Enter pouch (after Flagon) | **6,773 LC** |
| Half-year haul share | **+9,116 LC** |
| Lodging (**252** × **6.5**) | **−1,638 LC** |
| Food (**10**/day × **182**) | **−1,820 LC** |
| Kit (sword repairs **480** + boots **60** + cracked leather **250**) | **−790 LC** |
| **End pouch (Not bad)** | **11,641 LC** |

Personal stone bank unchanged: **288** rice + **16** leader.
