# Rigid-Link Tentacle Arm: Design Exercise

> Earth invent loot / fiction vehicle design. Indestructible-link four-arm harness, wrap math, taper, force limits, magic swap. Not Caldris law. Motion modes: `TentacleMotionModes.md`. Ride smoothness: `WalkerRideSmoothness.md`. Legged machines: `LeggedVehicles.md`. Walking house: `WalkingHouse.md`. Shaft / driveline: `ShaftJointTransmission.md`. Hub g / vestibular context: `../Body/AccelerometersGyroscopesVestibular.md`, `../Body/GForceTolerance.md`. Surface grip / spikes: `../Body/GripBiteBracing.md`. Goals wishlist: `../../../People/Roland/Goals.md`. Nav: `Index.md`.

---

## 0. Assumptions

- **Links:** Made of an indestructible material. Cannot bend, break, stretch, wear, fatigue or deform in any way.
- **Physical properties that still apply:** The material still has mass, a surface friction value and thermal and electrical behavior. For the math below it is treated like steel for density (7,850 kg/m³), conducts heat and electricity like a metal and has a slick bare surface unless padded.
- **Internals:** Ordinary materials (motors, cables, rubber pads, fluids, sensors, batteries) are available and are NOT indestructible unless stated.
- **Arm:** 20 ft long. Four arms on a hub harness.
- **Pilot:** About 200 lb.

---

## 1. When a Chain Acts Like a Wire

A chain of rigid links wrapped around a pole forms a polygon around the circle. Two numbers decide whether it behaves like wire.

- **Angle per joint:** Δ ≈ 2·asin(p ÷ 2R), where p is link pitch (length) and R is the radius of the wrapped object.
- **Gap from a true circle (sagitta):** s ≈ p² ÷ 8R.

**Rule: link pitch ≤ half the radius of the smallest object the section must wrap (p ≤ R/2).**

At that size:
- Each joint bends about 29 degrees.
- The polygon sits within about 3 percent of the radius from a true circle.
- There are about 13 links per wrap.
- Contact pads absorb the remaining gap.

### The Polygon Actually Grips Better
At each link corner the chain changes direction sharply. Friction at a corner follows:

T₁ ÷ T₂ = (cos(Δ/2) + μ·sin(Δ/2)) ÷ (cos(Δ/2) − μ·sin(Δ/2))

At 12 links per wrap and μ = 0.5:
- Smooth wire: 23.1 times holding per wrap.
- Rigid-link polygon: 25.3 times holding per wrap.

A link chain at this pitch holds about 10 percent better than a perfect wire.

### Pitch Needed by Object

| Object | Diameter | Max link pitch |
|---|---|---|
| Building column | 4 ft | 12 in |
| Building column | 2 ft | 6 in |
| Tree trunk, utility pole | 16 in | 4 in |
| Streetlight pole | 8 in | 2 in |
| Fence post, human limb | 6 in | 1.5 in |
| Pipe, handrail | 2 in | 1/2 in |
| Rebar, cable, tool handle | 1/2 in | 1/8 in |
| Pen, key ring, wire bundle | 1/4 in | 1/16 in |

Joints should allow at least ±45 degrees so sections can coil tighter than their minimum, tie knots and conform to irregular shapes.

---

## 2. Taper: The Science Behind It

Because the material is indestructible, strength never forces a taper. Three other factors do.

### Factor 1: Actuator Torque (the main driver)
To push sideways with force F at the tip, a joint at distance s from the tip needs torque τ = F·s. Joints near the tip need very little torque. Joints near the base need a lot.

- **Tendon-driven sections:** Torque = tendon tension × tendon offset, and the offset scales with diameter d. So d ∝ s. Result: **linear (conical) taper**. Octopus arms are close to conical for this reason.
- **Hydraulic or motor-in-joint sections:** Piston area scales with d² and lever arm with d, so torque ∝ d³. Result: d ∝ s^(1/3). **Cube-root taper**: thick for most of the length, then thin quickly near the end. Human arms follow this pattern (thick upper arm, narrow wrist).

### Factor 2: Self-Weight
Each section carries the weight of everything beyond it. A heavy tip forces every joint behind it to be stronger, so tapering the tip reduces load all the way back to the shoulder.

