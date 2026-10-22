# Generators

Hub: `../Science.md`. Chemical cells: `Batteries.md`. Stillwire / mythril windings: `RefinedMana.md`, `../../../Runes/ManaMaterials.md`. **Electrical** conductivity here is Earth physics. **Mana** conductivity is narrative and does not follow this ranking (`../../../Runes/Energy.md`; orihalcum is the prime example).

## Electric Generator: What Makes It Efficient

A generator works by Faraday's law. Moving a magnetic field past a coil of wire, or a coil through a field, pushes electrons along the wire. Voltage depends on field strength, number of turns and how fast the field changes.

Best large generators reach 98 to 99% efficiency. The factors behind that:

- **Strong magnets:** neodymium (NdFeB) permanent magnets give the strongest field for their size. Large power plants use electromagnets instead so the field can be controlled.
- **Low-resistance windings:** thick, high-purity wire wastes less energy as heat. Resistance loss rises with current squared, so heavier wire pays off at high output.
- **Laminated iron cores:** the iron that guides the magnetic field is made of thin insulated sheets instead of a solid block. Solid iron lets swirling eddy currents form and waste energy as heat.
- **Low-loss core steel:** silicon steel loses less energy each time the field flips direction.
- **Small air gap:** the gap between the spinning and stationary parts should be as narrow as possible. Air carries magnetic field poorly.
- **Low friction:** good bearings and balanced rotors cut mechanical loss. Very large units use hydrogen cooling gas because it creates less drag than air.
- **Cooling:** hotter wire has higher resistance, so cooling directly improves efficiency.
- **Correct speed and load:** every generator has a speed and load range where it runs best. Running far outside it drops efficiency.
- **Multiple phases:** three-phase designs deliver smoother power with less waste than single-phase.

## Winding Material: Copper vs Silver

| Property | Copper | Silver |
|---|---|---|
| Conductivity | Baseline (100% IACS) | About 5 to 6% higher (about 105% IACS) |
| Cost | Low | Roughly 100 times copper by weight |
| Density | 8.96 g/cm³ | 10.49 g/cm³ (about 17% heavier) |
| Strength | Good for winding | Softer, easier to damage |
| Corrosion | Oxidizes | Tarnishes with sulfur compounds |

- **Copper wins for nearly every generator.** Silver's small conductivity gain is far outweighed by cost. A slightly thicker copper wire matches silver's resistance for a fraction of the price.
- **Silver is used where tiny gains matter more than cost:** electrical contacts, switch points, plating on high-frequency connectors and some specialty aerospace or laboratory equipment.
- **Aluminum** conducts worse than copper but is far lighter. It wins when weight per unit of conductivity matters, such as long power lines.
- **Superconductors** have zero resistance when cooled far below freezing. They are used in some experimental and very large machines where the cooling cost is worth it.

## Best Conductor Regardless of Price

Ignoring price, silver is the best choice among ordinary metals. Gold is a worse conductor than copper.

**Room-temperature conductivity ranking (copper = 100%)**
- Silver: about 105 to 106%
- Copper: 100%
- Gold: about 70 to 73%
- Aluminum: about 61%

**Why gold is still used in electronics**
Gold does not oxidize or tarnish. A thin gold plating keeps connector and contact surfaces clean and reliable for decades. It is never chosen for carrying current through windings or wire.

**Best combination with no cost limit**
- Silver windings for the lowest resistance.
- Thin gold plating only on exposed contacts and terminals, where it protects against corrosion.

**Beyond silver**
- **Superconductors:** zero resistance below a critical temperature. Niobium-titanium needs liquid helium cooling. High-temperature superconductors such as REBCO tape work with liquid nitrogen. These outperform any metal by an enormous margin.
- **Ultra-pure cryogenic metals:** very pure copper or aluminum cooled to extremely low temperatures becomes hundreds of times more conductive than at room temperature, though still not zero.
- **Carbon nanotube wire:** individual nanotubes beat copper, but bulk wire made from them does not yet match copper's conductivity.

