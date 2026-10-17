# Building Metals: Steel, Aluminum and Others

> Earth reference / invent loot. Not locked law. Availability tags: `Metals.md`. Shop craft: `../Science/Metallurgy/CraftMetal.md`. Processing encyclopedia: `MaterialsProcessing.md`. Structural EE-EC ladder / concrete core: `BuildingMaterials.md`.

Nav: `Index.md`.

Deep production, metallurgy and strengthening for structural metals. Extracted from BuildingMaterials §§4–6 so the building EE ladder can stay thin and point here.

---

# 4. Steel and Iron

## 4.1 Atomic basis

Iron is a transition metal with metallic bonding: a lattice of positive ion cores in a sea of delocalized electrons. Bonding is non-directional, so atoms can slide past each other without breaking the material apart. This produces ductility.

Iron has two key crystal structures:
- **Ferrite (α-Fe)**: body-centered cubic (BCC), stable below 912°C; dissolves at most 0.022% carbon
- **Austenite (γ-Fe)**: face-centered cubic (FCC), stable from 912 to 1394°C; dissolves up to 2.14% carbon

The difference in carbon solubility between these phases is the basis of all steel heat treatment.

## 4.2 The iron-carbon system

- **Cementite (Fe₃C)**: hard, brittle iron carbide (6.67% C)
- **Eutectoid** at 0.76% C and 727°C: austenite transforms to **pearlite**, alternating lamellae of ferrite and cementite, a natural nanocomposite
- **Structural steels**: 0.05 to 0.25% C; microstructure of ferrite grains plus some pearlite
- **Cast iron**: 2 to 4% C; carbon present as graphite flakes (gray iron, brittle in tension) or spheres (ductile iron)
- **Martensite**: austenite quenched rapidly enough to suppress diffusion transforms by shear into body-centered tetragonal (BCT) iron supersaturated with carbon. Extremely hard, brittle. Tempering (reheating to 200 to 650°C) lets carbon precipitate as fine carbides, restoring toughness.

## 4.3 Strengthening mechanisms

Every method obstructs dislocation motion.

1. **Solid-solution strengthening**: Interstitial atoms (C, N) and substitutional atoms (Mn, Si, Cr, Ni) distort the lattice. Strain fields pin dislocations. Carbon in solution is extremely potent but limited by solubility in ferrite.

2. **Grain refinement (Hall-Petch)**: Grain boundaries block dislocation slip.
 σ_y = σ₀ + k_y·d^(-1/2)
 For low-carbon steel σ₀ ≈ 50 to 70 MPa and k_y ≈ 0.6 to 0.75 MPa·m^½. Reducing grain size from 50 µm to 5 µm raises yield by roughly 200 MPa. Grain refinement is unique because it raises strength and toughness simultaneously.

3. **Precipitation / dispersion strengthening**: Fine carbides and nitrides (NbC, VC, TiN) force dislocations to bow between them (Orowan mechanism):
 Δτ ≈ Gb / L (L = particle spacing). Microalloying additions of only 0.01 to 0.1% niobium, vanadium or titanium create high-strength low-alloy (HSLA) steels.

4. **Work hardening**: Plastic deformation multiplies dislocations; they tangle and obstruct each other.
 τ = αGb√ρ (Taylor relation, ρ = dislocation density, from ~10¹⁰ m⁻² annealed to ~10¹⁵ m⁻² heavily worked)
 Cold-drawn wire for prestressing strand reaches 1700 to 2000 MPa partly by this route.

5. **Phase transformation strengthening**: Pearlite, bainite and martensite microstructures.

### Processing routes for structural products
- **Thermomechanically controlled processing (TMCP)**: rolling at controlled temperatures so austenite recrystallizes into fine grains, then accelerated cooling. Produces fine-grained, weldable, tough plate without high carbon.
- **Tempcore / QST rebar**: hot-rolled bar is water-quenched so the surface transforms to martensite; heat from the still-hot core then tempers the surface. Result: hard tempered-martensite rim with a ductile ferrite-pearlite core, yield 500+ MPa without expensive alloys.

## 4.4 Properties

| Grade | Yield (MPa) | Ultimate (MPa) | Elongation |
|---|---|---|---|
| Mild steel S235 / A36 | 235-250 | 360-510 | 20-26% |
| Structural S355 / A992 | 345-355 | 450-630 | 18-22% |
| HSLA S460 | 460 | 540-720 | 17% |
| Rebar B500 / Grade 60 | 420-500 | 540-620 | 8-14% |
| Prestressing strand | 1600-1700 (0.1% proof) | 1770-1960 | 3.5% |
| High-strength bolts (Grade 10.9) | 900 | 1000 | 9% |

