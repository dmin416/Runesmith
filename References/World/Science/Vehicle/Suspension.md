# Suspension

Vehicle suspension architecture for carts, coaches, wagons and invent-grade active systems. Era baseline: `../../Tech/Technology.md`. Roads: `Roads.md`. Wheels: `Wheels.md`. Brakes on the unsprung mass: `Brakes.md`. Sprung seats: `Positions.md`.

## Narrative

Caldris road stock uses simple isolation: rigid axles, strap or thoroughbrace coach bodies, and leaf springs once smith guilds can roll and heat-treat strip. Fully active ride control is invent or prestige work. It needs sensors, a controller, actuators and a power plant that can move each corner as fast as the road.

## Detail

### What suspension is doing

The road moves the wheel. The body should stay put. Springing stores bump energy. Damping spends it so the body does not bounce forever. Location links keep the axle or upright where geometry wants it.

**Split the jobs:**

| Job | Passive answer | Active answer |
|---|---|---|
| Hold static weight | Spring (leaf, coil, torsion, air) | Still a spring (or constant force support). Actuators should not carry the whole vehicle weight all day |
| Kill bounce | Friction, hydraulic damper | Controlled damper or actuator force vs velocity |
| Keep body flat through bumps | Soft spring + travel (compromise) | Actuator moves the wheel up into a bump and down into a hole so the body path stays level |
| Know what to do | Geometry and tune | Sensors + controller |

### Caldris baseline (locked feel)

**In reach for craft / early industrial magitech:**

- Rigid axle, no spring
- Strap / chain suspended cabin
- Thoroughbrace leather
- Leaf springs (steel strip + heat treat)
- Located live axles on heavier wagons and rail-adjacent stock

**Not baseline (invent, rare workshop or magic stand-in):**

- Consumer telescopic gas shocks
- Hydropneumatic self-leveling cars
- Magnetorheological / semi-active dampers as common goods
- Fully active hydraulic or electromagnetic corner control
- MacPherson / multi-link mass-auto layouts

### Fully active system (nine parts)

Goal: wheel follows the road. Body motion stays near zero. Five sense, one decides, three do the work.

**Sense**

| # | Part | Role |
|---|---|---|
| 1 | Ride height sensor (each corner) | Gap between body and wheel. Where each corner sits now |
| 2 | Body motion sensor (1–2 on body) | Rise, drop, roll, pitch of the cabin. Target reading: near zero |
| 3 | Wheel motion sensor (each corner) | Instant the tire starts rising or dropping |
| 4 | Road preview (front) | Camera or laser map of bumps ahead. Optional. Feedforward |
| 5 | Speed sensor | Converts preview distance into arrival time at each tire |

Without preview the loop is **reactive**: it only moves after the wheel or body starts to move. With preview it is **feedforward**: it can preload the actuator before contact.

**Preview timing**

```
t_arrive ≈ d_bump / v
```

`d_bump` = distance from preview hit to that tire along the path. `v` = ground speed. Miss speed and the actuator fires early or late and makes the ride worse.

**Decide**

| # | Part | Role |
|---|---|---|
| 6 | Controller | Reads sensors. Commands how far and how fast each corner actuator must move |

**Do**

| # | Part | Role |
|---|---|---|
| 7 | Actuator (each corner) | Pulls wheel up into a bump, pushes down into a dip |
| 8 | Spring (each corner) | Carries static weight so the actuator mostly fights motion, not gravity |
| 9 | Power supply | Hydraulic pump + accumulator, or high-output electric (or magitech equivalent) sized for peak actuator speed × force |

**Why the spring stays:** continuous support of vehicle weight on actuators alone burns power and cooks the hardware. Spring holds `mg` share per corner. Actuator supplies the dynamic delta.

**Order-of-magnitude power (planning):**

```
P_corner,peak ≈ F_act × |v_wheel_rel|
F_act ~ bump force the body would have felt (fraction of corner load)
```

Sharp roads and high speed raise `|v_wheel_rel|` and peak power. Accumulator or mana-stone buffer covers spikes so the pump or generator is not sized for every peak.

### Magic substitutes (invent notes only)

Do not invent D's vehicle kit here. When a build needs active ride without Earth electronics:

- Sense: Mana Sense / shaped pings for gap and body motion. Preview as forward sense pulse
- Decide: skill, scroll logic or a small runic controller
- Act: hydraulic rams with mana pump, or force barriers / Mana Hands at the upright (cost follows Energy / ManaCast law)
- Power: mana stone + pump, not a silent free ride

Failure still needs a passive fallback (leaf or strap) if the active loop dies.

### Build checklist

1. Lock vehicle mass, speed band and road class
2. Choose passive ceiling (leaf / thoroughbrace) or active invent
3. If active: list all nine parts. Mark which are Earth tech vs magic stand-in
4. Size spring for static weight. Size actuator and power for peak bump speed
5. If using preview: wire speed into timing or drop preview and accept reactive lag
6. Keep a passive path when power or control fails

### Earth tech ladder (summary)

