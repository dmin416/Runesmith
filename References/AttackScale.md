# Attack Scale

Joule ladder for physical hits and mana barriers. Use this when a fight beat asks “does the shield hold?” or “how hard is that thrust?” Full formulas live in `Science.md` and `Progression.md`. This file is the **order-of-magnitude map** plus worked locks.

**Street baseline:** untrained adult **STR 15 / AGI 15**.

---

## Physical output (STR / AGI)

From `Progression.md` / `Science.md`:

```
P        = 25 × AGI                         W
v_sprint = 6 × √(AGI / 15)                  m/s
v_s      = 15 × √(AGI / 15)                 m/s   (arm / kinetic-chain tip)
E_window = P × Δt                           J     (Δt ≈ 0.2 s throw; longer for a committed lunge)
deadlift = 6 × STR                          kg
```

Equal-mass body KE at sprint: `½ × m × v_sprint²` (≈ **80 kg** adult). A weapon tip does **not** deliver full body KE. Tip delivery uses effective striking mass (blade + arm share, often **~0.4–1.2 kg**) at tip speed.

### AGI landmarks

| AGI | Power | Sprint | Arm-chain tip `v_s` | Notes |
|---|---|---|---|---|
| **15** | 375 W | 6.0 m/s | 15 m/s | Street man |
| **40** | 1,000 W | 9.8 m/s | 24.5 m/s | Serious athlete band |
| **48** | 1,200 W | 10.7 m/s | 26.8 m/s | Bolt-class power |
| **100** | 2,500 W | 15.5 m/s | 38.7 m/s | High T1 / soft T2 |
| **200** | 5,000 W | 21.9 m/s | 54.8 m/s | Hard T2 physical specialist |

### Tip KE estimate

```
KE_tip ≈ ½ × m_eff × (k × v_s)²
```

- `m_eff`: **0.4–1.2 kg** (light thrust → heavy cut / lunge share)
- `k`: **1.0** base committed strike; **1.5–2.5+** with a speed skill (e.g. Gale Step)

| AGI | Base tip (`k=1`, m=0.8 kg) | Gale-like `k=2` | Gale-like `k=2.5` |
|---|---|---|---|
| 15 | ~90 J | ~360 J | ~560 J |
| 40 | ~240 J | ~960 J | ~1.5 kJ |
| 100 | ~600 J | ~2.4 kJ | ~3.7 kJ |
| **200** | **~1.2 kJ** | **~4.8 kJ** | **~7.5 kJ** |

At `m_eff = 1.2 kg` and `k = 2–2.5`, AGI **200** tip KE sits **~7–11 kJ**.

**Table weapons at street stats** (Science human list): rapier thrust **30–60 J**, sword cut **60–130 J**, warhammer **200–400 J**. Those are **AGI ~15** anchors. Do **not** paste them onto a STR/AGI 200 T2 without scaling.

Rough scale of table thrust to high AGI: multiply by **AGI/15** if you only need a quick check (same √S speed → linear KE in AGI). Prefer the tip-KE formula for specialists.

---

## Mana Shield absorb pool

```
Pool (J) = 20 × M × η(L) × μ(INT) × S × R
N        = floor(Pool / J_threat)    # whole attacks; N = 0 → pierces
```

- Baseline cast **M = 100** mana. Overcharge = mana spent.
- `η(1)=0.3`; `η(L)=1+(L-2)×2/7` for L2–L9
- `μ=(INT/15)^0.8`
- **Focused disk:** A = 0.2 m² → **S = 1**, R = 1
- **Bubble / semicircle:** A ≈ 6.28 m² → **S ≈ 0.178** (much weaker per mana)

### Roland Ch 14 rewrite (Shield L6, INT 137)

`η(6) ≈ 2.14`, `μ(137) ≈ 5.87`

| M (mana) | Focused disk | Bubble (S=0.178) |
|---|---|---|
| 100 | ~**25 kJ** | ~**4.5 kJ** |
| 150 | ~**38 kJ** | ~**6.7 kJ** |
| 200 | ~**50 kJ** | ~**9.0 kJ** |

**Shape matters more than a small overcharge.** Same cast as a hard disk can stop what a body bubble cannot.

### Profile pools (focused disk, M=100) for orientation

| Profile | INT | L | Pool |
|---|---|---|---|
| Novice | 15 | 1 | ~0.6 kJ |
| Apprentice | 40 | 2 | ~4.4 kJ |
| Journeyman | 73 | 3 | ~9.1 kJ |
| Adept | 100 | 5 | ~17 kJ |
| Master | 200 | 7 | ~39 kJ |

---

## Threat ladder (Science)

| Threat | J | vs street | vs AGI 200 Gale tip |
|---|---|---|---|
| Rapier thrust (street) | 30–60 | baseline thrust | irrelevant |
| Longbow arrow | 100 | — | — |
| Warhammer / greatsword | 200–400 | heavy melee | soft vs T2 tip |
| Volley, 10 warbow | 1,250 | — | — |
| Ogre club | 3,400 | — | soft Gale tip band |
| Ballista bolt | 6,000 | — | hard Gale tip band |
| Horse + rider canter | 19,000 | — | full body KE band |
| Dragon claw | 35,000 | — | — |
| Trebuchet stone | 90,000 | — | — |

Weapon rune blasts (e.g. detonation tip ~**100 MP** activation) sit on top of kinetic tip KE when the tip is lit.

---

## Worked lock: Ch 14 watcher vs Reyna shield

**Levels:** watcher / T2 fencer overall **L55** (T1 **25** + ~**30** into T2). Becky / Sahildr / Reyna overall **~45** (second T1 deep, e.g. **25+~20**). Roland Mage **L25**. Sahildr’s “just advanced” line is trash talk; he is not a fresh T2.

**Roland:** Mage L25 rewrite, INT **137**, Mana Shield **L6**. Casts a **bubble** on Reyna, screams / overcharges → treat **M ≈ 150–200**. Bubble pool **~6.7–9.0 kJ**.

**Watcher:** Tier 2 physical, speed + penetration specialist. Working sheet for scale: **STR 200 / AGI 200** + **Gale Step** (+ orange detonation tip).

| Attack model | Energy into bubble |
|---|---|
| Street rapier only | 30–60 J (never pierces) |
| AGI 200 base lunge | ~1–2 kJ |
| AGI 200 + Gale Step (`k≈2–2.5`) | **~5–11 kJ** |
| + tip detonation | higher still |

**On-page result:** bubble holds a moment, tip bends then **blasts through** with explosion; Reyna’s dagger cannot fully fend → shoulder graze. Matches hard Gale Step tip KE overlapping the overcharged bubble. A **focused disk** at the same mana (**~25–50 kJ**) would stop that thrust.

Do not re-litigate this beat with street weapon table numbers.

---

## Spell attack scale (pointer)

Mana Bolt / Arrow useful energy:

```
Useful (J) = mana × 10 × η(L) × μ(INT)
```

Voice sets mana (Bolt normal **25**, Arrow **2×** Bolt). Overcharge = mana used. Hardness gates for tips: `Science.md`. Healing potions close flesh; they are not joule weapons (`Items.md`).

---

## Quick checks

1. **Who is hitting?** If STR/AGI ≫ 15, scale tip KE; do not use the street weapon row raw.
2. **What shape is the shield?** Disk vs bubble can be a **5–6×** pool gap.
3. **Is a skill multiplying speed?** `k` on tip speed squares into KE.
4. **N = 0** means pierce. **N ≥ 1** means that whole attack is eaten (then the pool drops for the next).
