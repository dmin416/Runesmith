# Wheels: Types, Science, Tradeoffs and Wild Builds

> Earth reference / invent loot. Not locked law. Era / Caldris wheel tech ladder: `Wheels.md`. Vehicle families: `VehicleTypes.md`. Legs / wheel-legs: `LeggedVehicles.md`. Auto tires invent: `MechanicalCarComponents.md`. Fat-tire bike sizing: `FatTireBike.md`. Roads / trail surfaces: `Roads.md`, `../Invent/TrailBuilding.md`. Suspension: `Suspension.md`.

Nav: `Index.md`.

All figures are typical engineering values. Real numbers shift with surface, temperature, tire model and build quality.

---

## 1. The Physics That Decides Everything

Every wheel design is a trade among seven forces and effects. Once these are clear, every "which wheel is best" question answers itself.

### 1.1 Rolling Resistance

Rolling resistance force:

```
F_rr = Crr × N
```

- `Crr` = coefficient of rolling resistance (dimensionless)
- `N` = normal load (weight on the wheel, in newtons)

The main cause is **hysteresis**. Rubber or urethane deforms as it enters the contact patch and does not give all that energy back as it leaves. The lost energy becomes heat. Harder material, thinner casing and higher pressure mean less deformation, so lower Crr on smooth ground.

On rough ground the rule flips. A rock-hard tire bounces the whole vehicle and rider over every bump. That vertical motion gets absorbed by flesh, frame and suspension as **impedance losses**. Bicycle tire testing on rough chipseal has shown that supple tires at moderate pressure roll faster than hard tires at maximum pressure. There is an optimum pressure for each surface.

**Power cost:**

```
P = Crr × m × g × v
```

Example: 90 kg bike plus rider at 30 km/h (8.33 m/s):
- Fast road tire, Crr 0.004: about **29 W**
- Knobby MTB tire on pavement, Crr 0.015: about **110 W**

That gap is why road bikes feel effortless and mountain bikes on pavement feel like riding through syrup.

**Approximate Crr values:**

| Wheel / Surface | Crr |
|---|---|
| Steel train wheel on steel rail | 0.001 to 0.002 |
| High-end road bike tire, smooth asphalt | 0.0025 to 0.004 |
| Low rolling resistance car tire | 0.006 to 0.008 |
| Inline skate urethane, smooth concrete | 0.005 to 0.015 |
| Normal car tire, asphalt | 0.008 to 0.014 |
| Go-kart slick, asphalt | 0.010 to 0.015 |
| Golf cart turf tire, pavement | 0.012 to 0.020 |
| Knobby MTB tire, pavement | 0.008 to 0.020 |
| Fat bike tire, pavement | 0.012 to 0.025 |
| ATV tire, pavement | 0.020 to 0.040 |
| Any tire, packed dirt | 0.03 to 0.08 |
| Any tire, loose sand | 0.10 to 0.30 |

Surface matters more than the wheel. A road tire in sand is worse than a fat tire in sand by a huge margin.

### 1.2 Contact Patch and Inflation Pressure

For a pneumatic tire, a simple approximation:

```
Contact area ≈ Load ÷ Inflation pressure
```

The air pressure is what holds the load. The casing adds a little stiffness on top.

| Vehicle | Load per tire | Pressure | Approx. contact patch |
|---|---|---|---|
| Road bike rear | 55 kg (120 lb) | 90 psi | 1.3 in² (8.5 cm²) |
| Mountain bike rear | 55 kg (120 lb) | 25 psi | 4.8 in² (31 cm²) |
| Fat bike rear | 55 kg (120 lb) | 8 psi | 15 in² (97 cm²) |
| Car corner | 450 kg (1000 lb) | 32 psi | 31 in² (200 cm²) |
| ATV corner | 90 kg (200 lb) | 5 psi | 40 in² (260 cm²) |

Key consequence: **ground pressure roughly equals tire pressure.** A car presses on the ground at about 32 psi (220 kPa). An ATV at 5 psi presses at about 35 kPa. This number is what decides whether you sink.

**Ground pressure comparison:**