| Band | Typical gear |
|---|---|
| Antiquity | Rigid axle; flex floor / frame |
| Medieval–early modern | Strap cabin; thoroughbrace |
| Early industrial | Leaf springs; live axle on leaves |
| Late 1800s–1914 | Coil; pneumatic tire; early independent oddities |
| Early 20th c. | Hydraulic dampers; torsion bar; wishbone; swing axle; tracked Christie |
| Mid 20th c. | Telescopic dampers; MacPherson; air / hydropneumatic; monoshock |
| Late 20th–21st | Multi-link; semi-active; fully active (nine-part above) |

Caldris baseline stops at leaf / thoroughbrace class unless an invent beat unlocks more.

### Best for the job

The nine-part active loop above is the best **ride**. Everything else is the best **passive** answer for a constraint: load, dirt, craft, or packaging. Soft is not automatically best. A spring that moves forever is worse than a stiffer one with a damper.

Body frequency is `f = (1 / 2π) √(k / m)` with `k` in N/m and `m` the sprung mass on that spring. About **1 to 1.3 Hz** feels like a comfortable road vehicle. Sports setups sit nearer **1.5 to 2 Hz**. Much below 1 Hz wallows and floats. The wheel, tire, and upright (unsprung mass) should bounce near **10 to 15 Hz** so the tire stays on the road while the body does not join in.

Damping ratio is `c / (2 √(k m))`. Around **0.3 to 0.5** keeps a ride from bouncing. Toward **0.7** the body stops quicker and feels tighter. At 1.0 the motion dies with no overshoot and the ride goes harsh. Leaf-to-leaf friction is a crude damper and a source of stick-slip, which is why a good leaf still wants a real damper once speeds rise.

Travel has to swallow the bump before the stop. Hitting the bump stop is an infinite spring rate. Dirt and ruts want more travel than a city street: on the order of **100 mm** at the wheel for a fast road vehicle, and **250 mm or more** if the same vehicle is asked to cross broken ground. A coach strap can sway a long way and still fail to keep a wheel down, because nothing damps it and nothing locates it.

| Job | Best passive layout | Why it wins |
|---|---|---|
| Heavy wagon, bad road, smith-built | Semi-elliptic leaf on a solid axle, long travel | One part springs the load and locates the axle. Tough, dirty, and repairable. Add a friction or hydraulic damper when the leaf's own rub is not enough |
| Low-speed coach comfort | Thoroughbrace or strap cabin, then an elliptic leaf | Isolates the body from a rigid axle. The next gain is a damper so the cabin does not pitch all the way into town |
| Unsprung cart, one occupant | A sprung **seat** only (`Positions.md`) | Smaller than springing the whole bed, and it saves the spine |
| Fast road, light vehicle | Double wishbone or multi-link, coil, telescopic damper, anti-roll bar | Camber stays honest in roll, unsprung mass stays low, the anti-roll bar lets the spring stay soft |
| Best geometry you can draw on purpose | Double wishbone | Upper and lower arms set camber gain, roll center, and scrub. Forgable |
| Best refined road geometry | Multi-link | Same freedoms, and longitudinal compliance can be separated from cornering stiffness. Many joints. A late invent |
| Tight space, one corner unit | MacPherson strut | Spring, damper, and location in one tower. The best compromise, not the best camber |
| Articulation, rocks, ruts | Solid axle, long coils or leaves, anti-roll bar that can be disconnected | Both wheels stay planted when the ground twists. Independent looks better on a road and picks up wheels off one |
| Axle location without leaves | Coil or air plus links: trailing arms, a Panhard bar or a Watt's link | A coil does not locate anything. Forget the links and the axle walks |
| Load that changes a lot | Air spring | Height and rate follow pressure, so a full wagon and an empty one sit level. Needs seals, a valve, and a pump |
| Spring tucked out of the way | Torsion bar | Same steel-in-twist as a coil, straightened so it can run along a hull. The tank answer, and some cars |
| One hard landing | Oleo (oil damper + gas spring in one leg) | Dissipates a single impact. The aircraft gear answer, not a road spring |
| Motorcycle front | A double link (Hossack / Telelever class), not a telescopic fork | Braking force does not have to travel down the same tubes that absorb the bump, so the front dives less |
| Rail passenger | Soft secondary spring (air or coil) between bogie and body | The axle-to-bogie spring takes the rail. The second stage takes the people |
| Best ride, invent unlocked | Active corners with road preview (nine-part above) | The actuator puts the wheel up into the bump before the body feels it. Power and a passive fallback are the price |

**Unsprung mass** is whatever moves with the wheel: tire, rim, hub, and usually the brake. Lower is better, because the road has less mass to accelerate. Inboard brakes and light wheels help. A heavy live axle is the cost of the wagon layout's toughness.

**Anti-roll bar:** a spring that only works in roll. Best way to keep a soft ride spring and still not fall over in a corner. Too stiff, and a bump on one wheel twists the other. Off-road, the best bar is one you can unlink so the axle can articulate.

**Anti-dive:** slant the wishbone pivots or the trailing links so braking weight does not pitch the nose as hard. Worth doing on a fast vehicle with real brakes. Irrelevant on a cart.

Caldris baseline stays leaf, strap, and thoroughbrace. The best step up that a smith can actually finish is a longer leaf with a separate damper, or a sprung seat if the axle will not be sprung at all. Wishbones, air, and active corners are invents.

## Open

- Wheel layout: `Wheels.md`
