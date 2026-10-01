# Thermometers Without Electronics

Three buildable designs for a magic setting: alcohol-in-glass, thermocouple, and bimetallic spring. No electronics.

Use for invent beats (brew / weather thermometers, oven dials, forge probes). Do not paste Earth brand names into prose unless the story invents them.

**Accuracy:** solid popular physics / craft summary. Ranges and fixed points are order-of-magnitude, good enough for prerequisite checks. Galinstan and Type letter codes are Earth labels; use setting names in prose.

**Caldris readout** (`../World/Technology.md`): craftsman + early-industrial magitech. **In reach or near-reach:** alcohol-in-glass (glassblowing + distillation + ice/boil calibration), bimetallic oven dials (brass / steel strip, coil, pointer). Mercury or glycerin high-temp liquid tubes if glass and sealing exist. **Invent or prestige:** thermocouples with a galvanometer (fine wire, magnets, cold junction), mythril / mana-steel high-temp pairs, adamantium sheaths, magic-stabilized fill liquids, enchanted uniform bore. Heat Sense and heat runes can substitute for instruments until craft catches up.

Companions: `CraftMetal.md`, `Body.md` (thermal math), `WritingTools.md` (kiln / heat-rune craft), `../Ideas.md` (civilian tech).

---

## 1. Alcohol-in-Glass Thermometer

**Range:** about -100 to 75°C (ethanol boils near 78°C)

**Materials**
- Glass: soda-lime works. Borosilicate handles temperature swings better.
- Ethanol distilled as pure as possible. Water contamination shifts the readings.
- Alcohol-soluble dye (madder red or cochineal) so the column is visible.
- Backing board of wood, bone, or ceramic for the scale.

**Tools**
- Glassblowing setup: furnace or flame, blowpipe, tongs.
- Method to draw a capillary: heat a glass tube and pull it to a thin, even bore. Uniform bore matters most because uneven width makes degrees unequal.
- Funnel or fine pipette.
- Reference baths: crushed ice and water (0 point), boiling water (100 point).

**Process**
1. Blow a small thin-walled bulb on one end of the capillary.
2. Warm the bulb so the air expands, then dip the open end into dyed alcohol. As the bulb cools the liquid is drawn in.
3. Repeat, or gently heat to drive out trapped air, until the bulb and part of the tube are full.
4. Seal the top in flame while the alcohol is slightly warm so a small gas gap remains.
5. Dip in ice water and mark the level. Dip in boiling water and mark the level. Divide the space between into equal degrees.

**Magic shortcuts:** an enchantment for a perfectly uniform bore, or sealing the tube under vacuum.

### Baking Variant (high-temperature liquid thermometer)

Ethanol cannot be used for baking (150 to 260°C). The design stays the same but the fill liquid and glass change.

| Fill liquid | Usable to | Notes |
|---|---|---|
| Mercury | about 350°C | Classic choice. Toxic. Needs a sealed, protected tube. |
| Mercury with pressurized nitrogen above it | 500°C+ | Gas pressure raises the boiling point. Needs thick-walled glass. |
| Galinstan (gallium, indium, tin) | 1000°C+ | Non-toxic. Needs quartz or very pure glass and oxygen-free sealing. |
| Glycerin or heavy mineral oil | about 250°C | Cheap and safe but slow, viscous, and can darken with age. |
| Magic-stabilized liquid | Set by the enchantment | A fire-resistant or boiling-point-raised alcohol. |

**Changes from the basic build**
- Use borosilicate or quartz glass so the tube survives oven heat.
- Thicker bulb walls and a metal or ceramic guard cage, since oven use means bumps and thermal shock.
- Calibrate at fixed points: ice (0°C), boiling water (100°C), tin melts (232°C), lead melts (327°C).
- Sealed gas gap above the liquid, sized so expansion never bursts the tube.

## 2. Thermocouple

**Range:** about -200 to 1700°C depending on metal pair

**Principle:** two different metals joined at one end produce a tiny voltage that depends on the temperature difference between the joined end and a reference end (Seebeck effect). Expect roughly 40 to 55 microvolts per degree.

**Metal pairs**
- Iron and constantan (copper-nickel): Type J, good to a few hundred degrees and beyond.
- Copper and constantan: Type T, cold to moderate heat.
- Bismuth and antimony: Seebeck's original pair. Easy to cast but brittle.
- High-temperature pair (replaces platinum and platinum-rhodium): see below.

