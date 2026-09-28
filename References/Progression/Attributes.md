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

Earth baseline for a **5 L** adult, then speed by Vit/End, then by **Recovery** skill.

```
M = ((Vitality + Endurance) / 2) / 15
Recovery_time = 1 − 0.1 × Recovery_level    (L0 = 1.0; L5 = 0.5; L9 = 0.1)
Recovery_rate = 1 / Recovery_time            (L5 = 2×; L9 = 10×)
```

Adult Vit/End **15/15** → **M = 1.0**. Base rates × M. Then × **Recovery_rate** for how fast he actually restores blood / closes the same class of wound.

When Vit or End rises, **recompute M**. When Recovery levels, **recompute Recovery_rate**. Both stack.

- **Plasma (~2.75 L):** base **100–150 mL/h** at M = 1; effective = base × M × Recovery_rate.
- **Red cells (~2.25 L of that 5 L):** base **15–25 mL/day** at M = 1; effective = base × M × Recovery_rate.
- Full-volume / 1 L RBC clock: base times ÷ M ÷ Recovery_rate.

**Recovery covers blood loss, cuts, wounds and soft-tissue damage.** It does **not** regrow missing limbs (`Skills.md`).

| Snapshot | Vit | End | M | Rec | Plasma effective | RBC effective |
|---|---|---|---|---|---|---|
| Adult baseline | 15 | 15 | **1.00** | L0 **1×** | 100–150 mL/h | 15–25 mL/day |
| Roland Ch 13 (Rec L5) | 47 | 53 | **3.33** | **2×** | **~666–1000 mL/h** | **~100–166 mL/day** |
| Roland post Ch 19 (Rec L9) | higher | higher | recompute | **10×** | M × 10 × base | M × 10 × base |

**Daily Ned feed:** whole blood, not packed cells. Red-cell slice ≈ **40–45%** of the drip. Comfortable daily whole-blood feed ≈ **(effective RBC rate) / 0.45**. Ch 13 story lock **150 mL/day** whole blood sits inside the Ch 13 Rec L5 band (~100–166 mL RBC/day → ~220–370 mL whole-blood ceiling; he feeds under the ceiling). Raise the drip when M or Recovery climbs if he is still feeding “as much as he recovers.”

Ned hemolymph (mass-scaled caterpillar): `../People/Ned.md`.

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

**Cast law:** `Useful (J) = mana × 10 × η(L) × μ(INT)` with `η(1)=0.3`, `η(L)=1+(L-2)×2/7` (L2=1 … L9=3), `μ=(INT/15)^0.8`. See `../Science/ManaCast.md`.

Skill, trait and class bonuses can raise displayed MP above the bare attribute total. Chapter 23: low mana → dizzy/sleepy; **zero MP** → splitting headache and possible pass-out, plus a next-day mana-regen debuff.

## Elemental affinities

Hidden until after the **first class**. First seen: Chapter 5.

At Tier 1 the sheet shows the basic four: Fire, Wind, Earth, Water. Higher-tier elements (lightning, gravity and others) unlock later. Affinity % steers which elemental mage paths open. Roland’s first read is **0% / 0% / 0% / 0%** (unprecedented to House Arden). A glass measuring orb is also used; it glows faintly with no useful reading when affinities are zero.

Chapter 6 book: an **elemental affinity skill** needs at least **~1%** affinity. Zero on all four blocks elemental mage T2s and the weak Superior Mage upgrade. Rare (~one in a million). Typical new mage Intelligence sits near **20**.

## Class resource bonuses (examples)

### Mage (Tier 1)
First seen: Chapter 5–6 skill card
- **+2% max mana** per Mage class level
- **+1% mana regeneration** per Mage class level
`MP = ((Int×10)+(Will×4)) × (1 + 0.02 × Mage level)`. Regen rating **+1% × Mage level**. Source fixed **+20% / +15%** discarded. **Blessed by Mana** is narrative regen feel only (no flat MP). Kept as secondary. See `Skills.md`.

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
