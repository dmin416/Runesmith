# The Science of Running-Specific Prostheses ("Blades") and the Limits of Running Speed

> Earth invent loot. Blade spring physics, muscle and force-rate limits, research cases, animal comparisons, drag / traction ceilings, superhuman budgets. Not Caldris law. Human speed records: `HumanSpeed.md`. Grip / traction: `GripBiteBracing.md`. City vs forest ceilings: `TopSpeedCityVsForest.md`. G-force: `GForceTolerance.md`. Falling: `Falling.md`. Nav: `Index.md`.

Spring physics, muscle limits, speed limits, efficiency and whether anyone could use blades to run faster.

Part II (sections 13 to 22) compares cheetahs, kangaroos and ostriches, then works through the physical limits on human speed, air drag, traction, heat and what a superhuman runner would actually need.

---

## 0. Bottom Line

- A running blade is a passive carbon-fiber leaf spring. It stores energy when compressed and gives most of it back. It can never give back more than it receives. A biological ankle can, because muscle adds work on every step.
- Evidence to date says blades do **not** make a sprinter faster over 100 m. They cost acceleration, start speed, curve speed and peak ground force. They may help in specific ways: lighter swing leg, high energy return, no calf fatigue, possibly extra leg length.
- The open debate (Pistorius 2008, Leeper 2020) is mostly about the **400 m** and about **leg length**, not about the spring itself being "better than a leg."
- Long jump is the event where a blade looks closest to an advantage at takeoff. It still costs run-up speed.
- An able-bodied athlete gains nothing by amputation. Wearable spring devices (stilts, exoskeletons, super shoes) produce real but modest economy gains (roughly 4% to 15% in metabolic cost) and no proven sprint speed gain.
- The hard ceiling for any legged runner is how much force can be pushed into the ground during a very short contact. Springs do not raise that ceiling much. Muscles, tissue tolerance and control set it.

---

## 1. What a Running-Specific Prosthesis Is

### 1.1 Construction

| Component | Description |
|---|---|
| Spring element | Laminated carbon-fiber reinforced polymer (CFRP), dozens of plies of unidirectional and woven fiber in epoxy. Shaped as a "C" (sprint) or "J" (distance/general). |
| Socket | Custom carbon or thermoplastic shell molded to the residual limb. Uses a liner (silicone, gel) and suspension (pin lock, suction, vacuum). |
| Pylon/adapter | Short connector in some models. Sprint "C" blades often bolt directly behind the socket. |
| Sole | Rubber tread or bolted spike plate. |
| Mass | Blade roughly 0.5 to 1 kg. Full prosthesis with socket roughly 1.5 to 2.5 kg. |

Common models in research and competition:

- Össur Cheetah (Xtend, Xcel, Xplore): C-shape, sprint-oriented.
- Össur Flex-Run: J-shape, distance.
- Ottobock 1E90 Sprinter: C-shape sprint.
- Ottobock 1E91 Runner: distance.
- Fillauer/Freedom Innovations Catapult: J-shape.

### 1.2 Stiffness categories

Manufacturers sell each blade in numbered stiffness categories chosen by body mass and activity. Higher category means stiffer. Actual stiffness also changes with mounting height, alignment and how the load is applied. A 2016 study by Beck, Taboga and Grabowski tested 55 blades across models, categories and heights and showed stiffness varies with all of these, so the category label alone does not tell you the spring rate. A 2024 systematic review concluded manufacturers still do not report mechanical properties consistently.

### 1.3 Para classes that use them

| Class | Impairment |
|---|---|
| T61 | Bilateral above-knee, prostheses |
| T62 | Bilateral below-knee, prostheses |
| T63 | Single above-knee, prosthesis |
| T64 | Single below-knee (or equivalent), prosthesis |
| T42 to T44 | Similar impairments competing without prosthesis |

---

## 2. The Physics: Running as a Bouncing Spring

### 2.1 The spring-mass model

Human running is modeled as a point mass bouncing on a massless spring (the "leg spring"). During the first half of stance the body falls, the leg compresses and stores energy. During the second half the leg extends and returns it.

Core quantities:

```
Leg stiffness:        k_leg  = F_max / ΔL
Vertical stiffness:   k_vert = F_max / Δy
Leg compression:      ΔL = Δy + L0 (1 − cos θ)
Half sweep angle:     θ = arcsin( v · t_c / (2 · L0) )
Contact time (approx, vertical bounce):   t_c ≈ π · sqrt( m / k_vert )
Elastic energy stored:                    E = F² / (2k) = ½ k x²
Hysteresis (fraction lost):               H = (E_in − E_out) / E_in
```

Where `F_max` is peak vertical ground force, `Δy` is center of mass drop, `L0` is resting leg length, `v` is forward speed, `t_c` is contact time and `m` is body mass.

Typical human values:

| Quantity | Jogging (~3 m/s) | Elite sprint (~11 to 12 m/s) |
|---|---|---|
| Contact time | 0.25 to 0.30 s | 0.08 to 0.10 s |
| Peak vertical force | 2.5 to 3 × body weight | 4 to 5+ × body weight |
| Leg stiffness | ~10 to 20 kN/m | rises with speed (vertical stiffness rises sharply) |
| Steps per second | ~2.7 to 3 | ~4.5 to 5 |

### 2.2 Worked example: one blade step

Sprinter, 75 kg (735 N body weight), top-speed peak vertical force 4 × BW:

```
F_max = 4 × 735 N ≈ 2,940 N
Blade compression ≈ 7 cm  →  k ≈ 2,940 / 0.07 ≈ 42 kN/m
Stored energy E = F² / (2k) = 2,940² / 84,000 ≈ 103 J
At 90% return: ~93 J returned, ~10 J lost as heat
At ~2.3 blade contacts per second (bilateral ~4.6): ~23 to 46 W of heat per runner
```

That ~100 J per contact is comparable to the total fluctuation in the body's mechanical energy per step during fast running. A blade really can carry most of the bounce.

### 2.3 What the spring cannot do

1. **No net positive work.** Energy out ≤ energy in. Every cycle loses some energy to hysteresis.
2. **No timing control.** A passive spring releases energy at a rate set by its stiffness and the mass on it. It cannot "push harder late in stance" the way a calf does.
3. **No stiffness adjustment.** Biological legs retune stiffness every step for speed and surface (Ferris and colleagues showed runners compensate almost perfectly for soft versus hard surfaces). A blade is fixed. The athlete can only adjust through knee and hip.
4. **No sensing.** No ankle proprioception, no cutaneous feedback from the sole.

The biological ankle has the opposite profile. Beck's group notes that at 2.8 m/s the intact ankle appears to return about 241% of the energy it stores. The extra 141% is muscle work added on top of tendon recoil. That gap is the single most important difference between a leg and a blade.

---

## 3. Energy Return and Hysteresis

### 3.1 Measured values

