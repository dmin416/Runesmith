# Suspension

Vehicle suspension architecture for carts, coaches, wagons and invent-grade active systems. Era baseline: `../../Tech/Technology.md`. Roads: `Roads.md`. Wheels: `Wheels.md`.

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

## Open

- Absorb Old `Wheels.md` → `Wheels.md`
