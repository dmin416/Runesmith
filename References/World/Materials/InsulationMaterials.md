# Insulation Materials

> Earth reference / design loot. Not locked law. Thermal skills do **not** insulate (`../../Progression/ResistanceImmunitySystem.md`). Gear and separate skills sit here. Fantasy insulator ideas: `MaterialConsiderations.md`. Graphene aerogel / metamaterials invent: `ExoticMaterials.md`. Silica feed: `../Science/Metallurgy/SilicaSand.md`. Structural / enclosure EE-EC ladder: `BuildingMaterials.md`. Touch temperature / sanitary surface energy: `CleanableSurfaces.md`.

---

## Best Insulators

Thermal conductivity measures how fast heat flows through a material. Lower means better insulation.

| Material | Conductivity (W/m·K) |
|---|---|
| Copper (for contrast) | ~400 |
| Steel | ~15–50 |
| Glass | ~1 |
| Water | ~0.6 |
| Human skin | ~0.3–0.4 |
| Wood | ~0.12 |
| Wool, fiberglass | ~0.04 |
| Still air | ~0.026 |
| Polyurethane foam | ~0.022 |
| Silica aerogel | ~0.012–0.02 |
| Vacuum insulation panel | ~0.004 |
| Multilayer insulation in vacuum (spacecraft blankets) | ~0.00001–0.0001 |

**Best ordinary insulator:** silica aerogel. It is about 99% air trapped in pores smaller than the distance air molecules travel between collisions, so even the air can't carry heat. It beats still air.

**Best insulator possible:** vacuum. With no matter, heat can't conduct or convect and can only radiate. Stacking thin reflective layers in a vacuum (spacecraft blankets, thermos flasks) blocks most of that radiation as well. Nothing outperforms vacuum plus reflective layers.

**Lowest-conducting dense solid:** disordered layered tungsten diselenide (WSe₂), measured in 2007 at ~0.05 W/m·K. That is solid material insulating nearly as well as wool.

## High-Temperature Insulators

| Material | Survives | Notes |
|---|---|---|
| Space Shuttle silica tiles (LI-900) | ~1,260°C | Over 90% air, 99.9% pure silica fibers |
| Reinforced carbon-carbon | ~1,650°C | Shuttle nose and wing edges; a heat-resistant shield rather than an insulator |
| Alumina and zirconia fiber | 1,600–2,000°C+ | Furnace linings |
| Boron nitride aerogel | ~1,400°C | Survives repeated swings from −198°C to 900°C without cracking |
| Carbon aerogel (no oxygen present) | 2,000°C+ | Burns if exposed to air |

## Why Shuttle Tiles Cool Instantly

The famous demonstration: a tile comes out of a furnace at ~1,260°C with its center still glowing, and a person holds it by the edges bare-handed within seconds.

1. **Almost nothing is there.** The tile is over 90% air, about one seventh the density of water. It stores very little heat.
2. **Heat can't travel through it.** The interior heat can't reach the surface or fingers quickly. The core can glow while the edges are cool.
3. **The surface sheds heat fast.** Only a thin outer layer is in contact with air, and it loses its small heat load in seconds.
4. **Contact is tiny.** Fingers touch the tips of thin glass fibers rather than a solid surface.
5. **It doesn't crack.** Silica barely expands with heat, so sudden temperature changes don't shatter it.

## Contact Temperature

What skin feels on touch depends on **effusivity**: how readily a material gives up heat on contact.

**Contact temperature = (e₁T₁ + e₂T₂) / (e₁ + e₂)**

| Material | Effusivity (approx.) |
|---|---|
| Copper | ~37,000 |
| Steel | ~14,000 |
| Water | ~1,600 |
| Human skin | ~1,100 |
| Wood | ~400 |
| Shuttle tile | ~85 |
| Aerogel | ~40 |

| Touching | Object temp | Skin feels |
|---|---|---|
| Steel | 100°C | ~95°C (burns) |
| Wood sauna bench | 100°C | ~51°C (tolerable briefly) |
| Heat-skilled character's skin | 300°C | ~166°C (instant burn) |

## Skill System Application

