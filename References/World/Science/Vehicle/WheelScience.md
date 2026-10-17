# Wheels: Types, Science, Tradeoffs and Wild Builds

> Earth reference / invent loot. Not locked law. Era / Caldris wheel tech ladder: `Wheels.md`. Auto tires invent: `MechanicalCarComponents.md`. Fat-tire bike sizing: `FatTireBike.md`. Roads / trail surfaces: `Roads.md`, `TrailBuilding.md`. Suspension: `Suspension.md`.

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

## 8. Articulated Arms: The Giant Spider

### 8.1 Why Legs at All

Roboticist Marc Raibert noted in the 1980s that only about half of Earth's land surface is accessible to existing wheeled and tracked vehicles. Legs can reach much more because they:
- Choose discrete footholds and skip bad ground between them
- Step over obstacles taller than the body would allow a wheel to climb
- Cross gaps and trenches
- Keep the body level on steep or broken slopes
- Damage terrain less (separate footprints instead of a continuous rut), which is why Finnish forestry firm Plustech built a six-legged walking timber harvester prototype in the 1990s

### 8.2 Why Wheels Still Dominate

**Cost of transport (CoT)** measures energy per unit weight per unit distance:

```
CoT = P ÷ (m × g × v)
```

Lower is better. Wheels on hard surfaces are vastly more efficient than any walking machine. Legged robots have historically ranged from roughly CoT 1 up to 15 or more for hydraulic machines like early military quadrupeds, against well under 0.1 for road vehicles in good conditions. A wheel rolls continuously. A leg must lift, swing, accelerate, decelerate and absorb impact every step.

Other leg problems:
- **Actuator count:** each leg needs at least 3 degrees of freedom (hip swing, hip lift, knee). A hexapod needs 18 actuators; an eight-legged spider needs 24. Every actuator is a cost, weight and failure point.
- **Speed:** big walking machines are slow. Matt Denton's Mantis, a ridable hexapod of about 2 tonnes with a diesel hydraulic system, walks around 1 km/h.
- **Control complexity:** sensing terrain, planning footholds, coordinating gait.

### 8.3 Stability: Why Spiders Use Many Legs

**Static stability** means the machine will not fall even if it freezes mid-step. The center of mass must stay inside the **support polygon** formed by the feet touching the ground.

- **Six legs (hexapod):** the **tripod gait** keeps three legs down at all times (front and back on one side plus middle on the other). Always a stable triangle. Insects use this.
- **Eight legs (spider):** more redundancy. Can lift two legs at a time and still keep a wide polygon, or keep walking after losing a leg.
- **Four legs:** must shift weight carefully or walk dynamically (like a dog or Boston Dynamics Spot).
- **Two legs:** always dynamically balancing.

### 8.4 The Square-Cube Problem

Scale a spider up by a factor of `k`:
- Mass grows with volume: `k³`
- Leg strength grows with cross-sectional area: `k²`
- Stress in the legs grows by `k`

Double the size and leg stress doubles. A house-sized spider with spider proportions would collapse. This is why elephants have thick pillar legs held nearly straight under the body and why real spiders stay small. A giant mechanical spider needs:
- Much thicker legs than a real spider proportionally
- Legs angled more vertically under the body to carry load in compression rather than bending
- Lightweight structure (aluminum, steel tube trusses, composites)

Fun biology fact: real spiders lack extensor muscles at some leg joints. They extend those legs with **hydraulic pressure** from body fluid (hemolymph). That is why dead spiders curl up. A giant mechanical spider would almost certainly use hydraulics too, for power density.

### 8.5 Feet and Ground Pressure

Example: a 4-tonne spider walking with 4 of 8 feet down at once.
- Foot pad 0.1 m² each: `(4000 × 9.81) ÷ 0.4 = 98 kPa`, similar to a tank, will sink in soft ground
- Foot pad 0.3 m² each: about **33 kPa**, similar to an ATV
- Foot pad 0.5 m² each: about **20 kPa**, similar to a human

Wide hinged feet (like snowshoes) are essential. Gripping toes or spikes help on rock and slopes.

### 8.6 Speed Limit for Walkers

The **Froude number** predicts walking speed limits:

```
Fr = v² ÷ (g × L)
```

where `L` is leg length. Animals switch from walking to running near Fr ≈ 0.5. For a machine with 2 m legs:

```
v ≈ √(0.5 × 9.81 × 2) ≈ 3.1 m/s ≈ 11 km/h
```

That is the theoretical comfortable walking limit. Real heavy hydraulic walkers move far slower because of pump flow limits and control demands.

### 8.7 The Real Answer: Wheels on Legs

The best real-world machines combine both:
- **Walking excavators (Menzi Muck and similar "spider excavators"):** four articulated legs, wheels on the ends. They drive on wheels when the ground allows and lift, plant and walk their legs on steep alpine slopes, stream beds and rubble. Used where no other machine can work.
- **NASA JPL ATHLETE:** a six-limbed robot with a wheel at the end of each limb. Rolls on smooth ground, walks on rough ground.
- **Wheeled quadruped robots (such as ANYmal variants):** legged robots with powered wheels for feet. They roll efficiently and step up stairs and curbs.
- **Hyundai Elevate concept:** a car with wheels on articulated legs, designed to walk over rubble in disaster zones.

