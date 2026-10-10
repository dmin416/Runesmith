# Class Packages

> **Live class packages, tier growth multipliers, forward-only rule.** Tier caps / reclass: `Progression.md`. Thin class hub: `Classes.md`. Fat catalog: `ClassesDesign.md`. Roland path: `RolandClasses.md`. Split from old `Levels.md` (no data dropped).

## Two tracks

| Track | Example | Raises from | Does |
|---|---|---|---|
| **Overall level** | Level 28 | XP (shared pool) | Pure level total. XP cost to advance uses the linear curve below. Not class-based. |
| **Class level** | Mage L5, Scribe L3 | Same XP pool, applied to the **main** class | Grows attributes via class package. Hits a class cap before the next class. |
| **Skill level** | Diagnosis L8, Basic Climbing L3 | Practice / use | Improves that action and often adds flat attribute bonuses. |

**Overall level ≈ sum of class levels** on the sheet (Mage L25 + Scribe L3 → Level 28). XP fills one bar. When it rolls over, overall level and main class level both go up by 1 (until that class is capped).

Dungeon **floors** are also called levels in prose. Those are places, not this system.

## Class levels

### What a class level-up does

- Awards a **class package**: fixed favored attributes each get points (Tier 1 usually **+1 per favored attribute**). Those attribute gains are **permanent**.
- The active tier’s **growth rate** scales that package (forward-only). See packages and math below.
- Recalculates HP / SP / MP from attributes (see `Attributes.md`). Skill pool bonuses can apply on top. Class cards do **not** raise max pools.
- **Class cards** are narrative benefits (e.g. Mage mana recovery), kept only while that class is primary or secondary. **Blessed by Mana** (perk): multiplies mana recovery (narrative; no flat MP).
- Fills toward the class **level cap**. At cap you need a class change / next class, not more levels in the same slot.

Chapter screens stay truth when numbers appear. Packages below are the rewrite planning defaults.

### Caps (Roland path and common bands)

| Tier | Typical cap before next class |
|---|---|
| 1 | L25 |
| 2 | L50 |
| 3 | L75 |
| 4 and above | L100 each |

Multiple past classes can sit on the sheet (primary / secondary; maxed lower tiers often go inactive). There is **no Tertiary active slot**.

**Secondary class (Chapter 17):** unlocking a second class lets you keep **one** prior class as secondary to retain its special effects (e.g. Mage mana recovery). Switch secondary **once per day**; no item required. Drop Mage from the secondary slot and that recovery goes with it. Overall level is the shared sum (rewrite Ch 17: Mage L25 + Scribe L1 → overall L26). Live reclass carries full bank (**1479 / 13000**); Old half-cut **739** quarantined. Extra Tier 1 classes slow the shared bar further; most people avoid a third T1.

**Reclass rules (Chapter 5 book talk):** no hard limit on how many classes a person can hold over a life. You cannot leave a class for another until you have at least **25 levels** in the current one. Tier 1 classes must be finished to their **L25** cap. First ascension crystal use awards a class (Roland’s space still required a Yes/No confirm). Later crystal uses need a **trial** (battle, craft or puzzle). Used first-ascension crystal turns to dust.


## Tier multipliers

Combat / prestige classes get a **growth multiplier** on new class levels. Pure craft classes often get **none**; their power is skills and products.

| Band | Growth rate | Notes |
|---|---|---|
| Tier 1 | ×1 | Baseline per-level package |
| Normal Tier 2 | ×1.5 | Common next step |
| Prestige Tier 2 (Lord) | ×2 | e.g. Runesmith Lord |
| Normal Tier 3 | ×3 | Baseline T3 |
| High-Lord | ×4 | Prestige T3 |
| Overlord | ×4.5 | Roland’s peak band |

Applies to **basic attributes except Luck and Charisma** unless a specific trait says otherwise. The rate multiplies **new** level-up package points only. See rewrite decision below.

