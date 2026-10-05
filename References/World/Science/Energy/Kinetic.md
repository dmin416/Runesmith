# Kinetic

Hub: `../Science.md`. Cast law: `ManaCast.md`. Flywheel pairs: `Generators.md`. Pinch launch energies: `Projectiles.md`. Human recoil feel: `../Body/Body.md`.

Potential apps under Manipulate Mana / Mana Hands / thrust. Mana from Useful joules:

`Mana = J / (10 × η(L) × μ(INT))`  
`Mana/s = P / (10 × η(L) × μ(INT))`

Raw examples below quote **J** and **J/10** as the ημ = 1 reference (L2, INT 15). Real cast cost divides by ημ.

## Equations

- KE = ½ m v²
- Relativistic KE = (γ − 1) m c²
- With path losses: E_total = ½ m v² + F_drag · d + F_friction · d (+ m g h for lifts)
- Constant force: E = F · d
- Force from accel: F = m (v / t)
- Momentum: p = m v (relativistic: p = γ m v)
- Lift + launch: E = m g h + ½ m v²
- Recoil energy of mass M: E = p² / (2M)
- Felt average force over time t: F = p / t
- Constant brake over stroke d: F = E / d

## Worked reference (ημ = 1)

| Action | J | ≈ mana at ημ 1 |
|---|---|---|
| 20 g arrow to 60 m/s | 36 | 3.6 |
| 50 kg lift 1 m | 491 | 49 |
| 50 kg to 10 m/s (KE only) | 2,500 | 250 |
| 50 kg to 20 m/s | 10,000 | 1,000 |
| 100 kg lift 1 m | 981 | 98 |
| 100 kg to 10 m/s | 5,000 | 500 |
| 100 kg to 20 m/s | 20,000 | 2,000 |

Delivered over 1 s, those mana figures are also mana/s at ημ = 1.

At INT 40 L2 (21.9 J/mana): divide J by 21.9. Example: 50 kg to 10 m/s → 2500/21.9 ≈ **114 mana** (or mana/s if over 1 s).

Static **hold** drain for a gripped mass stays on the Mana Hands table in `ManaCast.md` (proposed J/s). Airborne sustain is `Flight.md`, not the hold row.

### Apps

Lifts, throws, pulls, bellows, well buckets, portcullis and cart work (Hands energy table in `ManaCast.md`). Dash / jump bursts as short KE dumps. Combined lift+launch for vaulting a body or crate: pay m g h + ½ m v².

## Recoil (momentum out)

Momentum is conserved for the whole shooter-launcher-projectile system. Once the projectile carries momentum **p** forward, something must carry **p** backward. Parts that stay attached to the launcher only push through the frame to the shooter. Total impulse on the shooter is still exactly **p**. Internal mechanisms can only **spread** that push over time.

Flywheels store energy, not linear momentum. A counter-rotating pair (`Generators.md`) has zero net angular momentum; the shot's **p = m·v** still recoils through the axles.

Energy cannot cancel momentum. Extra flywheel burn inside the launcher becomes heat and internal motion only. Cancelling recoil means pushing mass (or light) **out**.

### Space drift

Internal motion never produces net travel (astronaut arm shake ends where it started; non-reciprocal paths can reorient but not translate). Released mass does. Drift of shooter system mass M: **v = p / M**.

| Shot | Recoil momentum | Drift for 100 kg astronaut + gear |
|---|---|---|
| 60 g at 1 km/s | 60 N·s | 0.6 m/s |
| 60 g at 3 km/s | 180 N·s | 1.8 m/s |
| 60 g at 0.01c | 180,000 N·s | 1.8 km/s |
| 60 g at 0.1c | 1,800,000 N·s | 18 km/s |

### Fire-out-of-battery

Throw the heavy carriage forward first; fire mid-travel so recoil stops the carriage. Shooter feels nothing at the shot, but feels full **p** earlier as a steady push. Failed shot slams the carriage into the forward stop.

### Countermass

Eject mass backward with momentum **p**. Energy cost **p² / (2M)** (heavier, slower mass costs less). Only perfect handheld cancel. In space, mass is consumed every shot.

| Countermass (for 60 N·s) | Exit speed | Extra energy |
|---|---|---|
| 60 g | 1,000 m/s | 30 kJ |
| 0.6 kg | 100 m/s | 3 kJ |
| 6 kg | 10 m/s | 300 J |
| 60 kg | 1 m/s | 30 J |

**Light as countermass:** momentum E/c, needs **E = p·c**. For 60 g at 1 km/s: 18 GJ (~4.3 t TNT) of light vs 30 kJ arrow. Far more costly than the shot.

### Countermass vs anchored pulley

| | Countermass | Anchored pulley |
|---|---|---|
| Cancels recoil | Fully, anywhere | Fully, by passing it to the anchor |
| Works in space | Yes | Only if tethered |
| Handheld / mobile | Yes | No |
| Consumables | Mass each shot | None |
| Hazard | Backblast | Anchor / rope failure |
| Stealth | Ejected mass | Silent apart from the shot |

A shooter-carried pulley is internal and cancels nothing. Block-and-tackle with a damper stretches recoil into a long pull on the anchor. Relativistic shots prefer bedrock / hull spine anchors over huge countermass.

### Sliding flywheels as recoil mass

Match **momentum**, not energy. Example: 60 g × 1,000 m/s = 60 N·s; 20 kg wheels at 3 m/s = 60 N·s. Matching the arrow's 30 kJ into 20 kg would be 55 m/s and 1,100 N·s (18× too much). Cancellation lasts only while the wheels keep moving; stopping them dumps **p** into the frame unless they coast on a long track, detach as countermass, or brace into ground/wall.

### Gyros do not eat linear recoil

Linear and angular momentum are conserved separately. Spin resists twist and muzzle climb; it does not reduce the straight backward push. Exotic: stored energy adds inertia (E = mc²); +1 kg of inertia needs ~21 megatons of stored energy.

### Recoil buffers

Goal: constant force over the longest stroke. For 20 kg at 3 m/s (90 J): 300 N over 30 cm, 150 N over 60 cm, ~18,000 N spike if stopped in 5 mm.

Water slammed across a vacuum (water hammer) spikes. The same water through a small orifice damps smoothly.

Stack that works: regenerative rack into the wheels → eddy-current brake (copper/aluminum past magnets) → tapered hydraulic orifice → gas spring for catch and reset. Shear-thickening fluid as final safety stop.
