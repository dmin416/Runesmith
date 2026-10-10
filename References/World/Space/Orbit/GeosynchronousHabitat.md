# Living in Geosynchronous Orbit (22,236 miles)

Hub: `../Space.md`. Orbit geometry and layers: `../Atmosphere.md`. Lower station and LEO vs GEO compare: `LowEarthOrbitHabitat.md`. Launch energy: `OrbitEnergy.md`. Open-air mana at this height: `../../Science/Energy/ManaConcentration.md`. World size: `../../World.md` (Earth-sized Terra).

Terra-analog of Earth geosynchronous living. Figures are engineering estimates scaled from Earth ISS data and NASA life-support planning numbers. Magic can replace hardware later; this file is the mundane baseline.

---

# Part 1: Requirements

## Radiation Protection

The biggest difference from a ~250 mi orbital station. Geosynchronous orbit sits inside the outer radiation belt and gets far less shielding from Terra's magnetic field.

- Heavy hull shielding using water, polyethylene or other hydrogen-rich materials
- A dedicated storm shelter with extra shielding for solar particle events
- Space weather monitoring and alerts, since strong solar storms can compress the magnetosphere inside 22,236 miles and expose the station to raw solar wind
- Radiation-hardened electronics
- Personal dosimeters and strict career exposure limits for crew

## Breathable Atmosphere

- Pressurized hull holding about 14.7 psi
- Oxygen generation through water electrolysis plus stored oxygen reserves
- Carbon dioxide scrubbers
- Trace contaminant filters for gases released by materials and people
- Humidity and temperature control
- Fire detection and suppression
- Leak detection and patching kits

## Water

- Closed-loop recycling of urine, sweat and humidity (Earth ISS reaches about 98% recovery)
- Purification and contamination testing
- Reserve tanks, which double as radiation shielding

## Food

- Long-shelf-life stored food with large reserves, since resupply is slower and costlier than low orbit
- Hydroponic or aeroponic gardens for fresh produce on long stays
- Food preparation and storage systems that work in microgravity

## Power

- Large solar arrays (the orbit sees almost constant sunlight)
- Batteries for eclipse seasons around the equinoxes, when the station passes through Terra's shadow for up to about 72 minutes per day
- Backup power systems

## Thermal Control

- Radiators to dump heat from people and equipment, especially important with near-constant sunlight
- Multilayer insulation
- Active fluid loops to move heat around the station

## Gravity and Physical Health

- Daily exercise of about 2 hours on treadmills, bikes and resistance machines to slow bone loss of roughly 1 to 1.5% per month and muscle wasting
- Or a rotating section to create artificial gravity
- Medical bay with diagnostic equipment, medications and surgical supplies
- Telemedicine link (communication delay to Terra is only about a quarter second round trip)

## Waste Management

- Toilets that use airflow instead of gravity
- Solid waste storage, compaction or processing
- Trash disposal on departing cargo ships

## Transportation

- Crew vehicles capable of the much larger fuel budget needed to climb from low orbit to 22,236 miles
- Regular cargo resupply flights
- Docking ports and airlocks
- Emergency return capsule always attached, with a heat shield rated for reentry at about 6.2 miles per second versus about 4.9 for low-orbit returns

## Station Keeping

- Thrusters and fuel to hold position against gravitational tugs from the Sun and moons and pressure from sunlight
- Attitude control using gyroscopes or reaction wheels
- Tracking and collision avoidance

## Debris Protection

- Whipple shielding against micrometeoroids and debris
- Debris at this height never decays naturally, so the hazard only grows over time

## Communications

- Constant line of sight to one side of Terra, which makes contact with ground stations simple and uninterrupted
- Relay links for contact with the opposite hemisphere

## Psychological Support

- Private quarters
- Regular contact with family and mission control
- Entertainment, recreation and windows (a geostationary station sees the same face of Terra at all times)
- Structured schedules and crew selection for long-duration isolation

---

# Part 2: Estimates for One Person

## Baseline Assumptions

- Mission length: 1 year
- Habitat: aluminum cylinder 13.1 ft (4 m) in diameter and 16.4 ft (5 m) long inside, about 2,220 cu ft (63 m³) pressurized
- About half the interior is usable living space after equipment
- Water forms a jacket around the entire hull and serves as the radiation shield
- Figures are engineering estimates scaled from Earth ISS data and NASA life support planning numbers

## Radiation Shielding (Water)

### Hull Water Jacket Options

| Jacket thickness | Water mass | Estimated annual dose |
|---|---|---|
| None (thin hull only) | 0 | Several to tens of grays from trapped electrons (lethal) |
| 8 in (20 cm) | 19,300 kg (42,550 lb) | ~0.5 Sv |
| 20 in (50 cm) | 55,000 kg (121,250 lb) | ~0.4 Sv |
| 39 in (1 m) | 135,000 kg (297,620 lb) | ~0.3 Sv |

