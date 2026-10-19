# Tentacle Motion Modes

> Earth invent loot. Serpentine programming for a four-arm harness rig. Four-arm walking is the default. Not Caldris law. Rigid-link arm design: `RigidLinkTentacleArm.md`. Ride smoothness / contact math: `WalkerRideSmoothness.md`. Legged machines: `LeggedVehicles.md`. Walking house / rune legs: `WalkingHouse.md`. Suspension / hub leveling: `Suspension.md`. Goals wishlist: `../../../People/Roland/Goals.md`. Nav: `Index.md`.

---

Serpentine programming for a four-arm harness rig. Four-arm walking is the default. Every other mode runs automatically when the terrain or the fight calls for it.

## Control Basis

- **Central pattern generators (CPGs):** Small looping programs that output rhythmic waves on their own, the same way a spinal cord runs walking rhythm without conscious thought. Real snake robots use them. The pilot picks the mode. The arms handle the timing.
- **Stability rule:** With four arms, three anchored and one moving keeps the rig statically stable. Any mode that ties up two arms leaves only two for support, so it runs only when the rig is otherwise anchored or braced.
- **Transitions:** Switch one arm at a time. Run both controllers during a change and blend between them over about a second instead of snapping.

## Modes

### Four-Arm Walk (Default)
- Arms act as legs in a crawl gait. One lifts while three stay planted.
- Fastest mode on open ground.
- The pilot hangs at the hub, so ride smoothness comes from active hub leveling, not from the arms.

### Wrap Grip (Capstan)
- The arm coils around a pipe, beam, pole or railing.
- Holding force = load × e^(μθ), where μ is friction and θ is wrap angle in radians.
- At μ = 0.5:
  - Half wrap holds about 4.8 times the load.
  - One wrap holds about 23 times the load.
  - Two wraps hold about 535 times the load.
- Works on anything that can be encircled. The wall or surface does not need to be solid enough for a claw.

### Helical Pole Climb
- The arm forms a helix around a pole or tree and rolls, so the helix travels up the pole. Carnegie Mellon snake robots climb this way.
- Two arms climb alternately. Each one anchors fully before the other releases.

### Concertina (Shafts and Ducts)
- The arm bunches into S-curves that press against opposite walls. The front extends while the rear holds, then the rear pulls up while the front holds.
- Works in elevator shafts, chimneys, ducts and narrow alleys between buildings.

### Lateral Undulation (Rubble)
- Waves along the arm push against rocks and debris. More obstacles means more push points, so rough ground helps.
- Used for crossing collapsed structures with arms laid out low.

### Sidewinding (Loose Surfaces)
- Sections lift and set down sideways with almost no sliding.
- Used on sand, gravel and loose debris where pushing would just dig in.

### Gap Bridge
- Two arms twist together and lock rigid. Twisted and locked, the pair resists bending several times better than either arm alone.
- The pair cantilevers across, anchors on the far side and becomes a bridge or rope for the rig to cross.

### Coil Strike
- The arm pulls into an S-curve, storing energy, then releases it all at once.
- Gives very fast jabs and grabs. Target tracking runs automatically.

### Constrictor Pin
- The arm coils around an opponent's limbs or torso.
- Tightens a step every time the target shifts and never loosens. There is no single point to pull free from.

## Mode Selection

| Situation | Mode |
|---|---|
| Open ground | Four-arm walk |
| Pipe, pole, beam or railing | Wrap grip or helical climb |
| Shaft, chimney or duct | Concertina |
| Rubble | Lateral undulation |
| Sand or gravel | Sidewinding |
| Gap between buildings | Gap bridge |
| Attack | Coil strike |
| Restrain | Constrictor pin |

## Limits

- Ride smoothness depends on hub leveling, not slithering, because the pilot hangs above the arms instead of lying on the ground.
- Serpentine modes are slower than the four-arm walk on open ground.
- Four arms is tight. Six would allow three to anchor or walk while three fight, without ever breaking the stable tripod.
