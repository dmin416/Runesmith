# Air and Hydraulic Suspension

> Earth reference / invent loot. Not locked law. Caldris ceiling + active nine-part: `Suspension.md`. Era: `../../Tech/Technology.md`. Roads: `Roads.md`. Wheels: `Wheels.md`. Brakes: `Brakes.md`.

Covers Citroën hydropneumatics, Land Rover / Range Rover air suspension, BMC/Rover Hydrolastic and Hydragas, Mercedes and other OEM systems, active hydraulic systems, hydraulic dampers ("shocks"), military and industrial uses, aftermarket air ride and lowrider hydraulics.

---

## 1. Fundamentals

### 1.1 Spring vs. damper

Every suspension corner has two jobs:

| Function | Component | What it does |
|---|---|---|
| Spring | Coil, leaf, torsion bar, rubber, air bag, gas sphere | Holds the car up and stores energy when the wheel hits a bump |
| Damper ("shock absorber") | Hydraulic piston forcing oil through valves | Turns that stored energy into heat so the body stops bouncing |

A "hydraulic shock" in the conventional sense is only a damper. Air and hydropneumatic systems replace the **spring** with compressed gas. Citroën's system combines spring, damper and self-leveling into a single hydraulic circuit.

### 1.2 Why gas springs

Steel springs have a fixed rate. Load the car and it sags. Stiffen the spring to resist sag and the empty car rides hard. A gas spring can be refilled or pumped to restore height under any load and its rate rises naturally as it compresses (progressive), giving a soft initial ride with strong resistance near full compression.

### 1.3 Gas spring physics

Air spring force:

```
F = P_gauge × A_eff
```

Stiffness (rate):

```
k = n × P_abs × A_eff² / V   +   P_gauge × (dA_eff / dx)
```

- `n` = polytropic exponent: about 1.0 for slow (isothermal) motion, up to 1.4 for fast (adiabatic) motion. Real suspension sits around 1.2 to 1.38.
- `V` = gas volume. Bigger volume means softer spring.
- The second term comes from the bag's effective area changing with height. Rolling-lobe piston shape is used to tune this.

Natural frequency of a corner (sprung mass `m`):

```
f = (1 / 2π) × √(k / m)
```

**Air suspension with leveling (constant volume, air mass added):** at ride height `V` is fixed. Adding load means adding air so pressure rises in proportion to load. Mass `m = P A / g`. Substituting:

```
f ≈ (1 / 2π) × √(n × g × A_eff / V)
```

Load cancels out. **Ride frequency stays essentially constant whether the vehicle is empty or fully loaded.** This is the main engineering advantage of leveling air suspension.

**Citroën-style hydropneumatic (constant gas mass, fluid added):** the nitrogen in each sphere is sealed. Leveling adds fluid, which compresses the fixed gas charge into a smaller volume. Gas volume falls as pressure rises (`V = P0 × V0 / P`), so:

```
f ≈ (1 / 2π) × √(n × g × A × P / (P0 × V0))
```

Frequency rises with the square root of load. A laden Citroën rides firmer than an empty one though far less so than a steel-sprung car would sag. Height stays constant either way.

### 1.4 Typical ride frequencies

| Vehicle type | Approx. body frequency |
|---|---|
| Citroën DS / CX (soft) | 0.6 to 0.9 Hz |
| Luxury sedan, air | 0.9 to 1.2 Hz |
| Typical passenger car | 1.0 to 1.5 Hz |
| Sports car | 1.5 to 2.5 Hz |
| Race car with aero | 3 to 5+ Hz |

---

## 2. Citroën Hydropneumatic Suspension

### 2.1 History

Invented by **Paul Magès**, a self-taught Citroën engineer. First used at the rear of the **Traction Avant 15-Six H (1954)** as a test bed, then across the entire **DS (1955)**.