**Pure craft note:** plain Blacksmith / Weaponsmith / Armorsmith lines often have **no growth-rate trait** (stay at ×1 packages even at higher craft tiers). Hybrid prestige (Runesmith Lord, Overlord, Rune Arch-Knight) does get a rate. Matches Source’s “craft has no multiplier” talk without nerfing Roland’s prestige path.

See `SkillsDesign.md` (Traits section) and `RolandClasses.md` for named traits.

---

## Class packages (Tier 1 baseline)

World name is **Willpower**, not Wisdom.

**Rule:** each favored attribute in the package gains **+1** at Tier 1 (growth rate ×1). Unlisted attributes do not gain from that class level (they can still rise from skills, training, or other classes).

| Class | Favored per level (T1) | Total points / level |
|---|---|---|
| **Mage** | Intelligence +1, Willpower +1 | 2 |
| **Warrior** | Strength +1, Vitality +1, Endurance +1 | 3 |
| **Archer** | Agility +1, Dexterity +1 | 2 |
| **Thief** | Agility +1, Dexterity +1 | 2 |
| **Blacksmith** | Strength +1, Endurance +1, Dexterity +1 | 3 |
| **Mana Scribe / Runic Mana Scribe** | Intelligence +1, Dexterity +1, Willpower +1 | 3 |
| **Acolyte** | Willpower +1, Vitality +1 | 2 |

**Scaled package** = each favored gain × current growth rate, then **round to nearest** (0.5 rounds up). Example: Mage at normal Tier 2 (×1.5) → Int +2, Will +2 (1.5 rounds to 2). Lord / Overlord use ×2 / ×4.5 before rounding.

Luck and Charisma stay out of growth-rate scaling unless a class or trait says otherwise. Small Cha bumps in early sheets are skill / story noise, not Mage package.

**Check vs early rewrite sheets (Mage):** L5→L25 over 20 levels gained about +26 Int and +29 Will (~+1.3 / +1.45 per level). Baseline +1/+1 plus skill bonuses and training accounts for the extras. Close enough to keep +1/+1 as the class package.

---

## Package math examples

Childhood / transfer bases ignored. These rows are **class-level gains only**.

### One level

| Class | T1 (×1) | Normal T2 (×1.5 → round) | Lord (×2) | Normal T3 (×3) | Overlord (×4.5 → round) |
|---|---|---|---|---|---|
| Mage | Int +1, Will +1 | Int +2, Will +2 | Int +2, Will +2 | Int +3, Will +3 | Int +5, Will +5 |
| Blacksmith (with rate) | Str +1, End +1, Dex +1 | +2 each | +2 each | +3 each | +5 each |
| Blacksmith (pure craft, no rate) | +1 each | +1 each | — | +1 each | — |
| Warrior | Str +1, Vit +1, End +1 | +2 each | +2 each | +3 each | +5 each |

### Mage only through 25 / 50 / 50 (125 levels, always Mage package)

Forward-only. Round ×1.5 and ×4.5 as above.

| Band | Levels | Int gained | Will gained |
|---|---|---|---|
| T1 ×1 | 25 | 25 | 25 |
| Normal T2 ×1.5→2 | 50 | 100 | 100 |
| Normal T3 ×3 | 50 | 150 | 150 |
| **Total (normal)** | **125** | **275** | **275** |
| T1 ×1 | 25 | 25 | 25 |
| Lord ×2 | 50 | 100 | 100 |
| Overlord ×4.5→5 | 50 | 250 | 250 |
| **Total (prestige)** | **125** | **375** | **375** |

### Roland-shaped split (planning sketch)

Assume: Mage 25 → Runic Mana Scribe 25 → Runic Blacksmith 25 (all T1 ×1) → Runesmith Lord 50 (×2) → later Overlord levels separate.

| Stretch | Package | Levels | Int | Will | Dex | Str | End |
|---|---|---|---|---|---|---|---|
| Mage | Int/Will | 25 | +25 | +25 | — | — | — |
| Runic Mana Scribe | Int/Dex/Will | 25 | +25 | +25 | +25 | — | — |
| Runic Blacksmith | Str/End/Dex | 25 | — | — | +25 | +25 | +25 |
| Runesmith Lord | use Lord hybrid: Int/Dex/Will/Str/End or craft-combat mix TBD | 50 | TBD ×2 | TBD | TBD | TBD | TBD |

