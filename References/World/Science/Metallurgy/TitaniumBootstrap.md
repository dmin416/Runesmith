# Titanium Bootstrap (Beach to Metal)

Hub: `Titanium.md`, `TitaniumProcessing.md`. Hawaiian resource limits: `../../Geography/VolcanicIsland/Sands.md`, `../../Geography/VolcanicIsland/HawaiianMinerals.md`. Nickel/nitinol: `Nickel.md`, `Nitinol.md`.

Earth design loot: full chemical bootstrap. Mundane Ti on Terra is SPECIALTY/invent.

This document is a procedural encyclopedia for bootstrapping **commercial-purity titanium (99.5%+, Grade 1/2)** from beach heavy mineral sand through the **Hunter process** (TiCl₄ reduced with sodium). Optional **Van Arkel-de Boer iodide crystal bar** refining can push toward ultra-high purity. Every step assumes **no magic**, only materials and energy you can gather on or near a volcanic island coast.

---

## Overview and Route Choice

### Goal

| Target | Specification | Typical use |
|---|---|---|
| CP sponge / button | ≥99.5% Ti, O+N+C+H controlled | Grade 1/2 structural, lab proof |
| Ultra pure (optional) | ≥99.99% via iodide bar | Filament, getter, research |

Titanium metal is useless if contaminated: **oxygen**, **nitrogen**, **carbon**, and **water** must stay out from the moment TiCl₄ exists until the ingot is solid.

### Core chemistry chain

```
Beach HM sand → TiO₂ concentrate → TiCl₄ (distilled) → reduce (Na or Mg) → sponge/powder → leach → consolidate (vacuum/Ar arc)
```

| Step | Reaction (simplified) | Notes |
|---|---|---|
| Concentrate | Physical upgrade to ~90%+ TiO₂ | Magnetic split, hand pick rutile |
| Chlorination | TiO₂ + 2C + 2Cl₂ → TiCl₄ + 2CO (also CO₂) | 800-900°C, dry Cl₂ |
| Distillation | TiCl₄ b.p. 136.4°C | Separate from SiCl₄, FeCl₃, AlCl₃ |
| Hunter | TiCl₄ + 4Na → Ti + 4NaCl | 800-1000°C, sealed bomb |
| Kroll (alt) | TiCl₄ + 2Mg → Ti + 2MgCl₂ | 800-900°C, Mg vapor |
| Consolidation | Arc melt or sinter | Under argon or vacuum |

### Route comparison

| Route | ID | Reductant | Pros | Cons | Bootstrap fit |
|---|---|---|---|---|---|
| **Hunter** | A | Sodium metal | Single batch bomb, well documented, Na from soda + carbon | Na pyrophoric, bomb hazard, need dry inert gas | **Recommended** once Na and Cl₂ exist |
| **Kroll** | B | Magnesium | Industry standard, Mg from seawater/bittern | Mg distillation retort, longer cycle, Mg fire risk | Good if **bittern** and **dolomite/Pidgeon** path is built |
| **Iodide refine** | C | I₂ cycle on hot filament | Highest purity crystal bar | Needs W or Ti filament, iodine, vacuum | **After** first metal exists; optional |

**Recommended sequence:** A (Hunter) for first metal, then C on a slice of sponge if ultra purity is required.

### Minimum ingredient list (bootstrap)

| Category | Material | Role in Ti chain |
|---|---|---|
| Beach | Black sand (titanomagnetite, ilmenite, rutile) | Ti feed |
| Forest | Wood | Charcoal, tools, heat |
| Ground | Clay | Refractories, chlorinator tube, crucibles |
| Sea | Seawater | Salt, bittern, Mg recovery, evaporation |
| Shore | Shells, coral | Lime (CaO) for soda, slaking, scrubbers |
| Beach | Magnetite (iron sand) | Bloomery iron (bombs, retorts) |
| Mineral | Sulfur (native or pyrite) | H₂SO₄, vitriol |
| Mineral | Saltpeter beds (KNO₃) | Oxidizer, niter for acids side chain |
| Mineral | Pyrolusite (MnO₂) | Cl₂ from HCl (Scheele) |
| Sea | Kelp | Potash, iodine (optional bar) |
| Beach/river | Quartz sand | Glass, labware |
| General | Fresh water | Leach, slaking, batteries |
| Farm | Sugar / starch | Ethanol for Na quench |
| Ore | Copper, zinc, cinnabar, lead | Wire, joints, Hg pump, chamber acid |
| Geology | Petroleum seep / coal | Protective oil for Na, tar |
| Air | Atmosphere | N₂/O₂ separation for Ar (chemical) |
| Optional | Wolframite | W filament for iodide bar |

---

## Dependency Map

ASCII flow from raw island inputs to solid Ti:

