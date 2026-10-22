# Printer Manufacturing: Process Reference

Design loot. Pack hub: `PrinterManufacturing.md`. Materials: `PrinterManufacturingMaterials.md`. Vehicles: `PrinterManufacturingVehicles.md`.

## 2. Process Reference

### 2.1 Casting methods

| Method | How it works | Best for | Typical finish |
|---|---|---|---|
| Green sand | Sand plus clay plus water rammed around a pattern | Engine blocks, heads, manifolds, brake drums, cast iron cookware | Rough, needs machining on all mating faces |
| Resin-bonded sand / sand cores | Sand bound with resin, baked hard | Water jackets and oil passages inside blocks and heads | Better than green sand |
| Investment (lost wax) | Wax pattern coated in ceramic slurry, wax melted out, metal poured into shell | Rocker arms, small complex steel parts, valve bodies, turbine wheels | Fine, near-net shape |
| Permanent mold | Reusable steel or iron mold, gravity pour | Aluminum pistons, aluminum heads, wheels | Good |
| Low-pressure die casting | Molten aluminum pushed up into a mold by gas pressure | Cast aluminum wheels | Good, low porosity |
| High-pressure die casting | Metal injected at high speed into steel dies | Zinc carburetor bodies, aluminum appliance housings, transmission cases | Excellent, but porous inside so not heat treatable |
| Centrifugal | Mold spun while metal is poured | Cylinder liners, pipes, bushings | Dense outer wall |
| Chill casting | Iron or copper chills placed in the mold where hardness is wanted | Camshaft lobes in cast iron (forms hard white iron on lobe surface) | Hard surface where chilled |

### 2.2 Forging methods

| Method | How it works | Used for |
|---|---|---|
| Open die | Hammer or press between flat or simple dies, part rotated by hand | Shafts, axles, large rings, blacksmith work |
| Closed die (impression die) | Hot billet hammered or pressed between shaped dies; excess squeezes out as flash, which is trimmed | Crankshafts, connecting rods, gear blanks, steering knuckles, control arms, wrenches |
| Upset forging | Bar end heated and pushed to increase diameter | Valve heads, bolt heads, axle flanges |
| Roll forging | Bar passed through grooved rolls | Tapered leaf springs, axle shafts |
| Ring rolling | Pierced donut rolled to a larger thin ring | Bearing races, gear rings |
| Cold heading | Wire pushed into dies at room temperature | Bolts, rivets, bearing balls (headed as rough spheres before grinding) |

**Forging temperatures (steel):** Typically 1100-1250°C start, stop working before falling below about 850-900°C. Working too cold cracks the part. Working too hot burns the steel (grain boundaries oxidize) and it cannot be saved.

**Hand forging check:** Steel at forging heat glows bright orange to yellow. When it fades to dull red, return it to the fire.

### 2.3 Machining

| Operation | Purpose | Typical tolerance |
|---|---|---|
| Milling | Flat faces, pockets, slots, gasket surfaces, bolt bosses | ±0.025-0.05 mm routine |
| Turning (lathe) | Round parts: shafts, pistons, pins, axles | ±0.01-0.025 mm |
| Boring | Opening holes to precise size and alignment: cylinder bores, main bearing line bore, cam tunnel | ±0.01 mm |
| Drilling and reaming | Holes; reaming brings them to exact size | Reamed ±0.01 mm |
| Hobbing / gear shaping | Cutting gear teeth | AGMA quality depends on machine |
| Broaching | Internal splines and keyways in one pass | Very consistent |
| Grinding | Final size and finish on hardened surfaces (journals, races, cam lobes, valve stems, gear teeth) | ±0.002-0.005 mm |
| Honing | Cylinder bores, lifter bores, rod big ends; produces crosshatch for oil retention | Roundness under 0.005 mm |
| Lapping | Ultimate flatness and finish: bearing balls, valve seats, fuel injector parts, gauge blocks | Sub-micron |
| Superfinishing | Removes the peaks left by grinding on journals and races | Ra 0.05-0.2 µm |

**Rule:** Anything that slides, rotates in a bearing, seals against a gasket, or meshes with gear teeth gets machined, and if hardened, ground after hardening. Printers at Tier A and B cannot reach these surfaces directly.

### 2.4 Heat treatment of steel

