# Printer Manufacturing: Motorcycle and Car

Design loot. Pack hub: `PrinterManufacturing.md`. Process: `PrinterManufacturingProcess.md`. Materials: `PrinterManufacturingMaterials.md`. Component ladder (lighter): `../Vehicle/MechanicalCarComponents.md`. Suspension / brakes / wheels: `../Vehicle/Index.md`.

## 4. Motorcycle

**Reference design:** 1960s-style air-cooled parallel twin or single, pushrod or single overhead cam, carbureted, points ignition or magneto, four or five-speed gearbox, chain final drive, telescopic forks, twin rear shocks. No semiconductors required if a magneto or points plus DC generator is used.

### 4.1 Engine

| Part | Material | Primary method | Heat treatment | Finish operations | Notes |
|---|---|---|---|---|---|
| Crankcase halves | A356 or 319 aluminum | Cast or print | T6 | Mill gasket faces flat; line bore main bearing housings with both halves bolted together; drill and tap; pressure test oil galleries | Print oil passages directly; a big Tier A/B advantage |
| Cylinder barrel | A356 with gray iron liner, or A356 with Nikasil bore | Cast barrel with fins; centrifugally cast liner | Barrel T6; liner stress relieved | Shrink fit liner (heat barrel to about 150-200°C, chill liner); bore and hone with 45° crosshatch; plateau hone | Fins can be printed thinner and deeper than any casting allows |
| Cylinder head | A356-T6 | Cast or print with ports | T6 | Mill deck flat; press in valve guides; shrink fit valve seat inserts; cut seats with 45° face plus 30° and 60° blend angles; lap valves | Port shapes can be printed to CFD-optimal geometry |
| Valve seat inserts | Sintered iron alloy or nickel alloy; beryllium copper for racing | Powder metal or print | Hardened as made | Shrink fit, then cut | Never use plain aluminum seat; it hammers out |
| Valve guides | Phosphor bronze, aluminum bronze or cast iron | Machined from bar | None | Press in, ream to size; intake clearance about 0.025-0.05 mm, exhaust about 0.04-0.07 mm | |
| Crankshaft (one-piece, twin) | 4340 or 4140 | **Must be forged** (or Tier B print + HIP) | Normalize, rough machine, quench and temper to about 28-34 HRC, then nitride or induction harden journals | Turn, grind journals to ±0.005 mm, fillet roll, dynamic balance, superfinish journals to Ra 0.1-0.2 µm | Never use a gray iron casting. Ductile iron only for low-output engines |
| Crankshaft (built-up, single or twin) | Flywheels: forged 1045 or 4140. Crankpin: 52100 or carburized 8620 | Forge flywheels, turn crankpin | Flywheels quench and temper; crankpin through-hardened or carburized | Press crankpin into flywheels with interference fit, then true the assembly on centers with a dial indicator and brass hammer | Allows one-piece rod with roller big-end bearing |
| Connecting rods | 4340 forged, or Ti-6Al-4V | **Must be forged** or printed + HIP | Quench and temper to about 32-38 HRC | Shot peen entire rod; machine big and small ends; press bronze bushing in small end and hone; balance end-to-end weight | Rod failure destroys the engine. Never cast |
| Rod bolts | 8740 or similar | Cold headed | Quench and temper | Threads rolled after heat treatment | Measure stretch, not just torque |
| Pistons | Forged 2618 or 4032; or cast hypereutectic A390 | Forge (performance) or cast | T6 or T61 | Machine ring grooves; cam-grind skirt oval; hone wrist pin bore; optional skirt coating and ring land anodizing | Forged piston-to-wall clearance about 0.08-0.13 mm per 100 mm bore; cast about 0.025-0.05 mm |
| Piston rings | Top: nitrided steel or ductile iron. Second: gray iron. Oil: three-piece steel | Ring material machined or cast into pots, then cut | Nitride or chrome face | Lap faces; file end gap to spec (top ring roughly 0.004 x bore diameter) | |
| Wrist pins | 8620 or 9310 | Turned from bar | Carburize, quench, temper | Grind to size, optional DLC coating | |
| Camshaft | Chilled gray iron, or 8620 bar | Chill cast (lobes against iron chills) or machine from bar | Chilled iron needs no further hardening; 8620 is carburized | Grind lobes on a cam grinder; phosphate coat for break-in | |
| Lifters / followers | Chilled iron or carburized steel | Cast or machine | Hardened faces | Grind face with slight crown | Lobe and lifter must be broken in together |
| Pushrods | 4130 or 4140 tube | Drawn tube | Hardened ends | Ball ends pressed or welded | |
| Rocker arms | Forged steel or investment-cast steel | Forge or cast | Harden contact pad | Grind pad radius; bushing pivot | |
| Valves (intake) | One-piece stainless or 21-4N | Upset forge | Solution treat and age | Grind stem, face and keeper grooves; chrome plate stem | |
| Valves (exhaust) | 21-4N head friction welded to hardenable stem | Upset forge head, friction weld to stem | Harden stem tip | Stellite hardface seat; grind | Exhaust valves run red hot |
| Valve springs | Chrome silicon wire | Cold coiled | Stress relieve, shot peen, preset (compressed solid to take initial set) | Check seat and open pressure on a spring tester | |
| Primary drive and gearbox gears | 8620 | Forge blanks | Carburize about 0.8-1.2 mm case at about 925°C, oil quench, temper 150-180°C | Hob or shape teeth before hardening; grind or hone teeth after; shot peen roots; surface 58-62 HRC, core 30-40 HRC | |
| Gearbox shafts | 8620 or 4140 | Turned bar | Carburize or induction harden | Hob or roll splines; grind bearing seats | |
| Shift drum and forks | Drum: steel or aluminum. Forks: forged steel | Machine drum; forge forks | Harden fork tips | Grind fork pad width | Bronze pads acceptable on fork tips |
| Clutch steel plates | 1050-1065 sheet | Stamped | Quench and temper, flatten | Surface grind flat | |
| Clutch friction plates | Steel or aluminum core plus bonded friction material (paper, cork, sintered bronze) | Stamped core, bonded lining | Cure bonding resin | Grind thickness | Friction material formulation is chemistry |
| Clutch basket | Cast or forged aluminum | Cast | T6 | Machine slots | Steel inserts in tang slots prevent notching |
| Bearings (all ball and roller) | 52100 | Rings: forge or ring roll. Balls: cold head from wire | Through-harden to 60-64 HRC in vacuum or protective atmosphere | Rings: turn, harden, grind, hone, superfinish. Balls: flash, rough grind, harden, fine grind, lap to grade 10 or better (sphericity within 0.25 µm) | The hardest precision job on the vehicle. Print cages in brass or pressed steel |
| Oil pump | Cast iron or aluminum body; sintered steel gerotor or gears | Cast body; machine gears | Harden gears | Mill end faces flat; side clearance about 0.025-0.075 mm | |
| Gaskets | Fiber composite, annealed copper, or printed elastomer | Cut or print | Anneal copper | | Copper head gaskets annealed before every reuse |
| Fasteners | 10B21, 4140 or 4340 | Cold headed | Quench and temper (grade 8 / 10.9 / 12.9) | Roll threads after heat treat | |
| Carburetor body | Zamak 3 or aluminum | Die cast or print | None | Machine bores and float bowl seat | |
| Carburetor jets and emulsion tubes | C360 brass | Turned on lathe | None | Drill calibrated orifices; ream; flow test | Orifice size controls mixture; precision matters more than material |
| Float needle | Brass with Viton tip | Turned | None | Lap seat | |
| Exhaust headers and mufflers | Mild steel or 304 stainless | Mandrel bent tube | Stress relieve stainless if heavily formed | TIG welded; chrome plate mild steel | Packing: fiberglass or steel wool |
| Spark plug | Alumina insulator, nickel alloy electrodes, steel shell, copper core | Press and sinter alumina at about 1600°C; cold form shell | | Glaze insulator; crimp and seal | Printer at Tier C could print the whole plug |
| Ignition coil | Silicon steel laminations, enameled copper wire | Stack laminations; wind primary (heavy wire, about 150-300 turns) and secondary (fine wire, about 15,000-30,000 turns) | Anneal laminations | Vacuum impregnate with varnish or epoxy | |
| Contact points | Tungsten contacts on steel arm | Braze tungsten onto arm | | Gap set by feeler gauge | |
| Condenser | Aluminum foil and paper or polyester film | Wound | | Sealed in can | |
| Magneto (alternative) | Permanent magnet rotor, laminated armature, coil, points | Machine and wind | | | Needs no battery to run |

