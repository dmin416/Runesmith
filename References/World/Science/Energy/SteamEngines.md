# Steam Engines

Hub: `Engines.md`. Closed-cycle cousin: `StirlingEngines.md`. Shaft to volts: `Generators.md`, `ElectricMotors.md`. Cylinder and seal craft: `../../../Food/KitchenCraft.md`, `Pumps.md`. Line shaft: `../Invent/MechanicalPrecision.md`. Farm traction: `../../Geography/FarmingSystems.md`. Baseline: `../../Tech/Technology.md`.

A steam engine boils water, lets the vapor push a piston or a turbine, then exhausts or condenses it. The working fluid is thrown away or recycled. That open Rankine loop is the difference from a Stirling, which keeps one gas sealed inside.

## Caldris filter

| Band | What exists |
|---|---|
| Baseline | Boilers, condensers, and mana-stone rail that behaves like steam. Noisy, multi-day, passenger and freight. Gnomes built the trains. |
| Near-reach invent | Atmospheric and low-pressure beam engines, a single-cylinder mill engine, a steam pump. Needs a bored cylinder, a piston seal, and plate that holds a few atmospheres. |
| Industrial invent | High-pressure pistons, compound expansion, locomotive and traction engines, fire-tube boilers with a safety valve and a water gauge. |
| Prestige / late | Multi-stage turbines, superheat, condensers good enough for ship plants and central dynamos. Flash boilers. Not street craft. |

Personal firearms stay niche. Steam does not depend on that. Farm uses (threshers, gang plows, sawmills, gins) sit on the Earth steam-and-muscle list in `FarmingSystems.md`.

## What the heat is actually doing

Heating 1 kg of water from room temperature to boiling takes about 335 kJ. Turning that kilogram into steam at the same temperature takes about 2,260 kJ. Almost all the fuel goes into the phase change, not into making the kettle hotter.

Work comes from letting that vapor expand. Early engines barely expanded it. They filled a cylinder and then threw the rest of the heat away. Later engines cut off admission early and let the steam expand inside the cylinder. Turbines expand it across many stages. Condensing the exhaust makes a vacuum on the outlet side, so the same steam drops across a larger pressure ratio.

Carnot ceiling is `1 − T_cold / T_hot` on an absolute scale. A boiler at 200 °C (473 K) dumping heat at 30 °C (303 K) cannot beat about 36% even as a perfect engine. A plant at 500 °C against the same cold end cannot beat about 61%. Real engines sit far below those ceilings because combustion heat enters across a range of temperatures, and friction, leakage, and incomplete expansion eat the rest.

Watt's horsepower is 33,000 ft·lbf per minute, about 746 W. It was a sales comparison against a mill horse, not a property of steam.

## Real efficiencies

| Machine | Era | Thermal efficiency | What changed |
|---|---|---|---|
| Savery pump | 1698 | Very poor, often under 0.5% | No piston. Steam pressure and then a condensation vacuum lifted water in the pipe itself. |
| Newcomen atmospheric | 1712 | About 0.5% | Piston and beam. Atmosphere did the push after injected water collapsed the steam. |
| Watt, separate condenser | 1769 onward | A few percent | Cylinder stayed hot. Later double-acting, rotative, and governed. |
| High-pressure non-condensing | from about 1800 | A few percent, far more power per tonne | Trevithick and Evans. Compact enough for locomotives and portable engines. |
| Cornish pumping engine | early 1800s | Best duty near 10% | High pressure, early cutoff, and a condenser. |
| Compound through quadruple expansion | mid to late 1800s | About 10 to 18% on good marine plants | Steam expanded in successive cylinders. |
| Uniflow piston | early 1900s | Toward the top of the piston range | Exhaust at mid-cylinder so the hot ends stayed hot. |
| Large steam turbine plant | 1900s to now | About 33 to 45% | Many stages, superheat, reheat, feedwater heating. Supercritical steam is the high end. |

"Duty" on old pumping engines was foot-pounds of water lifted per bushel of coal (94 lb). Roughly, 10 million duty is about 1% thermal, and 100 million is about 11%, for coal near 12,000 BTU/lb.

## Reciprocating ladder

### Aeolipile

Hero's sphere, first century. Steam jets out of bent nozzles and the ball spins in reaction. It is a toy turbine with no shaft you can load. It shows that steam can make rotation. It does not show a useful engine.

### Savery pump (1698)

No piston and no beam. Steam pushed into a vessel, then condensed, and the vacuum sucked mine water up a pipe. A second dose of steam pushed that water higher. Lift was limited by boiler pressure and by about 30 feet of vacuum suction. Mines wanted more lift than it could give safely. Boilers burst.

