# Acoustic Levitation

> **Design loot / Earth physics.** Holding things in the air with sound. Standing-wave traps, steerable tweezers and near-field floating plates. Not automatic law.
>
> Base equations, Q and the Levitation Lattice note: `Sound.md`. Ultrasonic sources and safety: `Ultrasonics.md`. Mana Hands hold drain: `ManaHandPhysics.md`. Gem seats: `../Metallurgy/GemInlay.md`. Glass science: `../../Materials/GlassScience.md`. Cast law: `../../../Runes/Energy.md`, `ManaCast.md`.

## Shared cost law

- **1 MP = 10 J.** Raw MP below is J ÷ 10. Real casters divide by their conversion (`ManaHandPhysics.md` §2).
- **A standing wave stores energy.** A tuned field only pays its losses each second (`Sound.md` Q rule). Breaking the field and stopping its air pays the rest (`ManaHandPhysics.md` §10).

## Three kinds

| Kind | How | Holds | Gap |
|---|---|---|---|
| **Standing-wave trap** | Emitter and reflector (or two emitter banks) set up still nodes | Small objects in the quiet nodes | Nodes λ/2 apart |
| **Acoustic tweezers** | Phased array shapes the field and moves the trap | Small objects moved in 3D | Free path |
| **Near-field float** | A flat face vibrates under a flat object | Plates, wafers, shafts | Tens to hundreds of µm |

## Size limit

Objects must fit inside a node. Practical limit is under about λ/2.

| Frequency | λ/2 in air | Largest object |
|---|---|---|
| 20 kHz | 8.6 mm | under 1 cm |
| 40 kHz | 4.3 mm | about 4 mm |
| 100 kHz | 1.7 mm | under 2 mm |

## Loudness needed by density

Simple model: the field's energy density times the wavenumber must beat the object's weight per volume. Real traps need some margin above these numbers.

| Material | Density | At 20 kHz | At 40 kHz |
|---|---|---|---|
| Polystyrene foam | 0.02 g/cm³ | 143 dB | 140 dB |
| Cork, light seed | 0.25 g/cm³ | 154 dB | 151 dB |
| Water drop | 1.0 g/cm³ | 160 dB | 157 dB |
| Glass | 2.5 g/cm³ | 164 dB | 161 dB |
| Steel | 7.9 g/cm³ | 169 dB | 166 dB |
| Gold | 19.3 g/cm³ | 173 dB | 170 dB |

- A cheap 40 kHz array (TinyLev, 2017) draws about 10 W and traps water drops and objects up to about 4 mm.
- High-power lab rigs have held small spheres of very dense metals.
- Ultrasound at these levels is inaudible but still strong. Keep heads out of the field (`Ultrasonics.md`).

### Why not a person

A person is about 1.7 m and as dense as water. A node that size needs about 100 Hz. Holding water up at 100 Hz takes about 183 dB of audible sound. That deafens and injures everyone in the room long before anything floats. Person-scale acoustic levitation is not practical. Use Mana Hands or Flight (`Flight.md`).

## Cost of a field

```
Stored energy    E_stored = energy density × field volume
Drive power      P ≈ 2π × f × E_stored ÷ Q
```

Example: water drops at 40 kHz need about 13 J/m³. A 50 cm³ field stores about 0.7 mJ. At Q about 50 the drive is about 3.4 W. That is about **0.3 MP/s raw**.

### Versus Mana Hands

Mana Hands hold drain is about 1 J/s per kg (`ManaHandPhysics.md`). A 10 mg drop costs Hands about 0.00001 W. Hands are far cheaper for one object.

Acoustic levitation wins when:

- **Many objects** sit in one field (one trap holds dozens of nodes at once) without spending Multitasking slots.
- **No contact** is allowed: molten beads, wet drops, dust, reagents that a Hand grip would smear or contaminate.
- **A rune device** runs it on a stone without the caster's attention.
- **Heat** would burn a Hand's focus: hot glass and metal beads.

## Near-field floating

A flat face vibrating at ultrasonic pitch squeezes a thin air film under a flat object. The object floats with no contact.

| Example | Load | Gap |
|---|---|---|
| Light plate | about 68 g | about 50 to 210 µm |
| Spindle bearing, 50 mm shaft | about 51 N (about 5 kg) | tens of µm |
| Double-acting lab transducer | up to about 343 N (about 35 kg) | about 25 µm total |

Load grows with face size and vibration swing. Gap shrinks as load grows. Needs smooth flat faces. Needs air.

- **Frictionless bearings.** Shafts, turntables, potter's wheels and flywheels with no wear (`FlywheelStorage.md`, `FrictionNotes.md`).
- **Glass and plate conveyor.** Move window glass or polished stone without scratches.
- **Gem and lens handling.** Float a polished face without touch.

## Side effects

- **Streaming.** Strong fields push steady air currents that can knock objects out of nodes.
- **Heating.** Losses warm the air and the object.
- **Drops deform.** Water drops flatten and burst into mist near the limit (`Ultrasonics.md` mist).
- **Audible leaks.** Moving or pulsing the trap can make clicks and whines.
- **Animals.** Insects and very small animals have been levitated in labs. Bats and dogs hear the field.

## Uses

- **Containerless chemistry.** Hold drops of reagent in air and mix them. No container touches or taints them.
- **Clean glass and gem melts.** A melt held without a crucible avoids the contact points that start crystals. Supercooled glass and pure beads (`../../Materials/GlassScience.md`).
- **Small-part assembly.** Watch parts, rune micro-pieces, gem chips and wire held in position for fitting.
- **Gem setting.** Hold a stone over its seat with no tweezers (`../Metallurgy/GemInlay.md`).
- **Drying drops to powder.** Hold a drop until it dries into a clean particle.
- **Density sorting.** Light particles hold at lower power. Turn the field down and heavy ones fall out first.
- **Floating display.** A tiny bead traced fast through the air and lit by light draws a picture in midair.
- **Cell and fluid sorting.** Acoustic traps in liquid sort cells and particles for medicine.

## Potential

- **Bead Lattice.** A field of dozens of nodes holding reagent drops or gem chips. About 0.3 MP/s raw per small trap.
- **Hot Hold.** Melt and cool glass, metal or alloy beads without a crucible.
- **Float Bearing.** Contact-free bearing face for Roland's wheels and shafts.
- **Glass Glide.** Slide plates and panes with no scratch.

## Open

- Whether a rune can hold a tuned field on a stone long-term and what its loss rate is.
- How Mana Hands and an acoustic trap share a workbench (Hands for force, trap for many small holds).
