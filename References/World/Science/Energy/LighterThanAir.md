# Lighter Than Air: Hot Air, Helium, Hydrogen, Vacuum Shells, Tethers and Assisted Ascent

> Earth invent loot. Compiled October 2026. Computed tables from first-principles physics. Baseline air: 26 C, 1015 hPa, density 1.182 kg/m3 (warm sea-level). Prices are approximate 2020s ranges. Not locked law.
>
> Hover / actuator disk: `Flight.md`. Beach / ridge winds: `../../Geography/VolcanicIsland/HawaiianWindsBeachGlider.md`. Perfect glider: `../Vehicle/PerfectGlider/Index.md`. H2 film barriers: `../../Materials/PermeationBarriers.md`. Helium sources: `Optics.md`. Hover bike wishlist: `../../../People/Roland/Goals.md`.

---

## Contents

1. Constants and assumptions
2. Buoyancy fundamentals
3. Lifting media compared
4. Hot air balloons in depth
5. Helium in depth
6. Hydrogen in depth
7. Other lifting gases
8. How much volume a 100 kg person needs
9. The square-cube law and minimum balloon size
10. Toy balloons, weather balloons and cluster ballooning
11. Altitude, expansion and ascent rate
12. Balloon architectures: zero pressure, superpressure, Roziere, hybrid
13. Vacuum lifting bodies
14. Tethers: materials, mass and maximum height
15. Tethered balloons in wind
16. Aerostat shapes and tether systems in service
17. Pre-established ascent systems
18. Buoyancy-assisted climbing
19. Energy cost of altitude
20. Comparison of ascent methods
21. Weather limits for balloon operations
22. Regulations (United States)
23. History timeline
24. Records
25. Formula sheet
26. Unit conversions

---

## 1. Constants and assumptions

| Quantity | Value |
|---|---|
| Universal gas constant R | 8.314462 J/(mol K) |
| Molar mass of dry air | 28.965 g/mol |
| Standard gravity | 9.80665 m/s2 |
| Baseline air density | 1.182 kg/m3 (26 C, 1015 hPa) |
| ISA sea-level air density | 1.225 kg/m3 (15 C, 1013.25 hPa) |
| Propane lower heating value | 46.35 MJ/kg |
| Liquid propane density | about 0.51 kg/L |
| Default human mass | 100 kg |

---

## 2. Buoyancy fundamentals

**Archimedes' principle:** a body immersed in a fluid is pushed up by a force equal to the weight of the fluid it displaces.

**Gross lift** = Volume x (air density minus gas density)

**Net (useful) lift** = Gross lift minus envelope, structure, equipment and gas containment mass

**Free lift** = Net lift minus payload. Positive free lift makes the balloon rise. Zero free lift means equilibrium (floating level). Negative free lift means descent.

**Ideal gas law:** density = p M / (R T). At equal pressure and temperature, density is proportional to molar mass. Air at 29 g/mol is about 14.4 times denser than hydrogen (2 g/mol) and about 7.2 times denser than helium (4 g/mol).

**Why hydrogen is only 8% better than helium despite being half the density:** lift depends on the difference between air density and gas density. Air 1.18, helium 0.16, hydrogen 0.08 kg/m3. The differences are 1.02 vs 1.10, a gap of only about 8%.

**Hot air** uses the same air molecules made less dense by heating. Density scales with 1/T in kelvin. Air at 100 C is about 20% less dense than air at 26 C, so hot air lifts only about a quarter as much per cubic meter as helium.

---

## 3. Lifting media compared

| Lifting medium | Molar mass (g/mol) | Density at 26 C, 1015 hPa (kg/m3) | Gross lift (kg per m3) | Lift vs hydrogen | m3 to lift 100 kg (gas only) | Hazard | Cost character (USD) |
|---|---|---|---|---|---|---|---|
| Hydrogen H2 | 2.016 | 0.0823 | 1.100 | 100% | 91 | Extremely flammable, 4 to 75% in air | Low, about 0.2 to 0.6 per m3 from electrolysis or reforming |
| Helium He | 4.003 | 0.1634 | 1.019 | 93% | 98 | Inert, nonflammable | High and volatile, roughly 10 to 40+ per m3 retail balloon grade |
| Methane CH4 (natural gas) | 16.04 | 0.6546 | 0.527 | 48% | 190 | Flammable, 5 to 15% in air | Very low |
| Ammonia NH3 | 17.03 | 0.6950 | 0.487 | 44% | 205 | Toxic, flammable 15 to 28% | Low |
| Neon Ne | 20.18 | 0.8235 | 0.358 | 33% | 279 | Inert | Very high |
| Coal gas / town gas (historic) | 11.0 | 0.4489 | 0.733 | 67% | 136 | Flammable, toxic CO | Historic, cheap in 1800s |
| Water vapor (100 C steam) | 18.015 | 0.5894 | 0.593 | 54% | 169 | Nonflammable, condenses | Fuel cost only |
| Nitrogen N2 (reference) | 28.013 | 1.1431 | 0.039 | 4% | 2574 | Inert | Low |
| Hot air, envelope 60 C above 26 C ambient | 28.97 | 0.9845 | 0.197 | 18% | 506 | Propane burner fire risk | Propane, roughly 20 to 50 kg per hour |
| Hot air, envelope 80 C above 26 C ambient | 28.97 | 0.9326 | 0.249 | 23% | 401 | Propane burner fire risk | Propane, roughly 20 to 50 kg per hour |
| Hot air, envelope 100 C above 26 C ambient | 28.97 | 0.8859 | 0.296 | 27% | 338 | Propane burner fire risk | Propane, roughly 20 to 50 kg per hour |
| Perfect vacuum | 0 | 0.0000 | 1.182 | 107% | 85 | Implosion and buckling | Structural, see section 9 |

### 3.1 Key safety and handling data

| Property | Hydrogen | Helium | Methane | Hot air |
|---|---|---|---|---|
| Flammable range in air (% by volume) | 4 to 75 | None | 5 to 15 | Not applicable (fuel is propane: 2.1 to 9.5) |
| Minimum ignition energy | 0.017 mJ | None | 0.28 mJ | Propane 0.25 mJ |
| Autoignition temperature | about 585 C | None | about 540 C | Propane about 470 C |
| Diffusion coefficient in air | 0.61 cm2/s (very fast dispersal) | 0.69 cm2/s | 0.16 cm2/s | n/a |
| Flame visibility | Nearly invisible in daylight | n/a | Blue | Propane flame visible |
| Permeation through films | Very high | Very high (smallest atom) | Low | n/a |
| Asphyxiation risk | Yes in enclosed spaces | Yes in enclosed spaces | Yes | No |
| Detonation range | about 18 to 59% | None | 6 to 14% | n/a |
| Embrittles metals | Yes (hydrogen embrittlement of steels) | No | No | No |

---

## 4. Hot air balloons in depth

### 4.1 Lift per cubic meter vs ambient and envelope temperature (kg/m3)

| Ambient (C) | Air density (kg/m3) | Envelope 70 C | 80 C | 90 C | 100 C | 110 C | 120 C (max continuous) |
|---|---|---|---|---|---|---|---|
| 0 | 1.295 | 0.264 | 0.293 | 0.321 | 0.347 | 0.372 | 0.395 |
| 10 | 1.249 | 0.218 | 0.248 | 0.275 | 0.301 | 0.326 | 0.349 |
| 15 | 1.227 | 0.197 | 0.226 | 0.253 | 0.280 | 0.304 | 0.328 |
| 20 | 1.206 | 0.176 | 0.205 | 0.233 | 0.259 | 0.283 | 0.307 |
| 26 | 1.182 | 0.152 | 0.181 | 0.208 | 0.234 | 0.259 | 0.283 |
| 32 | 1.159 | 0.128 | 0.157 | 0.185 | 0.211 | 0.236 | 0.259 |
| 38 | 1.136 | 0.106 | 0.135 | 0.163 | 0.189 | 0.214 | 0.237 |

