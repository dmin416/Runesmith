# RaceMult

> **Live RaceMult table and worked kills.** Kill law: `Progression.md` (`50 × killed_L × RaceMult`). Overall XP curve: `ExperienceCurve.md`. Ch 4–19 ledger: `../../Story/Notes/Experience.md`. Old `(49 + L)` / Mult **10/20** L1 samples quarantined. Narrative threat: `../World/Fauna/MonsterThreat.md`. Split from old `Levels.md` (no data dropped).

## Kill XP (live)

```
XP_kill = 50 × killed_L × RaceMult
```

Round to nearest whole XP after RaceMult. No class modifier on the pool. Party contribution then splits that total. Hub: `Progression.md`.

**Locked early anchors (live law)**

| Action | XP |
|---|---|
| Monster kill (solo, full credit) | **50 × monster level × RaceMult** |
| Goblin L1 (estate bravery) | **50** (RaceMult 1.0) |
| Goblin L2 / L3 / L4 (live) | **100 / 150 / 200** |
| Typical early forest goblin (~L4) | **200** (RaceMult 1.0) |
| First Kill achievement (on top of the kill) | **+200** (Chapter 4; not every kill) |
| First-time basic / lesser rune schematic at **[Highest]** | **1000** (quality ladder: **100 / 200 / 400 / 600 / 1000**; raise pays difference) |
| Repeat scrolls / practice crafts | much less than first schematic (story: ~20 regular, ~50 runic until retuned) |

**Goblin levels in early rewrite**

| Fight | Monster level | Notes |
|---|---|---|
| Arden bravery test (age 9) | **Goblin L1** (HP 117) | Explicit status screen; XP **50** |
| Weekly estate training | L1-tier training stock | Same pen as bravery test; **50** each |
| First Carwen forest group | **L2, L3 and L4** | Live XP **100 / 150 / 200**; Old ledger **51 / 52 / 53** quarantined in `../../Story/Notes/Experience.md` |
| Later same-day chase kills | **L4 / L5** then **L3 / L4** | Live **200 / 250** then **150 / 200**; day end **1000 / 2000** at L4 (`../../Story/Notes/Experience.md`) |
| Later Carwen forest nests | higher than estate, still common goblins | Levels not always shown; treat as low single digits unless the chapter names them |

Other notes:

- Monster kills (solo or party). Party XP ties to **ability and contribution**. Teaming with higher-tier people is allowed; a low cut still pays something. Idle spectating on the Chapter 11 spiked boar: Roland **6 XP** (**~1%** of the kill for being in the group; he could kill it alone if he tried). Active contribution raises his cut. People still prefer same-tier parties.
- Leveling skills and spells. Leveling a spell (e.g. Mana Bolt rank-up) can grant a popup XP award; Chapter 10 notes this is often **more** than trash goblin kills. Craft classes also gain XP by making items.
- Crafting / item creation. **First** successful schematic discovery pays the big 1000. Copying the same rune again does not.
- **Pre-class XP** (Chapter 4–6): kills and achievements before first ascension bank with a **½ penalty** when the class finally applies. Estate bravery **250** + **55** more L1 goblins (**2750**) = bank **3000** → **1500** applied. Ascension starts Mage L1 empty; bank lands **Mage L3** empty. The bank applies **once** at the first ascension only. It does **not** refill for later class changes. See `../../Story/Notes/Experience.md`.
- **Second Tier 1 class** (Chapter 10 talk): most people do not ascend at age 10. There is **no XP gain debuff**. Kill XP stays the same. More classes means you need **more total experience** because overall level keeps climbing on the shared bar to raise each class. Combat second T1s take longest to push through that climb; lighter crafting second T1s level faster but grant weaker packages.


### Kill XP formula (live)

```
XP_kill = 50 × killed_L × RaceMult
```

Round to nearest whole XP after RaceMult. No class modifier on the pool. Party contribution then splits that total. Hub: `Progression.md`.

**Common goblin** (RaceMult **1.0**): Chapter 4 L1 → **50**. L4 → **200**.

**Carwen early anchors (draft dungeon L, RaceMult):** dungeon rat **L5 / 0.2** → solo **50**; Needle Worm **L16 / 0.5** → **400**; Needle Moth **L18 / 2.0** → **1,800**; Spiked Boar **L8 / 1.5** → **600** (idle **~1%** / active **~1/4**); Wereboar **L26 / 2.0** → **2,600** (evolved Spiked Boar; min **L26**).

**People / classed races** (humans, elves, beastmen, dwarves, etc. with classes; not monster races like goblins): RaceMult **1.0** → `50 × OverallLevel`. Split among the XP takers (Ch 14: five - Roland, Becky, Sahildr, Reyna, Ned). **Extra factors** (ability + contribution) push each award above or below an equal cut. Tamed companions take a share from the kill; they do not need to eat the corpse.

**Ch 14 lock:** fencer overall **L55** → pool **2750**. Equal fifth **550**. Roland on-page **479** (extras below equal). Ned's share tips him **25→26** / **Greater Needle Worm**.

#### Danger vs stats (people)

- **Stats** set physical ceiling only: tip KE, sprint, HP pool (`../Combat/AttackScale.md`, street baseline STR/AGI **15**).
- **Danger** is stats × skills × gear × tactics. A combat-classed person with actives (Gale Step), enchanted weapons and training hits far above a same-stat civilian or a same-level trash monster.
- Same overall level: a fighter usually out-threats goblin-tier trash; dense beasts (Wereboar band) can still win a raw brawl on size and HP. Tier 2 skills make L55 specialists spike hard even when their sheet looks "only" mid-T2.
- Do not treat overall level alone as threat. Read class tier, skill loadout and gear with the numbers. People XP pool is **`50 × overall level`** (RaceMult 1.0).

