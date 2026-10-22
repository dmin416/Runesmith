# Spin

> **Design loot / Earth physics.** Rotation as a tool. Centrifuges, spin drying, projectile stabilization, curve shots, gyroscopes, vortices, rotary tools and spinning bodies. Not automatic law.
>
> Cast law: `../../../Runes/Energy.md`, `ManaCast.md`. Mana Hands pricing and the braking rule: `ManaHandPhysics.md`. Flywheels: `FlywheelStorage.md`, `FlywheelApplications.md`. Random Magnus on unrifled shots: `Projectiles.md`. Stability, CP and CM: `ProjectileShapes.md`. Vestibular sense: `../Body/AccelerometersGyroscopesVestibular.md`. G tolerance: `../Body/GForceTolerance.md`. Drying and separation floors: `EnergyPumping.md`. Shear: `Shear.md`. Pressure: `Gradients.md`. Vortex rings: `../../../Combat/SonicAirDisplacement.md`.

## Shared cost law

- **1 MP = 10 J.** Raw MP below is J ÷ 10. Real casters divide by their conversion (`ManaHandPhysics.md` §2).
- **Stopping a spin costs the same as starting it.** Damping rotation pays the full rotational energy removed (`ManaHandPhysics.md` §10). Let things coast down on their own friction when time allows.
- **Spin is stored energy.** A spinning wheel keeps its energy until friction takes it. Spin up early and use it later (`FlywheelStorage.md`).

## Formulas

```
Rotational energy    E = ½ × I × ω²             (ω in rad/s = rpm × 2π ÷ 60)
Angular momentum     L = I × ω
Spin acceleration    a = ω² × r       g-number = ω² × r ÷ 9.81
                     RCF ≈ 1.118 × 10⁻⁵ × r(mm) × rpm²
Rim speed            v = ω × r        energy per kg at the rim = ½ v²
Gyro precession      Ω = torque ÷ L
Magnus side force    F = ½ × ρ × v² × A × C_L     (C_L about 0.2 to 0.3 for a spinning ball)
```

| Shape | Moment of inertia I |
|---|---|
| Thin ring or rim | m r² |
| Solid disc | ½ m r² |
| Solid sphere | ⅖ m r² |
| Rod about its middle | m L² ÷ 12 |
| Standing person about the vertical axis | about 1 to 1.5 kg·m² |

**Same spin, less energy:** pull mass toward the axis. A skater spins faster with arms in at no cost. A Hand that tucks a falling body's limbs speeds its flip for free.

## Centrifuges and spin separation

| Device | Speed | Radius | Spin force |
|---|---|---|---|
| Salad spinner | 600 rpm | 10 cm | about 40 g |
| Honey extractor | 300 rpm | 25 cm | about 25 g |
| Spin dryer | 1,200 rpm | 25 cm | about 400 g |
| Blood centrifuge | 3,000 rpm | 15 cm | about 1,500 g |
| Cream separator | 4,700 to 7,700 rpm bowls | | about 3,000 to 6,000 g |

Dense parts move out. Light parts move in. Separation speed scales with the spin force.

| Job | Cost | Raw MP |
|---|---|---|
| Spin 1 kg of milk at the rim of a 15 cm, 6,000 rpm bowl | about 4.4 kJ per kg passed through (rim speed 94 m/s) | about 440 per kg |
| Spin 2 kg of wet laundry to 1,200 rpm | under 1 kJ to spin up, the same to stop | under 100 each way |
| Spin out free water from 0.5 kg wet cloak | a few hundred J | tens |
| Evaporate the same water instead | 1.13 MJ | 113,000 |

- **Cream and butter.** Cream skimmed in minutes instead of a day of settling.
- **Blood and serum.** Plasma separation for medicine (`../Medicine/Antivenom.md` serum work, `../Body/BloodTech.md`).
- **Honey, oils and juices.** Clear liquids without long settling or filter cloth.
- **Drying.** Spin first and evaporate only the remainder (`EnergyPumping.md` §3).
- **Ore and sand.** Heavy minerals spun out of slurry. Gold and titanium sands (`../Metallurgy/TitaniumBootstrap.md`).
- **Cyclone separator.** Spin a dust-laden airflow so the particles fly out to the wall. No filter. Works on sawdust, flour, ash and grit above a few microns.

## Spin on projectiles

Spin keeps the axis pointed and cancels random Magnus drift (`Projectiles.md`). It costs almost nothing.

| Round | Spin | Spin energy | Flight energy | Share |
|---|---|---|---|---|
| 9 mm pistol (1 in 10 twist) | about 1,400 rev/s | about 2.6 J | 518 J | 0.5% |
| 5.56 rifle (1 in 7 twist) | about 5,300 rev/s | about 7 J | 1,770 J | 0.4% |

