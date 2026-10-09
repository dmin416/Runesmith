# Nitinol (Earth Metallurgy)

Hub: `Nickel.md`, `Titanium.md`, `TitaniumBootstrap.md`. Mana-saturated gear lore: `../../Materials/MaterialConsiderations.md`. Hawaiian mass balance: end of this file + `../../Geography/HawaiianMinerals.md`.

Earth NiTi shape-memory / superelastic alloy. On Terra, mundane nitinol is invent from D's Earth knowledge; mana-saturated variant is locked in MaterialConsiderations.

## Fundamentals

Intermetallic near equal atomic Ni and Ti (~50 to 51 at% Ni, ~55 to 56 wt% Ni). Name: Nickel Titanium Naval Ordnance Laboratory. Discovered by Buehler et al. 1959 to 1962; Wang explained much crystal behavior.

| Behavior | What happens | Requirement |
|---|---|---|
| Shape memory | Bent cold (martensite), stays bent; heat above Af → snaps to trained shape | Used below transformation temperature |
| Superelasticity | Bends ~8% strain and springs fully back | Used just above Af |

| Phase | Structure | Stable at | Character |
|---|---|---|---|
| Austenite (B2) | Ordered cubic | High T | Stiffer, parent shape |
| Martensite (B19′) | Monoclinic, twinned | Low T | Soft, detwins easily |
| R-phase | Rhombohedral | Intermediate (some alloys/HT) | Small strain, small hysteresis |

| Symbol | Meaning |
|---|---|
| Ms / Mf | Martensite start / finish on cooling |
| As / Af | Austenite start / finish on heating (Af is the key spec) |
| Md | Above this, stress cannot induce martensite; SE stops |

Hysteresis typically ~20 to 40°C for B2↔B19′, 1 to 5°C for R-phase. Af settable roughly −100°C to +100°C by composition and heat treatment.

**Shape memory mechanism:** cool → twinned martensite (no net shape change) → bend detwins → heat → single austenite arrangement restores trained shape.

**Superelasticity:** above Af, stress induces martensite (plateau strain) → unload → reverts.

### Typical properties

| Property | Austenite | Martensite |
|---|---|---|
| Density | 6.45 g/cm³ | 6.45 |
| Melting point | ~1310°C | ~1310 |
| Young's modulus | 70 to 83 GPa | 28 to 41 GPa |
| Yield | 195 to 690 MPa | 70 to 140 MPa (detwinning) |
| UTS annealed / cold worked | ~900 / up to ~1900 MPa | |
| Elongation | 15 to 50% | |
| Recoverable strain (one way) | Up to ~8% | |
| Two way / long life actuators | ~2 to 4% / keep under ~3 to 4% | |
| Resistivity | ~82 µΩ·cm | ~76 |
| Thermal conductivity | ~18 W/m·K | ~9 |
| Corrosion / magnetism | Excellent TiO₂ film / nonmagnetic | |

Uses: stents, guidewires, orthodontic archwires, actuators, shrink couplings, eyeglass frames, dampers, deployables.

## Composition and Purity

wt% Ni = (at% Ni × 58.69) / [(at% Ni × 58.69) + ((100 − at% Ni) × 47.87)] × 100

| at% Ni | wt% Ni | wt% Ti | Per 100 g (Ni / Ti) | Typical behavior |
|---|---|---|---|---|
| 49.5 | 54.58 | 45.42 | 54.58 / 45.42 | SM, high Af (Ti₂Ni present) |
| 50.0 | 55.07 | 44.93 | 55.07 / 44.93 | SM, Af roughly 60 to 100°C |
| 50.4 | 55.47 | 44.53 | 55.47 / 44.53 | SM near body/room T |
| 50.8 | 55.87 | 44.13 | 55.87 / 44.13 | SE at room/body (common medical) |
| 51.0 | 56.07 | 43.93 | 56.07 / 43.93 | SE, lower Af |

Ni-rich side: ~0.1 at% more Ni lowers transformation T by roughly 10 to 20°C. Ti-rich side levels off (extra Ti → Ti₂Ni). Weigh to ~0.01 g on a 100 g charge (1 mg preferred).

