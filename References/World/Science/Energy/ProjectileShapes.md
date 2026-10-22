# Projectile Shapes, Flight Patterns and Stability

> Earth reference / invent loot. Not locked law. Launch physics / sphere scatter / flywheel: `Projectiles.md`. Guided munitions: `GuidedProjectiles.md`. Arrowheads: `../Metallurgy/Arrowheads.md`. Kinetic impartation: `KineticImpartation.md`. Recoil: `Kinetic.md`. Terminal / wounding tables: `../../../Combat/Firearms.md`. Space combat / debris: `../../../Combat/SpaceProjectiles.md`. Propellant: `GunpowderFirearms.md`.

Nav: `Index.md`. Hub: `../Science.md`.

Complete reference for atmosphere and vacuum.

---

## Contents

1. Core Physics
2. Stabilization Methods
3. Flight Patterns in Atmosphere
4. Flight in Vacuum
5. Projectile Catalog
6. The Hypersonic Needle
7. Penetration and Terminal Effects (pointer: Combat/Firearms.md)
8. Comparison Tables
9. Key Takeaways

---

## 1. Core Physics

Sphere scatter, transonic Cd and random Magnus on uncontrolled spin: `Projectiles.md` (Sphere flight randomness). This file owns shapes, CM/CP, stabilization and vacuum orientation.

### 1.1 Forces Acting on a Projectile

| Force or Moment | What It Does | Present in Vacuum |
|---|---|---|
| Gravity | Pulls the projectile down. Acts at the center of mass. Uniform gravity produces no rotation. | Yes |
| Drag | Slows the projectile. Scales with air density, velocity squared, frontal area and drag coefficient. Peaks near Mach 1. | No |
| Normal force (lift) | Pushes sideways whenever the projectile flies at an angle to its direction of travel. | No |
| Overturning moment | Rotates the projectile when the normal force acts away from the center of mass. | No |
| Damping moment | Resists angular motion. Fins generate strong damping. | No |
| Magnus force | Sideways push created by spin combined with yaw. | No |
| Coriolis effect | Apparent deflection caused by the rotation of the planet. Matters at long range. | Yes (if on a rotating body) |
| Gravity gradient | Tiny torque that aligns long objects vertically. Matters only at orbital scales. | Yes |

### 1.2 Center of Mass vs Center of Pressure

Every projectile has two key points:

- **Center of mass (CM):** where gravity and inertia effectively act.
- **Center of pressure (CP):** where the combined aerodynamic forces effectively act.

The relationship between the two decides everything about atmospheric stability:

- **CP behind CM:** statically stable. A disturbance creates a restoring force that swings the nose back into the airflow. The projectile weathervanes. Arrows, darts, mortar bombs, APFSDS rods and shuttlecocks work this way.
- **CP ahead of CM:** statically unstable. A disturbance creates a moment that tries to flip the projectile backward. Nearly every bullet and artillery shell falls into this category because the pointed nose generates most of the lift forward of the center of mass. These need spin to survive.
- **Static margin:** the distance between CM and CP, usually measured in calibers. A larger margin gives stronger correction. A smaller margin gives a more responsive but less forgiving projectile.

### 1.3 Static vs Dynamic Stability

- **Static stability:** whether a disturbance produces a restoring force at all.
- **Dynamic stability:** whether the resulting oscillations shrink or grow over time.

A projectile can be statically stable yet dynamically unstable. Its oscillations grow until it tumbles. A spin-stabilized shell is statically unstable yet can be both gyroscopically and dynamically stable.

### 1.4 Gyroscopic Stability

Spin gives the projectile angular momentum. When the overturning moment pushes on the nose, the spinning body precesses (the nose circles) instead of flipping.

- **Gyroscopic stability factor (Sg):** ratio of gyroscopic stiffness to overturning tendency.
  - Below 1.0: unstable. The projectile tumbles.
  - 1.0 to about 1.3: marginal. Accuracy suffers and cold dense air can push it into instability.
  - About 1.3 to 2.5: normal operating range.
  - Very high: overstabilized. The nose refuses to follow a curving trajectory in high-angle fire.
- **Length matters most.** Longer projectiles have larger overturning moments and need faster spin. The Greenhill rule of thumb captures this: required twist rate gets faster as bullet length grows. Practical spin-stabilized projectiles top out around 5 to 7 calibers long.
- **Air density matters.** Thin air lowers the overturning moment and raises stability. Cold dense air lowers stability.
- **Stability usually increases downrange.** Spin decays more slowly than forward velocity, so a bullet that leaves the muzzle marginally stable often becomes more stable as it travels.

### 1.5 Angular Motion Modes

| Mode | Description |
|---|---|
| Yaw | Angle between the projectile's axis and its direction of travel. |
| Precession (slow mode) | Large slow circling of the nose around the flight path. |
| Nutation (fast mode) | Small fast wobble superimposed on precession. |
| Coning | Combined circular yaw motion. Visible as a spiraling nose. |
| Yaw of repose | Small steady yaw that lets a spinning bullet's nose track a curving trajectory. Produces spin drift. |
| Tumbling | Continuous end-over-end rotation after stability fails. |
| Keyholing | Bullet strikes sideways and leaves an elongated hole. Sign of instability. |
| Porpoising / fishtailing | Pitch or yaw oscillation in a single plane. Common with arrows and flexible projectiles. |

### 1.6 Mach Regimes

| Regime | Mach Number | Behavior |
|---|---|---|
| Subsonic | Below 0.8 | Drag dominated by skin friction and base drag. Boat-tails help the most here. |
| Transonic | 0.8 to 1.2 | Shock waves form and shift. CP moves. Drag spikes. Many projectiles wobble or destabilize while passing through. |
| Supersonic | 1.2 to 5 | Wave drag dominates. Sharp noses pay off. Boat-tails help less. |
| Hypersonic | Above 5 | Severe aerodynamic heating. Shock lies close to the body. Tips and fins ablate. Thin fins lose authority. Flares become attractive. |
| Hypervelocity impact | Roughly 3 km/s and above at impact | Projectile and target behave like fluids on contact. Material strength matters little. |

### 1.7 Sectional Density and Ballistic Coefficient

- **Sectional density:** mass divided by frontal area. Higher values hold velocity better and penetrate deeper.
- **Ballistic coefficient (BC):** sectional density divided by a form factor that describes shape efficiency. A higher BC means slower deceleration, a flatter trajectory and less wind drift.
- **Long, thin, dense and pointed** wins on both counts. This is why the long rod penetrator dominates anti-armor kinetic weapons.

---

## 2. Stabilization Methods

### 2.1 No Stabilization (Symmetric Shapes)