- Skin touching skin splits the difference evenly. A Heat Immunity holder at 300°C burns anyone who touches them instantly.
- Low-effusivity layers like wool, aerogel fabric or silica fiber between them sharply cut the heat transferred.
- Insulation falls under separate gear or skills, not the Thermal family.

---

## Building Foam Insulation (from BuildingMaterials)

> Structural polymer strength and EE also summarized in `BuildingMaterials.md` §14 stub. Permeation / vapor: `PermeationBarriers.md`.

## 14.1 How polymers achieve strength

Polymer chains have strong covalent backbones (C-C bonds ~350 kJ/mol), but bulk strength depends on interactions between chains:
- **Thermoplastics** (PVC, PE, PP, PC, PMMA): chains held by van der Waals forces, hydrogen bonds and entanglement. Crystalline regions (lamellae ~10 nm thick) in semicrystalline polymers add stiffness. They soften on heating and can be remelted.
- **Thermosets** (epoxy, polyester, phenolic, polyurethane rigid foam): covalently crosslinked 3D networks; do not melt; usually stiffer and more heat-resistant but not remeltable.

Above the glass transition temperature (Tg), amorphous regions become rubbery. Polymers creep significantly at room temperature.

| Polymer | Tensile (MPa) | E (GPa) | Tg / Tm | Use |
|---|---|---|---|---|
| PVC (rigid) | 40-55 | 2.5-3.5 | Tg ~80°C | Pipes, window frames, membranes, cladding |
| HDPE | 20-35 | 0.8-1.2 | Tm ~130°C | Pipes, geomembranes |
| Polypropylene | 30-40 | 1.2-1.7 | Tm ~165°C | Fibers in concrete, pipes |
| Polycarbonate | 55-75 | 2.2-2.5 | Tg ~147°C | Impact-resistant glazing |
| PMMA (acrylic) | 50-75 | 2.4-3.3 | Tg ~105°C | Glazing, skylights |
| Epoxy | 50-90 | 2.5-4 | Tg 60-180°C | Adhesives, coatings, FRP matrix |

## 14.2 Insulation foams
- **EPS (expanded polystyrene)**: beads expanded with pentane, fused in molds; λ ≈ 0.031 to 0.038 W/m·K
- **XPS (extruded polystyrene)**: closed-cell; historically blown with HFCs (high global warming potential), now shifting to CO₂ and HFOs; λ ≈ 0.029 to 0.035
- **PIR/PUR (polyisocyanurate/polyurethane)**: thermoset closed-cell foam; λ ≈ 0.022 to 0.028
- **Phenolic foam**: λ ≈ 0.018 to 0.023
- **Mineral wool (stone/glass)**: not polymer; fibers spun from molten rock at ~1500°C or glass; binder; λ ≈ 0.032 to 0.040; non-combustible

## 14.3 Production and renewability
Feedstocks come from crude oil or natural gas by steam cracking (ethylene, propylene) at ~850°C, followed by polymerization. PVC adds chlorine from salt electrolysis (chlor-alkali process): ~57% of PVC mass is chlorine.

| Material | EE (MJ/kg) | EC (kg CO₂e/kg) |
|---|---|---|
| PVC | 60-80 | 2-3.2 |
| HDPE | 75-85 | 1.9-2.0 |
| EPS | 85-90 | 3.3-3.5 |
| XPS (HFO/CO₂ blown) | 85-95 | 3-4 (much higher with HFC blowing) |
| PIR | 90-100 | 3.5-4.5 |
| Mineral wool | 15-20 | 1.1-1.3 |
| Polycarbonate | 100-115 | 6-8 |

Note: roughly half the embodied energy of polymers is "feedstock energy" locked in the material (recoverable by incineration).

- **Renewability**: Class F (fossil). Bio-based polyethylene (from sugarcane ethanol) and other bio-polymers exist at small scale.
- **Recycling**: technically possible for thermoplastics; actual building plastic recycling rates are low due to contamination, additives and mixed materials. VinylPlus in Europe recycles hundreds of thousands of tonnes of PVC annually.
- **Durability concerns**: UV degradation (chain scission), plasticizer migration, flammability and toxic smoke.

**Effort rating**: High energy; chemically complex process chains.

---

