# Compression

Hub: `Science.md`. Cast law: `ManaCast.md`. Mana = J / (10 × η × μ). ημ = 1 figures are L2 INT 15 reference.

## Gases (isothermal)

W = P₁ V₁ ln(V₁ / V₂)

## Solids / dense elastic (bulk modulus B, strain ΔV/V)

E = ½ · B · (ΔV/V)² · V  
ΔV/V = √(2 E / (B · V))

Use **only** for elastic storage or crush. Hydrostatic squeeze does **not** forge or work-harden metal (von Mises is pressure-independent). Permanent shape / harden:

E ≈ σ_flow × ε_plastic × V

Example plastic: 400 MPa flow × 10% strain × 1 cm³ ≈ **40 J** (~4 mana at ημ 1). Roughly hundreds of times the elastic-only figure for the same volume.

### Worked elastic examples

Hammer-scale blow **50 J** into V = 10 cm³ = 10×10⁻⁶ m³:

| Material | B | ΔV/V | Notes |
|---|---|---|---|
| Soft dense (B = 2 GPa) | 2×10⁹ | √(100 / (2×10⁹×10×10⁻⁶)) ≈ **0.07** (7%) | Crush / store elastic |
| Hot steel (wrong soft B = 30 GPa) | do not use | — | Old soft-B myth |
| Hot or cold steel (real) | **100–130 GPa** | at 50 J / 10 cm³: ΔV/V ≈ **0.018–0.020** (~2%) | Elastic only |

Blacksmith swings often **20–80 J** per blow on hot stock; shaping cost is still **σ_flow × ε × V**, not the B formula.

### Hot steel

Bulk modulus stays high when hot: **B ≈ 100–130 GPa** (cold ~160 GPa, only ~30–40% drop). What collapses at forging heat is **flow stress** (roughly tenfold). Model “hot is easy to shape” as low σ_flow in the plastic equation, not soft B.

## Fire Piston (adiabatic compression ignition)

T₂ = T₁ × (V₁/V₂)^(γ−1), γ = 1.4 for air.

10:1 from 293 K → T₂ = 293 × 10^0.4 ≈ **736 K** (~463 °C), above cellulose char ignition (~300–400 °C). Flameless ignition of tinder, lamp oil or a powder / fuel store at range with no visible spark.

Adiabatic work: W = P₁ V₁ / (γ−1) × [(V₁/V₂)^(γ−1) − 1]

For 1 L, 10:1: W = 101325×0.001/0.4 × (10^0.4 − 1) ≈ **383 J** (~38 mana at ημ 1).

**Apps:** camp tinder, lamp light, sabotage powder stores, silent ignition where Ember’s open heat would show.

Ember (`ManaCast.md`) pays heat **at the fuel**. Fire Piston pays **compression work** on a gas pocket. Different paths; pick by scene. Impact rune stroke / hold (compressed mana particles, same “only under force” spirit): `ImpactRune.md`.

## Frost Breath (adiabatic expansion cooling)

Mirror of Fire Piston: pre-compress, then expand.

T₂ = T₁ × (P₂/P₁)^((γ−1)/γ)

From 10× atm back to 1× at 293 K: ideal T₂ ≈ **117 K**. Practical with losses closer to **−50 to −80 °C**. Enough to flash-freeze a lock, hinge, bowstring or thin ice bridge. Setup cost mirrors Fire Piston (~383 J for the 1 L / 10× case). Same compression school, heat and cold.

## Pressure purification (HPP-style)

E/V ≈ P² / (2 B), B ≈ 2.2 GPa for water.

At 500 MPa: E/V = (5×10⁸)² / (2×2.2×10⁹) ≈ **56.8 J/L** → ~57 J for 1 L (~5.7 mana at ημ 1). Sterilize wound irrigation, ration pack or flask without cooking. Distinct from freeze-dry / vacuum preservation (`Vacuum.md`).

## Air cartridge (compressed-gas storage)

Isothermal fill: W = P₁ V₁ ln(P₂ / P₁)

1 L to 200 bar (2×10⁷ Pa) from 1 atm: W = 101325×0.001×ln(200) ≈ **537 J** (~54 mana at ημ 1). Pre-charge in downtime; later discharge as air-bolt, door-ram or jump jet with no cast time in the moment. Overfill / puncture is its own hazard.
