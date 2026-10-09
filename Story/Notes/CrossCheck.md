# CrossCheck

When updating chapter status screens, skills, traits, XP, coin or related facts, cross-check these files. The chapter text stays put. Filing is a copy, never a move.

## Source of truth

1. `Story/Chapters/` is the source for what Roland currently has on screen (live prose).
2. Copy numbers and wording from the chapter block. Do not invent fields the screen does not show (for example Height belongs in prose notes, not in the status box, unless the chapter puts it there).
3. If the chapter later renames or clarifies something (???? Sickness → Mana Sickness), record both steps when that matters.
4. **Rewrite law** for attributes, skill technique ranks and XP lives in `References/` plus `Story/Notes/StatusBreakdown.md`. When live chapter numbers disagree with rewrite law, keep the live block and add a rewrite-target note. Retcon the chapter when that chapter is rewritten.
5. **`Source/`** is the original novel. Do not “fix” Source spelling or numbers to match the rewrite. Search-and-replace scopes stop at Story, Notes, References and `.cursor`.

## Roland tracking (Story/Notes)

Update these together when a chapter changes his sheet. Keep history by chapter. Append. Do not overwrite earlier entries.

| Change in chapter | Update |
|---|---|
| Status / HP MP SP / attributes / class / effects / affinities / rank | `Status.md` |
| Attribute bucket math (Body / Class / Skills-Traits) | `StatusBreakdown.md` |
| Skills, traits, titles (Passive, Active, Spell, Class bonuses, trait cards) | `Skills.md` |
| Gear / carried items / Identify item blocks / pouch snapshot | `Items.md` |
| Consumable item types (healing potions, etc.) | `References/Items/Items.md` |
| Kill XP, bars, level-ups, kill totals, grind ledgers (coin tied to kills) | `Experience.md` |
| First-clear skill index / Source delay list | `Roland's Skills.md`, `Early Logical Skills.md` |
| Rewrite intent, plot beats, companion type, formatting rules | `Notes.md` |
| Ned companion level / form / attributes / skills by chapter | `NedStatus.md` |

Skills and traits often share one chapter menu. File both under that chapter in `Skills.md` (use a Traits subsection when useful). There is no separate `Traits.md`.

Current note coverage: Chapters 1 through 80.

## Catalogs (References)

Also update the matching reference when a named thing is new, renamed or its description changes:

| Topic | File |
|---|---|
| Skills and traits | `References/Progression/Skills.md` |
| Attributes and resource formulas | `References/Progression/Attributes.md` |
| Body / mental age tracks, technique ranks, daily loop | `References/Progression/Progression.md` |
| Spells | `References/Combat/Spells.md` |
| Classes (all named) | `References/Progression/Classes.md` |
| Roland’s classes | `References/Progression/RolandClasses.md` |
| Class / skill levels, XP, packages, skill attribute bonuses | `References/Progression/Levels.md` |
| Coin peg, wages, prices, ledgers | `References/World/Economy.md` |
| Food / meal flavor anchors | `References/Food/` (`Food.md`, `EssentialIngredients.md`, `EssentialFlavorings.md`) |
| Places (inns, towns, shops) | `References/World/Places.md` |
| Dungeon layouts / floor patterns | `References/World/DungeonDesign.md` |
| Adventurer ranks | `References/Progression/AdventurerRanks.md` |
| Family / house people | `References/People/Family.md` |
| Runes / schematics | `References/Runes/Runes.md` |
| Science / Earth tech anchors | `References/Science/Science.md` |
| Attack / shield joule scale (physical STR·AGI tips, Mana Shield pools, Ch 14 lock) | `References/Combat/AttackScale.md` |
| Weapons / blade loadout design | `References/Combat/Weapons.md` |
| Races, creatures, mounts, encounters | `References/World/` (`Races.md`, `Creatures.md`, `Mounts.md`, `Encounters.md`) |
| Technology / era baseline | `References/World/Technology.md` |
| People (family, Ned design) | `References/People/` |
| Potential magic rungs | `References/PotentialMagic/PotentialMagic.md` |
| Ideas scratch | `References/Ideas.md` |

`Story/Notes` holds Roland's personal sheet by chapter. `References` holds the world catalog. Keep both. Do not delete one because the other exists.

## Attribute rewrite rules (quick)

```
Displayed = Body + Class levels + Skills/Traits (+ Other if needed)
```

