# Perfect Glider: Design A "Tandem"

Hub: [PerfectGlider.md](PerfectGlider.md).

Two people lying prone in tandem inside a laminar pod.

| Spec | Value |
|---|---|
| Wingspan | 31 m |
| Root chord / tip chord | 0.39 m / 0.31 m |
| Wing area | 10.8 m² |
| Aspect ratio | 89 |
| Thickness | 12% root, 9% tip |
| Pod drag area | 0.030 m² (best-case laminar pod) |
| Tail drag area | 0.009 m² |
| Crew load (two people plus gear) | ~200 kg |
| Max load with water ballast | 900 kg |

The span grew from 25 m to 31 m. Once tail drag and Reynolds-number effects are counted, 25 m gives a glide ratio of 67, not 78. Holding the target of 77 takes 31 m.

## Span options at 500 kg

| Span | Glide ratio, Ideal | Glide ratio, Real | Best-glide speed |
|---|---|---|---|
| 20 m | 57 | 54 | 100 km/h |
| 25 m | 67 | 63 | 91 km/h |
| 28 m | 72 | 68 | 86 km/h |
| **31 m** | **77** | **72** | **83 km/h** |
| 35 m | 82 | 76 | 80 km/h |
| 40 m | 86 | 80 | 80 km/h |

## Performance by load

| Total mass | Glide ratio, Ideal | Glide ratio, Real | Best-glide speed | Min sink (Ideal / Real) | Stall clean | Stall with flaps |
|---|---|---|---|---|---|---|
| 200 kg (crew only) | 69 | 65 | 52 km/h | 0.20 / 0.22 m/s | 51 km/h | 44 km/h |
| 350 kg | 74 | 69 | 69 km/h | 0.25 / 0.27 m/s | 67 km/h | 58 km/h |
| **500 kg** | **77** | **72** | **83 km/h** | **0.29 / 0.31 m/s** | **80 km/h** | **69 km/h** |
| 700 kg | 80 | 74 | 99 km/h | 0.33 / 0.36 m/s | 95 km/h | 82 km/h |
| 900 kg | 82 | 76 | 113 km/h | 0.37 / 0.39 m/s | 107 km/h | 93 km/h |

## Glide ratio at speed (Real)

| Total mass | At 108 km/h | At 144 km/h | At 198 km/h |
|---|---|---|---|
| 200 kg | 28 | 17 | 10 |
| 500 kg | 62 | 42 | 25 |
| 900 kg | 76 | 67 | 44 |

Fly light (200 kg) for slow launches and landings. Load water ballast for speed and wind penetration. Dump it before landing.

## Pod drag sensitivity

The 0.030 m² pod is a best case: two prone adults in a long laminar body with no canopy bulge. A pod of ordinary sailplane quality (~0.046 m²) drops the Real glide ratio from 65 / 72 / 76 to **60 / 66 / 70** at 200 / 500 / 900 kg. A large share of Design A's performance lives in the pod.

## Reynolds numbers

| Station | At 500 kg (83 km/h) | At 200 kg (52 km/h) |
|---|---|---|
| Root (0.39 m) | 616,000 | 385,000 |
| Tip (0.31 m) | 490,000 | 307,000 |

These sit in the normal range for outer sailplane wing panels. Flown light, the tips run at low Reynolds numbers where drag climbs. The drag model already charges for this.

## Circling sink in thermals (Real)

| Mass | 30° bank | 45° bank |
|---|---|---|
| 200 kg | 0.27 m/s | 0.37 m/s |
| 500 kg | 0.39 m/s | 0.52 m/s |
| 900 kg | 0.49 m/s | 0.66 m/s |

## Packing

| Part | Method | Packed size |
|---|---|---|
| Wing | ~29 prismatic 0.6 m sleeves per side | 0.39 × 0.09 × 0.6 m (~22 L) |
| Wing, 0.3 m sleeves | ~62 per side. Clearance must stay under 0.15 mm | 0.39 × 0.09 × 0.3 m (~11 L) |
| Tail surfaces | Telescoping stacks | Fit inside the hollow innermost wing sleeves |
| Tandem pod (~4.5 m long) | ~10 nested rings | ~100 to 125 L |
| **Whole glider** | | **~130 to 150 L, one very large duffel** |

The pod sets the packed size. Water ballast goes in bladders in the pod by default (see [GustsHandling](GustsHandling.md) for wing ballast).
