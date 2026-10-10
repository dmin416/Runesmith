# Progression

Live status / XP / class foundation. Guild ranks: `AdventurerRanks.md`.

| File | Role |
|---|---|
| `Progression.md` | XP, tiers, resources, reclass locks |
| `RaceMult.md` | Live RaceMult table + worked kills |
| `ExperienceCurve.md` | Overall XP curve, schematic ladders, grind samples |
| `SkillRanks.md` | Skill L1–L9 / evolve + field-use curve |
| `ClassPackages.md` | Class packages + tier multipliers + forward-only |
| `Levels.md` | Stub index only (points at the four files above) |
| `AdventurerRanks.md` | Eight-rank guild ladder + chapter notes |
| `Attributes.md` | Stat / resource / blood / affinity locks |
| `AttributesDesign.md` | Fat attribute blurbs (design loot) |
| `Classes.md` | Tier / path thin hub |
| `ClassesDesign.md` | Named world class catalog (design loot) |
| `RolandClasses.md` | Roland planned vs attained path (live) |
| `Skills.md` | Skill law thin hub |
| `SkillsDesign.md` | Named skills / traits catalog (design loot) |
| `NormalPersonSkills.md` | Ordinary L9 training clocks (design loot) |
| `SkillsRedesign.md` | WIP redesign park (design loot; not a second lock) |
| `Training.md` | Age / technique / endurance tracks (+ Career Scale appendix) |
| `CareerScale.md` | Stub → Training appendix |
| `../SourceLoot/RolandStatus.md` | Source status scrape |
| `../../Story/Notes/Experience.md` | Chapter XP ledger (Ch 4–19 locked) |

## Narrative

Everyone has a status system with attributes and resources. Skills like Identify, Analyze, and Mana Sense exist. Affinities gate elemental mage paths. Classes and monster evolutions share the same tier caps (T1 25, T2 50, T3 75, T4+ 100 each). Combat and production paths are both valid. Overall level is a sheet number that sets XP needed to advance. No mana pool → no active ambient absorb. Mana-rich places may heal body/spirit without storing mana. Forced absorb before Mage/Acolyte (or any no-pool body) poisons or kills like radiation (`../Runes/Energy.md`). Enchanting and runecrafting are different crafts. Diagnosis is D-only. Death is death; only D is a transmigrator.

## Detail

**Status:** Native. Everyone has one. Screens are private unless shared (or forced by a strong enough peek skill / item).

**Attributes:** Strength, Agility, Dexterity, Vitality, Endurance, Intelligence, Willpower, Charisma, Luck.

**Resources:** HP, MP, SP. Derived from attributes (formulas below).

**Info skills:** Identify and Analyze exist in the world.

**Mana Sense:** Exists as a skill / aptitude some people have.

**Diagnosis:** D-unique. Not a normal world skill. Sees / understands flaws in a system. Feeds his medical background. Old name was Debugger. See `Skills.md` and `../People/Roland/Character.md` with Technology and Fabrication.

**Affinities:** Matter for elemental mage paths. Detail: `Attributes.md`.

**Skill ranks:** Every skill name hard-caps at **L9**. It **evolves** at **2,000,000** clean uses, when the ability surpasses itself. The next form starts at L1. No L10 on the same name. Class skills use the same rule. Full tables: `SkillRanks.md` / `Skills.md`. Using an ability at its current peak accelerates the climb; that is mostly narrative pacing on top of the clean-use counts.

