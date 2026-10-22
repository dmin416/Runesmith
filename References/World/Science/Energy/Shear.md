# Shear

> **Design loot / Earth physics.** Force applied along a surface instead of into it. Cutting, splitting, mixing, emulsifying, lubricating, landslides and the fluids that change behavior when sheared. Not automatic law.
>
> Cast law: `../../../Runes/Energy.md`, `ManaCast.md`. Mana Hands pricing, hardness and the braking rule: `ManaHandPhysics.md`. Interface friction: `FrictionNotes.md`. Damping stack and shear-thickening stop: `Kinetic.md`. Quickground: `Sound.md`. Ink: `../Invent/Ink.md`. Wood grain: `../Biomaterials/StructuralTimber.md`. Pumping and drying: `EnergyPumping.md`. Spin: `Spin.md`. Pressure drives: `Gradients.md`.

## Shared cost law

- **1 MP = 10 J.** Raw MP below is J ÷ 10. Real casters divide by their conversion (`ManaHandPhysics.md` §2).
- **Stopping costs the same as starting.** Damping a sliding layer pays the full energy removed (`ManaHandPhysics.md` §10). A viscous brake is not a refund.
- **Two sides.** Shear needs two opposed pushes (blade and anvil, two plates or one plate and an anchor). A Hand that shears must be held rigid. Rigidity costs focus and Will on top of the joules (`ManaHandPhysics.md` §8).

## What shear is

```
Shear stress    τ = F ÷ A               (force parallel to the area)
Solid work      W ≈ F × slip to failure
Fluid           τ = μ × shear rate       (μ viscosity, rate = speed difference ÷ gap)
Fluid power     P = μ × rate² × volume   (laminar)
Soil            τ_max = c + σ' × tan φ   (Mohr-Coulomb)
```

Friction is shear at an interface. The Heat spell is shear heating on a tiny patch. Lubrication is a weak shear layer slipped between two strong ones.

## Shear strength ladder

| Material | Shear strength | Note |
|---|---|---|
| Water, air | 0 | Flows under any shear |
| Soft clay | 10 to 50 kPa | Spade cuts it |
| Stiff clay | 100 to 200 kPa | Pick and mattock |
| Wood along the grain | about 6 to 15 MPa (oak 12 to 15) | Why wood splits along its length |
| Wood across the grain | several times higher | Why chopping across is hard |
| Cortical bone | about 50 to 70 MPa | |
| Mild steel | about 200 to 250 MPa | About 0.6 × tensile strength |
| Hardened tool steel | 600 MPa and up | |

## Cutting by shear

Shear failure needs a slip of about a quarter of the thickness. The force is large. The work is small.

| Target | Shear area | Force | Work | Raw MP |
|---|---|---|---|---|
| 6 mm steel pin | 28 mm² | 8.5 kN | about 13 J | 1.3 |
| M10 mild steel bolt | 79 mm² | 20 kN | about 50 J | 5 |
| Iron chain link, 8 mm (two sides) | 100 mm² | 20 kN | about 40 J | 4 |
| Sword blade, 4 × 40 mm section | 160 mm² | 64 kN | about 64 J | 6.4 |
| Oak board along the grain, 2 × 10 cm | 20 cm² | 26 kN | about 130 J | 13 |
| 1 mm steel sheet, scissor cut | Progressive | 250 N per mm engaged | about 75 J per meter | 7.5 per m |