### Factor 3: Wrap Targets
Each section's link pitch must suit the objects it is meant to wrap (Section 1). Good bending also needs pitch around 1/4 to 1/2 of the section diameter.

### Recommended Profile
- Cube-root taper through the hydraulic shoulder.
- Linear taper through the tendon-driven middle.
- A step down at the wrist into a sensor and actuator pod.
- A branch into three fingers.
- Fingers taper linearly to fine filament tips.

**Overall taper: 6 in at the shoulder to 1/8 in at the filament tips.** That is 48:1 in diameter and about 2,300:1 in cross-section area.

---

## 3. Full Arm Layout

| Section | Span | Diameter | Link pitch | Links | Wraps down to | Drive |
|---|---|---|---|---|---|---|
| Shoulder | 0 to 6 ft | 6 in | 12 in | 6 | 4 ft column | Hydraulic |
| Upper arm | 6 to 11 ft | 4 in | 4 in | 15 | 16 in trunk | Tendons from hub |
| Forearm | 11 to 15 ft | 2.5 in | 1.5 in | 32 | 6 in post or limb | Tendons from hub |
| Wrist | 15 to 18 ft | 1.5 in | 1/2 in | 72 | 2 in pipe | Tendons from hub |
| Wrist pod | at 18 ft | 2.5 in housing | none | 1 | none | Holds finger motors |
| Fingers (×3) | 18 to 19.75 ft | 1/2 in tapering to 1/4 in | 1/8 in | 168 each | 1/2 in rod | Tendons from pod |
| Filament tips (×3) | last 3 in | 1/4 in tapering to 1/8 in | 1/16 in | 48 each | 1/4 in rod | Tendons from pod |

**Total: about 773 links per arm, 648 of them in the fingers.**

### Why the Wrist Pod Exists
Tendons lose tension to friction every time they pass through a bend (Section 7). A tendon running 20 ft from the hub through a coiled arm loses most of its pull before reaching the fingers. Putting small motors in a pod at the wrist keeps finger tendons short, so fingertip control stays precise no matter how the rest of the arm is coiled.

---

## 4. Detailed Tips

### Grip Types With Three Fingers
- **Wrap (power grip):** Fingers coil around an object. Strongest grip.
- **Pinch:** Two filament tips press together. For small objects and fine control.
- **Hook:** One finger curls and pulls. For handles, ledges and triggers.
- **Splay:** Fingers spread to brace against a surface. Stabilizes the wrist for precise work.
- **Thread:** One filament tip snakes through a gap, hole or mechanism.

### Smallest Practical Size
- **Mechanical limit:** Effectively none. Indestructible pins can be microscopic. Watch parts already use pins around 0.1 mm.
- **Actuated limit: about 1/8 in (3 mm) diameter.** Below that there is no room for tendon channels. The smallest steerable surgical catheters and endoscopes sit around 2 to 3 mm for the same reason.
- **Passive limit:** Links smaller than 1/8 in can still exist as unactuated whiskers or bristles, moved only by the section behind them. Useful for sensing, threading and probing.

### Sensing at the Tips
- **Shape sensing:** An optical fiber with Bragg gratings runs through each section and measures its own bend along the full length. Surgical robots use this. Tracking 773 links with individual encoders is impractical.
- **Touch:** Pressure-sensing pads on the inner faces of fingers.
- **Vision:** Endoscope cameras are 1 to 4 mm across and fit in the wrist pod and fingertips.

### Precision
- **Absolute accuracy from the shoulder is poor.** An angle error of 0.1 degrees at the shoulder moves the tip 0.42 in at 20 ft.
- **Joint slop adds up.** With 0.0005 in clearance in a 0.5 in finger joint, each joint has about 0.001 radians of play. Across 216 finger joints the random error reaches about 0.2 in at the fingertip (error ≈ play × length × √(joints ÷ 3)).
- **Fixes:**
  - Tendon preload pulls every joint tight against one side and removes slop.
  - The locking cable removes slop completely.
  - Brace the wrist on the target (splay grip) and work relative to it, the same way a person rests their hand to write.
- **Result:** Sub-millimeter fingertip control relative to the wrist.

