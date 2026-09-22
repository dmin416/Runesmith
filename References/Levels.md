# Levels

How class levels, skill levels and tier multipliers work. Physical training timelines stay in `Progression.md`.

## Two tracks

| Track | Example | Raises from | Does |
|---|---|---|---|
| **Overall level** | Level 28 | XP (shared pool) | Pure level total. XP cost to advance uses the linear curve below. Not class-based. |
| **Class level** | Mage L5, Scrybe L3 | Same XP pool, applied to the **main** class | Grows attributes via class package. Hits a class cap before the next class. |
| **Skill level** | Debugger L8, Basic Climbing L3 | Practice / use | Improves that action and often adds flat attribute bonuses. |

**Overall level ≈ sum of class levels** on the sheet (Mage L25 + Scrybe L3 → Level 28). XP fills one bar. When it rolls over, overall level and main class level both go up by 1 (until that class is capped).

Dungeon **floors** are also called levels in prose. Those are places, not this system.

## Class levels

### What a class level-up does

- Awards a **class package**: fixed favored attributes each get points (Tier 1 usually **+1 per favored attribute**).
- The active tier’s **growth rate** scales that package (forward-only). See packages and math below.
- Recalculates HP / SP / MP from attributes (see `Attributes.md`). Class bonuses (e.g. Mage +20% mana) apply on top.
- Traits can add extra on level-up (e.g. **Blessed by Mana**: extra MP each Mage level, on top of Int/Will gains).
- Fills toward the class **level cap**. At cap you need a class change / next class, not more levels in the same slot.

Chapter screens stay truth when numbers appear. Packages below are the rewrite planning defaults.

### Caps (Roland path and common bands)

| Tier | Typical cap before next class |
|---|---|
| 1 | L25 |
| 2 | L50 |
| 3+ | Continues; midpoints can unlock further trials |

Multiple past classes can sit on the sheet (primary / secondary / tertiary). Maxed lower-tier classes often go inactive once higher ones take the front.

**Secondary class (Chapter 17):** unlocking a second class lets you keep **one** prior class as secondary to retain its special effects (e.g. Mage mana pool / regen). Switch secondary **once per day**; no item required. Overall level is shared (Scrybe L3 at overall L28 means L25→L28 on the same bar). Extra Tier 1 classes slow the shared bar further; most people avoid a third T1.

**Reclass rules (Chapter 5 book talk):** no hard limit on how many classes a person can hold over a life. You cannot leave a class for another until you have at least **25 levels** in the current one. Tier 1 classes must be finished to their **L25** cap. First ascension crystal use awards a class (Roland’s space still required a Yes/No confirm). Later crystal uses need a **trial** (battle, craft or puzzle). Used first-ascension crystal turns to dust.

### XP sources

Awards are **straightforward**: flat or simple by action. Class does **not** change how much XP an action is worth. Class only decides which package you get when the overall bar rolls.

**Locked early anchors**

| Action | XP |
|---|---|
| Monster kill (solo, full credit) | **(49 + monster level) × RaceMult** |
| Goblin L1 (estate bravery) | **50** (49+1) |
| Goblin L2 / L3 / L4 (first Carwen group) | **51 / 52 / 53** |
| Typical early forest goblin (~L4) | **53** (RaceMult 1.0) |
| First Kill achievement (on top of the kill) | **+200** (Chapter 4; not every kill) |
| First-time basic / lesser rune schematic (drawing it into the system) | **1000** |
| Repeat scrolls / practice crafts | much less than first schematic (story: ~20 regular, ~50 runic until retuned) |

**Goblin levels in early rewrite**

| Fight | Monster level | Notes |
|---|---|---|
| Arden bravery test (age 9) | **Goblin L1** (HP 117) | Explicit status screen; XP **50** = 49+1 |
| Weekly estate training | L1-tier training stock | Same pen as bravery test; **50** each |
| First Carwen forest group | **L2, L3 and L4** | Thought-ID; XP **51 / 52 / 53**; opens with mental ear bolt |
| Later same-day chase kills | **L4 / L5** then **L3 / L4** | XP **53 / 54** (level-up) then **52 / 53**; Mage **L3→L4** when estate Mage doubles left the bar at **1250 / 1500** (`Experience.md`) |
| Later Carwen forest nests | higher than estate, still common goblins | Levels not always shown; treat as low single digits unless the chapter names them |

Other notes:

