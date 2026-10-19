# Grip, Bite and Bracing

> Earth invent loot. Friction / interlock / adhesion / bracing ceilings, sprint and jump traction limits, peg-leg and spike scenarios, surface shear catalog. Not Caldris law. Human speed records: `HumanSpeed.md`. Blade / drag-friction speed ceilings: `RunningBladesSpeedLimits.md`. City vs forest speed: `TopSpeedCityVsForest.md`. G-force: `GForceTolerance.md`. Falling: `Falling.md`. Tentacle wrap / friction: `../Vehicle/RigidLinkTentacleArm.md`. Nav: `Index.md`.

Limitations of friction and molecular forces. Sprinting. Jumping. How feet make horizontal force on wood, stone, concrete, dirt and the rest.

---

## Estimating Top Sprint Speed from Traction and Drag

### Sprinting: traction caps acceleration, not strength

Grip limit: Horizontal force from the ground can't exceed μ × normal force. On flat ground the average normal force over a stride is just body weight. Pushing harder only bounces the runner upward. Strength can't create grip.

Typical μ: Rubber on dry asphalt ~0.7 to 0.9, track spikes ~1.0, wet grass ~0.3, ice ~0.05.

Acceleration ceiling: ~μg, about 0.8 to 1 g. Elite sprinters already hit this in the first few steps.

Top speed ceiling: Drag grows with v². Top speed is reached when drag equals the grip available: `v = √(2μmg ÷ ρC_dA)`. For an 80 kg runner (μ 0.8, C_dA ~0.4 m²) that is ~50 m/s (~115 mph), no matter how much power is available. Mass helps only as √m: a 200 kg body tops out around 80 m/s.

Turning and stopping use the same budget: At 50 m/s the tightest turn radius is ~320 m. Stopping distance is ~160 m.

### Jumping: ground strength and the body fail first

Height depends on takeoff speed. Takeoff speed depends on force over a ~0.5 m leg push. Figures assume 80 kg, two-foot takeoff (~0.04 m² of sole), no drag:

| Height | Takeoff speed | Accel | Force | Foot pressure |
|---|---|---|---|---|
| 1 m | 4.4 m/s | 2 g | 0.24 t | 0.06 MPa |
| 10 m | 14 m/s | 20 g | 1.7 t | 0.4 MPa |
| 100 m | 44 m/s | 200 g | 16 t | 4 MPa |
| 1 km | 140 m/s | 2,000 g | 160 t | 39 MPa |

Ground failure: Soil fails around 0.2 to 0.6 MPa, so a 10 m jump off dirt sinks into it. Asphalt cracks at a few MPa. Concrete (20 to 40 MPa) crushes around the 1 km tier. Granite (~150+ MPa) holds much longer.

Drag: Above ~50 m/s drag noticeably cuts real height. A "1 km" launch lands far short.

Landing: Same forces in reverse, unless stopping distance is longer.

### Molecular and biological ceilings

Why μ rarely exceeds ~1: Friction is the shearing of microscopic contact junctions. μ is roughly the softer material's shear strength divided by its hardness, which pins most dry pairs between 0.1 and 1. Exceptions: soft adhesive rubber, gecko-style van der Waals setae, and clean metals in vacuum that cold-weld.

Tendons: ~100 MPa tensile strength. Elite sprinters already load the Achilles (~9 kN peaks) within about a factor of 2 of rupture.

Bones: Cortical bone fails around 130 to 200 MPa. Leg bones break near 1 tonne-force, roughly 12 to 15× body weight.

Soft tissue: Organs and brain take damage past ~50 to 100 g even in short pulses. The 100 m jump tier (200 g) liquefies an unreinforced body.

### Ways around the limits

- **Dig in:** Claws or cleats swap μ for the shear strength of the surface, while tearing it up.
- **Add weight or downforce:** Raises the grip budget directly.
- **Push off walls or ceilings:** Adds normal force in new directions.
- **Lengthen the push:** Crouching deeper or using a longer limb lowers the g-load for the same jump.
- **Spread the foot:** Bigger footprint lowers ground pressure.
- **Reinforce everything:** Tendons, bones and organs each need separate scaling. Muscle strength alone shreds its own attachments.

