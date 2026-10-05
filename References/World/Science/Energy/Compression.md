# Compression

Gas and solid compression math for Fire Piston, Frost Breath, air cartridges, micro-pierce and cloak cooling. Cloak cycle: `CloakAirCooling.md`. Cast: `../../../Runes/Energy.md` (`Mana = J / (10 × η × μ)`). ημ = 1 figures are L2 INT 15 reference.

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

Same law, expand instead. 10:1 from 293 K → **~117 K** ideal; practical **−50 to −80 °C**. Freeze lock, hinge, string, thin ice. Setup mirrors Fire Piston (~383 J for 1 L / 10×). Personal sphere path: `CloakAirCooling.md`.

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

## Open

- CraftMetal barrier molds

Compressed-mana stroke cousin (Sahildr hammer): `../../../Combat/ImpactRune.md`.
