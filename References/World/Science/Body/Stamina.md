# Stamina

How human stamina works, and how it scales when muscle force rises by k in a body that stays the same size and mass.

The stamina-point formula stays in `../../../Progression/Attributes.md`. A street adult at 15 is **240 SP**. **1 SP = 10 J** when it pays a rune, the same peg as mana. Anaerobic muscle work spends the bar at one sixth that price, so the same point covers **62.5 J** of work above critical power and the street pool is still the **15 kJ** science reserve. Health points stay the Vitality and Endurance formula in that same file. They are not blood volume.

Sheet conversions stay in `../../../Progression/Training.md` and `../../../Combat/AttackScale.md`: Agility 15 is **375 W** and a **6 m/s** sprint, Endurance 15 is **3 L/min** VO2, and the adult mass used for sprint kinetic energy is about **80 kg**. The worked sprint below is a **70 kg** body with a **10 m/s** baseline. Those rows are the scaling example.

k is force at fixed mass. Speed scales as √k and power as k^1.5. That is the same square-root movement law as `../../../Combat/SpeedVsIntellect.md` and `EyeEarScaling.md`. Muscle efficiency of about 25% matches the 20 to 25% band in `../../../Combat/MageDefense.md`.

## Part 1: How Human Stamina Works

Stamina is the rate and duration at which the body can resupply ATP to muscle while keeping heat, acidity and tissue damage under control. Three energy systems overlap. Whichever one is the bottleneck sets the limit.

| System | Fuel | Max-effort duration | Relative peak power |
|---|---|---|---|
| Phosphagen | Stored ATP and phosphocreatine (PCr) | 8 to 10 s | 100% |
| Anaerobic glycolysis | Muscle glycogen broken down to lactate | 10 s to 2 min | 50 to 60% |
| Aerobic (oxidative) | Glycogen, blood glucose, fat | Minutes to days | 25 to 35% |

**The aerobic chain.** Oxygen moves from the lungs to the heart, then through the blood and capillaries to the mitochondria. The weakest link caps output, and for most people that link is cardiac output: about 20 to 25 L/min untrained and 35 to 40 L/min in elite athletes.

- **VO2max.** About 35 to 45 ml/kg/min untrained, 50 to 60 trained and 70 to 90 elite. The human record is about 97.
- **Energy per liter.** Each liter of oxygen yields about 20.9 kJ (5 kcal).
- **Example.** A 70 kg person at 55 ml/kg/min burns about 1.3 kW at maximum. About 25% of that becomes mechanical work and about 75% becomes heat.

**Thresholds.** Lactate threshold, or critical power (CP), is the highest output sustainable for roughly 30 to 60 minutes. Above CP the body spends a finite anaerobic reserve called W', about 15 to 25 kJ in trained people. Time to exhaustion above CP is approximately W' / (P − CP).

**Fuel.**
- **Glycogen.** Muscle holds 400 to 500 g and the liver about 100 g, roughly 2,000 kcal in total. That lasts 90 to 120 minutes at a hard pace, which is "the wall."
- **Fat.** 10 kg of body fat holds about 90,000 kcal. Maximum fat oxidation is only 0.5 to 1 g/min (300 to 600 W metabolic), which is too slow to fuel hard efforts.

**Heat.** Heat dissipation is the human specialty and the reason persistence hunting works.
- Sweat output is 1 to 2 L/h, with elite athletes reaching about 3 L/h.
- Each liter evaporated removes 2.4 MJ, so 1.5 L/h dumps about 1 kW.
- The core temperature limit is about 40 °C. Body tissue stores 3.5 kJ per kg per °C, which gives a 70 kg body about 735 kJ of buffer between 37 °C and 40 °C.

**Fatigue mechanisms.**
- **Peripheral (in the muscle).** Inorganic phosphate builds up and disrupts calcium release and cross-bridge force. Hydrogen ions accumulate, potassium leaks out of muscle cells and glycogen runs out.
- **Central (in the brain).** The brain reduces motor drive in response to core temperature, fuel status and perceived effort.

