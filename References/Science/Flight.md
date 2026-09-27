# Flight

Hub: `Science.md`. Cast law: `ManaCast.md`. Kinetic lifts: `Kinetic.md`. Hands hold: `ManaCast.md`.

**Ruling:** no locked expensive or cheap flight. Cost is the power equation for the method in use, converted with η(L) and μ(INT).

## Static hold ≠ flight

Mana Hands **hold** rows (e.g. 80 kg → 78 J/s) are grip / restraint against gravity with a fixed attachment feel. They are **not** the cost of staying airborne in air.

## Actuator-disk hover (momentum theory)

P_ideal = (m g)^1.5 / √(2 ρ A)

- ρ ≈ 1.2 kg/m³
- A = effective downwash disk area (body-scale example ≈ 1 m²)

Real rotors / similar systems: figure of merit FM ≈ 0.6–0.8.  
P_real ≈ P_ideal / FM.

Example mass 80 kg, A = 1 m²:

| | Power |
|---|---|
| Ideal | ≈ 14,170 W |
| Realistic (FM ~0.67 → ~21 kW mid) | ≈ 18,000–24,000 W |

Mana/s = P / (10 × η × μ)

| Tier | J/mana | Mana/s at 14.17 kW | Mana/s at ~21 kW |
|---|---|---|---|
| INT 40, L2 (ημ → 21.9) | 21.9 | ≈ 647 | ≈ 959 |
| INT 500, L9 (ημ → 496) | 496 | ≈ 28.6 | ≈ 42.3 |

Larger A lowers power (scales 1/√A). Wing-shaped downwash beats a tight body hug on math alone.

Holding a mass still does zero net mechanical work against gravity in the abstract; hover cost is continuous momentum dumped into air. A **reactionless** or **ground-push** model would use a different equation (or near-zero continuous power). If that model is used, pay whatever that equation says. Do not mix it silently with actuator-disk numbers.

## Vacuum-pocket lift assist

Lift from pressure differential: F = ΔP × A.

To support 80 kg (785 N) on 1 m²: ΔP ≈ **785 Pa** (~0.77% of full vacuum).

Establish cost for pocket volume V: W ≈ ΔP × V (partial). Example V = 0.1 m³ → **~78.5 J** (~7.85 mana at ημ 1; ~3.6 mana at INT 40 L2). Ongoing cost is leak / maintenance rate, not full actuator-disk power, **if** the pocket stays sealed.

Living-target vacuum rules in `Vacuum.md` still apply when the pocket is cast on a person who can resist. Self-flight assist on the caster’s own sealed pocket is a different contest (own vitality cooperating).

### Method checklist

| Method | Pay |
|---|---|
| Actuator-disk hover | P_ideal or P_real continuous |
| Vacuum-pocket support | ΔP×V to establish + leak mana/s |
| Jet / thrust (Mana Jet) | KE and momentum dump per `Kinetic.md` / continuous F·v |
| Reactionless / ground-push | Separate equation if used; never mix silently with disk power |
