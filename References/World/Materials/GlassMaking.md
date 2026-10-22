# Glass Making: Industrial and Workshop

Earth invent. Pack hub: `GlassScience.md`. Tempering: `GlassTempering.md`. Related: `GlassRelated.md`. Craft overview: `TranslucentMaterials.md`. Silica feed: `MaterialPurification.md`, `../Science/Metallurgy/SilicaSand.md`.

## 16. How Glass Is Made

### 16.1 Raw Materials for Soda-Lime Glass

| Material | Chemical | Supplies | Notes |
|---|---|---|---|
| Silica sand | SiO2 | Network former | Low-iron sand for clear glass (under about 0.02 percent Fe2O3 for extra-clear) |
| Soda ash | Na2CO3 | Na2O (flux) | Releases CO2 |
| Limestone | CaCO3 | CaO (stabilizer) | Releases CO2 |
| Dolomite | CaMg(CO3)2 | CaO and MgO | Releases CO2 |
| Feldspar or nepheline syenite | (Na,K)AlSi3O8 | Al2O3, alkalis | Improves durability |
| Salt cake | Na2SO4 | Fining agent | Releases SO2 and O2 bubbles |
| Cullet | Recycled glass | Everything | Melts easier, lowers energy |
| Decolorizers and colorants | Se, Co, CeO2, Fe2O3 etc. | Color control | |

**Why each oxide is needed**:
- Silica alone melts above 1,700 C and is extremely viscous.
- Soda (Na2O) drops the melting temperature dramatically but makes the glass water-soluble ("water glass").
- Lime (CaO) restores chemical durability.
- Magnesia and alumina improve durability and reduce devitrification.

### 16.2 Batch Reactions

On heating, carbonates react with silica and release CO2:

```
Na2CO3 + SiO2 → Na2SiO3 + CO2↑     (begins about 700 to 900 C)
CaCO3 → CaO + CO2↑                 (about 800 to 900 C)
CaO + SiO2 → CaSiO3
Na2SO4 + C → Na2SO3 + CO           (with reducing agents)
```

Low-melting alkali-rich silicate liquids form first and dissolve the remaining sand grains.

About 15 to 20 percent of the batch mass leaves as gas. For every tonne of glass, roughly 0.15 to 0.2 tonnes of CO2 come from carbonate decomposition alone, before counting fuel combustion.

### 16.3 Melting Stages