### Grit
Sand grains range from about 0.0025 to 0.08 in. Filament joints at 1/16 in pitch are sand-grain size, so grit can lodge in them and jam them. Fine sections need a thin sealed outer sleeve. The sleeve is ordinary material and can be torn in combat.

---

## 5. How Strength Changes Along the Arm

The links are infinitely strong everywhere. What changes along the arm is what each section can **do**, which is set by its actuators and geometry.

### The Core Principle
**In tension the arm is a cable with unlimited strength. In bending it is a crane limited by its weakest joint.**

- Pulling, hanging and wrapping put the chain in tension. Indestructible links never fail, so the limit moves to whatever the arm is attached to.
- Pushing sideways requires joints to resist bending. That is limited by joint torque, and torque shrinks toward the tip.

### Joint Torque by Section
Using indestructible chain as tendons (tension limited only by the pulling motor):

| Section | Tendon offset | Max tendon tension | Joint torque |
|---|---|---|---|
| Shoulder | Hydraulic | n/a | 5,000 lb·ft |
| Upper arm | 1.6 in | 6,000 lb | 800 lb·ft |
| Forearm | 1.0 in | 6,000 lb | 500 lb·ft |
| Wrist | 0.6 in | 6,000 lb | 300 lb·ft |
| Finger (each) | 0.2 in | 300 lb | 5 lb·ft |
| Filament (each) | 0.1 in | 50 lb | 0.4 lb·ft |

With ordinary steel cable tendons instead, the upper sections drop to roughly a quarter of these values.

### Sideways Push at the Tip
Arm straight and horizontal, after carrying its own weight:

| Limited by | Max sideways push |
|---|---|
| Shoulder | 230 lb |
| Upper arm | 44 lb |
| Forearm | 47 lb |
| Wrist | 55 lb |
| Each finger | 2 lb |

- Pushing with the wrist pod at full reach: about **45 lb**, limited by the upper arm.
- Pushing with a fingertip: about **2 lb**.
- Pushing close in, with the arm curled so the contact point is 5 ft from the shoulder: about **900 lb**.

**Design consequence:** Use the forearm and wrist pod as the striking and pushing surface. Fingers are for touch, wrapping and fine control.

### Squeeze Pressure
A wrap under tension T presses on the object with pressure P = T ÷ (R·w), where w is the gripping face width.

| Wrap | Tension | Object | Pressure |
|---|---|---|---|
| Finger, 0.4 in pad | 300 lb | 1 in rod | 1,500 psi |
| Wrist, 1.2 in pad | 6,000 lb | 4 in pole | 2,500 psi |
| Wrist, edge exposed (0.05 in) | 6,000 lb | 4 in pole | 60,000 psi |

For reference: concrete fails around 4,000 psi, wood crushes across the grain around 500 to 1,500 psi and mild steel yields around 36,000 psi. With pads out the wrist grips. With the edge exposed it cuts through steel.

### Weight per Foot
Thin indestructible shells (0.5 mm walls) at steel density, plus internals and pads:

| Section | Weight |
|---|---|
| Shoulder | ~3 lb/ft |
| Upper arm | ~2.2 lb/ft |
| Forearm | ~1.4 lb/ft |
| Wrist | ~0.9 lb/ft |
| Wrist pod | ~5 lb total |
| Each finger | ~0.3 lb/ft |

About 44 lb per arm. Center of mass about 8.8 ft from the shoulder, so holding the arm level alone costs about 390 lb·ft of shoulder torque.

---

## 6. How Much Force It Can Exert

The arm is rarely the limit. Newton's third law is. Every push on the world pushes the rig back equally.

### Full Rig Weight
- Four arms: ~176 lb.
- Hub, hydraulics, motors, battery, frame: ~90 lb.
- Pilot: ~200 lb.
- **Total: ~470 lb.**

### Unanchored on the Ground
Maximum sideways push = μ × total weight before the rig slides.

| Ground | μ | Max push |
|---|---|---|
| Dry concrete | 0.7 | ~330 lb |
| Dirt | 0.4 | ~190 lb |
| Wet tile | 0.2 | ~95 lb |
| Ice | 0.1 | ~47 lb |

### Unanchored Lifting (Tipping Limit)
Standing on three arms spread about 8 ft out from center, the rig tips when load × reach exceeds 470 lb × 8 ft = 3,760 lb·ft.
- At 10 ft reach: ~375 lb.
- At 5 ft reach: ~750 lb.

