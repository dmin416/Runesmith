# Scroll Imbue (Idea)

> **Unread idea / design loot.** Not reviewed. **Not a lock.** Live **rune-quality** efficiency is **only** `Energy.md` η_cond: Lowest **0.20** / Low **0.40** / Intermediate **0.60** / High **0.80** / Highest **1.00**. Scroll quality is a different strength grade (`ScrollAspects.md`). Ink numbers below use **η_ink**, never the name η_cond.

Parked model for how substrate density, narrative resistance, ink grade and engraving channels could set **imbuing** and **charging** costs for scripts. Kept here so it is findable next to Magic / ink notes.

---

## Why (three adjustments)

The model holds together with three adjustments.

1. **Density and conductivity can conflict.** Silver is ten times denser than parchment yet conducts mana far better. The rules need a formula that weighs both rather than ranking materials on one trait.
2. **Charging cost should account for conduction losses.** Canon useful output = mana × 10 × η_cond × A with **η_cond = rune quality only**. This idea’s separate ink loss dial is **η_ink** (not rune quality, not scroll quality).
3. **Thin materials need a depth cap.** If imbuing saturates the whole thickness, a stone tablet becomes absurd. Imbuing should saturate a fixed bond depth under the line, so volumetric density matters and total thickness only matters when the material is thinner than that depth.

**Conflict note vs live lock:** Live `Energy.md` ties **η_cond** only to **rune quality** **0.20 / 0.40 / 0.60 / 0.80 / 1.00**. This file must never reuse that symbol or those steps for ink.

---

## Proposed rules

**Rule 1: Density.** Imbuing must saturate the matter beneath the script to a fixed bond depth. Denser material packs more matter into that depth, so it costs more. Density uses real values, relative to plant paper (about 0.8 g/cm³). Material thinner than the bond depth (leaf, foil) scales its density down proportionally.

**Rule 2: Substrate resistance.** Each material has a mana resistance value. These values are narrative choices rather than physics. Blood-bearing and silver materials resist little. Stone resists heavily. Orihalcum blocks mana entirely and aurium damps flowing mana, so neither can hold a script.

**Rule 3: Ink quality.** The ink is the actual conduction path. Better ink lowers imbuing cost, raises conduction efficiency (lowering charging cost) and raises capacity. Each ink grade has a maximum spell tier it can carry. Overloading it burns the line through local energy spikes, consistent with canon on mana damage from forced movement.

**Rule 4: Channels.** Ink painted on a surface soaks into the substrate, so the substrate's density and resistance apply in full. Engraving a groove and filling it keeps most of the ink in the channel and gives a thicker conductor cross-section. Lining the groove with mana insulation stops bleed into the substrate almost entirely, which makes heavy materials viable. An empty channel carries nothing; it must hold ink or an inlaid wire. Channels require a rigid substrate, so paper, silk and vellum can only take surface ink.

**Rule 5: Durability.** Surface ink on soft materials burns out on use. Engraved or inlaid scripts survive casting, so the scroll only needs its reservoir recharged.

**Rule 6: Size.** Canon sets A4 as the tier 1 inscription standard with compression fractions down to 1/512. Compressing a script onto a smaller surface should multiply imbuing cost, giving pocket scrolls and inscribed rings a real premium.

---

## Formula

```
Imbue = Spell × [1 + (D × R × I × C)]
Charge = Spell ÷ η_ink
```

| Variable | Meaning |
|---|---|
| D | Density relative to plant paper |
| R | Substrate resistance (paper = 1) |
| I | Ink factor |
| C | Channel factor |
| η_ink | Ink conduction (idea dial only; **not** quality η_cond) |

The leading 1 guarantees imbuing never costs less than the spell itself.

### Ink grades (η_ink only; not the quality ladder)

| Ink | I | η_ink |
|---|---|---|
| Soot ink | 1.5 | 0.60 |
| Standard (mana stone dust) | 1.0 | 0.80 |
| Monster blood ink | 0.6 | 0.88 |
| Blood-silver ink | 0.35 | 0.94 |
| Mithril ink | 0.15 | 0.98 |

### Channel types

| Method | C |
|---|---|
| Surface ink | 1.0 |
| Engraved, ink-filled | 0.4 |
| Engraved, insulated lining | 0.1 |

### Substrates (surface ink, standard ink)

| Material | Real density | D | R | Factor |
|---|---|---|---|---|
| Plant paper | 0.8 | 1.0 | 1.0 | 2.0 |
| Vellum | 1.0 | 1.25 | 0.7 | 1.9 |
| Needle worm silk | 1.3 | 1.6 | 0.4 | 1.6 |
| Dry oak | 0.75 | 0.95 | 1.5 | 2.4 |
| Bone | 1.9 | 2.4 | 1.2 | 3.9 |
| Steel | 7.8 | 9.75 | 0.8 | 8.8 |
| Granite | 2.7 | 3.4 | 3.0 | 11.2 |
| Silver plate | 10.5 | 13 | 0.05 | 1.65 |
| Mithril (standard grade) | | 13 | 0.02 | 1.26 |

Factor column = `1 + (D × R × I × C)` at **I = 1.0**, **C = 1.0** (standard ink, surface).

---

## Worked examples (100-mana spell)

| Scroll | Imbue | Charge | Total | Reusable |
|---|---|---|---|---|
| Paper, soot ink, surface | 250 | 167 | 417 | No |
| Paper, standard ink, surface | 200 | 125 | 325 | No |
| Silk, blood-silver ink, surface | 122 | 106 | 228 | No |
| Granite, standard ink, surface | 1,120 | 125 | 1,245 | Yes |
| Granite, blood-silver, engraved | 243 | 106 | 349 | Yes |
| Granite, blood-silver, insulated | 136 | 106 | 242 | Yes |
| Oak, blood-silver, insulated | 105 | 106 | 211 | Yes |

These results produce a clean economy. Cheap paper scrolls cost the most mana per use. Good ink is the single biggest lever for a scribe, since it cuts both costs at once. Engraving turns heavy, cheap materials into efficient permanent scrolls at the price of labor and tools, which gives craftsmen with engraving skills a natural partnership with scribes.

---

## Cross-links

- Live output law (do not replace yet): `Energy.md`
- Magic hub: `Magic.md`
- Earth ink catalog: `../World/Science/Invent/Ink.md`
- Path hosts / blood ink: `ManaMaterials.md`
- Shop scroll prices: `ScrollEconomy.md`
- Setup pour (separate design): `RuneSetup.md`
