# Legged Vehicles and Wheel-Legs

> Earth reference / invent loot. Not locked law. Wheel physics: `WheelScience.md`. Vehicle families: `VehicleTypes.md`. Suspension: `Suspension.md`. Mounts design: `../../Fauna/Design/MountsDesign.md`.

Nav: `Index.md`.

Articulated arms, walking machines and wheels on legs. Extracted from the wheels encyclopedia so wheel physics stays one job.

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