### Anchored
Once other arms wrap structure, the limits become:
- Shoulder torque in bending (5,000 lb·ft).
- Hub winch and harness frame in tension (designed to several thousand pounds).
- The strength of whatever is wrapped.

**Doctrine: anchor first, then apply force.** An unanchored rig cannot out-push a strong person braced on good footing by very much.

### Strike Energy
- **Locked forearm swing:** About 8 lb of effective mass at 50 ft/s delivers about 310 ft·lb (420 J). Comparable to or above a full sledgehammer swing. The arm never breaks, so it can strike as hard as the actuators and pilot can tolerate.
- **Peak impact force:** Rigid-on-rigid contact lasts about 2 milliseconds. That swing peaks around 6,000 lb at contact.
- **Whip strike:** A tapered chain swung in a whip motion concentrates energy into the light tip, the same way a bullwhip tip breaks the sound barrier. The 48:1 taper allows very high tip speeds. The tip carries little energy but enormous pressure over a tiny area, so it lacerates rather than crushes.

---

## 7. Limitations of an Indestructible Material

Indestructible links remove one failure mode and move every other problem somewhere else.

### The Weakest Link Is Never the Link
Failure moves to:
- Tendons and locking cables (if ordinary material)
- Rubber pads and sleeves
- Motors, hydraulics and seals
- Sensors and fiber optics
- The hub and harness
- The pilot's body
- Whatever the arm is wrapped around

### No Energy Absorption
Infinite stiffness means zero flex. Every impact passes straight through the arm to the hub as a sharp spike. Without deliberate compliance, the pilot absorbs it. The hub needs series elastic elements (springs between actuators and links) and shock mounts.

### No Elastic Energy Storage
Real tentacles and muscles store energy in stretch and release it in strikes. Rigid links cannot. Any spring effect must come from springs in the actuators or tendons.

### Mass Still Exists
- Momentum and inertia make fast changes of direction expensive.
- **Reaction spin:** Swinging one 44 lb arm rotates the whole rig the other way unless another arm is anchored or a counter-swing balances it.

### Fixed Length
Rigid links cannot stretch or compress. Reach changes only by curling. Pulling an object closer along the arm's line requires curling the arm or reeling it into the hub. Fine sections can spool onto a drum. Coarse shoulder links cannot.

### Tendon Friction Loss
A tendon passing through bends loses tension exponentially: T_out = T_in × e^(−μ·Θ), where Θ is the total bend angle along its path.

| Total bend on tendon path | Low-friction routing (μ = 0.05) | Standard routing (μ = 0.15) |
|---|---|---|
| Half wrap (π) | 85% delivered | 62% delivered |
| One wrap (2π) | 73% delivered | 39% delivered |
| Two wraps (4π) | 53% delivered | 15% delivered |

This is why the wrist pod exists, why tendons need low-friction liners or tiny pulleys at every joint and why a tightly coiled arm loses strength at its tip.

### Manufacturing Is Permanent
- Nothing can be drilled, trimmed or adjusted after the links are made.
- Every tolerance error is permanent.
- Joints never wear in, so they must be perfect from the start.

### Surface Friction
- The bare material may be too slick to grip. Pads supply friction and can be damaged.
- If the bare surface happens to be grippy, retracting pads no longer reduces grip.

### Heat
- If the material conducts like a metal, fire heats the whole arm and that heat reaches internals and the pilot.
- Silicone pads fail around 200 to 230 °C. Polyurethane fails around 80 to 100 °C.
- Neodymium motor magnets begin losing strength around 80 to 150 °C.
- Ordinary fires run 600 to 1,000 °C.
- The shoulder needs a thermal break.

### Cold
Rubber pads stiffen and lose friction below roughly −20 to −40 °C.

### Electricity
A conductive arm touching a power line or struck by lightning routes current to the hub and pilot. The shoulder joint needs electrical insulation.

### Grit and Jamming
Fine joints at sand-grain scale jam. Small actuators may not generate enough force to crush a lodged grain.

### Noise
Rigid impacts ring. Pads and sleeves dampen sound for stealth.

