# Perfect Glider: Design C "Pocket Wing"

Hub: [PerfectGlider.md](PerfectGlider.md).

One person, 100 kg total. A 25 m wing of nested telescoping sleeves. It lands on foot and is light enough on power for a person to fly it by pedaling.

| Spec | Value |
|---|---|
| Wingspan | 25 m |
| Wing area | 16 m² (sized for foot launch and landing) |
| Root chord / tip chord | 0.74 m / 0.54 m |
| Aspect ratio | 39 |
| Thickness | 12% root, 9% tip |
| Total mass | 100 kg (pilot and gear) |

## Performance

| Config | Drag area (with tail) | Glide ratio, Ideal | Glide ratio, Real | Best-glide speed | Min sink (Real) | Stall clean | Stall with flaps |
|---|---|---|---|---|---|---|---|
| Exposed pilot, prone harness | 0.14 m² | 41 | 39 | 32 km/h | 0.21 m/s | 29 km/h | 25 km/h |
| **Pilot in collapsible shell** | **0.05 m²** | **52** | **49** | **35 km/h** | **0.18 m/s** | **29 km/h** | **25 km/h** |

These are lower than the earlier 47 and 62. The difference is tail drag (a 25 m slow wing needs large tail surfaces, ~2.5 m² total) and higher airfoil drag at the low Reynolds numbers this wing flies at (330,000 at the tip, 450,000 at the root).

| Speed | Exposed (Real) | Shelled (Real) |
|---|---|---|
| 36 km/h | 37 | 49 |
| 54 km/h | 24 | 35 |
| 72 km/h | 15 | 23 |

## Span options at 16 m² and 100 kg

| Span | Exposed (Ideal / Real) | Shelled (Ideal / Real) | Best-glide speed | Pedal power needed (shelled, Real) |
|---|---|---|---|---|
| 10 m (hang glider) | 19 / 18 | 25 / 24 | 50 to 57 km/h | 690 W |
| 15 m | 27 / 26 | 36 / 34 | 40 to 46 km/h | 400 W |
| 20 m | 35 / 33 | 44 / 42 | 35 to 39 km/h | 270 W |
| **25 m** | **41 / 39** | **52 / 49** | **32 to 35 km/h** | **213 W** |
| 30 m | 47 / 44 | 58 / 55 | 30 to 33 km/h | 182 W |
| 40 m | 53 / 49 | 67 / 62 | 29 to 30 km/h | 157 W |

Past ~30 m the craft flies so slowly that moderate wind stops all forward progress. 25 m is the best balance of glide, speed, packed size and pedal power.

## Circling sink in thermals (Real)

| Config | 30° bank | 45° bank |
|---|---|---|
| Exposed | 0.26 m/s | 0.36 m/s |
| Shelled | 0.22 m/s | 0.30 m/s |

Even weak 0.5 m/s thermals give a climb. Roll rate limits how tightly it can work them ([GustsHandling](GustsHandling.md)).

## Packing

| Part | Method | Packed size |
|---|---|---|
| Wing | ~50 prismatic 0.3 m sleeves per side | 0.74 × 0.18 × 0.3 m (~40 L) |
| Wing, 0.6 m sleeves | ~23 per side | 0.74 × 0.18 × 0.6 m (~80 L) |
| Tail (~2.5 m² total) | Telescoping stacks | Mostly inside the innermost wing sleeves, ~5 L overflow |
| Harness (exposed version) | Fabric, not cast | ~5 L, ~2 kg |
| Pilot shell (shelled version) | ~8 nested rings | ~50 to 60 L |
| **Exposed rig** | | **~50 L, a large hiking pack** |
| **Shelled rig** | | **~100 to 110 L, an expedition pack** |

The earlier "slim daypack" and "thick book" sizes were wrong. They came from the dropped chordwise-split scheme. Two stacked root sections (2 × 0.089 m) set the wing's packed height. The 0.74 m root chord sets its packed width.

## Ground handling

- A 16 m² wing produces about **30 kg of lift in a 20 km/h breeze** and **70 kg at 30 km/h**. Partially deployed in wind, it will drag or lift the wearer.
- Deploy facing into the wind.
- A 25 m span needs a clear strip with no trees, walls or crowds within ~13 m on either side.
- Above ~25 km/h of wind it becomes very hard to handle on the ground. It cannot be safely deployed in 30+ km/h wind.

## Human-powered flight

| Config | Crank power for level flight | Speed |
|---|---|---|
| Shelled | ~213 W | ~29 km/h |
| Exposed | ~253 W | ~29 km/h |

- A cast propeller, crank and drive shaft weigh effectively nothing.
- **Who can do it:** A trained cyclist holds 213 to 250 W for one to several hours. A fit amateur manages the shelled version for under an hour. The exposed version needs a strong rider.
- **Range:** 30 to 115 km in still air depending on the rider.
- **Partial pedaling:** 100 W stretches the effective glide ratio from 49 to ~90 shelled and from 39 to ~65 exposed.
- **Conditions:** Human-powered flight only works in calm, smooth air: surface wind under ~10 km/h, no strong thermals, early morning or evening. Takeoff needs a smooth strip of 100+ m that is 25+ m wide. This is the regime Daedalus 88 flew in. Trade-wind Hawaii is a different sport. Calm Kona-coast mornings in the lee of Mauna Kea and Hualālai are the realistic Hawaiian window.
- **Precedent:** Daedalus 88 (31 kg aircraft, Olympic cyclist pilot) flew 115 km from Crete to Santorini in 3 hours 54 minutes on April 23, 1988.
