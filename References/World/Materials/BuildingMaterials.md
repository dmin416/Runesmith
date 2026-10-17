# Building Materials: Strength Mechanisms, Science, Renewability and Production Effort

> Earth reference / invent loot. Not locked law. Metals tags: Metals.md. Glass / clear panes: TranslucentMaterials.md. Glass fracture / temper / making: GlassScience.md. Insulation ladder: InsulationMaterials.md. Sheer / cover / heat under cloth: SheerMaterials.md. Purification / kiln energy: MaterialPurification.md, AtomizationEnergy.md. Timber biomaterials: ../Science/Biomaterials/. Farm construction (barns, sheds, silos, farmstead sequence): ../Science/Invent/FarmBuildings.md. Floating / pontoon bridges (buoyancy, pontoon materials, construction): ../Science/Invent/FloatingBridges.md. Caldris build tech filter: ../Tech/Technology.md. Exterior wear and climate spoil: WeatheringWear.md pack. Curing, recycling and crack repair: ConcreteCuringRecycling.md. Cleanable / sanitary surfaces and fixtures: CleanableSurfaces.md.

Nav: Index.md.

A technical comparison of every major structural and enclosure material: what holds it together at the atomic and microstructural scale, how its strength is developed and measured, what it costs in energy and carbon to make, how renewable its raw materials are and how much physical work stands between the raw resource and a finished building element. Concrete receives the deepest treatment.

All figures are typical ranges. Embodied energy (EE) and embodied carbon (EC) values are cradle-to-gate unless stated, drawn from the general range of the Inventory of Carbon and Energy (ICE, University of Bath / Circular Ecology), worldsteel, the International Aluminium Institute, GCCA, IEA and the USDA Wood Handbook. Values vary by region, fuel mix and plant technology by a factor of 2 or more.

---

## Contents

1. Foundations: how any material resists load
2. Concrete (full treatment)
3. Lime, ancient binders and cement alternatives
4. Steel and iron
5. Aluminum
6. Other metals: stainless steel, copper, zinc, titanium
7. Timber and engineered wood
8. Bamboo
9. Natural stone
10. Fired clay brick and ceramics
11. Earth construction: adobe, rammed earth, cob, CEB
12. Gypsum
13. Glass
14. Polymers and foam insulation
15. Fiber-reinforced polymers and basalt fiber
16. Bio-based and rapidly renewable materials
17. Emerging and experimental materials
18. Master comparison tables
19. Synthesis

---

# 1. Foundations: How Any Material Resists Load

## 1.1 Stress, strain and stiffness

- **Stress (σ)** = force / area, in pascals (1 MPa = 1 N/mm² ≈ 145 psi).
- **Strain (ε)** = change in length / original length (dimensionless).
- **Young's modulus (E)** = σ/ε in the linear elastic region. It measures stiffness, not strength. Stiffness comes directly from the curvature of the interatomic potential energy well: E ≈ (1/r₀)(d²U/dr²) at the equilibrium spacing r₀. Steeper wells (covalent, ionic) give stiffer materials; shallow wells (van der Waals between polymer chains) give compliant ones.
- **Yield strength** = stress at which permanent (plastic) deformation begins. Only meaningful for ductile materials (metals, some polymers, wood in compression).
- **Ultimate strength** = maximum stress before failure.
- **Compressive vs tensile strength**: brittle materials (concrete, stone, brick, glass) are typically 8 to 15 times stronger in compression than tension because compression closes cracks while tension opens them.

## 1.2 Bond types and what they mean for buildings

| Bond type | Typical energy (kJ/mol) | Where it dominates | Consequence |
|---|---|---|---|
| Covalent | 150-1000 | Silicate networks in glass, C-S-H chains, cellulose backbone, carbon fiber | Very stiff, very strong in theory, brittle in practice |
| Ionic | 600-4000 (lattice) | Calcite, gypsum, clay minerals, oxides | Stiff, brittle, often water-sensitive |
| Metallic | 100-850 | Steel, aluminum, copper | Non-directional; atoms slide via dislocations, giving ductility |
| Hydrogen bonds | 10-40 | Between cellulose chains, in clay-water systems, in C-S-H interlayer water | Moderate; moisture-sensitive |
| Van der Waals | 0.5-10 | Between polymer chains, between C-S-H particles, between clay platelets | Weak individually, strong collectively across huge surface areas |

## 1.3 Theoretical vs real strength: why flaws rule everything

The theoretical cohesive strength of a perfect solid is approximately E/10. For glass (E ≈ 70 GPa) this predicts about 7 GPa. Real window glass breaks at 30 to 100 MPa, roughly 1/100 of theory. The gap is explained by flaws.

**Griffith criterion (1921)** for brittle fracture:

σ_f = √(2Eγ / πa)

where γ is surface energy and a is the half-length of the critical crack. Strength falls with the square root of flaw size. A 1 µm surface scratch on glass is enough to cut strength by two orders of magnitude.

**Fracture toughness (K_IC)** generalizes this: a crack grows when the stress intensity K = Yσ√(πa) reaches K_IC.

| Material | K_IC (MPa·√m) |
|---|---|
| Glass | 0.7-0.8 |
| Cement paste | 0.2-0.5 |
| Concrete | 0.5-1.5 |
| Granite | 1-2 |
| Wood (across grain, crack along grain) | 0.5-1 |
| Wood (crack across grain) | 5-15 |
| Aluminum alloys | 20-45 |
| Structural steel | 50-200 |

The 100-fold difference between concrete and steel explains why concrete needs reinforcement and why steel buildings deform visibly before collapse while unreinforced masonry and glass fail suddenly.

**For metals**, the theoretical shear strength is about G/10 (several GPa for iron). Real mild steel yields at around 250 MPa because dislocations (line defects in the crystal lattice) let planes of atoms slip one row at a time instead of all at once. Almost all metal strengthening is the science of obstructing dislocation motion.

## 1.4 Specific properties

For structures that must carry their own weight (long spans, tall buildings, transport) the relevant figures are strength/density (specific strength) and stiffness/density (specific stiffness). A remarkable fact: steel, aluminum, wood (along the grain) and glass all have nearly the same specific stiffness, about 25 to 28 MJ/kg (E/ρ in MPa per kg/m³ × 1000). Nature and metallurgy converge on the same limit for common bonds. Only carbon and certain ceramic fibers break far past it.

## 1.5 Defining embodied energy and carbon

- **Embodied energy (EE)**: total primary energy consumed to extract, process and manufacture a material up to the factory gate (MJ/kg).
- **Embodied carbon (EC)**: total greenhouse gas emissions over the same boundary (kg CO₂e/kg). Includes fuel combustion and **process emissions** (chemical CO₂ released by the reactions themselves, which no change of fuel can eliminate).
- **Biogenic carbon**: CO₂ absorbed by plants during growth and stored in wood, bamboo, straw or hemp. Accounted separately because it returns to the atmosphere if the material burns or rots.

## 1.6 Defining renewability

Used throughout this document:

| Class | Meaning | Examples |
|---|---|---|
| R1 Rapidly renewable | Regrows in under 10 years | Bamboo, straw, hemp, cork, reed |
| R2 Renewable | Regrows in 10 to 100 years | Timber |
| A1 Abundant non-renewable | Geological stock so large that depletion is not a practical constraint | Limestone, clay, most stone, iron ore, silica |
| A2 Locally limited | Global stock large but usable grades or accessible deposits limited | Construction sand, gravel, high-grade bauxite, gypsum (natural) |
| F Fossil-derived | Made from oil, gas or coal | Plastics, foam insulation, bitumen, resin matrices |
| C Circular | Recyclable into the same grade repeatedly | Steel, aluminum, copper, (partially) glass |

---

# 2. Concrete

Concrete is the most-used manufactured substance on Earth, at roughly 25 to 30 billion tonnes per year, second only to water in total human consumption. It is a composite of a binder (cement paste) and inert fillers (aggregates). Its strength comes almost entirely from a chemical reaction between cement and water that grows an interlocking nanoscale gel inside the voids between sand and stone.

## 2.1 Typical composition

Per cubic meter of ordinary 30 MPa structural concrete:

| Component | Mass (kg) | Volume fraction | Role |
|---|---|---|---|
| Portland cement | 300-380 | ~10-12% | Reactive binder |
| Water | 160-190 | ~16-19% | Reactant and workability |
| Fine aggregate (sand) | 700-850 | ~26-30% | Fills voids between stone; reduces paste demand |
| Coarse aggregate (gravel/crushed rock, 10-20 mm) | 1000-1150 | ~38-42% | Skeleton, stiffness, dimensional stability, low cost |
| Entrapped/entrained air | n/a | 1-8% | Freeze-thaw resistance (if entrained) |
| Admixtures | 1-5 L | <1% | Flow, set time, durability |
| Supplementary cementitious materials (SCMs) | 0-200 (replacing cement) | variable | Strength, durability, lower carbon |

Aggregates make up 60 to 75% of the volume. They are not merely filler: they carry a large share of load, resist shrinkage and creep (paste alone shrinks several times more than concrete) and set the elastic modulus.

## 2.2 Making Portland cement: the chain of work

### Step 1: Quarrying
Limestone (CaCO₃) supplies calcium. Clay or shale supplies silica (SiO₂), alumina (Al₂O₃) and iron oxide (Fe₂O₃). Corrective materials (sand, iron ore, bauxite) adjust chemistry. Roughly 1.5 to 1.7 tonnes of raw material are needed per tonne of clinker because the limestone loses about 44% of its mass as CO₂.

Work involved: drilling, blasting, hauling with 50 to 100 tonne trucks, primary crushing to under 100 mm.

### Step 2: Raw meal preparation
Materials are proportioned by online X-ray analysis, then ground in vertical roller mills to a powder with about 10 to 15% retained on a 90 µm sieve. Target chemistry is described by three moduli:

- Lime saturation factor LSF = CaO / (2.8 SiO₂ + 1.2 Al₂O₃ + 0.65 Fe₂O₃), target 0.92 to 0.98
- Silica modulus SM = SiO₂ / (Al₂O₃ + Fe₂O₃), target 2.0 to 3.0
- Alumina modulus AM = Al₂O₃ / Fe₂O₃, target 1.0 to 4.0

### Step 3: Preheating and calcination
Raw meal falls through a 4 to 6 stage cyclone preheater tower against rising kiln gas. In the precalciner (a dedicated combustion chamber burning up to 60% of total fuel) the limestone decomposes:

CaCO₃ → CaO + CO₂  ΔH ≈ +178 kJ/mol (about 1.78 MJ per kg of CaCO₃)

This reaction runs to 90 to 95% completion at 850 to 900°C before material enters the kiln. **This is the irreducible process emission.** Clinker contains about 65% CaO. Each tonne of CaO from limestone releases 44/56 = 0.786 t CO₂, giving roughly 0.51 t CO₂ per tonne of clinker from chemistry alone, regardless of fuel.

### Step 4: Clinkering in the rotary kiln
A steel tube 3.5 to 6 m in diameter and 50 to 100 m long, lined with refractory brick, inclined 3 to 4% and rotating 3 to 5 rpm. A flame at the discharge end reaches about 2000°C; material reaches 1400 to 1500°C. Around 20 to 30% of the charge melts into an aluminoferrite liquid that acts as a flux, allowing solid-state reactions to proceed rapidly:

- 2CaO + SiO₂ → Ca₂SiO₄ (belite, C₂S) at 1100 to 1200°C
- Ca₂SiO₄ + CaO → Ca₃SiO₅ (alite, C₃S) above about 1250°C, mostly in the liquid-assisted zone near 1450°C
- 3CaO + Al₂O₃ → Ca₃Al₂O₆ (C₃A) and 4CaO + Al₂O₃ + Fe₂O₃ → Ca₄Al₂Fe₂O₁₀ (C₄AF) crystallize from the melt on cooling

Product: dark gray nodules 3 to 25 mm called clinker.

### Step 5: Cooling
Grate coolers quench clinker from about 1400°C to under 100°C in minutes. Fast cooling freezes alite in its reactive form (alite is metastable below 1250°C and would decompose to belite and free lime if cooled slowly) and keeps C₃A finely crystalline. Hot cooler air is recycled as combustion air.

### Step 6: Finish grinding
Clinker plus 3 to 5% gypsum (CaSO₄·2H₂O) is ground in ball mills or roller presses to a specific surface (Blaine) of 300 to 450 m²/kg for ordinary cement and up to 600 m²/kg for rapid-hardening grades. Median particle size about 10 to 15 µm. Grinding is the largest electrical load in a cement plant.

Gypsum is essential: without it, C₃A reacts with water almost instantly ("flash set") and the paste stiffens in minutes.

### Energy accounting
| Item | Typical value |
|---|---|
| Theoretical heat of clinker formation (net) | ~1.75 GJ/t clinker |
| Modern dry-process kiln with preheater and precalciner | 3.0-3.5 GJ/t clinker thermal |
| Old wet-process kilns | 5-6+ GJ/t clinker |
| Electricity | 90-120 kWh/t cement |
| Total CO₂ per tonne clinker | ~0.82-0.90 t (about 60% process, 40% fuel) |
| CO₂ per tonne Portland cement CEM I (95% clinker) | ~0.85-0.95 t |
| CO₂ per tonne global average cement (with SCMs/fillers) | ~0.55-0.65 t |

