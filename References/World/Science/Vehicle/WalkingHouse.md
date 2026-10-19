# Walking House (Mechanics and Magic)

> Earth invent loot / fiction vehicle design. Legged buildings, four-leg apartment, force rail, repulsion-shield glide, Mana Shield area cost for a 100 m² sheet, programming legs with proximity / distance-set / kinetic runes. Not Caldris law. Legged machines: `LeggedVehicles.md`. Ride smoothness / limb count / IK: `WalkerRideSmoothness.md`. Caravan amenities: `MobileHome.md`. Mana Shield spread / pool: `../Energy/ManaShield.md`, `ManaCast.md`. Shaft / driveline: `ShaftJointTransmission.md`. Ground / trails: `TrailBuilding.md`, `Roads.md`. Goals wishlist: `../../../People/Roland/Goals.md`. Nav: `Index.md`.

---

## 1. Legged Buildings and Vehicles

A walking building with precise legs can cross rough terrain without breaking the dishes. The cost is energy, speed and mechanical complexity.

### Real Precedents

- **Walking draglines:** Big Muskie weighed about 13,000 tons and moved on giant hydraulic "shoes."
- **Menzi Muck walking excavators:** climb slopes and streambeds.
- **Plustech/Timberjack harvester:** a six-legged machine that walked through forests.
- **Hyundai Elevate:** a concept car with wheeled legs.

### Why Contents Can Stay Safe

Legs work as active suspension. Each leg changes length so the body stays level no matter what the ground does, the same way a chicken holds its head still while its body bobs. With good control and floor damping, the ride can feel like a slow train. The main risks are a foot slipping, soft ground collapsing under a foot or a leg failing.

### Hard Limits

- **Square-cube law:** Doubling the size multiplies the weight by 8 but leg strength only by 4. A castle-sized walker needs short, thick legs, many legs or very slow movement.
- **Leg count:** Two legs need constant dynamic balance. Six legs allow a tripod gait with three feet always down, which is statically stable.
- **Energy:** Walking lifts and lowers mass every step, so it is far less efficient than wheels or tracks. It only wins off-road, where it can step over obstacles and choose where each foot lands.
- **Ground pressure:** Feet concentrate the load, so they need wide pads or they sink.
- **Speed:** Draglines walk at a few hundred feet per hour. Faster gaits mean bigger accelerations inside.
- **The building itself:** It has to be built like an RV or a ship, with a rigid frame, flexible plumbing and wiring, and latched cabinets. A normal house frame is not designed for repeated dynamic loads.
- **Maintenance:** Dozens of actuators, joints and hydraulic lines all wear and can fail.

### Best Real-World Design

A hybrid with wheels on the leg tips that roll on flat ground and legs that lock out to walk over rough terrain. This gets most of the stability benefit without paying the full energy cost of walking all the time.

## 2. Four-Legged Two-Story Apartment with Ground Strengthening

Ground strengthening (the ground under each foot behaves as if the foot were much larger, with no added weight) solves the biggest real-world problems: sinking, slipping and soil collapsing under a foot. What remains is standard heavy-machinery engineering.

### Weight and Legs

A small two-story apartment with a steel frame, actuators and batteries comes out around 30 to 60 tonnes. That is excavator territory, so the leg hardware already exists. Each leg should be rated for at least half the total weight, since loads shift heavily during each step.

### Gait

A four-legged walker lifts one leg at a time and keeps three down, which is statically stable. Before each step, the body shifts so its center of mass sits inside the triangle formed by the three planted feet. Walking is slow and deliberate, like a cautious crawl. That pace keeps the inside calm.

### Ride Quality

With stiffened ground there is no foot slip or sudden sinking, so active leveling can keep the floors almost perfectly flat. Accelerations stay very low. Furniture and dishes are fine as long as cabinets latch. The upper floor amplifies any body tilt, so the leveling system has to be good.

### Remaining Limits

