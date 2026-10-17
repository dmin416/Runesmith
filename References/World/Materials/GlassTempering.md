# Glass Tempering and Strengthening

Earth invent. Pack hub: `GlassScience.md`. Making: `GlassMaking.md`. Related: `GlassRelated.md`.

## 7. The Physics of Thermal Tempering

### 7.1 Core Idea

1. Heat the glass uniformly to just above its transition range, where it is soft enough for stress to relax quickly but stiff enough not to deform (about 620 to 650 C for soda-lime).
2. Blow cold air on both faces simultaneously and evenly.
3. The surfaces cool and stiffen first while the interior is still soft and hot.
4. The interior then cools and contracts. The already-rigid surfaces resist this contraction.
5. The interior ends up pulling inward on the surfaces: **surfaces in compression, core in tension**.

### 7.2 Simple Explanation Through Time

| Stage | Surface | Interior | Stress |
|---|---|---|---|
| Start of quench | Cooling fast, contracting | Hot and fluid | Surface briefly in tension; the soft interior flows and relieves it |
| Mid quench | Rigid | Still viscous, relaxing | Stress continually relaxes in the interior |
| Late quench | Cold and rigid | Now passing through transition, contracting more | Interior contraction pulls surfaces into compression |
| Room temperature | Compression | Tension | Permanent residual stress state |

### 7.3 The Parabolic Stress Profile

For a plate tempered from both sides, the residual stress across the thickness is close to a parabola.

Taking z measured from the midplane, h = half-thickness:

```
σ(z) = σ_CT × (1 - 3 × (z/h)²)
```

- At the midplane (z = 0): σ = +σ_CT (central tension).
- At the surface (z = h): σ = -2 × σ_CT (surface compression).
- **Surface compression ≈ 2 × central tension.**
- Stress crosses zero where (z/h)² = 1/3, so z/h = 0.577.
- **Depth of compression ≈ 21 percent of the total thickness from each surface.** A 10 mm pane has about 2.1 mm of compressive layer on each side.

Force balance: the integral of stress across the thickness is zero. The compressed outer layers balance the tensioned core.

### 7.4 The Instant Freeze Model

A first approximation treats glass as fully fluid above a freezing temperature and fully elastic below. If the temperature profile at the moment of freezing is parabolic with a difference ΔT between midplane and surface:

```
σ_surface = -(2/3) × E × α × ΔT / (1 - ν)
σ_center  = +(1/3) × E × α × ΔT / (1 - ν)
```

For soda-lime: E × α / (1 - ν) ≈ 70,000 MPa × 9×10^-6 / 0.78 ≈ 0.81 MPa per kelvin.

| ΔT at freeze | Surface compression | Central tension |
|---|---|---|
| 60 K | about 32 MPa | about 16 MPa |
| 100 K | about 54 MPa | about 27 MPa |
| 150 K | about 81 MPa | about 40 MPa |
| 190 K | about 102 MPa | about 51 MPa |
| 250 K | about 135 MPa | about 67 MPa |

**Key lesson**: residual stress scales with **E × α × ΔT**. Glass with low expansion (borosilicate, fused silica) produces much less stress for the same temperature gradient. Borosilicate can be thermally tempered but reaches only about one-third of the stress of soda-lime under similar conditions. Fused silica cannot be usefully tempered this way.

### 7.5 Viscoelastic Models

Real glass relaxes gradually, not instantly. Accurate tempering models include two effects:

1. **Stress relaxation**: shear stress decays over time according to a stretched exponential or Prony series, with relaxation time τ = η/G.
2. **Structural relaxation**: the glass structure itself (and its volume) depends on thermal history through the fictive temperature. Fast-cooled surfaces have a higher fictive temperature and slightly lower density than the slower-cooled core. This structural mismatch adds roughly 20 to 30 percent of the final stress in typical tempering.

The industry-standard model is the **Narayanaswamy model** (1971, 1978), combining:
- Tool-Narayanaswamy-Moynihan (TNM) structural relaxation
- Thermorheological simplicity (one shift function scales all relaxation times with temperature)
- Viscoelastic stress relaxation