World cement output is about 4 billion tonnes per year, roughly half in China. Cement accounts for about 7 to 8% of global anthropogenic CO₂ emissions.

## 2.3 Clinker phases (cement chemist notation)

Cement chemists abbreviate oxides: C = CaO, S = SiO₂, A = Al₂O₃, F = Fe₂O₃, H = H₂O, S̄ = SO₃.

| Phase | Mineral | Mass % in OPC | Hydration rate | Heat of hydration (J/g) | Contribution |
|---|---|---|---|---|---|
| C₃S | Alite | 50-70 | Fast (hours to days) | ~500 | Most early strength (1-28 days) |
| C₂S | Belite | 15-30 | Slow (weeks to years) | ~260 | Long-term strength gain |
| C₃A | Aluminate | 5-10 | Very fast (minutes) | ~870 (with gypsum) | Early stiffening; sulfate vulnerability |
| C₄AF | Ferrite | 5-15 | Moderate | ~420 | Little strength; gives gray color |

Total heat of hydration for ordinary Portland cement: about 400 to 500 J/g at full hydration.

## 2.4 Hydration chemistry: where strength is born

Cement does not "dry" to gain strength. It reacts chemically with water. Concrete cured underwater gains strength normally. Drying actually halts the reaction.

### Silicate reactions (the strength reactions)

2C₃S + 6H → C₃S₂H₃ + 3CH
2C₂S + 4H → C₃S₂H₃ + CH

In ordinary chemistry: 2Ca₃SiO₅ + 6H₂O → 3CaO·2SiO₂·3H₂O + 3Ca(OH)₂

The products:
- **C-S-H (calcium silicate hydrate)**: the glue. Written with hyphens because its composition is variable (Ca/Si molar ratio typically 1.5 to 2.0 in Portland systems, water content variable). It forms 50 to 60% of the solid volume of hydrated paste.
- **CH (calcium hydroxide, portlandite)**: 20 to 25% of solid volume. Large hexagonal crystals. Contributes little to strength but buffers pore solution to pH 12.5 to 13.5, which protects steel reinforcement.

By mass, C₃S hydration yields about 61% C-S-H and 39% CH. C₂S yields about 82% C-S-H and 18% CH. Belite-rich cements are therefore ultimately stronger and more durable per unit of CH, but slower.

### Aluminate reactions (set control)

With gypsum present:
C₃A + 3CS̄H₂ + 26H → C₆AS̄₃H₃₂ (ettringite, needle-like crystals)

Ettringite coats C₃A grains and slows their reaction. When gypsum is exhausted (typically within 12 to 36 hours) ettringite converts:

2C₃A + C₆AS̄₃H₃₂ + 4H → 3C₄AS̄H₁₂ (monosulfoaluminate, "AFm")

If sulfate later enters from soil or seawater, monosulfate can convert back to ettringite with a large volume increase. That is the basis of external sulfate attack.

### The five stages of hydration (measured by isothermal calorimetry)

1. **Initial reaction (0 to 15 min)**: rapid dissolution of ions; C₃A reacts with gypsum; sharp heat spike.
2. **Induction / dormant period (15 min to 2-4 h)**: heat output falls to near zero. Concrete remains workable. Leading explanation: dissolution of C₃S slows dramatically as the pore solution approaches saturation with respect to C₃S surfaces (geochemical dissolution-rate theory), with possible contribution from a thin protective layer. This window is what makes mixing, transport and placement possible.
3. **Acceleration (2-4 h to 8-12 h)**: C-S-H nucleates and grows rapidly on grain surfaces. Initial set then final set occur. Main heat peak.
4. **Deceleration (12-24 h onward)**: growing hydration shells and filled pore space slow the reaction to diffusion control.
5. **Steady state (days to years)**: slow continued hydration; belite contributes most of the late strength. Hydration may continue for decades if moisture is available.

## 2.5 The nanostructure of C-S-H: why it holds

C-S-H is the strength-giving phase and one of the most studied materials in civil engineering.

### Layered structure
At the molecular level C-S-H resembles defective versions of the natural minerals tobermorite (Ca/Si ~0.83) and jennite (Ca/Si ~1.5). It consists of:
- Central calcium oxide sheets
- Silicate chains attached on both sides in a repeating three-tetrahedra "dreierketten" pattern, with many bridging tetrahedra missing at the high Ca/Si ratios of Portland cement, so chains are short (average 2 to 5 tetrahedra)
- An interlayer containing water molecules and additional calcium ions

### Colloidal structure
At the 2 to 5 nm scale C-S-H forms tiny solid particles ("globules" in the Jennings colloid model). These pack into two morphologies:
- **Low-density (LD) C-S-H**, packing fraction about 0.64 (close to random loose packing), formed early in open space ("outer product")
- **High-density (HD) C-S-H**, packing fraction about 0.74 (close to ordered packing), formed later inside the original cement grain boundary ("inner product")

Nanoindentation (Constantinides and Ulm) measures LD C-S-H at E ≈ 18 to 21 GPa and HD C-S-H at E ≈ 29 to 32 GPa. These packing values match granular physics limits, indicating C-S-H mechanical behavior is governed by particle packing, not by a continuous crystal.

### What holds the particles together
C-S-H particle surfaces are negatively charged (deprotonated silanol groups, Si-O⁻). Calcium ions (Ca²⁺) in the thin water films between particles produce **ion-correlation forces**: fluctuations in the arrangement of divalent counterions create a net attraction that can exceed the electrostatic repulsion of like-charged surfaces. Combined with van der Waals forces, hydrogen bonding through interlayer water and some genuine ionic-covalent bridging, this creates a cohesive gel with very high specific surface area (100 to 700 m²/g depending on measurement method). Strength comes from the sheer number of these contacts.

This is why C-S-H behaves partly like a solid and partly like a compacted colloid, explaining both its strength and its creep and drying shrinkage (water movement in the interlayer and gel pores lets particles rearrange under load).

## 2.6 Porosity: the master variable

Hardened paste contains:
- **Gel pores**: under 10 nm, intrinsic to C-S-H, about 28% of gel volume. Do not reduce strength significantly.
- **Capillary pores**: 10 nm to 10 µm, the remnants of original water-filled space not yet filled by hydrates. These control strength and permeability.
- **Air voids**: 10 µm to several mm, from entrapment (accidental) or entrainment (deliberate).

### Water-to-cement ratio (w/c)
Chemically, complete hydration binds only about 0.23 g of water per g of cement. Powers showed that about 0.42 g/g is required for complete hydration without leaving capillary pores empty (the extra water fills gel pores). Most concrete uses w/c of 0.40 to 0.60 for workability. Every bit of water beyond what hydration consumes leaves capillary pores.

**Abrams' law (1918)**: f_c = A / B^(w/c), an empirical exponential decline in strength with rising w/c.

**Powers gel-space ratio model (1958)**:

X = 0.68α / (0.32α + w/c)

f_c = A·Xⁿ, with A ≈ 234 MPa and n ≈ 3

where α is the degree of hydration (0 to 1). X is the fraction of available space filled by gel. At w/c = 0.5 and α = 0.8: X = 0.544/0.656 = 0.83, f_c ≈ 234 × 0.57 ≈ 133 MPa for paste (concrete is lower because of the interfacial zone and aggregate effects). The constant A represents the intrinsic strength of zero-porosity gel.

**Porosity-strength relations** (Ryshkewitch-type): f = f₀·e^(-kp), where p is porosity. Each 1% increase in porosity reduces strength by roughly 4 to 6%.

### Typical strength vs w/c (Portland cement, 28 days, moist cured)
| w/c | Approx. compressive strength (MPa) |
|---|---|
| 0.35 | 50-60 |
| 0.40 | 42-50 |
| 0.45 | 37-43 |
| 0.50 | 32-37 |
| 0.60 | 24-28 |
| 0.70 | 18-22 |

## 2.7 The interfacial transition zone (ITZ)

Around each aggregate particle, cement grains cannot pack efficiently against the flat surface (the "wall effect"). Water also accumulates there through bleeding. The result is a 10 to 50 µm shell with:
- Higher porosity (up to 2 to 3 times bulk paste)
- Large, oriented CH crystals with cleavage planes parallel to the aggregate surface
- More ettringite

The ITZ is the weakest link in normal concrete. Microcracks exist there before any load is applied (from shrinkage and bleeding). Under load, cracks initiate in the ITZ, propagate through paste and eventually coalesce. This explains:
- Why concrete is weaker than either its paste or its rock
- Why the stress-strain curve becomes nonlinear above about 30 to 40% of peak stress (stable microcracking) and accelerates above 70 to 90% (unstable crack growth)
- Why silica fume dramatically strengthens concrete (it consumes CH in the ITZ and fills the packing gap)

## 2.8 Aggregates in detail

| Aggregate | Density (kg/m³) | Effect |
|---|---|---|
| Crushed granite/basalt | 2600-3000 | Angular, rough: excellent bond, higher water demand |
| River gravel | 2550-2700 | Rounded, smooth: better flow, weaker bond |
| Limestone | 2500-2700 | Chemically reactive with paste in a beneficial way; low thermal expansion |
| Lightweight expanded clay/shale | 600-1600 | Concrete 1400-1900 kg/m³; internal curing |
| Heavyweight (magnetite, barite) | 4000-4600 | Radiation shielding |
| Recycled concrete aggregate | 2200-2500 | Higher absorption from attached old mortar; 10-30% strength loss at full replacement |

**Gradation**: a well-graded mix (Fuller curve, P = 100(d/D)^0.45 approximately) minimizes voids and therefore paste requirement.

**Sand scarcity**: desert sand is wind-rounded and too uniform for concrete. River and marine sand are the usable sources. Global extraction of sand and gravel is estimated at 40 to 50 billion tonnes per year, exceeding natural replenishment in many river systems and causing riverbed lowering, delta erosion and illegal mining.

## 2.9 Admixtures

| Type | Chemistry | Mechanism | Effect |
|---|---|---|---|
| Normal plasticizer | Lignosulfonates | Adsorb onto cement grains, electrostatic repulsion | 5-10% water reduction |
| Superplasticizer (older) | Sulfonated naphthalene or melamine formaldehyde | Strong electrostatic dispersion | 15-25% water reduction |
| Superplasticizer (modern) | Polycarboxylate ethers (PCE) | Comb polymer: backbone adsorbs, side chains provide steric hindrance | 25-40% water reduction; enables w/c below 0.30 and self-consolidating concrete |
| Retarder | Sugars, gluconates, phosphates | Adsorb and poison nucleation sites | Extend workability in heat |
| Accelerator | CaCl₂ (chloride), calcium nitrate, C-S-H seeds | Promote nucleation | Faster strength in cold; chlorides corrode steel so restricted in reinforced work |
| Air-entrainer | Vinsol resin, synthetic surfactants | Stabilize microscopic bubbles (10-300 µm) | Freeze-thaw protection |
| Shrinkage reducer | Polyoxyalkylene glycols | Lower pore water surface tension | Reduces capillary stress |
| Corrosion inhibitor | Calcium nitrite | Stabilizes passive film | Delays chloride-induced corrosion |
| Viscosity modifier | Cellulose ethers, welan gum | Thicken paste | Prevent segregation in flowable mixes |

Superplasticizers are the single biggest reason modern concrete is stronger than mid-century concrete: they allow very low water content while keeping the mix placeable.

## 2.10 Supplementary cementitious materials (SCMs)

### Pozzolanic reaction
Reactive amorphous silica consumes the weak CH and converts it into additional C-S-H:

CH + S + H → C-S-H (lower Ca/Si, typically ~1.0-1.5)

This refines pores, strengthens the ITZ, lowers permeability and reduces available alkali.

| SCM | Source | Particle size | Typical replacement | Reaction type | Notes |
|---|---|---|---|---|---|
| Fly ash Class F | Bituminous coal combustion | 1-100 µm spheres | 15-35% | Pozzolanic | Slower early strength, higher long-term; ball-bearing effect improves flow; supply shrinking as coal plants close |
| Fly ash Class C | Sub-bituminous/lignite | 1-100 µm | 15-40% | Pozzolanic + some hydraulic | Higher CaO |
| Ground granulated blast furnace slag (GGBS) | Quenched iron blast furnace slag | ~10 µm | 30-70% | Latent hydraulic (activated by CH and alkalis) | Excellent sulfate and chloride resistance; lower heat |
| Silica fume | Silicon/ferrosilicon smelting byproduct | ~0.1-0.2 µm (100x finer than cement) | 5-10% | Highly pozzolanic + filler | Enables 100+ MPa; very sticky |
| Metakaolin | Kaolin clay calcined at 650-800°C | 1-5 µm | 10-20% | Pozzolanic | Bright white; strong early pozzolan |
| Calcined clay + limestone (LC³) | Common clays + limestone | Varies | Clinker reduced to ~50% | Synergistic: aluminate from clay reacts with carbonate | Up to ~40% lower CO₂ with comparable strength |
| Natural pozzolans | Volcanic ash, pumice, diatomaceous earth | Varies | 15-40% | Pozzolanic | Roman-era tradition |
| Ground limestone filler | Raw limestone | 1-10 µm | 5-15% | Mostly filler; small carboaluminate reaction | Nucleation sites accelerate C₃S |