```
[Beach black sand] ──pan/sluice/magnet──► [HM concentrate: ilmenite/rutile]
        │                                      │
        │                                      ▼
[Wood]──►[Charcoal]──────────────────► [Pellet: TiO₂ + charcoal]
        │                                      │
        ▼                                      ▼
[Furnace+bellows]                    [Porcelain chlorinator 800-900°C]
        │                                      │
        │         [MnO₂] + [HCl] ◄── [Salt] + [H₂SO₄] ◄── [Sulfur/pyrite]
        │              │                      │
        │              ▼                      │
        │         [Cl₂ dry train]─────────────┘
        │              │
        ▼              ▼
[Lime]◄──[Shells]   [TiCl₄ crude] ──distill 135-137°C──► [TiCl₄ ampoules]
        │                                              │
        ▼                                              │
[Na₂CO₃]◄──[Kelp ash / Leblanc]                        │
        │                                              │
[Carbon]──► [Na retort Deville] ──► [Na in oil] ────────┤
        │                                              │
        ▼                                              ▼
[Iron bomb 1cm wall] ◄── [Steel from bloomery]   [Hunter: TiCl₄ + 4Na]
        │                                              │
        ▼                                              ▼
[Argon]◄── [Air → lye → Cu → Mg/Ti getter]      [Sponge + NaCl]
        │                                              │
[Vacuum]◄── [Hg Sprengel / Toepler]                     ▼
        │                                    [Leach HCl / AgNO₃ test / dry]
        ▼                                              │
[DC 20-40V 100-300A] ◄── [Dynamo / battery bank]         ▼
        │                                    [Arc melt Cu hearth under Ar]
        ▼                                              │
[Solid Ti button/ingot] ◄────────────────────────────────┘
        │
        └──optional──► [I₂ + W filament] ──► [Crystal bar Ti]
```

---

## Build Order

Phases are sequential. Overlap only where safety and tooling allow.

| Phase | Name | Deliverable | Depends on |
|---|---|---|---|
| 1 | Fire and tools | Embers, stone/wood tools, water handling | None |
| 2 | Charcoal | Calcined charcoal for chemistry | Phase 1 |
| 3 | Furnace | Tuyere furnace, bellows, 1100°C+ capability | 1-2 |
| 4 | Lime and salt | CaO, NaCl, bittern reserve | 1-3, seawater, shells |
| 5 | Iron | Bloom, forgeable bar, screws | 3-4, magnetite sand |
| 6 | Copper and lead | Cu wire, Pb sheet/pipe, basic smelting | 3-5 |
| 7 | Acids foundation | Sulfur, green vitriol, H₂SO₄ | 5-6, S, pyrite |
| 8 | HCl and soda | HCl gas, Na₂CO₃, NaOH | 4, 7 |
| 9 | Glass and labware | Retorts, Liebig, ampoules, joints | 4, 7-8, quartz sand |
| 10 | Chlorine | Dry Cl₂ train, scrubber | 8-9, MnO₂ |
| 11 | Ti concentrate | ≥85-95% TiO₂ feed pellets | 1, magnets, sand |
| 12 | TiCl₄ | Distilled liquid TiCl₄ in sealed glass | 9-11 |
| 13 | Sodium | Na metal in petroleum oil | 8, 5, protective oil |
| 14 | Hunter bomb | Sealed steel reactor, first reduction | 5, 12-13 |
| 15 | Inert gas and vacuum | Ar chemical loop, Sprengel pump | 8-9, Cu, Mg or Ti getter |
| 16 | Electricity | 20-40 V DC, 100-300 A sustained | 6, Zn, acid, or dynamo |
| 17 | Arc consolidation | Dense Ti button under Ar | 5-6, 14-16 |
| 18 | Optional iodide bar | Ultra-pure crystal Ti | 17, kelp I₂, optional W |

---

## Fire, Tools and Water

### Friction and percussion fire

| Method | Procedure | Materials |
|---|---|---|
| Hand drill | Hard spindle ( hardwood), hearth board, bow cord, ember nest of dry fiber | Dry grass, bark, char cloth boost |
| Fire plow | Groove in softwood, hard stick rubbed fast | Same tinder chain |
| Flint and steel | High-carbon steel striker on flint, catch in char cloth | Later iron phase |

**Tinder chain:** fine dry fiber → small twigs → finger wood → wrist wood. Never smother a new coal.

### Stone, wood, fiber tools

| Tool | Make | Use |
|---|---|---|
| Hammerstones | Dense basalt | Crush ore, knap edges |
| Grinding slab / handstone | Flat basalt | Pulverize sand, clay |
| Wooden trays | Carved logs | Panning, sluice |
| Baskets / fiber cloth | Local fiber | Dewatering concentrate |
| Bamboo or wood pipes | Hollow stems | Low-pressure gas ducting (not Cl₂ acid service) |

### Water

| Operation | Procedure |
|---|---|
| Settling | Slow pour through cloth; heavy HM sand settles first |
| Boiling | Kill biota; reduce dissolved CO₂ for some chem (not for TiCl₄ contact) |
| Distillation (later) | Glass retort + Liebig; needed for AgNO₃ tests and final Ti rinse |

