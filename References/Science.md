# Science

## Sphere flight randomness

The randomness in flight comes from three effects and they matter far more than the arc shape at this velocity.

### Boundary-layer knuckling (the biggest one)

For a 9.5mm bearing at Mach 0.99, Reynolds number at the muzzle is ~2.17×10⁵. That sits inside the sphere's critical drag-crisis band (roughly 2×10⁵–4×10⁵), where the boundary layer flips unpredictably between laminar and turbulent separation on the two hemispheres of the ball. Each flip produces a lateral force that is not tied to spin, wind or release quality. It is the same mechanism that makes a knuckleball erratic.

A polished, smooth ball bearing actually makes this worse, not better: roughness (like golf-ball dimples) forces an early, repeatable transition, while a smooth surface keeps the transition point sensitive and twitchy. This is flight-path randomness with no correlation to anything the shooter controls and it repeats differently shot to shot even with identical release conditions.

### Magnus drift from uncontrolled spin

Neither a slingshot pouch nor a bow has rifling, so any spin imparted at release is essentially random in both axis and magnitude. Pouch peel-off, string nock friction or an off-center strike are enough. The force scales fast:

- 5 rev/s stray spin → 6% of the ball's weight in lateral force
- 20 rev/s → 25% of weight
- 50 rev/s → 63% of weight
- 100 rev/s → exceeds the ball's own weight

Since the spin axis is not fixed shot to shot (unlike a rifled bullet, where drift is at least predictable and correctable), this drift changes direction randomly between shots rather than being a consistent, zeroable bias.

### Transonic velocity sensitivity

Launching right at Mach 0.99 puts the shot on the steepest part of the drag-coefficient curve (Cd roughly doubles between Mach 0.9 and 1.0). A ~1% variation in release velocity, normal for a hand-drawn slingshot or bow, shifts Mach enough to meaningfully change Cd, which changes the whole deceleration profile and therefore range and drop, well beyond what the same velocity variance would cause at a slower, subsonic launch speed.

### Crosswind and atmospheric turbulence

A small sphere has poor ballistic coefficient, so wind drift accumulates quickly and gets worse the longer the ball is airborne. High-angle shots with several seconds of flight time are far more wind-sensitive than flat, direct shots.

### What helps consistency

A sphere has no yaw-of-repose or tumbling instability the way a stone or a non-spherical pellet would, since drag does not depend on orientation. Strip out spin and the Re-crisis zone and the flight would be quite repeatable. With them in play, the knuckling effect and the uncontrolled spin are the two dominant, genuinely random contributors, with the transonic velocity sensitivity a close third.

## Arrow speed and Mach 0.99 evasion

An average compound-bow arrow flies about 250 to 300 fps (75 to 90 m/s). Recurve and traditional bow arrows run slower at 150 to 200 fps. Mach 0.99 is about 1,115 fps (340 m/s), roughly 4× faster than a compound arrow and 6 to 7× faster than a recurve arrow.

Evasion assumes about 0.25 s to react to a visual cue and another 0.25 s to move.

- Compound arrow at 30 m: arrives in about 0.33 s, so a dodge is only possible if the archer is spotted at release.
- Mach 0.99 arrow at 30 m: arrives in about 0.09 s, well under the 0.25 s needed just to react.
- Minimum dodge distance (about 0.5 s total): roughly 45 m for a compound arrow versus roughly 170 m at Mach 0.99.

Audio warning: a normal arrow arrives after the bow's twang, giving a cue. At Mach 0.99 the sound of release arrives almost simultaneously with the arrow, so there is no useful cue from that sound.

Impact energy scales with speed squared, about 14× higher if mass is held equal. A 26 g arrow goes from roughly 105 J to over 1,500 J.

Dodging goes from difficult to effectively impossible on reaction alone. The only defenses left are cover, moving before release or disrupting the archer's aim.

## Near-Mach arrow sound (captive piston launch)

A captive piston removes the gas blast, but the flight itself is still loud: roughly 80 to 100 dB a few meters away, a sharp hissing rip.

