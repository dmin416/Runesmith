# Mana Hand Physics

> Physics companion for Mana Hands. Canon conversion and worked actions: `ManaCast.md` § Mana Hands. Form / \(R\) / evolve lock: `../../../Progression/ManaHands.md`. Cast law: `../../../Runes/Energy.md`. Fast nudge pricing: `../../../Combat/MageDefense.md`. Hover: `Flight.md`. Passive all-day hold (Roland): `../../../../Story/Notes/Capabilities/ManaHandsPassive.md`. Nav: `Index.md`.

## 1. Core Quantities

| Quantity | Formula | Unit | What it means |
|---|---|---|---|
| Force | F = m × a | newton (N) | A push or pull. 1 kg weighs 9.81 N. |
| Work | W = F × d | joule (J) | Force applied through a distance |
| Kinetic energy | KE = ½mv² | J | Energy of motion |
| Potential energy | PE = mgh | J | Energy stored by height |
| Momentum | p = m × v | kg·m/s | Carried "shove." Decides knockback. |
| Impulse | F × t = Δp | N·s | Force over time. Changes momentum. |
| Power | P = W ÷ t | watt (W) | How fast joules are delivered |
| Torque | τ = F × r | N·m | Turning force: force times distance from a pivot |
| Pressure | F ÷ Area | pascal (Pa) | Force per area. Concentrates stress. |

Physics laws that still drive everything:

1. **Work happens along the direction of motion.** In ideal physics a force at right angles to motion changes direction without changing speed.
2. **Machines never multiply energy.** Levers, pulleys and gears trade force for distance.
3. **Energy grows with the square of speed. Momentum grows linearly.** Double the speed costs 4× the energy.

Mana Hands canon departs from ideal physics in two places: holding costs drain per second and braking costs the full energy magnitude (section 10).

## 2. Conversion and Budget

Hands do not use Bolt's η(L):

```
mana_paid = Useful_J / (10 × μ(INT) × A) × R
Effective J per paid mana = 10 × μ(INT) × A / R
```

| Caster | μ(INT) | R | J per paid mana |
|---|---|---|---|
| Street baseline (INT 15, unskilled) | 1 | 1 | 10 |
| INT 15, Hands L9 | 1 | 0.1 | 100 |
| Roland mid-hunt (INT 177, Hands L9) | ~7.2 | 0.1 | ~720 |

Hands carry no verbal component, no cast time and no minimum cost. Each action pays its own converted joule cost. One sustained Hands presence performs many actions, with concurrency set by Multitasking. Typical action prices run from under 0.1 J (flip a page) to a few joules (open a door).

**10 J (one paid mana at street baseline) can:**
- Lift 1 kg up 1 m, or 10 kg up 10 cm
- Throw a 10 g pebble at 45 m/s at the Hand
- Throw a 100 g stone at 14 m/s
- Throw a 1 kg rock at 4.5 m/s
- Hold 1 kg aloft for about 10 seconds

**Reference energies:**

| Thing | Energy |
|---|---|
| Longbow arrow | 80-120 J |
| Thrown baseball (145 g at 40 m/s) | 116 J |
| .22 LR rifle | 150 J |
| 9 mm pistol | 518 J |
| Lift a 70 kg person 1 m | 687 J |
| 5.56 rifle | 1,750 J |
| 100 kg boar charging at 8 m/s | 3,200 J |
| .308 rifle | 3,500 J |
| Catch an 80 kg person falling 10 m | 7,800 J |
| 1,000 kg cart at a trot (4 m/s) | 8,000 J |

A 200-mana pool at the unskilled baseline equals 2,000 J of raw energy. The same pool for Roland equals roughly 144,000 J.

## 3. Mass vs. Speed

Same 200 J into different masses, measured at the Hand:

| Mass | Speed | Momentum |
|---|---|---|
| 10 g | 200 m/s | 2 |
| 100 g | 63 m/s | 6.3 |
| 1 kg | 20 m/s | 20 |
| 10 kg | 6.3 m/s | 63 |
| 70 kg (a person) | 2.4 m/s | 167 |

