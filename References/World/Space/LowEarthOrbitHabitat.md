# Living in Low Earth Orbit (250 miles)

Hub: `Space.md`. Orbit layers: `Atmosphere.md`. Higher station: `GeosynchronousHabitat.md`. Launch energy: `OrbitEnergy.md`. Open-air mana at this height: `../Science/Energy/ManaConcentration.md`. World size: `../World.md` (Earth-sized Terra).

Terra-analog of Earth low-orbit living (~ISS altitude). Figures are engineering estimates scaled from Earth ISS data and NASA life-support planning numbers. Magic can replace hardware later; this file is the mundane baseline.

---

# Part 1: Requirements

## Radiation Protection

Much milder than geosynchronous orbit. Terra's magnetic field deflects most charged particles and Terra itself blocks about a third of the sky.

- Moderate hull shielding using water, polyethylene or other hydrogen-rich materials
- Protection during passes through the South Atlantic Anomaly, a dip in the inner Van Allen belt that the station crosses several times a day
- A storm shelter for strong solar particle events, mainly a concern on the high-latitude parts of the orbit
- Space weather monitoring and alerts
- Radiation-tolerant electronics
- Personal dosimeters and career exposure limits for crew

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

- Stored food with moderate reserves, since resupply is frequent and relatively cheap
- Optional hydroponic or aeroponic gardens for fresh produce
- Food preparation and storage systems that work in microgravity

## Power

- Solar arrays sized to run the station and recharge batteries during the sunlit part of each orbit
- Batteries for the shadow portion of every orbit, about 36 minutes out of each 92-minute orbit
- Batteries rated for about 5,800 charge cycles per year
- Backup power systems

## Thermal Control

- Radiators sized for sunlight plus heat reflected and radiated by Terra
- Multilayer insulation to handle 16 hot-cold cycles per day
- Active fluid loops to move heat around the station
- Exterior materials resistant to atomic oxygen, which erodes many plastics and coatings at this altitude

## Gravity and Physical Health

- Daily exercise of about 2 hours on treadmills, bikes and resistance machines to slow bone loss of roughly 1 to 1.5% per month and muscle wasting
- Or a rotating section to create artificial gravity
- Medical bay with diagnostic equipment, medications and surgical supplies
- Telemedicine link through relay satellites

## Waste Management

- Toilets that use airflow instead of gravity
- Solid waste storage, compaction or processing
- Trash loaded on departing cargo ships that burn up on reentry

## Transportation

- Launch vehicles reach this orbit directly from the ground
- Frequent crew and cargo flights
- Docking ports and airlocks
- Emergency return capsule always attached, reentering at about 4.9 miles per second with landing a few hours after undocking

## Orbit Maintenance

- Regular reboosts against atmospheric drag, which would otherwise bring the station down within a few years
- Attitude control using gyroscopes or reaction wheels
- Collision avoidance maneuvers, typically a few per year
- Controlled deorbit at end of life so surviving pieces fall into an unpopulated ocean area

## Debris Protection

- Heavier Whipple shielding, since low orbit has the highest debris density and impacts average about 6 miles per second
- Drag clears small debris within a few years but new debris keeps arriving

## Communications

- Direct ground station contact lasts only about 5 to 10 minutes per pass
- Relay satellites needed for continuous contact

## Psychological Support

- Private quarters
- Regular contact with family and mission control
- Entertainment, recreation and windows (Terra fills about a third of the sky with 16 sunrises and sunsets per day)
- Structured schedules and crew selection for long-duration isolation

---

# Part 2: Estimates for One Person

## Baseline Assumptions

- Mission length: 1 year
- Orbit: 250 miles (400 km) at 51.6° inclination, the same as the Earth ISS
- Habitat: aluminum cylinder 13.1 ft (4 m) in diameter and 16.4 ft (5 m) long inside, about 2,220 cu ft (63 m³) pressurized
- About half the interior is usable living space after equipment
- Water forms a jacket around the entire hull and serves as the radiation shield
- Figures are engineering estimates scaled from Earth ISS data and NASA life support planning numbers

## Radiation Shielding (Water)