Lee, Rogers and Woo (1965) and Gardon (1960s to 1980) did the foundational modeling of the tempering process.

### 7.6 Heat Transfer Requirements

The temperature difference inside the glass during the quench depends on heat flux and thickness. For a slab of half-thickness L cooled from both faces with conductivity k:

```
ΔT ≈ q × L / (2k)
q = h_c × (T_surface - T_air)
```

Thinner glass needs a much higher heat-transfer coefficient h_c to reach the same internal ΔT.

| Glass thickness | Approximate h needed for full temper (W/m²·K) |
|---|---|
| 19 mm | 70 to 100 |
| 12 mm | 100 to 150 |
| 10 mm | 150 to 200 |
| 6 mm | 250 to 350 |
| 4 mm | 400 to 550 |
| 3.2 mm | 550 to 750 |
| 2 to 2.5 mm | 800 to 1,500+ |

- Thick glass tempers easily with gentle air but must be cooled long enough to avoid breakage from late reheating of the surface by the hot core.
- Thin glass needs high-pressure, closely spaced nozzles. Below about 3 mm conventional air quench becomes very difficult. Specialized processes (high-pressure air, gas bearings, contact quench, liquid or mist quench) are used for 2 mm automotive and solar glass.
- Radiation contributes roughly 50 to 70 W/m²·K at the start of the quench.

### 7.7 Biot Number

```
Bi = h × L / k
```

Tempering works best when the Biot number is moderate. Too low and the glass cools nearly uniformly (no gradient, no temper). The parabolic profile assumption holds well once the quench has run for a short time.

### 7.8 Why Initial Temperature Matters

- Too cold (below about 600 C for soda-lime): the interior is already too stiff. Stresses that form early do not relax; the final compression is low. The glass may also break during the quench from transient tension.
- Correct range (about 620 to 650 C): best combination of relaxation and stiffness. Final stress reaches a plateau.
- Too hot (above about 670 to 680 C): the glass sags, roller marks and distortion increase and optical quality drops.

---

## 8. Industrial Thermal Tempering Process

### 8.1 Steps

1. **Cutting** to final size. Tempered glass cannot be cut afterward.
2. **Edge work**: arrissing (seaming), grinding or polishing. Edge flaws strongly control strength and breakage during the quench.
3. **Drilling and notching**: holes must be at least the glass thickness in diameter and placed away from edges and corners according to fabricator rules (common rules: hole diameter at least equal to thickness, edge distance at least 2 times thickness).
4. **Washing** with deionized water to avoid spots and contaminants that fuse into the surface.
5. **Inspection** for defects.
6. **Heating** in a furnace.
7. **Quenching** with air jets.
8. **Cooling** to room temperature.
9. **Quality testing**: stress measurement, fragmentation test on samples, flatness and distortion checks.
10. **Heat soak test** (optional, for NiS risk).
11. **Marking** with a permanent logo or "bug" required by safety glazing codes.

### 8.2 Furnace Types

| Type | Heating method | Use |
|---|---|---|
| Horizontal roller hearth, radiant | Electric elements radiate onto glass on ceramic rollers | Standard clear glass |
| Forced convection | Hot air jets plus radiation | Low-E coated glass that reflects infrared, faster and more uniform heating |
| Vertical (tong) | Glass hangs from tongs | Older method; leaves tong marks and edge distortion |
| Gas hearth (air float) | Glass floats on a cushion of hot gas | Thin glass, high optical quality, bending |

**Heating time rule of thumb**: about 35 to 45 seconds per millimeter of thickness in a radiant furnace. A 6 mm pane might heat for about 220 to 260 seconds. Furnace temperatures typically run around 680 to 720 C with glass exit temperatures of about 620 to 650 C.

**Low-E coatings** reflect infrared, so radiant-only furnaces heat the coated side slowly. This causes bow and breakage. Convection heating fixes it.

### 8.3 Quench Section