| Thing | Approx. ground pressure |
|---|---|
| Road bike tire | 600+ kPa (90+ psi) |
| Car tire | 200 to 250 kPa |
| Main battle tank (tracked) | 80 to 110 kPa |
| Fat bike tire | 35 to 70 kPa |
| ATV tire | 25 to 50 kPa |
| Adult human standing | 15 to 25 kPa |
| Ultra low pressure "Rolligon" / terra tire | 7 to 15 kPa |
| Snowmobile | 3 to 5 kPa |

A 60-ton tank presses on soil less than half as hard as a family car because its tracks spread the load. Ground pressure, not weight, decides flotation.

### 1.3 Obstacle Climbing: Why Diameter Is King

Picture a rigid wheel of radius `r` rolling into a step of height `h`. The horizontal force needed at the axle to lift the wheel over the edge, as a fraction of the load on that wheel:

```
F / W = √( h × (2r − h) ) ÷ (r − h)
```

When `h` approaches `r`, the force goes to infinity. **A wheel cannot be pushed over a step equal to or taller than its radius.** It can only be driven over with grip on the face of the obstacle, or lifted.

**Force needed as a fraction of wheel load (rigid wheel model):**

| Wheel | Diameter | 10 mm step (pebble / crack) | 50 mm step (rock / curb lip) |
|---|---|---|---|
| Skateboard | 54 mm | **1.23** (dead stop, rider launched) | Impassable |
| Inline skate | 80 mm | **0.88** (near stop) | Impassable |
| Go-kart | ~280 mm (11 in) | 0.40 | 1.19 |
| Golf cart | ~457 mm (18 in) | 0.31 | 0.80 |
| ATV | ~635 mm (25 in) | 0.26 | 0.64 |
| Car | ~660 mm (26 in) | 0.25 | 0.62 |
| 700c / 29er bike | ~680 mm (27 in) | 0.25 | 0.61 |
| Rock crawler | ~1070 mm (42 in) | 0.20 | 0.47 |
| Giant wheel | 1500 mm (59 in) | 0.17 | 0.39 |

Reading the table: a 10 mm pebble requires an inline skate to supply a horizontal shove equal to 88 percent of the weight on that wheel. That is why a tiny pebble throws skaters forward. A bike wheel needs only 25 percent for the same pebble. A giant wheel needs 17 percent.

**Pneumatic tires cheat this math.** A soft tire wraps around (envelops) the obstacle so the effective step is smaller. This is why airing down off-road helps so much: the tire swallows rocks instead of climbing them.

### 1.4 Rotating Mass and Inertia

A wheel both moves forward and spins. Its effective mass during acceleration:

```
m_eff = m + I / r²
```

For a thin hoop (rim and tire), `I = m r²`, so **every kilogram at the rim acts like two kilograms when accelerating.** Mass at the hub adds almost nothing extra. This is why light rims matter for bikes and why giant wheels with heavy rims are sluggish to start and stop.

Inertia also stores energy. Once a heavy large wheel is spinning, it carries momentum through rough patches and smooths out speed. Good for cruising, bad for sprinting and braking.

### 1.5 Unsprung Mass

Unsprung mass is everything below the suspension: wheel, tire, brake, hub, part of the arm. When a heavy wheel hits a bump it flies upward with more momentum, then rebounds hard. Tire contact force fluctuates, so grip and comfort drop. Lighter wheels track the ground better. Car wheel hop resonance is typically around 10 to 15 Hz.

### 1.6 Traction

**On pavement:** `F_max ≈ μ × N`. Rubber grip comes from two mechanisms:
- **Adhesion**: molecular bonding between rubber and surface
- **Hysteresis**: rubber flowing around micro-bumps in the surface and resisting the flow

Soft rubber can exceed μ = 1.0. Racing slicks can exceed 1.5 when hot. On dry pavement a **slick tire grips best** because it has the most rubber touching the road. Tread exists to move water, mud and snow out of the way.

**On soil:** traction comes from shearing the soil itself. Soil shear strength follows the Mohr-Coulomb relation:

```
τ = c + σ × tan(φ)
```

- `c` = cohesion (sticky clay has high c; dry sand has near zero)
- `σ` = normal pressure
- `φ` = internal friction angle of the soil