### 4.2 Chassis

| Part | Material | Primary method | Heat treatment | Finish operations | Notes |
|---|---|---|---|---|---|
| Frame | 4130 chromoly tube | Cut and fishmouth tubes; TIG weld in a jig | Normalize optional on thin wall | Check alignment of steering head and swingarm pivot on a surface plate | 1950s alternative: mild steel tube with cast lugs, bronze brazed |
| Steering head | 4130 or 1020 tube | Machined | | Bore bearing cups after welding | Welding distorts; always machine after |
| Swingarm | 4130 tube or 6061 | Weld | 6061 must be re-solution-treated and aged after welding | Bore pivot after welding | |
| Fork stanchions | 4140 or 1045 tube | Drawn tube or gun-drilled bar | Induction harden surface | Grind, hard chrome plate, polish to Ra about 0.1 µm | Any scratch tears the seals |
| Fork lowers | A356-T6 | Cast | T6 | Hone bore; press in PTFE-coated bushings | |
| Triple clamps | 6061-T6 or 7075-T6 | Forge or machine from billet | T6 | Bore stanchion clamps; slit and drill pinch bolts | Steel forgings on vintage bikes |
| Fork and shock springs | 5160 or chrome silicon | Coiled | Quench and temper; preset | Grind ends flat | |
| Shock body and shaft | Steel body; hard chrome shaft | Drawn tube; ground shaft | Induction harden shaft | Spring steel shim stack valving; nitrogen charge | |
| Wheels (spoked) | Hub: cast aluminum or steel. Spokes: 304 stainless or galvanized steel wire. Rim: steel or 6061 | Spokes: cold head, bend, roll threads. Rim: roll extrusion into hoop, join, heat treat | Rim T6 | Lace and true on a truing stand to under 0.5 mm runout | |
| Wheels (cast) | A356 | Low-pressure cast | T6 | Machine bearing bores and rim seats; X-ray inspect; balance | |
| Brake rotors | 410 or 420 stainless | Laser or water jet cut from plate | Harden to about 32-38 HRC | Surface grind both faces parallel to under 0.01 mm | Car rotors are gray iron; motorcycle rotors are stainless for looks and corrosion |
| Brake drums (vintage) | Gray iron liner cast into aluminum or steel hub | Cast | | Turn braking surface | |
| Calipers | A356-T6 or forged 6061 | Cast or forge | T6 | Hone piston bores; machine seal grooves | |
| Brake pistons | Stainless or phenolic | Turned or molded | | Grind OD | |
| Brake pads | Sintered metallic or organic resin compound on steel backing plate | Pressed and sintered | | | Friction formulation is chemistry |
| Brake hoses | Rubber or PTFE with braided stainless | Extruded and braided | | Crimp fittings | |
| Axles | 4140 | Turned bar | Quench and temper | Grind bearing seats | |
| Drive chain | Plates: alloy steel. Pins: carburized steel. Rollers: carburized steel | Stamp plates; cold head pins; cut rollers from tube | Through-harden plates; carburize pins and rollers | Press fit pins and bushings; rivet master link; pre-stretch | O-ring chain adds rubber seals and grease |
| Sprockets | 1045 or 7075 | Machined or cut | Induction harden steel teeth | | |
| Fuel tank | Mild steel or aluminum sheet | Press stamp halves, or hammer form on English wheel and planishing hammer with anneal cycles | Anneal between forming stages | Seam weld or solder; slosh coat interior | |
| Fenders | Steel or aluminum sheet | Hammer form or stamp | Anneal | Roll edges; paint or chrome | |
| Tires | See section 5.6 | | | | |

