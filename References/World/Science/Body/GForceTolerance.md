# G-Force Tolerance by Body Position and Ride Type

Earth research: aerospace centrifuge, sliding-sport, and amusement-ride G limits by axis and posture. Vehicle seats: `../Vehicle/Positions.md`. Fall spikes: `Falling.md`. Hub: `../Science.md`.

All values are approximate composites for healthy adults. Individual tolerance varies by roughly ±1 G.

---

## 1. Axis Definitions

| Axis | Inertial push on the body | Common name | Blood shifts toward |
|---|---|---|---|
| +Gz | Head toward feet | Eyeballs down | Feet |
| -Gz | Feet toward head | Eyeballs up | Head |
| +Gx | Chest toward back | Eyeballs in | Back (small shift) |
| -Gx | Back toward chest | Eyeballs out | Chest (small shift) |
| ±Gy | Side to side | Eyeballs left/right | Lower side |

**Core rule:** tolerance depends on the length of the blood column between heart and eyes measured along the load. Upright that column is about 30 cm. Every 1 G along +Gz drops eye-level arterial pressure by roughly 22 to 25 mmHg. Vision fails first (grayout) because the eye's internal pressure (15 to 20 mmHg) collapses retinal flow before the brain loses flow. Blackout follows, then G-LOC (loss of consciousness).

Loads that run chest-to-back (Gx) barely change that column. Loads that run head-to-foot (Gz) stretch it to its maximum.

---

## 2. Master Tolerance Table (Sustained, Over 10 Seconds)

| Axis | Relaxed, untrained | Trained, straining maneuver | Trained + G-suit + pressure breathing | Limiting factor |
|---|---|---|---|---|
| +Gz | Grayout 3.5 to 4 G. G-LOC 4.5 to 5.5 G | 6.5 to 7.5 G | 9 G for 15 to 45 s | Brain and retinal blood flow |
| -Gz | -1 G uncomfortable for minutes. -2 to -3 G for 5 to 10 s | About -3 to -4 G brief | No effective protection exists | Redout, burst facial/eye capillaries, severe headache, slowed heart |
| +Gx | 4 to 6 G for several minutes. 8 to 10 G for about 1 min | 12 to 15 G for 5 to 20 s in a contoured couch | Same; suits add little on this axis | Breathing against chest weight, chest pain, tunnel vision from tearing |
| -Gx | About 60 to 75% of +Gx values | 6 to 8 G for tens of seconds in full harness | Same | Restraint pressure, breathing, eye/face congestion |
| ±Gy | 1 to 1.5 G with head unsupported. 2 to 3 G with full side support | F1 drivers: 4 to 6 G peaks for 1 to 3 s, repeated | Not applicable | Neck muscles, organ shift, side restraint |

### Time Tolerance, +Gz (Seated Upright, Relaxed)

| Load | Typical outcome |
|---|---|
| 2 G | Hours; fatigue limited |
| 3 G | Many minutes for most people; heavy limbs |
| 4 G | Seconds to about a minute before grayout for many |
| 5 G | G-LOC within roughly 5 to 10 s for many untrained people |
| 6 G+ | G-LOC within seconds without a straining maneuver |

### Time Tolerance, +Gx (Supine, Contoured Couch, Head Supported)

| Load | Approximate endurance |
|---|---|
| 3 G | About an hour |
| 6 G | 5 to 10 min |
| 9 to 10 G | 1 to 2 min |
| 14 to 15 G | 5 to 20 s |

---

## 3. Spikes Versus Sustained Loads

### Duration Bands

| Band | Duration | What limits tolerance |
|---|---|---|
| Impact | Under 0.2 s | Structure: spine, neck, organs, restraint contact. Blood has no time to move |
| Transient | 0.2 to 5 s | The brain holds about 4 to 6 s of oxygen reserve. +Gz above the G-LOC threshold can pass without blackout if it ends inside that window |
| Sustained | Over 5 to 10 s | Cardiovascular. Heart rate and vessel tone need 6 to 10 s to respond |

The ASTM ride standard draws the same line: its acceleration limits apply to events of 200 ms or longer. Sustained limits are driven by cardiovascular response while impact limits are driven by neuromuscular response.

