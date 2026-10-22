# Glass Tempering, Glass Strength and Related Brittle Materials

Earth invent / technical reference. What glass is, why it breaks, tempering and other strengthening, how glass is made, and how it compares with glass-ceramics, transparent ceramics, polymers, metallic glasses and dental ceramics.

**Owns:** glass structure, families, viscosity landmarks, fracture mechanics, thermal shock, pack index. Tempering / standards / stress measurement → `GlassTempering.md`. Furnace and workshop making → `GlassMaking.md`. Glass-ceramics, kin materials, natural glass, history, facts, worked calcs → `GlassRelated.md`.

**Companions:** Craft / sources overview: `TranslucentMaterials.md`. Structural EE/EC: `BuildingMaterials.md`. Weathering: `WeatheringGlassWood.md`. Silica feed: `MaterialPurification.md`, `../Science/Metallurgy/SilicaSand.md`. Optics: `../Science/Energy/Optics.md`. Thermometers: `../Science/Metallurgy/Thermometers.md`. Hub: `Index.md`.

## Pack

| File | Holds |
|---|---|
| This file | §§1–6: what glass is, families, viscosity, fracture, statistics, thermal shock |
| [GlassTempering.md](GlassTempering.md) | §§7–15: thermal tempering, chemical strengthen, laminated, stress measurement, standards |
| [GlassMaking.md](GlassMaking.md) | §§16–17: industrial making, float, annealing, workshop methods |
| [GlassRelated.md](GlassRelated.md) | §§18–25: glass-ceramics, kin materials, natural/bio, history, facts, calcs, glossary, refs |

## Table of Contents