| Impurity | Forms | Effect |
|---|---|---|
| Oxygen | Ti₄Ni₂Oₓ | Consumes Ti, matrix Ni-richer, lower Af, fatigue hits |
| Carbon | TiC | Same shift + crack inclusions |
| Nitrogen | TiN | Hard inclusions |
| Hydrogen | Hydrides | Embrittlement |
| Fe, Cr | Sub for Ni | Lower transformation T |
| Cobalt | Sub for Ni | Lower T, stiffens |
| Copper | Sub for Ni | Narrows hysteresis (sometimes intentional) |

Medical-grade style limits (ASTM F2063 approx; check current): Ni 54.5 to 57.0 wt%; C ~0.04 to 0.05% max; O ~0.04 to 0.05% max; H ~0.005% max; Fe/Co ~0.05% max; Cu/Cr ~0.01% max; Nb ~0.025% max; inclusion size/area limits.

**Raw materials:** Ti with low O (crystal bar ideal; clean Hunter + arc melt OK for non-medical). Ni 99.9%+, low Co/Fe/S/C (electrowon).

| Alloy | Addition | Purpose |
|---|---|---|
| NiTiCu | 5 to 10 at% Cu for Ni | Narrow hysteresis, actuators |
| NiTiFe / NiTiCr | Small Fe or Cr | Lower T, stiffer SE wire |
| NiTiNb | ~9 at% Nb | Wide hysteresis, couplings |
| NiTiHf/Zr/Pd/Pt | Various | High-T SMA (Af >100°C) |
| NiTiCo | Small Co | Higher stiffness SE |

| Phase | When | Effect |
|---|---|---|
| Ti₂Ni | Ti-rich / O contaminated | Brittle particles |
| Ni₄Ti₃ | Age Ni-rich 300 to 500°C | Raises Af, strengthens, R-phase |
| Ni₃Ti | Long age above ~600°C | Coarse, lower strength |
| TiC, Ti₄Ni₂Oₓ | C/O contamination | Inclusions |

## Melting

| Method | Pros | Cons |
|---|---|---|
| VIM (graphite crucible) | Mixing, composition | Carbon → TiC |
| VAR | Low C, clean | Segregation; multiple remelts |
| VIM + VAR | Medical standard | Some C from VIM |
| EB | Clean | Ni evaporates preferentially |
| Induction skull | No crucible pickup | Expensive, small |
| Plasma arc | Clean, little evaporation | Heavy gear |
| PM / SHS | Near-net, porous | O pickup, mixed phases |

### Small-scale arc melting

Same button furnace as Ti (`TitaniumBootstrap.md` Part 63 style): Cu hearth, W or Ti electrode, vacuum + Ar, DC.

1. Clean Ti (pickle HNO₃±HF or abrade + rinse ethanol) and Ni (abrade, dilute acid, rinse). Dry.
2. Weigh to target. Separate Ti getter.
3. Evacuate / Ar backfill ×3. Melt getter 30 to 60 s.
4. Melt charge fully (exothermic flare: moderate current). Hold 20 to 40 s sweeping.
5. Flip and remelt 5 to 8 times. Mass loss should be <<0.1%.
6. Homogenize: sealed ampoule/can with Ti getter, 900 to 1000°C, 12 to 24 h, water quench.
7. Trim: if Af too high add Ni and remelt; if too low add Ti. Re-homogenize.

## Working, Shape Setting, Heat Treat

**Hot work:** ~700 to 950°C (often 800 to 900). Short heats, coatings, or steel can. Frequent reheats.

**Cold work:** hardens fast. ~20 to 40% reduction then anneal 600 to 800°C minutes + water quench. Wire: point → carbide/diamond dies → oxide as lube carrier + graphite/MoS₂ → optional warm draw ~400 to 500°C. Final cold work ~30 to 45% before shape set for best SE.

**Shape set:** fixture to final form → ~450 to 550°C (start ~500°C) → fine wire 2 to 10 min, thicker 10 to 30 min → water quench. Large changes in steps.

| Treatment | Temperature | Effect |
|---|---|---|
| Solution anneal | 850 to 1000°C + quench | Dissolves Ni₄Ti₃, resets aging, softens |
| Shape set / age | 450 to 550°C, minutes | Sets shape, adjusts Af, strengthens |
| Low-T aging | 350 to 450°C | Ni₄Ti₃, raises Af, may R-phase |
| Overaging | Above ~600°C long | Coarse Ni₃Ti, unstable |
| Recovery on heavy CW | 300 to 450°C | High strength, partial SE |

Heating options: molten nitrate salt bath (NaNO₃+KNO₃, ~220 to 550°C, oxidizer, no organics), fluidized sand, air furnace, resistance heat of wire, molten lead (toxic).

