# Eye and Ear Scaling

How protective reflexes and damage thresholds change as a person becomes S times stronger than a normal human, for S from 1 to 100.

The movement term is the same square-root law as `../../../Combat/SpeedVsIntellect.md`: force scales with the body multiple, so movement time scales with 1/√ of that multiple. Combat timing stays there. Baseline reaction `t_r ≈ 0.2 s` is not replaced by this file. Earth reaction anchors: `SpeedPerception.md`. Parallel minds that do not think faster: `FocusCapacity.md`. Full-sphere optics: `Vision360.md`.

Symbols here are local.

- **S** is muscle-force multiple versus a normal human. It is not `P = physical_stat / 15`. √S and √P match only when S is that same multiple.
- **M** is conscious decision speed. It is not men-worth and it is not the focus-spot M.
- **N** is brainstem reflex speed. Intelligence does not raise it.
- **D = S** is the default assumption, not a lock. Set D apart for someone strong and fragile, or fragile and strong.

## Variables

| Symbol | Meaning | Default |
|---|---|---|
| S | Strength multiplier (muscle force vs a normal human) | 1 to 100 |
| D | Durability multiplier (tissue damage threshold vs a normal human) | D = S |
| N | Reflex nerve speed multiplier (brainstem loops) | 1 |
| M | Mental speed multiplier (conscious decisions) | 1 to 2 |
| H | Healing multiplier (recovery after injury) | separate input |
| E | Light irradiance at the cornea (W/cm²) | input |
| L | Sound pressure level (dB SPL) | input |

Two humans thinking in parallel process more information but react no faster. M = 2 changes nothing in the reaction formulas unless the second mind is also faster.

## Movement time

Any protective movement (eyelid closing, iris constricting, head turning, hand rising) moves a fixed mass m over a fixed distance d.

```
t = sqrt(2 · d · m / F)
```

Force F scales with S. Mass and distance stay the same.

```
t_move(S) = t_move(human) / sqrt(S)
```

Strength 4× gives movement 2× faster. Strength 25× gives movement 5× faster. Strength 100× gives movement 10× faster.

### Total response time

```
T_total = (neural latency / N) + (activation latency) + (t_move / sqrt(S))
```

- **Neural latency:** signal travel through nerves and synapses. Scales with N only.
- **Activation latency:** time for muscle chemistry to begin contracting. Fixed for human biology.
- **Movement:** scales with 1/√S.

### The latency floor

As S rises, the movement term shrinks. The response time can never drop below:

```
T_floor = (neural latency / N) + activation latency
```

With N = 1, strength alone cannot push reflexes below this floor. Anything that causes damage faster than the floor must be absorbed by durability D.