Lord / Overlord packages need a locked hybrid list (craft + combat). Until then, treat prestige as “scaled version of the class’s favored set,” not every attribute.

### Blacksmith only, 25 levels T1

| Attribute | Gain |
|---|---|
| Strength | +25 |
| Endurance | +25 |
| Dexterity | +25 |
| Intelligence / Willpower | +0 from class |

Same person as a Mage for 25 levels would instead be Int +25, Will +25, and flat physicals from class.

---

## Rewrite decision: how the multiplier applies

### Locked: Forward-only

**Class-up does not remultiply the current sheet.** Existing attributes stay as earned. The new tier’s multiplier only scales **future** class level-up packages (luck / charisma still out unless a trait says otherwise).

Example: Tier 1 Mage package is Intelligence +1 and Willpower +1. Normal Tier 2 (×1.5, round up at .5) → +2 / +2. Lord (×2) → +2 / +2. Overlord (×4.5 → round) → +5 / +5. See class packages above.

**Why this is the rewrite default**

- Softer power curve. No overnight body rewrite at every class-up.
- Prestige still matters: later levels bank much harder than early ones.
- Early levels keep their face value forever. Grinding T3 is where the sheet climbs fast.

**Writing beat:** class-up unlocks skills, trials and the new growth rate. The person feels stronger as they level in the new class, not as an instant ×N flash on the whole status screen.

### Rejected: Retroactive (Source)

Source multiplies the whole basic-stat sheet at class-up (e.g. ×1.5 / ×2 / ×4.5 on current totals). Do not use that for rewrite status math or class-up scenes.

### Not used: Hybrid

Small instant boost plus higher per-level gains. Left unused to keep sheets and status scenes simple.

---

## Worked example: 125 levels, one favored attribute

Contrast only for forward-only vs Source retroactive. For full Mage (Int+Will) totals, double the forward-only column or use the package math section above.

**Path:** 25 Tier 1 → 50 Tier 2 → 50 Tier 3. One attribute with T1 gain +1, scaled by growth rate **without** the round-to-int step (raw rates), so the contrast stays easy to read.

| Path | Forward-only end | Retroactive end (rejected) |
|---|---|---|
| Normal ×1.5 / ×3 | 25 + 75 + 150 = **250** | **375** |
| Prestige ×2 / ×4.5 | 25 + 100 + 225 = **350** | **562.5** |

With integer rounding (×1.5→2, ×4.5→5), Mage Int alone becomes **275** normal or **375** prestige over the same 125 Mage-only levels (see package math).

Real sheets also add childhood base, skills and traits on top.

---

## Quick rules for writing

1. Overall L# = shared XP bar (linear cost). Class L# = which package fires when that bar rolls.
2. XP awards ignore class. Class-up changes growth package / rate, not the XP curve.
3. Class-up into a multiplier class = **new growth rate on future levels**, not an instant ×N on the whole sheet.
4. Craft-only classes may gain levels with little combat growth multiplier.
5. Party XP works across tier gaps. Award by **ability and contribution** (idle still gets a thin cut). Same-tier parties are preferred socially, not required.
6. Skill L9 → evolve. Do not write L10 on the same skill name.
7. When a chapter shows numbers, copy them into `../../Story/Notes/Status.md` and keep this file as the rule layer.
8. If Source text says the sheet jumps at class-up, rewrite it to growth-rate talk instead.
9. XP_to_next = **500 × overall level**. Kill XP = **50 × killed_L × RaceMult** (goblin **1.0**; rat **0.2**; worm **0.5**; moth **2.0**; spiked boar **1.5**; wereboar **2.0**; people **1.0**; default unlisted **1.5**). Pre-class bank half-penalty lands Mage L3 from bravery + **55** estate L1s. Class-change half-cut stays dead. Chapter ledgers: `../../Story/Notes/Experience.md`. Change constants only if arcs feel wrong. Narrative threat (not XP): `../World/Fauna/MonsterThreat.md`.
