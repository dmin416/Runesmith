# Friction Notes

> Earth / invent loot. Not locked law. Indestructible / no-bend stock: `../../Materials/MaterialConsiderations.md`, `../../Materials/Metals.md`. Engines and pistons: `SteamEngines.md`, `StirlingEngines.md`, `Compression.md`. Flywheel zero-friction fiction: `FlywheelStorage.md`.

---

## Core Facts

- Friction comes from surface atoms bonding together (adhesion) and microscopic peaks catching on each other (deformation).
- Friction depends on the sideways or pressing force and on surface chemistry. It does not depend on how much area touches.
- Hardness does not equal low friction. Clean diamond on clean diamond in a vacuum grips about as hard as rubber on pavement.
- Polishing past a certain point makes surfaces stickier. Ultra-clean, ultra-flat metals can fuse on contact (cold welding).

## Best Ways to Reduce Friction (General)

1. **No contact at all.** Air bearings, magnetic levitation or a floating fluid film. Removes surface friction entirely.
2. **Fluid film lubrication.** Oil dragged into the gap by motion keeps surfaces apart. Friction about 0.001.
3. **Superlubricity.** Two crystal surfaces with mismatched atomic patterns slide almost freely. Friction about 0.0001 or lower. Currently only proven at micrometer scale.
4. **Solid lubricants.** Graphite or molybdenum disulfide. Layered sheets slide over each other easily.
5. **Boundary additives.** Coatings a few molecules thick that shear easily when a fluid film breaks down.
6. **Inert surface coatings.** A chemically passive skin stops atoms from bonding across the gap.
7. **Remove the pressing force.** Every source of sideways load removed lowers friction directly.

## Superlubricity

Friction near zero (0.001 or lower) while surfaces still touch.

**How it works:** crystal surfaces are grids of atomic bumps. Aligned grids lock together like stacked egg cartons. Rotated or mismatched grids cancel out their pushes and pulls so the top layer glides.

**Proven examples:**
- Graphite flakes on rotated graphite
- Graphene on hexagonal boron nitride (naturally mismatched spacing)
- Diamond-like carbon coatings (see below)
- Liquid superlubricity: certain glycerol and water-based films between ceramics or glass

**Limits:**
- Mostly micrometer scale. Defects and grain boundaries on large surfaces break it.
- Flakes rotate back into alignment and lock.
- Edges of the sliding piece add friction.
- Requires extreme cleanliness. One contaminant layer can ruin it.

## Diamond-Like Carbon (DLC) Coatings

### What It Is

- A thin coating (usually 1 to 5 micrometers) of amorphous carbon. No crystal structure.
- Mix of diamond-type bonds (hard) and graphite-type bonds (slippery).
- Applied in a vacuum chamber by plasma or vapor deposition onto metal, ceramic or plastic parts.

### Types (Full Classification)

Industry standard naming (VDI 2840). "a" = amorphous, "t" = tetrahedral (diamond-bond rich), ":H" = contains hydrogen, ":Me" = contains metal, ":X" = contains a non-metal additive.

| Type | Hydrogen | Diamond Bonds | Hardness (GPa) | Best Environment | Typical Friction | Notes |
|---|---|---|---|---|---|---|
| **a-C** | None | Low | 10 to 20 | Air, oil | 0.1 to 0.2 | Graphite-rich. Softer, tougher, cheap to sputter |
| **ta-C** | None | 50 to 85% | 40 to 80 | Humid air, oil | 0.05 to 0.15 (0.005 to 0.01 with glycerol or ester oil) | Hardest and most wear resistant. Heat stable to about 500 °C. High friction in vacuum |
| **a-C:H** | 10 to 40% | 20 to 60% | 10 to 30 | Dry gas, vacuum, oil | 0.01 to 0.1 dry, 0.1 to 0.3 humid | Most common industrial DLC. Smooth and low stress |
| **Near-frictionless carbon** (high-H a-C:H) | Very high | Moderate | 10 to 20 | Dry nitrogen, vacuum | 0.001 to 0.003 | Superlubric range. Very sensitive to humidity |
| **ta-C:H** | Low to moderate | High | 30 to 50 | Dry or lubricated | 0.05 to 0.1 | Between ta-C and a-C:H |
| **a-C:H:Me** (W, Ti, Cr) | Yes | Low to moderate | 10 to 20 | Air, oil | 0.1 to 0.2 | Metal carbide grains in carbon. Tougher, better adhesion, tolerates impact and soft substrates |
| **a-C:Me** | None | Low | 10 to 20 | Air, oil | 0.1 to 0.2 | Metal-containing, hydrogen-free |
| **a-C:H:Si** (or Si-O) | Yes | Moderate | 15 to 25 | Humid air | 0.05 to 0.1 | Silicon cuts humidity sensitivity and raises heat limit |
| **a-C:H:F** | Yes | Low | Under 10 | Air | 0.1 to 0.2 | Fluorine gives non-stick, water-repelling surface |
| **a-C:H:N** | Yes | Moderate | 15 to 25 | Air | 0.1 to 0.2 | Lower stress, conductive variants |

