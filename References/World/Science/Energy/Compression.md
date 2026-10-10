# Compression

Gas and solid compression math for Fire Piston, Frost Breath, air cartridges, micro-pierce and cloak cooling. Fans: `FanAirflow.md`. Cast: `../../../Runes/Energy.md` (`Mana = J / (10 × η × μ)`). ημ = 1 figures are L2 INT 15 reference.

## Narrative

Isothermal gas work is `P V ln`. Adiabatic ignition and freeze use the γ law. Metal does not harden under pure hydrostatic squeeze. Plastic flow (`σ × ε × V`) shapes and hardens. Living targets resist raw micro-compression the same way they resist cheap vacuum kills.

## Detail

### Gases (isothermal)

```
W = P₁ V₁ ln(V₁ / V₂)
```

### Solids

**Elastic only** (bulk modulus B):

```
E = ½ · B · (ΔV/V)² · V
```

Hydrostatic squeeze does **not** forge or work-harden (von Mises pressure-independent). Permanent shape:

```
E ≈ σ_flow × ε_plastic × V
```

Example: 400 MPa × 10% × 1 cm³ ≈ **40 J** (~4 mana at ημ 1), hundreds of times the elastic-only figure for the same V.

Hot steel: **B stays ~100–130 GPa** (cold ~160). What drops is **flow stress** (~10×). Model hot shaping as low σ_flow, not soft B.

Hammer-scale **50 J** into 10 cm³ steel (B 100–130 GPa) → elastic ΔV/V only ~**2%**. Real shaping still uses the plastic equation. Shop blows often **20–80 J**.

### Fire Piston (adiabatic ignition)

```
T₂ = T₁ × (V₁/V₂)^(γ−1)     // γ_air = 1.4
W = P₁ V₁ /(γ−1) × [(V₁/V₂)^(γ−1) − 1]
```

10:1 from 293 K → **~736 K** (~463 °C), above cellulose char. 1 L / 10:1 → **W ≈ 383 J** (~38 mana at ημ 1). Flameless tinder / lamp / powder ignition. Heat pays heat **at the fuel**. Fire Piston pays **compression work** on a gas pocket.

### Frost Breath (adiabatic expansion)

Same law, expand instead. 10:1 from 293 K → **~117 K** ideal; practical **−50 to −80 °C**. Freeze lock, hinge, string, thin ice. Setup mirrors Fire Piston (~383 J for 1 L / 10×). Personal sphere path: cloak air cooling below.

### Pressure purification (HPP-style)

```
E/V ≈ P² / (2 B)     // B_water ≈ 2.2 GPa
```

500 MPa → ~**57 kJ/L** (~5.7k mana at ημ 1; ~2.6k at INT40 L2). Sterilize water/rations without cooking. Distinct from vacuum freeze-dry.

### Air cartridge

Isothermal fill `W = P₁ V₁ ln(P₂/P₁)`. 1 L to 200 bar ≈ **537 J** (~54 mana at ημ 1). Pre-charge; later air-bolt / ram / jump. Overfill/puncture hazard.

### Micro-compression

Prefer plastic pierce `E ≈ σ_flow × ε × V`. Elastic proxy shows why small V is cheap: same strain on a tip vs a plate patch can be **~2500×** less energy.

- Mundane / unwarded: pay the equation (cleave, engrave, tumbler, rope fiber)  
- Living / mana-armored: vitality/magic resist blocks free kill / armor split (hub living-resistance rule)  
- Arrow tips: hardness gate still applies; do not silently replace tip H with micro-compression  

### Compression-forged edges (downtime)

Cold work can raise yield ~**20–50%** before anneal. Many low-strain passes on an edge strip. Overwork without anneal → microcrack. Success raises lasting hardness for later pierce tables.

### Cloak air cooling

Personal compress-expand cooling cycle. D prices it then **forgoes** it for a **cold rune** (less babysitting). Fans: `FanAirflow.md`. Mana: `../../../Runes/Energy.md`.

Cold from expansion only happens if the gas **does work** against a held push. Dump compressed air through a nozzle without catching that work and you get almost no chill. The cloak machine works. The heat plume, beach-ball tank and −113 °C metering make a cold rune win for the same comfort goal.

#### Charge size

```
V₀ = 5 m³          // sphere ≈ 2.1 m across (r ≈ 1.06 m)
~198 mol / 5.7 kg air at 35 °C, 1 atm
10:1 → 0.5 m³ (~0.98 m across, beach-ball class)
```

#### Why plain release fails

Spray cans cool because liquid boils. Dry 10 atm air through a nozzle drops only ~**2 K**. Magic (or a piston) must absorb expansion work so internal energy leaves as motion, not leftover heat.

#### Ideal 10:1 cycle

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

#### Run time

- One 10:1 charge ≈ **2 h** at 100 W rest, ≈ **26 min** at 500 W work (cloak leak shortens)  
- 100 W cooling ≈ **0.75 g/s** cold air  
- −113 °C burns skin → mix before contact; vent warm for max heat per gram  
- 10 min compress dumps ~**2 kW** upward (visible plume). Pre-compress in shade/rest  

#### Why cold rune wins

No fight sphere, no plume beacon, no cryogenic metering, same stay-cool job with less babysitting.

## Open

- CraftMetal barrier molds
- Exact cold-rune Useful joules when ManaCast absorbs

Compressed-mana stroke cousin (Sahildr hammer): `../../../Combat/ImpactRune.md`.