Cold days give dramatically more lift. A balloon that struggles to lift 3 people at 32 C ambient lifts 4 comfortably at 0 C. This is a major reason balloonists fly at dawn: the air is coolest, thermals have not started and winds are lightest.

### 4.2 Envelope temperature limits

| Item | Value |
|---|---|
| Typical cruise envelope temperature | 80 to 100 C |
| Maximum continuous for nylon fabric | about 120 C |
| Temperature telltale (fusible link) melt point | commonly about 127 C (250 F) |
| Nylon fabric strength loss | Accelerates above 120 C; fabric degrades cumulatively with hours at heat and UV |
| Polyester fabric | Somewhat better heat tolerance than nylon |
| Nomex scoop / skirt | Withstands direct flame contact near the burner |
| Envelope life | Roughly 400 to 800 flight hours depending on fabric, heat and sunlight |

### 4.3 FAI size classes and lift

| FAI class | Volume (m3) | Max volume (ft3) | Equivalent sphere diameter (m) | Gross lift at 100 C, 15 C day (kg) | Gross lift at 100 C, 26 C day (kg) |
|---|---|---|---|---|---|
| AX-1 | 0 to 250 | 8,829 | 7.8 | 70 | 59 |
| AX-2 | 250 to 400 | 14,126 | 9.1 | 112 | 94 |
| AX-3 | 400 to 600 | 21,189 | 10.5 | 167 | 141 |
| AX-4 | 600 to 900 | 31,783 | 12.0 | 251 | 211 |
| AX-5 | 900 to 1,200 | 42,378 | 13.2 | 335 | 281 |
| AX-6 | 1,200 to 1,600 | 56,504 | 14.5 | 446 | 375 |
| AX-7 | 1,600 to 2,200 | 77,692 | 16.1 | 614 | 516 |
| AX-8 | 2,200 to 3,000 | 105,944 | 17.9 | 837 | 703 |
| AX-9 | 3,000 to 4,000 | 141,259 | 19.7 | 1,116 | 938 |
| AX-10 | 4,000 to 6,000 | 211,888 | 22.5 | 1,674 | 1,406 |

A typical sport balloon is AX-7 (about 2,200 m3, 77,000 ft3), carrying 2 to 4 people. Commercial ride balloons run AX-10 and larger (up to 10,000+ m3, 12 to 32 passengers).

### 4.4 Anatomy

| Component | Material / typical spec | Function |
|---|---|---|
| Envelope gores | Ripstop nylon or polyester, 50 to 70 g/m2, silicone or polyurethane coated | Holds hot air |
| Load tapes | Polyester webbing running vertically and horizontally | Carry the load from crown to basket; the fabric itself carries little load |
| Crown ring | Aluminum | Top anchor for vertical tapes |
| Parachute valve | Fabric disk sealing a crown opening, held by hot air pressure | Pull to vent heat for descent, full release for deflation |
| Turning vents | Side slits | Rotate the balloon (does not steer it) |
| Scoop / skirt | Nomex | Shields lower envelope, guides burner flame |
| Burner | Stainless coils, 2 to 4 units, each about 3 to 8 MW peak | Liquid propane vaporizes in coils, burns with roaring flame |
| Whisper burner (cow burner) | Liquid fire with less noise | Quiet flight over livestock |
| Fuel tanks | Aluminum or stainless, 40 to 80 L each | Liquid propane, often nitrogen-pressurized in cold weather |
| Basket | Woven wicker or rattan on a steel or aluminum floor frame, leather trim | Flexes on landing, absorbs shock |
| Instruments | Variometer, altimeter, envelope temperature, GPS, radio | Flight control |

### 4.5 Heat loss and fuel burn (estimate, 80 C temperature rise, average convection plus radiation coefficient about 6 W/m2K)

| Envelope (m3) | Surface area (m2, 8% over sphere) | Avg heat loss at 80 C rise (kW) | Propane burn (kg/h) | Liters/h | US gal/h |
|---|---|---|---|---|---|
| 900 | 487 | 234 | 18 | 36 | 9 |
| 1,200 | 590 | 283 | 22 | 43 | 11 |
| 1,600 | 714 | 343 | 27 | 52 | 14 |
| 2,200 | 883 | 424 | 33 | 65 | 17 |
| 3,000 | 1,086 | 521 | 41 | 79 | 21 |
| 4,000 | 1,316 | 632 | 49 | 96 | 25 |
| 6,000 | 1,725 | 828 | 64 | 126 | 33 |
| 10,000 | 2,424 | 1,164 | 90 | 177 | 47 |

Real-world burn for an AX-7 is commonly 15 to 25 US gallons per hour depending on load, temperature and how much altitude changing the pilot does. Fuel loads of 40 to 60 gallons give 1.5 to 3 hours of flight. Peak burner output (several megawatts) far exceeds average heat loss: the burner fires in short bursts.

### 4.6 Flight control

| Action | Effect | Time lag |
|---|---|---|
| Burn | Heats air, increases lift | 15 to 30 seconds before response felt |
| Stop burning | Air cools, lift slowly decreases | Gradual |
| Open parachute valve | Dumps hot air, rapid descent | Immediate |
| Change altitude | Different wind direction and speed at different heights | Only way to "steer" |
| Rip-out at landing | Full deflation in high wind | Seconds |

Steering by altitude works because wind direction changes with height (Ekman spiral, sea breezes, valley flows, inversions). Skilled pilots in calm morning conditions can return close to the launch point using layered winds (the "Albuquerque box" at the Albuquerque International Balloon Fiesta is the classic case).

---

## 5. Helium in depth

| Topic | Data |
|---|---|
| Source | Radioactive alpha decay of uranium and thorium in rock; collects in natural gas deposits |
| Concentration in natural gas | Typically trace to about 7%; above 0.3% can be economic to extract |
| Extraction | Cryogenic separation from natural gas, then purification |
| Major producers | United States, Qatar, Algeria, Russia, Australia, Canada, Tanzania exploration |
| Atmospheric concentration | 5.2 ppm; escapes to space, effectively non-renewable on human timescales |
| Grades | Balloon grade about 95 to 99%; industrial 99.995%; research 99.9999% |
| Liquid helium boiling point | 4.2 K (minus 269 C) |
| Biggest uses | MRI magnets, semiconductors, fiber optics, welding, leak detection, rocketry purge, lifting gas |
| Cost behavior | Repeated shortages since 2006 caused large price spikes; sale of the US Federal Helium Reserve was completed in 2024 |
| Permeation | Leaks through latex in hours (party balloons last about 8 to 20 hours); foil (metallized nylon) balloons last days to weeks; laminated aerostat fabrics lose a few percent per month |
| Purity effect | Each 1% of air contamination cuts lift about 1.1% |
| Superheat | Sunlight heats helium 5 to 20+ C above ambient, adding several percent lift; at night it cools and lift drops (reason for ballast on long flights) |

---

## 6. Hydrogen in depth

| Topic | Data |
|---|---|
| Lift advantage over helium | About 8% more lift per volume |
| Production | Steam methane reforming (cheapest, CO2 emitting), water electrolysis (about 50 to 55 kWh per kg H2), chemical generators (aluminum or iron with acid or hydroxide, historically used in the field) |
| Volume per kg at 26 C | about 12.2 m3 per kg |
| Electrolysis energy per m3 | about 4.3 to 4.5 kWh per m3 |
| Field generation historically | Civil War balloons used iron filings and sulfuric acid wagons; WWI and WWII barrage balloons used compressed cylinders |
| Current use as lifting gas | National Weather Service and many weather services still fill radiosonde balloons with hydrogen at many sites because of cost |
| Hindenburg (1937) | 200,000 m3 hydrogen, 245 m long; fire at Lakehurst killed 36 of 97 aboard; doped fabric skin and hydrogen both burned |
| Safety mitigations used today | Generation on demand, no enclosed accumulation (it rises and disperses fast), static grounding, spark-free tools, inert cells, ventilation |
| Embrittlement | Steel fittings under high-pressure hydrogen lose ductility; aluminum and austenitic stainless are preferred |

