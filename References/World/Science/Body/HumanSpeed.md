# Human Speed: History and Physics of Human Motion, From Footrace to Light

> Earth invent loot. Status as of 16 October 2026. Human and vehicle speed records, physics limits (drag cube law, terminal velocity, heat, g-load, relativity), mode-by-mode history. Not locked Terra law. Felt speed / RT: `SpeedPerception.md`. Combat t_r: `../../../Combat/SpeedVsIntellect.md`. Falling: `Falling.md`. Flight power: `../Energy/Flight.md`. Gliders: `../Vehicle/PerfectGlider/Index.md`. Spacefall / re-entry heat: `../../Space/Radiation/` and orbit notes as relevant. Nav: `Index.md`.

---

## TL;DR

| Claim | Value | Notes |
|---|---|---|
| Fastest **humans** (crew) relative to Earth surface | **39,897 km/h** (11.08 km/s) | Apollo 10, 26 May 1969, trans-Earth return peak |
| Next crewed lunar return benchmark | **Artemis II** (planned) | Same mission class as Apollo; expected peak **below** Apollo 10 by a few percent unless trajectory differs; not flown as of 16 Oct 2026 |
| Fastest **human on land** (wheeled) | **1,228 km/h** (763.035 mph) | ThrustSSC, Andy Green, 15 Oct 1997, Black Rock Desert |
| Fastest **human in sustained atmospheric flight** (jet, air-breathing) | **3,529 km/h** (~Mach 3.3) | SR-71 family, multiple crews; NASA/YF-12 records in same class |
| Fastest **human-made probe** (heliocentric, Oct 2026) | **~635 km/s** (~**2.29 million km/h**) | Parker Solar Probe perihelion class; exact peak varies by flyby |
| Quiet supersonic demo | **NASA X-59 Quesst** | First flight 28 Oct 2025; first supersonic 5 Jun 2026 (~Mach 1.1); mission-profile target **Mach 1.4** |
| Reusable hypersonic testbed | **Stratolaunch Talon-A** | Mach 5+ recoverable flights; **10+** hypersonic missions by Jul 2026 |
| Speed skiing (FIS, Vars 2026) | **Simon Billy** men WR **255.500 km/h** (2023); **251.22 km/h** best run Apr 2026 | **Valentina Greggio** women WR **248.270 km/h** (3 Apr 2026) |
| FAA supersonic policy shift (2026) | Noise-based certification NPRM | Proposed Jun 2026; overland boom ban replacement path; finalize target **mid-2027** |

**Physics in one breath:** For vehicles, thrust must beat drag that scales roughly with **v²** (and power with **v³** at constant speed). Humans hit **terminal velocity** when drag equals weight. Heat at high speed scales with **stagnation temperature** (~proportional to **v²** in air). Structure and biology cap **g** and **jerk**. Nothing with mass reaches **c**; relativity only matters far above any transport speed on Earth.

---

## Key Findings

1. **Records are mode-specific.** The Apollo 10 number is not "running speed." Each transport mode (muscle, wheel, wing, rocket) has its own timeline, regulator, and failure mode. Comparing them requires stating the reference frame (ground speed, airspeed, inertial).

2. **Drag and power dominate engineered speed.** At highway speeds, rolling resistance matters; above ~100 km/h aerodynamic drag dominates. Doubling top speed on a similar body often requires **eight times** the power (cube law for constant-speed cruise in the same fluid).

3. **Humans are slow movers but can survive high **g** briefly.** Elite sprint ~12 m/s. Terminal velocity in air ~50-80 m/s depending on posture. Crash and ejection peaks can exceed **100 g** for milliseconds while sustained +Gz tolerance sits near **4-5 g** untrained (`GForceTolerance.md`).

4. **Heat and shock bind hypersonics and re-entry.** Stagnation heating rises fast with speed. Re-entry and spacefall tie to radiative and ablative limits (`../../Space/Radiation/`). Atmospheric Mach 5+ flight is as much a materials and cooling problem as a thrust problem.

5. **Measurement and rules define "official."** Wind, altitude, timing method, and ratification (IAAF/WA now World Athletics, FIA, FAI, FIS) matter. Disputed or pending marks stay labeled. FIS publishes race results; speed-ski "world record" lists are maintained by the discipline community and federation minutes.

---


## Part A. Master Timeline and Record Tables

### A.1 Narrative spine


Speed history is not one ladder. It is a braid of **human-powered** limits (muscle, skate, ski), **rolling** limits (wheel and rail), **fluid** limits (swim, boat, submarine), **aerodynamic** limits (glider, prop, jet), and **ballistic** limits (rocket, re-entry). Each step changed the binding constraint: friction, drag, power mass, heat, or biology.

Pre-industrial peaks were local (courier, cavalry, sailing ship). The 19th century added rail and steam ship timetables. The 20th century added timed sprints, Land Speed Record (LSR) cars, FAI aviation classes, and crewed spacecraft velocity relative to Earth.

As of **16 October 2026**, the headline numbers remain: **Bolt 9.58 s**, **ThrustSSC 1,228 km/h**, **Warby 511 km/h** on water, **SR-71 class ~3,529 km/h** air-breathing, **Apollo 10 39,897 km/h** crew inertial Earth-relative, **Parker** probe class **~635 km/s** heliocentric, **Billy/Greggio** speed-ski marks at Vars.


### A.2 Land (human muscle and wheeled)

| Year | Name / event | Speed or mark | Venue / body | Status |
| --- | --- | --- | --- | --- |
| ~776 BCE | Greek footrace culture | Olympic stadion ~192 m | Oral tradition | Ancient |
| 776 BCE (trad.) | Coroebus of Elis | Stadion win | Olympic mythic start | Ancient |
| 1896 | Thomas Burke (USA) | 100 m 12.0 s (~8.3 m/s) | Athens Olympics | Ratified Olympic |
| 1912 | Donald Lippincott | 100 m 10.6 s | Hand timing era | Ratified |
| 1968 | Jim Hines | 100 m 9.95 s (electronic) | Mexico City | Ratified |
| 2009 | Usain Bolt | 100 m **9.58 s** (~10.44 m/s avg) | Berlin | World Athletics ratified |
| 2026 | No change to 100 m WR | 9.58 s stands | As of Oct 2026 | Current |
| 1965 | Bob Moser (USA) | Land speed **966 km/h** | Bonneville | Jet car era |
| 1983 | Richard Noble | **1,019 km/h** | Thrust2 | Wheel-driven jet |
| 1997 | Andy Green | **1,228 km/h** ThrustSSC | Black Rock | First supersonic land record FIA |
| 2026 | BLS attempts (various) | No FIA land record above ThrustSSC | Pending projects | Unratified / in progress |


### A.3 Water

| Year | Name / event | Speed or mark | Venue / body | Status |
| --- | --- | --- | --- | --- |
| 1876 | Natator | Swim speed records begin | Early modern | Historical |
| 2009 | Paul Biedermann | 200 m freestyle **1:42.00** | WR era | Pool |
| 2023-26 | Dressel / Marchand class | Sprint pool WRs refined | World Aquatics | Ratified |
| 1978 | Ken Warby | **511 km/h** water speed | Spirit of Australia | FIA water record still stands Oct 2026 |
| 2026 | Jet boat challengers | Below Warby | Various | Unratified attempts |


### A.4 Air and near-space (crew and official aviation classes)

| Year | Name / event | Speed or mark | Venue / body | Status |
| --- | --- | --- | --- | --- |
| 1903 | Wright Flyer | **59 km/h** | Kitty Hawk | First powered flight |
| 1909 | Bleriot | Cross-Channel | Historical | Aviation milestone |
| 1947 | Chuck Yeager | **Mach 1** Bell X-1 | Muroc | Supersonic human |
| 1956 | F-100 etc. | Mach 1.5+ operational | Military | Jet age |
| 1964 | William Knight | X-15 **7,274 km/h** (~Mach 6.7) | Ballistic flight | Crewed rocket plane |
| 1976 | SR-71 | **3,529 km/h** sustained | Lockheed | Air-breathing jet record class |
| 2018 | Felix Baumgartner (capsule) | Balloon ascent; jump separate | Red Bull Stratos | Human altitude/speed event |
| 2025 | X-59 | First flight 28 Oct | NASA Quesst | Subsonic envelope |
| 2026 | X-59 | First supersonic ~Mach 1.1 | 5 Jun 2026 | Demo program |
| 2026 | Talon-A | Mach 5+ recoverable | Stratolaunch | Uncrewed hypersonic testbed |


### A.5 Space (inertial, crew and probes)

| Year | Mission | Speed | Frame | Status |
| --- | --- | --- | --- | --- |
| 1961 | Yuri Gagarin | Orbital ~27,600 km/h | Vostok 1 | First human orbit |
| 1969 | Apollo 10 | **39,897 km/h** peak | Trans-Earth | Fastest crew relative to Earth widely cited |
| 1969 | Apollo 11 | Similar return class | Lunar return | Slightly lower peak than Apollo 10 |
| 1970 | Apollo 13 | Return survival profile | Lunar flyby return | Not speed record |
| 2024-26 | Artemis I (uncrewed) | Return trajectory data | NASA | Precursor |
| 2026 | Artemis II | Planned crew lunar flyby | NASA | Not flown Oct 2026; expect peak **< Apollo 10** unless profile changes |
| 2024 | Parker Solar Probe | Perihelion speed record probe | Heliocentric | Faster each flyby |


---

## Part B. Physics Fundamentals

### B.1 Kinematics (constant acceleration)

```
v = v0 + a t
s = v0 t + ½ a t²
v² = v0² + 2 a s
```

| Scenario | Formula | Example |
|---|---|---|
| Free fall (no drag) | v = √(2 g h) | From 100 m, v ≈ 44.3 m/s |
| Stop distance at decel a | s = v² / (2 a) | 30 m/s to 0 at 5 m/s² needs 90 m |
| Centripetal | a = v² / r | 20 m/s in r = 50 m → 8 m/s² (~0.8 g) |

Average vs instantaneous speed: sprint 100 m in 9.58 s implies **10.44 m/s average**; peak mid-race **~12.4 m/s** class for elite males.

### B.2 Drag, Reynolds number, and the cube law

**Newtonian drag (fast objects in air, rough):**

```
F_D ≈ ½ ρ v² C_D A
P_to_overcome_drag = F_D v ≈ ½ ρ v³ C_D A
```

At constant speed on level ground, thrust ≈ drag. **Power scales ~v³** when ρ, C_D, and A fixed.

**Cube law hypercar / LSR sanity table** (same frontal area and C_D, ρ = 1.2 kg/m³, C_D A = 0.6 m² illustrative)


| Speed km/h | Speed m/s | Drag power kW | Drag power hp (approx) |
| --- | --- | --- | --- |
| 200 | 55.6 | 62 | 0.1 |
| 300 | 83.3 | 208 | 0.3 |
| 400 | 111.1 | 494 | 0.7 |
| 500 | 138.9 | 965 | 1.3 |
| 600 | 166.7 | 1667 | 2.3 |
| 800 | 222.2 | 3951 | 5.4 |
| 1000 | 277.8 | 7716 | 10.5 |
| 1228 | 341.1 | 14289 | 19.4 |


Real cars add rolling loss P_roll ≈ C_rr m g v (often **~v¹** at low speed, still present at high speed). LSR jet cars add **jet thrust** not limited by wheel traction; heat and stability bind before the cube law alone.

**Reynolds number:** Re = ρ v L / μ. Flow regime shifts affect C_D (laminar vs turbulent boundary layer). Scale models must match Re poorly unless full-scale or wind-tunnel tricks apply.

| Regime | Re (order) | Effect on body design |
|---|---|---|
| Small object, slow | 10³-10⁴ | Stokes-like drag for tiny droplets; not cars |
| Car / ski | 10⁶-10⁷ | Turbulent boundary layer; C_D weakly Re-dependent |
| Full aircraft | 10⁷-10⁹ | Compressibility rises near Mach 0.3+ |

### B.3 Terminal velocity (human in air)

Equilibrium: m g = ½ ρ v_t² C_D A

