# Attributes

Attribute explanations from the status screen. First seen: Chapter 2.

For physical and mental scale: untrained adult man average **15**, trained age tables (body + adult-mind Int/Will), and linear real-output conversion (Output = k × S), see `Progression.md`.

## Strength
Indicates the physical power of an individual, increases attack damage and stamina slightly.

SP: +3 per point of Strength.

## Agility
Indicates how agile and nimble a person is, increases speed, quickness and stamina slightly.

SP: +3 per point of Agility.

## Dexterity
Indicates skill in performing tasks, especially with the hands, increases attack damage with finesse weapons and attack speed.

## Vitality
Increases health points, defense, physical resistances and the life span of an individual.

HP: +10 per point of Vitality.

## Endurance
Increases an individual's stamina, stamina regeneration and health points slightly.

HP: +3 per point of Endurance.
SP: +10 per point of Endurance.

### Blood restore (human / Roland)

Earth baseline for a **5 L** adult, then speed by Vit/End.

```
M = ((Vitality + Endurance) / 2) / 15
```

Adult Vit/End **15/15** → **M = 1.0**. Rate × M; times ÷ M.

- **Plasma (~2.75 L):** **100–150 mL/h** at M = 1 (fluid intake + internal shifts); full volume **24–48 h**.
- **Red cells (~2.25 L of that 5 L):** **15–25 mL/day** at M = 1 (marrow; faster if erythropoietin ramps after loss). Replacing **1 L** RBCs takes **4–6 weeks** at M = 1.

Use **rewrite** sheets for continuity (`Status.md` / `StatusBreakdown.md`). Live Ch 13 Source block (Vit **25** / End **26**) is not the math lock.

| Snapshot | Vit | End | M | Plasma rate | Full plasma | RBC rate | 1 L RBCs |
|---|---|---|---|---|---|---|---|
| Adult baseline | 15 | 15 | **1.00** | 100–150 mL/h | 24–48 h | 15–25 mL/day | 4–6 weeks |
| Roland Ch 13 rewrite | 47 | 53 | **3.33** | **333–500 mL/h** | **~7–14 h** | **50–83 mL/day** | **~1.2–1.8 weeks** |

Small Mana Hands drips to Ned are a trivial plasma hit at Roland’s M; marrow lag still owns any real bleed. Ned hemolymph (mass-scaled caterpillar): `Ned.md`.

## Intelligence
Increases an individual's mana points, magic attack and learning speed. Helps visualize and recall spell circles (Chapter 10).

MP: +10 per point of Intelligence.

## Willpower
Increases an individual's resistance to elemental attacks, status effects and mana points slightly.

MP: +4 per point of Willpower.

## Charisma
Indicates an individual's charm. A measure of personality, persuasiveness, leadership.

## Luck
Increases the chance of critical attacks and other various skills related to chance.

## Resource Formulas

First worked out by Roland in Chapter 2. Checked against later status sheets.

- HP = (Vitality x 10) + (Endurance x 3)
- SP = (Endurance x 10) + (Strength x 3) + (Agility x 3)
- MP = (Intelligence x 10) + (Willpower x 4)

**Cast law:** `Useful (J) = mana × 10 × η(L) × μ(INT)` with `η(1)=0.3`, `η(L)=1+(L-2)×2/7` (L2=1 … L9=3), `μ=(INT/15)^0.8`. See `Science.md`.

Skill, trait and class bonuses can raise displayed MP above the bare attribute total. Chapter 23: low mana → dizzy/sleepy; **zero MP** → splitting headache and possible pass-out, plus a next-day mana-regen debuff.

## Elemental affinities

Hidden until after the **first class**. First seen: Chapter 5.

At Tier 1 the sheet shows the basic four: Fire, Wind, Earth, Water. Higher-tier elements (lightning, gravity and others) unlock later. Affinity % steers which elemental mage paths open. Roland’s first read is **0% / 0% / 0% / 0%** (unprecedented to House Arden). A glass measuring orb is also used; it glows faintly with no useful reading when affinities are zero.

Chapter 6 book: an **elemental affinity skill** needs at least **~1%** affinity. Zero on all four blocks elemental mage T2s and the weak Superior Mage upgrade. Rare (~one in a million). Typical new mage Intelligence sits near **20**.

## Class resource bonuses (examples)

### Mage (Tier 1)
First seen: Chapter 6 skill card
- **+20%** max mana
- **+15%** mana regeneration
Applies on top of attribute MP. **Blessed by Mana** is narrative mana regen only (no flat MP). See `Skills.md`.

## Attribute perks

Rewrite map of one perk per core attribute at **40**. Full list and notes: `Skills.md` (Attribute perks under Traits).

| Stat | Perk name | Perk theme | Threshold |
|---|---|---|---|
| Strength | Titan's Back | Carry capacity | 40 |
| Dexterity | Exacting Motion | Accuracy of body movement | 40 |
| Intelligence | Blessed by Mana | Mana regeneration (narrative) | 40 + Mage |
| Willpower | Unbroken Focus | Focus | 40 |
| Agility | Sure Footing | Balance | 40 |
| Vitality | Defiance of Years | Reduced aging | 40 |
| Endurance | Rapid Renewal | Recovery speed | 40 |