| Model | Years | System |
|---|---|---|
| Traction Avant 15-Six H | 1954-1955 | Rear hydropneumatic only |
| DS / ID | 1955-1975 | Full hydropneumatic; DS also powered brakes, steering, clutch and gearbox |
| SM | 1970-1975 | Hydropneumatic plus DIRAVI speed-sensitive self-centering steering |
| GS / GSA | 1970-1986 | First compact car with hydropneumatics |
| CX | 1974-1991 | Hydropneumatic; DIRAVI on upper trims |
| BX | 1982-1994 | Hydropneumatic in a mass-market family car |
| XM | 1989-2000 | **Hydractive** (first electronically controlled version) |
| Xantia | 1993-2001 | Hydractive II; **Activa** (1994) with active roll control |
| C5 (I) | 2001-2008 | **Hydractive 3 / 3+**, electric pump, separate brakes and steering |
| C6 | 2005-2012 | Hydractive 3+ |
| C5 (II) | 2008-2017 | Hydractive 3+ on upper versions; steel springs on others |

Production ended with the C5 in 2017. Citroën's later "Progressive Hydraulic Cushions" (2017 onward) are conventional dampers with secondary hydraulic stops, not hydropneumatic.

Licensed or derived uses:
- **Rolls-Royce Silver Shadow / Bentley T (1965)**: Citroën-licensed high-pressure hydraulics for brakes and self-leveling (steel coil springs carry the car; hydraulic rams adjust height). Front leveling dropped in 1969.
- **Mercedes-Benz 450 SEL 6.9 (1975)**: full hydropneumatic, mineral-oil, self-leveling. Mercedes also used hydropneumatic rear leveling on the W123 estate and other models.
- **Maserati Quattroporte II (1974)**: SM-derived hydraulics during Citroën ownership of Maserati.
- **Peugeot 405 Mi16x4 / x4 variants**: hydropneumatic rear.

### 2.2 How it works

The system is a closed high-pressure hydraulic circuit:

```
Reservoir → Pump → Pressure regulator → Main accumulator → Security valve
                                                          ├→ Front height corrector → front struts + spheres
                                                          ├→ Rear height corrector  → rear struts + spheres
                                                          ├→ Brakes (priority circuit)
                                                          └→ Steering / gearbox (DS, SM, CX)
Return lines → Reservoir
```

**Pump**
- DS: engine-driven 7-piston axial pump (single-piston on ID).
- Later cars: belt-driven 5- or 6-piston pumps.
- Hydractive 3: electric pump inside the **BHI (Built-in Hydroelectronic Interface)** unit.

**Pressure regulator and main accumulator**
- Holds system pressure in a band, roughly 145 bar cut-in and 170 bar cut-out on LHM systems.
- The main accumulator (a sphere) stores pressure so the pump does not run continuously and so brakes have reserve with the engine off.

**Security (priority) valve**
- Feeds brakes first. Suspension only receives pressure once braking pressure is secure.

**Spheres**
- Steel ball split by a flexible membrane (diaphragm).
- Top half: nitrogen at a precharge pressure (the spring).
- Bottom half: hydraulic fluid connected to the suspension cylinder.
- Wheel moves up, piston pushes fluid into the sphere, nitrogen compresses.

**Damping**
- Built into the neck of each sphere: a valve block with small bypass holes plus spring-steel leaf stacks.
- Low-speed motion bleeds through the holes. Faster motion deflects the leaves. Fluid passing through generates damping force.
- No separate shock absorbers exist on classic Citroëns.

**Suspension cylinders (struts)**
- Piston in a cylinder pushes fluid to the sphere. Fluid is effectively incompressible so all spring action happens in the gas.

**Height correctors**
- One per axle, mechanically linked to the anti-roll bar.
- Car sits too low: corrector opens to admit pressurized fluid.
- Car sits too high: corrector opens to return.
- Includes a dashpot delay so it reacts to sustained load changes, not to individual bumps.

**Height control lever (DS through BX)**
- Driver-selected positions: Low, Normal, High (rough roads, fords), Extra High (wheel change).

### 2.3 Hydraulic fluids

| Fluid | Color | Base | Era | Notes |
|---|---|---|---|---|
| LHS / LHS2 | Red / colorless | Synthetic, glycol-based | 1955-1967 | Hygroscopic, absorbs water, corrosive over time |
| LHM | Green | Mineral oil | 1967-2001 | Non-hygroscopic, stable, cheap |
| LDS | Orange | Synthetic | Hydractive 3 (2001-2017) | Not compatible with LHM |

**Fluids are not interchangeable.** Wrong fluid destroys seals. LHM cars use green seals/rubber; LHS cars use different rubber compounds.

