# Mechanical Precision

Earth reference for **gears, cams, linkages, gyros and optics** as computing and manufacturing. Calculation is mechanical. Motors and synchros may move gun mounts later; the solve itself is shafts and gear trains.

Use for invent beats (screw machines, cams, governors, rangefinders, integrators). Do not paste Earth brand names into prose unless the story invents them.

**Accuracy:** solid popular engineering-history summary. Dates and “firsts” are order-of-magnitude, good enough for prerequisite checks.

**Caldris readout** (`../../Tech/Technology.md`): craftsman + early-industrial magitech. **In reach or near-reach** with smith guilds, gnome machining culture, and magic heat: screw-cutting lathes, power feed, cam automatics (if someone builds them), Whitworth flats, gauge blocks, governors, basic optics polish. **Not baseline:** naval rangekeepers, Norden bombsights, AA predictors, radar-fed directors. Those need invent arcs, rare workshops, or magic substitutes. Projectiles are mostly magic / runic rather than gunpowder artillery; the **mechanical computing principles** still transfer to runic siege gear, train governors, and shop automation.

Companions: `../Vehicle/Wheels.md`, `../Vehicle/Suspension.md`, `../Metallurgy/CraftMetal.md`, `../../../Ideas.md` (civilian tech shortlist). Hand vs tool precision (Weber, loupes, tremor): `../Body/MeasurementPerception.md`.

---

# Part 1: Machining and Manufacturing

## 1. Screw-cutting lathe (lead screw and change gears)

Henry Maudslay's lathe of about 1800 fixed the layout that every later screw-cutting lathe follows.

- The spindle drives a gear train to a long precision **lead screw** running along the bed.
- A **split (half) nut** on the carriage clamps onto the lead screw. While it is closed the carriage moves a fixed distance per spindle revolution.
- The tool therefore cuts a helix on the rotating workpiece with a pitch set by the gear ratio.
- Pitch is set by swapping **change gears** on a swinging quadrant (banjo):

  TPI cut = lead screw TPI × (driven teeth ÷ driver teeth)

  Example: an 8 TPI lead screw with a 20-tooth gear on the spindle side and a 40-tooth gear on the lead screw side cuts 16 TPI.
- A **tumbler reverser** flips the lead screw direction for backing out or cutting left-hand threads.
- The **compound rest** is set to about 29.5° so each pass infeeds mostly on one flank of the thread.
- A **thread dial** (a small gear on the carriage that rides the lead screw) tells the operator when to close the half nut so the tool falls into the same groove every pass.
- The **Norton quick-change gearbox** (1890s) replaced loose change gears. A tumbler gear slides along a cone of gears so a lever selects the pitch.

## 2. Automatic power feed

- The lead screw is kept for threading only so its wear stays low.
- A separate **feed rod** with a keyway runs the length of the bed. A sliding worm on the apron rides the rod and drives a gear train.
- That train turns a pinion on the bed rack for longitudinal travel or a screw for cross travel. This gives automatic turning and facing.
- A friction or dog clutch in the apron engages and releases the feed. Adjustable **trip stops** on the bed knock the clutch out at a set position.
- Feed per revolution is fixed by the gear ratio between spindle and feed rod.

## 3. Tapping and die heads

- A tap held in the tailstock is advanced by hand while the spindle turns slowly. The tap pulls itself forward along its own thread.
- **Self-opening die heads** (such as the Geometric head) close chasers onto the work and release automatically at a preset length.
- Reversing-clutch tap holders back the tap out without stopping the machine.

## 4. Cam-driven automatic screw machines

Christopher Spencer's automatic screw machine (1870s) removed the operator from the cycle.

- A **camshaft** turns once per part. Each cam profile pushes a lever that moves a cross slide or the turret.
- The **turret** indexes between stations through a Geneva or ratchet mechanism. Each station holds a different tool: drill or form tool or die head or cut-off blade.
- A **stop drum** or lever limits feed depth.
- **Bar stock** is fed by a spring collet and chuck. Stock is pushed forward each cycle and clamped again.
- Cam shape sets stroke and timing and speed. Changing the part means cutting new cams.
- Brown & Sharpe and Davenport screw machines and Swiss-type automatics all work this way.

## 5. Line shaft power

- A water wheel or steam engine turns an overhead **line shaft**.
- A flat belt runs from the line shaft to a **stepped cone pulley** on the headstock. Each step gives a different spindle speed.
- **Back gears** (a reduction pair engaged behind the cone) trade speed for torque on heavy cuts.
- Treadle lathes used a crank and flywheel instead.

## 6. Three-plate flat method (Whitworth, 1830s)

- Two surfaces lapped together can end up as matching convex and concave curves. Three surfaces lapped in rotating pairs cannot. They converge only when all three are true planes.
- This makes flat surfaces from nothing. Machine beds and surface plates and straightedges all trace back to it.

## 7. Johansson gauge blocks (1896)

- Blocks are lapped so flat that they wring together by molecular adhesion and a thin oil film.
- Stacked combinations give any dimension to fractions of a micron.
- They calibrate every other measuring tool in a shop.