---

## Grip, Bite and Bracing: Full Breakdown

### 1. Four ways a foot makes horizontal force

| Mechanism | Ceiling set by | Needs body weight |
|---|---|---|
| Friction | μ × normal force | Yes |
| Interlock (spikes, cleats, claws) | Strength of the surface material | Only to embed |
| Adhesion (gecko, suction, magnets) | Bond strength × contact area | No |
| Bracing (pushing on an edge, wall or object) | Compressive strength + anchoring | No |

Real feet stack these. Total grip ≈ friction + interlock + adhesion. Suction and magnets add normal force, so their contribution gets multiplied by μ.

### 2. The molecular ceiling

Why μ sits between 0.1 and 1: Surfaces touch only at microscopic high points. Those points crush until real contact area = load ÷ hardness. Sliding means shearing those junctions. So μ ≈ shear strength ÷ hardness of the softer material (Bowden-Tabor). For most dry pairs that ratio lands near 0.2, with surface roughness and plowing pushing it toward 1.

Van der Waals limit: Two atomically flat surfaces at ~0.4 nm separation stick at roughly 50 to 100 MPa. Real surfaces achieve a tiny fraction because almost nothing touches.

Absolute ceiling for every method: Horizontal force can never exceed the shear strength of the weakest layer × the area engaged. Past that, the surface tears off its substrate (paint, tile, topsoil, wood fibers, the dust layer). Next ceiling is the structure: nails in floorboards, tile adhesive, a slab's footing.

### 3. Spikes: the geometry rule

A cone pressed into a material that yields plastically (wood, soil, ice, soft metal) sinks until the material's hardness × the cone's footprint equals the load. Pushing sideways then loads the cone's side profile. Working it through:

Sideways hold ÷ vertical load = 1 ÷ (π × tan of half the point angle)

Effective μ depends on sharpness, not on the material:

| Point angle | Effective μ |
|---|---|
| 90° (blunt) | 0.3 |
| 60° | 0.55 |
| 30° | 1.2 |
| 20° | 1.8 |
| 10° | 3.6 |

Add ordinary sole friction on top. The catches:

- Depth scales with √(load ÷ hardness). Soft ground swallows the point. Hard ground barely admits it.
- Brittle materials break the rule. Concrete, stone, ice and wood loaded along the grain crack and chip a wedge out in front of a shallow spike. Hold drops to tensile strength × breakout area, often a fraction of the plastic value.
- Sharp points snap. Bending stress at the root of a 30° cone ≈ 66 × sideways force ÷ depth². At 3 kN sideways: 2 cm deep gives ~500 MPa (hardened steel survives, mild steel bends). 2 mm deep gives ~50 GPa (any tip shears off). Shallow bites on hard surfaces destroy points. This is why crampon points are thick and cleats are short and blunt.
- Splitting load among many points keeps the same total hold while each bites shallower, which protects tips and reduces chipping. Spread too thin and none penetrate (bed of nails effect), reverting to plain friction. Maximum biting points ≈ load ÷ (surface hardness × tip area).
- Extraction costs. Wood clamps a spike like a nail. Mud adds suction (up to 101 kPa × the plug's area). Every stride spends time and energy pulling free.
- Every step leaves a hole. Sustained sprinting chews up floors, decks and trails.

### 4. How deep a sharp spike goes

Single steel point, 30° tip, 2.4 kN load (sprint peak for 80 kg):

| Surface | Depth | Result |
|---|---|---|
| Mud | 30 cm+ | Plunges, suction on pull-out |
| Loose sand | 15 to 25 cm | No hold, sand flows |
| Fresh to packed snow | 10 to 30 cm | Weak hold unless firm |
| Packed dirt | 5 to 10 cm | Strong hold |
| Softwood | ~2 cm | Strong hold, sticks |
| Hardwood | ~1.5 cm | Strong hold, sticks |
| Ice | 1 to 2 cm | Strong hold, chips if shallow |
| Asphalt | 1 to 3 cm | Good in heat, wanders off embedded stones |
| Mild steel | 1 to 3 mm | Needs a hardened point |
| Brick | ~5 mm | Chips |
| Concrete | 2 to 4 mm | Crushes paste, deflects off aggregate, tip dulls |
| Granite | ~1 mm | Quartz is harder than steel; tip dulls first |
| Glass | None | Skids or starts a crack |

### 5. Peg-leg scenarios

**Blunt wooden peg (3 cm tip)**

- Wood on dry stone μ ~0.3 to 0.5, on wet tile 0.1 to 0.2. Worst case: polished wet floor.
- No ankle and no toe means no push-off lever. The tip pivots under any off-axis load.
- Pressure: 1.1 MPa standing, 3.4 MPa at sprint peak. Soil fails around 0.2 to 0.6 MPa, so it sinks into dirt, lawn, sand and snow every step.
- Once sunk in firm clay the hole acts as a socket and grip can exceed μ 1, at the cost of pull-out.

**Rubber-capped peg (crutch tip)**

- μ 0.7 to 1.0 on dry hard surfaces. Still sinks in soft ground. Wet polished surfaces drop it to 0.2 to 0.4.

**Sharp steel peg**

- μ_eff 1.2 to 1.5 on wood, ice, packed dirt, warm asphalt and mild steel decking.
- Fails on concrete, granite and glass (skids like an ice pick on a mirror, μ ~0.2 to 0.4).
- Fails on sand, mud and snow by plunging. Fix: a stop disk 2 to 3 cm up the shaft, like a ski-pole basket, which caps depth and adds bearing area.
- Acts as a pivot pin in soft materials. Sharp turns become possible by swinging around the planted spike, limited only by spike bending and the material tearing out.
- Grinds down on every concrete step.

**Multi-tine peg (fork or crampon pattern, 4 to 12 points)**

- Same total hold as one spike, shallower bites, much longer tip life. Best all-round spike design for dirt, wood, ice and snow. Still useless on glass and hard stone.

**Knife-edge blade (skate-like line contact)**

- Directional. Along the edge: almost no resistance (skate on ice μ ~0.01, cuts grooves in wood). Across the edge: bearing over the whole blade length, very high hold.
- Rewards a skating stride that pushes diagonally. Strong cornering.

**Wide spiked plate (snowshoe with cleats)**

- Large area stops sinking. Spikes engage soil. Best design for sand, snow and mud.

### 6. Foot covered in microspines

Microspines (as on wall-climbing robots) are hundreds of tiny hooked points on individually sprung mounts. They catch existing bumps rather than penetrating.

- Each spine holds ~1 to 10 N on a bump. A foot with 1,000 spines could hold several kN.
- Works on rough hard surfaces where penetrating spikes fail: concrete, brick, rough stone, bark, stucco.
- Fails on smooth surfaces: glass, polished stone, metal, glazed tile.
- Complements gecko pads exactly. Microspines cover rough hard surfaces; gecko pads cover smooth ones; large spikes cover soft ones.

### 7. Gecko pads and van der Waals

- Real gecko pads: ~0.1 MPa in shear. Best synthetic pads: ~0.3 MPa on glass.
- A 0.02 m² foot at 0.1 to 0.3 MPa gives 2 to 6 kN of shear per foot. For 80 kg that is 2.5 to 7 g, independent of body weight. Works on walls and ceilings.
- Directional: Grip engages when dragged toward the heel. Straight pull-off strength is much weaker. Release happens by peeling the pad at ~30°, which suits running.
- Needs: smooth, clean, dry, rigid surfaces with decent surface energy. Glass, polished stone, metal, gloss paint, smooth plastic.
- Fails on: dust (grit coats the pad each step), water films, Teflon or wax, rough surfaces (concrete, asphalt, bark, carpet) and loose ground.
- At superhuman grip the surface fails first: paint peels at ~1 to 5 MPa, tile adhesive releases at ~1 to 2 MPa, window panes pop out of frames.

### 8. Suction, magnets, electroadhesion

- **Suction:** Maximum = atmospheric pressure (101 kPa) × area. A foot-sized cup adds ~2 kN of clamping. Smooth non-porous surfaces only. Weaker at altitude (~70 kPa at 3,000 m), stronger underwater.
- **Magnets:** Clamping pressure ≈ B² ÷ 2μ₀. Neodymium at 1.4 T: ~0.8 MPa. Saturated electromagnet at 2 T: ~1.6 MPa. A foot-sized pad gives 16 to 32 kN of clamping, so 8 to 16 kN of shear at μ 0.5. Strongest method available. Thick ferromagnetic steel only; thin sheet saturates and holds a fraction; most stainless is non-magnetic.
- **Electroadhesion:** 1 to 20 kPa. Weak but works on rough surfaces.
- **Wet adhesion (tree frog):** 1 to 5 kPa. Weak.

### 9. Bracing and compressive pushes

- **Flat face:** Limited by compressive strength × contact area, boosted 2 to 3× when the load sits away from edges. A concrete wall face takes hundreds of kN under a foot.
- **Edges fail early.** Corners are unconfined and break in tension. A toe on a concrete step nosing spalls it at a few tonnes. Brick and stone ledges fail at the mortar first (bond shear ~0.2 to 1 MPa).
- **Drywall** (gypsum, 3 to 6 MPa) punches through under hard kicks.
- **Anchoring:** Whatever gets pushed must stay put. A 1,500 kg car slides at ~10 kN. A launch to 44 m/s off a free-sliding car pushes it back at ~2.3 m/s. Loose rocks, furniture and shallow-rooted trees move.
- **Wall runs:** Friction on a wall needs pushing into it, which pushes the body away. Duration lasts only until sideways momentum runs out. Gecko pads, microspines or magnets remove that limit.

### 10. Surfaces in detail

#### Loose ground

- **Dry sand:** Zero cohesion, internal friction angle 30 to 35°. Effective μ ~0.5 to 0.6, but the top layer slides. Bearing 0.1 to 0.3 MPa. Spikes plow. Wide plates win.
- **Wet sand:** Capillary cohesion of a few kPa. Much firmer. Saturated and vibrated, it liquefies.
- **Gravel:** Rounded stones roll like bearings. Effective μ 0.4 to 0.6. Spikes shove stones aside. Each push sprays gravel backward.
- **Mud and soft wet clay:** Shear strength 5 to 25 kPa. Rubber μ 0.2 to 0.4. Heavy suction on pull-out.

#### Firm ground

- **Packed dirt:** Cohesion 10 to 50 kPa, bearing 0.2 to 0.6 MPa. Cleats and spikes work well. Grip ceiling ≈ footprint area × (cohesion + pressure × tan of friction angle), giving effective μ near 0.9 for a cleated shoe. Longer spikes engage a larger wedge of soil, with resistance growing roughly with depth².
- **Dry stiff clay:** Cohesion 50 to 200 kPa. Strong footing.
- **Grass and turf:** Roots add 10 to 30 kPa in the top 10 cm. Rubber μ 0.35 to 0.5 dry, 0.2 to 0.3 wet. Overloaded cleats tear out a divot.
- **Snow:** Fresh snow holds under 1 kPa. Packed snow 10 to 100 kPa. Rubber μ 0.2 to 0.4.

#### Frozen

- **Ice:** Rubber μ 0.05 to 0.15 near 0 °C because of a meltwater film, rising toward 0.3 to 0.5 at −30 °C. Compressive 5 to 25 MPa, higher at fast loading and lower temperatures. Tensile only 1 to 2 MPa. Spikes bite well but shallow bites chip out.

#### Wood

- **Softwood (pine, fir):** Compressive 30 to 50 MPa along the grain, 3 to 7 MPa across it. Shear 6 to 10 MPa. Splits at 2 to 4 MPa tension across the grain.
- **Hardwood (oak, maple):** Compressive 50 to 60 MPa along the grain, 7 to 10 MPa across. Shear 10 to 14 MPa.
- **Grain direction:** A spike pushed along the grain wedges fibers apart and splits the board. Pushed across the grain, it crushes fibers and holds far better.
- **Finished floors:** Rubber μ 0.4 to 0.6 dry, 0.2 to 0.3 wet. Socks ~0.2 to 0.3.
- **Decks and floorboards:** Each nail or screw takes ~0.5 to 1.5 kN sideways. Superhuman pushes rip boards off fasteners before the wood itself fails. Plywood delaminates.

#### Pavement

- **Asphalt:** Rubber μ 0.7 to 0.9 dry, 0.5 to 0.7 wet. Compressive 2 to 10 MPa, heavily temperature-dependent. Soft and rutting above ~45 °C, brittle below freezing. Embedded stones deflect spikes.
- **Concrete:** Rubber μ 0.6 to 0.85 dry, 0.45 to 0.6 wet. Polished concrete wet drops to 0.2 to 0.4. Compressive 20 to 40 MPa, tensile 2 to 4 MPa. Strength rises 1.5 to 2× under impact-speed loading. The thin top skin is weaker than the core.

#### Stone and masonry

- **Brick:** Compressive 20 to 50 MPa typical. Mortar is the weak link. Bricks set in sand pop out individually.
- **Sandstone:** Compressive 20 to 170 MPa, tensile 2 to 10 MPa. Grains break loose under spikes. Rubber μ 0.6 to 0.9 dry. Notably weaker when wet.
- **Limestone:** Compressive 30 to 250 MPa. Worn smooth steps become very slick when wet.
- **Granite and basalt:** Compressive 100 to 300 MPa, tensile 7 to 25 MPa. Quartz content outlasts steel points. Rough granite gives rubber μ 0.8 to 1.0.
- **Polished marble and stone:** Rubber μ 0.4 to 0.6 dry, 0.1 to 0.2 wet. Ideal for gecko pads.
- **Glazed tile:** Wet μ 0.1 to 0.3. Bonded at 1 to 2 MPa, so heavy shear pops tiles loose.

#### Manufactured

- **Mild steel plate:** Yield ~250 MPa, hardness ~1.3 GPa. Rubber μ 0.5 to 0.7 dry, ~0.1 oily. Raised tread plate adds interlock. Magnets dominate.
- **Sheet metal roofing:** Dents and buckles under concentrated load before grip runs out.
- **Glass:** Annealed tensile ~40 MPa, hardness ~6 GPa. Rubber μ 0.9+ dry, 0.2 to 0.4 wet. Spikes start cracks; tempered glass shatters entirely. Gecko pads and suction are ideal.
- **Carpet:** Spikes snag fibers. The whole carpet can slide on its pad. Loose rugs on hardwood slide at μ ~0.3.
- **Vinyl:** Rubber μ 0.5 to 0.7 dry, 0.2 to 0.4 wet.

### 11. Best method by surface

| Surface | Best grip |
|---|---|
| Sand, snow, mud | Wide plate + cleats |
| Dirt, turf | Cleats, multi-tine spikes |
| Wood, ice | Sharp multi-tine spikes |
| Asphalt | Rubber, or spikes when warm |
| Concrete, brick, rough stone | Microspines, rubber |
| Glass, polished stone, tile | Gecko pads, suction |
| Thick steel | Magnets |

### 12. What better grip buys in speed

Top speed on flat ground occurs where average grip equals drag: `v = √(2 × average grip ÷ (air density × C_dA))`. For an 80 kg runner:

| Foot | Top speed |
|---|---|
| Rubber sole, μ 0.8 | ~50 m/s |
| 20° spikes in wood, μ_eff 1.8 | ~75 m/s |
| Gecko pads, 4 kN, 40% ground contact | ~80 m/s |
| Magnets on steel deck, 10 kN | ~130 m/s |

Turning radius follows the same budget: `radius = v² ÷ (grip ÷ mass)`. Doubling grip halves the turn radius at any speed.

### 13. Order of failure as grip increases

1. The grip mechanism itself (friction, bite, bond)
2. The surface layer (topsoil, paint, wood fibers, tile adhesive)
3. The spike, claw or pad (bending, dulling, delamination)
4. The structure under the surface (fasteners, mortar, footings)
5. Anchoring of loose objects (cars, rocks, furniture)
6. The body (tendons ~100 MPa, bone 130 to 200 MPa, organs past ~50 to 100 g)
7. Air drag, which grows with v² regardless of everything above