## 5. Car

**Reference design:** 1960s rear-wheel-drive sedan with body on frame, cast iron inline-6 or V8, carburetor, points ignition, DC generator or alternator, 3 or 4-speed manual, solid rear axle, drum or front disc brakes. This avoids computers, airbags and semiconductor-heavy systems.

Engine internals follow the same rules as the motorcycle in section 4.1. Differences and additions are listed below.

### 5.1 Engine (car-specific)

| Part | Material | Primary method | Heat treatment | Finish operations | Notes |
|---|---|---|---|---|---|
| Engine block | Gray iron class 30-40 | Sand cast with resin sand cores for water jackets and oil galleries | Stress relieve or age (about 550°C) before machining | Mill deck and pan rails; line bore mains and cam tunnel with caps installed; bore and torque-plate hone cylinders; deburr and wash every gallery | The largest casting in the car. Printing it removes core shift, the main source of thin walls |
| Main bearing caps | Ductile iron or billet 1045 / 4140 | Cast or machine | | Machined with block as a set; numbered and never swapped | |
| Cylinder heads | Gray iron or A356-T6 | Sand or permanent mold cast | Aluminum T6 | Same as motorcycle head | Aluminum heads need hardened seats and bronze guides |
| Crankshaft | Ductile iron (stock), forged 1053 or 4340 (performance) | Cast or forge | Quench and temper forged; ductile iron as cast or austempered | Grind, fillet roll, nitride or induction harden journals, balance | Main bearing clearance roughly 0.025 mm per 25 mm of journal diameter |
| Plain bearings (mains and rods) | Steel backing with babbitt or copper-lead or aluminum-tin overlay | Roll bond lining to steel strip, stamp, form | | Bore to wall thickness tolerance; check crush height | Vintage: poured babbitt directly into rod and block, then line bored |
| Timing gears / chain | Gears: cast iron, steel or fiber. Chain: roller chain like section 4.2 | Hob gears | Harden steel gears | | |
| Flywheel | Gray iron or billet steel | Cast or machine | | Turn friction face; balance with crank | |
| Starter ring gear | 1045 | Machine teeth | Induction harden teeth | Shrink fit onto flywheel after heating ring to about 200°C | |
| Harmonic balancer | Cast iron hub and inertia ring bonded with rubber | Cast and machine, bond elastomer | | Balance | |
| Water pump | Cast iron or aluminum housing; cast iron or stamped steel impeller | Cast | | Machine seal and bearing bores; ceramic and carbon face seal | |
| Radiator (vintage) | Brass tubes, copper fins, brass tanks | Form tubes; stamp fins; assemble core | | Dip solder entire core with lead-tin solder; pressure test | |
| Radiator (modern) | 3003 aluminum clad with 4343 braze alloy | Form tubes, fins, headers | | Controlled atmosphere or vacuum braze whole assembly at about 600°C in one pass; plastic tanks crimped on | |
| Thermostat | Brass and wax pellet | Stamp and assemble | | | |
| Intake manifold | Gray iron or aluminum | Cast or print | Aluminum T6 optional | Mill flanges flat | Non-critical strength part. Print as-is |
| Exhaust manifold | High silicon molybdenum ductile iron or gray iron | Cast | Stress relieve | Mill flanges flat | |
| Oil pan, valve covers | Stamped steel or cast aluminum | Stamp or cast | | | Non-critical. Print as-is |
| Fuel pump (mechanical) | Die cast body; rubber diaphragm; steel arm | Cast and stamp | Harden lever contact | | |
| Distributor | Die cast housing; steel shaft; bakelite cap and rotor | Cast and machine | Harden shaft cam | | |
| Generator / alternator | Silicon steel laminations; copper windings; steel shaft; carbon brushes | Stack and wind | Anneal laminations | Varnish impregnate; turn commutator (generator) | Alternator needs diodes (semiconductors). DC generator with mechanical voltage regulator avoids them |
| Starter motor | Same construction as generator; Bendix drive pinion | Wind and machine | Harden pinion | | |