## 8. Error-averaging lead screws and dividing engines

- **Rowland's ruling engine screw** (1880s) was lapped with a long nut so its local errors average out. The same method makes accurate lead screws for lathes and milling machines.
- **Dividing engines** cut gear teeth and scale graduations. A master worm wheel is indexed by a screw and any residual error in the wheel is averaged out by repeated indexing and lapping.
- Accurate gears and dials for instruments are cut from this master accuracy.

## 9. Making instrument cams and gears

- **Cams** are profiled by following a large master template with a stylus that steers the cutter. Reduction linkages (pantographs) shrink the master to the working size.
- **Gears** are cut on hobbing or gear shaping machines with dividing heads and are then lapped for smooth meshing.
- **Integrator discs and balls** are hardened and lapped so slip stays low. Any slip is a computing error.

## 10. Jacquard punched cards (1804)

- Each card row lets chosen hooks lift or stay down. The hooks lift chosen warp threads.
- It is the first stored program driving a machine. Cam drums and punched control on automatic machines follow the same idea.

## 11. Watt centrifugal governor (1788)

- Flyballs swing outward as the engine speeds up and close the throttle through a linkage. Slower running opens the throttle.
- It holds line shafts and steam and water power at constant speed so belts and lathes run steadily under changing load.
- It is the model for every later mechanical feedback control.

## 12. Foucault knife-edge test (1858)

- A blade cuts the light at a mirror's focus so surface errors appear as shadows.
- Opticians polish and re-test until the surface is right to a small fraction of a wavelength.
- It makes the lenses and mirrors used in rangefinders and periscopes and telescopes.

---

# Part 2: Super Long-Range Targeting (Naval and Coastal Gunnery)

## The problem

- A large shell flies for 30 to 60 seconds at extreme range. In that time the target moves and the firing ship moves and the ship is rolling.
- The shell is pushed by wind and air density and the rotation of the Earth.
- The gun must be aimed at where the target will be and not where it is.

## Step 1: Measure range and bearing

- **Coincidence rangefinder:** two windows a long baseline apart form two images. The operator rotates a prism until the images line up. The prism angle gives range by triangulation.
- **Stereoscopic rangefinder:** the operator sees a 3D view and the target appears at a depth. A marker in the eyepiece is moved to match.
- Range error grows with the square of range and shrinks with baseline length and magnification. This is why battleships carried long rangefinders in turrets.
- **Bearing** is read from a director telescope high on the ship.

## Step 2: Solve relative motion

- **Dumaresq (1902):** a hand-operated device with sliding scales that solves the relative velocity between own ship and target from own course and speed and the target's estimated course and speed.
- **Dreyer Fire Control Table and Argo Clock (1910s):** clockwork plotters that keep a running estimate of range and bearing. A pen traces predicted range against observed range so the operator can spot a mismatch.
- **Ford rangekeeper (Mark 1 and 1A):** the American solution. It takes range and bearing observations and own ship data and continuously updates the target's estimated motion.

## Step 3: Compute the ballistic solution

The rangekeeper applies these corrections mechanically:

- **Time of flight:** a cam gives shell flight time as a function of range and elevation.
- **Wind:** a component solver splits wind into range and deflection parts.
- **Air density and temperature:** these change drag on the shell. Correction knobs feed the ballistics cams.
- **Powder temperature and gun wear:** these change muzzle velocity. Correction knobs feed the cams.
- **Spin drift:** the shell's rotation pushes it sideways. A correction cam adds a fixed deflection.
- **Coriolis effect:** the Earth's rotation deflects a shell over long flights. The computer includes latitude.
- **Own ship and target motion:** integrators advance the predicted target position through the time of flight.

## Step 4: Stabilize the line of sight

- A **stable element** (a gyro-stabilized vertical reference) senses ship roll and pitch. Its output corrects gun elevation and cross-level so the shell leaves at the correct angle regardless of the deck's motion.

## Step 5: Fire and correct

- **Salvo bracketing:** fire salvos over and short of the target. Splash observations refine the range.
- Spotters report where shells land. The operator enters the correction and the computer updates the range solution.
- Corrections shrink the range error each salvo until hits are scored.

## Step 6: Firing tables

- Trajectories over long ranges are computed offline. The **differential analyzer** (Vannevar Bush, 1931) solved the ballistic differential equations with wheel-and-disc integrators and produced the firing tables used by artillery.

## Mechanical computing elements used

| Element | What it does |
|---|---|
| Differential gear | Adds or subtracts two rotations |
| Cam and follower | Gives a stored function such as time of flight against range |
| Resolver (crank and slider) | Splits a vector into components with sine and cosine |
| Ball-and-disc integrator | Integrates one quantity against another |
| Multiplier (variable-lever) | Multiplies two quantities |
| Servo follow-up | Drives the guns to match the computed angles |

---

# Part 3: Targeting from High Up (Aerial Bombsights)

## The problem

