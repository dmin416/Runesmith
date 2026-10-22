# Perfect Glider: Premise and Model

Hub: [PerfectGlider.md](PerfectGlider.md).

## What the material changes

| Normal limit | With the cast material |
|---|---|
| Wing thickness set by spar depth | Thickness chosen for airflow only. Best is about 12% at the root and 9% at the tip. Much thinner sections stall abruptly and lose lift |
| Skin thickness set by strength | As thin as desired. No buckling, no denting |
| Long thin wings droop and twist | None. Any aspect ratio holds its exact shape |
| Flutter at speed | None |
| Airframe weight | Effectively zero |
| Tail boom diameter | A rod the width of a pencil |
| Trailing edges | Razor-sharp, which trims a little drag |
| Pod size | Set only by the human bodies inside |
| Folding wings | Cast parts cannot fold. Wings collapse as nested sleeves instead ([Joints](Joints.md)) |

## What the material does not change

- **Induced drag.** Span is still the main lever on glide ratio.
- **Airfoil shape.** The wing stays a hollow airfoil. A zero-thickness curved plate performs worse at these speeds. Only the walls get thinner.
- **Joints.** Each cast part is perfectly stiff. A wing of 20 to 60 sliding sleeves is an assembly. Its fits, locks, seals and steps set the real stiffness and part of the real drag.
- **Everything not cast.** People, harness straps, control cables, seals, transparent canopy panels (if the material is opaque), engines, motors, batteries, solar cells, fuel, water ballast, instruments and oxygen all keep their normal mass and bulk. Propellers, drive shafts, gears and pedal cranks can be cast and weigh effectively nothing.

## The span law

**L/D max ≈ (b / 2) · √(π · e / f)**

- **b** = wingspan
- **e** = span efficiency
- **f** = total drag area of everything not tied to lift (pod, pilot, tail, wing skin friction), in m²

Doubling span roughly doubles glide ratio. Thin material cannot beat this. It only shrinks **f**.

## Model assumptions

- Sea-level air unless noted
- Airfoil drag scaled by Reynolds number: c_d ≈ 0.0052 · (Re / 10⁶)^-0.5 with a floor of 0.0040, plus a lift-dependent term. This is calibrated to good laminar sections and costs low-speed, small-chord wings more than the earlier model did
- Tail surface drag included (it was missing in earlier versions)
- Lift coefficient limit 1.5 clean, 2.0 with flaps
- Propeller efficiency 85%. Small engines 25% efficient
- Airframe mass zero

Two cases are given wherever it matters:

| Case | Span efficiency | Wing profile drag | Other drag | Meaning |
|---|---|---|---|---|
| **Ideal** | 0.99 | As modeled | As modeled | Perfectly sealed joints with micron-scale steps |
| **Real** | 0.97 | +10% | +10% | Joints with 0.1 to 0.3 mm steps and clearances, a few turbulent wedges, imperfect sealing |

Rain and insects cost a further 20 to 40% on top of either case.

**Use the Real numbers.** They are the working model for every plan, route and story beat. Ideal numbers are a ceiling that only a perfectly built, perfectly maintained wing approaches. Planning tables (Hawaii, cross-country, power) use the Real case only.