---

## Charcoal

Charcoal is reductant in chlorination, sodium retort, and general heat. **Chemistry-grade** charcoal is calcined extra to remove volatiles.

### Earth mound (clamp)

1. Drive central chimney stake; lay kindling around base.
2. Stack wood radially around chimney, tight but with air gaps at base.
3. Cover with turf/mud leaving top vent and bottom air slots.
4. Light from top or base; smoke then glow.
5. Seal vents when flame dies; cool 24-48 h.
6. Yield **15-25%** by mass of dry wood.

### Pit method

1. Dig pit; fill with stacked wood.
2. Cover with green logs, soil; light through tunnel.
3. When smoke stops, seal tunnel; cool.

### Retort method (cleaner)

1. Clay or iron barrel packed with wood, closed except outlet pipe to fire pit or water seal.
2. Heat outer fire; tar and water exit pipe first, then gas burns.
3. When gas stops, cool sealed. Higher fixed-carbon fraction.

### Calcining for chemistry (800-1000°C)

1. Crush charcoal; load crucible or small shaft furnace.
2. Heat with bellows to dull red-orange (**800-1000°C**) 1-2 h until weight loss stabilizes.
3. Store dry. Use for TiO₂ pellets and Na₂CO₃ reduction.

---

## Clay, Ceramics, Refractories

### Finding and processing clay

1. Dig below topsoil; test roll into snake, bend 90° without cracking.
2. **Levigation:** slurry in water; decant fines; dry slip.
3. **Temper:** 10-30% grog (fired crushed pottery) or sand for shrink control.
4. **Wedge** to homogenize; form while plastic.

### Forming and firing

| Stage | Condition |
|---|---|
| Dry | Slow shade; avoid cracks |
| Bisque | 900-1000°C |
| High fire | 1200-1300°C for stoneware/porcelain chlorinator tube |

### Refractory recipes (volume parts, adjust with tests)

| Item | Composition | Max service | Notes |
|---|---|---|---|
| Firebrick body | Clay 60, grog 30, sand 10 | ~1400°C | Furnace lining |
| Crucible (iron melt) | Fireclay 70, grog 20, graphite 10 | ~1500°C | Short melts |
| Graphite crucible | Graphite + clay bond (if graphite sourced) | ~1600°C | Optional |
| Mortar | Same as firebrick, finer screen | Match brick | Wet joints |
| Lime crucible (slag) | Burned lime + sand | CaO melts high with iron | Not for TiCl₄ |

### Salt glaze and porcelain for chlorinator

- **Salt glaze:** throw salt into 1200°C kiln; NaCl vapor glazes silicate surface (acid-resistant-ish).
- **Porcelain body:** kaolin if found, else high-clay + silica + flux (feldspar or ash); vitrify at **1280-1300°C** for TiCl₄ chlorinator tube inner surface.

---

## Furnaces and Bellows

### Bellows types

| Type | Mechanism | Pressure |
|---|---|---|
| Bag | Leather bag, hand squeeze | Low, steady |
| Pot | Clay pot + leather disk | Medium |
| Box | Twin chamber, flap valves | Medium-high |
| Water | Water displacement bubble | Very steady, low leak |

### Tuyere and shaft furnace

1. Build cylinder of firebrick or clay-lined stone, **30-50 cm** bore minimum for iron.
2. Tuyere pipe (clay or iron) **15-30°** upward into base.
3. Charge port top; tap hole bottom front.
4. Connect bellows; preheat lining with wood before ore.

### Furnace types and temperatures

| Furnace | Typical T (°C) | Use |
|---|---|---|
| Open hearth / forge | 1000-1200 | Iron bloom, Na bomb preheat |
| Charcoal blast (small) | 1200-1400 | Iron, Deville retort |
| Pottery kiln | 900-1300 | Glass, porcelain tube |
| Chlorinator furnace | 800-900 | TiO₂ + Cl₂ |
| Lime kiln | 900-1100 | CaO from shells |
| Sodium retort | 1100-1200 | Deville |

---

## Lime

### Calcining shells or coral (900-1100°C)

1. Crush shells; layer in kiln with charcoal.
2. Heat with bellows until pieces glow white and crumble (**CaCO₃ → CaO + CO₂**).
3. Quicklime (CaO) is caustic; store dry.

### Slaking

1. Add CaO to water slowly (violent heat).
2. Stir to milk of lime **Ca(OH)₂**; settle; decant for causticizing.

### Chalk for sodium retort

If soft chalk or limestone exists, same calcining path. Lime is also **Cl₂ exhaust scrubber** (bleach slurry) and **Leblanc** causticizing agent.

---

## Salt and Bittern

### Solar evaporation stages (sequential crystallization)