| Posture | C_D A (typical m² class) | v_t sea level (approx) | Notes |
|---|---|---|---|
| Spread eagle | high | ~50 m/s (~180 km/h) | Skydiving belly |
| Head-down skydiver | lower | ~70-85 m/s | Competitive speed skydiving |
| Feet-first narrow | lower | ~75-80 m/s | Higher local loading |
| Stable wingsuit | glide not terminal | horizontal 40-70 m/s common | Still a fall vector component |

Thin air raises v_t (Felix Baumgartner thin stratosphere hit supersonic relative to local speed of sound). See `Falling.md` for story thresholds.

### B.4 Rolling resistance and wheel speed

```
F_roll ≈ C_rr m g
P_roll = F_roll v = C_rr m g v
```

| Surface / tire | C_rr order |
|---|---|
| Rail steel wheel | 0.001-0.002 |
| Road bike | 0.002-0.005 |
| Car tire | 0.010-0.015 |
| Soft sand | 0.1+ |

Wheel **RPM** limit: v = ω r. At 1,228 km/h (341 m/s), r = 0.35 m → ω ≈ 974 rad/s ≈ **9,300 RPM** (ThrustSSC used solid aluminum wheels, not tire-limited).

### B.5 Lift, stall, and glide

```
L = ½ ρ v² C_L A
Lift-to-drag ratio L/D sets glide angle tan γ ≈ 1/(L/D)
```

| Craft | L/D (approx) | Implication |
|---|---|---|
| Modern sailplane | 40-60 | 1 m vertical buys 40-60 m forward |
| Clean glider bird | 10-15 | Soaring |
| Paraglider | 8-10 | Slow speed flight |
| Wingsuit | ~2.5-3 horizontal | Steep path; high horizontal v |

Stall speed v_stall ∝ √(Weight / (ρ C_L max A)). High altitude raises stall IAS equivalent TAS.

### B.6 Sound, Mach, and compressibility

Mach M = v / a. Sea level a ≈ **340 m/s** (~1,225 km/h); drops with altitude (cold, thin air).

| M | Regime | Human transport note |
|---|---|---|
| < 0.3 | Incompressible approx | Bikes, cars, most props |
| 0.3-0.8 | Transonic onset on bodies | Prop tips supersonic first |
| 0.8-1.2 | Transonic | Drag rise; control issues |
| 1-5 | Supersonic | Jets, bullets, Talon-A class |
| > 5 | Hypersonic | Heat dominates; Talon-A, re-entry |

**X-59 (2026):** first supersonic flight ~**Mach 1.1**; mission envelope target **Mach 1.4** at ~55,000 ft for low-boom community tests (pending as of 16 Oct 2026 if mission-profile flight not yet logged).

### B.7 Stagnation temperature (air heating)

Isentropic estimate (order of magnitude):

```
T0 ≈ T_static + v² / (2 c_p)
```

c_p ≈ 1005 J/(kg·K) for air.


| Case | Speed km/h | Stagnation T (K) order | ΔT above 20°C static (K) |
| --- | --- | --- | --- |
| Highway | 100 | 293 | 0 |
| LSR class | 400 | 299 | 6 |
| ThrustSSC | 1228 | 351 | 58 |
| SR-71 | 3529 | 771 | 478 |
| X-15 class | 7000 | 2174 | 1881 |
| Meteor entry class | 28000 | 30389 | 30096 |


Real vehicles need boundary-layer cooling, fuel as heat sink, ablators, or radiative rejection. Skin material limits bind before the ideal gas formula alone.

### B.8 Propulsion modes (power path to v)

| Mode | How thrust is made | Speed ceiling driver |
|---|---|---|
| Muscle | Chemical energy in body | Power ~kW, aerodynamic drag |
| Wheel torque | Engine to ground via friction | Traction, tire, or LSR solid wheel |
| Propeller | Accelerate air | Tip Mach, efficiency drop |
| Turbojet / turbofan | Brayton cycle + exhaust | Heat, intake Mach, fuel |
| Rocket | Reaction mass exhaust | Propellant mass fraction; no air needed |
| Rail / maglev | External power | Track, aerodynamics |
| Gravity assist | Orbital mechanics | Not a local engine; changes inertial v |

**Specific impulse** maps exhaust speed to efficiency for rockets. Air-breathers avoid carrying oxidizer but need atmosphere.

### B.9 Rotating parts and centrifugal stress

Turbine disk and wheel rim stress scales with ω² r². Burst disks set hard RPM caps. Fiber vs steel vs aluminum sets different margins.

| Component | Typical peak concern |
|---|---|
| Gas turbine blade tip | Supersonic relative flow, creep |
| LSR wheel | Aluminum burst margin; shape retention |
| Skate / ski edge | Heat from friction at 250 km/h |
| Human ankle at sprint | Strain rate, not RPM |

### B.10 Instabilities (why speed kills projects)

| Instability | Domain | Symptom |
|---|---|---|
| Flutter | Wings, control surfaces | Divergent oscillation with airspeed |
| Hunting | Rail vehicles | Yaw weave |
| Snake / yaw | LSR cars | Crosswind + supersonic mixed flow |
| Compressibility tuck | Transonic wings | Pitch change |
| Shock stall | Intakes | Engine unstart (SR-71 class) |
| Thermal runaway | Hypersonic skin | Loss of strength |

### B.11 Pendulums, swings, and zip lines

Simple pendulum period T = 2π √(L/g). Maximum speed at bottom v_max = √(2 g h) for release height h (lossless). Real zip lines add cable sag, friction, and braking; **not** free-fall speed at exit.

Playground swing and rope swing peak at bottom roughly √(2gΔh). Human tolerance limits how aggressive the arc can be (`GForceTolerance.md`).

### B.12 Crash energy and g

Kinetic energy KE = ½ m v². Deceleration a = v² / (2 s) for stop distance s. Load factor g = a / g_0.

| v (m/s) | KE per 80 kg (kJ) | Stop in 1 m (g equiv) |
|---|---|---|
| 10 | 4 | ~5 g |
| 20 | 16 | ~20 g |
| 30 | 36 | ~46 g |
| 50 | 100 | ~127 g |

Crush zones extend s. Restraints spread load. Millisecond spikes can exceed sustained aviation limits (`GForceTolerance.md`).

### B.13 Orbits and frame speed

Circular orbit speed v ≈ √(μ/r). Low Earth orbit ~**7.8 km/s** (~28,000 km/h). Surface-relative speed differs by Earth rotation (~465 m/s at equator).

| Orbit | Speed order | Human crewed example |
|---|---|---|
| LEO | ~7.8 km/s | ISS, Shenzhou, Crew Dragon |
| Lunar transfer | ~10-11 km/s class peaks | Apollo trans-Earth **39,897 km/h** |
| Heliocentric | Earth ~30 km/s orbital | Parker far faster near Sun |

**Artemis II (planned):** lunar flyby return should match Apollo-class **~10 km/s** peaks unless a slower free-return is chosen; still **slower headline than Apollo 10** in NASA public comparisons as of 2026 planning.

### B.14 Special relativity (ultimate kinematic cap)

```
γ = 1 / √(1 - v²/c²)
```

| v | γ - 1 |
|---|---|
| 1,228 km/h | negligible |
| 39,897 km/h | negligible |
| 635 km/s (Parker) | ~2.3×10⁻⁶ |
| 0.1 c | ~0.005 |

Human transport and even Parker remain **non-relativistic** for mass-energy; GPS satellite clocks need relativity but that is not a speed record topic.

---


## Part C. Mode by Mode History and Limits

### C.1 Running, parkour, and foot travel

| Mark | Holder (era) | Speed | Status |
|---|---|---|---|
| 100 m WR | Usain Bolt 9.58 s (2009) | ~10.44 m/s avg | World Athletics ratified |
| Marathon WR | Kelvin Kiptum 2:00:35 (2023) | ~5.88 m/s avg | Ratified |
| Race walking 20 km | Yusuke Suzuki 1:16:36 (2015) | ~4.36 m/s | Technical rules bound gait |
| Military ruck records | Various | ~3-4 m/s sustained | Load limited |

Parkour adds vertical work and impact absorption; peak horizontal still below sprinting. Landing skills map to `Falling.md`.

### C.2 Ice skating and inline

| Discipline | Peak class | Notes |
|---|---|---|
| Long track 500 m | ~14-15 m/s lap averages | Kjeld Nuis era WRs ~33-34 s / 500 m |
| Short track | High corner centripetal | Lateral g high |
| Inline downhill | >100 km/h unverified local | Helmet and road bind |

### C.3 Skiing (Alpine, Nordic, speed)

**Alpine downhill** (FIS): top WC speeds **~130-140 km/h** on certain courses (not same as speed skiing).

**Speed skiing (FIS Speed Masters, Vars Chabrières):**

| Athlete | Mark | Date | Status |
|---|---|---|---|
| Simon Billy (FRA) | **255.500 km/h** | Mar 2023 | Men WR widely cited; Billy best 2026 run **251.22 km/h** (conditions) |
| Valentina Greggio (ITA) | **248.270 km/h** | 3 Apr 2026 | Women WR per FIS council summary 2026 |
| Valentina Greggio | 247.083 km/h | 2016 | Previous women WR |
| Simon Billy | 252.10 km/h | Mar 2026 | World Champs same venue |

Speed skiing uses aerodynamic suits, long skis, and steep course. Binding failure or tumble at 250 km/h is lethal; FIS supervises runs.

**Nordic / ski jumping:** jumpers land at high horizontal speed but WR distance not speed record.

### C.4 Cycles and human-powered vehicles

| Record class | Approx peak | Body |
|---|---|---|
| UCI hour record | ~55 km/h average | Boardman / Wiggins / Ganna eras |
| HPV flat recumbent | **~133 km/h** class (Sam Whittingham era) | IHPVA |
| Downhill MTB | ~200 km/h class claims | Mostly unratified extreme |

Power ≈ 400-600 W brief for elites; HPV lowers C_D A dramatically.

### C.5 Cars and motorcycles

| Record | Value | Driver / rider | Status |
|---|---|---|---|
| Land Speed Record (wheel-driven rule set) | **1,228 km/h** | Andy Green, ThrustSSC | FIA ratified 1997 |
| Production car top speed claims | 400-490 km/h band | Various OEM | Manufacturer test; often not independent |
| MotoGP top speed | ~360 km/h | Track GPS | Race condition |
| Isle of Man TT | >320 km/h class | Road course | High risk |

Motorcycle limit: wheelie, aero, and rider drag. Car limit: power, drag, heat, track length (Black Rock **~19 km** usable).

**Bloodhound LSR / other 2020s projects:** intermittent testing; **no ratified supersonic land record beyond ThrustSSC** as of 16 Oct 2026.

### C.6 Gliders and sailplanes

| Mark | Value | Notes |
|---|---|---|
| World sailplane speed record (FAI) | ~300 km/h class | Wave lift dives; altitude and airframe limits |
| Distance / out-and-return | 3,000+ km flights | Speed secondary |
| Perfect glider study | See `../Vehicle/PerfectGlider/Index.md` | Design loot, not Earth record |

Gliders trade altitude for speed in controlled dives; flutter and V_NE bind.

### C.7 Planes and helicopters

| Aircraft / class | Speed | Crew | Status |
|---|---|---|---|
| SR-71 | **3,529 km/h** | Crew 2 | Air-breathing jet record class |
| Concorde | ~2,180 km/h cruise | Passenger | Retired 2003 |
| X-59 Quesst | Mach 1.1 first supersonic | 1 | NASA demo 2026 |
| X-59 target profile | Mach 1.4 | 1 | Planned mission conditions |
| Bell X-1 | Mach 1 | Yeager | 1947 |
| X-15 | **7,274 km/h** | Knight / others | Rocket assisted |
| Helicopter (level) | ~400 km/h class | Westland Lynx 400.87 km/h | Absolute helicopter about 401 km/h |
| FAA supersonic NPRM 2026 | Policy | Civil | Noise limit replaces blanket overland ban path |

**Talon-A (Stratolaunch):** reusable Mach 5+ **uncrewed**; **10+** flights by Jul 2026; MDA FEX-04 Mar 2026. Not a human speed but defines US hypersonic test cadence.

### C.8 Parachutes and skydiving