- **Body:** `Progression.md` trained physicals + adult-mind Int/Will age row.
- **Class:** packages only (Mage = +1 Int and +1 Will per level).
- **Skills/Traits:** skill bonus = **+1 × current skill level** per favored attribute; traits are flat cards.
- Full early tallies: `StatusBreakdown.md`.

## XP / coin quick rules

- Kill XP: `50 × killed_L × RaceMult` (`Progression.md` / `Levels.md`). Goblin **1.0**; rat **0.2**; worm **0.5**; moth **2.0**; spiked boar **1.5**; wereboar **2.0**; people **1.0**. Ch 14 L55 pool **2750** / Roland **479**.
- Class bar: `XP_to_next(L) = 500 × L`.
- People danger ≠ sheet alone: stats × skills × gear × tactics (`Levels.md`). Companions take kill XP without eating the corpse.
- Pre-class bank: half penalty, **one-time** on first ascension only (`Experience.md`).
- Skill / spell rank XP can fill a bar but must not silently cut a locked kill count.
- Pouch math: update `Experience.md` (grind ledgers), `Items.md` (kit / stones), `Status.md` (chapter coin lines), `Economy.md` / `Places.md` when a quoted price changes.

## Common traps

- Never rewrite older chapter entries when something levels later. Append the new level under the chapter where it happens. Leave transfer and prior snapshots alone (add rewrite-target notes beside them).
- Chapter text shows what the scene shows. System level-up lines in prose do not have to list every stat bonus. **Stat bonuses still go in Notes** (`Skills.md`, `Status.md`, `Roland's Skills.md`, `Notes.md`) under that chapter. Do not drop the bonus from notes because it was removed from chapter wording.
- Skill rename in rewrite (example: **Technology** vs old Circuitry). Fix chapter, Story/Notes and References. Leave Source as Circuitry.
- Class rename in rewrite: **Scribe** (Mana Scribe / Runic Mana Scribe), not Scrybe. Fix Story/Notes/References/`.cursor`. Leave `Source/` as Scrybe.
- Trait listed under the Skills menu in chapter text. Still file it under the Traits subsection in `Skills.md` (Notes and References).
- Class bonuses and affinity screens. Put them in Status for that chapter, and Spells or Skills if they unlock named abilities.
- Resource math. If formulas change, update `References/Progression/Attributes.md` and any Status note that quotes them.
- Later chapters. When filing a new status block, keep earlier chapter entries. Append. Do not overwrite the history.
- Do not treat Source Ch 7 “all Basics L9” / Leather L4 as canon. Live Story Ch 7 uses `Progression.md` age-10 technique targets.
- Destination beats: Ch 9.5 ends on research, not a named next city. Ch 10 on-page may still pick **Edelgard**. Do not backfill Edelgard into Ch 9.5 notes.
- Self-taught Absorption / Reinforcement land in Ch 9.5. Later Source book beats become practice ranks only (`Skills.md`, `Roland's Skills.md`).

## Quick pass after an edit

1. Chapter block still intact.
2. Matching Story/Notes file updated for that chapter (`Status`, `Skills`, `Items`, `Experience`, `Notes` as needed).
3. Matching References entry added or corrected if the name, price or effect is catalog material.
4. If attributes or skill ranks changed, check `StatusBreakdown.md` / `Progression.md` for rewrite targets.
5. No leftover old name in rewrite files (search the old term; ignore `Source/`).
6. If kills, XP bars or pouch changed: `Experience.md` totals, chapter Notes beat and any Economy/Places quote still match.

## Open checks (Ch 1–19 rewrite pass)

