# Attributes

Live attribute list and resource formulas. Fat blurbs / perk notes: `AttributesDesign.md`. XP / tiers: `Progression.md`. Scale tables: `Training.md`.

## Core attributes

Strength, Agility, Dexterity, Vitality, Endurance, Intelligence, Willpower, Charisma, Luck.

Untrained adult street baseline for physical scale work: **STR 15 / AGI 15** (`../Combat/AttackScale.md`).

## Resources (locked)

```
HP = (Vitality × 10) + (Endurance × 3)
SP = (Endurance × 10) + (Strength × 3) + (Agility × 3)
MP = (Intelligence × 10) + (Willpower × 4)
```

Class and skill bonuses can raise displayed pools above the bare formulas.

**Mage (T1) class card:** **+2% max MP** and **+1% mana regen** per Mage class level.
`MP = ((Int×10)+(Will×4)) × (1 + 0.02 × Mage level)`.

Chapter 23: low mana → dizzy/sleepy; **zero MP** → splitting headache and possible pass-out, plus a next-day mana-regen debuff.

## Blood restore (human / Roland)

Earth baseline for a **5 L** adult, then speed by Vit/End, then by **Recovery** skill.

```
M = ((Vitality + Endurance) / 2) / 15
Recovery_time = 1 − 0.1 × Recovery_level    (L0 = 1.0; L5 = 0.5; L9 = 0.1)
Recovery_rate = 1 / Recovery_time            (L5 = 2×; L9 = 10×)
```

Adult Vit/End **15/15** → **M = 1.0**. Base rates × M. Then × **Recovery_rate**.

- **Plasma (~2.75 L):** base **100–150 mL/h** at M = 1
- **Red cells (~2.25 L of that 5 L):** base **15–25 mL/day** at M = 1
- **Recovery** covers blood loss, cuts, wounds and soft-tissue damage. It does **not** regrow missing limbs.

| Snapshot | Vit | End | M | Rec | Plasma effective | RBC effective |
|---|---|---|---|---|---|---|
| Adult baseline | 15 | 15 | **1.00** | L0 **1×** | 100–150 mL/h | 15–25 mL/day |
| Roland Ch 13 (Rec L5) | 47 | 53 | **3.33** | **2×** | **~666–1000 mL/h** | **~100–166 mL/day** |

**Daily Ned feed:** whole blood. Comfortable daily whole-blood feed ≈ **(effective RBC rate) / 0.45**. Ch 13 story lock **150 mL/day** sits under the Rec L5 ceiling. Ned: `../People/Ned.md`.

## Elemental affinities

Hidden until after the **first class**. At Tier 1 the sheet shows Fire, Wind, Earth, Water. Higher-tier elements unlock later. Affinity % steers elemental mage paths. Roland's first read is **0% / 0% / 0% / 0%**. An elemental affinity skill needs at least **~1%**. Zero on all four blocks elemental mage T2s (rare, ~one in a million).

## Attribute perks

One named perk per core attribute at **40** (Cha / Luck out unless a later trait says otherwise). Blessed by Mana needs Mage.

| Stat | Perk name | Theme |
|---|---|---|
| Strength | Titan's Back | Carry capacity |
| Dexterity | Exacting Motion | Accuracy of body movement |
| Intelligence | Blessed by Mana | Mana regeneration (narrative; no flat MP) |
| Willpower | Unbroken Focus | Focus |
| Agility | Sure Footing | Balance |
| Vitality | Defiance of Years | Reduced aging |
| Endurance | Rapid Renewal | Recovery speed |

Full perk blurbs: `SkillsDesign.md` / `AttributesDesign.md`.