### Choosing a Type

- Lowest friction in dry or vacuum: near-frictionless carbon or a-C:H
- Lowest friction with oil: ta-C with ester or glycerol-based lubricant
- Maximum wear resistance: ta-C
- Humid open air: ta-C or a-C:H:Si
- Impacts, shock loads or softer base metal: a-C:H:Me
- High heat: ta-C or a-C:H:Si
- Non-stick: a-C:H:F

### Why It Is So Slippery

- **Surface passivation:** hydrogen or hydroxyl groups cap the loose carbon bonds on the surface. Nothing is left to bond across the gap. This is the same effect that makes natural diamond slippery in air.
- **Transfer layer:** during sliding, a thin graphite-like film forms on the contact and smears onto the opposite surface. The two surfaces then slide carbon on carbon along weak layers.
- **Amorphous structure:** no repeating atomic grid means nothing lines up to lock.
- **High hardness:** peaks barely deform, so very little plowing.

### Where It Is Used

- Engine parts: piston pins, piston rings, cam followers, valve lifters
- Fuel injector components
- Razor blades and cutting tools
- Hard drive platter overcoats
- Medical implants
- Firearm parts and bearings

### Limits

- Internal stress limits thickness. Thick coatings crack or peel.
- Needs bonding interlayers (chromium, silicon, titanium) to stick to the base material.
- Hydrogenated types break down above roughly 300 to 350 °C. ta-C survives to roughly 500 °C.
- Each type only performs well in its matching environment (dry vs humid vs oiled).
- Coating wears eventually even when the base material does not.

### How DLC Is Made

DLC is not made separately and glued on. It is grown directly on the part inside a vacuum chamber, atom by atom. Making it and applying it are the same process.

**The key principle:** carbon ions hitting the surface at around 100 electron-volts get driven just under the surface, packing atoms tightly and forcing diamond-type bonds. Too little energy gives soft graphite-like carbon. Too much energy heats the spot and converts it back to graphite-like bonds.

**Deposition methods:**

| Method | Carbon Source | Produces | Part Temperature | Strengths | Weaknesses |
|---|---|---|---|---|---|
| **PECVD** (plasma-enhanced chemical vapor deposition) | Hydrocarbon gas (acetylene, methane) broken apart by plasma. Part given negative voltage to pull ions in | a-C:H, a-C:H:Si, a-C:H:F, a-C:H:N | 150 to 250 °C | Coats complex shapes and inside surfaces evenly. Cheap at scale | Always contains hydrogen. Lower hardness |
| **Magnetron sputtering** | Solid graphite target blasted by argon ions | a-C, a-C:H (with added gas), a-C:H:Me (with metal target) | 100 to 250 °C | Easy to dope with metals. Smooth films | Lower diamond bond content. Slower |
| **HiPIMS** (high-power impulse sputtering) | Graphite target hit with short intense pulses | Dense a-C, ta-C:H | 100 to 200 °C | Denser and harder than normal sputtering | More complex equipment |
| **Filtered cathodic vacuum arc** | Electric arc on solid graphite. Magnetic filter removes droplets | ta-C | Near room temp to 150 °C | Hardest films, highest diamond bonds | Line of sight only. Droplets if unfiltered |
| **Pulsed laser deposition** | Laser blasts graphite target | ta-C | Room temp | High quality | Lab scale, small areas |
| **Ion beam deposition** | Carbon ion beam aimed at part | ta-C, a-C:H | Room temp | Precise control | Slow, small areas |

### How DLC Is Applied (Process Steps)

1. **Choose a hard enough base.** Thin hard coating on a soft base cracks like an eggshell under load. Use hardened steel, nitrided steel, carbide, titanium alloy or ceramic. Base must tolerate the process temperature without softening.
2. **Finish the surface.** Coating copies the surface underneath. Polish to the final smoothness wanted before coating (roughness under about 0.1 micrometers for sliding parts).
3. **Clean thoroughly.** Degrease, ultrasonic bath in solvents and water, dry. Any oil or fingerprint causes peeling.
4. **Load and pump down.** Vacuum chamber pumped to about one hundred-millionth of normal air pressure.
5. **Heat and ion etch.** Argon plasma blasts away the oxide layer and remaining contamination, leaving bare clean metal.
6. **Adhesion interlayer.** A bonding layer of chromium, titanium or silicon (often 0.1 to 0.5 micrometers).
7. **Gradient layer.** Gradual transition from metal to carbon (such as chromium nitride, tungsten carbide or metal-doped carbon) so stress doesn't concentrate at one boundary.
8. **DLC top layer.** Grown to 1 to 5 micrometers. Thicker builds internal stress and risks peeling unless built in alternating layers.
9. **Cool in vacuum and vent.** Cooling slowly avoids thermal shock cracking.
10. **Inspect.** Thickness check (ball crater test), adhesion check (indent or scratch test), hardness check.