A sphere has no preferred orientation, so it presents the same shape no matter how it rotates.

- **Strengths:** cheap, simple, orientation never matters.
- **Weaknesses:** very low ballistic coefficient. Random spin produces Magnus curves. Rough or non-spinning surfaces can produce erratic knuckleball motion.
- **In vacuum:** ideal. Orientation is irrelevant and drag no longer punishes the blunt shape.

### 2.2 Spin Stabilization

Methods of imparting spin:

- Rifled barrels (grooves engraved into the projectile or its driving band)
- Gain twist barrels (twist rate increases toward the muzzle)
- Canted fins or canted rocket nozzles
- Spin tables (spacecraft and upper-stage rockets)

| Strengths | Weaknesses |
|---|---|
| Compact. No fins needed. | Practical length limit of about 5 to 7 calibers. |
| Works in atmosphere and vacuum. | Spin breaks up shaped charge jets. |
| Low drag. | Produces spin drift. |
| Holds orientation against small disturbances. | Overstabilization in high-angle fire keeps the nose pointed upward. |

### 2.3 Fin Stabilization

Fins move the center of pressure behind the center of mass.

- **Strengths:** works at any length-to-diameter ratio. Strong damping. Handles launch disturbances well.
- **Weaknesses:** adds drag. Usually needs a smoothbore or a sabot. Thin fins heat and ablate at hypersonic speed. Completely useless in vacuum.
- **Slow roll:** many fin-stabilized rounds use slightly canted fins to induce a slow roll. The roll averages out manufacturing asymmetries. It does not provide the main stability.
- **Crosswind behavior:** fin-stabilized projectiles turn their nose into a crosswind. Unpowered ones still drift downwind. Rockets under thrust turn into the wind and actually fly upwind.

### 2.4 Flare (Drag) Stabilization

A conical skirt at the tail, or a light trailing body behind a heavy nose, holds the CP aft.

- **Strengths:** survives heating far better than fins. Mechanically simple.
- **Weaknesses:** more drag than fins.
- **Examples:** shuttlecocks, Brenneke and Foster shotgun slugs, some explosively formed penetrators, some hypersonic test projectiles.

### 2.5 Weight-Forward Stabilization

Instead of pushing the CP back, this moves the CM forward.

- **Examples:** arrows with heavy points, Foster slugs, lawn darts, the Lazy Dog steel dart.
- Often combined with fins or flares.

### 2.6 Active Stabilization

- Movable fins or canards
- Thrust vectoring
- Side thrusters or cold-gas jets
- Reaction wheels (vacuum)

The only method that can actually steer. Expensive and complex.

### 2.7 Hybrid Lift and Spin

Discs and ring airfoils use spin to hold orientation while their shape produces lift. Frisbees, chakrams and ring airfoil projectiles fall here.

### 2.8 Stabilization Method Summary

| Method | Max Practical Length | Works in Vacuum | Drag Penalty | Heat Tolerance | Steering |
|---|---|---|---|---|---|
| None (sphere) | Not applicable | Yes (no need) | High | High | No |
| Spin | About 5 to 7 calibers | Yes | Low | High | No |
| Fins | Unlimited (30+ calibers) | No | Moderate | Low at hypersonic | No |
| Flare | Unlimited | No | High | High | No |
| Weight-forward | Moderate | No | Varies | Varies | No |
| Active | Unlimited | Yes (thrusters, wheels) | Varies | Varies | Yes |

---

## 3. Flight Patterns in Atmosphere

### 3.1 Trajectory Shape

- **In vacuum:** a perfect symmetric parabola.
- **In air:** drag bends the parabola into an asymmetric curve. The apex shifts toward the target. The descending branch is steeper than the ascending branch. Impact angle is steeper than launch angle.
- **Maximum range angle:** below 45 degrees for most small arms (often around 30 to 35 degrees) because drag punishes long flight times. Above 45 degrees for very high-velocity long-range guns that reach thin upper air quickly.

### 3.2 Fire Types

| Type | Description | Typical Weapons |
|---|---|---|
| Flat (direct) fire | Low angle. Line of sight to target. | Rifles, tank guns, anti-tank guns |
| Plunging fire | Projectile descends at a steep angle at long range. | Machine guns at extreme range, naval guns |
| Indirect (high-angle) fire | Lofted over obstacles. | Howitzers, mortars |

### 3.3 Sources of Deflection

| Source | Effect | Notes |
|---|---|---|
| Wind drift | Pushes the projectile downwind. | Biggest error source for small arms. |
| Spin drift | Right-hand twist drifts right. Left-hand twist drifts left. | Caused by yaw of repose. Grows with time of flight. |
| Magnus effect | Sideways push from spin plus yaw. | Small for bullets. Large for spinning balls. |
| Aerodynamic jump | Vertical shift caused by a crosswind at the muzzle. | Appears immediately and stays constant. |
| Coriolis effect | Deflects right in the Northern Hemisphere. | Matters beyond roughly 1 km. |
| Eötvös effect | Eastward shots hit slightly high. Westward shots hit slightly low. | Long range only. |

### 3.4 Velocity Decay Patterns

- **Spheres:** lose speed fastest. Musket balls dropped below half their muzzle velocity within roughly 100 to 200 m.
- **Round and flat noses:** moderate loss.
- **Spitzers:** much slower loss.
- **Spitzer boat-tails and very-low-drag designs:** slowest loss among spin-stabilized shapes.
- **Long rod penetrators:** lose roughly 50 to 100 m/s per kilometer. Extremely efficient.

### 3.5 The Transonic Problem

As a projectile slows through Mach 1.2 to 0.8, shock waves move along its body, the center of pressure shifts and drag swings violently. Many bullets that fly well at supersonic speed begin to wobble or tumble here. Long-range shooters often define effective range as the point where the bullet goes transonic.

### 3.6 Instability Patterns

| Pattern | Cause | Result |
|---|---|---|
| Keyholing | Insufficient spin | Sideways impacts. Large group sizes. |
| Tumbling | Total loss of stability | Rapid velocity loss. Wild deflection. |
| Coning growth | Dynamic instability | Accuracy degrades with range. |
| Fishtailing | Flexible shaft (arrows) | The archer's paradox. Shaft bends around the bow and recovers. |
| Launch yaw | Muzzle blast, crown damage, sabot discard | Initial wobble that fins or spin must damp. |
| Transonic buffet | Shock movement near Mach 1 | Wobble or tumbling at long range. |
| Overstabilization | Too much spin in high-angle fire | Shell lands base-first or flat. Nose fuzes can fail. |

### 3.7 Ricochet

