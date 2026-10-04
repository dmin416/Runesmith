# Pumps And Taps

Water lift, head, valves and faucet logic for wells, mines, baths and magitech plumbing. Pipe: `../Metallurgy/CopperPipe.md`, `../Metallurgy/Brass.md`. Fans (air): `FanAirflow.md`.

## Narrative

Atmosphere only pushes so high. Beyond that you need a force pump, staged lifts or a ram. Timing can come from water momentum, springs, weights or muscle. Taps are just valves with human hands on them.

## Detail

### Hard limits

```
h_atm_max ≈ 10.3 m water at sea level     // practical suction ~7–8 m; less with altitude
Δp ≈ ρ g h
10 m water head ≈ 1 bar ≈ 14.5 psi
```

Suction pumps pull. Force pumps push and are limited by pipe strength and power, not atmosphere.

### Lift devices (pre-industrial → useful)

| Device | Power | Lift band | Note |
|---|---|---|---|
| Shadoof | Human + counterweight | 1–3 m | Simple |
| Archimedes screw | Human / animal | 1–3 m per stage | Mud OK |
| Noria | River current | up to ~20 m | Continuous |
| Saqiya | Animal gear | 5–10 m | Pot chain |
| Chain / rag-and-chain | Muscle / wheel | staged tens of m | Mines |
| Ctesibius force pump | Lever | high | Dual cylinder + flaps |
| Bucket + windlass | Human | any well | Slow |
| Hydraulic ram | Drive-pipe flow | ~10× fall height on ~1/10 of flow | No outside power |

### Hydraulic ram (water-timed)

1. Drive flow exits open waste valve and speeds up  
2. Waste valve slams → water hammer spike  
3. Spike drives check into air chamber  
4. Pressure falls → waste reopens → repeat (~30–90/min)

Efficiency ~60–80%. Air chamber smooths delivery. Timing is momentum + valve weight. Sibling tricks: intermittent siphon, tipping bucket, clepsydra orifice clocks, pilot diaphragms.

### Energy sources compared

| Source | Runtime | Output feel | Best use |
|---|---|---|---|
| Water head / flow | Continuous on site | Steady | Lift, automata, metering taps |
| Spring | Until unwind | Fades unless fusee | Portable timed dose / valve return (~100–300 J/kg steel) |
| Weight | Until drop | Constant | Clocks, slow drive (mass cheap) |
| Muscle | Until tired | Variable | General pumping |

### Valves inside pumps / taps

Flap (leather), ball check, poppet (+ spring), piston cup seals. Faucet bodies: bronze/brass. Seals: leather → rubber → ceramic disc.

| Need | Tap design |
|---|---|
| Cheap | Spigot / plug cock |
| Fine control | Compression (screw washer) |
| Public save water | Spring self-close or hydraulic metering |
| Timed, no electric | Metering piston bleed or pilot diaphragm |
| Tank fill | Float valve |
| Stable shower temp | Pressure-balance / thermostatic |
| Huge flow, light touch | Pilot-operated diaphragm |

**Pressure bands:** tank 5 m → ~0.5 bar; 20 m → ~2 bar; tower 30–50 m → 3–5 bar. Homes often ~2.8–5.5 bar. Snap-close springs → water hammer unless air chamber or slow-close.

### Caldris filter

Shadoof through force pump and gravity tanks fit the era. Hydraulic rams and float valves are invent-friendly without electricity. Magitech can replace the drive with mana stones but still obeys head and pipe strength. Pair copper/brass rules for wet lines.

## Open

- Mine dewatering staged layouts
- Exact ram sizing for a named river fall