### How to Maintain DLC

**Day-to-day:**
- Generally needs no maintenance. Chemically inert and resists almost all solvents, acids, bases and corrosion.
- Clean with mild soap, solvents or alcohol. Avoid abrasive pads and polishing compounds that scratch through.
- Keep the operating environment matched to the type (dry for a-C:H, oiled or humid for ta-C).

**Break-in:**
- Friction starts higher and drops as the transfer layer forms on the opposite surface.
- Run at light loads first so the layer forms without damage.

**Lubricant compatibility:**
- Ester oils and glycerol-based fluids work best with ta-C.
- Some molybdenum-based friction additives (MoDTC) in engine oils speed up DLC wear. Avoid them on hydrogenated types.
- Filter oil. Hard particles in the oil act like sandpaper.

**Things that destroy it:**
- Temperatures above its limit (300 to 350 °C hydrogenated, about 500 °C ta-C) convert it toward graphite
- Point impacts on a soft base (eggshell cracking)
- Abrasive grit
- Sliding a-C:H in humid air or ta-C in vacuum (wrong environment)
- Oxygen plasma or high-temperature air (burns carbon away)

**Inspection:**
- Wear-through shows as base metal color appearing through the dark gray or black coating.
- Look for flaking at edges and around impact points.
- Rising friction or noise means the coating is thinning or the transfer layer is gone.

**Stripping and recoating:**
- Oxygen plasma burns the carbon off as carbon dioxide without harming most metals.
- Chemical or electrochemical baths remove the metal interlayer.
- After stripping, the part goes back through the full application process.
- Worn parts are usually stripped and recoated rather than patched. Patching leaves weak boundaries.

## Air Bearings

Surface floats on an air film a few micrometers thick. No contact, no surface friction, no wear. Only slight air drag.

**Types:**
- **Aerostatic (externally pressurized):** compressed air fed through tiny holes or porous material (often porous graphite). Works at zero speed. Used in precision measuring machines and semiconductor manufacturing stages.
- **Aerodynamic (self-acting):** motion drags air into a narrowing gap and pressurizes it. Needs speed to lift off. Rubs briefly at startup. Foil bearings in turbochargers, microturbines and aircraft cooling units.

**Strengths:** near-zero friction at any speed, extremely smooth precise motion, no oil contamination, effectively unlimited life.

**Weaknesses:** much lower load per area than oil, needs clean dry air (and a compressor for aerostatic), needs very tight stable gaps, can vibrate unstably (pneumatic hammer), crashes at speed usually destroy the bearing.

**Existing gas-bearing pistons:** space cryocoolers and some linear compressors float pistons on a gas film with a tiny clearance gap as the only seal. They run for years with no oil and no wear. Glass-and-graphite dashpot pistons also run nearly frictionless.

## Indestructible Material Piston (No Expansion, No Bending, No Wear)

### Best Design

- Piston machined to sit a few micrometers off the cylinder wall. Never touches.
- Rows of fine ridges along the sides as a **labyrinth seal**. Gas loses pressure at each ridge and groove, so very little leaks past.
- Thin gas or oil film in the gap centers the piston and carries side loads (hydrodynamic bearing).
- No rings, no O-rings, no spring force.

### Why the Material Makes This Work

- Normal labyrinth seals need extra gap for heat expansion, vibration and wear. That gap causes leakage.
- A material that never changes shape allows the gap to be held tiny and constant forever.
- Result: friction only from shearing the thin film, roughly 100 times lower than metal rubbing metal. No wear, no rings, runs indefinitely.

### Sideways Forces to Eliminate or Manage

| Source | Present With Rigid Spikes/Ridges? | Fix |
|---|---|---|
| Ring spring tension | No | Already removed |
| Gas pushing rings outward | No | Already removed |
| Connecting rod side thrust | Yes | Crosshead design (keeps piston push straight in line) or fluid film to carry it |
| Gravity (horizontal cylinder) | Yes | Vertical cylinder or fluid/gas bearing film |

### Key Points

- Spikes touching the wall do not lower friction. Any sideways load concentrates onto the tips that make contact.
- With zero sideways load, touching spikes would have near-zero friction. Real machines almost always have some load.
- Non-contact ridges (labyrinth seal) beat touching spikes in every case.
- Indestructible does not mean frictionless. The surface chemistry still bonds on contact. Keeping a gap is what matters.
- The material removes the two biggest air bearing weaknesses: gaps stay perfectly tight forever and crashes cause no damage. A startup rub or overload contact costs only momentary friction.
- For any contact that does happen, a DLC coating matched to the environment (a-C:H or near-frictionless carbon for dry gas, ta-C for oil or humid air) caps the surface bonds and cuts friction. The coating itself is not indestructible and would wear at contact points, so it works best as backup protection behind a gas film rather than as the main sliding surface.
