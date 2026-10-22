# Gradients

> **Design loot / Earth physics.** Everything flows downhill along a gradient. Pressure drives fluid. Temperature drives heat. Concentration drives diffusion and osmosis. Voltage drives charge. Density drives buoyancy. Mana can create a gradient or ride one that already exists. Not automatic law.
>
> Cast law: `../../../Runes/Energy.md`, `ManaCast.md`. Mana Hands pricing and the braking rule: `ManaHandPhysics.md`. Vacuum shells, latent heat and freeze-drying: `../Metallurgy/Vacuum.md`. Compression and Fire Piston: `Compression.md`. Water lift: `Pumps.md`. Moving heat, water, molecules and charge: `EnergyPumping.md`. Shear: `Shear.md`. Spin: `Spin.md`. Balloons: `LighterThanAir.md`. Eardrum and lung thresholds: `../../../Combat/SonicAirDisplacement.md`.

## Shared cost law

- **1 MP = 10 J.** Raw MP below is J ÷ 10. Real casters divide by their conversion (`ManaHandPhysics.md` §2).
- **Stopping costs the same as starting.** Halting a flow pays the full energy removed (`ManaHandPhysics.md` §10). Let flows run out instead of catching them.
- **Riding a gradient is cheaper than making one.** A gradient that already exists is stored energy. Opening a path for it is close to free. Building one from flat ground pays the full bill.

## 1. Pressure

```
Flow runs from high pressure to low
Void of volume V            W = p₀ × V            (101 J per liter at sea level)
Squeeze gas (slow, cool)    W = p₀ × V × ln(p ÷ p₀)
Push liquid                 W = Δp × V
Force on an area            F = Δp × A
Hydrostatic                 Δp = ρ × g × h         (10 m water ≈ 1 bar)
```

- **Suction tops out at one atmosphere.** A perfect vacuum only lets the air push with 101 kPa. Pushing has no such ceiling. It is limited by the walls and by the cost.
- The void cost matches `../Metallurgy/Vacuum.md` (10 L full vacuum ≈ 1,013 J).

| Job | Work | Raw MP |
|---|---|---|
| Empty 1 L to vacuum | 101 J | 10 |
| Squeeze 1 L of air to 2 bar | 70 J | 7 |
| Squeeze 1 L of air to 10 bar | 233 J | 23 |
| Empty 1 m³ to vacuum | 101 kJ | 10,100 |

### Suction grip

A flat seal holds with `F = 101 kPa × A` and the void is nearly zero volume. Making it is almost free. Holding it is free while the seal holds.

| Cup width | Hold force | Holds about |
|---|---|---|
| 5 cm | 200 N | 20 kg |
| 10 cm | 800 N | 80 kg |
| 20 cm | 3.2 kN | 320 kg |

Smooth glass, polished stone, metal and lacquered wood seal. Rough stone, bark and cloth leak. A leaking seal pays the leak rate as continuous vacuum work.

### Boiling point follows pressure

| Pressure | Water boils at | Use |
|---|---|---|
| 0.6 kPa | 0 °C | Freeze-drying below this (`../Metallurgy/Vacuum.md`) |
| 10 kPa | 46 °C | Concentrate syrups, honey and potions with no scorch |
| 20 kPa | 60 °C | Low-heat jam and extract reduction |
| 50 kPa | 81 °C | |
| 70 kPa (about 3,000 m altitude) | 90 °C | Why mountain cooking is slow |
| 101 kPa | 100 °C | Sea level |
| 200 kPa | 120 °C | Pressure cooking |
| 500 kPa | 152 °C | |
| 1,000 kPa | 180 °C | Boiler territory |

**Pressure cooking.** Cooking rates roughly double per 10 °C. A barrier lid held at 2 bar (120 °C) cooks tough meat and beans about 3 to 4 times faster. A 20 cm pot lid at 1 bar extra carries about 3.1 kN. The lid must hold. A failed lid sprays superheated water.

### Bernoulli

Faster flow has lower pressure. Atomizers, carburetors and wings work on this. Storm wind lifts roofs this way. A Hand jet across the top of a tube draws liquid up and sprays it (perfume, lamp oil, paint mist).

### Pipes

Flow through a thin tube scales with radius to the fourth power: `Q = π r⁴ Δp ÷ (8 μ L)`. Half the radius gives one sixteenth of the flow. Useful for metered drips, dosing and irrigation.

### Hydraulics

A small piston pushes a large one and force multiplies by the area ratio. Energy does not. The small piston travels farther. Mana Hands gain nothing in joules from a press. They gain force at a lower rigidity demand.

### Bodies and pressure