Common to all: E ≈ 200 to 210 GPa, density 7850 kg/m³, Poisson's ratio 0.3, thermal expansion ~12 × 10⁻⁶/K, fracture toughness 50 to 200 MPa·√m.

**Fatigue**: Steel has an endurance limit (around 40 to 50% of tensile strength for smooth specimens) below which it can sustain infinite cycles. Welds and notches lower this greatly.

**Brittle fracture**: BCC steels have a ductile-to-brittle transition temperature. Below it, cleavage fracture occurs with little energy absorption (Liberty ship failures 1940s). Modern specifications require Charpy impact energy at specified low temperatures.

**Fire**: Eurocode reduction factors for yield: about 0.78 at 500°C, 0.47 at 600°C, 0.23 at 700°C. Fire protection (intumescent paint, board, spray) keeps steel below about 550°C for the required period.

**Corrosion**: Iron spontaneously oxidizes in moist air. Protection: paint systems; hot-dip galvanizing (zinc corrodes sacrificially, 50 to 100 years in rural air); weathering steel (Cu, Cr, Ni, P additions form a dense adherent patina); stainless steel (see section 6).

## 4.5 Production routes and work to attain

### Route A: Blast furnace / basic oxygen furnace (BF-BOF), ~70% of world output

1. **Mining**: iron ore (hematite Fe₂O₃, magnetite Fe₃O₄) at 30 to 65% Fe. Roughly 1.5 to 1.7 t ore per t iron.
2. **Beneficiation**: crushing, grinding, magnetic separation, flotation to concentrate
3. **Agglomeration**: sintering (fusing fines with limestone on a moving grate at ~1300°C) or pelletizing (firing balls at ~1300°C)
4. **Cokemaking**: metallurgical coal heated to 1000 to 1100°C without air for 18 to 24 hours, driving off volatiles to leave strong porous carbon. Roughly 0.35 to 0.45 t coke per t hot metal.
5. **Blast furnace**: a counter-current reactor 30+ m tall. Hot air blast (1000 to 1250°C) burns coke at the tuyeres (raceway temperature 2000 to 2300°C), producing CO:
 C + O₂ → CO₂; CO₂ + C → 2CO (Boudouard reaction)
 Ore is reduced stepwise as it descends:
 3Fe₂O₃ + CO → 2Fe₃O₄ + CO₂
 Fe₃O₄ + CO → 3FeO + CO₂
 FeO + CO → Fe + CO₂
 Limestone flux forms slag with silica and alumina gangue. Product: hot metal (pig iron) at ~1500°C with 4 to 4.5% C.
6. **Basic oxygen furnace**: pure oxygen blown at supersonic speed onto molten iron plus 15 to 25% scrap. Carbon oxidizes to CO, removing it to under 0.1% in about 20 minutes. Reaction is exothermic enough that no external fuel is needed.
7. **Secondary (ladle) metallurgy**: deoxidation (Al, Si), desulfurization, alloying, vacuum degassing.
8. **Continuous casting** into slabs, blooms or billets.
9. **Hot rolling** into plate, sections (I-beams), bar; optional cold forming, galvanizing.

| BF-BOF metric | Value |
|---|---|
| Energy intensity | ~18-22 GJ/t crude steel |
| Thermodynamic minimum for Fe₂O₃ reduction | ~7 GJ/t Fe |
| CO₂ | ~2.0-2.3 t/t crude steel |

### Route B: Electric arc furnace (EAF), ~30% of world output
Graphite electrodes strike arcs (temperatures in the arc exceed 3000°C) to melt scrap and/or direct reduced iron. Energy ~350 to 500 kWh/t of electricity for scrap.

| EAF (scrap) metric | Value |
|---|---|
| Energy | ~6-10 GJ/t |
| CO₂ | ~0.3-0.7 t/t (dominated by grid electricity) |

### Route C: Direct reduction (DRI)
Iron ore pellets reduced as solids at 800 to 1050°C by natural gas reformed to CO and H₂, or by pure hydrogen:
Fe₂O₃ + 3H₂ → 2Fe + 3H₂O (endothermic, ΔH ≈ +96 kJ/mol)
Hydrogen-DRI-EAF with renewable electricity could cut emissions by 90%+. Requires roughly 50 to 55 kg of hydrogen per tonne of steel, or about 2.5 to 3.5 MWh of electricity per tonne including electrolysis. Several plants are under construction in Europe.