### 2.4 Capabilities

- **Constant ride height** at any load.
- **Very low ride frequency** with good body control from progressive gas springs.
- **Adjustable height** for rough roads, flood crossings, parking.
- **Wheel changes without a jack**: select high position, place stand under sill, select low; the wheel retracts off the ground.
- **Driving on three wheels**: the DS can be driven with a rear wheel removed because the hydraulics redistribute load. A famous Citroën demonstration.
- **Load-sensing brakes (DS)**: rear brake pressure is taken from the rear suspension circuit, so braking force scales with rear load automatically.
- **Pitch and squat resistance** from the progressive spring rate.
- **Flat towing and tire puncture tolerance**: the car stays level on a deflating tire.

### 2.5 Hydractive (1989 onward)

Adds electronic control of stiffness.

**Principle:** each axle gets an extra **center (third) sphere** connected through an electrically controlled valve.

| Mode | Valve state | Gas volume | Result |
|---|---|---|---|
| Soft | Open | Corner spheres + center sphere | Larger gas volume, extra damping path, soft ride |
| Firm | Closed | Corner spheres only | Smaller gas volume, stiffer spring, more roll control; left and right isolated |

**ECU inputs:** steering angle and rate, throttle position and movement, brake pressure, vehicle speed, body movement. The car switches to firm for fractions of a second during hard cornering, braking or acceleration and returns to soft on straight roads.

**Generations**
- **Hydractive 1 (XM 1989):** first version, logic tuned later because the car spent too much time in firm.
- **Hydractive 2 (XM Series 2, Xantia):** revised logic, Sport switch.
- **Anti-sink valve (Xantia onward):** stops the car settling to the bump stops when parked for long periods.

### 2.6 Activa (Xantia Activa, 1994)

Active roll control:
- Two additional spheres plus hydraulic rams in the anti-roll bar linkages (ten spheres total).
- Rams stiffen the anti-roll bars in real time to hold the body almost flat; roll limited to well under 1 degree.
- Body stays level in corners while the soft suspension remains on straights.
- The Xantia Activa V6 recorded one of the best Swedish moose-test (elk test) results ever published, outperforming numerous sports cars.

### 2.7 Hydractive 3 and 3+ (C5, C6)

Major redesign:
- **BHI unit**: electric pump, ECU, valves combined under the hood.
- **Electronic height sensors** replace mechanical correctors.
- Suspension only: brakes and steering became conventional.
- **LDS** fluid, longer service intervals, higher-durability spheres.

Automatic height functions (C5):
- Above about 110 km/h on good roads: lowers about 15 mm front, 11 mm rear (aero and stability).
- Below about 70 km/h on poor roads: raises about 13 mm front, 20 mm rear.
- Maintains height when parked for extended periods.
- Manual heights for loading and rough terrain, speed-limited.

**Hydractive 3+** adds the third (center) spheres back for soft/firm switching plus a Sport mode. Fitted to higher-spec C5 and all C6.

### 2.8 Weaknesses and maintenance

| Issue | Cause | Remedy |
|---|---|---|
| Harsh ride, crashing over bumps | Nitrogen permeates the membrane; sphere goes flat | Replace or regas spheres (typical life 60,000 to 100,000 miles or so depending on type and era) |
| Car sinks overnight | Internal leakage in correctors, struts or valves | Normal on old cars; anti-sink valves fix it on later models |
| Pump runs constantly / clicks frequently | Flat main accumulator | Replace or regas accumulator |
| Fluid on ground | Corroded return pipes, leaking seals, perished hoses | Replace lines; use correct fluid |
| Height fault (Hydractive 3) | Sensor failure, BHI pump or valve failure | Diagnosis tool, BHI repair or replacement |
| Seal damage | Wrong fluid or contamination | Flush, replace all affected seals |

Regassable spheres have a fill screw on top. Many later spheres are sealed and must be replaced.

---

## 3. BMC / British Leyland / Rover: Hydrolastic and Hydragas

Designed by **Alex Moulton**. Used on most BMC and later Rover small and mid-size cars.

### 3.1 Hydrolastic (1962)

**Displacer unit** at each wheel: a rubber spring element combined with a fluid chamber and diaphragm.