---

## 7. Other lifting gases

| Gas | Lift (kg/m3, approx.) | Notes |
|---|---|---|
| Hot steam | about 0.58 at 100 C | Lifts well while hot, condenses into water as it cools; proposed for some airship designs with heated envelopes |
| Methane | about 0.52 | Half the lift of helium, flammable but less volatile than hydrogen, greenhouse gas |
| Ammonia | about 0.48 | Toxic; used in some 1800s and early 1900s experiments; easy to compress to liquid for variable buoyancy |
| Coal gas | about 0.65 | Standard lifting gas for 1800s balloons after hydrogen; produced by town gasworks |
| Neon | about 0.35 | Inert, very expensive |
| Hot hydrogen / hot helium (Roziere) | Gas lift plus heat lift | Long-duration balloons |

---

## 8. How much volume a 100 kg person needs

### 8.1 Volume for gross loads (sphere diameter in parentheses)

| Medium | Lift (kg/m3) | 100 kg | 150 kg | 250 kg | 400 kg | 600 kg | 1000 kg | 2000 kg |
|---|---|---|---|---|---|---|---|---|
| Hydrogen | 1.100 | 91 m3 (5.6 m) | 136 m3 (6.4 m) | 227 m3 (7.6 m) | 364 m3 (8.9 m) | 546 m3 (10.1 m) | 909 m3 (12.0 m) | 1,819 m3 (15.1 m) |
| Helium (pure) | 1.019 | 98 m3 (5.7 m) | 147 m3 (6.6 m) | 245 m3 (7.8 m) | 393 m3 (9.1 m) | 589 m3 (10.4 m) | 982 m3 (12.3 m) | 1,963 m3 (15.5 m) |
| Helium (95% purity, typical) | 0.968 | 103 m3 (5.8 m) | 155 m3 (6.7 m) | 258 m3 (7.9 m) | 413 m3 (9.2 m) | 620 m3 (10.6 m) | 1,033 m3 (12.5 m) | 2,067 m3 (15.8 m) |
| Hot air, 100 C envelope | 0.234 | 427 m3 (9.3 m) | 640 m3 (10.7 m) | 1,067 m3 (12.7 m) | 1,706 m3 (14.8 m) | 2,560 m3 (17.0 m) | 4,266 m3 (20.1 m) | 8,532 m3 (25.4 m) |
| Hot air, 120 C envelope | 0.283 | 354 m3 (8.8 m) | 531 m3 (10.0 m) | 885 m3 (11.9 m) | 1,415 m3 (13.9 m) | 2,123 m3 (15.9 m) | 3,538 m3 (18.9 m) | 7,077 m3 (23.8 m) |
| Vacuum (ideal, massless shell) | 1.182 | 85 m3 (5.4 m) | 127 m3 (6.2 m) | 212 m3 (7.4 m) | 338 m3 (8.6 m) | 508 m3 (9.9 m) | 846 m3 (11.7 m) | 1,692 m3 (14.8 m) |

### 8.2 Minimum single-person balloon

Payload assumptions: 100 kg pilot plus 15 kg seat and harness, plus 15 kg ballast for gas balloons or 55 kg of burner, single tank and fuel for hot air. Envelope fabric 60 to 65 g/m2, 10% extra area for seams and shape.

| Medium | Payload: pilot + seat/harness + equipment (kg) | Volume for equilibrium (m3) | Sphere dia. (m) | Envelope mass (kg) | Gross lift (kg) |
|---|---|---|---|---|---|
| Hydrogen | 130 | 125 | 6.2 | 8 | 138 |
| Helium | 130 | 136 | 6.4 | 8 | 138 |
| Hot air 100 C | 170 | 858 | 11.8 | 31 | 201 |
| Hot air 120 C | 170 | 698 | 11.0 | 27 | 197 |

A "cloudhopper" (single-seat hot air balloon with the pilot in a harness under the burner) typically runs 600 to 1,000 m3, matching these numbers. A single-person gas balloon is a very small object: a helium sphere just over 6 m across can float a 100 kg person.

---

## 9. The square-cube law and minimum balloon size

Volume and lift grow with diameter cubed. Envelope area and mass grow only with diameter squared. Small balloons are mostly skin. Large balloons are mostly lift.

| Sphere diameter (m) | Volume (m3) | Surface (m2) | He gross lift (kg) | Envelope 60 g/m2 (kg) | He net lift (kg) | Hot air 100 C gross (kg) | Envelope 65 g/m2 (kg) | Hot air net (kg, before burner/basket) |
|---|---|---|---|---|---|---|---|---|
| 0.3 | 0.01 | 0.3 | 0.0 | 0.0 | -0.0 | 0.0 | 0.0 | -0.0 |
| 0.5 | 0.07 | 0.8 | 0.1 | 0.0 | 0.0 | 0.0 | 0.1 | -0.0 |
| 1 | 0.52 | 3.1 | 0.5 | 0.2 | 0.3 | 0.1 | 0.2 | -0.1 |
| 2 | 4.19 | 12.6 | 4.3 | 0.8 | 3.5 | 1.0 | 0.8 | 0.2 |
| 3 | 14.14 | 28.3 | 14.4 | 1.7 | 12.7 | 3.3 | 1.8 | 1.5 |
| 4 | 33.51 | 50.3 | 34.1 | 3.0 | 31.1 | 7.9 | 3.3 | 4.6 |
| 5 | 65.45 | 78.5 | 66.7 | 4.7 | 62.0 | 15.3 | 5.1 | 10.2 |
| 6 | 113.10 | 113.1 | 115.2 | 6.8 | 108.4 | 26.5 | 7.4 | 19.2 |
| 8 | 268.08 | 201.1 | 273.1 | 12.1 | 261.0 | 62.8 | 13.1 | 49.8 |
| 10 | 523.60 | 314.2 | 533.4 | 18.8 | 514.5 | 122.7 | 20.4 | 102.3 |
| 12 | 904.78 | 452.4 | 921.6 | 27.1 | 894.5 | 212.1 | 29.4 | 182.7 |
| 15 | 1,767.15 | 706.9 | 1,800.1 | 42.4 | 1,757.7 | 414.2 | 45.9 | 368.3 |
| 18 | 3,053.63 | 1,017.9 | 3,110.6 | 61.1 | 3,049.5 | 715.8 | 66.2 | 649.6 |
| 20 | 4,188.79 | 1,256.6 | 4,266.9 | 75.4 | 4,191.5 | 981.9 | 81.7 | 900.2 |
| 25 | 8,181.23 | 1,963.5 | 8,333.8 | 117.8 | 8,215.9 | 1,917.7 | 127.6 | 1,790.1 |
| 30 | 14,137.17 | 2,827.4 | 14,400.7 | 169.6 | 14,231.1 | 3,313.8 | 183.8 | 3,130.0 |

Net lift crosses zero at a diameter where gross lift equals envelope mass. For 60 g/m2 film that is about 0.35 m for helium. Mylar and polyethylene films at 10 to 25 g/m2 shrink that further. Hot air balloons need about 4 times the volume of helium for the same lift, so they must be much larger for the same payload.

---

## 10. Toy balloons, weather balloons and cluster ballooning

| Balloon | Volume (liters) | He gross lift (g) | Rubber mass (g) | Net lift (g) | Count to float 100 kg | Total helium (m3) |
|---|---|---|---|---|---|---|
| 11 in party balloon | 11.5 | 11.7 | 3.0 | 8.7 | 11,483 | 132 |
| 16 in | 33.5 | 34.1 | 6.0 | 28.1 | 3,554 | 119 |
| 36 in giant | 394.6 | 401.9 | 40.0 | 361.9 | 276 | 109 |
| 1.8 m (6 ft) weather balloon | 3,053.6 | 3,110.6 | 600.0 | 2,510.6 | 40 | 122 |
| 3 m (10 ft) weather balloon, about 1,500 g | 14,137.2 | 14,400.7 | 1500.0 | 12,900.7 | 8 | 110 |