### Embodied values
| Product | EE (MJ/kg) | EC (kg CO₂e/kg) |
|---|---|---|
| Steel world average (~30-40% recycled content) | 20-25 | 1.8-2.0 |
| Primary (BF-BOF) sections | 25-35 | 2.2-2.8 |
| EAF scrap-based sections/rebar | 9-13 | 0.5-1.0 |
| Galvanized sheet | 25-40 | 2.5-3.0 |

Global crude steel output: about 1.9 billion tonnes per year. Steel accounts for roughly 7% of global CO₂ emissions.

## 4.6 Renewability: steel
- **Raw material**: Iron is about 5% of Earth's crust, fourth most abundant element. Economic reserves of ore last well over a century at current rates; resources far longer. Class A1.
- **Circularity**: Class C. Steel can be remelted indefinitely without loss of fundamental properties. Structural steel recovery rates from demolition exceed 85 to 95%; rebar recovery is lower (~70%) because it must be separated from concrete. One challenge: copper contamination from mixed scrap accumulates (copper cannot be removed by oxidation) and causes hot shortness above ~0.2 to 0.3% Cu.
- **Reuse**: Bolted steel sections can be reclaimed and reused directly after testing.
- **Limit on recycling**: Total demand exceeds available scrap because of growth and long building lifetimes (50 to 100 years), so primary steel will remain necessary for decades.

**Effort rating**: High. Multiple high-temperature stages, heavy mining. Scrap route is roughly one third the energy.

---


# 5. Aluminum

## 5.1 Atomic basis

FCC metallic crystal, density 2700 kg/m³ (about one third of steel). Pure aluminum is weak (yield ~30 MPa). Building alloys reach 150 to 500 MPa through precipitation hardening.

Aluminum oxidizes instantly in air to form a 2 to 5 nm amorphous Al₂O₃ film that is adherent, self-healing and impermeable. This passive film, not inherent nobility, gives aluminum its corrosion resistance. Anodizing thickens it electrochemically to 5 to 25 µm.

## 5.2 Precipitation hardening (age hardening)

Discovered by Alfred Wilm in 1906. Process:
1. **Solution treatment**: heat to ~530°C (6xxx series) to dissolve alloying elements into a single solid solution
2. **Quench**: rapid cooling traps them in a supersaturated solid solution (SSSS)
3. **Aging**: holding at 160 to 180°C (artificial aging, "T6") or room temperature ("T4") allows atoms to cluster into nanoscale precipitates

Sequence in 6xxx (Al-Mg-Si) alloys:
SSSS → solute clusters → GP zones → β'' (needle-shaped, coherent, ~4 × 4 × 50 nm, the main strengthener) → β' → β (Mg₂Si, equilibrium, coarse)

Peak strength occurs when β'' precipitates are dense and coherent, forcing dislocations to cut through them. Over-aging coarsens precipitates; dislocations then bypass them (Orowan looping) and strength drops.

| Alloy | Main elements | Yield (MPa) | UTS (MPa) | Use |
|---|---|---|---|---|
| 6063-T6 | Mg, Si | 215 | 240 | Window frames, curtain wall mullions |
| 6061-T6 | Mg, Si, Cu | 275 | 310 | Structural extrusions |
| 6082-T6 | Mg, Si, Mn | 260 | 310 | European structural |
| 5083-H116 | Mg (solid solution + work hardening) | 215 | 305 | Marine, welded |
| 7075-T6 | Zn, Mg, Cu | 500 | 570 | Aerospace; rarely in buildings (corrosion, weldability) |

E ≈ 69 to 72 GPa (one third of steel, so deflection often governs design). Thermal expansion ~23 × 10⁻⁶/K (twice steel). No fatigue endurance limit (eventually fails at any cyclic stress). Loses about half its strength by ~250 to 300°C, so fire performance is poor. Melts at ~600 to 660°C.

## 5.3 Production and work to attain