### Fantasy Metal Replacement for Platinum

Real Type S and R thermocouples use pure platinum for one leg and a platinum-rhodium alloy for the other. They need a stable, corrosion-proof metal that can be drawn into wire and keeps its properties at furnace heat.

| Metal | Verdict | Reasoning |
|---|---|---|
| **Mythril** | Best choice | Magically saturated Ag–Cu; pearlish silvery gold; drawable specialist wire. Stable superconducting leg. Not titanium. |
| **Mana steel** | Good as the alloy partner | Responds to mana, which gives the second leg a different voltage curve. Alone it drifts with ambient mana, so keep it as a minor alloying element. |
| **Adamantium** | Poor as a wire | Too hard to draw into fine wire and too inert to give a useful voltage difference. Better as the protective sheath around the probe. |

**Recommended high-temperature pair**
- Leg A: pure mythril.
- Leg B: mythril alloyed with a small amount of mana steel (the equivalent of platinum-rhodium).
- Sheath: adamantium tube, so the probe survives forge or kiln conditions.

**Materials and tools (all pairs)**
- Insulation: ceramic beads, fired clay tubes, or glass fiber.
- Smelting and alloying equipment.
- Drawplate for wire.
- Forge or flame to fuse the junction (twist the ends, then braze or weld).
- Ice bath to hold the reference end at 0°C.

**Reading the signal without electronics**
- Galvanometer: a fine wire coil suspended between magnet poles on a thread or hairspring. Current twists the coil and moves a pointer, or a mirror reflects a light beam onto a scale.
- Thermopile: many junctions wired in series so the voltages add up.
- Magic option: a rune or enchanted element that shifts color or position in proportion to voltage.

**Calibration:** mark the meter at ice (0°C), boiling water (100°C), tin (232°C), lead (327°C), and zinc (420°C), then interpolate.

## 3. Bimetallic Spring Thermometer

**Range:** about -70 to 500°C

**Principle:** two metals with different expansion rates are bonded into one strip. Heating makes one side expand more, so the strip bends. Coiled into a spiral, the bending turns a pointer across a dial. This is the most practical design for ovens and baking.

**Materials**
- Two bonding metals: steel and brass (brass expands more). Copper and iron also work.
- Thin sheet of each, about 0.2 to 0.5 mm.
- Brass or steel dial face, pointer needle, and a central shaft.
- Protective metal case with a glass or crystal window (heat-tolerant glass for ovens).
- Stem or mounting clip to hold it in an oven rack or food.

**Tools**
- Rolling mill or hammer and anvil to get thin, even sheet.
- Brazing flame and flux, or rivets, to bond the two layers along their full length.
- Mandrel or rod to coil the strip into a spiral.
- Fine files, drill, and a lathe or hand tools for the shaft and pointer.

**Process**
1. Cut matching strips of each metal.
2. Bond them face to face (braze, hammer-weld, or rivet along the length) so they cannot slide apart.
3. Wind the bonded strip around a rod into a flat spiral or helix.
4. Fix the outer end to the case and the inner end to the pointer shaft.
5. Mount the dial behind the pointer.
6. Calibrate in a bath or oven against known points (ice, boiling water, tin melt) and mark the dial.

**Advantages for baking:** no liquid to boil, no fragile capillary, and it tolerates the full oven range. It reads slower than a liquid thermometer and loses accuracy if the bond weakens or the spiral is bent.

**Magic shortcuts:** an enchanted bond that never separates, or a mana-steel layer for a larger deflection per degree.

## Quick Comparison

| Type | Range | Accuracy | Best for | Key skill |
|---|---|---|---|---|
| Alcohol-in-glass | -100 to 75°C | Good | Weather, cold storage, brewing | Glassblowing |
| High-temp liquid (mercury or galinstan) | up to 350 to 1000°C+ | Good | Baking, kilns | Glassblowing, sealing |
| Thermocouple | -200 to 1700°C | Moderate | Forges, kilns, furnaces | Metallurgy, wire drawing |
| Bimetallic spring | -70 to 500°C | Moderate | Ovens, meat, dial gauges | Metalworking |