| Structure | Energy return | Notes |
|---|---|---|
| Carbon running blades | ~63% to 95% reported across studies; lab tests often 85% to 95% | Varies with model, load rate, test method |
| Old SACH prosthetic foot | Very poor | Foam heel, damping by design |
| Human tendon (Achilles, etc.) | ~90% to 95% | 5% to 10% hysteresis |
| Human ankle joint overall (with muscle) | Can exceed 100% "return" | Muscle adds work |
| Super-shoe PEBA foam | ~85% to 90% | Nike ZoomX class foams |
| EVA midsole foam | ~65% to 75% | Older trainer foam |
| Natural rubber | ~80% to 90% | Rate and temperature dependent |
| Resilin (insect protein) | ~97% | Best known biological spring |

### 3.2 Where energy is lost in a blade

- Internal friction in the epoxy matrix (viscoelastic).
- Micro-slip between plies and at fiber-matrix interfaces.
- Sole/tread rubber compression.
- Socket and liner: soft tissue of the residual limb compresses and shears inside the socket. This damping is often larger than the blade's own hysteresis and is rarely included in "energy return" marketing.
- Vibration after toe-off.

### 3.3 Energy density: why carbon fiber and why tendon

Strain energy per unit volume at a given stress:

```
U = σ² / (2E)
```

Practical comparison (ideal uniform tension, rough values):

| Material | Stress used | Modulus E | Density | Energy at that stress |
|---|---|---|---|---|
| Spring steel | ~1,000 MPa | 200 GPa | 7,850 kg/m³ | ~2.5 MJ/m³ → ~0.3 kJ/kg |
| Titanium alloy (Ti-6Al-4V) | ~900 MPa | 114 GPa | 4,430 kg/m³ | ~3.6 MJ/m³ → ~0.8 kJ/kg |
| Unidirectional CFRP (near failure) | ~1,500 MPa | 135 GPa | 1,550 kg/m³ | ~8.3 MJ/m³ → ~5.4 kJ/kg |
| CFRP at fatigue-safe stress (~⅓ of failure) | ~500 MPa | 135 GPa | 1,550 kg/m³ | ~0.9 MJ/m³ → ~0.6 kJ/kg |
| Tendon near failure | ~100 MPa | ~1.2 to 1.5 GPa | ~1,120 kg/m³ | ~3.5 to 4 MJ/m³ → ~3 to 3.7 kJ/kg |
| Tendon at running stress (~50 MPa) | ~50 MPa | ~1.2 to 1.5 GPa | ~1,120 kg/m³ | ~1 MJ/m³ → ~0.8 to 0.9 kJ/kg |
| Natural rubber (large strain) | n/a | very low | ~930 kg/m³ | can exceed several kJ/kg |

Key points:

- **Bending wastes material.** A leaf spring loaded in bending stresses only its outer fibers fully. A rectangular cantilever with an end load uses roughly 1/9 of its volume as effectively as a bar in uniform tension. That is why blades weigh far more than the theoretical minimum.
- **Fatigue sets the real limit.** A blade must survive millions of cycles. Design stresses sit far below failure stress. Energy scales with stress squared, so cutting stress to one third cuts stored energy to one ninth.
- **Tendon is extraordinary.** Per kilogram at working stress it is in the same class as carbon fiber at working stress, with low hysteresis, self-repair and in-series muscle that tunes it. Tendons run at low safety factors (roughly 1.5 to 3) that no engineer would accept in a prosthesis.

### 3.4 How much energy biology already recycles

Classic measurements (Ker, Alexander and colleagues, 1987) for a ~70 kg runner at ~4.5 m/s:

- Achilles tendon stores ~35 J per step.
- The arch of the foot stores ~17 J per step.
- Together roughly half the mechanical energy needed per step is recycled elastically.

Cavagna and others found the "apparent efficiency" of running (mechanical work done divided by metabolic energy) is 40% to 70%+, far above the ~25% maximum efficiency of muscle doing positive work. The difference is elastic recoil. Humans are already spring-legged.

**Implication:** Replacing a tendon-calf-foot unit with a carbon spring does not unlock a large pool of "free" energy. The pool was already being recycled. The blade wins on lightness and loses on active power.

---

## 4. Muscles: The Real Limits

### 4.1 Muscle performance numbers

| Property | Approximate value |
|---|---|
| Max isometric stress | ~25 to 35 N/cm² (250 to 350 kPa) |
| Max shortening velocity (fast fibers) | ~6 to 10 fiber lengths per second |
| Peak power output | roughly 200 to 400 W per kg of muscle |
| Efficiency of positive work | ~20% to 25% max |
| Cost of negative (eccentric) work | roughly 1/3 to 1/5 of positive work cost |
| Force at high shortening speed | falls toward zero (Hill force-velocity curve) |

### 4.2 The force-velocity problem

Muscle force drops as shortening speed rises. At top sprint speed, contact lasts under 0.1 s. A muscle that had to shorten quickly through the whole stance would produce little force. Tendons solve this: the muscle stays near-isometric (high force, low cost) while the tendon stretches and recoils (high speed). This is the "catapult" mechanism.

A blade does the tendon's job for the lost shank. It cannot do the muscle's job. Muscle mass that remains (hip extensors, knee extensors, hamstrings) must supply all net positive work and must do it through the knee and hip.

### 4.3 The cost-of-force hypothesis

Kram and Taylor (1990): metabolic cost of running scales with body weight divided by contact time.

```
E_metab / time ∝ W_body / t_c
```

Shorter contacts require faster, more costly muscle fibers. A softer spring lengthens contact, lowering this cost. That is exactly what Beck's 2017 study found for bilateral amputees: **reduced prosthetic stiffness lowered metabolic cost**, while longer prosthetic height did not help distance economy.

### 4.4 Why top speed is a force-in-time problem

Weyand and colleagues (2000, 2010) showed:

- Swing time (repositioning the leg) is nearly the same in slow and fast runners, about 0.34 to 0.37 s.
- Faster runners are faster because they apply **more vertical force in less contact time**.

Speed identity:

```
v = step frequency × step length
Top-speed model (Weyand):  v ≈ (F_avg / W_body) × L_c × f_step
```

Where `L_c` is contact length (distance the body travels during stance).

Weyand's 2010 study found humans produce greater ground forces during one-legged forward hopping than during top-speed running. Muscle can generate more force than sprinting uses. The limit is how fast muscle can generate that force within a ~0.09 s contact. The authors speculated humans could theoretically reach roughly 35 to 40 mph (16 to 18 m/s) if that speed-of-force limit were removed.

**For blades:** a passive spring does not raise the rate of force development. It reduces it in practice because the knee and hip must drive force through a compliant element with no ankle push.

---

## 5. What Research Says About Blades and Speed

### 5.1 Oscar Pistorius (bilateral below-knee, 400 m)

