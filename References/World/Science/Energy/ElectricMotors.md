# Electric Motors

Hub: `Engines.md`. The same machines run as generators: `Generators.md` (Faraday law, laminations, copper vs silver, mythril windings, bearings). Cells: `Batteries.md`. Prime movers that can spin a dynamo: `SteamEngines.md`, `StirlingEngines.md`.

A motor puts current through a magnetic field so the wire is pushed. A generator pushes wire through a field so current is driven. Wound correctly, one carcass can do either job. Gramme's dynamo (1871) made that obvious, and it is why motors became common only after generators did: the power had to come from somewhere.

Caldris exosuits that move by rune tension are a different mechanism. Do not describe those as these motors.

## Caldris filter

| Band | What exists |
|---|---|
| Baseline | No public motor trade. Mana stones, steam, water, and muscle already turn shafts. Electricity is an invent chain (heat engine or water wheel, then dynamo, then motor). |
| Near-reach | Brushed DC with iron field coils, a commutator, and carbon or copper brushes. Permanent magnets of steel or lodestone for a weak demonstration. Series, shunt, and compound windings. A solenoid. |
| Needs an AC supply | Induction motors and synchronous motors. The supply can be a spinning alternator geared to a steam shaft. No electronics required for a fixed-speed three-phase mill motor. |
| Needs fast switching | Brushless DC, variable-frequency drives, switched-reluctance drives, stepper drivers. Rune timing can stand in for the switches. Semiconductor inverters cannot be assumed. |
| Prestige | Rare-earth permanent magnets, superconducting stator windings (mythril path in `Generators.md`), piezo and electrostatic motors, homopolar ship drives. |

## The push

A current-carrying wire in a magnetic field feels a force at right angles to both the current and the field. Coil that wire and the forces add up as torque.

- Torque grows with current and with field strength.
- Spinning the same coil in the field produces a back voltage that rises with speed. At no-load speed, back voltage nearly equals supply voltage and current falls to whatever friction requires.
- Shaft power is torque times rotational speed.
- Reverse the current or the field, not both, and the shaft reverses.

Losses, in every family:

- **Copper:** current squared times winding resistance. Thick wire and high voltage (less current for the same power) cut this.
- **Iron:** the core is remagnetized every time the field changes. Hysteresis and eddy currents heat a solid chunk of iron. Thin varnished sheets (laminations) are the cure. Details in `Generators.md`. A DC field pole can be solid. An armature or any AC core should be laminated.
- **Mechanical:** bearings, brushes, and windage.
- **Stray:** leakage flux, skin effect at high frequency, magnet heating.

Efficiency bands that are fair to quote:

| Machine | Typical efficiency |
|---|---|
| Shaded-pole fan motor | About 20 to 30% |
| Small brushed toy motor | About 40 to 70% |
| Universal (tool) motor | About 60 to 75% |
| Good brushed DC, human-scale | About 75 to 85% |
| Industrial induction, small | Around 85% at 1 hp, higher as the frame grows |
| Industrial induction or PM synchronous, large | About 95%, and past 97% in big slow machines |
| Synchronous machine the size of a plant generator | About 98 to 99%, same band as large generators |

## Family list