- Arrays of nozzles above and below the glass deliver air at high velocity.
- Blowers or compressors supply pressures from a few kPa (thick glass) to over 20 kPa (thin glass).
- The glass oscillates back and forth under the nozzles to even out cooling and avoid strain patterns.
- Top and bottom cooling must be balanced. An imbalance bends the glass because one side ends up more compressed than the other.
- Quench time is short for the initial freeze (seconds) followed by a longer cooling phase.

### 8.4 Process Defects

| Defect | Cause | Effect |
|---|---|---|
| **Roller wave** | Hot glass sagging between rollers | Optical distortion visible in reflection |
| **Edge kink / edge lift** | Edges sagging or curling at the leading and trailing ends | Distortion near edges, problems in insulating glass units |
| **Bow and warp** | Uneven heating or quench top vs bottom | Pane not flat |
| **Anisotropy (quench marks, "leopard spots", iridescence)** | Stress varies in a pattern matching nozzle layout, causing birefringence | Dark or rainbow patterns visible under polarized light (sky light, polarized sunglasses) |
| **Roller pick-up** | Glass particles or contaminants stuck to rollers | Small surface marks |
| **White haze** | Rollers contaminated or SO2 reactions | Surface haze |
| **Breakage in quench** | Edge flaws, too cold, inclusions, poor hole quality | Lost product |

Anisotropy cannot be completely eliminated in thermally tempered glass. It is a natural consequence of jet cooling. Modern measurement systems scan every pane and grade it.

### 8.5 Bending and Tempering

Automotive side and rear windows are bent and tempered in one heat. The glass is heated, pressed or sag-bent to shape on a mold, then quenched immediately. Windshields are usually bent in pairs, slowly cooled (annealed) and laminated rather than tempered.

---

## 9. Annealed vs Heat-Strengthened vs Fully Tempered

| Property | Annealed | Heat-strengthened (HS) | Fully tempered (FT) |
|---|---|---|---|
| Surface compression | about 0 to 5 MPa | 24 to 52 MPa (ASTM C1048) | at least 69 MPa (10,000 psi) per ASTM C1048 (edge at least 67 MPa); commonly 90 to 150 MPa |
| Approximate bending strength relative to annealed | 1 | about 2 | about 4 to 5 |
| EN characteristic bending strength (float) | 45 MPa | 70 MPa | 120 MPa |
| Thermal shock resistance (approx.) | 40 to 60 C | 100 to 150 C | 200 to 250 C |
| Break pattern | Long sharp shards radiating from impact | Larger pieces running edge to edge, tends to stay in frame | Small cube-like dice |
| Safety glazing? | No | No | Yes (meets impact standards) |
| Can be cut after treatment? | Yes | No | No |
| NiS spontaneous breakage risk | Essentially none | Very low | Present (reduced by heat soak) |
| Optical distortion | Lowest | Low | Higher |

**Why heat-strengthened glass exists**: it is roughly twice as strong as annealed glass but breaks into large pieces that tend to stay in the frame. In laminated overhead glazing this is often preferred, because a laminated pair of fully tempered lites can collapse like a wet blanket once both break, while broken heat-strengthened lites interlock and carry some load.

---

## 10. Fragmentation: Why Tempered Glass Dices

### 10.1 Stored Elastic Energy

A tempered pane is a loaded spring. With the parabolic profile and equal biaxial stress, the stored strain energy per unit area of a pane of thickness t is:

```
U/A = 0.8 × (1 - ν) × σ_CT² × t / E
```

Example: 6 mm soda-lime with σ_CT = 50 MPa:

U/A ≈ 0.8 × 0.78 × (50×10^6)² × 0.006 / (70×10^9) ≈ 134 J/m²

That energy is about 30 to 40 times what is needed to create the new fracture surfaces in a coarse break, so once a crack reaches the tensile core it branches repeatedly.

### 10.2 What Happens When It Breaks