- 2007: IAAF-commissioned tests (Brüggemann, Cologne) concluded Pistorius used less energy at submaximal constant speed and the blades returned energy more efficiently than intact ankles. IAAF banned him.
- 2008: CAS overturned the ban. Reasons included that testing covered only straight-line steady running, not start, acceleration or full race demands.
- 2009: Weyand and colleagues published detailed measurements. Compared with intact sprinters at top speed, Pistorius had about 14% longer contacts, about 34% shorter aerial times, about 21% faster swing times and about 23% lower stance-averaged vertical forces. Metabolic cost was in the normal range for trained runners.
- 2010 debate (Journal of Applied Physiology, point/counterpoint):
  - **Weyand and Bundle:** the faster swing (lighter distal limbs) plus lower force needs amounted to a large advantage, estimated at seconds over 400 m.
  - **Kram, Grabowski, McGowan, Brown and Herr:** lower ground force is a **disadvantage** because force limits speed. Swing time was not the cause of the speed. No advantage was demonstrated.
- The scientific community never fully settled it.

### 5.2 Unilateral amputee sprinters (T64, T44)

- Grabowski and colleagues (2010): the prosthetic leg produced roughly 9% lower average vertical ground force than the intact leg at top speed. The prosthesis limits force and therefore speed.
- Prosthetic legs compensate with higher hip work.
- Curve running: athletes with a prosthesis on the inside (left) leg run slower on curves. Blades cannot generate the inward lateral forces an ankle and foot can.
- Block starts and acceleration: slower. Acceleration requires large net positive horizontal impulse, which a passive spring cannot add.

### 5.3 Blake Leeper (bilateral, 400 m)

- World Athletics found his blades gave a leg length of 104 cm and a standing height of 184 cm, exceeding the Maximum Allowable Standing Height (MASH) predicted for his body.
- 2020 CAS ruling:
  - Struck down the rule placing the burden of proof on the disabled athlete. World Athletics now must prove an advantage.
  - Upheld the ban on his specific blades because they let him run several inches taller than his maximum possible intact height.
- Leeper's team argued MASH was derived from data that underrepresented Black athletes' body proportions. World Athletics rejected this.

### 5.4 Markus Rehm (single below-knee, long jump)

- T64 world record 8.72 m. Won his eighth world title in New Delhi 2025 with 8.43 m, longer than the 8.39 m that won the 2025 World Athletics Championships.
- Willwacher and colleagues (2016) compared Rehm with elite non-amputee jumpers. Rehm approached the board slower but converted horizontal speed into vertical lift more effectively at takeoff on his blade. The run-up disadvantage and takeoff advantage could not be netted into a clear overall conclusion.
- Denied Olympic entry because he could not prove no overall advantage under the old burden-of-proof rule.

Why long jump is different: takeoff is a single violent compression and rebound. A stiff spring with low hysteresis and a long lever is very good at that one event. The run-up still needs acceleration and top speed, which blades handicap.

### 5.5 Distance running

- Beck et al. (bilateral): softer blades lowered metabolic cost. Taller blades did not help economy.
- Beck et al. (unilateral): blade model mattered (the Ottobock 1E90 Sprinter lowered cost compared with others), stiffness and height did not.
- Blade users' running economy falls within the range of non-amputee runners. No consistent economy advantage.

### 5.6 Performance gaps (records)

| Event | Blade record | Olympic-class record | Gap |
|---|---|---|---|
| 100 m (T64, single blade) | 10.61 s (Richard Browne 2015; tied by Sherman Guity 2026) | 9.58 s | ~10.7% slower |
| 100 m (T62, bilateral) | 10.54 s (Johannes Floors 2019) | 9.58 s | ~10.0% slower |
| 400 m (T62, bilateral) | 45.70 s (Hunter Woodhall 2025) | 43.03 s | ~6.2% slower |
| Long jump (T64) | 8.72 m (Markus Rehm) | 8.95 m | ~2.6% shorter |

The pattern matches the physics:

- **100 m:** worst gap. Start and acceleration depend heavily on ankle power.
- **400 m:** smaller gap. Acceleration is a small fraction of the race. Elastic economy, swing speed and the absence of calf fatigue matter more.
- **Long jump:** smallest gap. Single spring-dominated takeoff.

Note the pool of elite blade athletes is tiny compared with the global sprint pool, which inflates all of these gaps.

---

## 6. Specific Advantages and Disadvantages of Blades

### 6.1 Possible advantages

| Factor | Mechanism | Size of effect |
|---|---|---|
| Lighter distal limb | Biological shank plus foot is ~6% of body mass (~4.5 kg for 75 kg). Blade side is lighter. Lower moment of inertia means faster, cheaper swing. | Real. Disputed whether it matters for top speed. |
| No calf fatigue | Carbon does not accumulate metabolites or lose force over 400 m. | Plausible late-race benefit. Unquantified. |
| Leg length | Longer legs increase contact length L_c, giving more time to apply force at the same speed. | Real. Basis of MASH rule. |
| Low hysteresis at takeoff | Stiff spring rebound for a single jump. | Seen in long jump takeoff. |
| Consistent stiffness | Does not soften with fatigue. | Minor. |

### 6.2 Disadvantages

| Factor | Mechanism |
|---|---|
| No ankle push-off | Zero net positive work from the device. Hip and knee must supply all propulsion. |
| Slow starts and acceleration | Acceleration demands net horizontal impulse a passive spring cannot add. |
| Lower peak ground force | Documented ~9% lower on the affected side for unilateral sprinters. Force sets top speed. |
| Curve running | Poor lateral force generation and stability on the inside leg. |
| Socket interface | Soft tissue damping, pain, skin breakdown, volume changes, sweat, loss of suspension. |
| No proprioception | Harder balance control, uneven surfaces, foot placement. |
| Fixed stiffness | Cannot retune per stride, per speed, per surface. |
| Asymmetry (unilateral) | Mismatched step timing and force between legs. |
| Above-knee | Prosthetic knee adds a large control and power deficit. T61/T63 times are much slower. |

---

## 7. Could an Able-Bodied Athlete Use Something Like It to Run Faster?

### 7.1 Elective amputation

No. Every measured variable that limits sprint speed gets worse: peak force, acceleration, curve speed, balance. Long-term risks include residual limb pain, skin injury, bone overgrowth, neuroma, osteoarthritis in remaining joints and lower back stress from asymmetry. World Athletics Technical Rule 6.3.4 bars mechanical aids unless they give no overall advantage, so even a hypothetical gain would not be legal in able-bodied competition.

### 7.2 Spring stilts strapped over the leg (jumping stilts, "Powerisers," "bionic boots")

Physics:

- They add leg length and a big leaf spring below the foot.
- They put large mass far from the hip, which raises swing inertia sharply.
- The lever arm from ground to knee grows, raising knee and ankle torques and injury risk.
- The ankle is locked inside the device, so ankle muscles contribute little.

Results: they do increase hop height and bounding stride. Marketing claims of very high speeds exist for some designs. No controlled study has shown them beating elite unassisted sprint times. They are a recreation device.

### 7.3 Exoskeletons

| Device | Result |
|---|---|
| Unpowered ankle exoskeleton, walking (Collins et al. 2015) | ~7% lower metabolic cost |
| Exotendon connecting the legs, running (Simpson et al. 2019) | ~6% lower metabolic cost |
| Powered ankle exoskeleton, running (Witte et al. 2020) | ~15% lower cost. Unpowered spring version did not help. |
| Soft hip exosuit, running (Kim et al. 2019) | ~4% lower cost |

