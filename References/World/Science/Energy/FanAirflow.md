# Fan Airflow

Order-of-magnitude fan sizing for bellows, hoods, cloak blowers and magitech air movers. Air density at room temp: **ρ ≈ 1.2 kg/m³**. Mana paying shaft work: `../../../Runes/Energy.md`, `ManaCast.md`.

## Narrative

Pick diameter and RPM, read tip speed, then flow and pressure from dimensionless coefficients. Real airflow is where the fan curve meets duct resistance, not the free design point alone.

## Detail

### Design-point chain

```
u = π × D × N / 60

Q = φ × (π/4 × D²) × u

Δp = ψ × ρ × u²

P_air      = Q × Δp
P_shaft    = Q × Δp / η_fan
P_drive    = Q × Δp / (η_fan × η_drive)
```

| Symbol | Meaning | Unit |
|---|---|---|
| D | Wheel diameter | m |
| N | Speed | RPM |
| u | Tip speed | m/s |
| Q | Volume flow | m³/s (×2119 → CFM) |
| Δp | Pressure rise | Pa (÷249 → in. water) |
| φ | Flow coefficient | - |
| ψ | Pressure coefficient | - |
| η_fan | Fan efficiency | - |
| η_drive | Motor / turbine / mana-engine efficiency | - |

Imperial shortcut:

```
P_drive (W) ≈ CFM × (in. water) × 0.1175 / (η_fan × η_drive)
```

### Coefficient bands

| Fan type | φ | ψ | η_fan |
|---|---|---|---|
| Axial (propeller) | 0.15–0.35 | 0.05–0.15 | 0.50–0.75 |
| Vane-axial (stator) | 0.20–0.40 | 0.15–0.35 | 0.70–0.85 |
| Forward-curved centrifugal | 0.40–0.80 | 0.50–0.80 | 0.50–0.65 |
| Backward-curved / airfoil centrifugal | 0.10–0.25 | 0.40–0.55 | 0.75–0.88 |
| Radial-blade centrifugal | 0.05–0.15 | 0.50–0.60 | 0.55–0.70 |

| Drive | η_drive |
|---|---|
| Cheap shaded-pole electric | 0.20–0.30 |
| PSC induction | 0.50–0.65 |
| EC / brushless | 0.75–0.90 |
| Premium 3-phase | 0.88–0.95 |
| Magitech / mana shaft (planning) | use ημ path; do not assume free air |

### Same-geometry scaling

```
Q  ∝ N × D³
Δp ∝ N² × D²
P  ∝ N³ × D⁵
```

| Change | Q | Δp | P |
|---|---|---|---|
| 2× RPM | 2× | 4× | 8× |
| 2× diameter | 8× | 4× | 32× |

Double the wheel and power explodes. Prefer more RPM or a better φ/ψ type before growing D.

### Operating point (duct wins)

Design formulas are capability at a chosen coefficient point. Installed flow is the intersection with system resistance:

```
Δp_system = k × Q²
```

Higher `k` (long duct, elbows, small ID, filters) → less Q at the same N. Lower resistance → more air for the same energy.

### Worked check (12 in backward-curved, 1750 RPM, EC)

D = 0.3048 m, φ = 0.20, ψ = 0.50, η_fan = 0.80, η_drive = 0.85

```
u  ≈ 27.9 m/s
Q  ≈ 0.408 m³/s  (≈ 864 CFM)
Δp ≈ 468 Pa      (≈ 1.88 in. water)
P_air ≈ 191 W → P_shaft ≈ 238 W → P_drive ≈ 281 W
```

### Caldris filter

Hand bellows and forge blowers are axial / radial craft. Magitech can hit centrifugal bands if the shop can cut a balanced wheel and spin it. Personal cooling may skip fans for a cold rune (Old cloak-compress note) when pool cost of continuous shaft work is ugly.

## Open

- Pull CloakAirCooling into this folder or Science when personal cooling returns
- Pump counterpart: MostRecentNotes `pump-technology.md`
