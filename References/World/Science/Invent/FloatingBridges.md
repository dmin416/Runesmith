# Floating Bridges: Science, Engineering, Construction and Buoyancy Mathematics

> Earth reference / invent loot. Not locked law. Structural materials: `../../Materials/BuildingMaterials.md`. Trails / drainage: `TrailBuilding.md`. Farm construction: `FarmBuildings.md`. Roads: `../Vehicle/Roads.md`. Island roads: `../../Geography/VolcanicIsland/HawaiianRoads.md`.

Nav: `Index.md`.

---

## Contents

1. What a Floating Bridge Is
2. History and Notable Bridges
3. Buoyancy Fundamentals
4. Hydrostatic Equations for Pontoon Shapes
5. Hydrostatic Stability
6. Structural Mechanics: The Bridge as a Beam on an Elastic Foundation
7. Environmental Loads
8. Dynamics: Heave, Roll and Resonance
9. Mooring and Anchorage
10. Watertightness, Flooding and Damage Stability
11. Materials
12. Engineering Design Process (Highway Scale)
13. Construction Methods
14. Building a Small Floating Footbridge or Dock
15. Military and Emergency Floating Bridges
16. Difficulty Assessment
17. Failure Modes and Case Studies
18. Worked Examples (Full Calculations)
19. Python Calculator
20. Reference Tables
21. Equation Cheat Sheet
22. Glossary

---

## 1. What a Floating Bridge Is

A floating bridge carries its loads to the water instead of to the ground. Every newton of dead load (structure) and live load (traffic, people, snow) is balanced by the buoyant force of displaced water. Piers and foundations are replaced by pontoons, anchors and cables.

### 1.1 When a floating bridge is the right answer

| Site condition | Why it favors floating |
|---|---|
| Very deep water | Pier foundations become impractical once depth passes roughly 50 to 60 m. Lake Washington reaches about 60 m (200 ft). |
| Very soft lakebed or seabed | Deep mud or soft sediment cannot support piers economically. |
| Long crossing with low current | Floating cost scales roughly linearly with length; suspension spans scale much worse past their economic range. |
| Curved alignment | A floating structure can follow a curve; a long suspension bridge cannot. |
| Temporary or tactical need | Military and emergency crossings must be built in hours and removed later. |
| Seismic regions | The floating section is isolated from ground shaking (the transitions and anchors are not). |

### 1.2 When it is the wrong answer

* Strong currents (anchors and drag forces grow with velocity squared)
* Large tidal ranges (transition spans become long and complex)
* Long open fetch with large waves (wave loads dominate and become expensive)
* Heavy ice flows
* Busy deep-draft shipping lanes (navigation openings are complex and slow)

### 1.3 Classification

| Type | Description | Typical use |
|---|---|---|
| Continuous pontoon | Pontoons rigidly joined end to end into one long floating girder; deck sits on or above the pontoons | Washington State highway bridges |
| Separated (discrete) pontoon | Individual floats spaced apart with a girder or truss spanning between them | Norwegian fjord bridges (Bergsøysund, Nordhordland), historic boat bridges |
| Ribbon / folding bay | Hinged aluminum bays that unfold on the water and pin together | Military bridging (Improved Ribbon Bridge and similar) |
| Treadway / balk on pontoons | Pneumatic or rigid floats carrying track treads | WWII era military bridges |
| Modular cube or float system | Small plastic or foam units bolted together | Docks, marinas, temporary footbridges, event crossings |
| Submerged floating tunnel | Buoyant tube held below the surface by tethers | Proposed for deep Norwegian fjords; not yet in traffic service |

---

## 2. History and Notable Bridges

### 2.1 Ancient and pre-industrial

| Date | Bridge | Notes |
|---|---|---|
| c. 513 BC | Darius I across the Bosporus | Boat bridge for a Persian invasion force |
| 480 BC | Xerxes across the Hellespont | Two lines of lashed ships with cables; the first set was destroyed by a storm and rebuilt |
| Han to Tang dynasties | Chinese boat bridges | The Pujin bridge over the Yellow River used massive cast-iron oxen (Tang era) as shore anchors for its chains |
| 1812 | Berezina crossing | Napoleonic pontonniers built trestle and pontoon bridges in freezing water |
| 1940s | WWII Rhine crossings | Bailey pontoon and treadway bridges assembled under fire |

### 2.2 Modern permanent floating bridges

| Bridge | Location | Opened | Type | Notes |
|---|---|---|---|---|
| Lacey V. Murrow Memorial | Lake Washington, I-90 | 1940 | Continuous concrete pontoon | First concrete floating bridge; sank in 1990 during renovation; replacement opened 1993 |
| Hood Canal Bridge | Hood Canal, WA | 1961 | Continuous pontoon in saltwater with tides | West half sank in a 1979 windstorm; rebuilt; east half replaced in 2009 |
| Original Evergreen Point (SR 520) | Lake Washington | 1963 | Continuous pontoon | Replaced in 2016 |
| Homer M. Hadley | Lake Washington, I-90 | 1989 | Continuous pontoon | Parallel to the Murrow bridge |
| Bergsøysund | Norway | 1992 | Separated pontoons with steel truss | Curved in plan; anchored only at the ends |
| Nordhordland | Norway | 1994 | Separated pontoons with steel box girder | Curved in plan; end anchored; elevated high-level section for ships |
| William R. Bennett | Okanagan Lake, Canada | 2008 | Continuous pontoon | Includes a lift span for boats |
| New Evergreen Point (SR 520) | Lake Washington | 2016 | Continuous concrete pontoon | Longest floating bridge in the world; floating section 7,710 ft (2,350 m) |

**SR 520 key figures (2016 bridge):** 77 concrete pontoons in total. The 21 longitudinal pontoons are each about 360 ft long, 75 ft wide and 28 to 29 ft tall, weighing about 11,000 tons each. The bridge is held by 58 anchors, the largest weighing about 450 tons. Pontoons were cast in Aberdeen and Tacoma, floated out of casting basins, towed and bolted together on the lake. The reported design capacity includes sustained winds of roughly 89 mph (143 km/h). WSDOT identifies wind and wave forces as the controlling loads for floating bridge design, with fetch as the primary driver of wave size.

---

## 3. Buoyancy Fundamentals

### 3.1 Archimedes' principle

A body immersed in a fluid experiences an upward force equal to the weight of the fluid it displaces.

$$F_B = \rho_w \, g \, \nabla$$

| Symbol | Meaning | SI unit |
|---|---|---|
| $F_B$ | Buoyant force | N |
| $\rho_w$ | Water density | kg/m³ |
| $g$ | Gravitational acceleration, 9.81 | m/s² |
| $\nabla$ | Displaced volume (submerged volume) | m³ |

### 3.2 Equilibrium (free floating)

A floating body settles until buoyancy equals total weight:

$$\rho_w \, g \, \nabla = W = m g \quad\Rightarrow\quad \nabla = \frac{m}{\rho_w}$$

Displacement $\Delta$ is the mass of displaced water and equals the total floating mass:

$$\Delta = \rho_w \nabla = m_{total}$$

### 3.3 Why a concrete box floats

Concrete has a density near 2,400 kg/m³, far heavier than water. A pontoon floats because its **effective density** (total mass divided by total enclosed envelope volume) is below that of water:

$$\rho_{eff} = \frac{m_{structure} + m_{contents}}{V_{envelope}} < \rho_w$$

A hollow concrete box with walls that occupy 20 percent of its envelope has an effective density of about $0.20 \times 2400 = 480$ kg/m³. It floats roughly half submerged before any deck or traffic is added.

### 3.4 Draft, freeboard and reserve buoyancy

| Term | Definition |
|---|---|
| Draft $T$ | Depth from waterline to the pontoon bottom |
| Depth $D$ | Total pontoon height |
| Freeboard $f$ | $f = D - T$ (height of pontoon wall above water) |
| Reserve buoyancy | Unused watertight volume above the waterline: $V_{reserve} = V_{envelope} - \nabla$ |
| Reserve buoyancy ratio | $R = V_{reserve} / \nabla$; highway pontoons often carry large ratios because flooding of one cell must not sink the bridge |

Reserve buoyancy force:

$$F_{reserve} = \rho_w \, g \, (V_{envelope} - \nabla)$$

This is the extra load that would push the pontoon to the point of submergence. A safe design never uses all of it.

### 3.5 Fresh versus salt water

| Water | Density (kg/m³) | Specific weight (kN/m³) | Specific weight (lb/ft³) |
|---|---|---|---|
| Fresh, 4 °C | 1000 | 9.81 | 62.4 |
| Fresh, 20 °C | 998 | 9.79 | 62.3 |
| Brackish (typical estuary) | 1010 to 1020 | 9.91 to 10.0 | 63.0 to 63.7 |
| Sea water | 1025 | 10.06 | 64.0 |

The same pontoon floats deeper in fresh water:

$$T_{fresh} = T_{salt}\,\frac{\rho_{salt}}{\rho_{fresh}} \approx 1.025\,T_{salt}$$

Hood Canal is salt water; Lake Washington is fresh. A pontoon towed from a saltwater casting site into a freshwater lake sinks about 2.5 percent deeper on arrival. This is the Fresh Water Allowance (FWA) used in ship loading.

---

## 4. Hydrostatic Equations for Pontoon Shapes

### 4.1 Rectangular box pontoon

Waterplane area: $A_{wp} = L \cdot B$

$$\nabla = L B T \qquad T = \frac{m}{\rho_w L B}$$

Maximum displacement (fully submerged):

$$\Delta_{max} = \rho_w L B D$$

Maximum payload with a required freeboard $f_{min}$:

$$m_{payload,max} = \rho_w L B (D - f_{min}) - m_{structure}$$

### 4.2 Added draft from added load (parallel sinkage)

For wall-sided pontoons the waterplane area stays constant as the draft changes:

$$\Delta T = \frac{\Delta m}{\rho_w \, A_{wp}}$$

**Tonnes per centimetre immersion (TPC):**

$$TPC = \frac{\rho_w A_{wp}}{100} \quad (\rho_w \text{ in t/m}^3,\ A_{wp} \text{ in m}^2)$$

**Tons per inch immersion (US customary):**

$$TPI_{salt} = \frac{A_{wp}(\text{ft}^2)}{420} \text{ long tons/in} \qquad TPI_{fresh} = \frac{A_{wp}(\text{ft}^2)}{432} \text{ long tons/in}$$

(These use 35 ft³ per long ton of sea water and 36 ft³ per long ton of fresh water.)

### 4.3 Vertical cylinder (spar or barrel standing upright)

$$\nabla = \pi R^2 T \qquad T = \frac{m}{\rho_w \pi R^2}$$

Upright cylinders have tiny waterplane areas and therefore poor stability on their own. They are used in groups with wide spacing.

### 4.4 Horizontal cylinder (drum lying on its side, pipe float)

For a horizontal cylinder of radius $R$ and length $\ell$ at draft $d$, define the central angle subtended by the waterline chord:

$$\theta = 2\arccos\!\left(\frac{R-d}{R}\right)$$

Submerged cross-section area (circular segment):

$$A_{seg} = \frac{R^2}{2}\left(\theta - \sin\theta\right)$$

Displaced volume:

$$\nabla = A_{seg}\,\ell$$

Waterline width (needed for stability):

$$c = 2\sqrt{d\,(2R - d)}$$

Centroid of the submerged segment measured down from the cylinder axis:

$$\bar z = \frac{4R\sin^3(\theta/2)}{3(\theta - \sin\theta)}$$

so the center of buoyancy above the bottom is $KB = R - \bar z$.

Key property: at half depth ($d = R$) exactly half the volume is submerged; above that the volume rises slowly near the top. Waterplane width is greatest at $d = R$ and shrinks to zero at full immersion, which is why horizontal cylinders become unstable when pushed near submergence.

Draft has no closed-form solution; it is solved numerically (bisection or Newton iteration). Section 19 includes a solver.

### 4.5 Trapezoidal or sloped-wall pontoons

For a pontoon with bottom width $B_0$ and side slope giving width $B(z) = B_0 + 2z\cot\alpha$:

$$\nabla = L\left(B_0 T + T^2 \cot\alpha\right)$$

Solve the quadratic for $T$:

$$T = \frac{-B_0 + \sqrt{B_0^2 + 4\cot\alpha\,\dfrac{m}{\rho_w L}}}{2\cot\alpha}$$

Flared sides increase waterplane area as the pontoon sinks, which increases stiffness and stability with load.

### 4.6 Multiple floats sharing a load

For $n$ identical floats:

$$\nabla_{each} = \frac{m_{total}}{n\,\rho_w}$$

For unequal floats or uneven load, each float settles independently only if the deck is flexible. A rigid deck forces all floats to a common plane (heave plus heel plus trim) and the loads redistribute according to Section 5.

---

## 5. Hydrostatic Stability

A floating bridge must not roll over under offset loads (traffic in one lane, crowds at a railing, wind on one side, ice on one side).

### 5.1 Key points

| Point | Meaning |
|---|---|
| K | Keel (bottom of pontoon), the reference datum |
| B | Center of buoyancy (centroid of the submerged volume) |
| G | Center of gravity of the whole floating system |
| M | Metacenter (the point B swings around for small heel angles) |

### 5.2 Metacentric height

$$GM = KB + BM - KG$$

$$BM = \frac{I_T}{\nabla}$$

where $I_T$ is the second moment of the waterplane area about the longitudinal centerline.

**Stability criterion:** $GM > 0$ is stable. Practical designs require a healthy margin (often well over 1 m for large pontoons; for small docks 0.3 m or more after the worst crowd case).

### 5.3 Rectangular box formulas

$$KB = \frac{T}{2} \qquad I_T = \frac{L B^3}{12} \qquad BM_T = \frac{B^2}{12\,T}$$

$$GM_T = \frac{T}{2} + \frac{B^2}{12T} - KG$$

Longitudinal:

$$BM_L = \frac{L^2}{12\,T}$$

Because $B$ appears squared, **doubling the width quadruples BM**. Width is the most powerful stability lever.

### 5.4 Separated floats (catamaran and outrigger effect)

When several floats are connected by a rigid frame, use the parallel axis theorem:

$$I_T = \sum_i \left(i_{0,i} + a_i\,y_i^2\right)$$

| Term | Meaning |
|---|---|
| $i_{0,i}$ | Float's own waterplane second moment about its own axis |
| $a_i$ | Float waterplane area |
| $y_i$ | Distance from the float centerline to the system centerline |

The $a_i y_i^2$ term dominates. Moving floats outward is far more effective than making them bigger. This is the main reason pontoon docks put floats at the edges.

### 5.5 Righting moment and heel

Small-angle righting arm:

$$GZ \approx GM \sin\phi$$

Righting moment:

$$M_R = \Delta\,g\,GM\sin\phi$$

Heel from a load $w$ placed off center at distance $e$:

$$\tan\phi = \frac{w\,e}{\Delta\,GM}$$

Here $\Delta$ is total displacement including $w$ while $GM$ is computed with $w$ included in $KG$.

**Heel from a lateral force** (wind) $F$ acting at lever arm $h_F$ above the center of lateral water resistance:

$$\tan\phi = \frac{F\,h_F}{\Delta\,g\,GM}$$

### 5.6 Large angles: the wall-sided formula

For box sections before the deck edge submerges or the bottom emerges:

$$GZ = \sin\phi\left(GM + \frac{BM}{2}\tan^2\phi\right)$$

Angle of deck edge immersion:

$$\tan\phi_{de} = \frac{2f}{B}$$

Angle of bottom emergence:

$$\tan\phi_{be} = \frac{2T}{B}$$

Beyond these angles waterplane area drops and stability can collapse quickly.

### 5.7 Longitudinal trim from a moving load

Moment to change trim one centimetre:

$$MCT_{1cm} = \frac{\Delta\,GM_L}{100\,L}$$

Trim produced by a load $w$ at longitudinal offset $x$:

$$t\,(\text{cm}) = \frac{w\,x}{MCT_{1cm}}$$

For a single short pontoon this governs how a vehicle tilts it as it drives across. For a continuous bridge the structure's bending stiffness takes over (Section 6).

### 5.8 Free surface effect

Water sloshing inside a partially flooded compartment shifts toward the low side and acts as if $G$ were raised:

$$GG' = \frac{\rho_l}{\rho_w}\cdot\frac{i_{fs}}{\nabla}$$

$$GM_{eff} = GM - \sum GG'$$

For a rectangular tank of length $l$ and width $b$:

$$i_{fs} = \frac{l\,b^3}{12}$$

Subdividing a compartment with a longitudinal bulkhead into two halves reduces $i_{fs}$ by a factor of 4 (each half has $b/2$, so $2 \times (b/2)^3 = b^3/4$). This is why pontoons are divided into many small cells.

---

## 6. Structural Mechanics: The Bridge as a Beam on an Elastic Foundation

### 6.1 Water acts like a spring bed

When a long continuous pontoon is pushed down locally by $w(x)$, buoyancy increases by $\rho_w g B\,w(x)$ per unit length. That is exactly a Winkler elastic foundation with modulus:

$$k = \rho_w\,g\,B \quad (\text{N/m per m of length, i.e. N/m}^2)$$

For discrete floats spaced at $s$:

$$k_{equiv} = \frac{\rho_w\,g\,A_{wp,float}}{s}$$

### 6.2 Governing equation

$$EI\,\frac{d^4 w}{dx^4} + k\,w = q(x)$$

| Symbol | Meaning |
|---|---|
| $EI$ | Flexural rigidity of the floating girder |
| $w(x)$ | Vertical deflection |
| $q(x)$ | Applied distributed load |

