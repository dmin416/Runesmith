# Superposition vs Added Energy: Kinetic Impartation

> Earth / invent loot. Not locked law. Assumes ideal, perfectly synchronized superposition: pushes occupy the same point at the same instant and add with no losses. Kinetic hub: `Kinetic.md`. Wave example: `SevenFirecrackers.md`. Sound power: `Sound.md`. Impact stroke: `../../../Combat/ImpactRune.md`. Cast tables: `ManaCast.md`.

**Energy delivered always equals energy supplied.** Superposition never multiplies energy. The result depends entirely on how a "push" is defined.

---

## Key Point

| Push defined by | What superposition does |
|---|---|
| **Capped energy** (each push can give at most 100 J) | Energies add as N. Two pushes = 200 J. Identical to instantly imparting 200 J. |
| **Fixed force** (the force that would give a resting ball 100 J) | Forces add as N. Each source works against a faster ball and supplies more energy. Two pushes = 400 J supplied and delivered. |

## Core Physics

Superposition adds the **linear** quantities: amplitude, force, impulse, momentum, velocity.

Kinetic energy scales with velocity **squared**:

KE = ½mv²

- Adding energy raises velocity by the square root of the energy increase.
- Adding force raises velocity directly. The energy needed then rises by the square, and the sources must supply it.

## Worked Example

Ball mass: 2 kg (chosen to keep the numbers clean)

### Case A: One 100 J push

v = √(2 × 100 / 2) = **10 m/s**
p = 2 × 10 = **20 kg·m/s**
KE = **100 J**

### Case B: Instantly impart 200 J

v = √(2 × 200 / 2) = **14.14 m/s**
p = 2 × 14.14 = **28.28 kg·m/s**
KE = **200 J**

### Case C: Two superimposed pushes, each capped at 100 J

Total energy supplied = 200 J

v = **14.14 m/s**
p = **28.28 kg·m/s**
KE = **200 J**

Identical to Case B. Nothing more.

### Case D: Two superimposed fixed-force pushes

Each push alone gives 10 m/s. Superimposed, the forces add and the velocities add:

v = 10 + 10 = **20 m/s**
p = 2 × 20 = **40 kg·m/s**
KE = ½ × 2 × 20² = **400 J**

Total energy supplied by the sources = **400 J**

### Comparison

| Case | Energy supplied | Velocity | Momentum | Ball KE |
|---|---|---|---|---|
| A: One 100 J push | 100 J | 10 m/s | 20 kg·m/s | 100 J |
| B: Instant 200 J | 200 J | 14.14 m/s | 28.28 kg·m/s | 200 J |
| C: Two superimposed, capped at 100 J | 200 J | 14.14 m/s | 28.28 kg·m/s | 200 J |
| D: Two superimposed fixed-force | 400 J | 20 m/s | 40 kg·m/s | 400 J |

Case D delivers more only because the sources supply more. In every case, ball KE equals energy supplied.

## Why Fixed-Force Superposition Draws 400 J

A fixed-force push applies force F for time t. On a resting ball it covers distance d, and work = F × d = 100 J.

Superimposed, the ball feels 2F. It accelerates twice as fast and covers 2d during the same time t. Each source still applies F, but now over 2d:

| | Force per source | Distance during push | Work per source | Total work |
|---|---|---|---|---|
| One source alone | F | d | 100 J | 100 J |
| Two superimposed | F | 2d | 200 J | 400 J |

Each source supplies **twice its solo energy** from its own reserve. Two superimposed fixed-force pushes are identical to one push with double the force.

## Sequential vs Superimposed

| Push type | Two pushes superimposed | Two pushes in sequence |
|---|---|---|
| Fixed force | 20 m/s, 400 J | 20 m/s, 400 J |
| Capped at 100 J | 14.14 m/s, 200 J | 14.14 m/s, 200 J |

On a free ball, sequence and superposition reach the same final state. A later fixed-force push acts on a faster ball and does more work, just as superimposed pushes do.

What superposition uniquely provides is **timing**: the full result arrives in one push duration instead of N durations, so **peak force** is higher.

## Scaling With More Pushes

N pushes, each defined from a 100 J base:

| N | Capped pushes (KE) | Fixed-force pushes superimposed (KE = energy supplied) | Fixed-force velocity |
|---|---|---|---|
| 1 | 100 J | 100 J | 10 m/s |
| 2 | 200 J | 400 J | 20 m/s |
| 3 | 300 J | 900 J | 30 m/s |
| 5 | 500 J | 2,500 J | 50 m/s |
| 7 | 700 J | 4,900 J | 70 m/s |
| 10 | 1,000 J | 10,000 J | 100 m/s |
| 100 | 10,000 J | 1,000,000 J | 1,000 m/s |

- Capped pushes: energy scales as **N**.
- Fixed-force pushes: force and velocity scale as **N**, energy supplied and delivered scale as **N²**.

## By Type of Push

Each table compares one source, one source with doubled energy input and two superimposed fixed-amplitude sources. The energy-supplied row shows where the output comes from.

### Shockwave (pressure pulse)

Overpressure is an amplitude, so superimposed pulses add pressure directly.

| Quantity | Normal | Doubled energy | Two superimposed |
|---|---|---|---|
| Energy supplied | 1x | 2x | 4x |
| Peak pressure / force | 1x | 1.41x | 2x |
| Impulse delivered | 1x | 1.41x | 2x |
| Target velocity | 1x | 1.41x | 2x |
| Target KE | 1x | 2x | 4x |