1. A flaw or impact drives a crack through the compressive surface layer into the tensile core.
2. The crack runs through the core at roughly terminal velocity, about 1.5 km/s.
3. Released stored energy causes repeated branching.
4. The whole pane fractures in milliseconds into small, relatively blunt fragments.

Fragments are not truly harmless (they can cut) but they are far less dangerous than long annealed shards.

### 10.3 Fragmentation Tests

- **EN 12150-1**: break the specimen with a pointed hammer or center punch. Count fragments in a 50 mm × 50 mm square in the coarsest region. Minimum counts for soda-lime float: 15 for 3 mm thickness, 40 for 4 to 12 mm, 30 for 15 to 19 mm. The longest fragment must not exceed 100 mm.
- **ANSI Z97.1 / CPSC**: the ten largest crack-free particles collected within a set time after breakage must weigh no more than the equivalent of 10 square inches (6,450 mm²) of the original specimen.

Fragment size decreases sharply as central tension rises. Particle count is used in production as a practical check that the glass reached full temper.

### 10.4 Breakage Without Visible Cause

Tempered glass has a "self-destruct" mode. A chip or scratch that penetrates the compression layer can cause the whole pane to burst later, sometimes long after the damage. Common triggers:
- Edge damage during installation
- Contact with metal frames or fasteners
- Nickel sulfide inclusions (Section 11)
- Severe thermal stress at a damaged edge
- Oven door glass, shower doors and table tops cracking under thermal cycling plus edge damage

---

## 11. Nickel Sulfide Inclusions and Spontaneous Breakage

### 11.1 The Mechanism

- Nickel (often from stainless steel or nickel alloy contamination in batch or cullet) combines with sulfur (from sodium sulfate fining) to form tiny **NiS** particles.
- Typical size: about 0.04 to 0.6 mm diameter, often invisible to the eye.
- NiS has two crystal forms:
  - **α-NiS**: high-temperature form, stable above about 379 C.
  - **β-NiS (millerite)**: low-temperature form.
- During tempering, the glass is heated above 379 C (NiS converts to α) then quenched so fast that the α form is trapped.
- At room temperature the α form slowly transforms to β over months or years, expanding about 2 to 4 percent in volume.
- If the inclusion sits in the **tensile core**, this expansion generates enough local stress to start a crack. The stored energy then shatters the entire pane.
- Inclusions in the compressive surface layer are generally harmless. Annealed glass is rarely affected because there is no tensile core and the slow cooling already converts NiS to β.

### 11.2 Signature

The fracture origin shows a characteristic **"butterfly" or "figure 8"** pattern: two large adjacent fragments around a small particle, visible under magnification.

### 11.3 Heat Soak Testing

- Tempered panes are reheated and held at a temperature that accelerates the α to β transformation, so susceptible panes break in the factory instead of on the building.
- **EN 14179**: hold at 290 C ± 10 C for 2 hours (glass temperature).
- Heat soaking reduces but does not completely remove the risk. Residual failure rate after EN 14179 is commonly cited around one breakage per 400 tonnes of glass.
- Heat soaking too hot (above about 320 C) can reverse the transformation and is avoided.
- **Alternative**: use heat-strengthened glass where possible, because its lower central tension makes NiS breakage much less likely.

---

## 12. Chemical Strengthening (Ion Exchange)

### 12.1 Principle

Glass is immersed in a molten potassium nitrate (KNO3) bath below its strain point. Smaller sodium ions (Na+, radius about 102 pm in six-fold coordination) in the glass surface swap places with larger potassium ions (K+, about 138 pm) from the salt.

```
Na+ (glass) + K+ (melt) ⇌ K+ (glass) + Na+ (melt)
```

Because this happens below the strain point, the network cannot relax to accommodate the larger ions. The surface is **"stuffed"**, producing very high compressive stress.

### 12.2 Typical Conditions

