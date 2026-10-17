# Attack Scale

Order-of-magnitude map for physical hits and mana barriers. Cast law: `../Runes/Energy.md`. Attributes: `../Progression/Progression.md`. Tip hardness / spell punch tables: `../World/Science/Energy/ManaCast.md`. Mana Shield master (grip, hold drain, threat tables): `../World/Science/Energy/ManaShield.md`. Mage Hands timing: `MageDefense.md`. Earth martial strike-force lab ceilings: `PanzerKunstFishmanKarate.md`.

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

Direct-cast barrier. Same ambient term as spell Useful (`../Runes/Energy.md`). Full threat / weather / space tables: `../World/Science/Energy/ManaShield.md`.

```
Pool (J)     = 10 × M × η(L) × μ(INT) × S × R × A     # head-on
Hit taken    = J_threat × sin²(θ)
Grip G(v)    = 0.2 + 0.8 × v²/(v² + 40²)              # mundane matter
             = 1.0                                      # skills and spells (mana meets mana)
Pool spent   = Hit taken ÷ G                            # stopped hit
N            = floor(Pool / (Hit taken ÷ G))            # whole attacks; N = 0 → pierces
A            = √C                                       # ambient; open ground A = 1
S            = min(1, √(0.2 / area))                    # area = shield face, m²
```

- Baseline cast **M = 100** mana. Street overcharge soft cap **~2×** (scream band **150–200**). Higher is rare, not free.
- `η(1)=0.3`; `η(L)=1+(L-2)×2/7` for L2–L9. `μ=(INT/15)^0.8`
- **Focused disk:** area = 0.2 m² → **S = 1**. Settles at **45°** by default (Hit taken = half of head-on J). Disks have no area bleed.
- **Bubble / 1 m hemisphere:** area ≈ 6.28 m² → **S ≈ 0.178**. Full sphere (airborne / underwater) ≈ 12.57 m² → **S ≈ 0.126**.
- **Bubble bleed:** 0.1% of starting pool per second per 6.28 m². **Hold drain:** 0.3 J/s per newton of steady force (weight, wind, water, slow press).
- **Failed shield:** collapses; the attack passes at full energy. **Stopped hit:** spends pool as above.
- **Momentum:** held shield passes shove to the caster; anchored into ground passes it to the earth.
- **Selectivity (default unsealed):** air / gas / smoke / radiant heat pass; condensed matter and water blocked. Sealing blocks gas and pays full wind / water push as hold drain.
- **Give (for g / knockback feel):** disk ~0.05 m, bubble ~0.15 m.
- Tables below are open-ground **A = 1**. Mana paid is unchanged with altitude; thicker ambient raises **output** (pool) via `A`.

### Roland Ch 14 rewrite (Shield L6, INT 137)

`η(6) ≈ 2.14`, `μ(137) ≈ 5.87`, open ground **A = 1**. Head-on pool. Default disk at 45° stops twice as much head-on threat energy as the head-on pool number.

| M (mana) | Disk head-on | Disk vs threat at 45° | Bubble head-on |
|---|---|---|---|
| 100 | ~**12.6 kJ** | ~**25 kJ** of head-on J | ~**2.2 kJ** |
| 150 | ~**18.9 kJ** | ~**38 kJ** | ~**3.4 kJ** |
| 200 | ~**25.1 kJ** | ~**50 kJ** | ~**4.5 kJ** |

**Shape matters more than a small overcharge.** Same cast as a hard disk can stop what a body bubble cannot.

### Profile pools (focused disk, M=100, head-on)

| Profile | INT | L | Pool head-on | Vs threat at 45° |
|---|---|---|---|---|
| Novice | 15 | 1 | ~0.3 kJ | ~0.6 kJ |
| Apprentice | 40 | 2 | ~2.2 kJ | ~4.4 kJ |
| Journeyman | 73 | 3 | ~4.6 kJ | ~9.1 kJ |
| Adept | 100 | 5 | ~8.5 kJ | ~17 kJ |
| Master | 200 | 7 | ~19.3 kJ | ~39 kJ |