- Fluid: water with alcohol (antifreeze) and anti-corrosion additives.
- **Front and rear displacers on each side are connected by a pipe.**
- Front wheel hits a bump: fluid is pushed to the rear displacer, lifting the rear in step. Car stays level in pitch.
- Both ends compress together (load or roll): no fluid transfer, the rubber springs carry it. Stiff in roll, soft in pitch.
- Damping valves inside each displacer; many installations also had separate dampers.

Used on: Morris/Austin 1100 and 1300 (1962), Mini (1964-1971; returned to rubber cones afterward), Austin 1800, Austin Maxi, Austin Kimberley and Tasman.

### 3.2 Hydragas (1973)

Evolution of Hydrolastic: the rubber spring is replaced with a **nitrogen sphere**, making it a hydropneumatic system with front-rear interconnection.

- Nitrogen chamber separated from fluid by a diaphragm.
- Same side-to-side fore-aft interconnection.
- No pump, no self-leveling. Height is set by charging fluid with a service pump through a Schrader-type valve.

Used on: Austin Allegro (1973), Princess (1975), Austin Ambassador (1982), Austin/MG Metro (1980), Rover Metro / Rover 100 (1990-1998, interconnected version), **MGF (1995-2002)**. The MG TF (2002) switched to coil springs.

### 3.3 Characteristics and maintenance

| Feature | Detail |
|---|---|
| Strength | Excellent pitch control, compact, no separate springs |
| Weakness | No leveling; units lose pressure and the car sags over time |
| Service | Re-pressurize with a dedicated pump to factory height |
| Failure | Displacer units perish internally; corroded interconnect pipes |
| Rover 100 / MGF height | Set by pressurizing and measuring wheel-arch height; Hydragas units are no longer made new by the original supplier but reconditioned units circulate |

---

## 4. Land Rover / Range Rover Air Suspension

### 4.1 Range Rover Classic

- **1970 to 1992**: coil springs with a **Boge Hydromat self-pumping leveler** at the rear center. It used road motion to pump itself up to height under load. No external pump.
- **1992 (1993 model year, LSE / long wheelbase): EAS (Electronic Air Suspension)** introduced. Air springs replace coils on beam axles.

Components:
- Electric compressor with desiccant air dryer
- Reservoir (air tank)
- Valve block (solenoid valves per corner plus inlet and exhaust)
- Four height sensors
- EAS ECU
- Rubber air springs

Height modes (approximate):
| Mode | Change | Use |
|---|---|---|
| Access | Lowest, about 60 mm down | Entry and exit when parked |
| Low (motorway) | About 20 mm down | Automatic above roughly 50 mph |
| Standard | Base | Normal driving |
| High | About 25 to 40 mm up | Off-road, selected at low speed |

### 4.2 P38A Range Rover (1994-2002)

- EAS standard on all models.
- Wabco-based system: compressor, dryer, valve block, reservoir, four height sensors.
- Five heights: Access, Motorway, Standard, Off-road High, plus Extended (temporary extra lift when a wheel hangs or the chassis grounds).
- Auto-lowering at speed and auto-raise prevention above set speeds.
- The system logs faults; certain faults drop the car to a fixed height and display a speed-limit message on the dash.

Known issues: valve block O-ring leaks, compressor wear from running against leaks, saturated dryer causing water in lines, perished air springs, height sensor failure, ECU relay faults. Many owners fit coil conversion kits or diagnostic tools (such as dedicated EAS interfaces) to reset faults and calibrate heights.

### 4.3 L322 Range Rover (2002-2012), Discovery 3 / 4 (2004-2016), Range Rover Sport L320 (2005-2013)

**Independent air suspension at all four corners.** Developed under BMW ownership for the L322.

Key feature: **cross-linking**
- At low speed off-road, valves connect the left and right air springs on each axle.
- Air flows from the compressed side to the extended side.
- Mimics a solid axle: one wheel pushed up pushes the opposite wheel down.
- Greatly increases wheel articulation and traction on uneven ground.
- Disconnected on-road for roll stiffness.

Height modes (approximate):
| Mode | Change |
|---|---|
| Access | About 50 mm down |
| On-road (standard) | Base |
| Off-road | About 55 mm up |
| Extended | Additional temporary lift when grounded or articulated |
| Motorway / aero | Auto-lowers at speed |