| Change | Effect |
|---|---|
| A few kPa fast | Ear pressure, pop, brief disorientation |
| About 35 kPa | Eardrum rupture threshold |
| Fast drop from over 2 bar of breathing (diving) | Decompression sickness |
| Half pressure (about 5,500 m) | Altitude sickness for most people |

### Implosion

A void collapses with the energy it cost: 101 kJ per m³ (about 24 g of TNT worth). Focused collapse in water gives water hammer and cavitation damage. Hazard of large vacuum shells.

### Chimney draft

`Δp ≈ ρ × g × h × (1 − T_air ÷ T_flue)`. A 10 m chimney with a 200 °C flue pulls about 45 Pa. A small Hand fan at the chimney foot adds draft for a few watts (`FanAirflow.md`).

## 2. Temperature

```
Conduction    q = k × ΔT ÷ L                  (W per m²)
Work available from a gradient  W ≤ Q × (1 − T_cold ÷ T_hot)
```

- **Heat moves on its own.** Mana pays only to speed it up, slow it down or send it uphill (`EnergyPumping.md`).
- **Every gradient is an engine.** A forge at 1,200 °C beside 20 °C air can give up to 80% of the heat it passes as work (Carnot). Stirling engines run on any gradient (`StirlingEngines.md`). Thermoelectric junctions also turn a gradient into current, at a few percent.
- **Thermal shock.** Glass and stone crack when one face heats faster than the other. Tempering uses the same stress on purpose (`../../Materials/GlassTempering.md`).
- **Convection.** Hot air rises in plumes. Gliders ride them (`../Vehicle/PerfectGlider/`). Stirring a pot breaks the still layer at the bottom and stops scorching.

## 3. Concentration

### Diffusion

`t ≈ x² ÷ (2 × D)`. Time grows with the square of the distance.

| Job | Distance | Time (no stirring) |
|---|---|---|
| Sugar into fruit | 5 mm | about 7 h |
| Sugar into fruit | 1 cm | about 28 h |
| Salt into meat | 1 cm | about 9 h |

Diffusion is slow over centimeters. Speed it up three ways:

1. **Stir.** Shear thins the still layer at the surface (`Shear.md`).
2. **Pressure cycle.** Pull a vacuum then let it go. Air leaves the pores and the brine rushes in. Vacuum marinating and vacuum impregnation of wood both work this way.
3. **Cut thinner.** Half the thickness gives a quarter of the time.

### Osmosis

Water moves across a membrane toward the saltier side. Seawater pulls with about 2.7 to 3 MPa.

- Salt draws water out of meat, fish and vegetables. Curing and pickling.
- Fresh water swells and bursts cells. Salt dries slugs and leeches.
- Reverse osmosis is pushing the other way at more than the osmotic pressure. That is the desalination row in `EnergyPumping.md`.

## 4. Voltage

Charge flows down a voltage gradient. Dry air breaks down at about 3 MV per meter. That is the spark and the lightning stroke. Pushing charge uphill is charge pumping (`EnergyPumping.md`). Storm gradients: `TriggeredLightning.md`.

## 5. Density

- **Buoyancy.** Light rises and heavy sinks. Hot air balloons and vacuum shells: `LighterThanAir.md`.
- **Dense gas pools.** Carbon dioxide and smoke sink into cellars, mines and wells. A silent killer. A Hand fan clears it for a few watts.
- **Layered water.** Cold water sinks under warm. Lakes and the sea stratify. Fish and mixing follow the layers.
- **Mirages.** Hot air over sand or road bends light. Heat shimmer hides and misplaces distant targets.

## Potential

- **Pressure Lid.** Barrier lid at 2 bar. Faster stews, tender meat and sterilizing jars at 120 °C.
- **Vacuum Still.** Reduce syrups, honey, potions and extracts at 45 to 60 °C. No scorch. Keeps volatile aromas better.
- **Suction Grip.** Climb glass and polished stone. Hold a door or a shield to a wall. Lift a smooth slab.
- **Vacuum Marinade.** Brine or cure in minutes instead of hours. Also impregnates wood with oil or resin.
- **Ear Pop.** A fast change of a few kPa at a target's head. Brief disorientation. Dangerous above about 35 kPa.
- **Altitude Bubble.** Hold air near sea-level pressure around the head on a mountain. Lowers altitude sickness.
- **Draft Boost.** More pull for forges, kilns and chimneys for a few watts.
- **Atomizer.** Spray oil, perfume, paint or medicine mist.
- **Gradient Tap.** Open a path for heat, water or pressure that already wants to move. Close to free.
- **Implosion Pocket.** Let a prepared void collapse at the right moment. Costs what the void cost.

## Open

- Barrier hold cost for a sustained pressure difference (lid, bubble, seal). Physics says zero for a perfect static seal. Canon hold drain for Hands is about 1 J/s per kg (`ManaHandPhysics.md`). A barrier rule is not locked.