### 5.2 Drivetrain

| Part | Material | Primary method | Heat treatment | Finish operations | Notes |
|---|---|---|---|---|---|
| Clutch disc | Steel hub and plate; torsion springs; riveted friction facings | Stamp, rivet | Harden springs | True runout | |
| Pressure plate | Gray iron ring; stamped steel cover; diaphragm spring of 5160 class steel | Cast ring; stamp cover; form spring | Quench and temper spring | Grind friction face | |
| Transmission case | Gray iron or aluminum | Cast | Aluminum T6 if heat treatable alloy | Line bore shaft bearing bores; mill faces | |
| Transmission gears | 8620 | Forge blanks | Carburize, quench, temper | Hob, shave, harden, grind or hone; shot peen | Some gear clusters are electron beam welded to their shafts |
| Synchronizer rings | Manganese bronze or brass, molybdenum sprayed steel | Forge or cast | | Machine internal cone threads | |
| Driveshaft | DOM 1020-1026 tube | Cut tube | | Weld yokes; balance at operating speed | |
| U-joints | 8620 cross; 52100 needle bearings | Forge cross | Carburize | Grind trunnions | |
| Rear axle housing | Stamped steel halves welded, or cast ductile iron center | Stamp and weld | Stress relieve | Machine bearing seats and carrier mounting face; check tube straightness | |
| Ring and pinion | 8620 | Forge blanks | Carburize, quench, temper | Cut hypoid teeth; harden; lap as a matched pair and keep together | |
| Differential carrier and spider gears | Ductile iron carrier; 8620 gears | Cast carrier; forge gears | Carburize gears | | |
| Axle shafts | 1541 or 4340 | Forge flange end (upset) or friction weld flange | Induction harden along length | Grind bearing seat; roll splines | |
| Wheel bearings | Tapered roller, 52100 or carburized steel | As section 4.1 bearings | | | |