### Onset Rate

- **Slow onset (about 0.1 G/s):** reflexes keep up. Worth roughly +1 G of tolerance compared with rapid onset. Grayout gives warning before G-LOC.
- **Rapid onset (over 1 to 3 G/s):** reflexes cannot keep up. G-LOC can arrive with no grayout warning. Fighter training uses 6 G/s onset for this reason.
- **Jerk** (rate of change of G) drives head snaps and whiplash. Smooth transition curves (clothoids) cut jerk.

### Impact Tolerance (Under 0.2 s, Fully Restrained, Braced)

| Direction | Non-injurious peak | Notes |
|---|---|---|
| +Gx (pushed back into contoured seat) | 30 to 45 G for under 0.1 s | Best impact axis |
| -Gx (thrown forward into full harness) | 20 to 25 G routinely tolerated | John Paul Stapp rode a rocket sled to 46.2 G peak in 1954 with temporary injuries |
| +Gz (spine compression) | 15 to 20 G | Ejection seats operate in the 12 to 20 G range. Fracture risk climbs fast above 20 to 25 G or with a bent spine |
| -Gz | About 10 G | Neck and head vessels |
| ±Gy | 10 to 15 G with side support and headrest | Far lower with the head free |

Survived (with injury) crash spikes: David Purley 179.8 G (1977 F1). Kenny Bräck about 214 G (2003 IndyCar). These lasted only milliseconds.

### Spine Check (Why +Gz Impact Tops Out Near 20 G)

- Torso mass above the lower lumbar spine: about 55 to 60% of body mass (about 45 kg for an 80 kg person).
- Young adult lumbar compressive failure: roughly 6 to 10 kN.
- At 10 G that torso loads the spine with about 4.4 kN. At 20 G about 8.8 kN, which reaches the failure range.

---

## 4. Force-to-Axis Map by Position

What each ride force becomes once it reaches the body.

| Position | Forward acceleration | Braking | Flat (unbanked) turn | Banked turn, valley, loop bottom | Crest, airtime |
|---|---|---|---|---|---|
| Seated upright, facing forward | +Gx | -Gx | Gy | +Gz | -Gz |
| Standing, facing forward | +Gx (must lean or brace) | -Gx (must brace) | Gy (balance limited) | +Gz on legs | -Gz (feet unload) |
| Reclined 45°, feet forward | +Gx with some -Gz | -Gx with some +Gz | Gy | Split about evenly +Gz and +Gx | -Gz and -Gx |
| Supine, feet first (luge) | -Gz | +Gz | Gy | +Gx | -Gx (lifts off) |
| Supine, head first | +Gz | -Gz | Gy | +Gx | -Gx |
| Prone, head first (skeleton, superman zipline) | +Gz | -Gz | Gy | -Gx, chest supported | +Gx (lifts off) |
| Prone, feet first | -Gz | +Gz | Gy | -Gx, chest supported | +Gx |
| Bicycle | +Gx (power limited) | -Gx (pitch-over limited) | Rider leans so it becomes +Gz | +Gz | -Gz |

### Rankings

**Loads perpendicular to the path (valleys, banked turns, loops), best to worst:**

1. Supine (+Gx)
2. Reclined 60 to 70°
3. Prone with full chest, hip and head support (-Gx through a surface)
4. Reclined 30 to 45°
5. Seated upright (+Gz)
6. Standing (+Gz plus leg strength limit plus longest blood column to the feet)

**Loads along the path (launches, braking), best to worst:**

1. Seated upright or reclined with a seatback for launch and a harness for braking (Gx)
2. Supine or prone with acceleration pushing toward the feet (+Gz)
3. Standing (balance and grip limited)
4. Supine or prone with deceleration pushing toward the head (-Gz)

**Flat turns:** poor in every position. Seated with side bolsters and headrest is best. Banking the path so the resultant runs through the best-tolerated axis solves most turn problems.

---

## 5. Position Profiles

### Seated Upright

