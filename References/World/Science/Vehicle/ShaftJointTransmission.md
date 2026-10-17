# Shaft, Joint, Gear and Transmission Mechanics

> Earth invent loot. Steel vs indestructible (rigid, no yield / wear / fatigue) comparison for axles, U-joints, double Cardan, gears, differentials and whole drivelines. Not Caldris law. Car parts ladder: `MechanicalCarComponents.md`. Wheels / traction: `Wheels.md`, `WheelScience.md`. Suspension: `Suspension.md`. Engines: `../Energy/Engines.md`, `../Energy/SteamEngines.md`. Shop gears / precision: `../Invent/MechanicalPrecision.md`. Printer vehicle manufacture: `../Invent/PrinterManufacturingVehicles.md`. Nav: `Index.md`.

Two cases are compared throughout:

- **Steel:** ordinary heat-treated alloy steel (4340 class). Shear strength about 90 ksi. Shear modulus G about 11.5 x 10^6 psi.
- **Indestructible:** a material that cannot yield, crack, wear or fatigue. It is also treated as perfectly rigid unless noted.

---

## 1. Core Physics

### Torque and power

- **P = T x ω**
- P = power, T = torque, ω = angular speed (rad/s)
- In imperial units: **HP = T (lb-ft) x RPM / 5252**

Power is conserved through any shaft, joint or gear (minus friction losses). Any device that raises torque lowers speed by the same factor. No shaft, joint or gearbox creates power. It only trades torque against speed.

### Twist of a shaft

- **θ = T x L / (G x J)**
- θ = twist angle (radians), L = length, G = shear modulus, J = polar moment of inertia
- Solid shaft: J = π d^4 / 32

A shaft is a torsional spring. Torsional stiffness is k = G J / L.

| Case | Behavior |
|---|---|
| Steel | Twists under load. Stores energy like a spring (E = ½ T θ). Absorbs shock and releases it as wind-up and rebound. |
| Indestructible (rigid) | Zero twist. No energy storage. Every torque spike at one end arrives instantly and fully at the other end. |

### Torque from force

- **T = F x r**
- A wheel of radius r pushing the ground with force F requires axle torque F x r.
- The ground can only push back up to **F_max = μ x N** (friction coefficient x normal load).

This traction limit applies to both cases. An indestructible axle with infinite torque still only produces as much thrust as the tire grip allows. Past that point the wheel spins.

---

## 2. Straight Axle

A straight axle at 0° is the ideal transmitter:

- Output speed equals input speed at every instant.
- Output torque equals input torque at every instant.
- No secondary forces or couples are created.

### Loads on a drive axle

- **Torsion:** the drive torque.
- **Bending:** vehicle weight and cornering loads acting at the wheel hub.

### Critical speed (whirl)

A spinning shaft has a natural bending frequency. At that speed small imbalances grow without limit.

