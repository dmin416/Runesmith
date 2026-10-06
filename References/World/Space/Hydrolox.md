# Liquid Hydrogen + Liquid Oxygen (Hydrolox)

Hub: `Space.md`. Mechanical orbit energy: `OrbitEnergy.md`. Station masses: `LowEarthOrbitHabitat.md`, `GeosynchronousHabitat.md`.

Highest-efficiency chemical rocket propellant in common Earth use. Mundane baseline for putting habitat mass on orbit; magic can replace hardware later.

## Chemistry

- Reaction: 2H₂ + O₂ → 2H₂O
- Typical mix: about 6 kg of oxygen per 1 kg of hydrogen (slightly hydrogen-rich to lower exhaust weight and engine temperature)
- Energy content of hydrogen: 120 MJ/kg, nearly three times gasoline
- Exhaust: superheated water vapor at roughly 5,500°F in the combustion chamber

## Performance

| Measure | Value |
|---|---|
| Efficiency in vacuum (specific impulse) | 450 to 465 seconds, the highest of any chemical rocket fuel in use |
| Exhaust speed | about 2.8 mi/s (4.4 km/s) |
| Liquid hydrogen density | 0.071 g/cm³ (about 1/14 of water) |
| Liquid oxygen density | 1.14 g/cm³ |
| Combined propellant density | about 0.36 g/cm³ |
| Hydrogen storage temperature | -423°F (20 K) |
| Oxygen storage temperature | -297°F (90 K) |

## Production

Earth supply is mostly natural-gas steam reforming (~9 to 12 kg CO2 per kg H₂). Coal gasification is worse. Carbon capture, methane splitting, nuclear or renewable electrolysis cut that footprint.

**Electrolysis (clean invent path)**

- Theoretical minimum: 39.4 kWh per kg of hydrogen
- Current electrolyzers: about 50 to 55 kWh per kg
- Water consumed: about 9 kg per kg of hydrogen
- Byproduct: 8 kg of oxygen per kg of hydrogen, more than enough to supply the rocket's oxygen

**Liquefaction**

- Current plants: about 10 to 13 kWh per kg (roughly 30% of the hydrogen's energy)
- Theoretical minimum: about 3.9 kWh per kg
- Liquid oxygen liquefaction: about 0.4 kWh per kg

## Exhaust and handling profile

**Clean at the pad**

- No CO2, soot, chlorine or alumina at launch
- Nontoxic propellants; a spill evaporates without contaminating soil or water

**Remaining impacts**

- **Water vapor in the upper atmosphere:** stays much longer at high altitude than near the ground; small warming effect; can seed high-altitude clouds
- **Nitrogen oxides:** hot exhaust plume heats surrounding air enough to form some NOx in the lower atmosphere
- **Hydrogen leaks:** hydrogen is an indirect greenhouse gas (extends methane lifetime); the tiny molecule leaks through seals easily
- **Production source:** the biggest factor by far; dirty hydrogen erases most of the launch-site benefit

**Liftoff thrust problem**

Hydrogen's low density gives weak liftoff thrust for its tank size. Many Earth hydrolox vehicles strap on solid boosters to get off the pad (dirty exhaust). Pure-hydrolox heavy lifters are rare.

## Engineering challenges

- Huge, heavily insulated tanks due to low density
- Constant boil-off; long-term storage in orbit requires active cooling
- Hydrogen embrittlement weakens many metals over time
- Leaks are common and the flame is nearly invisible in daylight
- Conversion between two molecular forms of hydrogen (ortho and para) releases heat during storage unless handled during liquefaction

## Applied to the stations

Estimates scale from an Earth heavy hydrolox reference that used about 90,000 kg of hydrogen and 537,000 kg of oxygen to put 28,800 kg into low orbit. Green hydrogen at 55 kWh per kg plus 11 kWh per kg liquefaction. Oxygen comes from the electrolysis byproduct.

GEO column uses mass that must reach **low** orbit first (~127,000 kg including transfer stage), not the on-station GEO mass alone. Pure orbital energy: `OrbitEnergy.md`.

| | Low orbit station | Geosynchronous station |
|---|---|---|
| Mass in low orbit | 32,600 kg | 127,000 kg (includes transfer stage) |
| Hydrogen | ~102,000 kg (225,000 lb) | ~397,000 kg (875,000 lb) |
| Oxygen | ~609,000 kg (1.34 million lb) | ~2.37 million kg (5.22 million lb) |
| Water to electrolyze | ~920,000 kg (243,000 gal) | ~3.57 million kg (943,000 gal) |
| Electricity to produce | ~7.0 GWh | ~27.2 GWh |
| Pure orbital energy | 0.30 GWh | 0.78 GWh |
| Overall efficiency, power plant to orbit | ~4% | ~3% |
| Continuous power to make that in one year | ~0.8 MW | ~3.1 MW |