Synced for the live Ch 1–19 rewrite: estate doubles → Ch 9 L3→L4, Ch 9.5 kill/coin/stone ledger (**1,000** / end **3,595 LC** / **218** rice + **8** leader), Ch 10 nest (**+7** / **220** rice + **8** leader / pouch **3,630 LC**), rewrite L20 inn sheet (spells Bolt **L5** / Arrow **L4** / Shield **L3** / Heat **L5** / Hands **L5**; **no skill evolves**; Abs/Reinf **L9**), Ch 11 first dungeon day + trial weeks (Spiked Boar **L8** RaceMult **1.5**; day **456** XP; bar **~8,540/10k** / pouch **~4,413 LC**), Ch 12 Iron Flagon (**−45** → **~4,368 LC**; **12** worms **+1,272** → bar **~9,812/10k**; **Basic Taming** pet scarf), Ch 13 **half year with girls** after **3 mo** goblins (**342** kills / kill **40,776** + skill **4,608** → Mage L25 / pouch **~5,977 LC**; leave age **11** / **6y**; live sheet Str **49** / Agi **63** / Int **137** / MP **2292** / SP **956**; **Basic Dodging L6**), Ch 14 watcher (**+479** / **Basic Dodging L7** / Ned **25→26**), Ch 15 cremation + Detonation [Highest] (**+1000 XP** / **Runic Scholar**; bank **1479**; Enchanter path affinity-gated), Ch 16 **Runic Mana Scribe** (five-region Fire Orb trial; mana-hand blunder; Ned silk; **full bank 1479 / 13000**), Ch 17 **L26** / Scribe **L1** (Ned wake; shield-muffled rapier; shows **Edelgard**; letters to father/Martha; wallet **5,977 → +5 SG → ~10,977 → ~11,641** personal), Ch 18 Impact [Highest] + Drawing L1 (**+1000**; bar **2479 / 13000**); Bronze→Steel; parting **+10 SG** → enter Ch 19 **21,641 LC**; hugs farewell / train to Edelgard, Ch 19 train week (Sound/Echo **L7**; Breath **L5**; grill slate; Fire Orb High→Highest **+1000** → bar **3479 / 13000**; Solaria **1 SS**; end wallet **21,598 LC**), Absorption/Reinforcement self-taught, Scribe spelling, Ch 9.5 destination = research only, Ch 10 picks **Edelgard**. Narrative threat: `MonsterThreat.md`.

**Post–Ch 13 status:** every chapter through **80** now has a rewrite line or full Live+Rewrite sheet in `Status.md`. Full-sheet rewrite checkpoints: Ch **17 / 23 / 27 / 34 / 47 / 62 / 68 / 77** (`StatusBreakdown.md` delta table). Method: Ch 13 rewrite baseline + Source growth deltas; Luck seed **7**; Mage secondary mana bonuses kept. Ch 17–18 rewrite sheets stay **L27** / Scribe **L1** (Drawing Dex **+10** into Ch 18); later checkpoints still need re-audit when those chapters rewrite.

Still needs attention when touching these beats:

| Item | Where | Check |
|---|---|---|
| Ch 10 Edelgard goal | `Notes.md`, `Status.md`, `RolandClasses.md`, chapter | OK for Ch 10+. Must stay out of Ch 9.5 close. |
| Ch 19+ party / dungeon notes | Notes 20–80 | Written to Source plot. Re-audit when those chapters are rewritten. |
| Ch 11 day haul lock | `Experience.md`, `Economy.md`, `Items.md`, `Notes.md` | Prose says “more” boars; lock stays **4** / **2** stones / **+128 LC** unless chapter names a count. |
| Ch 12 drink / worm ledger | `Experience.md`, `Items.md`, `Notes.md`, `Skills.md` | First round **45 LC**; pocket **12** worms **+1,272 XP**; bar **~9,812/10k**; pet worm kept; Hands ≥**L7**. |
| Ch 13 half-year Floor-3 | `Experience.md`, `Items.md`, `Skills.md`, `Status.md`, `StatusBreakdown.md`, `Timeline.md`, `Economy.md` | Carwen lock: **3 mo** goblins + **half year** with girls = **9 mo** total; leave age **11** / world **6y**. **342** kills; kill **40,776** + skill **4,608** → L25; haul **+5,857**; pouch **~5,977 LC**; Wereboar mats **156**. Live sheet Str **49** / Agi **63** / Int **137** / MP **2292** / SP **956**; **Basic Dodging L6**. No skill-name evolves. |
| Ch 11–12 pouch / trial XP | `Items.md`, `Notes.md`, `Status.md`, `Experience.md` | Pouch **3,630 → 3,758 → ~4,413 → ~4,368**. Trial kill **+2,184** + Hands **~100** → bar **~8,540/10k**. Incantation stays **L6**. |
| Ch 14 watcher / Ned evo | `Notes.md`, `NedStatus.md`, `Ned.md`, `Levels.md`, `Encounters.md` | Fencer **L55** / girls **~45**; people XP **`50 × L`**; pool **2750** / Roland **479**; Ned **25→26** **Greater Needle Worm** **4x**. |
| Ch 19 train / Ned / Edelgard | `Skills.md`, `NedStatus.md`, `Ned.md`, `Notes.md`, `Status.md`, `Items.md`, `Places.md` | Sound/Echo **L7**; Multitask **L5**; Breath **L5**; grill Heat/Cold/Pain **L5**; Recovery **L5**; Poison **L6**. Ned Spike/Stealth/Climb **L7**; Seal/Pain/Heat/Cold **L5**. Solaria tip **1 SS**; map **19 LC**; Crow **14 LC**; enter wallet **21,641 LC** (own savings + parting **10 SG**); end **21,598 LC**. |
| Ch 19 Fire Orb schematic | `Notes.md`, `Items.md`, `Experience.md`, `Skills.md`, `Status.md`, `Levels.md` | Memory: **[High] +600** (uneven) then thin-sheet **[Highest] +400** (total **1000**); lesser quality ladder **100/200/400/600/1000**; bar **3479 / 13000**; Source one-shot Highest discarded. |
| Writing tools / pencil invent | `WritingTools.md`, `Places.md`, `Ideas.md`, `Ned.md`, `Notes.md` Ch 19–20 | Terra: soft metal, chalk, quills, rare fountain pens. **No** common pencil; **no** Edelgard lump graphite. Roland synthesizes graphite; Ned toxin-free spike; invents pencil then pen after metalwork. Source Ch 20 “buys pencil” dropped (prose still has Source buys at Ch 20/22/26 until rewritten). |
| Paper / hide surfaces | `Paper.md`, `Economy.md` §17, `WritingTools.md`, `Technology.md` | Craftsman economy. Lock vs early pegs / **Ch 19 only**. Lowest magical hide **2–6 LC** (~**4–5** typ) undercuts paper **5–12**. Magical paper **20–60**. Mundane parchment **25–80** / finest **60–250**. Source Ch 20 blank≈scroll prices discarded; retune when writing Ch 20+. |
| Ch 14 ambush | `Skills.md`, `Status.md`, `Notes.md` | **Basic Dodging L6→L7** mid-chase; Agi **64** / SP **959**. |
| Wallet path Ch 13→19 | `Experience.md`, `Items.md`, `Status.md`, `Notes.md` | **5,977** → **+5 SG** → **10,977** → **+~664** → **11,641** → **+10 SG** → enter **21,641** → tip/map/Crow → **21,598**. |
| Ch 15 cremation / schematic | `Notes.md`, `Items.md`, `Experience.md`, `Skills.md`, `Weapons.md` | Body burn **1000 MP**; tip **125 MP**; hold-lock insert; Detonation [Highest] **+1000**; bank **1479**; Enchanter affinity dead-end. |
| Ch 16 Fire Orb trial | `Notes.md`, `Skills.md`, `Items.md`, `RuneCraftScrapes.md`, `Runes.md`, `RuneSystem.md` | Five-region linear chain; temp skills after book; mana-hand cascade ~**1/4 MP**; success fist orb; Ned silk; no binary / max-size hard rule on-page. |
| Ch 17 leave / L26 sheet | `Notes.md`, `Items.md`, `Status.md`, `Family.md`, `Encounters.md` | Ned wake; shield-muffled rapier (**2096/2309**); shows **Edelgard**; letters to father/Martha; loot **>20 SG** / girls **+5**; hammer ask. |
| Ch 18 Impact / farewell | `Notes.md`, `Items.md`, `Experience.md`, `Skills.md`, `AdventurerRanks.md` | Impact [Highest] + Drawing L1; bar **2479 / 13000**; Bronze→Steel; parting bag; hugs; component fantasies. |
| Mana Bolt joule / Int curve | `References/Science/ManaCast.md`, chapter fight beats | Keep formula and on-page damage language aligned when editing fights. |
| Meal / lodging quotes | `References/World/Society/Economy.md`, PlacesDesign, Ch 9 Notes | Meal **5 LC**; lodging **1 SS**/night + **5 LC** breakfast; monthly ~**10%** on **30** nights → **270 LC**. Year = **12×30 + New Year's Day** (**361**). |
| Goblin Hunter title | `Skills.md` / `Status.md` Ch 9.5–10 | Past **1000** kills into the skip; card text matches chapter. |
| Ch 10 nest ledger | `Experience.md`, `Items.md`, `Status.md`, `Notes.md` | **+7** kills → **1,095**; pouch **3,630 LC**; stones **220** rice + **8** leader. |
| Source delay skills | `Roland's Skills.md`, `Early Logical Skills.md` | Absorption/Reinforcement already owned in rewrite; Heat/Hands self-taught Ch 9.5; later book chapters = rank practice only. |
| Search Scrybe | Story / Notes / References / `.cursor` | Must stay empty. `Source/` may keep Scrybe. |