- Comfortable sustained: 2 to 3 G.
- Grayout begins: 3.5 to 4 G relaxed.
- Brief peaks of 5 to 6 G lasting under 1 to 2 s pass without symptoms for most healthy riders.
- Airtime: -0.5 to -1.5 G brief with restraint.
- Lateral: 1.5 to 2 G brief with side support.

### Standing

- Longest hydrostatic column (heart to feet about 1.2 to 1.3 m). Blood pools in the legs fastest of any position. Some people faint standing motionless at 1 G.
- Legs carry the load. Sustained 2 G is roughly equal to squatting an extra bodyweight. Over 2 to 3 G sustained, knees fatigue and buckle.
- Unbraced lateral: about 0.15 to 0.3 G before a step is needed. With handholds about 0.5 G.
- Leaning athletes (skiers, surfers, snowboarders) convert lateral load into +Gz and sustain 2 to 3 G in carved turns with peaks near 4 G.
- Landing spikes at the feet of 5 to 10 G for 0.05 to 0.1 s are routine with flexed knees. Locked knees send the spike straight up the spine.
- Leg muscle pumping helps venous return. Standing still under load is worse than shifting weight.

### Reclined

Approximate gain against +Gz as the seatback tilts back (angle from vertical):

| Recline | Effective heart-to-eye column | Tolerance multiplier |
|---|---|---|
| 0° | 100% | 1.0× |
| 30° (F-16 seat) | 87% | About 1.15× (+0.5 G) |
| 45° | 71% | About 1.4× |
| 60° | 50% | About 2× |
| 65 to 70° | 34 to 42% | About 2.4 to 2.9× |
| 80°+ | Under 20% | Behaves as +Gx |

- Most of the benefit arrives past 45°.
- Head support is required. Elevated legs add further gain by improving venous return.

### Supine

- Best position for loads through the track surface (+Gx).
- Above 6 G, inhaling against the weight of the chest wall becomes labored. Above 10 to 12 G only short shallow breaths work.
- Head must be supported. If the head is lifted to see (luge), the neck carries head weight × G.
- Braking direction matters. Feet first, braking pushes toward the feet (+Gz) and is tolerable. Head first, braking pushes blood to the head (-Gz).

### Prone

- Loads through a fully supported chest are well tolerated: 6 to 8 G sustained and higher in brief peaks. 1950s prone-pilot aircraft trials demonstrated this.
- Weak points: lifting the head to see forward loads the neck extensors with head weight × G. Chest compression against the support restricts breathing more than supine.
- Head-first braking is -Gz. Keep sustained braking under about 1 to 1.5 G.
- Skeleton riders take up to about 5 G in curves with the head inches above the ice.

### Luge (Supine, Feet First)

- Curve loads: up to about 5 G. Bobsleigh and skeleton rules cap centrifugal force at 5 G.
- The Whistler track was designed to a 5.02 G maximum. Sleds typically pull 2.5 to 3 G.
- Racing speeds average 120 to 145 km/h through high banked curves.
- Load in banked curves is +Gx (well tolerated). The limit is the neck holding the head up to see, plus shoulder and core strength for steering. Blurred vision and concentration loss are common in high-G curves.
- Head plus helmet (about 6 to 6.5 kg) weighs about 30 kg on the neck at 5 G.

### Bicycle

- Lean angle: tan θ = v² / (g·R). Total load along the body: √(1 + (v² / (g·R))²).
- Lean keeps the turn load running head-to-seat (+Gz) so the body handles it easily.
- Tire grip caps flat-road turns near 0.8 to 1.0 G lateral (about 40 to 45° lean), so total load stays near 1.3 to 1.4 G.
- Steep velodrome banking at track speed: roughly 1.5 to 2 G total.
- Braking: 0.5 to 0.7 G before the rear lifts or the rider pitches over.
- BMX and pump tracks: 2 to 3 G brief in transitions. Landings spike higher and are absorbed by bent arms and legs.
- Standing on the pedals turns the legs into suspension for spikes. Sitting is better for sustained load.
- Bicycle G is limited by traction long before the body.

---

## 6. Best Ways to Resist G-Force

