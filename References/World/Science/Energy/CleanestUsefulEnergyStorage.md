# Cleanest Useful Energy Storage

> Earth comparison / design loot. Not locked law. Fantasy flywheel sizes: `FlywheelStorage.md`, `FlywheelApplications.md`. Chemical cells vs mana stones: `Batteries.md`. Air compression: `Compression.md`. Insulation for thermal tanks: `../../Materials/InsulationMaterials.md`.

---

## Quick Comparison

| # | Type | Round-Trip Efficiency | Lifespan | Duration | Core Materials |
|---|------|----------------------|----------|----------|----------------|
| 1 | Flywheel | 85-95% | 20+ years | Seconds to minutes | Steel or carbon fiber |
| 2 | Hydrogen | 30-40% | 20-30 years (equipment) | Days to seasonal | Water, electrolyzer metals |
| 3 | Solar (thermal storage) | ~40% (sun to grid) | 25-30+ years | Hours | Glass, steel, nitrate salts |
| 4 | Wind (paired) | Depends on pairing | 20-30 years | Depends on pairing | Steel, fiberglass, concrete |
| 5 | Pumped hydro | 70-85% | 50-100 years | Hours to days | Water, concrete |
| 6 | Thermal (sand, brick, salt) | 90%+ as heat / 30-40% as power | 20-30+ years | Hours to weeks | Sand, brick, salt |
| 7 | Compressed air (adiabatic) | 60-70% | 30-50 years | Hours to days | Air, rock caverns |
| 8 | Liquid air | 50-60% (up to ~70%) | 30-40 years | Hours to days | Air, steel tanks |
| 9 | Iron-air battery | ~40-50% | 20+ years | ~100 hours | Iron, water, air |
| 10 | Vanadium flow battery | 65-80% | 20-30 years | 4-12 hours | Vanadium electrolyte |
| 11 | Sodium-ion battery | 85-92% | 10-20 years | 1-4 hours | Sodium, carbon, aluminum |
| 12 | LFP lithium battery | 90-95% | 10-20 years | 1-4 hours | Lithium, iron, phosphate |
| 13 | Supercapacitor | 95%+ | 15-20 years | Seconds | Activated carbon |

---

## 1. Flywheel

**How it works:** Electricity drives a motor that spins a heavy rotor up to very high speed. Energy is held as rotational momentum. To discharge, the rotor drives the same motor as a generator and slows down.

**Construction:** Modern rotors are carbon fiber composite or high-strength steel spinning at 10,000-50,000+ RPM. The rotor sits in a vacuum chamber to remove air drag and often floats on magnetic bearings to remove friction. Units are usually buried or housed in reinforced containment in case of rotor failure.

**Performance:**
- Round-trip efficiency: 85-95%
- Cycle life: hundreds of thousands to millions of cycles with almost no degradation
- Response time: milliseconds
- Self-discharge: high, often 5-20% per hour, so it suits short bursts and is poor for long storage

**Environmental profile:** No toxic chemicals, no combustion, no electrolyte to leak or catch fire. Materials are mostly steel, carbon fiber and copper windings. End-of-life recycling is simple for steel units. Carbon fiber is harder to recycle.

**Best uses:**
- Grid frequency regulation (smoothing tiny second-to-second swings)
- Uninterruptible power for data centers, hospitals and factories
- Bridging the gap until backup generators start
- Regenerative braking in rail and motorsport

**Real examples:** Beacon Power runs 20 MW flywheel plants in Stephentown, New York and Hazle Township, Pennsylvania for grid frequency regulation.

**Cost profile:** Expensive per kWh stored. Cheap per kW of instant power delivered.

---

## 2. Hydrogen

**How it works:** Electricity splits water into hydrogen and oxygen through electrolysis. The hydrogen is stored and later converted back to electricity in a fuel cell or a hydrogen-burning turbine. A fuel cell's only exhaust is water.

**Production methods:**
- **PEM electrolyzers:** fast response, good for following variable solar and wind output; use platinum and iridium catalysts
- **Alkaline electrolyzers:** older, cheaper, use nickel; slower to ramp
- **Solid oxide electrolyzers:** high-temperature, most efficient when waste heat is available

**Clean only when green:** "Green" hydrogen uses renewable electricity. "Grey" hydrogen comes from fossil fuel reforming and is not clean. "Blue" captures part of the fossil carbon.

**Storage methods:**
- Compressed gas tanks at 350-700 bar
- Liquid hydrogen at -253°C
- Underground salt caverns (cheapest at large scale)
- Converted to ammonia for shipping