The legs act as **active suspension with almost unlimited travel**. Each wheel can be lifted, placed, raised over a ledge or pushed down into a hole. The body stays level. Energy use stays low on easy ground.

### 8.8 Giant Spider Design Sketch

| Element | Recommendation | Reason |
|---|---|---|
| Leg count | 6 (cost) or 8 (redundancy) | Static stability with tripod gait or better |
| Joints per leg | 3 minimum, 4 for foot leveling | Full foot placement |
| Actuation | Hydraulic cylinders | Highest force per weight for large machines |
| Feet | Wide hinged pads with powered wheels | Low ground pressure plus rolling mode |
| Legs | Truss or thick tube, near-vertical under load | Beat square-cube stress |
| Body | Low, wide | Keep CG inside support polygon on slopes |
| Control | Terrain sensing (lidar, cameras), force sensors in feet | Foothold choice and load balancing |
| Modes | Roll on easy ground, walk on hard ground | Efficiency plus capability |

**Spider pros:** climbs ledges taller than any wheel could, crosses gaps, stays level on slopes, light terrain impact, can survive losing a leg.

**Spider cons:** slow, 18 to 24+ actuators to buy and maintain, high energy use when walking, complex control software, heavy and expensive.

---

## 9. Vehicle Category Breakdown

Every wheel family in this guide powers a family of vehicles. This section breaks each family into its real subtypes with specs, best uses, pros and cons. Speeds, weights and prices are typical ranges; prices are rough US figures and shift with market and model year.

### 9.1 Bicycles

**Core science:** a cyclist sustains roughly 100 to 250 W for hours (trained racers 300+ W). At speeds above about 20 km/h (12 mph), aerodynamic drag becomes the largest force, rising with the square of speed. Power to beat drag rises with the cube of speed. That is why body position and frame shape matter more than weight on flat roads, while weight matters most on climbs.

```
P_aero = 0.5 × ρ × CdA × v³
```

- `ρ` = air density (about 1.2 kg/m³)
- `CdA` = drag area: upright cruiser about 0.6 m², road bike on the hoods about 0.35 m², time trial position about 0.22 m², faired velomobile about 0.05 m²

**Subtypes:**

