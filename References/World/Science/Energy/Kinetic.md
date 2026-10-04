# Kinetic

Hub: `../Science.md`. Cast law: `ManaCast.md`.

Potential apps under Manipulate Mana / Mana Hands / thrust. Mana from Useful joules:

`Mana = J / (10 × η(L) × μ(INT))`  
`Mana/s = P / (10 × η(L) × μ(INT))`

Raw examples below quote **J** and **J/10** as the ημ = 1 reference (L2, INT 15). Real cast cost divides by ημ.

## Equations

- KE = ½ m v²
- With path losses: E_total = ½ m v² + F_drag · d + F_friction · d (+ m g h for lifts)
- Constant force: E = F · d
- Force from accel: F = m (v / t)
- Momentum: p = m v
- Lift + launch: E = m g h + ½ m v²

## Worked reference (ημ = 1)

| Action | J | ≈ mana at ημ 1 |
|---|---|---|
| 20 g arrow to 60 m/s | 36 | 3.6 |
| 50 kg lift 1 m | 491 | 49 |
| 50 kg to 10 m/s (KE only) | 2,500 | 250 |
| 50 kg to 20 m/s | 10,000 | 1,000 |
| 100 kg lift 1 m | 981 | 98 |
| 100 kg to 10 m/s | 5,000 | 500 |
| 100 kg to 20 m/s | 20,000 | 2,000 |

Delivered over 1 s, those mana figures are also mana/s at ημ = 1.

At INT 40 L2 (21.9 J/mana): divide J by 21.9. Example: 50 kg to 10 m/s → 2500/21.9 ≈ **114 mana** (or mana/s if over 1 s).

Static **hold** drain for a gripped mass stays on the Mana Hands table in `ManaCast.md` (proposed J/s). Airborne sustain is `Flight.md`, not the hold row.

### Apps

Lifts, throws, pulls, bellows, well buckets, portcullis and cart work (Hands energy table in `ManaCast.md`). Dash / jump bursts as short KE dumps. Combined lift+launch for vaulting a body or crate: pay m g h + ½ m v².
