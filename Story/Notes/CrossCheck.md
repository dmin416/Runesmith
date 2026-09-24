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
| Skills and traits | `References/Skills.md` |
| Attributes and resource formulas | `References/Attributes.md` |
| Body / mental age tracks, technique ranks, daily loop | `References/Progression.md` |
| Spells | `References/Spells.md` |
| Classes (all named) | `References/Classes.md` |
| Roland’s classes | `References/RolandClasses.md` |
| Class / skill levels, XP, packages, skill attribute bonuses | `References/Levels.md` |
| Coin peg, wages, prices, ledgers | `References/Economy.md` |
| Food / meal flavor anchors | `References/Food.md` |
| Places (inns, towns, shops) | `References/Places.md` |
| Dungeon layouts / floor patterns | `References/DungeonDesign.md` |
| Adventurer ranks | `References/AdventurerRanks.md` |
| Family / house people | `References/Family.md` |
| Runes / schematics | `References/Runes.md` |
| Science / Earth tech anchors | `References/Science.md` |
| Weapons / blade loadout design | `References/Weapons.md` |
| Races, creatures, mounts, encounters | matching `References/` file |

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

- Kill XP: `(49 + MonsterLevel) × RaceMult`. Common goblin RaceMult **1.0**. Dungeon rat: **`9 + level`**. Needle Worm: **`24 + level`**. Spiked Boar: **`499 + level`**.
- Class bar: `XP_to_next(L) = 500 × L`.
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
- Resource math. If formulas change, update `References/Attributes.md` and any Status note that quotes them.
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

## Open checks (Ch 1–12 rewrite pass)

Synced for the live Ch 1–13 rewrite: estate doubles → Ch 9 L3→L4, Ch 9.5 kill/coin/stone ledger (**1,481** / end **6,000 LC** / **286** rice + **16** leader), Ch 10 nest (**+7** / **288** rice + **16** leader / pouch **6,035 LC**), rewrite L20 inn sheet, Ch 11 first dungeon day + trial weeks (bar **~2,774/10k** / pouch **~6,818 LC**), Ch 12 Iron Flagon (**−45** → **~6,773 LC**) + Needle Worm cook/tame (**+492 XP** → bar **~3,266/10k**; **Basic Taming** pet scarf), Ch 13 half-year Floor-3 (**1,102** kills / **51,734 XP** → **Mage L25** / pouch **11,641 LC**; rewrite sheet Str **49** / Int **137** / MP **2542**), Absorption/Reinforcement self-taught, Scribe spelling, Ch 9.5 destination = research only, Ch 10 picks **Edelgard**.

**Post–Ch 13 status:** every chapter through **80** now has a rewrite line or full Live+Rewrite sheet in `Status.md`. Full-sheet rewrite checkpoints: Ch **17 / 23 / 27 / 34 / 47 / 62 / 68 / 77** (`StatusBreakdown.md` delta table). Method: Ch 13 rewrite baseline + Source growth deltas; Luck seed **7**; Mage secondary mana bonuses kept.

Still needs attention when touching these beats:

| Item | Where | Check |
|---|---|---|
| Ch 10 Edelgard goal | `Notes.md`, `Status.md`, `RolandClasses.md`, chapter | OK for Ch 10+. Must stay out of Ch 9.5 close. |
| Ch 13+ party / dungeon notes | Notes 13–80 | Written to Source plot. Re-audit when those chapters are rewritten. |
| Ch 11 day haul lock | `Experience.md`, `Economy.md`, `Items.md`, `Notes.md` | Prose says “more” boars; lock stays **4** / **2** stones / **+128 LC** unless chapter names a count. |
| Ch 12 drink / worm ledger | `Experience.md`, `Items.md`, `Notes.md`, `Skills.md` | First round **45 LC**; pocket **12** worms **+492 XP**; pet worm kept; Hands ≥**L7**. |
| Ch 13 half-year Floor-3 | `Experience.md`, `Items.md`, `Skills.md`, `Status.md`, `StatusBreakdown.md`, `Economy.md` | **1,102** kills; **51,734 XP** → L25; haul **+9,116**; pouch **11,641 LC**; Wereboar mats **156**. Rewrite sheet Str **49** / Int **137** / MP **2542**; Live Source block still on-page. |
| Mana Bolt joule / Int curve | `References/Science.md`, chapter fight beats | Keep formula and on-page damage language aligned when editing fights. |
| Meal / lodging quotes | `Economy.md`, `Places.md`, Ch 9 Notes | Meal **5 LC**; lodging **1 SS**/night + **5 LC** breakfast; monthly ~**10%** on **28** nights → **252 LC**. Year = **13×28**. |
| Goblin Hunter title | `Skills.md` / `Status.md` Ch 9.5–10 | Past **1000** kills into the skip; card text matches chapter. |
| Ch 10 nest ledger | `Experience.md`, `Items.md`, `Status.md`, `Notes.md` | **+7** kills → **1,576**; pouch **6,035 LC**; stones **288** rice + **16** leader. |
| Source delay skills | `Roland's Skills.md`, `Early Logical Skills.md` | Absorption/Reinforcement already owned in rewrite; Ember/Hands self-taught Ch 9.5; later book chapters = rank practice only. |
| Search Scrybe | Story / Notes / References / `.cursor` | Must stay empty. `Source/` may keep Scrybe. |