| Parameter | Soda-lime glass | Aluminosilicate cover glass |
|---|---|---|
| Bath | 99+ percent KNO3 | KNO3 (single step) or NaNO3/KNO3 mixes (multi-step) |
| Temperature | 400 to 470 C | 380 to 450 C |
| Time | 4 to 24+ hours | 1 to 16 hours |
| Surface compressive stress (CS) | about 300 to 600 MPa | about 700 to 1,000+ MPa |
| Depth of layer (DOL) | about 10 to 25 µm | about 30 to 100 µm (K for Na); up to about 150 µm or more with Li-based glass |

KNO3 melts at 334 C. It begins decomposing to nitrite and oxygen as temperatures climb toward 500 to 550 C, so baths are kept below that range.

### 12.3 Physics of the Stress

Ideal stress from network dilation:

```
σ(z) = -[ B × E / (1 - ν) ] × [ C(z) - C_avg ]
```

- B = linear network dilation coefficient (how much the network expands per unit concentration of exchanged ions).
- C(z) = concentration of the invading ion at depth z.
- The stress profile follows the diffusion profile, roughly a complementary error function, not a parabola.

**Diffusion depth**:

```
DOL ≈ k × sqrt(D × t)
```

- Interdiffusion coefficient D for K/Na exchange at about 420 C: roughly 10^-15 to 10^-14 m²/s in aluminosilicate glass, an order of magnitude lower in soda-lime.
- Doubling DOL requires four times the time.
- Longer times or higher temperatures allow stress relaxation, which lowers CS. Every process is a compromise between CS and DOL.

### 12.4 Why Aluminosilicate Works So Well

- Al2O3 opens the network and gives fast Na+ mobility, so ions diffuse deeper in less time.
- Al2O3 also raises the strain point, reducing stress relaxation during exchange.
- Low CaO and MgO: alkaline earth ions block alkali diffusion paths.
- B2O3 and P2O5 additions in some grades improve damage resistance (crack initiation resistance) through more compliant structures.

### 12.5 Lithium-Containing Glasses and Two-Step Exchange

- Newer cover glasses contain Li2O.
- In a sodium-rich bath, Li+ (small) is replaced by Na+, giving a deep compressive layer (often 100 to 150+ µm).
- A second bath rich in potassium adds a thin, very high-stress "spike" at the surface (K for Na).
- Result: a profile with both high surface stress (resists scratches and sharp contact) and deep compression (resists drops onto rough surfaces, where flaws penetrate tens of micrometers).

### 12.6 Advantages and Limits

| Chemical strengthening | Thermal tempering |
|---|---|
| Works on very thin glass (down to about 30 µm ultra-thin glass for foldable displays) | Practical limit about 2 to 3 mm |
| Very high surface stress (500 to 1,000+ MPa) | Surface stress about 70 to 150 MPa |
| Shallow layer (micrometers) | Deep layer (about 21 percent of thickness) |
| No optical distortion or anisotropy pattern | Roller wave and quench patterns |
| Works on complex shapes | Best on flat or simply bent glass |
| Slow and more expensive | Fast and cheap |
| Deep scratches can penetrate the layer | Deep compression tolerates deeper damage |
| Can be cut in limited ways if CT is low | Cannot be cut |
| Fragmentation depends on central tension; low CT glass breaks like annealed glass | Dices |

### 12.7 Frangibility in Ion-Exchanged Glass

If central tension in thin chemically strengthened glass exceeds a threshold (which depends on thickness, roughly tens of MPa for 0.5 to 1 mm glass), the glass becomes **frangible** and explodes into many small pieces like tempered glass. Cover glass designers stay just below this limit.

### 12.8 Other Ion Exchange Uses

- **Gradient-index (GRIN) lenses**: Ag+ or Tl+ exchange changes refractive index locally.
- **Optical waveguides**: Ag+/Na+ exchange writes light-guiding channels into glass.
- **Antimicrobial glass**: Ag+ ions in the surface.

---

## 13. Other Strengthening and Safety Methods

### 13.1 Laminated Glass