1. **Batch melting** (about 1,100 to 1,400 C): reactions, sand dissolution.
2. **Fining** (about 1,450 to 1,550 C): bubbles rise and escape. Sulfate releases SO2 and O2 that grow small bubbles so they rise faster (Stokes' law: rise velocity scales with radius squared).
3. **Homogenization**: convection currents and stirring remove cords (streaks of different composition).
4. **Conditioning**: the melt cools to forming temperature, about 1,050 to 1,200 C.

**Furnace types**: regenerative cross-fired and end-port furnaces (natural gas plus preheated air, about 1,500 to 1,600 C crown temperatures), oxy-fuel furnaces, all-electric melters, hybrid electric boosting. Large float furnaces hold about 1,500 to 2,500 tonnes of molten glass and produce 500 to 1,000+ tonnes per day continuously for 15 to 20 years.

**Refractories**: fused-cast AZS (alumina-zirconia-silica), silica crowns, high-zirconia blocks contact the melt.

### 16.4 Forming Methods

| Method | Product | Principle |
|---|---|---|
| **Float process** | Flat glass (window, architectural, automotive) | Melt flows onto molten tin bath |
| **Fusion draw (overflow downdraw)** | Display glass, cover glass | Glass overflows both sides of a trough and fuses below; surfaces never touch anything |
| **Slot downdraw** | Thin glass | Glass drawn through a slot |
| **Rolling** | Patterned, wired, solar glass | Glass passes between textured rollers |
| **Blow and blow / press and blow** | Bottles, jars | Individual section (IS) machines |
| **Pressing** | Lenses, tableware, TV funnels | Glass pressed into molds |
| **Tube drawing (Danner, Vello)** | Tubing, rods | Glass drawn around a mandrel |
| **Fiber drawing** | Insulation, reinforcement, optical fiber | Bushings or preform drawing |
| **Hand blowing and lampworking** | Art, scientific glass | Gathered or flame-worked glass |
| **Casting** | Large optics, art | Glass poured into molds |

### 16.5 The Float Process in Detail

- Invented by Alastair Pilkington and Kenneth Bickerstaff; idea about 1952, commercially successful from 1959.
- Molten glass at about 1,100 C pours onto a bath of molten tin in a nitrogen-hydrogen atmosphere (to prevent tin oxidation).
- Tin is used because it is liquid across the needed range (melting point 232 C, boiling point about 2,600 C), is denser than glass (glass floats) and does not react strongly with glass under reducing conditions.
- Glass spreads until gravity and surface tension balance at an **equilibrium thickness of about 6 to 7 mm**.
- **Top rollers** grip the edges and stretch the ribbon thinner (down to about 0.4 mm) or hold it back for thicker glass (up to about 25 mm).
- The ribbon leaves the bath at about 600 C, stiff enough to touch rollers.
- Both surfaces are fire-flat, needing no grinding or polishing. Before float glass, plate glass needed costly grinding and polishing on both sides.
- The ribbon then enters the **annealing lehr**, a long tunnel where it cools slowly through the annealing and strain range.

### 16.6 Annealing

**Purpose**: remove the stresses that form when glass cools unevenly.

Two stages:
1. Hold at or slightly above the annealing point so existing stresses relax (minutes at 10^12 Pa·s).
2. Cool slowly through the range down to the strain point so no new permanent stress forms.
3. Below the strain point, cool faster (stresses that form are temporary and disappear at room temperature), limited only by thermal shock risk.

**Residual stress from annealing scales with cooling rate × thickness²**. Under a constant cooling rate r, the temperature difference between mid-plane and surface of a slab of thickness t is approximately:

```
ΔT ≈ r × t² / (8 × κ)
```

where κ = thermal diffusivity (about 4 to 5×10^-7 m²/s for glass). Doubling thickness requires cooling about four times slower to get the same stress.

### 16.7 Color in Glass

| Colorant | Color |
|---|---|
| Fe2+ (ferrous) | Blue-green; absorbs near-infrared |
| Fe3+ (ferric) | Yellow-brown, weak |
| Fe + S (reduced) | Amber (bottle glass) |
| Co2+ | Intense blue |
| Cr3+ | Green |
| Cu2+ | Blue to blue-green |
| Cu nanoparticles | Ruby red (copper ruby) |
| Au nanoparticles | Ruby red to pink (gold ruby, purple of Cassius) |
| Ag nanoparticles | Yellow (silver stain) |
| Mn3+ | Purple |
| Ni2+ | Brown to gray-purple |
| Se | Pink; in small amounts cancels green iron tint (decolorizing) |
| Nd3+ | Lavender with sharp absorption lines (welding and glass-blowing eyewear) |
| Er3+ | Pink |
| U (uranium glass) | Yellow-green, fluoresces bright green under UV |
| CdS/CdSe | Yellow, orange and red (striking colors) |

Green edges on window glass come from ferrous iron. "Low-iron" or "extra-clear" glass reduces iron to minimize that tint for solar panels, display cases and aquariums.

### 16.8 Recycling

- Cullet melts at lower energy than raw batch. Each 10 percent cullet addition saves roughly 2.5 to 3 percent of melting energy.
- Recycled glass also eliminates the CO2 released from carbonates.
- Glass can be remelted indefinitely without degradation in quality if sorted by color and kept free of ceramics, stones and heat-resistant glass (which do not melt properly in soda-lime furnaces and cause defects).

---

## 17. Small-Scale and Workshop Methods

### 17.1 Melting a Soda-Lime Glass From Raw Materials

**Target composition (weight percent)**: 72 SiO2, 14 Na2O, 10 CaO, 3 MgO, 1 Al2O3.

**Conversion factors** (raw material mass per unit oxide mass):

| Raw material | Oxide | Factor |
|---|---|---|
| Na2CO3 (soda ash, MW 105.99) | Na2O (61.98) | 1.710 |
| CaCO3 (MW 100.09) | CaO (56.08) | 1.785 |
| MgCO3 (MW 84.31) | MgO (40.30) | 2.092 |
| K2CO3 (MW 138.21) | K2O (94.20) | 1.467 |
| H3BO3 (MW 61.83) | B2O3 (69.62) | 1.776 (per B2O3, two moles of acid) |
| Al(OH)3 (MW 78.00) | Al2O3 (101.96) | 1.530 |

**Batch for 100 g of glass**:

| Ingredient | Mass |
|---|---|
| Silica (fine quartz sand or flint) | 72.0 g |
| Soda ash | 23.9 g |
| Calcium carbonate | 17.9 g |
| Magnesium carbonate | 6.3 g |
| Alumina (or 1.5 g aluminum hydroxide) | 1.0 g |
| Sodium sulfate (fining) | 0.3 to 0.5 g |
| **Total batch** | about 121.5 g |
| CO2 lost | about 21 g |

**Process**:
1. Mix dry ingredients thoroughly.
2. Fill a crucible (alumina, fireclay or for lab work platinum) no more than half full to allow foaming.
3. Melt at 1,450 to 1,500 C for 2 to 4 hours; add batch in portions if foaming is heavy.
4. Pour onto a preheated steel or graphite plate, or into a mold.
5. Move immediately to an annealing kiln at about 540 to 550 C, hold, then cool slowly.

**Lower-melting option**: most hobby kilns top out around 1,260 to 1,300 C. Replacing some silica and lime with boric oxide and more alkali (sodium borosilicate) lets the glass melt at 1,100 to 1,250 C. Another route is to melt purchased cullet or frit, which needs about 1,100 to 1,200 C.

### 17.2 Annealing Schedules (Typical)

| Glass type | Annealing soak | Cool to | Notes |
|---|---|---|---|
| Soda-lime (bottle, float) | 540 to 550 C | 480 C slowly, then faster | Strain point about 510 C |
| COE 90 / COE 96 fusing glass | 482 to 516 C (900 to 960 F) | 370 C (700 F) slowly | Manufacturer charts by thickness |
| COE 104 soft glass (lampworking) | about 510 to 520 C | slowly through about 400 C | |
| Borosilicate 3.3 | 560 to 570 C | slowly through about 480 C | |

**Thickness rule**: soak time and cooling rate depend strongly on thickness. Typical fusing guidance for 6 mm uniform pieces: soak about 1 hour at the annealing temperature, then cool around 50 to 80 C per hour through the strain range. Doubling thickness requires roughly 4 times slower cooling.

### 17.3 Checking Annealing at Home

Place the glass between two linear polarizing sheets rotated 90 degrees to each other, in front of a light. Well-annealed glass looks uniformly dark. Bright halos, colored fringes or bands show residual stress.

### 17.4 Prince Rupert's Drops

- Drip molten soda-lime glass from a rod or gather into cold water.
- The surface freezes instantly; the interior solidifies later and pulls the surface into very high compression.
- Measured surface compression is roughly 400 to 700 MPa (Aben, Chaudhri and colleagues, 2016 to 2017), much higher than commercial tempered glass, because the quench is extremely severe and the shape is compact.
- The head resists hammer blows and even low-velocity bullets.
- Breaking the thin tail lets a crack reach the tensile core; the whole drop explodes into powder in microseconds.
- Typical yield: many drops crack during the quench or contain bubbles; borosilicate and soda-lime rods both work, with soda-lime giving more dramatic results.

### 17.5 Bologna Flask (Bologna Phial)

- A thick-walled, unannealed glass flask with the outside in compression and the inside in tension.
- It survives blows on the outside.
- Dropping a small sharp flint or quartz chip inside scratches the tensile inner surface and the flask shatters.
- An 18th-century demonstration that strength depends on where flaws sit relative to stress.

### 17.6 Small-Scale Thermal Tempering

Requirements for a workshop setup:
1. Glass at least 4 to 6 mm thick (thinner needs very high air flow).
2. Final edges and holes finished before treatment.
3. Uniform heating to about 620 to 650 C (soda-lime) in a kiln, typically with the glass supported on a few points or a ceramic-fiber surface to limit marking.
4. Rapid transfer (a few seconds) to a quench station.
5. Opposed manifolds of air nozzles on both faces, equal pressure top and bottom, typically fed by a large blower or compressed air at several hundred kPa through many small holes spaced about 20 to 40 mm apart and set about 20 to 40 mm from the glass.
6. Oscillate the glass or nozzles to even out cooling.
7. Continue blowing until the glass is below about 300 C.

Testing: polariscope inspection (pattern of spots matching nozzles indicates tempering) and breaking a test piece to check the fragment count against EN 12150 numbers.

Practical constraints: uneven quench gives bow or breakage; heating too long gives sag and marks; heating too short gives low stress.

### 17.7 Small-Scale Chemical Strengthening

1. Clean glass thoroughly (no oils or organic residue).
2. Preheat glass in a kiln to near bath temperature to avoid thermal shock.
3. Melt technical-grade KNO3 in a stainless steel or ceramic container at about 420 to 450 C.
4. Immerse glass fully for several hours (soda-lime: 8 to 24 hours for useful depth).
5. Remove, cool slowly, rinse off salt with warm water.
6. Check with a scratch-then-flex test or a ring-on-ring test against untreated samples.

Process notes:
- Water or wet items contacting molten salt cause violent spattering; everything entering the bath must be dry and preheated.
- Molten nitrate is a strong oxidizer; organic material in contact with it can ignite.
- Sodium builds up in the bath with use ("poisoning") and lowers achievable stress; replace or replenish KNO3 periodically.
- Results on soda-lime glass typically double to quadruple flexural strength in coupon tests, with a thin layer that deep scratches can penetrate.

### 17.8 Lampworking and Thermal Compatibility

- **COE (coefficient of expansion)** numbers in art glass (90, 96, 104, 33) are expansion × 10^7 per C. COE 33 is borosilicate (3.3×10^-6/K).
- Different glasses fused together must match expansion closely (typically within about 1 to 2 units for fusing glass, ideally tested for compatibility) or cooling creates stress that cracks the piece.
- A "seal" between glasses of different expansion can be graded through intermediate glasses (graded seals in scientific glassblowing).

---