### Hull Water Jacket Options

| Jacket thickness | Water mass | Estimated annual dose |
|---|---|---|
| None (thin hull only) | 0 | ~0.4 Sv |
| 4 in (10 cm) | 9,200 kg (20,280 lb) | ~0.25 Sv |
| 8 in (20 cm) | 19,300 kg (42,550 lb) | ~0.2 Sv |
| 20 in (50 cm) | 55,000 kg (121,250 lb) | ~0.15 Sv |

For comparison: Earth ISS crews receive about 0.2 to 0.3 Sv per year. NASA's career limit is 0.6 Sv. Ground-level background is about 0.003 Sv per year.

Roughly half the dose comes from South Atlantic Anomaly passes. Water handles those trapped protons well. Galactic cosmic rays make up most of the rest and resist water shielding, which is why thicker jackets bring diminishing returns.

**Baseline choice for the rest of this file: 4 in (10 cm) jacket**, which matches ISS-level exposure.

### Storm Shelter

- Sleeping pod 3.3 ft (1 m) wide and 6.6 ft (2 m) long inside the habitat
- Extra 6 in (15 cm) water wrap: 1,500 kg (3,310 lb)
- Combined protection inside the pod: about 25 g/cm² of water
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
| Emergency oxygen reserve | | 60 days: 50 kg (110 lb) |
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
| Separate reserve tank | 300 L (79 gal) |
| Recycling hardware | ~400 kg (880 lb) |

The 9,200 kg shield holds about 25 years of makeup water. Makeup should come from the separate reserve tank so the shield stays at full thickness.

## Food

| Item | Amount |
|---|---|
| Daily (about 2,800 kcal including packaging) | 1.8 kg (4 lb) |
| Annual | 660 kg (1,455 lb) |
| Reserve | 60 days: 110 kg (243 lb) |
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

- Solar arrays: ~538 sq ft (50 m²) producing about 18 kW in sunlight, since they must run the station and recharge the batteries in the 56 sunlit minutes of each orbit; ~200 kg (440 lb)
- Batteries: 18 kWh to cover a 36-minute shadow pass at about 30% depth of discharge for long cycle life; ~120 kg (265 lb)
- Backup: second battery string plus a 3 kW survival mode
- Power distribution and wiring: ~300 kg (660 lb)

## Thermal Control

- Heat to reject: ~9 kW plus heat from Terra's reflected sunlight and infrared glow
- Radiator area: ~538 sq ft (50 m²)
- Multilayer insulation: ~1,020 sq ft (95 m²) of exterior coverage with an atomic oxygen resistant outer layer
- Radiators, pumps and fluid loops: ~1,100 kg (2,430 lb)

## Gravity and Physical Health

- Exercise: 2 hours per day, 730 hours per year
- Treadmill with harness, cycle and resistance machine with vibration isolation: ~500 kg (1,100 lb)
- Medical kit with ultrasound, defibrillator, 1 year of medications, minor surgery and dental tools: ~100 kg (220 lb)
- Artificial gravity alternative: tether to a counterweight such as a spent rocket stage
  - 1 g at 2 rpm needs a 735 ft (224 m) radius
  - 1 g at 4 rpm needs a 183 ft (56 m) radius
  - Long tethers add drag and complicate reboosts in low orbit

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
- Waste burns up with departing cargo vehicles

## Transportation

- Velocity change from the ground to this orbit: ~5.8 mi/s (9.4 km/s)
- Deorbit burn for return: ~0.07 mi/s (0.12 km/s)
- Emergency return capsule (one seat, heat shield, deorbit propellant): ~3,500 kg (7,720 lb), of which ~300 kg (660 lb) is propellant
- Typical undocking to landing time: about 3.5 hours
- Docking port and adapter: ~500 kg (1,100 lb)
- Annual resupply (food, water, gas, clothing, hygiene, spares, reboost propellant): ~2,200 kg (4,850 lb)

## Orbit Maintenance