### 5.3 Suspension and steering

| Part | Material | Primary method | Heat treatment | Finish operations | Notes |
|---|---|---|---|---|---|
| Frame rails | 1020 or HSLA steel | Stamped C-channel or boxed sections | | Rivet or weld crossmembers; check diagonals for square | |
| Control arms | Stamped steel (welded halves) or forged 1045 | Stamp and weld, or forge | Forged arms quench and temper | Bore bushing and ball joint seats | Forged or printed + HIP for any racing use |
| Ball joints | Ball stud: 4140 or 8620. Housing: forged steel | Forge and machine | Carburize or induction harden ball | Grind ball spherical; assemble with bearing seat | Ball joint failure drops the corner of the car |
| Steering knuckles / spindles | Forged 1045 / 4140 or cast ductile iron | **Forge** (preferred) | Quench and temper; induction harden spindle bearing surface | Grind bearing seats; machine kingpin or ball joint taper | Safety critical. Magnetic particle inspect every one |
| Coil springs | 5160 or 9254 | Hot coil heavy wire at about 900°C, or cold coil lighter wire | Quench and temper (hot coiled) or stress relieve (cold coiled) | Shot peen; preset | |
| Leaf springs | 5160 flat bar | Taper roll ends; hot form arc | Oil quench, temper to about 44-48 HRC | Shot peen tension side; assemble with center bolt and clips | |
| Sway bar | 1045 or 5160 bar | Hot bend | Quench and temper | | |
| Shock absorbers | Steel tubes; hard chrome rod; steel shim valves; hydraulic oil | Drawn tube; ground rod | | Weld, fill, crimp seal | |
| Steering box (recirculating ball) | Housing: ductile or gray iron. Worm and sector: 8620 | Cast housing; machine worm | Carburize worm and sector | Grind worm groove; select balls for preload | |
| Tie rods and drag link | 1045 or 4140 | Forge ends; thread tube | Quench and temper | Roll threads | |
| Steering wheel | Steel armature; plastic or wood rim | Weld armature; mold rim | | | |

### 5.4 Brakes

| Part | Material | Method | Finish | Notes |
|---|---|---|---|---|
| Rotors | High-carbon gray iron (G3000 class) | Cast with internal vanes | Turn both faces parallel; balance | Gray iron chosen for heat capacity and damping |
| Drums | Gray iron or gray iron cast into steel shell | Cast | Turn braking surface | |
| Calipers | Ductile iron or aluminum | Cast | Hone bores | |
| Master cylinder | Gray iron or aluminum | Cast | Hone bore; anodize aluminum bore | |
| Wheel cylinders | Gray iron | Cast | Hone | |
| Brake lines | Copper-nickel or coated steel tube | Drawn tube | Double flare ends | Annealed copper-nickel flares easily |
| Shoes and pads | Steel backing plus friction material | Stamp backing; bond or rivet lining | Grind lining to arc | |

### 5.5 Body and glass