- Monster kills (solo or party). Party share needs members close enough in **overall level** and **same tier band**; a Tier 2 cannot power-level a Tier 1 (even crippling a monster so a lower-tier finishes it grants that lower-tier nothing). Idle spectating still pays a tiny share (Chapter 11: **5 XP** on a spiked boar Roland did not fight). Active contribution raises his cut.
- Leveling skills and spells. Leveling a spell (e.g. Mana Bolt rank-up) can grant a popup XP award; Chapter 10 notes this is often **more** than trash goblin kills. Craft classes also gain XP by making items.
- Crafting / item creation. **First** successful schematic discovery pays the big 1000. Copying the same rune again does not.
- **Pre-class XP** (Chapter 4–6): kills and achievements before first ascension bank with a **½ penalty** when the class finally applies. Estate bravery **250** + **55** more L1 goblins (**2750**) = bank **3000** → **1500** applied. Ascension starts Mage L1 empty; bank lands **Mage L3** empty. The bank applies **once** at the first ascension only. It does **not** refill for later class changes. See `Experience.md`.
- **Second Tier 1 class** (Chapter 10 talk): most people do not ascend at age 10. Taking a second T1 after the first has an XP gain debuff. Combat second T1s take the heaviest hit; lighter crafting second T1s level faster but grant weaker packages.

### Kill XP formula

```
XP_from_kill = (49 + MonsterLevel) × RaceMult
```

**Common goblin** (RaceMult 1.0): **49 + level**. Chapter 4 L1 → **50**. Round to nearest whole XP after RaceMult. No class modifier. Party contribution then splits that total.

#### Race / species multipliers

Use the creature’s **family**, not every cosmetic variant name. Evolved or named bosses can stack a boss tag later; until then pick the closest row. L4 column uses `(49 + 4) × RaceMult`.

| Race / family | RaceMult | Examples | L4 solo XP |
|---|---|---|---|
| **Goblin** (common) | **1.0** | Green lowland goblin, estate training stock | **53** |
| Mountain / gray goblin | 1.25 | Edelgard mountain goblin, gray forest goblin | 66 |
| Goblin leader / elite goblin | 1.5 | Goblin Leader (not full king) | 80 |
| Goblin King / king-tier | 2.0 | Cull-trigger king variants | 106 |
| **Hobgoblin** | **1.75** | Wild hobgoblin, lab subjects | 93 |
| Gray Hobgoblin Berserker | 2.25 | Rage / berserk hob | 119 |
| Spiked Boar / common dungeon beast | 1.25 | Emerald Wilderness boar, similar floor trash | 66 |
| Needle Worm / lesser ambusher | 1.25 | Floor-2 caterpillar | 66 |
| Wereboar / floor elite beast | 2.0 | Floor-3 Carwen target | 106 |
| **Myrmeke Worker** (giant ant) | **1.5** | Dog-sized mine ants | 80 |
| Myrmeke Soldier | 2.5 | Horse-sized L50+ soldiers | 133 |
| Myrmeke Queen | 4.0 | Nest boss | 212 |
| **Orc** | **2.0** | Arena / wild orcs | 106 |
| Red Orc High-Chieftain | 3.5 | Tier-3 orc leader | 186 |
| **Greater Mantodea** (mantis) | **3.0** | Giant praying mantis | 159 |
| Volcanic Kamacuras / fire mantis | 3.0 | Same band as mantis | 159 |
| Skeleton / basic undead | 1.25 | Early blazing / fiery skeletons | 66 |
| Devil / imp (lesser) | 2.0 | Pale Imp, Lesser Spiked Devil | 106 |
| Golem (ruby / volcanic) | 3.0 | Mid dungeon constructs | 159 |
| Drake / lesser dragon-kin | 3.5 | Later open-field threats | 186 |
| **Default (unlisted monster)** | **1.5** | Anything not in this table | 80 |

Add new rows when a chapter names a repeat family. Prefer a band over inventing one-off decimals. Named chapter payouts (e.g. Gray Hobgoblin Berserker **950**) override the table when the prose shows a number.

#### Worked early kills

| Kill | Level | RaceMult | XP |
|---|---|---|---|
| Estate bravery goblin | 1 | 1.0 | **50** (49+1) |
| Carwen forest goblin | 3 | 1.0 | **52** |
| Carwen forest goblin | 4 | 1.0 | **53** |
| Same level hobgoblin | 4 | 1.75 | **93** |
| Same level myrmeke worker | 4 | 1.5 | **80** |
| Same level orc | 4 | 2.0 | **106** |
| Same level greater mantis | 4 | 3.0 | **159** |