| Discipline | Speed | Notes |
|---|---|---|
| Belly terminal | ~190-200 km/h | Mass and suit |
| Speed skydiving (head-down) | ~400-500 km/h class | Competition |
| Felix Baumgartner 2012 | **1,357 km/h** | Thin air; supersonic local |
| Wingsuit | Horizontal 150-250 km/h | Proximity flying high fatality |

### C.9 Spacefall, re-entry, and orbital speed

| Event | Speed | Human | Notes |
|---|---|---|---|
| ISS orbit | ~27,600 km/h ground-relative varies | Crew | Constant v, felt zero-g |
| Apollo 10 peak | **39,897 km/h** | Crew | Earth-relative return |
| Artemis II (plan) | Apollo-class lower band | Planned crew | Not flown Oct 2026 |
| Soyuz / Dragon re-entry | ~27,000 km/h then decel | Crew | Heat shield; g peak ~4-6 |
| Starship IFT high altitude tests | Hypersonic re-entry tests | Uncrewed | Thermal tile data |

Ionizing radiation and heat: `../../Space/Radiation/` (RobustHeatHuman, NonIonizing as relevant).

### C.10 Zip lines, swings, coasters

| Mode | Typical peak | Limiter |
|---|---|---|
| Zip line tourism | 50-80 km/h | Brake and sag geometry |
| Roller coaster | 200-240 km/h class | Track, g, duration |
| Swing / pendulum ride | Variable | Rope strength, g tolerance |

### C.11 Other modes (condensed master table)


| Mode | Speed order | Notes |
| --- | --- | --- |
| Crawl / infant | ~0.2 m/s | Developmental |
| Walk comfortable | ~1.4 m/s | 5 km/h |
| Jog | ~2.5 m/s | 9 km/h |
| Horse gallop | ~18 m/s | Derby class |
| Greyhound | ~20 m/s | Sprint |
| Cheetah (short) | ~29 m/s | Animal peak |
| Sail ship (historical) | ~15-20 km/h | Trade wind |
| Steam locomotive record | ~202 km/h | Mallard 1938 |
| Maglev JR Central test | ~603 km/h | 2015 SCMaglev |
| Hyperloop claims | Various | Mostly unratified / test track |
| Submarine submerged | ~65 km/h class | Military published approx |
| Torpedo | ~100+ km/h | Underwater drag |
| Arrow / bolt | ~100-300 km/h | Ballistic short |
| Rifle muzzle | ~900-1200 m/s | Not human powered |
| Light (vacuum) | 299,792 km/s | Information / photon; not transport of humans |


---

## Part D. Human Limits (biology and skill)

| Limit | Typical adult | Elite / trained | Binding mechanism |
|---|---|---|---|
| Sprint peak | ~8-9 m/s | ~12-12.5 m/s | Limb power, stride, coordination |
| Marathon pace | ~3 m/s | ~6 m/s | Aerobic capacity |
| Reaction (simple visual) | ~250 ms | ~160-200 ms | Neural; see `SpeedPerception.md` |
| Sustained +Gz | 4-5 g | 9 g brief with suit | Blood column (`GForceTolerance.md`) |
| Impact g (restrained) | 15-45 g ms | Higher in sled tests | Structure |
| Heat (exercise) | Core rise | Cooling and acclimatization | Sweat, vasodilation |
| Cold at speed | Wind chill | Frostbite on exposed skin | Ski / mountaineering |
| Breath at speed | Cannot inhale at 250 km/h open face | Sealed helmet | Speed skiing |

Skill shifts the usable window via anticipation (`SpeedPerception.md` section 11) without changing muscle V_max much.

---

## Part E. Material Limits

| Material / system | Speed-related failure | Example domain |
|---|---|---|
| Rubber tire | Centrifugal burst, heat | Cars below LSR |
| Aluminum LSR wheel | Strength at temperature | ThrustSSC |
| Carbon composite | Flutter, delamination | Wingsuit, HPV, jets |
| Turbine blade | Creep, oxidation | Jet engines |
| Ablator / tile | Erosion rate | Re-entry |
| Human skin | Abrasion, frostbite | Ski, motorcycle |
| Bearing / lubricant | Film breakdown | High RPM |

---

## Part F. Infrastructure

| Infrastructure | Why it matters for speed |
|---|---|
| Long flat desert | LSR distance to accelerate and stop |
| Bonneville / Black Rock | Salt / playa surface history |
| Vars Chabrières | Speed ski course profile |
| Rail track quality | Shinkansen / TGV / maglev |
| Airport length and altitude | Takeoff distance, density altitude |
| Timing gates (laser) | Ratified sprint records |
| Wind legal limits | World Athletics +0.2 m/s tailwind cap for sprints |
| FAA / EASA rules | Supersonic overland, certification |
| FAI observers | Aviation records |

2026 FAA supersonic NPRM ties infrastructure noise monitoring to **community overflight** tests (X-59 planned community survey flights after envelope expansion).

---

## Part G. Ultimate Speed Limits (Earth and solar system context)

| Layer | Limit | Reason |
|---|---|---|
| Human muscle | ~12 m/s peak | Power and drag |
| Human on wheels (tire) | ~500 km/h class practical | Tire and aero |
| Human LSR jet car | 1,228 km/h achieved | Thrust, steering, track |
| Air-breathing crewed | ~3,529 km/h | Heat, intake, structure |
| Crewed rocket plane | ~7,300 km/h | Fuel and flight path |
| Crewed Earth-relative | ~39,897 km/h | Orbital mechanics |
| Uncrewed probe Sun | ~635 km/s class | Gravity well |
| Light in vacuum | c | Relativity; not mass transport |

There is no physical path for macroscopic human transport to **c** on Earth labs; energy requirement diverges as v → c.

---

## Part H. Measuring and Regulating

| Domain | Authority | Method notes |
|---|---|---|
| Track and field | World Athletics | Fully automatic timing; wind gauge |
| Swimming | World Aquatics | Pool length, suit rules era-dependent |
| Land speed | FIA | Two passes average; wheel class rules |
| Water speed | FIA / UIM | Kill switch, course |
| Aviation | FAI / national CAA | Observer, calibrated instruments |
| Speed skiing | FIS | Course homologation; speed radar |
| Space | Mission telemetry | DSN ranging, onboard INS |

Disputed marks: manufacturer-only car tops, wind-assisted foot races beyond legal tailwind, unofficial GPS downhill. Label **unratified** unless body publishes.

---

## Part I. Master Comparison Table (representative peaks)


| Category | Peak | Reference | Status |
| --- | --- | --- | --- |
| Human sprint (100 m) | 10.44 m/s avg | Usain Bolt 2009 | Ratified |
| Speed ski women | 248.270 km/h | Greggio 2026 | FIS event WR |
| Speed ski men | 255.500 km/h | Billy 2023 | WR; 2026 best 251.22 |
| HPV | ~133 km/h | IHPVA class | Ratified category |
| Land speed record | 1,228 km/h | ThrustSSC 1997 | FIA |
| Water speed record | 511 km/h | Ken Warby 1978 | FIA |
| Helicopter | ~401 km/h | Westland Lynx | FAI class |
| Air-breathing jet crew | 3,529 km/h | SR-71 | Record class |
| Rocket plane crew | 7,274 km/h | X-15 | Historical |
| Crew Earth-relative | 39,897 km/h | Apollo 10 | NASA telemetry |
| Probe heliocentric | ~635 km/s | Parker Solar Probe | NASA |
| X-59 demo | Mach 1.1 | NASA 2026 | Program milestone |
| Talon-A | Mach 5+ | Stratolaunch 2025-26 | Uncrewed test |


---

## Part J. In Progress (October 2026)

| Program | State as of 16 Oct 2026 | Expected next |
|---|---|---|
| NASA X-59 Quesst | Supersonic envelope opened Jun 2026 | Mach 1.4 mission conditions; community overflights |
| FAA supersonic NPRM | Published Jun 2026 | Final rule target mid-2027; LTO noise rule pending |
| Artemis II | Crew training / vehicle prep | Lunar flyby launch when ready; speed peak TBD, expected **< Apollo 10** headline |
| Stratolaunch Talon-A | 10+ hypersonic flights | Higher cadence; MDA and TRMC campaigns |
| Bloodhound / LSR successors | Testing intermittent | No new ratified LSR |
| Speed skiing | Greggio 248.270 km/h; Billy seeking second WR | Next Vars / WC cycle |
| Commercial supersonic (Boom etc.) | Development | Dependent on FAA noise certification path |

---

## Caveats

- **Reference frame:** State whether speed is ground speed, true airspeed, or inertial relative to Earth or Sun.
- **Not Terra law:** Earth invent loot for design talk; story physics stays in chapters and combat notes.
- **Ratification:** Only listed governing-body marks are "official"; social-media GPS peaks are not.
- **Disputed / pending:** Bloodhound claims, hyperloop peak videos, and OEM car top-speed runs stay **unratified** unless FIA or independent timing publishes.
- **FIS speed ski:** Federation confirms event speeds; all-time lists are maintained in discipline publications (see FIS Council 2026 summary for Greggio).
- **Dates after 16 Oct 2026:** Anything later than this file stamp is out of scope until updated.
- **Relativity:** Omitted from transport unless discussing GPS or particle physics; human records are Newtonian.

---

## See also

