# Runic Blade Channels

**Verdict:** a hybrid beats both pure routes. Forge the mundane blade to near net shape and cut the channels by magic while the steel is soft (annealed). Then heat treat and inlay after temper. Casting around a core gives the weakest steel. Tunneling a fully hardened blade gives the best geometry but carries the highest crack risk.

Companion forge metallurgy: `CraftMetal.md`. Fuel / forge energy bands: `BlacksmithProducts.md`. 1095 HT: `EarthAlloys.md`. Path / Useful: `../../../Runes/Energy.md`.

## Assumptions

- Finished blade **1.1 kg** from a **1.8 kg** billet.
- Circuit channel **3 mm** bore by **1 m** long. That is **7 cm³** or about **55 g** of steel.
- Charcoal at **30 MJ/kg** and forge or furnace efficiency of **5 to 10%**.
- Magic cost uses the bond-breaking floor of iron (about **7.4 MJ/kg**; table **7.5** in `../../Materials/AtomizationEnergy.md`) divided by an efficiency of **10 to 30%**. Floor for the channel mass alone ≈ **0.41 MJ**.

## Energy estimates

| Step | A: Cast around core | B: Forge then tunnel hardened | C: Forge then tunnel annealed |
|---|---|---|---|
| Melt or forge (fuel) | 25 to 45 MJ melt | 100 to 250 MJ | 100 to 250 MJ |
| Mold burnout and preheat | 40 to 90 MJ | none | none |
| Homogenizing soak | 30 to 60 MJ | none | none |
| Heat treatment | 15 to 35 MJ | 15 to 35 MJ | 15 to 35 MJ |
| Magic work | 0.2 to 0.7 MJ (core forming and removal) | 1.4 to 4 MJ (floor 0.41 MJ) | 0.5 to 3 MJ |
| **Total fuel** | **110 to 230 MJ** | **115 to 285 MJ** | **115 to 285 MJ** |

The magic share is about **1%** or less of the total in every route. The whole tunneling budget equals roughly **100 to 150 g** of charcoal. Energy therefore does not decide the choice. Quality does.

## Route A: cast around a core

**Pros:**

- Curved and branching 3D circuits form in one operation with no tool access limits.
- No cutting stress and no heat-affected zone from tunneling.
- Cheapest per unit in batches, which suits a steam-powered foundry turning out many runic blades.
- Lowest magic energy.

**Cons:**

- Foam cannot hold a void. It burns away and metal fills the space. Foam shapes the outside only.
- The channel needs a solid core that survives **1550 °C** or more, such as a magic-formed ceramic or crystal.
- Steel shrinks about **2%** linearly on cooling. A rigid core resists that and causes hot tears or a cracked core. The core must collapse or crush.
- Pulling a core out of a **1 m** by **3 mm** bore needs dissolution or magic extraction. Walls come out rough with a ceramic reaction layer.
- As-cast steel is dendritic with segregation, porosity and inclusions. Toughness and fatigue life under blade flex fall well below forged steel.
- Forging the cast blank to fix the grain would collapse or kink the hollow channel. The refinement step is effectively unavailable.
- Lost-foam residue adds carbon and gas defects if foam is used for the outer pattern.
- Shrinkage shifts channel dimensions by about **2%**. That matters if rune function depends on exact geometry.

## Route B: finished mundane sword then tunnel by magic

**Pros:**

- Best steel. It is fully forged, grain refined and quenched with no compromises.
- Channel geometry is exact and unaffected by shrinkage.
- Heat-sensitive runic inlay goes in last and never sees a quench.
- Existing blades can be retrofitted.

**Cons:**

- Hardened steel at **58 to 60 HRC** is the worst state to cut. Thermal-type magic leaves a recast layer with microcracks and locally softens the temper, like EDM.
- Residual tensile stress and a stress concentrator sit in a thin wall of brittle steel. This is the classic origin of a fatigue crack that snaps the blade.
- Closed-end channels are hard to flush of debris.
- Entry and exit points must be sealed.
- Highest magic energy of the three routes.

## Route C: forge, tunnel while annealed, then heat treat

**Pros:**

- Soft steel cuts cleanly and tolerates the tunneling process.
- Normalizing and austenitizing afterward erase any heat-affected zone and relieve residual stress.
- Keeps the full forged microstructure.
- Inlay still goes in after temper.

**Cons:**

- The channel is present during quench and acts as a stress concentrator. Mitigate with an oil or interrupted (martempering) quench and large corner radii.
- Plug the channel with a ceramic or steel rod during austenitizing to prevent decarburization and quench-fluid trapping.
- Quench distortion of about **0.1 to 0.2%** slightly shifts channel geometry.
- Requires a thicker mid-section. A **3 mm** bore needs a blade at least **7 mm** thick at the rib. Thinner blades need a **1.5 to 2 mm** bore (a **2 mm** bore cuts the energy figures by more than half).

## Ranking for a single high-quality blade

| Factor | A | B | C |
|---|---|---|---|
| Steel toughness and fatigue | Poor | Excellent | Excellent |
| Channel precision | Fair | Excellent | Good |
| Crack risk | Moderate | High | Low to moderate |
| Complex circuit geometry | Excellent | Good | Good |
| Batch scalability | Excellent | Poor | Fair |
| Fuel energy | Equal | Equal | Equal |
| Magic energy | Lowest | Highest | Low |

Route A wins only for mass production where runic function matters more than steel quality. Route B wins only when the runic material cannot take any heat and the blade already exists. Route C is the best default for a master-grade magic sword.