## 2.11 Curing and strength development

**Curing** means keeping concrete moist and at suitable temperature so hydration continues. Without curing, surface concrete can lose 30 to 50% of potential strength and become porous and dusty.

Typical strength gain (OPC, 20°C, moist):
| Age | % of 28-day strength |
|---|---|
| 1 day | 15-25 |
| 3 days | 40-50 |
| 7 days | 65-70 |
| 28 days | 100 (reference) |
| 90 days | 110-120 |
| 1 year | 115-130 |

**Maturity method (Nurse-Saul)**: M = Σ(T - T₀)Δt, with datum temperature T₀ ≈ -10°C. Concrete of equal maturity has approximately equal strength regardless of the time-temperature path. The Arrhenius-based equivalent age approach is more accurate (apparent activation energy ~40 kJ/mol).

**Temperature effects**: Hydration roughly doubles in rate for each 10 to 15°C rise. Below about 5°C it slows severely; freezing before about 3.5 MPa strength damages the concrete permanently. High early temperatures accelerate early strength but produce coarser, less dense C-S-H and lower ultimate strength (the "crossover effect").

**Mass concrete**: Heat of hydration in large pours can raise core temperatures 40 to 60°C above ambient. Differential cooling between hot core and cool surface causes thermal cracking. Hoover Dam (1931-1936) was built in interlocking blocks with embedded cooling pipes carrying refrigerated water; engineers estimated that without cooling the dam would have taken over a century to cool.

**Delayed ettringite formation (DEF)**: If concrete exceeds about 70°C during early curing, ettringite fails to form or decomposes. It later re-forms in hardened concrete, expanding and cracking it.

## 2.12 Mechanical properties of concrete

| Property | Normal (20-50 MPa) | High-strength (60-120 MPa) | UHPC (150-250 MPa) |
|---|---|---|---|
| Density (kg/m³) | 2300-2400 | 2400-2500 | 2400-2600 |
| Elastic modulus (GPa) | 25-35 | 35-45 | 45-60 |
| Tensile (direct) (MPa) | 2-4 | 4-6 | 7-12 (fiber) |
| Flexural (MPa) | 3-6 | 6-9 | 15-50 (fiber) |
| Fracture energy (N/m) | 80-150 | 120-200 | 10,000-40,000 (fiber) |
| Poisson's ratio | 0.15-0.22 | 0.18-0.22 | 0.18-0.22 |
| Thermal expansion (×10⁻⁶/K) | 7-12 | 7-12 | 10-14 |
| Typical w/c | 0.40-0.60 | 0.25-0.35 | 0.15-0.22 |