| Type | Typical specs | Best for | Pros | Cons |
|---|---|---|---|---|
| Road (endurance / race) | 7 to 9 kg; 700c × 25 to 32 mm; drop bars; 25 to 40 km/h sustained | Paved roads, long rides, group rides | Fastest per watt on pavement; light; climbs well; efficient over 100+ km | Harsh on broken pavement; little cargo; tires vulnerable to glass; aggressive posture |
| Aero / time trial | Deep-section or disc wheels; aero tubes; extended bars | Racing against the clock, flat fast roads | Lowest drag of any upright bike; very fast solo | Deep rims catch crosswinds; uncomfortable; poor handling in groups; expensive ($4,000 to $15,000+) |
| Gravel / all-road | 8.5 to 11 kg; 700c × 38 to 50 mm or 650b × 47 mm+; mounts for bags | Mixed pavement and dirt, bikepacking | Extremely versatile; comfortable; one bike for most riding | Slower than road on pavement; less capable than MTB on technical trails |
| Cyclocross | Similar to gravel with tighter clearance, 33 mm race tires | Short muddy races with dismounts | Light; nimble; mud clearance | Narrow tire limit; racier geometry less stable for touring |
| Touring | Steel frame; 14 to 17 kg; racks front and rear; 35 to 50 mm tires | Multi-week loaded travel | Carries 20 to 40 kg gear; durable; repairable worldwide | Heavy; slow; sluggish unloaded |
| Hybrid / commuter | Flat bars; 32 to 45 mm tires; fenders and rack mounts | City errands, fitness, commuting | Upright and comfortable; practical; affordable | Jack of all trades; upright posture creates drag above 25 km/h |
| Cruiser | 26 × 2.125 in+ balloon tires; coaster brake; 15 to 20 kg | Beach paths, flat neighborhoods | Very comfortable; simple; stylish; low maintenance | Heavy; slow; poor on hills; weak braking |
| Hardtail MTB | Front suspension 100 to 140 mm; 29 or 27.5 in; 11 to 14 kg | Trails, budget mountain biking, bikepacking | Cheaper; efficient pedaling; fewer parts to service | Rear wheel hammers over rough descents; rider fatigue |
| Full-suspension XC | 100 to 120 mm travel; 10 to 12 kg | Cross-country racing and fast trail rides | Fast climbing; grip and control on rough ground | Expensive; pivot bearings and shock service |
| Trail | 130 to 150 mm travel; 13 to 15 kg | All-around mountain riding | Climbs and descends well; most versatile MTB | Heavier and costlier than hardtail; overkill on smooth trails |
| Enduro | 160 to 180 mm travel; 15 to 17 kg | Steep aggressive descents with climbing between | Huge descending capability; still pedalable uphill | Heavy; slow on flats; expensive |
| Downhill | 200 mm travel; 16 to 19 kg; dual-crown fork | Lift-served bike parks, racing | Best descending bike ever built; absorbs huge hits | Nearly impossible to climb; needs lift or shuttle |
| Dirt jump / slopestyle | 24 or 26 in; short hardtail; single speed | Jumps, pump tracks | Strong; playful; simple | Useless for distance; no real seat height |
| Fat bike | 4 to 5 in tires; 5 to 15 psi; 14 to 18 kg | Snow, sand, beaches, winter trails | Floats on soft ground; very stable; huge grip | Heavy; slow on pavement; costly tires; self-steer on pavement at low pressure |
| BMX | 20 in wheels; 10 to 12 kg; single speed | Tricks, ramps, racing, street | Very strong wheels; cheap; durable | Tiny gearing for distance; uncomfortable for long rides |
| Folding | 16 to 20 in wheels; folds in seconds | Train and bus commuting, small apartments | Portable; storable anywhere; carry onto transit | Small wheels feel pebbles; twitchy steering; quality models expensive |
| Cargo longtail | Extended rear; carries 1 to 2 kids or 80 to 200 kg cargo | Family transport, car replacement | Carries real loads; rides like a normal bike | Heavy (20 to 35 kg); storage space; cost |
| Cargo box bike (bakfiets) | Box ahead of rider; 2 or 3 wheels | Kids, groceries, deliveries | Huge capacity; kids visible in front | Very heavy (30 to 50 kg); wide; slow steering; hard to store |
| Recumbent two-wheel | Reclined seat; long or short wheelbase | Long-distance comfort | No saddle pain; lower drag than upright | Hard to climb; low in traffic; learning curve |
| Recumbent trike | Two wheels front or rear; 20 in wheels | Touring, riders with balance concerns | Stable at stop; extremely comfortable | Wide; low visibility in traffic; expensive; side loads need strong wheels |
| Velomobile | Fully faired recumbent trike; 20 to 35 kg | Fast commuting, long-distance | Can hold 45 to 50 km/h at power that moves a road bike near 30 km/h; weather protection | Expensive ($8,000 to $15,000+); hot in summer; awkward to store |
| Tandem | Two riders; 18 to 25 kg | Couples, mixed-fitness pairs | Two engines, one drag profile, so fast on flats | Long; heavy wheel loads; needs coordination |
| Fixed gear / track | No freewheel; direct drive | Velodromes, minimalist city riding | Simple; light; direct feel | No coasting; hard on knees downhill; often single brake or none |
| E-bike Class 1 (US) | Pedal assist to 20 mph (32 km/h) | Commuting, trails where allowed | Flattens hills; access to most bike paths | 20 to 30 kg; battery cost $400 to $1,000 |
| E-bike Class 2 (US) | Throttle to 20 mph | Riders who need assist without pedaling | Works even with limited pedaling ability | Banned from some trails; battery drains faster |
| E-bike Class 3 (US) | Pedal assist to 28 mph (45 km/h) | Fast road commuting | Car-competitive commute speeds | Restricted from many paths; higher crash energy |
| EU pedelec | 250 W continuous; assist to 25 km/h | European commuting | Treated like a bicycle legally | Assist cuts out at 25 km/h |

**Bicycle family overall:**
- **Pros:** most energy-efficient vehicle humans have built; cheap to own; healthy; parks anywhere; no license in most places
- **Cons:** exposed to weather and traffic; limited cargo without special designs; rider is the crumple zone; theft

### 9.2 Skates

| Type | Typical specs | Best for | Pros | Cons |
|---|---|---|---|---|
| Quad roller skates | 2 × 2 wheels; 57 to 65 mm; toe stop | Rinks, roller derby, dance, jam skating | Stable when standing; easy backward skating; great for spins | Slower than inline; small wheels hate rough ground; heavier |
| Recreational inline | 4 × 76 to 84 mm; soft boot | Casual skating on paths | Easy to learn; cheap ($80 to $200); comfortable | Soft boot gives sloppy control at speed |
| Fitness / marathon | 3 × 100 to 110 mm or 4 × 90 to 100 mm | Long-distance fitness skating | Faster; smoother over cracks | Higher center of gravity; harder to stop |
| Speed skates | 4 × 110 mm or 3 × 125 mm; low carbon boot | Racing | 30 to 40 km/h sustained for elite skaters | No ankle support; custom fit needed; expensive |
| Aggressive | 4 × 55 to 60 mm; grind blocks; hard boot | Skate parks, rails, street tricks | Built for grinding; durable | Slow; harsh; stopped by any rough ground |
| Urban / freeskate | 3 × 100 to 110 mm or 4 × 80 mm; hard shell boot | City streets, slalom, commuting | Agile; strong ankle support; handles city surfaces | Costly ($250 to $600); still small wheels |
| Off-road pneumatic | 150 to 200 mm air tires; 2 or 3 wheels | Grass, dirt paths, rough pavement | Rolls over terrain no urethane wheel can | Heavy; tall; tiring; braking is weak |
| Electric skates | Hub motors; remote throttle | Novelty commuting | Assist on flats | Heavy; short range; balance demands at speed |