Implications:
- In **clay and mud** (high cohesion), traction scales with contact **area**. Big footprints win.
- In **dry sand** (zero cohesion), traction scales with **load**. Weight on the driven wheels wins.
- **Lugs** dig in so the tire shears a block of soil instead of sliding across the top.

**Sinkage (Bekker model):**

```
p = (k_c / b + k_φ) × z^n
```

- `p` = ground pressure, `b` = tire width, `z` = sinkage depth
- `k_c`, `k_φ`, `n` = soil constants

Wider tires shrink the `k_c / b` term, so they sink less. Lower pressure lowers `p`. Both reduce sinkage, which reduces the "bulldozing" resistance of pushing a rut ahead of the wheel.

**Narrow versus wide nuance:** In shallow mud over a firm base, narrow tires cut down to the hard layer and grip it. Ford Model T owners on dirt roads benefited from this. In deep soft soil, sand or snow with no firm base, wide low-pressure tires float on top. Pick by what lies beneath the slop.

### 1.7 Hydroplaning

NASA's Horne equation estimates the speed where a tire rides fully on a water film:

```
V (knots) ≈ 9 × √(tire pressure in psi)
```

A car tire at 32 psi: about 51 knots, roughly **59 mph (95 km/h)**. A bike tire at 90 psi: about 85 knots, roughly 98 mph. Bikes effectively cannot hydroplane at human speeds because their pressure is so high and their contact patch so narrow and rounded. Worn tread lowers the real-world threshold for cars significantly.

### 1.8 Stability and the Gyroscope Myth

Spinning wheels have angular momentum `L = Iω` and resist tilting. For bicycles this effect is real but minor. A 2011 study in *Science* (Kooijman et al.) built a bicycle with counter-spinning wheels canceling gyroscopic effects and zero trail. It still balanced itself. Self-stability comes mainly from mass distribution and steering geometry. Gyroscopic effects matter more for heavy wheels at high speed (motorcycles, monowheels).

### 1.9 How a Spoked Wheel Actually Works

A bicycle wheel is a **prestressed tension structure**. Every spoke is tightened to roughly 1000 to 1200 N (100 to 120 kgf). When loaded, the hub does not hang from the top spokes. Instead, the few spokes near the ground **lose some tension**, and that imbalance supports the hub. The rim stays in compression the whole time.

Results:
- A wheel of about 1 to 2 kg routinely carries 100+ kg. Strength to weight is extraordinary.
- **Radial strength is huge. Lateral strength is weak.** Side stiffness comes only from the bracing angle: how wide the hub flanges are compared to the rim radius. A big rim on a narrow hub has a shallow angle and folds sideways easily ("taco-ing").
- Smaller diameter wheels with wide hubs are much stiffer sideways. BMX and 20-inch trike wheels are far tougher laterally than 29-inch wheels.

Bicycles and motorcycles **lean into turns**, so cornering forces stay mostly in the plane of the wheel where it is strong. Vehicles that do not lean (cars, golf carts, skateboards, trikes) push sideways on their wheels in every turn. That single fact drives most of the "can I swap in bike wheels" answers below.

### 1.10 Wheel Materials

| Type | Examples | Strengths | Weaknesses |
|---|---|---|---|
| Pneumatic (air) | Bike, car, ATV | Comfort, envelopment, adjustable pressure, low Crr | Flats, maintenance |
| Solid rubber | Industrial carts, forklifts | Cannot puncture, cheap | Harsh, heavy, high Crr |
| Polyurethane | Skates, skateboards, scooters | Durable, rebound, tunable hardness | Tiny diameter, no envelopment |
| Airless spoke (Michelin Tweel type) | UTVs, skid steers, mowers | Flat-proof, some compliance | Heat buildup at speed, heavy, costly |
| Steel | Trains, tractors (some) | Lowest Crr on rails | No grip on most surfaces |

**Urethane hardness (durometer, A scale):**
- 74A to 80A: soft, grippy, smooth over rough asphalt, slower on smooth floors
- 82A to 88A: all-around, indoor rinks, parks
- 95A to 101A: hard skate park and street skateboard wheels, slide easily, feel every crack

---

## 2. The Wheel Types

### 2.1 Bicycle Wheels