| Method | Approximate gain | How |
|---|---|---|
| Position the load chest-to-back | 2 to 3× | Supine or recline past 60° so curve loads run as +Gx |
| Anti-G straining maneuver (AGSM) | +1.5 to 3 G | Tighten legs, glutes and abdomen hard. Strain against a closed throat for about 3 s. Exhale and inhale in under 1 s. Repeat |
| G-suit (leg and abdominal bladders) | +1 to 1.5 G | Squeezes blood out of the legs and gut. Full-coverage suits add more |
| Positive pressure breathing | +1 to 2 G with suit | Pressurized oxygen supports the chest during straining |
| Combined (AGSM + suit + PBG + training) | Up to 9 G sustained | Fighter pilot standard |
| Leg elevation | Moderate | Raises venous return to the heart |
| Pre-tension before onset | Avoids rapid-onset G-LOC | Tense and brace the head against the headrest before the load arrives |
| Strength training | Extends AGSM endurance | Legs, core and neck. Neck work matters most for lateral, prone and luge loads |
| Hydration, food, sleep | Avoids losses of 0.5 to 1 G | Dehydration, low blood sugar, fatigue, alcohol (12 to 24 h prior) and heat all lower tolerance |
| Repeated exposure | Short-term gain | Tolerance fades after weeks without exposure |
| Avoid push-pull | Prevents losses of 1 to 2 G | -Gz right before +Gz drops +Gz tolerance. Keep muscles tense through airtime into a valley |
| Head straight along the load | Reduces neck injury | Turning the head under load or in rotation strains the neck and causes Coriolis disorientation |
| Wide, contoured restraint | Raises impact and sustained limits | Spreads pressure. 5-point harness for -Gx. Side bolsters for Gy |

Body type: a shorter heart-to-eye distance means higher +Gz tolerance. Higher resting blood pressure gives a slight advantage.

---

## 7. Hard Constraints of the Human Body

**Cardiovascular**
- Eye-level arterial pressure drops about 22 to 25 mmHg per +Gz.
- Reflex compensation takes 6 to 10 s.
- Brain oxygen reserve lasts about 4 to 6 s after flow stops.
- Recovery from G-LOC: 10 to 30 s of incapacitation plus confusion afterward.

**Visual**
- Grayout (loss of peripheral vision), then blackout (vision lost while conscious), then G-LOC.
- -Gz: redout and burst eye capillaries.

**Respiratory**
- +Gx over 6 G: labored breathing. Over 12 G: very shallow breathing only.
- -Gx: harness straps compress the chest.
- Prone: support surface compresses the chest.

**Spine**
- Axial impact limit about 15 to 20 G.
- Bent or twisted posture lowers it sharply.

**Neck**

| Load | Head alone (about 5 kg) | Head + helmet (about 6.5 kg) |
|---|---|---|
| 3 G | 15 kg | 20 kg |
| 5 G | 25 kg | 33 kg |
| 9 G | 45 kg | 59 kg |

Lateral loads are the worst case for the neck because the side muscles are weakest.

**Organs**
- +Gz pulls the heart and diaphragm down. Abdominal contents shift.
- Lateral loads swing organs against their attachments.

**Vestibular**
- Rotation combined with head movement causes disorientation and nausea.
- Repeated rapid direction changes cause motion sickness.

**Skin and contact**
- Small contact areas under high G bruise. Restraint edges concentrate pressure.

**Suspension in harness**
- Hanging motionless in a harness pools blood in the legs. Faintness can begin within 10 to 30 minutes.

**Fatigue and repetition**
- AGSM is exhausting. Repeated high-G cycles reduce tolerance over a session.

**Excluded conditions**
- Heart disease, high blood pressure, aneurysm, pregnancy, recent surgery, spine or neck injury, retinal problems, seizure disorders.

---

## 8. Ride Types

### Roller Coasters

**Standard envelope (ASTM F2291, duration scaled):**
- Brief positive vertical peaks roughly 5 to 6 G.
- Negative vertical about -2 G brief.
- Lateral around ±1.5 G.
- Lower limits apply the longer a force lasts.
- Events under 200 ms are handled separately as impact events.

**Typical modern design:**
- Valley and loop peaks: 3.5 to 4.5 G lasting 0.5 to 2 s.
- Airtime: -0.5 to -1.5 G.
- Launches: 1 to 3 G as +Gx.

