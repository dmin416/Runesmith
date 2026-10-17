# Structural Timber and Engineered Wood

> Earth reference / invent loot. Not locked law. Seasoning / aging: `AgingWood.md`. Short kiln chain: `WoodProcessing.md`. Building EE-EC ladder / concrete core: `../../Materials/BuildingMaterials.md`. Weathering: `../../Materials/WeatheringGlassWood.md`. Island trees: `../../Geography/VolcanicIsland/HawaiianNativeLandscape.md`.

Nav: `Index.md`.

Extracted from BuildingMaterials §7 so the EE ladder stays one job and timber science lives with biomaterials.

---

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