Integration:
- **Terrain Response** (Discovery 3 onward) selects height, cross-link behavior and traction programs for grass/gravel/snow, mud and ruts, sand, rock crawl.
- Wading depth relies on raised height.
- Locking the car with the key fob in access mode, crane mode (locks height for jacking or transport), tow mode.

Common faults:
- Air spring perishing or splitting at the crimp, especially front bags.
- Compressor failure (often caused by a slow leak making it run excessively).
- Valve block leaks.
- Height sensor faults.
- Reservoir drain issues.
- Suspension fault messages restricting speed and height until repaired.

### 4.4 Current generation (2012 onward)

Range Rover L405 (2012), Range Rover Sport L494 (2013), Discovery 5 (2017), Velar (2017), Defender L663 (2020), Range Rover L460 (2022), Range Rover Sport L461 (2022).

- Lightweight aluminum architecture with four-corner air springs.
- **Adaptive Dynamics**: continuously variable dampers adjusting many times per second.
- **Dynamic Response**: active anti-roll bars (hydraulic on earlier models, 48-volt electric on later models).
- **Dynamic Air Suspension (L460 / L461)**: switchable-volume (twin-chamber) air springs that change spring rate on the fly, plus predictive control using navigation data.
- **Defender L663**: off-road height about 75 mm above standard; extended mode adds more for clearance; wading depth up to 900 mm with air suspension.
- Faster compressors and reservoirs for quicker height changes.
- Integration with Terrain Response 2 (automatic terrain detection).

### 4.5 Land Rover coil conversions

Available for Classic, P38, L322, Discovery 3/4 and Range Rover Sport. Trade-offs:
- Lose height adjustment, auto-leveling and cross-linking.
- Gain simplicity and reliability.
- Later models need an electronic module to stop the ECU from logging suspension faults and disabling Terrain Response features.

---

## 5. Air Suspension: Components in Detail

### 5.1 Air springs

| Type | Construction | Use |
|---|---|---|
| Convoluted (bellows) | One to three stacked rubber lobes with girdle rings | Trucks, aftermarket, some rear axles; short and powerful |
| Rolling lobe (sleeve) | Rubber sleeve rolls over a shaped piston | Most modern cars; piston profile tunes rate |
| Air strut | Air spring built around a damper | Front and rear corners on most luxury cars |
| Switchable volume | Two chambers joined by a valve | Changes rate electronically (Mercedes, BMW, Porsche, Range Rover) |

Rubber is reinforced with fabric cords. Life is limited by ozone cracking, UV, abrasion from grit at the rolling fold, and age.

### 5.2 Compressor and dryer

- 12 V electric compressor (on modern cars), sometimes engine-driven on trucks.
- Desiccant dryer removes water so moisture does not freeze or corrode valves.
- Exhaust air passes back through the dryer to regenerate it.
- Thermal protection limits run time; overrun from leaks is the classic failure path.

### 5.3 Reservoir

- Stores compressed air for fast raise without waiting on the compressor.
- Typical systems run roughly 10 to 20 bar in the circuit.

### 5.4 Valve block

- Solenoid valves for each corner plus inlet and exhaust valves.
- O-rings and solenoid coils are common failure points.

### 5.5 Sensors and ECU

- Height sensors (rotary or linear Hall-effect) at each corner or axle.
- Pressure sensor in the reservoir or gallery.
- Acceleration sensors, steering angle, speed, door and load signals.
- ECU decides height targets, rates, faults and calibration.

### 5.6 Open vs. closed systems

| System | Operation | Result |
|---|---|---|
| Open | Draws ambient air, vents to atmosphere | Simple; slower; dryer works harder |
| Closed | Air moves between springs and reservoir, rarely vents | Faster height changes; less moisture ingress; more complex |

---

## 6. Other OEM Air and Hydraulic Systems

### 6.1 Early air suspension (1950s-1960s)

- **1957 Cadillac Eldorado Brougham**: air suspension standard.
- **1958 GM option** on Cadillac, Buick, Oldsmobile, Chevrolet, Pontiac: leaks and unreliability led to rapid withdrawal and many retrofits to coils.
- **Mercedes-Benz 300 SE (W112, 1961)** and **600 (W100, 1963)**: air suspension. The 600 also used high-pressure hydraulics for doors, windows and seats.
- **Borgward P100 (1959)**: early German air suspension.

