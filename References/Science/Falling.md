# Falling

Hub: `Science.md`. Pole brake: Shepherd's Leap below. Strength scale: `../Progression/Progression.md`. Mana soft-fall spells stay separate.

## Fall landings (hard flat ground)

All free-fall speeds use `v = √(2gh)` with `g = 9.81 m/s²` (no air drag). Thresholds are typical for an adult on hard flat ground, shaded slightly for **100 kg**. KE = `½mv²` at **m = 100 kg**. Convert: **1 m/s ≈ 2.24 mph ≈ 3.6 km/h**.

Under about **10 m**, drag is negligible so posture barely changes speed. At high speed, spread-out terminal velocity is about **50 m/s (~112 mph)** and feet-first about **80 m/s (~179 mph)**. Free-fall `√(2gh)` overstates speed once drag matters; use it as a vacuum / low-height yardstick.

### Outcome thresholds

| Outcome | Max height | Landing speed | KE at impact |
|---|---|---|---|
| Easy landing, no damage | 0.5 m | 3.1 m/s (**7 mph** / 11 km/h) | 490 J |
| Deep knee bend, no damage | 2 m | 6.3 m/s (**14 mph** / 23 km/h) | 1,960 J |
| Roll, no damage (trained) | 3.5 m | 8.3 m/s (**19 mph** / 30 km/h) | 3,430 J |
| Roll, some damage (bruises, sprains, possible fracture) | 3.5 to 7 m | 8.3 to 11.7 m/s (**19–26 mph**) | 3,430 to 6,870 J |
| Feet-first, no roll, ankle or bone damage | 3 to 6 m | 7.7 to 10.8 m/s (**17–24 mph**) | 2,940 to 5,890 J |
| Catastrophic (spine, pelvis, skull, organ trauma) | 10 to 15 m | 14 to 17 m/s (**31–38 mph**) | 9,810 to 14,720 J |
| Death likely (~50% near 12 m) | 12 to 15 m and up | 15.3 to 17 m/s and up (**34–38 mph+**) | 11,770 J and up |
| Death near certain | 25 m and up | 22 m/s and up (**49 mph+**) | 24,500 J and up |

### Height → speed (free fall, no drag)

`h = v² / (2g)`. Above ~10 m, real air slows the fall; heights to reach a listed speed grow, especially when approaching terminal.

| Landing speed | mph | km/h | Height (no drag) | Notes |
|---|---|---|---|---|
| 3.1 m/s | **7** | 11 | 0.5 m | Easy landing |
| 6.3 m/s | **14** | 23 | 2.0 m | Deep knee bend |
| 8.3 m/s | **19** | 30 | 3.5 m | Trained roll |
| 10.8 m/s | **24** | 39 | 5.9 m | Hard feet-first band |
| 11.7 m/s | **26** | 42 | 7.0 m | Upper roll-damage band |
| 14 m/s | **31** | 50 | 10.0 m | Catastrophic start |
| 15.3 m/s | **34** | 55 | 11.9 m | ~50% death yardstick |
| 17 m/s | **38** | 61 | 14.7 m | High catastrophic |
| 22 m/s | **49** | 79 | 24.7 m | Death near certain |
| 30 m/s | **67** | 108 | 45.9 m | Drag already large in air |
| 40 m/s | **89** | 144 | 81.5 m | |
| 50 m/s | **112** | 180 | 127 m | ~**spread-out terminal** |
| 60 m/s | **134** | 216 | 184 m | Between postures |
| 70 m/s | **157** | 252 | 250 m | |
| 80 m/s | **179** | 288 | 326 m | ~**feet-first terminal** |

### Standing (feet-first) versus spread out

Under about **10 m**, both postures give the same speed. Spread out only adds a little height for the same landing speed at higher speeds (more drag).

| Landing speed | mph | Height, feet-first | Height, spread out |
|---|---|---|---|
| 8.3 m/s | 19 | 3.5 m | 3.5 m |
| 14 m/s | 31 | 10.0 m | 10.4 m |
| 17 m/s | 38 | 14.8 m | 15.6 m |
| 22 m/s | 49 | 24.9 m | 27.4 m |
| ~50 m/s terminal | ~112 | (not reached feet-first) | asymptotic |
| ~80 m/s terminal | ~179 | asymptotic | (not reached spread) |

### Posture effects on damage