#### Race / species multipliers (live)

Use the creature’s **family**, not every cosmetic variant name. Evolved or named bosses can stack a boss tag later; until then pick the closest row. L4 column = `50 × 4 × RaceMult`.

| Race / family | RaceMult | Examples | L4 solo XP |
|---|---|---|---|
| **Dungeon rat** (vermin) | **0.2** | Entrance corridor rats | **40** |
| **Needle Worm** (floor-2 ambusher) | **0.5** | Spiky caterpillar; stone **½ rice** | **100** |
| **Goblin** (common) | **1.0** | Green lowland goblin, estate training stock | **200** |
| Mountain / gray goblin | 1.25 | Edelgard mountain goblin, gray forest goblin | 250 |
| Goblin leader / elite goblin | 1.5 | Goblin Leader (not full king) | 300 |
| Skeleton / basic undead | 1.25 | Early blazing / fiery skeletons | 250 |
| **Needle Moth** (floor-3 adult/elite) | **2.0** | Winged Needle Worm line; stone **rice** | **400** |
| Goblin King / king-tier | 2.0 | Cull-trigger king variants | 400 |
| Devil / imp (lesser) | 2.0 | Pale Imp, Lesser Spiked Devil | 400 |
| **Hobgoblin** | **1.75** | Wild hobgoblin, lab subjects | 350 |
| Gray Hobgoblin Berserker | 2.25 | Rage / berserk hob | 450 |
| **Myrmeke Worker** (giant ant) | **1.5** | Dog-sized mine ants | 300 |
| Myrmeke Soldier | 2.5 | Horse-sized L50+ soldiers | 500 |
| Myrmeke Queen | 4.0 | Nest boss | 800 |
| **Orc** | **2.0** | Arena / wild orcs | 400 |
| Red Orc High-Chieftain | 3.5 | Tier-3 orc leader | 700 |
| **Greater Mantodea** (mantis) | **3.0** | Giant praying mantis | 600 |
| Volcanic Kamacuras / fire mantis | 3.0 | Same band as mantis | 600 |
| Golem (ruby / volcanic) | 3.0 | Mid dungeon constructs | 600 |
| Drake / lesser dragon-kin | 3.5 | Later open-field threats | 700 |
| **Spiked Boar** (floor-1 beast) | **1.5** | Emerald Wilderness; draft common **~L8** (solo **600**) | **300** |
| **Wereboar** (floor-3 elite) | **2.0** | Evolved Spiked Boar; **min L26** (solo **2,600**) | **400** |
| **People / classed race** | **1.0** | Humans, elves, beastmen, dwarves with classes | **200** |
| **Default (unlisted monster)** | **1.5** | Anything not in this table | 300 |

Add new rows when a chapter names a repeat family. Prefer a band over inventing one-off decimals. Named chapter payouts must match this law; ledger: `../../Story/Notes/Experience.md`.

#### Worked early kills (live)

| Kill | Level | RaceMult | XP |
|---|---|---|---|
| Estate bravery goblin | 1 | 1.0 | **50** |
| Dungeon rat (Ch 11 entrance) | **5** | 0.2 | Solo **50**; Roland **full solo** on party test; active ~**12** / idle ~**1** |
| Needle Worm (Ch 12 floor 2) | **16** | 0.5 | Solo **400**; active ~**100** / idle ~**4**; stone **½ rice** (**1 SS**) |
| Needle Moth (Ch 13 floor 3) | **18** | 2.0 | Solo **1,800**; active ~**450** / idle ~**18**; stone **rice** (**2 SS**) |
| Spiked Boar (Ch 11 Emerald Wilderness) | **8** | **1.5** | Solo **600**; idle **+6 (1%)**; active **+150 (1/4)** each |
| Wereboar (Ch 13 floor 3) | **26** | **2.0** | Solo **2,600**; idle **+26 (1%)**; active **+650 (1/4)** each |
| Person / classed race (Ch 14 fencer) | **55** | 1.0 | Pool **2750**; equal fifth **550**; Roland **479**; Ned tips **25→26** |
| Carwen forest goblin | 3 | 1.0 | **150** |
| Carwen forest goblin | 4 | 1.0 | **200** |
| Same level hobgoblin | 4 | 1.75 | **350** |
| Same level myrmeke worker | 4 | 1.5 | **300** |
| Same level orc | 4 | 2.0 | **400** |
| Same level greater mantis | 4 | 3.0 | **600** |
| Gray Hobgoblin Berserker (Ch 37) | **59** | **2.25** | **6,638** (solo) |
| Fire Slime (Ch 71) | **2** | **1.5** (default) | **150** |
| Fiery Skeleton (Ch 72) | **10** | **1.25** | **625** |
| Crimson Giant Rat (Ch 75) | **14** | **0.2** (vermin) | **140** |
| Baby Salamander (Ch 75) | **21** | **1.5** (default) | **1,575** |

Same level, harder race → more XP. That is the whole point of RaceMult.

**Level-gap note (optional, not required for early arcs):** Source often treats far-weaker mobs as nearly worthless XP. If needed later, apply a soft penalty when the killer’s overall level is far above the monster (e.g. heavily reduced when gap ≥ 10). Do not use that to replace `50 × killed_L × RaceMult`.

At class **cap**, further XP does not raise that class. Bank it for the next class change (**no half-cut**; full carry; Ch 16 **1479** locked) or it sits until you switch. Do not invent a second XP bar per class. Class does not change what a monster fight pays (`Progression.md`).