**Long-term ceiling.** Over weeks to months, energy expenditure plateaus near 2.5× basal metabolic rate (BMR), about 4,000 to 5,000 kcal/day. Gut absorption is the limit. Efforts lasting only days can reach 4 to 5× BMR by burning body reserves.

**Recovery.**
- PCr has a resynthesis half-time of about 30 s and refills fully in 3 to 5 minutes. The aerobic system drives this.
- Lactate clears over tens of minutes.
- Glycogen takes 24 to 48 hours to restore.

## Part 2: The Enhanced Body

**Assumption.** The enhanced human keeps the same mass (70 kg) and size, and the muscle produces k× the force.

**Why speed scales as √k.** A stride or a punch is force applied over a fixed limb travel distance. That is work, and the work becomes kinetic energy, ½mv². Multiplying the work by k with the same mass multiplies speed by √k. The scenario is internally consistent.

If the strength came from bigger muscles instead, mass would rise faster than strength (the square-cube law) and the speed gain would vanish. Everything below assumes denser, better muscle in an ordinary-sized body.

| Quantity | Scales as | k = 2 | k = 4 |
|---|---|---|---|
| Force | k | 2× | 4× |
| Speed | √k | 1.41× | 2× |
| Acceleration | k | 2× | 4× |
| Time per action | 1/√k | 0.71× | 0.5× |
| Distance per action and distance to top speed | 1 | 1× | 1× |
| Kinetic energy (work) per action | k | 2× | 4× |
| Momentum | √k | 1.41× | 2× |
| Power | k^1.5 | 2.83× | 8× |
| Drag force at top speed | k | 2× | 4× |
| Drag power at top speed | k^1.5 | 2.83× | 8× |
| Heat produced at full output | k^1.5 | 2.83× | 8× |

**Sprint example (k = 2).**

| Measure | Baseline | Enhanced |
|---|---|---|
| Top speed | 10 m/s | 14.1 m/s (31.6 mph) |
| 100 m time | 11.5 s | 8.1 s |
| Acceleration distance | Same | Same |
| Kinetic energy at top speed | 3.5 kJ | 7 kJ |
| Momentum | 700 kg·m/s | 990 kg·m/s |

## Part 3: Each Physics Factor

**Kinetic energy (scales as k).** Every stride, swing, jump and throw costs k× the energy. If energy stores also scale by k, the number of full-power actions stays the same, so this factor is matched.

**Momentum (scales as √k).** Force scales by k while momentum scales only by √k. Stopping or changing direction therefore takes 1/√k the time over the same distance, so agility improves. Peak impact forces on joints scale by k.

**Drag.**
- At full output, drag force scales with v², which equals k. That is exactly the same fraction of muscle force as at baseline.
- Drag power scales with v³ (k^1.5), which matches muscle power.
- So drag takes the same share as in a normal human at sprint speed, about 8 to 13% of total energy cost based on Pugh's wind tunnel measurements.
- Drag would only outclass the enhanced body if speed rose faster than √k. It does bite at cruising pace (Part 5).

**Power (scales as k^1.5).** This is the core mismatch. Stamina scaled by k supplies k against a demand of k^1.5, a shortfall of √k.

**Heat (scales as k^1.5).** Cooling depends on skin area and sweat rate, which stay fixed unless they are also enhanced. Heat is the hardest wall.

**Tissue fatigue.** The fatigue life of bone and tendon falls steeply with stress. Cycles to failure scale with stress raised to roughly the −10th power in bone studies. Doubling the load cuts fatigue life by about 1,000×. Unless the skeleton and tendons scale too, the body breaks down long before fuel runs out.

## Part 4: Stamina Scenarios at Full Output (k = 2)

Let s be the stamina multiplier, with energy stores and supply rate scaled together.

- Full-output duration scales as s / k^1.5.
- Full-output distance or action count scales as s / k.