### 6.3 Characteristic parameter

$$\lambda = \left(\frac{k}{4EI}\right)^{1/4}$$

The characteristic length $1/\lambda$ tells how far a load spreads. Most of the response to a point load fades within about $\pi/\lambda$ to $2\pi/\lambda$ on each side.

### 6.4 Infinite beam under a point load $P$ (Hetényi solution)

Deflection:

$$w(x) = \frac{P\lambda}{2k}\,e^{-\lambda|x|}\left(\cos\lambda|x| + \sin\lambda|x|\right)$$

Bending moment:

$$M(x) = \frac{P}{4\lambda}\,e^{-\lambda|x|}\left(\cos\lambda|x| - \sin\lambda|x|\right)$$

Shear:

$$V(x) = \pm\frac{P}{2}\,e^{-\lambda|x|}\cos\lambda|x|$$

Peak values under the load:

$$w_0 = \frac{P\lambda}{2k} \qquad M_0 = \frac{P}{4\lambda} \qquad V_0 = \frac{P}{2}$$

Interpretation:

* A stiffer girder (larger $EI$) spreads load farther, so less local sinkage but larger moments
* A wider pontoon (larger $k$) reduces sinkage
* Multiple vehicles combine by superposition: add each $w(x - x_i)$ and $M(x - x_i)$

### 6.5 Uniform distributed load

A uniform load $q$ over a long length produces simple parallel sinkage $w = q/k$ with zero bending away from the ends. Bending comes from load **variation**, not total load.

### 6.6 Distributed patch load (traffic jam over length $a$)

Inside the patch, for a point at distances $a_1$ and $a_2$ to the patch ends:

$$w = \frac{q}{2k}\left[2 - e^{-\lambda a_1}\cos\lambda a_1 - e^{-\lambda a_2}\cos\lambda a_2\right]$$

### 6.7 Wave-induced bending

A long floating girder in a regular wave of amplitude $a$ and wavenumber $\kappa = 2\pi/L_w$ is forced by a varying buoyancy. A simplified quasi-static model gives deflection amplitude:

$$\hat w = \frac{k\,a\,\chi}{EI\,\kappa^4 + k}$$

where $\chi \approx e^{-\kappa T}$ accounts for pressure decay with depth (Smith correction). Bending moment amplitude:

$$\hat M = EI\,\kappa^2\,\hat w$$

The moment peaks at the critical wavenumber:

$$\kappa^* = \left(\frac{k}{EI}\right)^{1/4} = \sqrt{2}\,\lambda \qquad L_w^* = \frac{2\pi}{\kappa^*}$$

$$\hat M_{max} = \frac{a}{2}\sqrt{k\,EI}$$

Design lesson: waves with lengths near $L_w^*$ produce the largest bending. Lakes with short fetch generate short waves far below $L_w^*$, which is part of why long rigid concrete floating bridges work on sheltered lakes and struggle in open seas. Full design uses hydrodynamic diffraction and radiation analysis instead of this simplified form.

### 6.8 Hinged versus rigid connections

| Connection | Behavior | Used where |
|---|---|---|
| Rigid (post-tensioned) | Whole bridge acts as one beam; spreads load well; attracts large wave moments | Highway continuous pontoon bridges |
| Hinged (pinned) | No moment transfer; each unit floats more independently; larger local sinkage | Military ribbon bridges, small docks |
| Semi-rigid (rubber fenders, flexible couplers) | Limited moment transfer; reduces fatigue and impact | Marinas, modular cube systems |

For small docks and footbridges, hinged joints between modules prevent wave action from cracking the frames.

---

## 7. Environmental Loads

### 7.1 Load list

| Load | Direction | Notes |
|---|---|---|
| Dead load | Vertical | Structure, ballast, utilities |
| Live load | Vertical, often eccentric | Vehicles, pedestrians, crowds |
| Wind | Lateral, overturning | Drives both direct force and wave generation |
| Waves | Vertical, lateral, torsional | Usually controlling for large floating bridges |
| Current | Lateral | Drag grows with velocity squared |
| Water level change | Vertical | Lake seasonal changes, tides, flood stages |
| Temperature | Axial | Expansion and contraction |
| Ice | Lateral, vertical | Ice sheets push; ice accretion adds weight high up |
| Snow | Vertical | Adds weight and raises G |
| Vessel collision | Lateral, impact | Anchors and pontoon walls must resist |
| Seismic | Indirect | Floating section isolated; transitions, anchors and seiche waves are not |
| Debris / log impact | Lateral | Significant on rivers |

### 7.2 Wind force

$$F_{wind} = \tfrac{1}{2}\,\rho_a\,C_d\,A_{proj}\,V^2$$

| Symbol | Typical value |
|---|---|
| $\rho_a$ | 1.225 kg/m³ at sea level |
| $C_d$ | 1.2 to 2.0 for bluff decks with railings and vehicles |
| $A_{proj}$ | Exposed lateral area above water (deck, railings, vehicles, pontoon freeboard) |

Force per metre of bridge for exposed height $h_e$:

$$f_{wind} = \tfrac{1}{2}\,\rho_a\,C_d\,h_e\,V^2$$

Gust effects are applied with gust factors from the governing code. Wind also causes the bridge to heel (Section 5.5).

### 7.3 Current force

$$F_{current} = \tfrac{1}{2}\,\rho_w\,C_d\,A_{sub}\,U^2$$

Water is about 800 times denser than air, so a 1 m/s current on the submerged face pushes as hard as a wind of roughly 28 m/s on the same area. River crossings with fast current need many anchors or separated pontoons with streamlined bows.

### 7.4 Wave generation from wind (fetch-limited)

A wave climate is estimated from wind speed $U$ (m/s) and fetch $F$ (m). One commonly used deep-water, fetch-limited form:

$$H_s = 0.0016\,\frac{U^2}{g}\left(\frac{gF}{U^2}\right)^{1/2}$$

$$T_p = 0.2857\,\frac{U}{g}\left(\frac{gF}{U^2}\right)^{1/3}$$

| Symbol | Meaning |
|---|---|
| $H_s$ | Significant wave height (mean of highest third) |
| $T_p$ | Peak spectral period |

The design maximum individual wave is often taken near $H_{max} \approx 1.8\,H_s$ for storm durations of a few hours.

### 7.5 Wave basics

Dispersion relation:

$$\omega^2 = g\,\kappa\,\tanh(\kappa h)$$

Deep water ($h > L_w/2$):

$$L_w = \frac{g\,T^2}{2\pi} \approx 1.56\,T^2 \ (\text{m})$$

Wave celerity:

$$c = \frac{L_w}{T} = \frac{gT}{2\pi}$$

Wave energy per unit surface area:

$$E = \tfrac{1}{8}\,\rho_w\,g\,H^2$$

Wave steepness limit (breaking): $H/L_w \approx 1/7$.

### 7.6 Mean wave drift force

Waves reflecting off a long pontoon push it steadily downwave. Per unit length for a regular wave of amplitude $a$ with reflection coefficient $R_c$:

$$f_{drift} = \tfrac{1}{2}\,\rho_w\,g\,a^2\,R_c^2$$

Drift forces are small compared to oscillating forces but act in one direction, so anchors carry them continuously.

### 7.7 Water level change and transitions

Floating sections rise and fall; shore approaches do not. A **transition span** (hinged or with bearings that allow rotation) connects them. The required rotation:

$$\theta_{transition} \approx \frac{\Delta h_{water} + \Delta T_{live}}{L_{transition}}$$

Lakes may vary by a metre or so seasonally. Saltwater sites with several metres of tide need longer transitions or adjustable ramps. Vehicle comfort and joint wear limit the allowable slope change.

### 7.8 Thermal movement

$$\Delta L = \alpha\,L\,\Delta T_{temp}$$

| Material | $\alpha$ (per °C) |
|---|---|
| Concrete | about 10 × 10⁻⁶ to 12 × 10⁻⁶ |
| Steel | about 12 × 10⁻⁶ |
| Aluminum | about 23 × 10⁻⁶ |
| HDPE | about 100 × 10⁻⁶ to 200 × 10⁻⁶ |

A 2,350 m concrete bridge with a 30 °C range moves about $10^{-5} \times 2350 \times 30 \approx 0.7$ m in total. The pontoons in contact with water stay near water temperature, which damps this somewhat; deck structures exposed to sun move more. Expansion joints sit at the transitions.

---

## 8. Dynamics: Heave, Roll and Resonance

### 8.1 Heave (vertical bobbing)

Hydrostatic stiffness:

$$k_{heave} = \rho_w\,g\,A_{wp}$$

Natural period:

$$T_{n,heave} = 2\pi\sqrt{\frac{m + m_a}{\rho_w\,g\,A_{wp}}}$$

Added mass $m_a$ is the water that moves with the pontoon. For a long rectangular section of width $B$, a rough estimate per unit length is in the range of:

$$m_a' \approx C_a\,\rho_w\,\frac{\pi B^2}{8}, \quad C_a \approx 0.7 \text{ to } 1.0$$

For a wall-sided box without added mass:

$$T_{n,heave} \approx 2\pi\sqrt{\frac{T}{g}}$$

### 8.2 Roll

$$T_{n,roll} = \frac{2\pi\,r_{xx}}{\sqrt{g\,GM}}$$

where $r_{xx}$ is the roll radius of gyration including added inertia. A very stiff (large GM) pontoon has a short, snappy roll period that can be uncomfortable or can coincide with short lake waves.

### 8.3 Resonance avoidance

The response amplitude operator (RAO) peaks when wave period approaches a natural period. Design goals:

* Place heave and roll natural periods well away from the dominant site wave periods
* Make pontoon length much greater than design wavelength so wave forces average out along the length
* Add damping (heave plates, skirts, bilge keels) where needed
* Check vehicle-induced vibration and pedestrian-induced sway for light footbridges (pedestrian lateral sway frequency near 1 Hz)

**Length averaging:** a pontoon of length $L$ in waves of length $L_w$ along its axis feels a net heave force reduced roughly by the factor:

$$\left|\frac{\sin(\pi L/L_w)}{\pi L/L_w}\right|$$

When $L \gg L_w$ this factor is small. Long pontoons ride over short waves.

---

## 9. Mooring and Anchorage

### 9.1 Anchor types

| Type | How it holds | Typical use |
|---|---|---|
| Gravity anchor (concrete block) | Submerged weight times friction | Hard bottoms, small docks, many highway anchors |
| Fluke / plate anchor | Embeds and resists by soil bearing | Soft mud |
| Driven or drilled pile | Lateral soil resistance | Shallow water near shore |
| Box or fluke anchors jetted into soft lakebed | Large embedment in deep soft sediment | Lake Washington bridges |
| End anchorage only | Structure curved in plan acts as a horizontal arch | Norwegian fjord bridges where depth makes side anchors impractical |
| Guide piles with collars | Allow vertical travel, prevent horizontal drift | Docks, small footbridges with water level change |

### 9.2 Gravity anchor holding

Submerged weight:

$$W_{sub} = V_{anchor}\,(\rho_{anchor} - \rho_w)\,g$$

For concrete at 2,400 kg/m³ in fresh water, submerged weight is about 58 percent of weight in air.

Sliding resistance:

$$H_{hold} = \mu\,(W_{sub} - F_{V,up})$$

where $\mu$ is the friction coefficient (roughly 0.3 to 0.7 depending on bottom and anchor shape) and $F_{V,up}$ is the uplift component of line tension.

### 9.3 Catenary mooring line

A chain or cable hanging under its own submerged weight per length $w$ with horizontal tension $H$ forms a catenary. With origin at the touchdown point:

$$y(x) = \frac{H}{w}\left[\cosh\!\left(\frac{w\,x}{H}\right) - 1\right]$$

Suspended length to reach depth $h$:

$$s = \sqrt{h\left(h + \frac{2H}{w}\right)}$$

Horizontal distance covered by the suspended part:

$$x = \frac{H}{w}\,\sinh^{-1}\!\left(\frac{s\,w}{H}\right)$$

Tension at the top (fairlead):

$$T_{top} = H + w\,h$$

Vertical component at the top:

$$V_{top} = w\,s$$

As the bridge drifts, $H$ rises and the chain lifts off the bottom; the lifting chain provides restoring stiffness. Taut cables (pretensioned steel strand, as on large highway bridges) are stiffer and mainly use elastic stretch:

$$k_{cable} = \frac{E_c\,A_c}{L_c}\cos^2\beta$$

where $\beta$ is the cable angle from horizontal.

### 9.4 Anchor layout

* Anchors on both sides resist wind and waves from either direction
* Spacing commonly matches pontoon joints
* Cables are pretensioned to limit lateral drift and are adjustable
* Redundancy: losing one cable must not cause progressive failure
* Lateral stiffness of all anchors combined determines how far the bridge sways under wind

### 9.5 End-anchored curved bridges

A floating bridge curved in plan with radius $R_p$ carrying lateral distributed load $p$ develops axial compression like an arch:

$$N = p\,R_p$$

This allows long spans of open water with no side anchors at all. It requires very stiff ends and buckling checks of the floating arch.

---

## 10. Watertightness, Flooding and Damage Stability

### 10.1 Compartmentalization

Highway pontoons are divided into many watertight cells by internal walls. Design checks assume one or more cells flood (damage, leak, collision) and verify the bridge still floats with adequate freeboard and stability.

### 10.2 Lost-buoyancy method (parallel sinkage after flooding)

If a compartment of waterplane area $a$ floods to the outside waterline with permeability $\mu_p$ (fraction of compartment volume open to water, 1.0 for an empty cell):

$$\delta T = \frac{\mu_p\,a\,T}{A_{wp} - \mu_p\,a}$$

The flooded cell no longer contributes waterplane, so stability also drops:

$$I_{T,damaged} = I_T - \left(i_0 + a\,y^2\right)_{flooded}$$

Off-center flooding also causes heel and possibly trim. Each case is checked separately.

### 10.3 Leak rate through a hole

Orifice flow:

$$Q = C_d\,A_{hole}\,\sqrt{2\,g\,h_{head}}$$

with $C_d \approx 0.6$ for a sharp-edged hole. Leaks grow as the cell fills only until the inside level equals the outside level.

### 10.4 Defenses against flooding

* Many small cells
* Watertight hatches that are kept closed and alarmed
* Water-level sensors in every cell feeding a monitoring system
* Permanent or portable bilge pumps sized for credible leak rates
* Low-permeability concrete with adequate cover and controlled crack width
* Post-tensioning to keep concrete in compression and cracks closed
* Regular inspection of every cell

---

## 11. Materials

| Material | Density (kg/m³) | Strengths | Weaknesses | Typical use |
|---|---|---|---|---|
| Reinforced / post-tensioned concrete | 2,400 to 2,500 | Durable in water, low maintenance, heavy (stable), cheap per volume, fire proof | Heavy, needs casting basin, cracks leak if not controlled | Highway pontoons |
| Structural steel | 7,850 | Strong, light structure, fast fabrication | Corrosion; needs coatings and cathodic protection; fatigue at welds | Norwegian girders, older pontoons, military |
| Aluminum alloys (marine grade) | 2,700 | Light, corrosion resistant, transportable | Expensive, fatigue sensitive, lower stiffness | Military ribbon bridges, gangways |
| HDPE plastic (drums, cubes, pipe) | 940 to 960 | Floats on its own, rot proof, cheap, impact tolerant | Low stiffness, UV degradation without stabilizer, creep, thermal movement | Docks, modular floats, temporary bridges |
| Expanded polystyrene (EPS) foam | 15 to 30 | Huge buoyancy per kg, cannot leak | Absorbs water over time if unprotected, damaged by fuel, animals burrow | Encapsulated dock floats only |
| Closed-cell polyurethane foam | 30 to 60 | Fills irregular shells, adds puncture redundancy | Cost, must be marine rated | Filling hulls and drums |
| Timber (treated) | 450 to 750 | Workable, cheap, floats | Rot, borers, fasteners corrode | Decking, small frames |
| Fiber reinforced polymer (FRP) | 1,500 to 2,000 | Light, corrosion proof | Cost, joints and fire | Decks, gratings, modern pedestrian bridges |

**Concrete pontoon specifics:**
* High-performance, low-permeability mixes with supplementary cementitious materials
* Post-tensioning in both directions to keep walls and slabs in compression
* Limits on crack width (tight) because cracks are leak paths
* Epoxy-coated or stainless reinforcement in the splash zone
* Shear keys and post-tensioned or bolted joints between pontoons

---

## 12. Engineering Design Process (Highway Scale)

### 12.1 Step sequence

1. **Site investigation:** bathymetry, soil cores for anchors, wind records, fetch geometry, water level history, currents, ice, navigation traffic, environmental constraints
2. **Design criteria:** return periods for wind and waves (often 100 year storms with checks at longer events), traffic loading per governing code, service life (75 to 100 years), owner's manuals (WSDOT and the Norwegian Public Roads Administration publish floating bridge criteria)
3. **Concept selection:** continuous versus separated pontoons, anchored versus end-anchored, navigation opening type
4. **Hydrostatic sizing:** pontoon width, depth, length; draft and freeboard under dead, live and damaged conditions
5. **Stability:** intact and damaged GM; heel under eccentric traffic and wind
6. **Global structural analysis:** beam on elastic foundation for traffic, then hydrodynamic analysis (frequency domain diffraction and radiation, then time domain for storms) for wave bending, torsion and shear
7. **Mooring design:** anchor capacity, cable sizing, pretension, redundancy (one cable broken)
8. **Local structural design:** walls, slabs, hatches, cell joints, connections, transitions
9. **Fatigue:** millions of wave cycles over the design life; connections and steel details govern
10. **Navigation openings:** draw span, lift span, elevated high-rise section or a deep gap
11. **Transitions and approaches:** hinges, bearings, expansion joints
12. **Monitoring systems:** leak detection, cable tension, motion sensors, wind instruments
13. **Construction engineering:** casting basin design, launch and float-out, tow route and draft limits, joining sequence, anchor installation
14. **Operations and maintenance plan:** inspection schedules, storm closure thresholds, draw span procedures