- A bomb released from altitude falls for tens of seconds. It leaves the aircraft with the aircraft's horizontal speed and is slowed by air drag. The drag lag behind the aircraft is called **trail**.
- The correct release point depends on altitude and ground speed and wind drift and trail.
- The aircraft pitches and rolls and yaws during the bombing run.

## Norden bombsight (1930s)

A gyro-stabilized optical sight with a mechanical computer.

1. **Setup:** the bombardier sets altitude and airspeed and the bomb's ballistic trail into the sight.
2. **Stabilization:** gyroscopes hold the telescope steady against aircraft motion. Its line of sight stays true even in a banking or pitching aircraft.
3. **Course end:** the bombardier turns a knob so the crosshair does not drift sideways across the target. This aligns the sight with the actual ground track and gives the drift angle.
4. **Rate end:** the bombardier adjusts a rate knob so the crosshair does not creep forward or back along the track. An internal motor turns the telescope at the rate that holds the target on the crosshair. That rate is proportional to ground speed divided by altitude.
5. **Dropping angle:** the computer combines the rate (which fixes ground speed) with the bomb's time of fall and trail to give the dropping angle.

   tan θ ≈ (ground speed × time of fall − trail) ÷ altitude

6. **Release:** as the target's sighting angle falls to the dropping angle the sight releases the bombs automatically.
7. **Autopilot link (Stabilized Bombing Approach Equipment):** the sight steers the aircraft by feeding the course-end output into the autopilot. The aircraft is flown on the bombing run by the sight.

Ground speed is found by tracking rather than measured directly. The sight solves the wind problem by observing how the target moves across the field of view.

## Sperry S-1

- A similar gyro-stabilized design from the Sperry Gyroscope Company. It also computes a dropping angle by tracking rate.

## Limits

- Cloud cover blocks the view of the target.
- Wind that changes during the bombing run creates errors that the sight cannot predict.
- Altitude must be set correctly. A wrong altitude changes the fall time.

---

# Part 4: Anti-Aircraft Targeting

## The problem

- Aircraft fly fast in three dimensions and the shell needs several seconds to reach altitude.
- The gun must aim at a **future position**.
- The time of flight depends on how far away that future position is. This creates a loop. The gun needs the future position to find the flight time and needs the flight time to find the future position.

## Predictor solution (Kerrison Predictor and similar directors)

1. **Tracking:** operators follow the target with telescopes for **azimuth** and **elevation**. A rangefinder or height finder gives slant range.
2. **Present position:** these three values give the target's present position in space.
3. **Rates:** integrators and rate-measuring linkages estimate how fast the target's position changes.
4. **Assumption:** the target keeps flying straight at the same speed and altitude during the flight of the shell.
5. **Iteration by feedback:** the mechanism guesses a time of flight and computes the future position. It then computes the flight time to that position from a ballistics cam. If the two flight times differ it adjusts the guess. The loop settles on a consistent answer in a fraction of a second.
6. **Output:** gun azimuth and elevation and **fuze time** are sent to the guns.
7. **Fuze setter:** a clockwork fuze is set to burst the shell at the predicted time so it explodes near the target.

## Naval AA systems (Mark 37 Gun Fire Control System)

- A **director** on the ship tracks the target with optics. Later radar supplied range.
- A **stable element** holds the gyro reference to correct for ship roll and pitch.
- The **Mark 1 computer** in the plotting room solves the predicted position and gun angles.
- The gun mounts follow the computer's commands automatically.
- The straight-line constant-speed assumption gives good results for a few seconds of flight but fails against maneuvering targets.

## Gyroscopic lead-computing sight (Mark 14)

A compact solution for small AA guns.

- The gunner tracks the target with the reticle. As the gun swings the gyroscope resists the motion and precesses. The precession moves the reticle away from the line of sight by an angle proportional to the gun's turning rate.
- Because the lead angle is equal to target angular rate multiplied by flight time the shifted reticle points at the future position.
- Range is entered by adjusting the reticle size (a ring of dots) to match the target's wingspan. The reticle size acts as a range estimator that sets flight time.
- The gunner simply keeps the target on the reticle and fires. The lead is applied automatically.

## Why it works

- Feedback loops solve the flight time and the future position together.
- Rate measurement replaces prediction from history.
- Cams supply the ballistic function of time of flight against range and elevation.

---

# Part 5: Shared Principles

- **Bootstrapping precision:** flat surfaces and true screws come from lapping parts against each other until the errors average out. Tools make better tools.
- **Function generation with cams:** a cam profile stores a mathematical function and follows it as it rotates.
- **Summing and integrating with gears:** differential gears add and wheel-and-disc units integrate.
- **Feedback with linkages:** governors and iterative solvers compare a computed value to a target and push the error toward zero.
- **Stored programs on cams and cards:** the Jacquard loom and screw-machine cams and ballistics cams are the same idea.
- **Gyroscopes as references:** a spinning mass keeps its orientation. It stabilizes sights and provides a stable vertical and measures turn rate.
- **Precision of manufacture is the limit:** a rangekeeper or bombsight is only as accurate as its cams and gears and integrator discs. The machining methods in Part 1 made those parts.