### Newcomen (1712)

A vertical cylinder over a boiler, a piston chained to a rocking beam, and pump rods on the other end of the beam.

1. Steam at about atmospheric pressure fills the cylinder under the piston.
2. A spray of cold water condenses that steam.
3. Vacuum forms. The atmosphere pushes the piston down. That stroke is the power stroke.
4. The beam rocks back and lifts the mine pump.

Speed was on the order of 12 strokes a minute. The cylinder was heated and then chilled every stroke, which is why the coal use was enormous. It still drained mines that horses could not drain, and it stayed in service for a century because it was simple and could be built by millwrights.

### Watt

The separate condenser (patent 1769) put the cold spray in another vessel. The working cylinder stayed hot. That was the efficiency jump.

Later Watt pieces, useful as a checklist for a "complete" low-pressure engine:

- **Steam jacket:** a steam-filled outer skin so the cylinder walls do not steal heat.
- **Double-acting cylinder:** steam pushes both sides of the piston, so every stroke works. Needs a sealed piston rod and a stuffing box.
- **Rotative output:** sun-and-planet gear, then a crank. Turns a mill shaft instead of only pumping.
- **Parallel motion:** keeps the piston rod straight while the beam end arcs.
- **Centrifugal governor:** spins with the shaft and throttles steam as speed rises.
- **Expansive working:** inlet valve closes before the end of the stroke. Trapped steam finishes the push while expanding.

Watt engines ran at only a little above atmospheric pressure and relied on the condenser vacuum. They were building-sized for tens of horsepower. They were safe compared with high-pressure boilers and too heavy for a vehicle.

### High pressure

After Watt's patent lapsed in 1800, Trevithick in Britain and Evans in America built engines at tens of psi above atmosphere, exhausting straight to the air. Losing the condenser costs efficiency. Shedding the huge beam, the condenser, and the low-pressure bulk cuts weight so much that a wagon or a rail chassis can carry the engine. Locomotives, portable farm engines, and traction engines come from this branch.

Higher pressure also lets expansive cutoff do more work per pound of steam. The Cornish engine kept the condenser and added high pressure and a very early cutoff. It was a pumping engine, slow and efficient, not a locomotive.

### Compound expansion

One cylinder cannot expand steam from full boiler pressure down to a condenser vacuum without becoming huge and cold at the outlet end. Compound engines split the expansion:

- **Woolf / receiver compound:** high-pressure cylinder exhausts into a receiver, then into a larger low-pressure cylinder.
- **Tandem:** both pistons on one rod.
- **Cross-compound:** cylinders side by side, cranks often at 90° so the engine can start in any position.
- **Triple and quadruple:** marine practice from the 1880s. Each stage is a larger cylinder. The low-pressure piston can be taller than a person on a liner.

Cutoff on the first cylinder sets the power. Later cylinders are sized to accept that volume.

### Uniflow

Steam enters at the hot ends of the cylinder and leaves through a belt of ports at the middle, uncovered by the piston at the end of the stroke. Inlet metal stays hot and exhaust metal stays cooler, so less steam condenses on the walls each stroke. Early twentieth-century uniflow engines were among the best piston prime movers. Turbines took the large installations anyway, because a turbine has no reciprocating mass and no valve gear.

### Valve gear, only what changes the engine

- **D-slide valve:** one sliding block opens inlet and exhaust. Simple, rubs hard, and leaks more as pressure rises. Fine for a first low-pressure engine.
- **Piston valve:** a bobbin sliding in a sleeve. Pressure-balanced, so high-pressure locomotives used it.
- **Corliss valves:** separate rotary inlet and exhaust valves with a trip that drops the inlet shut. Very efficient at part load on mill engines. Fussy to make.
- **Poppet valves:** lift off a seat like a pump valve. Less wire-drawing than a long slide.
- **Link gear** (Stephenson, Walschaerts, Baker): one mechanism sets both direction and cutoff. This is what lets a locomotive reverse and run economically. A fixed eccentric is enough for an engine that always turns the same way.

Oscillating-cylinder engines pivot the whole cylinder on a steam joint so the pivot is the valve. Toys and some small boat engines. Few parts, leaky joint, low power.

## Boilers

The engine is not the dangerous part. The boiler is a pressure vessel full of water that wants to become two thousand times its liquid volume.