- **Tipping:** A tall building on a narrow stance is top-heavy. A wide, splayed leg stance is correct. Heavy parts (batteries, water tanks, hydraulics) belong low in the belly section.
- **Slopes and wind:** Steep side slopes and strong wind are the real tipping risks. The house should crouch lower in both cases to drop its center of mass.
- **Power:** Walking costs roughly what running an excavator does, which is tens of kilowatts. Rooftop solar on a house that size provides maybe 80 to 100 kWh on a good day. That covers a few hours of slow walking per day of charging, which suits a nomadic life rather than a commute.
- **Leg failure:** Losing a leg on a four-legged walker means a fall unless it can kneel. The safest design lets the belly rest on the ground when parked, which also takes load off the joints.
- **Maintenance:** Hydraulic seals, joint bearings and actuators wear out and need replacing on a schedule.

### Verdict

A slow-moving home that keeps its contents safe over almost any terrain and works best relocating every few days.

## 3. Force Rail

The building projects a force rail that averages out the ground beneath it, so movement becomes a glide along a smooth, curved surface. This turns the walker into a train that lays its own track.

### What Changes

- **Ride quality:** No step-by-step load shifting. The inside experiences only gentle, steady curves. Dishes stay on open shelves.
- **Energy:** Rolling or sliding on a smooth rail is dramatically cheaper than walking. A 50-tonne rail vehicle at walking speed on level ground needs only a few kilowatts, so rooftop solar could power all-day travel.
- **Speed:** Without gait limits, it moves as fast as the rail's curvature allows.
- **Legs:** Their role shifts to suspension, leveling and anchoring when parked.

### Curvature Versus Speed

Vertical acceleration on a curve = speed² ÷ curve radius. Keeping it under 0.05 g (the train comfort standard) requires:

| Speed | Minimum Curve Radius |
|---|---|
| Walking pace (1.5 m/s) | about 5 m |
| Bicycle pace (5 m/s) | about 50 m |
| Backroad car pace (10 m/s) | about 200 m |

The faster it goes, the longer a stretch of ground the rail has to average over. At high speed, it also needs to project the rail far ahead for braking room.

### Remaining Limits

- **Grade:** Averaging cannot flatten a mountain. A steep hillside still produces a steep rail. Grades past about 5 to 10 percent get expensive in power.
- **Propulsion and braking:** A smooth glide needs something to push against: powered wheels gripping the rail, legs pushing off it or a linear-motor style drive.
- **Turning:** Sideways curves create sideways force. Banking the rail into turns cancels most of it.
- **Obstacles above the rail:** Trees, overhangs and structures still need to be avoided.
- **Load path:** The rail's weight still ends up on the ground. Ground strengthening handles this.

## 4. Repulsion Shield Glide

The house casts a shield over a large area of ground, averaging it out. The house glides on the shield through repulsion, like two magnets pushing apart. There is no kinetic impact, only frictional wear. The shield is close to infinitely hard but can still break. The ground underneath supports the shield to reduce cost.

This maps closely onto real maglev. The house never touches the shield, so the "wear" is the strain of holding the field against the house's weight and motion. With the ground backing the shield, that strain stays low almost everywhere.

### Why Ground Support Matters

- **Load spreading:** A 50-tonne house spread over a 100 m² shield puts about 5 kPa on the ground. That is lighter per area than a person standing, so almost any soil holds it.
- **The shield's real job:** Over solid ground, the shield barely works. It only has to bridge the gaps where the ground falls away under the averaged surface.

### Where the Shield Breaks

- **Voids:** Over ditches, ravines and sinkholes, the shield carries the full load as a bridge. Cost and strain climb with the span.
- **Point contacts:** A boulder poking up under the averaged surface concentrates support onto one spot, like a pea under a mattress. This is the most likely place for a crack.
- **The leading edge:** The front of the shield takes the load first as the house moves onto it. That edge sees the most stress, especially at speed.

### Problems the Magic Needs to Address

- **Sideways stability:** Pure repulsion is unstable sideways. Real magnets pushing apart slip off to the side, which is why real maglev trains wrap around a guide rail. The shield should have a shallow trough shape or raised edges so the house centers itself.
- **Drag:** Real maglev loses energy to the field itself, and the loss rises with speed. Mana cost should rise with speed, which naturally caps travel speed.
- **Slopes and stopping:** A frictionless glide slides downhill on its own. The house needs a braking method, such as deliberately increasing drag or setting down feet. When parked, it rests on its legs or drops onto the ground.