### Amplitude-driven wall (force set by field strength)

Same scaling as the shockwave table.

### Intensity-driven wall (radiation-pressure style, sustained push)

Pressure is proportional to intensity, which is already amplitude squared. A constant force then gives target KE proportional to force squared.

| Quantity (same push time) | Normal | Doubled energy | Two superimposed |
|---|---|---|---|
| Beam energy supplied | 1x | 2x | 4x |
| Pressure / force | 1x | 2x | 4x |
| Target velocity | 1x | 2x | 4x |
| Distance pushed | 1x | 2x | 4x |
| Target KE | 1x | 4x | 16x |

Only a small fraction of a radiation-pressure beam's energy reaches the target as motion, so target KE can scale faster than beam energy without breaking conservation.

### Merged projectiles (same total energy)

Two identical 100 J projectiles superimposed vs one 200 J projectile. Both carry 200 J.

| Quantity | One 200 J projectile | Two merged 100 J projectiles |
|---|---|---|
| Energy | 200 J | 200 J |
| Velocity | 1.41x | 1x |
| Momentum | 1.41x | 2x |
| Push on a heavy target | 2x | 4x |

Here the energy really is equal. The difference is how it is split between mass and speed.

- Single fast projectile favors **speed**: penetration and heating.
- Merged projectiles favor **momentum**: pushing and knockback.

## Friction Heating at One Spot

Friction converts directed motion into heat at the contact point. Heat produced equals the kinetic energy converted.

| Setup (2 pushes from a 100 J base) | Energy supplied | Heat at spot |
|---|---|---|
| Two different spots | 100 J each | 100 J each |
| Same spot, capped pushes | 200 J | 200 J |
| Same spot, random timing or direction (fixed force) | 200 J | 200 J |
| Same spot, synchronized fixed-force pushes | 400 J | 400 J |

Direct rubbing: friction heating power = friction coefficient × normal force × sliding speed. Superimposed sources double the force. If they also double sliding speed, heating power is 2 × 2 = **4x**, and the sources must supply that 4x.

## Limits

| Limit | Effect |
|---|---|
| Source energy reserve | Fixed-force sources must each supply N times their solo energy. A source capped at 100 J caps the total at N × 100 J. |
| Pusher speed | A pusher only imparts velocity while it keeps contact. Each source must be able to move N times faster than its solo push. |
| Timing and overlap | Pushes must overlap within a small fraction of the push duration. For waves, phase error must be small compared to one period and overlap must be within a fraction of a wavelength. |
| Target strength | N times the force means N times the stress. Past the material's strength, energy goes into deforming or shattering the target instead of moving it. |
| Speed of light | Velocities cannot add past c. Near light speed the N² scaling disappears. |

## When Superposition Beats a Plain Push

| Situation | Superimpose? |
|---|---|
| Limit is total energy available | No. Same energy, same result. |
| Free ball, plenty of time | No advantage over pushing longer with the same force. |
| Limit is maximum force per source (muscle, emitter amplitude, max thrust) | Yes. N sources give N times the force. |
| Short contact window | Yes. All the impulse lands inside the window. |
| Breaking a threshold (static friction, armor, material strength) | Yes. Peak force is what crosses thresholds. |

**Hypothetical-system loophole:** if each push costs a fixed amount regardless of what the target is doing, superposition delivers N² output for N cost. That is effectively unlimited energy and is the loophole any such system must account for.

## Sound Reference

| Sources | Superimposed origin | Spread-out speakers | Gap |
|---|---|---|
| 2 | +6 dB | +3 dB | 3 dB |
| 7 | +16.9 dB | +8.5 dB | 8.5 dB |
| 10 | +20 dB | +10 dB | 10 dB |
| 100 | +40 dB | +20 dB | 20 dB |

One source with 2x energy: +3 dB. Two sources superimposed: +6 dB (4x intensity). The superimposed sources each radiate twice their solo power, drawing it from their own supply (mutual coupling).

Seven firecrackers superimposed: 7x pressure, 49x energy density under pure wave superposition. With each firecracker capped at its own chemical energy, the total is 7x energy and about 2.65x pressure.

## Summary

| Comparison | Result |
|---|---|
| Instant 200 J vs two superimposed pushes capped at 100 J | Identical: 200 J, 14.14 m/s |
| Two superimposed fixed-force pushes | 400 J, 20 m/s, because the sources supply 400 J |
| N superimposed fixed-force pushes | N² energy, all of it drawn from the sources |
| Same energy, merged projectiles vs one fast projectile | Same energy, 41% more momentum per doubling |
| Unique benefit of superposition | Higher peak force in a shorter time |

Superposition stacks **force and velocity**. It never creates energy. Whatever kinetic energy the target gains, the sources supplied.

## Terra readout (soft)

| Piece | Note |
|---|---|
| **Mana / rune cost** | Prefer **capped Useful J** (Case C). Fixed-force stacking without drawing N² mana is the loophole above |
| **SevenFirecrackers** | Wave amplitude case; 7x pressure / 49x intensity only while sources can supply N² energy density |
| **Impact rune** | Stroke adds ΔKE as Useful J; stacking strokes without extra paid mana does not unlock Case D |
| **Merged bolts** | Same total energy → more momentum, less speed than one hot projectile |