Indestructible rims / axles / housings: **adamantium** (`../../Materials/Metals.md`; no stretch, no bend). Rim-weighted sizes, 0.1c/0.9c tables, solid-drum pack: `FlywheelStorage.md`. Magic lossless crystal dump (unlimited rate): `FlywheelApplications.md` (bypasses the mundane bottleneck below). Pinch launch from flywheels: `Projectiles.md`. Recoil when that energy leaves as a shot: `Kinetic.md`.

## Paired Flywheels

Paired flywheels interact with each other and with the shared frame. Behavior depends on whether they spin the same way or opposite ways.

### Counter-rotating pair (equal speed, opposite spin)

- Net angular momentum is zero, so the assembly has no overall gyroscopic resistance. The host frame can turn, tilt or yaw freely without precession.
- Spin-up and spin-down reaction torques cancel. Each motor pushes the frame in an opposite direction, so the housing does not twist when power is added or drawn.
- Stored energy adds (kinetic energy is scalar). Two wheels store double the energy with none of the handling penalty.
- Cancellation is through the structure. When the frame rotates, each wheel still produces its own gyroscopic moment on its bearings. The two moments are equal and opposite, so the frame between the wheels carries a bending or twisting load. Mount stiffness and bearing rating must account for this.
- A speed mismatch leaves residual net momentum and can cause beat-frequency vibration. Geared coupling or synchronized motor control prevents this.

Default for handheld devices, vehicles and generators that must be aimed or turned freely.

### Co-rotating pair (same direction)

- Angular momentum adds, doubling gyroscopic stiffness. Suits stabilization (ship roll, spacecraft attitude hold).
- Reaction torques also add, so the frame feels twice the torque during speed changes.

### Gimbaled pairs (control moment gyros)

In a scissored pair, both wheels tilt by equal and opposite gimbal angles. Output torques combine along one axis and cancel on the cross axis. Clean single-axis torque for steering or balancing.

### Common coupling layouts

- **Coaxial contra-rotating:** one shaft inside another. Compact with minimal frame bending.
- **Side-by-side geared:** gear mesh forces equal and opposite speeds.
- **Independent motors:** flexible but needs control electronics to stay matched.

## Egg-Sized Cryogenic Generator with Relativistic Flywheels

Setup: an egg-sized generator with ultra-pure cryogenically cooled copper windings, driven by a counter-rotating pair of indestructible flywheels about one foot (30.5 cm) in diameter. Sized storage tables (20 g / 20 kg rim-weighted, 5 t drums): `FlywheelStorage.md`.

### Energy stored (per kg of thin rim)

Kinetic energy at relativistic speed is (γ − 1)mc² for mass at the rim. A solid disk stores less. Best real flywheels ~1,000 m/s rim (~0.0003% of c).

| Rim speed | RPM (1 ft diameter) | Energy per kg of rim | TNT equivalent per kg |
|---|---|---|---|
| 0.01c | about 188 million | 4.5 × 10¹² J | about 1 kiloton |
| 0.1c | about 1.9 billion | 4.5 × 10¹⁴ J | about 108 kilotons |
| 0.5c | about 9.4 billion | 1.4 × 10¹⁶ J | about 3.3 megatons |
| 0.9c | about 17 billion | 1.2 × 10¹⁷ J | about 28 megatons |

### The generator is the bottleneck

An egg-sized generator cannot drain energy anywhere near as fast as the flywheels can store it.

- **Power limit:** an egg-sized high-speed generator realistically produces a few kilowatts. Cryogenic copper cuts resistive loss sharply but does not raise the magnetic limit of the core (iron saturates around 2 tesla). A generous estimate is tens of kilowatts.
- **Drain time:** 1 kg of rim at 0.5c feeding a 10 kW generator lasts about 44,000 years.
- **Practical result:** the system acts as a near-endless power cell with a small output.

### Engineering problems even with indestructible flywheels