### Casting Pattern

The shield only needs to exist under and ahead of the house, dissolving behind it like a rolling carpet. The look-ahead distance sets the safe top speed, since the house can only brake within the shield it has already laid.

## 5. Shield Cost for 100 m²

### Baseline

- Personal Mana Shield: 1 m radius dome, area 6.28 m²
- Cost: 100 MP
- Absorbs: 1,000 J (1 MP = 10 J)

### Method A: Constant Absorption per Area

- 100 m² ÷ 6.28 m² = 15.9 times the area
- 15.9 × 100 MP = **about 1,600 MP**
- Absorption capacity: about 16,000 J

### Method B: Canon Spread Factor S = √(0.2 / A)

- Personal dome (6.28 m²): S = 0.178
- 100 m² sheet: S = 0.045, about 4 times weaker per hit at the same cost
- Matching personal-dome strength: **about 400 MP**

### Which to Use

Method A keeps absorption per square meter constant. Method B keeps per-hit strength constant under the spread rule. For a ground-supported glide shield, Method B fits better, since the ground carries most of the load and the shield mainly has to hold its shape.

### Scale

| Cost | Fledgling Mage Pools (200 MP each) |
|---|---|
| 400 MP | 2 |
| 1,600 MP | 8 |

## 6. Programming the Legs with Runes

Available runes: proximity detection, distance-set casting and direct energy-to-kinetic transmission.

The control problem is solvable with these three runes as long as rune output can scale proportionally instead of only switching on and off. Real walking robots break into sensing, deciding and acting. The runes cover sensing and acting. The deciding is where the complexity lives.

### Rune Roles

- **Proximity rune:** the sensor
- **Distance-set casting:** places ground strengthening exactly where a foot will land, or lays the rail ahead
- **Kinetic rune:** the actuator, applying direct torque at each joint with no hydraulics, pumps or seals

### Sensors Built from Proximity Runes

- **Foot contact:** a rune on the sole reads distance to the ground. Zero means planted.
- **Load:** a rune measuring how far a spring in the leg compresses works as a scale.
- **Tilt:** a rune measuring the gap to a hanging plumb weight inside the house gives a level reading.
- **Terrain ahead:** forward runes scan where the next steps will land.

### Reflex Layer (Easy)

Each leg runs its own loop, with the kinetic rune's output scaled to the gap between measured and target height. This alone keeps the floors level. Insects walk mostly this way, using local reflexes and simple rules between neighboring legs instead of a central brain.

The output also has to respond to how fast the reading changes. Without that damping, the legs bounce like an undamped spring.

### Gait Layer (Moderate)

Four legs step in a fixed order: left front, right rear, right front, left rear. This works as a chain of triggers. When one leg's load rune reads full weight, the next leg is allowed to lift.

Before lifting, the body shifts until that leg's load rune reads nearly zero, which proves the weight has moved onto the other three. This sidesteps calculating the center of mass entirely.

### Hard Layer

Steering, route choice and telling a bush from a boulder. A proximity rune reads the nearest object, so tall grass looks like ground. A pilot handles this layer, either a mage or a crew member setting direction and speed while the runes handle everything below.

### Canon Complications

- **Casting damage:** Continuous kinetic runes in steel joints corrupt the metal over time. Rune channels need mithril pathways with mana insulation.
- **Energy:** Lifting a 50-tonne body 5 cm per step takes about 24.5 kJ, or about 2,450 MP at full efficiency. Sustained walking needs mana stones, not a mage's pool.
- **Holding still:** In physics, holding weight does no work. If kinetic runes charge only for movement, standing still is free. If they charge for force, parking on legs drains mana and resting the belly on the ground becomes mandatory.

### Summary

| Layer | Difficulty | Handled By |
|---|---|---|
| Leveling and foot contact | Easy | Per-leg reflex loops |
| Gait sequencing and weight shift | Moderate | Load-triggered rune chain |
| Steering and obstacle judgment | Hard | Pilot |
