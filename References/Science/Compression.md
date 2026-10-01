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

Mirror of Fire Piston: pre-compress, then expand. Same volume-ratio law; expand instead of compress.

T₂ = T₁ × (V₁/V₂)^(γ−1), γ = 1.4 for air.

10:1 expansion from 293 K → T₂ = 293 × 10^(−0.4) ≈ **117 K**. Practical with losses closer to **−50 to −80 °C**. Enough to flash-freeze a lock, hinge, bowstring or thin ice bridge. Setup cost mirrors Fire Piston (~383 J for the 1 L / 10× case). Same compression school, heat and cold.

Personal cloak cooling with a held compressed sphere (Roland experiments then drops for a cold rune): `CloakAirCooling.md`.

## Pressure purification (HPP-style)

E/V ≈ P² / (2 B), B ≈ 2.2 GPa for water.

At 500 MPa: E/V = (5×10⁸)² / (2×2.2×10⁹) ≈ **5.68×10⁷ J/m³** = **56.8 kJ/L** → ~56,800 J for 1 L (~5,680 mana at ημ 1; ~2,590 mana at INT 40 L2). On the order of a Walnut stone's full capacity. Sterilize wound irrigation, ration pack or flask without cooking. Distinct from freeze-dry / vacuum preservation (`Vacuum.md`).

## Air cartridge (compressed-gas storage)

Isothermal fill: W = P₁ V₁ ln(P₂ / P₁)

1 L to 200 bar (2×10⁷ Pa) from 1 atm: W = 101325×0.001×ln(200) ≈ **537 J** (~54 mana at ημ 1). Pre-charge in downtime; later discharge as air-bolt, door-ram or jump jet with no cast time in the moment. Overfill / puncture is its own hazard.

## Micro-compression

Elastic proxy: E = ½ B (ΔV/V)² V. Prefer plastic pierce for real penetration: E ≈ σ_flow × ε × V.

### Worked elastic proxy (steel B ≈ 160 GPa, ΔV/V ≈ 0.05)

| Target volume | V | E | ≈ mana at ημ 1 |
|---|---|---|---|
| Plate patch 10×10 cm × 2 mm | 20 cm³ = 2×10⁻⁵ m³ | ½×160e9×0.0025×2e−5 = **4,000 J** | ~400 |
| Tip 2×2×2 mm | 8×10⁻⁹ m³ | **1.6 J** | ~0.16 |

~**2,500×** cheaper for the same fractional strain by shrinking V. Matches “exceed strength locally” logic.

### Where it applies

- **Mundane objects / unwarded materials:** pay the equation. Gem cleave along a plane, engrave, crack a lock tumbler pin, wax seal, mortar joint, rope fiber, wood grain.
- **Living or mana-armored targets:** vitality / magic resistance blocks raw micro-compression as a free kill or armor-splitter (`Science.md` hub). Soft-tissue paths only when resistance does not apply (helpless / no contest), same exception spirit as vacuum-in-armor.
- **Medical (unresisting tissue / patient):** focused collapse of a stone or blockage as a compression cousin to Stone-Breaker; decide contact vs short standoff explicitly (compression has no automatic 1000× air–tissue loss, but living resistance may still apply in combat).
- **Arrow tips:** hardness gate H ≥ 1.5 R (`ManaCast.md`) stays for shaped projectiles. Do not replace tip hardness with micro-compression on the same shot without calling it a different technique.

## Compression-forged edges (craft downtime)

Cold work piles dislocations; yield can rise ~**20–50%** before anneal is needed. Repeated low-strain passes on an edge strip:

Example elastic proxy: 5 cm edge, 1×1 mm section (V = 5×10⁻⁸ m³), B = 160 GPa, ΔV/V = 0.01 per pass → E = ½×160e9×0.0001×5e−8 = **0.4 J** (~0.04 mana at ημ 1). Prefer σ_flow × ε × V for plastic work-hardening accounting.

Many passes; overwork without anneal → microcrack / brittle edge. Patience and judgment are the cost. Success raises lasting hardness / effective R for later pierce tables. Companion metallurgy: `CraftMetal.md`.
