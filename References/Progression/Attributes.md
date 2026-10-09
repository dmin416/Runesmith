# Attributes

Live attribute list and resource formulas. Fat blurbs / perk notes: `AttributesDesign.md`. XP / tiers: `Progression.md`. Scale tables: `Training.md`.

## Core attributes

Strength, Agility, Dexterity, Vitality, Endurance, Intelligence, Willpower, Charisma, Luck.

Untrained adult street baseline is **15 across the board**: not an athlete. Physical combat anchors at STR/AGI 15: street tip KE and weapon rows in `../Combat/AttackScale.md` (rapier ~30–60 J, sword cut ~60–130 J, warhammer ~200–400 J). Cha/Luck 15 is ordinary social luck, not perks (perks gate at 40). No class packages assumed.

| Stat | Real feel at 15 |
|---|---|
| STR | ~90 kg max deadlift |
| VIT | ~45-year constitution potential (abstract) |
| END | ~3 L/min VO2 max |
| AGI | ~375 W burst; sprint ~6 m/s (~13 mph) |
| DEX | ~15 pegboard pegs (right hand) |
| INT | ~7.5 digit working-memory span; cast μ = 1 |
| WILL | ~30 years effective life experience |
| Vit/End heal | M = 1.0 (normal adult blood recovery) |

## Resources (locked)

```
HP = (Vitality × 10) + (Endurance × 3)
SP = (Endurance × 10) + (Strength × 3) + (Agility × 3)
MP = (Intelligence × 10) + (Willpower × 4)
```

Bare all-15 (no class bonuses): **HP 195**, **SP 240**, **MP 210**. A street adult with no Mage/Acolyte still has no usable mana pool to absorb into; the MP number is the sheet formula once a pool exists.

Skill bonuses can raise displayed pools above the bare formulas (e.g. Mana Reinforcement). **Mage** and **Blessed by Mana** do **not** raise max MP.

**Class levels vs class cards:** leveling a class permanently raises its package attributes. Those stats stay after you leave the class. The class **card** is a separate narrative benefit.

**Mage (T1) class card:** mana recovery (narrative). Kept while Mage is primary or secondary. Lost when Mage is dropped from the secondary slot (switch secondary **once per day**).

**Blacksmith / Runic Blacksmith (T1) class card:** increased fire resistance and increased stamina recovery (narrative). Same keep / drop rules as Mage.

**Blessed by Mana:** multiplies mana recovery (narrative). Permanent perk once unlocked. No flat MP.

Chapter 23: low mana → dizzy/sleepy; **zero MP** → splitting headache and possible pass-out, plus a next-day mana-regen debuff.

## Blood restore (human / Roland)

Earth baseline for a **5 L** adult, then speed by Vit/End, then by **Recovery** skill.

```
M = ((Vitality + Endurance) / 2) / 15
Recovery_time = 1 − 0.1 × Recovery_level    (L0 = 1.0; L5 = 0.5; L9 = 0.1)
Recovery_rate = 1 / Recovery_time            (L5 = 2×; L9 = 10×)
```

Adult Vit/End **15/15** → **M = 1.0**. Base rates × M. Then × **Recovery_rate**. Effective rate = base × M × Recovery_rate. When Vit or End rises, recompute M. When Recovery levels, recompute Recovery_rate. Both stack.

**Breath hold** uses the same **M**. Comfortable seated hold = **T0 × M**, with **T0 = 1 minute** at Vit/End 15. **Breath Control** multiplies that by skill level (`SkillsDesign.md`): `hold = T0 × M × BreathControl_level`. Body alone at Vit/End ~45–50 is about **3×** average. Breath Control **L5** makes that about **5×** the body-only band (~**15–17×** average).

- **Plasma (~2.75 L):** base **100–150 mL/h** at M = 1
- **Red cells (~2.25 L of that 5 L):** base **15–25 mL/day** at M = 1
- **Recovery** covers blood loss, cuts, wounds and soft-tissue damage. It does **not** regrow missing limbs.

| Snapshot | Vit | End | M | Rec | Plasma effective | RBC effective |
|---|---|---|---|---|---|---|
| Adult baseline | 15 | 15 | **1.00** | L0 **1×** | 100–150 mL/h | 15–25 mL/day |
| Roland Ch 13 (Rec L5) | 47 | 53 | **3.33** | **2×** | **~666–1000 mL/h** | **~100–166 mL/day** |
| Roland Ch 19 exit (Rec L5) | ~47 | ~53 | **~3.3** | **2×** | ~same as Ch 13 band | ~same as Ch 13 band |

**Daily Ned feed:** whole blood, not packed cells. Red-cell slice ≈ **40–45%** of the drip. Comfortable daily whole-blood feed ≈ **(effective RBC rate) / 0.45**. Ch 13 Rec L5 band is ~100–166 mL RBC/day, so the whole-blood ceiling is about **220–370 mL**. Story lock **150 mL/day** sits under that ceiling. Ned: `../People/Ned.md`.

## Elemental affinities

Hidden until after the **first class**. At Tier 1 the sheet shows Fire, Wind, Earth, Water. Higher-tier elements unlock later. Affinity % steers elemental mage paths. Roland's first read is **0% / 0% / 0% / 0%**. An elemental affinity skill needs at least **~1%**. Zero on all four blocks elemental mage T2s (rare, ~one in a million).

## Attribute perks

One named perk per core attribute at **40** (Cha / Luck out unless a later trait says otherwise). Blessed by Mana needs Mage.

| Stat | Perk name | Theme |
|---|---|---|
| Strength | Titan's Back | Carry capacity |
| Dexterity | Exacting Motion | Accuracy of body movement |
| Intelligence | Blessed by Mana | Multiplies mana recovery (narrative; no flat MP) |
| Willpower | Unbroken Focus | Focus |
| Agility | Sure Footing | Balance |
| Vitality | Defiance of Years | Reduced aging |
| Endurance | Rapid Renewal | Recovery speed |

Full perk blurbs: `SkillsDesign.md` / `AttributesDesign.md`.