Same level, harder race → more XP. That is the whole point of RaceMult.

**Level-gap note (optional, not required for early arcs):** Source often treats far-weaker mobs as nearly worthless XP. If needed later, apply a soft penalty when the killer’s overall level is far above the monster (e.g. heavily reduced when gap ≥ 10). Do not use that to replace the base `(49 + MonsterLevel) × RaceMult` line.

At class **cap**, further XP does not raise that class. Bank it for the next class change (partial carry, about half lost on change; Chapter 13–16: do not keep dungeon grinding at Mage L25 before switching; schematic XP also takes the half cut) or it sits until you switch. Do not invent a second XP bar per class. Crafting classes also earn less XP from monster fights than combat classes.

## Experience curve (overall level)

### Source pacing (what we matched)

Source payouts were smaller (goblin ~15–20 XP, same **1000** first schematic). Rewrite keeps the **kill counts / time feel**, not the old raw numbers.

| Source beat | What happened | Implied cost (Source XP) |
|---|---|---|
| First adventurer day, Mage L3 | ~7 goblin ears; leveled once during the hunt | estate Mage doubles left **1250 / 1500**; hunt **263** finishes L3→L4 |
| ~3 months forest grind | L5 → ~L20 | many goblins/day plus spell/skill XP |
| Party dungeon arc | ~half a year more toward Mage L25 cap | higher XP/fight than forest goblins |
| First lesser schematic | **1000 XP**; “couple of levels” if spent right after a fresh class (low L) | 1000 ≈ 1–2 levels near overall L2–L3 |
| Late Source | bar called “exponential” and stubborn | rewrite stays **linear**; high constant makes late levels slow without a second curve |

### Locked rules

1. XP needed to go from overall level **L → L+1** depends only on **L**, not on which class is main.
2. Formula is **linear** in L (Source’s late “exponential” talk is not used).
3. One shared XP pool. Class packages fire when the bar rolls.

### Formula (locked: pre-class L3 + half bank)

Anchor: bank **3000** (Ch 4 bravery 250 + **55** estate L1×50), half on apply = **1500**, Mage L1 empty → L3 empty. See `Experience.md`.

```
XP_to_next(L) = 500 × L
```

At L5: **2500 XP** ≈ **47 × L4 goblins** (empty bar). First-day forest kills alone are a small slice; spell/skill XP and denser hunting carry the early adventurer grind (Chapter 9–10).

| Current L | XP to reach L+1 | Goblins @ 53 (empty bar) | First schematic 1000 |
|---|---|---|---|
| 1 | 500 | 9.4 | 2 levels |
| 5 | 2500 | **47** | 0.4 level |
| 10 | 5000 | 94 | 0.2 level |
| 20 | 10000 | 189 | 0.1 level |
| 25 | 12500 | 236 | 0.08 level |
| 28 | 14000 | 264 | 0.07 level |
| 50 | 25000 | 472 | 0.04 level |
| 75 | 37500 | 708 | 0.03 level |
| 100 | 50000 | 943 | 0.02 level |
| 125 | 62500 | 1179 | 0.02 level |

**Schematic check:** after class change at low overall L (e.g. L2–L3), **1000 XP** is about **two levels**. At Mage L25 it is a small fraction of a level. Spell/skill XP still matters early (Chapter 10: spell rank-ups often beat trash goblin kills).

### Cumulative XP (from L1 up to level N)

```
XP_total_to_reach(N) = 500 × (1 + 2 + … + (N−1))
                     = 250 × (N−1) × N
```

| Reach overall | Total XP from L1 | Rough goblin-equivalents (÷53) |
|---|---|---|
| 25 (one T1 maxed) | **150,000** | ~2,830 |
| 50 | **612,500** | ~11,557 |
| 75 (25+50) | **1,387,500** | ~26,179 |
| 125 (25+50+50) | **3,875,000** | ~73,113 |

XP already spent stays spent. Goblin-counts are a yardstick only. Real paths mix dungeon mobs, skill XP, schematics and quests.

**L5→L20 only** (15 steps, costs 500×(5+…+19) = 500×180): **90,000 XP** ≈ **1,698 goblins**. Over ~90 days that is ~19 goblins/day if empty-bar pure grind. Source banks spell/skill XP and denser hunting, so the three-month L5→L20 arc still needs those non-kill sources.

