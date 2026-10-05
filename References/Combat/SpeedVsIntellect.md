# Speed Vs Intellect

Think time vs move time when INT and physical stats diverge. Mage Hands / instant magic: `Combat.md`, Old `MageDefense.md`. Sound / ping limits sit at the end.

## Narrative

Mental speed scales about **linear** with intellect multiple. Physical limb speed scales about **√P** because kinetic energy rises with v² for the same mass budget. Specialists hit floors. Instant magic removes the move term and flips the value of INT.

## Detail

### Core split

```
I = INT / 15
P = physical_stat / 15          // STR or AGI as the motion stat
Think = t_r / I
Move  = t_m / √P
Total = Think + Move
```

Baseline reaction `t_r ≈ 0.2 s`. `t_m` = baseline human motion time for that action.

### Specialist floors

```
Intellect build (×x mind, 1× body):  T = t_r/x + t_m
Speed build (1× mind, ×x body):      T = t_r + t_m/√x
```

Intellect never beats pure `t_m`. Speed never beats pure `t_r`.

```
Intellect wins when: 1 + 1/√x > t_m / t_r
```

| Action | t_m | t_m/t_r | Winner pattern |
|---|---|---|---|
| Jab | ~0.12 s | 0.6 | Intellect always |
| Sword cut | ~0.35 s | 1.75 | Intellect early; speed past ~1.78× |
| Pistol draw | ~1 s | 5 | Speed always |
| Close 10 m | ~1.8 s | 9 | Speed always |

Mixed builds remove both floors. Rough optimum when `t_r / I² = t_m / (2·P^1.5)`.

### Worked 240-point split (no magic)

You: INT 150 (10×), STR/AGI 45 (√3 ≈ 1.73×)  
Foe: INT 30 (2×), STR/AGI 105 (√7 ≈ 2.65×)

```
You:  0.02 + t_m/1.73
Foe:  0.10 + t_m/2.65
```

You start **0.08 s** ahead. Crossover ~**0.4 s** baseline motion.

| Action | You | Foe | Winner |
|---|---|---|---|
| Jab 0.12 | 0.089 | 0.145 | You |
| Sword 0.35 | 0.222 | 0.232 | You (thin) |
| Pistol 1.0 | 0.597 | 0.478 | Foe |
| Close 10 m | 1.059 | 0.780 | Foe |

Without magic: win point-blank exchanges and counters, not footraces. Marginal +1 physical usually beats +1 INT on motions longer than leftover think time.

### Instant-activation magic

Your time → think only (`0.02 s` at 10× INT). You win every exchange magic can resolve unless detection, delivery, resources or momentum say otherwise.

**Still loses to:**

1. **Not detected** (ambush, behind, close bullets already in flight)  
2. **Shield fails** (energy, momentum into body, coverage gaps, already grappled)  
3. **Attack fails** (orihalcum / star metal, enemy shields, own shield blocking outbound spell)  
4. **Resources** (mana attrition, many angles)  
5. **Bad decisions** (feints, illusions)

Shield then attack ≈ two activations (~0.04 s) still beats a 2.65× jab window in the worked example.

Close bullet rule of thumb: pistol ~360 m/s inside ~7 m and rifle ~850 m/s inside ~17 m finish inside 0.02 s think. Need pre-trigger read or faster detection.

### Laser aim (think-bound)

Once the beam is on target, light speed removes the dodge term. The fight is aim and track: Think + any turret slew. High INT / Parallel Thinking operators close that gap against superhuman movers. Doctrine: `Lasers.md`. Physics: `../World/Science/Energy/Optics.md`.

### Sound and echolocation (sensing floor)

- Frequency does not change sound speed (~343 m/s air). Amplitude can: `Mach ≈ √(1 + 0.857·Δp/p0)`
- Ultrasound (>20 kHz) can be quiet to bystanders; absorption rises with frequency. Workable bat-like band ~**40–100 kHz**, useful map ~**5–30 m**
- Infrasound carries far but is too coarse for detail
- **Sense Danger**-class EM detect (if locked later): ~3.3 ns/m. Remaining delay is still think time (+ nerve path if routed through the body)

## Open

- Wire exact INT/AGI sheet numbers for D when Progression deepens
- Full MageDefense absorb for Hands timing numbers