### Air and Water Drag
- **Wind:** An extended arm presents about 6.7 ft² to the wind. A 50 mph gust pushes about 50 lb on it.
- **Underwater:** Water is about 830 times denser than air, so the same drag force allows only about 1/29 the speed. Strikes slow drastically.
- **Sinking:** At steel density the arms sink.

### The Pilot
- Humans tolerate brief accelerations of a few g comfortably. Hub acceleration should stay around 2 to 3 g for routine moves.
- Sudden stops from a rigid arm can injure the neck and spine. The harness needs head and neck support.

---

## 8. Cases and Circumstances

| Case | Limiting factor | Approach |
|---|---|---|
| Steel-frame building | Beam spacing | Wrap beams with forearm and wrist sections. Ideal terrain. |
| Glass skyscraper | No wrap points | Wrap window mullions, or drive the tip through glass to create anchor points. |
| Concrete wall | Concrete pullout strength | Wrap balconies, railings and columns. Driving the tip in like a piton holds hundreds to a couple thousand pounds depending on depth. |
| Tree | Trunk and branch strength | Wrap trunk with upper arm. Fingers wrap smaller branches. |
| Cliff | Crack geometry | Jam a knotted tip into a crack. A wedge locks itself when its half-angle is below arctan(μ), about 30 degrees for rubber on rock. |
| Ice or oily surfaces | Low friction | Many wraps (see table below). |
| Descending (rappel) | Speed control | Wrap a fixed object and let the arm slip under controlled tension. The capstan becomes a brake. |
| Catching a falling person | Their deceleration | Stop with controlled slip, never a locked arm (see below). |
| Stopping a car | Momentum | Wrap a strong anchor and slip-brake over distance (see below). |
| Lifting a car | Tipping and shoulder torque | Never crane-lift. Hang from overhead structure and winch in tension. |
| Restraining a person | Injury from pressure | Wide pads, low pressure, long contact area. Pin across joints so limbs can't slide free. |
| Disarming | Grip on the weapon | Wrap and pull in tension, where strength is unlimited. |
| Gunfire | Pilot coverage | Arms locked side by side form an indestructible shield. A rifle bullet's momentum barely moves the rig. |
| Explosion | Blast push | Overpressure of 10 psi on an 8 ft² shield pushes over 11,000 lb. Unanchored, the rig is thrown. Anchored, the hub needs shock absorbers. |
| Fine work (keys, switches, wiring, valves) | Precision | Splay-brace the wrist on the object, then work with filament tips. |
| Fire or power lines | Heat and current | Thermal break and insulation at the shoulder. Limit contact time. |
| Underwater | Drag and sinking | Slow deliberate movement. Wrap and pull rather than strike. |
| Fighting another indestructible rig | Their links can't be damaged | Target tendons, pads, actuators, hub and pilot. Wrap their arms to lock joints. |

### Wraps Needed by Surface (100× holding ratio)

| Surface | Typical μ | Wraps needed |
|---|---|---|
| Rubber pad on dry concrete or rough metal | 0.8 | ~0.9 |
| Rubber pad on dry smooth steel | 0.6 | ~1.2 |
| Wood or bark | 0.5 | ~1.5 |
| Wet metal | 0.3 | ~2.4 |
| Ice or oily surface | 0.1 | ~7.3 |
| Greased surface | 0.05 | ~14.7 |

Formula: wraps = ln(ratio) ÷ (2π·μ). The tip only has to hold the load divided by the ratio, so a finger easily maintains the grip.

### Catching a Falling Person (30 ft fall, 44 ft/s at impact)

| Stopping distance | Deceleration |
|---|---|
| A few inches (locked arm) | 50+ g |
| 1 ft | 30 g |
| 3 ft | 10 g |
| 6 ft | 5 g |
| 10 ft | 3 g |

Controlled slip over 6 to 10 ft keeps it survivable.

### Stopping a Car (3,500 lb at 30 mph)
Kinetic energy is about 105,000 ft·lb.

| Stopping distance | Average force |
|---|---|
| 10 ft | ~10,500 lb |
| 30 ft | ~3,500 lb (1 g) |

Many highway light poles are designed to break away on impact, so the anchor should be a building column or other heavy structure, not a streetlight.

---

## 9. Actuators and Control