- Two or more glass plies bonded with a polymer interlayer under heat and pressure in an autoclave (typically about 130 to 140 C and 10 to 14 bar).
- Interlayers:
  - **PVB** (polyvinyl butyral): standard for windshields and architectural glass, typically 0.38 mm, 0.76 mm or 1.52 mm thick.
  - **Ionoplast (SGP)**: about 100 times stiffer than PVB at room temperature and about 5 times stronger in tear, used for structural glass floors, stairs, balustrades and hurricane glazing.
  - **EVA**: used in some architectural and solar products, more moisture-tolerant edges.
  - **TPU** and polycarbonate composites in security and bullet-resistant glazing.
- Laminated glass is not stronger than an equal monolithic thickness before breakage in most cases. After breaking the fragments stick to the interlayer and the opening stays closed.
- Edouard Benedictus patented laminated glass after a 1903 lab accident with a cellulose nitrate-coated flask that cracked but held together.

### 13.2 Bullet-Resistant and Blast Glazing

- Multiple glass layers bonded to polycarbonate or other polymer backing.
- Hard glass faces blunt and break up the projectile; polymer layers absorb energy and stop spall.
- Standards: UL 752 (US levels 1 to 10), EN 1063, NIJ 0108.01.
- High-end transparent armor uses ALON, spinel or sapphire strike faces to cut weight.

### 13.3 Acid Etching and Flaw Blunting

- Hydrofluoric acid (HF) dissolves a thin layer of glass, removing or blunting surface flaws.
- Strength of etched glass can rise several-fold, sometimes approaching 1 GPa or more in small specimens, until new damage occurs.
- Often combined with ion exchange or used on thin display glass edges.
- HF is acutely toxic and penetrates skin, binding calcium; industrial use is strictly controlled.

### 13.4 Fire Polishing and Edge Finishing

- Melting the surface with a flame heals scratches and rounds crack tips.
- Polished edges are much stronger than as-cut edges.
- Laser cutting and laser edge treatment produce cleaner edges than mechanical scoring.

### 13.5 Coatings

- Hot-end coatings on bottles (tin oxide or titanium oxide applied while the bottle is hot) plus cold-end lubricious coatings (polyethylene or stearates) reduce scratch damage during handling.
- Polymer coatings on optical fibers protect pristine strength.
- Hard coatings (sapphire-like or diamond-like carbon) improve scratch resistance on some lenses and displays.

### 13.6 Dual-Phase and Composite Glazing

- Glass-polycarbonate laminates for lightweight impact resistance.
- Glass fibers in polymers (fiberglass) use the very high strength of thin glass fibers in a tough matrix.

### 13.7 Fiber Strength

| Fiber | Tensile strength (pristine, room temperature) |
|---|---|
| E-glass | about 3.4 GPa |
| S-glass / S-2 | about 4.6 to 4.9 GPa |
| R-glass | about 4.4 GPa |
| Silica optical fiber | about 5 to 6 GPa in air; up to about 14 GPa in liquid nitrogen |

Thin fibers are strong because a short, thin specimen has very little surface for a large flaw to occupy and because the fiber is formed and coated before damage can occur.

---

## 14. Measuring Stress in Glass

### 14.1 Photoelasticity

Stress makes glass birefringent: light polarized along the two principal stress directions travels at different speeds.

```
δ = C × (σ1 - σ2) × d
```

- δ = optical retardation (nm), d = path length, C = stress-optic coefficient.
- Soda-lime: C ≈ 2.6 to 2.7 Brewster (10^-12 Pa^-1), equivalent to about 2.6 to 2.7 nm per cm per MPa.
- Borosilicate about 3.9 to 4.0 Brewster; fused silica about 3.4 to 3.5 Brewster.

**Crossed polarizers (polariscope)**: placing glass between two polarizing filters at 90 degrees reveals stress as bright or colored fringes. Annealed glass stays dark. Tempered glass shows patterns matching the quench nozzles. Polarized sunglasses viewing a car's rear window often show these patterns.

### 14.2 Surface Stress Instruments

