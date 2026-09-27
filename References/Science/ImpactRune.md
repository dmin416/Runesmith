# Impact Rune (Sahildr hammer)

Earth-physics model for Sahildr’s **Lesser Impact** warhammer rune. Catalog: `../Runes/Runes.md`. Compression cousin: `Compression.md` (Fire Piston). Path law: `../Runes/Energy.md`. Unit: **1 mana ≈ 10 J** paid. Path metal: **steel**.

## Rules that drive the math (locked)

From `Energy.md` / ManaCast conversion layers:

```
Paid cost is fixed.
Useful (J) = mana × 10 × η_path × G
```

This is a **rune** stroke. Use path η and ambient G only. Do **not** also multiply η(L) or μ(INT).

| Lock | Value |
|---|---|
| Full activate | **100 mana** |
| Steel η | **0.85** |
| Input | **1,000 J** |
| Useful | **850 × G** J |

| Ambient G | Useful from 100 mana |
|---|---|
| 1 (sealed) | **850 J** |
| 1.5 (indoors) | **1,275 J** |
| 3 (open air) | **2,550 J** |

That Useful **is** the energy the stroke adds to the head (ΔKE). Ambient sets how hard the same 100 mana hits. Nothing “fails” the cost rule.

## Model (locked)

The mass / velocity boost is **not** stored energy in a charged state.

Mana particles sit in a **compressed configuration**, like a Fire Piston holding air only while force is on the piston. That compression **is** the boosted mass and velocity. Feeding mana does the compressing. Stop feeding and nothing holds the dense state. The particles disperse almost at once. The weapon returns to baseline on about the **same timescale as the swing**, not a slow decay after.

**Hold** as a standing buff is unaffordable (dispersal is swing-fast).

## Activation sequence (working)

1. **Absorption** – draws from magic stone, stamina or mana. Source only.
2. **Mass increase** – head gains weight at activate. Head only, not haft.
3. **Velocity increase** – pushes along the existing swing and cancels the drag from the mass step.

Momentum scales as **a × b**. KE scales as **a × b²**. Velocity is the stronger damage lever. Peaks must meet at contact.

## Warhammer package (working)

| Spec | Value |
|---|---|
| Total mass | **30 kg** |
| Head mass (baseline, ~2/3) | **20 kg** |
| Baseline tip speed | **8 m/s** |
| Baseline KE | **½ × 20 × 8² = 640 J** |

### What 100 mana does (math from the rules)

```
KE₁ = KE₀ + Useful = 640 + 850 × G
```

Equal split (story: mass and speed both step; set **a = b**):

```
a × b² = a³ = KE₁ / KE₀
a = b = (KE₁ / 640)^(1/3)
Δm = (a − 1) × 20 kg
Δv = (b − 1) × 8 m/s
```

| Ambient G | Useful (ΔKE) | KE₁ | a = b | Head mass | Tip speed | Δm | Δv |
|---|---|---|---|---|---|---|---|
| 1 | **850 J** | 1,490 J | **1.33** | **26.5 kg** | **10.6 m/s** | **+6.5 kg** | **+2.6 m/s** |
| 1.5 | **1,275 J** | 1,915 J | **1.44** | **28.8 kg** | **11.5 m/s** | **+8.8 kg** | **+3.5 m/s** |
| 3 | **2,550 J** | 3,190 J | **1.71** | **34.2 kg** | **13.7 m/s** | **+14.2 kg** | **+5.7 m/s** |

Checks (G 1.5 example): ½ × 28.8 × 11.5² ≈ **1,905 J** ≈ KE₁. Momentum 28.8 × 11.5 ≈ **331 kg·m/s** vs baseline 20 × 8 = **160** (~2.1×).

### Per mana (linear in Useful; equal split follows from full stroke)

| Ambient G | Useful / mana | Δm / mana | Δv / mana |
|---|---|---|---|
| 1 | **8.5 J** | **+65 g** | **+0.026 m/s** |
| 1.5 | **12.75 J** | **+88 g** | **+0.035 m/s** |
| 3 | **25.5 J** | **+142 g** | **+0.057 m/s** |

**Duration:** peak lasts about the swing window **~0.2 s** (`../Combat/AttackScale.md`), then dumps. More mana = stronger stroke in that window, not a longer buff.

Partial feed: Useful scales with mana paid. Rebuild **a** from `a = ((KE₀ + Useful) / KE₀)^(1/3)` with the same equal-split rule.

## Skull crush locks

| Target | Crush energy into bone |
|---|---|
| Pig | **200 J** |
| Boar | **250 J** |
| Monster boar | **500–1,000 J** (2×–4× boar; mid **750 J**) |

Unaided **640 J** already clears pig / boar and sits in the monster band on a clean hit. Rune strokes above add margin / pulp / bad-angle insurance.

Draft pulp color (~2,500–3,000 J): open-air full stroke (**KE₁ ≈ 3,190 J**) reaches it. Sealed / indoor full strokes do not need to; they still crush.

## Story fit

- Sahildr must **time** the activate with the swing (Ch 13 Wereboar; Ch 14 watcher finish; Ch 18 weight-on-activate talk).
- Poor as a solo scroll (`Runes.md`).
- On-page “mass or gravity” can stay Roland’s guess. Rewrite model is compressed mana particles.

## Open

- Which ambient **G** Carwen floors use when she one-shots (biome open vs corridor).
- Which monster rung (2× / 3× / 4×) Spiked Boar vs Wereboar use.
- Equal **a = b** split vs a different locked split (still one Useful budget).
- STR / AGI on Sahildr’s sheet vs swinging **30 kg** at **8 m/s**.