### Per Arm
- **Shoulder:** Two-axis hydraulic rotary actuators plus a rotation actuator. A 2 in bore piston at 3,000 psi produces about 9,400 lb of force.
- **Upper arm, forearm, wrist:** Three or four tendons each, pulled by ball-screw actuators in the hub. Tendon travel is small (1.6 in offset × 90 degrees = 2.5 in), so screws provide high force at modest speed.
- **Wrist pod:** About 15 micro actuators driving finger and filament tendons, plus cameras and the local controller.
- **Locking cables:** One per section. Slack for limp, tight for rigid.
- **Series elastic elements:** Springs between the shoulder actuators and links to absorb impacts and measure force.
- **Total:** About 30 actuators per arm, about 120 for the rig.

### Control Layers
1. Pilot intent (move, climb, grab, strike, shield).
2. Mode selection (walk, wrap, climb, strike and the rest; see `TentacleMotionModes.md`).
3. Pattern generators for rhythmic motion.
4. Shape control from fiber shape sensing.
5. Tendon and joint control.
6. Safety limits: pressure caps on living targets, acceleration caps for the pilot, anchoring checks before high-force actions.

---

## 10. Power

### Climbing
- Lifting 470 lb up a 100 ft building takes about 47,000 ft·lb, roughly 18 Wh.
- At 30 percent system efficiency, about 60 Wh. Climbing is cheap.

### Holding
- Zero power with joints locked.

### Peak Output
- Lifting 470 lb at 3 ft/s: about 1.9 kW.
- Combat strikes: 3 to 5 kW bursts per arm.
- Whole system peak: 15 to 20 kW.

### Endurance
- Average combat use: 2 to 3 kW.
- One hour needs 2 to 3 kWh. Lithium-ion at about 250 Wh/kg means roughly 10 to 12 kg (about 25 lb) of battery.
- An electric motor drives the hydraulic pump. Tendon actuators run directly on electric power.

---

## 11. Pseudo-Magic Version

Magic replaces the power source and selected components. The physics rules stay in force, which keeps the design grounded.

### Rules That Keep It Grounded
- **Mana converts to torque at a joint only, never to free force.** That rule is why the rig climbs instead of flies.
- **Fixed output.** The mana core has a peak rating (for example 20 kW) and a capacity, the same as a battery.
- **Newton still applies.** Reaction forces, momentum, friction and anchoring all work exactly as above.

### Component Replacements
| Tech component | Magic replacement |
|---|---|
| Battery | Mana core |
| Hydraulics and tendons | Runic joint actuators at each link |
| Locking cable | Locking rune: rigid on command, no upkeep |
| Rubber pads | Friction rune on inner faces, flips to a cutting edge |
| Shape sensing fiber | Link-sense enchantment reporting every joint angle |
| Series elastic springs | Absorption rune converting impact into heat or stored mana |

### What Magic Solves
- Tendon friction loss disappears because each link drives itself.
- Actuated size limit disappears, so filament tips can be actuated down to bristle scale.
- Wrist pod becomes unnecessary.

### What Magic Doesn't Solve
- Anchoring and reaction forces.
- Pilot g-limits.
- Weight and momentum.
- Heat and current conducted through the links.
- Anti-magic effects. A mechanical locking cable as backup keeps the arms from collapsing if runes fail.

---

## 12. Most Effective Combat Setup

- **Arm count:** Four minimum. Six is better: three anchor or walk while three fight, and the stable tripod never breaks.
- **Three arm states:**
  - Limp: wrapping, grappling, climbing.
  - Locked: spear, beam, bridge, shield strut.
  - Flexing: walking, striking.
- **Use each section for its strength:**
  - Shoulder and upper arm: lifting, anchoring, heavy wraps.
  - Forearm and wrist pod: strikes and pushing.
  - Fingers: grip, disarm, manipulate.
  - Filament tips: fine work, threading, sensing, whip strikes.
- **Pads in or out:** grip or cut.
- **Shield mode:** Two arms locked side by side form an indestructible wall.
- **Anchor before force:** Every high-force action starts with another arm wrapping structure.
- **Reflex layer:** Pre-programmed modes run automatically. The pilot gives intent, not joint commands.
- **Pilot protection:** Indestructible frame around the torso, shock-mounted hub, head and neck support, hub acceleration capped around 2 to 3 g.