**Performance:**
- Electrolyzer efficiency: 60-80%
- Fuel cell efficiency: 40-60%
- Round-trip efficiency: about 30-40%
- Energy per kilogram: very high at ~33 kWh/kg
- Energy per liter: very low unless compressed or liquefied

**Environmental profile:** Water in, water out. About 9 kg of purified water per kg of hydrogen. Leaked hydrogen indirectly warms the atmosphere by extending methane's lifetime. Turbines burning hydrogen produce some NOx. Fuel cells produce none.

**Best uses:**
- Seasonal storage (summer solar saved for winter)
- Steel making, fertilizer and heavy industry
- Long-haul trucking, shipping and backup power where batteries are too heavy

**Real examples:** The ACES Delta project in Delta, Utah pairs large electrolyzers with salt caverns to store hydrogen for the Intermountain Power plant. Salt cavern hydrogen storage has operated in Teesside, UK since the 1970s and in Texas for decades.

---

## 3. Solar

**Note:** Solar panels generate power. They do not store it. Solar becomes storage in two ways.

### Concentrated Solar Power (CSP) with Molten Salt
**How it works:** Fields of mirrors focus sunlight onto a central tower or along pipes. The heat melts a salt mixture (about 60% sodium nitrate and 40% potassium nitrate). Hot salt at ~565°C sits in an insulated tank. When power is needed it passes through a heat exchanger to make steam that drives a turbine. Cooled salt at ~290°C returns to a second tank.

**Performance:**
- Storage duration: commonly 7-17 hours
- Heat loss: about 1% per day in well-insulated tanks
- Plant lifespan: 25-30+ years

**Environmental profile:** Salts are common fertilizer-grade nitrates. No combustion. Large land footprint. Water use for cooling unless dry-cooled. Concentrated beams can harm birds.

**Real examples:**
- Gemasolar, Spain: 15 hours of storage, one of the first plants to run 24 hours a day
- Cerro Dominador, Chile: 110 MW with 17.5 hours of storage
- Noor Ouarzazate, Morocco: one of the largest CSP complexes in the world

### Photovoltaic (PV) Plus Batteries
The far more common approach today. Standard panels feed a battery bank (usually LFP) on the same site. Panels last 25-30 years and are mostly glass, aluminum and silicon, all recyclable.

---

## 4. Wind

**Note:** Wind turbines generate power. They do not store it. Wind becomes useful storage when paired with another technology.

**Output pattern:** Onshore turbines produce 25-45% of their rated maximum over a year. Offshore turbines reach 40-55%. Output swings with weather and is often strongest at night and in winter.

**Common pairings:**
- **Pumped hydro:** excess night wind pumps water uphill
- **Hydrogen:** surplus wind runs electrolyzers (common in Germany, Denmark and Scotland)
- **Batteries:** smooth hour-to-hour swings
- **Compressed air:** stores surplus in caverns

**Environmental profile:** No emissions during operation. Steel towers and copper are recyclable. Fiberglass blades have been hard to recycle, though newer blades use recyclable resins. Bird and bat impacts exist and are reduced with careful siting and curtailment during migration.

**Real example:** The Gaildorf project in Germany built water reservoirs into the bases of wind turbine towers so the turbines double as the upper reservoir of a pumped hydro system.

---

## 5. Pumped Hydro

**How it works:** Two reservoirs at different heights. Surplus electricity pumps water uphill. When power is needed, water flows downhill through turbines. It is a giant water battery.

**Types:**
- **Open-loop:** connected to a natural river or lake
- **Closed-loop:** two artificial reservoirs with no river connection, lower ecological impact
- **Underground:** uses old mines as the lower reservoir

**Performance:**
- Round-trip efficiency: 70-85%
- Lifespan: 50-100 years, with turbines refurbished along the way
- Response time: seconds to a few minutes
- Duration: typically 6-24 hours, some systems far longer

**Scale:** Holds most of the world's stored grid energy. Single plants reach multiple gigawatts.

**Environmental profile:** Only water and concrete. No chemicals. Main impacts are land flooding, habitat change and construction emissions from concrete. Closed-loop designs avoid most river impacts.

**Real examples:**
- Fengning, China: about 3.6 GW, the largest in the world
- Bath County, Virginia: about 3 GW, the largest in the US
- Dinorwig, Wales: built inside a mountain, reaches full output in about 16 seconds

**Limitation:** Needs specific geography with elevation difference and water access.