**Skates overall:**
- **Pros:** hands-free; tiny storage; full-body workout; cheap
- **Cons:** tiny wheels make every pebble a hazard; poor braking (heel brake or T-stop); no cargo; wrist fractures are the classic injury

### 9.3 Skateboards, Scooters and Boards

| Type | Typical specs | Best for | Pros | Cons |
|---|---|---|---|---|
| Street skateboard | 7.5 to 8.5 in deck; 50 to 56 mm 99A wheels | Tricks, skate parks | Light; ollies and flips; portable | Hard wheels stop on pebbles; terrible for transport |
| Cruiser | 26 to 32 in deck; 60 to 65 mm 78A to 83A wheels | Short city hops | Soft wheels smooth out cracks; portable | Small deck; wheel bite in hard turns |
| Longboard (carving / cruising) | 34 to 46 in deck; 65 to 75 mm soft wheels | Commuting, campus travel, carving | Stable; smooth; efficient pushing | Bulky to carry |
| Longboard (downhill / freeride) | Stiff low deck; 70 to 80 mm wheels; precision trucks | Speed runs on mountain roads | Racers exceed 100 km/h (60+ mph); controlled slides | Requires leathers and full-face helmet; braking is by sliding or foot |
| Dancer longboard | 42 to 48 in flat deck | Board walking, cross-stepping | Room for footwork tricks | Long and heavy; poor for tight turns |
| Surfskate | Special pivoting front truck | Surf training, pumping without pushing | Generates speed by pumping | Twitchy at speed |
| Mountainboard | 8 to 10 in pneumatic tires; channel trucks; foot bindings | Grass hills, dirt, bike parks | Real off-road board; bindings for jumps | Heavy (7 to 10 kg); weak braking on unpowered models |
| Electric skateboard | 30 to 40 km/h; 15 to 40 km range; belt or hub motors | Commuting | Fast; fun; portable-ish | Falls at speed are serious; regenerative braking can weaken or vanish on a fully charged battery; rain damage |
| Off-road electric board | Pneumatic 6 to 8 in tires; dual or quad motors | Trails, gravel | Climbs dirt and grass | 15 to 25 kg; expensive |
| Onewheel-type | Single central kart-style tire; self-balancing | Trails, beaches, city | Handles dirt, grass and sand; carves like snowboarding | Nosedive if the motor runs out of balancing torque; learning curve; heavy |
| Dirtsurfer-type | Two in-line bike-style wheels; lean steering | Grass hills, dirt roads | Big wheels roll over terrain | Long; specialized; few makers |
| Kick scooter | 100 to 200 mm urethane wheels; folding | Kids, short commutes | Easy; cheap; foldable | Small wheels catch cracks |
| Footbike / big-wheel scooter | Up to 28 in front, 12 to 20 in rear | Fitness, dog scootering, distance kicking | Rolls like a bike; whole-body workout | Large and not foldable |
| Electric kick scooter | 8 to 10 in wheels; 25 to 40 km/h | Urban commuting, shared fleets | Easy; portable; cheap per mile | Small wheels plus speed equals pothole crashes; stem and folding joint failures on cheap units |

**Board family overall:**
- **Pros:** cheap; portable; fun; carves and flows
- **Cons:** wheel diameter limits terrain; minimal braking; falls happen at full speed with no protection

### 9.4 Go-Karts

**Core science:** racing karts have no suspension, no differential and a frame designed to flex. The chassis twists in turns so the inside rear wheel lightens or lifts, letting the solid axle turn without scrubbing. Steering geometry (caster plus kingpin inclination) also lifts the inside front corner when steered, adding to this effect. Weight per horsepower is extreme: a shifter kart with driver has a better power-to-weight ratio than many sports cars.

| Type | Typical specs | Best for | Pros | Cons |
|---|---|---|---|---|
| Rental / concession | 4-stroke 6.5 to 13 hp or electric; 40 to 70 km/h; bumpers | Indoor and outdoor rental tracks | No ownership cost; safe-ish; social | Slow; worn tires; limited tuning |
| 4-stroke sprint (LO206 class) | Sealed ~9 hp engine; ~80 km/h | Entry-level racing | Cheap racing; reliable; sealed engines keep it fair | Slowest racing class |
| 125cc TaG 2-stroke (Rotax Max, X30) | ~28 to 30 hp; 110 to 130 km/h | National level racing | Fast; electric start; strong classes worldwide | Engine rebuilds; tire costs |
| Shifter (KZ) | 125cc 6-speed, ~45 to 50 hp; 0 to 100 km/h in about 3 s | Top-level sprint racing | Brutal acceleration and braking; pure driving skill | Physically punishing; expensive upkeep; rib injuries |
| Superkart | 250cc, 90+ hp; aero bodywork; 200+ km/h | Full-size road circuits | Among the highest power-to-weight vehicles on any track | Very costly; dangerous at speed with no crash structure |
| Enduro / laydown | Driver lies back; long races | Endurance racing on big tracks | Aerodynamic; long seat time | Niche class; few tracks |
| Electric racing kart | Instant torque; quiet | Indoor tracks, noise-limited venues | No fumes; low maintenance | Battery heat; limited run time |
| Off-road / yard kart | 196 to 420cc; suspension; roll cage; 13 to 22 in tires | Backyards, farms, dirt tracks | Handles grass and dirt; cheap fun | Often low build quality; little crash protection |
| Dune buggy | Tube frame; car engine; long travel | Dunes, desert | Light and fast on sand | Mostly custom builds; road legality varies |
| Cyclekart | Small vintage-style kart; ~6.5 hp; narrow tall wheels | Club racing with style | Cheap; DIY-friendly; slow speeds make close racing | Niche; homebuilt quality varies |