### 6.2 Mercedes-Benz

| System | Introduced | Type |
|---|---|---|
| Hydropneumatic | 450 SEL 6.9 (1975) | Fully hydropneumatic, self-leveling |
| Rear level control | W123 estate and others | Hydropneumatic leveling rear |
| **Airmatic** | S-Class W220 (1998) | Air springs with adaptive damping (ADS) |
| **Active Body Control (ABC)** | CL C215 (1999) | Hydraulic plungers on steel coils actively cancel roll, pitch and heave up to about 5 Hz; high-pressure hydraulic pump |
| **Magic Body Control** | S-Class W222 (2013) | ABC plus stereo camera scanning the road ahead to pre-adjust for bumps |
| **E-Active Body Control** | GLE (2019) | 48 V hydraulic active suspension; can rock the body to free a stuck car, leans into curves |

### 6.3 Other examples

- **Lincoln**: Mark VIII, Continental, Town Car rear air leveling (1980s-2000s).
- **Ford Crown Victoria / Mercury Grand Marquis**: optional rear air.
- **Lexus LS 400 (1989)** and Toyota Celsior: optional air suspension.
- **Audi**: allroad quattro (2000) adaptive air suspension with five heights; A8, A6, Q7, Q8, e-tron.
- **VW Touareg / Porsche Cayenne / Audi Q7**: shared air platform with off-road heights.
- **Porsche**: Panamera, Taycan, Cayenne with three-chamber air springs.
- **BMW**: rear self-leveling air on 5 and 7 Series Touring; full air on X5 (later generations), 7 Series, iX.
- **Bentley / Rolls-Royce**: air suspension on Phantom (2003 onward), Ghost, Cullinan; Rolls-Royce "Flagbearer" camera system pre-adjusts.
- **Jeep Grand Cherokee Quadra-Lift (2011)**: five-height air suspension.
- **Ram 1500 (2013)**: air suspension in a full-size pickup.
- **Tesla Model S / X**, **Lucid Air**, **Rivian R1T / R1S**: air suspension with GPS-based height memory.
- **Toyota KDSS (2009)**: hydraulic cylinders on the anti-roll bars connected through an accumulator; locks bars on-road, frees them off-road for articulation.
- **McLaren 12C (2011), 720S**: **ProActive Chassis Control**, hydraulically interconnected dampers with accumulators and no mechanical anti-roll bars.

### 6.4 Active hydraulic suspension

- **Lotus Active (1980s)**: computer-controlled hydraulic actuators replacing springs; F1 Lotus 99T (1987).
- **Williams FW14B / FW15C (1992-1993)**: dominant F1 active suspension. Banned for 1994.
- **Toyota Soarer / Celica (1989-1991)** and **Infiniti Q45 (1991)**: production active hydraulic systems.
- **Mercedes ABC / MBC / E-ABC**: see above.

Contrast: **Bose electromagnetic suspension** (prototype 2004, later ClearMotion) and **Audi A8 predictive active suspension (2018)** use electric actuators instead of hydraulics.

---

## 7. Hydraulic Dampers ("Shock Absorbers")

### 7.1 Principle

A piston with valves moves through oil. Oil forced through small orifices and spring-steel shim stacks creates resistance proportional to velocity. Energy becomes heat.

- **Compression (bump)**: wheel moves up.
- **Rebound (extension)**: wheel moves down. Rebound damping is usually stronger and controls body float.

### 7.2 Construction types

| Type | Design | Traits |
|---|---|---|
| Twin-tube | Inner working tube plus outer reserve tube | Cheap, compact, can aerate under heavy use |
| Twin-tube gas | Low-pressure nitrogen in reserve tube | Reduces aeration |
| Monotube (de Carbon) | Single tube; floating piston separates oil from high-pressure nitrogen | Invented by Christian Bourcier de Carbon in the 1950s; better cooling, no aeration, mountable upside down |
| Remote reservoir | Monotube with separate gas/oil canister | More oil volume, cooler running, room for adjusters |
| Lever arm | Rotary vane or piston in a body bolted to the chassis | Pre-war and classic British cars |
| Friction | Clamped plates, no oil | Pre-1930s |