| Stamina | Time at full output | Distance or actions at full output | Phosphagen sprint (baseline 10 s) | Glycogen at proportional hard pace (baseline ~2 h) |
|---|---|---|---|---|
| ×1 | 0.35× | 0.5× | 3.5 s | 42 min |
| ×1.41 (scales with speed) | 0.5× | 0.71× | 5 s | 60 min |
| ×2 (scales with strength) | 0.71× | 1× | 7.1 s | 85 min |
| ×2.83 (scales with power) | 1× | 1.41× | 10 s | 2 h |

Power parity requires VO2max to rise from 55 to about 156 ml/kg/min, far above the human record of about 97. Cardiac output would need to rise from about 25 to about 70 L/min.

## Part 5: Sustained Cruising (Not Full Force)

Moving the same 70 kg body costs about the same per meter (about 4 J/kg/m metabolic) regardless of strength. Extra strength costs nothing until it is used.

Running metabolic power is approximately 280v + 0.58v³ W. The first term is the ground-contact cost and the second is drag, assuming CdA 0.24 m² and 25% efficiency.

| Aerobic power | Sustainable pace | Drag share | Heat to dump | Share of top speed |
|---|---|---|---|---|
| Baseline human (1,140 W) | 4.0 m/s (8.9 mph) | 3% | 855 W | 40% |
| ×1 (1,140 W) | 4.0 m/s (8.9 mph) | 3% | 855 W | 28% |
| ×1.41 (1,610 W) | 5.4 m/s (12.1 mph) | 6% | 1,210 W | 38% |
| ×2 (2,280 W) | 7.3 m/s (16.4 mph) | 10% | 1,710 W | 52% |
| ×2.83 (3,230 W) | 9.6 m/s (21.6 mph) | 16% | 2,420 W | 68% |

Running cost per meter rises above about 7 m/s, so the bottom two rows are optimistic.

**Drag is not the problem here.** With stamina ×2 the enhanced runner holds a larger share of top speed than a normal human, because body mass did not change.

**Heat is the binding constraint.** Maximum cooling is about 1,000 W in temperate conditions.
- At stamina ×2, the 710 W excess empties the 735 kJ heat buffer in about 17 minutes.
- At stamina ×2.83, the 1,420 W excess empties it in about 9 minutes.
- Without enhanced cooling, the heat-limited sustainable pace is about 4.6 m/s regardless of stamina.

**Water is also a limit.** Dumping 1,710 W requires evaporating 2.5 L/h of sweat, and 2,420 W requires 3.6 L/h. The gut absorbs only about 1 L/h, so dehydration follows quickly.

## Part 6: General Scaling by k

Top sprint speeds assume a 10 m/s baseline.

| Strength k | Top sprint speed | Power | Stamina for equal action count | Stamina for equal full-output time | Full-output time if stamina = k | Heat at full output |
|---|---|---|---|---|---|---|
| 2 | 14.1 m/s (32 mph) | 2.83× | 2× | 2.83× | 71% | 2.83× |
| 3 | 17.3 m/s (39 mph) | 5.2× | 3× | 5.2× | 58% | 5.2× |
| 4 | 20 m/s (45 mph) | 8× | 4× | 8× | 50% | 8× |
| 10 | 31.6 m/s (71 mph) | 31.6× | 10× | 31.6× | 32% | 31.6× |

## Bottom Line

When stamina scales the same way as strength (×k):

- **Kinetic energy and drag are matched.** The enhanced human performs the same number of full-power actions and covers the same distance at full output.
- **Power wins by √k.** Full output lasts 1/√k as long, which is 71% at k = 2.
- **Heat wins by k^1.5 against fixed cooling.** Overheating arrives within minutes at proportional effort. This is the dominant limit.
- **Connective tissue fails first.** Fatigue life drops by orders of magnitude.

Full parity requires several things to scale together:
- Energy supply rate and energy stores by k^1.5.
- Cooling capacity by k^1.5.
- Gut absorption by k^1.5 for output sustained over multiple days.
- Bone and tendon strength by at least k, with fatigue resistance well beyond that.

## What a stamina point is

```
SP = (Endurance × 10) + (Strength × 3) + (Agility × 3)
```

Street 15 / 15 / 15 is **240 SP**.

```
Rune or mana swap:     1 SP = 10 J
Anaerobic muscle work: 1 SP = 62.5 J above critical power
```