- Reboost to counter drag: ~25 to 60 m/s (82 to 197 ft/s) per year depending on the solar cycle, averaging about 40 m/s (131 ft/s)
- Collision avoidance: a few maneuvers per year at about 1 m/s (3 ft/s) each, included above
- Propellant for the full ~32,600 kg station: ~440 kg (970 lb) per year chemical (range 270 to 650 kg) or ~85 kg (187 lb) per year electric
- Propulsion system dry mass: ~500 kg (1,100 lb)
- Attitude control (reaction wheels or gyroscopes): ~200 kg (440 lb)
- End-of-life controlled deorbit: ~1,300 kg (2,870 lb) of propellant, delivered near retirement and not counted in the total below

## Debris Protection

- Stuffed Whipple shield (aluminum plus Kevlar and Nextel layers) over ~1,020 sq ft (95 m²) of exterior: ~2,500 kg (5,510 lb)
- The water jacket adds a second barrier behind it

## Communications

- Relay terminal and antennas: ~120 kg (265 lb)
- Power: 0.8 kW (included in power budget)
- Continuous contact through relay satellites
- Round-trip delay: under 0.1 seconds through low-orbit relay constellations, about 0.5 seconds through geosynchronous relays

## Psychological Support

- Solo occupant with no crew contact, so daily video calls with mission control and family
- Storm shelter pod doubles as private sleeping quarters
- One small window: ~100 kg (220 lb), fitted with a water-filled shutter since it creates a gap in the shield
- Recreation items: ~20 kg (44 lb); entertainment is digital

---

## Total Mass Delivered to Low Earth Orbit

| System | Mass |
|---|---|
| Pressure hull and structure | 7,000 kg (15,430 lb) |
| Water shield (4 in jacket) | 9,200 kg (20,280 lb) |
| Storm shelter water | 1,500 kg (3,310 lb) |
| Debris shielding | 2,500 kg (5,510 lb) |
| Life support hardware | 1,500 kg (3,310 lb) |
| Air, water and gas reserves | 750 kg (1,650 lb) |
| Power system | 650 kg (1,430 lb) |
| Thermal control | 1,100 kg (2,430 lb) |
| Exercise and medical | 600 kg (1,320 lb) |
| Galley, hygiene and waste systems | 300 kg (660 lb) |
| Propulsion, attitude control and docking | 1,200 kg (2,650 lb) |
| Communications | 120 kg (265 lb) |
| Window and interior outfitting | 500 kg (1,100 lb) |
| Emergency return capsule | 3,500 kg (7,720 lb) |
| First year consumables and spares | 2,200 kg (4,850 lb) |
| **Total** | **~32,600 kg (71,870 lb)** |

- With the 8 in (20 cm) water jacket instead: ~42,700 kg (94,140 lb)
- Water makes up about a third of the baseline station mass

---

## Low Orbit vs Geosynchronous Orbit

| Item | Low orbit (250 mi) | Geosynchronous (22,236 mi) |
|---|---|---|
| Baseline water jacket | 4 in (10 cm) | 8 in (20 cm) |
| Estimated annual dose | ~0.25 Sv | ~0.5 Sv |
| Station mass | ~32,600 kg (71,870 lb) | ~48,800 kg (107,600 lb) |
| Mass that must reach low orbit | ~32,600 kg (71,870 lb) | ~127,000 kg (280,000 lb) |
| Annual orbit-keeping propellant (chemical) | ~440 kg (970 lb) | ~800 kg (1,760 lb) |
| Main orbit-keeping cause | Atmospheric drag | Sun and Moon gravity |
| Battery cycles per year | ~5,800 | ~90 (two eclipse seasons) |
| Return capsule mass | ~3,500 kg (7,720 lb) | ~8,000 kg (17,640 lb) |
| Reentry speed | ~4.9 mi/s | ~6.2 mi/s |
| Debris risk | Highest density; drag clears small pieces | Lower density; nothing decays |
| Signal round trip to Terra | Under 0.1 to about 0.5 seconds via relays | ~0.24 seconds direct |

Deep geosync budget: `GeosynchronousHabitat.md`.

## Open

- Magic substitutes (mana life support, aurium / orihalcum shielding, star-iron structure) when a beat invents them
- Caldris tech ceiling vs invent-path station
