# Stirling Engines

Hub: `Engines.md`. Open-cycle steam: `SteamEngines.md`. Reverse this machine into a cooler: `CloakAirCooling.md` is a different cold path. Shaft to volts: `Generators.md`.

Robert Stirling, 1816, patented a closed hot-air engine and the regenerator he called an economiser. The gas inside never leaves. Heat enters through a metal wall at one end and leaves through a metal wall at the other. Any flame, ember, sun, geothermal spring, or heating rune can sit outside. There is no boiler drum and no exhaust of working fluid.

A Stirling boiler is an unrelated water-tube steam boiler. Same surname, different machine. Steam boilers live in `SteamEngines.md`.

## Caldris filter

| Band | What exists |
|---|---|
| Baseline | No Stirling industry. Steam and mana stones already cover rail and kettle heat. |
| Near-reach invent | An atmospheric-air gamma engine with a wire-mesh regenerator, run from a stove or a heating rune. Watts to a fraction of a horsepower. A proof that closed air can turn a shaft. |
| Industrial invent | Pressurized air or helium, metal good for a 600 °C heater head, proper cooler, and a seal that does not leak the charge. This is a real prime mover in the same power class as a small steam engine, quieter and thirstier for craft. |
| Prestige / late | Free-piston engines with clearance seals, hydrogen charge, dish collectors, and reversed machines used as refrigerators. Submarine-style air-independent burners. |

## Ideal cycle

Four steps, with the regenerator storing heat between the hot end and the cold end:

1. **Compress** the gas while it is cold. A little work goes in.
2. **Pass it through the regenerator.** The mesh gives back heat stored on the previous pass. Pressure rises as the gas warms in a fixed volume.
3. **Expand** the gas while the hot end keeps it hot. More work comes out than went in.
4. **Pass it back through the regenerator.** The mesh takes the heat out again before the cold compression.

On paper the efficiency equals Carnot: `1 − T_cold / T_hot`. A real engine does not, because the walls conduct heat the wrong way, the mesh is imperfect, seals leak, bearings drag, and the gas does not stay isothermal while it is compressed and expanded.

Practical bands:

| Build | Efficiency | Notes |
|---|---|---|
| Toy, open to the air, poor mesh | A few percent | Moves itself and a tiny load. |
| Careful atmospheric shop engine | About 5 to 15% | Believable early invent. |
| Pressurized helium, good exchangers | About 25 to 40% | Twentieth-century machines reached the high 30s at the shaft. |
| Dish collector to electricity | About 30% sun to wire on the best tests | Optics and the generator eat part of the engine's share. |
| Low temperature difference | Often under 1 to 2% | The Carnot ceiling is tiny if the two ends are only 20 degrees apart. |

Early nineteenth-century hot-air engines lost to steam on power per weight. Heater heads of wrought iron burned out. The idea came back once stainless heater heads, pressurized inert gas, and better seals existed. The lasting commercial form on Earth was the reversed machine: a Stirling cooler.

## Three kinematic layouts

All three use two moving pieces whose motions are about 90° apart. One piece (the displacer, or the hot piston) shuttles gas between hot and cold. The other (the power piston) compresses and expands it.

| Layout | Arrangement | Trait |
|---|---|---|
| Alpha | Two power pistons, one in a hot cylinder and one in a cold cylinder, joined by a pipe and a crank | Highest power for the bulk. The hot piston's seal lives at heater temperature. Hardest seal in the family. |
| Beta | Displacer and power piston share one cylinder. Displacer is the loose shuttle; power piston is the sealed end, usually the cold end | Compact. Classic "one tube" look. Mechanism to nest both rods is fiddly (a yoke or a rod through a rod). |
| Gamma | Displacer cylinder and power cylinder are separate, piped together | Easiest to build and to seal. More dead volume in the pipe, so less power for the same swept volume. The right first engine. |

The displacer is not the piece that makes the work. Pressure on its two faces nearly cancels. It only has to move gas. It should be light, and it should be a poor conductor along its length so it does not short the hot end to the cold end. A thin stainless shell is the usual answer. The gap around it is a clearance path: too wide and gas sneaks past without touching the heater or cooler, too tight and it rubs as the metal grows.

The power piston carries the full pressure difference. It belongs at the cold end whenever the layout allows, which is the beta and gamma argument.

**Dead volume** is gas space that is neither swept by the power piston nor doing useful heat transfer: pipes, clearances, the inside of a bad manifold. Some dead volume is required, because the heater, mesh, and cooler have to have passage area. Extra empty space flattens the pressure swing and steals power.

## Regenerator

A stack of fine wire mesh, or a metal felt, sitting between the hot end and the cold end. Gas on the way to the cooler gives heat to the mesh. Gas on the way back picks that heat up.

Without it, every cycle throws the gas's heat into the cooler and then pays fuel to heat the same gas again. The engine still runs. It runs as a crude hot-air engine with poor efficiency. With a good mesh, regeneration can hand back more than 95% of that heat.

The mesh wants high surface area, high heat capacity, and low conduction from the hot face of the stack to the cold face. Stainless woven mesh is the usual shop answer. Packing it too tight chokes the flow. Packing it too loose lets gas pass without trading heat. Oil film on the mesh is fatal to the temperature swap, so keep cylinder oil off the regenerator. Dry seals or a lubricant that cannot migrate.

## Gas, pressure, speed

Power scales about with mean pressure, swept volume, and cycle rate, until the exchangers cannot keep up.

A builder's estimate (Beale), for a competent engine with a hot end near 650 °C and a cold end near room temperature:

`watts ≈ 0.015 × mean pressure in bar × power-piston swept volume in cm³ × cycles per second`