- **Scissor principle.** Cut progressively along a line. Only a short length engages at once so the force stays small. Total work is the same.
- **The joule bill is cheap. The rigidity is not.** A Hand pair that shears a bolt must hold 20 kN without yielding. That is a focus and Will gate, not a mana gate.
- **Reaction.** The cut piece has to be held. Shear against an anchor (a wall, the ground, the target's own mass) or with a second Hand.

## Fluids

| Fluid | Viscosity |
|---|---|
| Air | 0.000018 Pa·s |
| Water | 0.001 Pa·s |
| Olive oil | about 0.08 Pa·s |
| Honey | about 10 Pa·s |
| Pitch | about 10⁸ Pa·s |

Stirring 1 L of honey at a shear rate of 10 per second is about 1 W. At 100 per second it is about 100 W. Water is cheap to shear but goes turbulent fast. Turbulent mixing costs more than the laminar formula says.

### Emulsions

Droplets break when shear stress beats surface tension pulling them round: `τ ≈ σ ÷ r`. Halving droplet size doubles the needed stress.

| Product | What shear does |
|---|---|
| Mayonnaise and dressings | Breaks oil into fine droplets that stay suspended |
| Homogenized milk | Shrinks fat globules so cream does not rise |
| Butter | Shear breaks fat globule skins until fat clumps and buttermilk separates |
| Whipped cream | Shear plus trapped air |
| Paint and ink | Grinds pigment clumps and spreads them (`../Invent/Ink.md`) |
| Potion and salve bases | Stable oil and water blends |

Shear from a Hand works on every one of these at a few watts. Precision is the gate: a steady rate across the whole bowl beats a fast swirl in one spot.

### Fluids that change when sheared

| Type | Behavior | Examples | Use |
|---|---|---|---|
| Shear thinning | Runs easier when stirred or pushed | Ketchup, paint, blood, wet clay | Paint that holds on a wall then brushes smooth |
| Thixotropic | Thins with time under shear then sets again at rest | Drilling mud, some clays, quicksand | Quicksand releases a slow pull and grips a fast one |
| Shear thickening | Hardens under fast shear | Cornstarch in water, silica shear-thickening fluid | Soft armor layer, final damping stop (`Kinetic.md`) |
| Bingham | Will not flow until a threshold | Toothpaste, mortar | Mortar that stays where trowelled |

## Soil, snow and granular shear

`τ_max = c + σ' × tan φ`. Sand has φ about 30 to 35° and almost no c. Clay has c and a low φ. Water pressure in the pores lowers σ' and the strength with it (Quickground in `Sound.md`).

- **Landslides.** A slope fails along one shear surface. Drain the water and the slope gains strength. Add water or vibration and it loses strength.
- **Avalanches.** A snow slab rests on a weak layer. A small shear trigger releases the whole slab. This is release of stored energy (`ManaHandPhysics.md` §11 priority 1).
- **Digging.** Cut a block on its sides first (shear) then lift it. Cheaper than prying loose soil.

## Interfaces

- **Peel versus shear.** Glue and tape are strong in shear and weak in peel. Peel concentrates all the load at the edge. A Hand that lifts an edge removes a patch, seal or bandage with a tiny force.
- **Skin friction drag.** Most of a slow boat's drag is shear in the water layer at the hull. A thin air or mana film lowers it (air lubrication on Earth ships). Same idea as the Sprint Coat in `../../../Ideas.md`.
- **Lubrication.** Put the slip where you want it. Graphite, oil or a mana film. Details: `FrictionNotes.md`.

## Potential

- **Shear Plane.** Two rigid opposed plates slide past each other. Cuts bolts, pins, chain, lock shackles and buckles for single-digit raw MP. Gate is rigidity.
- **Cleave.** Split wood, slate and mica along their weak planes. Kindling and shingles for almost nothing.
- **Tailor's Edge.** Scissor-cut cloth and leather along a held line. Clean patterns for clothing and leatherwork.
- **Kitchen shear.** Mayonnaise, butter, whipped cream, homogenized milk and smooth sauces without a whisk.
- **Ink and paint mill.** Even pigment grind for scrolls and runes. Ties to `../Invent/Ink.md`.
- **Slope work.** Trench walls, terraces, a landslide started or stopped on purpose.
- **Avalanche trigger.** One small cut on a loaded slope. Dangerous to everyone below.
- **Peel.** Quick removal of seals, patches and stuck dressings.
- **Viscous damper.** A sheared fluid layer stretches out a stop. Still pays full energy. Spreads the force over time.

## Open

- Whether Hand rigidity has a numeric cap in kN for Roland's stretch.
- Whether a Shear Plane counts as Mana Hands or needs a spell form.
