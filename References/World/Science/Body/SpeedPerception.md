# Human Speed Perception: Limits, Formulas and Elite Performance

Earth research on how humans judge and respond to speed. Think vs move with INT: `../../../Combat/SpeedVsIntellect.md`. Light / dodge escalation: `../../../Combat/LightWarfare.md`. Full-sphere vision hardware: `Vision360.md`. Weight / length / volume precision: `MeasurementPerception.md`. Falling / terminal velocity: `Falling.md`. Roland sense wishlist: `../../../People/Roland/Goals.md`.

## Story notes (Terra)

Not a second lock. Live combat timing still sits in `SpeedVsIntellect.md` (`t_r ≈ 0.2 s`).

| Fact from this file | Story use |
|---|---|
| No speed sensor; optic flow + acceleration only | High-altitude flight, orbit and dungeon shafts can feel slow while ground proximity feels violent |
| Visual simple RT ~190-250 ms; absolute floor ~0.10-0.15 s | INT multiples cut **decision / prediction** time (`Think = t_r / I`). Nerve and muscle still need magic or body stats for the move term |
| Constant velocity is invisible to the inner ear | Straight-line Mach flight is comfortable; hard turns and g black people out |
| Elites win by anticipation, not raw RT | Diagnosis, Analyze, echolocation / Energy Sense and drilled Marksmanship buy the same 100-300 ms lead as Earth athletes |
| Preview time `D / v` sets comprehension | Runic bolts, vehicles and golems fail when `T_available < T_needed` unless the user looks far ahead or pre-aims |

---

## Earth research (reference only)

### 1. The core problem

Humans have no speed sensor. Speed is reconstructed from four inputs:

| Input | What it actually detects | Blind spot |
|---|---|---|
| Eyes (optic flow) | How fast images slide across the retina (angular speed) | Distant objects barely move even at huge speeds |
| Inner ear (vestibular) | Acceleration and rotation only | Constant velocity reads as zero |
| Skin and ears | Wind pressure, wind noise, vibration | Absent in sealed cabins or vacuum |
| Body (proprioception) | Muscle load, g-force on organs | Only active during acceleration |

Consequence: a person at 28,000 km/h on the ISS feels stationary. A person at 60 km/h on a motorcycle inches above asphalt feels like they are flying. The brain judges speed by how much the near world is moving, not by actual velocity.

---

### 2. The processing pipeline (photon to action)

Approximate timeline for an average adult reacting to a visual event:

| Stage | Time after event | Notes |
|---|---|---|
| Light hits retina, photoreceptors respond | 20-40 ms | Slower in dim light |
| Signal reaches primary visual cortex (V1) | 50-70 ms | |
| Motion processing area (MT) responds | 60-90 ms | Direction and speed computed here |
| Object recognized | 100-150 ms | Faces, familiar shapes faster |
| Conscious awareness of the event | 150-250 ms | The "now" a person experiences is already in the past |
| Motor command reaches muscles | +20-50 ms | |
| Muscle produces force (electromechanical delay) | +30-50 ms | |
| **Simple visual reaction (one stimulus, one response)** | **~250 ms** | Range 190-300 ms |
| **Choice reaction (which of several options)** | **350-600 ms** | Grows with number of options |
| **Unexpected event, real-world response** | **1.0-1.5 s** | Includes noticing, interpreting, deciding |

The brain compensates for its own lag by extrapolating moving objects forward roughly 80-100 ms. This is why a flashed dot appears to lag behind a moving one (the flash-lag effect). Perception is a prediction, not a live feed.

#### Reaction time by sense (average adult)

| Stimulus | Simple RT |
|---|---|
| Sound | 150-170 ms |
| Touch | 150-180 ms |
| Vision | 190-250 ms |
| Unexpected visual hazard (driving) | 700-1,500 ms |

Sound is processed fastest. Sprint starts use a gun for this reason.

---

### 3. Eye hardware limits

#### 3.1 Temporal resolution ("frame rate")

The eye does not capture frames. It integrates light continuously.

| Measure | Value |
|---|---|
| Flicker fusion (light stops flickering), center of vision | 50-90 Hz |
| Flicker fusion, peripheral vision | Higher; flicker noticed in the corner that vanishes when looked at directly |
| Edge artifacts detectable during eye movement | Up to ~500 Hz |
| Temporal integration window (bright light) | ~20-50 ms |
| Temporal integration window (dim light) | ~100 ms |

The integration window is what creates motion blur inside the eye.