| Stage | Solid | Chemistry | Keep? |
|---|---|---|---|
| 1 | Fe/CaCO₃/hydroxide scum | Surface skim | Waste |
| 2 | Gypsum | CaSO₄·2H₂O | Discard or wallboard |
| 3 | Halite | NaCl | **Primary salt** |
| 4 | Bittern | MgCl₂, KCl, MgSO₄, bromides | **Keep for Mg** |

### Boiling refinement

If solar is slow: boil seawater in iron pot; scrape scale; crystallize NaCl; remaining liquor is **bittern** concentrate.

### Storage

Keep bittern for **Dow-style Mg(OH)₂** path and later **Castner** or **Pidgeon** magnesium if choosing Kroll.

---

## Iron and Steel

### Beach magnetite bloomery

1. Charge: magnetite sand + charcoal in shaft furnace.
2. Reduce to spongy **bloom** (Fe + slag + unreduced ore).
3. Hammer on anvil; fold out slag; weld at yellow heat.
4. Carburize in charcoal crucible pack for **0.6-1.0% C** steel if needed.

### Heat treat

| Step | Purpose |
|---|---|
| Normalize | Reduce internal stress |
| Quench oil/water | Hard edge tools |
| Temper | Soften for toughness |

### Iron items for Ti chain

| Item | Spec | Why |
|---|---|---|
| Hunter bomb body | Wrought/steel **≥1 cm wall**, welded seam | Contains Na + TiCl₄ at 800-1000°C |
| Bomb lid | **Machined flat face + gasket groove** | Seal |
| **Tight screw lid** | Fine thread or bolt circle **≥8 bolts** | Open without torch cut |
| Sodium retort | Iron pipe + welded bottom, **≥5 mm** | Deville 1100°C |
| Flat condenser plate | Iron, water cooled optional | Na vapor condense |
| Tuyere pipes | Cast or forged iron | Furnaces |
| Dynam iron/steel | Shaft, pole pieces | Generator |
| Cu-coated not needed | Keep Cu separate | Avoid Cu contamination in Ti |

---

## Copper, Lead, Zinc, Mercury

| Metal | Smelt route | Ti chain use |
|---|---|---|
| **Copper** | Roasted sulfide ore + charcoal; matte → metal | Wire, dynamo windings, gas-tight joints |
| **Lead** | Carbon reduction of roasted cerussite/galena | H₂SO₄ chambers, pipes |
| **Zinc** | Distill from roasted calamine + charcoal | Daniell cells, galvanizing |
| **Mercury** | Roast cinnabar; condense vapor | **Sprengel vacuum pump** |

### Copper wire drawing

1. Cast rod; file point; pull through progressively smaller iron plate holes.
2. Anneal between passes. Need **km of wire** for serious dynamo.

---

## Sulfur

| Source | Procedure |
|---|---|
| Native sulfur | Melt at **~115°C**; filter; distill for purity |
| Pyrite roast | FeS₂ + O₂ → SO₂; collect for chamber acid or make **green vitriol** |
| Green vitriol | Weather pyrite heaps moist; blue-green **FeSO₄·7H₂O** crystals |

---

## Saltpeter

### Niter bed method (6 months to 2 years)

1. Mix manure, wood ash, porous soil in shed; keep moist, not flooded.
2. Leach with urine/ash water; evaporate leachate.
3. Crystallize **KNO₃** (less soluble than NaNO₃ at cold).

### Recrystallize

Dissolve crude niter in hot water; cool; harvest KNO₃; repeat for purity. Used for oxidizer and some glass decolorizing, not core Ti step.

---

## Sulfuric Acid

| Route | Procedure | Bootstrap rating |
|---|---|---|
| **Distill green vitriol** | Heat FeSO₄·7H₂O + HNO₃ or air roast to Fe₂O₃; capture SO₃/H₂SO₄ | Early, small scale |
| **Bell jar** | SO₂ + H₂O₂ or nitrosyl in glass bell | Lab scale |
| **Lead chamber** | SO₂ + HNO₃ + H₂O in Pb-lined chamber; tower absorb | **Bulk H₂SO₄** |

### Concentrating

Boil in glass or Pb until **~98%** (azeotrope ~98.3%). Store in glass or Pb.

### Drying agent

Conc. H₂SO₄ dries HCl and Cl₂ in train (**never** use for TiCl₄ liquid, which reacts).

---

## Hydrochloric Acid

### Saltcake pan: NaCl + H₂SO₄

1. Heat NaCl + conc. H₂SO₄ in iron or ceramic pan → **HCl gas** + NaHSO₄ then Na₂SO₄.
2. Lead or glass **absorption tower** with water → conc. HCl.
3. For dry HCl: bubble through conc. H₂SO₄ first.

### Keep saltcake

Na₂SO₄ / NaHSO₄ feed for **Leblanc** (soda ash) later.

---

## Soda Ash and Caustic