Larry Walters (1982) lifted off from San Pedro, California in a lawn chair carrying 45 helium weather balloons, rising to about 4,900 m (16,000 ft) and drifting into controlled airspace near Long Beach airport. Modern cluster balloonists (such as Jonathan Trappe, who crossed the English Channel in 2010) use dozens to hundreds of large latex balloons with ballast and cutaways for altitude control.

---

## 11. Altitude, expansion and ascent rate

### 11.1 Standard atmosphere and lift with altitude

| Altitude (m) | ft | ISA temp (C) | Pressure (hPa) | Air density (kg/m3) | Density vs sea level | Zero-pressure balloon expansion factor | He lift (kg/m3, same T) | Hot air lift, 80 C above ambient (kg/m3) |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 15.0 | 1013.2 | 1.2250 | 100.0% | 1.00 | 1.0557 | 0.266 |
| 500 | 1,640 | 11.8 | 954.6 | 1.1672 | 95.3% | 1.05 | 1.0059 | 0.256 |
| 1,000 | 3,281 | 8.5 | 898.7 | 1.1116 | 90.7% | 1.10 | 0.9580 | 0.246 |
| 1,500 | 4,921 | 5.2 | 845.6 | 1.0581 | 86.4% | 1.16 | 0.9118 | 0.236 |
| 2,000 | 6,562 | 2.0 | 795.0 | 1.0065 | 82.2% | 1.22 | 0.8674 | 0.227 |
| 3,000 | 9,843 | -4.5 | 701.1 | 0.9091 | 74.2% | 1.35 | 0.7835 | 0.209 |
| 4,000 | 13,123 | -11.0 | 616.4 | 0.8191 | 66.9% | 1.50 | 0.7059 | 0.192 |
| 5,000 | 16,404 | -17.5 | 540.2 | 0.7361 | 60.1% | 1.66 | 0.6344 | 0.175 |
| 6,000 | 19,685 | -24.0 | 471.8 | 0.6597 | 53.9% | 1.86 | 0.5685 | 0.160 |
| 8,000 | 26,247 | -37.0 | 356.0 | 0.5252 | 42.9% | 2.33 | 0.4526 | 0.133 |
| 10,000 | 32,808 | -50.0 | 264.4 | 0.4127 | 33.7% | 2.97 | 0.3557 | 0.109 |
| 12,000 | 39,370 | -56.5 | 193.3 | 0.3108 | 25.4% | 3.94 | 0.2679 | 0.084 |
| 15,000 | 49,213 | -56.5 | 120.4 | 0.1937 | 15.8% | 6.33 | 0.1669 | 0.052 |
| 20,000 | 65,617 | -56.5 | 54.7 | 0.0880 | 7.2% | 13.91 | 0.0759 | 0.024 |
| 25,000 | 82,021 | -51.5 | 25.1 | 0.0395 | 3.2% | 31.04 | 0.0340 | 0.010 |
| 30,000 | 98,425 | -46.5 | 11.7 | 0.0180 | 1.5% | 68.01 | 0.0155 | 0.005 |
| 35,000 | 114,829 | -36.1 | 5.6 | 0.0082 | 0.7% | 149.14 | 0.0071 | 0.002 |
| 40,000 | 131,234 | -22.1 | 2.8 | 0.0039 | 0.3% | 318.09 | 0.0033 | 0.001 |
| 45,000 | 147,638 | -8.1 | 1.4 | 0.0019 | 0.2% | 651.13 | 0.0016 | 0.000 |

A sealed balloon that is full at the ground bursts or vents as it rises. A zero-pressure balloon launched partly full grows as it climbs: a balloon reaching 30 km must expand about 67 times from its sea-level gas volume (about 145 times at 35 km). High-altitude science balloons look like limp, half-empty sheets at launch for this reason.

### 11.2 Ascent rate of a gas balloon

Steady ascent velocity v = sqrt(2 F_free / (rho Cd A)). Drag coefficient of a balloon about 0.3. Free lift given as a fraction of gross lift.

| Balloon dia. (m) | Volume (m3) | Free lift 5% of gross: ascent (m/s) | 10% | 20% | 30% |
|---|---|---|---|---|---|
| 1.8 | 3.1 | 1.8 | 2.6 | 3.7 | 4.5 |
| 3 | 14.1 | 2.4 | 3.4 | 4.7 | 5.8 |
| 6 | 113.1 | 3.4 | 4.7 | 6.7 | 8.2 |
| 10 | 523.6 | 4.3 | 6.1 | 8.7 | 10.6 |
| 20 | 4,188.8 | 6.1 | 8.7 | 12.3 | 15.0 |

Weather balloons ascend about 5 m/s and burst between 25 and 35 km after roughly 90 to 120 minutes.

### 11.3 Altitude control

| Method | Effect | Balloon type |
|---|---|---|
| Drop ballast (sand, water, steel shot) | Rise | Gas balloons |
| Vent gas | Descend (gas is lost permanently) | Gas balloons |
| Burn | Rise | Hot air |
| Vent hot air | Descend | Hot air |
| Pump air into an internal ballonet | Descend (heavier) | Superpressure balloons, airships |
| Compress lifting gas into tanks | Descend, reversible | Experimental variable-buoyancy airships |
| Aerodynamic lift (fins, shape) | Up or down with airspeed | Airships, hybrid aerostats |
| Solar heating / night cooling | Daily altitude cycle | Unpressurized gas balloons |

---

## 12. Balloon architectures

| Type | Principle | Advantages | Drawbacks | Example |
|---|---|---|---|---|
| Hot air (Montgolfiere) | Heated air | Cheap fuel, reusable, simple | Low lift per volume, fuel-limited endurance | Sport and ride balloons |
| Zero-pressure gas (Charliere) | Gas open to atmosphere at bottom duct | Simple, reaches very high altitudes | Loses gas each day-night cycle, needs ballast | NASA science balloons, gas ballooning races |
| Superpressure | Sealed, stiff envelope holds gas above ambient pressure | Constant altitude for weeks to months | Envelope must resist large pressure differential | NASA superpressure flights, Google Loon (100+ day flights) |
| Roziere (hybrid) | Gas cell above a hot-air cone | Combines gas efficiency with hot-air altitude control | Complex, fire risk if hydrogen | Breitling Orbiter 3, Spirit of Freedom (around the world) |
| Solar balloon | Black envelope heated by sunlight | No fuel | Daytime only, weather-dependent | Hobby and research flights |
| Tethered aerostat | Gas balloon on a cable | Persistent fixed station | Wind blowdown, tether weight | TARS, Aerophile rides |
| Airship (rigid, semi-rigid, blimp) | Gas envelope plus engines | Steerable | Cost, ground handling | Zeppelin NT, Goodyear blimps |
| Hybrid airship | Gas lift plus lifting-body aerodynamics | Heavier than air on ground, easier handling | Needs airspeed for full lift | Airlander 10 |

---

## 13. Vacuum lifting bodies

### 13.1 The idea

Removing all gas from a rigid shell gives the maximum possible buoyancy: 1.182 kg per m3 at sea level, about 7% more than hydrogen. Francesco Lana de Terzi proposed a "flying ship" lifted by four evacuated copper spheres in 1670. The problem: the full weight of the atmosphere (101,325 Pa, about 10.3 tonnes per square meter) presses on the shell with nothing inside pushing back.

### 13.2 Physics of the problem

- **Buckling, not crushing, is the limit.** A thin spherical shell fails by snapping inward long before the material reaches its crushing strength.
- **Classical buckling pressure of a sphere:** p_cr = 2 E (t/R)^2 / sqrt(3 (1 - nu^2)).
- **Real shells buckle at 20 to 30% of the classical value** because of small imperfections (knockdown factor).
- **Shell mass to lift ratio:** mass/lift = 3 (rho_shell / rho_air) (t/R). Setting t/R from buckling gives a ratio independent of size. Making the sphere bigger does not help a monocoque shell.

### 13.3 Monocoque spherical shells (sea level)