---

## 6. Thermal Storage (Sand, Brick, Molten Salt)

**How it works:** Electricity heats a cheap, inert material through resistive heating (like a giant toaster element). The material holds heat in an insulated container for hours to weeks. Heat is pulled back out as hot air, steam or hot water.

**Variants:**
- **Sand batteries:** sand heated to ~500-600°C in a steel silo. Sand is cheap and stable at high temperature.
- **Brick (firebrick) storage:** bricks heated past 1,000°C for industrial process heat. Rondo Energy builds these.
- **Carbon block storage:** Antora Energy heats carbon blocks until they glow and converts the light to electricity with thermophotovoltaic cells.
- **Molten salt:** same as CSP but charged with grid electricity.
- **Ice storage:** freezes water at night to cool buildings during the day.

**Performance:**
- Heat-in to heat-out efficiency: 90%+
- Heat-to-electricity efficiency: 30-40% (much lower)
- Heat loss: a few percent per day or less in large insulated units
- Lifespan: 20-30+ years with almost no material degradation

**Environmental profile:** Among the cleanest options. Sand, brick and salt are abundant and non-toxic. Nothing burns. Nothing wears out chemically.

**Best uses:**
- District heating for towns
- Industrial process heat (food processing, paper, chemicals, cement)
- Replacing fossil boilers

**Real examples:** Polar Night Energy runs commercial sand batteries in Kankaanpää and Pornainen, Finland that heat entire towns through district heating networks.

---

## 7. Compressed Air (Adiabatic)

**How it works:** Surplus electricity runs compressors that pump air into sealed underground caverns or tanks. Compression heats the air. Adiabatic systems capture and store that heat separately. To discharge, the stored heat rewarms the air as it expands through turbines. No fuel is burned.

**Storage locations:**
- Solution-mined salt caverns
- Hard rock caverns
- Depleted aquifers
- Purpose-built pressure vessels at smaller scale

**Hydrostor design:** Uses a water-compensated hard rock cavern. A surface reservoir pushes water into the cavern as air is withdrawn, keeping pressure constant and improving efficiency.

**Performance:**
- Round-trip efficiency: 60-70%
- Lifespan: 30-50 years
- Duration: 4-24+ hours

**Environmental profile:** Uses only air, rock and water. No chemicals. Construction impact comes from excavation and steel. Caverns last indefinitely.

**Real examples:**
- Hydrostor Goderich, Ontario: commercial operation
- Hydrostor Willow Rock, California: planned at 500 MW with 8 hours of storage
- China has built multiple 100-300 MW advanced compressed air plants in salt caverns in Hebei and Hubei provinces

---

## 8. Liquid Air

**How it works:** Surplus electricity cleans and cools air to -196°C, turning it into liquid that takes up about 1/700th of its gas volume. Liquid air sits in insulated low-pressure tanks. To discharge, it is pumped, warmed and expands back to gas at high pressure, spinning a turbine.

**Performance:**
- Round-trip efficiency: 50-60%, up to ~70% when paired with nearby waste heat or cold
- Lifespan: 30-40 years
- Duration: hours to days, scaled by adding more tanks
- Location: works anywhere, needs no special geography

**Environmental profile:** Uses only air. No toxic chemicals, no rare materials. Built from standard industrial components (compressors, turbines, steel tanks) that are fully recyclable.

**Real examples:** Highview Power ran a pilot plant at Pilsworth near Manchester, UK and is building a 50 MW plant with 300 MWh of storage at Carrington, UK.

---

## 9. Iron-Air Battery

**How it works:** The battery reversibly rusts iron. Discharging pulls oxygen from the air into iron pellets, forming rust and releasing electricity. Charging reverses the reaction, turning rust back into iron and releasing oxygen.

**Construction:** Iron pellets, a water-based electrolyte and an air-breathing electrode in large modules about the size of a washing machine, grouped into enclosures.

**Performance:**
- Round-trip efficiency: about 40-50%
- Duration: about 100 hours, far longer than lithium
- Lifespan: 20+ years
- Cost target: around $20 per kWh, a fraction of lithium

**Environmental profile:** Iron is one of the most abundant elements on Earth. Electrolyte is water-based and nonflammable. No lithium, cobalt or nickel. No fire risk.

**Best uses:** Covering multi-day stretches of low wind and cloud cover, which short batteries cannot.

**Real examples:** Form Energy builds these at a factory in Weirton, West Virginia. Early deployments include Great River Energy in Cambridge, Minnesota at 1.5 MW with 150 MWh of storage.