**Why coasters can exceed sustained limits:** peaks last well under 2 s. Blood cannot pool enough to cause blackout in that time.

**Rider positions:**

| Coaster type | Body position | Valley load becomes |
|---|---|---|
| Sit-down / floorless / wing | Seated upright | +Gz |
| Stand-up | Standing on a bike-style saddle | +Gz on legs and saddle |
| Flying | Prone, face down in harness | -Gx through chest harness |
| Lay-down | Supine | +Gx |

**Design constraints:**
- Clothoid (teardrop) loops cut entry G compared with circular loops.
- Heartline rolls rotate riders around the heart to keep lateral load near zero.
- No hard valley right after big airtime (push-pull).
- Headrests and side bolsters for any lateral work.

### Massive Slides (Water and Dry)

- Not covered by ASTM F2291. Water slides fall under ASTM F2376. Riders are unrestrained, which makes slides the most constrained ride type.
- **Rule 1: no airtime.** Normal force must stay positive with margin. For a crest of radius R: v ≤ √(0.8·g·R) keeps at least +0.2 G.
- **Rule 2: feet first, supine.** Ankles crossed, arms crossed over the chest. Curve loads run as +Gx. Runout braking runs as +Gz.
- **Self-banking:** an open slide rider climbs the wall to tan θ = v² / (g·R). The wall must be taller than that climb. Enclosed tubes contain the rider but allow tumbling or climbing overhead if v² / (g·R) gets large.
- **Targets for unrestrained riders:** peaks 2.5 to 3 G, sustained 2 G or less, zero airtime, runout deceleration about 1 G or less with no abrupt water impact.
- **Vertical-drop slides:** near free fall at the top. The bottom transition must ramp G up gradually or it becomes a spine-compression spike.

### Mountain-Scale Tubes

Two forms: inflatable tubes on a groomed snow or synthetic chute, and enclosed tubes descending a mountainside.

**Speed is drag-limited.** With enough vertical drop the rider reaches terminal speed:

v_terminal = √( 2·m·g·(sin α − μ·cos α) / (ρ·CdA) )

| Case | Slope | Friction μ | CdA | Mass | Terminal speed |
|---|---|---|---|---|---|
| Rider on slick slide, supine feet first | 30° | 0.05 | 0.2 m² | 80 kg | About 55 m/s (200 km/h) |
| Snow tube, seated | 20° | 0.12 | 0.5 m² | 90 kg | About 26 m/s (93 km/h) |

Speed must be controlled by grade (keep it shallow), friction strips, uphill sections or water braking. Vertical drop alone cannot be the limiter on a mountain.

**Rider position:** seated semi-reclined, feet first is best. Prone head-first puts braking and collisions on the head.

**Spinning tubes** add rotational disorientation.

### Giant Ziplines

**Positions:**
- Seated harness: hanging upright.
- Superman: prone, head first, face down.

**Force sources:**
- Cable sag curvature at the low point: modest +Gz.
- High speed: giant lines run 100 to 160 km/h.
- Braking: the main load event.
- Pendulum swing when the trolley slows: the main spike risk.

**Pendulum spike:** if the trolley stops while the rider still moves at speed v on a lanyard of length L, load at the start of the swing is 1 + v² / (g·L).

| Residual speed at trolley stop | Lanyard 1.5 m |
|---|---|
| 10 m/s | About 7.8 G |
| 5 m/s | About 2.7 G |
| 3 m/s | About 1.6 G |

Residual speed at arrest must be low (3 m/s or under). Hard stop blocks create spikes. Magnetic eddy-current brakes, spring systems and uphill runouts give smooth deceleration.

**Braking by position:**
- Seated: braking is -Gx with forward swing.
- Superman: braking pushes blood toward the head (-Gz) while harness straps load the chest and thighs. Keep sustained deceleration near 1 G or less.

**Mass variability:** heavier riders arrive faster. Brakes must cover the full rider weight range.

**Suspension trauma:** riders stranded motionless on the line face blood pooling within 10 to 30 minutes.

---

## 9. Design Tables