- **Feet-first** concentrates load through heels, ankles, shins and spine. Bone damage begins early (~**3 m**).
- **Spread out / flat** on hard ground spreads force over area (helps bones) but sends shock into torso and organs. Not safer at catastrophic speeds.
- **Rolling** stretches stopping distance from ~**0.1 m** to **1 m+**. Average force `F = m·v²/(2d)`: same **8.3 m/s** is about **34,000 N** over 0.1 m and about **3,400 N** over 1 m.

## Shepherd's Leap (pole brake fall)

Emergency landing when **mana is empty** (no Hands / Shield / soft-fall spells). Pull a **pole** from the spatial bag, plant tip, and slide so braking acts over meters instead of an instant slam. Named for the pastoral pole vault / slide; used here as a **descent brake**.

### Energy balance

```
v = sqrt( 2 * ( g*h - F*d / m ) )
```

- `v` = landing speed (m/s)
- `g` = 9.81 m/s²
- `h` = drop height already fallen or total drop (use consistent start-from-rest PE)
- `m` = body mass
- `F` = average braking force (grip friction + tip drag), newtons
- `d` = distance over which braking acts (~**3 m** as the practical slide length with a bag pole; use full `h` only if sliding the whole drop)

No pole → `F = 0` → `v = sqrt(2*g*h)`.

Force for a target landing speed:

```
F = m * ( g*h - v_target² / 2 ) / d
```

Define `f = F / (m*g)`. If `d = h`:

```
v = sqrt( 2*g*h * (1 - f) )
```

Heavier bodies need proportionally more `F` for the same `f`. Grip and tip force **relative to body weight** matter most. If `f ≥ 1`, descent stops / hangs (do not take a negative under the root).

### Full stack (do not use STR alone)

Height ceiling is the product of several sheet lines. Mana empty → no Reinforcement / Hands soft-fall.

| Factor | Sheet | Role |
|---|---|---|
| **Brake speed cut** | Strength | Muscle squeeze `N` and tip drive. Raises `F`. Main height lever under a short `d`. |
| **Hand robustness** | Vitality (bones, tendons, palm tissue) | Caps how hard he can squeeze without breaking hands. Usable `N ≈ min(N_STR, N_Vit)` for sustained slide. |
| **Palm abrasion** | Vit skin + **Recovery** | Friction work ≈ `F_grip × d`. Split palms are expected at high squeeze. Recovery licenses that damage on a short clock (L9 = **10×** knit). Without enough Recovery he throttles grip to avoid lasting hand injury → lower `F` → lower `h`. |
| **Grip stamina** | Endurance / SP | Holds squeeze through the stroke. Fade still applies on long slides. |
| **Landing speed resistance** | Vit + End (`M = ((Vit+End)/2)/15`) | How fast he may still hit and only pay palm cost. `v_safe ≈ 3.5 × √M` m/s (street soft ~**3.5 m/s** at M = 1). Legs / ankles / knees eat leftover KE over knee bend `s`. |
| **Landing form** | Acrobatics / Dodging (technique) | Helps use the full `v_safe` band. Does not replace Vit tissue. |
| **Pain** | Pain Resistance | Keeps grip after palms split. Does not raise force or `v_safe` by itself. |

```
F_grip ≈ μ * N_use
N_use  = min( N_street × STR/15, N_street × Vit/15 )   # Rec L9: allow full STR N and accept splits
F      = F_grip + F_tip
v_safe ≈ 3.5 × √M
h_max  = ( F*d/m + v_safe²/2 ) / g
```

- `N_street` ≈ **800 N** two hands (~**400 N**/hand)
- `μ` ≈ **0.4–0.6** wood, bare or glove
- `F_tip` = iron tip drag / bite; often **1–1.5×** `F_grip` on rock or packed soil (STR shove + ground). Great bite ~**2×** is a clean plant ceiling.
- `d ≈ 3 m` default bag-pole stroke unless the fall is shorter

**STR alone understates** height: Vit/End raise `v_safe` so the same brake can leave more leftover speed. **STR alone overstates** if Vit lags or Recovery is low (hands throttle or break).

### Worked feel (80 kg, h = 6 m, d = 6 m)

