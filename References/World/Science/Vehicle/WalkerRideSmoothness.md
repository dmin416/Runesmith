# Walker Ride Smoothness

> Earth invent loot. Contact points, limb count, mode transitions, inverse kinematics effort by terrain. Not Caldris law. Legged machines: `LeggedVehicles.md`. Four-arm harness modes: `TentacleMotionModes.md`. Rigid-link arm design: `RigidLinkTentacleArm.md`. Walking house / rune legs: `WalkingHouse.md`. Suspension / seat isolation: `Suspension.md`. Wheels: `WheelScience.md`. Goals wishlist: `../../../People/Roland/Goals.md`. Nav: `Index.md`.

---

## Part 1: Contact Points

Smoothness depends on two things: keeping enough limbs on the ground at every moment and actively holding the seat level. Limb count sets the floor. Active control does the rest.

### The Core Math

- Three contact points form a support triangle. As long as the center of mass stays inside it, the body cannot tip. Three is the minimum for standing stable.
- To walk while staying stable, at least three must stay planted while the others move.
- With n limbs sharing weight W, lifting one shifts about W ÷ n onto the rest. That load shift is what causes bumps and sway, so more limbs means smaller jolts per step.
- People rate a ride comfortable when vibration stays below roughly 0.3 m/s² (ISO 2631 comfort scale). That is the target.

### By Limb Count

- **1 tendril:** Stepping with it means hopping, which is rough. Moving like a snake makes it one of the smoothest options on any terrain. The whole length stays in contact and acts like hundreds of contact points. The body flows over the ground while the head holds steady, so a seat on the head rides level. Snakes cover nearly every surface:
  - Lateral undulation pushes off rocks and rubble, so rough ground actually helps.
  - Sidewinding crosses loose sand.
  - Concertina movement climbs and passes through tight spaces.
  - The body can cantilever across gaps a large fraction of its own length.
  - The tradeoffs are speed and length. Snakes are slower than legged runners. The tendril needs to be several times longer than the largest obstacle.
- **2:** Constant balancing. The body sways with every step and any slip causes a fall. Active leveling makes flat ground decent. Rough terrain stays jarring.
- **4:** Lifting one limb at a time keeps three down, so a slow walk is stable. Faster gaits lift two at once and turn back into balancing.
- **6:** Tripod gait. Two alternating triangles of three, so three limbs are always planted at any speed. Insects use this. It can lose a limb and keep walking. This is the minimum for stable movement at speed.
- **8:** Two limbs can probe, climb or grip while six stay planted. Each limb carries only 1/8 of the weight, so a missed step barely registers.
- **10+:** Diminishing returns. Smoothness gains past 8 are small while weight, coordination load and tangle risk keep rising.

### For Any Terrain

For the smoothest ride, a single long snake-like tendril with the seat on the head. The body absorbs the terrain and the head stays level.

For speed with stability, eight long limbs plus an actively leveled seat. Six is the practical minimum. Eight adds spare limbs to reach across gaps, grip slopes and test unstable ground without ever breaking the stable tripod.

Limb length matters as much as count. Limbs should be at least 1.5 times the height of the largest obstacle so the body can pass over it without tilting.

The seat should sit on a gimbal or damped mount. Even a perfect gait transmits small shocks. Isolating the rider from the body is how every smooth vehicle works, regardless of whether wheels or legs are underneath.

### Combinations and Transitions

Combining modes beats any single design. Each form handles the terrain it's best at, and the body switches as the ground changes.

| Terrain | Best mode |
|---|---|
| Flat road | Limbs curl into wheels and roll |
| Firm open ground | Six to eight legs at a trot |
| Rubble and rocks | Slither, pushing off the rocks |
| Loose sand | Sidewind, or lay limbs flat side by side as a broad tread |
| Cliffs and slopes | Tail coils around an anchor while the front reaches up |
| Gaps | Limbs bundle into one stiff trunk and cantilever across |
| Water | Undulate like a swimming snake |

**Useful combinations**
- **Snake body with retractable legs:** Slithers through rubble and sand. Legs deploy for speed on firm ground or to brace on slopes.
- **Splitting and merging tendrils:** Eight tendrils walk as legs, lie flat together as a tread on soft ground and bundle into one trunk for gaps. Bending stiffness grows with the fourth power of radius, so four tendrils merged into one trunk of double radius are four times stiffer than the same four acting separately.
- **Wheel-legs:** Rolling is the most efficient mode on smooth surfaces. Legs take over when the ground breaks up.
- **Anchor and reach:** One end grips while the other extends, like an inchworm or a climber on a rope. Slow but works on near-vertical terrain.

**Keeping transitions smooth**
- Never drop below three support points or continuous body contact during a change.
- Switch one limb at a time so the load shift stays at W ÷ n per step instead of all at once.
- Run both controllers during a change and blend from one to the other over about a second, rather than snapping between them.
- The seat gimbal covers whatever small jolts remain.
- Terrain sensing picks the mode ahead of time, so the switch starts before the ground changes under the body.

For a magic floating-segment version, transitions get easier. Segments can rearrange freely with no mechanical joints, so splitting, merging, curling into wheels or stretching into a tendril becomes a change in formation rather than a change in hardware.

---

## Part 2: Inverse Kinematics

The core math is simple. The hard part is everything around it. A chair that walks forward smoothly on flat ground is a hobby project. One that does it on any terrain is a research-team problem.

### IK Itself Is Small

For one leg with a hip swivel, hip hinge and knee, the full solution is a few lines of trigonometry. Given a foot target at (x, y, z) relative to the hip, upper leg length L1 and lower leg length L2:

```
hip_yaw   = atan2(y, x)
d         = distance from hip hinge to foot
knee      = acos((L1² + L2² − d²) / (2·L1·L2))
hip_pitch = atan2(z, horizontal_reach) + acos((L1² + d² − L2²) / (2·L1·d))
```

Run that for each leg every frame and the joints land where the feet need to be. Roughly 20 to 50 lines of code per leg type.

### Why IK Naturally Gives a Smooth Ride

The controller never commands the legs directly. It commands the body: move forward at this speed, stay at this height, stay level. Planted feet stay fixed in world space, so as the body glides forward, IK recalculates every planted leg to push it along. A smooth body path automatically produces correct leg motion.

### The Layers Above IK

1. **Command:** "Forward" becomes a target speed and direction.
2. **Gait scheduler:** Decides which legs lift and when, such as the tripod gait for six legs.
3. **Foot placement:** Picks where each lifted foot lands, normally a fixed spot ahead of the hip.
4. **Swing path:** Moves the lifted foot in an arc so it clears the ground.
5. **IK:** Converts every foot position into joint angles.
6. **Joint control:** Drives each motor to its angle.

### Effort by Terrain

- **Flat ground, fixed gait:** A few hundred lines. Hobby hexapods do this on a cheap microcontroller. Saying "forward" is all the rider needs.
- **Uneven ground:** Add foot contact sensors so a leg stops when it touches down instead of at a fixed height, plus a tilt sensor that adjusts each leg's height to keep the body level. A few thousand lines and months of tuning.
- **Any terrain:** Add cameras or lidar to map the ground, foothold selection that avoids loose rock and gaps, slip detection and fall recovery. Modern machines like Spot and ANYmal solve this by training neural network controllers in simulation across millions of virtual terrains. This takes a full engineering team and years.

### Minimum Input From the Rider

Direction and speed, whatever the terrain. Everything else runs automatically underneath. The complexity lives in how well the machine senses the ground, not in what the rider has to say.