### Sample grind checks

| Action | XP | At L5 (need 2500) | At L25 (need 12500) | At L50 (need 25000) |
|---|---|---|---|---|
| Goblin L1 (49+1) | 50 | tiny | tiny | tiny |
| Goblin L4 (49+4) | 53 | ~1/47 level | ~1/236 level | ~1/472 level |
| First basic/lesser rune schematic | 1000 | 0.4 level | 0.08 level | 0.04 level |
| First Common rune schematic (e.g. Fire Arrow) | **2000** (2× lesser) | 0.8 level | 0.16 level | 0.08 level |
| Mana Arrow scroll (repeat craft) | 20 | tiny | tiny | tiny |
| Fire Orb runic scroll (repeat) | 50 | tiny | tiny | tiny |
| Tier 2 fencer (party share) | 479 | ~0.19 level | ~0.04 level | ~0.02 level |

Chapter 26 schematic stacking: Intermediate common = **1000 XP**; then perfecting to Highest adds another **1000** (total 2000). Going straight to Highest also pays 2000. No further XP for redoing the same schematic past that cap.

Chapter 21 timing: regular Mana Arrow ~**10 min** / 20 XP; Fire Orb runic ~**45 min** / 50 XP (imperfect). Five regular scrolls ≈ one runic's time for more XP; schematics still dominate leveling. Shop magic contracts can curse breach with **−60% mana** until the term ends. Common schematics pay **2×** lesser (Chapter 22 Fire Arrow).

Chapter 14 narration: common Tier 2 packages grow about **×1.5** vs Tier 1 (forward-only on new levels). Fresh T2 physicals still burn hard on active skills (stamina + mana). A coordinated T1 party deep into second classes can beat a green T2.

### Optional later tweaks (not locked)

- Monster XP scaled by level gap can sit on top of flat base values.
- If the curve still feels fast or slow after a few written arcs, change only the constant **500** (keep linear). Halving to **250 × L** would cut every cost in half.

## Skill levels

Rewrite law (also in `Ideas.md`):

- Skills rank **L1 through L9**. L9 is the hard max for that skill name.
- **Until the first Tier 2 class is gained**, no skill may exceed **L9**. There is no L10 on any name in the T1 span.
- Next step at L9 is **evolution** (Basic X → X → Advanced / Expert), not L10 on the same name. The new name starts at L1 and is also hard-capped at L9 while he is still T1-only.
- **Advanced / Expert** skill tracks that sit above ordinary evolved forms wait on Tier 2 (or later) class gates unless a chapter locks an earlier exception.
- Effects and skill-tied stat bonuses scale with the current skill’s level.
- Evolving a Basic skill can grant a free attribute point (e.g. Basic Sneaking → Agility) **in addition to** the ongoing +level bonus of the new skill form if it still lists attribute bonuses.
- **Technique only:** level is form / efficiency / timing / decisions, not body power. L5 = dedicated adult amateur, L7 = competitive or professional, L9 = pinnacle of normal human technique. Early Basic ranks by age: `Progression.md`.
- Chapter 4 books say max Mana Sense at **L10** for Mage. Treat that as in-world rounding / old wording. Rewrite sheet max is **L9**.

Chapter 7: Roland thinks Basics stop at L9 from **class restrictions**. Rewrite reason is the L9 hard max (then evolve), not Mage locking physical Basics.

### Practice thresholds (Chapter 4 Climbing test)

Roland’s Climbing grind on one tree: **L1** on first success, **L2** after about **10** repeats, **L3** after about **50**. He reads this as an achievement curve (each rank needs more clean reps). Exact counts vary by skill and conditions (taller tree, real opponents).

### Field-use curve (locked for Ch 9.5 combat math)

Extend the Climbing anchors with a steady climb after L3. Counts are **cumulative clean uses** to *reach* that level (not XP).

| Reach | Cum clean uses | Step from prior |
|---|---|---|
| L1 | **1** | first success |
| L2 | **10** | +9 |
| L3 | **50** | +40 |
| L4 | **155** | +105 (= 35×3) |
| L5 | **295** | +140 (= 35×4) |
| L6 | **470** | +175 (= 35×5) |
| L7 | **680** | +210 (= 35×6) |
| L8 | **925** | +245 (= 35×7) |
| L9 | **1205** | +280 (= 35×8) |