**Sizes (ISO bead seat diameter):**
- 700c / 29er: 622 mm
- 650b / 27.5: 584 mm
- 26 inch: 559 mm
- 24 inch, 20 inch BMX (406 mm), 16 inch
- 36er (giant touring and unicycle wheels): 787 mm

**Tire widths:** 23 to 32 mm road, 35 to 50 mm gravel, 2.2 to 2.6 in mountain, 3.8 to 5 in fat bike.

**Pressure:** 70 to 110 psi road, 30 to 45 gravel, 18 to 30 mountain, 5 to 15 fat bike.

**Pros:**
- Best strength to weight of any wheel built
- Very low rolling resistance in road form
- Large diameter rolls over obstacles well
- Cheap, repairable, standard parts everywhere
- Huge range from razor-thin road to snow-floating fat

**Cons:**
- Weak against side loads unless the vehicle leans
- Low load capacity per wheel by vehicle standards (roughly 100 to 150 kg typical)
- Narrow road versions sink in anything soft
- Pinch flats at low pressure on rocks unless tubeless

**Best for:** human-powered transport, light electric vehicles that lean, anything where efficiency per watt matters.

### 2.2 Inline Skate Wheels

**Sizes:** 72 to 125 mm diameter. Recreational 76 to 84 mm, speed and urban 100 to 125 mm.

**Construction:** polyurethane tire bonded to a plastic or aluminum core, two 608 bearings.

**Pros:**
- Light and compact, so the skater stays agile
- Low rolling resistance on smooth surfaces
- Excellent grip and rebound with quality urethane
- Bigger 110 to 125 mm wheels make urban skating far smoother and faster

**Cons:**
- Tiny diameter: a 5 to 10 mm pebble can stop a wheel dead (see Section 1.3)
- No envelopment, so every crack transmits straight to the feet
- Useless on grass, gravel, sand, mud
- Wear fast on rough asphalt

**Best for:** smooth pavement, rinks, trails paved in good condition. Bigger wheel equals more forgiving.

**Off-road variant:** pneumatic "all-terrain skates" use 150 to 200 mm air tires. They handle grass and dirt paths but are heavy and tall.

### 2.3 Go-Kart Wheels

**Sizes:** 5 or 6 inch rims. Common tires: 10 × 4.50-5 front, 11 × 7.10-5 rear for racing; 13 × 5.00-6 and 13 × 6.50-6 for recreational and yard karts.

**Pressure:** racing slicks around 9 to 15 psi; rec karts somewhat higher.

**Physics notes:**
- Racing karts have **no suspension** and a **solid rear axle** with no differential. Both rear wheels must turn at the same speed, so the inside rear tire scrubs in a turn. Kart chassis are designed to flex so the inside rear wheel lifts slightly, letting the kart turn.
- Short sidewalls and wide footprint give strong lateral grip and fast steering response.

**Pros:**
- Massive grip for size on smooth pavement
- Low center of gravity
- Light, cheap, fast to swap
- Precise steering

**Cons:**
- Small diameter, poor over bumps and holes
- Minimal cushioning (the tire is the suspension)
- Racing slicks wear out in hours
- Poor in grass, gravel, sand

**Best for:** pavement and smooth tracks. Knobby 13-inch "turf" or "ATV-style" kart tires extend this to yards and dirt.

### 2.4 Golf Cart Wheels

**Sizes:** 8, 10, 12 and 14 inch rims. Standard tire 18 × 8.50-8. Lifted carts run 20 to 23 inch tall all-terrain tires on 10 to 14 inch rims.

**Pressure:** about 18 to 22 psi for standard turf tires.

**Load:** a 4-ply load range B golf cart tire carries roughly 250 kg (550 lb).

**Design goal:** protect grass. Turf-saver tires have wide, shallow, rounded tread so they do not tear sod.

**Pros:**
- Low ground pressure protects lawns
- Wide stable footprint for a top-heavy vehicle
- Cheap and widely available
- Handle the weight of a 450 to 550 kg cart plus passengers

**Cons:**
- Smallish diameter limits obstacle and rut handling
- Turf tread is poor in mud
- Not rated for high speed (most are designed for about 15 to 25 mph)