### 12.2 Navigation opening options

| Option | Description |
|---|---|
| Retractable draw span | Pontoon sections slide inside adjacent pontoons to open a channel (Hood Canal, historic I-90) |
| Lift span | Vertical lift on towers at one end or segment (Okanagan Lake) |
| Elevated section | Bridge climbs on an approach to a high-level fixed span for ships (Nordhordland) |
| Gap span at shore | Fixed high span between the floating section and land |

---

## 13. Construction Methods

### 13.1 Casting basins

Large concrete pontoons are cast in a dry basin (a graving dock) next to the water. When a batch is complete the basin is flooded, the gate opened and the pontoons floated out. SR 520 pontoons were cast in basins in Aberdeen and Tacoma, Washington.

### 13.2 Float-out and tow

* Check draft against channel depth, lock sill depth and tow route
* Seal all openings; verify freeboard and stability for the tow
* Tugs move pontoons like barges; SR 520 pontoons were towed roughly 260 nautical miles from Grays Harbor and passed through the Ballard Locks into Lake Washington
* Fresh water arrival increases draft (Section 3.5)

### 13.3 Anchor installation

Anchors and cables go in first so each arriving pontoon can be held immediately. Anchor types are chosen to suit the lakebed soil (gravity, fluke or jetted box anchors).

### 13.4 Joining pontoons

* Pontoons are aligned using winches and anchor cables
* Joint faces are matched with shear keys
* Connections are made with large bolts or post-tensioned tendons; the SR 520 joining used 80 bolts per joint, each 16 to 20 ft long
* Joint seals are installed and tested for watertightness

### 13.5 Superstructure

Columns, girders and deck are built on top of the pontoons. Every added tonne changes draft, trim and heel, so ballast is adjusted during construction to keep the floating structure level.

### 13.6 Repairs

Repairs below the waterline use floating cofferdams. On SR 520 a 600 ton steel floating cofferdam, ballasted with water, was positioned under a pontoon to create a dry work area.

---

## 14. Building a Small Floating Footbridge or Dock

### 14.1 Float options

| Float | Buoyancy | Notes |
|---|---|---|
| Encapsulated foam dock float | Rated by manufacturer per float | Best choice; rot and puncture resistant; rated loads given |
| HDPE 55 gal (208 L) drum | Gross about 230 kg per drum (outer volume about 0.23 m³) minus about 10 kg drum mass | Use only clean, sealed, preferably food-grade drums; secure bungs; do not use drums that held toxic contents |
| Modular plastic cubes | Typically about 0.5 m cube units | Bolt together into any shape; built-in hinge effect |
| Sealed PVC or HDPE pipe | Calculate with Section 4.4 | Cheap for narrow walkways; ends must be welded or sealed |
| Plastic or aluminum pontoon tubes | Rated per tube | Boat-pontoon style; good for longer spans |

### 14.2 Design rules of thumb

* Size floats so the **full live load draft stays at or below 50 to 60 percent of float depth** (keeps reserve buoyancy and waterplane width)
* Put floats at the **outer edges** of the frame, not the center
* Minimum walkway width about 1.2 m for single file, 1.8 to 2.4 m for comfortable two-way traffic and stability
* Check GM with the worst crowd case and a person standing at the railing
* Hinge modules together so waves bend the joints, not the frames
* Plan for water level change: hinged shore ramp plus guide posts or slack anchor chains
* Use stainless or hot-dip galvanized fasteners
* Include rails, non-slip decking, a posted load limit and life rings

### 14.3 Step-by-step build

1. **Measure the site:** crossing length, depth, bottom type, water level range, wave and boat wake exposure, current speed
2. **Decide module size:** typical module 2.4 m × 2.4 m (8 ft × 8 ft) or 3.0 m × 1.8 m; length set by handling weight
3. **Compute loads:** frame and decking mass; live load (common dock design values are around 2.4 to 4.8 kPa, i.e. 50 to 100 psf; the governing local code controls)
4. **Size floats** with $\nabla = m/\rho_w$ at 50 to 60 percent submersion
5. **Check stability** with Section 5.4 using the real float positions
6. **Build frames:** pressure-treated lumber rated for ground contact or marine aluminum; diagonal bracing or plywood shear panels to keep frames square
7. **Attach floats:** through-bolted straps, cradles or manufacturer brackets; floats must not slide or roll out
8. **Deck:** composite, treated lumber or aluminum grating with gaps for drainage
9. **Launch modules one at a time** and measure actual draft and freeboard against calculations
10. **Connect modules** with hinges, chain links or rubber couplers
11. **Anchor:** guide posts with sliding collars, or chains to concrete blocks in a crossed (X) pattern with enough slack for the full water level range plus 25 percent
12. **Shore connection:** hinged ramp with a roller or slide at the float end
13. **Load test:** gradually load with known weights (water containers, sandbags) to the design load; check draft, heel at the edge and joint behavior
14. **Post the load limit** and inspect after storms and every season

### 14.4 Permits

Structures in lakes, rivers and coastal waters usually require permits. In the United States, work in navigable waters involves the US Army Corps of Engineers plus state and local shoreline or fish and wildlife agencies. Private ponds still may fall under local building rules.

### 14.5 DIY example summary

Section 18.3 shows a complete drum-float calculation. The key result: a narrow 1.2 m module with four drums **capsizes** with one 100 kg person at the edge and is unstable with 200 kg standing on it, even though buoyancy is more than adequate. The same four drums spread across a 2.4 m frame remain stable with about 400 kg aboard. Width governs small floating bridges far more than float count.

---

## 15. Military and Emergency Floating Bridges

### 15.1 Systems

| System family | Description |
|---|---|
| Ribbon bridges (Soviet PMP and Western derivatives such as the Improved Ribbon Bridge) | Folded aluminum bays launched from trucks that unfold on hitting the water; boats push them into line; crews pin them together. Bays can be used singly as rafts or joined into a continuous bridge |
| Pneumatic float bridges | Inflatable floats carrying steel or aluminum treadways |
| Bailey and modular panel bridges on pontoons | Panel girders carried on boat-shaped pontoons |
| Amphibious rigs | Self-propelled vehicles that drive into the water and link into a bridge or ferry |

### 15.2 Military Load Class (MLC)

Vehicles and bridges are rated by MLC numbers that combine weight, axle loads and track geometry. A bridge's MLC rating drops as current speed rises, because drag and bow-down trim reduce freeboard. Tables published for each bridge relate allowable class to current speed.

### 15.3 Military engineering checks

* Current speed (bridge rating falls and anchoring needs rise)
* Bank conditions for launch and ramps
* Bridge length versus available bays
* Anchorage: boats holding position, kedge anchors or overhead cable systems
* Vehicle spacing to keep loads separate on the elastic foundation
* Speed limits to reduce bow waves and dynamic loads

### 15.4 Difficulty

With trained crews and the correct equipment, ribbon bridges are among the fastest wide-gap crossings possible. Without equipment, improvising a vehicle-rated floating bridge is extremely difficult because vehicle point loads demand both large buoyancy and a stiff deck to spread the load.

---

## 16. Difficulty Assessment

### 16.1 Scale comparison

| Project | Difficulty (1 to 10) | Engineering level | Typical team | Time | Rough cost scale |
|---|---|---|---|---|---|
| Single drum or foam raft for a pond | 1 | Basic arithmetic | 1 to 2 people | 1 day | Under US$500 |
| Floating dock (one or two modules) | 2 to 3 | Buoyancy and stability checks | 2 people | Weekend to a week | US$1,000 to US$10,000 |
| Floating footbridge across a pond or slow creek, 20 to 50 m | 4 | Stability, anchoring, water level design, permits | Small crew | Weeks | US$10,000 to US$100,000+ |
| Commercial marina or event floating walkway | 5 to 6 | Professional engineer, code loads, wave and wake analysis | Contractor | Months | Hundreds of thousands to millions |
| Military ribbon bridge deployment | 5 (with equipment and training) | Doctrine and drills | Trained bridge company | Hours | Equipment already owned |
| Light vehicle floating bridge, improvised | 7 | Elastic foundation behavior, point loads, connection design | Engineers plus labor | Weeks | High relative to output |
| Highway floating bridge on a sheltered lake | 9 | Hydrodynamics, prestressed concrete, mooring, marine construction | Large agency plus contractors | Decade including planning | Billions (SR 520 program reported about US$4.6 billion) |
| Open-sea or fjord floating bridge / floating tunnel | 10 | Frontier engineering | National programs | Decades | Billions |