After L3: `reps_to_next(L) = 35 × L` where L is the level you are leaving.

**What counts**
- **Spells:** every finished cast (chant completes, spell leaves the hand).
- **Technique skills** (Shaping, Incantation, Sword, Sneak, etc.): only **clean** reps. Misses, panics and interrupted casts do not. Field rule of thumb: about **40%** of raw attempts are clean.
- **Mana Absorption / Mana Reinforcement:** every time the pool is spent down and topped back up. Cast → drain → absorb refill and reinforce hold count as uses. These run **constantly in combat** as mana is used, not only in town meditation. Clean-rate is higher than attack technique (~**70%**) because the loop is deliberate.
- **Already high Basics (L8–L9):** do not restart the table at 0. Only the step to the next rank (or evolve) counts. Opponent/variety gates still apply (`Progression.md`: H2H / Sword / Sneak need real field work for the last tick / evolve). Hard cap remains **L9** until first T2 class.
- **Evening utility** (Ember cook-pot, Mana Hands mug lifts) can add uses outside the forest. Absorption / Reinforcement do **not** need a town-only track; hunts already cycle them hard.

### Ch 9.5 combat volume (yardstick)

~**70** hunt days in **90** calendar days. ~**10** kills/day average → ~**700** goblins. Class need L4→L20 ≈ **94k XP**; kills at ~53 ≈ **37k**; remaining ≈ **57k** from spell/skill rank-ups (matches “spell XP beats trash kills”).

Raw combat actions (order-of-magnitude): Mana Bolt ~**1100** casts, Mana Arrow ~**380** (from late month 1), Mana Shield ~**130** (from month 2), short-sword finishes ~**350**, aimed shots (Bolt+Arrow) ~**1480**. Absorption / Reinforcement cycles ~**20**/hunt day × 70 ≈ **1400** raw (mana spent and restored under Reinforcement) → ~**980** clean at 70%.

Apply the curve → end ranks in `Story/Notes/Skills.md` Chapter 9.5. No skill past **L9** before T2.

### Pre-ascension unlock rules (Chapter 4)

- Most skills available before first class are **Basic** and combat-leaning.
- Toy / non-weapon props may fail (ball toss did not unlock throwing; rock + dummy did). Stick ≠ spear for spear-throwing.
- **Production / craft class skills** (smithing, etc.) do **not** unlock without the matching class. Combat hammer use is a different path.
- Ambient mana absorption before Mage or Acolyte causes mana poisoning.

### Skill attribute bonuses

**Locked rule (Chapter 2 screens + Chapter 4 talk):**

```
Attribute bonus from a skill = +1 × current skill level
```

per favored attribute listed on that skill. When the skill gains a level, that attribute goes up by 1. Bonus equals the level on the skill card (Debugger L8 → Intelligence +8).

Not every skill grants attributes. Identify, Analyze, Sleep Resistance, Map Reading and Basic Mathematics show no attribute line at transfer. Mana Sense gains Intelligence (Chapter 4; L4 → +4 Int).

**Transfer examples (bonus = level)**

| Skill | Level | Bonus |
|---|---|---|
| Debugger | 8 | Int +8 |
| Technology | 7 | Dex +7, Int +7 |
| Tinkerer | 8 | Dex +8 |
| Cooking | 3 | Dex +3, Agi +3 |
| Marksmanship | 7 | Dex +7 |
| Acting | 4 | Cha +4 |
| Hastened Reading | 2 | Int +2 |

**Early Basic map (rewrite default)**

Favored attributes for skills Roland trains in Chapters 4–7. Same +1 × level rule.

| Skill | Bonus per level |
|---|---|
| Basic Running | Endurance +1 |
| Basic Sprint | Vitality +1, Endurance +1 |
| Basic Hand to Hand Combat | Strength +1, Vitality +1 |
| Basic Climbing | Strength +1, Agility +1 |
| Basic Throwing | Dexterity +1 |
| Basic Sneaking | Agility +1 |
| Basic One-Handed Swordsmanship | Strength +1 |
| Basic Leather Armor Proficiency | Vitality +1, Endurance +1 |
| Reading Proficiency | Intelligence +1, Willpower +1 |
| Mana Sense | Intelligence +1, Willpower +1 |
| Basic Mana Shaping | Intelligence +2, Willpower +1 |
| Basic Mana Regulation | Intelligence +1, Willpower +2 |
| Basic Incantation | Intelligence +1, Willpower +1 |
| Mana Absorption | Intelligence +1, Willpower +2 |
| Mana Reinforcement | Intelligence +1, Willpower +1 |
| Identify | none |

