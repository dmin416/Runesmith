# CrossCheck

When updating chapter status screens, skills, traits or related facts, cross-check these files. The chapter text stays put. Filing is a copy, never a move.

## Source of truth

1. `Story/Chapters/` is the source for what Roland currently has on screen (live prose).
2. Copy numbers and wording from the chapter block. Do not invent fields the screen does not show (for example Height belongs in prose notes, not in the status box, unless the chapter puts it there).
3. If the chapter later renames or clarifies something (???? Sickness → Mana Sickness), record both steps when that matters.
4. **Rewrite law** for attributes, skill technique ranks and XP lives in `References/` plus `Story/Notes/StatusBreakdown.md`. When live chapter numbers disagree with rewrite law, keep the live block and add a rewrite-target note. Retcon the chapter when that chapter is rewritten.

## Roland tracking (Story/Notes)

Update these together when a chapter changes his sheet. Keep history by chapter. Append. Do not overwrite earlier entries.

| Change in chapter | Update |
|---|---|
| Status / HP MP SP / attributes / class / effects / affinities / rank | `Status.md` |
| Attribute bucket math (Body / Class / Skills-Traits) | `StatusBreakdown.md` |
| Skills, traits, titles (Passive, Active, Spell, Class bonuses, trait cards) | `Skills.md` |
| Gear / carried items / Identify item blocks | `Items.md` |
| First-clear skill index / Source delay list | `Roland's Skills.md`, `Early Logical Skills.md` |
| Rewrite intent, plot beats, companion type, formatting rules | `Notes.md` |

Skills and traits often share one chapter menu. File both under that chapter in `Skills.md` (use a Traits subsection when useful).

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
| Adventurer ranks | `References/AdventurerRanks.md` |
| Family / house people | `References/Family.md` |
| Places | `References/Places.md` |
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

## Common traps

- Never rewrite older chapter entries when something levels later. Append the new level under the chapter where it happens. Leave transfer and prior snapshots alone (add rewrite-target notes beside them).
- Chapter text shows what the scene shows. System level-up lines in prose do not have to list every stat bonus. **Stat bonuses still go in Notes** (`Skills.md`, `Status.md`, `Roland's Skills.md`, `Notes.md`) under that chapter. Do not drop the bonus from notes because it was removed from chapter wording.
- Skill rename in rewrite (example: Technology vs old Circuitry). Fix chapter, Story/Notes and References.
- Trait listed under the Skills menu in chapter text. Still file it under the Traits subsection in `Skills.md` (Notes and References).
- Class bonuses and affinity screens. Put them in Status for that chapter, and Spells or Skills if they unlock named abilities.
- Resource math. If formulas change, update `References/Attributes.md` and any Status note that quotes them.
- Later chapters. When filing a new status block, keep earlier chapter entries. Append. Do not overwrite the history.
- Do not treat Source Ch 7 “all Basics L9” / Leather L4 as canon. Live Story Ch 7 uses `Progression.md` age-10 technique targets.

## Quick pass after an edit

1. Chapter block still intact.
2. Matching Story/Notes file updated for that chapter.
3. Matching References entry added or corrected if the name or effect is catalog material.
4. If attributes or skill ranks changed, check `StatusBreakdown.md` / `Progression.md` for rewrite targets.
5. No leftover old name in the other files (search the old term).