| Process | Steps | Effect | When used |
|---|---|---|---|
| Full anneal | Heat above upper critical (roughly 815-900°C depending on alloy), hold, cool very slowly in the furnace | Softest, most machinable state | Before heavy machining or cold forming |
| Normalize | Heat above upper critical, cool in still air | Refines and evens out grain after forging or welding | After every forging, before hardening |
| Stress relief | Heat to 550-650°C, hold, slow cool | Removes residual stress without changing hardness much | After welding, heavy machining, printing |
| Quench (harden) | Heat to austenitizing temperature (about 815-870°C for medium carbon and alloy steels), plunge into water, brine, oil, polymer or air depending on alloy | Forms martensite: very hard, very brittle | All hardened parts |
| Temper | Reheat to 150-650°C after quench, hold 1-2 hours per 25 mm thickness, usually twice | Trades hardness for toughness. Low temper: hard and wear resistant. High temper: tough and springy | Immediately after every quench, before the part cools fully to room temperature for crack-prone alloys |
| Austemper | Quench into molten salt around 260-400°C and hold | Bainite: tough with less distortion | Springs, clips, some gears, austempered ductile iron |
| Carburize | Hold low-carbon steel (8620, 9310) at about 900-930°C in carbon-rich atmosphere, then quench and temper | Hard high-carbon skin over a tough low-carbon core | Gears, cam followers, wrist pins, U-joint crosses, ring and pinion |
| Carbonitride | Like carburizing with added nitrogen, lower temperature | Thinner hard case | Small gears, fasteners, shift parts |
| Nitride | Hold finished part at about 500-550°C in ammonia or plasma nitrogen | Very hard thin case, almost no distortion since no quench | Crankshaft journals, cylinder liners, piston rings, gun-drilled shafts, valve stems |
| Induction harden | Electromagnetic coil heats only the surface, water spray quench follows | Hard surface where needed, soft elsewhere | Axle shafts, crankshaft journals, sprocket teeth, ring gear teeth, fork stanchions |
| Flame harden | Torch heats the surface, then quench | Same idea as induction, cruder | Large gears, lathe ways |

**Quench media by alloy:**
- **Water or brine:** Plain carbon steels (1045, 1095). Fastest, highest risk of cracking.
- **Oil:** Alloy steels (4140, 4340, 8620 after carburizing, 52100, 5160). Slower, less distortion.
- **Polymer:** Water with added polymer; speed adjustable between water and oil.
- **Air:** Air-hardening tool steels (A2, D2) and some stainless grades.
- **Vacuum furnace with gas quench:** Bearings, tool steels and precision parts where surface decarburization is unacceptable.

### 2.5 Heat treatment of aluminum

Aluminum does not harden by quench alone. Heat treatable alloys (2xxx, 6xxx, 7xxx, cast A356/A357/319) use precipitation hardening.

1. **Solution treat:** Heat to just below melting of the alloy's eutectic (6061 about 530°C, 2024 about 495°C, 7075 about 470°C, A356 about 540°C). Hold until alloying elements dissolve.
2. **Quench:** Into water quickly, within seconds of leaving the furnace.
3. **Age:** Natural aging at room temperature gives T4. Artificial aging (6061 about 160-175°C for 8-18 hours, A356 about 155°C for 3-5 hours) gives T6, the high-strength condition.

**Welding warning for design:** Welding 6061-T6 drops the heat-affected zone to roughly annealed strength, losing a large share of its strength. Welded aluminum frames and swingarms must either be fully re-solution-treated and aged after welding or designed with thicker sections at the joints.

### 2.6 Work hardening and annealing of non-ferrous metals

Copper, brass, aluminum and stainless all get harder and more brittle as they are hammered, bent or drawn. Annealing resets them.

| Metal | Anneal temperature | Cooling | Notes |
|---|---|---|---|
| Copper | 400-650°C (dull red in dim light) | Water quench or air, both fine | Copper does not harden from quench. Water quench also knocks off scale. Used for crush washers, head gaskets, tubing before flaring |
| Brass | 425-600°C | Air or water | Season cracking can occur if stressed brass is left unannealed around ammonia |
| Aluminum (non-heat-treatable 1100, 3003, 5052) | About 340-415°C | Air | **Soot method:** coat the panel with acetylene soot from a rich oxy-acetylene flame, then heat with a neutral flame until the soot burns away. That signals annealing temperature. Classic panel beater technique. |
| Austenitic stainless (304) | 1010-1120°C | Rapid cool (water or forced air) | Slow cooling through 450-850°C causes sensitization and corrosion along grain boundaries |

**Hammer forming cycle:** Hammer or wheel until the metal starts to resist and spring back, anneal, repeat. Deep shapes (a motorcycle tank, a fender, a kettle body) may need three to ten cycles.

### 2.7 Joining