**Kart family overall:**
- **Pros:** cheapest real motorsport; teaches racecraft; huge grip for size; minimal mechanics
- **Cons:** no suspension; very little crash protection; tires and engines wear fast; not road legal

### 9.5 Golf Carts and Low-Speed Vehicles

| Type | Typical specs | Best for | Pros | Cons |
|---|---|---|---|---|
| Gas golf cart | 10 to 14 hp 4-stroke; 12 to 20 mph | Large properties, hilly courses | Long range; quick refuel; strong on hills | Noise; fumes; engine maintenance |
| Electric (lead-acid) | 36 or 48 V; 25 to 40 mi range; about 150 to 200 kg of batteries | Courses, communities | Quiet; cheaper upfront; simple | Battery watering; 3 to 6 year pack life; range fades on hills and in cold |
| Electric (lithium) | 48 to 72 V; 40 to 80 mi range | Daily neighborhood transport | Lighter; no watering; 2,000+ cycle life; stronger acceleration | Higher upfront cost |
| Lifted / off-road cart | 4 to 8 in lift; 20 to 23 in all-terrain tires | Trails, farms, hunting | More clearance; handles dirt and light mud | Higher rollover risk; slower without motor upgrade; turf damage |
| Street-legal LSV (US) | Top speed 20 to 25 mph; lights, signals, mirrors, belts, windshield, VIN | Neighborhoods, beach towns, retirement communities | Legal on many low-speed roads; cheap per mile | Limited to roads with low speed limits (rules vary by state); minimal crash protection |
| Utility / turf vehicle | Cargo bed 200 to 500 kg | Groundskeeping, campuses, farms | Hauls tools and material; turf-friendly | Slow; basic comfort |
| 4 and 6 seat carts | Extended frame; rear-facing or forward bench | Family transport, resorts | Moves groups cheaply | Long turning radius; higher load on small wheels |

**Golf cart family overall:**
- **Pros:** cheap to run; quiet (electric); easy to drive; gentle on grass
- **Cons:** slow; minimal suspension and crash safety; small wheels limit terrain; legal road use is restricted

### 9.6 ATVs, UTVs and Off-Road Motorsports

**Core science:** ATVs are **rider-active**: the rider shifts body weight to steer and stay upright. Solid rear axles on many ATVs resist turning and can cause tip-overs if the rider does not lean. UTVs are **driver-passive**: seated, belted and protected by a roll cage (ROPS), steered like a car.

| Type | Typical specs | Best for | Pros | Cons |
|---|---|---|---|---|
| Youth ATV | 50 to 110cc; speed limiters | Supervised training | Teaches control at low speed | Real injury risk; kids outgrow them fast |
| Sport ATV | 400 to 700cc; 30 to 50 hp; 2WD; 170 to 190 kg | Dunes, motocross tracks, jumps | Excellent power-to-weight; long travel suspension; nimble | No cargo; demanding to ride; rollover and flip risk |
| Utility ATV | 450 to 1000cc; 4WD; racks; 270 to 350 kg; tows 500 to 800 kg | Farms, hunting, trails, plowing | Narrow for tight trails; versatile; cheaper than a UTV | Rider-active handling is tiring; single rider on most; can flip backward on steep climbs |
| Two-up ATV | Extended seat for passenger | Couples, guides | Carries two legally | Long wheelbase; still no cage |
| Utility UTV | Bench seating 2 to 6; bed 300 to 600 kg; tows 900+ kg | Ranch and farm work | Car-like controls; cage; seatbelts; serious cargo | Wide (some trails limit to 50 in); heavier; costs $12,000 to $30,000 |
| Sport UTV | Turbo up to 200+ hp; 20+ in suspension travel | Desert racing, dunes, whoops | Blistering speed over rough ground; protective cage | $25,000 to $50,000+; heavy fuel use; expensive breakage |
| Rock crawler / buggy | Tube chassis; 37 to 42+ in tires; portal axles; locked diffs; gear reduction 100:1 or more | Extreme rock trails | Climbs ledges taller than its tires | Very slow; usually not road legal; needs a trailer; costly |
| Trophy truck | 800 to 900+ hp V8; 30+ in suspension travel | Desert racing (Baja 1000) | Fastest vehicle across rough desert, 160+ km/h over whoops | Costs from hundreds of thousands to over a million dollars |
| Motocross bike | 250 to 450cc; ~105 kg; no lights | Closed tracks, jumps | Lightest powerful off-road vehicle; huge suspension | Not street legal; frequent engine service |
| Enduro bike | Lights; wide-ratio gearbox; 110 to 120 kg | Long rugged trails | Fits single-track; climbs and descends technical ground | Physically demanding; one rider |
| Trials bike | No seat; ~70 kg; tires at about 4 to 6 psi | Boulders, logs, cliffs | Climbs obstacles nothing else with wheels can | Useless for distance or speed |
| Dual-sport bike | Street legal dirt bike | Ride to the trail, adventure | One vehicle for road and dirt | Compromise on both |
| Amphibious 6×6 / 8×8 | Balloon tires at 1 to 3 psi; skid steer; floats | Swamp, marsh, snow, water | Goes almost anywhere soft; swims | Slow (water speed only a few km/h); skid steering tears ground; rough ride |
| Snowmobile | Track plus skis; 3 to 5 kPa ground pressure | Snow | Fastest over snow (some exceed 100 mph) | Only works on snow; noise; avalanche terrain risk |
| Tracked UTV conversion | Rubber track kits replace tires | Deep snow, swamp | Huge flotation increase | Lower top speed; more drivetrain stress; costly kits |