| Route | Steps |
|---|---|
| **Plant/kelp ash** | Burn kelp; leach potash; convert to carbonate with lime kiln CO₂ if needed |
| **Leblanc** | Na₂SO₄ + CaCO₃ + C → Na₂CO₃ + CaS (black ash); leach; crystallize |
| **Caustic** | Na₂CO₃ + Ca(OH)₂ → 2 NaOH + CaCO₃ |

NaOH enables **Castner** sodium and **argon** air separation (remove CO₂).

---

## Glass and Labware

### Batch ratios (soda-lime, by weight)

| Component | Parts |
|---|---|
| Quartz sand (SiO₂) | 70 |
| Soda ash (Na₂CO₃) | 15 |
| Lime (CaO) | 10 |
| Minor cullet | 5 |

Melt **1450-1500°C** in crucible; gather on blowpipe.

### Apparatus list

| Piece | Function |
|---|---|
| Retorts | Distill TiCl₄, H₂SO₄ |
| Liebig condenser | Water cooled distillate |
| Wash bottles | Scrub gas (water, then acid) |
| Ampoules | Store TiCl₄ sealed |
| Sprengel pump | Hg vacuum |
| Ground joints | Grease with stopcock grease or wet ground glass |

### Soda-lime limits

**Not** for hot concentrated HF or long-term hot conc. H₂SO₄. OK for TiCl₄ distillation if dry and no NaOH contact.

### Distilled water

Retort + condenser; store in clean glass. Required for AgNO₃ chloride test and final sponge rinse.

---

## Ethanol

1. Ferment sugar or starch mash with wild yeast **3-7 days**.
2. Distill through pot still; discard foreshots; collect **80-95%** ethanol.
3. Use to **destroy residual sodium** on sponge (slow add, vent, fire away).

---

## Protective Oil

1. Collect petroleum seep or distill **coal tar** low fractions.
2. Dehydrate; store Na under **mineral oil layer ≥2 cm**.
3. **Do not** use vegetable oils (saponify with Na, crust fails).

---

## Manganese Dioxide

| Source | Notes |
|---|---|
| Pyrolusite (MnO₂) | Primary for Scheele chlorine |
| Wad (impure MnO₂) | Wash, roast |

### Weldon recycle (later)

MnCl₂ from Scheele spent liquor + lime + air → regenerated MnO₂. Closes Cl loop partially.

---

## Chlorine Gas

| Method | Reaction | Scale |
|---|---|---|
| **Scheele** | MnO₂ + 4 HCl → MnCl₂ + Cl₂ + 2 H₂O | Bootstrap first Cl₂ |
| **Berthollet** | 2 MnO₂ + 4 HCl + O (from KClO₃) | Faster, needs saltpeter |
| **Deacon** | 4 HCl + O₂ → 2 Cl₂ + 2 H₂O (CuCl₂ on brick catalyst, ~450°C) | After HCl surplus |
| **Brine electrolysis** | 2 NaCl + 2 H₂O → Cl₂ + H₂ + 2 NaOH | Needs steady DC |

### Critical dry gas train (order matters)

```
Cl₂ generator → **water wash** (remove HCl mist) → **conc. H₂SO₄ trap 1** → **conc. H₂SO₄ trap 2** → chlorinator
```

### Exhaust

Bubble waste Cl₂ through **lime milk** (Ca(OH)₂) → Ca(OCl)₂ bleach; do not vent to people.

---

## Titanium Concentrate from Beach

### Finding ore

- Dark **streaks** on beach after storm; sand feels dense.
- Magnet pulls black grains (titanomagnetite); some non-magnetic red-brown (ilmenite).

### Pan and sluice

1. Shovel into wooden riffle box or pan; wash until light sand exits.
2. Magnetic split: hand magnet in bag, pull titanomagnetite/ilmenite.

### Rutile hand pick

Clear red-brown grains, non-magnetic, **~95% TiO₂** if pure rutile. Separate from ilmenite (often magnetic weak, darker).

### Optional low-tech Becher upgrade (ilmenite)

1. Roast ilmenite with sulfuric acid to solubilize iron (messy, slow).
2. Or repeated **magnetic + gravity** and discard light gangue until **85%+ TiO₂** acceptable for chlorinator.

Industrial Becher uses HCl pressure leach; bootstrap stays with physical upgrade unless acid plant is strong.

### Pelletize for chlorinator

Mix **TiO₂ concentrate : calcined charcoal ≈ 1 : 0.15-0.25 by weight**; moisten; roll 5-10 mm pills; dry.

---

## Making TiCl₄

### Reactions

```
TiO₂ + 2 Cl₂ + C → TiCl₄ + CO₂   (exothermic overall with carbon)
TiO₂ + 2 Cl₂ + 2 C → TiCl₄ + 2 CO
Side: Fe₂O₃ + 3 Cl₂ + 3 C → 2 FeCl₃ + 3 CO
      SiO₂ + 2 Cl₂ + 2 C → SiCl₄ + 2 CO   (SiCl₄ b.p. 57°C, separates before TiCl₄)
```