| Braking force F | f | Landing speed |
|---|---|---|
| 0 N (free fall) | 0 | 10.8 m/s (**24 mph**) |
| 400 N (grip only, weak surface) | 0.51 | 7.6 m/s (**17 mph**) |
| 600 N | 0.76 | 5.3 m/s (**12 mph**) |
| 725 N | 0.92 | 3.0 m/s (**7 mph**, soft-landing band) |

With a bag pole, treat **`d ≈ 3 m`** as the default brake stroke unless the fall is shorter. Same `F` over half the distance leaves more leftover speed: raise tip bite or accept a harder landing into the Vit/End `v_safe` band.

### Impact at the end

```
F_impact ≈ m * v² / (2 * s) + m*g
```

`s` = knee bend ~**0.4–0.5 m**. Street soft landing ~**3–4 m/s**. Roland scales that band with **√M** (Vit/End). Peaks exceed the average.

### Roland yardsticks (full stack, m = 80 kg, d = 3 m)

Palm cost = split skin that **Recovery** closes fast. Not broken metacarpals (Vit must cover squeeze).

| Snapshot | STR / Vit / End / Rec | Good plant (`F_tip ≈ 1.5 F_grip`) | Notes |
|---|---|---|---|
| Ch 13–18 rewrite | **49 / 47 / 53 / L5** | **~15 m** (`v_safe ~6.4`) | Vit ≈ STR so hands mostly keep up; Rec L5 = throttle near tissue, light splits |
| Ch 19+ train exit | **49 / ~63 / ~76 / L9** | **~15 m** (`v_safe ~7.5`) | Same STR brake; higher Vit/End buys leftover speed; Rec L9 licenses full-squeeze splits |
| Ch 19 great tip bite | same | **~18 m** | Clean iron bite ~**2×** grip |
| Later rewrite (STR **78** band) | **78 / ~74 / ~87 / L9** | **~23 m** | STR climb dominates; Vit must stay close or hands become the cap |

Equal tip (~**1×** grip) sits a few meters lower; weak surface / tip skip falls back toward grip-only.

**Factor split (Ch 19, good plant):** STR brake at street-soft **3.5 m/s** leftover ≈ **13 m**. Adding Vit/End `v_safe` ≈ **+2 m**. Recovery does not add meters directly; it **keeps** the full STR grip in play.

### Story use (Roland)

1. Mana gone mid-fall.
2. Spatial bag → pole (dead matter; fast draw).
3. Plant tip, two-hand slide, tip digs for `F_tip`.
4. Brake over ~**3 m** of pole travel so the slam stretches into a slide.
5. **Strength** cuts speed; **Vit/End** eat the leftover landing; **Recovery** (and Pain) let palms split and still hold the shaft.

**Caveats:** grip fades over a long slide; sweat / polish cuts `μ`; tip catch or skip is lumpy; bad plant = no brake; Vit-lagging STR → broken hands before max brake. Not a substitute for mana soft-fall when the pool still has juice.

## Ned fall-proof

Body stays **1 m / 10 kg** (`../People/Ned.md`). Sideways terminal ≈ **38 m/s (~85 mph)**, KE ≈ **7.2 kJ**. Tissue force scales with Vit vs street (**Vit / 15**); crumple distance is the main lever.

### Belly / side landings

Resilin + soft body give about **0.2 m** of give. Safe landing speed matches terminal at **Vit ~100** → **4x Greater** (overall **26**, Ch 14+). Earlier bands survive lower drops only (1x ~**19 m** vacuum, ~3x ~**56 m**).

### Tip / point landings (fold)

He can **fold on impact** and turn a tip hit into an accordion crumple along the body. Useful stroke ≈ **0.4–0.5 m** (about half his length). That raises safe speed enough that:

| Band | Vit | Tip-fold vs terminal (~38 m/s) |
|---|---|---|
| 1x tame | 25 | Short of terminal (~**27–30 m/s** safe); high drops still hurt |
| **~3x** (Ch 13) | **75** | **At / above terminal** with a clean fold |
| **4x Greater** | **100** | Clear margin (~**54–61 m/s** safe) |

**Story lock:** from **Greater 4x** he is fall-proof from any height on belly, side **or** tip if he folds. From **~3x** tip-fold already covers terminal if the fold lands true. Bad tip plant with no fold still concentrates load; do not treat every tip hit as free before he has the habit.

Skin knife-energy table is puncture budget, not whole-body slam. Prefer the force + crumple / fold reading for falls.