Critical lesson from the running exoskeleton work: **adding a passive spring at the ankle of an intact runner did not help**, because the intact Achilles is already a good spring. Adding external power did help. The bottleneck is positive work, not elastic storage.

### 7.4 Super shoes (the legal mini version)

- Carbon plate plus high-return PEBA foam plus tall stack.
- Lab studies (Hoogkamer et al. 2018): about 4% average reduction in metabolic cost at distance running speeds.
- Mechanisms: foam returns more energy than older foams, the plate stiffens the toe joint, changes ankle lever mechanics and reduces wasted work at the toes.
- World Athletics now limits stack height (40 mm road, 20 mm for track events under 800 m, 25 mm for 800 m and longer).
- Sprint spikes with plates and foams help a little. Sprint times did not jump the way marathon times did. Sprinting is force-rate limited, not economy limited.

### 7.5 Powered prostheses

A powered ankle could in principle exceed biological power:

- Battery energy density ~250 Wh/kg ≈ 900 kJ/kg.
- Motor power density can reach several kW/kg.

The ceiling then moves to:

- **Socket tissue tolerance.** Skin and soft tissue tolerate limited pressure and shear. Peak sprint forces of 4 to 5 × body weight pass through a residual limb.
- **Bone-anchored (osseointegrated) limbs** remove the socket but transfer bending and torsion straight into bone. Fracture and implant loosening limit loading.
- **Remaining joints.** Knee ligaments, cartilage and hip structures must carry the extra force.
- **Control.** Timing torque within a ~90 ms contact requires sensing and actuation faster than current systems manage reliably at sprint speed.
- **Rules.** Powered devices are banned in both Olympic and Paralympic athletics.

---

## 8. Theoretical Speed Limits of a Spring-Legged Runner

### 8.1 What a perfect spring buys

Imagine a spring leg with 100% return, zero mass and ideal stiffness. Steady-speed running still requires:

1. **Holding force.** Muscles must still produce force to keep the knee and hip from collapsing. Force costs energy even with zero work (cost-of-force hypothesis).
2. **Swing.** The leg must be repositioned 4 to 5 times per second at sprint speed.
3. **Air drag.** Power ≈ ½ ρ C_dA v³. At 10 m/s with C_dA ≈ 0.24 m²: about 140 W. At 12 m/s: about 250 W.
4. **Control losses.** Foot placement errors, collisions, braking impulse at touchdown.

A perfect spring lowers steady-state cost. It does not raise top speed by itself, because top speed is set by how hard you can hit the ground in the time available.

### 8.2 What changes top speed

From `v ≈ (F_avg / W) × L_c × f_step`:

| Lever | How a device could change it | Catch |
|---|---|---|
| F_avg / W | Powered actuation | Tissue and joint limits, control |
| L_c (contact length) | Longer leg | MASH rule, stability, swing inertia |
| f_step | Lighter leg, faster swing | Swing time is already near a biological floor |
| Contact time window | Softer spring lengthens it | Longer contact at same force means lower speed unless force rises |

### 8.3 Stiffness trade-off

- **Too soft:** large compression, long contact, the center of mass sinks, the leg sweeps too far, braking increases.
- **Too stiff:** short contact, very high peak force required, little elastic storage, impact loads climb.
- **Optimal:** matched to body mass, speed and the athlete's hip/knee strength. Humans hit this automatically. Blade users need the right category and fit. The optimum for the start differs from the optimum for top speed.

### 8.4 Upper-bound estimates

- Fastest recorded human: ~12.4 m/s peak (Bolt, 2009).
- Weyand's force-rate argument: muscles theoretically could support ~16 to 18 m/s if force could be applied faster.
- A passive spring does not change the force-rate limit, so the realistic ceiling for passive blades sits at or below the intact human ceiling.
- A powered device could theoretically go past it. Tissue and control limits would arrive first.

---

## 9. Efficiency Summary

| System | Approximate figure |
|---|---|
| Muscle, positive work | ~20% to 25% efficient |
| Whole-body running "apparent efficiency" | ~40% to 70%+ (because of elastic recoil) |
| Human metabolic cost of running | ~4 J per kg per meter (about 1 kcal per kg per km), nearly speed-independent at distance speeds |
| Carbon blade energy return | ~85% to 95% (device alone) |
| Blade users' running economy | Within the normal non-amputee range |
| Super shoes | ~4% metabolic savings |
| Powered ankle exoskeleton (running) | ~15% metabolic savings |

---

## 10. Materials and Design Frontiers

- **Variable-stiffness blades:** mechanisms that shift stiffness between acceleration and top speed. Banned in competition if powered. Passive variants remain experimental.
- **Tuned laminate layups:** ply angles that couple bending and twisting to improve curve running.
- **Lighter sockets and better liners:** reduce interface damping, which can waste more energy than the blade.
- **Osseointegration:** removes the socket, improves control and feedback (osseoperception). Long-term durability under sprint loads is not established.
- **Neural interfaces (agonist-antagonist myoneural interface surgery, Herr and colleagues):** restore a sense of ankle position for powered prostheses. Currently aimed at walking and daily life.
- **Better testing standards:** the 2024 review called for standardized reporting of stiffness and hysteresis under running-relevant loads.

---

## 11. Rules Snapshot

| Rule | Content |
|---|---|
| World Athletics Technical Rule 6.3.4 | Mechanical aids prohibited unless no overall competitive advantage. After CAS 2020 the federation carries the burden of proof. |
| MASH (Maximum Allowable Standing Height) | Para athletics limit on prosthetic standing height, calculated from intact body segment dimensions. Applied by World Athletics in Leeper's case. |
| Pistorius CAS 2008 | Ban overturned. He ran the 400 m at the 2012 Olympics. |
| Leeper CAS 2020 | Burden-of-proof rule struck down. His specific blades still barred for exceeding height limits. |
| Para athletics | Passive devices only. No powered prostheses. |
| Shoe stack limits | 40 mm road, 20 mm track under 800 m, 25 mm track 800 m and up. |

---

## 12. Key Takeaways

1. A blade is a very good spring and a very bad muscle.
2. Humans already recycle roughly half of running energy through tendons. The blade does not access a hidden energy reserve.
3. Blades lose most in acceleration and sprinting, lose less in the 400 m and come closest to parity in long jump takeoff.
4. The genuine advantage arguments are lighter swing limbs, no calf fatigue and extra leg length.
5. Able-bodied athletes gain nothing from amputation. Exoskeletons and super shoes give 4% to 15% economy gains, not sprint speed.
6. Top speed for any legged runner is limited by how fast force can be pushed into the ground. Only powered systems could move that limit. Human tissue tolerance becomes the next wall.

---

# PART II: Animals, Human Limits, Drag and Superhumans

---

## 13. Nature's Spring Runners: Overview