### Apparatus (ASCII)

```
        [Cl₂ dry train]
              │
              ▼
    ┌─── porcelain tube ───┐  ◄── furnace 800-900°C
    │  pellets TiO₂+C      │
    └───┬──────────────┬───┘
        │ crude out    │ vent (to lime scrub if needed)
        ▼
   [condenser 150°C] ──► [receiver in ice-salt]
        │
        ▼
   [distillation column] 136°C head temp
        │
        ▼
   [TiCl₄ ampoules]
```

### Run procedure

1. Dry pellets overnight over charcoal heat.
2. Purge tube with dry Cl₂.
3. Feed Cl₂ **slowly**; exotherm; keep **800-900°C** measured at tube center.
4. Collect liquid in cooled receiver; color yellow to red if FeCl₃.

### Crude problems

| Problem | Cause | Fix |
|---|---|---|
| Yellow/red liquid | FeCl₃ | Redistill; discard low boiler |
| Milky after water | Hydrolysis TiCl₄ + 2 H₂O → TiO₂ + 4 HCl | **Never** wet; reject batch |
| Green tint | VCl₄ / CrCl₃ | More distillation cuts |
| Solid in lines | FeCl₃ freezes ~37°C | Heat tracing |

### Distillation

Collect fraction **135-137°C** at atmospheric pressure (adjust for barometer). Store in **sealed glass ampoules** under dry inert if possible.

---

## Sodium Metal

### Deville (bootstrap primary)

**Na₂CO₃ + 2 C → 2 Na + 3 CO** (simplified stoichiometry; CO/CO₂ mix at temperature)

| Apparatus part | Detail |
|---|---|
| Retort | Iron, **1100-1200°C** zone |
| Condenser | Flat iron plate or short chimney dipping into **hot mineral oil** |
| Collection | Oil bath under condenser lip |

Procedure:

1. Charge dry Na₂CO₃ + calcined charcoal (slight excess C).
2. Heat retort; when Na vapor appears, **orange flame** at vent (CO burning).
3. Na liquid drips into oil; forms beads.
4. Scoop under oil; store jars of oil.

### Castner (molten NaOH electrolysis)

NaOH melt **~320°C**; iron cathode, nickel anode; **DC**; Na floats on melt. Needs steady power and leak-proof cell.

### Downs cell

Molten NaCl + CaCl₂ mix; **~600°C**; industrial scale; harder glass seals bootstrap.

### Na properties and storage

| Property | Value |
|---|---|
| m.p. | 97.8°C |
| Density | 0.97 (floats on oil) |
| Air | Ignites with moisture |
| Storage | **Under mineral oil**, sealed; small jars |

---

## Magnesium (Kroll alt)

| Path | Outline |
|---|---|
| **Seawater Dow** | Bittern + lime → Mg(OH)₂ → HCl → MgCl₂ melt electrolysis → Mg |
| **Pidgeon** | Dolomite calcined + ferrosilicon (needs Si) → Mg vapor distill |
| Use | **Kroll:** TiCl₄ + 2 Mg → Ti + 2 MgCl₂ in retort |

See `TitaniumProcessing.md` for Kroll retort geometry. Bootstrap chooses Hunter if only Deville Na exists.

---

## Argon from Air

### Rayleigh/Ramsay chemical method (bootstrap)

1. Remove CO₂ with **NaOH** or lime water.
2. Pass over **hot copper** → removes O₂ as CuO.
3. Pass over **hot magnesium** (or **fresh Ti sponge getter**) → removes residual O₂/N₂ reactively.
4. Remaining **~0.93% Ar** in "argon enriched" stream; recycle loop through getters until usable for arc melting.

Yield low; **recirculate** same gas in closed arc hood.

### Cryogenic note

Liquid air distillation gives pure Ar but needs **-186°C** and high compression. Not first bootstrap.

### Ti getter trick

First Hunter sponge: crush; heat in tube; absorbs O₂/N₂ from argon loop cheaply.

---

## Vacuum

| Pump | Mechanism | Bootstrap |
|---|---|---|
| **Sprengel** | Hg falling columns trap gas | Best 19th c. lab vacuum |
| **Toepler** | Mercury piston displacement | Moderate vacuum |
| Mechanical | Later piston | Needs machining |

### Leak seals

Stopcock grease, ground glass, mercury joints. **No rubber** with Cl₂ long term.

### Manometer / McLeod

Measure low pressure for iodide bar and degassing.

---

## Electricity

| Source | Spec | Notes |
|---|---|---|
| Voltaic pile | Cu/Zn plates + acid | Trickle; stack many |
| Daniell cell | Cu/CuSO₄ || Zn/ZnSO₄ | Steadier |
| Bunsen (carbon/zinc) | Higher voltage | Corrosive |
| **Dynamo** | Hand or water wheel | **Target 20-40 V DC, 100-300 A** for arc |

### Dynamo construction (outline)