- **Piercing** wants speed on a small area: light, dense, pointed projectiles.
- **Knockback and shoving** want momentum: heavy and slow gives far more shove per joule.
- **Direct body push:** 200 J into 70 kg gives 2.4 m/s on paper as rigid center-of-mass motion. Push height, push duration and the target's recovery step decide whether a fall happens.
- **Stroke length:** energy = force × distance. 200 J across a 2 m stroke needs 100 N average. Across 10 cm it needs 2,000 N.

**Speed retained at range** (subsonic drag, approximate; KE fraction remaining):

| 200 J launch | 20 m | 50 m | 100 m |
|---|---|---|---|
| 10 g stone pebble (~200 m/s) | 71% | 43% | 18% |
| 10 g steel ball | 85% | 66% | 44% |
| 10 g steel dart (6 mm, pointed) | 98% | 95% | 90% |
| 1 kg rock (20 m/s) | ~100% | ~99% | ~98% |

Sectional density (mass ÷ frontal area) decides retention. Darts and bolts keep their energy. Light round projectiles shed it fast.

## 4. Torque and Leverage

- **Push at the far end of the lever.** An opponent's wrist resists roughly 15-20 N·m. 25 N at a sword tip 0.8 m out matches that. Moving the tip 30 cm off line takes 7.5 J of work at slow speed.
- **Toppling a person:** raising a passive rigid body's center of mass past the heel or toe pivot costs 3 to 8 J. That is a theoretical floor. Canon combat price for knocking a standing man off balance is 50 to 100 J, covering stepping, bracing, friction and delivering angular impulse before the recovery step.
- **Rotational energy** = ½Iω². Mass far from the spin axis stores more energy. Spinning a projectile for stability costs a small fraction of its total energy.

## 5. Deflection

An ideal sideways impulse that only rotates the velocity vector costs near zero energy. A cruder model that adds sideways speed while keeping forward speed costs:

| Target | Stop it | Deflect it (conservative model) |
|---|---|---|
| Arrow (30 g at 60 m/s) | 54 J | 10°: 1.7 J |
| Pistol round (8 g at 360 m/s) | 518 J | 2°: 0.63 J (0.7 m miss at 20 m) |
| Boar (100 kg at 8 m/s) | 3,200 J | Sweep a lifted front leg: small cost; the boar spends its own 3,200 J on the ground |

The real gates are delivering the impulse inside the contact window and actuation speed. Canon prices a nudge as scaling with 1/t², so a full mind-speed nudge costs 18 to 54 J.

- **Arrows:** a shot from 30 m takes about 0.5 s to arrive, inside enhanced perception. Reactive deflection works at nudge prices.
- **Bullets:** a 1 ms window against roughly 0.07 s enhanced perception. Reactive deflection is effectively impossible. Only pre-positioned Hands deflect bullets.

## 6. Mana as a Trigger, Not a Motor

| Stored energy | Release cost | Payoff |
|---|---|---|
| 500 kg boulder on a ledge, 10 m drop | Tipping it | 49,000 J |
| Spanned crossbow or spring trap | Pulling the trigger: under 1 J | 100-200 J |
| Rope holding a load | Cutting or untying it | The whole load |
| Charging enemy | A trip at nudge prices | Their full kinetic energy |
| Opponent mid-swing | A nudge to the blade | Swing lands on ground, ally or self |
| Lantern, brazier, powder keg | A tip or a spark | Chemical energy |

**Banking:** a raised stone stores its energy for free only while it rests on something physical (a ledge, a shelf, a propped beam). A stone held up by a Hand pays hold drain the whole time.

## 7. Moving Objects Efficiently

Hold drain is about 1 J/s per kg (80 kg costs 78 J/s, 500 kg costs 490 J/s). Braking pays its full magnitude.

**100 kg crate over 10 m:**

| Method | Cost |
|---|---|
| Drag on wood (μ 0.4) | ~3,900 J |
| Lift 5 cm and glide at the optimal 1.7 m/s | ~910 J (49 lift + 145 accelerate + 145 brake + ~575 hold drain) |
| Roll on wheels | 100-200 J |

**Optimal glide speed** balances kinetic cost (paid twice) against hold drain:

```
v* = (hold_rate_per_kg × distance ÷ 2)^(1/3)
```