| Boiler | Layout | Trait |
|---|---|---|
| Haystack, wagon, egg-ended | Early shells, often a fire underneath | Simple and burst-prone. |
| Cornish | One large flue through a shell | Better firing than a kettle. Low steam rate. |
| Lancashire | Two flues | More grate, still a shell boiler. |
| Locomotive | Many small fire tubes from a firebox to a smokebox | High steam rate for the weight. Needs decent water and a blast to pull the fire. |
| Scotch marine | Short fat shell, furnaces inside, tubes back | Standard ship boiler before water-tube took over. |
| Water-tube | Water in the tubes, fire outside | Safer (less stored water) and happier at high pressure. The bent-tube "Stirling boiler" is this family, named for a boiler firm. It is not a Stirling engine. |
| Monotube / flash | A pumped coil in the fire | Little stored water, steam in seconds, hard to control. Serpollet and Doble steam cars. A burst is a ruptured tube, not a flying shell. |

Safety parts that belong on any boiler above a toy: water level gauge, pressure gauge, spring or deadweight safety valve, and a fusible plug in the crown that melts if the water falls and the firebox overheats. Scale from hard water insulates the plate and burns it. Priming (water carried over with steam) wrecks cylinders.

A heating rune or a mana stone under the shell replaces the grate. It does not replace the water level, the valve, or the plate strength. Emptying a boiler while the heat stays on still overheats the metal.

## Turbines

A turbine expands steam through nozzles or blade rows and takes the work as pure rotation. No piston, no valve clatter, and no shaking foundation. Speed is high: early single-stage impulse wheels ran at tens of thousands of rpm and needed gearing. Multi-stage reaction machines (Parsons, 1884) ran slower and could sit on a dynamo shaft.

- **Impulse:** nozzles turn pressure into a jet, and buckets turn the jet. The pressure drop is in the nozzle.
- **Reaction:** blades are shaped so pressure also drops across the moving row. More stages, finer clearances.
- **Velocity compounding:** several moving rows take energy from one nozzle's jet (Curtis). Compact, less efficient.
- **Pressure compounding:** many stages, each taking a small pressure drop. This is the power-station pattern.

Large plants add superheat (steam hotter than the boiling point at that pressure, so it stays dry in the later stages), reheat between cylinders, and bleed steam to warm the feedwater. Those three are why a turbine station can pass 40% while a locomotive rarely reached the mid-teens even on test.

A turbine hates going backward and hates low speed under load. Piston engines are better when the shaft must start against a heavy load, reverse, or linger at a few dozen rpm. Turbines are better when the load is a generator or a fast propeller that can stay in one direction.

## Rotary piston attempts

Vane, gear, and wobble-plate steam engines were patented all through the nineteenth century. The idea was a turbine's smooth spin with a piston engine's tolerance for wet steam. In practice the sliding seals leaked as soon as they wore, and heat warped the rotor. The turbine won that contest. Treat rotary steam pistons as a known dead end unless magic supplies a seal that does not wear.

## Craft walls

- **Boring:** a hammered cylinder is not round enough. Watt's engines became practical after Wilkinson's boring bar (1774) could keep a large bore true. This is the same lathe-and-boring step as `KitchenCraft.md`.
- **Piston seal:** hemp packing, then cast-iron piston rings sprung outward. Leakage past the piston is lost work and wet condensate.
- **Stuffing box:** where the rod leaves the cylinder. Packing too tight wastes power and scores the rod. Too loose, steam cuts through.
- **Lubrication:** cylinder oil has to survive steam and not wash off. Animal tallow was the early answer. Mineral cylinder oil came later. Water in the steam strips oil.
- **Condenser air leak:** a condenser only makes vacuum if air cannot get in. An air pump has to pull out the air that leaks and the air that was dissolved in the feedwater.
- **Speed and balance:** a single piston shakes the frame. Two cylinders at 90° or a flywheel (`FlywheelStorage.md` is the extreme; a cast-iron mill flywheel is the mundane version) smooth the shaft.
- **Stored energy:** boiler explosions kill by scalding and by the blast of the shell. High-pressure steam is a prestige hazard, not a cottage toy.

## Story-scale sizes

| Engine | Rough size | Output |
|---|---|---|
| Table model, a few psi | Kettle and a thumb-sized bore | Watts. A demonstration. |
| Workshop single cylinder | Wheelbarrow to cart | 1 to 10 hp. A lathe line, a pump, a small dynamo. |
| Portable / traction | Wagon, with its own boiler | 5 to 30 hp. Thresher, plow, saw. |
| Locomotive | The vehicle is the boiler | Hundreds to a few thousand hp. |
| Mill beam or Corliss | A room, a masonry foundation | Tens to a few hundred hp. |
| Ship compound or turbine | An engine room | Thousands to tens of thousands of hp. |

Mana-stone fire can shrink the grate and the fuel bunker. It does not shrink the cylinder that has to pass a given horsepower, and it does not shrink a condenser that has to swallow the exhaust.