### 16.2 What makes floating bridges hard

1. **Everything moves:** the structure has six degrees of freedom (heave, sway, surge, roll, pitch, yaw) and responds dynamically
2. **Waves dominate:** long-life designs must survive rare storms with wave periods and fetch effects specific to the site
3. **Water gets in:** any crack, hatch or joint can leak; flooding is progressive and silent without monitoring
4. **Transitions:** joining a moving structure to a fixed shore requires hinges, joints and approach spans that survive millions of cycles
5. **Anchoring in deep soft soil:** anchors must hold in mud at great depth and be installed from barges
6. **Navigation:** boats must pass, which requires moving spans or elevated sections
7. **Construction logistics:** casting basins, tows, locks and draft limits
8. **Fatigue:** wave loading runs continuously for the entire life of the bridge
9. **Corrosion and durability:** permanent water contact
10. **Public consequence:** a failure closes a key route and costs years to replace

### 16.3 What makes them easier than they look

* Buoyancy math is simple and exact
* Uniform dead load produces no bending at all (Section 6.5)
* No deep foundations are needed
* Seismic isolation is built in for the floating part
* Small-scale versions are within reach of anyone who can compute volume and do a stability check

---

## 17. Failure Modes and Case Studies

### 17.1 Failure modes

| Mode | Cause | Defense |
|---|---|---|
| Progressive flooding | Leaks, open hatches, collision | Many cells, closed hatches, sensors, pumps |
| Capsize | Insufficient GM, offset load, wind, ice buildup | Width, low KG, outer floats, load limits |
| Breakup from wave bending | Storm waves near critical wavelength | Hydrodynamic design, strong joints, storm closures |
| Mooring failure | Anchor drag, cable break, corrosion | Redundancy, pretension monitoring, inspection |
| Connection fatigue | Repeated wave and traffic cycles | Detailing, post-tensioning, inspection |
| Overload | Crowds, vehicles over rating | Posted limits, enforcement |
| Ice damage | Lateral ice pressure, ice weight | Ice breakers, design ice loads, seasonal removal for small docks |
| Vessel impact | Collision | Fendering, navigation aids, collision design |
| Transition failure | Water level extremes beyond joint range | Range design with margin |

### 17.2 Hood Canal Bridge, 1979

During a severe February 1979 windstorm with very high gusts, the western portion of the bridge broke apart and sank. Contributing factors identified afterward included wave and wind loads exceeding the design assumptions of the era and flooding of pontoons (accounts include open hatches and pontoon damage letting water in). The bridge was rebuilt and reopened in the early 1980s. Lessons: stronger storm criteria, watertight integrity, storm procedures (opening the draw span to relieve loads) and better anchor design.

### 17.3 Lacey V. Murrow Bridge, 1990

During renovation in November 1990, water from hydrodemolition work was being stored inside the pontoons and watertight hatches had been removed. A storm brought rain and waves; water accumulated in the pontoons until they sank in sequence over several hours. The sinking bridge damaged anchor cables of the adjacent Hadley bridge. Lessons: never compromise compartment integrity during construction, monitor water in cells and treat temporary conditions with the same rigor as final conditions.

### 17.4 Ancient lesson: Xerxes' first bridge

Herodotus records that a storm destroyed the first Hellespont crossing. The rebuilt version used heavier cables and anchors at both ends with ships oriented to the current. Anchoring and storm design have been the deciding factors for 2,500 years.

---

## 18. Worked Examples (Full Calculations)

All results below were computed and checked numerically. SI units unless stated.

### 18.1 Large concrete pontoon (SR 520 scale, illustrative)

Pontoon only, without superstructure. Given:

* $L = 360$ ft $= 109.7$ m
* $B = 75$ ft $= 22.86$ m
* $D = 29$ ft $= 8.84$ m
* Mass $= 11{,}000$ short tons $= 9.98 \times 10^6$ kg

**Waterplane area:**

$$A_{wp} = 109.7 \times 22.86 = 2508 \text{ m}^2$$

**Draft in fresh water:**

$$T = \frac{9.98\times10^6}{1000 \times 2508} = 3.98 \text{ m (13.1 ft)}$$

**Draft in sea water (during tow):**

$$T_{sea} = \frac{9.98\times10^6}{1025 \times 2508} = 3.88 \text{ m}$$

Arrival in fresh water adds about 0.10 m of draft.

**Freeboard (pontoon alone):**

$$f = 8.84 - 3.98 = 4.86 \text{ m}$$

The superstructure added later consumes part of this freeboard; actual in-service draft is larger.

**TPC:**

$$TPC = \frac{1.0 \times 2508}{100} = 25.1 \text{ t/cm}$$

A loaded 36 t truck sinks a free pontoon about 1.4 cm in parallel sinkage (ignoring bending spread).

**Stability (assumed KG = 3.8 m):**

$$KB = 1.99 \text{ m} \quad BM = \frac{22.86^2}{12 \times 3.98} = 10.95 \text{ m}$$

$$GM = 1.99 + 10.95 - 3.80 = 9.13 \text{ m}$$

Very large GM: a 75 ft wide box at 13 ft draft is extremely stable.

### 18.2 Truck on a continuous floating girder (beam on elastic foundation)

Given:

* Pontoon width $B = 22.86$ m, fresh water
* Assumed $E = 30$ GPa, $I = 273$ m⁴ (illustrative hollow concrete section)
* Truck $P = 80{,}000$ lb $= 356$ kN

**Foundation modulus:**

$$k = 1000 \times 9.81 \times 22.86 = 224{,}300 \text{ N/m}^2$$

**Characteristic parameter:**

$$\lambda = \left(\frac{224{,}300}{4 \times 30\times10^9 \times 273}\right)^{1/4} = 0.00910 \text{ m}^{-1}$$

$$1/\lambda = 110 \text{ m}$$

**Peak deflection:**

$$w_0 = \frac{356{,}000 \times 0.00910}{2 \times 224{,}300} = 0.0072 \text{ m} = 7.2 \text{ mm}$$

**Peak moment:**

$$M_0 = \frac{356{,}000}{4 \times 0.00910} = 9.78 \text{ MN·m}$$

The truck's weight spreads along about $\pi/\lambda \approx 345$ m of bridge in each direction. Compare with 1.4 cm of parallel sinkage on a single free pontoon: the rigid girder spreads the load and halves the local sinkage.

### 18.3 DIY drum-float module (stability governs)

Given:

* HDPE drums: diameter 0.58 m, length 0.88 m, outer volume 0.2325 m³ each, mass 10 kg each
* Four drums lying horizontally, axes along the walkway, two per side
* Person: 100 kg, center of gravity 1.0 m above deck
* Deck at 0.65 m above drum bottoms

**Configuration A: narrow module, 1.2 m wide, drum centerlines at ±0.35 m, frame 90 kg**

| Payload | Draft | Fill | KB | BM | KG | GM | Result |
|---|---|---|---|---|---|---|---|
| 100 kg | 0.172 m | 25% | 0.101 | 1.182 | 1.022 | +0.260 | Stable but a 100 kg person at the edge (0.6 m) gives a computed 45° heel: deck edge submerges and the module flips |
| 200 kg | 0.223 m | 35% | 0.130 | 0.897 | 1.212 | −0.185 | **Unstable** |
| 286 kg | 0.266 m | 45% | 0.154 | 0.735 | 1.303 | −0.414 | **Unstable** |

**Configuration B: wide module, 2.4 m wide, drum centerlines at ±0.95 m, frame 150 kg**

| Payload | Draft | Fill | KB | BM | KG | GM | Heel with 100 kg at edge (1.2 m) |
|---|---|---|---|---|---|---|---|
| 100 kg | 0.203 m | 31% | 0.119 | 6.23 | 0.945 | 5.41 | 4.4° |
| 200 kg | 0.253 m | 42% | 0.147 | 4.83 | 1.126 | 3.85 | 4.6° |
| 286 kg | 0.295 m | 51% | 0.170 | 3.99 | 1.221 | 2.94 | 4.9° |
| 400 kg | 0.352 m | 63% | 0.200 | 3.14 | 1.304 | 2.04 | 5.7° |

**Buoyancy capacity check (Configuration B):**

* Gross buoyancy at full submergence: $4 \times 232.5 = 930$ kg
* Fixed mass: $40 + 150 = 190$ kg
* Theoretical payload at zero reserve: 740 kg
* Payload at the recommended 50 to 60 percent fill: roughly 275 to 370 kg

**Conclusion:** the same four drums go from capsizing to comfortable simply by moving them from ±0.35 m to ±0.95 m. BM rose from about 1 m to about 4 to 6 m because of the $a\,y^2$ term.

### 18.4 Wave climate on a lake