| Process | How it works | Best for |
|---|---|---|
| TIG (GTAW) | Tungsten electrode arc, separate filler rod, argon shield | Chromoly frames, aluminum, stainless, thin wall tube. Cleanest, most controlled |
| MIG (GMAW) | Wire feed electrode, gas shield | Body panels, brackets, exhaust, frames. Faster |
| Stick (SMAW) | Flux-coated rod | Heavy steel, repairs |
| Oxy-acetylene welding | Gas flame melts base and filler | Thin steel sheet, old-school bodywork, easy to hammer-weld after (weld bead stays soft) |
| Resistance spot welding | Two copper electrodes clamp sheets, current pulse melts a nugget | Car body assembly; a typical unibody has several thousand spot welds |
| Brazing | Filler metal (brass, bronze, silver alloy) melts above 450°C, base metal does not melt | Lugged bicycle and motorcycle frames, copper refrigeration lines, carbide tool tips |
| Soldering | Filler melts below 450°C | Copper-brass radiators, electrical connections |
| Vacuum brazing | Parts with filler placed in joints, heated in vacuum furnace; no flux needed because no oxygen is present | Aluminum radiators, refrigerator evaporators, heat exchangers, magnetron anodes, stainless assemblies |
| Controlled atmosphere brazing | Same idea in nitrogen with a non-corrosive flux | Most modern aluminum radiators and condensers |
| Electron beam welding | Focused electron beam in vacuum; very deep, narrow welds with tiny heat zone | Joining gear clusters to shafts in transmissions, turbocharger wheels to shafts, two-piece valves |
| Friction welding | One part spun against the other under force until the interface plastically fuses | Two-piece valves (heat-resistant head to hardenable stem), axle shaft flanges, driveshaft yokes |
| Diffusion bonding | Clean surfaces pressed together at high temperature in vacuum; atoms migrate across the joint | Titanium structures, layered heat exchangers |
| Cold welding (vacuum) | Perfectly clean, oxide-free metal surfaces touching in vacuum fuse with no heat | A curiosity in space hardware; impractical for vehicles but a magical printer could exploit it to join printed sections invisibly |
| Riveting | Mechanical fastening | Truck frames, chassis rails, clutch plates, brake linings on older designs |
| Shrink fit | Heat outer part, chill inner part (dry ice or liquid nitrogen), assemble, let temperatures equalize | Cylinder liners, valve seats, flywheel ring gears, bearing races |
| Press fit | Interference fit forced together with a press | Built-up crankshafts, bushings, bearing races |

### 2.8 Surface treatments

| Treatment | Purpose | Used on |
|---|---|---|
| Shot peening | Steel shot blasted at surface creates compressive stress that resists fatigue cracking | Connecting rods, springs, gear roots, crankshafts, axles |
| Fillet rolling | Rollers pressed into crankshaft fillets to cold work them | Crankshaft journal fillets |
| Thread rolling | Threads formed by rolling instead of cutting; rolled after heat treatment gives the best fatigue life | High-strength bolts and studs |
| Hard chrome plating | Hard, low-friction coating | Fork stanchions, shock shafts, valve stems, piston rings |
| Nikasil | Nickel plus silicon carbide plating | Aluminum cylinder bores with no liner |
| Anodizing | Thick aluminum oxide layer | Aluminum parts for corrosion and wear, piston ring lands |
| Phosphating (Parkerizing) | Zinc or manganese phosphate conversion coating holds oil | Camshafts, lifters, gears for break-in; steel parts under paint |
| Porcelain enamel | Glass frit fused onto steel or cast iron around 800-850°C | Oven cavities, stovetops, enameled cast iron cookware |
| Zinc galvanizing | Hot dip in molten zinc | Underbody steel, fasteners |
| E-coat | Electrically deposited primer | Entire car body before paint |

### 2.9 Printed metal post-processing chain (Tier B)

1. **Stress relief on the plate:** Before removing supports, or the part warps when released. Steels about 600-650°C, titanium about 650-700°C, aluminum about 300°C.
2. **Remove supports:** Wire EDM or bandsaw for metal supports.
3. **HIP (hot isostatic pressing):** Part sealed in a pressure vessel at high temperature and roughly 100 MPa argon pressure. Collapses internal porosity. Steels about 1100-1150°C, Ti-6Al-4V about 900-920°C, aluminum about 500°C. HIP is the single step that makes printed parts trustworthy in fatigue.
4. **Full heat treatment:** Normalize, harden, temper (steel) or solution and age (aluminum, titanium, nickel alloys).
5. **Machine functional surfaces:** Bores, journals, threads, mating faces.
6. **Shot peen:** Restores compressive surface stress and removes printed surface roughness.
7. **Inspect:** CT scan for internal voids, then hardness, dimensional and crack testing.
