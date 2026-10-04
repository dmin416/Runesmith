# Cloak Air Cooling

Personal compress-expand cooling cycle. D prices it then **forgoes** it for a **cold rune** (less babysitting). Compression school: `Compression.md`. Fans: `FanAirflow.md`. Mana: `../../../Runes/Energy.md`.

## Narrative

Cold from expansion only happens if the gas **does work** against a held push. Dump compressed air through a nozzle without catching that work and you get almost no chill. The cloak machine works. The heat plume, beach-ball tank and −113 °C metering make a cold rune win for the same comfort goal.

## Detail

### Charge size

```
V₀ = 5 m³          // sphere ≈ 2.1 m across (r ≈ 1.06 m)
~198 mol / 5.7 kg air at 35 °C, 1 atm
10:1 → 0.5 m³ (~0.98 m across, beach-ball class)
```

### Why plain release fails

Spray cans cool because liquid boils. Dry 10 atm air through a nozzle drops only ~**2 K**. Magic (or a piston) must absorb expansion work so internal energy leaves as motion, not leftover heat.

### Ideal 10:1 cycle

1. Slow compress to 0.5 m³ → dump **~1.17 MJ** heat to 35 °C air (fast compress → ~320 °C gas)  
2. Hold at 10 atm ambient-temp “battery”  
3. Expand against magic → ~**−113 °C**, recover **~0.61 MJ**  
4. Meter into cloak → warm to 20 °C absorbing **~0.77 MJ** from body/cloak; vent hem  

```
W_net ideal ≈ 0.55 MJ (~130 kcal)
Imperfect 2–3× → 1.1–1.7 MJ (~260–400 kcal)
At ημ = 1 → ~110k–170k mana if the pool pays every joule
```

That mana scale is why the cold rune wins.

| Ratio | Compressed V | T after expand | Cooling / charge | Net work (ideal) |
|---|---|---|---|---|
| 5:1 | 1.0 m³ | −79 °C | 0.57 MJ | 0.35 MJ |
| 10:1 | 0.5 m³ | −113 °C | 0.77 MJ | 0.56 MJ |
| 20:1 | 0.25 m³ | −142 °C | 0.94 MJ | 0.79 MJ |

10→20: **+41%** work for **+22%** cooling. Diminishing returns.

### Run time

- One 10:1 charge ≈ **2 h** at 100 W rest, ≈ **26 min** at 500 W work (cloak leak shortens)  
- 100 W cooling ≈ **0.75 g/s** cold air  
- −113 °C burns skin → mix before contact; vent warm for max heat per gram  
- 10 min compress dumps ~**2 kW** upward (visible plume). Pre-compress in shade/rest  

### Why cold rune wins

No fight sphere, no plume beacon, no cryogenic metering, same stay-cool job with less babysitting.

## Open

- Exact cold-rune Useful joules when ManaCast absorbs  