Given: storm wind $U = 25$ m/s (56 mph), fetch $F = 10$ km.

$$\frac{gF}{U^2} = \frac{9.81 \times 10{,}000}{625} = 157$$

$$H_s = 0.0016 \times \frac{625}{9.81} \times 157^{0.5} = 1.28 \text{ m}$$

$$T_p = 0.2857 \times \frac{25}{9.81} \times 157^{1/3} = 3.93 \text{ s}$$

$$L_w = 1.56 \times 3.93^2 = 24.1 \text{ m}$$

A 110 m long pontoon spans more than four of these wavelengths, so heave forces largely cancel along its length.

**Critical bending wavelength** for the girder in 18.2:

$$L_w^* = \frac{\sqrt{2}\,\pi}{\lambda} = 488 \text{ m}$$

Lake storm waves of 24 m are far shorter than the 488 m critical length, which keeps wave bending moderate. Open-ocean swell with long periods approaches the critical range, which is one reason highway floating bridges are built on sheltered water.

### 18.5 Heave natural period

Using added mass about 0.9 × $\rho_w \pi B^2/8$ per metre:

$$m_a = 0.9 \times 1000 \times \frac{\pi \times 22.86^2}{8} \times 109.7 = 2.03 \times 10^7 \text{ kg}$$

$$T_{n} = 2\pi\sqrt{\frac{9.98\times10^6 + 2.03\times10^7}{1000 \times 9.81 \times 2508}} = 6.97 \text{ s}$$

The 7.0 s natural period sits well above the 3.9 s storm wave period, so heave resonance is avoided.

### 18.6 Wind on the deck

Gust $V = 40$ m/s, $C_d = 1.3$, exposed height including vehicles $h_e = 6$ m:

$$f_{wind} = 0.5 \times 1.225 \times 1.3 \times 6 \times 40^2 = 7{,}640 \text{ N/m}$$

Over one 110 m pontoon: about 840 kN of lateral load, which the anchors on that pontoon must resist together with wave and drift forces.

### 18.7 Mean wave drift force

$a = H_s/2 = 0.64$ m, reflection coefficient $R_c = 0.8$:

$$f_{drift} = 0.5 \times 1000 \times 9.81 \times 0.64^2 \times 0.8^2 = 1{,}280 \text{ N/m}$$

### 18.8 Mooring catenary

Chain submerged weight $w = 1.0$ kN/m, depth $h = 60$ m, design horizontal tension $H = 500$ kN:

$$s = \sqrt{60\left(60 + \frac{2\times500}{1.0}\right)} = 252.2 \text{ m}$$

$$x = \frac{500}{1.0}\,\sinh^{-1}\!\left(\frac{252.2 \times 1.0}{500}\right) = 242.6 \text{ m}$$

$$T_{top} = 500 + 1.0 \times 60 = 560 \text{ kN}$$

Horizontal stiffness at this tension (numerical derivative, including lifting chain): about 108 kN/m. At this stiffness the 840 kN wind load of 18.6 would need many lines sharing the load or taut pretensioned cables to keep drift small.

### 18.9 Gravity anchor size

Required horizontal hold 600 kN, friction $\mu = 0.5$, uplift from the line ignored for a long catenary with chain lying on the bottom:

$$W_{sub} = \frac{600}{0.5} = 1{,}200 \text{ kN}$$

Submerged concrete weighs $(2400 - 1000) \times 9.81 = 13.7$ kN/m³:

$$V = \frac{1200}{13.7} = 87.4 \text{ m}^3 \quad (\approx 210 \text{ t in air})$$

### 18.10 Leak and flooding

A 50 mm diameter hole 3 m below the waterline:

$$Q = 0.6 \times \frac{\pi \times 0.05^2}{4} \times \sqrt{2 \times 9.81 \times 3} = 0.00904 \text{ m}^3/\text{s}$$

That is about 32.5 m³ per hour or 780 m³ per day. A modest pump handles it if detected; undetected for a week it floods a large cell.

A flooded cell with waterplane area 400 m² in the pontoon of 18.1:

$$\delta T = \frac{400 \times 3.98}{2508 - 400} = 0.76 \text{ m}$$

### 18.11 Free surface correction

A 20 m × 20 m cell with a loose water surface in the pontoon of 18.1:

$$i_{fs} = \frac{20 \times 20^3}{12} = 13{,}333 \text{ m}^4 \qquad GG' = \frac{13{,}333}{9{,}979} = 1.34 \text{ m}$$

GM drops from 9.13 m to 7.79 m. Splitting the cell with one longitudinal bulkhead reduces the loss to 0.33 m.

---

## 19. Python Calculator

Standard library only. Output from the test run is shown after the code.

```python
"""Floating bridge quick calculator. SI units. Standard library only."""
import math

G = 9.81          # m/s^2
RHO_FW = 1000.0   # fresh water, kg/m^3
RHO_SW = 1025.0   # sea water, kg/m^3


def bisect(f, lo, hi, tol=1e-9, it=200):
    flo = f(lo)
    for _ in range(it):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if abs(fm) < tol or (hi - lo) < tol:
            return mid
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)


# ---------- Hydrostatics ----------
def box_draft(mass_kg, L, B, rho=RHO_FW):
    """Draft of a rectangular box pontoon."""
    return mass_kg / (rho * L * B)


def hcyl_segment_area(d, R):
    """Submerged cross-section area of a horizontal cylinder at draft d."""
    d = min(max(d, 0.0), 2 * R)
    th = 2 * math.acos((R - d) / R)
    return 0.5 * R * R * (th - math.sin(th))


def hcyl_draft(mass_kg, R, length, n=1, rho=RHO_FW):
    """Draft of n identical horizontal cylinders sharing a load."""
    cap = n * math.pi * R * R * length * rho
    if mass_kg >= cap:
        raise ValueError("Load exceeds total buoyancy: sinks")
    return bisect(lambda d: n * hcyl_segment_area(d, R) * length * rho - mass_kg,
                  1e-9, 2 * R - 1e-9)


def box_GM(B, T, KG):
    """Transverse metacentric height of a box: KB + BM - KG."""
    return T / 2 + B * B / (12 * T) - KG


def heel_deg(load_kg, offset_m, displacement_kg, GM):
    """Small-angle heel from an off-center load."""
    return math.degrees(math.atan(load_kg * offset_m / (displacement_kg * GM)))


def flood_sinkage(T, A_wp, a_flooded, permeability=1.0):
    """Lost-buoyancy method: parallel sinkage when one compartment floods."""
    a = permeability * a_flooded
    return a * T / (A_wp - a)


# ---------- Beam on elastic foundation ----------
def boef(P, B, E, I, rho=RHO_FW):
    """Infinite floating beam under point load P (N)."""
    k = rho * G * B
    lam = (k / (4 * E * I)) ** 0.25
    return {"k": k, "lambda": lam, "char_len": 1 / lam,
            "w0": P * lam / (2 * k), "M0": P / (4 * lam), "V0": P / 2}


def boef_deflection(x, P, k, lam):
    x = abs(x)
    return P * lam / (2 * k) * math.exp(-lam * x) * (math.cos(lam * x) + math.sin(lam * x))


# ---------- Waves ----------
def fetch_limited(U, F):
    """Deep-water fetch-limited growth. U wind m/s, F fetch m."""
    X = G * F / U ** 2
    Hs = 0.0016 * U ** 2 / G * X ** 0.5
    Tp = 0.2857 * U / G * X ** (1 / 3)
    return Hs, Tp


def wavelength(T, h=None):
    """Solve w^2 = g k tanh(k h). h None means deep water."""
    w = 2 * math.pi / T
    if h is None:
        return G * T * T / (2 * math.pi)
    k = bisect(lambda k: w * w - G * k * math.tanh(k * h), 1e-6, 50.0)
    return 2 * math.pi / k


# ---------- Mooring ----------
def catenary(H, w, h):
    """Simple catenary, touchdown at anchor. H horizontal tension N, w submerged weight N/m, h depth m."""
    s = math.sqrt(h * (h + 2 * H / w))
    x = (H / w) * math.asinh(s * w / H)
    T_top = H + w * h
    return {"suspended_len": s, "horiz_dist": x, "T_top": T_top}


def catenary_stiffness(H, w, h, dH=1.0):
    """Horizontal stiffness dH/dx including the change in lying chain."""
    def x_total(Hx, Ltot):
        c = catenary(Hx, w, h)
        return c["horiz_dist"] + (Ltot - c["suspended_len"])
    Ltot = catenary(H, w, h)["suspended_len"] + 50.0
    return dH / (x_total(H + dH, Ltot) - x_total(H, Ltot))


# ---------- Leaks ----------
def leak_rate(d_hole, head, Cd=0.6):
    """Inflow through a hole of diameter d_hole under head (m). Returns m^3/s."""
    A = math.pi * d_hole ** 2 / 4
    return Cd * A * math.sqrt(2 * G * head)


if __name__ == "__main__":
    m = 9.979e6; L = 109.7; B = 22.86
    T = box_draft(m, L, B)
    print(f"Draft fresh: {T:.2f} m   sea: {box_draft(m, L, B, RHO_SW):.2f} m")
    print(f"GM (KG 3.8 m): {box_GM(B, T, 3.8):.2f} m")
    r = boef(356e3, B, 30e9, 273.0)
    print(f"1/lambda {r['char_len']:.0f} m  w0 {r['w0']*1000:.1f} mm  M0 {r['M0']/1e6:.2f} MN*m")
    Hs, Tp = fetch_limited(25, 10_000)
    print(f"Hs {Hs:.2f} m  Tp {Tp:.2f} s  L {wavelength(Tp):.1f} m")
    c = catenary(500e3, 1000.0, 60.0)
    print({k: round(v, 1) for k, v in c.items()})
    print(f"Mooring stiffness ~ {catenary_stiffness(500e3, 1000.0, 60.0)/1e3:.1f} kN/m")
    print(f"Leak 50 mm hole at 3 m head: {leak_rate(0.05, 3.0)*3600:.1f} m^3/h")
    print(f"Flood sinkage: {flood_sinkage(T, L*B, 400):.2f} m")
    d = hcyl_draft(476, 0.29, 0.88, n=4)
    print(f"Drum float draft: {d:.3f} m of 0.58 m")
```

