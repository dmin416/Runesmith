# Road Paving Precision, Asphalt Science and the Roads of Hawaii

> Earth invent loot. Paving precision limits, asphalt binder and mix science, bump prevention, Hawaii road history, and every major island damage mechanism with speed and severity. Not Caldris law. Road layers / era ladder: `../../Science/Vehicle/Roads.md`. Unpaved trail science (drainage, erosion, soil): `../../Science/Invent/TrailBuilding.md`. Island transport verdict: `../../Science/Vehicle/HawaiianTransport.md`. Weather / rain: `Weather.md`. Biomes / lava: `HawaiianBiomes.md`, `HawaiianNativeLandscape.md`. Aggregates / basalt: `HawaiianMinerals.md`, `Sands.md`. Places (Dragnis-class): `../Places.md`. Nav: `Index.md`.

Units: both SI and US customary are given where practical. Figures marked "typical" are industry norms rather than Hawaii-specific measurements. Hawaii-specific figures are sourced at the end.

**Severity scale (Sections 7 and 8).** 1 = minor nuisance or slow wear. 2 = noticeable maintenance burden. 3 = recurring structural damage on vulnerable routes. 4 = major closures or rebuilds within a decade on affected segments. 5 = catastrophic or total loss of corridor until rebuilt elsewhere.

---

## Table of Contents

