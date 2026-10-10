# Biomaterials

How to turn animal and monster parts into usable craft numbers. Magic metal ladders: `../../Materials/Metals.md`. Heat damage: `../Metallurgy/OverheatedMetals.md`. Fans: `../Energy/FanAirflow.md`. Rubber / insect stocks: `RubberAndInsect.md`. Silk numbers: `BiologicalSilks.md`. Glue catalog: `BiologicalAdhesives.md`. Primary living harvest stream: `../../../People/Ned.md`. Worm biomechanics: `../../Fauna/Species/NeedleWorm.md`. Nav: `Index.md`.

**Owns:** process pipeline, N× vs living-stat scale, Ned harvest stream. Do not grow silk or glue encyclopedias here.

## Narrative

Earth analogues give the baseline. Monster grade and living companions raise those numbers. Process the part first. Do not start from a random foe sheet. D's regular stockpile is Ned: needles, hemolymph, parsleaves, later silk and gel nodules.

## Detail

### Process any animal material

Work the part in this order. Same pipeline for shed chitin, horn, silk or a living scarf worm.

1. **Name the part and job.** Spike tip, body fluid, skin wall, fiber, toxin, seasoning. Job decides which properties matter.
2. **Lock an Earth analogue.** Dentin, enamel, soft insect cuticle, hemolymph, spider / moth silk, plant toxin leaf. Write composition notes (water %, hollow pulp, laminate edge).
3. **Pick the scale law** (below). Composition-fixed N× and living-stat power laws are different. Do not mix them blindly.
4. **Hold or change density.** Same chemistry → ρ stays. New mineral fill or drying → ρ can move.
5. **Derive compare numbers.** Specific strength, specific stiffness, fracture energy, pierce thickness, edge chip risk.
6. **Write failure mode and care.** Crack vs bend, dry-out brittle, toxin contact, melanization of blood, regrow vs one-shot stock.
7. **Map craft use.** Weapon tip, seasoning, ink, hide blank, pencil core, binding line. Volume limited by harvest rate.

### Properties

| Property | Symbol | Ask this |
|---|---|---|
| Tensile / core strength | σ, MPa | Does the shaft snap under lever or impact? |
| Stiffness | E, GPa | Does a long piece whip? |
| Fracture toughness | K, MPa√m | Does a crack run? |
| Hardness | H, GPa | Does the tip chip or dull? |
| Density | ρ, g/cm³ | How heavy is this volume? |
| Toughness energy | G ≈ K²/E | How much energy before the crack grows? |

**Metals vs biological composites:** Tabor (hardness ≈ 3 × yield) is for metals. Bone, dentin, cuticle and enamel do not obey it. Living soft cuticle also depends on water content. Dry stock is more brittle than wet.

**Derived:**

```
σ_spec = σ / ρ
E_spec = E / ρ
G ≈ K² / E
```

### Two scale laws

**A. Composition-fixed N×** (dead part or “same tissue, stronger grade”)

Use when the story says every property is N times normal and chemistry is unchanged.

```
σ_N = N × σ_0
E_N = N × E_0
K_N = N × K_0
H_N = N × H_0    // sheet assumption
ρ_N = ρ_0
→ σ_spec and G also scale about ×N
```

Use when grade rises but chemistry stays the same. Density held. Apply to any biomaterial sheet.

**B. Living companion / attribute power laws** (Ned path)

Use when tissue grows with the creature's stats and regenerates. Biological materials often **level off**, so tip hardness and spike core need a sub-linear exponent, not raw N× on every row.

From Ned combat material locks:

```
spring_energy ∝ Strength          // muscle force × stroke
tip_hardness ∝ Strength^0.6
spike_core_σ ∝ Strength^0.6
skin_stab_resist ∝ Vitality²      // strength and stretch both rise
wound_close_time ∝ 1 / Vitality
```

Plate pierce (plug shear, tip must also out-hard the plate):

```
t_max ≈ (σ_core × diameter) / (4 × τ_plate)
need H_tip ≳ 1.5 × H_plate or the tip chips
```

Doubling spike diameter doubles thickness limit. Impact energy is often not the limit for a short spike; tip hardness and core shear are.

### Ned harvest stream (primary)

D uses these on a regular basis. Quality tracks Ned's power, diet (stones, meat, D's blood) and how charged the part was at harvest. Personal pipeline. Do not dump city prices.

| Part | Earth analogue / nature | Scale with | Craft / use |
|---|---|---|---|
| **Needles / spikes** | Hardened cuticle core (~200–300 MPa at tame band); Zn/Mn-reinforced tips (~1–3 GPa H early); continuous grow like incisors | Strength^0.6 on tip H and core σ; length with age / form | Combat tips, seasoning from toxin needles; later **toxin-free write spikes** as pencil cores / punches |
| **Hemolymph (“blood”)** | Open insect bath, ~85–90% water; amino acids, trehalose, lipids; melanizes in air unless stabilized | Magic biology completes human-scale nutrition; refill hours after seal (Vit/End band on Ned sheet) | BBQ / seasoning; small Seal drills; not ordinary butcher blood science |
| **Parsleaves** | Mild poison leaf Ned stashes; parsley-like smell; weaker than spikes | Stockpile dry; plant-toxin care | Seasoning / mild poison reagent |
| **Soft cuticle / skin** | Chitin-protein hydrogel (~40–75% water band); fibers ~35–70 MPa; resilin rebound ~95% | Vitality² stab resist; living repair | Not primary leather until nodules; living armor feel on Ned himself |
| **Gel nodules** (planned regular) | Detachable jelly tubercles; outer soft cuticle wall + inner gel; sacrificial drop | Nodule size / mana density with evolution and diet | Wall → magical hide / parchment blanks; gel → magical ink reagent |
| **Silk** (skill path) | Insect / spider silk anchors (`BiologicalSilks.md`) | Silk Production skill; Int dump slows evolve | Bind, travel lines, snares, later load-bearing weave |

**Harvest care**

- Voluntary drops and small cuts first so Ned does not learn fear.
- Toxin needles stay combat / food. Clean write spikes are a separate later needle variant.
- Hemolymph: stop melanization for food or ink-adjacent use; sequestered plant toxins and phenoloxidase are the main spoilers.
- Nodule skins and gel stockpile like needles and blood. Regrow rate caps volume.
- Diet lock: Ned breaks food into pure magic and rebuilds tissue. Do not run human pathogen rules on blood swaps.

**Needle vs plate (quick read)**

At tame-band Strength ~20, ~1 cm spike, mild steel sheet ~2 mm is near the chip-and-punch edge. Harder armor needs much more Strength before tip H and core σ clear the 1.5× hardness and shear rules. Full tables: `../../Fauna/Species/NeedleWorm.md`.

### Short template (copy for a new part)

```
Part:
Earth analogue:
Composition notes (ρ, water, hollow, laminate):
Scale law (N× or stat^exponent):
Key numbers (σ, E, K, H, ρ):
Derived (σ_spec, G, t_max, …):
Failure mode / care:
Craft use / harvest rate:
```

## Open

- Dead-loot N× sheets (horn, chitin, bone) when a scene needs one
- Earth metal production tables are **not** this file (`../Metallurgy/EarthAlloys.md`)