No full sonic boom: Mach 0.99 is subsonic in freestream. Airflow over the point, nock and fletching can locally exceed Mach 1, so small shocklets can form and add a faint crack on top of the hiss.

Aerodynamic noise from turbulence and vortex shedding off the shaft and vanes rises steeply with speed (order-of-magnitude scaling near speed to the sixth power for some aeroacoustic sources). Going from ~85 m/s to 340 m/s is roughly +36 dB under that scaling, turning a compound arrow's soft whisper (~50 dB) into something near 90 dB. Treat the exact dB figures as rough, not lab values.

Other launch noises still matter:

- Air ahead of the arrow in a tube gets shoved out at high speed and makes a puff or thump at the muzzle unless the barrel is vented.
- The piston hitting its stop is often the loudest launch sound, a mechanical bang around 100 dB or more without damping.

Versus a subsonic bullet: frontal area often favors the arrow. A shaft is about 5 to 8 mm across against 9 mm for the bullet. The real difference is everything behind the tip. An arrow is 70 to 80 cm long with a rougher surface, a nock and three fletching vanes, all shedding turbulence at 340 m/s. A 9 mm bullet is a smooth slug about 15 mm long with nothing protruding. Fletching is a major noise source and is why the arrow is still louder in flight than a subsonic bullet.

A fletchless design that is spin-stabilized or front-weighted would be far quieter in the air. Launch can be made quiet with a damped stop and a vented barrel. The flight noise from surface and vanes cannot be removed without changing the projectile.

## Rotating frictionless tube (radial slide launch)

Core result: for a frictionless tube rotating at constant angular speed ω, a ball starting at distance r₀ from the pivot and exiting at distance L leaves with:

v = ω√(2L² − r₀²)

This combines a tangential part (ωL) with a radial slide (ω√(L² − r₀²)). A ball starting at the far end gains only the tip speed. A ball starting near the pivot approaches 1.41 × tip speed. A 1 m tube with a 50 m/s tip speed launches at roughly 70 m/s. Accelerating the tube while the ball travels pushes the exit speed higher.

### Worked case: tube along the forearm