## Threat ladder

Ch 14 watcher Gale tip (AGI **120**, `k≈2–2.5`, `m_eff` 0.8–1.2) sits about **~3–7 kJ** before tip detonation. Skill tip uses **G = 1**.

| Threat | J | vs street | vs AGI 120 Gale tip |
|---|---|---|---|
| Rapier thrust (street) | 30–60 | baseline thrust | irrelevant |
| Longbow arrow | 100 | - | - |
| Warhammer / greatsword | 200–400 | heavy melee | well below Gale tip |
| Volley, 10 warbow | 1,250 | - | below Gale tip |
| Ogre club | 3,400 | - | ≈ soft / mid Gale tip |
| Ballista bolt | 6,000 | - | ≈ hard / top Gale tip |
| Horse + rider canter | 19,000 | - | full body KE (above tip) |
| Dragon claw | 35,000 | - | - |
| Trebuchet stone | 90,000 | - | - |

Bow / compound / Strength draw dial: `Bows.md` (STR 15 compound ~97 J). Weapon rune blasts (e.g. detonation tip) sit on top of kinetic tip KE when the tip is lit. Rune Useful uses η_cond × A (`A = √C`; `../Runes/Energy.md`), not μ(INT). Explosive / blast spell fills meet the shield at **G = 1** (full pool).

## Worked lock: Ch 14 watcher vs Reyna shield

**Levels:** watcher / T2 fencer overall **L55** (T1 **25** + ~**30** into T2). Becky / Sahildr / Reyna overall **~45** (second T1 deep, e.g. **25+~20**). Roland Mage **L25**. Sahildr's "just advanced" line is trash talk; he is not a fresh T2.

**Roland:** Mage L25 rewrite, INT **137**, Mana Shield **L6**. Casts a **bubble** on Reyna, screams / overcharges → treat **M ≈ 150–200**. Bubble pool **~3.4–4.5 kJ** head-on (skill tip, G = 1).

**Watcher:** Tier 2 physical, speed + penetration specialist. Working sheet for scale: **STR 120 / AGI 120** + **Gale Step** (+ orange detonation tip). Early–mid T2 for overall **L55**, not hard-T2 ceiling stats.

| Attack model | Energy into bubble |
|---|---|
| Street rapier only | 30–60 J (never pierces) |
| AGI 120 base lunge | ~0.7–1.1 kJ |
| AGI 120 + Gale Step (`k≈2–2.5`) | **~3–7 kJ** |
| + tip detonation | higher still (on-page blast through) |

**On-page result:** bubble holds a moment, tip bends then **blasts through** with explosion; Reyna's dagger cannot fully fend → shoulder graze. Gale tip KE sits at or above the overcharged bubble (~3.4–4.5 kJ), so the tip can pierce on its own; the detonation is still what the page shows finishing through. A **focused disk** at the same mana (~19–25 kJ head-on, ~38–50 kJ of head-on threat at the default 45° face) would stop that thrust.

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
3. **Is a skill multiplying speed?** `k` on tip speed squares into KE. Skills / spells use **G = 1**; slow mundane matter meets only partial grip.
4. **N = 0** means pierce (attack passes whole; shield collapses). **N ≥ 1** means that whole attack is eaten (pool drops for the next).
5. **Steady push?** Hold drain (0.3 J/s per N) empties the pool even when the first contact holds.

## Locked keep

Street STR/AGI 15 baseline. Tip KE from effective mass and tip speed. Speed skills raise tip speed factor k (KE scales with k²). Shield pools in joules (head-on formula ×10); default disk at 45°; focused disk ≫ bubble per mana; both shield and spell Useful × ambient `A` (mana paid unchanged). Ch 14 bubble vs Gale tip lock above (open ground). Hardness tables live in ManaCast.

## Open

Late raid math beyond the ladder stays unset until a fight beat needs a hard number.