- Shallow impact angles favor ricochet.
- Round noses and spheres ricochet readily.
- Water causes ricochet at surprisingly steep angles for spinning bullets. Naval round shot was deliberately skipped across water to extend range.
- After a ricochet most spin-stabilized projectiles tumble.

### 3.8 Behavior in Dense Media

Air is thin. Water, soil and tissue are roughly a thousand times denser. A spin-stabilized bullet tuned for air is badly understabilized in dense media. It yaws and often turns completely around. Fin-stabilized flechettes may bend into a hook shape. Spheres decelerate quickly but stay straight.

---

## 4. Flight in Vacuum

### 4.1 What Disappears

- Drag
- Lift and normal force
- Magnus force
- Wind
- Overturning moment
- Aerodynamic damping
- In-flight heating
- Sound barrier effects

### 4.2 What Remains

- **Gravity:** acts at the center of mass. Uniform gravity produces no torque, so it cannot rotate the projectile.
- **Gravity gradient:** a tiny torque that aligns long objects vertically. Only matters over orbital scales and long durations.
- **Launch conditions:** every bit of rotation imparted at launch persists for the entire flight.
- **Internal flexing:** a spinning body that flexes loses energy and slowly changes its spin axis.
- **Planetary rotation:** Coriolis still applies when firing from a rotating body.

### 4.3 Trajectory

A perfect parabola. Impact angle equals launch angle on level ground.

- **Range on level ground:** R = v² × sin(2θ) / g
- **Maximum range:** at 45 degrees, R = v² / g
- **Maximum height at 45 degrees:** v² / (4g)

**Example vacuum ranges at Earth gravity (9.81 m/s²), fired at 45 degrees:**

| Muzzle Velocity | Example | Vacuum Range | Typical Range in Air |
|---|---|---|---|
| 340 m/s | Subsonic pistol | About 11.8 km | About 1.5 to 2 km |
| 900 m/s | Rifle | About 82.6 km | About 3 to 5 km |
| 1,600 m/s | Tank APFSDS | About 261 km | Tens of km at best |
| 2,500 m/s | Railgun | About 637 km | Roughly 100 to 200 km claimed for guided rounds |
| 7,900 m/s | Low Earth orbit speed | Orbits the planet | Not applicable |

Above a few hundred kilometers the flat-ground assumption breaks down. Planetary curvature and decreasing gravity with altitude extend the real range further.

### 4.4 Orientation Behavior

- **Any launch wobble lasts forever.** In air, fins damp out tip-off yaw. In vacuum there is no damping, so a small rotation at launch becomes a permanent tumble or coning motion.
- **The projectile does not nose over.** In air it weathervanes to follow its curving path. In vacuum it keeps pointing in the launch direction while gravity bends the trajectory downward, so the angle between its axis and its direction of travel grows over time.
- **Flat fast shots stay nearly aligned.** At 1,600 m/s over 2 km, flight time is about 1.25 s. Gravity adds about 12 m/s of downward velocity. The projectile ends up only about 0.4 degrees off its path.
- **Lofted shots arrive sideways.** A needle fired at 45 degrees upward keeps pointing 45 degrees upward. It arrives traveling 45 degrees downward. It strikes completely broadside, 90 degrees off its path.

### 4.5 How to Keep a Projectile Stable in Vacuum

1. **Clean launch:** a precise bore, a symmetric sabot release and a rigid projectile reduce initial angular rate to near zero. Since nothing disturbs the projectile afterward, this is the single most important factor.
2. **Spin:** spin about the long axis gives gyroscopic stiffness against small launch asymmetries. Any wobble becomes a fixed bounded coning motion instead of a tumble. In vacuum spin no longer fights aerodynamic overturning, so modest spin rates are enough.
3. **Rigidity over long flights:** a spinning body that flexes internally loses energy and gradually shifts its rotation toward its axis of maximum moment of inertia. For a needle that is end-over-end. The Explorer 1 satellite failed this way in 1958 when its flexible antennas drained spin energy and it went into a flat spin. Over seconds this does not matter. Over hours or days a needle must be extremely stiff or actively controlled.
4. **Pre-aimed orientation:** for a known trajectory, the launch orientation can be offset so the projectile meets the target nose-first, since it will not rotate to follow the arc.
5. **Active attitude control:** cold-gas jets or an internal reaction wheel can steer orientation during flight. This is the only way to make a projectile actually track its curving path.
6. **Gravity gradient:** too weak to help on any weapon-scale flight.

### 4.6 Shape Implications in Vacuum

- **Aerodynamic shaping becomes irrelevant during flight.** A sphere retains velocity exactly as well as a spitzer.
- **Shape only matters at impact.**
- **Fins become dead weight.**
- **Flares become dead weight.**
- **Long rods need orientation control.** A rod that arrives yawed loses much of its penetration.
- **Spheres and compact shapes need no orientation control at all.** For simple kinetic kill in vacuum they are often the most practical choice.

### 4.7 Space Combat Considerations

Space combat, debris and orbital shotgun detail: `../../../Combat/SpaceProjectiles.md`.

### 4.8 Airless Planetary Surfaces

On bodies like the Moon, trajectories are pure parabolas under local gravity.

| Lunar Value | Figure |
|---|---|
| Surface gravity | 1.62 m/s² |
| Circular orbit speed at the surface | About 1.68 km/s |
| Escape velocity | About 2.38 km/s |

- A rifle bullet fired at 45 degrees on the Moon travels hundreds of kilometers. Lunar curvature strongly affects the result.
- A tank APFSDS round at about 1,700 m/s fired horizontally on the Moon is close to circular orbit speed. Terrain aside, it would circle the Moon.
- A railgun round would leave the Moon entirely.

### 4.9 Vacuum-to-Atmosphere Transition

Projectiles that start in space and descend into atmosphere (kinetic bombardment) face both problems:

- Orientation must be set before entry since nothing aligns it in vacuum.
- Once air thickens, aerodynamic stability takes over. A flare or fins can then align it.
- Entry heating ablates the tip and edges.
- A tumbling rod that enters sideways experiences massive drag and heating and may break apart.

---

## 5. Projectile Catalog

Each entry covers: **Shape**, **Stabilization**, **Atmospheric Flight**, **Vacuum Flight** and **Weapon Effectiveness**.

### 5.1 Unstabilized Shapes