**Best for:** golf courses, neighborhoods, campgrounds, flat property.

### 2.5 Off-Road ATV Wheels

**Sizes:** typical 25 × 8-12 front and 25 × 10-12 rear. Sport and mud machines go to 26 to 30 inches.

**Pressure:** 4 to 7 psi. Many have a pressure gauge that reads only to 15 psi.

**Construction:** bias-ply or radial, 6-ply to 8-ply for puncture resistance, deep lugs (0.75 to 1.5+ inches).

**Tread types:**
- **Mud:** tall widely spaced lugs that self-clean by flinging mud off as they spin
- **All-trail:** medium lugs, tighter spacing
- **Sand:** paddle tires with scoops on the rear, smooth rib on the front
- **Rock / desert:** dense tread, tough sidewalls

**Pros:**
- Very low ground pressure, excellent flotation
- Big soft tires swallow rocks and roots
- Deep lugs shear soil efficiently
- Strong enough for jumps and heavy loads

**Cons:**
- High rolling resistance and fast wear on pavement
- Vague, wandering steering on hard surfaces
- Low pressure means the bead can unseat in hard sideways hits unless using beadlock rims

**Best for:** trails, farms, mud, woods, sand dunes, snow.

### 2.6 Car Tires

**Construction:** radial ply casing, steel belts under the tread, nylon cap ply, bead wires. Tread compounds use silica for wet grip with lower hysteresis.

**Sizes:** 15 to 22 inch rims, overall diameter usually 24 to 30 inches. Sidewall markings: e.g., 225/45R17 91V = 225 mm wide, sidewall height 45 percent of width, radial, 17 inch rim, load index 91 (615 kg), speed rating V (149 mph / 240 km/h).

**Pressure:** 30 to 36 psi typical.

**Pros:**
- Engineered for high speed, heavy loads and long life (often 40,000 to 80,000+ miles)
- Excellent wet and dry grip
- Low rolling resistance for their load
- Predictable handling, good comfort

**Cons:**
- Heavy
- Too high pressure for soft terrain unless aired down
- Expensive to replace in sets

**Variants:** all-terrain (A/T), mud-terrain (M/T), winter (soft compound, many sipes, works below 7°C / 45°F where summer rubber hardens), performance summer.

**Best for:** roads at speed. Nothing else is close at 70 mph.

### 2.7 Giant Bike Wheels

Examples: penny-farthing (high wheeler) front wheels of 48 to 60 inches, 36-inch wheels on touring unicycles and some bikes, novelty "big wheel" bikes, monowheels where the rider sits inside a giant wheel.

**The penny-farthing logic:** with direct pedal drive, one pedal revolution equals one wheel revolution. Bigger wheel means more distance per stroke. A 60-inch wheel travels about 4.8 m (15.7 ft) per pedal turn. Modern bikes use chains and gears to get the same effect with normal-size wheels, which is why high wheelers vanished after the "safety bicycle" arrived in the late 1880s.

**Pros:**
- Rolls over cracks, roots and potholes with ease (see table in 1.3)
- Very smooth ride on rough roads
- Carries momentum well
- Commanding view

**Cons:**
- Heavy rim inertia: slow to accelerate, hard to brake
- Huge side area catches crosswinds
- Lateral weakness gets worse as diameter grows; needs more spokes, wider hubs or deeper rims
- High riding position means high center of gravity: penny-farthing riders were famous for pitching over the front ("taking a header")
- Hard to mount, store and transport
- Monowheels have a unique problem: braking or accelerating hard makes the rider swing around inside the wheel ("gerbiling")

**Best for:** novelty, rough roads with low speeds, showing off. Engineering-wise, 29 to 36 inches is close to the practical upper limit for a person-sized vehicle.

---

## 3. Master Comparison

