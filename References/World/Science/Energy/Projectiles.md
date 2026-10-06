# Projectiles

Hub: `../Science.md`. Physical arrowhead forge / cast / aero: `../Metallurgy/Arrowheads.md`. Guided munitions / turn limits: `GuidedProjectiles.md`. Flywheel pairs / storage: `Generators.md`. Recoil / countermass: `Kinetic.md`.

## Sphere flight randomness

The randomness in flight comes from two main effects plus wind and they matter far more than the arc shape at this velocity.

### Transonic Cd rise (primary)

Launching right at Mach 0.99 puts the shot on the steepest part of the drag-coefficient curve (Cd roughly doubles between Mach 0.9 and 1.0). A ~1% variation in release velocity, normal for a hand-drawn slingshot or bow, shifts Mach enough to meaningfully change Cd, which changes the whole deceleration profile and therefore range and drop, well beyond what the same velocity variance would cause at a slower, subsonic launch speed.

### Magnus drift from uncontrolled spin

Neither a slingshot pouch nor a bow has rifling, so any spin imparted at release is essentially random in both axis and magnitude. Pouch peel-off, string nock friction or an off-center strike are enough. The force scales fast:

- 5 rev/s stray spin → 6% of the ball's weight in lateral force
- 20 rev/s → 25% of weight
- 50 rev/s → 63% of weight
- 100 rev/s → exceeds the ball's own weight

Since the spin axis is not fixed shot to shot (unlike a rifled bullet, where drift is at least predictable and correctable), this drift changes direction randomly between shots rather than being a consistent, zeroable bias.

Reynolds number at the muzzle for a 9.5 mm bearing at Mach 0.99 is ~2.17×10⁵, inside the subsonic sphere drag-crisis band. At near-Mach-1 that crisis is largely suppressed by compressibility, so do not lean on knuckleball-style boundary-layer flips as the main scatter source here. Transonic Cd and random spin already carry the argument.

### Crosswind and atmospheric turbulence

A small sphere has poor ballistic coefficient, so wind drift accumulates quickly and gets worse the longer the ball is airborne. High-angle shots with several seconds of flight time are far more wind-sensitive than flat, direct shots.

### What helps consistency

A sphere has no yaw-of-repose or tumbling instability the way a stone or a non-spherical pellet would, since drag does not depend on orientation. With uncontrolled spin and a Mach 0.99 release, the random Magnus axis and the steep Cd curve are the two dominant scatter sources, with wind a close third on long flights.

## Arrow speed and Mach 0.99 evasion

An average compound-bow arrow flies about 250 to 300 fps (75 to 90 m/s). Recurve and traditional bow arrows run slower at 150 to 200 fps. Mach 0.99 is about 1,115 fps (340 m/s), roughly 4× faster than a compound arrow and 6 to 7× faster than a recurve arrow.

Evasion assumes about 0.25 s to react to a visual cue and another 0.25 s to move.

- Compound arrow at 30 m: arrives in about 0.33 s, so a dodge is only possible if the archer is spotted at release.
- Mach 0.99 arrow at 30 m: arrives in about 0.09 s, well under the 0.25 s needed just to react.
- Minimum dodge distance (about 0.5 s total): roughly 45 m for a compound arrow versus roughly 170 m at Mach 0.99.

Audio warning: a normal arrow arrives after the bow's twang, giving a cue. At Mach 0.99 the sound of release arrives almost simultaneously with the arrow, so there is no useful cue from that sound.

Impact energy scales with speed squared, about 14× higher if mass is held equal. A 26 g arrow goes from roughly 105 J to over 1,500 J.

Dodging goes from difficult to effectively impossible on reaction alone. The only defenses left are cover, moving before release or disrupting the archer's aim.

## Sling vs Bow vs Atlatl vs Throwing Knife vs Baseball Throw

### Quick numbers

| Weapon | Release speed | Effective range | Kinetic energy |
|---|---|---|---|
| Bow | 60–90 m/s (135–200 mph) | ~150–400 m | ~60–130 J |
| Sling | 45–90+ m/s (100–200 mph) | ~150–437 m | ~100–250 J |
| Baseball throw (by hand) | 40–47 m/s (90–105 mph) | ~90–136 m | ~115–160 J |
| Atlatl | 30–40 m/s (65–90 mph) | ~30–230 m | ~60–110 J |
| Throwing knife | 12–15 m/s (26–34 mph) | 3–10 m accurate | ~10–15 J |

### Ranking