**Skill scope:** A skill is the general ability, not the first thing he practiced on. Chapter 4: Tinkerer and Technology let him reassemble a clock he had never worked on. Poison Resistance is poison. The sound sense evolves Echolocation → Vibration Sense → Energy Sense.

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
XP_kill = 50 × killed_L × RaceMult
```

Round to nearest whole XP after RaceMult. Family table: `RaceMult.md`. Common goblin **RaceMult = 1.0**. Same level, harder race → more XP. At RaceMult 1.0, even fight (same level) ≈ **10%** of the killer's bar. Weaker / stronger level still scales the pool. Party contribution splits the pool. People / classed races use **RaceMult 1.0** (same `50 × L` shape). Default unlisted monster **1.5**. Curve / schematic ladders: `ExperienceCurve.md`.

**Party XP:** Split by ability and contribution. Early dungeon lock: idle / spectating ~**1%** of the kill; active help ~**1/4**. Later beats can refine the formula without reopening those counts.

**Craft / schematic XP:** First-time basic / lesser rune schematic at **[Highest]** pays **1000** XP. Quality ladder toward that: **100 / 200 / 400 / 600 / 1000** (raise pays the difference). A first Common schematic pays **2×** that lesser Highest award (**2000** XP, Fire Arrow). Repeat copies / practice crafts pay much less. Spell and skill rank-ups can also award XP.

**Pre-class bank:** XP before first ascension banks and applies at first class with a **½** penalty. One-time only. Does not refill for later class changes.

**Experience logs:** Quarantined leftovers in `ExperienceCurve.md` and `../../Story/Notes/Experience.md`. Retune chapter digits against this kill line; do not re-import class-change half-cut or Old `(49 + L)` / own-base formulas.

### Resources from attributes

```
HP = (Vitality × 10) + (Endurance × 3)
SP = (Endurance × 10) + (Strength × 3) + (Agility × 3)
MP = (Intelligence × 10) + (Willpower × 4)
```

Skill bonuses can raise displayed pools above the bare formulas. **Mage** = mana recovery (kept as secondary; lost when Mage is dropped). **Blessed by Mana** = multiplies mana recovery. Neither changes max MP.

### Ascension and classes

**Ascension / class crystal:** Needed to gain or change class. First use awards a class (confirm). Later uses need a trial (battle, craft, or puzzle). First-use crystal turns to dust. The trial is a personal realm. Long subjective time inside can equal seconds outside. The place Roland sees is in `../World/Geography/PlacesDesign.md`.

**Reclass:** No hard lifetime class count. Cannot leave a class for another until at least **25** levels in the current one. Tier 1 classes must be finished to their **L25** cap before leaving. **No half-cut bank on class change** (Old half-cut dropped). Cap overflow banks in full; Ch 16 carry **1479** locked in `../../Story/Notes/Experience.md`.

**Multiple classes:** Primary plus at most **one** secondary that keeps the class’s **narrative** special effect. Switch secondary **once per day**. No tertiary active slot. Maxed lower tiers can sit inactive on the sheet. Drop a class from secondary and its narrative benefit goes with it.

**Class packages:** On class level-up, favored attributes gain points. Those gains are **permanent**. Tier 1 default: **+1 per favored attribute** per class level. Active tier growth rate can scale the package (forward-only). Detail tables: `ClassPackages.md` / `ClassesDesign.md` (design). Class cards (Mage mana recovery, Blacksmith / Runic Blacksmith fire resistance + stamina recovery, Scribe learning-ease, etc.) are separate narrative benefits, not package math.

**Pre-class mana:** Ambient absorb before Mage / Acolyte = poison / death. Training other skills is still possible.

**Taming:** Real skill path. Companions can level.

**Craft split:** Enchanting and runecrafting are different crafts in the world's eyes.

**XP measure:** Kill XP tracks fight difficulty. Craft and practice still pay from repetition, exertion, and danger.

**People-kill XP:** Exists. High-stakes. `50 × overall level × RaceMult 1.0`.

**Skills → attributes:** Skill levels can raise attributes.

**Attribute perks:** One named perk per core attribute at **40** (Cha/Luck out unless a later trait says otherwise). Blessed by Mana needs Mage. List: `Attributes.md`.

**Titles:** Exist and can grant benefits.

**Death:** Death is death. Only D is a transmigrator. Not a public world mechanic.

**Guild ranks:** Eight-rank ladder in `AdventurerRanks.md`.

## Open

Pull fat class / skill cards when a beat needs them. Later party-split formula refinements beyond early ~**1%** / ~**1/4** if a fight needs them.