| Wheel | Typical OD | Pressure | Crr (pavement) | Obstacles | Soft ground | Speed potential | Side-load strength | Load per wheel |
|---|---|---|---|---|---|---|---|---|
| Inline skate | 3 to 4.5 in | Solid | Low on smooth | Very poor | None | Medium | High (tiny wheel) | 20 to 40 kg |
| Bike (road) | 27 in | 80 to 110 psi | Very low | Good | Poor | High | Weak | 100+ kg |
| Bike (MTB / fat) | 27 to 30 in | 5 to 30 psi | Medium | Very good | Good to excellent | Medium | Weak to medium | 100 to 150 kg |
| Go-kart | 10 to 13 in | 9 to 15 psi | Low to medium | Poor | Poor | High (pavement) | Strong | 50 to 100 kg |
| Golf cart | 18 to 23 in | 18 to 22 psi | Medium | Fair | Fair | Low | Strong | ~250 kg |
| ATV | 25 to 30 in | 4 to 7 psi | High | Very good | Excellent | Medium | Strong | 150 to 250 kg |
| Car | 25 to 30 in | 30 to 36 psi | Low | Good | Fair (better aired down) | Very high | Very strong | 500 to 800 kg |
| Giant bike wheel | 36 to 60 in | Varies | Low | Excellent | Fair | Medium | Very weak | ~100 kg |

---

## 4. What Is Best for What

| Situation | Best wheel | Why |
|---|---|---|
| Fast, efficient human travel on roads | Road bike wheel | Lowest Crr, light rim, large diameter |
| Smooth rinks and new pavement | Inline skate 80 to 110 mm | Light, agile, low resistance on smooth surfaces |
| Cracked urban sidewalks (skating) | Biggest inline wheels (110 to 125 mm), soft 80A to 85A | Diameter and softness absorb cracks |
| Tight paved racing | Go-kart slicks | Max grip, low CG, instant steering |
| Lawns without damage | Golf cart turf tires | Low ground pressure, gentle tread |
| Mud, woods, trails | ATV mud tires | Flotation plus self-cleaning lugs |
| Sand and snow | Fat bike (human power), ATV paddle or wide low-psi tires (motor) | Lowest ground pressure |
| Highway speed | Car radials | Only design rated and built for it |
| Potholes and broken roads at low speed | Large diameter bike / 36er | Diameter climbs everything |
| Rock crawling | 37 to 42 in tires, aired to 5 to 10 psi, beadlocks | Diameter plus envelopment |
| Max flat-proof reliability | Airless (Tweel-type) or solid | Cannot puncture |

There is no universal best wheel. **Diameter** fights obstacles. **Width and low pressure** fight sinking. **Hardness and high pressure** fight rolling resistance on smooth ground. **Lean or stiff hub geometry** fights side loads. Every design picks its priorities.

---

## 5. Skateboard With Bike Wheels

**Yes, it can be done.** It already exists in several forms.

### 5.1 Existing Proof
- **Mountainboards:** skateboard-style decks with 8 to 10 inch pneumatic tires on wide, spring-damped "channel trucks." Ridden down grass hills, dirt trails and ski slopes in summer.
- **Dirtsurfer-style boards:** a long frame with two bicycle-type wheels in line, front and rear, with the rider standing on a deck slung between them. Steering comes from leaning, which twists the front wheel.
- **Onewheel:** a self-balancing electric board using a single go-kart-type tire (roughly 11 inches tall) in the middle of the deck.
- **Kick scooters / footbikes:** standing platforms between a large front bike wheel (up to 28 inches) and a smaller rear wheel. Proof that a standing rider works fine with full-size bicycle wheels.

### 5.2 The Engineering Problems With Bolting Bike Wheels on Trucks

**1. Axle mounting.** Skateboard trucks hold wheels on a cantilevered 8 mm axle stub. Bicycle hubs are designed to be clamped on both sides by a fork or frame. Solutions:
- Use cantilever-style hubs from wheelchairs, some trikes or single-sided scooter designs
- Build a small yoke on each side so the wheel is held on both ends

**2. Deck height and lean steering.** Skateboard trucks steer by leaning: tilting the deck rotates the axle. The turning radius is roughly:

```
R ≈ Wheelbase ÷ (2 × tan(steer angle))
```

Large wheels force the deck either very high (center of gravity rises, board becomes tippy) or require deep cutouts so the deck clears the tires when leaned. A deck at 16 to 20 inches off the ground with lean steering is unstable.

Better layout: **drop the deck between the wheels**, like a cart or the Dirtsurfer frame, keeping the rider's feet low while the axles sit high.