Real muscle also has a maximum shortening velocity (Hill's equation). The √S law treats force as the only bottleneck, which is the generous assumption.

## Eye responses

### Human baseline

| Response | Neural latency | Activation | Movement | Human total |
|---|---|---|---|---|
| Light-triggered blink | 50 ms | ~0 (skeletal muscle) | 75 ms | 125 ms |
| Pupil constriction (to minimum) | 70 ms | 130 ms (smooth muscle) | 500 ms | 700 ms |
| Voluntary eye close | 200 ms (decision) | ~0 | 75 ms | 275 ms |
| Turn head away | 200 ms (decision) | ~0 | 150 ms | 350 ms |
| Retinal recovery after flash | chemical | n/a | n/a | 1 to 5 s |
| Full light adaptation | chemical | n/a | n/a | 5 to 10 min |

Decision latencies divide by M instead of N. The 200 ms decision rows are the same band as `t_r ≈ 0.2 s`.

### Formulas

```
T_blink     = 50/N  + 75/sqrt(S)            ms
T_pupil     = 70/N  + 130 + 500/sqrt(S)     ms
T_closeEyes = 200/M + 75/sqrt(S)            ms
T_turnHead  = 200/M + 150/sqrt(S)           ms
```

Retinal adaptation is pigment chemistry. It does not scale with S. It scales with H or a separate metabolic factor.

### Times by strength (N = 1, M = 1)

| S | Blink | Pupil | Close eyes | Turn head |
|---|---|---|---|---|
| 1 | 125 ms | 700 ms | 275 ms | 350 ms |
| 2 | 103 ms | 554 ms | 253 ms | 306 ms |
| 5 | 83.5 ms | 424 ms | 233.5 ms | 267 ms |
| 10 | 73.7 ms | 358 ms | 223.7 ms | 247 ms |
| 20 | 66.8 ms | 312 ms | 216.8 ms | 233.5 ms |
| 50 | 60.6 ms | 271 ms | 210.6 ms | 221 ms |
| 100 | 57.5 ms | 250 ms | 207.5 ms | 215 ms |

Floors with N = 1: blink 50 ms, pupil 200 ms, voluntary actions 200 ms.

### Pupil protection factor

A pupil shrinking from 7 mm to 2 mm cuts light entering the eye by:

```
P = (7 / 2)^2 = 12.25
```

Divide E by 12.25 once the pupil has fully constricted.

### Retinal damage (point sources)

Based on the international laser safety limits (ANSI Z136.1 / IEC 60825-1) for visible light (400 to 700 nm) with a 7 mm pupil. Real injury occurs at about 10× the published safety limit. The formulas below use the injury threshold.

```
Short exposures (under 18 µs):     t_injury = 5×10^-6 · D / E          seconds
Middle range (18 µs to 10 s):      t_injury = (1.8×10^-2 · D / E)^4     seconds
Equilibrium (over 10 s):           safe indefinitely if E ≤ 1.0×10^-2 · D
```

Use the short formula if the middle formula returns less than 18 µs.

The fourth power in the middle range means durability has a huge effect. Doubling D multiplies safe time by 16. Ten times D multiplies safe time by 10,000.

The eye avoids injury if its fastest response finishes before injury:

```
T_blink < t_injury
```

### Light injury times (D = S)

Corneal irradiance values assume a beam fully entering a 7 mm pupil.

| Source | E (W/cm²) | S = 1 | S = 2 | S = 5 | S = 10 | S = 20 | S = 50 | S = 100 |
|---|---|---|---|---|---|---|---|---|
| 5 mW laser pointer | 0.013 | 3.7 s | safe | safe | safe | safe | safe | safe |
| 100 mW laser | 0.26 | 23 µs | 0.37 ms | 14.4 ms | 230 ms | 3.7 s | safe | safe |
| 1 W laser | 2.6 | 1.9 µs | 3.8 µs | 9.6 µs | 23 µs | 0.37 ms | 14.4 ms | 230 ms |
| 100 W/cm² beam | 100 | 50 ns | 100 ns | 250 ns | 500 ns | 1 µs | 2.5 µs | 5 µs |

Against blink times:

- S = 1 vs a 5 mW pointer: injury at 3.7 s, blink at 125 ms. Protected.
- S = 5 vs a 100 mW laser: injury at 14.4 ms, blink at 83.5 ms. Injured.
- S = 10 vs a 100 mW laser: injury at 230 ms, blink at 73.7 ms. Protected.
- S = 50 vs a 1 W laser: injury at 14.4 ms, blink at 60.6 ms. Injured.
- S = 100 vs a 1 W laser: injury at 230 ms, blink at 57.5 ms. Protected.
- A 100 W/cm² beam injures in microseconds at every S in range. Reflexes never help.

### Direct sunlight

The sun is an extended source. Damage is photochemical and follows simple dose reciprocity.

```
t_sun ≈ 60 s · D
```

| S | Time staring at the sun before retinal damage |
|---|---|
| 1 | ~1 min |
| 2 | ~2 min |
| 5 | ~5 min |
| 10 | ~10 min |
| 20 | ~20 min |
| 50 | ~50 min |
| 100 | ~1.7 h |

## Ear responses

### Human baseline

| Response | Neural latency | Movement / rise | Human total | Protection |
|---|---|---|---|---|
| Acoustic reflex (stapedius + tensor tympani) | 25 ms | 100 ms | 125 ms | ~15 dB, low frequencies |
| Hands over ears (voluntary) | 150 ms (decision) | 250 ms | 400 ms | 15 to 25 dB |
| Temporary hearing loss recovery | cellular | n/a | 16 to 48 h | n/a |

Auditory reaction time (~150 ms) runs faster than visual reaction time (~200 ms).

### Formulas

```
T_reflex = 25/N  + 100/sqrt(S)     ms
T_hands  = 150/M + 250/sqrt(S)     ms
```

Stronger middle-ear muscles stiffen the ossicle chain harder. Low-frequency transmission falls in proportion to stiffness:

```
A_reflex = min(15 + 20·log10(S), 45)    dB
```

The 45 dB cap exists because sound still reaches the inner ear through skull bone conduction even with the ossicles fully locked. High frequencies (above ~2 kHz) receive about half the listed attenuation.

Human acoustic reflex strength halves within ~10 s of steady loud sound at mid to high frequencies. Model a stronger reflex as holding longer by roughly √S.

### Times by strength (N = 1, M = 1)

| S | Reflex | Reflex attenuation | Hands over ears |
|---|---|---|---|
| 1 | 125 ms | 15 dB | 400 ms |
| 2 | 95.7 ms | 21 dB | 327 ms |
| 5 | 69.7 ms | 29 dB | 262 ms |
| 10 | 56.6 ms | 35 dB | 229 ms |
| 20 | 47.4 ms | 41 dB | 206 ms |
| 50 | 39.1 ms | 45 dB (cap) | 185 ms |
| 100 | 35 ms | 45 dB (cap) | 175 ms |

Floors with N = 1: reflex 25 ms, hands 150 ms. The 45 dB cap is reached near S = 30.

### Impulse sounds

Gunshots and explosions reach peak pressure in under 1 ms. The acoustic reflex floor is 25 ms. No amount of strength lets a human-speed nervous system catch an impulse. Only durability protects against bangs. Only raising N lowers the floor.

### Damage formulas

Continuous noise, from the NIOSH 85 dBA / 3 dB exchange rule:

```
T_allowed = 28,800 s · D / 2^((L_eff − 85) / 3)
L_eff     = L − A_reflex − A_hands
```

Every 10× durability raises every noise limit by 10 dB.

Impulse noise ceiling (cochlea):

```
L_impulse_max = 140 + 10·log10(D)    dB peak
```

Eardrum rupture. Membrane strength scales with D. Pressure thresholds scale linearly, so decibels scale by 20·log10:

```
L_rupture   = 185 + 20·log10(D)    dB    (threshold, ~5 psi)
L_rupture50 = 194 + 20·log10(D)    dB    (50% rupture, ~15 psi)
```

### Continuous noise, no attenuation (D = S)

| Level | Example | S = 1 | S = 2 | S = 5 | S = 10 | S = 20 | S = 50 | S = 100 |
|---|---|---|---|---|---|---|---|---|
| 120 dB | Thunder nearby, rock concert front row | 8.9 s | 17.7 s | 44 s | 1.5 min | 3 min | 7.4 min | 14.8 min |
| 140 dB | Jet engine at 30 m | 87 ms | 174 ms | 0.44 s | 0.87 s | 1.7 s | 4.4 s | 8.7 s |
| 160 dB | Close-range explosion (sustained) | 0.86 ms | 1.7 ms | 4.3 ms | 8.6 ms | 17 ms | 43 ms | 86 ms |

Add the reflex and hand attenuation once those responses have fired. S = 100 with a full reflex (45 dB) turns 140 dB into an effective 95 dB, which allows about 80 h of exposure.

### Single-blast limits (D = S)

| S | Impulse ceiling (cochlea) | Eardrum rupture threshold | Rupture pressure |
|---|---|---|---|
| 1 | 140 dB | 185 dB | 34.5 kPa (5 psi) |
| 2 | 143 dB | 191 dB | 69 kPa (10 psi) |
| 5 | 147 dB | 199 dB | 173 kPa (25 psi) |
| 10 | 150 dB | 205 dB | 345 kPa (50 psi) |
| 20 | 153 dB | 211 dB | 690 kPa (100 psi) |
| 50 | 157 dB | 219 dB | 1.73 MPa (250 psi) |
| 100 | 160 dB | 225 dB | 3.45 MPa (500 psi) |

Sound in sea-level air cannot exceed ~194 dB as an ordinary wave. From S = 5 upward, only shock waves and blast overpressure can rupture the eardrum.

### Recovery

```
T_recover = T_recover(human) / H
```

Human temporary threshold shift recovers in 16 to 48 h. Permanent hair cell loss does not recover in humans (H = 0 for regrowth). Any H > 0 makes permanent loss temporary.

## What changes

| Factor | Scales with | Effect of rising S (N = 1, M = 1) |
|---|---|---|
| Eyelid, head, hand movement speed | 1/√S | Up to 10× faster at S = 100 |
| Iris movement speed | 1/√S | Faster, but smooth muscle activation stays at 130 ms |
| Middle-ear muscle force | S | Stronger attenuation up to the 45 dB bone conduction cap (reached near S = 30) |
| Reflex neural latency | N | Unchanged |
| Conscious decision time | M | Unchanged |
| Retinal pigment recovery | H or metabolism | Unchanged |
| Retinal damage threshold | D (to the 4th power in time) | Massively higher |
| Hearing damage threshold | 10·log10(D) dB | Up to 20 dB higher at S = 100 |
| Eardrum rupture threshold | 20·log10(D) dB | Up to 40 dB higher at S = 100 |

1. Most reflex gain happens by S ≈ 20. From S = 20 to S = 100, the blink improves only about 9 ms because neural latency dominates.
2. Durability does most of the protective work at the top of the range. Reflexes stop mattering for anything faster than about 50 ms (eyes) or about 25 ms (ears).
3. Flashes and bangs are durability tests, not reflex tests. Lasers, flashes and explosions arrive in microseconds to milliseconds. A human-speed nervous system never responds in time regardless of strength.
4. The fourth-power light law makes eyes extremely sensitive to D. A 10× tougher retina survives 10,000× longer exposure in the 18 µs to 10 s window.
5. Raising N is the only way to lower the floor. Fast brainstem reflexes without faster thought (N > 1, M = 1) give near-instant blinks and acoustic reflexes.

## Checklist

1. Choose S (1 to 100), D, N, M.
2. Compute T_blink, T_pupil and T_reflex from the formulas above.
3. Compute t_injury for light, or T_allowed and the rupture level for sound.
4. If the response time is shorter than the injury time, reflexes protect. Otherwise durability decides.
5. Apply the pupil factor (÷12.25) and ear attenuation after those response times have elapsed.
6. Apply H for recovery time.