| Trait | Human (elite sprinter) | Cheetah | Red kangaroo | Ostrich |
|---|---|---|---|---|
| Body mass | ~75 to 95 kg (Bolt ~94 kg) | ~35 to 65 kg | Large males up to ~85 kg | ~100 to 150 kg |
| Top speed | 12.4 m/s (44.7 km/h, 27.8 mph), Bolt 2009 | 25.9 m/s measured in the wild (58 mph); ~29 m/s (65 mph) claimed in captivity | Roughly 15 to 19 m/s reported (field estimates) | Over 19 m/s (70+ km/h) |
| Long-distance pace | 5.88 m/s average for the 1:59:30 marathon (Sawe, 2026) | Sprint lasts a few hundred meters | Cruises economically at moderate hopping speeds | ~60 km/h (16.7 m/s) steady running |
| Gait | Bipedal run | Rotary gallop, two flight phases per stride | Bipedal hop (pentapedal "five-leg" walk at slow speed) | Bipedal run on two toes |
| Main springs | Achilles tendon, foot arch | Leg tendons, flexing spine | Massive ankle tendons | Long digital flexor tendons, toe joint |
| Distal leg mass | Heavy (calf muscle low on leg) | Light | Light lower leg, heavy tail and thighs | Very light (muscle packed at hip and thigh) |
| Defining strength | Endurance, heat dumping, versatility | Acceleration and turning | Speed-independent energy cost | Economy plus speed, huge stride |

Approximate Froude numbers at top speed (Fr = v² / (g × leg length)), a dimensionless measure of how fast an animal runs for its size:

| Runner | Leg length (approx.) | Top speed | Froude number |
|---|---|---|---|
| Human | ~1.0 m | 12.4 m/s | ~16 |
| Kangaroo | ~0.7 m | ~16 m/s | ~37 |
| Ostrich | ~1.2 m | ~19.4 m/s | ~32 |
| Cheetah | ~0.8 m | 25.9 m/s | ~85 |

Walking becomes impossible near Fr ≈ 0.5 for almost every animal (the body would leave the ground over the vaulting leg). Above that, everything runs or hops. Humans sit far below the others in size-corrected top speed.

---

## 14. The Cheetah: Built for Acceleration

### 14.1 Measured performance

Wilson and colleagues (Nature, 2013) fitted wild Botswana cheetahs with GPS and inertial collars recording five times per second.

- Top speed recorded in the wild: 25.9 m/s (58 mph).
- Most hunts ran at about half of top speed. The hunts were won by acceleration, braking and turning.
- Acceleration was far greater than Bolt's. Mass-specific muscle power reached roughly 120 W per kg of body mass, around four times an elite human sprinter's.
- Braking was as violent as acceleration.

Speed is not the main weapon. The ability to change speed and direction faster than an antelope is.

### 14.2 Anatomy

| Feature | Function |
|---|---|
| Flexible spine | Flexes and extends each stride like a bow, adding stride length and storing elastic energy. Adds several meters to each stride. |
| Rotary gallop with two flight phases | One flight phase gathered (legs under the body), one extended. Stride length around 7 m at speed. |
| Semi-retractable claws | Act like cleats. Raise effective friction so the cheetah can push and turn harder than a smooth foot allows. |
| Hard footpads with ridges | Grip, like tire tread. |
| Long heavy tail | Counter-rotates the body in turns. Works like a rudder and reaction wheel. |
| Light build, small head | High power-to-mass ratio. |
| High proportion of fast-twitch fibers | Huge power, poor endurance. |
| Enlarged nasal passages, large heart and lungs | Rapid oxygen delivery and recovery after the sprint. |
| Light distal limbs | Fast, cheap leg swing. |

### 14.3 What limits the cheetah

- **Anaerobic fuel.** The sprint burns stored muscle energy. Chases end within a few hundred meters.
- **Traction.** Even claws have a ceiling. Turning at speed is friction-limited.
- **Structural strength.** Light bones trade safety for speed. Injuries end hunting careers.
- **Not overheating, mostly.** The old idea that cheetahs abandon chases because of heat has been challenged by body-temperature studies in the wild. Stress after the hunt raised body temperature more than the run itself.

### 14.4 Lessons for humans

A human cannot gallop usefully. Bipeds have no spine-flex stride extension, no front legs for propulsion and a heavy upright trunk. The cheetah's advantages come from body plan, not from a better spring.

---

## 15. The Kangaroo: The Energy Cheat

### 15.1 The famous result

Dawson and Taylor (Nature, 1973) put red kangaroos on a treadmill. Oxygen consumption did **not** rise as hopping speed increased over the measured range. It even fell slightly. In almost every other animal, energy use climbs with speed.

Kram and Dawson (1998) confirmed it: oxygen consumption stays nearly constant as level hopping speed increases, cost of transport falls at faster speeds, muscle efficiency is about 30% (normal) and maximal oxygen uptake during uphill hopping reached about 3 ml O₂ per kg per second, higher than nearly any other vertebrate.

### 15.2 How

- **Constant hop frequency.** A kangaroo speeds up mainly by hopping farther, not more often. Since much of the cost of running depends on how often muscles must activate, keeping frequency fixed holds cost flat.
- **Massive tendons in series with short muscles.** The ankle extensor tendons stretch and recoil each hop. Muscles stay short and nearly isometric (cheap force).
- **Posture shift.** A 2025 eLife study (Thornton, Clemente and colleagues) used 3D musculoskeletal models of red and grey kangaroos. At higher speed the hindlimb crouches more at the ankle and toe joints. The ankle's effective mechanical advantage falls, so the tendon is stretched harder and stores and returns more energy per hop. Net muscle work at the ankle stays roughly constant across speeds.
- **Tail.** At slow speed the tail acts as a fifth leg. At speed it balances the body.
- **Breathing coupled to hops.** Gut movement pumps air in rhythm with each bounce.

### 15.3 The limit

Kangaroos pay with structural risk. Large kangaroo tendons operate close to their breaking stress (low safety factor). Bigger kangaroos would snap tendons. This is a strong argument that very large extinct kangaroos could not have hopped quickly.

### 15.4 Lessons for humans

- Humans cannot hop efficiently over distance. Our tendons are too short relative to our muscles and our muscles sit too low on the leg.
- The kangaroo shows the best case for "spring legs": energy cost nearly independent of speed. It requires an entire body redesigned around the spring, not a spring added to a human leg.

---

## 16. The Ostrich: The Best Biped

### 16.1 Performance

- Top speed above 70 km/h (about 19.4+ m/s). Steady running around 60 km/h.
- Step length up to about 5 m, the longest of any running bird.
- At its steady pace an ostrich would cover a marathon in roughly 40 minutes.

### 16.2 Energy economy

Rubenson and colleagues (Journal of the Royal Society Interface, 2010/2011) compared ostriches with humans at matched conditions:

- Ostrich tendons store and return about **twice** as much elastic energy per step as human tendons.
- Walking cost was similar between the species. Running cost for ostriches was nearly **50% lower** than for humans.

### 16.3 Anatomy