- Simply supported shaft: **ω_c = (π² / L²) x √(E I / m')**
- E = elastic modulus, I = area moment of inertia, m' = mass per unit length

| Case | Behavior |
|---|---|
| Steel | Long thin shafts have low critical speeds. This is why long driveshafts are split into two pieces with a center bearing. |
| Indestructible (rigid) | No bending flex means no whirl. Critical speed is infinite. |

---

## 3. Single U-Joint (Cardan / Hooke's Joint)

### Speed relationship

For joint angle β and input rotation position θ:

**ω2 / ω1 = cos β / (1 − sin²β x sin²θ)**

The output speed swings between two extremes twice per revolution:

- Minimum: ω1 x cos β
- Maximum: ω1 / cos β

### Torque relationship

With no friction, power in equals power out at every instant, so torque swings inversely to speed:

- Minimum output torque: T1 x cos β
- Maximum output torque: T1 / cos β

### Example: 1,000 lb-ft input

| Joint angle β | Output torque range (lb-ft) | Output speed range (% of input) |
|---|---|---|
| 0° | 1,000 to 1,000 | 100 to 100 |
| 15° | 966 to 1,035 | 96.6 to 103.5 |
| 30° | 866 to 1,155 | 86.6 to 115.5 |
| 45° | 707 to 1,414 | 70.7 to 141.4 |
| 60° | 500 to 2,000 | 50 to 200 |
| 80° | 174 to 5,759 | 17.4 to 576 |
| 89° | 17 to 57,300 | 1.7 to 5,730 |
| 90° | 0 to infinite | Locked |

At 90° the cross pins line up with the shaft axis. The joint cannot turn. This is a geometric singularity, not a material failure. An indestructible joint locks at 90° exactly like a steel one.

### Forces on the cross (spider)

The cross trunnions carry the torque as a pair of forces. With trunnion radius r:

**F_trunnion (peak) ≈ T1 / (2 x r x cos β)**

Example: 1,000 lb-ft input, r = 1.5 in (0.125 ft)

| β | Peak trunnion force |
|---|---|
| 0° | 4,000 lb |
| 30° | 4,619 lb |
| 60° | 8,000 lb |
| 80° | 23,040 lb |
| 89° | 229,200 lb |

### Secondary couple

A U-joint at an angle also produces a bending couple on both shafts that rotates with the joint. Its peak is about:

**M ≈ T1 x tan β**

| β | Secondary couple (1,000 lb-ft input) |
|---|---|
| 15° | 268 lb-ft |
| 30° | 577 lb-ft |
| 60° | 1,732 lb-ft |
| 80° | 5,671 lb-ft |
| 89° | 57,290 lb-ft |

The support bearings must react this couple. It pulses twice per revolution.

### Inertia torque from speed fluctuation

The output speeds up and slows down twice per revolution. Peak angular acceleration of the output is about:

**α_peak ≈ ω1² x sin²β**

Example in SI units: 3,000 RPM input (314 rad/s), β = 15°

- α_peak ≈ 314² x 0.067 ≈ 6,600 rad/s²
- Driven inertia of 0.1 kg·m² needs ≈ 660 N·m (487 lb-ft) of extra torque just to accelerate and decelerate it each half turn

This torque is separate from the load torque and grows with the square of speed.

| Case | Effect |
|---|---|
| Steel | Fluctuation causes vibration, noise, bearing wear and fatigue. Practical limit about 15° continuous at road speed. Up to 30-45° only at low speed. |
| Indestructible | Parts survive any angle under 90°. The fluctuation still shakes the input source and driven load. At 3,000 RPM and high angle the input motor sees torque spikes many times its rating. |

---

## 4. Double U-Joint Shaft (Two Joints or Double Cardan)

### Cancellation principle

Two joints in series cancel each other's speed fluctuation when:

1. Both joint angles are equal.
2. The yokes on the intermediate shaft are in phase (lined up in the same plane).
3. Input and output shafts lie in the same plane as the intermediate shaft (Z or W layout).

When these are met, output speed equals input speed at every instant.

### What does not cancel

- The **intermediate shaft** still fluctuates between cos β and 1/cos β. Its own inertia creates inertia torque at both joints.
- **Trunnion forces** at each joint still scale with 1/cos β.
- **Secondary couples** still exist at each joint.

### Total angle

- Each joint carries half the total bend.
- Total articulation = 2 x β

| Case | Practical total angle |
|---|---|
| Steel, automotive double Cardan | 40-50° total |
| Steel, industrial slow-speed | Up to 90° total (45° per joint) |
| Indestructible | Anything under 180° total (each joint under 90°) |

### Indestructible double joint near 180°

At 178° total (89° per joint) the input and output still match in speed. The intermediate shaft swings between 1.7% and 5,730% of input speed twice per revolution. Unless it has zero mass, the inertia torque on it becomes enormous. A massless rigid indestructible intermediate shaft is the only version that runs smoothly near 180°.

---

## 5. Gears

Gears transmit torque by tooth contact at a fixed ratio. Unlike U-joints they run at constant velocity ratio at any angle the gear type allows.

### Ratio laws

- **ω_out = ω_in x (N_in / N_out)**
- **T_out = T_in x (N_out / N_in) x η**
- N = number of teeth, η = efficiency

### Tooth forces

With pitch radius r_p:

- Tangential (driving) force: **F_t = T / r_p**
- Radial (separating) force: **F_r = F_t x tan φ** (φ = pressure angle, usually 20°)
- Axial force on helical gears: **F_a = F_t x tan ψ** (ψ = helix angle)

Example: 1,000 lb-ft on a 3 in pitch radius (0.25 ft) spur gear

- F_t = 4,000 lb
- F_r = 1,456 lb
- The shaft bearings carry the resultant ≈ 4,257 lb

### Gear types and angles

| Gear type | Shaft angle | Velocity | Efficiency |
|---|---|---|
| Spur | Parallel (0°) | Constant | 98-99% |
| Helical | Parallel or crossed | Constant | 98-99% |
| Bevel | Any fixed angle, usually 90° | Constant | 97-98% |
| Hypoid | 90°, offset axes | Constant | 90-96% |
| Worm | 90°, offset axes | Constant | 50-90% |

Bevel gears turn power through 90° at perfectly constant speed. A single U-joint locks at 90°. For a fixed sharp angle, gears are the correct device. U-joints are for angles that change while running (suspension travel).

### Steel vs indestructible gears

| Factor | Steel | Indestructible |
|---|---|---|
| Tooth bending limit | Set by tooth size and root stress | None |
| Surface contact limit | Pitting and wear from Hertz contact pressure | None |
| Maximum ratio per stage | About 6:1 to 8:1 for spur and helical before teeth get too small | Unlimited in theory |
| Friction loss | Present | Present unless also frictionless |
| Worm self-locking | Yes at low lead angles | Yes, still a friction effect |

Friction is a surface interaction, not a strength property. Indestructible gears still lose energy to friction unless the material is also defined as frictionless.

---

## 6. Transmissions and Drivelines

### Stacking stages

- **Overall ratio = product of every stage ratio**
- **Overall efficiency = product of every stage efficiency**

### Differential

An open differential splits torque equally between the two axles. It allows them to turn at different speeds. Average axle speed equals carrier speed.

### Worked example: vehicle driveline

- Engine: 300 lb-ft
- 1st gear: 3.5:1
- Final drive: 3.73:1
- Combined efficiency: 90%
- Tire radius: 14 in (1.167 ft)

| Step | Value |
|---|---|
| After 1st gear | 300 x 3.5 = 1,050 lb-ft |
| After final drive | 1,050 x 3.73 = 3,917 lb-ft |
| After losses | 3,917 x 0.9 = 3,525 lb-ft |
| Per axle (open diff) | 1,762 lb-ft |
| Thrust per wheel | 1,762 / 1.167 = 1,510 lb |
| Total thrust | 3,020 lb |

### Shaft size needed

| Case | Axle requirement |
|---|---|
| Steel | Fails at T = τ π d³ / 16. For 1,762 lb-ft with a safety factor of 2: d ≈ 1.34 in. A 1 in steel axle would break in 1st gear. |
| Indestructible | Any diameter works, even a needle. The rigid shaft still has zero twist. |

### What limits an indestructible driveline

With unbreakable shafts, joints and gears, the maximum output is set by physics outside the parts:

1. **Input power:** the engine or motor rating. Gears can multiply torque without limit but power stays fixed.
2. **Traction:** thrust cannot exceed μ x N at the tires.
3. **Reaction:** whatever the shaft pushes against must hold. An infinite-torque axle on an ordinary frame twists the frame.
4. **Geometry:** U-joints still lock at 90°. Gear ratio still trades speed for torque.
5. **Inertia:** rigid parts transmit shock instantly. Without the spring effect of steel, impacts reach the engine and load undamped.

---

## 7. Best Angles Summary

| Device | Steel best angle | Steel max practical | Indestructible best angle | Indestructible max |
|---|---|---|---|---|
| Straight axle | 0° | 0° | 0° | 0° |
| Single U-joint | 1-3° (keeps needle bearings rolling and lubricated) | ~15° continuous, 30-45° slow | 0° exactly (no wear concerns) | Just under 90° (locks at 90°) |
| Double U-joint | 1-3° per joint, equal angles, yokes in phase | 40-50° total automotive, 90° total industrial | 0° | Just under 180° total |
| Bevel gears | Any fixed angle (90° standard) | Fixed by design | Any fixed angle | Any fixed angle |

### Maximum torque summary

| Device | Steel | Indestructible |
|---|---|---|
| Shaft | τ π d³ / 16 | Unlimited |
| U-joint | Shaft limit derated by cos β and speed | Unlimited below 90°, peaks of T / cos β pass through to the source |
| Gear stage | Tooth bending and contact limit | Unlimited, multiplied by ratio |
| Whole driveline | Weakest part | Input power, traction and reaction structure |