A rough first engine lands lower. A cold heat source lands much lower, because the temperature ratio is hidden inside the 0.015.

Example: 5 bar, 50 cm³, 10 cycles per second gives about 38 W if the engine is actually good. Atmospheric pressure (1 bar) on the same iron gives about 8 W. Ten atmospheres gives about 75 W. Pressure is the cheap power once the vessel and the seals can hold it.

| Gas | Why use it | Cost |
|---|---|---|
| Air | Free, and a leaking seal only hisses | Lower power. Oxygen plus oil is a fire risk in a hot cylinder. |
| Nitrogen | Air without the oxygen | Still a bottled gas. |
| Helium | Much better heat transfer, inert | Leaves through tiny gaps. Has to be topped up or sealed for life. |
| Hydrogen | Best power and best efficiency of the common gases | Leaks worse than helium, embrittles some steels, burns if it escapes onto a flame. |

Kinematic shop engines typically run a few hundred to a few thousand rpm. Low-difference engines may cycle about once a second. Free-piston machines often buzz at tens of hertz with a short stroke.

## Other forms

### Low temperature difference

A large, light displacer and a small power piston, run on a gap of a few degrees to a few tens of degrees. A hand on the plate, a sun-warmed stone, or a kettle lid is enough to make one turn. Power is milliwatts to a few watts unless the plates are huge. Useful as a meter for "there is a temperature difference here," and as a waste-heat toy. Useless as a mill engine. The Carnot ceiling for a 20 degree gap around room temperature is only about 6%, and these builds get a sliver of that.

### Free piston

No crank. The power piston and displacer bounce on gas springs and on each other, tuned so the 90° relationship happens by resonance. Seals are close clearances rather than rubbing rings, so a welded vessel can hold helium for years. A linear alternator wrapped around the power piston takes electricity without a rotary shaft. This is the long-life form: space power experiments and cryocoolers. It is a poor first build, because the dynamics are invisible and a wrong mass simply sits there.

### Ringbom

The power piston is on a crank. The displacer is not linked. Pressure pushes it between stops, and it overruns. Fewer joints than a beta, and more ways to stall.

### Fluidyne

Liquid pistons, usually water columns in a U-tube, with a heat exchanger at the closed end. No sliding seal at all. Frequency is about 1 Hz. The output wants to be a pulse of water, so the natural job is a simple pump. A fire, some pipe, and a regenerator can lift water without a machined piston. Power stays low.

### Thermoacoustic

A tube, a mesh stack or regenerator, and a temperature gradient. The heat maintains a sound wave. A piston or a linear alternator at one end turns the sound into shaft power or electricity. Standing-wave stacks are simpler and less efficient. Traveling-wave regenerators do better and start to resemble a Stirling with the piston optional. Craft is pipe and mesh rather than a phased crank. Noise is the product as well as the means.

### Ericsson and other external cousins

An Ericsson engine is external combustion with valves: it heats and cools at constant pressure and uses a regenerator. More like a hot-air steam engine with valves than like a valveless Stirling. Same shop temptation (any fire, no boiler) and an extra set of hot valves to leak.

The Malone engine used a liquid working fluid near its critical point. High pressure, high power density, and a sealing problem worse than helium. A note, not a path.

## Reversed: refrigerator

Drive the shaft and the cycle moves heat from the cold end to the hot end. Stirling coolers and their pulse-tube relatives reach cryogenic temperatures and are the reason the cycle survived commercially. On Caldris a cold rune already does this job more directly (`CloakAirCooling.md` for the air path). A reversed Stirling matters if someone wants cold without a cold rune, or wants to reach temperatures a domestic cold rune has not been asked for.

## Why it loses to steam, and where it does not

Steam won the nineteenth century on specific power, familiar boiler craft, and a seal that only has to hold steam for one stroke. A Stirling heater head must conduct heat in while holding pressure, at a temperature that softens iron. The first engines were large for the horsepower and ate their hot ends.

It wins when:

- The heat source is awkward for a boiler: sunshine, a geothermal seep, a mana stone that must not sit in water, a flame that should stay outside the mechanism.
- Quiet and lack of smoke matter. Combustion, if any, is continuous and can be a clean external burner. Submarine air-independent plants used this: a few tens of kilowatts per module, oxygen carried on board, almost no mechanical noise.
- The same hardware should later run backward as a cooler.
- There is waste heat at a moderate temperature and no wish to raise steam.

It loses when the load needs a fast throttle. The heater head is a lump of hot metal. Power follows temperature, and temperature follows minutes, not the flick of a valve. A steam throttle or a motor controller answers faster. Vehicles on Earth tried pressurized Stirlings more than once and kept the internal combustion engine.

## Craft walls

- Heater-head alloy that survives dull red heat without scaling shut. Plain wrought iron is why the 1816 engines died young.
- A regenerator mesh that is clean, uniformly packed, and not a thermal short from end to end.
- A cold-end seal that holds a pressurized charge for hours. Leather cup seals suit a steam piston and a water pump. They dry out and leak helium.
- A cooler with enough area. All the waste heat leaves through this wall. A small air-cooled fin stack limits the engine no matter how hot the fire is.
- Phase. If the displacer and power piston move together instead of a quarter turn apart, the gas shuttles and the shaft does nothing.
- Start time. The hot end has to come up to temperature before there is torque. A heating rune shortens this only if it is coupled into the heater head, not merely lit nearby.

For a first on-page engine, gamma, air at atmospheric pressure, stove or rune under the hot cap, mesh in the neck, power cylinder off to the side with a leather or soft-metal ring. Expect a machine that turns a small dynamo or a fan, not a train.