| Material | Buckling case | E (GPa) | Density (kg/m3) | Required t/R (x1000) | Shell mass / buoyant lift | Membrane stress (MPa) | Material strength (MPa) | Floats? |
|---|---|---|---|---|---|---|---|---|
| Steel (high strength) | ideal | 200 | 7850 | 0.65 | 12.92 | 78 | 1500 | No |
| Steel (high strength) | real knockdown 0.25 | 200 | 7850 | 1.30 | 25.84 | 39 | 1500 | No |
| Aluminum 7075 | ideal | 72 | 2810 | 1.08 | 7.67 | 47 | 500 | No |
| Aluminum 7075 | real knockdown 0.25 | 72 | 2810 | 2.15 | 15.34 | 24 | 500 | No |
| Titanium Ti-6Al-4V | ideal | 114 | 4430 | 0.85 | 9.57 | 60 | 880 | No |
| Titanium Ti-6Al-4V | real knockdown 0.25 | 114 | 4430 | 1.70 | 19.15 | 30 | 880 | No |
| Magnesium alloy | ideal | 45 | 1800 | 1.35 | 6.18 | 38 | 250 | No |
| Magnesium alloy | real knockdown 0.25 | 45 | 1800 | 2.71 | 12.36 | 19 | 250 | No |
| Glass (borosilicate) | ideal | 64 | 2230 | 1.16 | 6.57 | 44 | 50 | No |
| Glass (borosilicate) | real knockdown 0.25 | 64 | 2230 | 2.32 | 13.13 | 22 | 50 | No |
| CFRP quasi-isotropic | ideal | 70 | 1600 | 1.09 | 4.44 | 46 | 600 | No |
| CFRP quasi-isotropic | real knockdown 0.25 | 70 | 1600 | 2.19 | 8.89 | 23 | 600 | No |
| CFRP high-modulus quasi-iso | ideal | 120 | 1650 | 0.84 | 3.50 | 61 | 500 | No |
| CFRP high-modulus quasi-iso | real knockdown 0.25 | 120 | 1650 | 1.67 | 7.00 | 30 | 500 | No |
| Beryllium | ideal | 287 | 1850 | 0.55 | 2.60 | 92 | 370 | No |
| Beryllium | real knockdown 0.25 | 287 | 1850 | 1.11 | 5.20 | 46 | 370 | No |
| Alumina ceramic | ideal | 370 | 3950 | 0.48 | 4.83 | 105 | 300 | No |
| Alumina ceramic | real knockdown 0.25 | 370 | 3950 | 0.96 | 9.65 | 53 | 300 | No |
| Silicon carbide | ideal | 410 | 3210 | 0.46 | 3.75 | 110 | 400 | No |
| Silicon carbide | real knockdown 0.25 | 410 | 3210 | 0.92 | 7.51 | 55 | 400 | No |
| Boron carbide | ideal | 450 | 2520 | 0.44 | 2.81 | 116 | 350 | No |
| Boron carbide | real knockdown 0.25 | 450 | 2520 | 0.88 | 5.61 | 58 | 350 | No |
| Diamond (CVD) | ideal | 1050 | 3510 | 0.29 | 2.55 | 177 | 1000 | No |
| Diamond (CVD) | real knockdown 0.25 | 1050 | 3510 | 0.57 | 5.10 | 89 | 1000 | No |
| Graphene (idealized bulk) | ideal | 1000 | 2200 | 0.29 | 1.64 | 172 | 10000 | No |
| Graphene (idealized bulk) | real knockdown 0.25 | 1000 | 2200 | 0.59 | 3.29 | 86 | 10000 | No |

No known homogeneous material floats as a thin vacuum sphere at sea level. Even ideal diamond comes out about 2.5 times too heavy. The figure of merit is rho / sqrt(E): low density and very high stiffness.

### 13.4 Sandwich shells (simplified estimate)

A sandwich wall puts two thin stiff faces far apart on a light core (honeycomb or foam), giving much more bending stiffness per kilogram. Simplified estimate for a 10 m radius sphere, knockdown 0.3, core density 30 kg/m3:

| Sandwich shell, R = 10 m, knockdown 0.3 | Core depth (cm) | Each face thickness (micrometers) | Areal mass incl. 30 kg/m3 core (kg/m2) | Shell mass / lift | Floats on paper? |
|---|---|---|---|---|---|
| CFRP faces | 10.0 | 1345 | 7.44 | 1.89 | No |
| CFRP faces | 5.0 | 2690 | 10.38 | 2.63 | No |
| CFRP faces | 2.5 | 5379 | 18.50 | 4.70 | No |
| Boron carbide faces | 10.0 | 359 | 4.81 | 1.22 | No |
| Boron carbide faces | 5.0 | 717 | 5.11 | 1.30 | No |
| Boron carbide faces | 2.5 | 1434 | 7.98 | 2.03 | No |
| Beryllium faces | 10.0 | 562 | 5.08 | 1.29 | No |
| Beryllium faces | 5.0 | 1125 | 5.66 | 1.44 | No |
| Beryllium faces | 2.5 | 2249 | 9.07 | 2.30 | No |
| Diamond faces | 10.0 | 154 | 4.08 | 1.04 | No |
| Diamond faces | 5.0 | 307 | 3.66 | 0.93 | Yes |
| Diamond faces | 2.5 | 615 | 5.07 | 1.29 | No |

Detailed published analyses (for example the sandwich-shell design by Akhmeteli and Gavrilin, patented around 2007) found that very stiff ceramic faces with an optimized honeycomb core may come close to or slightly beat neutral buoyancy on paper. No vacuum airship has been built or flown.

### 13.5 Partial vacuum

| Internal pressure (% of ambient) | Lift (kg/m3 at 26 C) | Lift vs helium | Pressure difference the shell must resist (kPa) |
|---|---|---|---|
| 0% (full vacuum) | 1.18 | 116% | 101 |
| 10% | 1.06 | 104% | 91 |
| 20% | 0.94 | 92% | 81 |
| 50% | 0.59 | 58% | 51 |
| 80% | 0.24 | 23% | 20 |
| 90% | 0.12 | 12% | 10 |

Shell mass scales with the square root of the pressure difference, while lift falls linearly, so partial vacuum does not escape the problem. A shell that also contains helium (hybrid) gains a little but adds complexity.

### 13.6 Shapes and concepts

| Concept | Idea | Assessment |
|---|---|---|
| Sphere | Uniform compression, best buckling resistance per mass | Best simple shape, still too heavy in monocoque form |
| Cylinder / cigar | Airship-like streamlining | Buckles at much lower pressure than a sphere of equal wall |
| Geodesic frame plus skin | Struts carry load, skin spans panels | Skin panels bow inward and need their own stiffness; strut buckling dominates |
| Sandwich honeycomb sphere | Stiff faces separated by a core | Most promising on paper |
| Inflated double wall | Pressurized gas between two membranes stiffens the shell | Pressurizing gas adds mass that cancels much of the gain |
| Tensegrity sphere | Compression struts with tension cables | Struts must carry the full atmospheric load in compression |
| Electrostatic support | Like charges on inner surfaces push outward | Field strengths needed approach air breakdown limits |
| Magnetic or rotating shells | Proposed in speculative work | No practical analysis showing feasibility |
| Higher altitude operation | Lower outside pressure | Lift falls exactly as fast as pressure falls, ratio unchanged at same temperature |

---

## 14. Tethers: materials, mass and maximum height

### 14.1 Tether materials (rope sized for 25 kN breaking strength, 65% fiber efficiency in rope construction)