### Minimum Turn Radius for a Given Total Load (Banked, Coordinated)

R = v² / (g·√(G² − 1))

| Speed | 2 G total | 3 G total | 4 G total | 5 G total |
|---|---|---|---|---|
| 15 m/s (54 km/h) | 13.2 m | 8.1 m | 5.9 m | 4.7 m |
| 25 m/s (90 km/h) | 36.8 m | 22.5 m | 16.5 m | 13.0 m |
| 35 m/s (126 km/h) | 72.1 m | 44.2 m | 32.2 m | 25.5 m |
| 45 m/s (162 km/h) | 119.2 m | 73.0 m | 53.3 m | 42.1 m |

### Crest Radius (Vertical Hilltop)

| Speed | Zero G (weightless) R = v²/g | +0.2 G kept (unrestrained riders) R = v²/(0.8g) |
|---|---|---|
| 15 m/s | 22.9 m | 28.7 m |
| 25 m/s | 63.7 m | 79.6 m |
| 35 m/s | 124.9 m | 156 m |
| 45 m/s | 206.4 m | 258 m |

### Valley Radius for 3 G Total

R = v² / (g·(G − 1))

| Speed | Radius |
|---|---|
| 15 m/s | 11.5 m |
| 25 m/s | 31.9 m |
| 35 m/s | 62.4 m |
| 45 m/s | 103.2 m |

### Braking Distance at Constant Deceleration

d = v² / (2·a)

| Speed | 0.5 G | 1 G | 2 G |
|---|---|---|---|
| 15 m/s | 22.9 m | 11.5 m | 5.7 m |
| 25 m/s | 63.7 m | 31.9 m | 15.9 m |
| 35 m/s | 124.9 m | 62.4 m | 31.2 m |
| 45 m/s | 206.4 m | 103.2 m | 51.6 m |

---

## 10. Quick Reference by Position (Primary Load Direction)

Brief spike values assume onset of 3 to 5 G/s or less with duration of 2 s or less.

| Position (load axis) | Comfortable sustained | Max sustained, untrained | Brief spike (under 2 s) | Impact (under 0.2 s) |
|---|---|---|---|---|
| Seated upright (+Gz) | 2 to 3 G | 4 to 4.5 G | 5 to 6 G | 15 to 20 G |
| Standing (+Gz on legs) | 1.5 to 2 G | 2.5 to 3 G | 3 to 4 G, knees flexed | 8 to 10 G at feet with flexed landing |
| Reclined 45° | 3 to 3.5 G | 5 to 6 G | 6 to 7 G | 20+ G |
| Reclined 65 to 70° | 4 to 5 G | 7 to 8 G | 9 to 10 G | 25+ G |
| Supine (+Gx) | 4 to 6 G | 8 to 10 G | 12 to 15 G | 30 to 45 G |
| Prone, chest supported (-Gx) | 3 to 5 G | 6 to 8 G | 9 to 10 G | 20 to 25 G |
| Lateral, any position, side support (Gy) | 1 to 1.5 G | 2 to 3 G | 3 to 5 G | 10 to 15 G |
| Head-ward, any position (-Gz) | 0.5 to 1 G | -2 G | -3 G | About -10 G |

---

## Sources

- Luge (Wikipedia): https://en.wikipedia.org/wiki/Luge
- CBC, "Deadly luge track may have stretched the rules": https://www.cbc.ca/news/canada/deadly-luge-track-may-have-stretched-the-rules-1.1105659
- The Globe and Mail, Whistler track design G-force: https://www.theglobeandmail.com/news/national/why-this-track-means-fear/article1208321
- The Varsity, sliding sport physiology: https://thevarsity.ca/2010/02/25/olympic-athletes-pushed-to-new-dangerous-levels/
- Thrillzing, roller coaster G-force and ASTM F2291: https://thrillzing.com/science/roller-coaster-g-forces-explained/
- ASTM WK91645, revision of F2291 impact-event limits: https://store.astm.org/workitem-wk91645
- ASTM F2291 scope (excludes dry slides and water slides): https://eshop.normservis.sk/norma/astm-f2291-22-1.6.2022.html
