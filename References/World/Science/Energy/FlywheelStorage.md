# Indestructible Flywheel Storage (Rim-Weighted)

Hub: `../Science.md`. Pair handling / generator bottleneck: `Generators.md`. Laser / light / load runtimes: `FlywheelApplications.md`. Pinch launch: `Projectiles.md`. Recoil: `Kinetic.md`. Indestructible stock: `../../Materials/Metals.md` (adamantium: **no stretch, no bend**). Perfect-conductor / perfect-insulator speed ceiling and mana-per-kg table: `ElectricMotors.md`. Stocks: `../../Materials/MaterialConsiderations.md`.

Fiction baseline: perfect counter-rotating pair, zero-friction bearings, hard vacuum, superconducting cryogenic motor/generator (silver/gold conductors), magnetic levitation in normal operation.

## Wheel design

- Thin flat disk = locating web only.
- Outer **ring band** perpendicular to the disk (short drum). Axial cross-section looks like a T on its side.
- **98%** of mass in the ring. Ring radial thickness = **2%** of wheel radius.
- Very thin backup axle through the center with clearance; touches bearings only if levitation fails.

```
E ≈ 0.485 × m × v²     // classical; m = mass, v = rim speed
```

About **97%** of a thin-ring ideal (½ m v²) and **1.94×** a flat coin (¼ m v²) of equal mass.

| Wheel | Mass | Diameter |
|---|---|---|
| Small | 20 g | 24.26 mm (quarter diameter) |
| Big | 20 kg | 304.8 mm (1 foot) |

## Single wheel (classical tables)

| Rim speed | Small (20 g) | Big (20 kg) |
|---|---|---|
| 1,000 m/s | ~9.7 kJ | ~9.7 MJ |
| 1% of c | ~87 GJ (~21 tons TNT) | ~87 TJ (~21 kilotons) |
| 10% of c (0.1c) | ~8.7 TJ (~2.1 kilotons) | ~8.7 PJ (~2.1 megatons) |

| Rim speed | Small RPM | Big RPM |
|---|---|---|
| 1,000 m/s | ~787,000 | ~62,700 |
| 1% of c | ~2.4 billion | ~188 million |
| 0.1c | ~24 billion | ~1.9 billion |

## Pair at 0.1c

| Quantity | Small pair (40 g) | Big pair (40 kg) |
|---|---|---|
| Stored energy | ~17.5 TJ | ~17.5 PJ |
| TNT equivalent | ~4.2 kilotons | ~4.2 megatons |
| Mass gain per wheel (E/c²) | ~97 mg | ~97 g |
| Angular momentum per wheel | ~7,000 kg·m²/s | ~8.9 × 10⁷ kg·m²/s |

Big pair = **1,000×** small pair at the same rim speed.

**Relativity at 0.1c:** Lorentz factor γ ≈ 1.005. Rim contraction ~0.5%. Stored energy ~0.75% above the classical formula.

### Bonfires to fill at 0.1c (full capture, dry wood ~16 MJ/kg)

| Fire | Small pair | Big pair |
|---|---|---|
| Campfire (160 MJ) | ~109,000 | ~109 million |
| Backyard bonfire (3.2 GJ) | ~5,500 | ~5.5 million |
| Festival bonfire (320 GJ) | ~55 | ~55,000 |

| Rim speed from one fire (pair, from rest) | Small | Big |
|---|---|---|
| Campfire | ~91 km/s | ~2.9 km/s |
| Backyard | ~406 km/s | ~13 km/s |
| Festival | ~4,060 km/s | ~128 km/s |

## Shape comparison at 0.1c

| Version | Mass | Energy | TNT |
|---|---|---|---|
| Quarter coin | 5.67 g | ~1.28 TJ | ~300 tons |
| Rim-weighted | 5.67 g | ~2.48 TJ | ~590 tons |
| **Rim-weighted** | **20 g** | **~8.7 TJ** | **~2,100 tons** |
| Coin shape | 11.2 kg | ~2.53 PJ | ~600 kt |
| Rim-weighted | 11.2 kg | ~4.91 PJ | ~1.2 Mt |
| **Rim-weighted** | **20 kg** | **~8.7 PJ** | **~2.1 Mt** |

## Design notes

- **Ring width:** stable while axial width ≲ 2.45 × radius. Width = radius is a comfortable margin.
- **Web:** as thin as desired; no torque, no meaningful load.
- **Motor / levitation:** ring inner face = smooth cylinder. Stationary superconducting coils inside the ring couple to the heavy band; same coils can levitate.
- **Pair layout:** coaxial counter-rotating; webs outward; rings share a central stator.
- **Backup axle:** thinner is better (surface speed ∝ radius). At 0.1c, 1 mm axle ≈ 197 km/s surface; 0.1 mm ≈ 20 km/s. Levitation failure with a turning housing also dumps gyroscopic load on the axle; axle and mounts must be indestructible.
- **Vacuum:** residual gas hit near 0.1c gains ~130 MeV → nuclear reactions. Need deep-space-class vacuum, not lab vacuum.

## Rim-weighted at 0.9c (relativistic)