For comparison: Earth ISS crews receive about 0.2 to 0.3 Sv per year. NASA's career limit is 0.6 Sv. Ground-level background is about 0.003 Sv per year.

The 8 in jacket stops nearly all trapped belt electrons and most solar storm protons. Galactic cosmic rays are the remaining dose and resist water shielding, which is why thicker jackets bring diminishing returns.

**Baseline choice for the rest of this file: 8 in (20 cm) jacket.**

### Storm Shelter

- Sleeping pod 3.3 ft (1 m) wide and 6.6 ft (2 m) long inside the habitat
- Extra 12 in (30 cm) water wrap: 3,700 kg (8,160 lb)
- Combined protection inside the pod: about 50 g/cm² of water
- Doubles as the private sleeping quarters

### Other Radiation Items

- Personal dosimeter plus 4 area monitors: ~5 kg (11 lb)
- Space weather data feed from ground and satellite services: no onboard mass
- The jacket must be kept above freezing by cabin heat and heaters under the outer insulation

## Breathable Atmosphere

| Item | Daily | Annual or total |
|---|---|---|
| Oxygen consumed | 0.84 kg (1.85 lb) | 307 kg (677 lb) |
| CO2 exhaled | 1.0 kg (2.2 lb) | 365 kg (805 lb) |
| Cabin air at 14.7 psi | | 76 kg (168 lb) total: 18 kg oxygen and 58 kg nitrogen |
| Leak and airlock losses | ~0.1 kg (0.22 lb) | ~37 kg (82 lb) makeup gas |
| Emergency oxygen reserve | | 90 days: 76 kg (168 lb) |
| Repressurization reserve | | 2 full refills: 152 kg (335 lb) of air |
| Backup CO2 canisters (lithium hydroxide) | | 30 days: 40 kg (88 lb) |
| Trace contaminant filter replacements | | 10 kg (22 lb) |
| Fire extinguishers | | 3 units: 20 kg (44 lb) |

Hardware:

- Oxygen generator (electrolysis): ~200 kg (440 lb)
- Regenerable CO2 removal system: ~300 kg (660 lb)
- Sabatier reactor to recover water from CO2: ~100 kg (220 lb)
- Humidity, temperature and contaminant control: ~150 kg (330 lb)

## Water

| Item | Amount |
|---|---|
| Daily use (2 L drinking, 0.5 L food, 1.5 L hygiene) | 4 L (1.1 gal) |
| Annual throughput | 1,460 L (386 gal) |
| Working loop buffer | 200 L (53 gal) |
| Lost per year at 98% recovery | ~30 L (8 gal) |
| Water split for oxygen without Sabatier | 345 L (91 gal) per year |
| Water split for oxygen with Sabatier | ~175 L (46 gal) per year |
| Total annual makeup | 205 to 375 L (54 to 99 gal) |
| Separate reserve tank | 500 L (132 gal) |
| Recycling hardware | ~400 kg (880 lb) |

The 19,300 kg shield holds about 50 years of makeup water. Makeup should come from the separate reserve tank so the shield stays at full thickness.

## Food

| Item | Amount |
|---|---|
| Daily (about 2,800 kcal including packaging) | 1.8 kg (4 lb) |
| Annual | 660 kg (1,455 lb) |
| Reserve | 90 days: 165 kg (364 lb) |
| Hydroponic supplement | 22 to 43 sq ft (2 to 4 m²) grow area with 0.5 to 1 kW of lighting; fresh greens and herbs only |
| Full food independence | 430 to 540 sq ft (40 to 50 m²) of crops; too large for this habitat |
| Galley (warmer, rehydration station, refrigerator) | ~100 kg (220 lb) |

## Power

| Load | Average draw |
|---|---|
| Life support (air and water) | 2.5 kW |
| Thermal control pumps and fans | 1.0 kW |
| Galley, hygiene and lighting | 1.0 kW |
| Computers and communications | 0.8 kW |
| Hydroponics | 0.7 kW |
| Exercise equipment | 0.3 kW |
| Propulsion and attitude control | 0.5 kW |
| 30% margin | 2.0 kW |
| **Total** | **~9 kW** |

Hardware:

- Solar arrays: ~377 sq ft (35 m²) producing 10 kW at end of life, ~150 kg (330 lb)
- Batteries: 22 kWh to cover a 72-minute eclipse at half depth of discharge, ~150 kg (330 lb)
- Backup: second battery string plus a 3 kW survival mode
- Power distribution and wiring: ~300 kg (660 lb)

## Thermal Control

- Heat to reject: ~9 kW
- Radiator area: ~430 sq ft (40 m²)
- Multilayer insulation: ~1,076 sq ft (100 m²) of exterior coverage
- Radiators, pumps and fluid loops: ~1,000 kg (2,200 lb)