#### Sphere (Musket Ball, Round Shot, Buckshot, Ball Bearing)
- **Shape:** perfect or near-perfect sphere.
- **Stabilization:** none needed.
- **Atmospheric flight:** very poor ballistic coefficient. Rapid velocity loss. Random spin from bore contact produces Magnus curving. Smoothbore muskets were effective to roughly 50 to 100 m against massed formations.
- **Vacuum flight:** excellent. No orientation issues. Retains full velocity.
- **Effectiveness:** cheap and reliable. Strong close-range effect. Poor range and accuracy in air. Large naval round shot smashed hulls and rigging. In vacuum the sphere becomes one of the best simple kinetic projectiles available.

#### Irregular Fragments (Shell Fragments, Flak, Preformed Fragments)
- **Shape:** random jagged pieces, cubes, rods or preformed spheres.
- **Stabilization:** none. They tumble.
- **Atmospheric flight:** extremely high drag. Very high initial velocity but short effective range (tens to a few hundred meters).
- **Vacuum flight:** retain velocity indefinitely. Form a permanent expanding debris cloud.
- **Effectiveness:** the main killing mechanism of artillery. Most WWI and WWII casualties came from fragments. Preformed cubes and spheres give more predictable patterns than random fragmentation.

#### Chain Shot and Bar Shot
- **Shape:** two balls or half-balls joined by a chain or bar.
- **Stabilization:** none. Spins end over end.
- **Atmospheric flight:** high drag. Poor accuracy. Spinning motion sweeps a wide path.
- **Vacuum flight:** spins indefinitely on a parabola.
- **Effectiveness:** designed to cut sails and rigging in naval combat. Limited range. Obsolete after sail.

#### Canister and Grapeshot
- **Shape:** many balls packed in a container that breaks apart at the muzzle.
- **Stabilization:** none.
- **Atmospheric flight:** forms a cone like a giant shotgun. Effective out to a few hundred meters.
- **Vacuum flight:** cone expands without slowing. Pattern density drops with the square of distance.
- **Effectiveness:** devastating against infantry at close range. Napoleonic and Civil War artillery relied on it to break assaults.

#### Shrapnel Balls (Shrapnel Shell Payload)
- **Shape:** lead or steel balls carried inside a shell.
- **Stabilization:** the shell is spin-stabilized. The balls are not.
- **Atmospheric flight:** a time fuze ejects the balls forward in a cone above the target. The balls inherit the shell's forward velocity.
- **Vacuum flight:** the cone continues expanding without slowing.
- **Effectiveness:** very effective against troops in the open early in WWI. Nearly useless against troops in trenches or dugouts. High explosive shells largely replaced it by the war's end.

### 5.2 Spin-Stabilized Small Arms Bullets

#### Round Nose (RN)
- **Shape:** cylinder with a hemispherical or blunt-curved nose.
- **Stabilization:** spin.
- **Atmospheric flight:** moderate drag. Short to medium range. Reliable feeding in early firearms.
- **Vacuum flight:** identical to any other shape until impact.
- **Effectiveness:** adequate at short range. Prone to ricochet. Common in early military cartridges and handguns.

#### Flat Nose, Wadcutter and Semi-Wadcutter
- **Shape:** blunt front face. Wadcutters are nearly pure cylinders. Semi-wadcutters have a small truncated nose with a sharp shoulder.
- **Stabilization:** spin.
- **Atmospheric flight:** high drag. Short range.
- **Vacuum flight:** no penalty for the blunt shape.
- **Effectiveness:** wadcutters punch clean holes for target scoring. Flat noses crush rather than push tissue aside. Flat noses are required in tube-magazine rifles to avoid primer strikes. Poor at long range.

#### Minié Ball (Conical Expanding-Base Bullet)
- **Shape:** conical soft lead bullet with a hollow base.
- **Stabilization:** spin. The hollow base expands on firing to grip the rifling.
- **Atmospheric flight:** far better than musket balls. Accurate to several hundred meters.
- **Vacuum flight:** same as any spinning slug.
- **Effectiveness:** revolutionized 19th-century warfare by giving common infantry rifled accuracy with muzzleloader speed. Heavy soft lead produced severe wounds. Made Napoleonic close-order tactics suicidal.

#### Spitzer
- **Shape:** sharply pointed ogive nose on a flat-based cylinder.
- **Stabilization:** spin.
- **Atmospheric flight:** low supersonic drag. Flat trajectory. Long range. Introduced around 1898 to 1905 (French Balle D and German S Patrone).
- **Vacuum flight:** no advantage over blunter shapes during flight.
- **Effectiveness:** standard WWI rifle and machine gun bullet. Dramatically extended effective range of infantry and machine gun fire. Its long light nose and rear-heavy mass make it prone to yawing in tissue.

#### Spitzer Boat-Tail (SBT)
- **Shape:** spitzer with a tapered base.
- **Stabilization:** spin.
- **Atmospheric flight:** reduced base drag. The benefit is largest at subsonic and transonic speeds, so it shines at long range where bullets slow down.
- **Vacuum flight:** base taper has no effect.
- **Effectiveness:** standard for long-range rifle and machine gun ammunition. Greatly extended plunging fire range for WWI and WWII machine guns.

#### Very-Low-Drag (VLD) and Secant Ogive Designs
- **Shape:** very long secant ogive nose with a boat-tail. Long overall length.
- **Stabilization:** spin. Requires fast twist rates.
- **Atmospheric flight:** highest ballistic coefficients among conventional bullets. Stays supersonic longest.
- **Vacuum flight:** no advantage.
- **Effectiveness:** precision and sniper use. Excellent wind resistance. Sensitive to seating depth and twist rate.

#### Full Metal Jacket (FMJ)
- **Shape:** lead core fully enclosed in a copper or steel jacket on the nose.
- **Stabilization:** spin.
- **Atmospheric flight:** depends on profile (usually spitzer or round nose).
- **Vacuum flight:** same.
- **Effectiveness:** reliable feeding. Deep penetration. Does not expand. Military standard under the Hague Convention of 1899, which banned expanding bullets in international war. Wounding depends heavily on yaw and fragmentation behavior.

#### Hollow Point and Soft Point (Expanding)
- **Shape:** exposed lead tip or hollow cavity in the nose.
- **Stabilization:** spin.
- **Atmospheric flight:** slightly worse drag than pointed FMJ. Polymer tips restore pointed profiles.
- **Vacuum flight:** same as any bullet.
- **Effectiveness:** expands on impact to increase frontal area. Reduces over-penetration. Transfers more energy within the target. Standard for hunting and police use. Banned for international armed conflict under the Hague Convention.

#### Armor-Piercing (Hardened Core)
- **Shape:** spitzer with a hardened steel or tungsten carbide core.
- **Stabilization:** spin.
- **Atmospheric flight:** similar to standard spitzer. Often slightly lighter for its size.
- **Vacuum flight:** same.
- **Effectiveness:** defeats light armor, body armor and cover. WWI introduced the German K bullet with a steel core to defeat British trench shields and early tanks.