**Off-road motorsport family overall:**
- **Pros:** reach places roads never go; wide choice from cheap trail ATVs to desert racers; huge fun
- **Cons:** high injury rates (ATV rollovers especially); land access rules; maintenance after every hard ride; fuel thirsty

### 9.7 Cars and Trucks

**By body type:**

| Type | Typical specs | Best for | Pros | Cons |
|---|---|---|---|---|
| Kei car / microcar | Japan kei limits: 3.4 m long, 660cc, about 64 hp | Dense cities | Tiny footprint; cheap tax and insurance; efficient | Weak crash protection vs large vehicles; little space; slow on highways |
| Hatchback / compact | 4.0 to 4.4 m long | Cities, budget buyers | Efficient; easy to park; flexible fold-flat cargo | Small rear seat; less highway refinement |
| Sedan | 4.6 to 5.0 m long | Commuting, highway travel | Low center of gravity; aerodynamic; quiet; comfortable | Fixed trunk opening; less cargo flexibility |
| Station wagon | Sedan chassis with long roof | Families wanting handling plus space | Sedan handling with SUV-like cargo | Rare in some markets |
| Coupe / convertible | 2 doors; often sport tuned | Enjoyment, style | Style; open air (convertible); often lighter | Tight rear seats; less practical; convertibles flex more and are louder |
| Minivan | Sliding doors; 7 to 8 seats | Large families | Most usable interior space per dollar; easy kid access | Image; soft handling |
| Crossover SUV | Car-style unibody; optional AWD | Mainstream family use | High seating; easy entry; AWD for weather | Higher center of gravity and frontal area burn more fuel than a sedan; limited real off-road ability |
| Body-on-frame SUV | Separate ladder frame; low range 4WD | Towing, off-road, heavy duty | Tough; tows well; capable off-road | Heavy; bouncier ride; worse fuel economy |
| Pickup truck | Half-ton to heavy duty; tow ratings from about 5,000 lb to over 30,000 lb (heavy duty with fifth wheel) | Hauling, towing, work | Open bed; massive towing; durable | Long; hard to park; light rear axle loses grip when the bed is empty |
| Sports car | Light; RWD or mid-engine; low CG | Driving enjoyment, track days | Sharp handling; fast; engaging | Little cargo; stiff ride; costly tires and insurance |
| Supercar / hypercar | 500 to 1,500+ hp; carbon structures | Speed, collecting | Extreme performance | Huge cost; impractical; low ground clearance |
| Dedicated 4×4 | Solid axles or long-travel IFS; low range; lockers; high approach angles | Trail driving, overlanding | Real off-road ability out of the box | Vague road handling; heavy; poor fuel economy |

**By powertrain:**

| Powertrain | Pros | Cons |
|---|---|---|
| Gasoline (ICE) | Fast refuel; long range; cheap upfront; works in any climate | Converts only about 25 to 35 percent of fuel energy to motion; emissions; more moving parts |
| Diesel | High torque; best for towing; long engine life | Emissions equipment complexity; fuel cost in some regions |
| Hybrid | Recovers braking energy; big city fuel savings; no plugging in | More complexity; smaller benefit on highways |
| Plug-in hybrid | Electric commuting with gas backup | Carries two powertrains; heavy; small electric range on many |
| Battery electric (BEV) | About 85 to 90 percent of stored energy reaches the wheels; instant torque; low maintenance; quiet | Heavy batteries wear tires faster; cold weather often cuts range 20 to 40 percent; charging time; charger access |
| Hydrogen fuel cell | Fast refuel; electric drive | Very few fueling stations; expensive fuel |

**By drive layout:**

| Layout | Pros | Cons |
|---|---|---|
| Front-wheel drive | Cheap; space efficient; good in snow with weight over drive wheels | Torque steer; understeer at the limit |
| Rear-wheel drive | Balanced handling; better acceleration grip as weight shifts back | Weaker in snow without good tires |
| All-wheel drive | Grip in all weather; strong launches | Heavier; slightly more fuel; does not help braking or cornering on ice |
| Part-time 4WD with low range | Locked traction and gear reduction for real off-road | Cannot be engaged on dry pavement without binding drivetrain |

