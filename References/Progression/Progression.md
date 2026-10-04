# Progression

Live status / XP / class foundation. Guild ranks: `AdventurerRanks.md`.

| File | Role |
|---|---|
| `Progression.md` | XP, tiers, resources, reclass locks |
| `AdventurerRanks.md` | Eight-rank guild ladder |
| `AdventurerRanksDesign.md` | Chapter rank detail |
| `Attributes.md` | Stat / resource / blood / affinity locks |
| `AttributesDesign.md` | Fat attribute blurbs |
| `Classes.md` | Tier / path thin hub |
| `ClassesDesign.md` | Named world class catalog |
| `RolandClasses.md` | Roland planned vs attained path |
| `Skills.md` | Skill law thin hub |
| `SkillsDesign.md` | Named skills / traits catalog |
| `NormalPersonSkills.md` | Ordinary L9 training clocks |
| `TempRolandSkillChanges.md` | Skill redesign pass |
| `Training.md` | Age / technique / endurance tracks |
| `Levels.md` | **Quarantined** XP leftovers (RaceMult / half-cut); retune logs only |
| `../SourceLoot/RolandStatus.md` | Source status scrape |
| `../../Story/Notes/Experience.md` | Chapter XP ledger (retune later) |

## Narrative

Everyone has a status system with attributes and resources. Skills like Identify, Analyze, and Mana Sense exist. Affinities gate elemental mage paths. Classes and monster evolutions share the same tier caps (T1 25, T2 50, T3 75, T4+ 100 each). Combat and production paths are both valid. Overall level is a sheet number that sets XP needed to advance. Before a Mage or Acolyte class, absorbing ambient mana poisons or kills. Enchanting and runecrafting are different crafts. Diagnosis is D-only. Death is death; only D is a transmigrator.

## Detail

**Status:** Native. Everyone has one. Screens are private unless shared (or forced by a strong enough peek skill / item).

**Attributes:** Strength, Agility, Dexterity, Vitality, Endurance, Intelligence, Willpower, Charisma, Luck.

**Resources:** HP, MP, SP. Derived from attributes (formulas below).

**Info skills:** Identify and Analyze exist in the world.

**Mana Sense:** Exists as a skill / aptitude some people have.

**Diagnosis:** D-unique. Not a normal world skill. Sees / understands flaws in a system. Feeds his medical background. Old name was Debugger. See `Skills.md` and `../People/Roland/Character.md` with Technology and Fabrication.

**Affinities:** Matter for elemental mage paths. Detail: `Attributes.md`.

**Skill ranks:** Technique / basic skill soft-cap around **L9**. Class skills can go past basic caps with the class. Full tables later.

**Tiers (people and monsters):** Same tier ladder for person classes and monster evolutions.

| Tier | Class / evolution level cap |
|---|---|
| T1 | **25** |
| T2 | **50** |
| T3 | **75** |
| T4 and above | **100** each |

**Class paths:** Combat and production classes are both valid.

**Overall level:** A single number on the sheet. It sets XP needed to level up.

**XP to next level:**
```
XP_to_next(L) = 500 × L
```

**Kill XP (solo full credit):**

```
XP_kill = 50 × killed_L
```

Even fight (same level) ≈ **10%** of the killer's bar. Weaker prey pays less. Stronger prey pays more. Party contribution splits the pool. People kills use the same shape. No RaceMult multiplier.

**Party XP:** Split by ability and contribution. Idle / spectating can still take a thin cut (~1% of the kill in Old early dungeon). Active help raises the cut. Exact split math returns with Experience retune.

**Craft / schematic XP:** First-time basic / lesser rune schematic at **[Highest]** pays **1000** XP. Quality ladder toward that: **100 / 200 / 400 / 600 / 1000** (raise pays the difference). Repeat copies / practice crafts pay much less. Spell and skill rank-ups can also award XP.

**Pre-class bank:** XP before first ascension banks and applies at first class with a **½** penalty. One-time only. Does not refill for later class changes.

**Experience logs:** Quarantined leftovers in `Levels.md` and `../../Story/Notes/Experience.md`. Retune against this file's kill line; do not re-import RaceMult or class-change half-cut.

### Resources from attributes

```
HP = (Vitality × 10) + (Endurance × 3)
SP = (Endurance × 10) + (Strength × 3) + (Agility × 3)
MP = (Intelligence × 10) + (Willpower × 4)
```

Class and skill bonuses can raise displayed pools above the bare formulas (e.g. Mage **+2% max MP** and **+1% mana regen** per Mage class level).

### Ascension and classes

**Ascension / class crystal:** Needed to gain or change class. First use awards a class (confirm). Later uses need a trial (battle, craft, or puzzle). First-use crystal turns to dust.

**Reclass:** No hard lifetime class count. Cannot leave a class for another until at least **25** levels in the current one. Tier 1 classes must be finished to their **L25** cap before leaving. **No half-cut bank on class change** (Old half-cut dropped). Exact overflow / carry into the next class returns with Experience retune.

**Multiple classes:** Primary plus at most **one** secondary that keeps special effects. Switch secondary **once per day**. No tertiary active slot. Maxed lower tiers can sit inactive on the sheet.

**Class packages:** On class level-up, favored attributes gain points. Tier 1 default: **+1 per favored attribute** per class level. Active tier growth rate can scale the package (forward-only). Detail tables: `Levels.md` / `ClassesDesign.md` (design).

**Pre-class mana:** Ambient absorb before Mage / Acolyte = poison / death. Training other skills is still possible.

**Taming:** Real skill path. Companions can level.

**Craft split:** Enchanting and runecrafting are different crafts in the world's eyes.

**XP measure:** Kill XP tracks fight difficulty. Craft and practice still pay from repetition, exertion, and danger.

**People-kill XP:** Exists. High-stakes. Same `50 × overall level` shape.

**Skills → attributes:** Skill levels can raise attributes.

**Attribute perks:** One named perk per core attribute at **40** (Cha/Luck out unless a later trait says otherwise). Blessed by Mana needs Mage. List: `Attributes.md`.

**Titles:** Exist and can grant benefits.

**Death:** Death is death. Only D is a transmigrator. Not a public world mechanic.

**Guild ranks:** Eight-rank ladder in `AdventurerRanks.md`.

## Open

Party split exact math. Class-change XP carry detail. Experience chapter retune against live `50 × killed_L`. Pull fat class / skill cards when a beat needs them.