The 10 J peg matches mana. A 15 kJ untrained reserve is 1,500 of those joules-as-points, and the street bar is only 240, so anaerobic work is priced at one sixth. That is the fantasy multiplier. It is on the cost, not on the clock. Recovery stays the lab timing.

Critical power for that adult is **175 W** mechanical (**700 W** metabolic at 25% efficiency). The sheet's **375 W** at Agility 15 is the average power of building a sprint. A short all-out peak sits near **750 W**. Drain uses the peak.

The pool has two layers. The top layer is spent first. Both refill at once, at their own rates.

| Layer | Formula | Street adult | Fuel | Resting half-time |
|---|---|---|---|---|
| Burst | (Str + Agi) × 3 | 90 SP, the top of the bar (151 to 240) | Phosphocreatine | 30 s |
| Reserve | End × 10 | 150 SP, the bottom (1 to 150) | Glycolysis | 7 min |

```
Burst half-time = 15 s × (Str + Agi) / End
```

The reserve half-time stays **7 min** for every build. Endurance speeds how many reserve points come back per minute because the pool grew with it. It speeds the burst refill because the burst tank did not.

```
SP per second = (power − 175 W) / 62.5
```

Zero at or below 175 W.

| Street action | Mechanical power | Drain |
|---|---|---|
| All-out, while the burst layer lasts | 750 W | 9.2 SP/s |
| Hard sledge or warhammer drive, ~0.4 s, 200 to 400 J | ~500 to 1,000 W | about **4 SP** for a 300 J hit |
| 30 s all-out average | 500 W | 5.2 SP/s |
| At or below critical power | 175 W or less | 0 |

One full-power strike is about **2 SP** (750 W for 0.2 s). The 90-point burst layer covers about **50** of those, then the man is winded and later swings are not full power. A connected sledge lets the target take the energy. A miss still paid the ~4 SP swing, and the brake is extra load on the joints.

| Bar | Street SP | What he can still do |
|---|---|---|
| Fresh | 151 to 240 | Full peak |
| Winded | 76 to 150 | Peak capped near 65% |
| Burning | 1 to 75 | Peak capped near 50% |
| Spent | 0 | Stuck at 175 W until the bar is back to 10% (24 SP) |

## Recovery in a fight

The next full-power swing comes back fast. That fuel is the burst layer, half of whatever it lost every **30 s** he is not spending it. Mana takes hours. This does not.

The bar drops only during the swing itself. A pause, a step-off, or a walk starts the refill at once. Half-times stretch by `1 / (1 − f)` only while he is still working, and f is metabolic power divided by **700 W**. Standing in a fight is the 30 s row, not a frozen bar.

| Pause | Burst half-time | What that means |
|---|---|---|
| Standing | 30 s | Half the fresh tank back |
| Walk, 1.4 m/s | 43 s | Still inside a minute |
| Jog, 2 m/s | 2.6 min | Slower, still the fast layer |
| Mid-swing or a sprint | No refill during that effort | The pause after it counts |

Street adult, burst tank, from the moment he stops:

| Pause | Share of the missing burst back |
|---|---|
| 10 s | 21% |
| 20 s | 37% |
| 30 s | 50% |
| 60 s | 75% |
| 2 min | 94% |

- One sledge (**~4 SP**) is half back in **30 s** and fully back in about **2 min**.
- A 2.6 s flurry (**24 SP**) gives **5 SP** back in 10 s, **12** in 30 s, and the whole flurry in about **2.5 min**.
- Half the bar (**120 SP**) is **90** from the fast tank and **30** from the reserve. About **47 SP** is back in **30 s**, **90** in 2 min. He can swing hard again inside that first half minute.
- From empty, about **15 s** of rest puts **24 SP** back in the fast tank, which is enough to leave the spent cap and hit again. Science has that phosphocreatine tank full in **3 to 5 min**. The reserve under it clears over tens of minutes. Glycogen is a day or two and is not this bar.

The **7 min** half-time is only the reserve under the fresh tank, the acid and glycogen slice. It is not the clock on the next strike.