### 7.3 Valve characteristics

- **Linear**: force proportional to speed.
- **Digressive**: high force at low speed (body control), tapering at high speed (bump absorption). Common in performance setups.
- **Progressive**: low initial force rising sharply. Comfort tuned.
- **Bleed vs. blow-off**: low-speed flow through fixed bleeds; high-speed flow opens shim stacks.

### 7.4 Adjustable and adaptive dampers

| Technology | How it works | Examples |
|---|---|---|
| Manual clickers | Needle valves adjust bleed | Koni, Bilstein, Öhlins aftermarket |
| Frequency-selective (passive) | Valve responds to input frequency | Koni FSD |
| Position-sensitive | Bypass grooves soften the middle of travel | Off-road racing, Fox bypass |
| Electronically switched | Solenoid selects soft or firm | Early adaptive systems |
| Continuously variable (CDC, DCC) | Proportional solenoid valve adjusted in milliseconds | VW DCC, ZF CDC, Land Rover Adaptive Dynamics |
| Magnetorheological | Oil with iron particles; magnetic field changes viscosity instantly | Delphi/BWI MagneRide (2002 Cadillac Seville STS), Corvette, Audi R8, Ferrari |
| Hydraulic bump stops / secondary stops | Second piston near end of travel | Off-road trucks, Citroën Progressive Hydraulic Cushions |

### 7.5 Air shocks (aftermarket)

- **Air-adjustable shock absorbers**: a damper with an air sleeve wrapped around it (for example Monroe Max-Air). Inflate to raise the rear under load.
- **Air helper springs / bags**: installed inside or beside coil or leaf springs (Firestone Ride-Rite, Air Lift). Add load capacity for towing and campers.
- These assist the existing springs. They do not replace them.

---

## 8. Aftermarket Air Ride

Common on show cars, trucks, euro, stance and hot rods.

Components:
- Air bags (bellows or sleeve) or complete air struts.
- One or two 12 V compressors (Viair and similar).
- Tank (typically 3 to 5 gallons aluminum or steel).
- Lines (1/4 or 3/8 inch DOT tubing), push-to-connect or NPT fittings.
- Water traps and drains.
- Management: manual paddle valves, electric valve manifold, or full electronic management with height sensors and presets (Air Lift 3P/3H, AccuAir).

Capabilities:
- Lay frame on the ground when parked.
- Raise for driveways and speed bumps.
- Per-corner adjustment, preset heights, phone app control on modern kits.

Considerations:
- Driveshaft and CV angles, steering geometry, tire clearance.
- Leaks at fittings.
- Bag life depends on correct alignment and avoiding rubbing.
- Bags must not run fully deflated while driving.

---

## 9. Lowrider Hydraulics

- Origin commonly credited to **Ron Aguirre's 1959 Corvette** ("X-Sonic"), using surplus aircraft hydraulic pumps (Pesco and Marquette) to raise and lower the car.
- Developed in Southern California to defeat minimum-height laws and became a cultural art form.

Components:
- Hydraulic cylinders replace springs (or sit within coils).
- Electric pumps (gear pumps) driven by stacked 12 V batteries in series (24 V, 36 V, 48 V up to 96 V or more for competition hopping).
- **Dumps**: solenoid valves that release fluid back to the tank to drop a corner.
- Switch box: each switch raises or drops a corner, front, back, side.
- Reinforced frames, coil chopped springs, extended A-arms, wrapped frames.

Capabilities:
- Raise or drop any corner instantly.
- **Hopping**: rapid front-end pump pulses bounce the car off the ground; competitions measure height in inches.
- Three-wheel motion: lifting one corner while the car drives.
- **Dancing**: rapid sequencing of all four corners.

Air-bag lowriders use the same switch logic with air instead of oil; slower but smoother and street friendly.

---

## 10. Military and Industrial Hydropneumatics