1. **Bow** - best all-around: high speed, flat trajectory, best accuracy of the group.
2. **Sling** - matches or beats the bow on raw speed, range and energy; much harder to master.
3. **Baseball throw (by hand)** - no equipment at all, yet its energy rivals a bow or sling because a baseball is much heavier than an arrow or sling stone; trained throwers are also very accurate.
4. **Atlatl** - solid power and distance, but noticeably less accurate than the bow or a trained thrower.
5. **Throwing knife** - lowest speed, shortest range, lowest energy; accuracy collapses past a few meters.

### Why

- **Bow and sling** both store energy through mechanical leverage (limb bend / arm-extension via the sling cord), which is why they lead in speed and range.
- **Atlatl** also uses leverage (a lever arm extending the throwing arm) but transfers less energy than a bow or sling; its dart is heavier and slower, giving it more momentum but less kinetic energy per shot.
- **Baseball throw** has no mechanical assistance, just the arm, but a baseball (~145 g) is far heavier than an arrow, sling stone or dart, so even a 40–47 m/s throw carries surprising kinetic energy. This is the same reason line-drive fastballs can injure or kill; the biomechanics of an overhand throw are simply very well optimized by evolution and training.
- **Throwing knife** has no leverage and a light payload, so it trails every other option on every axis.

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
- ω ≈ 27.3 rad/s → exit after losses ≈ **31 m/s** (~69 mph)
- KE_ball ≈ **69 J** ≈ 0.92 × E_throw (nearly fills the AGI budget)

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

Power ratio ≈ ×3.3. Sheet mapping: **1 AGI ≈ 25 W**, so AGI 15 ≈ 375 W (street) and AGI 48 ≈ 1,200 W (Bolt-class power). Equal-mass sprint speed still uses `v = 6√(AGI/15)` in `../../../Progression/Progression.md`.

### Energy delivered to the projectile

Projectile KE = ½ × 0.145 × v². Compare to the AGI throw budget `E_throw = 25 × AGI × 0.2`.

| Launch | Exit v | KE_ball | Notes |
|---|---|---|---|
| Matched AGI 15 (street) | 31 m/s (~69 mph) | ~69 J | ≈ 92% of 75 J budget |
| Matched AGI 48 (Bolt power) | 55 m/s (~124 mph) | ~222 J | ≈ 93% of 240 J budget |
| Forearm band after losses | ~40 m/s (~90 mph) | ~116 J | needs ~AGI 25+ budget (E ≥ 116 J) |

A hard throw puts on the order of **70–220 J** into a baseball when stats are matched: a few percent of a sprinting man's **body** KE (1,440 J), but almost all of the **throw-window** AGI energy. The tube converts that small joule budget into high v on 0.145 kg; it does not mint energy past AGI.

### Roland ages 5–10 (formula stress test)

Ages for these years: `../../../../Story/Notes/Timeline.md` (wake at 5 through ascension at 10). The untrained body curve is `../../../Progression/Training.md` (age 10 baseline STR 15, not 40). The pairs below are the padded sheet used to stress the throw, not a second life clock.

Inputs from `../../../Progression/Progression.md` and `StatusBreakdown.md`:

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
- Peak press is not constant torque through the full 1.5 rad swing; the AGI budget cap is the external sanity check.
- Do not feed sprint speed into v_s. Sprint is locomotion only; throw pivot uses the AGI formula above.
- The age 5→6 jump is mostly Basics unlocking on the sheet.

**How to use it**

- Pipeline: STR → W → ω; AGI → v_s and E_throw; tube → v; require KE_ball ≤ E_throw.
- Matched STR ≈ AGI is the intended operating point. STR ≫ AGI fails the energy check.

## Flywheel pinch launch

Exit speed is at most rim surface speed. Cap: **KE = ½ m v_rim²**. Indestructible wheels (adamantium) remove the wheel-material rim limit; the projectile and contact physics remain. Paired wheels: `Generators.md`. Recoil after the shot leaves: `Kinetic.md`.

### Energy cost to the wheels

Wheels run at constant speed while the projectile starts at rest, so it slips during acceleration. Sliding friction turns as much energy into heat as it puts into the shot. Flywheels lose **m·v²** per shot (double the projectile KE). Staged pairs at stepped speeds raise efficiency to **n/(n+1)** (2 stages 67%, 4 → 80%, 9 → 90%, 19 → 95%).

### Steel ball between rigid wheels

| Rim speed | 1/4 in (1.05 g) | 3/8 in (3.55 g) | 1/2 in (8.4 g) |
|---|---|---|---|
| 300 m/s | 47 J | 160 J | 380 J |
| 1,000 m/s | 525 J | 1,775 J | 4,200 J |
| 3,000 m/s | 4,700 J | 16,000 J | 38,000 J |