| Instrument | Principle | Used for |
|---|---|---|
| **GASP / differential surface refractometer** | Grazing angle surface polarimetry, light guided along the surface | Thermally tempered and heat-strengthened glass |
| **SCALP** | Scattered light polarimetry through the thickness | Full stress profile, thermal or chemical |
| **FSM (surface stress meter)** | Waveguide mode spectroscopy in the ion-exchanged layer | CS and DOL of chemically strengthened glass |
| **Edge stress meter** | Birefringence measured through the edge | Edge compression in tempered and annealed glass |
| **Strain viewer / polariscope** | Qualitative birefringence | Annealing checks in glassblowing and lampwork |

Tin side vs air side: float glass has a few micrometers of tin diffused into its bottom surface. The tin side fluoresces under short-wave UV, which is how fabricators identify it. The tin side affects refractive-index-based stress measurement and ion exchange behavior.

### 14.3 Strength Testing

- **Ring-on-ring (coaxial double ring), EN 1288-5 / ASTM C1499**: biaxial bending, tests surface not edges.
- **Four-point bending, EN 1288-3**: tests edges and surface.
- **Ball drop tests**: impact resistance.
- **Pendulum (soft body impact)**: safety glazing.
- **Vickers indentation**: crack initiation resistance and fracture toughness estimates.

---

## 15. Standards and Design Values

### 15.1 Common Standards

| Standard | Subject |
|---|---|
| ASTM C1048 | Heat-strengthened and fully tempered flat glass |
| ASTM C1036 | Flat (annealed) glass |
| ASTM C1172 | Laminated architectural glass |
| ASTM E1300 | Load resistance of glass in buildings |
| ASTM C1279 | Measuring edge and surface stress by photoelasticity |
| ANSI Z97.1 | Safety glazing in buildings |
| CPSC 16 CFR 1201 | US federal safety glazing standard (Category I and II impact) |
| ANSI Z26.1 / FMVSS 205 | Automotive glazing |
| EN 572 | Basic soda-lime glass products |
| EN 1863 | Heat-strengthened glass |
| EN 12150 | Thermally toughened soda-lime safety glass |
| EN 14179 | Heat-soaked thermally toughened glass |
| EN 12337 | Chemically strengthened glass |
| EN 14449 / EN ISO 12543 | Laminated glass |
| EN 12600 | Pendulum impact test |
| EN 16612 | Design of glass panes for lateral loads |
| EN 1288 | Bending strength test methods |

### 15.2 Safety Glazing Impact Tests

- **CPSC 16 CFR 1201**: a 100 lb (45 kg) leather punching bag filled with lead shot swings into the glass. Category I = 150 ft·lbf (impact from 18 inches), Category II = 400 ft·lbf (48 inches).
- **EN 12600**: a 50 kg twin-tire impactor dropped from 190 mm (class 3), 450 mm (class 2) or 1,200 mm (class 1).
- Glass passes by not breaking, breaking safely (tempered fragments within limits) or breaking but remaining intact (laminated).

### 15.3 Design Values

**EN characteristic bending strengths**:

| Product | f_k |
|---|---|
| Annealed float (EN 572) | 45 MPa |
| Heat-strengthened float (EN 1863) | 70 MPa |
| Heat-strengthened patterned | 55 MPa |
| Toughened float (EN 12150) | 120 MPa |
| Toughened patterned | 90 MPa |
| Chemically strengthened (EN 12337) | 150 MPa |

**ASTM E1300 glass type factors** (relative to annealed, single lite):

| Glass | Short duration (3 s) | Long duration (30 days) |
|---|---|---|
| Annealed | 1.0 | 0.5 |
| Heat-strengthened | 2.0 | 1.3 |
| Fully tempered | 4.0 | 3.0 |

ASTM E1300 designs for a probability of breakage of 8 per 1,000 for vertical glass at first application of the design load.

### 15.4 Identifying Tempered Glass

- **Permanent mark ("bug")** in a corner listing the manufacturer and standard. US safety glazing codes require it.
- **Polarized sunglasses** reveal quench patterns.
- **Edges** are usually ground or seamed, never raw cut.
- **Slight roller wave** distortion in reflection.
- A **surface stress meter** gives a definitive answer.

---
