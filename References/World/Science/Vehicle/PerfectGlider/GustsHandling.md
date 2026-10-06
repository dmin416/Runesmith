# Perfect Glider: Gusts and Handling

Hub: [PerfectGlider.md](PerfectGlider.md).

## What zero airframe mass does

- **Vertical gusts:** The flying mass is still the pilot and payload, so vertical gust response depends on wing loading as it would on any aircraft. Zero airframe mass adds nothing new here.
- **No flex:** A normal wing bends in a gust and softens the jolt slightly. A cast wing does not. Gust loads reach the occupants undiluted.
- **Roll inertia is nearly gone.** A normal sailplane wing holds hundreds of kilograms spread across the span. Here the only roll inertia is the people near the centerline. Roll rate therefore follows aerodynamic moments almost instantly (roll time constant under a millisecond for A and C). Roll onset is instant. Maximum roll rate is still slow because a long wing's roll damping is huge.
- **Net result: twitchy onset, sluggish rate.** Every gust that hits one wing more than the other rolls the craft immediately with no inertia to smooth it.

## Gust loads (sharp-edged gusts at best-glide speed, with standard gust alleviation)

| Design | Wing loading | Extra g, 5 m/s gust | Extra g, 10 m/s gust |
|---|---|---|---|
| A, 200 kg | 182 N/m² | 1.0 | 1.9 |
| A, 500 kg | 454 N/m² | 0.7 | 1.5 |
| B, exposed | 467 N/m² | 0.6 | 1.2 |
| B, shelled | 467 N/m² | 0.8 | 1.5 |
| C, exposed | 61 N/m² | 0.8 | 1.6 |
| C, shelled | 61 N/m² | 0.9 | 1.7 |

These are normal values for sailplanes and hang gliders. The structure survives anything. The occupants feel 2 to 3 g peaks in strong thermals, which is uncomfortable but routine for soaring.

## Roll authority versus gusts

Full flaperon roll rate assumes a roll-helix value (pb/2V) of 0.07, which requires the outboard flaperons to get full travel ([Joints](Joints.md)). With shaft play or binding, roll rates fall by up to a third. Gust roll is the rate induced by a 2 m/s updraft difference from one wingtip to the other, which is common at thermal edges.

| Design | Max roll rate | Gust-induced roll rate | Time to reverse 45° bank to 45° |
|---|---|---|---|
| A, 200 kg (52 km/h) | 3.7°/s | 3.7°/s | 24 s |
| A, 500 kg (83 km/h) | 6.0°/s | 3.7°/s | 15 s |
| B, exposed (95 km/h) | 60°/s | 33°/s | 1.5 s |
| B, shelled (127 km/h) | 80°/s | 33°/s | 1.1 s |
| C at 32 to 35 km/h | 2.8 to 3.1°/s | 4.6°/s | ~30 s |
| C at 54 km/h | 4.8°/s | 4.6°/s | 19 s |
| C at 72 km/h | 6.4°/s | 4.6°/s | 14 s |

- **Design C at best-glide speed cannot out-roll a moderate thermal edge.** The gust rolls it faster than full controls can roll it back. It must speed up to ~55+ km/h in turbulence, which roughly halves its glide ratio.
- **Design A flown light** is marginal in the same way. Ballast fixes it.
- **Design B** is agile. Its problems are speed and sink, not control.

## Fixes

- **Wing ballast for Design A.** Putting 300 kg of water in bladders spread along the wing raises the roll time constant to ~0.3 s, like a normal sailplane. That filters gusts. Operations below.
- **Polyhedral.** A cast dihedral angle at the root joint (each half-wing stack is straight) adds roll stability and lets the rudder help roll the craft, as on human-powered aircraft.
- **Large all-moving rudder** for yaw control against the adverse yaw of a long slow wing.
- **Fly faster in rough air.** Every design gains roll authority with speed.

## Wing ballast operations (Design A)

- **Ground procedure only.** Bladders go into the wing after it is deployed and locked. They are fed in from the root through the hollow sleeves. Filling 300 L takes a crew 15 to 30 minutes with buckets and a hand pump. Water is strained first so no grit reaches the joints.
- **Equal fill is mandatory.** Each side is metered with its own sight gauge. Any left/right difference beyond a few kilograms is a hard abort. A heavy wing drops on the takeoff run before the flaperons have enough airspeed to hold it up.
- **Dumping must be symmetric.** Both sides dump through linked valves. If one side fails to dump in flight, close the other side and land heavy, holding the heavy wing up. Never land with one side full and the other empty.
- **Freezing:** Water freezes in wave climbs or high cold air. Dump before going above the freezing level, or add antifreeze.
- **After flight:** Drain completely and pull the bladders before packing. A bladder left in a sleeve blocks nesting.