---

## 10. Vanadium Flow Battery

**How it works:** Two large tanks hold liquid electrolyte made of vanadium dissolved in sulfuric acid. Pumps move the liquids past a membrane inside a cell stack where the vanadium changes charge state. Power depends on the size of the stack. Energy depends on the size of the tanks, so they scale independently.

**Performance:**
- Round-trip efficiency: 65-80%
- Cycle life: 15,000-20,000+ cycles
- Lifespan: 20-30 years
- Degradation: electrolyte does not wear out and can be rebalanced and reused indefinitely
- Duration: typically 4-12 hours

**Environmental profile:** Nonflammable. Electrolyte can be leased, recovered and reused in new systems. Vanadium is often recovered as a byproduct of steel slag. Main concerns are the acidic electrolyte and mining in China, Russia and South Africa.

**Other flow chemistries:**
- **Iron flow:** iron, salt and water (ESS Inc.)
- **Zinc-bromine:** cheaper, shorter life
- **Organic flow:** experimental, uses carbon-based molecules

**Real example:** Rongke Power's Dalian, China installation is one of the largest batteries of any kind in the world, with a first phase of 100 MW and 400 MWh.

---

## 11. Sodium-Ion Battery

**How it works:** Same principle as lithium-ion. Sodium ions shuttle between the electrodes in place of lithium.

**Materials:**
- Sodium from common salt or soda ash
- Hard carbon anodes
- Cathodes of layered oxides, Prussian blue analogs or phosphate compounds
- Aluminum current collectors on both sides (lithium needs copper on one side)

**Performance:**
- Round-trip efficiency: 85-92%
- Cycle life: 3,000-10,000 cycles
- Energy density: 100-175 Wh/kg, lower than lithium
- Cold weather: keeps much more capacity below freezing than lithium

**Environmental profile:** No lithium, cobalt or nickel. Sodium is effectively unlimited. Cells can be shipped at zero volts, which is safer for transport. Lower fire risk than most lithium chemistries.

**Best uses:** Stationary grid storage where weight does not matter, budget electric vehicles and cold climates.

**Real examples:** CATL and BYD manufacture sodium-ion cells at scale. Grid-scale sodium-ion installations have been built in China, including a 50 MW plant in Hubei.

---

## 12. Lithium Iron Phosphate (LFP) Battery

**How it works:** Lithium ions move between a graphite anode and a lithium iron phosphate cathode.

**Performance:**
- Round-trip efficiency: 90-95%
- Cycle life: 4,000-10,000 cycles
- Lifespan: 10-20 years
- Duration: typically 1-4 hours
- Response: milliseconds

**Environmental profile:**
- No cobalt or nickel, removing the worst mining concerns of other lithium batteries
- Much more resistant to thermal runaway and fire than nickel-based lithium batteries
- Lithium extraction uses large amounts of water in brine operations in Chile and Argentina and open-pit mining in Australia
- Recycling is growing through companies like Redwood Materials

**Best uses:** Daily solar shifting, peak demand, frequency response, home batteries and most current grid battery projects.

**Real examples:** Tesla Megapack and most large grid batteries built in California, Texas and Australia use LFP.

---

## 13. Supercapacitor

**How it works:** Stores energy as an electric field rather than a chemical reaction. Charge collects on the surface of porous activated carbon electrodes separated by a thin electrolyte layer.

**Performance:**
- Round-trip efficiency: 95%+
- Cycle life: 1,000,000+ cycles
- Charge and discharge time: seconds
- Energy density: very low at 5-10 Wh/kg
- Self-discharge: high, loses charge over days

**Environmental profile:** Mostly carbon and aluminum. No heavy metals. Extremely long life means very little waste. Some electrolytes are flammable organic solvents. Water-based versions avoid that.

**Best uses:**
- Regenerative braking in buses, trams, trains and elevators
- Port cranes
- Wind turbine blade pitch control
- Smoothing power spikes alongside batteries

**Real example:** Shanghai has run supercapacitor buses that fully recharge in seconds at each stop.

---

## Cleanest Overall

**Flywheels, pumped hydro and thermal storage.** They use only steel, water or sand. Nothing burns. Nothing toxic is involved. They last decades with almost no degradation.

**Best for long duration:** pumped hydro, green hydrogen, iron-air and compressed air.

**Best for daily cycling:** LFP, sodium-ion and vanadium flow.

**Best for instant response:** flywheels and supercapacitors.