#### Tracer
- **Shape:** standard profile with a pyrotechnic compound in the base.
- **Stabilization:** spin.
- **Atmospheric flight:** burning base fills the low-pressure wake and slightly reduces base drag. Mass shifts as the compound burns, which slightly changes trajectory.
- **Vacuum flight:** burns without oxygen only if the compound carries its own oxidizer. Visible only by its own light.
- **Effectiveness:** fire correction for machine guns and aircraft guns. Reveals the firer's position. Incendiary effect against fuel and balloons.

#### Monolithic Solid Copper or Brass
- **Shape:** single-piece bullet, often with hollow point or grooves.
- **Stabilization:** spin. Longer than lead for the same weight, so needs faster twist.
- **Atmospheric flight:** good with boat-tail and pointed designs.
- **Vacuum flight:** same.
- **Effectiveness:** retains nearly all mass. Deep penetration. Lead-free.

### 5.3 Shotgun Slugs

#### Foster Slug
- **Shape:** soft lead slug with a deep hollow rear. Mass concentrated in the nose.
- **Stabilization:** weight-forward drag stabilization. The external ribs do not impart meaningful spin.
- **Atmospheric flight:** flies like a shuttlecock. Accurate to about 75 to 100 m.
- **Vacuum flight:** no stabilization. Holds launch orientation.
- **Effectiveness:** powerful short-range impact from a smoothbore. Large wound or impact effect. Poor range.

#### Brenneke Slug
- **Shape:** solid lead slug with an attached fiber or plastic wad.
- **Stabilization:** drag stabilized. The wad acts like an arrow's tail.
- **Atmospheric flight:** similar to Foster. Slightly better penetration.
- **Vacuum flight:** same as Foster.
- **Effectiveness:** strong penetration for a shotgun. Used against large game and vehicles at short range.

#### Sabot Slug
- **Shape:** sub-caliber slug carried in a plastic sabot.
- **Stabilization:** spin from a rifled barrel.
- **Atmospheric flight:** much better ballistic coefficient. Accurate to 150 to 200 m.
- **Vacuum flight:** same as any spin-stabilized slug.
- **Effectiveness:** turns a shotgun into a short-range rifle.

### 5.4 Spin-Stabilized Artillery and Tank Projectiles

#### Common High Explosive (HE) Shell
- **Shape:** ogival nose, cylindrical body, copper or plastic driving band. Often a boat-tail.
- **Stabilization:** spin from rifling engaging the driving band.
- **Atmospheric flight:** good ballistic coefficient. Ranges of 10 to 30+ km depending on gun.
- **Vacuum flight:** perfect parabola. Holds launch orientation, so high-angle fire lands sideways or base-first.
- **Effectiveness:** the dominant killer of WWI. Blast and fragmentation destroy trenches, wire, guns and troops. Effectiveness depends on fuzing (impact, delay, time, proximity).

#### Base Bleed Shell
- **Shape:** HE shell with a slow-burning gas generator in the base.
- **Stabilization:** spin.
- **Atmospheric flight:** gas fills the low-pressure wake. Reduces base drag. Extends range by roughly 20 to 30 percent.
- **Vacuum flight:** no benefit. Base drag does not exist.
- **Effectiveness:** longer range without a rocket. Slightly lower payload.

#### Rocket-Assisted Projectile (RAP)
- **Shape:** HE shell with a small rocket motor in the base.
- **Stabilization:** spin.
- **Atmospheric flight:** rocket ignites after launch and adds velocity. Range gains of 30 percent or more. Thrust misalignment reduces accuracy.
- **Vacuum flight:** rocket adds velocity without fighting drag. Thrust misalignment errors persist uncorrected.
- **Effectiveness:** extended range at the cost of payload and accuracy.

#### Paris Gun Shell (WWI)
- **Shape:** long slender shell with pre-engraved rifling bands.
- **Stabilization:** spin.
- **Atmospheric flight:** muzzle velocity around 1,600 m/s. Fired at about 50 degrees. Climbed roughly 40 km into the stratosphere where thin air allowed near-vacuum flight. Range about 130 km. Gunners corrected for Coriolis effect.
- **Vacuum flight analogy:** the shell spent most of its flight in near-vacuum conditions. This is why it fired above 45 degrees.
- **Effectiveness:** tiny payload. Inaccurate at the target scale. Purely psychological against Paris. Barrels wore out after roughly 65 shots and were rebored to larger calibers.

#### Armor-Piercing (AP), APC, APBC and APCBC
- **Shape:** solid hardened steel shot. Variants add caps.
  - **AP:** plain pointed shot.
  - **APC (capped):** soft steel cap absorbs shock and prevents shattering on face-hardened armor.
  - **APBC (ballistic cap):** thin pointed windscreen over a blunt penetrating nose.
  - **APCBC:** both caps.
- **Stabilization:** spin.
- **Atmospheric flight:** ballistic caps restore good aerodynamics to blunt shock-resistant noses.
- **Vacuum flight:** ballistic caps are pointless. Penetrating caps still matter at impact.
- **Effectiveness:** WWII standard for tank and anti-tank guns. Full-caliber shot retains energy well at long range.

#### Armor-Piercing High Explosive (APHE)
- **Shape:** AP shell with a small explosive filler and base fuze.
- **Stabilization:** spin.
- **Effectiveness:** penetrates then detonates inside. Devastating behind armor. Smaller filler reduces penetration compared to solid shot.

#### APCR / HVAP (Composite Rigid / Hypervelocity)
- **Shape:** dense tungsten carbide core inside a lightweight full-caliber body.
- **Stabilization:** spin.
- **Atmospheric flight:** high muzzle velocity. The light overall projectile has low sectional density, so it loses speed quickly.
- **Vacuum flight:** high velocity retained indefinitely. The main weakness disappears.
- **Effectiveness:** excellent at short range. Poor at long range. Tungsten shortages limited WWII production.

#### APDS (Discarding Sabot)
- **Shape:** sub-caliber dense core carried by a full-caliber sabot that falls away at the muzzle.
- **Stabilization:** spin.
- **Atmospheric flight:** high velocity with high sectional density. Much better retention than APCR. Length limited to about 5 to 7 calibers by spin stability.
- **Vacuum flight:** excellent. Spin holds orientation.
- **Effectiveness:** dominant anti-armor round from late WWII through the 1970s. Replaced by APFSDS once longer rods became necessary.