| Feature | Function |
|---|---|
| Muscle packed at the hip and thigh | Distal leg is mostly bone and tendon. Very low swing inertia. |
| Long tendons running to the toes | Large elastic storage. |
| Two toes, one dominant | Reduced foot mass. A hoof-like contact. Claw pressure can reach roughly 40 kg/cm² during running. |
| Long legs relative to body | Long contact length, long stride. |
| Passive ankle stability | A dissected leg needed about 14 kg of downward force before the ankle collapsed. The bird can stand with little muscle effort. |
| Extra joint in the effective leg | Birds stand on their toes, so the long tarsometatarsus acts as an extra leg segment. |

### 16.4 Lessons for humans

The ostrich is the closest real-world example of what a "blade runner" design aims at: light distal limb, big tendons, power at the hip. It achieves it with tendons attached to muscles that can still add work. The design is also what a human with bilateral blades partially imitates, minus the muscle-driven toe push.

---

## 17. Other Fast Runners

Approximate published or commonly cited values. Field speeds vary with measurement method.

| Animal | Approx. top speed | Notes |
|---|---|---|
| Pronghorn | ~25 m/s bursts | Exceptional endurance at high speed. Very high aerobic capacity for its size. |
| Quarter Horse | ~24 m/s over short distance | Bred for the quarter mile. |
| Thoroughbred | ~19 to 20 m/s in races | Huge heart and spleen-boosted blood oxygen. Light lower legs with long tendons, like the ostrich. |
| Greyhound | ~18 to 19 m/s | Rotary gallop like the cheetah. Less spine flex and power. |
| Human | 12.4 m/s | Slow sprinter. Elite endurance runner. |

### Endurance flips the ranking

Humans are poor sprinters but rank among the best mammals at long-distance running in heat (Bramble and Lieberman, 2004):

- Profuse sweating and little body hair.
- Long Achilles tendon and arched foot springs.
- Nuchal ligament stabilizing the head.
- Large gluteus maximus for trunk stability.
- Breathing not locked to stride.

Persistence hunting (running prey into heat exhaustion) depends on these traits. Humans have beaten horses in long trail races such as Wales's Man versus Horse marathon.

---

## 18. Limits on Human Running Speed

### 18.1 Where human speed is today

- 100 m: 9.58 s (Bolt, 2009). Still standing as of 2026.
- Peak speed in that race: about 12.4 m/s.
- Marathon: 1:59:30 (Sabastian Sawe, London 2026). First official sub-two-hour marathon. Average speed 5.88 m/s.

### 18.2 What sets the sprint limit

| Limit | Explanation |
|---|---|
| Contact time | At top speed the foot is down less than 0.1 s. All support force must be applied in that window. |
| Rate of force development | Muscles can produce more force than sprinting uses (hopping tests prove it). They cannot produce it fast enough. |
| Swing time floor | Leg repositioning takes about 0.34 s or more in fast and slow runners alike. Step frequency is capped near 5 per second. |
| Muscle fiber speed | Fast-twitch fibers shorten at about 10 lengths per second at most. |
| Tendon and bone strength | Peak forces of 4 to 5 × body weight already use a good share of skeletal safety margin. |
| Anaerobic fuel | Phosphocreatine stores fade within seconds. Even Bolt slowed in the final 20 m. |
| Traction | Spikes help. Horizontal force is still friction-limited during the start. |

### 18.3 Predictions

- Statistical extrapolations of record progressions (for example Denny, 2008) suggested a human 100 m limit around 9.48 s.
- Weyand's force-rate analysis suggests human muscles could theoretically support ~16 to 18 m/s if they could apply force faster.
- Modern spike technology analyses have estimated Bolt might have run around 9.4 s with current shoes. That figure is hypothetical.

### 18.4 Robots are already there

- Unitree's humanoid "Superman" was reported in 2026 at a peak of 12.66 m/s (45.6 km/h), above Bolt's peak.
- Boston Dynamics' Cheetah quadruped reached about 28 mph (12.7 m/s) on a treadmill in 2012.
- Robots have motors that do not fatigue, no swing-time biology and can be repaired. They run into the same traction and drag physics as humans.

---

## 19. Air Drag

### 19.1 The equations

```
Drag force:   F_d = ½ ρ C_d A v²
Drag power:   P_d = F_d × v = ½ ρ C_d A v³
Dynamic pressure:  q = ½ ρ v²
```

- ρ (air density) ≈ 1.2 kg/m³ at sea level.
- C_d A (drag area) for an upright runner ≈ 0.25 to 0.4 m². Value used below: 0.3 m².
- Drag power scales with **speed cubed**. Double the speed, eight times the power.

### 19.2 Drag at different speeds (C_d A = 0.3 m², sea level)

| Speed | Context | Drag force | Drag power |
|---|---|---|---|
| 5 m/s | Easy run | 4.5 N | 23 W |
| 5.9 m/s | Sub-2 marathon pace | 6.3 N | 37 W |
| 10 m/s | Fast sprint | 18 N | 180 W |
| 12.4 m/s | Bolt peak | 28 N | 343 W |
| 20 m/s | Ostrich range | 72 N | 1.44 kW |
| 25.9 m/s | Wild cheetah peak (human body) | 121 N | 3.1 kW |
| 50 m/s | 112 mph | 450 N | 22.5 kW |
| 100 m/s | 224 mph | 1,800 N | 180 kW |
| 200 m/s | 447 mph | 7,200 N | 1.44 MW |
| 343 m/s | Speed of sound | ~21 kN (more in reality) | ~7.3 MW (more in reality) |

Near and above the speed of sound, compressibility raises the drag coefficient sharply (wave drag), so the last row is a minimum.

### 19.3 Drag in real races

- Classic wind-tunnel work (Pugh, 1970s) estimated drag takes about 4% of total energy at middle-distance speeds and close to 8% in sprinting.
- **Tailwind:** a legal +2.0 m/s tailwind is worth roughly 0.1 s in the 100 m.
- **Altitude:** air at Mexico City (2,240 m) is about 20% thinner. Sprint and jump records in 1968 benefited, including Beamon's 8.90 m long jump.
- **Drafting:** running closely behind others cuts a large share of drag. Rotating pacer formations are a big part of modern marathon records.
- **Body size:** drag area grows roughly with height squared while mass grows with height cubed, so drag hurts small runners proportionally more.

---

## 20. Hard Physical Limits on Any Runner

### 20.1 Traction: the friction ceiling

A runner can only push forward as hard as friction allows:

```
Max horizontal force (average) ≈ μ × m × g
Max acceleration ≈ μ × g
```

With μ ≈ 1 (good shoes on a track), maximum acceleration is about 9.8 m/s². Spikes and claws digging into the surface raise the effective value above 1.

**Fastest possible 100 m for any runner limited only by friction, starting from rest:**

```
t = sqrt(2d / a)
μ = 1.0:   t = sqrt(200 / 9.81) ≈ 4.5 s
μ = 1.5:   t = sqrt(200 / 14.7) ≈ 3.7 s
```

Infinite muscle power does not beat this. Only more grip, downforce or a push from something other than the ground does. Full surface catalog: `GripBiteBracing.md`.

### 20.2 The drag-friction speed ceiling

At steady top speed, the forward push must equal drag. The forward push cannot exceed friction:

```
½ ρ C_d A v² = μ m g
v_max = sqrt( 2 μ m g / (ρ C_d A) )
```

