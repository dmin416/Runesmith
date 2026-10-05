# Living Armor (Colony Plate)

Animated empty plate driven by a soft colony clinging inside the shell. Useful for dungeon living-armor foes and any “muscle in the metal” construct. Human baseline for multipliers: **stat 15**. Materials / plate: `../World/Materials/Metals.md`.

## Narrative

The colony is the muscle. The steel is shell and skeleton. Mollusks (or equivalent soft drivers) cluster at joints and pull plates against each other. Strong, slow, terrible stamina for long active fights. Catch-lock grips are the real terror.

## Detail

### Baseline block (worked example)

| Stat | Human | Living armor | × human |
|---|---|---|---|
| STR | 15 | 21 | 1.4 |
| AGI | 15 | 6 | 0.4 |
| Stamina | 15 | 5 | 0.33 |
| Mass | 75 kg | 54 kg | 0.72 |
| STR / kg | 0.20 | 0.39 | ~2× |

### How STR is spent

| Job | Muscle | STR mult | Effective | Speed |
|---|---|---|---|---|
| Strike / swing / lift / push | Striated | ×1 | sheet STR | AGI-limited |
| Hold / pin / grip / clamp | Catch | ×4 | 4 × sheet STR | Very slow to engage and release |
| Long active fight | Either | - | Stamina-limited | Falls off fast |

Catch muscle locks for hours near free. A pin lasts until release or the joint cluster dies.

### Per-point conversions (human 15 anchors)

```
deadlift_kg     = 6 × STR_eff              // same law as AttackScale / Attributes
leg_force_N     = 135 × STR_eff
grip_N          = 128 × STR_eff          // use catch STR_eff for pins
strike_vs_human = STR_eff / 15
speed_vs_human  = AGI / 15
time_per_swing  = 15 / AGI
fatigue_time    = Stamina / 15            // vs human bout length
strike_power    = STR × AGI / 15          // human 15 → 15
STR_per_kg      = STR / mass_kg
min_STR_lunge   ≈ 0.2 × mass_kg          // rough run/lunge floor
```

Example at STR 21 / AGI 6: deadlift 126 kg, grip (catch) 2688 N, swings at 0.4× human speed (~2.5× longer wind-up). Hard hit if it connects. Fast fighter steps inside.

### Where the numbers come from (rebuild kit)

Mass split example: ~30 kg shell + ~22 kg colony (of which ~12 kg muscle) + weapon ≈ 54 kg moving.

```
STR ≈ 15 × (m_muscle/m_human_muscle) × (σ/σ_human) × (L/L_human) × arch
```

Worked: muscle 12/32 → 0.375; stress match human skeletal (~0.3 MPa) → 1; leverage ~2.5 (rim attach ~10 cm vs ~4 cm tendon) → 2.5; thick short joint bags → 1.5  
→ STR ≈ 15 × 0.375 × 1 × 2.5 × 1.5 = **21**

```
AGI ≈ 15 / leverage_ratio
```

2.5× lever → AGI **6** (force over distance).

```
catch_mult ≈ σ_catch / σ_striated     // 1.2 / 0.3 → ×4
```

Lunge floor: need ~2.75 × body weight peak leg force. 54 kg × 9.81 × 2.75 ≈ 1457 N → min STR ~11. STR 21 clears it.

### Weak points

- Joint clusters **are** the muscles. Scrape or crush a joint → that limb dies
- Pop a plate off its attach → slack limb
- AGI tax on every swing
- Stamina 5: burst fighter, not a duel grinder
- Catch release is slow
- Soft drivers hate heat, cold and dry. Steel conducts that in fast

### Rescale any colony armor

1. Lock shell mass, colony mass, muscle mass
2. Set leverage ratio and catch/striated stress ratio
3. Compute STR and AGI from the formulas
4. Apply catch ×4 only to holds
5. Write the fight: heavy slow blows, deadly pins, joint-hunt kill path

## Open

- Named Terra species / dungeon floor placement
- Plate material upgrades (star steel, mythril shell) once a beat needs them