#### HESH / HEP (High Explosive Squash Head)
- **Shape:** thin-walled shell with a plastic explosive filler and base fuze.
- **Stabilization:** spin. Spin does not harm its effect.
- **Atmospheric flight:** relatively low velocity. Arcing trajectory.
- **Vacuum flight:** same.
- **Effectiveness:** explosive flattens against armor before detonating. The shockwave knocks spall off the interior face. Effective against concrete and buildings. Defeated by spaced armor and appliqué layers.

#### Spin-Compensated HEAT
- **Shape:** shaped charge shell with a slipping driving band or internal bearing.
- **Stabilization:** shell spins slowly or the liner is decoupled from spin.
- **Effectiveness:** compromise solution. Full-speed spin disperses the shaped charge jet, so most HEAT rounds use fins instead.

### 5.5 Fin and Drag-Stabilized Projectiles

#### Arrow
- **Shape:** long thin shaft, heavy point, fletching at the rear.
- **Stabilization:** fins (fletching) plus weight-forward. Helical fletching adds spin.
- **Atmospheric flight:** strong static stability. Flexes and oscillates early in flight (archer's paradox). Low velocity. Arcing trajectory.
- **Vacuum flight:** fletching useless. Holds launch orientation. Any launch wobble continues forever. Shaft flex slowly drains energy.
- **Effectiveness:** effective hunting and war weapon for millennia. Bodkin points defeated mail. War arrows remained relevant until gunpowder matured.

#### Crossbow Bolt (Quarrel)
- **Shape:** shorter, thicker and heavier than an arrow.
- **Stabilization:** vanes and weight-forward.
- **Atmospheric flight:** flatter at short range. Higher drag at long range.
- **Vacuum flight:** same as arrow.
- **Effectiveness:** strong armor penetration at short range. Slow reload.

#### Flechette
- **Shape:** small steel nail-like dart with stamped or machined fins.
- **Stabilization:** fins.
- **Atmospheric flight:** excellent ballistic coefficient for its size. Holds velocity well.
- **Vacuum flight:** fins useless. Must be launched cleanly. In a cloud, orientation of individual darts varies.
- **Effectiveness:**
  - WWI aircraft dropped steel fléchettes by the bucket onto troops and cavalry. Falling at terminal velocity they could pass through a man.
  - Vietnam-era beehive artillery rounds fired thousands of flechettes in a forward cone.
  - Experimental small arms (SPIW and similar) fired single flechettes at very high velocity.
  - High penetration. Narrow wound channels unless they bend or yaw.

#### Lazy Dog
- **Shape:** solid steel dart with fins. No explosive.
- **Stabilization:** fins plus weight-forward.
- **Atmospheric flight:** dropped from aircraft. Reaches high terminal velocity through free fall.
- **Vacuum flight:** would accelerate without limit until impact.
- **Effectiveness:** penetrated light cover and vehicles. Cheap area denial. Korean War and Vietnam use.

#### Mortar Bomb
- **Shape:** teardrop body with a fin assembly on a tail boom.
- **Stabilization:** fins.
- **Atmospheric flight:** subsonic to low supersonic. Very high-angle trajectory. Steep descent.
- **Vacuum flight:** fins useless. Holds launch orientation. High-angle shots would land tail-down without aerodynamic nose-over.
- **Effectiveness:** light, simple, portable indirect fire. Steep impact angle drops fragments into trenches and behind cover. The Stokes mortar of WWI established the modern form.

#### APFSDS (Armor-Piercing Fin-Stabilized Discarding Sabot)
- **Shape:** long tungsten heavy alloy or depleted uranium rod. Length-to-diameter ratio of 20 to 30 or more. Fins at the tail. Sabot discarded at the muzzle.
- **Stabilization:** fins. Canted fins induce a slow roll to average asymmetries.
- **Atmospheric flight:** muzzle velocity around 1,500 to 1,800 m/s (about Mach 4.5 to 5.5). Very flat trajectory. Loses only tens of meters per second per kilometer.
- **Vacuum flight:** fins useless. Sabot discard yaw persists uncorrected. Needs spin or active control to arrive nose-first on long flights.
- **Effectiveness:** the most effective kinetic anti-armor projectile in service. Penetration depends mainly on rod length, density and velocity. Depleted uranium self-sharpens through adiabatic shear. Tungsten tends to mushroom.

#### HEAT-FS (Fin-Stabilized High Explosive Anti-Tank)
- **Shape:** shaped charge warhead with a standoff probe and a fin assembly.
- **Stabilization:** fins (avoids spin degradation of the jet).
- **Atmospheric flight:** lower velocity than kinetic rounds. Arcing trajectory.
- **Vacuum flight:** fins useless. Velocity does not matter for its effect, so it remains effective if orientation holds.
- **Effectiveness:** penetration does not depend on impact velocity. Works from low-velocity launchers. Defeated by spaced armor, slat armor and reactive armor.

#### Rocket-Propelled Grenade (RPG)
- **Shape:** HEAT warhead on a rocket body with pop-out fins.
- **Stabilization:** fins plus slow spin.
- **Atmospheric flight:** strongly affected by crosswind. Under thrust it turns into the wind.
- **Vacuum flight:** fins useless. Spin and launch quality determine accuracy.
- **Effectiveness:** cheap infantry anti-armor. Short accurate range.

#### Railgun Hypervelocity Projectile
- **Shape:** slender dart with control fins or flare. Carried in a sabot and armature.
- **Stabilization:** fins, sometimes with guidance.
- **Atmospheric flight:** muzzle velocity above Mach 6. Severe heating. Long range with high impact velocity.
- **Vacuum flight:** ideal environment for velocity retention. Requires spin or active control for orientation.
- **Effectiveness:** enormous kinetic energy. Barrel and rail wear remain the main engineering limits.

#### Explosively Formed Penetrator (EFP)
- **Shape:** a metal plate driven by explosive into a slug or short rod. Some designs form fins or a flare during formation.
- **Stabilization:** flare or formed fins. Some tumble.
- **Atmospheric flight:** about 2,000 m/s. Effective at long standoff distances (hundreds of charge diameters).
- **Vacuum flight:** retains velocity. Orientation set by formation quality.
- **Effectiveness:** less penetration than a shaped charge jet. Works at much longer distance. Used in top-attack submunitions and roadside weapons.

#### Kinetic Bombardment Rod ("Rods from God")
- **Shape:** large dense metal rod. Typically proposed with fins or flare for the atmospheric phase.
- **Stabilization:** active control in space. Aerodynamic in the atmosphere.
- **Atmospheric flight:** enters at very high velocity. Heavy ablation. Drag reduces impact speed well below orbital speed.
- **Vacuum flight:** orbital. Needs attitude control before entry.
- **Effectiveness:** concept only. Impact energy comparable to a large conventional bomb. Very high launch cost per kilogram makes it impractical compared to conventional munitions.

### 5.6 Lifting and Spinning Planforms

#### Ring Airfoil Projectile
- **Shape:** hollow ring with an airfoil cross-section.
- **Stabilization:** spin plus lift.
- **Atmospheric flight:** lift counters gravity. Very flat trajectory. Low drag for its size.
- **Vacuum flight:** no lift. Ordinary spinning ring on a parabola.
- **Effectiveness:** used for less-lethal riot control rounds. Accurate at moderate range.

#### Disc, Chakram and Throwing Plate
- **Shape:** flat disc or ring.
- **Stabilization:** spin.
- **Atmospheric flight:** generates lift. Curves in the direction of spin as it slows.
- **Vacuum flight:** no lift. Holds its spin axis. Follows a plain parabola.
- **Effectiveness:** limited. Cutting damage at short range.

#### Boomerang
- **Shape:** angled wing with airfoil sections.
- **Stabilization:** spin.
- **Atmospheric flight:** uneven lift on advancing and retreating wings causes gyroscopic precession that turns the flight path into a loop.
- **Vacuum flight:** no lift. Does not return. Flies straight on a parabola.
- **Effectiveness:** hunting tool. Non-returning throwing sticks are more lethal than returning boomerangs.

### 5.7 Self-Propelled Projectiles

#### Unguided Rocket
- **Shape:** cylindrical body with fins, stick or canted nozzles.
- **Stabilization:** fins, spin or both. Congreve rockets used a long guide stick.
- **Atmospheric flight:** thrust misalignment and crosswind turning cause wide dispersion. Accuracy improves with spin and longer launch rails.
- **Vacuum flight:** fins useless. Thrust misalignment errors grow uncorrected. Spin stabilization is standard for unguided rockets and upper stages in space.
- **Effectiveness:** large volume of fire. Area saturation (Katyusha and similar). Poor individual accuracy.

#### Gyrojet
- **Shape:** small rocket bullet with angled nozzles for spin.
- **Stabilization:** spin.
- **Atmospheric flight:** low muzzle velocity. Accelerates downrange. Poor accuracy from thrust variation.
- **Vacuum flight:** recoilless launch is attractive. Spin holds orientation.
- **Effectiveness:** commercial failure. Weak at close range. Interesting concept for low-gravity or vacuum use.

#### Guided Missile
- **Shape:** body with control surfaces or thrust vectoring.
- **Stabilization:** active.
- **Atmospheric flight:** can maneuver to hit moving targets.
- **Vacuum flight:** requires thrust vectoring, side thrusters or divert motors. Aerodynamic surfaces useless.
- **Effectiveness:** highest hit probability. Highest cost per shot.

### 5.8 Space and Hypervelocity Concepts

#### Hypervelocity Pellet or Sphere
- **Shape:** sphere or compact slug.
- **Stabilization:** none needed.
- **Vacuum flight:** ideal. Orientation never matters.
- **Effectiveness:** at orbital closing speeds even small pellets destroy spacecraft. Simple and cheap per shot.

#### Pellet Cloud (Orbital Shotgun)
- **Shape:** many small pellets released together.
- **Vacuum flight:** cloud expands at a constant rate. Density falls with the square of distance.
- **Effectiveness:** high hit probability against large targets at short to moderate range. Creates long-lasting debris.

#### Whipple Shield Interaction
A thin sacrificial plate placed ahead of the main hull. A hypervelocity projectile shatters or vaporizes on contact with the bumper. The resulting cloud spreads over a wide area before striking the main wall. Long rods and pellet clouds respond differently: rods may pass several bumpers while staying partly intact, while pellets are largely neutralized.

---

## 6. The Hypersonic Needle

### 6.1 In Atmosphere

A hypersonic needle can be stabilized. Tank APFSDS rounds are essentially hypersonic needles. They are tungsten or depleted uranium rods that leave the muzzle at roughly 1,500 to 1,800 m/s (about Mach 4.5 to 5.5) and stay stable in flight. Naval railgun test projectiles exceeded Mach 6 using the same basic approach.

**Stabilization methods:**
- **Fins:** tail fins put the center of pressure behind the center of mass. The needle then weathervanes into the airflow and self-corrects any yaw. This is the standard solution for long rods.
- **Flare:** a conical skirt at the tail does the same job without fins. It handles heat better and stays effective at very high Mach numbers where thin fins start losing authority.
- **Spin:** spin works poorly on its own. The spin rate needed for gyroscopic stability climbs steeply with length-to-diameter ratio, so a true needle would need an impractical spin rate. Many fin-stabilized rounds use slightly canted fins to add a slow roll. The roll averages out manufacturing asymmetries instead of providing the main stability.

**Hypersonic complications:**
- Aerodynamic heating ablates the tip and fin leading edges. This shifts the balance point and increases drag over long flights.
- Sabot separation at launch kicks the rod with initial yaw that the fins must damp out.
- Long thin rods flex and vibrate in flight. That bending couples with yaw oscillation.
- Dense air bleeds speed quickly from a light needle. Heavy materials like tungsten or depleted uranium stretch the hypersonic window. In thin upper atmosphere or vacuum, aerodynamic stabilization stops mattering because there is little or no air to destabilize the needle.

### 6.2 In Vacuum With Normal Gravity

Stability is assured mostly by launching cleanly, because nothing acts on the needle to change its orientation after it leaves the barrel. Gravity pulls on the center of mass and produces no torque, so the needle keeps whatever orientation and rotation it had at launch for the whole flight.

**What happens without air:**
- **Any launch wobble lasts forever.** There is no damping, so a small rotation at launch becomes a permanent tumble or coning motion.
- **The needle does not nose over.** It keeps pointing in the launch direction while gravity bends the trajectory downward. The angle between the needle and its direction of travel grows over time.
- **That angle stays small on flat fast shots.** At 1,600 m/s over 2 km, flight time is about 1.25 s and gravity adds about 12 m/s of downward velocity. The needle ends up only about 0.4 degrees off its path. Lofted long-range shots end up far more misaligned.

**How to keep it stable:**
1. **Clean launch:** a precise bore, a symmetric sabot release and a rigid rod reduce the initial angular rate to near zero.
2. **Spin:** gives gyroscopic stiffness against small launch asymmetries. Any wobble becomes a fixed bounded coning instead of a tumble. Modest spin is enough in vacuum.
3. **Rigidity over long flights:** a flexing spinning needle drifts toward end-over-end rotation (the Explorer 1 failure mode). Irrelevant over seconds. Critical over hours or days.
4. **Pre-aiming the angle:** the launch orientation can be offset so the needle meets the target nose-first.
5. **Active attitude control:** cold-gas jets or an internal reaction wheel. The only way to make the needle actually track its curving path.

Gravity gradient adds a tiny torque that tends to align a long object vertically. It only matters at orbital scales and flight times.

---

## 7. Penetration and Terminal Effects

Shape-driven penetration physics (sectional density, nose shape, yaw) sits with the shape catalog above. Wound channels, stopping power and small-arms / artillery terminal tables: `../../../Combat/Firearms.md` (Terminal Effects from ProjectileShapes). Propellant and barrel pressure: `GunpowderFirearms.md`.

Short rules of thumb for invent:

- Longer, denser rods (high L/D, high density) penetrate armor better at equal velocity.
- Blunt noses dump energy early; sharp noses and long rods keep going.
- Yaw and tumbling multiply wound volume for soft targets after the projectile turns sideways.
- In vacuum there is no aerodynamic yaw; orientation is set by spin, tip-off or thrusters.

---

## 8. Comparison Tables

### 8.1 Shape Performance by Environment

| Shape | Stabilization | Air Range | Air Accuracy | Vacuum Suitability | Orientation Needed at Impact |
|---|---|---|---|---|---|
| Sphere | None | Very short | Poor | Excellent | No |
| Fragment | None | Very short | Not applicable | Good (debris) | No |
| Round nose | Spin | Short to medium | Good | Good | Low |
| Wadcutter / flat nose | Spin | Short | Good at short range | Good | Low |
| Minié ball | Spin | Medium | Good | Good | Low |
| Spitzer | Spin | Long | Very good | Good | Moderate |
| Spitzer boat-tail | Spin | Very long | Excellent | Good | Moderate |
| VLD | Spin | Very long | Excellent | Good | Moderate |
| Shotgun slug (Foster/Brenneke) | Drag | Short | Fair | Poor without spin | Moderate |
| Artillery HE shell | Spin | Very long | Fair (area) | Good | Fuze dependent |
| APDS | Spin | Long | Very good | Very good | High |
| APFSDS long rod | Fins | Long | Excellent | Fair (needs spin or control) | Very high |
| Arrow / bolt | Fins | Short | Fair | Poor | High |
| Flechette | Fins | Medium | Good | Fair | High |
| Mortar bomb | Fins | Medium | Fair (area) | Fair | Fuze dependent |
| HEAT-FS | Fins | Medium | Good | Fair | Very high |
| EFP | Flare / formed fins | Medium standoff | Good | Good | Moderate |
| Ring airfoil | Spin + lift | Medium | Good | Fair | Low |
| Unguided rocket | Fins / spin | Long | Poor | Fair with spin | Varies |
| Guided missile | Active | Very long | Excellent | Excellent with thrusters | Controlled |

### 8.2 Weapon Effectiveness Ratings (1 to 5)

| Projectile | Range (Air) | Armor Penetration | Soft Target Effect | Vacuum Effectiveness | Cost / Simplicity |
|---|---|---|---|---|---|
| Musket ball | 1 | 1 | 3 | 4 | 5 |
| Canister / grapeshot | 1 | 1 | 5 (close) | 3 | 5 |
| Shrapnel shell | 3 | 1 | 4 (open ground) | 3 | 3 |
| Spitzer FMJ | 4 | 2 | 3 | 4 | 5 |
| Expanding bullet | 3 | 1 | 5 | 4 | 4 |
| AP bullet | 4 | 3 | 2 | 4 | 4 |
| HE artillery shell | 5 | 2 | 5 | 3 | 3 |
| APCBC | 4 | 3 | 1 | 4 | 3 |
| APCR / HVAP | 2 | 3 | 1 | 4 | 2 |
| APDS | 4 | 4 | 1 | 5 | 2 |
| APFSDS | 5 | 5 | 1 | 4 (with spin) | 2 |
| HESH | 3 | 3 | 3 | 3 | 3 |
| HEAT-FS | 3 | 4 | 2 | 4 | 3 |
| Flechette (single) | 3 | 3 | 3 | 3 | 4 |
| Flechette (beehive) | 2 | 1 | 5 (close) | 3 | 3 |
| Mortar bomb | 3 | 1 | 4 | 2 | 4 |
| Arrow | 1 | 2 | 3 | 2 | 5 |
| EFP | 2 (standoff) | 4 | 2 | 4 | 3 |
| Railgun projectile | 5 | 5 | 2 | 5 | 1 |
| Hypervelocity pellet (space) | Not applicable | 5 (vs spacecraft) | Not applicable | 5 | 4 |
| Guided missile | 5 | 5 | 5 | 5 | 1 |

### 8.3 What Changes Between Atmosphere and Vacuum

| Factor | Atmosphere | Vacuum |
|---|---|---|
| Best general shape | Long pointed boat-tail or finned rod | Sphere or spin-stabilized compact slug |
| Range limit | Drag | Accuracy, target motion, planetary curvature |
| Stabilization | Spin, fins, flares | Clean launch, spin, active control |
| Fins | Essential for long rods | Dead weight |
| Launch wobble | Damped out by fins | Permanent |
| Nose follows trajectory | Yes | No |
| Velocity retention | Depends on ballistic coefficient | Total |
| Heating | In-flight aerodynamic heating | Launcher heating only |
| Misses | Fall to the ground | Continue indefinitely or orbit |
| Wind | Major error source | None |
| Transonic instability | Major issue | None |

---

## 9. Key Takeaways

1. **In air, the CM and CP relationship decides stability.** CP behind CM means self-correcting. CP ahead of CM means spin is mandatory.
2. **Spin works up to about 5 to 7 calibers long.** Anything longer needs fins or flares.
3. **Fins and flares only work with air.** In vacuum they add nothing but mass.
4. **In vacuum, launch quality is everything.** Uniform gravity cannot rotate a projectile. Whatever rotation it leaves the barrel with, it keeps.
5. **In vacuum, projectiles do not nose over.** Flat fast shots stay aligned. Lofted shots arrive sideways.
6. **In vacuum, spheres become excellent.** They lose nothing to drag and never need orientation.
7. **Long rods dominate armor penetration in air.** In vacuum they still penetrate best per shot but require spin or active control to arrive nose-first.
8. **Above about 2 to 3 km/s, length and density beat strength and nose shape.**
9. **Chemical energy warheads (HEAT, HESH) do not depend on velocity.** They suit slow launchers and remain effective in vacuum if orientation holds.
10. **Space combat range is limited by accuracy and time of flight, not by the projectile.** Every miss becomes permanent debris.