| Tether material | Fiber strength (GPa) | Density (kg/m3) | Free breaking length (km) | Rope dia. for 25 kN break (mm) | Mass (g/m) | Mass of 100 m (kg) | 1,000 m (kg) | 3,000 m (kg) |
|---|---|---|---|---|---|---|---|---|
| UHMWPE (Dyneema SK78) | 3.4 | 975 | 356 | 3.8 | 11.0 | 1.1 | 11 | 33 |
| Aramid (Kevlar 29) | 2.9 | 1440 | 205 | 4.1 | 19.1 | 1.9 | 19 | 57 |
| PBO (Zylon AS) | 5.8 | 1540 | 384 | 2.9 | 10.2 | 1.0 | 10 | 31 |
| Carbon fiber (as rope) | 4.0 | 1800 | 227 | 3.5 | 17.3 | 1.7 | 17 | 52 |
| Vectran (LCP) | 3.2 | 1400 | 233 | 3.9 | 16.8 | 1.7 | 17 | 50 |
| Nylon 6,6 | 0.9 | 1140 | 81 | 7.4 | 48.7 | 4.9 | 49 | 146 |
| Polyester (PET) | 1.0 | 1380 | 74 | 7.0 | 53.1 | 5.3 | 53 | 159 |
| Steel wire rope | 1.8 | 7850 | 23 | 5.2 | 167.7 | 16.8 | 168 | 503 |
| Spectra/Dyneema braid real rope | 2.0 | 975 | 209 | 4.9 | 18.8 | 1.9 | 19 | 56 |

Free breaking length is how long a hanging fiber can be before it snaps under its own weight. UHMWPE (Dyneema, Spectra) floats on water and has the best strength per weight of common ropes. Steel is cheap, abrasion-resistant and conductive (a lightning and static hazard).

### 14.2 Maximum tether height where the line consumes all free lift (safety factor 5 on line strength, minimum 2 kN breaking)

| Free lift available for tether (kg) | UHMWPE: line mass, height where line weight = lift | Aramid | Steel wire |
|---|---|---|---|
| 20 | 0.9 g/m, 22,667 m | 1.5 g/m, 13,090 m | 13.4 g/m, 1,490 m |
| 50 | 1.1 g/m, 46,227 m | 1.9 g/m, 26,697 m | 16.4 g/m, 3,040 m |
| 100 | 2.2 g/m, 46,227 m | 3.7 g/m, 26,697 m | 32.9 g/m, 3,040 m |
| 200 | 4.3 g/m, 46,227 m | 7.5 g/m, 26,697 m | 65.8 g/m, 3,040 m |
| 500 | 10.8 g/m, 46,227 m | 18.7 g/m, 26,697 m | 164.5 g/m, 3,040 m |
| 1000 | 21.6 g/m, 46,227 m | 37.5 g/m, 26,697 m | 329.0 g/m, 3,040 m |

Real aerostats need margin for wind loads (see next section), so useful heights are much lower. Fiber-optic and power conductors inside the tether add mass.

### 14.3 Tether hazards and design data

| Item | Data |
|---|---|
| Static charge | Long tethers in dry or dusty wind build high voltage; conductive tethers need grounding |
| Lightning | Tethered aerostats are lightning rods; operations come down ahead of storms |
| Tether break | A balloon losing its tether becomes a free balloon; regulations require automatic rapid deflation devices |
| Catenary sag | A heavy tether hangs in a curve, so the balloon flies lower and farther downwind than a straight line suggests |
| Strumming | Vortex shedding vibrates the line; fairings or helical strakes reduce it |
| Winch | Level-wind drum, slip ring for power, tension sensor; descent under power, ascent under buoyancy |

---

## 15. Tethered balloons in wind

Drag pushes a tethered balloon downwind and pulls it down toward the ground (blowdown). Drag force D = 0.5 rho V^2 Cd A with Cd about 0.4 for a sphere. Lean angle from vertical = atan(drag / net free lift). Payloads assumed: 100 kg for the 6 m sphere, 300 kg for the 10 m and 15 m spheres, 2,500 kg (gondola plus 30 passengers) for the 22.5 m sphere. Envelope 100 g/m2.

| Helium sphere | Volume (m3) | Net free lift after envelope and payload (kg) | 5 mph drag / lean | 10 mph | 15 mph | 20 mph | 25 mph | 30 mph |
|---|---|---|---|---|---|---|---|---|
| 6 m sphere | 113 | 4 | 3 kg / 41 deg | 14 kg / 74 deg | 31 kg / 83 deg | 54 kg / 86 deg | 85 kg / 87 deg | 123 kg / 88 deg |
| 10 m sphere | 524 | 202 | 9 kg / 3 deg | 38 kg / 11 deg | 85 kg / 23 deg | 151 kg / 37 deg | 236 kg / 50 deg | 341 kg / 59 deg |
| 15 m sphere | 1,767 | 1,429 | 21 kg / 1 deg | 85 kg / 3 deg | 192 kg / 8 deg | 341 kg / 13 deg | 532 kg / 20 deg | 766 kg / 28 deg |
| 22.5 m sphere (Aerophile class, about 6,000 m3) | 5,964 | 3,416 | 48 kg / 1 deg | 192 kg / 3 deg | 431 kg / 7 deg | 766 kg / 13 deg | 1,197 kg / 19 deg | 1,724 kg / 27 deg |

A spherical balloon with little spare lift lies nearly flat in a light breeze. Big spheres hold position in moderate wind. This is why captive passenger balloons stop operating in winds above roughly 25 to 30 mph. It is also why tethered hot air ride balloons operate in early morning calm.

---

## 16. Aerostat shapes and tether systems in service

| System | Gas | Size | Operating height | Use |
|---|---|---|---|---|
| Aerophile captive balloons (Paris Parc Andre Citroen, Disney Springs Orlando and others) | Helium | About 6,000 m3, 22.5 m diameter | About 150 m | Tourist rides, up to about 30 passengers in a ring gondola; electric winch pulls it down, buoyancy lifts it up |
| Tethered hot air rides | Hot air | AX-7 to AX-9 | 15 to 30 m | Three-point tethers to vehicles or anchors; Oahu's North Shore has offered tethered rides |
| TARS (Tethered Aerostat Radar System, US southern border) | Helium | About 7,000 to 12,000 m3, aerodynamic shape with fins | Up to about 4,500 m | Low-level air surveillance |
| JLENS (retired) | Helium | 74 m long | About 3,000 m | Cruise missile detection; one broke loose in 2015 and dragged its tether across Pennsylvania |
| Barrage balloons (WWII) | Hydrogen | About 550 m3 | 1,500 m or more | Steel cables to snag low-flying aircraft |
| Caquot kite balloons (WWI) | Hydrogen | About 900 to 1,000 m3, sausage shape with fins | 1,000 to 1,500 m | Artillery observation; observers carried parachutes |
| Union Army Balloon Corps (US Civil War) | Coal gas and hydrogen | Up to about 900 m3 | Up to about 300 m | Thaddeus Lowe; telegraph line to the ground |
| Kytoon | Helium | Small | Up to a few hundred meters | Balloon with kite surfaces for stability in wind |
| Helikite (Allsopp) | Helium | 1 to 250 m3 | Up to about 600 m | Balloon plus kite, flies higher in wind instead of being blown down |

### 16.1 Why aerodynamic shapes beat spheres in wind

- Streamlined body: drag coefficient about 0.05 to 0.1 based on frontal area versus about 0.4 for a sphere.
- Fins: keep the nose into the wind, stopping erratic motion.
- Angle of attack: the hull generates aerodynamic lift that increases with wind, offsetting blowdown.
- Helikites and kytoons can actually climb in rising wind.

---

## 17. Pre-established ascent systems

A pre-established system means the infrastructure for gaining height already exists: a tether, a rope, a counterweight, a cable, a winch, a stored energy source. The person only uses it. The physics of each system decides how much effort the user spends.

### 17.1 Categories