#### 3.2 Eye movement limits

| Movement | Speed / timing | Function |
|---|---|---|
| Smooth pursuit (tracking a moving object) | Accurate to ~30°/s; degrades past that; practical max ~60-100°/s | Keeps a moving target sharp |
| Pursuit startup latency | 100-150 ms | Eye lags a suddenly moving target |
| Saccade (jump) | 20-50 ms duration, peak 500-900°/s | Repositions gaze |
| Saccade latency | 180-250 ms average; "express" saccades 100-120 ms | Time to decide where to jump |
| Saccadic suppression | Vision mostly shut off during each jump | 3-4 saccades per second means ~10-15% of time is effectively blind |
| Vestibulo-ocular reflex (VOR) | 7-15 ms latency, works up to ~300°/s head rotation | Stabilizes vision against head movement |

#### 3.3 Acuity

| Measure | Average | Elite athlete |
|---|---|---|
| Static acuity | 20/20 (1 arcminute) | 20/15 to 20/10 |
| Professional baseball players (study average) | | ~20/13 |
| Dynamic visual acuity (reading detail on a moving target) | Drops sharply above ~30°/s | Holds detail to roughly 2x the angular speed |
| Sharp-vision zone (fovea) | ~2° wide (a thumbnail at arm's length) | Same hardware; elites aim it better |
| Total field of view | ~200° horizontal | Same |

Only about 2° of the visual field is sharp. Everything else is low-resolution motion and contrast detection. Comprehension at speed depends on where the fovea is pointed.

#### 3.4 Depth perception

| Cue | Effective range |
|---|---|
| Stereo (two-eye) depth | Strong under ~10 m, weak past ~20-30 m |
| Looming (object growing in size) | Works at any range; main cue for time-to-collision |
| Motion parallax | Strong close up, fades with distance |
| Known size of objects | Any range; error-prone with unfamiliar objects |

---

### 4. Body and inner ear limits

#### 4.1 Vestibular detection

| Measure | Threshold |
|---|---|
| Linear acceleration detection | ~0.005-0.01 g (roughly 5-10 cm/s²) |
| Rotational acceleration detection | ~0.5-2°/s² |
| Constant linear velocity | Undetectable |
| Constant rotation | Sensation fades within ~15-30 s |

This is why pilots in clouds can enter a slow banking turn and feel level (the "graveyard spiral"). Slow, smooth changes slip under the threshold.

#### 4.2 G-force tolerance (sustained, seconds)

| Direction | Effect | Typical threshold |
|---|---|---|
| +Gz (head-to-foot, pulling up in a jet) | Greyout (color loss, tunnel vision) | ~4-5 g untrained |
| +Gz | Blackout | ~5-6 g untrained |
| +Gz with G-suit and straining maneuver | Functional | ~9 g |
| -Gz (foot-to-head) | Redout, pain | ~-2 to -3 g |
| Gx (chest-to-back, rocket launch) | Tolerable | 10-15 g for short periods |
| Gx brief impact (record test) | Survived | 46 g (John Stapp rocket sled) |

G-force is about changing speed or direction, not speed itself. A fighter at Mach 2 in a straight line is comfortable. The same jet turning hard at 900 km/h blacks out the pilot.

---

### 5. Attention and decision limits

| Measure | Value |
|---|---|
| Moving objects trackable at once | ~4 (some people 5) |
| Gap needed between two separate decisions (psychological refractory period) | ~200-300 ms; a second stimulus inside that window waits in line |
| Practical conscious decisions per second under pressure | ~2-4 |
| Speed difference noticeable (Weber fraction) | ~5-10% change |
| Speed adaptation | After minutes at high speed, slower speeds feel slower than they are (why drivers leave the highway too fast) |

---

### 6. Core formulas

#### 6.1 Distance covered before reacting

```
d_react = v × t_react
```

- `v` in meters per second (km/h ÷ 3.6)
- `t_react` in seconds

#### 6.2 Angular speed of an object passing to the side

For an object at perpendicular distance `d` from the travel path, currently a distance `x` ahead:

```
ω = (v × d) / (d² + x²)        (radians per second)
ω_max = v / d                  (at the moment it is directly beside you)
ω in degrees/s = ω × 57.3
```

#### 6.3 Angular speed of a point ahead at angle α from heading

```
ω = v × sin(α) / R
```

- `R` = distance to the point
- Looking far ahead and close to the direction of travel keeps ω tiny. Every expert driver, rider and pilot exploits this.

#### 6.4 "Untrackable zone" beside you

The closest an object can pass and still be tracked smoothly:

```
d_min = v / ω_limit        (ω_limit in radians/s)
```

- Average person: ω_limit ≈ 40°/s = 0.70 rad/s
- Elite tracker: ω_limit ≈ 100°/s = 1.75 rad/s

#### 6.5 Time to collision (looming)

An object of size `S` at distance `D` approaching at speed `v`:

```
θ  = S / D                 (angular size, radians)
dθ/dt = S × v / D²         (expansion rate)
τ  = θ / (dθ/dt) = D / v   (time to contact)
```

The brain reads τ directly from the expansion rate without knowing distance or speed. Human expansion-rate detection threshold is roughly 0.003 rad/s. Below that, an approaching object appears stationary. This is why drivers misjudge closing speed on a car far ahead.

Distance where approach first becomes noticeable:

```
D_notice = √(S × v / 0.003)
```

#### 6.6 Optic flow and perceived speed

The felt sense of speed tracks speed divided by eye height above the nearest surface:

```
Flow rate = v / h          (eye-heights per second)
```

#### 6.7 Retinal blur

```
blur (degrees) = retinal slip (°/s) × t_integration (s)
retinal slip = ω_object - ω_eye
```

With `t_integration` ≈ 0.025 s in daylight. If blur exceeds the size of the detail needed (a letter, a seam on a ball, a gap in traffic), that detail is gone.

#### 6.8 Choice reaction (Hick's Law)

```
RT = a + b × log₂(n + 1)
```

- `n` = number of equally likely options
- `a` ≈ 200-250 ms (base reaction)
- `b` ≈ 150 ms per bit untrained; heavy practice drives `b` toward zero for familiar patterns

| Options (n) | Untrained RT (a=0.22, b=0.15) |
|---|---|
| 1 | 0.37 s |
| 3 | 0.52 s |
| 7 | 0.67 s |

Elite athletes beat Hick's Law by shrinking `n` through prediction: they eliminate options before the event happens.

#### 6.9 Total time budget needed

```
T_needed = t_perceive + t_decide + t_move + t_action_completes
T_available = D_visible / v
Comprehension holds if T_available > T_needed
```

---

### 7. Worked tables

#### 7.1 Distance traveled during reaction

| Speed | Elite simple RT (0.15 s) | Average simple RT (0.25 s) | Average surprise (1.5 s) | Road design value (2.5 s) |
|---|---|---|---|---|
| 20 km/h | 0.8 m | 1.4 m | 8.3 m | 13.9 m |
| 50 km/h | 2.1 m | 3.5 m | 20.8 m | 34.7 m |
| 100 km/h | 4.2 m | 6.9 m | 41.7 m | 69.4 m |
| 200 km/h | 8.3 m | 13.9 m | 83.3 m | 139 m |
| 300 km/h | 12.5 m | 20.8 m | 125 m | 208 m |
| 1,000 km/h | 41.7 m | 69.4 m | 417 m | 694 m |

#### 7.2 Untrackable side zone (objects passing closer than this blur at closest approach)

| Speed | Average (40°/s) | Elite (100°/s) |
|---|---|---|
| 50 km/h | 20 m | 8 m |
| 100 km/h | 40 m | 16 m |
| 200 km/h | 80 m | 32 m |
| 300 km/h | 119 m | 48 m |

Objects inside these distances can still be tracked while far ahead. They become a smear only as they pass.

#### 7.3 Flow rate (felt speed) comparison

| Situation | Speed | Eye height / nearest surface | Flow (eye-heights/s) | Felt speed |
|---|---|---|---|---|
| Airliner cruise | 250 m/s | 11,000 m | 0.02 | Very slow |
| ISS orbit | 7,700 m/s | 400,000 m | 0.02 | Very slow |
| Skydiver at 3,000 m | 54 m/s | 3,000 m | 0.02 | Floating |
| Skydiver at 300 m | 54 m/s | 300 m | 0.18 | Ground starting to rush |
| Skydiver at 30 m (no canopy) | 54 m/s | 30 m | 1.8 | Violent |
| Walking | 1.4 m/s | 1.6 m | 0.9 | Normal |
| Car, highway | 28 m/s | 1.2 m | 23 | Fast |
| Wingsuit proximity, 20 m above terrain | 50 m/s | 20 m | 2.5 | Fast with depth |
| Wingsuit proximity, 5 m above terrain | 50 m/s | 5 m | 10 | Extreme |
| Formula 1 | 90 m/s | ~0.8 m | ~110 | Extreme |
| Motorcycle knee-down | 60 m/s | ~0.5 m (knee to asphalt) | ~120 locally | Extreme |

---

### 8. Sport breakdowns: average person vs elite

#### 8.1 Baseball hitting

| Parameter | Value |
|---|---|
| Release to plate distance | ~16.5 m |
| 95 mph pitch (42.5 m/s at release, slows ~8-10%) | ~0.41 s flight |
| 100 mph pitch | ~0.39 s flight |
| Swing duration (bat start to contact) | ~0.14-0.16 s |
| Neural delay to start the swing | ~0.10 s |
| **Last moment visual info can affect the swing** | ~0.15-0.16 s after release |
| Ball position at that moment | ~6-7 m out of pitcher's hand, ~10 m from the plate |

Result: the final ~10 m of flight (about 60% of the trip) cannot change the decision to swing. Hitters judge the pitch from the pitcher's arm slot, grip cues and the first ~0.15 s of flight. Small mid-swing corrections and checked swings are possible but limited.

Tracking: Bahill and LaRitz (1984) found professionals kept their eyes on the ball until roughly 1.7 m in front of the plate. Students lost it much earlier. With the ball passing ~0.75 m from the eyes, angular speed at 1.7 m out is roughly:

```
ω = (39 × 0.75) / (0.75² + 1.7²) ≈ 8.5 rad/s ≈ 490°/s
```

That is far past smooth pursuit. Some hitters instead make a predictive saccade to where the ball will meet the bat and "see" contact with a jump of the eyes rather than tracking.

| Person | Can hit a 95 mph fastball? |
|---|---|
| Average adult | Rarely makes contact; RT plus swing exceeds flight time without prediction |
| College player | Contact with practice |
| MLB hitter | Contact ~75-80% of swings; relies on pitch recognition before half-flight |

#### 8.2 Table tennis

| Parameter | Value |
|---|---|
| Table length | 2.74 m |
| Typical player-to-player distance | 3-6 m |
| Fast topspin rally ball speed | 15-20 m/s |
| Elite smash | 25-30 m/s |
| Interval between opponent's hit and own hit (fast exchanges) | ~0.25-0.5 s |
| Smash return window | ~0.2 s |
| Short stroke duration | ~0.1 s |
| Spin rate (elite loops) | Up to ~100-150 revolutions/s |

The budget: 0.1 s visual delay plus 0.1 s stroke leaves almost nothing during a 0.25 s exchange. Elite players read spin and direction from the opponent's racket angle, arm speed and body position before contact. Land and Furneaux (1997) showed players track the ball briefly then saccade ahead to the predicted bounce point, arriving there before the ball does.

| Person | Can return an elite smash? |
|---|---|
| Average adult | No; the ball passes before a response starts |
| Club player | Occasionally, if already positioned |
| Elite | Regularly, by anticipating from the opponent's stroke |

#### 8.3 Cricket (fast bowling)

| Parameter | Value |
|---|---|
| Delivery speed | 140-160 km/h |
| Release to batter | ~18.5 m |
| Flight time | ~0.45-0.5 s (bounce slows the ball) |

Land and McLeod (2000): batters fixate the release, then saccade to the predicted bounce point 0.1-0.2 s before the ball lands. Better batters make that jump earlier. Post-bounce movement (seam, swing) in the final ~0.2 s is largely unplayable, which is why late movement takes wickets.

#### 8.4 Tennis return of serve

| Parameter | Value |
|---|---|
| Elite serve | 200-250 km/h |
| Time to reach the returner | ~0.5-0.6 s |

Returners split-step as the server strikes and commit direction from the toss and racket face, often before the ball crosses the net.

#### 8.5 Hockey goaltending

| Parameter | Value |
|---|---|
| Slapshot | 150-170 km/h (~45 m/s) |
| Shot from 10 m | ~0.22 s |
| Reaction plus glove or pad movement | ~0.3-0.4 s |

The shot arrives before a visual reaction can finish. Goalies win with angle and positioning before the shot, plus reading the shooter's stick and body.

#### 8.6 Soccer penalty kick

| Parameter | Value |
|---|---|
| Distance | 11 m |
| Well-struck shot | 25-30 m/s |
| Flight time | ~0.4-0.45 s |
| Keeper dive to a top corner | ~0.5-0.7 s |

Keeper movement must begin at or before foot contact. Keepers guess from the kicker's hips and planted foot.

#### 8.7 Combat sports

| Parameter | Value |
|---|---|
| Elite jab, start to impact | ~0.1-0.2 s |
| Distance traveled by fist | ~0.5-0.8 m |

Faster than simple RT for most people. Defense keys off shoulder, hip and foot cues that precede the punch. The best fighters hide those cues.

#### 8.8 Sprinting start

| Parameter | Value |
|---|---|
| Elite reaction to gun | ~0.12-0.16 s |
| False start rule threshold | Under 0.10 s (considered anticipation, not reaction) |

0.10 s is treated as the floor of genuine human auditory reaction.

---

### 9. High-speed travel breakdowns

#### 9.1 Driving

| Parameter | Value |
|---|---|
| Expected event (brake lights ahead, alert driver) | ~0.7-0.75 s |
| Unexpected but common event | ~1.25 s |
| Surprise event (pedestrian stepping out) | ~1.5 s |
| Road design assumption | 2.5 s |
| Comfortable following time gap | 2-3 s |

At 100 km/h a surprise event costs ~42 m before the foot even touches the brake.

#### 9.2 Formula 1 and motorcycle racing

| Parameter | Value |
|---|---|
| Top speed | 340-360 km/h (~95-100 m/s) |
| Lateral g in corners | 4-6 g (F1) |
| Distance per 0.2 s | ~20 m |

Drivers do not react to the track. They memorize it. Gaze sits on the next braking marker or apex 1-2 s ahead where angular speed is small. The near track at the car's sides is a blur that is never consciously processed. Unpracticed tracks at these speeds would exceed human capability.

#### 9.3 Aviation see-and-avoid

The FAA's standard budget for a pilot avoiding another aircraft:

| Step | Time |
|---|---|
| See the object | 0.1 s |
| Recognize it as an aircraft | 1.0 s |
| Realize it is on a collision course | 5.0 s |
| Decide which way to turn | 4.0 s |
| Muscular reaction | 0.4 s |
| Aircraft responds | 2.0 s |
| **Total** | **12.5 s** |

Two jets closing at a combined 1,000 km/h (278 m/s) need ~3.5 km of warning. A fighter-sized aircraft head-on at 3.5 km is a dot under 0.3° across with almost no looming. This is why mid-air collisions happen with good visibility.

Using the looming threshold:

```
D_notice = √(S × v / 0.003)
S = 12 m, v = 278 m/s
D_notice = √(12 × 278 / 0.003) ≈ 1,055 m
```

Looming only becomes noticeable at ~1 km, giving ~3.8 s. That is well below the 12.5 s budget. Detection has to come from spotting the dot, not from seeing it grow.

#### 9.4 Skydiving and falling

| Parameter | Value |
|---|---|
| Time to reach terminal velocity | ~10-12 s |
| Terminal velocity, belly-down | ~190-200 km/h (54 m/s) |
| Terminal velocity, head-down | ~240-300 km/h |
| Felix Baumgartner, 2012 (thin air at ~39 km) | ~1,357 km/h, supersonic |

Phases of comprehension:

1. **Exit (0-10 s):** Accelerating. The stomach drop and weightlessness are the vestibular system reading acceleration.
2. **Terminal velocity, high altitude:** Acceleration stops. Inner ear reports nothing. The ground barely moves (0.02 eye-heights/s). Jumpers describe floating on a cushion of air. Only wind roar signals speed. Baumgartner reported no sensation of passing the sound barrier.
3. **Below ~600 m:** Ground texture starts expanding. Flow rate rises tenfold.
4. **Below ~300 m:** "Ground rush." 300 m at 54 m/s is ~5.5 s.
5. **Final ~50 m:** Under 1 s. Comprehension of terrain detail is impossible.

Altimeters exist because eyes judge altitude poorly from high up. At high altitude humans can comprehend the fall completely. The failure happens only at the very end.

#### 9.5 Wingsuit proximity flying

| Parameter | Value |
|---|---|
| Horizontal speed | 150-250 km/h (40-70 m/s) |
| Glide ratio | ~2.5-3:1 |
| Terrain distance in proximity lines | 5-50 m |

Rock 10 m beside the flight path at 50 m/s:

```
ω_max = 50 / 10 = 5 rad/s ≈ 286°/s
```

Untrackable. A ridge first visible 50 m ahead gives 1 s, below the average surprise response. Proximity pilots fly memorized lines, scout terrain repeatedly and keep gaze on exit points far ahead. This activity sits at the human edge and has a high fatality rate.

---

### 10. The human comprehension zones

#### 10.1 By preview time (T = visible distance ÷ speed)

| Preview time | Average person | Trained / elite in a practiced task |
|---|---|---|
| > 3 s | Full comprehension and deliberate choice | Full comprehension |
| 1-3 s | Reacts, limited understanding, errors common | Comfortable |
| 0.4-1 s | Mostly too late; reflexive flinch | Functional only with anticipation and drilled responses |
| 0.15-0.4 s | No meaningful response | Only pre-planned responses committed before full information (batting, table tennis, goalkeeping) |
| < 0.15 s | No visual reaction possible | No visual reaction possible; outcome decided by prior positioning |

**0.10-0.15 s is the hard floor for any human.** Nothing inside that window can be seen and answered.

#### 10.2 By angular speed of the thing that matters

| Angular speed | What the eye gets |
|---|---|
| < 30°/s | Full detail via smooth tracking |
| 30-100°/s | Tracked with degrading detail; elites hold detail far better |
| 100-500°/s | Tracking fails; position sampled by saccades; motion detected but detail lost |
| > 500-1,000°/s | A streak or flicker; only "something passed" registers |

#### 10.3 By g-force

| Sustained load | Effect on comprehension |
|---|---|
| 0-3 g | Normal |
| 3-5 g | Effortful; peripheral vision starts fading |
| 5-6 g (untrained) | Tunnel vision then blackout |
| 9 g (trained, G-suit) | Functional but exhausting |

---

### 11. What elites actually do differently

The raw hardware gap between average and elite is small:

| Trait | Average | Elite | Gap |
|---|---|---|---|
| Simple visual RT | ~250 ms | ~160-200 ms | ~20-35% |
| Acuity | 20/20 | 20/15-20/10 | Modest |
| Smooth pursuit limit | ~30-40°/s | ~70-100°/s | ~2x |
| Choice RT on trained patterns | 400-600 ms | Near simple RT | Large |
| Useful lead time from anticipation | ~0 | 100-300 ms | Decisive |

The decisive difference is prediction. Elites:

1. **Read cues before the event:** pitcher arm slot, opponent racket face, shooter's hips. This buys 100-300 ms, more than the entire hardware advantage.
2. **Reduce the options (Hick's Law):** fewer possibilities means faster choice.
3. **Aim the fovea better:** fixate the release point, then jump to where the object will be instead of chasing where it is.
4. **Look far ahead:** at speed, gaze goes to points with low angular speed (the apex, the exit, the bounce point).
5. **Run drilled motor programs:** the response is pre-built and only triggered.
6. **Commit early and correct late:** start the action on a prediction and make small adjustments if new information arrives in time.

---

### 12. Bottom line

- **Speed itself is never the limit.** Humans comprehend 28,000 km/h in orbit perfectly.
- **The limit is close-range angular speed plus time to impact.** Things nearby that need a response are what overwhelm the system.
- **Average person ceiling:** about 1-1.5 s of warning to respond meaningfully to a surprise; smooth tracking to ~30-40°/s.
- **Elite ceiling:** about 0.15-0.4 s in a practiced, predictable task; tracking to ~100°/s; everything faster handled by anticipation.
- **Absolute human floor:** ~0.10-0.15 s. Below that nobody responds to what they see.
- **Acceleration is a separate wall:** blackout at 5-6 g untrained, ~9 g with equipment and training.

---

### Key studies referenced

- Bahill & LaRitz (1984): eye tracking of baseball pitches by professional vs amateur hitters
- Land & Furneaux (1997): gaze strategies in table tennis
- Land & McLeod (2000): anticipatory saccades in cricket batting
- Laby et al. (1996): visual acuity of professional baseball players
- Hick (1952): choice reaction time and number of alternatives
- Green (2000): driver perception-reaction times
- FAA Advisory Circular 90-48: pilot see-and-avoid timing
- Stapp (1954): human deceleration tolerance

## Cross-links

- Think vs move (INT / body): `../../../Combat/SpeedVsIntellect.md`
- Light dodge threshold: `../../../Combat/LightWarfare.md`, `LightWarfareVariables.md`
- Acuity / sphere vision: `Vision360.md`
- Terminal fall speeds: `Falling.md`
- Flight / optic-flow altitude: `../Energy/Flight.md`
- Sense training (echolocation → Energy Sense): `../../../People/Roland/Goals.md`