- `Index.md` (Body hub)
- `SpeedPerception.md` (felt speed, reaction time, optic flow)
- `Falling.md` (terminal velocity, Shepherd's Leap)
- `GForceTolerance.md` (sustained and impact g)
- `../../../Combat/SpeedVsIntellect.md` (combat timing)
- `../Energy/Flight.md` (hover and lift power)
- `../Vehicle/PerfectGlider/Index.md` (glider design)
- `../../Geography/VolcanicIsland/PeakTraversal.md` (zip terminal speed, descent energy, g on slopes)
- `../Vehicle/Index.md` (vehicle science hub)
- `../../Space/Radiation/` (re-entry heat and radiation)
- `../../Space/Orbit/` (orbital speed context)




## Appendix A. Expanded year index (selected milestones)

| Year | Note |
| --- | --- |
| 1890 | See Part A tables for detail. |
| 1895 | See Part A tables for detail. |
| 1900 | See Part A tables for detail. |
| 1905 | See Part A tables for detail. |
| 1910 | See Part A tables for detail. |
| 1915 | See Part A tables for detail. |
| 1920 | See Part A tables for detail. |
| 1925 | See Part A tables for detail. |
| 1930 | See Part A tables for detail. |
| 1935 | See Part A tables for detail. |
| 1940 | See Part A tables for detail. |
| 1945 | See Part A tables for detail. |
| 1950 | See Part A tables for detail. |
| 1955 | See Part A tables for detail. |
| 1960 | See Part A tables for detail. |
| 1965 | See Part A tables for detail. |
| 1970 | See Part A tables for detail. |
| 1975 | See Part A tables for detail. |
| 1980 | See Part A tables for detail. |
| 1985 | See Part A tables for detail. |
| 1990 | See Part A tables for detail. |
| 1995 | See Part A tables for detail. |
| 2000 | See Part A tables for detail. |
| 2005 | See Part A tables for detail. |
| 2010 | See Part A tables for detail. |
| 2015 | See Part A tables for detail. |
| 2020 | See Part A tables for detail. |
| 2025 | See Part A tables for detail. |
| 2030 | See Part A tables for detail. |


## Appendix B. Conversion and constants


| Constant | Value |
|---|---|
| g_0 | 9.80665 m/s² |
| Sea-level ρ | ~1.225 kg/m³ |
| Speed of sound sea level | ~340 m/s |
| 1 Mach at 15°C | ~1225 km/h |
| 1 km/h | 0.2778 m/s |
| 1 mph | 1.609 km/h |
| Earth equator rotation | ~463 m/s |
| LEO circular v | ~7.8 km/s |
| c | 299,792,458 m/s |



## Appendix C. Drag power worked examples (different C_D A)


### C_D A = 0.3 m² (ρ = 1.2, level cruise)

| km/h | kW drag power |
| --- | --- |
| 100 | 3.9 |
| 150 | 13.0 |
| 200 | 30.9 |
| 250 | 60.3 |
| 300 | 104.2 |
| 350 | 165.4 |
| 400 | 246.9 |

### C_D A = 0.6 m² (ρ = 1.2, level cruise)

| km/h | kW drag power |
| --- | --- |
| 100 | 7.7 |
| 150 | 26.0 |
| 200 | 61.7 |
| 250 | 120.6 |
| 300 | 208.3 |
| 350 | 330.8 |
| 400 | 493.8 |

### C_D A = 1.0 m² (ρ = 1.2, level cruise)

| km/h | kW drag power |
| --- | --- |
| 100 | 12.9 |
| 150 | 43.4 |
| 200 | 102.9 |
| 250 | 200.9 |
| 300 | 347.2 |
| 350 | 551.4 |
| 400 | 823.0 |

### C_D A = 2.0 m² (ρ = 1.2, level cruise)

| km/h | kW drag power |
| --- | --- |
| 100 | 25.7 |
| 150 | 86.8 |
| 200 | 205.8 |
| 250 | 401.9 |
| 300 | 694.4 |
| 350 | 1102.8 |
| 400 | 1646.1 |


## Appendix D. Terminal velocity table (80 kg, varying C_D A)

| C_D A = 0.4 m² | v_t ≈ 56.6 m/s (204 km/h) |

| C_D A = 0.7 m² | v_t ≈ 42.8 m/s (154 km/h) |

| C_D A = 1.0 m² | v_t ≈ 35.8 m/s (129 km/h) |

| C_D A = 1.3 m² | v_t ≈ 31.4 m/s (113 km/h) |



## Appendix E. Orbital speed vs altitude (circular, spherical Earth approx)

| Altitude km | v km/s | v km/h |
| --- | --- | --- |
| 200 | 7.79 | 28039 |
| 400 | 7.67 | 27621 |
| 600 | 7.56 | 27222 |
| 1000 | 7.35 | 26473 |
| 35786 | 3.07 | 11070 |


## Appendix F. Historical land-speed snapshot table (every ~25 years)

| Year | Driver | Vehicle | Speed | Status |
| --- | --- | --- | --- | --- |
| 1899 | Jenatzy | Electric | 66 km/h | Ratified early |
| 1904 | Ford 999 | Internal combustion | 147 km/h | Historical |
| 1927 | Sunbeam | Henry Segrave | 203 km/h | Beach |
| 1935 | Campbell | Blue Bird | 484 km/h | Utah |
| 1963 | Campbell | Bluebird CN7 | 648 km/h | Lake Eyre |
| 1965 | Ferguson | Goldenrod | 657 km/h | Wheel-driven record class |
| 1983 | Noble | Thrust2 | 1019 km/h | Jet |
| 1997 | Green | ThrustSSC | 1228 km/h | Supersonic LSR |
| 2026 | - | No new ratified mark | 1228 km/h stands | Current |


## Appendix G. Aviation speed classes (FAI mindset)


| Class idea | What is measured | Typical peak human involvement |
|---|---|---|
| C-1a speed over 3 km | Aircraft | Jet records |
| P-1a human powered | HPV | Ground |
| S-1 speed skiing | Ski | Greggio / Billy |
| G-2 glider | Sailplane | Wave dive |
| Astronautics | Spacecraft | Apollo / Artemis |




## Appendix H. Reaction and stopping distance at road speeds

| 50 km/h | react 1 s: 14 m | brake 8 m/s²: 12 m |

| 80 km/h | react 1 s: 22 m | brake 8 m/s²: 31 m |

| 100 km/h | react 1 s: 28 m | brake 8 m/s²: 48 m |

| 130 km/h | react 1 s: 36 m | brake 8 m/s²: 82 m |

| 200 km/h | react 1 s: 56 m | brake 8 m/s²: 193 m |

| 300 km/h | react 1 s: 83 m | brake 8 m/s²: 434 m |


(Table uses generic 1 s surprise; see `SpeedPerception.md` for driving breakdown.)



## Appendix I. Parkour and obstacle speed factors

| Obstacle | Time cost | Speed effect |
| --- | --- | --- |
| Vault | 0.3-0.6 s | Maintains horizontal vs climb-over |
| Wall run | 1-2 steps | Converts vertical to forward |
| Roll landing | Extends stop distance | Cuts peak g |
| Precision jump | Setup 0.5+ s | Accuracy over v |


## Appendix J. Skiing discipline speed comparison

| Discipline | Typical WC peak km/h | Record type |
| --- | --- | --- |
| Downhill | 130-140 | Course segment GPS |
| Super-G | 120-130 | Course segment |
| Giant slalom | 60-80 | Turn technical |
| Speed skiing | 255+ | Straight Chabrières |


## Appendix K. Motorcycle and car track vs absolute

| Venue type | Peak km/h class | Limit |
| --- | --- | --- |
| F1 straight | 340-360 | Drag + rules |
| Bonneville motorcycle | 400+ | Streamliner |
| Public road legal hypercar | 400-450 claimed | Tire / aero |
| LSR jet car | 1228 | FIA absolute land |


## Appendix L. Parachute deployment speed windows

| Phase | Speed | Risk |
| --- | --- | --- |
| Exit to accelerate | 0-60 m/s | Stability |
| Terminal belly | ~55 m/s | Normal track |
| Deployment opening | Design 50-60 m/s typical | Shock load on canopy |
| High-speed opening | Specialized canopies | Higher g opening |


## Appendix M. Zip line engineering sketch


```
Tension T rises with span and load; rider speed set by height drop minus friction.
v_end ≈ √(2 g Δh_eff - friction work/m)
Brake mandatory before terminal platform; emergency arrest systems rated for approach speed.
```

Tourism lines cap speed for insurance; competition lines higher but rare.




## Appendix N. Swinging (playground) peak speed estimate

| Release height 1 m | v_bottom ≈ 4.4 m/s (16 km/h) |

| Release height 2 m | v_bottom ≈ 6.3 m/s (23 km/h) |

| Release height 3 m | v_bottom ≈ 7.7 m/s (28 km/h) |

| Release height 4 m | v_bottom ≈ 8.9 m/s (32 km/h) |

| Release height 5 m | v_bottom ≈ 9.9 m/s (36 km/h) |



## Appendix O. Spacefall velocity phases (crew capsule)

| Phase | Speed order | Human feel |
| --- | --- | --- |
| Orbit | 28,000 km/h | Zero-g, no wind |
| Entry interface | Still orbital class | G builds, plasma |
| Peak heating | High dynamic pressure | Sustained g |
| Parachute / splash | <50 m/s vertical | Jerk moderated |


## Appendix P. 2025-26 news digest (speed-relevant)


| Date | Event |
|---|---|
| Dec 2024 | Talon-A2 first Mach 5+ recoverable flight (Stratolaunch) |
| Mar 2025 | Talon-A2 second Mach 5+ flight |
| May 2025 | DoD / TRMC reusable hypersonic announcement |
| Sep 2025 | Talon-A third Mach 5+ flight |
| 28 Oct 2025 | X-59 first flight |
| Mar 2026 | Simon Billy world champs 252.10 km/h Vars |
| 3 Apr 2026 | Greggio 248.270 km/h women WR |
| 4 Apr 2026 | Billy 251.22 km/h best run Speed Masters 2026 |
| 5 Jun 2026 | X-59 first supersonic ~Mach 1.1 |
| Jun 2026 | FAA supersonic NPRM proposed |
| 30 Jun 2026 | DOT/FAA public supersonic announcement |
| Mar 2026 | Talon-A3 MDA FEX-04 |
| Jul 2026 | Stratolaunch 10+ hypersonic flights milestone |



## Appendix Q. Propulsion efficiency vs speed (qualitative)

| Speed band | Best engine type | Why |
| --- | --- | --- |
| <40 km/h | Muscle / electric motor | Low power need |
| 40-200 km/h | ICE / EV | Rolling + aero mix |
| 200-500 km/h | High-power ICE / jet assist | Cube law bites |
| 500-1228 km/h | Jet / rocket hybrid LSR | Thrust >> drag peak |
| Mach 1-3 | Turbojet / ramjet | Compressibility managed |
| Mach 3+ | Ramjet / scramjet / rocket | Heat and intake |


## Appendix R. Material temperature hints (order of magnitude)

| Component | Max use temp class | Speed link |
| --- | --- | --- |
| Aluminum structure | ~150-200°C sustained | LSR wheel |
| Titanium hot section | ~600°C | Jet engine |
| Carbon epoxy | ~150°C glass transition | Aero moldings |
| Inconel | ~1000°C | Turbine blades |
| Ablative PICA | Transient thousands °C | Capsule heat shield |


## Appendix S. Instability checklist for designers

1. **Flutter:** Mass balance, stiffen, limit V_NE

2. **Dutch roll:** Yaw damper

3. **Porpoise:** Aero balance, damping

4. **Wheel shimmy:** Geometry, damper

5. **Snake at LSR:** Fin area, crosswind abort

6. **Shock stall:** Intake geometry, schedule



## Appendix T. Pendulum period examples

| Length 1 m | Period 2.01 s |

| Length 2 m | Period 2.84 s |

| Length 4 m | Period 4.01 s |

| Length 10 m | Period 6.34 s |



## Appendix U. Relativity sanity for fast probes

| 11 km/s | γ = 1.000000000673 |

| 30 km/s | γ = 1.000000005007 |

| 635 km/s | γ = 1.000002243249 |

| 1000 km/s | γ = 1.000005563297 |

| 10000 km/s | γ = 1.000556789705 |



## Appendix V. Master timeline duplicate (land water air space) for sortable scan

| Decade | Land | Water/Air | Space |
| --- | --- | --- | --- |
| 1900s | See Part A | Records evolve by mode | Historical cluster |
| 1910s | See Part A | Records evolve by mode | Historical cluster |
| 1920s | See Part A | Records evolve by mode | Historical cluster |
| 1930s | See Part A | Records evolve by mode | Historical cluster |
| 1940s | See Part A | Records evolve by mode | Historical cluster |
| 1950s | See Part A | Records evolve by mode | Historical cluster |
| 1960s | See Part A | Records evolve by mode | Historical cluster |
| 1970s | See Part A | Records evolve by mode | Historical cluster |
| 1980s | See Part A | Records evolve by mode | Historical cluster |
| 1990s | See Part A | Records evolve by mode | Historical cluster |
| 2000s | See Part A | Records evolve by mode | Historical cluster |
| 2010s | See Part A | Records evolve by mode | Historical cluster |
| 2020s | See Part A | Records evolve by mode | Historical cluster |


## Appendix W. Glossary (speed and measurement)

- **Airspeed:** Speed relative to air mass; IAS vs TAS

- **Ground speed:** Speed over ground; wind affects aircraft

- **Calibrated airspeed:** Instrument corrected for position error

- **Mach number:** Ratio to local speed of sound

- **Dynamic pressure:** q = ½ ρ v²

- **V_NE:** Never-exceed airspeed for aircraft

- **LSR:** Land Speed Record under FIA rules

- **TAS:** True airspeed

- **IAS:** Indicated airspeed

- **FAI:** Fédération Aéronautique Internationale

- **FIA:** Fédération Internationale de l'Automobile

- **FIS:** International Ski Federation

- **IHPVA:** Human Powered Vehicle Association

- **SCRAM:** Supersonic combustion ramjet

- **Staging:** Rocket dropping mass to accelerate

- **Boost-glide:** Hypersonic lift segment

- **Hohmann transfer:** Efficient orbit change

- **Perigee:** Closest approach in orbit

- **Apogee:** Farthest point

- **Stagnation point:** Where flow velocity relative to body is zero

- **Boundary layer:** Thin slow region near surface

- **Wave drag:** Supersonic shock-related drag

- **Induced drag:** Drag from producing lift

- **Parasite drag:** Form + friction drag

- **Rolling resistance:** Wheel deformation losses

- **Coefficient of drag:** C_D dimensionless

- **Lift coefficient:** C_L dimensionless

- **Load factor:** Acceleration in g units

- **Jerk:** Rate of change of acceleration

- **Ratified:** Approved by governing body

- **Unratified:** Claimed but not official



## Appendix X. World Athletics sprint and relay marks (selected ratified)

| Event | Mark | Athlete | Year | Avg speed note |
| --- | --- | --- | --- | --- |
| 100 m | 9.58 s | Usain Bolt | 2009 | 10.44 m/s avg |
| 200 m | 19.19 s | Usain Bolt | 2009 | 10.42 m/s avg |
| 400 m | 43.03 s | Wayde van Niekerk | 2016 | 9.30 m/s avg |
| 800 m | 1:40.91 | David Rudisha | 2012 | 7.92 m/s avg |
| 1500 m | 3:26.00 | Hicham El Guerrouj | 1998 | 7.28 m/s avg |
| Mile | 3:43.13 | Hicham El Guerrouj | 1999 | 7.22 m/s avg |
| 5000 m | 12:35.36 | Joshua Cheptegei | 2020 | 6.62 m/s avg |
| 10000 m | 26:11.00 | Joshua Cheptegei | 2020 | 6.38 m/s avg |
| 100 m women | 10.49 s | Florence Griffith-Joyner | 1988 | Wind legal debate historical |
| 100 m women | 10.54 s | Sha'Carri Richardson | 2023 | Post-2023 elite cluster |
| Marathon men | 2:00:35 | Kelvin Kiptum | 2023 | 5.88 m/s avg |
| Marathon women | 2:09:56 | Ruth Chepngetich | 2024 | 5.46 m/s avg |
| 4×100 m relay | 36.84 s | Jamaica | 2012 | Team |


## Appendix Y. Rail and maglev speed (representative)

| Year | Train | Speed | Notes |
| --- | --- | --- | --- |
| 1938 | LNER Mallard | 202 km/h | Steam record UK |
| 1955 | SNCF CC 7107 | 331 km/h | Test |
| 1964 | Shinkansen 0 series | 210 km/h service | Japan |
| 1981 | TGV | 260 km/h service | France |
| 1990 | TGV Atlantique | 515.3 km/h | Test unmodified |
| 2003 | Shinkansen MLX01 | 581 km/h | Maglev test |
| 2015 | JR SCMaglev | 603 km/h | Test record |
| 2026 | Commercial HSR service | 320-350 km/h typical | China / Europe / Japan |


## Appendix Z. Swimming pool world records (long course, selected Oct 2026)

| Event | Mark band | Reference name | Notes |
| --- | --- | --- | --- |
| 50 m free M | ~20.9 s class | César Cielo era 20.91 | Sprint |
| 100 m free M | ~46.8 s class | Pan Zhanle 46.86 (2024) | WR cluster |
| 200 m free M | 1:42.00 | Paul Biedermann | 2009 |
| 400 m free M | ~3:40 class | Sun Yang era | Distance |
| 1500 m free M | ~14:30 class | Katie Ledecky holds many WRs women side |
| 50 m free W | ~23.6 s class | Sarah Sjöström era | Sprint |
| 100 m free W | ~51.7 s class | Various 2020s | Sprint |
| 100 m fly M | ~49.4 s class | Phelps / Dressel eras | Stroke |


## Appendix AA. Production and race aircraft speed snapshot

| Aircraft | Speed km/h | Year | Role |
| --- | --- | --- | --- |
| Wright Flyer | 59 | 1903 | First flight |
| Spitfire Mk IX | 710 | 1944 | WWII fighter |
| P-51 Mustang | 703 | 1944 | Escort |
| Me 262 | 870 | 1944 | Jet WWII |
| F-86 Sabre | 1100 | 1950 | Korean war jet |
| F-104 Starfighter | 2120 | 1958 | Mach 2 class |
| Concorde | 2180 | 1976 | Cruise supersonic pax |
| Boeing 747 | 988 | 1970 | Cruise ~Mach 0.85 |
| Boeing 787 | 954 | 2010 | Cruise |
| A380 | 945 | 2005 | Cruise |
| F-16 | 2120 | 1978 | Fighter |
| F-22 | 2410 | 2005 | Supercruise class |
| F-35 | 1960 | 2015 | Cruise max published approx |
| MiG-25 | 3020 | 1964 | Recon speed class |
| SR-71 Blackbird | 3529 | 1976 | Air-breathing record class |
| XB-70 Valkyrie | 3300 | 1966 | Mach 3 bomber test |
| X-59 Quesst | 1147 | 2026 | Mach 1.1 first supersonic (~713 mph NASA) |
| X-59 target | 1480 | 2026 | Mach 1.4 planned profile |
| Bell X-1 | 1475 | 1947 | Mach 1 |
| X-15 | 7274 | 1967 | Rocket plane |
| Space Shuttle | 28000 | 1981 | Orbital class km/h |
| Cessna 172 | 302 | 1956 | Trainer cruise |
| Piper Cub | 185 | 1938 | General aviation |
| Red Bull air race plane | 370 | 2000s | Course limited |


## Appendix AB. Human-powered vehicle and cycling records

| Category | Speed | Name / era | Status |
| --- | --- | --- | --- |
| Hour record UCI | ~56 km/h avg | Filippo Ganna era 2022+ | Track |
| Hour recumbent IHPVA | ~105 km/h class | Francesco Russo / Whittingham history | HPV |
| 200 m flying start HPV | ~133 km/h | Sam Whittingham | Flat desert |
| Tour de France stage avg | ~45 km/h | Modern flat stages | Drafting peloton |
| Downhill MTB | ~227 km/h claim | Eric Barone 2017 | Unratified extreme |
| BMX | ~55 km/h | Track sprint | Short |


## Appendix AC. Apollo lunar mission Earth-relative peak speeds (return)

| Mission | Peak speed order | Notes | Year |
| --- | --- | --- | --- |
| Apollo 8 | ~38,000 km/h class | First lunar orbit crew | 1968 |
| Apollo 10 | **39,897 km/h** | Fastest crewed Earth-relative widely cited | 1969 |
| Apollo 11 | ~39,000 km/h class | Landing mission return | 1969 |
| Apollo 12 | Similar band | Second landing | 1969 |
| Apollo 13 | Return survival | Free return | 1970 |
| Apollo 17 | Last landing return | 1972 | Similar class |
| Artemis I | Uncrewed | 2022 | Precursor telemetry |
| Artemis II | Planned crew | Not flown Oct 2026 | Expected **slower peak than Apollo 10** in planning docs |


## Appendix AD. Parker Solar Probe speed milestones


| Flyby era | Perihelion speed order | Notes |
|---|---|---|
| Early Venus gravity assists | Rising each orbit | NASA mission |
| 2024 perihelion class | **~635 km/s** (~2.29 M km/h) | Fastest human-made object near Sun |
| Oct 2026 | Same mission ongoing | Further assists may raise v slightly |

Speed is heliocentric, not "how fast astronauts feel" (uncrewed).




## Appendix AE. ThrustSSC and LSR engineering notes


| Parameter | ThrustSSC value / note |
|---|---|
| Driver | Andy Green (RAF) |
| Date | 15 October 1997 |
| Average two-way | **763.035 mph** (1,228 km/h) |
| Engine | Two Rolls-Royce Spey turbofans from Phantom |
| Thrust class | ~100 kN per side order |
| Wheel | Solid aluminum, no tire |
| Track | Black Rock Desert, Nevada |
| Supersonic | First LSR through sound barrier |
| Next target | Projects since 1997; none ratified faster Oct 2026 |

Stopping distance and parachutes/brakes equally critical; Green had prior Thrust2 experience.




## Appendix AF. SR-71 operational speed facts


| Fact | Detail |
|---|---|
| Crew | Pilot + RSO |
| Cruise | Mach 3.2 class high altitude |
| Record | **3,529 km/h** (2,193 mph) 28 July 1976 |
| Limit | Skin temperature, engine unstart, structural |
| Air-breathing | J58 with bleed bypass; not a rocket |
| Retired | USAF 1998; NASA test beds later |

Pilot reports: turn at full speed required careful bank to avoid inlet unstart.




## Appendix AG. FAA supersonic NPRM 2026 (summary bullets)


| Topic | Proposed direction (Jun 2026 NPRM) |
|---|---|
| Overland ban | Move from blanket prohibition toward **noise-based** certification |
| Sonic boom | Limit overpressure at surface (NPRM cites 0.11 psf class for low-boom path) |
| X-59 data | NASA Quesst community response tests inform acceptable thump levels |
| Timeline | Final rule target **mid-2027** per FAA public statements |
| LTO noise | Separate rule planned for takeoff/landing noise |
| Executive Order | EO 14304 cited in FAA supersonic page |

Not final law as of 16 Oct 2026; comment period and revisions may change numbers.




## Appendix AH. Stratolaunch Talon-A flight log (selected)

| Date | Vehicle | Result | Program |
| --- | --- | --- | --- |
| Dec 2024 | Talon-A2 | Mach 5+ recoverable | First reusable hypersonic milestone |
| Mar 2025 | Talon-A2 | Mach 5+ second flight | TRMC MACH-TB |
| May 2025 | Press release | Reuse demonstrated | DoD statement |
| Sep 2025 | TA-2 | Third Mach 5+ flight | Aviation Week |
| Mar 2026 | Talon-A3 | MDA FEX-04 | Higher release altitude profile |
| Jul 2026 | Fleet | 10+ hypersonic flights | Company milestone |


## Appendix AI. Speed skiing chronology Vars

| Date | Event | Mark | Venue |
| --- | --- | --- | --- |
| 2006 | Les Arcs era | 200+ km/h women cluster | FIS history |
| 2013 | Greggio 247.083 | Women WR | Vars |
| 2016 | Greggio retains | 247.083 ratified era | Vars |
| 2023 | Billy 255.500 | Men WR first >255 | Vars |
| Mar 2026 | Billy 252.10 | World Champs | Vars |
| Apr 2026 | Greggio 248.270 | Women WR | Vars |
| Apr 2026 | Billy 251.22 | Best run not WR | Vars Speed Masters |


## Appendix AJ. Skydiving speed record table

| Mode | Speed | Notes |
| --- | --- | --- |
| Formation belly | ~200 km/h | Typical group |
| Head-down FS | ~400 km/h | Competition |
| Speed skydiving WR class | ~500+ km/h | Specialized suit/helmet |
| Felix Baumgartner | 1,357 km/h | 2012 Red Bull Stratos |
| Alan Eustace | 1,323 km/h | 2014 Google balloon jump |


## Appendix AK. Water speed beyond Warby


Ken Warby **511 km/h** (1978) Spirit of Australia still FIA water record Oct 2026. Jet boats approach but salt water, cavitation, and fatality risk stop casual attempts. Propeller tip speed and ventilation bind.




## Appendix AL. Glider and sailplane records (FAI classes)

| Record type | Value band | Notes |
| --- | --- | --- |
| Absolute distance | 3,000+ km | Modern wave season |
| Speed over out-and-return 500 km | Class records ~200+ km/h | Weather dependent |
| Gain of height | 15,000+ m class | Wave lift |
| Study reference | PerfectGlider | ../Vehicle/PerfectGlider/Index.md |


## Appendix AM. Zip line world claims (tourism vs sport)

| Type | Speed | Safety |
| --- | --- | --- |
| Typical adventure | 50-60 km/h | Brake before platform |
| Longest lines | Lower avg, high peak | Sag physics |
| Extreme claims | 120+ km/h | Often unverified; harness and brake rated |


## Appendix AN. Coaster and thrill ride speed

| Ride | Speed | Region |
| --- | --- | --- |
| Formula Rossa | ~240 km/h | Ferrari World UAE |
| Kingda Ka | ~206 km/h | Six Flags |
| Top Thrill 2 | ~190 km/h class | Refurb era |
| Swing ride pendulum | ~100 km/h class | Amusement pendulum |


## Appendix AO. Part B supplement: viscosity and drag regime


Dynamic viscosity μ for air ~1.8×10⁻⁵ Pa·s at 15°C. Reynolds number Re = ρ v L / μ.

| Body length L | v = 10 m/s Re | v = 100 m/s Re |
|---|---|---|
| 1 m human | 6.8×10⁵ | 6.8×10⁶ |
| 4 m car | 2.7×10⁶ | 2.7×10⁷ |
| 30 m aircraft | 2.0×10⁷ | 2.0×10⁸ |

Turbulent boundary layers dominate drag at operational Re.




## Appendix AP. Part B supplement: rocket equation sketch


```
Δv = v_e ln(m0/mf)
```
| Mission idea | Δv order | Implication |
|---|---|---|
| LEO | ~9.4 km/s | Mass ratio heavy |
| Lunar return | Adds ~6 km/s class | Multi-stage |
| Earth escape | ~11.2 km/s | Deep space |

Apollo trans-Earth injection produced the **39,897 km/h** peak relative to Earth as combined orbital energy and trajectory geometry, not foot speed.




## Appendix AQ. Part D supplement: energy cost of running


Metabolic power at marathon pace ~400 W; sprint peak >2000 W brief. Speed limited by aerobic vs anaerobic clearance. See `Stamina.md` for Terra SP mapping; Earth invent only here.

| Pace | Speed m/s | VO2 proxy |
|---|---|---|
| Walk | 1.4 | Low |
| Jog | 3 | Moderate |
| 5k race | 5.5 | High |
| Sprint | 12 | Peak anaerobic |




## Appendix AR. Part E supplement: brake systems vs speed


| Brake | Effective speed band | Limit |
|---|---|---|
| Rim brake bicycle | <60 km/h descents | Heat fade |
| Disc automotive | 200+ km/h repeated | Rotor temperature |
| Carbon carbon aircraft | Landing rollout | Wear |
| Parachute LSR | 800+ km/h | Deployment timing |
| Thrust reverse jet | Taxi | Not emergency stop at max speed |

Cross-link: `../Vehicle/Brakes.md`




## Appendix AS. Part F supplement: road design speeds


| Road class | Design speed km/h | Human factor |
|---|---|---|
| Urban local | 30-50 | Pedestrian RT |
| Rural highway | 80-100 | Surprise hazard 1.5 s |
| Autobahn / motorway | 120-130 legal | Closing speed |
| Track day | 250+ | Barriers and runoff |

Preview time D/v ties to `SpeedPerception.md`.




## Appendix AT. Part H supplement: timing technology


| Era | Sprint timing | Error band |
|---|---|---|
| Hand timing | Stopwatch | ±0.1-0.2 s |
| Fully automatic ( FAT ) | Photo finish | ±0.001 s class |
| Wind gauge | Laser / ultrasonic | ±0.1 m/s |
| GPS consumer | 1 Hz | Unratified speed skiing |
| Radar speed gun | Doppler | FIS / police calibration |




## Appendix AU. Combat cross-reference (not Earth record)


Story combat reaction uses INT and `SpeedVsIntellect.md`. This file's Earth records do **not** set Roland's spell or bolt speeds. Use felt speed from `SpeedPerception.md` when writing flight scenes.




## Appendix AV. Mode narrative: parkour expanded


Parkour (art du déplacement) optimizes **time-to-cross** an environment, not peak km/h on a track. Wall runs convert gravitational potential to horizontal impulse. Precision landings use roll to increase stop distance (see `Falling.md`). Elite traceurs on sprint segments approach **8-9 m/s** but rarely hold it. Obstacle density forces stops; average crossing speed over 1 km urban course may sit **3-5 m/s**.

Safety: impact training, ankle conditioning, and route scouting mirror wingsuit scouting at lower speeds.




## Appendix AW. Mode narrative: ice skating expanded


Long-track speed skating 500 m times ~33 s imply **~15 m/s** average with higher peak in straights. Ice friction μ is tiny (~0.001-0.005); limit is air drag and corner crossovers. Short-track packs drafting and collision risk. Inline downhill can exceed **100 km/h** on mountain roads with aerodynamic tuck; ratification rare.




## Appendix AX. Mode narrative: motorcycles expanded


MotoGP GPS peaks ~360 km/h. Isle of Man TT road course peaks similar with zero runoff forgiveness. Streamliner Bonneville motorcycles exceed **400 km/h** in FIM classes. Rider drag is large fraction; tuck essential. Wheelie and front lift bind acceleration at high power.




## Appendix AY. Mode narrative: spacefall expanded


Crew capsules enter at **~11 km/s** order relative to atmosphere interface, not the Apollo 10 **39,897 km/h** figure (which is trans-Earth in space). Re-entry converts orbital energy to heat in shock layer. Human limits: sustained g during deceleration, not the orbital speed itself. Heat shield and g-seat orientation (`../Vehicle/Positions.md`, `GForceTolerance.md`). Radiation environment: `../../Space/Radiation/`.

Uncrewed sample return and Starship tests continue thermal protection research in 2025-26.




## Appendix AZ. Relativity and GPS (operational speed note)


Orbital clocks run faster in weaker gravity and slower due to speed (Special + General relativity). GPS satellites include relativistic corrections ~38 μs/day equivalent. This does not change human speed records but explains why "exactly c" never appears in transport tables.




## Appendix BA. Land speed micro-history (sample years)

| Year | km/h | Vehicle | Status |
| --- | --- | --- | --- |
| 1930 | 245 | Campbell Sunbeam | Historical LSR cluster |
| 1935 | 484 | Campbell Blue Bird | Historical LSR cluster |
| 1947 | 634 | John Cobb Railton | Historical LSR cluster |
| 1963 | 648 | Campbell CN7 | Historical LSR cluster |
| 1964 | 648 | Art Arfons Green Monster | Historical LSR cluster |
| 1965 | 966 | Craig Breedlove Spirit of America | Historical LSR cluster |
| 1970 | 1014 | Gary Gabelich Blue Flame | Historical LSR cluster |
| 1983 | 1019 | Richard Noble Thrust2 | Historical LSR cluster |
| 1997 | 1228 | Andy Green ThrustSSC | Historical LSR cluster |


## Appendix BB. Stagnation temperature full ladder (c_p = 1005 J/kg/K, T_static = 288 K)

| v km/h | T °C approx | T K approx |
| --- | --- | --- |
| 100 | 15 | 288 |
| 200 | 17 | 290 |
| 300 | 18 | 291 |
| 400 | 21 | 294 |
| 500 | 25 | 298 |
| 600 | 29 | 302 |
| 700 | 34 | 307 |
| 800 | 40 | 313 |
| 900 | 46 | 319 |
| 1000 | 53 | 326 |
| 1100 | 61 | 334 |
| 1200 | 70 | 343 |
| 1300 | 80 | 353 |
| 1400 | 90 | 363 |
| 1500 | 101 | 374 |
| 1600 | 113 | 386 |
| 1700 | 126 | 399 |
| 1800 | 139 | 412 |
| 1900 | 154 | 427 |
| 2000 | 169 | 442 |
| 2100 | 184 | 457 |
| 2200 | 201 | 474 |
| 2300 | 218 | 491 |
| 2400 | 236 | 509 |
| 2500 | 255 | 528 |
| 2600 | 275 | 548 |
| 2700 | 295 | 568 |
| 2800 | 316 | 589 |
| 2900 | 338 | 611 |
| 3000 | 360 | 633 |
| 3100 | 384 | 657 |
| 3200 | 408 | 681 |
| 3300 | 433 | 706 |
| 3400 | 459 | 732 |
| 3500 | 485 | 758 |


## Appendix BC. Drag power at v = 300 km/h for many C_D A values

| C_D A m² | kW at 300 km/h | hp approx |
| --- | --- | --- |
| 0.2 | 69 | 0 |
| 0.25 | 87 | 0 |
| 0.3 | 104 | 0 |
| 0.35 | 122 | 0 |
| 0.4 | 139 | 0 |
| 0.45 | 156 | 0 |
| 0.5 | 174 | 0 |
| 0.55 | 191 | 0 |
| 0.6 | 208 | 0 |
| 0.7 | 243 | 0 |
| 0.8 | 278 | 0 |
| 0.9 | 312 | 0 |
| 1.0 | 347 | 0 |
| 1.2 | 417 | 1 |
| 1.5 | 521 | 1 |
| 2.0 | 694 | 1 |


## Appendix BD. Centripetal acceleration table (various v and r)

| v km/h | radius m | g load |
| --- | --- | --- |
| 50 | 10 | 1.97 |
| 50 | 25 | 0.79 |
| 50 | 50 | 0.39 |
| 50 | 100 | 0.20 |
| 50 | 200 | 0.10 |
| 50 | 500 | 0.04 |
| 100 | 10 | 7.87 |
| 100 | 25 | 3.15 |
| 100 | 50 | 1.57 |
| 100 | 100 | 0.79 |
| 100 | 200 | 0.39 |
| 100 | 500 | 0.16 |
| 150 | 10 | 17.70 |
| 150 | 25 | 7.08 |
| 150 | 50 | 3.54 |
| 150 | 100 | 1.77 |
| 150 | 200 | 0.88 |
| 150 | 500 | 0.35 |
| 200 | 10 | 31.46 |
| 200 | 25 | 12.58 |
| 200 | 50 | 6.29 |
| 200 | 100 | 3.15 |
| 200 | 200 | 1.57 |
| 200 | 500 | 0.63 |
| 250 | 10 | 49.16 |
| 250 | 25 | 19.66 |
| 250 | 50 | 9.83 |
| 250 | 100 | 4.92 |
| 250 | 200 | 2.46 |
| 250 | 500 | 0.98 |
| 300 | 10 | 70.79 |
| 300 | 25 | 28.32 |
| 300 | 50 | 14.16 |
| 300 | 100 | 7.08 |
| 300 | 200 | 3.54 |
| 300 | 500 | 1.42 |


## Appendix BE. Free-fall speed vs height (no drag)

| h m | v m/s | v km/h |
| --- | --- | --- |
| 5 | 9.9 | 36 |
| 10 | 14.0 | 50 |
| 15 | 17.2 | 62 |
| 20 | 19.8 | 71 |
| 25 | 22.1 | 80 |
| 30 | 24.3 | 87 |
| 35 | 26.2 | 94 |
| 40 | 28.0 | 101 |
| 45 | 29.7 | 107 |
| 50 | 31.3 | 113 |
| 55 | 32.8 | 118 |
| 60 | 34.3 | 124 |
| 65 | 35.7 | 129 |
| 70 | 37.1 | 133 |
| 75 | 38.4 | 138 |
| 80 | 39.6 | 143 |
| 85 | 40.8 | 147 |
| 90 | 42.0 | 151 |
| 95 | 43.2 | 155 |
| 100 | 44.3 | 159 |
| 105 | 45.4 | 163 |
| 110 | 46.5 | 167 |
| 115 | 47.5 | 171 |
| 120 | 48.5 | 175 |
| 125 | 49.5 | 178 |
| 130 | 50.5 | 182 |
| 135 | 51.5 | 185 |
| 140 | 52.4 | 189 |
| 145 | 53.3 | 192 |
| 150 | 54.2 | 195 |
| 155 | 55.1 | 199 |
| 160 | 56.0 | 202 |
| 165 | 56.9 | 205 |
| 170 | 57.8 | 208 |
| 175 | 58.6 | 211 |
| 180 | 59.4 | 214 |
| 185 | 60.2 | 217 |
| 190 | 61.1 | 220 |
| 195 | 61.9 | 223 |
| 200 | 62.6 | 226 |
| 205 | 63.4 | 228 |
| 210 | 64.2 | 231 |
| 215 | 64.9 | 234 |
| 220 | 65.7 | 237 |
| 225 | 66.4 | 239 |
| 230 | 67.2 | 242 |
| 235 | 67.9 | 244 |
| 240 | 68.6 | 247 |
| 245 | 69.3 | 250 |
| 250 | 70.0 | 252 |
| 255 | 70.7 | 255 |
| 260 | 71.4 | 257 |
| 265 | 72.1 | 260 |
| 270 | 72.8 | 262 |
| 275 | 73.5 | 264 |
| 280 | 74.1 | 267 |
| 285 | 74.8 | 269 |
| 290 | 75.4 | 272 |
| 295 | 76.1 | 274 |
| 300 | 76.7 | 276 |
| 305 | 77.4 | 278 |
| 310 | 78.0 | 281 |
| 315 | 78.6 | 283 |
| 320 | 79.2 | 285 |
| 325 | 79.9 | 287 |
| 330 | 80.5 | 290 |
| 335 | 81.1 | 292 |
| 340 | 81.7 | 294 |
| 345 | 82.3 | 296 |
| 350 | 82.9 | 298 |
| 355 | 83.5 | 300 |
| 360 | 84.0 | 303 |
| 365 | 84.6 | 305 |
| 370 | 85.2 | 307 |
| 375 | 85.8 | 309 |
| 380 | 86.3 | 311 |
| 385 | 86.9 | 313 |
| 390 | 87.5 | 315 |
| 395 | 88.0 | 317 |
| 400 | 88.6 | 319 |
| 405 | 89.1 | 321 |
| 410 | 89.7 | 323 |
| 415 | 90.2 | 325 |
| 420 | 90.8 | 327 |
| 425 | 91.3 | 329 |
| 430 | 91.9 | 331 |
| 435 | 92.4 | 333 |
| 440 | 92.9 | 334 |
| 445 | 93.4 | 336 |
| 450 | 94.0 | 338 |
| 455 | 94.5 | 340 |
| 460 | 95.0 | 342 |
| 465 | 95.5 | 344 |
| 470 | 96.0 | 346 |
| 475 | 96.5 | 348 |
| 480 | 97.0 | 349 |
| 485 | 97.5 | 351 |
| 490 | 98.0 | 353 |
| 495 | 98.5 | 355 |
| 500 | 99.0 | 357 |


## Appendix BF. Terminal velocity vs mass (C_D A = 1.0 m², ρ = 1.225)

| 50 kg | v_t = 28.3 m/s (102 km/h) |

| 60 kg | v_t = 31.0 m/s (112 km/h) |

| 70 kg | v_t = 33.5 m/s (121 km/h) |

| 80 kg | v_t = 35.8 m/s (129 km/h) |

| 90 kg | v_t = 38.0 m/s (137 km/h) |

| 100 kg | v_t = 40.0 m/s (144 km/h) |

| 110 kg | v_t = 42.0 m/s (151 km/h) |

| 120 kg | v_t = 43.8 m/s (158 km/h) |

| 130 kg | v_t = 45.6 m/s (164 km/h) |

| 140 kg | v_t = 47.4 m/s (170 km/h) |

| 150 kg | v_t = 49.0 m/s (176 km/h) |



## Appendix BG. Mach number at altitude (ISA sketch, v in km/h to Mach)


| Altitude km | a approx m/s | 1000 km/h = Mach |
|---|---|---|
| 0 | 340 | 0.82 |
| 5 | 320 | 0.87 |
| 11 | 295 | 0.94 |
| 15 | 295 | 0.94 |
| 20 | 295 | 0.94 |
| 25 | 300 | 0.93 |

X-59 mission profile **55,000 ft (~16.8 km)** uses low-boom shape at **Mach 1.4** for community tests.




## Appendix BH. Human limits extended table (age and sex classes)

| Population | 100 m class | Marathon class | Notes |
| --- | --- | --- | --- |
| M open WR | 9.58 s | 2:00:35 | Bolt / Kiptum |
| W open WR | 10.49 s (disputed wind) | 2:09:56 | Flo-Jo / Chepngetich |
| Masters 40+ | ~10.8 s class | 2:20+ class | Age graded |
| U18 boys | ~10.4 s class | Not distance peak | Development |
| Wheelchair racing | 14.00 s class 100 m | 1:18:25 marathon class | Separate WA classes |


## Appendix BI. Animal speed comparison (land)

| Species | Speed | Notes |
| --- | --- | --- |
| Human sprint | 12 m/s | Elite |
| Horse | 18 m/s | Gallop |
| Greyhound | 20 m/s | Sprint |
| Cheetah | 29 m/s | Short burst |
| Ostrich | 12 m/s | Sustained runner bird |
| Kangaroo | 14 m/s | Hop |


## Appendix BJ. Sailing and wind-powered water speed

| Craft | Speed order | Notes |
| --- | --- | --- |
| Trade wind clipper avg | 15-20 km/h | Historical routes |
| Modern foiling sail WC | 50+ km/h | Moth / AC75 class |
| Land yacht record | 200+ km/h | Dry lake |
| Ice yacht | 150+ km/h | Frozen lake |
| Kitewing ski | 80+ km/h | Wind dependent |


## Appendix BK. Submarine and underwater human speed

| Mode | Speed | Notes |
| --- | --- | --- |
| SEAL swimmer DPV | 5-10 km/h | Battery diver propulsion |
| Submarine fast | ~65 km/h class published | Military approx |
| Torpedo | 100+ km/h | Not human |
| Freedive horizontal | 1-2 m/s | Human fin |


## Appendix BL. Elevator and vertical transport speed

| System | Speed | Notes |
| --- | --- | --- |
| Otis skyscraper | 20-30 km/h | Comfort and ear pressure |
| Taipei 101 era | ~60 km/h class | High rise |
| Mine hoist | Variable | Not passenger sport |
| Eiffel Tower elevator historical | Low | Tourism |


## Appendix BM. Escalator and moving walkway


Typical **0.5-0.65 m/s** (1.8-2.3 km/h). Airport walkways add **0.5 m/s** to walking ~1.4 m/s for **~7 km/h** combined. Not speed records but daily human motion band.




## Appendix BN. Typing and fine motor (not locomotion but motion speed)

| Task | Rate | Notes |
| --- | --- | --- |
| Keyboard WPM world class | 150-200+ WPM | Not travel speed |
| Piano trill | 15 notes/s hand | Muscle limit |
| Table tennis smash | 100+ km/h ball | Human initiated |


## Appendix BO. Ball sports projectile speed (human triggered)

| Sport | Object speed | Notes |
| --- | --- | --- |
| Tennis serve | 250+ km/h | Record class |
| Golf drive | 280+ km/h ball | Pro |
| Baseball pitch | 170+ km/h | MLB |
| Jai alai pelota | 300+ km/h claims | Historical |
| Badminton smash | 400+ km/h shuttle | Record class |


## Appendix BP. Internal body motion (not transport)


| Motion | Speed order | Notes |
|---|---|---|
| Nerve impulse | ~120 m/s | Myelinated |
| Blood flow aorta | ~1 m/s peak | Not whole body travel |
| Eye saccade | 300-700°/s | Angular |
| Finger tap | ~10 Hz | RT limited |

Separate from vehicle records; listed so "human motion" is not confused with transport.




## Appendix BQ. Historical foot messenger and cavalry

| Mode | Daily distance | Avg speed |
| --- | --- | --- |
| Roman courier relay | 80-100 km/day | ~4 km/h effective |
| Pony Express | 250 km/day short peak | Relay horses |
| Cavalry march | 40-50 km/day | Sustain |
| Modern ultramarathon 6-day | 300+ km/day | 6-7 km/h sleep deprived |


## Appendix BR. Wind legal and track material (sprint)


World Athletics legal tailwind for records: **+2.0 m/s** max. Over that, mark is not ratified as WR (still race legal). All-weather vs mondo track surfaces affect spike traction; not top speed on ice.




## Appendix BS. FIA land speed classes (conceptual)


| Class idea | Wheel rule | Example |
|---|---|---|
| Wheel-driven | Power to ground via wheel | Goldenrod 657 km/h |
| Jet car | Jet thrust | ThrustSSC |
| Rocket car | Rocket | Bloodhound design |

Ratified LSR absolute peak remains **ThrustSSC** Oct 2026.




## Appendix BT. World Water Speed Record attempts post-Warby

| 1980 | Challengers below 511 km/h | No new ratified mark |

| 1985 | Challengers below 511 km/h | No new ratified mark |

| 1990 | Challengers below 511 km/h | No new ratified mark |

| 1995 | Challengers below 511 km/h | No new ratified mark |

| 2000 | Challengers below 511 km/h | No new ratified mark |

| 2005 | Challengers below 511 km/h | No new ratified mark |

| 2010 | Challengers below 511 km/h | No new ratified mark |

| 2015 | Challengers below 511 km/h | No new ratified mark |

| 2020 | Challengers below 511 km/h | No new ratified mark |

| 2025 | Challengers below 511 km/h | No new ratified mark |



## Appendix BU. Rotorcraft and autogyro

| Type | Speed km/h | Notes |
| --- | --- | --- |
| Westland Lynx 400.87 | 401 | Absolute helicopter about 401 km/h |
| Chinook cruise | 280 | Heavy lift |
| Autogyro record class | 200+ class | Ungoverned niche |


## Appendix BV. Balloon and airship human speed


Balloons move with wind; ground speed equals wind speed. Round-the-world balloon flights exceed **400 km/h** ground speed in jet stream with **zero airspeed** felt inside basket. Airships cruise **100-150 km/h** historical passenger.




## Appendix BW. Crawl, walk, race walk legal limits

| Gait | Speed m/s | Rule |
| --- | --- | --- |
| Race walk 20 km WR pace | 4.36 | One foot on ground visible |
| Power walking | 2.0-2.5 | Recreational |
| Baby crawl | 0.2-0.4 | Development |


## Appendix BX. Climbing speed (vertical)

| Discipline | Speed | Notes |
| --- | --- | --- |
| IFSC speed climb WR | ~6-7 m/s route | 15 m wall |
| El Cap Nose speed record | Hours not m/s | Big wall |
| Stair climb tower racing | 0.5-1 m/s vertical | Empire State run-up |


## Appendix BY. Rowing and paddling

| Boat | Speed | Notes |
| --- | --- | --- |
| Single scull sprint | 20 km/h class | Olympic |
| Kayak sprint 200 m | 22 km/h class | Flat water |
| Outrigger canoe | 15-25 km/h | Pacific tradition |
| Dragon boat | 15 km/h class | Team |


## Appendix BZ. Cross-country skiing (not speed ski)


WC skate sprint peaks **~45 km/h** on flats; downhill sections higher but technical. Distinct from speed skiing straight Chabrières course.




## Appendix CA. Narrative: Part B drag derivation walkthrough


Start from Newton's second law for steady horizontal cruise: thrust T equals drag F_D.

```
F_D = ½ ρ v² C_D A
T = F_D
P = T v = ½ ρ v³ C_D A
```

Hold ρ, C_D, and A constant. Double v: drag quadruples, power **octuples**. That is why ThrustSSC needed jet fighters' engines, not a bigger piston engine.

Rolling term P_roll = C_rr m g v adds linearly in v. At 50 km/h on a car, rolling may be half of drag; at 200 km/h, rolling is often under 10% of total resistive power.

Compressibility: as M rises toward 1, C_D often rises (wave drag). SR-71 operations managed inlet spikes and skin heating simultaneously.

Heat: stagnation temperature estimate adds ΔT ≈ v²/(2 c_p). At Mach 3, ΔT is hundreds of kelvin; structure must survive transient and sustained soak.

Terminal velocity for humans: same drag equation with F_D = m g. Heavier jumper with same posture falls faster (√m dependence). Opening shock when parachute deploys converts kinetic energy over short time; higher deployment speed needs stronger canopy and longer slider stroke.

Orbit speed: circular v = √(μ/r). Lower orbit is faster. Apollo return peak is not "orbital speed" alone but the vector sum during trans-Earth injection and lunar gravity assist geometry.

Relativity: at v/c ≪ 1, Newtonian tables in this file suffice. Parker at 635 km/s still has γ within 1 + 2×10⁻⁶.




## Appendix CB. Narrative: regulating speed in society


Speed limits on roads trade mobility for pedestrian survival time. Aviation noise rules shaped Concorde overland routes. FIS homologation prevents speed skiing on unprofiled slopes. FIA LSR requires two passes and certified timing.

The 2026 FAA supersonic NPRM is a regulatory speed unlock **conditional on noise**, not a blanket Mach number permission. X-59 must prove community acceptable thump before civil routes reopen over land at supersonic cruise.

Sporting bodies disqualify pharmacological enhancement; technology enhancement (spikes, suits) is regulated separately (speed ski suits, swimming supersuit era bans).




## Appendix CC. Duplicate master comparison (extended rows)

| Category | Peak | Reference | Status |
| --- | --- | --- | --- |
| Human sprint (100 m) | 10.44 m/s avg | Usain Bolt 2009 | Ratified |
| Speed ski women | 248.270 km/h | Greggio 2026 | FIS event WR |
| Speed ski men | 255.500 km/h | Billy 2023 | WR; 2026 best 251.22 |
| HPV | ~133 km/h | IHPVA class | Ratified category |
| Land speed record | 1,228 km/h | ThrustSSC 1997 | FIA |
| Water speed record | 511 km/h | Ken Warby 1978 | FIA |
| Helicopter | ~401 km/h | Westland Lynx | FAI class |
| Air-breathing jet crew | 3,529 km/h | SR-71 | Record class |
| Rocket plane crew | 7,274 km/h | X-15 | Historical |
| Crew Earth-relative | 39,897 km/h | Apollo 10 | NASA telemetry |
| Probe heliocentric | ~635 km/s | Parker Solar Probe | NASA |
| X-59 demo | Mach 1.1 | NASA 2026 | Program milestone |
| Talon-A | Mach 5+ | Stratolaunch 2025-26 | Uncrewed test |
| Parker probe | ~635 km/s | NASA 2024 perihelion class | Uncrewed |
| ISS crew ground track | ~27,600 km/h | Low orbit | Crew |
| Maglev test JR | 603 km/h | 2015 | Uncrewed test |
| Warby water | 511 km/h | 1978 | Ratified |
| Talon-A | Mach 5+ | 2025-26 | Uncrewed recoverable |
| Greggio 2026 | 248.270 km/h | Speed ski | FIS event |
| Billy WR | 255.500 km/h | 2023 | Speed ski |
| Bolt 100 m | 10.44 m/s avg | 2009 | WA ratified |


## Appendix CD. Stop distance at g = 4 m/s² (comfortable car brake)

| 30 km/h | 9 m stop at 4 m/s² decel |

| 40 km/h | 15 m stop at 4 m/s² decel |

| 50 km/h | 24 m stop at 4 m/s² decel |

| 60 km/h | 35 m stop at 4 m/s² decel |

| 70 km/h | 47 m stop at 4 m/s² decel |

| 80 km/h | 62 m stop at 4 m/s² decel |

| 90 km/h | 78 m stop at 4 m/s² decel |

| 100 km/h | 96 m stop at 4 m/s² decel |

| 110 km/h | 117 m stop at 4 m/s² decel |

| 120 km/h | 139 m stop at 4 m/s² decel |

| 130 km/h | 163 m stop at 4 m/s² decel |

| 140 km/h | 189 m stop at 4 m/s² decel |

| 150 km/h | 217 m stop at 4 m/s² decel |

| 160 km/h | 247 m stop at 4 m/s² decel |

| 170 km/h | 279 m stop at 4 m/s² decel |

| 180 km/h | 312 m stop at 4 m/s² decel |

| 190 km/h | 348 m stop at 4 m/s² decel |

| 200 km/h | 386 m stop at 4 m/s² decel |

| 210 km/h | 425 m stop at 4 m/s² decel |

| 220 km/h | 467 m stop at 4 m/s² decel |

| 230 km/h | 510 m stop at 4 m/s² decel |

| 240 km/h | 556 m stop at 4 m/s² decel |

| 250 km/h | 603 m stop at 4 m/s² decel |

| 260 km/h | 652 m stop at 4 m/s² decel |

| 270 km/h | 703 m stop at 4 m/s² decel |

| 280 km/h | 756 m stop at 4 m/s² decel |

| 290 km/h | 811 m stop at 4 m/s² decel |

| 300 km/h | 868 m stop at 4 m/s² decel |

| 310 km/h | 927 m stop at 4 m/s² decel |

| 320 km/h | 988 m stop at 4 m/s² decel |

| 330 km/h | 1050 m stop at 4 m/s² decel |



## Appendix CE. Jet and rocket exhaust speed order

| Engine | Exhaust / jet speed order | Use |
| --- | --- | --- |
| Turbofan bypass | 300 m/s class | Airliners |
| Turbojet | 600-1000 m/s | Fighters |
| Rocket vacuum Isp high | 3000-4500 m/s effective | Upper stage |
| Ion thruster | 10-100 km/s exhaust equivalent | Deep space low thrust |


## Appendix CF. Part C mode checklist (one-line each)

- Foot sprint: WA ratified 100 m 9.58 s.

- Marathon: Kiptum 2:00:35 endurance band.

- Race walk: legal gait caps speed.

- Parkour: obstacle time not track v_max.

- Ice skate: low μ, air drag at 15 m/s.

- Alpine ski WC: 130-140 km/h segments.

- Speed ski FIS: Billy 255.5 / Greggio 248.27.

- HPV: IHPVA 133 km/h class.

- LSR: ThrustSSC 1228 km/h.

- MotoGP: 360 km/h GPS.

- Warby water: 511 km/h.

- Sailplane: FAI wave dive ~300 km/h class.

- SR-71: 3529 km/h air-breathing.

- X-59: Mach 1.1 flown Jun 2026.

- Talon-A: Mach 5+ reusable.

- Parachute: Baumgartner 1357 km/h.

- Apollo 10: 39897 km/h crew Earth-relative.

- Artemis II: planned slower peak than Apollo 10.

- Parker: 635 km/s probe.

- Zip line: brake-limited tourism speeds.

- Coaster: 200+ km/h steel.

- Maglev: 603 km/h test.

- Rail Mallard steam: 202 km/h.

- Concorde cruise: 2180 km/h.

- X-15: 7274 km/h rocket plane.

- Helicopter Lynx: 401 km/h.

- FAA NPRM 2026: noise-based supersonic path.



## Appendix CG. Source and status legend


| Label | Meaning |
|---|---|
| Ratified | Governing body published mark |
| Unratified | Measured but not certified |
| Disputed | Wind, timing, or equipment controversy |
| Pending | Attempt announced, not completed |
| Program milestone | Demo flight, not transport WR |
| Earth invent loot | Reference only, not Terra lock |

This file stamped **16 October 2026**. Updates belong in a new status line when refreshed.




## Appendix CH. Year-by-year speed highlights (1900-2026, one row per year)

| Year | Highlight |
| --- | --- |
| 1900 | Incremental transport and sport advances. |
| 1901 | Incremental transport and sport advances. |
| 1902 | Incremental transport and sport advances. |
| 1903 | Wright Flyer first powered flight ~59 km/h. |
| 1904 | Incremental transport and sport advances. |
| 1905 | Incremental transport and sport advances. |
| 1906 | Incremental transport and sport advances. |
| 1907 | Incremental transport and sport advances. |
| 1908 | Incremental transport and sport advances. |
| 1909 | Bleriot cross-Channel; aviation practical. |
| 1910 | Incremental transport and sport advances. |
| 1911 | Incremental transport and sport advances. |
| 1912 | Titanic era steamship ~40 km/h service. |
| 1913 | Incremental transport and sport advances. |
| 1914 | Incremental transport and sport advances. |
| 1915 | Incremental transport and sport advances. |
| 1916 | Incremental transport and sport advances. |
| 1917 | Incremental transport and sport advances. |
| 1918 | Incremental transport and sport advances. |
| 1919 | Incremental transport and sport advances. |
| 1920 | Incremental transport and sport advances. |
| 1921 | Incremental transport and sport advances. |
| 1922 | Incremental transport and sport advances. |
| 1923 | Incremental transport and sport advances. |
| 1924 | Incremental transport and sport advances. |
| 1925 | Incremental transport and sport advances. |
| 1926 | Incremental transport and sport advances. |
| 1927 | Incremental transport and sport advances. |
| 1928 | Incremental transport and sport advances. |
| 1929 | Incremental transport and sport advances. |
| 1930 | Incremental transport and sport advances. |
| 1931 | Incremental transport and sport advances. |
| 1932 | Incremental transport and sport advances. |
| 1933 | Incremental transport and sport advances. |
| 1934 | Incremental transport and sport advances. |
| 1935 | Campbell 484 km/h land. |
| 1936 | Incremental transport and sport advances. |
| 1937 | Incremental transport and sport advances. |
| 1938 | Mallard steam train 202 km/h. |
| 1939 | Incremental transport and sport advances. |
| 1940 | Incremental transport and sport advances. |
| 1941 | Incremental transport and sport advances. |
| 1942 | Incremental transport and sport advances. |
| 1943 | Incremental transport and sport advances. |
| 1944 | Incremental transport and sport advances. |
| 1945 | Incremental transport and sport advances. |
| 1946 | Incremental transport and sport advances. |
| 1947 | Yeager Mach 1; sound barrier broken. |
| 1948 | Incremental transport and sport advances. |
| 1949 | Incremental transport and sport advances. |
| 1950 | Incremental transport and sport advances. |
| 1951 | Incremental transport and sport advances. |
| 1952 | Incremental transport and sport advances. |
| 1953 | Incremental transport and sport advances. |
| 1954 | Stapp rocket sled human deceleration tests. |
| 1955 | Incremental transport and sport advances. |
| 1956 | Incremental transport and sport advances. |
| 1957 | Incremental transport and sport advances. |
| 1958 | Incremental transport and sport advances. |
| 1959 | Incremental transport and sport advances. |
| 1960 | Incremental transport and sport advances. |
| 1961 | Gagarin orbital human. |
| 1962 | Incremental transport and sport advances. |
| 1963 | Incremental transport and sport advances. |
| 1964 | Incremental transport and sport advances. |
| 1965 | Incremental transport and sport advances. |
| 1966 | Incremental transport and sport advances. |
| 1967 | Incremental transport and sport advances. |
| 1968 | Incremental transport and sport advances. |
| 1969 | Apollo 10 peak 39897 km/h; Apollo 11 landing. |
| 1970 | Incremental transport and sport advances. |
| 1971 | Incremental transport and sport advances. |
| 1972 | Incremental transport and sport advances. |
| 1973 | Incremental transport and sport advances. |
| 1974 | Incremental transport and sport advances. |
| 1975 | Incremental transport and sport advances. |
| 1976 | SR-71 record; Concorde service begins. |
| 1977 | Incremental transport and sport advances. |
| 1978 | Warby 511 km/h water record. |
| 1979 | Incremental transport and sport advances. |
| 1980 | Incremental transport and sport advances. |
| 1981 | Incremental transport and sport advances. |
| 1982 | Incremental transport and sport advances. |
| 1983 | Incremental transport and sport advances. |
| 1984 | Incremental transport and sport advances. |
| 1985 | Incremental transport and sport advances. |
| 1986 | Incremental transport and sport advances. |
| 1987 | Incremental transport and sport advances. |
| 1988 | Flo-Jo 100 m 10.49 s (wind scrutiny). |
| 1989 | Incremental transport and sport advances. |
| 1990 | Incremental transport and sport advances. |
| 1991 | Incremental transport and sport advances. |
| 1992 | Incremental transport and sport advances. |
| 1993 | Incremental transport and sport advances. |
| 1994 | Incremental transport and sport advances. |
| 1995 | Incremental transport and sport advances. |
| 1996 | Incremental transport and sport advances. |
| 1997 | ThrustSSC supersonic LSR. |
| 1998 | Incremental transport and sport advances. |
| 1999 | Incremental transport and sport advances. |
| 2000 | Incremental transport and sport advances. |
| 2001 | Incremental transport and sport advances. |
| 2002 | Incremental transport and sport advances. |
| 2003 | Incremental transport and sport advances. |
| 2004 | Incremental transport and sport advances. |
| 2005 | Incremental transport and sport advances. |
| 2006 | Incremental transport and sport advances. |
| 2007 | Incremental transport and sport advances. |
| 2008 | Incremental transport and sport advances. |
| 2009 | Bolt 9.58 s 100 m. |
| 2010 | Incremental transport and sport advances. |
| 2011 | Incremental transport and sport advances. |
| 2012 | Baumgartner balloon jump campaign. |
| 2013 | Incremental transport and sport advances. |
| 2014 | Incremental transport and sport advances. |
| 2015 | JR maglev 603 km/h test. |
| 2016 | Incremental transport and sport advances. |
| 2017 | Incremental transport and sport advances. |
| 2018 | Incremental transport and sport advances. |
| 2019 | Incremental transport and sport advances. |
| 2020 | Incremental transport and sport advances. |
| 2021 | Incremental transport and sport advances. |
| 2022 | Incremental transport and sport advances. |
| 2023 | Billy speed ski 255.5 km/h; Kiptum marathon. |
| 2024 | Parker perihelion speed class ~635 km/s. |
| 2025 | X-59 first flight Oct; Talon-A reuse flights. |
| 2026 | Greggio 248.27; X-59 supersonic; FAA NPRM; Talon 10+ flights. |