It is independent of mass. 10 m gives 1.7 m/s. 100 m gives 3.7 m/s. Slower glides bleed drain. Faster glides overpay kinetic energy.

Priority: roll first, glide second, drag never. Hover is a separate, larger bill priced by actuator-disk math in Flight.md, not the hold row.

## 8. High Force Over Tiny Distances

Work = force × distance, so 5,000 N through 2 mm is 10 J of work. Applying a clamp, prying a lid a few millimeters or jamming a gear is cheap to start. Pinning and clamping then pay drain per second, so duration sets the real bill.

**Concentration:** 200 N on a palm-sized 100 cm² is 20 kPa. The same 200 N on a 1 mm² point is 200 MPa. Stress concentration is not a cutting threshold: piercing also pays fracture and displacement work as the point advances. The Hand has no fixed material hardness. Hardness costs focus and Will on top of the joule bill, so a pointed Hand only works as a point while it is held rigid enough.

## 9. Speed of Actuation

Canon prices fast delivery through actuation kinetic energy rather than a separate watt cap. The faster a Hand must move to act in time, the more it pays, scaling as 1/t². Wind-ups, pre-positioning and set-up before the moment of need all cut this cost.

## 10. Laws of Mana Status

| Rule | Ideal physics | Canon |
|---|---|---|
| Conversion | N/A | 10 × μ(INT) × A ÷ R per paid mana; no η(L) |
| Minimum cost | N/A | None for Hands; no verbal, no cast time |
| Holding still | Zero work | ~1 J/s per kg drain; Roland's all-day budget ~290 kg clothed, shared across all Hands, offset by regen |
| Braking and catching | Negative work, recoverable | Pays full magnitude; no refunds |
| Fast actuation | Power | Priced by actuation KE, ~1/t² |
| Hand hardness | N/A | Focus and Will on top of the joule bill |
| Concurrency | N/A | Set by Multitasking |
| Recoil | Equal and opposite force on something | **Open lock** |

**Recoil options:** a throw could shove the caster, shove the air or shove nothing. Nearby canon leans toward conservation: Mana Shield passes stopped momentum into the caster unless anchored into the ground, and Flight hover dumps momentum into the air. Caster recoil makes heavy throws and pins anchor-dependent. Air recoil adds a backwash. Reactionless pushes remove both limits.

## 11. Efficiency Priorities

1. Release stored energy instead of supplying it.
2. Redirect instead of stopping.
3. Strike the unloaded moment: mid-stride foot, mid-swing blade.
4. Push at the far end of the longest lever.
5. Heavy and slow for knockback. Light, dense and pointed for piercing; darts over balls at range.
6. Set loads down on physical supports. Keep holds short.
7. Roll before gliding. Glide at the optimal speed. Never drag.
8. Pre-position Hands for fast threats instead of reacting.
9. Use force through millimeters for quick clamps; release before drain adds up.
10. Avoid catching and braking when a deflection or a softer stop works.

## 12. Scaling

| Task | Useful J | Mana at 10 J | Mana at 100 J | Mana at ~720 J (Roland) |
|---|---|---|---|---|
| Match a 9 mm round | 518 | 52 | 5.2 | 0.7 |
| Lift a 70 kg person 1 m | 687 | 69 | 6.9 | 1.0 |
| Throw a 10 kg stone at 20 m/s | 2,000 | 200 | 20 | 2.8 |
| Stop a charging boar | 3,200 | 320 | 32 | 4.4 |
| Match a .308 round | 3,500 | 350 | 35 | 4.9 |
| Hold 80 kg for 1 minute | 4,680 | 468 | 47 | 6.5 |
| Catch 80 kg falling 10 m | 7,800 | 780 | 78 | 10.8 |
| Lift a 1-ton block 2 m | 19,620 | 1,962 | 196 | 27 |
| Hold 500 kg for 1 minute | 29,400 | 2,940 | 294 | 41 |

Brute force scales directly with J per paid mana, so for Roland it becomes cheap. Leverage tactics were already cheap in joules and gain less in relative terms. At Roland's scale the limiting factors shift from joules to hold duration, actuation speed, hardness (focus and Will) and Multitasking concurrency.