## Gravity and Physical Health

- Exercise: 2 hours per day, 730 hours per year
- Treadmill with harness, cycle and resistance machine with vibration isolation: ~500 kg (1,100 lb)
- Medical kit with ultrasound, defibrillator, 1 year of medications, minor surgery and dental tools: ~100 kg (220 lb)
- Artificial gravity alternative: tether to a counterweight such as a spent rocket stage
  - 1 g at 2 rpm needs a 735 ft (224 m) radius
  - 1 g at 4 rpm needs a 183 ft (56 m) radius

## Waste Management

| Item | Daily | Annual |
|---|---|---|
| Urine (recycled into water loop) | 1.5 L (0.4 gal) | 548 L (145 gal) |
| Feces | 0.15 kg (0.33 lb) | 55 kg (121 lb) |
| Trash and packaging | 0.7 kg (1.5 lb) | 255 kg (562 lb) |
| Toilet consumables (filters, liners, pretreatment) | | 40 kg (88 lb) |
| Clothing (no laundry) | | 70 kg (154 lb) |
| Hygiene supplies | | 40 kg (88 lb) |

- Toilet and waste processing hardware: ~100 kg (220 lb)
- Waste leaves on departing cargo vehicles

## Transportation

- Velocity change from low orbit to geosynchronous orbit: ~2.6 mi/s (4.2 km/s)
- Deorbit burn from geosynchronous orbit: ~0.9 mi/s (1.5 km/s)
- Emergency return capsule (one seat, heat shield, deorbit propellant): ~8,000 kg (17,640 lb), of which ~3,000 kg (6,600 lb) is propellant
- Docking port and adapter: ~500 kg (1,100 lb)
- Annual resupply (food, water, gas, clothing, hygiene, spares, station-keeping propellant): ~2,500 kg (5,510 lb)
- Every 1 kg delivered to geosynchronous orbit needs about 2.6 kg in low orbit using a hydrogen-oxygen transfer stage

## Station Keeping

- North-south correction: ~50 m/s (164 ft/s) per year
- East-west correction: ~2 m/s (7 ft/s) per year
- Propellant for the full ~48,800 kg complex: ~800 kg (1,760 lb) per year chemical or ~160 kg (350 lb) per year electric
- Propulsion system dry mass: ~500 kg (1,100 lb)
- Attitude control (reaction wheels or gyroscopes): ~200 kg (440 lb)

## Debris Protection

- Whipple shield over ~1,076 sq ft (100 m²) of exterior: ~1,500 kg (3,310 lb)
- The water jacket adds a second barrier behind it

## Communications

- 4 ft (1.2 m) dish plus backup antennas: ~150 kg (330 lb)
- Power: 0.8 kW (included in power budget)
- Opposite-hemisphere contact through leased relay capacity on existing geosynchronous satellites
- Round-trip delay: ~0.24 seconds

## Psychological Support

- Solo occupant with no crew contact, so daily video calls with mission control and family
- Storm shelter pod doubles as private sleeping quarters
- One small window: ~100 kg (220 lb), fitted with a water-filled shutter since it creates a gap in the shield
- Recreation items: ~20 kg (44 lb); entertainment is digital

---

## Total Mass Delivered to Geosynchronous Orbit

| System | Mass |
|---|---|
| Pressure hull and structure | 7,000 kg (15,430 lb) |
| Water shield (8 in jacket) | 19,300 kg (42,550 lb) |
| Storm shelter water | 3,700 kg (8,160 lb) |
| Debris shielding | 1,500 kg (3,310 lb) |
| Life support hardware | 1,500 kg (3,310 lb) |
| Air, water and gas reserves | 950 kg (2,090 lb) |
| Power system | 600 kg (1,320 lb) |
| Thermal control | 1,000 kg (2,200 lb) |
| Exercise and medical | 600 kg (1,320 lb) |
| Galley, hygiene and waste systems | 300 kg (660 lb) |
| Propulsion, attitude control and docking | 1,200 kg (2,650 lb) |
| Communications | 150 kg (330 lb) |
| Window and interior outfitting | 500 kg (1,100 lb) |
| Emergency return capsule | 8,000 kg (17,640 lb) |
| First year consumables and spares | 2,500 kg (5,510 lb) |
| **Total** | **~48,800 kg (107,600 lb)** |

- Mass required in low orbit with a hydrogen-oxygen transfer stage: ~127,000 kg (280,000 lb)
- With the 39 in (1 m) water jacket instead: ~164,500 kg (362,700 lb) at geosynchronous orbit
- Water makes up about 47% of the baseline station mass

## Open

- Magic substitutes (mana life support, aurium / orihalcum shielding, star-iron structure) when a beat invents them
- Caldris tech ceiling vs invent-path station