| Type | Supply | Sliding contacts | Rotor | Trait |
|---|---|---|---|---|
| Homopolar (Faraday disc) | DC | Brushes at rim and shaft | Conducting disc in an axial field | True DC. One "turn." Enormous current, tiny voltage. |
| Brushed permanent-magnet DC | DC | Commutator | Wound armature | Simple speed control by voltage. Magnet sets the field. |
| Series DC | DC | Commutator | Wound | Field in series with the armature. Huge start torque. Runs away if unloaded. |
| Shunt DC | DC | Commutator | Wound | Field across the supply. Nearly constant speed. |
| Cumulative compound DC | DC | Commutator | Wound | Shunt plus a series winding that aids it. Start torque and stable speed. The useful compound. |
| Differential compound DC | DC | Commutator | Wound | Series opposes shunt. Can unload and surge. Avoid. |
| Universal | DC or AC | Commutator | Wound, series | Field and armature reverse together on AC, so torque keeps its direction. Very high speed. |
| Coreless DC | DC | Commutator, or none if brushless | Winding with no iron, often a cup or a disc | Low inertia, no cogging. Fragile coil. |
| Brushless DC | DC via an inverter | None | Permanent-magnet rotor | Electronic commutator. Trapezoidal drive. |
| Squirrel-cage induction | AC, usually 3-phase | None | Conducting bars shorted at the ends | The default industrial motor. No brushes, no magnets. |
| Wound-rotor induction | AC | Slip rings | Wound rotor with external resistors | High start torque by adding resistance, then cutting it out. |
| Single-phase induction | AC, 1-phase | None, plus a start device | Cage | Will not start alone. Split-phase, capacitor, or shaded pole provides the second phase. |
| Shaded-pole induction | AC, 1-phase | None | Cage | A copper band on part of each pole delays that flux. Weak start, cheap, fans. |
| Repulsion | AC | Commutator, brushes not fed from the line | Wound | Currents induced in the rotor are repelled by the stator. High start torque. Historical. |
| Wound-field synchronous | AC | Slip rings for the DC field | Electromagnet locked to the spinning field | Fixed speed. Can make or absorb reactive power. |
| Permanent-magnet synchronous | AC | None | Magnet rotor | Best efficiency of the common motors. Fixed speed on fixed frequency. |
| Interior permanent magnet | AC via inverter | None | Magnets buried in a steel rotor | Magnet torque plus reluctance torque. The usual modern traction motor. |
| Surface permanent magnet | AC via inverter | None | Magnets glued to the rotor surface | Smoother field, weaker field-weakening, easier to throw a magnet at high speed. |
| Synchronous reluctance | AC | None | Shaped steel, no magnets and no windings | Torque from the rotor preferring the easy magnetic path. Modern ones reach high efficiency. |
| PM-assisted reluctance | AC via inverter | None | Mostly steel, few magnets | Reluctance torque with a small magnet assist. |
| Hysteresis | AC | None | Hard magnetic cylinder, no winding | Starts as an induction motor, locks in as synchronous. Smooth, low efficiency. Clocks and gyros. |
| Switched reluctance | DC pulses | None | Toothed steel only | Stator coils switched in sequence. Robust and hot-running. Noisy, rippled torque. |
| Variable reluctance stepper | DC pulses | None | Toothed steel | Many teeth, small angle per pulse. Open-loop position. |
| Permanent-magnet stepper | DC pulses | None | Magnet | Coarser step, more torque per size than a plain reluctance stepper. |
| Hybrid stepper | DC pulses | None | Magnet plus teeth | The common printer and machine-tool step motor. 200 steps per turn is typical. |
| Linear induction | AC | None | A plate or a rail (often the "rotor" is the track) | Unrolled cage motor. Launchers, some maglev. |
| Linear synchronous | AC | None | Magnets or a wound rail | Unrolled synchronous motor. Position follows the traveling field. |
| Voice coil | DC or audio AC | None | A short coil in a magnet gap | Force proportional to current over a short stroke. Speakers, fast small actuators. |
| Solenoid | DC, or AC with shading | None | A sliding iron plunger | On/off pull over a short distance. Not a rotary motor. |
| Torque motor (direct drive) | Usually inverter AC or brushless DC | None | Many poles, large diameter | High torque at low or zero speed. The load is bolted to the rotor. |
| Piezo / ultrasonic | High-frequency AC | None | A friction ring driven by vibrating ceramic | No magnetics. Low speed, high torque, holds position unpowered. Wear at the friction face. |
| Electrostatic | High voltage | None | Light electrodes | Force from charge, not current. Useful at insect size. Useless as a mill motor at ordinary voltages. |
| Superconducting | DC field plus an armature | Depends on type | Conventional or superconducting | Mythril stator windings for field. Same limits as `Generators.md`: critical current, quench, magnetic pressure. |

Synchros and selsyns are small wound machines that copy an angle to another shaft. They are instruments, not power motors.

## DC brushed machines

The commutator is a ring of copper bars, insulated, that the brushes rub. As the armature turns, the bars reverse the coil connections at the moment the coil's torque would reverse. From the outside the torque stays in one direction. From the coil's point of view the current flips every half turn.

That mechanical switch is the entire reason a DC motor can run from a battery with two wires and no other parts. It is also the part that sparks, wears, and limits speed and voltage.