**Car family overall:**
- **Pros:** fast; weatherproof; crash protection; carries people and cargo long distances
- **Cons:** expensive to own; parking; tire and road wear; highest energy use per person of common transport except large trucks and powersports

### 9.8 Giant-Wheel Vehicles

| Type | Typical specs | Best for | Pros | Cons |
|---|---|---|---|---|
| Penny-farthing | 48 to 60 in front wheel; direct pedal drive | Vintage riding, events | Smooth over rough roads; grand view | High fall risk ("headers"); hard mounting; no gearing |
| 36er bike / unicycle | 36 in wheels | Long-distance unicycling, novelty | Big rollover ability; high speed per pedal stroke (unicycles) | Heavy wheels; few tire options; flexy |
| Monowheel | Rider inside a single 1.5 to 2 m wheel | Novelty, records | Very simple drivetrain; unique | Rider swings inside on hard braking or acceleration; poor visibility; hard steering |
| Dicycle / self-balancing two-wheel | Two large wheels side by side, rider between | Novelty, compact personal transport | Turns in place | Needs active balancing; falls if power fails |
| Lunar Roving Vehicle (Apollo) | 81 cm wire-mesh wheels with titanium tread chevrons | Moon surface | Airless and light; works in vacuum and extreme temperatures | Single purpose; limited payload |
| Monster truck | 66 in tall tires; about 5,000+ kg; supercharged methanol engines near 1,500 hp | Shows, car crushing | Jumps and crushes; massive suspension travel | Hugely expensive; not road legal; fuel hungry |
| Farm tractor | Rear tires up to about 2 m tall; duals or triples; IF/VF low-pressure tires | Fields | High traction; low soil compaction with big low-pressure tires | Slow; wide; costly |
| Mining haul truck | Tires about 4 m tall weighing several tonnes each; payloads around 360 tonnes | Open-pit mines | Moves enormous loads per trip | Tires cost tens of thousands of dollars each; limited to mine roads |
| Polar / tundra buggies and snow buses | Very large low-pressure tires | Arctic tourism, Antarctic logistics | Floats on snow and tundra; high viewing platform | Slow; huge; specialized |

**Giant-wheel family overall:**
- **Pros:** roll over almost anything; ground pressure can be very low with wide tires; dramatic presence
- **Cons:** heavy rotating mass; high center of gravity; size makes transport and storage hard; side loads demand very strong hubs

### 9.9 Wild Off-Road Specialists

| Type | How it moves | Best for | Pros | Cons |
|---|---|---|---|---|
| Main battle tank | Steel tracks; 60+ tonnes | Military terrain | Ground pressure lower than a car; crosses trenches and walls | Huge fuel use; road damage; track maintenance |
| Bulldozer / crawler | Steel tracks; low gear | Earthmoving, steep slopes | Enormous pushing traction | Very slow |
| Snowcat | Wide rubber or steel tracks | Ski slopes, snow transport | Very low ground pressure; climbs steep snow | Slow; snow only |
| Articulated tracked carrier (Bv206 style) | Two tracked units linked by a steering joint | Arctic, swamp, military | Ground pressure below a person on foot; amphibious versions; huge mobility | Complex; costly; slow on roads |
| High-speed tracked vehicles (Ripsaw style) | Long-travel suspension on tracks | Fast cross-country | Track flotation at high speed | Very expensive; track wear |
| Track conversion kits (Mattracks style) | Four track units replace wheels | Trucks and UTVs in deep snow | Turns a normal truck into a snow vehicle | Lower top speed; added driveline load |
| Rolligon / terra tire vehicles | Huge ultra-low-pressure tires | Arctic tundra, wetlands | Very low surface damage | Slow; huge; specialized |
| Portal axle trucks (Unimog style) | Gear hubs raise axles; deep wading | Expedition, utility, flood | Massive clearance and wading; road legal | Costly; complex hubs |
| Screw-propelled vehicles | Two giant counter-rotating Archimedes screws | Deep mud, swamp, ice, water | Moves through slop that stops everything else | Nearly useless on firm ground; destroys surfaces; slow |
| Hovercraft | Air cushion; no wheels | Water, ice, mud flats | Crosses water and land; almost no ground pressure | Poor slope climbing; drifts sideways; loud; weak braking |
| Mars rovers (rocker-bogie) | Six wheels on passive linkages | Rocky planetary terrain | Keeps all wheels down; no springs to fail | Very slow (a few centimeters per second when navigating autonomously) |

### 9.10 Walking and Legged Machines