| Application | System | Capability |
|---|---|---|
| **Strv 103 "S-tank" (Sweden, 1967)** | Hydropneumatic | Tilts entire hull to aim the fixed gun |
| **Type 74 / Type 10 (Japan)** | Hydropneumatic | Kneels, tilts sideways and fore-aft |
| **K1 / K2 (South Korea)** | Hydropneumatic in-arm units | Pitch and height adjustment |
| **Challenger 1 / 2 (UK)** | Hydrogas (Horstman) | High-speed cross-country ride |
| **Leclerc (France)** | Hydropneumatic | Ride and stability |
| Mining haul trucks | Nitrogen-over-oil struts | Carry hundreds of tons with damping |
| Buses and coaches | Air suspension (ECAS) | Kneeling for boarding, leveling |
| Semi trucks and trailers | Air suspension, lift axles | Load leveling, axle lift, lower road wear |
| Railway | Air springs | Constant floor height at platforms, ride comfort |
| Cranes and machinery | Hydropneumatic | Lock-out for lifting, ride for road travel |

---

## 11. System Comparison

| Feature | Steel coil + damper | Air (leveling) | Citroën hydropneumatic | Hydragas | Active hydraulic (ABC type) |
|---|---|---|---|---|---|
| Spring medium | Steel | Air | Nitrogen sphere | Nitrogen + interconnected fluid | Steel + hydraulic actuator |
| Self-leveling | No | Yes | Yes | No | Yes |
| Height adjust | No | Yes | Yes | Manual service only | Yes |
| Ride frequency vs. load | Drops as load rises | Nearly constant | Rises with load | Drops as load rises | Controlled |
| Roll control | Anti-roll bar | Anti-roll bar, switchable volume | Anti-roll bar, Hydractive, Activa | Anti-roll bar, rubber/gas stiffness | Active cancellation |
| Pitch control | Damper | Damper | Progressive rate | Interconnection | Active cancellation |
| Complexity | Low | Medium to high | High | Medium | Very high |
| Typical failures | Worn dampers, broken springs | Bags, compressor, valves, sensors | Spheres, leaks, pipes, pumps | Displacer perishing, pressure loss | Pumps, valves, lines, accumulators |

---

## 12. Diagnosis Quick Reference

### Air systems
1. Car sags at one corner overnight: leaking bag (spray soapy water on bag and fittings), valve block O-ring, line leak.
2. Compressor runs often or overheats: leak somewhere in the system.
3. Slow raise: worn compressor, blocked dryer, leaking reservoir.
4. Height fault message: sensor out of range, broken linkage, ECU calibration loss.
5. Water in lines: saturated dryer.
6. Car stuck high or low: valve block solenoid, relay, fuse, or ECU protective lockout.

### Citroën hydropneumatics
1. Bouncy, harsh, crashing: flat spheres. Push down on each corner; minimal give means flat sphere.
2. Pump cycling rapidly: main accumulator flat.
3. Slow rise after start: weak pump, low fluid, flat accumulator, leaking corrector.
4. Car drops overnight on non-anti-sink models: normal; overnight drop in minutes indicates internal leak.
5. Fluid level: check with car at high position (procedure varies by model).

### Hydragas / Hydrolastic
1. Car sits low on one side: unit lost pressure; re-pump and check for leaks.
2. Crashing ride: low pressure or failed displacer.
3. Car pitches unevenly: blocked or corroded interconnect pipe.

---

## 13. Glossary

- **Accumulator**: pressurized gas sphere storing hydraulic energy.
- **BHI**: Built-in Hydroelectronic Interface, Hydractive 3 control unit with integrated pump.
- **Cross-linking**: Land Rover valve connecting left and right air springs to increase articulation.
- **Corrector (height corrector)**: valve that admits or releases fluid to hold height.
- **DIRAVI**: Citroën hydraulic power steering with speed-sensitive self-centering (SM, CX).
- **Displacer**: Moulton fluid/spring unit in Hydrolastic and Hydragas systems.
- **EAS**: Electronic Air Suspension (Land Rover).
- **Effective area**: area over which air pressure acts to support load.
- **LHM / LHS / LDS**: Citroën hydraulic fluids (mineral green / synthetic red / synthetic orange).
- **Nivomat / Hydromat**: Boge self-pumping leveling struts that use road motion to restore height.
- **Polytropic exponent**: describes how gas pressure changes with compression speed.
- **Sphere**: Citroën gas/fluid spring unit with diaphragm.
- **Third sphere / center sphere**: Hydractive extra gas volume per axle for soft mode.