- **Series:** current that makes torque also makes the field, so a stalled armature (huge current) makes a huge field and huge torque. Streetcars, cranes, and early traction used this. With no load the field collapses as current falls, back voltage stays small, and speed runs away until the armature bursts. Never belt a series motor to a load that can fall off.
- **Shunt:** field is a fine wire across the supply, current almost independent of the armature. Speed sags only a little from no-load to full load. Lathes and line shafts like this.
- **Cumulative compound:** mostly shunt, with a few series turns for harder starting. The mill-safe compromise.
- **Permanent magnet:** no field winding and no field power lost. Strength is whatever the magnet is. Early steel magnets are weak. This motor is excellent once the magnets are good, and it cannot field-weaken by a rheostat the way a wound field can.

Speed control without electronics:

- Lower armature voltage, lower speed. A series resistor works and wastes heat. A separate generator whose field you adjust (Ward Leonard set) does it cleanly: motor-generator, fully steampunk, no valves or semiconductors.
- Weaken the field, speed rises and available torque falls. Do this on shunt and compound only, and with a stop so the field cannot be opened (an open shunt field on a loaded motor is another runaway).
- Gears for anything the electrical range cannot cover.

## Universal motors

A series motor fed from AC still turns, because field and armature reverse on the same half-cycle and the torque direction stays put. Commutator motors of this kind spin very fast, often 10,000 rpm and up, and are light for the power. Hand tools, fans, and early vacuum cleaners. They are loud, the brushes wear, and they spit radio noise. Fine as a compact tool motor. Poor as a quiet all-day mill motor.

## Induction

Nikola Tesla and Galileo Ferraris, late 1880s. A three-phase winding makes a magnetic field that rotates at synchronous speed:

`ns = 120 × f / p`

where `ns` is revolutions per minute, `f` is frequency in hertz, and `p` is the number of poles.

| Poles | Speed on 50 Hz | Speed on 60 Hz |
|---|---|---|
| 2 | 3,000 | 3,600 |
| 4 | 1,500 | 1,800 |
| 6 | 1,000 | 1,200 |
| 8 | 750 | 900 |

The cage rotor is bars of copper or aluminum shorted by end rings, like a squirrel cage. The rotating field induces current in those bars. The bars feel a force that drags the rotor after the field. If the rotor ever caught the field, induced current would fall to zero and torque would vanish. So the rotor always slips a little. A few percent slip at full load is normal. Slip is why these are asynchronous.

No brushes, no magnets, no fragile winding on the spinning part. Overload it and it just draws more current and gets hot. Stall it and it survives if the protection opens before the winding cooks. This is why factories standardized on it.

Starting on full voltage draws several times running current. A wound rotor with slip rings lets the starter insert resistance (high torque, less current) and then short the rings. Star-delta and autotransformers are the other pre-electronic starts. A variable-frequency drive solves start and speed together and is a late invent.

**Single phase** has no rotating field by itself, only a pulsing one, so a cage rotor hums and stays still until something shoves it. Fixes, from crudest to best:

- **Shaded pole:** a copper loop on one side of the pole. Cheap fans. Weak.
- **Split phase:** a second winding with more resistance, switched out by a centrifugal switch once it is spinning.
- **Capacitor start:** the second winding fed through a capacitor for a truer phase shift. Stronger start. Switch opens after start.
- **Capacitor run:** a smaller capacitor left in circuit. Quieter, better efficiency, the right small-motor compromise.
- **Repulsion start:** commutator start, then a shorting ring makes it a cage. Historical, high torque.

A shop with only one-phase supply (one alternator winding) still wants three-phase motors on anything large. A rotary converter, which is a machine spun up and then delivering three phases, is the no-electronics bridge.

## Synchronous

The rotor is a magnet, wound or permanent, and it locks to the rotating stator field. Speed is the table above, with zero slip. Exceed the pull-out torque and it stalls abruptly instead of slowing smoothly.

Wound-field synchronous machines are how large alternators are built. As motors they can run at power factor 1, or can be over-excited to behave like capacitors and prop up the voltage of a factory line. They need a DC source for the rotor (a small exciter on the same shaft, or slip rings) and a way to get up to speed (a pony motor, damper bars that start them as induction motors, or a variable-frequency supply).

Permanent-magnet synchronous motors skip the exciter. On a fixed factory frequency they run at one speed, like a synchronous motor should. On an inverter they become the high-efficiency variable-speed motor. Burying the magnets in the rotor (interior type) adds reluctance torque and lets the drive weaken the field for high speed. Surface magnets are simpler and are easier to retain with a sleeve.

A hysteresis rotor is a ring of magnetically hard steel. It slips, heats, and then locks in. Inefficient and remarkably smooth. Instrument loads, not traction.

## Reluctance and steppers