- A Hand-thrown dart, bolt or stone spun about its long axis flies truer for under 1% extra cost.
- Statically unstable shapes (CP ahead of CM) need the spin to survive (`ProjectileShapes.md`).
- A thrown axe or knife spins end over end. Stopping that spin so it lands flat costs its rotational energy. A 1.5 kg axe at 2 rev/s holds about 6 J.

### Curve shots (Magnus)

| Throw | Speed | Range | Sideways curve |
|---|---|---|---|
| Baseball with strong spin | 40 m/s | 18 m | about 0.6 m |
| 100 g, 4 cm stone | 30 m/s | 20 m | about 0.4 m |

Enough to bend a shot around a shield edge or a tree at short range. Not enough to circle a corner. Spin ratio (rim speed ÷ flight speed) about 0.3 to 0.5 gives the strongest curve. Magnus needs air and a real object. A pure mana packet with no air grip does not curve this way.

## Gyroscopes

A 1 kg disc, 10 cm radius, at 6,000 rpm holds about 990 J and L ≈ 3.1 kg·m²/s. Hang 1 kg on it 10 cm off the axis and it does not fall. It turns slowly sideways (precession) at about 0.3 rad/s, one lap in about 20 s.

- **Stabilizer.** A spinning disc steadies a glider, a saddle, a tray of glassware or a hand-held sight.
- **Heading keeper.** A good gyro holds its axis in space. A gyrocompass needs very low friction. Indestructible bearings help (`FrictionNotes.md`).
- **Cost.** Spin-up once. Bearing and air friction drain slowly. Stopping it pays its energy back out.

## Spinning bodies

| Job | Cost | Note |
|---|---|---|
| Spin an airborne person 1 rev/s | about 24 J | A jumping or falling target |
| Spin an airborne person 3 rev/s | about 210 J | Landing goes badly |
| Spin a standing person against foot friction | about 250 J per turn | Friction at the feet dominates |
| Turn yourself 180° in 0.5 s | about 160 J (spin up plus stop) | |
| Turn yourself 180° in 0.2 s | about 990 J | Fast whole-body turns cost a lot. Turn the eyes or use 360 sight (`../Body/Vision360.md`) |

Dizziness and nausea follow sustained spin and a sudden stop (vestibular fluid keeps moving). Ten or so fast turns blur balance for most people.

## Vortices

| Vortex | Core pressure drop | Note |
|---|---|---|
| Dust devil, 10 m/s | about 120 Pa | Lifts dust, leaves and loose cloth |
| Strong tornado, 100 m/s | about 12 kPa | Roofs and walls fail from the pressure jump and the wind |

- **Vortex rings** carry a puff of air or smoke far without spreading. Signal smoke, scent decoys, candle snuffing at range.
- **Whirlpools** gather floating debris to the center. Drain or skim a pond.
- **Fire whirls** form when a fire gets spin. Burn rate and flame height jump. Never spin a fire unless the goal is a bigger fire.
- **Vortex tube.** Spun compressed air splits into a hot and a cold stream with no moving parts. Real but wasteful. A heat pump is far cheaper (`EnergyPumping.md`).

## Rotary tools

| Tool | Typical power | Raw MP/s |
|---|---|---|
| Spinning wheel (yarn) | tens of W | a few |
| Potter's wheel while centering | about 100 to 400 W | 10 to 40 |
| Grinding or sharpening wheel | about 200 to 500 W | 20 to 50 |
| Small lathe or drill | 0.25 to 1 kW | 25 to 100 |

Spin the work or the tool, never both. A Hand that turns a lathe chuck for a smith or a wheel for a potter replaces an apprentice on a treadle.

## Small notes

- **Coriolis** is negligible at human scale. It matters for long-range artillery and for weather.
- **Wheels.** A 15 kg cart wheel at 3 m/s holds about 68 J of spin on top of the cart's straight-line energy. Braking pays both.
- **Rope and thread.** Twist is spin stored in fibers. Plying two strands with opposite twist locks them.

## Potential

- **Spin Separator.** Cream, serum, honey, oils, juice and heavy-mineral sand.
- **Spin Dry.** Cloaks, leather, herbs and laundry for tens of MP instead of tens of thousands.
- **Rifling Spin.** Under 1% extra on any Hand-thrown dart or bolt for a straight, predictable flight.
- **Curve Throw.** Bend a stone or a ball around a shield edge.
- **Gyro Steady.** A spinning disc holds a mount saddle, a glider or a tray level.
- **Tumble.** Spin an airborne foe for tens to hundreds of joules. Wrecks their landing.
- **Vortex Ring.** Carry smoke, scent or a puff of air far and tight.
- **Cyclone Dust.** Clear sawdust, flour and ash from a shop without a filter.
- **Wheel Drive.** Turn a lathe, potter's wheel, grindstone or spinning wheel.

## Open

- Whether Hands can grip a fluid well enough to spin it directly or must spin a container.
- Spin-up of mana packets (Bolt, Arrow) for stability. Mana flight may not need it.