Chapter 4 prose: leveling physical Basics also makes him “run faster, jump higher and punch harder” via technique, and “bonuses to endurance and strength” when those skills get high enough. Rewrite pads: Running → Endurance; Sprint → Vitality + Endurance; Hand to Hand → Strength + Vitality; Leather → Vitality + Endurance; Reading / Mana Sense → Intelligence + Willpower. Age-10 goal: Str/Agi/Vit/End **40**; Dex/Will higher; Int highest (`StatusBreakdown.md`).

Evolution (Basic → non-Basic) can grant an extra free point once, then the new skill’s own +level line takes over if it has one.

### Sheet buckets

Displayed attributes split three ways. Full Roland tallies: `Story/Notes/StatusBreakdown.md`.

```
Displayed = Body + Class levels + Skills/Traits (+ Other if needed)
```

- **Body:** `Progression.md` age physicals + adult-mind Int/Will age row (age 5: Int 12, Will 15; Cha 3, Luck 7 seeds).
- **Class levels:** packages only (Mage = +1 Int and +1 Will per level).
- **Skills/Traits:** +1 × skill level per favored attribute, plus flat trait cards.

At age 10 with Basics at Progression targets, skills/traits supply most of STR/AGI/DEX/END/INT. Class levels are a small Int/Will slice until higher Mage ranks. Current Ch 4–8 sheets still omit the Basic physical pile (retcon debt).

## Spell casting (Chapter 10)

Tier 1 cast loop: imagine the **spell circle** (formula) + shape mana + chant, in sequence. Fail any step and the spell sizzles. Intelligence helps visualize and recall circles. Higher tiers use larger circles and longer chants; skills reduce mental strain.

**How spells are learned**

- Class level thresholds can dump a spell into the mind (incantation + construction).
- Books / teachers / self-experimentation for extras. Spellbooks are expensive.
- Mage’s three basics: Mana Bolt, Mana Arrow, Mana Shield. Ember and Mana Hands can come from a low-grade book.

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

See `Skills.md` (Traits section) and `RolandClasses.md` for named traits.

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
| **Mana Scrybe / Runic Mana Scrybe** | Intelligence +1, Dexterity +1, Willpower +1 | 3 |
| **Acolyte** | Willpower +1, Vitality +1 | 2 |

**Scaled package** = each favored gain × current growth rate, then **round to nearest** (0.5 rounds up). Example: Mage at normal Tier 2 (×1.5) → Int +2, Will +2 (1.5 rounds to 2). Lord / Overlord use ×2 / ×4.5 before rounding.

Luck and Charisma stay out of growth-rate scaling unless a class or trait says otherwise. Small Cha bumps in early sheets are skill / story noise, not Mage package.

**Check vs early rewrite sheets (Mage):** L5→L25 over 20 levels gained about +26 Int and +29 Will (~+1.3 / +1.45 per level). Baseline +1/+1 plus Blessed by Mana, skill bonuses and training accounts for the extras. Close enough to keep +1/+1 as the class package.

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

Assume: Mage 25 → Runic Mana Scrybe 25 → Runic Blacksmith 25 (all T1 ×1) → Runesmith Lord 50 (×2) → later Overlord levels separate.

| Stretch | Package | Levels | Int | Will | Dex | Str | End |
|---|---|---|---|---|---|---|---|
| Mage | Int/Will | 25 | +25 | +25 | — | — | — |
| Runic Mana Scrybe | Int/Dex/Will | 25 | +25 | +25 | +25 | — | — |
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
5. Party XP fails across tier gaps.
6. Skill L9 → evolve. Do not write L10 on the same skill name.
7. When a chapter shows numbers, copy them into `Story/Notes/Status.md` and keep this file as the rule layer.
8. If Source text says the sheet jumps at class-up, rewrite it to growth-rate talk instead.
9. XP_to_next = **500 × overall level**. Kill XP = **(49 + monster level) × RaceMult** (common goblin = 49 + level). Pre-class bank half-penalty lands Mage L3 from bravery + **55** estate L1s (`Experience.md`). Change constants only if arcs feel wrong.