| Quantity | Small 0.1c | Small 0.9c | Big 0.1c | Big 0.9c |
|---|---|---|---|---|
| Energy per wheel | ~8.7 TJ | ~2.1 PJ | ~8.7 PJ | ~2.1 EJ |
| TNT per wheel | ~2.1 kt | ~510 kt | ~2.1 Mt | ~510 Mt |
| Pair total | ~17.5 TJ | ~4.3 PJ (~1 Mt) | ~17.5 PJ | ~4.3 EJ (~1 Gt) |
| RPM | ~24B | ~212B | ~1.9B | ~17B |
| γ | 1.005 | 2.29 | 1.005 | 2.29 |
| Mass gain / wheel | ~97 mg | ~24 g | ~97 g | ~24 kg |

0.1c → 0.9c multiplies energy ~**245×** (classical v² would say 81×). At 0.9c each wheel holds ~1.19× its rest mass energy.

### Conditions at 0.9c

- **Relativistic stretch:** in the rim's frame the circumference wants ~γ× rest length. **Conflicts with adamantium "no stretch"** unless the story allows a Born-rigidity fiction exception or caps below stretch-critical speeds. See Open.
- **Effective mass:** ~2.2× rest (44 g small, 44 kg big).
- **Angular momentum / wheel:** ~1.5×10⁵ kg·m²/s small; ~1.9×10⁹ big.
- **Vacuum:** residual hits ~34 GeV (accelerator-class).
- **Electrical output frequency:** ~3.5 GHz per pole pair (small); ~280 MHz (big).
- **Neutral charge:** net charge on a 0.9c rim radiates energy away.

Bonfires to fill pair at 0.9c: campfire ~27M / 27B; backyard ~1.3M / 1.3B; festival ~13k / 13M (small / big).

## Energy per kilogram

| Storage | Energy per kg |
|---|---|
| Lift to escape height (Earth g) | ~62.5 MJ |
| Best steel springs | ~0.3 kJ |
| CNT springs (theory) | a few MJ |
| Best real CF flywheels | ~0.2–0.4 MJ |
| Gasoline (chem) | ~46 MJ |
| Indestructible rim @ 1,000 m/s | ~0.49 MJ |
| Uranium fission (ref) | ~80 TJ |
| DT fusion (ref) | ~340 TJ |
| **Rim flywheel @ 0.1c** | **~437 TJ** |
| Antimatter annihilation (ref) | ~90,000 TJ |
| **Rim flywheel @ 0.9c** | **~107,000 TJ** |

Past ~0.87c, KE per kg exceeds rest mass energy. Springs/gas hit a sound-speed ceiling; flywheels only hit *c*.

## Fixed space vs fixed mass

Thin ring wins **per kilogram**. In a **fixed enclosure**, a solid drum wins (more mass).

| Design (same space, same rim speed) | Relative energy |
|---|---|
| Ring, 2% radial thickness | 1× |
| Ring, 10% | 4.5× |
| Ring, 25% | 8.9× |
| Ring, 50% | 12.2× |
| **Solid drum** | **13×** |

Solid drum classical: **E = ¼ m v²**. At 0.9c about **0.393 m c²** (relativistic disk integral).

## 5,000 kg solid drum pair

- Enclosure **1 m × 1 m × 2 m** (2 m³); spin axis along 2 m.
- Two solid drums, **5,000 kg** each, **0.8 m** diameter, counter-rotating, shared stator in the gap, one vacuum chamber.

| Density | Drum width |
|---|---|
| Osmium (22.6 g/cm³) | ~0.44 m |
| Tungsten / gold (19.3) | ~0.52 m |

Need density ≳ 15.3 g/cm³ to stay under ~0.69 m stability width (≲ 0.87× diameter).

| Rim speed | RPM | Per wheel | Pair | Pair TNT |
|---|---|---|---|---|
| 1,000 m/s | ~23,900 | ~1.25 GJ | ~2.5 GJ | ~600 kg |
| 1% of c | ~72M | ~11 PJ | ~22.5 PJ | ~5.4 Mt |
| 0.1c | ~716M | ~1.13 EJ | ~2.25 EJ | ~540 Mt |
| 0.9c | ~6.4B | ~177 EJ | ~353 EJ | ~84 Gt |

Mass gain / wheel: ~12.5 kg at 0.1c; ~1,965 kg at 0.9c (pair effective ~13.9 t). Floor load ~5 t/m² at rest → ~7 t/m² at 0.9c on 2 m².

One fire from rest (pair): campfire ~253 m/s; backyard ~1.1 km/s; festival ~11.3 km/s rim.

## Perfect windings (design loot)

Not a second wheel geometry. Speed caps and the mana-per-kg table: `ElectricMotors.md`.

- **Build:** Indestructible rotor plus perfect windings.
- **Purpose:** Energy storage.
- **Motor and generator in one:** A perfect motor is also a perfect generator, since the same machine runs both ways. Spin it up to store energy, draw it down to release it, with almost nothing lost in either direction.

## Open

- **Adamantium vs 0.9c stretch:** live metal lock is no stretch / no bend. Either forbid 0.9c rim fiction, allow a relativity-only geometry exception, or use a different indestructible that may stretch.
- Generator drain still bottlenecked (`Generators.md`); these tables are **storage**, not dump rate.
- Silver/gold cryogenic windings vs Stillwire / mythril path: electrical here, not mana conductivity.