Refs: .22 LR ~160 J, 9mm ~500 J, 5.56 ~1,750 J, .308 ~3,500 J, .50 BMG ~18,000 J.

Limits that stop a normal steel ball well below rim speed:
- Rigid pinch contact is only a few mm. 1,000 m/s in 3 mm needs ~17 million g (~170 kN on a 1 g ball). Friction cannot deliver that at realistic clamp.
- Bearing steel yields ~2 GPa under Hertzian contact; high clamp flattens or shatters the ball.
- Slip heat ≈ ball KE on the surface. Melting 1 g steel ~950 J; near 1,000 m/s the surface melts or welds.
- Feeding a resting ball into the nip is a glancing strike at full rim speed. Plastic above a few hundred m/s; hypervelocity-like above ~3 km/s.

**Practical ceiling for solid steel on rigid wheels: about 300 to 600 m/s.** Higher needs staging, a sabot or a tougher projectile.

### Indestructible ball (adamantium)

Material limits drop. Cap is still **½ m v_rim²**; wheels still pay **m·v²**. Remaining limits: clamp force, vacuum around the rims, air after exit, energy stored in the wheels.

| Rim speed | 1/4 in (1.05 g) | 3/8 in (3.55 g) | 1/2 in (8.4 g) |
|---|---|---|---|
| 10 km/s | 52 kJ | 177 kJ | 420 kJ |
| 100 km/s | 5.3 MJ | 18 MJ | 42 MJ |
| 0.1c | 113 t TNT | 380 t TNT | 900 t TNT |
| 0.5c | 3.5 kt TNT | 12 kt TNT | 28 kt TNT |

1 kg TNT = 4.2 MJ. Above ~0.1c use **KE = (γ − 1) m c²**. Over 3 mm contact, 10 km/s needs ~1.7 billion g (~17 MN on a 1 g ball). Hypersonic rims need a vacuum housing. Slip heat still equals ball KE; the ball survives but leaves glowing.

**Sea-level sphere drag:** energy halves about every **21 m** (1/4 in) or **42 m** (1/2 in). A 3 km/s and a 100 km/s launch both dump ~99% of energy within ~140 m or ~280 m into a shock-heated air channel. Full energy at the target needs vacuum or very short range. Decay length for velocity (Cd ≈ 0.9): **L ≈ 2m / (ρ Cd A)**; energy decays twice as fast.

### Arrow instead of ball

Shaft contact along ~0.6 m (not 3 mm) cuts required grip ~200×. Grooved wheels or a fletchless fin-stabilized rod keep vanes clear. A 60 g, 8 mm arrow's energy halves roughly every **700 m** at sea level (vs 21 m for a 1/4 in ball). Long-rod penetrator at speed.

| Speed (60 g war arrow) | Energy | Recoil momentum |
|---|---|---|
| 55 m/s (war longbow) | 90 J | 3.3 N·s |
| 1,000 m/s | 30 kJ | 60 N·s |
| 3,000 m/s | 270 kJ | 180 N·s |
| 0.01c | 65 t TNT | 180,000 N·s |
| 0.1c | 6.5 kt TNT | 1,800,000 N·s |

.50 BMG recoil ~60 N·s ≈ braced handheld limit. Handheld flywheel arrows top out near **1 km/s** unless recoil is handled (`Kinetic.md`).

### Non-magical signature (sense-magic worlds)

- Stored: silent in vacuum housing. Mechanical bearings bleed heat. Enchanted bearings emit magic. Spin-up can be elsewhere and earlier.
- Firing: slip heat at the wheels; sonic boom above sound speed; glowing air channel above several km/s. Loud and bright, not magical.
- If adamantium itself carries a detectable aura, the launcher can be sensed even when idle.

### Practical weapon tiers

- **Handheld ≤ ~1 km/s:** silent until fired; rapid fire until wheels slow; ~300× longbow energy.
- **Braced 1 to 3 km/s:** anti-armor / anti-monster.
- **Mounted relativistic:** nuclear-scale per shot; wheels must store several times the shot energy.

### Launch formulas

- Classical projectile KE: **½ m v²**
- Relativistic: **(γ − 1) m c²**, γ = 1 / √(1 − v²/c²)
- Flywheel draw with full slip: **m v²**
- Accel over contact length d: **a = v² / (2d)**; tangential force **F = m a**; clamp per wheel ≈ F / (2μ)
- Staged efficiency (n equal steps): **n / (n + 1)**

