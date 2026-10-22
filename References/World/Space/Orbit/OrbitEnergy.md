# Orbit Energy

Hub: `../Space.md`. Station masses: `LowEarthOrbitHabitat.md`, `GeosynchronousHabitat.md`. Geometry: `../Atmosphere.md`. Chemical launch path: `Hydrolox.md`.

Minimum **mechanical** energy to put mass on orbit: lift to altitude (potential) plus bring it up to orbital speed (kinetic). Ignores the rocket itself, air drag, gravity losses and engine inefficiency.

## Per kilogram

| | Low orbit (250 mi) | Geosynchronous (22,236 mi) |
|---|---|---|
| Orbital speed | 17,160 mph (7.67 km/s) | 6,880 mph (3.07 km/s) |
| Lift (potential energy) | 3.7 MJ | 53.1 MJ |
| Speed (kinetic energy) | 29.4 MJ | 4.7 MJ |
| **Total per kg** | **33.1 MJ (9.2 kWh)** | **57.8 MJ (16.1 kWh)** |

At low orbit almost 90% of the energy goes into speed. At geosynchronous orbit over 90% goes into height, since the orbit there is much slower.

## Full one-person stations

Masses from the habitat files (baseline jackets).

| | Low orbit station | Geosynchronous station |
|---|---|---|
| Mass | 32,600 kg (71,870 lb) | 48,800 kg (107,600 lb) |
| Lift | 0.12 TJ (34 MWh) | 2.59 TJ (720 MWh) |
| Speed | 0.96 TJ (267 MWh) | 0.23 TJ (64 MWh) |
| **Total** | **1.08 TJ (300 MWh)** | **2.82 TJ (784 MWh)** |
| TNT equivalent | ~258 tons | ~675 tons |

## Real launch scale

Rockets deliver only about 10% of their propellant's chemical energy to the payload. The rest goes into accelerating the rocket's own fuel and structure, fighting gravity during the climb and pushing through the air. Actual launch energy runs roughly 10 times these figures: about 3,000 MWh for the low orbit station and about 8,000 MWh for the geosynchronous one.

Terra's rotation contributes a small free boost of about 1,040 mph at the equator. That cuts the totals by only 1 to 2%.

Green hydrolox propellant mass and plant-to-orbit electricity for the same stations: `Hydrolox.md` (~4% overall efficiency).