Test output:

```
Draft fresh: 3.98 m   sea: 3.88 m
GM (KG 3.8 m): 9.13 m
1/lambda 110 m  w0 7.2 mm  M0 9.78 MN*m
Hs 1.28 m  Tp 3.93 s  L 24.1 m
{'suspended_len': 252.2, 'horiz_dist': 242.6, 'T_top': 560000.0}
Mooring stiffness ~ 107.6 kN/m
Leak 50 mm hole at 3 m head: 32.5 m^3/h
Flood sinkage: 0.76 m
Drum float draft: 0.295 m of 0.58 m
```

---

## 20. Reference Tables

### 20.1 Unit conversions

| From | To | Multiply by |
|---|---|---|
| ft | m | 0.3048 |
| ft² | m² | 0.0929 |
| ft³ | m³ | 0.02832 |
| US gal | L | 3.785 |
| lb | kg | 0.4536 |
| short ton (2,000 lb) | tonne | 0.9072 |
| long ton (2,240 lb) | tonne | 1.016 |
| psf | kPa | 0.04788 |
| mph | m/s | 0.4470 |
| knot | m/s | 0.5144 |
| kip | kN | 4.448 |

### 20.2 Buoyancy per unit volume

| Water | Buoyancy per m³ | Buoyancy per ft³ | Buoyancy per US gal |
|---|---|---|---|
| Fresh | 1,000 kg | 62.4 lb | 8.34 lb |
| Sea | 1,025 kg | 64.0 lb | 8.55 lb |

### 20.3 Typical drag coefficients

| Shape | $C_d$ |
|---|---|
| Flat plate normal to flow | 2.0 |
| Rectangular box, sharp edges | 1.5 to 2.1 |
| Rounded box | 0.8 to 1.2 |
| Circular cylinder (subcritical) | 1.0 to 1.2 |
| Streamlined pontoon bow | 0.3 to 0.6 |
| Bridge deck with vehicles and railings | 1.3 to 2.0 |

### 20.4 Beaufort wind reference

| Beaufort | Description | Speed (m/s) | Speed (mph) |
|---|---|---|---|
| 6 | Strong breeze | 10.8 to 13.8 | 25 to 31 |
| 8 | Gale | 17.2 to 20.7 | 39 to 46 |
| 10 | Storm | 24.5 to 28.4 | 55 to 63 |
| 12 | Hurricane force | 32.7+ | 73+ |

### 20.5 Typical friction coefficients for gravity anchors

| Bottom | $\mu$ |
|---|---|
| Soft mud | 0.2 to 0.4 |
| Sand | 0.4 to 0.6 |
| Gravel | 0.5 to 0.7 |
| Rock (smooth) | 0.3 to 0.5 |

---

## 21. Equation Cheat Sheet

| Quantity | Equation |
|---|---|
| Buoyant force | $F_B = \rho_w g \nabla$ |
| Equilibrium volume | $\nabla = m / \rho_w$ |
| Box draft | $T = m / (\rho_w L B)$ |
| Freeboard | $f = D - T$ |
| Reserve buoyancy | $\rho_w g (V_{env} - \nabla)$ |
| Added draft | $\Delta T = \Delta m / (\rho_w A_{wp})$ |
| TPC | $\rho_w A_{wp} / 100$ |
| Salt to fresh draft | $T_f = T_s \rho_s/\rho_f$ |
| Horizontal cylinder area | $A = \tfrac{R^2}{2}(\theta - \sin\theta)$, $\theta = 2\arccos\tfrac{R-d}{R}$ |
| Metacentric height | $GM = KB + BM - KG$ |
| BM | $BM = I_T / \nabla$ |
| Box BM | $B^2/(12T)$ |
| Separated floats | $I_T = \sum(i_0 + a y^2)$ |
| Heel from offset load | $\tan\phi = w e / (\Delta GM)$ |
| Wall-sided GZ | $\sin\phi\,(GM + \tfrac{BM}{2}\tan^2\phi)$ |
| Deck edge immersion | $\tan\phi = 2f/B$ |
| Free surface loss | $GG' = (\rho_l/\rho_w)\, i_{fs}/\nabla$ |
| Foundation modulus | $k = \rho_w g B$ |
| BOEF parameter | $\lambda = (k / 4EI)^{1/4}$ |
| Point load deflection | $w_0 = P\lambda / 2k$ |
| Point load moment | $M_0 = P / 4\lambda$ |
| Critical wave length | $L_w^* = \sqrt{2}\,\pi/\lambda$ |
| Max wave moment (simplified) | $\tfrac{a}{2}\sqrt{k EI}$ |
| Wind force | $\tfrac12 \rho_a C_d A V^2$ |
| Current force | $\tfrac12 \rho_w C_d A U^2$ |
| Fetch-limited $H_s$ | $0.0016 \tfrac{U^2}{g}(gF/U^2)^{1/2}$ |
| Fetch-limited $T_p$ | $0.2857 \tfrac{U}{g}(gF/U^2)^{1/3}$ |
| Deep water wavelength | $L_w = gT^2/2\pi$ |
| Wave energy | $E = \rho_w g H^2 / 8$ |
| Drift force | $\tfrac12 \rho_w g a^2 R_c^2$ |
| Heave period | $2\pi\sqrt{(m+m_a)/(\rho_w g A_{wp})}$ |
| Roll period | $2\pi r_{xx}/\sqrt{g\,GM}$ |
| Catenary suspended length | $s = \sqrt{h(h + 2H/w)}$ |
| Catenary horizontal reach | $x = (H/w)\sinh^{-1}(sw/H)$ |
| Top tension | $T = H + wh$ |
| Gravity anchor hold | $\mu(W_{sub} - F_V)$ |
| Flooding sinkage | $\delta T = \mu_p a T/(A_{wp} - \mu_p a)$ |
| Leak rate | $Q = C_d A \sqrt{2gh}$ |
| Thermal movement | $\Delta L = \alpha L \Delta T$ |
| End-anchored arch force | $N = p R_p$ |

---

## 22. Glossary

| Term | Meaning |
|---|---|
| Added mass | Water accelerated along with a moving floating body |
| Ballast | Weight (often water) added to adjust draft, trim or heel |
| Bay | One unit of a military ribbon bridge |
| Casting basin | Dry dock where concrete pontoons are built |
| Catenary | Curve of a hanging chain or cable |
| Center of buoyancy (B) | Centroid of the displaced volume |
| Displacement ($\Delta$) | Mass of water displaced, equal to total floating mass |
| Draft | Depth of the bottom below the waterline |
| Draw span | Movable section that opens a navigation channel |
| Fetch | Unobstructed distance over water that wind blows across |
| Freeboard | Height of the side above the waterline |
| Heave | Vertical motion |
| Heel | Sideways tilt |
| KG | Height of the center of gravity above the keel |
| Metacenter (M) | Pivot point for small-angle heeling |
| Permeability | Fraction of a compartment volume that floodwater can fill |
| Pontoon | Watertight buoyant unit supporting the bridge |
| Post-tensioning | Steel tendons stressed after concrete hardens to keep it in compression |
| RAO | Response amplitude operator, motion per unit wave amplitude by frequency |
| Reserve buoyancy | Watertight volume above the waterline |
| Seiche | Standing oscillation of an enclosed water body |
| Transition span | Hinged span joining the floating section to fixed approaches |
| Trim | Fore and aft tilt |
| Waterplane | Horizontal cross-section of the hull at the waterline |
| Winkler foundation | Model of support as independent springs, which water exactly matches for a floating beam |