**Low-tech T cues:** Draper point faint red ~525°C; Zn MP 420; Pb 327; Al 660; NaNO₃ 308; steel temper colors ~220 to 320.

**Machining:** carbide, low speed, flood coolant; grind with coolant; EDM; laser (stents); waterjet. Avoid local overheat.

**Joining:** laser/TIG NiTi–NiTi under Ar; NiTi–steel needs Ni/Ta interlayer or mechanical; crimp common; solder needs aggressive flux or plate first.

**Surface:** blast/tumble oxide → pickle or polish → electropolish (medical) → passivate. Controlled oxidation for interference colors.

## Testing and Training

**Quick SM:** chill in ice → bend 90° → hot water 80 to 95°C → straightens instantly.

**Quick SE:** room-T tight loop → springs straight with no kink (steel takes permanent set sooner).

**Bend and free recovery (Af, ASTM F2082 style):** cool below Mf → bend on mandrel → slow warm (~0.5 to 1°C/min) in stirred bath → record As and Af.

Other: DSC, tensile plateaus, resistance vs T, hardness, fatigue, Ni release.

**One way vs two way:** one way needs external deform each cycle; two way trained (shape set hot shape → cool deform → heat constrained → repeat 20 to 100 cycles). Smaller strain, less stable.

**Electrical actuators:** current heats wire above Af → contracts ~3 to 5% length; bias spring returns on cool.

| Wire diameter | Approx current (still air) |
|---|---|
| 0.025 mm | ~45 mA |
| 0.05 mm | ~85 mA |
| 0.1 mm | ~180 mA |
| 0.15 mm | ~400 mA |
| 0.25 mm | ~1 A |
| 0.5 mm | ~4 A |

Overheating destroys trained shape. Long life: strain under ~3 to 4%, moderate stress.

## Hawaiian Raw Materials Mass Balance (100 g NiTi, 50.8 at% Ni)

Chain: olivine → HCl leach → Fe out → NiS/Ni(OH)₂ → Co/Mn out → electrowon Ni; Ti from laterite / Route H1 residue → TiCl₄ → Hunter → iodide bar → arc melt → work → shape set.

**Ni side (~56 g + 10% margin ≈ 62 g):** ~30 kg olivine concentrate (0.28% Ni, 75% recovery) or 100 to 150 kg picrite; ~30 kg HCl 100% basis (mostly recovered); 1 to 2 kg Cl₂; 0.2 to 0.3 kg H₂S if sulfide route; ~0.25 kWh EW + losses; byproducts ~12 kg silica, ~14 kg MgO, ~3 to 4 kg iron oxide.

**Ti side (~44 g + 15% ≈ 51 g):** ~85 g TiO₂; ~210 g of 40% TiO₂ residue or ~90 g rutile; ~150 g Cl₂ theoretical; ~200 g TiCl₄; ~98 g Na; few g I₂ recycled.

**Checkpoints:** Ni solution Co/Fe tests clean; Ni bright ductile 99.9%+; Ti silver bendable (prefer crystal bar); getter melt stays bright; button bright, no crack on cold-rolled corner, sharp water-bath transformation.

Practical: small arc buttons 10 to 100 g are realistic. Ti purity is the harder half.

## Hazards

| Material / step | Hazard | Control |
|---|---|---|
| Ni dusts, oxides, sulfides | Lung/nasal cancer risk | Wet handling, masks, no dry sweep |
| Ni salts / metal | Contact dermatitis | Gloves, wash |
| Nickel carbonyl | Delayed lethal lung injury | Avoid Mond |
| H₂S | Toxic, smell fatigue | Outdoors, scrub, small generators |
| HCl leach / pyrohydrolysis | Fumes, boil-over gels, hot HCl | Ventilation, gradual add, sealed absorbers |
| Cl₂ / hypochlorite | Toxic gas | Scrubbers, outdoors |
| Co compounds | Toxic, sensitizing | Same as Ni |
| Nitrate salt baths | Strong oxidizer | Clean dry parts, <~550°C, Fe/steel pots |
| HF pickle | Penetrating burns | Prefer mechanical cleaning |
| SE wire | Springs back violently | Eye protection, hold both ends |
| Actuator wire | Burns, overheat | Current limits |
| Arc melt / grind fines | UV, current, flammable fines | Dark glass, wet grind |
