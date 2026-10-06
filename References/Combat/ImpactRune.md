# Impact Rune (Sahildr hammer)

Earth-physics model for Sahildr's **Lesser Impact** warhammer rune. Catalog: `../Runes/Runes.md`. Compression cousin: `../World/Science/Energy/Compression.md` (Fire Piston). Path law: `../Runes/Energy.md`. Unit: **1 mana ≈ 10 J** paid. Path metal: **steel** (mid conductivity feel).

## Rules that drive the math

From `../Runes/Energy.md` conversion layers:

```
Paid cost is fixed.
Useful (J) = mana × 10 × η_cond × A
A = √C   // ambient osmosis; Energy.md / ManaConcentration.md
```

This is a **rune** stroke. Use mana conductivity and ambient `A` only. Do **not** also multiply η(L) or μ(INT).

| Lock | Value |
|---|---|
| Full activate | **100 mana** |
| Input at peg | **1,000 J** |
| Worked example | η_cond = 1, A = 1 (open ground) → **1,000 J** Useful |

Steel in story is a **mid** conductor (worse than mythril, better than iron). When a chapter needs steel η_cond or site `A`, set η_cond from conductivity feel and `C` from altitude + dungeon/spiritual thickness, then `A = √C`.

That Useful **is** the energy the stroke adds to the head (ΔKE).

Sahildr has the strength of 5 men. The **640 J** baseline below is her swing. A street warhammer at AGI ~15 is **200–400 J** (`../Progression/Attributes.md`, `AttackScale.md`). That band is a different body.

## Model (locked)

The mass / velocity boost is **not** stored energy in a charged state.

Mana particles sit in a **compressed configuration**, like a Fire Piston holding air only while force is on the piston. That compression **is** the boosted mass and velocity. Feeding mana does the compressing. Stop feeding and nothing holds the dense state. The particles disperse almost at once. The weapon returns to baseline on about the **same timescale as the swing**, not a slow decay after.

**Hold** as a standing buff is unaffordable (dispersal is swing-fast).

## Activation sequence (working)

1. **Absorption** - draws from magic stone, stamina or mana. Source only.
2. **Mass increase** - head gains weight at activate. Head only, not haft.
3. **Velocity increase** - pushes along the existing swing and cancels the drag from the mass step.

Momentum scales as **a × b**. KE scales as **a × b²**. Velocity is the stronger damage lever. Peaks must meet at contact.

## Warhammer package (working)

| Spec | Value |
|---|---|
| Total mass | **30 kg** |
| Head mass (baseline, ~2/3) | **20 kg** |
| Baseline tip speed | **8 m/s** |
| Baseline KE | **½ × 20 × 8² = 640 J** |

### Worked example (η_cond = 1, A = 1)

```
KE₁ = KE₀ + Useful = 640 + 1,000 = 1,640 J
```

Equal split (story: mass and speed both step; set **a = b**):

```
a × b² = a³ = KE₁ / KE₀
a = b = (KE₁ / 640)^(1/3) ≈ 1.37
Δm = (a − 1) × 20 kg ≈ +7.4 kg
Δv = (b − 1) × 8 m/s ≈ +3.0 m/s
```

| Head mass | Tip speed | KE₁ check |
|---|---|---|
| **27.4 kg** | **11.0 m/s** | ½ × 27.4 × 11.0² ≈ **1,658 J** ≈ KE₁ |

Scale any other η_cond × A by multiplying Useful first, then rebuild a from `a = ((KE₀ + Useful) / KE₀)^(1/3)`.

**Duration:** peak lasts about the swing window **~0.2 s** (`AttackScale.md`), then dumps. More mana = stronger stroke in that window, not a longer buff.

Partial feed: Useful scales with mana paid.

## Open

- Steel η_cond and site `A` (`√C`) when a fight beat needs exact joules