| System | Source of lifting energy | User effort | Typical height | Typical rate |
|---|---|---|---|---|
| Captive gas balloon with winch | Buoyancy (gas paid for once, reused for years with top-ups) | None | 100 to 300 m | 0.5 to 2 m/s |
| Tethered hot air balloon | Propane | None (pilot burns) | 10 to 40 m | 0.5 to 2 m/s |
| Elevator with counterweight | Electricity, counterweight balances the car | None | Any building | 1 to 10 m/s (Shanghai Tower elevators about 18 to 20 m/s) |
| Water-counterbalance funicular | Water ballast filled at the top car | None | 50 to 150 m | 1 to 3 m/s |
| Aerial cableway / gondola | Electricity | None | Hundreds to thousands of meters | 3 to 7 m/s along cable |
| Glider winch launch | Engine-driven winch | None (pilot flies) | 300 to 1,000 m | 10 to 20 m/s climb |
| Glider aerotow | Tow plane | None | 600 to 1,000 m typical release | 2 to 5 m/s |
| Parasail on a boat | Boat engine pulling a canopy | None | 30 to 150 m | 1 to 3 m/s |
| Man-lifting kites (Samuel Cody, about 1903 to 1906) | Wind | None | Up to about 600 m | Slow |
| Fixed rope with mechanical ascenders | Muscle | Full body weight | Cliffs, caves, trees | 5 to 20 m per minute |
| Buoyancy-assisted rope climb | Balloon plus muscle | Reduced by buoyancy fraction | Up to the tether height | See section 18 |
| Ridge or thermal soaring | Rising air | Piloting only | Hundreds to thousands of meters | 1 to 5 m/s in lift |

### 17.2 Water-counterbalance funiculars

Two cars connected by a cable over a top pulley. The upper car fills a water tank until it outweighs the lower car plus passengers, then descends, pulling the other car up. At the bottom the water drains. Energy comes from the height of the water source.

| Funicular | Location | Opened | Length | Rise | Notes |
|---|---|---|---|---|---|
| Bom Jesus do Monte | Braga, Portugal | 1882 | about 274 m | about 116 m | Oldest operating water-counterbalance funicular |
| Lynton and Lynmouth Cliff Railway | Devon, England | 1890 | about 263 m | about 152 m | Still runs on water power from the West Lyn River |
| Fribourg funicular | Switzerland | 1899 | about 121 m | about 56 m | Uses treated wastewater as ballast |

The same principle works with a balloon: a buoyant counterweight replaces the descending water. A captive passenger balloon is effectively a buoyancy-powered elevator whose cable winch only controls the speed and brings the gondola back down.

### 17.3 Glider winch launch (ties to the beach glider file)

| Winch cable length (m) | Typical release height, light wind (m) | With 15 to 20 knot headwind (m) |
|---|---|---|
| 500 | 150 to 200 | 225 to 275 |
| 800 | 240 to 320 | 360 to 440 |
| 1,000 | 300 to 400 | 450 to 550 |
| 1,200 | 360 to 480 | 540 to 660 |
| 1,500 | 450 to 600 | 675 to 825 |
| 2,000 | 600 to 800 | 900 to 1100 |

Winch launch releases a glider at roughly 30 to 40% of the cable length in light wind, more with a headwind. The winch spends a few liters of fuel to put a sailplane and pilot several hundred meters up in under a minute.

---

## 18. Buoyancy-assisted climbing

A 100 kg climber clipped to a fixed rope, with a helium balloon taking part of the weight. Helium volume shown is gas lift only (envelope mass adds more, see section 9). Sustained human output assumed 150 W (a fit person on a long climb; elite cyclists hold 300 to 400 W for an hour).

| Body weight offset by balloon | Residual weight (kg) | Pull force needed (N) | Helium volume (m3, gas lift only) | Sphere dia. (m) | Power to climb at 0.5 m/s (W) | At 1.0 m/s (W) | Minutes to climb 100 m at 150 W sustained |
|---|---|---|---|---|---|---|---|
| 0% | 100 | 981 | 0 | 0 | 490 | 981 | 10.9 |
| 50% | 50 | 490 | 49 | 4.5 | 245 | 490 | 5.4 |
| 75% | 25 | 245 | 74 | 5.2 | 123 | 245 | 2.7 |
| 90% | 10 | 98 | 88 | 5.5 | 49 | 98 | 1.1 |
| 95% | 5 | 49 | 93 | 5.6 | 25 | 49 | 0.5 |
| 98% | 2 | 20 | 96 | 5.7 | 10 | 20 | 0.2 |
| 100% | 0 | 0 | 98 | 5.7 | 0 | 0 | no effort needed |

At 90% offset a 100 kg person feels like 10 kg and can climb 100 m in about a minute of moderate effort. Above 100% the balloon pulls the climber up and the rope becomes a brake instead of a ladder. The same balloon needs to be large: about 90 m3 of helium (a 5.5 m sphere) per 90 kg offset. In wind the balloon drags sideways (section 15), so a fixed rope from a tethered aerostat is far more stable than a free balloon.

### 18.1 The tether-as-highway concept

A tethered aerostat holds a cable vertically (or nearly so). Riders clip onto the cable with an ascender or a motorized climber (like a miniature space elevator):

| Design choice | Effect |
|---|---|
| Aerostat net lift must exceed cable weight plus rider plus wind drag | Sets aerostat size (sections 14 and 15) |
| Rider climbs with a powered ascender | Battery climbers in rope access lift 100 to 250 kg at 10 to 25 m per minute |
| Rider with partial buoyancy | Reduces cable tension changes and motor power |
| Descent | Gravity, braked by a descender; energy can be regenerated in a motorized climber |
| Cable angle in wind | Cable leans downwind, rider climbs along the curve |

---

## 19. Energy cost of altitude

Raising 100 kg by height h requires m g h joules regardless of method. What differs is where the energy comes from and how efficiently it is used.

| Height gain (m) | Potential energy, 100 kg (kJ) | Wh | kcal (ideal) | Food kcal at 25% muscle efficiency | Minutes at 150 W human | Propane equivalent (g, 100% efficient) | Grid cost at 15 cents/kWh, 50% winch efficiency (USD) |
|---|---|---|---|---|---|---|---|
| 10 | 9.8 | 2.72 | 2 | 9 | 1.1 | 0.2 | 0.0008 |
| 30 | 29.4 | 8.17 | 7 | 28 | 3.3 | 0.6 | 0.0025 |
| 100 | 98.1 | 27.24 | 23 | 94 | 10.9 | 2.1 | 0.0082 |
| 300 | 294.2 | 81.72 | 70 | 281 | 32.7 | 6.3 | 0.0245 |
| 1,000 | 980.7 | 272.41 | 234 | 938 | 109.0 | 21.2 | 0.0817 |
| 3,000 | 2,942.0 | 817.22 | 703 | 2,813 | 326.9 | 63.5 | 0.2452 |

Lifting a person 100 m takes about 98 kJ: about 94 food kcal at the muscle (roughly a quarter of a peanut-butter sandwich), or less than a cent of grid electricity through a winch. Buoyancy systems get their energy from the atmosphere's weight: the work was done once when the gas was produced and compressed.

---

## 20. Comparison of ascent methods for a 100 kg person

| Method | Infrastructure needed | Recurring cost per ascent | Height range | Wind tolerance | Effort |
|---|---|---|---|---|---|
| Free hot air balloon | Envelope, burner, basket, fuel, chase crew | Propane, crew time | Up to several km (record 21 km) | Low (under about 10 knots surface) | Pilot skill |
| Free helium balloon | Envelope, gas | Helium (expensive), ballast | Up to tens of km | Low at launch and landing | Pilot skill |
| Free hydrogen balloon | Envelope, gas generation | Cheap gas | Same as helium | Low | Pilot skill plus fire discipline |
| Captive helium balloon | Winch, large envelope, site | Tiny (helium top-ups, electricity) | 100 to 300 m | Moderate | None |
| Tethered hot air | Anchors, balloon | Propane | 10 to 40 m | Low | None |
| Buoyancy-assisted rope | Tethered aerostat and fixed line | Helium top-ups | Up to tether height | Moderate | Reduced muscle |
| Paraglider / hang glider from a ridge | Launch site with steady wind | None | Up to cloud base | Needs 10 to 25 mph onto the ridge | Pilot skill |
| Glider winch launch | Winch, airfield | Fuel | 300 to 1,000 m | Moderate | Pilot skill |
| Elevator / funicular / gondola | Building or line | Electricity or water | Fixed | High | None |