| Part | Material | Primary method | Heat and finishing | Notes |
|---|---|---|---|
| Body panels | Drawing-quality low-carbon steel (or aluminum 5xxx/6xxx) | Press stamping with dies, or hand form on English wheel, planishing hammer, shrinker-stretcher | Anneal aluminum with the soot method between forming stages; steel rarely needs it for hand forming but does after heavy stretching | Printer is better used to print the stamping dies (cast iron or tool steel) than the thin panels themselves |
| Stamping dies | Gray iron, ductile iron or tool steel | Cast or print | Flame or induction harden die edges; vacuum harden tool steel inserts | Machine and hand-polish die surfaces |
| Body structure | Low-carbon steel sheet | Stamp | Resistance spot weld in fixtures | |
| Hinges, latches, strikers | Forged or stamped steel | Forge or stamp | Case harden wear points | |
| Corrosion protection | | Zinc phosphate dip, e-coat primer, seam sealer, primer surfacer, base and clear coat | Bake each coat | |
| Windshield | Two layers of annealed soda-lime glass with PVB interlayer | Float glass, cut, sag-bend pair together at about 600°C | Laminate in autoclave at about 140°C and roughly 12 bar | Laminated so it cracks without shattering |
| Side and rear glass | Soda-lime | Float glass, cut, edge grind, bend | Temper: heat to about 620°C, blast both faces with air | Shatters into small cubes |
| Seats | Steel frame, coil or zigzag springs, foam, upholstery | Weld frame; form springs | Heat treat springs | Foam is polyurethane chemistry |

### 5.6 Tires

| Component | Material |
|---|---|
| Tread | SBR and natural rubber blend, carbon black, silica, sulfur, zinc oxide, stearic acid, accelerators, process oil |
| Sidewall | Natural rubber blend with antiozonants |
| Body plies | Nylon, polyester or rayon cord coated in rubber |
| Belts (radial) | Brass-plated high-carbon steel cord |
| Bead | Bronze-coated high-carbon steel wire bundle |
| Inner liner or tube | Butyl rubber |

**Process:**
1. Mix compound in internal mixer (Banbury); sulfur and accelerators added last at low temperature.
2. Calender cords into rubber sheets; extrude tread and sidewall profiles.
3. Build green tire on a drum layer by layer.
4. Cure in a heated mold with an internal pressurized bladder, roughly 150-180°C for 10-15 minutes for passenger tires. Vulcanization crosslinks the rubber.

**Printer note:** A Tier A/B printer can print the uncured green tire and the cure mold. Curing still needs the press. A Tier C printer can print cured rubber directly. Bias-ply tires are simpler than radials for a first build.

### 5.7 Electrical

| Part | Construction |
|---|---|
| Wiring | Stranded annealed copper with PVC or cloth insulation |
| Battery (lead-acid) | Lead-calcium or lead-antimony grids, lead dioxide positive paste, sponge lead negative paste, separators, sulfuric acid electrolyte around 1.26-1.28 specific gravity, polypropylene or hard rubber case. Requires forming charge after filling |
| Lights | Tungsten filament in glass bulb filled with inert gas; sealed-beam headlights fuse lens, reflector and filament into one glass unit |
| Gauges | Bimetal or magnetic needle movements; mechanical speedometer driven by cable from transmission |
| Fuses | Glass tube with calibrated wire element |
| Voltage regulator | Electromechanical relay type for DC generator (no semiconductors) |
| Horn | Electromagnet vibrating a steel diaphragm |

### 5.8 Fluids and consumables (not printable as solid parts)

| Fluid | Source |
|---|---|
| Gasoline | Crude oil distillation and refining |
| Motor oil, gear oil | Refined base oil plus additive package |
| Grease | Base oil thickened with lithium soap |
| Brake fluid | Glycol ether (DOT 3/4) |
| Coolant | Ethylene glycol plus water plus corrosion inhibitors |
| Refrigerant (A/C, fridges) | R134a, R1234yf or R600a isobutane |

### 5.9 Modern systems (optional)

ECUs, fuel injectors with electronic control, ABS, sensors and alternator diodes all require semiconductor fabrication: ultra-pure silicon, doping, photolithography at micron or nanometer scale. Only a Tier C printer with atomic precision can print chips directly. Airbag inflators are energetic devices and are left out of this guide. A vintage build skips every one of these.