1. Iron pole pieces and field windings (copper wire).
2. Commutator rings; carbon brushes.
3. Water wheel or treadmill drive.

### Carbon electrodes

Bake hardwood rods in retort (**~1000°C**) for arc carbon. Tip arc melt under argon.

---

## Hunter Bomb Reduction

### Reaction

```
TiCl₄ + 4 Na → Ti + 4 NaCl     ΔH strongly exothermic
```

### Proportions per 100 g Ti metal (theoretical)

| Reagent | Molar mass | Moles | Mass |
|---|---|---|---|
| Ti product | 47.87 | 2.089 | 100 g |
| TiCl₄ | 189.68 | 2.089 | **396 g** |
| Na | 22.99 | 8.356 | **192 g** |

Practice: **5-10% excess Na**; TiCl₄ added slowly to Na pool or layered with Na chunks.

### Bomb build

1. Cylinder **≥1 cm wall** steel; one flat end welded.
2. Lid: **flat machined seat**, copper or soft iron gasket, **bolt ring**.
3. Interior **dry**; preheat to **200°C** to drive moisture.
4. Load Na under argon flood if available, else preheated dry bomb quickly.

### Procedure

1. Seal except vent needle; heat bomb to **800-1000°C** (external furnace or buried charcoal with bellows).
2. Introduce TiCl₄ vapor or pre-weighed liquid via **break-seal** or slow drip tube (glass into steel coupling).
3. Reaction self-heats; maintain temperature until pressure subsides.
4. **Cool** to room temp before opening.

### Opening

1. Unbolt remotely if possible; stand back.
2. Expect **NaCl crust** and **porous Ti sponge**.
3. Do not grind dry sponge to fine powder (fire risk).

---

## Leach Wash Dry

| Step | Action |
|---|---|
| 1 Ethanol | Pour ethanol over sponge to react **residual Na**; vent outdoors; no flames |
| 2 Water leach | Boil or soak in **distilled water**; dissolve NaCl |
| 3 Dilute HCl | **1-5%** HCl brief dip; remove oxide/hydroxide; do not soak hours |
| 4 Distilled rinse | Until no chloride |
| 5 AgNO₃ test | Drop nitrate on rinse water; **no white precipitate** |
| 6 Ethanol rinse | Displace water |
| 7 Dry | **Vacuum or warm <100°C**; or argon flush; store in sealed jar |

---

## Consolidation

### A Sinter press + 1100-1300°C vacuum/Ar

1. Crush sponge to **1-3 mm**; cold press in steel die.
2. Heat **1100-1300°C** hours under vacuum or argon.
3. Partial densification; may need repeat.

### B Arc melt button on water-cooled Cu hearth (full procedure)

1. **Cu hearth** plate, water cooled from below.
2. Hood flooded with **argon** (recirculated getter loop).
3. **20-40 V DC**, **100-300 A**; strike arc to sponge pile on hearth.
4. **Melt pool**; add sponge with rod; avoid long arc in air.
5. Button freezes on Cu (does not weld if cold copper).
6. Flip button; remelt 2-3 times for homogeneity.

### C EB/skull (later)

Electron beam or skull melting for big ingots; needs advanced vacuum and power.

### Quality checks during weld

| Observation | Meaning |
|---|---|
| Bright silver pool | Good inert cover |
| Blue/green tint | Air leak, contamination |
| Button silver-gray | OK Ti |
| Button dull gray | O/N pick-up |

---

## Iodide Crystal Bar

### Iodine from kelp

1. Burn kelp; leach ash.
2. Acidify with H₂SO₄; add MnO₂ or oxidizer; distill **I₂**.

### Optional W filament

Reduce wolframite (if available) to WO₃ then H₂ to W powder; sinter wire.

### Apparatus

Glass or quartz tube; **W or Ti** filament **1300-1500°C**; tube walls **200-400°C**.

### Procedure

1. Charge iodine + crude Ti at cold end.
2. Heat filament hot; iodine sublimes; **Ti + 2 I₂ ⇌ TiI₄** transports to hot wire.
3. Ti deposits on filament; **I₂** cycles.
4. Bar grows over hours/days under vacuum.

---

## Verifying Titanium

| Test | Expected for Ti |
|---|---|
| Density | **~4.5 g/cm³** (4.51) |
| Magnet | **Nonmagnetic** |
| Spark | **White** (not yellow Fe) |
| Salt water | **No rust** like steel |
| Bend | Elastic, hard |
| File | Hard, white streak chips |
| Heat tint | Thin oxide colors if heated in air |
| Anodize | Color sequence with voltage (if acid bath built) |
| Acid | Resists HCl room temp; HF attacks (avoid HF) |
| Melting point | **~1668°C** (lab indirect) |

---

## Mass Balance 100 g Ti

Assumes **pure TiO₂ feed** (rutile equivalent). Real ilmenite needs more mass and drops FeCl₃ side streams.

### Ti path (concentrate → metal)