- **Speed matching:** the generator rotor cannot spin at billions of RPM unless it is also indestructible. A coupling between them needs enormous speed reduction, such as magnetic or electrostatic coupling instead of gears.
- **Vacuum required:** any air touching a rim at relativistic speed hits it hard enough to cause nuclear reactions and radiation. The housing needs a hard vacuum.
- **Bearings:** contact bearings fail instantly. Magnetic levitation is the only workable option.
- **Counter-rotation:** a pair spinning in opposite directions cancels the gyroscopic effect, so the device can be moved and turned freely. A single flywheel would resist any change in orientation with tremendous force.
- **Containment:** the housing and mounts must also be indestructible. Any failure releases the full stored energy at once.
- **Spin-up:** the same energy has to be put in to begin with, which requires power on a large industrial scale.
- **Physics note:** relativity forbids a perfectly rigid disk from spinning near light speed (the Ehrenfest paradox). Indestructible material bypasses this in fiction but not in real physics.

### Cryogenic cooling note

Ultra-pure copper at liquid helium temperatures can be several hundred times more conductive than at room temperature. Keeping an egg-sized unit that cold requires a cryocooler or insulated reservoir, which adds bulk well beyond the egg itself.

## Capacitor banks for pulsed lasers

Dynamos or generators feed Leyden-jar style capacitor banks, then dump into flash tubes (ruby) or high-voltage discharge tubes (copper vapor, CO2). Most laser input becomes waste heat at the tube, so cooling still dominates the installation size. Optics and gas feedstock: `Optics.md`. Fight use: `../../../Combat/Lasers.md`.

## Superconducting windings

Mythril metal law stays in `../../../Materials/Metals.md`. This section is the machine use.

A superconducting winding is a coil of wire made from superconducting material. Like a copper winding, it carries current to create a magnetic field. The difference is that current flows with zero resistance (mythril / aether-mythril path mode).

**What zero resistance does**
- **No heat:** copper windings lose energy as heat (I²R loss). A superconducting winding loses nothing on steady DC however much current it carries.
- **Persistent current:** with the coil's ends joined in a closed loop, current circulates forever with no power supply. SMES coils and MRI magnets work this way. Etherium is the dedicated persistent-store metal; mythril windings can hold a persistent electrical current in the coil loop.
- **Much higher current density:** copper carries about 2 to 10 A/mm² before overheating. Current Earth superconductors carry 100 to 1,000+ A/mm². Gear-grade mythril still has a **Jc** ceiling; aether mythril aims higher.
- **Stronger fields:** more current in less space creates far stronger magnetic fields from a compact coil.

**Earth limits vs Caldris mythril**
- **Critical temperature:** Earth superconductors need cooling to between -269 °C and about -200 °C. Room-temperature mythril removes the cooling plant.
- **Critical field and critical current:** above a certain field or current, superconductivity collapses (a quench). Stored energy then turns into heat at once and can destroy the coil. Mythril **keeps Jc / quench** (rare on gear stock). Do not write it as perfect unlimited current.
- **Magnetic pressure:** strong fields push the windings outward. Adamantium or high-strength frames contain this; orihalcum is mana-resistant cladding / anvil damp, not the winding itself.
- **AC losses:** Earth superconductors lose a little when current changes quickly. Mythril pulses pay a little AC-loss feel. Steady DC is near lossless.

**Role in a flywheel / motor stack**
- **Motor/generator:** superconducting windings on the stator create a strong field. The rotor's magnets (or its own superconducting windings) turn through it. Charging speeds the rotor up and discharging slows it down. Ceiling layout, air-core axial discs in an adamantium cage: `ElectricMotors.md`.
- **Magnetic bearings:** superconductors push out magnetic fields (Meissner) and can lock magnets in place (flux pinning). This holds the rotor centered with no contact. Orihalcum plates are **mana-resistant** cladding (MR block), not superconducting bearings. Do not confuse shield stock with winding current.
- **Efficiency:** with no winding I²R loss, conversion between motion and electricity sits above 99% on the electrical side. Remaining losses are bearings, windage, and power electronics / rune converters.

Companions: `Batteries.md` (stone vs cell power), `RefinedMana.md` (Stillwire stone-refined wire; Lightthread), stone sockets as the mana feed.

