# Attack Scale

Order-of-magnitude map for physical hits and mana barriers. Cast law: `../Runes/Energy.md`. Attributes: `../Progression/Progression.md`. Tip hardness / spell punch tables: `../World/Science/Energy/ManaCast.md`. Mage Hands timing: `MageDefense.md`.

## Street baseline

Untrained adult **STR 15 / AGI 15**.

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
| **120** | 3,000 W | 17.0 m/s | 42.4 m/s | Early–mid T2 (Ch 14 watcher lock) |
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
| **120** | **~720 J** | **~2.9 kJ** | **~4.5 kJ** |
| **200** | **~1.2 kJ** | **~4.8 kJ** | **~7.5 kJ** |

At `m_eff = 1.2 kg` and `k = 2–2.5`, AGI **120** tip KE sits **~4.3–6.7 kJ**; AGI **200** sits **~7–11 kJ**.

**Table weapons at street stats:** rapier thrust **30–60 J**, sword cut **60–130 J**, warhammer **200–400 J**. Those are **AGI ~15** anchors. Do **not** paste them onto a high-AGI T2 without scaling.

Rough scale of table thrust to high AGI: multiply by **AGI/15** if you only need a quick check (same √S speed → linear KE in AGI). Prefer the tip-KE formula for specialists.

## Mana Shield absorb pool

Direct-cast barrier. Same ambient term as spell Useful (`Energy.md`).

```
Pool (J) = 20 × M × η(L) × μ(INT) × S × R × A
N        = floor(Pool / J_threat)    # whole attacks; N = 0 → pierces
A        = √C                        # ambient; open ground A = 1
```

- Baseline cast **M = 100** mana. Overcharge = mana spent.
- `η(1)=0.3`; `η(L)=1+(L-2)×2/7` for L2–L9
- `μ=(INT/15)^0.8`
- **Focused disk:** area = 0.2 m² → **S = 1**, R = 1
- **Bubble / semicircle:** area ≈ 6.28 m² → **S ≈ 0.178** (much weaker per mana)
- Tables below are open-ground **A = 1**. Thicker fields multiply the pool by `A`.

### Roland Ch 14 rewrite (Shield L6, INT 137)

`η(6) ≈ 2.14`, `μ(137) ≈ 5.87`, open ground **A = 1**

| M (mana) | Focused disk | Bubble (S=0.178) |
|---|---|---|
| 100 | ~**25 kJ** | ~**4.5 kJ** |
| 150 | ~**38 kJ** | ~**6.7 kJ** |
| 200 | ~**50 kJ** | ~**9.0 kJ** |

**Shape matters more than a small overcharge.** Same cast as a hard disk can stop what a body bubble cannot.

### Profile pools (focused disk, M=100)

| Profile | INT | L | Pool |
|---|---|---|---|
| Novice | 15 | 1 | ~0.6 kJ |
| Apprentice | 40 | 2 | ~4.4 kJ |
| Journeyman | 73 | 3 | ~9.1 kJ |
| Adept | 100 | 5 | ~17 kJ |
| Master | 200 | 7 | ~39 kJ |

## Threat ladder

Ch 14 watcher Gale tip (AGI **120**, `k≈2–2.5`, `m_eff` 0.8–1.2) sits about **~3–7 kJ** before tip detonation.

| Threat | J | vs street | vs AGI 120 Gale tip |
|---|---|---|---|
| Rapier thrust (street) | 30–60 | baseline thrust | irrelevant |
| Longbow arrow | 100 | — | — |
| Warhammer / greatsword | 200–400 | heavy melee | well below Gale tip |
| Volley, 10 warbow | 1,250 | — | below Gale tip |

Bow / compound / Strength draw dial: `Bows.md` (STR 15 compound ~97 J).
| Ogre club | 3,400 | — | ≈ soft / mid Gale tip |
| Ballista bolt | 6,000 | — | ≈ hard / top Gale tip |
| Horse + rider canter | 19,000 | — | full body KE (above tip) |
| Dragon claw | 35,000 | — | — |
| Trebuchet stone | 90,000 | — | — |

Weapon rune blasts (e.g. detonation tip) sit on top of kinetic tip KE when the tip is lit. Rune Useful uses η_cond × A (`A = √C`; `../Runes/Energy.md`), not μ(INT).

## Worked lock: Ch 14 watcher vs Reyna shield

**Levels:** watcher / T2 fencer overall **L55** (T1 **25** + ~**30** into T2). Becky / Sahildr / Reyna overall **~45** (second T1 deep, e.g. **25+~20**). Roland Mage **L25**. Sahildr's "just advanced" line is trash talk; he is not a fresh T2.

**Roland:** Mage L25 rewrite, INT **137**, Mana Shield **L6**. Casts a **bubble** on Reyna, screams / overcharges → treat **M ≈ 150–200**. Bubble pool **~6.7–9.0 kJ**.

**Watcher:** Tier 2 physical, speed + penetration specialist. Working sheet for scale: **STR 120 / AGI 120** + **Gale Step** (+ orange detonation tip). Early–mid T2 for overall **L55**, not hard-T2 ceiling stats.

| Attack model | Energy into bubble |
|---|---|
| Street rapier only | 30–60 J (never pierces) |
| AGI 120 base lunge | ~0.7–1.1 kJ |
| AGI 120 + Gale Step (`k≈2–2.5`) | **~3–7 kJ** |
| + tip detonation | higher still (blasts through after the tip holds) |

**On-page result:** bubble holds a moment, tip bends then **blasts through** with explosion; Reyna's dagger cannot fully fend → shoulder graze. Gale tip KE sits under or at the bubble's low end; tip detonation finishes the pierce. A **focused disk** at the same mana (**~25–50 kJ**) would stop that thrust.

Do not re-litigate this beat with street weapon table numbers.

## Spell Useful energy

```
Useful (J) = mana × 10 × η(L) × μ(INT) × A
A          = √C                    # ambient; open ground A = 1
```

Voice sets mana (Bolt normal **25**, Arrow **2×** Bolt). Overcharge = mana used. Street / early-arc tables at **A = 1**. Hardness gates for tips: `../World/Science/Energy/ManaCast.md`. Healing potions close flesh; they are not joule weapons (`../Items/Items.md`).

## Quick checks

1. **Who is hitting?** If STR/AGI ≫ 15, scale tip KE; do not use the street weapon row raw.
2. **What shape is the shield?** Disk vs bubble can be a **5–6×** pool gap.
3. **Is a skill multiplying speed?** `k` on tip speed squares into KE.
4. **N = 0** means pierce. **N ≥ 1** means that whole attack is eaten (then the pool drops for the next).

## Locked keep

Street STR/AGI 15 baseline. Tip KE from effective mass and tip speed. Speed skills raise tip speed factor k (KE scales with k²). Shield pools in joules; focused disk ≫ bubble per mana; both shield and spell Useful × ambient `A`. Ch 14 bubble vs Gale tip lock above (open ground). Hardness tables live in ManaCast.

## Open

Late raid math beyond the ladder stays unset until a fight beat needs a hard number.