| Type | Example | Pros | Cons |
|---|---|---|---|
| Wind-powered linkage walker | Theo Jansen's Strandbeest (Jansen linkage, PVC tubing) | No motors or electronics; elegant single-crank leg motion | Only works on flat beach; wind dependent |
| Crank linkage walker | Klann linkage hobby walkers | One motor drives all legs; simple | Fixed gait; cannot pick footholds; poor on rough terrain |
| Ridable hexapod | Mantis (about 2 tonnes, diesel hydraulic) | Statically stable tripod gait; dramatic; proves ridable walkers work | About 1 km/h; huge complexity |
| Quadruped robot | Boston Dynamics Spot (about 32 kg, about 1.6 m/s, about 90 min runtime) | Stairs, rubble, industrial inspection | Small payload; short runtime; high cost |
| Quadruped with wheel feet | ANYmal wheeled variants | Rolls efficiently and steps over curbs | Complex control; costly |
| Walking excavator | Menzi Muck style spider excavator | Works on steep slopes, rivers and rubble | Slow to relocate; expensive; skilled operator required |
| Walking harvester | Plustech prototype (1990s) | Low forest floor damage | Never mass produced; complex |
| Limbed rover with wheels | NASA JPL ATHLETE | Rolls on easy ground, walks on hard ground | Experimental |
| Walking car concept | Hyundai Elevate | Climbs rubble in disaster zones | Concept stage only |
| Theatrical giant walkers | Large street theater machines | Spectacle | Often crane-supported or crew-assisted rather than self-supporting |
| Piloted mech prototypes | Various demonstration mechs | Visual appeal | Slow; unstable; mostly demonstrators |

**Legged family overall:**
- **Pros:** reach terrain closed to wheels; step over obstacles and gaps; level body on slopes; light ground impact
- **Cons:** slow; energy hungry; many actuators; complex software; expensive

### 9.11 Custom Hybrids From This Guide

| Build | Wheel choice | Pros | Cons |
|---|---|---|---|
| Big-wheel skateboard | 16 to 20 in BMX wheels, drop deck, both-side axle support | Rolls over curbs, roots and gravel; smooth | Heavy; wide; lean steering geometry needs custom work |
| Bike-wheel golf cart | 20 in heavy-duty trike wheels on an ultralight frame, or motorcycle spoked wheels on a normal cart | Lower rolling resistance; more range; obstacle rolling; vintage look | Custom hubs and brakes; turf damage from narrow tires; higher rollover risk |
| Giant spider on wheel-legs | Hydraulic legs with powered wheels as feet | Rolls efficiently on easy ground; walks through anything else | Enormous cost and complexity; slow walking mode |

### 9.12 Cross-Category Comparison Matrix

| Vehicle | Typical top speed | Rough new cost (US) | Energy per km | Terrain range | People / cargo | Usual US license or registration |
|---|---|---|---|---|---|---|
| Walking (baseline) | 5 to 6 km/h | $0 | About 50 to 70 Wh (food) | Nearly everything | 1 person, light pack | None |
| Inline skates | 15 to 40 km/h | $80 to $600 | Low (human) | Smooth pavement only | 1 person | None |
| Skateboard / longboard | 10 to 30 km/h (pushing) | $80 to $350 | Low (human) | Pavement | 1 person | None |
| Road bike | 25 to 50 km/h | $1,000 to $12,000 | About 15 to 25 Wh (food) | Pavement | 1 person, small bags | None |
| Mountain bike | 15 to 40 km/h | $600 to $10,000 | About 20 to 40 Wh (food) | Trails, dirt, rock | 1 person | None |
| E-bike | 32 to 45 km/h assisted | $1,000 to $8,000 | About 8 to 15 Wh (battery) | Pavement and trails | 1 to 3 (cargo models) | Usually none; class rules apply |
| Electric skateboard / scooter | 25 to 40 km/h | $300 to $2,500 | About 10 to 20 Wh | Pavement (off-road models: dirt) | 1 person | Varies by city and state |
| Racing go-kart | 80 to 140+ km/h | $3,000 to $12,000+ | High per km | Tracks | 1 person | None (track use) |
| Electric golf cart | 20 to 40 km/h | $8,000 to $20,000 | About 80 to 120 Wh | Pavement, grass, packed dirt | 2 to 6 people | LSV models need registration and insurance |
| Utility ATV | 70 to 110 km/h | $6,000 to $16,000 | About 800 to 1,300 Wh (fuel) | Trails, mud, snow, farm | 1 to 2 people, rack cargo | Off-road registration in many states |
| Sport UTV | 110 to 150 km/h | $25,000 to $50,000+ | Very high | Desert, dunes, trails | 2 to 4 people | Off-road registration |
| Electric car | 150 to 250 km/h | $30,000 to $80,000+ | About 150 to 250 Wh | Roads | 4 to 7 people | Driver's license, registration, insurance |
| Gas car | 150 to 250 km/h | $25,000 to $70,000+ | About 500 to 900 Wh (fuel) | Roads | 4 to 7 people | Driver's license, registration, insurance |
| Rock crawler | 10 to 60 km/h | $20,000 to $100,000+ | Very high | Extreme rock | 1 to 2 people | Usually trailer to trail |
| Snowmobile | 100 to 160+ km/h | $10,000 to $20,000 | High | Snow only | 1 to 2 people | Snowmobile registration |
| Tracked carrier | 40 to 65 km/h | Six figures | High | Snow, swamp, tundra, water | 6 to 17 people | Specialized |
| Legged robot / walker | 1 to 6 km/h | $75,000 to millions | Very high per kg carried | Rubble, slopes, stairs | Small payloads (except excavators) | Specialized |

"Energy per km" for human-powered rows is metabolic food energy. Fuel rows count the full chemical energy of the fuel burned.

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
