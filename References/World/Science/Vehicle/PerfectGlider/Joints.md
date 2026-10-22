# Perfect Glider: Joints, Sleeves and Controls

Hub: [PerfectGlider.md](PerfectGlider.md).

This is the hardest engineering in all three designs. The flight numbers assume it works.

## Sleeve geometry

- **Each sleeve is prismatic.** Its cross-section is constant along its own length. A sleeve that tapered along its length could not slide through the one outside it.
- **Taper is stepped.** Each sleeve is slightly smaller than the one outside it, so the wing tapers in small steps from root to tip.
- **Nesting condition:** Each inner sleeve must be thinner than its outer sleeve by at least twice the sliding clearance everywhere around the section. Scaling each section about the flap hinge line keeps the hinge lines collinear and satisfies this.
- **Thickness taper gives the nesting room.** Going from 12% thick at the root to 9% at the tip leaves 0.6 to 0.8 mm of thickness to spare per sleeve on Designs A and C. That allows sliding clearance of up to 0.3 to 0.4 mm. A constant-thickness, constant-chord wing would leave almost none.
- **The trailing edge is the tightest fit.** Near a sharp trailing edge the section is only fractions of a millimeter thick. Each inner sleeve's trailing edge sits a few millimeters ahead of the outer sleeve's trailing edge to fit.
- **Washout is stepped.** Tip-stall protection needs about 2° of twist from root to tip. Prismatic sleeves can only twist in steps of 0.04 to 0.1° per sleeve. This eats part of the trailing-edge nesting room.
- **Overlap:** Each sleeve keeps ~5 cm inside its neighbor when deployed to carry bending loads. A 0.6 m sleeve adds 0.55 m of span.

## Clearance budget

Every item that sits between one sleeve and the next draws from the same small allowance: the thickness each sleeve loses relative to the one outside it.

| Item | Design A (0.6 m sleeves) | Design C (0.3 m sleeves) |
|---|---|---|
| **Spare thickness per sleeve** | **0.64 mm** | **0.80 mm** |
| Sliding clearance, both faces | 0.30 mm (0.15 mm each) | 0.40 mm (0.20 mm each) |
| Joint seal strips, both faces | 0.10 mm | 0.10 mm |
| Stepped washout (trailing-edge offset) | 0.12 mm | 0.13 mm |
| Flaperon hinge-gap seals | 0.10 mm | 0.10 mm |
| **Total used** | **0.62 mm** | **0.73 mm** |
| **Left over** | **0.02 mm** | **0.07 mm** |

Both budgets are essentially full. Solar cells are kept off the sleeves partly for this reason ([Powered](Powered.md)). If any single item needs more room, one of these must give:

- **Fewer, longer sleeves.** Doubling sleeve length doubles the spare thickness and doubles packed length. Design C at 0.6 m sleeves has 1.7 mm spare and packs to ~80 L of wing instead of ~40 L.
- **More taper.** A smaller tip chord frees room but loads the tips harder and worsens tip stall.
- **Tighter sliding clearance.** This makes grit jams more likely.
- **Larger steps at each joint.** This pushes drag past the Real case. A wing built that way should be planned with glide ratios a further 5 to 10% below the Real tables.

## Locking and sealing

- **Taper lock:** The last 5 cm of each sleeve is a slight cone. Pulled out, each sleeve wedges tight into the next with zero play, the way telescoping fishing rods lock. With perfectly stiff parts, a seated taper has no slop at all.
- **Bayonet twist** on top of the taper keeps vibration from working joints loose.
- **Seals:** Any open gap between sleeves lets high-pressure air under the wing leak to the low-pressure upper surface. That leak trips laminar flow and dumps lift locally. A seated taper seals by contact. A thin seal strip at each joint backs it up.
- **Grit is the field enemy.** Sand or dust larger than the sliding clearance jams a sleeve. Sleeves need cleaning before packing. A jammed sleeve means a jammed wing.

## Steps and laminar flow

- A sleeve joint is a small ridge running in the direction of the airflow, with a backward-facing step at the tip side.
- Under the premise the walls can be micron-thin and the clearance tiny, so steps are far below the size that trips laminar flow. That is the **Ideal** case.
- With real clearances of 0.1 to 0.3 mm plus misalignment, each joint can start a wedge of turbulent flow spreading downstream. That is most of the **Real** case's 10% profile drag penalty.
- Earlier versions split the chord into three panels to shrink the pack. That idea is dropped. Chordwise joints run across the airflow and trip laminar flow at the joint line. They also do not reduce packed volume, because the three panels stack taller than they get shorter.

## Controls

- **Roll and flaps:** Every sleeve carries its own flaperon segment along its trailing edge. A telescoping hex torque shaft runs along the hinge line through every sleeve, like a tractor power-takeoff shaft. When the wing deploys and locks, one shaft drives every segment. A mixer at the root combines aileron (opposite on each side) and flap (same on both sides) inputs.
- **Flaperon segments nest** with their sleeves. They must be at neutral to pack. Each segment's hinge gap needs its own seal.
- **Outboard roll authority is the weak link.** Each sliding hex joint needs a little rotational play to slide. On Design C that play adds up across ~50 joints between the root and the tip. Misalignment between segments can also make the shaft bind. Either one cuts travel on the outboard flaperons, which produce most of the rolling moment. The fix is to make each shaft joint taper-lock along with its sleeve so the play disappears when the wing is seated. If it does not, roll authority falls. The gust table in [GustsHandling](GustsHandling.md) assumes full authority (pb/2V = 0.07). At a reduced 0.05, Design C must fly ~72 km/h to match a moderate thermal edge, where its glide ratio drops to ~23 shelled and ~15 exposed.
- **Pitch and yaw:** All-moving tail surfaces on a telescoping boom. A second hex shaft inside the boom, or plain control cables, drives them. Cable stretch is tolerable here.
- **Trim:** Adjustable tail incidence through the same shaft.
- **Cockpit controls:**
  - Designs A and B: stick and rudder pedals
  - Design C: stick with a twist-grip rudder, since the feet may be pedaling the propeller
- **Weight shift does not work on Design C.** At 25 m span the wing's roll damping overwhelms anything a pilot can do by shifting body weight. Hang-glider-style control is out. It needs aerodynamic controls.

## Deployment

- Pull each half-wing out from the root like a telescoping pole, sleeve by sleeve, until each taper seats. A tip dolly or helper makes this faster.
- Deploy facing into the wind, nose down, with the wing held level. A half-deployed wing in wind generates lift unevenly and twists in the hands.
- Pack in reverse after clearing grit from each joint.