| Material | kg per 100 g Ti | Notes |
|---|---|---|
| TiO₂ (100%) | 0.167 | Stoichiometric |
| Charcoal (chlorination) | ~0.05 | 0.15-0.25 × TiO₂ |
| Cl₂ (to TiCl₄) | 0.296 | See Cl path |
| Na (Hunter + 5% excess) | 0.202 | 192 g + excess |
| TiCl₄ handled | 0.396 | Intermediate |

### Cl₂ path (Scheele, per 296 g Cl₂)

| Material | kg | Reaction basis |
|---|---|---|
| Cl₂ target | 0.296 | 4.18 mol |
| MnO₂ | 0.363 | 1 mol MnO₂ per mol Cl₂ |
| HCl (conc.) | ~1.2 L equiv. | 4 mol HCl per mol Cl₂ |
| MnCl₂ waste | Recycle Weldon | |

### Na path (Deville, per 202 g Na)

| Material | kg | Notes |
|---|---|---|
| Na metal | 0.202 | Product |
| Na₂CO₃ | ~0.47 | ~2.09 mol carbonate |
| C (fixing) | ~0.11 | Stoichiometric + loss |

### Major byproducts (100 g Ti batch)

| Byproduct | Approx mass | Disposal/use |
|---|---|---|
| NaCl | 0.48 kg | Leach liquor evaporate |
| CO/CO₂ | Gas | Vent |
| FeCl₃ (if Fe in feed) | Variable | Separate in distill |
| MnCl₂ liquor | From Cl₂ | Weldon |
| Sponge leach water | Saline | Evaporate salt |

---

## Hawaii Resource Availability

| Resource | On typical Hawaiian volcanic coast | Bootstrap note |
|---|---|---|
| Black sand HM (Ti) | **Yes** (localized beaches) | Feed; grade often ilmenite/titanomagnetite |
| Magnetite iron sand | **Yes** | Bloomery |
| Shells/coral lime | **Yes** | Soda, scrubbers |
| Seawater/brine | **Yes** | Salt, bittern, Mg |
| Clay | **Variable** | Refractories; test deposits |
| Quartz glass sand | **Often poor** | Import or crush quartzite if found |
| Native sulfur | **Rare** | Pyrite substitute unlikely locally |
| Coal/petroleum | **Limited** | Seep tar if any; charcoal primary |
| Copper/lead/zinc ores | **No** (trace) | **Import** for wire, Hg, Pb chamber |
| MnO₂ | **Unlikely local** | Import pyrolusite or make from Mn ore trade |
| Wolframite | **No** | Optional W import |
| Hydropower | **Some streams** | Brine electrolysis, dynamo |
| Hardwood charcoal | **Yes** (managed forest) | Energy limit |

### Practical Hawaii route note

- Expect **laterite/slag Ti** chemistry same as sand after concentrate.
- **Brine electrolysis** for Cl₂ and NaOH fits island **hydropower** if streams allow.
- **Import** glass sand, copper wire, MnO₂, and possibly first mercury for vacuum.
- First metal likely **small buttons** before tonnage.

---

## Bootstrap Hazards

| Hazard | Source | Mechanism | Control |
|---|---|---|---|
| **Cl₂** | MnO₂/HCl, electrolysis | Pulmonary edema, death | Scrubber, wind, train dryers |
| **TiCl₄** | Chlorinator | Fumes hydrolyze to HCl + TiO₂; burns skin | Dry gloves, hood, no water on liquid |
| **H₂SO₄** | Vitriol, chamber | Burns, exothermic dilution | Pb/glass, face shield |
| **HCl** | Saltcake | Corrosive mist | Glass, ventilation |
| **Na** | Deville, Hunter | Pyrophoric, explodes with water | Oil storage, dry bomb |
| **Hunter bomb** | TiCl₄ + Na | Overpressure, fireball if wet | Remote heat, gauge, bolt lid, dry |
| **CO** | Charcoal furnaces | Asphyxiant | Outdoor ops |
| **Hg** | Sprengel pump | Neurotoxin vapor | Tray spill control, no heat on Hg |
| **Pb** | Acid chambers | Chronic poison | Wash hands, no food near |
| **SO₂** | Roasts, chamber | Lung irritant | Tall stack, dilution |
| **Arc melt** | DC high current | UV, molten metal splash | Hood, gloves, argon |
| **Ti powder** | Fine sponge grind | Dust explosion | Keep coarse; wet if must grind |
| **Silica dust** | Sand, glass | Silicosis | Wet work, mask |
| **H₂** | Brine electrolysis | Explosive with air | Separate vent, no flames |

---

## Cross-links

- Industrial scale and pigment split: `TitaniumProcessing.md`
- Ore geography and laterite: `Titanium.md`, `../../Geography/VolcanicIsland/Sands.md`
- Purification ladder: `../../Materials/MaterialPurification.md`

*End of bootstrap reference.*