1. [How Smoothness Is Measured](#1-how-smoothness-is-measured)
2. [The Limits of Paving Precision](#2-the-limits-of-paving-precision)
3. [Difficulties and How They Are Solved](#3-difficulties-and-how-they-are-solved)
4. [How Asphalt Is Made](#4-how-asphalt-is-made)
5. [How Bumps Are Avoided](#5-how-bumps-are-avoided)
6. [History of Roads in Hawaii](#6-history-of-roads-in-hawaii)
7. [What Damages Hawaiian Roads: Case by Case](#7-what-damages-hawaiian-roads-case-by-case)
8. [Summary Table: Speed and Severity](#8-summary-table-speed-and-severity)
9. [Sources](#9-sources)

---

## 1. How Smoothness Is Measured

Road smoothness is not one number. Agencies use different instruments for acceptance, network screening, forensic work, and pay adjustments. Hawaii reports Interstate and National Highway System roughness to FHWA and uses HDOT (Hawaii Department of Transportation) Standard Specifications and supplemental special provisions on state routes, county roads, and airport aprons where applicable.

### 1.1 International Roughness Index (IRI) and the Quarter-Car Model

**IRI** is the global network metric. It is computed by running a **quarter-car simulation** over a measured **longitudinal profile** at **80 km/h (50 mph)** and integrating the response. The model is the World Bank "golden quarter-car" (Sayers, Gillespie, Paterson).

**Quarter-car parameters (standard IRI model).**

| Symbol | Value | Role |
|---|---|---|
| **k1** | **653** 1/s | Primary suspension spring rate (model units) |
| **c** | **6.0** 1/s | Suspension damping |
| **k2 / ms** | **63.3** 1/s² | Tire stiffness divided by sprung mass |
| **mu** | **0.15** | Sprung-mass damping ratio (fraction of critical) |

These constants are fixed so IRI is comparable worldwide. Changing them would break historical trend lines.

**IRI definition (conceptual).** Let **z(x)** be elevation along the wheel path (m), **x** distance (m). The simulation produces suspension motion **y(x)** relative to the body. IRI is:

**IRI (m/km) = (1/L) integral over L of |dy/dx| dx x 1000**

In practice, profile is sampled at **25 cm** or finer, high-pass filtered, and the quarter-car equations are integrated numerically. Output units:

- **m/km** (metric, World Bank standard)
- **in/mi** (US) via **IRI (in/mi) = 63.36 x IRI (m/km)** approximately

**Wavelength sensitivity.** IRI responds most to profile content with wavelengths **1.2 m to 30 m** (about **4 ft to 100 ft**). Shorter waves (texture, small aggregate) are partly filtered out. Longer waves (grade errors, sag on fills) dominate rider feel and IRI on Hawaii's **long fill sections** and **bridge approaches**.

| Wavelength band | Effect on IRI | Typical cause |
|---|---|---|
| Under 0.5 m | Low | Texture, minor segregation |
| 0.5 to 1.2 m | Moderate | Shoved mix, patch edges |
| **1.2 to 30 m** | **Strong** | Paver waves, differential compaction, subgrade settlement |
| Over 30 m | Moderate (grade) | Design profile, fill settlement |

### 1.2 FHWA and HDOT Interpretation Bands

| Category | IRI (m/km) | IRI (in/mi) | User perception |
|---|---|---|---|
| Very good | Under 1.2 | Under 76 | New premium, airports |
| Good | 1.2 to 1.9 | 76 to 120 | Smooth highway |
| Fair | 1.9 to 2.7 | 120 to 171 | Acceptable, maintenance planning |
| Poor | 2.7 to 3.5 | 171 to 222 | Rough, complaints rise |
| Very poor | Over 3.5 | Over 222 | Rehabilitation candidate |

FHWA HPMS reporting treats **good** as IRI under **1.5 m/km (95 in/mi)** on many tables; project specs often require **mean IRI under 1.0 to 1.3 m/km** on new HMA for bonus pay.

### 1.3 New Pavement IRI Targets (Typical Spec Ranges)

| Project type | Target mean IRI (m/km) | Target mean IRI (in/mi) | Notes |
|---|---|---|---|
| New Interstate HMA | 0.8 to 1.0 | 51 to 63 | H-1, H-2, H-3 overlays with profiler pay |
| New urban arterial | 1.0 to 1.3 | 63 to 82 | Utility conflicts raise variance |
| Mill and fill | 1.2 to 1.5 | 76 to 95 | Inherits long waves unless profile mill |
| County repave | 1.3 to 1.8 | 82 to 114 | Shorter paver runs, more stops |
| PCC new slab | 0.7 to 1.0 | 44 to 63 | Grinding can reach 0.5 m/km locally |

Hawaii **windward** segments often exceed targets within **3 to 5 years** if drainage fails, regardless of initial IRI.

### 1.4 Straightedge and Local Tolerance

Manual QC remains mandatory for **localized defects** IRI averages hide.

| Method | Rule (typical HDOT-style) | Use |
|---|---|---|
| **3 m (10 ft) straightedge** | **Gap under 3 mm (1/8 in)** max anywhere | Final riding surface, acceptance |
| **3 m straightedge** | **6 mm (1/4 in)** may apply to base or milled surface before overlay | Pre-overlay QC |
| Feeler gauge | Record max gap each placement | Dispute resolution |
| 1.2 m straightedge | Tighter for bike paths, airport tie-ins | Special projects |

A **6 mm** allowance on intermediate lifts prevents chasing base waviness that the overlay is meant to absorb.

### 1.5 Profilograph vs Inertial Profiler

| Feature | California profilograph | High-speed inertial profiler |
|---|---|---|
| Speed | Walking, about 3 km/h | 50 to 100 km/h |
| Sensor | Rolling wheel, mechanical trace | Lasers + accelerometers |
| Output | PPI, bump count, must-grind lists | **IRI**, rut, texture, GPS |
| Wavelength focus | About 0.3 to 15 m | Full IRI band plus rut |
| Hawaii use | Legacy airport, forensic | HDOT network, pay factors on H-1/H-3 |

Profilographs **over-report** short waves compared to IRI but excel at **finding individual bumps** (utility castings, joint faults). Inertial profilers dominate **annual HPMS** submissions.

### 1.6 Other Precision and Related Measures

| Measure | Unit / method | What it captures |
|---|---|---|
| **RN (Ride Number)** | 0 to 5 scale from profile | Legacy US spec |
| **PPI (Profile Index)** | in/mi from profilograph | Bump count per mile |
| **Half-car IRI (HRI)** | m/km | Shorter wheelbase sensitivity |
| **Rut depth** | mm in wheel paths | 12 mm often triggers overlay |
| **MTD / ETD** | mm texture depth | Wet skid on basalt polish |
| **Friction number (SN 40)** | British pendulum or DF | Curves, rain |
| **Crossfall error** | % vs design | Ponding on windward lanes |
| **FWD deflection** | microns at 40 kN | Weak andisol under thin HMA |
| **GPR layer depth** | cm | Verify thickness on lava fills |
| **Core air voids** | % Va | Compaction acceptance |
| **Longitudinal joint opening** | mm | Lane-to-lane timing |

For invent design on Dragnis-class islands, treat **IRI + 3 mm straightedge** as the dual gate for anything a wheeled carriage or bike feels at speed.

---

## 2. The Limits of Paving Precision

Perfect flatness is unattainable. The wearing course is the top of a stack of variable materials, thermal fields, and control errors. Hawaii adds **rapid UV aging**, **moisture-sensitive volcanic soils**, and **import-dependent binder logistics**.

### 2.1 Limit 1: Aggregate Gradation and Segregation

HMA is **93 to 96% aggregate** by mass. Gradation controls **VMA**, **density**, and **ride**. Island plants crush **Hawaiian basalt** (Makakilo, Kapaa, neighbor-island quarries).

- **Too many fines** stiffens mix, pushes **checking** on surface.
- **Too few fines** leaves **permeable mat**, water enters, **stripping** on windward routes.
- **Segregation** at truck dump, hopper wings, and hand raking creates soft, rough patches.

Residual IRI from gradation alone on a perfect subgrade: about **0.6 to 1.0 m/km** after optimal rolling.

### 2.2 Limit 2: Screed and Paver Dynamics

The **screed** is a floating beam. Thickness set by **head of material**, **tow angle**, and **paver speed**.

- Start/stop **transverse ripples** at **0.3 to 0.8 m** spacing.
- **Screed bounce** on stiff old PCC telegraphs **0.5 to 1.2 m** waves.
- **Automatic grade control** follows wire, ski, or 3D model. Any **reference drift** becomes a **15 to 80 m** hill invisible to straightedge.

Urban Oʻahu repaves (Kalihi, Dillingham) with **utility cuts** force **stop every 50 to 150 m**, raising ripple frequency.

### 2.3 Limit 3: Differential Compaction (Worked Example)

Rollers compact the hottest, most workable zone. **Stiff spots** (manhole, old concrete, bridge header) support more load; **soft spots** beside them compact deeper, leaving a **dip**.

**Worked example (typical teaching case).**

- Underlying feature creates **20 mm** thickness variation across **1.2 m** lateral distance before rolling.
- Basalt mix at **150 C** compresses **8 to 12%** height under roller on soft zone, **2 to 4%** on stiff zone.
- Differential **8% vs 3%** over 50 mm lift yields about **2.5 mm** extra settlement on soft side.
- After **multiple passes** and **thermal contraction**, net **residual dip about 4 mm** remains at **1.0 to 1.5 m** wavelength.

That **4 mm** exceeds **3 mm straightedge** unless corrected by **micro-milling** or **profile grinding**. It reads as **IRI bump** at 40 to 55 mph.

### 2.4 Limit 4: Grade Reference Accuracy

| Control method | Typical vertical accuracy | Longitudinal repeatability | Hawaii notes |
|---|---|---|---|
| Manual string line | 3 to 6 mm | Poor on wind | Rare today |
| Ski on previous mat | 5 to 10 mm | Follows old waves | Mill-and-fill inherits |
| Wire / sonic tracker | 3 to 5 mm | Good on tangent | Tunnel approaches |
| **3D GNSS + robotic total station** | **2 to 4 mm** | **Best on H-3, airports** | Multipath near cliffs |
| **Laser mill control** | 1 to 3 mm | Removes long waves | Premium repaves |

**GNSS + laser** is the practical ceiling for **absolute grade**. Remaining error is often **design intent** (crown **1.5 to 2.0%**, superelevation transitions) not mistake.

### 2.5 Limit 5: Thermal Movement and Cooling Time by Lift Thickness

Asphalt stiffens as it cools. Rolling must finish before **mix drops below about 80 to 90 C (175 to 195 F)** for conventional HMA.

**Approximate cooling time to rolling cutoff (ambient 25 C, light wind, basalt mix).**

| Lift thickness | Time to 90 C | Risk if delayed |
|---|---|---|
| 25 mm (1 in) | 8 to 12 min | Surface checks |
| 38 mm (1.5 in) | 12 to 18 min | Open graded friction courses |
| 50 mm (2 in) | 18 to 25 min | Standard overlay |
| 75 mm (3 in) | 25 to 40 min | Needs warm night or WMA |
| 100 mm (4 in) | 35 to 55 min | Base lift, windward evening |

**Night paving** on Hawaiʻi Island mauka or **Kona** with **15 C** ambient adds **30 to 50%** to times. **Thermal contraction** overnight opens **longitudinal joints** **2 to 4 mm**, creating **lane edge steps** if adjacent lanes paved on different days.

Surface **dark HMA** reaches **60 to 70 C** in Kona sun; binder **softens**, **rutting** under heavy trucks before oxidation completes.

### 2.6 Limit 6: Viscoelasticity and the WLF Equation

Binder is **viscoelastic**: behavior depends on **time and temperature**. At **high temperature**, it **flows** (rutting). At **low temperature**, it **cracks** (rare at sea level in Hawaii, relevant on **summit** roads).

**Williams-Landel-Ferry (WLF) shift factor** for time-temperature superposition:

**log10(aT) = -C1 (T - Tr) / (C2 + T - Tr)**

Typical constants for asphalt binders: **C1 about 17 to 20**, **C2 about 50 to 55 C**, **Tr** reference temperature.

At **pavement 60 C**, a load duration that would damage at **20 C** is accelerated by factor **aT** often **10^3 to 10^5**, explaining **rutting in one hot afternoon** on under-designed intersections.

**Arrhenius aging** (Section 4) uses **Ea about 60 to 90 kJ/mol** for oxidative hardening; Hawaii **UV + heat** pushes equivalent **PAV hours** faster than mainland **moderate** climate maps.

### 2.7 Limit 7: Intentional Non-Flatness

| Feature | Typical value | Purpose |
|---|---|---|
| Crown | 1.5 to 2.0% | Drain wheel paths |
| Superelevation | 2 to 6% on curves | H-3, Pali, Hana |
| Cross slope on superelevation runout | 0.5%/s max rate | Comfort |
| Rumble strips | 6 to 12 mm depth | Alert |
| Speed tables | 75 to 100 mm rise | Neighborhoods |
| Drainage dips | Design low points | Leeward gulches |

These are **not defects**. Profiler specs often **mask** rumble strips from pay IRI.

### 2.8 Limit 8: Embedded Urban Roughness

- **Manhole frames** set **3 to 6 mm high** for safety → impact at speed.
- **Bus pads**, **steel plates**, **trolley embeds** (legacy).
- **Reflective cracks** from **PCC** at **3 to 5 m** spacing.
- **Bridge expansion joints** **10 to 25 mm** step if seals fail (H-3 viaducts, Harano Bridge).

Urban **IRI mean** can read **fair** while **individual impacts** exceed **comfort thresholds**.

### 2.9 Limit 9: Practical Ceiling

Even with **GNSS paving**, **MTV**, and **IC**, a **full project length** on Hawaii rarely holds **mean IRI under 0.9 m/km** for more than **12 to 24 months**. Network reality for aged windward corridors:

**Practical residual band after normal construction: IRI 35 to 50 in/mi (0.55 to 0.79 m/km)** on best tangents only.

**Holding entire state systems under 120 in/mi (1.9 m/km)** requires **continuous overlay budget**, not one perfect pave. Weak **andisol**, **rain**, and **UV** dominate before paver skill limits are reached.

---

## 3. Difficulties and How They Are Solved

| Difficulty | Mechanism | Hawaii example | Mitigation |
|---|---|---|---|
| Rough or weak base | Deflection under load | Plantation-era base on Maui | Full-depth reclamation, thicker base |
| Segregated mix | Fine/coarse split | Long haul from Kapaa plant to North Shore | MTV, remix at paver |
| Variable mat temperature | Uneven density | Afternoon H-1 pave | MTV, infrared monitoring |
| Steep grade | Screed slip, rolling creep | Pali Highway, Saddle climbs | Echelon paving, lower speed |
| Narrow lane | Stop-start | Nuuanu, Lahaina | Night work, WMA window |
| Wind-blown cool | Fast surface set | Hawaiʻi Island mauka | WMA, more rollers |
| Rain on mat | Stripping risk | Windward repave season | Schedule Kau months, tent rare |
| Basalt polish | Low wet friction | H-1 curves | OGFC, high friction surface |
| High RAP content | Stiff, brittle | Statewide recycling push | Binder bump, limit RAP % |
| Utility trenches | Differential settle | All cities | Flowable fill, full-depth patch |
| Old PCC underneath | Reflective cracking | Moanalua | Crack relief, SAMI, thick overlay |
| Organic subgrade | Rut before surfacing | Hilo, Hanalei valley | Remove and replace, geotextile |
| Andisol fill | Compressible | Puna subdivisions | Surcharge, pile slabs worst cases |
| Remote job | Cold mat on truck | Hana, Kau north | Portable plant, shorter haul |
| Tunnel ventilation | Fumes, cool air | H-3 Tetsuo Harano | Night closure windows |
| Measuring too late | IC map after mat cold | Rookie crew | Real-time CMV, stop pass when cool |
| Wrong roller pattern | Under/over compact | Open graded courses | IC, vibration off on thin lifts |

### 3.1 Intelligent Compaction (IC)

**IC** mounts **accelerometers** on vibratory rollers and maps **Compaction Meter Value (CMV)** or **kneading meter** vs **GPS position**.

**Workflow.**

1. Set **pass coverage map** (minimum 4 to 6 passes typical).
2. Identify **soft zones** (CMV low) while **mat still above 90 C**.
3. **Supplement rolls** before joint cools.
4. Export **PDF map** for HDOT acceptance.

**Limits on Hawaii andisol:** CMV varies with **underlying stiffness**; geotechnical fix (lime, geogrid) still required. IC prevents **missing a soft stripe**, it does not **strengthen mud**.

### 3.2 Material Transfer Vehicle (MTV)

The **MTV** sits between **end-dump trucks** and **paver**.

**Functions.**

- **Remixes** segregated pile corners in **auger chamber**.
- **Buffers** paver from **truck bumping** screed.
- **Smooths feed rate** for **continuous pave**.

**Oʻahu contractors** (Grace Pacific, Road and Highway Builders, Jas. W. Glover) deploy MTVs on **H-1**, **Moanalua**, **Kamehameha Hwy** high-tonnage jobs. **Neighbor islands** mobilize for **airport** and **harbor** projects when **> 3,000 tons** per shift.

**Rule of thumb:** If **more than 4 trucks/hour** or **haul over 45 min**, MTV payback exceeds **segregation patch** cost.

---

## 4. How Asphalt Is Made

### 4.1 From Crude to Binder: Atmospheric and Vacuum Distillation

**Asphalt cement** is the **bottom of the barrel**, not tar (coal tar is a different chemistry).

1. **Atmospheric distillation** heats crude to about **350 to 400 C** at **1 atm**. Light fractions exit: **gas, naphtha, kerosene, gas oil**.
2. **Vacuum distillation** pulls **vacuum gas oil** and **residue** at **350 to 390 C** under **25 to 100 mmHg** so molecules do not crack.
3. **Vacuum residue** is **asphalt cement** (pen grade historically) or feed for **air blowing** ( roofing stiffness).

Hawaii receives **finished PG binder** by tanker; local **Kapolei refinery** reduction shifted dependence to **import terminal** at **Kalaeloa Barbers Point Harbor**.

Typical binder in HMA: **4.5 to 6.0%** by mass. Air voids target **4 to 7%** after compaction. Rest **aggregate**.

### 4.2 SARA Fractions

| Fraction | Polarity | Role in binder |
|---|---|---|
| **Saturates** | Non-polar | Lubricates, soft |
| **Aromatics** | Polarizable | Flexibility, compatibility |
| **Resins** | Polar | Adhesion to aggregate |
| **Asphaltenes** | Most polar | Structure, stiffness |

**Colloidal model:** asphaltenes micelles in aromatic/resin **maltene** phase. **Oxidation** shifts balance toward **more asphaltenes/resins**, **stiffening** binder.

### 4.3 Aging Chemistry

**Short-term (RTFOT, 163 C, 85 min):** simulates **plant heat**, loses light volatiles.

**Long-term (PAV, 100 C, 2.1 MPa, 20 to 40 hr):** simulates **field years**.

**Chemistry.**

- **Oxygen** adds **carbonyls (C=O)** and **sulfoxides** on aromatics.
- **Cross-linking** increases **complex modulus G***.
- **Raveling** when **resin depleted** at surface under **UV**.

**Arrhenius rate:** k = A exp(-Ea/RT). **Ea about 60 to 90 kJ/mol** for oxidative hardening. At **Hawaii pavement 55 to 65 C**, chemical age **1 year** can equal **several years** of **25 C** equivalent in lab hours.

### 4.4 Superpave Performance Grade (PG) and Tests

| Test | Measures | PG use |
|---|---|---|
| **Rotational viscometer (RV)** | Mix/plant viscosity at 135 C | Pumpability |
| **Dynamic shear rheometer (DSR)** | G*, phase angle at high T | **PG high temperature** (e.g. 64, 70, 76 C) |
| **Rolling thin film oven (RTFOT)** | Mass loss, DSR after | Short-term aged binder |
| **Pressure aging vessel (PAV)** | Long-term aged binder | Design life stiffness |
| **DSR on PAV residue** | Critical high T | Prevent rutting |
| **Bending beam rheometer (BBR)** | Stiffness at low T | **PG low** (e.g. -22 C), Hawaii rarely governs |
| **Direct tension (DT)** | Failure strain | Optional low T grade |
| **Multiple stress creep recovery (MSCR)** | Elastic recovery | Traffic level polymer grade |

Example designation: **PG 70-22** = passes rutting criteria to **70 C** and cracking to **-22 C**.

### 4.5 Polymer Modification (SBS)

**Styrene-butadiene-styrene (SBS)** block copolymer **3 to 7%** by weight of binder:

- Raises **elastic recovery** (MSCR **Jnr** lower).
- Cuts **rutting** at **H-1** intersections and **airport** fuel areas.
- Enables **SMA** (Stone Matrix Asphalt) **gap gradation** with **stable mastic**.

Produced at **Kalaeloa terminal** or **on-site blending** before truck to plant.

### 4.6 Hawaiian Aggregates: Vesicular Basalt and Absorption

Fresh **Hawaiian basalt** is **dense** (Gsb about **2.85 to 2.95**), but **vesicular flows** and **cinder** used locally can show **absorption 1 to 4%** (sometimes higher on **scoria**).

**Mix design impact.**

- **Effective binder content** must use **absorbed asphalt** correction: **Pbe = Pba x (1 - absorption)**.
- High absorption **pulls binder** from film, **raises stripping risk** unless **anti-strip** used.

**Crushed Makakilo/Kapaa** cubical faces give **good friction**; **LA abrasion** meets HDOT when **100% crushed**.

### 4.7 Moisture Susceptibility: Lime and Amine Anti-Strip

Windward Hawaii demands **TSR > 0.80 to 0.90** (AASHTO T283).

| Agent | Dose (typical) | Mechanism |
|---|---|---|
| **Hydrated lime** | 1.0 to 1.5% of dry aggregate | Raises pH, stiffens mastic, strips clay films |
| **Liquid amine anti-strip** | 0.25 to 0.75% of binder | Changes aggregate surface energy |
| **Polymer + lime** | Combined | Puna/Hilo projects |

**Failure mode:** **Hydraulic pumping** (Section 7.1) plus **weak film** → **raveling** in **first winter**.

### 4.8 Superpave Volumetrics (Design Targets)

| Parameter | Symbol | Typical spec range |
|---|---|---|
| Air voids | **Va** | **4.0%** target, 3.5 to 4.5% |
| Voids in mineral aggregate | **VMA** | Min **14%** (traffic dependent) |
| Voids filled with asphalt | **VFA** | 65 to 75% |
| Dust-to-binder ratio | **Db/s** | 0.6 to 1.2 |
| Gyrations **Ndesign** | | 75 light, 100 std, 125 heavy |

**Gmb** from **Superpave gyratory** at **Ndesign**; compare to **Gmm** from **Rice** test for **Va**.

### 4.9 Drum Plant Sequence

1. **Cold feed bins** proportion **aggregate** (+ **RAP** if used).
2. **Dryer** heats aggregate to **160 to 190 C**, removes moisture (critical after rain on stockpiles).
3. **Dust collector** returns **baghouse fines** (watch **Db/s**).
4. **Elevator** to **hot bins**.
5. **Weigh hopper** batches **aggregate + binder** (+ **lime**).
6. **Pugmill** mixes **30 to 45 s**.
7. **Load trucks** at **150 to 170 C** mix temp for short haul Oʻahu.

Large Oʻahu plants exceed **200,000 tons/year** each. Statewide demand has topped **1.2 million tons/year** in heavy years.

### 4.10 Warm-Mix Asphalt (WMA)

**WMA** technologies (foaming, wax, chemical) allow **120 to 140 C** placement.

**Hawaii use:** **Long haul** neighbor island, **night** work, **thick lifts**, **tunnel** ventilation savings on **H-3** maintenance windows.

### 4.11 Placement, Rolling, and Impact Spacing

**Paver speed** matched to **delivery**. **MTV** recommended over **4 trucks/hour**.

**Rolling pattern:** **Breakdown (steel vibratory)** → **intermediate (steel or pneumatic)** → **finish (static steel)**.

**Impact spacing (vibratory steel roller)** at frequency **f (Hz)** and speed **v (m/s)**:

**Spacing (m) = v / f**

Example: **v = 3 km/h = 0.833 m/s**, **f = 40 Hz** → spacing **0.021 m (21 mm)**. Operators aim **10 to 20 impacts per meter** by adjusting **speed** and **vibration**.

**Joint construction:** **Vertical edge**, **tack coat 0.05 to 0.10 gal/yd²**, **overlap **25 to 50 mm**** on adjacent lane same day when possible.

### 4.12 Portland Cement Concrete Alternative

**PCC** used where **rutting** impossible tolerance or **heavy static** loads:

- **Runways** (HNL, OGG, KOA, LIH)
- **Harbor aprons**, **Interstate** sections with **30+ year** rigid strategy

**Tradeoffs:** **Joint faulting**, **curling**, **higher upfront cost**, **dowel retrofit** maintenance. **Fuel spill** resistance favors **PCC** at **ports**.

---

## 5. How Bumps Are Avoided

Bumps are **symptoms** of **drainage**, **structure**, or **construction** failure.

### 5.1 Subgrade: Proctor and Stabilization

**Standard Proctor** (ASTM D698) or **Modified Proctor** (D1557) sets **moisture-density** targets for **subgrade compaction**.

| Treatment | When | Hawaii context |
|---|---|---|
| **Recompacted fill** | Organic removed | Hilo taro fills |
| **Lime stabilization** | Clay/plastic fines | Central Oʻahu pockets |
| **Cement stabilization** | Weak wet silt | Windward cuts |
| **Geotextile separator** | Soft fine subgrade | Andisol skirts |
| **Geogrid** | Spreads load | Heavy port haul roads |

**Proof roll** with **loaded truck**; **rut > 25 mm** → **dig out and replace**.

### 5.2 Base, Drainage, and AASHTO Drainage Coefficient

**Open-graded base** or **dense graded** over **geotextile**. **Underdrains** at **cut toes** on windward cliffs.

**AASHTO 1993 structural design** uses **drainage coefficient Cd**:

| Drainage quality | Cd |
|---|---|
| Excellent | 1.00 to 1.05 |
| Good | 0.95 to 1.00 |
| Fair | 0.90 to 0.95 |
| Poor | 0.80 to 0.90 |

Windward Hawaii **without underdrains** often designs as **fair to poor** unless **proven** dry.

### 5.3 Fourth Power Law and ESAL Table

**Fatigue life** scales roughly with **(1/strain)^4** for flexible pavements (AASHO Road Test basis).

**ESAL** = equivalent single axle load (**18,000 lb**, **80 kN**).

| Axle type | ESAL factor (approx) |
|---|---|
| Single 18 kip | 1.0 |
| Tandem 34 kip | 1.2 to 1.5 per pass |
| Container drayage peak | High repetitions on H-1 |

**Halving tensile strain** can multiply life by **up to 16** (idealized; real exponents **3 to 5** also used in MEPDG).

### 5.4 Structural Number (SN) Formula

**AASHTO SN:**

**SN = a1 D1 + a2 D2 m2 + a3 D3 m3**

- **D** = layer thickness (inches)
- **a** = layer coefficient (HMA about **0.44**, base **0.14**, subbase **0.11** typical start)
- **m** = sublayer drainage factor

Thinner **SN** on **weak andisol** → **wheel path fatigue** in **1 to 3 years**.

### 5.5 Construction Practice Checklist

1. **Dry subgrade** or **accept lower density** only with **structural bump**.
2. **Tack** every lift.
3. **MTV + IC** on major jobs.
4. **Match paver speed** to **roller train**.
5. **Weather window** (no rain on mat).
6. **Profile mill** if old **IRI > 150 in/mi** before thin overlay.
7. **Joint same day** when possible.
8. **Castings adjusted** before final lift.

### 5.6 Utilities

- **One-cut** coordination with **city/county**.
- **Flowable fill** or **95% Proctor** trench backfill.
- **Full-depth patch** minimum **1.5 m** beyond trench edge.

### 5.7 Bridge Approaches

**Bump at bridge** = **settlement differential** + **joint failure**.

| Fix | Role |
|---|---|
| **Approach slab** on piles | Limits settle |
| **Geofoam (EPS)** lightweight fill | Reduces load on weak fill (select HDOT projects) |
| **Wick drains** | Accelerates consolidation |
| **Joint seal replace** | Keeps salt out (coastal viaducts) |

**H-3** and **Harano Tribute Bridge** need **scheduled joint maintenance**.

### 5.8 Preventive Maintenance Table

| Treatment | When | Life extension |
|---|---|---|
| **Crack seal** | Width 3 to 19 mm | 2 to 4 years water block |
| **Chip seal** | Fair surface, sound base | 5 to 7 years |
| **Microsurfacing** | Urban arterials | 5 to 8 years |
| **Thin overlay 25 to 38 mm** | Rut < 12 mm | 8 to 12 years |
| **Fog seal** | OGFC binder loss | 1 to 3 years |

### 5.9 Pothole Repair Quality

| Method | Quality | Hawaii wet issue |
|---|---|---|
| **Throw-and-go cold mix** | Emergency | Washes out next rain |
| **Spray injection** | Medium | Needs dry cavity |
| **Saw-cut + hot mix + compact** | High | Best practice |
| **Infrared heat + blend** | High | Urban patches |

**Repeated potholes** in one wheel path → **structural overlay**, not better glue.

### 1.7 IRI Reporting on Hawaii NHS Segments

HPMS submissions bundle **IRI** by **functional class**. **Interstate** **H-1/H-2/H-3** segments typically **report** **good** **fraction** **targets** **above** **national** **average** **after** **fresh** **overlay** **cycles**. **Windward** **connectors** **off** **Interstate** **often** **drop** **to** **fair** **faster** **due** **to** **7.1** **rain** **without** **same** **overlay** **budget**.

### 1.8 Rut Depth and User Complaint Threshold

| Rut depth (mm) | Typical agency action |
|---|---|
| 6-8 | Monitor |
| 10-12 | Mill plan year 1-2 |
| 15+ | Emergency overlay or lane restriction |

**Basalt** **mix** **ruts** **less** **before** **polymer** **intersections** **still** **show** **12 mm** **after** **5-7 years** **on** **H-1** **Waipahu** **bus** **lanes**.

### 1.9 Macrotexture and Hawaii Wet Skid

**ETD** **0.6-1.2 mm** **target** **on** **OGFC** **windward** **installations**. **Polished** **dense** **graded** **surfaces** **fail** **locked-wheel** **tests** **after** **UV** **+** **traffic** **unless** **refreshed**.

---

### 2.10 Aggregate Crushing Under Roller

**Basalt** **LA** **loss** **< 30%** **typical** **HDOT** **acceptance**. **Over-vibration** **on** **hot** **mat** **crushes** **faces** **→** **smooth** **texture** **+** **extra** **fines** **→** **lower** **VMA** **risk** **if** **not** **caught** **in** **QC**.

### 2.11 Paver Speed vs Ripple Wavelength

**Ripple** **spacing** **approximately** **paver** **speed** **times** **screed** **hunt** **period**. **At** **3 m/min** **and** **2 s** **hunt**, **waves** **~0.1 m** **(too** **short** **for** **IRI** **dominance)**; **at** **stop-go**, **0.5-1.5 m** **transverse** **sets** **dominate** **driver** **feel**.

### 2.12 Cooling Wind on Mauna Kea Access

**Trade** **wind** **+** **elevation** **→** **fast** **surface** **cool** **on** **descent** **lanes** **→** **insufficient** **density** **if** **roller** **train** **too** **short** **(ties** **Section** **2.5** **table)**.

---

### 4.13 Vacuum Distillation Column Conditions (Reference)

| Stage | Pressure | Temperature (approx) | Product |
|---|---|---|---|
| Atmospheric tower top | 1 atm | 150-200 C | Naphtha range |
| Atmospheric residue | 1 atm | 350+ C | Feed to vacuum |
| Vacuum tower | 25-40 mmHg | 350-390 C | VGO + residue |
| Asphalt cement | Vacuum residue | - | PG binder feed |

**Air** **blowing** **optional** **for** **roofing** **grades** **not** **typical** **PG** **paving** **cement** **imported** **to** **Hawaii**.

### 4.14 RAP in Hawaii Plants

**Reclaimed** **Asphalt** **Pavement** **10-25%** **common** **in** **mixes** **→** **stiffer** **blend** **→** **binder** **grade** **bump** **(softer** **PG** **added** **or** **more** **new** **binder** **%)** **to** **hit** **Va/VMA**.

### 4.15 Anti-Strip TSR Test Protocol Sketch

1. **Compact** **specimens** **dry**.
2. **Compact** **second** **set** **with** **partial** **vacuum** **saturation** **+** **freeze** **optional** **(not** **sea-level** **HI** **focus)**.
3. **Indirect** **tensile** **strength** **ratio** **wet/dry** **>= 0.80** **minimum** **typical**.

---

### 5.10 Mechanistic Design (MEPDG) Note

**AASHTOWare** **Pavement** **ME** **Design** **uses** **climate** **files** **Honolulu** **and** **Hilo** **→** **predicts** **rutting** **and** **fatigue** **with** **traffic** **spectra** **better** **than** **1993** **SN** **alone**. **HDOT** **still** **uses** **SN** **family** **on** **many** **projects** **with** **ME** **for** **major** **Interstate** **reconstructions**.

### 5.11 Subgrade CBR and SN Allowable

| CBR | Typical treatment |
|---|---|
| < 4 | Replace, lime, or geogrid |
| 4-8 | Thick base + geotextile |
| 8-15 | Standard base thickness |
| > 15 | Reduced base |

**Andisol** **CBR** **2-6** **common** **unsaturated** **test** **→** **explains** **7.4** **severity**.

### 5.12 Fourth Power ESAL Life Table (Illustrative)

| Relative strain | Relative life (fourth power) |
|---|---|
| 1.00 | 1.00 |
| 1.10 | 0.69 |
| 1.20 | 0.48 |
| 1.30 | 0.35 |
| 1.50 | 0.20 |

---

### 6.8 Ala Loa Circumnavigation Concept

**Ala** **loa** **linked** **communities** **around** **each** **major** **island** **for** **tax** **collection**, **messengers**, **and** **pilgrimage**. **Width** **rarely** **exceeded** **two** **people** **abreast** **except** **near** **political** **centers** **(Honolulu**, **Hilo**, **Lāhaina** **historical** **capitals** **on** **different** **islands** **over** **time)**.

### 6.9 Territorial Route Numbers to Modern Designations

**Evolution** **from** **named** **roads** **(Pali**, **Volcano**, **Kona** **Coast)** **to** **numbered** **system** **eases** **HDOT** **maintenance** **contracting** **post-1960s** **highway** **boom**.

### 6.10 Neighbor Island Airport Corridors

**Keahole** **(Kona)**, **Kahului**, **Lihue**, **Hilo** **airports** **each** **anchor** **arterial** **pavement** **designed** **for** **fuel** **trucks** **and** **passenger** **volume** **→** **PCC** **or** **thick** **HMA** **on** **aprons** **per** **FAA** **/ad** **HDOT** **standards**.

### 6.11 Today's Pavement Condition Ranking Factors (Checklist)

1. **Age** **since** **last** **overlay**.
2. **Windward** **vs** **leeward** **exposure**.
3. **Traffic** **spectra** **(ESALs)**.
4. **Subgrade** **class** **(andisol** **flag)**.
5. **Coastal** **or** **tsunami** **zone**.
6. **Lava** **zone** **hazard** **(HVO** **maps)**.
7. **Maintenance** **entity** **budget** **(state** **vs** **county)**.

**Composite** **score** **drives** **which** **mile** **gets** **2020s** **overlay** **funding** **first**.

### 6.12 2005-2006 Crisis Timeline (Binder Supply)

| Period | Event |
|---|---|
| Pre-2006 | Refinery supply uncertainty on Oʻahu |
| Spring 2006 | Industry consortium commits to Kalaeloa terminal |
| 2006-2008 | Construction, permitting, heated pipeline |
| Summer 2008 | First tanker discharge, terminal operational |
| Post-2008 | ~300,000 barrel storage class; single major import node |

**Tesoro** **Kapolei** **refinery** **phase-out** **later** **reinforced** **import** **dependence** **(Star-Advertiser** **2013** **chain** **article)**.

---

### 3.3 Roller Train Example (50 mm Overlay)

1. **Breakdown** **steel** **vibratory** **3 passes** **while** **> 100 C**.
2. **Intermediate** **pneumatic** **6-8** **passes** **knit** **surface**.
3. **Finish** **steel** **static** **1-2** **passes** **until** **90 C** **cutoff**.

**IC** **map** **exported** **before** **mat** **drops** **below** **90 C**.

### 3.4 When MTV Is Optional vs Required

| Haul time | Tons/hour | MTV |
|---|---|---|
| < 20 min | < 200 | Optional |
| 20-45 min | 200-400 | Recommended |
| > 45 min | > 400 | Required for spec smoothness |

**Hana** **Highway** **jobs** **often** **portable** **plant** **instead** **of** **long** **haul** **from** **Kahului**.

---

## 6. History of Roads in Hawaii

### 6.1 Pre-Contact: Ala Hele and Ala Loa

**Ala hele** (path, trail) connected **ahupuaʻa** resources. **Ala loa** (long trail) encircled islands, often **within sight of coast**, passing **heiau**, **fishponds**, and **freshwater**.

- Width **single file** to **double file**; **stone paving** near chiefly centers.
- **No wheel traffic**; design for **foot**, **dog**, **pig**, later **horse**.
- **Waipiʻo** and **Hāmākua** cliff sections used **ladder trails** and **narrow ledges**.

### 6.2 Kingdom Period Laws and Early Roads

**Kamehameha III** era **statutes** began **public road** responsibility. **Privy pits** and **hog trespass** on roads appear in **1840s-1860s** law codes.

- **Pali Road** (Nuʻuanu) linked **Honolulu** to **windward** by **1840s-1850s** improvements.
- **Volcano Road** (Hilo to Kīlauea) developed for **tourism and freight**.
- **Horse and wagon** widened **selected** routes; **macadam** and **crushed rock** late **1800s**.

### 6.3 Territory and Plantation Era

**1898 annexation** → **Territorial government** standardized **right-of-way**.

- **Sugar/pineapple** built **cane haul roads** (**crushed lava**, **macadam**).
- **Round Top**, **Tantalus**, **Old Pali** show **manual cut** grades without modern geotech.
- **1920s-1930s** **Route numbering** begins; **ferries** link islands before **jet age**.

### 6.4 Statehood and the Interstate Program

**1959 statehood** brought **Interstate designation** (legal for **federal aid** despite ocean gaps).

**H-1 (Lunalilo Freeway / Queen Liliʻuokalani Freeway segments).**

- **Oʻahu east-west** backbone **Honolulu to Kapolei/Ewa**.
- Built in **stages 1960s-1990s**; **H-1/H-201** interchange complexity.
- Daily volume **200,000+** on peak segments.

**H-2 (Veterans Memorial Freeway).**

- **Waipahu / Pearl City** to **Wahiawa** and **Schofield**.
- Opened **1976**; connects **central Oʻahu** military and bedroom communities.

**H-3 (John H. Burns Freeway / Tetsuo Harano Tunnels).**

- **Kaneohe (Koʻolau)** to **Halawa (Pearl Harbor)** via **Koʻolau Range**.
- **Twin bored tunnels** about **1 mile** each; **viaducts** through **Haʻiku Valley**.
- Opened **December 1997** after **decades** of **environmental and cultural** controversy.
- **Cost class about $1.3 billion** (1990s dollars), among **most expensive per mile** US Interstates.

### 6.5 Neighbor Island Corridors

| Route | Character | Notes |
|---|---|---|
| **Hana Highway (360)** | **620+ curves**, **59 bridges** | Maui north coast tourism |
| **Piʻilani Highway (31)** | South Maui link | Completed modern alignment over decades |
| **Queen Kaʻahumanu (19)** | Kona coast | Resort and freight |
| **Kuhio Highway (56/560)** | Kauaʻi north | Hanalei, one-lane bridges |
| **Route 11** | Hawaiʻi Island belt | Hilo-Kona, volcanic and cliff |
| **Saddle Road (200)** | Cross-island | Upgraded **Daniel K. Inouye Highway** |

**Saddle Road modernization:** Federal/state investment reported about **$316.5 million** class for **alignment, safety, and military-civilian** connection between **Hilo** and **Kona** side access to **Mauna Kea** / **Waimea** region.

### 6.6 Today's Condition Rankings (Network Picture)

HPMS and public reporting generally show:

- **Best IRI bands:** New **Interstate** overlays, **airport** aprons, recent **Kona** resort frontage jobs.
- **Worst persistent roughness:** **Windward** county roads on **weak fill**, **Hana** maintenance backlog, **Puna** post-lava temporary alignments, **heavy port** arterials with **thin overlays**.

**Over 90%** of Hawaii lane-miles are **asphalt surfaced** (industry figure). Condition is **bimodal**: **premium urban Interstate** vs **aging windward collector**.

### 6.7 Asphalt Supply Crisis 2005-2006 and Kalaeloa Terminal

**Problem.** Closure and **refinery changes** on Oʻahu threatened **liquid asphalt cement** supply. **Tesoro Kapolei** and **Chevron** dynamics left contractors **without binder** for **months-class** risk.

**Industry response.** Consortium (major users) designed **import terminal**:

- **Groundbreaking** about **2006**; **operational summer 2008**.
- **Asphalt Hawaii (GLP)** terminal at **Kalaeloa Barbers Point Harbor**.
- **Heated pipeline** from **Piers 6-7** to **storage tanks**.
- Capacity class **300,000 barrels** total storage (industry and EA documents cite **multi-tank** farm at this scale).

**Supply chain today.**

1. **Binder** from **Canada / US Gulf** (often **Panama** route).
2. **Tanker** to **Kalaeloa**.
3. **Truck** to **Grace Pacific, Road and Highway Builders, Jas. W. Glover** plants.
4. **Basalt aggregate** local; **barge** mix components to **neighbor islands**.

When **terminal delays**, **projects slip** regardless of **local rock** availability.

---

## 7. What Damages Hawaiian Roads: Case by Case

Each case: **mechanism (step-by-step)**, **Hawaii rainfall or context table where relevant**, **speed**, **severity 1-5**, **routes**.

### Hawaii Reference Rainfall (Annual, Inches)

| Location | Approx. inches/year | Role |
|---|---|---|
| **Waiʻaleʻale / Mount Waiʻaleʻale (Kauaʻi)** | **450+** (long-term estimates **370-460+**) | Upper bound USA rain |
| **Hilo (Big Island)** | **125+** (often **130** class) | Chronic wet pavement |
| **Windward Oʻahu (Kaneohe)** | **80-100** | Trade shower loading |
| **Honolulu leeward** | **20-30** | UV-heavy, less rain damage |
| **Kawaihae (Kohala)** | **Under 10** | Flash flood gulches dry until storm |
| **Waimea (Kamuela)** | **30-50** | Mixed |

### 7.1 Rain and Chronic Wetting

**Mechanism (steps).**

1. **Trade wind** air rises on **windward** slopes → **continuous rain**.
2. **Cracks** and **open joints** admit **water**.
3. **Pore pressure** in **base/subgrade** rises.
4. **Hydraulic pumping** under **tire load** ejects **fines** → **mud** under slab/mat.
5. **Stripping** if **binder-aggregate bond** weak (see **TSR**).
6. **Block cracking** and **rutting** accelerate.

**Hydraulic pumping.** Each axle **compresses** pore water; **suction** on uplift **pulls fines** to surface → **mud pumping** visible at **joints**.

**Speed:** **One wet season** opens cracks on **thin overlay**; **3-7 years** to **fair/poor IRI** on neglected windward collectors.

**Severity:** **4** windward; **2** leeward with **good drainage**.

**Routes:** **Hilo Bayfront (Kamehameha Ave)**, **Kalanianaole** windward, **Kuhio** windward Kauaʻi, **Route 11** Hilo approaches.

### 7.2 Ultraviolet Radiation and Heat

**Mechanism.**

1. **UV** breaks **S-S and C-H** bonds in **maltenes**.
2. **Carbonyl formation** stiffens **surface film**.
3. **Fines ravel**; **macrotexture** lost.
4. **Pavement 60-70 C** softens **binder** → **plastic flow** in **wheel paths**.

**Speed:** **Surface graying 1-3 years**; **rutting** one **hot season** on **under-designed** bus stops.

**Severity:** **3** statewide; **4** **Kona**, **H-1** Ewa-Kapolei sun exposure.

### 7.3 Traffic Loading

**Mechanism.**

1. **Contact pressure** **500-800 kPa** class tires.
2. **Vertical compressive strain** in **HMA** and **subgrade**.
3. **Fatigue** initiates **bottom-up cracks**.
4. **Fourth power** of **axle load** on **life** → **containers** dominate.

**Speed:** **Months** on **thin urban** with **drayage**; **years** on **full-depth Interstate**.

**Severity:** **4** **H-1**, **Nimitz**, **Lahaina** frontage; **2** rural **one-lane** low ADT.

**Volume example:** **Honoapiʻilani Highway (Maui 30)** carries on order **17,000 vehicles/day** resort corridor → **fatigue** and **rutting** pressure.

### 7.4 Andisols and Volcanic Ash Soils

**Mechanism.**

1. **Low bulk density** ash/cinder fill **compresses**.
2. **High water retention** → **soft** after rain.
3. **Pavement** bridges **weak layer** → **flexes**.
4. **Settlement** **differential** at **property lines** and **culverts**.

**Speed:** **Weeks to months** post-pave on **unsurcharged** fill.

**Severity:** **4-5** **Puna**, **Volcano**, **Mauna Loa** skirts.

### 7.5 Expansive Clays and Smectite

**Mechanism.**

1. **Montmorillonite** absorbs **water**.
2. **Volume increase** **heaves** pavement.
3. **Dry cycle** **shrinks** → **cracks**.
4. **Repeat** → **roughness** and **reflection**.

**Speed:** **Seasonal** **1-2 years**.

**Severity:** **3** localized **Central Oʻahu**, **Central Maui** pockets.

### 7.6 Coastal Erosion and Wave Action

**Mechanism.**

1. **Wave run-up** undermines **road embankment**.
2. **Cliff retreat** removes **shoulder** and **lane**.
3. **Salt spray** accelerates **steel** corrosion in **guardrail and dowels**.

**Hawaii cases.**

- **Kamehameha Highway (Oʻahu windward)** segments repeatedly **armored**; **Hauula** area projects cited about **$600,000** class for **short protection** works; **long-term** **setback** costs **statewide coastal** programs discussed at **$1.5 billion** class over **decades** (planning figures, all islands).

**Speed:** **One storm** for **washout**; **decades** for **inch-per-year** cliff retreat **North Shore**.

**Severity:** **5** unprotected **coastal** mileage.

### 7.7 Lava Flows

**Mechanism.**

1. **Pāhoehoe** inflates and **buries** grade.
2. **ʻAʻā** ** bulldozes** and **locks** under **rubble**.
3. **Heat** **destroys** **HMA** and **base**.
4. **New rock** **settles** for **years** as **voids** close.

**Puʻu ʻŌʻō era (Kīlauea East Rift).** Repeated **overflows** threatened **Chain of Craters**, **Kalapana** area roads; **inundation** **hours**, **reopen** **years** after **cooling** and **stable** route.

**2018 Lower East Rift (Leilani Estates).**

- About **13 miles** of **road** destroyed or buried in **Puna**.
- Recovery included on order **109,000 cubic yards** **excavation** class **debris removal** and **temporary** **corridor** restoration (HDOT/county reporting scale).

**Speed:** **Hours** inundation.

**Severity:** **5** in **flow path**; **0** upslope mauka corridors unaffected.

### 7.8 Earthquakes

**Mechanism.**

1. **Seismic waves** **shake** **fills** → **liquefaction** if **saturated**.
2. **Fault slip** **offsets** pavement **meters** (rare).
3. **Rockfall** triggered (see 7.9).

**Kīholo Bay earthquake (October 15, 2006).**

- **Magnitude 6.7** and **6.8** pair **Kona** region.
- **Power outages**, **structural** damage; **Highways** **cracking**, **rockfall** **Kona** mauka routes, **bridge** **inspections** statewide.

**Speed:** **Instant**.

**Severity:** **3** statewide background; **4-5** **Big Island** **Kona** **fault** zones.

### 7.9 Rockfall and Landslides

**Mechanism.**

1. **Rain** infiltrates **ash beds** capped by **basalt**.
2. **Pore pressure** **reduces shear strength**.
3. **Blocks** release onto **road prism**.
4. **Maintenance** **scaling** and **barriers**.

**Waimea Bay / Kamehameha Highway (Oʻahu North Shore) rockfall program** cited about **$34.4 million** class **stabilization** (multi-year **mesh**, **bolts**, **barriers**).

**Speed:** **During/after rain**; **slow slides** **weeks**.

**Severity:** **4** **Hana**, **Hāmākua**, **North Shore**, **H-3** **portal** zones.

### 7.10 Thin Structural Sections

**Mechanism.**

1. **Overlay** placed on **weak** base.
2. **Large deflection** → **fatigue** **bottom-up**.
3. **Reflective** cracks **3-5 m** spacing.

**Speed:** **1-3 years** to **wheel path** failure.

**Severity:** **3** **legacy plantation** **county** roads.

### 7.11 Flash Floods

**Mechanism.**

1. **Intense cell** on **leeward** **bare** gulch.
2. **Culvert** **plugged** or **undersized**.
3. **Headcut** **washout** **embankment**.
4. **Road** **gone** **100-300 m** segments.

**Speed:** **Single storm**.

**Severity:** **4-5** **Saddle Road** gulches, **Kawaihae** **dry stream** beds, **Maui** **south** **leeward**.

### 7.12 Hurricanes and Tropical Storms

**Mechanism.**

1. **Wind** **>100 mph** **drops trees** (**albizia**).
2. **Rain** **saturates** **fills**.
3. **Storm surge** **undermines** **coastal**.

**Iniki (1992 Kauaʻi)** benchmark: **total network trauma**, **months** to **restore** **access**.

**Speed:** **One event**.

**Severity:** **5** **direct hit**; **2** **glancing**.

### 7.13 Tsunami

**Mechanism.**

1. **Drawdown** then **surge** **>5 m** in **worst** scenarios.
2. **Scour** **removes** **base**.
3. **Debris** **impact** **loads**.

**Speed:** **Hours** from **seismic** generation.

**Severity:** **5** **Hilo Bay**, **low** **Molokaʻi** **south**, **Kona** **hotel** **coast** **scenario** events.

### 7.14 Salt and Marine Aerosol

**Mechanism (Fick's law).**

**Flux J = -D (dC/dx)**. **Chloride** **concentration gradient** drives **ingress** into **cracks** and **concrete** **pores**.

1. **Salt** **reaches** **rebar** or **aggregate**.
2. **Expansion** and **spalling** on **PCC**; **accelerated** **aggregate** **deterioration** if **contaminated**.

**Speed:** **Years** **within 100 m** of **surf**.

**Severity:** **3** **coastal** **belt** roads.

### 7.15 Trees and Roots

**Mechanism.**

1. **Albizia** **weak wood**, **fast growth**, **shallow root**.
2. **Storm** **fall** **blocks** **road**.
3. **Roots** **heave** **sidewalk** and **curb lane**.

**Speed:** **Storm night** **fall**; **years** **heave**.

**Severity:** **3** **Puna**, **Big Island** **windward** **albizia** **belts**.

### 7.16 Freeze-Thaw

**Mechanism (summits only).**

1. **Nightly freeze** **Mauna Kea**, **Mauna Loa**, **Haleakalā** **>10,000 ft**.
2. **Moisture** **in** **cracks** **expands** **9%** **on** **freeze** (minimal **cycles** at **sea level**).

**Speed:** **Seasonal** on **summit** **gravel/asphalt**.

**Severity:** **1** **most** **lane-miles**; **2** **Mauna Kea** **access** **above** **Visitor** **Center**.

### 7.17 Wildfire

**Mechanism.**

1. **Fire** **softens** or **burns** **surface** **binder**.
2. **Vegetation** **loss** on **cuts** → **next rain** **erosion** **fills** **ditches**.

**Lahaina (2023 Maui)** and **leeward** **grass** **fires** show **adjacent** **road** **heat** **damage** and **debris** **loads** during **evacuation** **surges**.

**Speed:** **Fire** then **next rain** **washout**.

**Severity:** **2** **localized**; **evacuation** **traffic** **loads** **temporary** **4** **severity** **on** **Honoapiʻilani** **during** **crisis**.

### 7.18 Logistics and Import Dependence

**Mechanism.**

1. **Binder** **only** at **Kalaeloa** **scale**.
2. **Tanker delay** or **harbor** **closure** **stops** **plants**.
3. **Patches** **stay** **longer** → **IRI** **rises**.
4. **Neighbor island** **barge** **weather** **delays** **same**.

**2005-2006 crisis** **precursor** to **terminal**; **300,000 barrel** **storage** **buffers** **weeks** not **months** **global** **supply** **shock**.

**Speed:** **Project** **months**.

**Severity:** **2** as **physical** **damage**; **4** as **system** **risk**.

### 7.1 Rain (Extended Notes)

**Waiʻaleʻale** summit rain does not fall on pavement directly, but **orographic forcing** on **Kauaʻi windward** and **Big Island windward** produces **120-200+ inch** class zones where **highways** see **continuous moisture**. **Hilo** at **125 inches** means **pavement** is **rarely dry** at depth for **weeks** in **Hoʻoilo**.

**Maintenance cycle.** Crack seal crews on **Kamehameha Ave** and **Bayfront** treat **linear feet** per **dry window** measured in **days per month**, not **weeks** as on **Phoenix**-class climates.

**Ponding.** Inadequate **crossfall** on **windward** **resurfacing** → **hydroplaning** and **accelerated** **top-down** **oxidation** under **thin water film**.

### 7.2 UV (Extended Notes)

**Latitude 19-22 N** still delivers **high UV index** year-round. **Clear Kona** afternoons combine **UV** and **60-70 C** **surface** → **polymer-modified** binder **cost-effective** on **arterials** despite **import** **premium**.

**Color.** **Gray aggregate** **HMA** **lightens** less than **limestone** mixes; **basalt** **dark** **mat** **absorbs** **more** **heat**.

### 7.3 Traffic (Extended Notes)

**ESAL accumulation** on **H-1** **Ewa** **segment** drives **Ndesign 100-125** **mix** and **75-100 mm** **structural** **overlays** on **failure** **cycles** **8-12 years** without **full** **reconstruction**.

**Tour buses** and **rental** **fleet** add **daily** **repetitions** on **Hana**, **Waimea Canyon**, **Volcano** **routes** with **thin** **sections**.

### 7.4 Andisols (Extended Notes)

**Andisols** (Andisol order) form on **tephra**. **Bulk density** **0.6-0.9 g/cm³** **unsaturated** vs **1.6+** for **compacted** **granular** **base**.

**Design** **mistake:** **Pave** **new** **subdivision** **access** on **scraped** **cinder** **without** **surcharge** → **12-25 mm** **settlement** **first** **year** → **IRI** **jump** **80+ in/mi** **locally**.

### 7.5 Expansive Clay (Extended Notes)

**Smectite** **zones** **map** **patchy**. **Geotechnical** **borings** **before** **widening** **Kamehameha** **V Hwy** **segments** **avoid** **repeat** **heave**.

### 7.6 Coastal (Extended Notes)

**Shoreline** **hard** **armor** **without** **beach** **nourishment** **can** **accelerate** **down-drift** **loss**, **moving** **problem** **along** **shore** **mile** **by** **mile**.

**Hauula** **class** **$600k** **projects** **typify** **short** **reach** **fixes**; **state** **coastal** **highway** **program** **planning** **aggregates** **setback** **and** **raise** **costs** at **$1.5B** **class** **decades** **scale** (all islands, inflation-sensitive).

### 7.7 Lava (Extended Notes)

**Chain of Craters** **closed** **1990s** **flows**; **reopen** **requires** **stable** **lava** **field** **and** **NPS/HDOT** **agreement**.

**2018** **Leilani** **event** **taught** **logistics:** **hot** **mix** **competed** with **housing** **base** **pads** for **same** **plant** **hours**; **109k cy** **excavation** **scale** **shows** **earthwork** **before** **pave** **returns**.

**Puʻu ʻŌʻō** **1983-2018** **activity** **repeatedly** **threatened** **Kalapana** **area** **access**; **flow** **speed** **m/h** **on** **steep** **slopes** **exceeds** **road** **relocation** **planning** **speed**.

### 7.8 Earthquake (Extended Notes)

**2006 Kīholo Bay** **pair** **damaged** **Hawaiian** **homes** and **triggered** **inspection** **protocols** for **bridges** **statewide**. **Pavement** **cracking** **on** **fill** **approaches** **to** **Queen Kaʻahumanu** **near** **epicentral** **region**.

**Magnitude** **6+** **events** **expect** **every** **few** **decades** **Big Island**; **design** **seismic** **joint** **width** on **major** **bridges**.

### 7.9 Rockfall (Extended Notes)

**Waimea Bay** **$34.4M** **program** **illustrates** **cost** **to** **stabilize** **iconic** **North Shore** **mile** **vs** **cheap** **rural** **lane**.

**H-3** **tunnel** **portals** **require** **daily** **inspection** **after** **heavy** **rain** **events**.

**Hana** **Highway** **landslides** **close** **route** **for** **tourist** **and** **resident** **supply**; **helicopter** **cost** **externalized** **to** **community**.

### 7.10 Thin Sections (Extended Notes)

**Plantation** **roads** **built** **6-8 inch** **total** **structure** for **light** **trucks**; **modern** **SUV** **and** **delivery** **fleet** **exceed** **design** **ESAL** **10x**.

### 7.11 Flash Floods (Extended Notes)

**Kawaihae** **under** **10 in/yr** **mean** **misleading**; **single** **Kona** **storm** **can** **drop** **6+ inches** **in** **hours** on **bare** **lava** **catchments**.

**Kauaʻi April 2018** **rain** **event** **flooded** **north** **shore** **communities**; **road** **recovery** **about** **14 months** **class** **for** **full** **access** **restoration** **reporting** **on** **Kūhiō** **Highway** **segments**.

### 7.12 Hurricanes (Extended Notes)

**Iniki** **1992** **Kauaʻi** **remains** **benchmark** **for** **total** **road** **network** **damage** **from** **one** **cyclone** **in** **Hawaii**.

**Climate** **change** **tracks** **debated**; **planning** **still** **uses** **Iniki** **plus** **margin**.

### 7.13 Tsunami (Extended Notes)

**Hilo** **1960** **Chile** **tsunami** **history** **defines** **vertical** **evacuation** **zones** **affecting** **coastal** **road** **prism** **design** **(elevation** **of** **new** **alignments).

### 7.14 Salt (Extended Notes)

**Fickian** **diffusion** **coefficient** **D** **higher** in **cracked** **HMA** than **sound** **mat**; **seal** **cracks** **slows** **chloride** **front**.

**Bridge** **decks** **coastal** **use** **epoxy** **coated** **rebar** **where** **specified**.

### 7.15 Trees (Extended Notes)

**Albizia** **Falcataria** **invades** **disturbed** **windward** **lots**; **fallen** **trunk** **blocks** **both** **lanes** **Puna** **class** **roads** **monthly** **in** **storm** **season** without **cutting** **programs**.

### 7.16 Freeze-Thaw (Extended Notes)

**Mauna Kea** **Visitor** **Information** **Station** **at** **9,200 ft** **sees** **occasional** **ice**; **summit** **road** **above** **restricted** **to** **4WD** **and** **special** **use** **with** **seasonal** **closure**.

**Sea level** **Hawaii** **freeze-thaw** **severity** **1** **justified**.

### 7.17 Wildfire (Extended Notes)

**Lahaina** **2023** **evacuation** **loaded** **Honoapiʻilani** and **Kuihelani** **beyond** **design** **traffic** **→** **surface** **shear** **and** **shoulder** **damage** **from** **soft** **shoulders** **and** **debris**.

**Post-fire** **rain** **on** **burned** **slopes** **above** **Lahaina** **highway** **raises** **7.11** **chain** **risk**.

### 7.18 Logistics (Extended Notes)

**Star-Advertiser** **2013** **reporting** **cited** **~75,000 tons** **liquid** **asphalt** **to** **make** **~1.2M tons** **pavement** **2012** **statewide**.

**Single-supplier** **concentration** **post-refinery** **exit** **motivated** **300,000 barrel** **Kalaeloa** **farm**; **still** **one** **harbor** **node** **for** **bulk** **binder**.

**Neighbor island** **plants** **depend** **on** **barge** **binder** **and** **aggregate** **imports** **for** **some** **fractions**.

---

## Appendix A. Quarter-Car Simulation (Numerical Steps)

1. **Sample** profile **z(x)** at **delta x <= 0.25 m**.
2. **Apply** **high-pass** filter removing **wavelengths** **> 300 m** (per protocol variant).
3. **Initialize** **quarter-car** **state** **variables** **y, dy/dt** at **speed** **80 km/h**.
4. **Integrate** **equations** **using** **k1=653**, **c=6.0**, **k2/ms=63.3**, **mu=0.15**.
5. **Accumulate** **|dy/dx|** over **segment** **length** **L**.
6. **Report** **IRI** **m/km** and **convert** **in/mi** **if** **required**.

## Appendix B. AASHTO 1993 SN Example (Illustrative)

**Given** **HMA** **2.0 in**, **a1=0.44**; **base** **6 in**, **a2=0.14**, **m2=1.0**; **subbase** **8 in**, **a3=0.11**, **m3=1.0**:

**SN = 0.44*2 + 0.14*6*1 + 0.11*8*1 = 0.88 + 0.84 + 0.88 = 2.60**

**Thin** **overlay-only** **SN** **without** **base** **fix** on **andisol** **fails** **when** **calculated** **ESALs** **exceed** **chart** **allowable** **for** **subgrade** **CBR** **< 4**.

## Appendix C. HDOT and County Maintenance Split

- **HDOT** **state** **routes** **(numbered** **highways**, **Interstates)**.
- **County** **maintains** **most** **local** **collectors** **and** **residential** **frontage**.
- **Federal-aid** **overlays** **on** **NH** **system** **require** **IRI** **reporting**.

**Windward** **county** **mileage** **often** **shows** **worst** **public** **IRI** **because** **budget** **per** **lane-mile** **lower** **than** **Interstate** **program**.

## Appendix D. Piʻilani Highway and Maui South Shore Development

**Piʻilani** **Highway (Route 31)** **connects** **Kihei**, **Wailea**, **Makena** **resort** **growth** **to** **Kahului** **port** **and** **airport**. **Decades** **of** **widening** **from** **two-lane** **coastal** **to** **four-lane** **divided** **sections** **track** **17k+** **vpd** **class** **loads** **on** **Honoapiʻilani** **corridor** **parallel**.

**Subgrade** **on** **young** **Maui** **lava** **fields** **requires** **thick** **base** **like** **Oʻahu** **but** **with** **longer** **aggregate** **haul** **from **central** **Maui** **pits**.

## Appendix E. Kingdom Road Law Concepts (Historical)

**Mōʻī** **period** **statutes** **addressed** **obstructions**, **animals** **on** **road**, **width** **of** **cart** **paths** **near** **Honolulu** **harbor**. **Western-style** **survey** **and** **ROW** **width** **emerged** **late** **1800s** **with** **sugar** **capital**.

**Ala loa** **vs** **mauka** **trails** **still** **visible** **on** **some** **Ahupuaʻa** **maps** **(`HawaiianNativeLandscape.md`)**.

## Appendix F. Intelligent Compaction CMV Interpretation

**CMV** **not** **directly** **density**; **correlate** **on** **project** **via** **cores**. **Soft** **CMV** **stripe** **at** **constant** **pass** **→** **add** **pass** **or** **lower** **vibration** **if** **aggregate** **crushing**.

## Appendix G. MTV Throughput

**Typical** **MTV** **feed** **300-600** **tons/hour** **to** **paver** **vs** **200-350** **direct** **dump** **with** **segregation** **risk**.

## Appendix H. WMA Temperature Reduction

**WMA** **allows** **15-30 C** **lower** **mix** **temperature** **→** **extends** **rolling** **window** **on** **Hawaiʻi** **Island** **afternoon** **thunder** **showers** **risk** **days**.

## Appendix I. Concrete Pavement Joints in Hawaii

**Doweled** **transverse** **joints** **every** **4-5 m**; **sealant** **failure** **→** **corners** **spall** **under** **container** **loads** **at** **Barbers** **Point** **access**.

## Appendix J. Pothole Repair Decision Tree

1. **Is** **base** **sound?** **No** → **full-depth** **patch** **min** **150 mm** **HMA** **+** **base** **fix**.
2. **Is** **cavity** **dry?** **No** → **wait** **or** **infrared** **dry** **(rare** **windward)**.
3. **Apply** **tack**, **hot** **mix**, **compact** **with** **vibratory** **plate**.
4. **Seal** **patch** **joint** **if** **wide** **temperature** **swing** **expected**.

## Appendix K. ESAL Fourth Power Numeric Example

If **strain** **ratio** **0.8** **(20%** **higher** **strain** **due** **thin** **section**):

**Life ratio ≈ (1/0.8)^4 = 1.56^4 ≈ 5.9** **→** **less** **than** **one-fifth** **life** **vs** **design** **strain**.

## Appendix L. Reading IRI on a Profile Printout

**Long** **wave** **peak** **30 m** ** wavelength** **0.05 m** ** amplitude** **can** **produce** **IRI** **1.2-1.8 m/km** **alone** **on** **otherwise** **smooth** **mat**.

## Appendix M. Basalt Aggregate Polishing Mechanism

**Microtexture** **wears** **under** **tire** **→** **polished** **basalt** **friction** **drops** **SN40** **below** **36** **on** **curves** **→** **OGFC** **or** **HFST** **overlay**.

## Appendix N. Kalaeloa Terminal Operations Snapshot

**Rack** **hours** **typical** **weekday** **0630-1400** **(`Asphalt** **Hawaii`)**. **Tanker** **discharge** **heated** **lines** **from** **Piers** **6-7**. **Polymer** **modification** **blended** **for** **SMA** **airport** **jobs**.

## Appendix O. Saddle Road History Sketch

**Original** **Saddle** **gravel** **military** **road** **connecting** **Hilo** **side** **to** **Waimea/Kona** **access** **without** **circumnavigation** **via** **south**. **Modernization** **~$316.5M** **class** **improved** **alignment**, **wildlife** **crossings**, **shoulders**, **design** **speed**. **Still** **exposed** **to** **7.11** **flash** **floods** **in** **gulches**.

## Appendix P. H-1, H-2, H-3 Cost and Traffic Context

| Route | Opened / key date | Cost class (historical) | Role |
|---|---|---|---|
| H-1 | Stages 1960s-1990s | Multi-billion cumulative | Urban Oʻahu spine |
| H-2 | 1976 | Hundreds of millions class | Central access |
| H-3 | 1997 | ~$1.3B class | Windward-leeward link |

**H-3** **tunnels** **reduce** **Pali** **Highway** **and** **Likelike** **congestion** **for** **Kaneohe/Kailua** **commuters**; **maintenance** **budget** **tunnel** **ventilation** **and** **fire** **life** **safety** **dominates** **routine** **cost**.

## Appendix Q. Profilograph Bump Count Example

**PPI** **> 7 in/mi** **on** **airport** **section** **→** **diamond** **grind** **plan** **to** **restore** **before** **747** **class** **fatigue** **(historical** **FAA** **criteria** **family)**.

## Appendix R. Drainage Coefficient Design Choice

**Windward** **project** **without** **underdrain** **→** **use** **Cd=0.85** **in** **SN** **calculation** **→** ** thicker** **base** **required** **vs** **Cd=1.0** **desert** **mainland** **peer**.

## Appendix S. Lime Stabilization Recipe Sketch

**Quicklime** **4-6%** **by** **dry** **weight** **of** **soil**, **mix**, ** mellow** **24-48 hr**, **compact** **to** **Proctor** **→** **PI** **reduction** **on** **clay** **for** **subgrade** **platform**.

## Appendix T. Geotextile Separation Layer

**AASHTO** **Class** **1** **or** **2** **nonwoven** **between** **silty** **andisol** **and** **base** **prevents** **pumping** **fines** **upward** **under** **7.1** **rain** **loading**.

## Appendix U. Bridge Approach Geofoam Note

**EPS** **geofoam** **blocks** **reduce** **vertical** **stress** **on** **weak** **approach** **fill** **by** **order** **of** **magnitude** **vs** **earth** **fill** **→** **limits** **post-construction** **settlement** **bump**.

## Appendix V. Wick Drain Spacing

**Vertical** **drains** **1-2 m** **spacing** **accelerate** **consolidation** **of** **soft** **coastal** **fill** **before** **pave** **(months** **vs** **years** **wait)**.

## Appendix W. Preventive Maintenance Priority on Windward Mile

**Crack** **seal** **> chip** **seal** **> overlay** **when** **IRI** **still** **< 2.5 m/km** **and** **structural** **cores** **show** **Va** **in** **spec**.

## Appendix X. Star-Advertiser Supply Chain Summary

**Canada** **and** **Gulf** **binder** **→** **Panama** **→** **Kalaeloa** **→** **three** **major** **Oʻahu** **contractors** **→** **neighbor** **island** **barge**. **Over** **90%** **roads** **asphalt** **surfaced**.

## Appendix Y. 2018 Kauaʻi Flood Road Recovery Timeline

**North** **shore** **isolated** **by** **multiple** **slides** **and** **bridge** **damage**; **full** **restoration** **order** **14 months** **class** **for** **some** **Kūhiō** **Highway** **segments** **(reporting** **round** **figure** **for** **planning** **invent)**.

## Appendix Z. Invent Use for Dragnis-Class Fiction

When **staging** **road** **travel** **beats**, **match** **IRI** **band** **to** **vehicle** **(see** **`Suspension.md`)** **and** **damage** **rank** **1-7** **to** **which** **side** **of** **island** **the** **chapter** **uses** **(windward** **rain** **vs** **leeward** **UV** **vs** **mauka** **rockfall** **vs** **Puna** **andisol** **vs** **coastal** **setback** **threat** **without** **naming** **future** **chapters** **beyond** **scope** **files** **in** **repo).

### 4.16 Binder PG Selection for Hawaii Climate Zone

| Location | Suggested PG high (typical) | Notes |
|---|---|---|
| Honolulu urban | PG 70-22 | Traffic bumps to 76-22 at heavy intersections |
| Hilo windward | PG 64-22 + strong anti-strip | Rain TSR governs |
| Kona leeward | PG 70-22 or polymer | Heat rutting |
| Summit access | PG 64-28 | Low temp rare issue |

### 4.17 Plant Quality Control Tests Each Shift

- **Gradation** **on** **cold** **feed** **and** **hot** **bins**.
- **Binder** **content** **ignition** **oven** **or** **nuclear**.
- **Mix** **temperature** **truck** **load**.
- **Gmb** **from** **gyratory** **compaction** **correlation**.

### 5.13 Chip Seal on County Windward Roads

**Single** **chip** **seal** **extends** **life** **5-7** **years** **when** **base** **sound** **and** **cracks** **sealed** **first** **→** **common** **Kauaʻi** **county** **strategy** **where** **overlay** **budget** **thin**.

### 5.14 Bridge Deck Asphalt Overlay on Concrete

**Waterproof** **membrane** **+** ** adhesive** **+** **HMA** **wearing** **course** **on** **PCC** **deck** **→** **thermal** **reflective** **cracks** **managed** **with** **reinforced** **fabric** **interlayer**.

### 6.13 H-3 Environmental and Archaeological Context

**Haʻiku** **Valley** **viaduct** **and** **tunnel** **portal** **areas** **required** **archaeological** **monitoring** **and** **endangered** **species** **protocols** **during** **construction** **→** **cost** **and** **delay** **factors** **in** **$1.3B** **class** **total**.

### 6.14 Molokaʻi and Lānaʻi Road Network Scale

**Molokaʻi** **Kamehameha** **V** **Highway** **primary** **circumferential** **;** **Lānaʻi** **single** **paved** **loop** **with** **logistics** **from** **Manele** **harbor** **→** **7.18** **magnified** **per** **lane-mile**.

### 7.1 Rain: Hilo Bayfront Maintenance Window Math

**Average** **125** **in/yr** **≈** **3.2** **mm/day** **long-term** **;** **many** **days** **with** **zero** **sun** **dry** **hours** **→** **effective** **crack** **seal** **productivity** **50-200** **lf/day/crew** **vs** **500+** **mainland** **desert**.

### 7.3 Traffic: Container Drayage on Nimitz and H-1

**Peak** **axle** **loads** **legal** **80,000** **lb** **GVW** **class** **→** **ESAL** **per** **trip** **high** **→** **intersection** **approach** **rutting** **primary** **complaint** **near** **Barbers** **Point**.

### 7.7 Lava: Chain of Craters Road Mile Markers

**Mile** **markers** **buried** **repeatedly** **1986-2018** **period** **→** **NPS** **does** **not** **plan** **reopen** **through** **active** **field** **without** **stable** **decade** **quiet**.

### 7.11 Flash Flood: Kauaʻi 2018 Specifics

**April** **2018** **record** **rain** **north** **shore** **→** **landslides** **on** **Kūhiō** **Highway** **→** **community** **isolation** **Hanalei** **→** **recovery** **timeline** **~14** **months** **class** **for** **full** **highway** **function** **(invent** **planning** **figure** **from** **public** **reporting** **round** **numbers)**.

### 8.4 Severity vs Speed Matrix (Cross-Plot)

|  | Fast onset (hours-season) | Slow onset (years) |
|---|---|---|
| **Severity 5** | Lava, tsunami, hurricane direct | Coastal retreat (decades) |
| **Severity 4** | Flash flood, earthquake+rockfall | Rain on thin section |
| **Severity 3** | Rockfall rain event | UV, traffic fatigue |
| **Severity 2** | Wildfire debris load | Salt aerosol |
| **Severity 1** | - | Summit freeze cosmetic |

### 8.5 Long-Term Rank 1-7 Restated with Lane-Mile Weighting

**Rank** **1** **rain** **because** **>60%** **state** **population** **lives** **windward** **of** **mountain** **crest** **or** **in** **Hilo-equivalent** **rain** **regimes** **on** **Big** **Island** **and** **Kauaʻi**. **Rank** **2** **traffic** **because** **Oʻahu** **concentrates** **ESALs** **even** **when** **neighbor** **islands** **are** **quiet**. **Rank** **7** **lump** **catastrophic** **low-frequency** **events** **that** **nonetheless** **define** **emergency** **appropriations**.

### 9.1 Additional Hawaii URLs

- HDOT news and projects: https://hidot.hawaii.gov/
- County of Kauaʻi infrastructure: https://www.kauai.gov/
- County of Maui Public Works: https://www.mauicounty.gov/
- City and County of Honolulu Department of Transportation Services: https://www.honolulu.gov/dts.html
- USGS Earthquake Catalog Hawaii: https://earthquake.usgs.gov/
- Hawaii State Climate Office: https://climate.hawaii.edu/

---

## 8. Summary Table: Speed and Severity

### 8.1 All Mechanisms (18 Rows)

| ID | Mechanism | Onset speed | Severity (1-5) | Primary Hawaii exposure |
|---|---|---|---|---|
| 7.1 | Rain / hydraulic pumping | 1 season to 7 yr | 4 (windward) | Hilo 125 in/yr, windward Oʻahu, Kauaʻi |
| 7.2 | UV / heat aging | 1-3 yr surface | 3-4 | Kona, H-1, parking lots |
| 7.3 | Traffic / ESAL fatigue | Months to years | 4 | H-1, Honoapiʻilani ~17k vpd |
| 7.4 | Andisols / ash fills | Weeks to months | 4-5 | Puna, Volcano subdivisions |
| 7.5 | Expansive clay | 1-2 seasons | 3 | Central Oʻahu, Central Maui |
| 7.6 | Coastal erosion | Storm to decades | 5 | Hauula armor $600k class; $1.5B coastal plan class |
| 7.7 | Lava inundation | Hours | 5 in path | 2018: ~13 mi roads; ~109k cy excavation class |
| 7.8 | Earthquake | Instant | 3-5 | Kīholo Bay 2006 M6.7/6.8 |
| 7.9 | Rockfall / landslide | Rain event | 4 | Waimea Bay $34.4M stabilization class |
| 7.10 | Thin structural section | 1-3 years | 3 | Legacy county roads |
| 7.11 | Flash flood washout | Single storm | 4-5 | Kawaihae under 10 in/yr until cell hits |
| 7.12 | Hurricane | Single event | 5 direct | Iniki 1992 Kauaʻi |
| 7.13 | Tsunami scour | Hours | 5 low coast | Hilo Bay history |
| 7.14 | Salt (Fick ingress) | Years coastal | 3 | Belt highways near surf |
| 7.15 | Trees / albizia | Storm / years | 3 | Big Island windward |
| 7.16 | Freeze-thaw | Seasonal summit | 1-2 | Mauna Kea access high |
| 7.17 | Wildfire + erosion | Fire then rain | 2-4 crisis | Lahaina corridor evacuation loads |
| 7.18 | Binder logistics | Months delay | 2-4 system | Kalaeloa 300k bbl buffer |

**Speed key:** *Instant* = hours or less. *Season* = one wet or dry period. *Years* = aging without catastrophic trigger.

### 8.2 Combination Chains (How Failures Stack)

| Chain step A | Step B | Step C | Outcome |
|---|---|---|---|
| Rain (7.1) | Weak TSR / stripping | Traffic (7.3) | Rapid ravel + potholes in one wheel path |
| Thin section (7.10) | Rain pumping | Fair IRI in 18 months | County road rehab list |
| Flash flood (7.11) | Emergency cold patch | Logistics delay (7.18) | Rough segment stays 2+ years |
| Lava (7.7) | Excavation backlog | Import binder queue | Puna recovery competition for plants |
| Coastal erosion (7.6) | Tsunami (7.13) same mile | Setback rebuild | Complete alignment change |
| Earthquake (7.8) | Rockfall (7.9) | Lane closure weeks | North Kona / H-3 portal protocols |
| Wildfire (7.17) | Rain erosion | Culvert plug (7.11) | Leeward gulch washout next storm |
| UV (7.2) | Heavy traffic (7.3) | Rutting same summer | Intersection rebuild before overlay life |
| Andisol (7.4) | New pave without surcharge | Differential compaction (Sec 2.3) | 4 mm dips at manholes on new subdivisions |

### 8.3 Ranked Long-Term Impact on the Hawaii Network (1 = Highest)

Planning rank merges **severity**, **lane-miles exposed**, **recurrence**, and **cost to restore**.

| Rank | Mechanism | Why it ranks here |
|---|---|---|
| **1** | Rain, drainage, hydraulic pumping | Most windward lane-miles; Waiʻaleʻale 450 in class vs Kawaihae under 10 in shows gradient |
| **2** | Traffic loading (ESAL, fourth power) | H-1, ports, Maui 17k vpd corridors define structural demand |
| **3** | UV and heat aging | Every asphalt mile; Kona heat softens binder annually |
| **4** | Rockfall and landslides | Cliff routes (Hana, Hāmākua, North Shore) need perpetual retention $ |
| **5** | Andisols and weak volcanic fills | Puna/Volcano growth zones; settlement in months |
| **6** | Coastal erosion and sea level | Lower mileage but $1.5B class planning stakes |
| **7** | Lava, hurricane, tsunami, earthquake | Catastrophic but geographically or temporally bounded |

**Rank 7 group** still drives **emergency budgets** (2018 lava, Iniki, Kīholo, tsunami maps) even when **average annual** lane impact is lower than **chronic rain**.

**Logistics (7.18)** is a **multiplier** on ranks **1-5**: when Kalaeloa supply slips, maintenance on rain-damaged windward miles backs up first.

---

## 9. Sources

Hawaii-specific and pavement-engineering references for this invent file.

### Hawaii DOT and State

- HDOT Highways: https://hidot.hawaii.gov/highways/
- HDOT H-3 Freeway: https://hidot.hawaii.gov/highways/h-3/
- HDOT Harbors (Kalaeloa Barbers Point): https://hidot.hawaii.gov/harbors/
- Kalaeloa Fuel Pier BCA (Grace Pacific / GLP Asphalt terminal description): https://hidot.hawaii.gov/harbors/files/2019/03/2017_Plasch_Kalaeloa-Barbers-Point-Harbor-Fuel-Pier-BCA.pdf
- Kalaeloa Asphalt Terminal FONSI/EA (2007): https://files.hawaii.gov/dbedt/erp/EA_EIS_Library/2007-06-08-OA-FEA-Kalaeloa-Asphalt-Terminal.pdf
- Hawaii climate data portal (rainfall gradients): https://www.hawaii.edu/climate-data-portal/
- DBEDT environmental documents library: https://files.hawaii.gov/dbedt/erp/EA_EIS_Library/

### Asphalt Supply and Industry (Hawaii)

- Asphalt Hawaii: https://www.asphalthawaii.com/
- Hawaii Asphalt Paving Industry Association, Kalaeloa terminal: https://hawaiiasphalt.org/how-a-kalaeloa-facility-has-served-the-asphalt-industry-in-hawaii-for-over-a-decade/
- Honolulu Star-Advertiser, isle climate harsh on asphalt / import chain: https://www.staradvertiser.com/2013/03/24/hawaii-news/isle-climate-harsh-on-asphalt/
- Grace Pacific (aggregate, HMA production context): https://www.gracepacific.com/

### Geology, Volcanoes, Earthquakes

- USGS Hawaiian Volcano Observatory: https://www.usgs.gov/observatories/hvo
- 2018 Kīlauea lower east rift eruption impacts (USGS/HVO summaries): https://www.usgs.gov/observatories/hvo
- USGS Kīholo Bay earthquake October 15, 2006: https://www.usgs.gov/earthquakes/eventpage/ci3140465
- NPS Hawaiʻi Volcanoes, Chain of Craters Road: https://www.nps.gov/havo/planyourvisit/chain-of-craters-road.htm

### Soils, Rainfall, Hazards

- NRCS Hawaii soil surveys (andisols): https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geo-database
- NOAA Central Pacific Hurricane Center: https://www.nhc.noaa.gov/cphc/
- NOAA tsunami.gov Hawaii products: https://www.tsunami.gov/
- Kauaʻi flood recovery reporting (2018): https://www.kauai.gov/

### Federal Pavement Methods

- FHWA IRI and smoothness: https://www.fhwa.dot.gov/pavement/smoothness/
- FHWA HMA handbook: https://www.fhwa.dot.gov/pavement/asphalt/pubs/hma_handbook/
- FHWA intelligent compaction: https://www.fhwa.dot.gov/pavement/asphalt/ic/
- AASHTO M 323 PG binder (via state adoptions)
- NCHRP 648 Intelligent Compaction: https://www.trb.org/Publications/Blurbs/163848.aspx
- Asphalt Institute MS-2 mix design: https://www.asphaltinstitute.org/
- World Bank IRI quarter-car (Sayers et al.): https://www.worldbank.org/en/topic/transport

### Routes, Projects, News (Representative)

- FHWA Interstate route log (H-1, H-2, H-3): https://www.fhwa.dot.gov/planning/national_highway_system/interstate_highway_system/routefinder/
- Daniel K. Inouye Highway (Saddle Road) program summaries via HDOT: https://hidot.hawaii.gov/highways/
- HDOT / county news releases on Puna 2018 road recovery and North Shore rockfall programs (search hidot.hawaii.gov)

---

## See also

- `../../Science/Vehicle/Roads.md` - layer stack, era ladder, Caldris filter
- `../../Science/Vehicle/HawaiianTransport.md` - island mobility verdict vs road building
- `Weather.md` - rain, trades, Kona storms, hurricane season
- `HawaiianBiomes.md` - elevation, windward vs leeward context
- `HawaiianNativeLandscape.md` - ahupuaʻa trails and human geography
- `HawaiianMinerals.md` - basalt aggregate and element inventory
- `Index.md` - Volcanic Island file list