For a 75 kg runner, μ = 1, C_d A = 0.3 m²:

```
v_max = sqrt( 2 × 1 × 75 × 9.81 / (1.2 × 0.3) ) ≈ 64 m/s (≈ 230 km/h, 143 mph)
```

No amount of strength lets an upright human-shaped runner on ordinary ground exceed roughly 64 m/s. Crouching to cut drag area, digging spikes into the surface or adding body mass raises it. A heavier runner gets more friction for the same drag.

### 20.3 Turning

```
Minimum turning radius r = v² / (μ g)
```

| Speed | Radius at μ = 1 |
|---|---|
| 12.4 m/s (Bolt) | ~16 m |
| 25.9 m/s (cheetah, no claws) | ~68 m |
| 64 m/s | ~420 m |
| 100 m/s | ~1 km |
| 343 m/s | ~12 km |

A standard 400 m track bend has a radius of about 36.5 m. That is why curve running costs sprinters speed. A superfast runner could not take a track curve at all.

### 20.4 Stopping

```
Stopping distance d = v² / (2 μ g)
```

From 100 m/s with μ = 1: about 510 m. From Bolt's peak: about 8 m.

---

## 21. What If the Runner Were Superhuman?

### 21.1 Option A: bigger and stronger (the square-cube law)

Scale a human up by a factor L:

- Muscle force scales with cross-sectional area: L².
- Body mass scales with volume: L³.
- Force per unit weight scales as 1/L.

A human twice as tall has four times the strength and eight times the weight. Relative strength halves. Bones and tendons face the same problem. This is why giants in fiction would be slow, why elephants cannot gallop and why Hirt and colleagues (Nature Ecology & Evolution, 2017) found top speed across running, flying and swimming animals is hump-shaped with body mass. The largest animals run out of stored anaerobic energy before they finish accelerating. The fastest animals (cheetah on land, marlin in water, peregrine falcon in air) sit at intermediate sizes.

### 21.2 Option B: same body, superhuman muscles

Take a 75 kg human-shaped speedster to 100 m/s (224 mph). Two ways to run that fast:

**Path 1: normal stride length (~2.5 m), extreme cadence**

```
Step frequency = 100 / 2.5 = 40 steps per second
Contact time (1 m contact length) = 0.01 s
Swing time ≈ 0.025 s per leg
Average vertical force during contact ≈ 2.5 × body weight (similar to now)
```

Ground force stays manageable. Limb speed does not. The swinging foot moves at up to ~200 m/s relative to the ground. Muscles must cycle 40 times per second at high force. The fastest real vertebrate muscles (rattlesnake shaker muscle ~90 Hz, toadfish swimbladder muscle ~200 Hz) achieve high frequency only by producing very little force. A muscle that is both fast and strong does not exist in biology.

**Path 2: normal cadence (~5 steps per second), giant bounds**

```
Step length = 100 / 5 = 20 m
Flight time ≈ 0.19 s per step, contact 0.01 s
Duty factor ≈ 5%
Average vertical force during contact ≈ 20 × body weight
Peak force ≈ 40 × body weight or more
```

Human bones and tendons tolerate perhaps 10 to 15 × body weight before failure. This path shatters the skeleton.

Either path requires tissue that does not exist: reinforced bone and tendon for Path 2, or muscle with both cheetah force and insect-like speed for Path 1.

### 21.3 Power and heat budget at 100 m/s

| Item | Estimate |
|---|---|
| Drag power | ~180 kW |
| Limb swing (internal) power | Scales roughly with v³. Several hundred kW (order of magnitude). |
| Total mechanical power | Several hundred kW to ~1 MW |
| Metabolic power at 25% efficiency | ~0.7 to 4 MW |
| Waste heat | Most of that |
| Body heat capacity (75 kg) | ~260 kJ per °C |
| Core temperature rise | At least ~2 °C per second from drag alone. Several °C per second with limb work. |

A normal body would reach lethal temperature within seconds. A speedster needs a heat sink or a metabolism far more efficient than muscle.

Fuel: human anaerobic stores are tiny by comparison. At several hundred kW the entire phosphocreatine supply would last a fraction of a second.

### 21.4 The environment at speed

| Speed | Dynamic pressure on body | Comparable to | Stagnation heating of air |
|---|---|---|---|
| 12.4 m/s | ~92 Pa | Strong breeze | negligible |
| 50 m/s | ~1.5 kPa | Severe hurricane gust | ~1 °C |
| 100 m/s | ~6 kPa | Beyond the strongest hurricanes | ~5 °C |
| 343 m/s | ~70 kPa (about 0.7 atmosphere) | Supersonic jet blast | ~58 °C |

At 100 m/s and above:

- Breathing against the airflow becomes difficult without a face shield.
- Eyes are hit by debris, insects and dust at aircraft speeds.
- A sonic boom follows anything above 343 m/s and would damage windows and eardrums along the path.
- Traction limit: from section 20.2, ~64 m/s is the ceiling for an upright runner on ordinary ground. Above that, the speedster must dig into the ground (damaging it) or use a crouched aerodynamic posture.

### 21.5 Reaction time and control

- Human simple reaction time ~0.15 to 0.2 s. At 100 m/s that is 15 to 20 m traveled before any response.
- Visual processing would need to run many times faster to place each foot. At 40 steps per second each step decision would take ~25 ms.
- Balance: the vestibular system and spinal reflexes operate on 30 to 100 ms timescales. A superhuman runner needs a superhuman nervous system as much as superhuman muscles. Vestibular detail: `AccelerometersGyroscopesVestibular.md`.

### 21.6 Momentum and impact

| Speed | Kinetic energy (75 kg) | Comparable to |
|---|---|---|
| 12.4 m/s | 5.8 kJ | Bolt at top speed |
| 25.9 m/s | 25 kJ | Human at cheetah speed |
| 100 m/s | 375 kJ | Small car at highway speed |
| 343 m/s | 4.4 MJ | About 1 kg of TNT |

Collision with anything at these speeds is lethal to both parties without extraordinary durability.

### 21.7 A plausible "realistic superhuman"

What a biologically plausible upgrade might reach:

| Upgrade | Effect | Plausible speed |
|---|---|---|
| Elite human | Baseline | 12.4 m/s |
| Ostrich-style legs (light distal limb, long tendons) | Lower swing cost, longer contact | ~14 to 16 m/s |
| Cheetah-level power (~120 W/kg) plus cleat-like feet | Huge acceleration, higher traction | ~18 to 22 m/s |
| Quadrupedal gallop with flexing spine | Stride length gain | ~25 to 30 m/s (cheetah territory) |
| Beyond that | Requires non-biological materials, cooling and nerves | Friction ceiling ~64 m/s for upright running |

---

## 22. Summary Tables

### 22.1 Speed limits by cause