---

## 21. Weather limits for balloon operations

| Condition | Typical limit or effect |
|---|---|
| Surface wind for hot air launch and landing | Under about 8 to 10 knots (9 to 12 mph) |
| Winds aloft | Higher winds tolerated; fast drift complicates landing |
| Thermals | Hot air flights avoid midday thermals; flights run from sunrise to 2 to 3 hours after |
| Evening flights | Possible after thermals decay, before dark |
| Gusts and wind shear | Can deform the envelope and cause rapid altitude loss |
| Rain | Wet envelope gains weight; cold rain cools the air inside |
| Thunderstorms | No flight within many miles: outflow gusts, lightning |
| Hawaiian trade winds | 10 to 20+ mph most days rules out most free hot air flight; island geography and the ocean leave little landing room |
| Fog / low cloud | Visual flight rules apply |
| Altitude and heat | Hot and high days cut lift (section 4.1) |

---

## 22. Regulations (United States, summary)

| Rule set | Covers | Key points |
|---|---|---|
| 14 CFR Part 31 | Airworthiness standards for manned free balloons | Envelope, burner, basket design requirements |
| 14 CFR Part 91 | General operating rules | Applies to manned balloons |
| Pilot certification | Commercial or private pilot certificate with lighter-than-air balloon class rating | Separate ratings for hot air and gas balloons |
| 14 CFR Part 101 | Moored balloons, kites, unmanned free balloons | Moored balloons over 6 ft diameter or over 115 ft3 gas capacity are covered: limits near airports and clouds, notice to ATC above 150 ft, tether marking and lighting plus an automatic rapid deflation device if the balloon escapes |
| 14 CFR Part 103 | Ultralight vehicles | Unpowered ultralights include hang gliders and paragliders; certain small single-occupant balloons also fall under Part 103 |
| Commercial ride operators | FAA rules on balloon ride operations (strengthened after the 2016 Lockhart, Texas accident) | Commercial balloon pilots now hold medical certificates and face oversight similar to other commercial operators |

---

## 23. History timeline

| Year | Event |
|---|---|
| About 220 to 280 AD | Sky lanterns (Kongming lanterns) in China: small hot air balloons |
| 1670 | Francesco Lana de Terzi proposes a vacuum airship |
| 1709 | Bartolomeu de Gusmao demonstrates a small hot air balloon in Lisbon |
| 1766 | Henry Cavendish identifies hydrogen ("inflammable air") |
| 1783 June | Montgolfier brothers fly an unmanned hot air balloon at Annonay |
| 1783 November 21 | First manned free flight: Pilatre de Rozier and the Marquis d'Arlandes, Montgolfier hot air balloon, Paris |
| 1783 December 1 | Jacques Charles and Nicolas-Louis Robert fly the first manned hydrogen balloon |
| 1785 | Blanchard and Jeffries cross the English Channel by gas balloon; Pilatre de Rozier dies attempting the crossing in a hybrid hydrogen and hot air balloon |
| 1794 | French army uses observation balloons at Fleurus |
| 1852 | Henri Giffard flies the first powered (steam) airship |
| 1861 to 1863 | Union Army Balloon Corps |
| 1870 to 1871 | Siege of Paris: balloons carry people and mail out of the city |
| 1868 | Helium detected in the solar spectrum |
| 1900 | First Zeppelin (LZ 1) flies |
| 1903 | Helium found in Kansas natural gas (identified 1905) |
| 1931 to 1932 | Auguste Piccard reaches the stratosphere in a pressurized gondola |
| 1937 | Hindenburg disaster ends the era of passenger hydrogen airships |
| 1950s | Ed Yost develops the modern propane hot air balloon |
| 1960 | Joseph Kittinger jumps from 31.3 km (Excelsior III) |
| 1978 | Double Eagle II: first transatlantic balloon crossing |
| 1987 | Richard Branson and Per Lindstrand: first transatlantic hot air balloon crossing |
| 1999 | Bertrand Piccard and Brian Jones: first nonstop around-the-world balloon flight (Breitling Orbiter 3, Roziere) |
| 2002 | Steve Fossett: first solo around-the-world balloon flight |
| 2012 | Felix Baumgartner jumps from about 39 km (Red Bull Stratos) |
| 2014 | Alan Eustace jumps from about 41.4 km |
| 2016 | Fedor Konyukhov solo around-the-world in about 11 days |
| 2013 to 2021 | Google Loon superpressure balloons deliver internet, some flights over 300 days |

---

## 24. Records

| Record | Value | Holder / flight |
|---|---|---|
| Hot air balloon altitude | 21,027 m (about 69,000 ft) | Vijaypat Singhania, 2005, Mumbai |
| Manned gas balloon altitude | about 41.4 km | Alan Eustace, 2014 (helium) |
| Unmanned balloon altitude | about 53.7 km | JAXA thin-film balloon, 2013 |
| First around the world nonstop | 19 days 21 hours | Piccard and Jones, 1999 |
| Fastest solo around the world | about 11 days | Fedor Konyukhov, 2016 |
| Gas balloon distance (Roziere) | about 40,800 km | Breitling Orbiter 3 |
| Largest hot air balloons | About 25,000 m3 and above for large ride and record balloons | Various |
| Cluster balloon | 4,900 m in a lawn chair | Larry Walters, 1982 |

---

## 25. Formula sheet

| Purpose | Formula |
|---|---|
| Gas density | rho = p M / (R T) |
| Gross lift | L = V (rho_air - rho_gas) |
| Hot air gross lift | L = V rho_air (1 - T_ambient / T_envelope), temperatures in kelvin |
| Sphere volume | V = pi D^3 / 6 |
| Sphere surface | A = pi D^2 |
| Envelope mass | m = A x areal density |
| Net lift | L_net = L - m_envelope - m_equipment |
| Ascent velocity | v = sqrt(2 F_free / (rho Cd A_frontal)) |
| Expansion with altitude | V(h) / V(0) = rho(0) / rho(h) at equal gas temperature |
| Heat loss | Q = h A Delta T |
| Fuel rate | m_dot = Q / LHV |
| Sphere buckling pressure | p_cr = 2 E (t/R)^2 / sqrt(3 (1 - nu^2)) |
| Vacuum shell mass to lift | 3 (rho_shell / rho_air) (t/R) |
| Thin shell membrane stress | sigma = p R / (2 t) |
| Free breaking length | L_b = sigma / (rho g) |
| Tether mass | m = (cross section) x density x length |
| Drag | D = 0.5 rho V^2 Cd A |
| Blowdown angle | theta = atan(D / net lift) |
| Potential energy | E = m g h |
| Climbing power | P = m_residual g v |

---

## 26. Unit conversions

| From | To | Multiply by |
|---|---|---|
| ft3 | m3 | 0.0283168 |
| m3 | ft3 | 35.3147 |
| kg/m3 | lb/ft3 | 0.062428 |
| US gallon | liter | 3.78541 |
| liter propane | kg | about 0.51 |
| US gallon propane | kg | about 1.93 |
| kWh | MJ | 3.6 |
| kJ | kcal | 0.239 |
| psi | kPa | 6.89476 |
| atmosphere | kPa | 101.325 |
| m | ft | 3.28084 |
| GPa | ksi | 145.04 |

## Terra readout (soft)

| Piece | Note |
|---|---|
| **Flight.md** | Actuator-disk hover; this file is buoyancy and tethers |
| **Hawaiian trades** | Free hot air usually ruled out; tethered dawn rides or Kona lee windows |
| **Swing transport** | Balloon-tether swinging fails as transport. Verdict: `../Vehicle/HawaiianTransport.md`. Section 15 still owns the 15 m lean |
| **H2 vs He** | H2 ~8% more lift, cheap, fire risk; film permeation `PermeationBarriers.md` |
| **Vacuum shell** | No monocoque floats at sea level; adamantium / magic sandwich invent only |
| **Hover bike** | Heavier-than-air; aerostat is the other ascent family |