1. **Bauxite mining**: open-pit, mainly gibbsite Al(OH)₃ and boehmite AlO(OH). Roughly 4 to 5 t bauxite per t aluminum. Major producers: Australia, Guinea, China, Brazil.
2. **Bayer process**: bauxite digested in hot sodium hydroxide (140 to 240°C, pressurized):
 Al(OH)₃ + NaOH → NaAl(OH)₄
 Impurities (iron oxides, silica, titania) settle as **red mud**, roughly 1 to 1.5 t per t alumina, highly alkaline (pH 10 to 13) and stored in large tailings ponds (failures have caused disasters, e.g. Ajka, Hungary, 2010).
 Cooling and seeding precipitate Al(OH)₃, calcined at ~1000°C to alumina (Al₂O₃). About 2 t alumina per t aluminum.
3. **Hall-Héroult electrolysis**: alumina dissolved in molten cryolite (Na₃AlF₆) at 950 to 980°C. Carbon anodes, ~4 to 4.5 V per cell, 300 to 600 kA currents:
 2Al₂O₃ + 3C → 4Al + 3CO₂
 Electricity: 13 to 15 kWh per kg aluminum (best plants ~12.5). Thermodynamic minimum with consumable carbon anodes ~6.3 kWh/kg. Carbon anodes consumed ~0.4 to 0.45 t/t Al.
 Anode effects release perfluorocarbons (CF₄, C₂F₆) with global warming potentials of 6,500 to 12,000.
 Inert anode technology under development would release O₂ instead of CO₂.
4. **Casting, extrusion, rolling, heat treatment, anodizing or powder coating**

| Product | EE (MJ/kg) | EC (kg CO₂e/kg) |
|---|---|---|
| Primary, hydropower smelting | 130-160 | 4-6 |
| Primary, global average | 155-200 | 12-17 |
| Primary, coal-powered smelting | 180-220 | 16-20 |
| Recycled (secondary) | 8-30 | 0.5-1.5 |
| Typical extruded product (mixed content) | 50-150 | 4-10 |

Recycling uses about 5% of the energy of primary production. World primary production ~70 million t/yr; aluminum accounts for roughly 2% of global emissions.

## 5.4 Renewability
- Aluminum is the most abundant metal in Earth's crust (~8%), but economically extractable bauxite is Class A2 (reserves ~30 billion t, roughly a century at current rates; resources larger).
- Circularity Class C: recyclable indefinitely, though alloy mixing (different series in mixed scrap) leads to downcycling into casting alloys unless sorted.

**Effort rating**: Very high for primary metal (the most electricity-intensive common building material by mass). Low for recycled.

---


# 6. Other Metals

## 6.1 Stainless steel
Iron with at least 10.5% chromium. Chromium forms a 1 to 3 nm self-repairing Cr₂O₃ passive layer. Austenitic grades (304: 18% Cr, 8% Ni; 316: adds 2 to 3% Mo for chloride resistance) are FCC, non-magnetic, very ductile and tough at cryogenic temperatures. Duplex grades (22% Cr, 5% Ni, ferrite + austenite) have about twice the yield strength (~450 MPa).
- EE: 50 to 80 MJ/kg; EC: 4 to 7 kg CO₂e/kg (nickel and chromium mining and smelting are energy-intensive)
- Highly recyclable; scrap content typically 60 to 85%

## 6.2 Copper
FCC, very ductile, high electrical and thermal conductivity. Used for wiring, plumbing, roofing and cladding. Strengthened by cold working. Develops verdigris patina (basic copper carbonates and sulfates) that protects roofs for 100+ years.
- Ore grades now often 0.5 to 1% Cu, so mining moves huge rock volumes (roughly 100 to 200 t ore per t Cu)
- Smelting: concentrating, flash smelting to matte, converting, electrorefining
- EE: 40 to 60 MJ/kg primary; EC: 2.5 to 4 kg CO₂e/kg
- Class A2 (declining grades) and C (highly recyclable)

## 6.3 Zinc
Used as roofing, cladding and galvanizing coatings. Hexagonal close-packed; creeps under sustained load at room temperature. Protective patina of zinc hydroxycarbonate.
- EE: ~50 to 70 MJ/kg; EC: ~3 to 4 kg CO₂e/kg

## 6.4 Titanium
Hexagonal (α) and BCC (β) phases. Exceptional corrosion resistance (TiO₂ film), yield 250 to 1100 MPa depending on grade, density 4500 kg/m³. Used for prestige cladding (Guggenheim Bilbao). Kroll process (TiCl₄ reduced by magnesium in batch reactors) is extremely energy-intensive.
- EE: 360 to 750 MJ/kg; EC: 30 to 40+ kg CO₂e/kg

---