Pivot at the elbow, ω = 40 rad/s (pitcher's forearm), elbow already moving 15 m/s from trunk rotation, ball starting at the hand (0.3 m) and exiting at 0.91 m.

On the Progression arm table, elbow→fingertip ≈ **0.254 × height**. At ~180 cm that is ~46 cm; L = 0.91 m means the tube runs about 45 cm past the fingertips. Shoulder-pivoted swings use full arm ≈ **0.44 × height** as the flesh pivot-to-tip length before any stick or tube.

- Tangential: 40 × 0.91 ≈ 36 m/s, plus 15 m/s from the elbow ≈ 51 m/s
- Radial slide: 40 × √(0.91² − 0.3²) ≈ 34 m/s
- Total: about 62 m/s (138 mph) frictionless

Friction, rolling and tube flex cost roughly a third of that, leaving about 40 m/s or more (90+ mph). That matches a pro fastball and can beat it with good technique. A longer lever gives more tip speed for the same arm motion, which is why the jai alai cesta, lacrosse stick and atlatl outrun a bare-hand throw.

### Strength-to-ω formula

**Step 1: angular speed from lifting strength**

ω = √( 2 W g ℓ θ / ((m_s/3 + m) L²) )

**Step 2: pivot speed from AGI (not sprint)**

The forearm note’s elbow add is kinetic-chain speed, about **15 m/s** for the AGI 15 man. Scale with the same √S curve as sprint:

```
v_sprint = 6 × √(AGI / 15)     m/s     (locomotion)
v_s      = 15 × √(AGI / 15)    m/s     (throw pivot)
P        = 25 × AGI            W
E_throw  = P × Δt              J       (Δt ≈ 0.2 s per throw)
```

**Step 3: exit velocity**

v = (1 − f) × √( (ωL + v_s)² + ω²(L² − r₀²) )

**Step 4: projectile energy check**

```
KE_ball = ½ × 0.145 × v²
```

`KE_ball` must stay ≤ `E_throw` (AGI power through the throw window). If STR is far ahead of AGI, the lift-based ω overstates what the body can feed the ball; lower W, shorten the swing or treat the shot as AGI-capped.

| Symbol | Meaning | Default |
|---|---|---|
| W | Max lift (kg), overhead press | from STR (≈ 0.5 × 6 × STR) |
| v_s | Pivot / elbow-chain speed | 15 × √(AGI/15) m/s |
| g | Gravity | 9.81 m/s² |
| ℓ | Effective lever arm of the lifted load | 0.3 m |
| θ | Swing arc before release | 1.5 rad |
| m_s | Mass of the swinging arm and tube | 1.5 kg |
| m | Projectile mass | 0.145 kg |
| L | Exit distance from pivot | 0.91 m |
| r₀ | Starting distance from pivot | 0.3 m |
| f | Friction, rolling and flex loss | 0.33 |
| Δt | Throw power window | 0.2 s |

Worked example: AGI 15 man, W = 45 kg (matched street STR≈15), v_s = 15 m/s.

- E_throw = 375 × 0.2 = **75 J**
- ω ≈ 28.2 rad/s → exit after losses ≈ **31 m/s** (~69 mph)
- KE_ball ≈ **69 J** ≈ 0.92 × E_throw (nearly fills the AGI budget)

Old W = 100 kg + v_s = 9 m/s demo (≈87 mph, ~109 J) is a strong press with a weak pivot add. Against an AGI 15 budget of 75 J it **overshoots**; that combo is STR-rich / AGI-poor and fails Step 4 unless AGI is higher.

Matched STR ≈ AGI (adult tube, OHP = 0.5 × deadlift, v_s from AGI):

| AGI (=STR) | P | E_throw | v_s | Exit v | KE_ball | KE / E_throw |
|---|---|---|---|---|---|---|
| 15 | 375 W | 75 J | 15.0 m/s | 31 m/s (69 mph) | ~69 J | ~0.92 |
| 21 | 525 W | 105 J | 17.7 m/s | 37 m/s (82 mph) | ~97 J | ~0.92 |
| 40 | 1,000 W | 200 J | 24.5 m/s | 51 m/s (113 mph) | ~185 J | ~0.93 |
| 48 | 1,200 W | 240 J | 26.8 m/s | 55 m/s (124 mph) | ~222 J | ~0.93 |

So with matched stats the projectile math **closes from AGI**: ball energy is almost the whole throw budget. The tube’s job is turning that joule budget into high v on a small mass, not inventing energy past AGI.

Scaling: exit speed rises with √W through ω and with √AGI through v_s. Heavier projectiles raise inertia and lower ω.

### Sprinter KE and power (AGI calibration)

`KE = ½ m v²`

| | Mass | Top speed | Body KE |
|---|---|---|---|
| Average man | 80 kg | 6 m/s | ½ × 80 × 6² = **1,440 J** |
| Usain Bolt | 94 kg | 12.4 m/s | ½ × 94 × 12.4² ≈ **7,227 J** |

On the Progression height/weight line, 80 kg ≈ 183 cm and 94 kg = 195 cm.
Ratio 7,227 / 1,440 ≈ **×5.0**. Speed contributes (12.4/6)² ≈ ×4.27. Mass contributes 94/80 ≈ ×1.18. Together ≈ ×5.

Work to reach top speed ≈ that KE (ignore air drag and internal limb motion):

| | KE | Time to top | Avg mechanical power |
|---|---|---|---|
| Average man | 1,440 J | ~4 s | ≈ **360 W** |
| Bolt | 7,227 J | ~6 s | ≈ **1,200 W** |

Power ratio ≈ ×3.3. Sheet mapping: **1 AGI ≈ 25 W**, so AGI 15 ≈ 375 W (street) and AGI 48 ≈ 1,200 W (Bolt-class power). Equal-mass sprint speed still uses `v = 6√(AGI/15)` in `Progression.md`.

### Energy delivered to the projectile

Projectile KE = ½ × 0.145 × v². Compare to the AGI throw budget `E_throw = 25 × AGI × 0.2`.

| Launch | Exit v | KE_ball | Notes |
|---|---|---|---|
| Matched AGI 15 (street) | 31 m/s (~69 mph) | ~69 J | ≈ 92% of 75 J budget |
| Matched AGI 48 (Bolt power) | 55 m/s (~124 mph) | ~222 J | ≈ 93% of 240 J budget |
| Forearm band after losses | ~40 m/s (~90 mph) | ~116 J | needs ~AGI 25+ budget (E ≥ 116 J) |
| Old W = 100 kg demo after losses | 38.7 m/s (~87 mph) | ~109 J | overshoots AGI 15's 75 J |

A hard throw puts on the order of **70–220 J** into a baseball when stats are matched: a few percent of a sprinting man's **body** KE (1,440 J), but almost all of the **throw-window** AGI energy. The tube converts that small joule budget into high v on 0.145 kg; it does not mint energy past AGI.

### Roland ages 5–10 (formula stress test)

Inputs from `Progression.md` and `StatusBreakdown.md`:

- Deadlift = 6 × STR kg. Overhead press W ≈ 0.5 × deadlift.
- v_s = 15 × √(AGI / 15) m/s (throw pivot). Sprint = 6 × √(AGI / 15) is locomotion only.
- E_throw = 25 × AGI × 0.2 J. Ball KE must not exceed this.
- Full sheet = body + Basic skill pads (+ Cooking AGI at transfer).
- Adult tube L = 0.91 m (device length fixed; child-scaled sticks understate lever weapons).

| Age | STR / AGI | W | v_s | Sprint | Exit v | KE_ball | E_throw | KE / E |
|---|---|---|---|---|---|---|---|---|
| 5 | 4 / 8 | 12 kg | 11.0 m/s | 4.4 m/s | 18 m/s (40 mph) | ~23 J | 40 J | 0.58 |
| 6 | 16 / 21 | 48 kg | 17.7 m/s | 7.1 m/s | 33 m/s (74 mph) | ~80 J | 105 J | 0.76 |
| 7 | 24 / 27 | 72 kg | 20.1 m/s | 8.0 m/s | 40 m/s (89 mph) | ~115 J | 135 J | 0.85 |
| 8 | 31 / 32 | 93 kg | 21.9 m/s | 8.8 m/s | 45 m/s (100 mph) | ~145 J | 160 J | 0.91 |
| 9 | 36 / 35 | 108 kg | 22.9 m/s | 9.2 m/s | 48 m/s (107 mph) | ~165 J | 175 J | 0.94 |
| 10 | 40 / 40 | 120 kg | 24.5 m/s | 9.8 m/s | 51 m/s (113 mph) | ~185 J | 200 J | 0.93 |

**What holds**

- From age 8 on, STR and AGI are nearly matched and ball KE fills ~90%+ of the AGI throw budget. Projectile math closes from AGI.
- Age 10 lands in soft-cesta / hard-sling territory (~113 mph) with budget headroom, not an energy violation.
- Ages 5–6 are STR-poor relative to AGI (or just weak): exit speed is low and KE / E is well under 1.

**Caveats**

1. Constant-ω slide and finite swing energy still disagree inside the ω step; the AGI budget cap is the external sanity check.
2. Peak press is not constant torque through 1.5 rad.
3. Do not feed sprint into v_s. That was the bug that starved the tangential term and made tube speeds look too slow vs sling expectations.
4. The age 5→6 jump is mostly Basics unlocking on the sheet.

**How to use it**

- Pipeline: STR → W → ω; AGI → v_s and E_throw; tube → v; require KE_ball ≤ E_throw.
- Matched STR ≈ AGI is the intended operating point. STR ≫ AGI fails the energy check.

## Mana energy (shared INT curve)

**1 mana ≈ 10 J.** Mana pays the cast. **Intelligence** sets how much of that budget becomes useful projectile energy.

**Shared formula (Bolt and Arrow):**

```
E(INT) = 118.9 × ln(1 + INT / 100)     joules
```

Anchors: **40 J at INT 40**, **65 J at INT 73**. No floor at low INT. Doubling INT does not double energy.

| INT | E |
|---|---|
| 15 | 17 J |
| 25 | 27 J |
| 40 | 40 J |
| 73 | 65 J |
| 100 | 82 J |
| 200 | 131 J |
| 500 | 213 J |
| 1,000 | 285 J |

Optional slower late growth (legacy): `E = 40 + 41.6 × ln(INT / 40)` floored at 0. Default rewrite math uses **118.9 × ln(1 + INT/100)**.

## Mana Bolt speaking levels

Blunt bean/egg. **Pop = kinetic = useful energy.** Both follow the speaking-level energy below.

```
Useful = E(INT) × (level_share / 65)
Speed = √(2 × Useful / 0.084 kg)
Ram pressure = ½ ρ v²    (ρ = 2,000 kg/m³)
```

"Pop" is swelling energy at contact. Goblin: head 3 kg, skull failure 3.3 kN, contact 1.5 ms.

### Speaking levels

Same five-second statement. Voice level sets power. Shares are relative to the INT 73 normal anchor (65 J):

| Level | Mana | Share of 65 J | At INT 73 (pop = kinetic) |
|---|---|---|---|
| Mental | 15 | 20 / 65 | 20 J |
| Whisper | 15 | 45 / 65 | 45 J |
| Quiet | 20 | 55 / 65 | 55 J |
| Normal | 25 | 65 / 65 | 65 J |
| Overcharged | 40 | 120 / 65 | 120 J |
| Overcharged (max) | 50 | 150 / 65 | 150 J |

Mental wastes budget because no voice carries the focus. Whisper costs the same 15 mana as mental but delivers more useful energy.

### Output by INT (normal level)

| INT | Pop and kinetic each | Speed | Ram pressure |
|---|---|---|---|
| 15 | 17 J | 20 m/s | 0.40 MPa |
| 25 | 27 J | 25 m/s | 0.63 MPa |
| 40 | 40 J | 31 m/s | 0.95 MPa |
| 73 | 65 J | 39 m/s | 1.55 MPa |
| 100 | 82 J | 44 m/s | 1.96 MPa |
| 200 | 131 J | 56 m/s | 3.1 MPa |
| 500 | 213 J | 71 m/s | 5.1 MPa |
| 1,000 | 285 J | 82 m/s | 6.8 MPa |

Ram pressure stays under ~20 MPa skin failure across this band.

### Goblin kill thresholds (normal)

Orbit skull failure ~**32 J** pop → INT **~31**. Full eye-entry burst ~**63 J** → INT **~70**. Whisper vault kill needs higher INT (about **100+** on whisper share). Temple hits fail earlier than vault hits.

### Speaking level costs

| Level | Cost |
|---|---|
| Mental | 15 |
| Whisper | 15 |
| Quiet | 20 |
| Normal | 25 |
| Overcharged | 40 |
| Overcharged (max) | 50 |

## Mana Arrow

Pure kinetic projectile with **no pop**. Condensed mana shaped as an arrow with hidden razor vanes.

### Base stats

| Property | Value |
|---|---|
| Size | 4 mm × 400 mm (5.03 cm³) |
| Mass | 40 g |
| Effective density | ~7,950 kg/m³ |
| Hydrodynamic reach (soft tissue) | ~1,101 mm |
| Damage type | Kinetic and slicing |

Shaft mass stays **40 g** at any thickness (condensed mana). Speed and kinetic energy do not depend on shaft width. Effective density rises as the shaft narrows.

```
Hydrodynamic reach = L × √(ρ_shaft / ρ_tissue)     (ρ_tissue = 1,050 kg/m³)
```

At 400 mm and ~7,950 kg/m³ this is 400 × √(7,950/1,050) ≈ **1,101 mm**. Treat as condensed-mana fiction (the long-rod rule is hypervelocity on Earth). A goblin torso (~140 mm) and a human torso (~220 mm) sit inside this limit on a soft path.

### Energy

```
E(INT) = 118.9 × ln(1 + INT / 100)
Kinetic = E(INT) × (mana / 25)
Speed = √(2 × Kinetic / 0.04 kg)
```

Normal cast = **25 mana**. Doubling mana doubles kinetic energy. Speed rises by √2.

| Mana | INT | Kinetic | Speed |
|---|---|---|---|
| 25 | 40 | 40 J | 45 m/s |
| 50 | 40 | 80 J | 63 m/s |
| 100 | 40 | 160 J | 89 m/s |
| 25 | 73 | 65 J | 57 m/s |
| 50 | 73 | 130 J | 81 m/s |
| 100 | 73 | 260 J | 114 m/s |

Warbow arrows fly about 55–65 m/s; compound about 80–95 m/s.

### Punch cost (4 mm shaft)

```
E_punch = 1.5 × R × A × t
A = 0.1257 cm²
```

R in MPa, t in cm, E in J. Cost scales with diameter squared (4 mm = 25% of an 8 mm shaft).

| Material | R | Thickness | Joules | Mana at INT 40 |
|---|---|---|---|---|
| Goblin skin | 15 MPa | 2 mm | 0.6 J | 0.4 |
| Hobgoblin skin | 30 MPa | 4 mm | 2.2 J | 1.4 |
| Cow hide | 40 MPa | 4 mm | 3.0 J | 1.9 |
| Hardened leather | 60 MPa | 5 mm | 5.6 J | 3.5 |
| Mail | 350 MPa | 1.5 mm | 9.6 J | 6.0 |
| Dog-sized ant | 180 MPa | 3 mm | 10.2 J | 6.4 |
| Dog-sized mantis | 250 MPa | 3 mm | 14.1 J | 8.8 |
| Brigandine | 500 MPa plate + ~40 MPa backing | 1.5 mm + 3 mm | 16 J | 10 |
| Iron (2 mm) | 700 MPa | 2 mm | 26 J | 16 |
| Steel (1 mm) | 1,400 MPa | 1 mm | 26 J | 16 |
| Car-sized ant plate | 180 MPa | 18 mm | 61 J | 38 |
| Car-sized mantis plate | 250 MPa | 18 mm | 85 J | 53 |
| Mithril / supersteel | 3,500 MPa | 1 mm | 66 J | 41 |

Brigandine is **not** 500 MPa through 4.5 mm (that would be ~42 J). It is hard plate plus soft backing.

### Hardness gate

Tip and vanes share one gate: they only bite when hardness **H ≥ 1.5 × R**. Below that the tip blunts or shatters and vanes chip or skate. Hardness does not depend on shaft width.

```
H(INT) = 600 × ln(1 + INT / 100) / ln(1.4)     MPa
Max R cleared = H / 1.5
```

**Joule costs apply only after the gate clears.** A through-shot near the tip limit may open a hole and still fail to slice if the vanes do not clear R.

| INT | H | Max R cleared |
|---|---|---|
| 15 | 249 MPa | 166 MPa |
| 25 | 398 MPa | 265 MPa |
| 40 | 600 MPa | 400 MPa |
| 73 | 977 MPa | 651 MPa |
| 100 | 1,236 MPa | 824 MPa |
| 200 | 1,959 MPa | 1,306 MPa |
| 500 | 3,195 MPa | 2,130 MPa |
| 1,000 | 4,276 MPa | 2,851 MPa |
| 2,000 | 5,429 MPa | 3,619 MPa |

Minimum INT to clear R: goblin skin **2** / hardened leather **6** / dog ant **17** / dog mantis **24** / mail **35** / brigandine plate **53** / iron **81** / steel **225** / mithril **1,800**.

At **INT 40** (max R 400 MPa): leather and mail are open; **brigandine plate, iron, steel and mithril are closed** even if joules would allow them. Example: 50 mana at INT 40 gives 80 J, enough joules for steel, but the hardness gate still blocks steel until INT ~225.

### Slicing fletchings

Three razor vanes at 120°. Each is 60 mm long and reaches 20 mm from the shaft with a 0.5 mm edge. Visible fletching looks only ~8 mm wide.

- Tip punches a ~0.4 cm hole; vanes cut a three-armed star slit ~4 cm across on a through-shot.
- Slicing only on through-shots. A stopped arrow gets tip/shaft damage and a small entry cut.
- A head shot that lodges against the back of the skull never engages the vanes. Tip alone kills at about **8 J**.
- Vane cost does not change with shaft width.

| Layer | Toughness | Blade cost |
|---|---|---|
| Skin (2 mm) | 1.5 J/cm² | 1.8 J per wall |
| Muscle | 0.2 J/cm² | 1.2 J per cm |
| Lung / liver / bowel / brain | 0.1 J/cm² | 0.6 J per cm |

#### Goblin kill paths (through and through, between ribs)

| Path | Joules | Mana at INT 40 | Mana at INT 73 | Time to death |
|---|---|---|---|---|
| Neck (carotids and jugulars) | 13 J | 8 | 5 | 10 to 30 s |
| Chest through the heart | 17 J | 11 | 7 | 10 to 60 s |
| Chest through the lung | 17 J | 11 | 7 | 1 to 5 min |
| Abdomen through the liver | 17 J | 11 | 7 | 2 to 10 min |
| Thigh (femoral vessels) | 25 J | 16 | 10 | 1 to 3 min |

A rib in the path adds roughly **20 J**.

#### Full slicing pass through armor

| Armor | Punch | Vane slit | Total | Mana at INT 40 | Gate |
|---|---|---|---|---|---|
| Hardened leather | 5.6 J | 9 J | 14.6 J | 9 | open from INT 6 |
| Mail | 9.6 J | 16 J | 25.6 J | 16 | open from INT 35 |
| Steel (1 mm) | 26 J | 42 J | 68 J | 43 | **closed until INT ~225** |

If the vanes stall, the arrow lodges with vanes outside and no slicing happens.

### Car-sized insects

Dog-sized ants and mantises fall to a single arrow anywhere once joules and hardness clear (INT **17** / **24**). Headshots always work.

Car-sized specimens have **18 mm** plate. Weakspots fall at any casting INT.

| Weakspot | R | Thickness | Joules |
|---|---|---|---|
| Joint membrane (neck / leg root / waist) | 30 MPa | 0.5 mm | 0.28 J |
| Compound eye | 100 MPa | 1 mm | 1.9 J |
| Antenna base | 100 MPa | 1 mm | 1.9 J |

```
Plate depth per arrow = Kinetic / (0.1885 × R)   cm
```

| INT (25 mana) | Kinetic | Arrows for ant plate | Arrows for mantis plate |
|---|---|---|---|
| 73 | 65 J | 1 | 2 |
| 200 | 131 J | 1 | 1 |

One arrow clears ant plate at **61 J** (38 mana at INT 40) and mantis plate at **85 J** (53 mana at INT 40), if hardness already clears (true by INT 24+).

### Elemental versions

Element takes share **f** of kinetic K; punch keeps `(1 − f) × K`. A 4 mm shaft allows **f up to 0.85** at 80 J and still punches mail (9.6 J).

| Element | Mechanism | Effect at 80 J |
|---|---|---|
| Fire | Momentum becomes heat | Ignites cloth and hair at about 10 J. Coagulates about 1 cm³ of tissue. Seared cuts seal and reduce bleeding |
| Cold | Momentum becomes heat removal | Freezes about 0.2 g of tissue. Suits a brittle wound rim or a slowed limb |
| Wind | Wide slash | Cuts a 30 cm slash about 12 cm deep in flesh. Armor stops it completely |
| Water | Pressure sheet | Needs v above √(2R / 1,000) with R in MPa and water density 1,000 kg/m³: skin **173 m/s**, leather **346 m/s**, mail **837 m/s**. Sheet volume = E / R |
| Stone | Spike | 40 g becomes a 15 cm³ spike. Tip yields near 150 MPa. Passes hide and leather; shatters on carapace and harder |

### Katana comparison

Katana edge hardness ~**400 MPa** clears R up to **267 MPa** (matches an arrow around INT **25**). A katana swing carries about **125 J**. It cuts through mantis carapace and fails on mail and harder. A goblin neck takes about **56 J** (soft tissue ~11 J and vertebra ~45 J). A mana-infused katana uses the same `H(INT)` curve as the arrow tip.

See also `Spells.md` (Mana Bolt, Mana Arrow).