A reluctance motor has a rotor that is only shaped iron. Magnetic circuits pull hardest when the easy path lines up with the field. That pull is the torque. No magnets to demagnetize, no rotor copper to melt, and the rotor can run hotter than a magnet machine.

- **Synchronous reluctance** on a three-phase supply locks in like a synchronous motor once it is near speed. Modern laminated shapes reach induction-class and better efficiency.
- **Switched reluctance** energizes one stator tooth pair at a time, in sequence, as the rotor crest approaches. It needs a rotor-position sensor or a good estimate, and a switch per phase. Torque is lumpy and the machine is loud. The payoff is a rotor that is a stack of punchings and a stator that tolerates heat. A rune or a mechanical commutator could fire the phases on a crude version. A good version wants fast switches.
- **Steppers** are reluctance or magnet motors built so each pulse moves a known angle. Hold current keeps the shaft on that step even at zero speed. They run open-loop until overloaded, then they lose steps silently and the position is wrong. Efficiency is mediocre because the windings stay energized. Right for a feed screw or a pointer. Wrong for a fan that runs all day.

## Linear forms and short strokes

Unroll a rotary motor and the traveling field drags a plate (induction) or locks a magnet track (synchronous). Force replaces torque. Air gap is the enemy: a linear machine has a long gap and uses more current than a rotary motor of the same power. Good for a launcher, a sliding door, a maglev sled. Wasteful as a substitute for a piston unless the motion was already linear.

A voice coil is a short solenoid optimized so force is proportional to current across the stroke. Speakers are the common case. Stroke is millimeters to a few centimeters.

A plain solenoid yanks a plunger into the coil. Force is high at the end of the stroke and weak at the start. Valves, catches, bells, and trip mechanisms. AC solenoids need a shading ring or they buzz.

Piezoelectric stacks change length by a tiny fraction when voltage is applied. An ultrasonic motor lets that vibration walk a rotor through friction. No magnetic field, so it can sit next to a compass or a sensitive instrument. It wears, and it wants a high-frequency supply.

Electrostatic motors need either tiny gaps (insect mechanisms, MEMS) or voltages that are a hazard at human scale. Skip them for workshop invents.

## Magnets and wire, in the order a shop would meet them

| Field source | Strength | Shop note |
|---|---|---|
| Lodestone, magnetite | Weak | A demonstration that the field can be permanent. |
| Hardened steel bar | Weak to modest | Eighteenth and nineteenth century permanent magnets. Touchy. Easy to knock down. |
| Electromagnet, soft iron, copper coil | Strong, and adjustable | The real near-reach field. Needs continuous current. A dynamo can supply its own field once it is flashed. |
| Alnico (aluminum-nickel-cobalt) | Strong | Holds against heat and vibration better than later rare earths. Can be cast. |
| Ferrite ceramic | Modest | Cheap, brittle, rust-proof. Good enough for a fan or a speaker. |
| Samarium-cobalt | Very strong | Holds magnetism when hot. |
| Neodymium-iron-boron | Strongest common magnet | Rusts if unplated. Loses magnetism when hot. Grades differ, but many are unhappy above the temperature of boiling water, and the Curie point is a few hundred degrees. Do not put one next to a steam chest. |

Windings are copper. Silver is a small conductivity win and a bad shop habit (`Generators.md`). Aluminum is lighter and worse per cross-section. Insulation is varnish, silk, cotton, and later enamel. Without insulation the coil is one shorted turn and makes heat instead of field.

Mythril superconducting windings remove copper loss on a DC field and raise the field a compact coil can hold. They still quench above a critical current, and the frame still has to hold the magnetic pressure. They do not remove the need for laminations in an armature that sees a changing field, and they do not replace a commutator by themselves.

## What to build first

1. A two-pole electromagnet and a commutator drum on a hand crank, to see generation.
2. The same machine fed from a battery or from a second dynamo, as a brushed DC motor.
3. Shunt winding for anything that must not run away, series only for a load that is always engaged.
4. Three-phase cage induction once an alternator exists, for mill shafts that can run at one speed.
5. Brushless, stepper, and switched-reluctance drives only after there is a way to switch current faster than a mechanical commutator, whether that way is electronic or runic.

Speed is still `120 × frequency / poles` for every synchronous and, approximately, every induction motor. Changing speed on those machines means changing frequency, changing pole count with a second winding, or putting gears in the drive. A DC armature voltage is the easier knob until inverters exist.