| Cause of limit | Approximate ceiling |
|---|---|
| Human biology today | ~12.4 m/s peak |
| Human muscle force capacity (if applied faster) | ~16 to 18 m/s |
| Best land animal (cheetah) | ~26 to 29 m/s |
| Friction plus drag, upright human shape, μ = 1 | ~64 m/s |
| Friction only, 100 m from rest, μ = 1 | 100 m in ~4.5 s minimum |
| Heat and fuel for a human body | Seconds at 100 m/s |
| Sound barrier | 343 m/s, drag and shock waves rise sharply |

### 22.2 Springs across the four runners

| Runner | Spring | Muscle role | Result |
|---|---|---|---|
| Human | Achilles, arch | Adds work at ankle, knee, hip | Good economy, modest speed |
| Human with blades | Carbon leaf spring | Hip and knee only | Similar economy, poor acceleration |
| Cheetah | Tendons plus flexing spine | Massive power | Fastest acceleration and speed |
| Kangaroo | Huge ankle tendons, crouched posture | Near-isometric, constant frequency | Energy cost independent of speed |
| Ostrich | Long toe tendons | Muscles high on leg | Fast and about half the human running cost |

### 22.3 Core principles

1. Springs save energy. Muscles make speed.
2. The best runners pair big tendons with light distal limbs and power at the hip.
3. Body plan matters more than any single spring: gallop, hop and two-toed bird legs each solve the problem differently.
4. Drag grows with speed cubed. Above ~20 m/s it dominates.
5. Friction caps acceleration near 1 g for any runner without claws, spikes or downforce.
6. A superhuman speedster runs into traction, heat, fuel, tissue strength, reaction time and aerodynamics, in roughly that order.

---

## Sources

- Beck, Taboga, Grabowski. Characterizing the Mechanical Properties of Running-Specific Prostheses. PLoS ONE 2016. https://scholar.colorado.edu/downloads/m326m223p
- Correction to the above (model list). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5348000/
- Beck, Taboga, Grabowski. Reduced Prosthetic Stiffness Lowers the Metabolic Cost of Running for Athletes with Bilateral Transtibial Amputations. J Appl Physiol 2017. https://sites.edb.utexas.edu/wp-content/uploads/sites/181/2022/08/Reduced-Prosthetic-Stiffness-Lowers-the-Metabolic-Cost-of-Running-for-Athletes-with-Bilateral-Transtibial-Amputations.pdf
- Beck, Taboga, Grabowski. Prosthetic Model but not Stiffness or Height Affects the Metabolic Cost of Running for Athletes with Unilateral Transtibial Amputations. https://sites.edb.utexas.edu/wp-content/uploads/sites/181/2022/08/Prosthetic-Model-but-not-Stiffness-or-Height-Affects-the-Metabolic-Cost-of-Running-for-Athletes-with-Unilateral-Transtibial-Amputations.pdf
- A review of evidence on mechanical properties of running specific prostheses and their relationship with running performance. Front Rehabil Sci 2024. https://pubmed.ncbi.nlm.nih.gov/38962729/
- Grabowski seminar summary on running-specific prostheses and performance. https://bme.utah.edu/?p=1360326
- World Athletics rejects Leeper application (Reuters). https://www.aol.com/news/athletics-amputee-leepers-application-compete-172927404.html
- CAS ruling coverage. https://www.sabcnews.com/sabcnews/?p=578813
- Leeper v IAAF legal analysis. https://littletonchambers.com/prosthetics-post-pistorius-cass-decision-in-the-case-of-blake-leeper/
- Rehm 8.72 m record. https://www.guinnessworldrecords.com/world-records/541467-farthest-long-jump-t64-male
- Rehm New Delhi 2025 world title. https://www.paralympic.org/news/new-delhi-2025-markus-rehm-leaps-eighth-world-title-pays-tribute-coach-steffi
- Guity ties T64 100 m record, 2026. https://www.paralympic.org/news/athletics-tlaxcala-2026-world-records-grand-prix-mexico
- Floors T62 100 m record. https://www.guinnessworldrecords.com/world-records/606361-fastest-run-100-metres-t62-male
- T62 400 m records table. https://en.wikipedia.org/wiki/Athletics_at_the_2024_Summer_Paralympics_%E2%80%93_Men%27s_400_metres_T62
- Classic literature referenced from established knowledge: Weyand et al. 2000 and 2010 (J Appl Physiol), Weyand et al. 2009 (Pistorius), Kram et al. 2010 counterpoint, Grabowski et al. 2010 (Biol Lett), Willwacher et al. 2016 (PLoS ONE), Ker et al. 1987 (Nature), Kram and Taylor 1990 (Nature), Cavagna and Kaneko 1977, Ferris et al. 1998, Collins et al. 2015 (Nature), Simpson et al. 2019 (J Exp Biol), Witte et al. 2020, Kim et al. 2019 (Science), Hoogkamer et al. 2018 (Sports Med).
- Sawe 1:59:30 marathon, ratified world records (World Athletics, 2026). https://worldathletics.org/news/press-releases/ratified-world-records-sawe-ehammer-charlton-mcrae-yan-duplantis-assefa
- Bolt's 9.58 still standing (Il Post, August 2026). https://www.ilpost.it/2026/08/21/usain-bolt-storia-record/
- Unitree "Superman" humanoid at 12.66 m/s. https://www.eweek.com/news/unitree-superman-robot-usain-bolt-speed/
- Wild cheetah hunting dynamics (NPR coverage of Wilson et al. 2013). https://www.kpbs.org/news/science-technology/2013/06/13/fancy-feet-wild-cheetahs-excel-at-acceleration
- Wilson et al. 2013, Locomotion dynamics of hunting in wild cheetahs (PDF). https://www.originalwisdom.com/wp-content/uploads/bsk-pdf-manager/2019/04/wilson-et-al_2013_Locomotion-dynamics-of-hunting-in-wild-cheetahs.pdf
- Kram and Dawson 1998, Energetics and biomechanics of locomotion by red kangaroos. https://pubmed.ncbi.nlm.nih.gov/9787777/
- Thornton et al., Postural adaptations in hopping kangaroos (eLife). https://elifesciences.org/articles/96437
- How kangaroos hop faster without using more energy. https://www.earth.com/news/how-kangaroos-hop-faster-without-using-more-energy/
- Rubenson et al., ostrich tendon elastic energy and running cost (UWA release). https://www.news.uwa.edu.au/201010273018/international/not-just-pretty-feathers-ostriches-step-science
- What makes ostriches so fast (Science in School). https://scienceinschool.web.cern.ch/?p=97574
- Ostrich biomechanics overview (Notre Dame). https://sites.nd.edu/biomechanics-in-the-wild/2025/10/29/ostrich-ized-from-flight-but-not-from-stride-the-unique-biomechanics-of-the-worlds-fastest-bird/
- Hirt et al. 2017, why the largest animals are not the fastest (Cosmos summary). https://cosmosmagazine.com/science/biology/why-arent-the-biggest-animals-the-fastest
- Additional classic literature from established knowledge: Dawson and Taylor 1973 (Nature), Bramble and Lieberman 2004 (Nature), Pugh 1970/1971 (J Physiol), Denny 2008 (J Exp Biol), Hetem et al. 2013 (cheetah body temperature), Rome et al. (superfast muscles).
