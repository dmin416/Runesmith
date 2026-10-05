# Blacksmith Products

What a skilled smith makes, how hard it is and rough time/fuel/force. Metallurgy: `CraftMetal.md`. Machine path: `../Invent/MedievalIndustrialization.md`. Cookware production is Food-domain (`../../../Food/KitchenCraft.md`), not a metal-law source here. Heads: `Arrowheads.md`. Structural: `StructuralForge.md`.

## Narrative

Village smiths do nails to plowshares. Cities split locksmiths, cutlers, armorers and farriers. Iron bar supply limits more than skill. Steel edges cost a premium. The fire burns far more energy than the hammer puts into the metal.

## Detail

### Difficulty scale

| Band | Meaning |
|---|---|
| Easy | Repeatable, little ruin risk |
| Moderate | Needs practiced judgment |
| Hard | Frequent fails even for skilled hands |
| Very hard | Specialist; one error wastes days |

### Product ladder

| Item | Diff | Main challenge |
|---|---|---|
| Nails and hooks | Easy | Speed / consistency (hundreds/day) |
| Hinges / door hardware | Easy–mod | Fit; decorative scrolls |
| Horseshoes | Moderate | Fit to the horse (farrier skill) |
| Ag tools (share, sickle, axe) | Moderate | Clean steel-on-iron weld; scythes hardest |
| Chains / rings | Moderate | Worst-link weld |
| Knives | Mod–hard | Heat treat unknown carbon |
| Locks and keys | Hard | Fine cold filing / springs |
| Trade tools (chisel, saw…) | Hard | Temper matched to use; saws worst |
| Armor pieces | Very hard | Raise without warp; articulations |
| Swords | Very hard | Distal taper + high-stakes quench |

**Fails:** split nail heads; cold-shut scrolls; bad shoe fit; lifted steel edges; fake-sound cold welds; quench cracks; sticky locks; chipped/uneven temper; armor thin spots; sword warp/delam.

### Smith's own tools

| Tool | Diff | Note |
|---|---|---|
| Tongs | Moderate | Jaw shape + rivet tension |
| Punches / drifts / chisels | Easy–mod | Hot vs cold temper |
| Hammers | Moderate | Punched eye; hard face, tough eye |
| Anvil (≥50 kg) | Very hard | Iron body + steel face weld; team fire |
| Bellows | Specialist | Wood + leather (often bought) |
| Files / rasps | Hard | Hand-cut teeth; machine-tool bottleneck later |

### Constraints

- Buy bar iron; few smiths smelt  
- Carbon read by spark, fracture, fire feel  
- Charcoal for fine work; coal sulfur can harm  
- Town size → specialization  

### Energy model (order of magnitude)

```
E_blow_hand ≈ 25 J     // 1.2 kg @ ~6 m/s
E_blow_sledge ≈ 100–120 J
E_heat ≈ 0.7 MJ/kg to ~1150 °C
η_forge ≈ 5–8%         // charcoal ~29 MJ/kg
Fire burn ≈ 2–3 kg charcoal/h (more for anvil work)
η_deform ≈ 10–25% of swing energy into real plastic work
```

**Takeaway:** fuel energy is about **1,500–4,000×** hammer mechanical energy. Food for the smith (~2 MJ/h) is tiny next to charcoal.

| Item | Mass | Skilled time | Blows | Swing E | Charcoal |
|---|---|---|---|---|---|
| Nail | 15 g | ~40 s | ~15 | 0.4 kJ | 0.02 kg |
| Strap hinge | 0.6 kg | 1–2 h | 600–1k | 20–35 kJ | 2–4 kg |
| Horseshoe | 0.4 kg | 20–40 min | 150–250 | 5–9 kJ | 0.7–1.2 kg |
| Axe / share | ~2 kg | 3–5 h | 2.5–4k | 100–200 kJ | 8–12 kg |
| Chain 1 m | 1.2 kg | 1–1.5 h | 600–900 | 20–35 kJ | 2–3 kg |
| Knife | 0.25 kg | 3–4 h | 600–1k | 18–30 kJ | 2–3 kg |
| Warded lock | 0.5 kg | 12–30 h | 1–1.5k | 25–40 kJ | 4–6 kg |
| Chisel | 0.25 kg | 2–3 h | 500–800 | 15–28 kJ | 2–3 kg |
| Helmet | 2 kg | 15–40 h | 15–40k | 225–600 kJ | 12–20 kg |
| Sword | 1.2 kg | 15–35 h | 10–20k | 400–800 kJ | 30–60 kg |
| Tongs | 0.8 kg | 1.5–3 h | 1.2–2k | 40–70 kJ | 3–5 kg |
| Hammer | 1.2 kg | 1.5–3 h | 1.5–2.5k | 50–90 kJ | 4–7 kg |
| Anvil 50 kg | 50 kg | 60–150 person-h | 5–10k sledge | 0.5–1.2 MJ | 150–400 kg |

Pattern-weld sword ≈ **2–3×** forge time/fuel. Full plate harness ≈ **500–1,000 h**, **300–500 kg** charcoal. Charcoal ≈ **15–25%** of wood weight → sword charcoal = **150–400 kg** wood. Striker roughly doubles person-hours on heavy jobs.

### Peak force bands

| Action | Force |
|---|---|
| Hand hammer on hot iron | 5–15 kN |
| Sledge on hot iron | 25–50 kN |
| Punch 10 mm through 8 mm hot | ~15 kN shear |
| Drift hammer eye in 25 mm bar | 50–100 kN staged |
| Planish cold sheet | 1–3 kN |

## Open

- Price pegs when Economy shop tables deepen  
- Water-powered trip hammer multipliers  