**3. Side loads.** A skateboard does not lean its wheels. The deck leans but the wheels stay mostly upright, so every carve pushes sideways on the wheels. A 29-inch spoked wheel with a narrow hub will flex and eventually fold. A **16 or 20 inch BMX wheel** with 36 to 48 spokes and wide hub flanges is laterally stiff enough for a rider of normal weight.

**4. Weight.** Four 20-inch BMX wheels with tires weigh around 8 to 10 kg total. Not light, but rideable.

### 5.3 Verdict
- **Practical sweet spot:** 8 to 10 inch pneumatic (mountainboard) or 12 inch kid-bike wheels.
- **Big-wheel monster board:** 16 to 20 inch BMX wheels, drop-deck frame, wide-flange hubs, through-axles, linkage or lean steering. Rolls over almost anything a person can walk over. Rides like a stand-up quad cart more than a skateboard.
- **Avoid:** full 26 to 29 inch wheels on four-wheel boards. Too tall, too weak sideways, too heavy.

---

## 6. Golf Cart With Bike Wheels

### 6.1 The Load Math

- Typical electric golf cart: 450 to 550 kg (1000 to 1200 lb) with batteries
- Plus two adults: about 160 kg
- Total: about 650 to 700 kg, so **roughly 170 kg per wheel** static
- Bumps and potholes: dynamic loads 2 to 3 times static, so **350 to 500 kg peaks**
- Cornering at 0.4 g: lateral force about 70 kgf on an average wheel, more on the outside wheels due to weight transfer

A typical bicycle wheel is designed for roughly 100 to 150 kg **radial** with the vehicle **leaning**. A golf cart does not lean. Every corner shoves sideways on the wheels. A standard bike wheel would:
1. Overload radially on bumps
2. Taco sideways in the first brisk turn
3. Burst or pinch-flat the tire under the load

There is also no mounting interface. Golf carts use a 4-bolt hub pattern (4 × 4 inch, 101.6 mm) with 1/2 inch or 12 mm studs. Bike hubs have no bolt pattern at all.

### 6.2 How It Could Work

**Option A: Lighten the vehicle drastically.** A custom ultralight electric quad built from aluminum tube, lithium batteries and a single seat could total under about 250 kg with rider. That is roughly 60 kg per wheel. With heavy-duty wheels it becomes viable. Recumbent trikes and quadricycles already do this.

**Option B: Use the right "bike" wheels.**
- **20 inch trike or cargo bike wheels:** dished wide hubs, 13 or 12 gauge spokes, 36 to 48 spokes, strong double-wall rims. Designed for non-leaning side loads.
- **Moped or motorcycle spoked wheels:** look like big bike wheels, thicker spokes, rated for 150 to 200+ kg each, real brakes, real bearings. This is the best route for the "big skinny spoked wheel" look on a real cart.
- **Automotive wire wheels:** classic sports cars used spoked wheels for decades. They work because spoke gauge, count and hub flange spread are scaled up for side loads.

**Option C: Get the look without the problem.** Use 14 inch golf cart rims with tall, narrow tires and a lift kit.

### 6.3 Effects of Tall, Narrow Wheels on a Cart
- **Better:** obstacle rolling, lower rolling resistance on pavement, less battery drain, more ground clearance
- **Worse:** higher ground pressure tears turf, sinks in soft sand, higher center of gravity raises rollover risk, much more steering leverage on the linkage, gearing goes taller so hill climbing torque drops

### 6.4 Verdict
- Stock golf cart plus standard bike wheels: will fail.
- Ultralight custom cart plus heavy-duty 20 inch trike wheels: works.
- Normal-weight cart plus motorcycle spoked wheels and custom hubs: works and looks the part.

---

## 7. Wild Off-Roading

### 7.1 What Wins Off-Road, in Order of Importance

**1. Ground pressure.** If you sink, nothing else matters. Lower pressure and bigger footprints come first.

**2. Diameter.** Taller wheels climb bigger steps, improve approach and departure angles and bridge holes.

**3. Envelopment and sidewall flex.** Aired-down tires mold around rocks. Rock crawlers run 37 to 42+ inch tires at 5 to 10 psi with beadlock rims so the bead cannot pop off.

