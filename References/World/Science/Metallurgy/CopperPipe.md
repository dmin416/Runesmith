# Copper Pipe

How to make, harden, join and fail copper tube. Brass fittings: `Brass.md`. Overheat: `OverheatedMetals.md`. Vacuum cast help: Old `SteelVacuumChamber.md` / `Vacuum.md` until pulled.

## Narrative

Copper is the long-life water line metal: joins clean, bends when soft, resists ordinary bacterial growth and does not burn. Cost, freeze burst and bad water chemistry are the real enemies.

## Detail

### Why use it / why not

**Pros:** decades in normal water (50–70+ years Earth band); easy solder / braze; soft coil bends cut joint count; recyclable; non-combustible.

**Cons:** expensive; freeze-burst; acidic or very soft water → pinhole leaks, blue-green stain, metallic taste; galvanic attack on steel / iron it touches.

### Pipe grades (wall and job)

| Type | Wall | Job |
|---|---|---|
| K | Thickest | Buried supply |
| L | Medium | Standard indoor pressure |
| M | Thin | Light household pressure |
| DWV | Thinnest | Drain / vent only. No pressure |

Hard = straight lengths. Soft = coil, hand-bendable.

### Make the tube

```
T_melt_Cu = 1085 °C
```

**Vacuum cast slug / tube:** no dissolved air → no bubble leaks. Oxygen-free copper stays ductile when later brazed (ordinary tough-pitch copper can go brittle in flame). Soft as-cast → use a slightly thicker wall than hard-drawn, or cold-work after.

**Older paths:** hammer sheet around a mandrel and seam; cast thick then hammer / roll / draw down; modern pierce-and-draw from a billet.

### Strength = metal must move

Hardening needs permanent shape change (thinner, longer, wider, bent). Equal pressure from all sides with nowhere to flow → elastic squeeze only → **no work hardening**.

**Optional grain refine before final cold work:**

- Hot work ~700–900 °C, reduce ~⅓–½, or
- Cold reduce ~30–50% then anneal ~400–650 °C (no glow below ~525 °C; dull red at top in dim light)

**Cold reduction → temper (yield / permanent-bend resistance):**

| Thinned by | Temper feel | Approx. strength vs soft | Bend / flare |
|---|---|---|---|
| 0% | Soft cast | 1× | Easy |
| ~10% | Slightly firm | ~3× | Still easy |
| ~20–25% | Half hard | ~4× | Careful |
| ~35–40% | Hard | ~4.5× | Stiff; may crack |
| ~50%+ | Extra hard | Little more gain | Cracks on sharp bend / flare |

Most of the gain is in the first **10–20%**. Water pipe target: about **15–25%** reduction (hard-drawn band). Past ~40% is too stiff for field bends and flares.

**Annealing reset:** heat ~400–650 °C, cool. Soft again. Only cold work **after** the last anneal counts toward final temper.

**Rotary swage / mandrel hammer:** wall thins a little, length grows. That counts as cold work. Light surface peen hardens skin only.

### Join

| Method | Note |
|---|---|
| Soft solder | Low heat. Lead-free on drinking water |
| Braze | Hotter, stronger. Softens hard temper near the joint |
| Flare | Cone the end, clamp |
| Compression | Ferrule bites the tube |

Clean off leftover flux. Flux left on the line eats pinholes.

### Fittings and mixed metals

- **Bronze** valves / cast fittings: pour well, corrosion resistant
- **Brass** machine threads: cheaper; aggressive water can dezincify (`Brass.md`)
- Copper + bronze + brass + stainless: generally OK together
- Copper + steel / iron: steel rusts fast → dielectric union or non-metal spacer

### Water that kills copper

- pH under ~6.5
- Very soft water
- High velocity (especially hot) eroding the ID
- Freeze

## Open

- Exact magitech draw-bench / vacuum pour beats when a workshop scene needs them
- Pair with road / building water systems when city infrastructure notes land