Common design relations (ACI 318, f'_c in MPa):
- E_c ≈ 4700√f'_c
- Modulus of rupture f_r ≈ 0.62√f'_c
- Splitting tensile ≈ 0.56√f'_c

Tensile strength scales with roughly the square root of compressive strength. Doubling compressive strength gains only about 40% in tension.

### Size effect
Brittle materials show lower average strength in larger specimens because larger volumes contain larger flaws (Weibull statistics) and because fracture process zones do not scale (Bažant size effect law: σ_N = Bf_t / √(1 + D/D₀)). This is why standard cylinders (150 × 300 mm) or cubes (150 mm) are specified: cube strength is about 1.25 times cylinder strength for the same concrete due to platen friction confinement and shape.

### Confinement
Concrete under triaxial compression is far stronger. Richart's relation: f_cc = f'_c + 4.1·f_l, where f_l is the lateral confining pressure. Spiral reinforcement and steel tubes (concrete-filled steel tube columns) exploit this.

## 2.13 Time-dependent deformation

- **Plastic shrinkage**: evaporation from fresh concrete before set; surface cracking in hot, windy conditions.
- **Autogenous shrinkage**: hydration products occupy about 8 to 10% less volume than reactants (chemical shrinkage). At low w/c, self-desiccation creates capillary tension and bulk shrinkage of 200 to 600 microstrain. Major issue in high-strength concrete.
- **Drying shrinkage**: loss of water from capillary and gel pores. Typical 400 to 800 microstrain. Driven by capillary pressure (Kelvin-Laplace), disjoining pressure and surface energy changes.
- **Creep**: continued deformation under sustained load, typically 1.5 to 3 times the initial elastic strain over years. Caused by C-S-H particle sliding and water redistribution. Critical for prestress losses and long-span deflections.
- **Carbonation shrinkage**: CO₂ reacting with CH and C-S-H causes additional small shrinkage.

## 2.14 Reinforced concrete: the partnership with steel

Concrete is excellent in compression and poor in tension. Steel is excellent in tension. Together they form the most widely used structural system in the world. The partnership works because of five coincidences:

1. **Matched thermal expansion**: steel ~12 × 10⁻⁶/K and concrete ~10 × 10⁻⁶/K, so they do not tear apart with temperature changes.
2. **Bond**: ribbed (deformed) bars create mechanical interlock; adhesion and friction add more. Bond stresses of 5 to 15 MPa develop over embedment lengths of 30 to 50 bar diameters.
3. **Chemical protection**: the pH 12.5 to 13.5 pore solution forms a nanometer-thick passive film of iron oxides/hydroxides on steel, reducing corrosion to negligible rates.
4. **Fire protection**: concrete cover insulates steel, which loses half its strength near 550 to 600°C.
5. **Cost**: concrete supplies bulk cheaply; steel is used only where tension demands it.

**Prestressed concrete** applies compression in advance (high-strength strands at 1600 to 1900 MPa, tensioned before or after casting) so service loads never put concrete into tension. Enables spans of 30 to 300+ m in bridges.

**Fiber reinforcement**: steel, glass, polypropylene, PVA or basalt fibers (0.5 to 2% by volume) bridge microcracks and convert brittle failure into gradual pullout.

## 2.15 Durability science

### Carbonation
CO₂ + Ca(OH)₂ → CaCO₃ + H₂O

CO₂ diffuses inward; depth follows x = K√t (K typically 1 to 10 mm/√year depending on quality and humidity). Carbonation lowers pore pH from about 13 to about 9, destroying steel passivation. Fastest at 50 to 70% relative humidity.

### Chloride-induced corrosion
Chlorides (seawater, deicing salts) penetrate by diffusion (Fick's second law, typical D = 10⁻¹² to 10⁻¹¹ m²/s) and locally break down the passive film once a threshold (roughly 0.2 to 0.4% Cl⁻ by mass of cement, or Cl⁻/OH⁻ > ~0.6) is reached. Pitting corrosion follows.

Anodic: Fe → Fe²⁺ + 2e⁻
Cathodic: O₂ + 2H₂O + 4e⁻ → 4OH⁻

Rust products occupy 2 to 6 times the volume of the original steel. The expansion cracks and spalls the cover. This is the dominant cause of deterioration in bridges, parking structures and marine works.

### Alkali-silica reaction (ASR)
Reactive amorphous or strained silica in some aggregates reacts with alkali hydroxides (Na, K) in pore solution, forming a hygroscopic alkali-silicate gel that swells when it absorbs water. Characteristic map cracking. Mitigation: low-alkali cement, SCMs (which bind alkalis), lithium compounds, non-reactive aggregate.

### Sulfate attack
External sulfates react with monosulfate and CH to form expansive ettringite and gypsum. In cold, wet, carbonate-rich conditions, thaumasite (CaSiO₃·CaCO₃·CaSO₄·15H₂O) forms by consuming C-S-H itself, turning concrete to mush. Sulfate-resisting cement limits C₃A to under 5%.

### Freeze-thaw
Water expands about 9% on freezing. Hydraulic pressure and osmotic effects in capillary pores crack non-air-entrained concrete. Entrained air (4 to 8% by volume, bubble spacing factor under 0.20 mm) provides escape chambers. Each 1% of air reduces strength by roughly 4 to 6%, which is accepted as the price of durability.

### Fire
- 100°C: free water evaporates
- 180 to 300°C: C-S-H and ettringite begin dehydrating
- 400 to 500°C: CH decomposes (Ca(OH)₂ → CaO + H₂O)
- 573°C: quartz α-β inversion with ~0.8% volume expansion in siliceous aggregate
- 600 to 800°C: C-S-H breaks down; CaCO₃ in limestone aggregate starts decomposing around 700°C+
- Explosive spalling occurs when vapor pressure builds in dense, low-permeability concrete. Polypropylene fibers (melting at ~160°C) create escape channels.

## 2.16 High-performance and ultra-high-performance concrete

**High-strength concrete (60 to 120 MPa)**: low w/c (0.25 to 0.35) enabled by PCE superplasticizer, 5 to 10% silica fume, strong crushed aggregate with maximum size reduced to 10 to 14 mm. Failure passes through aggregate instead of around it because the ITZ is no longer weaker.

**Ultra-high-performance concrete (UHPC, 150 to 250 MPa)**:
- w/b 0.15 to 0.22
- No coarse aggregate; fine quartz sand under 0.6 mm
- Ground quartz flour and silica fume optimizing particle packing across four size classes (packing density approaching 0.80+)
- 2 to 3% steel microfibers (13 mm long, 0.2 mm diameter, 2000+ MPa)
- Often heat-cured at 90°C for 48 h, which converts C-S-H to denser forms and drives pozzolanic reaction to completion
- Capillary porosity nearly eliminated; chloride diffusion 10 to 100 times lower than normal concrete

**Reactive powder concrete** with steel aggregate, pressure during setting and 250 to 400°C curing has reached about 800 MPa in laboratories, at which point some crystalline xonotlite forms.

## 2.17 Embodied energy and carbon of concrete

| Material | EE (MJ/kg) | EC (kg CO₂e/kg) |
|---|---|---|
| Aggregate (crushed) | 0.08-0.11 | 0.004-0.007 |
| Portland cement CEM I | 4.5-6.5 | 0.85-0.95 |
| GGBS | 0.6-1.6 | 0.04-0.08 |
| Fly ash | ~0.1 (allocated) | ~0.01-0.03 |
| Concrete C20/25 general | 0.7-0.8 | 0.09-0.11 |
| Concrete C30/37 OPC | 0.85-1.0 | 0.12-0.14 |
| Concrete C40/50 OPC | 1.0-1.2 | 0.14-0.17 |
| Concrete C30/37 with 50% GGBS | 0.6-0.7 | 0.07-0.09 |
| Reinforced concrete (~110 kg rebar/m³) | 1.8-2.0 | 0.18-0.22 |

Per cubic meter, a typical 30 MPa mix emits about 250 to 350 kg CO₂e. Cement accounts for roughly 85 to 90% of this despite being about 12 to 15% of the mass.

**Carbonation uptake**: over its service life and after demolition (when crushed concrete exposes large surface area), concrete reabsorbs some of the CO₂ released during calcination. Published global estimates suggest cumulative uptake could equal a substantial fraction (estimates range from about 20% to over 40%) of historical calcination emissions. Uptake is slow and concentrated near surfaces.

## 2.18 Renewability and work to attain: concrete

**Raw materials**: Limestone (A1, effectively inexhaustible; sedimentary carbonate covers about 10% of land surface), clay (A1), sand and gravel (A2, locally scarce), gypsum (A1 natural plus synthetic FGD gypsum from coal plant scrubbers, which is declining), water (local constraint in arid regions; concrete production uses roughly 1 to 2% of global industrial water withdrawal).

**Renewability**: Non-renewable but not depletion-limited. The binding constraint is the carbon emitted, not the rock.

**Recyclability**: Downcycling only. Demolished concrete is crushed into recycled aggregate for road base or new concrete. Hydrated cement cannot be easily returned to clinker except by re-firing. Research routes include separating fine cement paste and re-clinkering it (one Cambridge process uses old cement paste as the flux in electric arc steel furnaces, producing re-activated clinker as a byproduct).

**Work chain summary**:
1. Blast and haul limestone and clay
2. Crush and grind raw meal (electrical)
3. Calcine at 900°C and clinker at 1450°C (thermal, the dominant energy load)
4. Cool, add gypsum, grind fine (electrical)
5. Quarry, crush, wash and grade aggregates
6. Batch and mix (ready-mix plant)
7. Transport in agitating trucks; must be placed within about 90 minutes
8. Build formwork (often the largest labor cost in concrete construction), place reinforcement
9. Pour, vibrate to remove entrapped air, finish surfaces
10. Cure 7+ days; strip formwork after reaching 50 to 70% of design strength

**Effort rating**: Moderate per kg, very high in aggregate due to scale. Energy is concentrated in one step (the kiln). Labor is concentrated on site (formwork, rebar fixing, placement).

---

# 3. Lime, Ancient Binders and Cement Alternatives

## 3.1 Lime (air lime)

**Production**: Limestone burned at 900 to 1100°C:
CaCO₃ → CaO + CO₂ (quicklime)

**Slaking**: CaO + H₂O → Ca(OH)₂ + heat (ΔH ≈ -65 kJ/mol; violent enough to boil water)

**Hardening by carbonation**: Ca(OH)₂ + CO₂ → CaCO₃ + H₂O

The mortar literally turns back into limestone by absorbing CO₂ from air. The process is diffusion-limited, advancing roughly a few millimeters per year in a wall; thick walls can take decades to carbonate fully. Strength results from interlocking micro-calcite crystals growing in pores and bridging sand grains.

**Properties**: compressive strength 0.5 to 3 MPa. Weak but flexible, vapor-permeable and self-healing (dissolved Ca(OH)₂ migrates into cracks and re-carbonates). Ideal for soft historic masonry because it is weaker than the bricks; cracks pass through replaceable mortar instead of the masonry units.

**Hydraulic lime (NHL)**: Limestone containing 6 to 20% clay or silica, burned at 900 to 1200°C, forms belite (C₂S) and calcium aluminates. Sets partly by hydration (even underwater) and partly by carbonation. Grades NHL 2, 3.5 and 5 refer to minimum 28-day strength in MPa.

**Embodied**: ~4.5 to 5.5 MJ/kg; ~0.75 to 0.9 kg CO₂e/kg at the plant. Air lime can reabsorb most of its process CO₂ over time, so its lifetime net emissions are substantially lower than the gate figure suggests.

## 3.2 Roman concrete (opus caementicium)

**Recipe**: Lime + volcanic ash (pulvis puteolanus, from Pozzuoli near Naples) + rock fragments (caementa). Marine structures used seawater.

**Chemistry**: Volcanic glass and zeolites in the ash reacted with lime to form C-A-S-H (calcium aluminosilicate hydrate, aluminum-substituted C-S-H). In marine structures, seawater percolation over centuries dissolved ash components and precipitated **aluminous tobermorite** (a crystalline, platy, rare mineral that normally requires hydrothermal conditions) and **phillipsite** (a zeolite) in pores and cracks. These crystals reinforce the matrix over time. Roman harbor concrete has survived 2000 years of wave attack.

**Hot mixing and self-healing**: Studies (published 2023) identified white millimeter-scale "lime clasts" in Roman concrete as products of mixing with quicklime directly (hot mixing) instead of slaked lime. The clasts act as calcium reservoirs: when cracks admit water, calcium dissolves from the clast and reprecipitates as calcite, sealing the crack.

**Strength**: ~5 to 15 MPa, much weaker than modern concrete. Roman structures relied on massive compression-only geometry (the Pantheon dome: 43.3 m unreinforced span, density graded from heavy basalt aggregate at the base to light pumice at the top).

## 3.3 Sticky rice mortar

Chinese builders from about the 5th century onward added boiled glutinous rice soup to lime mortar. Research shows amylopectin (the branched polysaccharide in sticky rice) acts as an inhibitor that controls calcite crystal growth, producing a compact microstructure of small calcite crystals within an organic matrix. The result: stronger, more water-resistant and more cohesive mortar. Used in the Great Wall sections, tombs and city walls still standing.

## 3.4 Geopolymers and alkali-activated materials

Aluminosilicate powders (fly ash, slag, metakaolin) dissolved in concentrated alkali (sodium hydroxide, sodium silicate) re-polymerize into an amorphous three-dimensional network of SiO₄ and AlO₄ tetrahedra (N-A-S-H gel for low-calcium precursors, C-A-S-H for slag). No limestone calcination is needed.

- Strength: 20 to 80+ MPa
- Excellent acid and fire resistance
- CO₂ savings 40 to 80% vs OPC, though sodium silicate production is energy-intensive
- Challenges: caustic activators (handling hazards), variable raw materials, rapid setting, limited long-term standards

## 3.5 Other low-carbon cements

| Cement | Clinkering temp. | Key phase | CO₂ vs OPC | Notes |
|---|---|---|---|---|
| Calcium sulfoaluminate (CSA) | ~1250°C | Ye'elimite C₄A₃S̄ | -25 to -35% | Rapid strength; forms ettringite as main binder |
| Belite-rich | ~1350°C | C₂S | -10 to -15% | Slower early strength |
| LC³ (limestone calcined clay) | Clay at 750-850°C | OPC clinker + calcined clay + limestone | Up to -40% | Commercially deployed in several countries |
| Magnesium-based (MgO) | 650-800°C (from various sources) | Brucite, hydrated magnesium carbonates | Variable; possibly negative if from silicates | Early stage |
| Carbonatable calcium silicate | ~1200°C | Wollastonite, rankinite | -30 to -70% | Hardens by CO₂ curing instead of water |
| Electrochemically produced cement | Low-temp electrolysis | Ca(OH)₂ from non-carbonate sources | Potentially near-zero process CO₂ | Pilot scale |

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

# 7. Timber and Engineered Wood

## 7.1 Wood as a natural fiber composite

Wood is a cellular solid built from hollow tube-shaped cells whose walls are a layered fiber-reinforced polymer composite.

### Chemical composition (dry mass, softwood)
| Polymer | % | Structure | Role |
|---|---|---|---|
| Cellulose | 40-45 | Linear chains of β-1,4-linked glucose (degree of polymerization 5,000-10,000); chains hydrogen-bonded into crystalline microfibrils 3-4 nm wide | Tensile reinforcement |
| Hemicellulose | 25-30 | Branched, amorphous polysaccharides (glucomannan in softwoods, xylan in hardwoods) | Coupling agent between cellulose and lignin; most hygroscopic component |
| Lignin | 25-30 | 3D crosslinked phenolic polymer from coniferyl, sinapyl and p-coumaryl alcohols | Stiff matrix; resists compression and buckling of microfibrils; hydrophobic; resists decay |
| Extractives | 2-10 | Resins, tannins, terpenes | Color, odor, natural decay resistance |

Crystalline cellulose is remarkable: axial modulus about 130 to 150 GPa and theoretical tensile strength several GPa, comparable to steel per unit weight and far better per unit density. Each glucose unit forms intra- and interchain hydrogen bonds (O3-H···O5 and O6-H···O3) that lock chains into sheets; van der Waals forces stack the sheets.

### Cell wall architecture
- **Middle lamella**: lignin-rich layer cementing adjacent cells
- **Primary wall**: thin, random microfibril orientation
- **Secondary wall**:
 - S1: thin, microfibrils at 50 to 70° to the cell axis
 - **S2: about 75 to 85% of wall thickness; microfibrils at 5 to 30° to the axis (the microfibril angle, MFA)**
 - S3: thin, nearly transverse microfibrils

The S2 layer with low MFA dominates longitudinal strength and stiffness. Low MFA means stiff, strong wood. Juvenile wood near the pith has high MFA (30 to 40°) and is weaker. Compression wood (on the lower side of leaning conifers) also has high MFA and more lignin.

### Cellular structure
- **Softwoods** (conifers): 90 to 95% tracheids, cells 2 to 5 mm long and 20 to 50 µm wide, serving both water conduction and support
- **Hardwoods** (angiosperms): fibers for support, vessels for conduction (visible as pores), rays and parenchyma

Cell wall material density is about 1500 kg/m³ regardless of species. Wood density (100 kg/m³ for balsa to 1300 kg/m³ for lignum vitae) depends on how much of the volume is wall vs empty lumen. Most mechanical properties scale nearly linearly with density (strength ∝ ρ^1 to ρ^1.5 for cellular solids per Gibson and Ashby).

### Anisotropy
Three principal directions: longitudinal (L, along the grain), radial (R, across growth rings) and tangential (T, tangent to rings).

E_L : E_R : E_T ≈ 20 : 1.6 : 1 (typical softwood)

Tension along the grain is 20 to 40 times greater than tension across the grain. Engineered products exist largely to overcome this.

## 7.2 Moisture

- Green wood can contain 30 to 200% water by dry mass
- **Fiber saturation point (FSP)**: about 25 to 30% moisture content (MC), where cell walls are saturated but lumens are empty
- Below FSP, water leaves the cell walls: wood shrinks (tangential ~6 to 10%, radial ~3 to 5%, longitudinal ~0.1 to 0.2% from green to oven dry) and strength rises sharply because hydrogen bonds between polymer chains replace hydrogen bonds to water
- Compressive strength parallel to grain roughly doubles from green to 12% MC
- Equilibrium MC indoors: 6 to 12%; outdoors under cover: 12 to 18%

## 7.3 Strength (clear wood, 12% MC, USDA Wood Handbook ranges)

| Species | Density (kg/m³) | Bending MOR (MPa) | E (GPa) | Compression ∥ (MPa) | Tension ⊥ (MPa) | Shear (MPa) |
|---|---|---|---|---|---|---|
| Douglas-fir (coast) | 480 | 85 | 13.4 | 50 | 2.3 | 7.8 |
| Southern yellow pine (loblolly) | 510 | 88 | 12.3 | 49 | 3.2 | 9.6 |
| Spruce (Sitka) | 400 | 70 | 10.8 | 38 | 2.6 | 7.9 |
| White oak | 680 | 105 | 12.3 | 51 | 5.5 | 13.8 |
| Hard maple | 700 | 109 | 12.6 | 54 | n/a | 16.1 |
| Balsa | 160 | 20 | 3.8 | 12 | n/a | n/a |

Tension parallel to grain for clear wood: roughly 80 to 150 MPa. Specific tensile strength along the grain rivals mild steel.

**Real lumber is far weaker**: knots (where branches disrupt fiber alignment), slope of grain, checks and splits reduce design values to 25 to 50% of clear wood. Strength grading (visual or machine stress-graded by measuring stiffness) assigns classes such as C24 (EN 338: characteristic bending 24 MPa, tension ~14.5 MPa, compression ~21 MPa, mean E ~11 GPa).

**Duration of load**: wood is viscoelastic; it carries about 60% of its short-term strength under permanent load (Madison curve). Design codes apply load-duration factors.

## 7.4 Engineered wood: how strength is achieved

Engineered products spread defects randomly through the cross-section (statistical averaging) and cross-laminate to control anisotropy.

| Product | Construction | Strength mechanism | Typical use |
|---|---|---|---|
| Plywood | Thin veneers, alternating 90° | Cross-lamination: dimensional stability, two-way strength | Sheathing, subfloors |
| OSB | Wood strands in oriented layers, resin-bonded | Small strands disperse defects; uses small fast-grown trees | Sheathing, I-joist webs |
| Glulam | Graded laminations (19-45 mm) glued parallel | Best grades placed in outer zones where bending stress is highest; defects dispersed | Beams to 100+ m spans |
| LVL | Veneers (3 mm) glued parallel | Extremely uniform; defects distributed | Headers, beams |
| PSL (Parallam) | Long veneer strands glued parallel | High uniform strength | Columns, beams |
| CLT (cross-laminated timber) | 3, 5, 7+ layers of lumber at 90° | Two-way slab action; dimensional stability; panels up to 3 × 18 m | Floors, walls of mass timber towers |
| I-joists | LVL or lumber flanges, OSB web | Material placed where bending stress is | Floor joists |

Adhesives: phenol-resorcinol-formaldehyde (PRF), melamine-urea-formaldehyde (MUF), polyurethane (PUR), emulsion polymer isocyanate (EPI). Glue lines are stronger than the wood itself; failure tests require wood failure, not glue failure.

**Mass timber towers**: Mjøstårnet (Norway, 85 m, 2019) and Ascent (Milwaukee, ~87 m, 2022) demonstrate CLT and glulam at high-rise scale.

## 7.5 Fire behavior

Wood burns, yet large sections perform well in fire because charcoal forms on the surface. Char has very low conductivity (~0.1 W/m·K) and insulates the core. Below a ~40 mm heat-affected zone, inner wood stays near ambient temperature and full strength.

- Pyrolysis begins ~200 to 280°C
- Char front at about 300°C
- Design charring rate (softwood, Eurocode 5): ~0.65 mm/min one-dimensional; ~0.7 to 0.8 mm/min notional
- A 60-minute fire consumes about 40 to 45 mm of each exposed face

## 7.6 Biological degradation

- **Brown rot fungi**: attack cellulose and hemicellulose via Fenton chemistry (hydroxyl radicals), leaving cubical cracked brown lignin residue; can lose 70% of strength at 10% mass loss
- **White rot fungi**: degrade lignin and cellulose, leaving bleached fibrous wood
- **Soft rot**: in very wet conditions
- **Insects**: termites (digest cellulose via gut symbionts), carpenter ants, powderpost beetles
- **Requirements for decay**: MC above ~20%, oxygen, temperature 5 to 40°C, food. Keeping wood below 20% MC prevents decay. Fully submerged wood without oxygen can last millennia (Venice foundation piles).
- **Preservation**: copper-based (ACQ, copper azole), borates (diffusible, for indoor use), creosote (historic), thermal modification (180 to 230°C), acetylation (reacting hydroxyl groups with acetic anhydride so cell walls no longer absorb water)

## 7.7 Carbon storage

Photosynthesis: 6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂

Dry wood is about 50% carbon by mass. Each kg of dry wood stores 0.5 × (44/12) ≈ **1.83 kg CO₂**. A cubic meter of softwood (~450 kg dry) stores about 800 kg CO₂, more than the ~300 kg emitted making a cubic meter of ordinary concrete.

This storage persists only as long as the wood does not burn or rot. Accounting standards treat it carefully (EN 16449, EN 15804).

## 7.8 Production and work to attain

1. **Forest establishment and growth**: 25 to 40 years for plantation pine (southern US, New Zealand); 50 to 80 years for Douglas-fir and spruce; 80 to 150+ years for oak and old-growth species
2. **Harvesting**: felling (feller-bunchers or chainsaws), delimbing, bucking to length, skidding/forwarding to landing; harvester-forwarder systems process a tree in under a minute
3. **Transport** to mill
4. **Sawmilling**: debarking, primary breakdown (band or circular saws), edging, trimming. Lumber recovery typically 40 to 60% of log volume; the rest becomes chips (pulp, OSB, particleboard), sawdust and bark (biomass fuel)
5. **Drying**: kiln drying at 60 to 120°C for days to weeks. **Drying is typically the largest energy input** in lumber production, often 60 to 80% of process energy. Most mills burn their own bark and sawdust, so much of this energy is biogenic.
6. **Planing and grading**
7. **For engineered products**: finger-jointing, adhesive application, pressing, CNC fabrication

| Product | EE (MJ/kg) | Fossil EC (kg CO₂e/kg) | Biogenic stored (kg CO₂/kg) |
|---|---|---|---|
| Sawn softwood, kiln dried | 7-10 (much biomass) | 0.2-0.3 | -1.6 to -1.7 |
| Sawn hardwood | 8-11 | 0.25-0.35 | -1.6 to -1.7 |
| Glulam | 10-12 | 0.4-0.5 | -1.6 |
| CLT | 8-12 | 0.3-0.45 | -1.6 |
| Plywood | 12-15 | 0.4-0.7 | -1.5 |
| OSB | 12-15 | 0.4-0.6 | -1.5 |

## 7.9 Renewability: timber
- **Class R2**. Genuinely renewable if harvest does not exceed growth and forest ecosystems are maintained. Certification schemes (FSC, PEFC) audit this.
- Global industrial roundwood harvest ~2 billion m³/yr (total roundwood including fuel ~4 billion m³).
- **End of life**: direct reuse of beams; cascading into particleboard; energy recovery (releases stored carbon but displaces fossil fuel); landfill (anaerobic decay can release methane).
- **Risks**: deforestation, monoculture, forest carbon debt (harvest reduces forest carbon stock temporarily), wildfire and pest outbreaks under climate change.

**Effort rating**: Low to moderate. Sunlight does the chemistry. Human work is mechanical (cutting, transport) plus drying.

---

# 8. Bamboo

## 8.1 Structure and strength

Bamboo is a giant grass (family Poaceae, subfamily Bambusoideae), not a tree. It has no secondary thickening: the culm (stem) reaches full diameter at emergence and full height within one growing season (2 to 4 months), then hardens over 3 to 5 years through lignification.

**Functionally graded composite**: Vascular bundles (cellulose fiber sheaths surrounding vessels) are embedded in parenchyma (thin-walled storage cells). Fiber density increases from about 15 to 20% at the inner wall to 50 to 60% at the outer wall. Tensile strength and stiffness rise correspondingly from inside to outside. Nature places the strongest material where bending stresses are greatest.

**Fiber cell walls**: multilayered (up to 8 to 10 alternating thick and thin lamellae with alternating microfibril angles), very low MFA in thick layers. This polylamellate structure gives high strength and toughness.

**Nodes and diaphragms**: internal walls at intervals prevent the hollow tube from buckling and ovalizing; fibers interweave at nodes.

**Outer skin**: silica-rich epidermis protects the culm.

| Property | Typical range |
|---|---|
| Density | 600-900 kg/m³ |
| Tensile (parallel) | 100-400 MPa (outer strips at top end) |
| Compressive (parallel) | 40-90 MPa |
| Bending MOR | 80-200 MPa |
| E | 10-25 GPa |
| Shear | 7-20 MPa |

Specific tensile strength of high-grade bamboo strips exceeds structural steel.

## 8.2 Weaknesses
- Low splitting resistance (fibers all parallel; tension perpendicular is very low)
- Starch in parenchyma attracts powderpost beetles (Dinoderus) and fungi; untreated bamboo may last only 2 to 5 years outdoors
- Hollow round geometry and variable diameter complicate connections
- Poor fire performance in thin walls

**Treatment**: harvesting in dry season when starch is low; leaching in water; boron (borax + boric acid) diffusion or pressure treatment; heat treatment.

**Engineered bamboo**: laminated bamboo lumber (strips glued) and bamboo scrimber (crushed fiber bundles impregnated with resin and hot-pressed to density ~1100 to 1200 kg/m³). These convert irregular culms into dimensional products at the cost of more energy and resin.

## 8.3 Renewability and work
- **Class R1**. Moso bamboo (Phyllostachys edulis) is harvestable at 4 to 6 years; the plant regenerates from its rhizome without replanting. Some species grow up to roughly 1 m per day at peak.
- Annual yields per hectare can exceed most timber plantations.
- **Work**: cutting by hand or saw; curing; treatment; splitting for engineered products.
- **EE**: raw culms ~1 to 3 MJ/kg (plus transport, which dominates when shipped internationally); engineered bamboo 5 to 25 MJ/kg depending on resin.
- **Biogenic carbon**: about the same as wood per kg (~1.6 to 1.8 kg CO₂ stored per kg).

**Effort rating**: Very low for raw culms. Moderate for engineered bamboo.

---

# 9. Natural Stone

## 9.1 How stone gets its strength

Strength depends on how mineral grains are bonded together.

### Igneous rocks
Crystallize from magma. Grains interlock directly as they grow against each other, like a 3D jigsaw with no weaker cement phase. Mineral strength comes from silicate frameworks (covalent Si-O bonds, ~450 kJ/mol).

- **Granite**: quartz (SiO₂, hardness 7), feldspars (KAlSi₃O₈, NaAlSi₃O₈-CaAl₂Si₂O₈), micas. Coarse grains (1 to 10 mm) from slow cooling deep underground.
- **Basalt**: fine-grained (fast cooling), pyroxene and plagioclase; very strong and dense.

### Sedimentary rocks
Grains deposited and later cemented together (lithification).
- **Sandstone**: quartz grains bound by a cement of silica (strongest), calcite (moderate) or clay/iron oxide (weakest). Strength depends on cement type and porosity.
- **Limestone**: calcite (CaCO₃) from shells, skeletons or chemical precipitation. Oolitic limestones (spherical grains), shelly limestones, chalk (weak, porous). Ionic Ca-CO₃ bonds; calcite has perfect rhombohedral cleavage.

### Metamorphic rocks
Recrystallized under heat and pressure.
- **Marble**: recrystallized limestone; interlocking calcite crystals, no pores; can be translucent.
- **Slate**: metamorphosed shale; aligned platy minerals give perfect cleavage, splitting into thin sheets for roofing.
- **Quartzite**: metamorphosed sandstone; quartz grains fused; extremely hard.

## 9.2 Properties

| Stone | Density (kg/m³) | Compressive (MPa) | Tensile (MPa) | E (GPa) | Porosity |
|---|---|---|---|---|---|
| Granite | 2600-2750 | 100-250 | 7-25 | 30-70 | 0.5-1.5% |
| Basalt | 2800-3000 | 100-300 | 10-30 | 50-100 | <1% |
| Limestone (dense) | 2300-2700 | 30-250 | 3-15 | 15-55 | 1-30% |
| Sandstone | 2000-2600 | 20-170 | 2-15 | 5-40 | 5-30% |
| Marble | 2650-2750 | 50-180 | 7-20 | 50-70 | <1% |
| Slate | 2700-2800 | 100-200 | 7-25 | 40-90 | <1% |

### Durability mechanisms
- **Freeze-thaw** in porous stones (pore size distribution matters more than total porosity)
- **Salt crystallization**: salts crystallizing in pores generate pressures exceeding the tensile strength of many stones
- **Acid dissolution** of carbonates: CaCO₃ + H₂SO₄ → CaSO₄·2H₂O (gypsum crusts on limestone buildings in polluted cities)
- **Thermal cycling** in marble: anisotropic thermal expansion of calcite crystals causes granular disintegration and bowing of thin panels
- **Clay swelling** in some sandstones

## 9.3 Production and work to attain
1. **Quarrying**: Dimension stone (blocks) is extracted with diamond wire saws, chain saws, line drilling and splitting with wedges or expansive grout; explosives are avoided because they fracture blocks. Crushed stone (aggregate) uses blasting.
2. **Block transport** (blocks of 10 to 40 t)
3. **Sawing**: gang saws (multiple steel blades with abrasive slurry or diamond segments) or diamond wire multi-saws cut slabs; hours to days per block
4. **Finishing**: polishing, flaming (thermal shock spalls surface crystals on granite for slip resistance), honing, bush hammering
5. **Waste**: 50 to 70% of quarried material can become waste between quarry and finished product

| Product | EE (MJ/kg) | EC (kg CO₂e/kg) |
|---|---|---|
| Local rough stone / rubble | 0.1-1 | 0.01-0.06 |
| Local cut limestone/sandstone | 1-3 | 0.06-0.2 |
| Granite slab, imported long-distance | 10-13 | 0.6-0.8 |
| Slate roofing | 0.1-1 (local) | 0.03-0.06 |

## 9.4 Renewability
- Class A1: geologically non-renewable but reserves are effectively unlimited for most types.
- Extremely durable (centuries to millennia) and reusable. Reclaimed stone is common.
- Local stone is one of the lowest-carbon structural materials in existence; transport often dominates its footprint.

**Effort rating**: Low energy, high labor and capital for dimension stone. Historically one of the most labor-intensive materials (hand quarrying and dressing).

---

# 10. Fired Clay Brick and Ceramics

## 10.1 Raw material
Clay minerals are layered aluminosilicates formed by weathering of feldspar:
- **Kaolinite** Al₂Si₂O₅(OH)₄: 1:1 layer (one silica tetrahedral sheet + one alumina octahedral sheet), non-swelling
- **Illite**: 2:1 layer with potassium between layers
- **Montmorillonite (smectite)**: 2:1 layer, swells strongly with water

Brick clays typically also contain quartz, feldspar, iron oxides and calcite. Plasticity comes from water films and electrostatic interactions between platy clay particles (under 2 µm), letting the mass be molded.

## 10.2 Firing chemistry: how strength develops

| Temperature (°C) | Process |
|---|---|
| 100-200 | Free and adsorbed water removed (must be slow to avoid steam cracking) |
| 200-450 | Organic matter burns out |
| 450-650 | **Dehydroxylation**: Al₂Si₂O₅(OH)₄ → Al₂Si₂O₇ (metakaolin) + 2H₂O. Crystal structure collapses into a disordered reactive phase |
| 573 | Quartz α-β inversion, ~0.8% volume change (critical during cooling to avoid "dunting" cracks) |
| 700-900 | Calcite decomposes (CaCO₃ → CaO + CO₂); CaO reacts with silica and alumina forming calcium silicates (gehlenite, wollastonite, anorthite) |
| 900-1000 | Metakaolin reorganizes into Al-Si spinel; fluxes (K₂O, Na₂O, FeO, CaO) begin forming a silicate melt |
| 1000-1200 | **Vitrification**: liquid-phase sintering. The glassy melt flows into pores by capillary action, pulling particles together and bonding them. **Mullite** (3Al₂O₃·2SiO₂) crystallizes as interlocking needles within the glass |

Upon cooling, the glassy phase solidifies, welding unmelted quartz and mullite needles into a rigid ceramic. Strength rises with degree of vitrification and falls with porosity. Iron oxide in an oxidizing kiln atmosphere produces red color (hematite); reducing atmospheres produce darker colors.

Firing temperature for common bricks: 900 to 1100°C. Engineering bricks and clinker bricks: 1100 to 1250°C. Firing schedule: 24 to 72 hours in tunnel kilns; days to weeks in traditional clamps.

## 10.3 Properties

| Type | Compressive (MPa) | Water absorption | Density (kg/m³) |
|---|---|---|---|
| Common brick | 10-40 | 10-25% | 1600-1900 |
| Facing brick | 20-80 | 5-15% | 1800-2000 |
| Engineering brick Class B | ≥75 | ≤7% | 2100-2300 |
| Engineering brick Class A | ≥125 | ≤4.5% | 2200-2400 |

Tensile and flexural: ~2 to 10 MPa (brittle). E ≈ 10 to 30 GPa.

**Masonry strength** is lower than brick strength because mortar joints are softer and expand laterally under compression, inducing tension in bricks. Masonry compressive strength f_k ≈ K·f_b^0.7·f_m^0.3 (Eurocode 6). Typical masonry: 4 to 15 MPa.

**Durability issues**: efflorescence (soluble salts migrating to surface), frost damage in under-fired porous bricks, moisture expansion (fired clay slowly absorbs water and expands irreversibly over decades, ~0.5 to 1 mm/m).

## 10.4 Production and work to attain
1. Clay extraction (open pit), weathering/aging
2. Crushing, grinding, mixing with water (and sand or additives)
3. Forming: extrusion through a die and wire cutting (most modern bricks), soft-mud molding or dry pressing
4. Drying: 1 to 3 days in heated chambers, typically using waste heat from kilns; drying shrinkage 4 to 10%
5. Firing in tunnel kilns (bricks on carts moving through preheat, firing and cooling zones), Hoffmann kilns or traditional clamps
6. Sorting and packing

| Metric | Value |
|---|---|
| Firing energy | ~2-3 GJ/t |
| EE | 2.5-4 MJ/kg |
| EC | 0.2-0.3 kg CO₂e/kg |
| World production | ~1.5 trillion bricks/yr |

Traditional small kilns in South Asia (e.g., fixed chimney bull's trench kilns) burn coal, wood and even tires with high particulate emissions and severe air quality effects.

## 10.5 Renewability
- Class A1 (clay is abundant), though removal of fertile topsoil for brickmaking is a problem in parts of South Asia.
- Highly durable (centuries). Reusable if laid in lime mortar (cement mortar is often stronger than the brick, making clean separation difficult). Otherwise crushed for fill or aggregate.

**Effort rating**: Moderate. One high-temperature step, simple mechanical forming.

---

# 11. Earth Construction

## 11.1 How unfired earth holds together

Earth walls use clay as a binder for a skeleton of sand, silt and gravel. No chemical reaction is involved in unstabilized earth. Strength comes from:

1. **Capillary suction (matric suction)**: In partially saturated soil, water forms menisci between particles. Surface tension pulls particles together. The suction pressure ψ = 2γ/r (Young-Laplace) can reach tens of MPa in fine pores. This is the dominant mechanism and is why earth is strongest when dry.
2. **Electrostatic and van der Waals forces** between clay platelets with negatively charged faces and cation-mediated bridges (similar in principle to C-S-H cohesion, far weaker).
3. **Mechanical interlock** of angular sand and gravel.
4. **Compaction density**: Rammed earth is compacted in 100 to 150 mm layers to near Proctor maximum dry density. Higher density means more particle contacts and smaller pores (stronger suction).

When saturated, suction disappears and unstabilized earth loses most of its strength. Protection requires "a good hat and good boots": wide roof overhangs and a raised plinth.

### Stabilization
- **Cement (5 to 10%)**: forms C-S-H bridges; strength 5 to 15 MPa; reduces water sensitivity but raises embodied carbon and reduces recyclability
- **Lime (5 to 10%)**: reacts with clay minerals (pozzolanic reaction with dissolved silica and alumina from clay at high pH) and through cation exchange flocculates clay
- **Fibers** (straw in cob and adobe): tensile reinforcement, reduce shrinkage cracking
- **Natural stabilizers**: dung (ammonia and fibers), plant juices, casein, tannins

## 11.2 Types and properties

| Technique | Method | Density (kg/m³) | Compressive (MPa) |
|---|---|---|---|
| Adobe | Molded mud bricks, sun-dried | 1200-1700 | 1-3 |
| Cob | Wet earth + straw built up by hand | 1200-1700 | 0.5-2 |
| Rammed earth (unstabilized) | Damp earth compacted in formwork | 1800-2200 | 1-4 |
| Rammed earth (stabilized) | With 5-10% cement | 1900-2200 | 5-15 |
| Compressed earth block (CEB) | Pressed in a mechanical or hydraulic press | 1700-2100 | 2-8 (unstabilized); up to 10+ stabilized |
| Wattle and daub | Woven sticks plastered with earth | n/a | Non-structural infill |

**Thermal mass**: high density and specific heat (~0.8 to 1.0 kJ/kg·K) smooth indoor temperature swings.
**Hygric buffering**: clay absorbs and releases moisture, stabilizing indoor humidity.

## 11.3 Renewability and work
- Raw material is often excavated on site (subsoil, not topsoil). Class A1 with near-zero processing.
- **Unstabilized earth is fully recyclable**: it can be wetted and reused or returned to the ground with no waste.
- **EE**: unstabilized 0.05 to 0.5 MJ/kg (mostly machinery for excavation and compaction); stabilized 0.5 to 1 MJ/kg.
- **EC**: unstabilized ~0.005 to 0.02 kg CO₂e/kg; cement-stabilized 0.04 to 0.08.
- **Labor**: very labor-intensive by hand (ramming, mixing), though mechanized rammed earth with pneumatic tampers and modern formwork is efficient.
- Seismic vulnerability: unreinforced adobe performs very poorly in earthquakes; reinforcement (bamboo, geomesh, timber ring beams) is required in seismic zones.

**Effort rating**: Lowest energy of any wall material. Labor moderate to high.

---

# 12. Gypsum

## 12.1 Chemistry of setting

Gypsum (calcium sulfate dihydrate, CaSO₄·2H₂O) is heated to drive off part of its water:

CaSO₄·2H₂O → CaSO₄·½H₂O + 1½H₂O (at 120 to 180°C)

The hemihydrate is "plaster of Paris" (named for Montmartre deposits). Two forms:
- **β-hemihydrate**: calcined in open kettles; porous, flaky crystals; needs more water; weaker
- **α-hemihydrate**: produced in pressurized steam autoclaves; dense, well-formed crystals; less water; stronger (dental and high-strength plasters)

Mixed with water, hemihydrate dissolves (it is about 4 times more soluble than dihydrate). The solution becomes supersaturated with respect to dihydrate, which precipitates as needle-shaped and plate-like crystals that grow and interlock into a rigid network. Setting is a dissolution-precipitation process completed in 10 to 40 minutes.

Strength comes from the interlocking crystal network and crystal-crystal contacts. Excess water evaporates leaving porosity; set plaster compressive strength ranges from about 5 MPa (β, high water) to over 50 MPa (α dental stones, low water).

## 12.2 Plasterboard (drywall)
A gypsum core (with foam for lower density, starch for paper bonding, glass fibers in fire-rated board) between paper facings. Paper provides tensile strength in bending.

**Fire resistance**: gypsum contains about 21% chemically bound water by mass. In fire, dehydration absorbs about 700 kJ/kg of energy and releases steam, holding the unexposed side near 100°C until dehydration is complete. Type X board adds glass fibers to hold the calcined core together.

## 12.3 Renewability and work
- Natural gypsum (evaporite deposits) is Class A1/A2. Synthetic FGD gypsum from coal power plant scrubbers (SO₂ + CaCO₃ → CaSO₄) has supplied a large share of drywall gypsum; supply is falling as coal plants close.
- **Recyclable in a closed loop**: plasterboard offcuts can be ground, re-calcined and remade into board; also used as soil amendment.
- Must not go to landfill with organic waste: sulfate-reducing bacteria produce toxic H₂S.
- **EE**: plasterboard 3 to 7 MJ/kg; **EC**: 0.25 to 0.4 kg CO₂e/kg. Low calcination temperature makes gypsum one of the least energy-intensive binders.

**Effort rating**: Low.

---

# 13. Glass

## 13.1 Atomic structure

Glass is an amorphous solid: a liquid structure frozen in place by cooling faster than crystallization can occur. Its backbone is a network of SiO₄ tetrahedra joined at corners through bridging oxygens (strong covalent Si-O bonds, ~450 kJ/mol).

Pure silica glass needs over 2000°C to melt. **Network modifiers** break the network and lower melting temperature:
- Na₂O (soda): creates non-bridging oxygens (Si-O⁻ Na⁺), reduces viscosity; too much makes glass water-soluble
- CaO (lime): stabilizes against water attack
- MgO, Al₂O₃: improve chemical durability and control viscosity

**Soda-lime-silica float glass**: SiO₂ 71 to 74%, Na₂O 12 to 15%, CaO 8 to 10%, MgO 3 to 5%, Al₂O₃ 0.5 to 1.5%.

## 13.2 Why glass is strong in theory and weak in practice

- Theoretical strength: ~10 to 20 GPa
- Pristine fibers drawn in vacuum: ~5 to 10 GPa
- Window glass: 30 to 100 MPa

The reduction is entirely due to surface flaws (Griffith cracks) from handling, abrasion and contact. Glass has no dislocations and no plasticity, so stress at a flaw tip cannot be relieved by yielding.

**Static fatigue (stress corrosion)**: Water reacts with strained Si-O-Si bonds at crack tips:
Si-O-Si + H₂O → Si-OH + HO-Si
Cracks grow slowly under sustained load in humid air. Long-duration design strength is therefore much lower than short-term test strength (load duration factors).

## 13.3 Strengthening glass

| Process | Mechanism | Surface compression | Strength vs annealed | Break pattern |
|---|---|---|---|---|
| Annealed | Slow controlled cooling removes residual stress | ~0 | 1x (~45 MPa characteristic) | Large sharp shards |
| Heat-strengthened | Heated to ~620-650°C, moderately quenched with air jets | 24-52 MPa | ~2x (~70 MPa) | Large pieces stay in frame |
| Fully tempered (toughened) | Heated to ~620-650°C, rapidly quenched | ≥69 MPa (typically 90-150) | ~4-5x (~120 MPa) | Small cubic fragments ("safety glass") |
| Chemically strengthened | Ion exchange in molten KNO₃ at ~400°C; larger K⁺ ions replace Na⁺ in surface | 300-900 MPa (thin layer) | 5-8x | Variable |
| Laminated | Two or more plies bonded with PVB, SGP (ionoplast) or EVA interlayer | n/a | Post-breakage integrity | Fragments adhere to interlayer |

**Tempering physics**: During quenching, the surface solidifies first while the interior is still soft. As the interior later cools and contracts, it pulls the rigid surface into compression and itself goes into tension (parabolic stress profile, surface compression about twice the central tension). Any crack must first overcome the built-in compression before it can open.

**Nickel sulfide inclusions**: tiny NiS stones trapped during melting can undergo a slow phase change (α to β) with ~2 to 4% volume expansion, causing spontaneous breakage of tempered glass years after installation. Heat-soak testing (holding at ~290°C) breaks susceptible panes before shipment.

## 13.4 Properties
- Density 2500 kg/m³
- E ≈ 70 GPa
- Fracture toughness ~0.75 MPa·√m
- Thermal expansion ~9 × 10⁻⁶/K
- Thermal conductivity ~1.0 W/m·K
- Softening point ~720°C

## 13.5 Production and work to attain
1. **Raw materials**: silica sand (high purity, low iron), soda ash (Na₂CO₃, from the Solvay process or natural trona), limestone, dolomite, plus 10 to 30% cullet (recycled glass)
2. **Melting**: regenerative furnaces at 1500 to 1600°C; a float furnace holds 1500 to 2500 t of molten glass and runs continuously for 15 to 20 years
 Carbonate raw materials release process CO₂: Na₂CO₃ → Na₂O + CO₂; CaCO₃ → CaO + CO₂
3. **Float process** (Pilkington, 1950s): molten glass poured onto a bath of molten tin at ~1100°C under nitrogen/hydrogen atmosphere; gravity and surface tension produce a flat, fire-polished ribbon (equilibrium thickness ~6 mm; top rollers stretch or compress for other thicknesses)
4. **Annealing lehr**: controlled cooling from ~600°C
5. **Cutting, coating** (low-emissivity silver or tin oxide coatings, sputtered or pyrolytic), tempering, laminating, assembling into insulated glazing units

| Metric | Value |
|---|---|
| Melting energy (practical) | ~5-8 GJ/t |
| Theoretical minimum | ~2.5-2.7 GJ/t |
| EE float glass | 12-16 MJ/kg |
| EE toughened | 20-25 MJ/kg |
| EC | 0.9-1.5 kg CO₂e/kg |

Each 10% cullet reduces furnace energy by about 2.5 to 3% and avoids carbonate process emissions.

## 13.6 Renewability
- Silica sand: Class A1/A2 (high-purity glass sand is less common than construction sand).
- Soda ash: Class A1.
- **Recycling**: container glass is widely recycled; flat glass closed-loop recycling is limited because composition and contamination (coatings, interlayers, sealants) must be tightly controlled. Most demolition glass is downcycled or landfilled.

**Effort rating**: High temperature, continuous energy-intensive process.

---

# 14. Polymers and Foam Insulation

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

# 15. Fiber-Reinforced Polymers and Basalt Fiber

## 15.1 Composite mechanics

**Rule of mixtures** (longitudinal stiffness):
E_c = V_f·E_f + V_m·E_m

**Transverse stiffness** (inverse rule):
1/E_c = V_f/E_f + V_m/E_m

Fibers carry load; the matrix transfers stress between fibers by shear, protects fibers from damage and environment, and holds geometry. Fiber volume fractions typically 50 to 65%.

## 15.2 Carbon fiber

**Structure**: Turbostratic graphite: sheets of sp²-bonded carbon (graphene-like) stacked imperfectly, with basal planes aligned along the fiber axis. In-plane graphene has a modulus of ~1 TPa and strength of ~130 GPa; carbon fiber captures a fraction of that.

**Production from polyacrylonitrile (PAN)**:
1. Polymerize acrylonitrile, spin into precursor fiber
2. **Stabilization (oxidation)**: 200 to 300°C in air under tension for 1 to 2 hours. Nitrile groups cyclize into ladder polymer; fiber becomes black and infusible
3. **Carbonization**: 1000 to 1600°C in nitrogen. Non-carbon atoms leave as HCN, NH₃, N₂, H₂O; carbon content rises above 92%
4. **Graphitization** (high-modulus grades): 2000 to 3000°C in argon; improves crystal order and alignment
5. Surface treatment (electrochemical oxidation) and sizing for matrix adhesion

Only about 50% of the PAN mass ends up as fiber.

| Grade | Tensile (GPa) | E (GPa) |
|---|---|---|
| Standard modulus | 3.5-5 | 230-240 |
| Intermediate modulus | 5-7 | 280-300 |
| High modulus | 3.5-4.5 | 350-600+ |
| CFRP laminate (unidirectional, ~60% fiber) | 1.5-2.8 | 135-180 |

**Use in buildings**: strengthening existing concrete beams, columns and slabs (externally bonded plates and wraps), prestressing tendons in corrosive environments, lightweight long-span structures.

## 15.3 Glass fiber
E-glass (aluminoborosilicate) drawn from melts at ~1200 to 1400°C through platinum-rhodium bushings at speeds of ~1000 to 3000 m/min. Pristine fibers are strong because their tiny diameter (10 to 20 µm) limits flaw size.
- Tensile: 2 to 3.5 GPa; E: 72 to 85 GPa
- AR (alkali-resistant) glass contains ~16 to 20% zirconia to survive the high pH in concrete (glass fiber reinforced concrete, GRC)

**GFRP rebar**: tensile 600 to 1200 MPa, E 40 to 60 GPa. Does not corrode. Linear elastic to failure (no yielding, so designs are over-reinforced to ensure concrete crushing governs). Low modulus increases deflections and crack widths. Loses strength above the resin Tg.

## 15.4 Basalt fiber
Melted from a single raw material (crushed basalt) at ~1450 to 1500°C and drawn like glass fiber. No additives needed.
- Tensile: 2.8 to 4.8 GPa; E: 85 to 95 GPa
- Better alkali and heat resistance than E-glass
- Used in rebar and concrete fiber reinforcement

## 15.5 Embodied values and renewability

| Material | EE (MJ/kg) | EC (kg CO₂e/kg) |
|---|---|---|
| Carbon fiber | 180-600 (widely varying estimates) | 20-40 |
| CFRP composite | 100-300 | 10-30 |
| Glass fiber | 25-35 | 1.5-2.5 |
| GFRP rebar | 40-80 | 2.5-4 |
| Basalt fiber | 15-25 | 1-2 |
| Epoxy resin | 100-140 | 5-7 |

- Fibers: glass and basalt Class A1; carbon fiber Class F (petrochemical precursor)
- Matrix: Class F
- **Recycling**: thermosets cannot be remelted. Options: mechanical grinding (filler), pyrolysis (recovers carbon fibers at reduced strength), solvolysis. Mostly landfilled today.
- **Effort rating**: Extreme for carbon fiber; moderate for glass and basalt.

---

# 16. Bio-Based and Rapidly Renewable Materials

## 16.1 Hempcrete (hemp-lime)
**Composition**: chopped woody core of the hemp stalk (hurd or shiv) + lime-based binder (often hydrated lime with a small hydraulic or pozzolanic component) + water.

**How it holds together**: lime carbonates and partially hydrates around the hurd particles, coating and bridging them. Hurd provides a porous lightweight skeleton (cellulose/lignin, ~70% porosity). The result is a non-structural insulating wall that is cast around a timber frame.

| Property | Value |
|---|---|
| Density | 250-450 kg/m³ (wall), up to 600 (floor) |
| Compressive | 0.3-1.2 MPa |
| Thermal conductivity | 0.06-0.12 W/m·K |
| Vapor permeability | High (breathable) |
| Fire | Resistant (lime coating; does not readily ignite) |

**Carbon**: Hemp grows to 3 to 4 m in about 4 months, absorbing roughly 1.5 to 1.7 t CO₂ per t of dry stalk. Combined with lime recarbonation over time, hempcrete walls are frequently reported as net carbon negative across their life cycle, even though the lime binder emits CO₂ at manufacture.

**Work**: cultivation (few pesticides needed), harvest, retting, decortication (separating fiber from hurd), mixing, casting in formwork, months of drying.

**Renewability**: R1.

## 16.2 Straw bale
Wheat, rice, rye or barley straw baled to 90 to 130 kg/m³. Used load-bearing (Nebraska-style, walls carry roof via a top plate) or as infill in a frame. Plastered both sides with lime or clay; the plaster skins act as a sandwich panel carrying load and protecting the straw.
- Thermal conductivity ~0.045 to 0.065 W/m·K
- Fire: densely packed and plastered bales perform well (insufficient oxygen inside the bale)
- Critical risk: moisture above ~20% enables fungal decay
- Agricultural byproduct; EE ~0.1 to 0.3 MJ/kg; R1

## 16.3 Cork
Bark of the cork oak (Quercus suber). Harvested every 9 years without felling the tree; trees live 150 to 250 years. Cells are tiny hexagonal prisms (~40 µm) with walls rich in **suberin** (a waterproof polyester-like biopolymer) and filled with air. Result: compressible, elastic, low conductivity (~0.040 W/m·K), rot-resistant.

Expanded cork board is made by heating cork granules with superheated steam (~300°C); natural resins (suberin) bind granules without added glue.
- R1. Harvested cork forests store carbon and support biodiversity.

## 16.4 Mycelium composites
Fungal mycelium (vegetative hyphae, chitin-glucan cell walls) grown through agricultural waste (hemp hurd, sawdust, husks) in molds over 1 to 2 weeks, then heat-killed. The hyphal network binds particles.
- Density 60 to 300 kg/m³; compressive ~0.1 to 1 MPa
- Insulation, acoustic panels, packaging; experimental bricks
- Very low energy; R1; compostable

## 16.5 Thatch, reed and other plant materials
- Water reed and straw thatch: 25 to 60 years (reed) with steep pitch for water shedding
- Rammed straw, sheep's wool insulation (keratin protein, naturally hygroscopic and fire-resistant), wood fiber insulation board (made by defibrating wood chips, either wet process using lignin as natural binder or dry process with PUR resin)

---

# 17. Emerging and Experimental Materials

## 17.1 Self-healing concrete
**Bacterial approach**: Alkali-tolerant spore-forming bacteria (e.g., Bacillus cohnii, B. pseudofirmus) plus a nutrient (calcium lactate) are embedded in porous capsules or lightweight aggregate. Dormant spores survive decades at pH 13. When a crack admits water and oxygen, spores germinate and metabolize lactate:

Ca(C₃H₅O₃)₂ + 6O₂ → CaCO₃ + 5CO₂ + 5H₂O

CO₂ produced also reacts with CH in the matrix to form more calcite. Cracks up to ~0.5 to 0.8 mm can seal.

**Ureolytic MICP (microbially induced calcite precipitation)**: bacteria with urease enzyme:
CO(NH₂)₂ + 2H₂O → 2NH₄⁺ + CO₃²⁻
Ca²⁺ + CO₃²⁻ → CaCO₃
Used for soil stabilization and biocement bricks; ammonium byproduct is a drawback.

**Autogenous healing**: Ordinary concrete heals cracks under ~0.1 mm on its own via continued hydration and calcite precipitation, enhanced by crystalline admixtures.

## 17.2 CO₂ mineralization
- **CO₂ injection in fresh concrete**: liquid CO₂ injected during mixing reacts with calcium ions to form nano-CaCO₃ that seeds C-S-H growth; allows slight cement reduction while permanently mineralizing small amounts of CO₂
- **Carbonation curing**: precast blocks cured in CO₂-rich chambers; with carbonatable calcium silicate cements, CO₂ is the hardening agent instead of water
- **Recycled aggregate carbonation**: exposing crushed concrete to CO₂ improves its quality and sequesters carbon

## 17.3 Graphene and nanomaterials in concrete
Graphene oxide at 0.01 to 0.05% by mass of cement has been reported to increase compressive strength 15 to 40% in laboratory studies by providing nucleation sites, regulating hydration product morphology and bridging nanocracks. Dispersion and cost are barriers. Nano-silica and carbon nanotubes work on similar principles.

## 17.4 Densified and transparent wood
- **Densified wood**: partial delignification (boiling in NaOH/Na₂SO₃) followed by hot pressing at ~100°C collapses cell lumens and aligns cellulose nanofibers. Published results (2018) report tensile strength over 500 MPa and specific strength exceeding many steels.
- **Transparent wood**: full or partial lignin removal (or lignin modification), then infiltration with a refractive-index-matched polymer (PMMA or epoxy). Up to 80 to 90% light transmittance with wood's toughness.

## 17.5 Low-carbon steel and aluminum
- Hydrogen DRI-EAF steel (section 4.5)
- Molten oxide electrolysis: direct electrolysis of iron oxide at ~1600°C, releasing oxygen
- Inert anodes for aluminum smelting

## 17.6 3D-printed concrete
Extrusion of stiff, thixotropic mortar layer by layer. Requires precise rheology: low yield stress during pumping, rapid structural buildup (thixotropy and accelerated hydration) to support subsequent layers. Saves formwork (the largest labor cost in conventional concrete) but typically uses high cement content mortars with no coarse aggregate, raising carbon per m³.

## 17.7 Electric and recycled cement
- Recycled cement paste re-clinkered in electric arc furnaces during steel recycling
- Electrochemical decarbonation routes that avoid kiln combustion
- Calcining with electric kilns or concentrated solar heat (fuel emissions eliminated, process emissions remain unless captured)
- Carbon capture at cement plants (amine scrubbing, oxyfuel kilns, calcium looping); first full-scale capture installations in Norway (Brevik) began operating in 2025

---

# 18. Master Comparison Tables

## 18.1 Mechanical properties

| Material | Density (kg/m³) | Compressive (MPa) | Tensile (MPa) | E (GPa) | Specific tensile strength (kN·m/kg) | Specific stiffness (MJ/kg) | Fracture behavior |
|---|---|---|---|---|---|---|---|
| Concrete (normal) | 2400 | 20-50 | 2-4 | 25-35 | 1-2 | 10-15 | Brittle |
| UHPC (fiber) | 2500 | 150-250 | 7-12 | 45-60 | 3-5 | 18-24 | Quasi-ductile |
| Reinforced concrete | 2450 | System | System | ~30 | n/a | n/a | Ductile if under-reinforced |
| Structural steel S355 | 7850 | 355 (yield) | 470-630 | 210 | 60-80 | 27 | Ductile |
| Prestressing strand | 7850 | n/a | 1860 | 195 | 237 | 25 | Limited ductility |
| Stainless 304 | 8000 | 210 (yield) | 520-720 | 193 | 65-90 | 24 | Very ductile |
| Aluminum 6061-T6 | 2700 | 276 (yield) | 310 | 69 | 115 | 26 | Ductile |
| Softwood (clear, along grain) | 450-550 | 40-55 | 80-150 | 10-14 | 150-280 | 22-27 | Brittle in tension, ductile in compression |
| Softwood lumber C24 (characteristic) | 420 | 21 | 14.5 | 11 | 35 | 26 | Variable |
| Glulam GL28h | 460 | 28 | 22 | 12.6 | 48 | 27 | Brittle in tension |
| Bamboo culm | 700 | 40-90 | 100-400 | 10-25 | 140-570 | 14-36 | Splits along fiber |
| Granite | 2650 | 100-250 | 7-25 | 30-70 | 3-9 | 11-26 | Brittle |
| Limestone | 2500 | 30-250 | 3-15 | 15-55 | 1-6 | 6-22 | Brittle |
| Fired brick | 1900 | 10-125 | 2-10 | 10-30 | 1-5 | 5-16 | Brittle |
| Rammed earth (unstab.) | 2000 | 1-4 | 0.1-0.4 | 0.5-3 | <0.2 | <1.5 | Brittle, water-sensitive |
| Gypsum (set plaster) | 1000-1200 | 5-15 | 1-4 | 4-10 | 1-3 | 4-8 | Brittle |
| Float glass (annealed) | 2500 | ~1000 (theoretical) | 30-100 | 70 | 12-40 | 28 | Very brittle |
| Tempered glass | 2500 | n/a | 120-200 | 70 | 48-80 | 28 | Very brittle |
| PVC | 1400 | 60-70 | 40-55 | 3 | 30-40 | 2 | Ductile/creep |
| CFRP (UD) | 1550-1600 | 1000-1500 | 1500-2800 | 135-180 | 950-1800 | 85-115 | Brittle |
| GFRP rebar | 2000-2100 | n/a | 600-1200 | 40-60 | 300-600 | 20-30 | Brittle |
| Hempcrete | 300-400 | 0.3-1.2 | <0.3 | 0.02-0.15 | <1 | <0.5 | Ductile crumble |

## 18.2 Embodied energy and carbon (cradle to gate, typical)

| Material | EE (MJ/kg) | Fossil EC (kg CO₂e/kg) | EC per m³ (kg CO₂e) | Biogenic storage (kg CO₂/kg) |
|---|---|---|---|---|
| Aggregate | 0.1 | 0.005 | ~10 | 0 |
| Rammed earth (unstab.) | 0.05-0.5 | 0.005-0.02 | 10-40 | 0 |
| Rammed earth (cement stab.) | 0.5-1 | 0.04-0.08 | 80-160 | 0 |
| Concrete C30 OPC | 0.9-1.0 | 0.12-0.14 | 280-330 | 0 |
| Concrete C30 50% GGBS | 0.6-0.7 | 0.07-0.09 | 170-210 | 0 |
| Reinforced concrete | 1.8-2.0 | 0.18-0.22 | 450-540 | 0 |
| Portland cement | 4.5-6.5 | 0.85-0.95 | n/a | 0 |
| Lime | 4.5-5.5 | 0.75-0.9 (then reabsorbs) | n/a | 0 |
| Local stone | 0.1-3 | 0.01-0.2 | 30-500 | 0 |
| Imported granite | 10-13 | 0.6-0.8 | 1600-2100 | 0 |
| Fired brick | 2.5-4 | 0.2-0.3 | 380-570 | 0 |
| Plasterboard | 3-7 | 0.25-0.4 | 250-400 | 0 |
| Sawn softwood | 7-10 | 0.2-0.3 | 90-150 | -1.6 to -1.7 |
| Glulam / CLT | 8-12 | 0.3-0.5 | 140-230 | -1.6 |
| Raw bamboo | 1-3 | 0.05-0.2 | 35-140 | -1.6 to -1.8 |
| Straw bale | 0.1-0.3 | 0.01-0.06 | 1-6 | -1.3 to -1.5 |
| Hempcrete (wall) | 1-3 | 0.15-0.3 | 50-100 | -0.4 to -0.6 (per kg wall) |
| Glass (float) | 12-16 | 0.9-1.5 | 2300-3700 | 0 |
| Steel (world avg) | 20-25 | 1.8-2.0 | 14,000-15,700 | 0 |
| Steel (EAF scrap) | 9-13 | 0.5-1.0 | 3,900-7,800 | 0 |
| Stainless steel | 50-80 | 4-7 | 32,000-56,000 | 0 |
| Aluminum (primary avg) | 155-200 | 12-17 | 32,000-46,000 | 0 |
| Aluminum (recycled) | 8-30 | 0.5-1.5 | 1,400-4,000 | 0 |
| Copper | 40-60 | 2.5-4 | 22,000-36,000 | 0 |
| PVC | 60-80 | 2-3.2 | 2,800-4,500 | 0 |
| EPS insulation | 85-90 | 3.3-3.5 | 50-80 (low density) | 0 |
| Mineral wool | 15-20 | 1.1-1.3 | 30-200 | 0 |
| Glass fiber | 25-35 | 1.5-2.5 | n/a | 0 |
| Carbon fiber | 180-600 | 20-40 | n/a | 0 |

## 18.3 Carbon per unit of strength (illustrative index)

Mass-based figures mislead because materials differ hugely in strength and density. A rough functional index: **kg CO₂e per m³ divided by characteristic strength (MPa)**. Lower is better. Fossil carbon only; biogenic storage would push timber and bamboo below zero.

| Material | Compression index | Tension index |
|---|---|---|
| Local granite | ~0.5-2 | ~10-30 |
| Raw bamboo | ~1-2 | ~0.3-1 |
| Unstabilized rammed earth | ~5-10 | ~50-100 |
| Sawn softwood C24 | ~5 | ~7 |
| Concrete C30, 50% GGBS | ~6 | ~60 (unreinforced) |
| Glulam GL28h | ~7 | ~9 |
| GFRP rebar | n/a | ~6-10 |
| Concrete C30 OPC | ~10 | ~100 (unreinforced) |
| Steel S355 (EAF scrap) | ~13 | ~13 |
| Fired brick (unit) | ~15-25 | ~60-120 |
| CFRP | n/a | ~20-30 |
| Tempered glass | n/a | ~25-30 |
| Steel S355 (world average) | ~42 | ~42 |
| Annealed glass | n/a | ~55-60 |
| Aluminum 6061-T6 (primary) | ~115 | ~115 |
| Aluminum 6061-T6 (recycled) | ~8 | ~8 |

**Interpretation**: In pure compression, stone, earth, timber and low-carbon concrete are the most carbon-efficient. In tension, bamboo, timber, recycled steel and GFRP lead. Primary aluminum is the least carbon-efficient structural option. This index ignores buckling, stiffness, durability, fire, connections and lifespan, all of which change real comparisons.

## 18.4 Renewability, effort and end of life

| Material | Raw material class | Regeneration time | Peak process temp (°C) | Effort level | Recyclability | End-of-life fate |
|---|---|---|---|---|---|---|
| Unstabilized earth | A1 | n/a (soil) | Ambient | Very low energy, high labor | Fully reusable | Returns to ground |
| Straw | R1 | 1 yr | Ambient | Very low | Compostable | Biodegrades |
| Hemp | R1 | 4 months | Ambient (lime ~900) | Low | Crushable, reusable as aggregate | Biodegrades/compostable |
| Bamboo | R1 | 3-6 yrs | Ambient | Very low (raw) | Reusable | Biodegrades; energy recovery |
| Cork | R1 | 9 yrs per harvest | ~300 (expanded) | Low | Granulated and reused | Biodegrades |
| Timber | R2 | 25-150 yrs | 60-120 (kiln) | Low-moderate | Reuse, cascade to panels | Energy recovery or decay |
| Local stone | A1 | Geologic | Ambient | Low energy, high labor | Directly reusable | Reuse/crushed aggregate |
| Gypsum | A1/A2 | Geologic | 120-180 | Low | Closed-loop possible | Recycle; landfill risk (H₂S) |
| Lime | A1 | Geologic | 900-1100 | Moderate | Mortar crushable | Reabsorbs CO₂ |
| Fired brick | A1 | Geologic | 900-1250 | Moderate | Reusable if lime mortar | Reuse/crushed aggregate |
| Concrete | A1 (A2 sand) | Geologic | 1450 | Moderate per kg, huge in total | Downcycled to aggregate | Crushed; carbonates over time |
| Glass | A1/A2 | Geologic | 1500-1600 | High | Container yes; flat limited | Mostly downcycled/landfill |
| Mineral wool | A1 | Geologic | ~1500 | Moderate-high | Limited | Landfill |
| Steel | A1 | Geologic | 1500-2300 | High (primary), moderate (scrap) | Infinite closed loop | 85-95% recycled (sections) |
| Copper | A2 | Geologic | ~1200-1300 | High | Infinite | Highly recycled |
| Aluminum | A2 | Geologic | 960 (electrolysis) + 1000 (calcining) | Very high (primary), low (recycled) | Infinite (alloy sorting needed) | Highly recycled |
| Plastics | F | Millions of yrs (fossil) | ~850 (cracking) | High | Technically yes, rarely in practice | Landfill/incineration |
| GFRP | A1 fiber + F resin | n/a | 1200-1400 | Moderate-high | Very poor | Landfill/grinding |
| CFRP | F | n/a | Up to 3000 | Extreme | Very poor (pyrolysis possible) | Landfill/pyrolysis |

## 18.5 Durability and service life

| Material | Typical design life | Main degradation mechanisms | Notable long-lived examples |
|---|---|---|---|
| Stone | 100-1000+ yrs | Salt crystallization, acid rain, frost | Pyramids (~4,500 yrs), Parthenon |
| Fired brick | 100-500+ yrs | Frost, salts, mortar decay | Roman and medieval structures |
| Roman concrete | 2000+ yrs | Very slow; self-healing | Pantheon, Roman harbors |
| Modern reinforced concrete | 50-100 yrs | Rebar corrosion, ASR, sulfate, freeze-thaw | Concrete without steel lasts far longer |
| Steel (protected) | 50-100+ yrs | Corrosion, fatigue | Eiffel Tower (1889, wrought iron, repainted every ~7 yrs) |
| Timber (dry, protected) | 100-1000+ yrs | Fungi, insects, fire | Hōryū-ji temple (Japan, ~1,300 yrs), Norwegian stave churches |
| Earth | 50-1000+ yrs | Water erosion | Shibam mud towers (Yemen, ~500 yrs), sections of Great Wall |
| Bamboo (treated) | 20-50+ yrs | Insects, fungi | Traditional houses in Asia and Latin America |
| Glass | 30-100+ yrs | Seal failure in IGUs, NiS breakage | Medieval stained glass (with lead came) |
| Plastics | 20-50 yrs | UV, plasticizer loss, creep | n/a |

---

# 19. Synthesis

## 19.1 The three strategies for strength

Every building material gets its strength through one of three broad routes:

1. **Grow it** (timber, bamboo, straw, hemp, cork): Biology assembles cellulose nanofibers into hierarchical composites using sunlight, water and atmospheric CO₂ at ambient temperature. The result is the best ratio of strength to energy input and the only route that removes carbon from the atmosphere. Limitations: anisotropy, moisture sensitivity, fire, biological decay and land area.

2. **Burn it** (cement, lime, brick, gypsum, glass): Heat destroys an existing mineral structure (carbonate, hydrate, clay crystal) to create a reactive or molten intermediate, which then rebuilds a new bonded network by hydration, carbonation, sintering or cooling. Process CO₂ from carbonates is the core environmental problem for cement and lime. Strength comes from countless small bonds (C-S-H particle contacts, interlocking crystals, glass bridges) and is limited by flaws and porosity.

3. **Reduce it** (steel, aluminum, copper, titanium): Strip oxygen from metal oxides using carbon or electricity, producing metals whose delocalized bonding allows ductility. Strength is then engineered by controlling dislocation motion through alloying, grain size, precipitates and deformation. These are the most energy-intensive per kg but also the most recyclable.

A fourth route, **dig it and shape it** (stone, earth), uses materials already bonded by geology or by simple capillary forces, requiring mechanical work but little chemistry.

## 19.2 Why concrete dominates despite its carbon

1. **Raw materials are everywhere**: limestone, clay, sand, gravel and water exist on every continent, so concrete is made locally (ready-mix trucks rarely travel more than 30 to 50 km).
2. **Low cost per tonne**: often under US$100 to $150 per m³ in many markets.
3. **Liquid to stone**: it can be poured into any shape on site and hardens without heat.
4. **Compressive strength, mass and stiffness**: ideal for foundations, columns, cores, dams and slabs.
5. **Fire and water resistance**: inherently non-combustible; durable in wet ground where timber rots and steel corrodes.
6. **Synergy with steel**: matched thermal expansion and chemical passivation make reinforced concrete uniquely effective.
7. **Low per-kg embodied energy**: roughly 1 MJ/kg, lower than nearly all manufactured materials except earth and stone. The problem is volume: tens of billions of tonnes per year turns a small per-kg figure into ~8% of global emissions.

## 19.3 Paths to lower-impact concrete
- Lower clinker content (SCMs, LC³, limestone fillers): the largest immediate lever
- Optimized structural design (less over-specification; using concrete only where its properties are needed)
- Higher strength concrete in columns (less volume for the same load)
- Lower w/c with superplasticizers (more strength per kg cement)
- Carbon capture at cement plants
- CO₂ mineralization in concrete and aggregates
- Alternative binders (geopolymers, CSA, carbonatable cements)
- Longer service life through better durability design (cover, low permeability, corrosion-resistant reinforcement)
- Hybrid structures: timber floors on concrete cores, steel-timber composites

## 19.4 Overall ranking by renewability and effort

From most renewable and least effort to least renewable and most effort:

1. Straw, unstabilized earth, raw bamboo, local rubble stone
2. Hemp, cork, mycelium, reed
3. Sawn timber
4. Engineered timber (glulam, CLT), engineered bamboo
5. Local cut stone, gypsum, lime
6. Fired brick
7. Concrete (with SCMs)
8. Concrete (OPC)
9. Recycled steel, recycled aluminum
10. Glass, mineral wool
11. Primary steel, copper
12. Plastics, foam insulation, GFRP
13. Stainless steel
14. Primary aluminum
15. Titanium, carbon fiber composites

## 19.5 Key equations reference

| Concept | Equation |
|---|---|
| Hooke's law | σ = Eε |
| Griffith fracture | σ_f = √(2Eγ/πa) |
| Stress intensity | K = Yσ√(πa) |
| Hall-Petch | σ_y = σ₀ + k_y·d^(-1/2) |
| Taylor hardening | τ = αGb√ρ |
| Orowan bypass | Δτ ≈ Gb/L |
| Powers gel-space ratio | X = 0.68α / (0.32α + w/c); f_c = 234·X³ MPa |
| Abrams' law | f_c = A / B^(w/c) |
| Porosity-strength | f = f₀·e^(-kp) |
| Concrete modulus (ACI) | E_c ≈ 4700√f'_c |
| Modulus of rupture (ACI) | f_r ≈ 0.62√f'_c |
| Confined concrete | f_cc = f'_c + 4.1·f_l |
| Carbonation depth | x = K√t |
| Nurse-Saul maturity | M = Σ(T - T₀)Δt |
| Composite rule of mixtures | E_c = V_f·E_f + V_m·E_m |
| Laplace suction (earth) | ψ = 2γ/r |
| Wood carbon storage | kg CO₂ = 0.5 × m_dry × 44/12 |
| Calcination process CO₂ | 0.786 t CO₂ per t CaO |

---

*Data ranges compiled from standard materials engineering references (Mindess, Young and Darwin, Concrete; Neville, Properties of Concrete; Mehta and Monteiro, Concrete: Microstructure, Properties and Materials; Ashby and Jones, Engineering Materials; Gibson and Ashby, Cellular Solids; USDA Forest Products Laboratory Wood Handbook; Hammond and Jones, Inventory of Carbon and Energy; worldsteel; International Aluminium Institute; GCCA; IEA). Regional and plant-level values vary widely; project-specific Environmental Product Declarations (EPDs) should be used for actual design decisions.*