**4. Keeping all wheels loaded.** Suspension articulation lets each wheel stay pressed down on twisted terrain. A wheel in the air does nothing. Locking differentials ensure the wheels that do touch get power.

**5. More wheels.** 6×6 and 8×8 machines spread load and keep traction when one wheel dangles.

**6. Tread matched to terrain:**

| Terrain | Tread | Pressure strategy |
|---|---|---|
| Deep mud | Tall, wide-spaced lugs, self-cleaning | Moderate, rely on lug depth |
| Rock | Sticky compound, dense tread, armored sidewalls | Very low with beadlocks |
| Sand | Paddles (rear), ribbed (front), or smooth balloon | Low (trucks often 12 to 15 psi) |
| Snow | Wide, siped, aggressive edges | Very low |
| Tundra / swamp | Balloon or terra tires | 1 to 3 psi |

### 7.2 The Best Off-Road Systems

**Large balloon / terra tires:** amphibious 6×6 and 8×8 machines run tires at 1 to 3 psi. Ground pressure falls below a walking human's. They float across bog and snow and even swim.

**Rocker-bogie suspension (Mars rovers):** each side has a rocker arm and a bogie arm, no springs, all six wheels stay in contact. NASA's Curiosity has 50 cm (20 in) aluminum wheels and is rated to climb obstacles about 65 cm (25 in) high, taller than its wheels. Curiosity's wheels later suffered punctures from sharp rocks, so Perseverance received narrower, thicker wheels with curved treads.

**Tracks:** spread load over a long footprint for the lowest ground pressure of any rolling system. Articulated tracked carriers (two linked tracked units) such as the Hägglunds Bv206 press on snow more lightly than a person on foot. Costs: heavy, slower, more complex, thrown tracks, high maintenance.

**Airless tires:** flat-proof in thorn and rock country. Run hot at sustained high speed.

### 7.3 Off-Road Ranking for Truly Wild Terrain

1. **Articulated tracks or 8×8 balloon tires:** swamp, snow, tundra, mud
2. **Big aired-down tires on long-travel suspension with lockers:** rock, mixed trail, desert
3. **Rocker-bogie multi-wheel:** slow rough rocky ground, no springs to fail
4. **Wheel-legs (Section 8):** steep slopes, ledges, gaps, terrain nothing else reaches

---

## 8. Articulated Arms (legged machines)

Full treatment: `LeggedVehicles.md` (wheel-legs, spider platforms, tradeoffs).

---

## 9. Vehicle Category Breakdown

Full treatment: `VehicleTypes.md` (bikes through cars, tanks, snow, energy/cost matrix).

---

## 10. Quick Verdicts

- **Best all-around wheel ever designed for efficiency:** the spoked bicycle wheel
- **Best for highway speed and load:** car radial
- **Best for soft or wild ground (wheeled):** big, wide, aired-down ATV or terra tire on articulated suspension
- **Best for lawns:** golf cart turf tire
- **Best for pavement grip per size:** go-kart slick
- **Worst at obstacles:** skateboard and inline skate wheels (diameter is too small)
- **Skateboard with bike wheels:** yes, with 16 to 20 inch BMX wheels, a drop deck and stiff hubs; mountainboards are the proven version
- **Golf cart with bike wheels:** only if the cart is ultralight and the wheels are heavy-duty trike or motorcycle spoked wheels
- **Wild off-roading:** tracks or 8×8 balloon tires for soft ground, aired-down 37 to 42 inch tires with lockers for rock
- **Giant spider legs:** possible and real; slow and complex; **wheels on articulated legs** gives the best of both worlds and already works on walking excavators and planetary robots
- **Most efficient vehicle overall:** bicycle, with e-bikes close behind for real-world commuting
- **Best do-everything personal off-roader:** utility UTV for cargo and safety, utility ATV for tight trails and lower cost
- **Fastest across rough ground:** trophy truck and sport UTV
- **Goes where nothing else goes:** articulated tracked carrier for soft ground, trials bike for rock, walking excavator for slopes
- **Cheapest real motorsport:** 4-stroke sprint go-kart
- **Best neighborhood runabout:** lithium electric golf cart or street-legal LSV