1. [What Glass Actually Is](#1-what-glass-actually-is)
2. [Glass Families and Their Properties](#2-glass-families-and-their-properties)
3. [Viscosity and the Temperature Landmarks of Glass](#3-viscosity-and-the-temperature-landmarks-of-glass)
4. [Why Glass Is Weak in Practice: Fracture Mechanics](#4-why-glass-is-weak-in-practice-fracture-mechanics)
5. [Statistics, Size Effects and Time-Dependent Strength](#5-statistics-size-effects-and-time-dependent-strength)
6. [Thermal Shock](#6-thermal-shock)
7. Tempering physics through standards → `GlassTempering.md`
8. Making and workshop → `GlassMaking.md`
9. Related materials through refs → `GlassRelated.md`

---

## 1. What Glass Actually Is

### 1.1 Definition

Glass is an amorphous (non-crystalline) solid that shows a **glass transition**. It has the short-range order of a crystal (each silicon atom still sits inside a tetrahedron of four oxygen atoms) but lacks long-range periodic order. Diffraction patterns of glass show broad diffuse halos instead of sharp Bragg peaks.

A practical definition used in glass science: *glass is a non-equilibrium, non-crystalline condensed state of matter that exhibits a glass transition and spontaneously relaxes toward the supercooled liquid state over time.*

### 1.2 The Glass Transition

- When a liquid cools below its melting point without crystallizing it becomes a **supercooled liquid**.
- Its viscosity rises steeply as temperature drops.
- At some point the atoms can no longer rearrange fast enough to keep up with the cooling. The structure "freezes" and the material becomes a glass.
- The temperature where this happens is the **glass transition temperature (Tg)**. It is not a fixed thermodynamic point. Faster cooling gives a higher Tg; slower cooling gives a lower Tg.
- The structure that gets frozen in is described by the **fictive temperature (Tf)**: the temperature at which the glass structure would be in equilibrium as a liquid. Quickly cooled glass has a higher fictive temperature, a slightly lower density (for most silicates) and higher stored enthalpy.
- On heating a glass through Tg, heat capacity and thermal expansion jump to liquid-like values. Differential scanning calorimetry (DSC) detects this as a step in the heat-flow curve.
- Viscosity at Tg is conventionally about 10^12 Pa·s (10^13 poise).

### 1.3 Structure of Silicate Glass

The building block is the **SiO4 tetrahedron**: one silicon surrounded by four oxygens, Si-O bond length about 0.162 nm, O-Si-O angle about 109.5 degrees. Tetrahedra link at corners through **bridging oxygens**. The Si-O-Si angle between tetrahedra varies widely in glass (roughly 120 to 180 degrees, centered near 144 to 150 degrees). This angle spread is what destroys long-range order.

**Zachariasen's rules (1932)** for oxide glass formation:
1. An oxygen atom links to no more than two cations.
2. The cation coordination number is small (3 or 4).
3. Oxygen polyhedra share corners, not edges or faces.
4. At least three corners of each polyhedron are shared, producing a 3D network.

### 1.4 Roles of Oxides

| Role | Examples | Effect |
|---|---|---|
| **Network formers** | SiO2, B2O3, P2O5, GeO2 | Form the continuous network on their own |
| **Network modifiers** | Na2O, K2O, Li2O, CaO, MgO, BaO | Break Si-O-Si bridges, create non-bridging oxygens (NBOs), lower viscosity and melting temperature, raise thermal expansion |
| **Intermediates** | Al2O3, TiO2, ZrO2, ZnO, PbO | Can enter the network or act as modifiers depending on composition |
| **Fining agents** | Na2SO4, Sb2O3, As2O3, SnO2, CeO2 | Release gas at high temperature to sweep out bubbles |
| **Colorants** | Fe, Co, Cr, Cu, Mn, Se, Au, Ni | Absorb specific wavelengths |

**Non-bridging oxygen (NBO)**: an oxygen bonded to only one silicon, carrying a negative charge balanced by a nearby modifier cation such as Na+. More NBOs mean a looser network, lower viscosity, higher expansion and lower chemical durability.

**Aluminum's special role**: Al3+ enters tetrahedral sites as AlO4- when charge-balanced by an alkali. Each Al consumes an NBO and re-polymerizes the network. This is why aluminosilicate glasses are stiffer, harder and much better for ion exchange (the network is both strong and open).

### 1.5 Glass Is Not a Slow-Flowing Liquid

The claim that medieval cathedral windows are thicker at the bottom because glass flows is false.
- Old crown glass and cylinder glass were uneven when made. Glaziers often put the thick edge down; examples with the thick edge up also exist.
- Calculations (Zanotto, 1998) estimate that room-temperature viscosity of window glass is on the order of 10^32 Pa·s or more, giving relaxation times far longer than the age of the universe.
- Roman glass, ancient obsidian tools and telescope mirrors centuries old show no measurable flow.

---

## 2. Glass Families and Their Properties

### 2.1 Typical Compositions (weight percent, approximate)

| Glass | SiO2 | Na2O | K2O | CaO | MgO | Al2O3 | B2O3 | PbO | Other |
|---|---|---|---|---|---|---|---|---|---|
| Soda-lime float (window) | 72 to 73 | 13 to 14 | 0 to 0.5 | 8 to 9 | 3.5 to 4 | 0.1 to 1 | 0 | 0 | Fe2O3 0.1, SO3 0.2 |
| Soda-lime container | 72 to 73 | 13 to 14 | 0.3 | 10 to 11 | 0 to 2 | 1.5 to 2 | 0 | 0 | colorants |
| Borosilicate (3.3 type, Pyrex 7740/Borofloat) | 80 to 81 | 4 | 0 to 0.5 | 0 | 0 | 2 to 2.5 | 12.5 to 13 | 0 | |
| Fused silica | 99.9+ | 0 | 0 | 0 | 0 | 0 | 0 | 0 | OH content varies |
| Aluminosilicate (ion-exchangeable cover glass) | 58 to 65 | 12 to 16 | 0 to 4 | 0 to 1 | 0 to 4 | 13 to 22 | 0 to 6 | 0 | Li2O in newer grades, P2O5 in some |
| Lead crystal | 54 to 65 | 0 to 6 | 6 to 13 | 0 | 0 | 0 to 1 | 0 | 24 to 35 | |
| E-glass (fiber) | 52 to 56 | 0 to 1 | 0 to 1 | 16 to 25 | 0 to 5 | 12 to 16 | 5 to 10 | 0 | |
| S-glass / R-glass (high-strength fiber) | 60 to 65 | 0 | 0 | 0 to 9 | 6 to 10 | 23 to 25 | 0 | 0 | |

### 2.2 Physical Properties (approximate, room temperature)

| Property | Soda-lime | Borosilicate 3.3 | Fused silica | Aluminosilicate (cover) | Lead crystal |
|---|---|---|---|---|---|
| Density (g/cm3) | 2.50 | 2.23 | 2.20 | 2.38 to 2.45 | 3.0 to 3.5 |
| Young's modulus E (GPa) | 70 to 73 | 63 to 64 | 72 to 73 | 70 to 85 | 55 to 60 |
| Shear modulus G (GPa) | 29 to 30 | 26 | 31 | 29 to 34 | 22 to 24 |
| Poisson's ratio | 0.22 to 0.23 | 0.20 | 0.17 | 0.21 to 0.23 | 0.22 to 0.25 |
| Thermal expansion (10^-6/K, 20 to 300 C) | 8.5 to 9.3 | 3.25 | 0.55 | 3.5 to 8.5 | 8 to 10 |
| Thermal conductivity (W/m·K) | 1.0 | 1.1 to 1.2 | 1.3 to 1.4 | 0.9 to 1.1 | 0.7 to 0.9 |
| Specific heat (J/kg·K) | 720 to 840 | 830 | 740 to 770 | 800 to 900 | 500 to 650 |
| Fracture toughness KIc (MPa·m^0.5) | 0.72 to 0.82 | 0.75 to 0.85 | 0.74 to 0.80 | 0.65 to 0.85 | 0.6 to 0.7 |
| Vickers hardness (GPa) | 5.4 to 5.8 | 5.8 to 6.3 | 7 to 9 | 6 to 7 | 4 to 5 |
| Mohs hardness | about 5.5 | about 6 | about 6.5 to 7 | about 6 to 6.5 | about 5 |
| Refractive index (nd) | 1.52 | 1.47 | 1.458 | 1.50 to 1.52 | 1.54 to 1.60+ |
| Tg (C) | 550 to 570 | 525 to 560 | about 1150 to 1200 | 600 to 720 | 430 to 470 |

### 2.3 Why Each Family Exists

- **Soda-lime**: cheap, easy to melt, easy to form. Over 90 percent of all glass made. High expansion makes it thermal-shock sensitive but also makes it the best candidate for **thermal tempering** (residual stress scales with expansion).
- **Borosilicate**: low expansion gives excellent thermal shock resistance. Used for lab ware, ovenware, lamp envelopes, pharmaceutical tubing (Type I), telescope mirror blanks (Palomar 200-inch mirror is Pyrex).
- **Fused silica**: lowest expansion of common glasses, highest temperature capability, excellent UV transmission. Used in optics, semiconductor processing, optical fibers, furnace sight glasses. Cannot be meaningfully thermally tempered and contains no alkali for ion exchange.
- **Aluminosilicate**: designed for chemical strengthening. Phone and tablet cover glass, aircraft cockpit windows, high-temperature lamp glass.
- **Lead crystal**: high refractive index and dispersion produce sparkle ("fire"). Soft, heavy, rings when struck. EU rule: at least 24 percent PbO for "lead crystal," at least 30 percent for "full lead" or "high lead" crystal.

---

## 3. Viscosity and the Temperature Landmarks of Glass

Glass softens gradually. The industry defines landmark temperatures by viscosity.

| Landmark | Viscosity (Pa·s) | Viscosity (poise) | Meaning | Soda-lime float | Borosilicate 3.3 | Fused silica |
|---|---|---|---|---|---|---|
| Melting point | 10 | 10^2 | Practical melting and fining | about 1450 to 1500 C | about 1650 C | above 2000 C |
| Working point | 10^3 | 10^4 | Gathering, pressing, blowing | about 1000 to 1050 C | about 1250 C | about 2000 C |
| Softening point (Littleton) | 10^6.6 | 10^7.6 | Glass sags under its own weight | about 720 to 730 C | about 820 C | about 1600 to 1700 C |
| Annealing point | 10^12 | 10^13 | Stress relaxes in minutes | about 545 to 550 C | about 560 C | about 1050 to 1200 C |
| Strain point | 10^13.5 | 10^14.5 | Stress relaxes in hours; below this no new permanent stress forms | about 510 to 515 C | about 510 to 520 C | about 990 to 1100 C |

**Working range** = temperatures between the working point and softening point. Soda-lime has a "short" working range compared with lead glass ("long" glass), which is why lead glass was favored for hand working.

### 3.1 Viscosity Equations

The **Vogel-Fulcher-Tammann (VFT)** equation:

```
log10(η) = A + B / (T - T0)
```

- η in Pa·s, T in kelvin or Celsius consistently.
- A is typically about -1.5 to -3, B a few thousand, T0 a few hundred degrees.
- Valid across the melting to annealing range for most commercial glasses.

The **MYEGA** equation (Mauro, Yue, Ellison, Gupta, Allan, 2009) gives better extrapolation to low temperatures:

```
log10(η) = log10(η∞) + (12 - log10(η∞)) × (Tg/T) × exp[ (m/(12 - log10(η∞)) - 1) × (Tg/T - 1) ]
```

where m is fragility, the slope of log η vs Tg/T at Tg.

### 3.2 Fragility

- **Strong** glass formers (fused silica, GeO2) have nearly Arrhenius viscosity, fragility m about 20.
- **Fragile** formers (many organic glasses, some metallic glasses) show sharp viscosity changes near Tg, m about 70 to 200.
- Soda-lime silicate sits in between, m about 30 to 40.

---

## 4. Why Glass Is Weak in Practice: Fracture Mechanics

### 4.1 Theoretical Strength

The stress needed to pull apart atomic bonds in a perfect solid (Orowan estimate):

```
σ_th ≈ sqrt( E × γ / a0 )
```

- E = Young's modulus, γ = surface energy, a0 = interatomic spacing.
- For silica glass: E ≈ 70 GPa, γ ≈ 1 J/m², a0 ≈ 0.2 to 0.3 nm gives σ_th ≈ 15 to 19 GPa.
- A rougher rule of thumb: σ_th ≈ E/10, about 7 GPa.

**Measured pristine strength**:
- Freshly drawn silica fibers tested in liquid nitrogen (no water): about 12 to 14 GPa.
- Same fibers in room air: about 5 to 6 GPa.
- Commercial optical fiber is proof-tested at 0.69 GPa (100 kpsi) or higher.

**Practical strength of window glass**: about 30 to 100 MPa for as-received annealed float. Design values are often 20 to 45 MPa. Real glass is roughly **100 to 300 times weaker** than its theoretical strength.

### 4.2 Griffith Theory (1921)

A. A. Griffith explained the gap: surfaces carry tiny cracks ("Griffith flaws") that concentrate stress.

Energy balance for a crack of half-length a in a plate under tension σ:

```
σ_f = sqrt( 2 × E × γ / (π × a) )
```

The crack grows when the elastic energy released by extending it exceeds the energy required to create two new surfaces.

**Inglis stress concentration** (1913) for an elliptical hole with semi-axis a and tip radius ρ:

```
σ_tip = σ × (1 + 2 × sqrt(a / ρ))
```

For a crack 10 µm long with a tip radius of 0.5 nm, the tip stress is about 300 times the applied stress.

### 4.3 Linear Elastic Fracture Mechanics (LEFM)

Modern treatment uses the **stress intensity factor**:

```
K_I = Y × σ × sqrt(π × a)
```

- Y = geometry factor (about 1.12 for a shallow edge crack, about 0.71 to 0.73 for a semicircular surface crack at its deepest point when written with π inside the root, depending on convention).
- Fracture occurs when K_I reaches **K_Ic**, the fracture toughness.
- For soda-lime glass K_Ic ≈ 0.75 MPa·m^0.5. Steel is about 50 to 200. Aluminum alloys about 20 to 45. Glass is among the most brittle engineering materials known.

**Critical flaw size vs strength** (soda-lime, Y = 1.12):

| Flaw depth a | Failure stress |
|---|---|
| 1 µm | about 380 MPa |
| 5 µm | about 170 MPa |
| 10 µm | about 120 MPa |
| 25 µm | about 75 MPa |
| 50 µm | about 53 MPa |
| 100 µm | about 38 MPa |
| 500 µm | about 17 MPa |

A scratch one-tenth of a millimeter deep cuts strength to roughly the level of ordinary design values.

### 4.4 Where Flaws Come From

- Contact with harder particles (quartz sand, Mohs 7, scratches glass of Mohs 5.5)
- Handling and conveyor rollers
- Cutting (score lines leave lateral and median cracks)
- Edge grinding and drilling
- Chemical attack and weathering
- Inclusions, stones, bubbles and cords from melting
- Devitrification (crystals with different expansion)

Edges are usually the weakest region of a pane, which is why edge finish strongly controls real strength.

### 4.5 Fracture Surface Features (Fractography)

A brittle fracture surface records how the crack accelerated.

1. **Origin**: the flaw that started failure.
2. **Mirror**: smooth, shiny region where the crack is still accelerating.
3. **Mist**: faint frosted band as the crack approaches terminal velocity and micro-branching begins.
4. **Hackle**: rough ridges where the crack branches macroscopically.
5. **Wallner lines**: curved ripples formed when stress waves interact with the crack front.
6. **Arrest lines** and **twist hackle** record pauses and changes in stress direction.

**Mirror radius relation**:

```
σ_f × sqrt(r_m) = A_m
```

- r_m = mirror radius, A_m = mirror constant (about 1.9 to 2.1 MPa·m^0.5 for soda-lime).
- Measuring the mirror radius on a broken piece gives the stress at failure. Forensic glass analysts and failure investigators use this routinely.

### 4.6 Crack Speed

- Terminal crack velocity in soda-lime glass is about 1,500 m/s.
- This is roughly 0.45 to 0.6 of the Rayleigh surface-wave speed (about 3,300 m/s).
- Crack branching begins when the energy delivered to the crack tip exceeds what a single crack can consume.
- In Prince Rupert's drops the fracture front has been measured at about 1,450 to 1,900 m/s.

### 4.7 Compression vs Tension

- Glass is extraordinarily strong in compression. Pure compressive strength of soda-lime glass is commonly quoted at about 1,000 MPa and above, limited by shear and densification rather than crack opening.
- Cracks need tension to open. Compression closes them.
- **Every strengthening method for glass works by putting the surface into compression**, so that any applied tension must first cancel the built-in compression before surface flaws can open.

---

## 5. Statistics, Size Effects and Time-Dependent Strength

### 5.1 Weibull Statistics

Glass strength is not a single number. It is a distribution governed by the worst flaw in the stressed region.

Two-parameter Weibull model:

```
P_f = 1 - exp[ -(A / A0) × (σ / σ0)^m ]
```

- P_f = probability of failure, A = stressed area, σ0 = scale parameter, m = Weibull modulus.
- High m means consistent strength. Low m means wide scatter.
- As-received float glass: m ≈ 5 to 10. Carefully prepared lab specimens: 10 to 20. Steel: 50 to 100+.

### 5.2 Size Effect

Larger areas contain more flaws, so they are weaker on average:

```
σ1 / σ2 = (A2 / A1)^(1/m)
```

Example: with m = 7, a panel with 10 times the stressed area of a test coupon has a characteristic strength about 10^(1/7) ≈ 1.39 times lower.

### 5.3 Static Fatigue (Stress Corrosion Cracking)

Glass loses strength under sustained load, especially in humid air or water. Water reacts with strained Si-O-Si bonds at the crack tip:

```
≡Si-O-Si≡ + H2O → ≡Si-OH + HO-Si≡
```

The crack grows slowly even when K_I is well below K_Ic. This is **subcritical crack growth**.

Crack velocity follows a power law (region I behavior):

```
v = A × K_I^n
```

- n = stress corrosion susceptibility exponent: about 15 to 20 for soda-lime in water, about 30 to 40 for fused silica, about 20 to 35 for borosilicate.
- Below a threshold (often near 0.25 × K_Ic for soda-lime) cracks may effectively stop growing.

**Consequence for load duration**:

```
σ_1 / σ_2 = (t_2 / t_1)^(1/n)
```

With n = 16: a load held for one year compared with a 3-second gust gives a strength ratio of about (10^7)^(1/16) ≈ 2.7. Glass carrying a permanent load can be expected to hold only around a third to a half of its short-term strength.

**Wiederhorn's crack velocity regions** (1967):
- Region I: velocity rises with K and humidity (reaction-limited).
- Region II: plateau (water transport to the tip limits speed).
- Region III: steep rise independent of environment, approaching K_Ic.

**Pre-stressed glass and fatigue**: tempered glass is far less sensitive to load duration because the surface flaws only experience the portion of applied stress that exceeds the built-in compression. Stress corrosion acts only on that excess.

### 5.4 Environmental Facts

- Glass tested in vacuum or dry nitrogen is noticeably stronger than in humid air.
- Glass is slightly stronger at very low temperatures because stress corrosion slows.
- Strength tests are often run at specified humidity and stress rate because both affect the result.

---

## 6. Thermal Shock

Sudden temperature changes create internal stress because the surface changes size before the interior. The simplest resistance index (critical temperature difference for a fully constrained surface):

```
ΔT_c = σ_f × (1 - ν) / (E × α)
```

Using σ_f = 50 MPa:

| Glass | E (GPa) | α (10^-6/K) | ν | ΔT_c |
|---|---|---|---|---|
| Soda-lime annealed | 70 | 9.0 | 0.22 | about 60 C |
| Borosilicate 3.3 | 64 | 3.3 | 0.20 | about 190 C |
| Fused silica | 72 | 0.55 | 0.17 | about 1,050 C |
| Low-expansion LAS glass-ceramic | 90 | about 0 | 0.25 | effectively unlimited for normal use |

Tempering raises the effective σ_f, so tempered soda-lime glass survives temperature differences of roughly 200 to 250 C, heat-strengthened about 100 to 150 C and annealed about 40 to 60 C (practical industry figures for pane edges).

**Common thermal stress failures**: sun hitting the center of a pane while the edge sits cold in a frame, partial shading, heaters blowing on glass, hot pans set on cold glass, cold water on hot ovenware. Thermal cracks typically leave the edge at 90 degrees to the edge, then meander.
