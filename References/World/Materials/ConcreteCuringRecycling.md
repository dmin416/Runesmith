# Concrete Guide: Curing, Recycling and Crack Repair

> Earth invent loot. Portland vs Roman marine curing, dry / fresh / salt water, self-healing (lime clasts, crystalline, bacterial), recycling crushed concrete as aggregate, crack diagnosis and repair methods. Not Caldris law. Strength / EE / production: `BuildingMaterials.md`. Deterioration pack: `WeatheringCementConcrete.md`, hub `WeatheringWear.md`. Volcanic ash / pozzolan feed: `MaterialPurification.md`. Caldris build filter: `../Tech/Technology.md`. Nav: `Index.md`.

---

Contents:
- Sections 1 to 9: Curing (dry vs fresh water vs salt water, Roman marine concrete, self-healing systems)
- Section 10: Breaking apart and recycling concrete
- Section 11: Crack diagnosis and repair
- Section 12: Key takeaways

## Short Answer

- **Dry curing is the least reliable method for any cement.** Hydration stops when the concrete dries out, so strength stays low and shrinkage cracks form.
- **Fresh water moist curing is the most reliable method for modern Portland cement.** It gives the highest strength and the lowest permeability.
- **Salt water curing that "crystallizes the cracks" only works with a lime + volcanic ash (pozzolan) binder.** This is the Roman marine concrete system. With modern Portland cement, salt water mostly causes damage: steel corrosion, sulfate attack, magnesium attack and salt crystallization spalling.
- **Self-healing and raw strength are a tradeoff.** Roman-style marine concrete heals and lasts for millennia in seawater but has a fraction of the compressive strength of modern concrete and cannot carry steel reinforcement.

---

## 1. How Cement Actually Hardens

Cement does not harden by drying. It hardens by **hydration**, a chemical reaction with water that grows interlocking crystals and gel. Remove the water early and the reaction stops permanently in the affected zone.

### 1.1 Portland Cement Composition

Cement chemist shorthand: C = CaO, S = SiO2, A = Al2O3, F = Fe2O3, H = H2O, S̄ = SO3.

| Phase | Name | Typical % of clinker | Role |
|---|---|---|---|
| C3S | Alite | 50 to 70% | Early strength (first 7 to 28 days) |
| C2S | Belite | 15 to 30% | Late strength (months to years) |
| C3A | Tricalcium aluminate | 5 to 10% | Fast set, high heat, vulnerable to sulfates |
| C4AF | Ferrite | 5 to 15% | Minor strength, gives gray color |
| CS̄H2 | Gypsum (added) | 3 to 5% | Controls flash set of C3A |

### 1.2 Main Hydration Reactions

- 2 C3S + 6 H → C3S2H3 (C-S-H gel) + 3 CH (calcium hydroxide)
- 2 C2S + 4 H → C3S2H3 + CH
- C3A + gypsum + water → ettringite, later converting to monosulfate

### 1.3 Hydration Products

- **C-S-H gel (calcium silicate hydrate):** 50 to 60% of hardened paste volume. This is the "glue" that provides nearly all strength.
- **Portlandite, Ca(OH)2:** 20 to 25% of paste volume. Adds little strength. It is soluble and is the main target of chemical attack. It is also the fuel for pozzolanic reactions.
- **Ettringite and monosulfate:** Aluminate sulfate phases. These matter a great deal for sulfate and seawater resistance.

### 1.4 Water to Cement Ratio (w/c)

- About **0.22 to 0.25** is chemically consumed for full hydration.
- About **0.40 to 0.42** is needed for full hydration including water held in gel pores.
- Above that, extra water leaves **capillary pores** that lower strength and raise permeability.
- Every 0.05 increase in w/c drops strength noticeably. Durable marine concrete typically targets **w/c 0.40 or lower**.

### 1.5 Strength Gain Under Proper Moist Curing

| Age | Approximate % of 28-day strength |
|---|---|
| 3 days | 40 to 50% |
| 7 days | 65 to 70% |
| 28 days | 100% |
| 90 days | 110 to 120% |
| 1 year+ | 120 to 130% (more with slag or fly ash) |

---

## 2. Dry Curing (Air Curing)

### 2.1 What Happens

- Surface water evaporates within hours.
- Hydration slows sharply once internal relative humidity falls below about **80%** and essentially stops near 30%.
- The outer 25 to 50 mm (the "cover zone") is hit hardest. This is the exact layer that protects reinforcement from the environment.

### 2.2 Types of Cracking Caused by Drying

- **Plastic shrinkage cracking:** Occurs in the first few hours while concrete is still soft. Risk becomes high when evaporation exceeds about **1.0 kg/m² per hour** (hot, windy, low humidity conditions).
- **Drying shrinkage:** Typical long-term shrinkage is **400 to 800 microstrain** (0.4 to 0.8 mm per meter). When the slab is restrained, this produces tensile cracking.
- **Crazing and dusting:** A weak, powdery surface layer with fine map cracking.

### 2.3 Strength Penalty

- Concrete air-cured the entire time commonly reaches only about **half to 60%** of the strength of continuously moist-cured concrete at 6 months.
- Concrete moist-cured for 7 days then air-dried recovers most of the gap but never fully matches continuous moist curing.
- Permeability of the cover zone can be several times higher, which accelerates every form of chemical attack later.

### 2.4 Verdict

Dry curing is the worst option on every measure: strength, cracking, permeability and long-term durability.

---

## 3. Fresh Water Moist Curing

### 3.1 Methods

- **Ponding or immersion:** Best possible curing. Common for lab specimens and flat slabs.
- **Wet burlap or cotton mats:** Kept continuously wet.
- **Fog or sprinkler curing:** Continuous light misting.
- **Plastic sheeting:** Traps internal moisture. Can cause surface discoloration.
- **Liquid membrane curing compounds:** Sprayed seal. Easier but less effective than wet curing.
- **Steam curing:** Used in precast plants for very fast early strength.

### 3.2 Duration (General Industry Guidance)

| Cement type | Minimum moist cure |
|---|---|
| Type III (high early strength) | 3 days |
| Type I / II (general use) | 7 days |
| Blends with fly ash or slag | 10 to 14 days |
| Marine or high durability work | 14 to 28 days |

### 3.3 Temperature

- Ideal range: **10 to 30 °C (50 to 85 °F)**.
- Below 5 °C hydration crawls.
- Concrete must reach about **3.5 MPa (500 psi)** before its first freeze or ice crystals will permanently damage it.
- Above about 35 °C early strength is high but long-term strength and microstructure suffer.

### 3.4 Autogenous Healing in Fresh Water

Ordinary concrete already self-heals small cracks when kept wet:

- **Continued hydration:** Unreacted cement grains exposed in the crack react with water and fill it with new C-S-H.
- **Calcite precipitation:** Ca(OH)2 leaches into the crack and reacts with dissolved CO2: Ca(OH)2 + CO2 → CaCO3 + H2O.
- **Effective crack width:** Reliable for cracks under about **0.1 to 0.2 mm**. Cracks wider than about 0.3 mm rarely seal on their own.
- This only works with water present. Dry concrete does not heal.

### 3.5 Verdict

For modern Portland cement, especially reinforced concrete, fresh water moist curing is the gold standard.

---

## 4. Salt Water With Modern Portland Cement

### 4.1 Seawater Composition (Typical Open Ocean)

| Ion | Approx. mg/L |
|---|---|
| Chloride (Cl⁻) | 19,000 |
| Sodium (Na⁺) | 10,500 |
| Sulfate (SO4²⁻) | 2,700 |
| Magnesium (Mg²⁺) | 1,300 |
| Calcium (Ca²⁺) | 400 |
| Potassium (K⁺) | 380 |
| Total dissolved salts | ~35,000 (3.5%) |

### 4.2 Effect on Strength

- **Early strength (1 to 7 days):** Often equal to or slightly higher than fresh water concrete. Chloride acts as a set accelerator.
- **Long-term strength (90 days+):** Usually somewhat lower. Reductions in the range of roughly 5 to 15% are commonly reported.
- The "crystals" that form in Portland cement exposed to seawater are mostly **damaging phases**, not strengthening ones.

### 4.3 Chloride Attack on Steel (The Biggest Problem)

- Concrete normally protects steel with a high pH (about 12.5 to 13.5) that forms a passive oxide film.
- Chloride ions break down this film even at high pH.
- Corrosion threshold: roughly **0.2 to 0.4% chloride by weight of cement**.
- Rust occupies **2 to 6 times** the volume of the original steel. The expansion cracks the cover, which lets in more seawater, which speeds corrosion.
- Result: cracking, rust staining, spalling and eventual structural failure.
- Some chloride is chemically bound as **Friedel's salt** (3CaO·Al2O3·CaCl2·10H2O). This helps a little but does not prevent corrosion.

### 4.4 Sulfate Attack

- Sulfate reacts with portlandite to form **gypsum** and with aluminate phases to form **ettringite**.
- Both reactions are expansive and cause internal cracking.
- In seawater specifically, the high chloride content makes ettringite more soluble. Seawater sulfate attack therefore tends to cause **softening and erosion** more than dramatic expansion.
- High C3A cements are most vulnerable. Type V or other sulfate-resistant cements keep C3A below 5%.

### 4.5 Magnesium Attack

- MgSO4 + Ca(OH)2 + 2H2O → CaSO4·2H2O (gypsum) + Mg(OH)2 (brucite)
- Magnesium can also replace calcium inside C-S-H, turning it into **M-S-H**, which has almost no binding strength.
- A thin surface layer of **brucite and aragonite** often forms. This layer actually slows further attack slightly. It is the closest Portland cement gets to "salt crystals sealing the surface," and the benefit is minor.

### 4.6 Salt Crystallization Damage

- In the **splash zone and tidal zone**, seawater soaks in and then dries out repeatedly.
- Salt crystals grow in pores as water evaporates. Crystal growth pressure can exceed the tensile strength of the paste.
- Result: surface scaling and spalling. This is the opposite of crack healing.
- Fully submerged concrete suffers far less than concrete that cycles wet and dry.

### 4.7 Standards Positions

- Most building codes and standards **prohibit seawater for mixing or curing reinforced and prestressed concrete**.
- Some standards allow seawater for **plain (unreinforced) concrete** with caution, accepting efflorescence, lower long-term strength and surface staining.

### 4.8 Verdict

For Portland cement, salt water curing gives no healing benefit worth the cost. With steel inside it is actively destructive.

---

## 5. Roman Marine Concrete: Where Salt Water Crystallization Works

### 5.1 The Recipe

- **Binder:** Lime (calcium oxide or calcium hydroxide) plus volcanic ash (pozzolana) from the Bay of Naples area.
- **Ratio for marine work:** Vitruvius recorded about **2 parts pozzolana to 1 part lime**.
- **Aggregate (caementa):** Chunks of volcanic tuff or rock packed into the mortar.
- **Placement:** Wooden formwork lowered into the sea. The mortar and aggregate were packed into the forms underwater and left to cure submerged in seawater.

### 5.2 The Chemistry

1. **Pozzolanic reaction:** Lime reacts with reactive silica and alumina in the volcanic glass: Ca(OH)2 + SiO2 + Al2O3 + H2O → C-A-S-H binder.
2. **Seawater percolation:** Seawater flows slowly through the porous concrete over decades and centuries. It dissolves more of the volcanic glass and raises local pH.
3. **Crystal growth:** New minerals grow inside pores, cracks and relict lime clasts:
   - **Aluminous tobermorite:** A rare, layered calcium silicate hydrate crystal. It normally forms only above about 80 °C in hydrothermal settings. In Roman harbors it formed at sea temperature over long time spans, helped early on by heat from the lime reaction.
   - **Phillipsite:** A zeolite mineral that also crystallizes in pores and voids.
4. **Mechanical effect:** The platy tobermorite and phillipsite crystals interlock and reinforce the matrix. They grow into microcracks and stop crack propagation.

### 5.3 Why It Gets Stronger Over Time

- Modern Portland concrete in seawater is in slow chemical decline.
- Roman marine concrete is in **slow chemical growth**. Seawater is a reactant in its strengthening process rather than an attacker.
- Studies of drill cores from Roman harbors (such as Portus Cosanus in Tuscany and Caesarea in modern Israel) found these crystals throughout structures that have been submerged for about **2,000 years**.

### 5.4 Limitations

| Property | Roman marine concrete | Modern Portland concrete |
|---|---|---|
| Compressive strength | Roughly 5 to 20 MPa | 25 to 50 MPa typical, 100+ MPa high performance |
| Early strength gain | Very slow (months to years) | Fast (days to weeks) |
| Steel reinforcement | Not compatible in seawater | Standard |
| Tensile strength | Low | Low (relies on steel) |
| Seawater durability | Excellent, improves with age | Moderate, declines with age |
| Self-healing | Strong | Limited to hairline cracks |
| Raw material requirement | Specific reactive volcanic ash | Widely available |

### 5.5 Verdict

If the goal is a structure that sits in seawater and heals itself for centuries, Roman-style lime + pozzolan cured in salt water is the better system. It cannot match modern concrete for load-bearing strength or speed.

---

## 6. Lime Clasts and "Hot Mixing" (Fresh or Salt Water Self-Healing)

### 6.1 The Discovery

Research published in 2023 (MIT and collaborators, studying Roman concrete from the site of Privernum) showed that the small white lumps found in Roman concrete are not mixing mistakes. They are deliberate or process-driven **lime clasts** created by hot mixing.

### 6.2 How Hot Mixing Works

- Instead of using pre-slaked lime (calcium hydroxide), **quicklime (calcium oxide)** is mixed directly with the pozzolan, aggregate and water.
- CaO + H2O → Ca(OH)2 releases about **65 kJ per mole** of heat.
- The heat speeds up setting and enables high-temperature reaction products that would not form otherwise.
- Not all the lime fully reacts or disperses. Millimeter-scale **calcium-rich clasts** remain embedded through the concrete.

### 6.3 How the Clasts Heal Cracks

1. A crack forms and propagates through the concrete.
2. Cracks preferentially travel through the brittle lime clasts.
3. Water enters the crack and dissolves calcium from the exposed clast, creating a calcium-saturated solution.
4. The solution recrystallizes as **calcium carbonate** (reacting with dissolved CO2) or reacts with surrounding pozzolan to form new binder.
5. The crack seals.

### 6.4 Test Results

- Cracked samples made with hot-mixed quicklime sealed completely within about **2 weeks** of water flowing through the crack.
- Control samples made without quicklime **never healed** and water continued to flow through.
- This mechanism works with fresh water or seawater. It does not depend on salt.

---

## 7. Modern Self-Healing and Marine Concrete Options

### 7.1 Supplementary Cementitious Materials (SCMs)

These are the modern equivalent of Roman pozzolana. They consume weak portlandite and convert it into extra C-S-H.

| Material | Typical replacement of cement | Main benefits |
|---|---|---|
| Fly ash (Class F) | 15 to 35% | Lower permeability, chloride binding, sulfate resistance, less heat |
| Ground granulated blast furnace slag (GGBFS) | 25 to 70% | Excellent chloride resistance, high long-term strength |
| Silica fume | 5 to 10% | Very dense paste, very low permeability, high strength |
| Metakaolin | 8 to 15% | Similar to silica fume, lighter color |
| Natural volcanic ash / pumice | 15 to 40% | Closest modern analog to Roman pozzolana |

### 7.2 Crystalline Admixtures

- Proprietary chemicals added at mixing.
- When water enters a crack, they react with water and unhydrated cement to grow **insoluble needle-like crystals** that block the crack.
- Typically seal cracks up to about **0.4 to 0.5 mm**.
- Remain dormant and reactivate each time new water enters.

### 7.3 Bacterial (Biological) Self-Healing Concrete

- Bacterial spores (alkali-tolerant Bacillus species) plus a food source such as calcium lactate are embedded in the mix, often in protective capsules or porous aggregate.
- When a crack lets in water and oxygen, the spores activate and metabolize the lactate.
- They precipitate **calcium carbonate (limestone)** that fills the crack.
- Seals cracks up to about **0.5 to 0.8 mm**.

### 7.4 Engineered Cementitious Composites (ECC, "Bendable Concrete")

- Fiber-reinforced mix that forms many tiny cracks under 60 micrometers wide instead of a few large ones.
- Cracks this small heal very reliably through autogenous healing when wet.

### 7.5 Non-Corroding Reinforcement

Removing steel removes the chloride corrosion problem, which opens the door to seawater mixing and curing:

- **GFRP (glass fiber reinforced polymer) bars**
- **BFRP (basalt fiber reinforced polymer) bars**
- **Stainless steel rebar** (much more chloride tolerant, expensive)
- **Epoxy-coated or galvanized rebar** (moderate improvement only)

### 7.6 Standard Modern Marine Concrete Practice

- Sulfate-resistant cement (low C3A) or high slag / fly ash blends
- w/c ratio of **0.40 or lower**
- Concrete cover over steel of **50 to 75 mm**
- Air entrainment if freeze-thaw exposure exists
- Mixed and moist-cured with **fresh water**, then placed in service in seawater

---

## 8. Full Comparison

| Factor | Dry cure (Portland) | Fresh water cure (Portland) | Salt water cure (Portland) | Salt water cure (Roman lime + pozzolan) |
|---|---|---|---|---|
| 28-day strength | Low | Highest | Slightly lower | Very low |
| Long-term strength | Low, stalls | High, keeps rising | Declines slowly | Rises slowly for centuries |
| Shrinkage cracking | Severe | Minimal | Minimal | Minimal |
| Self-healing | None | Hairline cracks only | Minor surface sealing | Strong |
| Steel compatible | Yes (poor cover quality) | Yes | No | No |
| Marine durability | Poor | Moderate to good | Poor to moderate | Excellent |
| Speed to usable strength | Slow and incomplete | Fast | Fast | Very slow |
| Overall reliability | Worst | Best for structural work | Poor | Best for unreinforced marine longevity |

---

## 9. Recommended Approaches by Goal

### 9.1 Maximum Structural Strength (Buildings, Foundations, Load-Bearing)

- Portland cement with 20 to 30% fly ash or 40 to 50% slag
- w/c ratio 0.40
- Steel reinforcement with proper cover
- Fresh water mixing
- Continuous fresh water moist curing for 7 to 14 days
- Optional crystalline admixture for crack sealing

### 9.2 Maximum Seawater Longevity, No Steel (Breakwaters, Harbor Blocks, Sea Walls)

Roman-style marine mix:

- **Quicklime (CaO):** 1 part by volume
- **Reactive volcanic ash or pumice pozzolan:** 2 to 3 parts by volume (metakaolin or fly ash can partially substitute)
- **Aggregate:** Volcanic tuff, pumice or dense stone chunks
- **Mixing water:** Seawater is acceptable
- **Method:** Hot mix (add quicklime directly) to generate heat and form lime clasts
- **Curing:** Place in formwork and keep submerged in seawater
- **Expectation:** Low early strength. Mineral growth and strengthening continue for decades.

### 9.3 Hybrid: Strong Now, Self-Healing Later, Marine Exposure

- Portland cement blended with 40 to 60% slag or natural pozzolan
- Small quicklime addition for lime clasts
- Crystalline admixture or bacterial healing agent
- GFRP or BFRP reinforcement instead of carbon steel
- Fresh water moist cure for 14+ days before seawater exposure
- Gives modern strength levels with much better crack sealing and no corrosion risk

---

## 10. Breaking Apart and Recycling Concrete

### 10.1 Bottom Line on Usefulness

- **Very useful as aggregate.** Crushed concrete replaces gravel and crushed stone in road base, fill, drainage and (at limited levels) new concrete.
- **Recovery rate is high.** Roughly **90 to 95%** of clean demolished concrete by mass comes out as usable aggregate. The steel rebar is recovered separately and is close to 100% recyclable.
- **It does not turn back into cement.** Hardened cement paste cannot be cheaply converted back into fresh Portland cement. Recycling recovers the rocks, not the glue.
- **Carbon savings are small unless cement use also drops.** Aggregate is only a few percent of concrete's carbon footprint. Cement is roughly 80 to 90% of it.
- **Biggest real wins:** Avoided landfill fees, avoided quarrying, shorter trucking distances and cheaper base material near cities.
- **Biggest real limit:** The old mortar stuck to recycled aggregate makes it weaker, more porous and more variable than virgin stone. That caps how much can go into high-grade structural concrete.

### 10.2 Breaking Methods

| Method | How it works | Best use | Notes |
|---|---|---|---|
| Jackhammer / pneumatic breaker | Impact chisel | Small areas, slabs | Cheap. Causes microcracking in the concrete left behind |
| Hydraulic breaker on excavator | Large impact hammer | Bulk demolition | Fast. Heavy vibration |
| Hydraulic crusher / pulverizer jaws | Squeezes concrete and separates rebar | Walls, columns, beams | Pre-sorts steel during demolition |
| Hydrodemolition | Water jets at roughly 1,000 to 2,800 bar | Removing damaged concrete before repair | Removes weak concrete selectively. Leaves rebar clean and undamaged. No microcracking in sound concrete |
| Diamond wire saw / wall saw | Abrasive cutting | Precise removal, reuse of whole blocks | Clean edges. Allows reuse of intact panels |
| Expansive demolition agents | Grout poured in drilled holes expands and splits concrete | Quiet or vibration-sensitive sites | Slow (hours to a day). No noise or flyrock |
| Controlled blasting | Explosives | Large structures | Requires licensed specialists |

### 10.3 Recycling Process Step by Step

1. **Pre-demolition sorting:** Remove wood, drywall (gypsum), asphalt, plastics, insulation and glass. Gypsum is the most harmful contaminant because its sulfate attacks new concrete.
2. **Primary crushing:** Jaw crusher breaks pieces down to roughly 100 to 200 mm.
3. **Steel removal:** Overhead magnets pull out rebar and wire mesh.
4. **Secondary crushing:** Cone or impact crusher reduces material to final sizes. Impact crushers knock off more of the adhered mortar and give a better quality product.
5. **Screening:** Vibrating screens split material into size fractions (for example 0 to 4 mm fines, 4 to 10 mm, 10 to 20 mm, 20 to 40 mm).
6. **Washing (optional):** Removes dust and fine mortar. Lowers water absorption and improves bond in new concrete.
7. **Stockpiling and testing:** Test for gradation, absorption, density, contaminants, chloride and sulfate content.

### 10.4 Typical Output From 1 Tonne of Clean Concrete

| Product | Approximate share |
|---|---|
| Coarse recycled aggregate (over 4 mm) | 60 to 70% |
| Fine recycled aggregate (under 4 mm) | 25 to 35% |
| Steel (if reinforced) | Variable, often 1 to 3% for typical reinforced members |
| Waste / unusable | Under 5% for clean source material |

### 10.5 Properties of Recycled Concrete Aggregate (RCA) vs Natural Aggregate

| Property | Natural aggregate | Coarse RCA | Fine RCA |
|---|---|---|
| Adhered old mortar | None | 20 to 50% by mass | 40 to 60%+ by mass |
| Water absorption | 0.5 to 2% | 3 to 8% | 6 to 12% |
| Particle density | 2,600 to 2,750 kg/m³ | 2,200 to 2,500 kg/m³ | 2,000 to 2,300 kg/m³ |
| LA abrasion loss | 15 to 30% | 25 to 45% | Not applicable |
| Variability | Low | Moderate to high | High |

The old mortar is the weak link. It is porous, has its own microcracks from crushing and creates a second weak interface zone inside the new concrete.

### 10.6 Uses Ranked From Most to Least Common

1. **Road base and subbase:** The largest single use. RCA often performs as well as or better than virgin base because leftover unhydrated cement and portlandite give it a mild self-cementing effect after compaction.
2. **General fill and backfill:** Trenches, embankments, site leveling.
3. **Drainage and erosion control:** French drains, riprap (large broken chunks), gabion fill.
4. **Non-structural concrete:** Sidewalks, curbs, gutters, mass foundations, lean concrete, blinding.
5. **Structural concrete:** Possible at controlled replacement levels. Many codes worldwide allow roughly 20 to 50% coarse RCA depending on strength class and exposure. Fine RCA is usually limited or excluded.
6. **Landscaping:** "Urbanite" (broken slabs) reused as paving stones and retaining walls.

### 10.7 Effect of RCA Replacement Level on New Concrete

Replacement of the coarse natural aggregate by coarse RCA, same w/c ratio, typical ranges:

| Property | 20 to 30% RCA | 50% RCA | 100% RCA |
|---|---|---|---|
| Compressive strength | 0 to 5% lower | 5 to 15% lower | 10 to 30% lower |
| Elastic modulus (stiffness) | 5 to 10% lower | 10 to 20% lower | 15 to 40% lower |
| Drying shrinkage | 5 to 15% higher | 15 to 30% higher | 20 to 60% higher |
| Creep | 5 to 15% higher | 15 to 35% higher | 30 to 60% higher |
| Water absorption / permeability | Slightly higher | Moderately higher | Much higher |
| Chloride penetration | Slightly higher | Higher | Significantly higher |

Practical reading: at **20 to 30% coarse replacement** the difference is close to unnoticeable for most work. At 100% replacement the concrete needs mix redesign (more cement or SCMs, lower w/c) to hit the same strength. That extra cement can erase the environmental benefit.

### 10.8 Methods That Improve Recycled Aggregate Quality

- **Better crushing:** Multiple crushing stages and impact crushers strip more old mortar.
- **Mechanical rubbing / abrasion:** Tumbling or attrition scrubbing removes weak mortar.
- **Heat treatment:** Heating to roughly 300 to 500 °C makes the old mortar brittle so it separates during rubbing. Energy intensive.
- **Acid presoaking:** Dilute acid dissolves adhered mortar. Must be fully rinsed to avoid contaminating new concrete.
- **Accelerated carbonation:** Exposing RCA to concentrated CO2 converts portlandite and some C-S-H in the old mortar to calcium carbonate. This fills pores, lowers absorption, raises density and permanently locks away CO2.
- **Pozzolan or polymer slurry coating:** Coats and seals the aggregate surface.
- **Two-stage mixing:** Mix the RCA with part of the water and the cement first to form a thin paste coating that fills surface pores, then add the remaining water. Improves the interface zone and strength.
- **Presoaking to saturated surface dry (SSD):** Stops the porous RCA from stealing mixing water and causing rapid slump loss.

### 10.9 Contaminant and Risk Checks

- **Chlorides:** Concrete from marine structures, parking decks or bridges treated with deicing salt can carry enough chloride to corrode steel in the new concrete.
- **Sulfates:** Gypsum drywall, plaster or sulfate-exposed concrete can trigger sulfate attack.
- **Alkali-silica reaction (ASR):** If the source concrete had ASR, its aggregate can still be reactive. Use with SCMs or avoid in structural work.
- **Asphalt, wood, plastic:** Lower strength and create voids.
- **Lead paint, asbestos, oil contamination:** Must be removed or handled as hazardous waste before crushing.

### 10.10 Recovering Value From the Old Cement Paste

- **Recarbonation:** Crushed concrete absorbs CO2 from the air, especially the fine fraction with its high surface area. Over time this reclaims part of the CO2 released when the original cement was made.
- **Recycled fines as filler or SCM:** Carbonated recycled paste fines can partially replace cement or limestone filler.
- **Thermal reactivation:** Heating hardened paste to roughly 600 to 800 °C dehydrates C-S-H and portlandite into partly reactive phases. It produces a weak binder and costs energy.
- **Clinker raw feed:** Old paste is already rich in calcium. Using it in place of limestone reduces the CO2 released by limestone calcination in a cement kiln.
- **Electric arc furnace route (research stage):** Recent research has demonstrated using recycled cement paste as the slag-forming flux in electric arc steel furnaces, producing reactivated cement clinker as a byproduct. This is not yet widespread commercially.

### 10.11 Economics

- **Transport dominates aggregate cost.** Trucking can double the delivered price of aggregate over a few tens of kilometers. Crushing demolition concrete on site or near the job is where recycling saves the most money.
- **Mobile crushers** process concrete directly at demolition sites, eliminating haul-out and haul-in.
- **Landfill tipping fees** are avoided entirely.
- **Recycled base material** is commonly priced below virgin crushed stone in urban markets.
- **Structural-grade RCA** costs more to produce than base material because of extra crushing, washing and testing.

### 10.12 Carbon Reality Check

| Component | Approximate share of concrete's embodied CO2 |
|---|---|
| Portland cement | 80 to 90% |
| Aggregate (quarrying, crushing, transport) | 2 to 10% |
| Admixtures, water, batching, delivery | Remainder |

Recycling aggregate alone saves a small slice of carbon. The large reductions come from using less Portland cement (slag, fly ash, calcined clay, natural pozzolan, lime-pozzolan binders) and from carbonating recycled material.

---

## 11. Crack Diagnosis and Repair

A "perfect" repair depends on fixing the **cause** first. Sealing a crack that is still moving or still being driven by rusting steel only buys a few months.

### 11.1 Step 1: Identify the Crack Type

| Crack type | Typical appearance | When it appears | Cause |
|---|---|---|---|
| Plastic shrinkage | Short, shallow, parallel or random cracks on slab surface | First hours | Rapid surface evaporation |
| Plastic settlement | Cracks directly above rebar or at depth changes | First hours | Concrete settling around fixed objects |
| Drying shrinkage | Fairly straight cracks at regular spacing, often through full depth | Weeks to months | Restrained shrinkage |
| Thermal | Similar to shrinkage. Common in massive pours | Days (internal heat) or seasonally | Temperature differences and restraint |
| Crazing | Fine hexagonal map pattern on surface | Days to weeks | Over-finishing, poor curing |
| Settlement / foundation movement | Diagonal or stair-step cracks, wider at one end | Any time | Soil movement |
| Structural / overload | Flexural cracks at mid-span bottom, diagonal shear cracks near supports | Under load | Excess load or under-design |
| Corrosion-induced | Cracks running along rebar lines, rust staining, hollow sound, spalling | Years | Chloride or carbonation corrosion of steel |
| Alkali-silica reaction (ASR) | Map cracking with gel exudation, often wider in damp areas | Years | Reactive aggregate expanding |
| Freeze-thaw | Surface scaling, D-cracking near joints and edges | Winters | Water freezing in saturated pores |
| Sulfate attack | Softening, expansion, map cracking | Years | Sulfate-bearing soil or water |

### 11.2 Step 2: Determine Whether the Crack Is Active or Dormant

- **Dormant:** No longer moving. Can be bonded rigidly (epoxy).
- **Active:** Still opening and closing (thermal cycles, ongoing settlement, ongoing corrosion). Needs a flexible repair or a joint, or the cause must be stopped first.
- **Monitoring tools:**
  - Crack monitor gauges (two overlapping plates with crosshairs) read to about 0.1 to 0.5 mm.
  - Pins glued on each side and measured with a caliper or demountable mechanical strain gauge.
  - Electronic displacement transducers for continuous logging.
  - Monitor for **at least several weeks**, ideally across seasonal temperature swings.

### 11.3 Step 3: Measure Width and Depth

- **Width:** Crack comparator card or crack-width microscope.
- **Depth:** Ultrasonic pulse velocity, small diameter cores or impact-echo testing.
- **Moisture:** Note whether the crack is dry, damp or actively leaking. This determines resin choice.
- **Hidden damage:** Hammer sounding or chain dragging on slabs finds hollow, delaminated areas that need removal rather than crack injection.

### 11.4 Tolerable Crack Widths (Widely Used Industry Guidance for Reinforced Concrete)

| Exposure | Approximate tolerable width |
|---|---|
| Dry air or protective membrane | 0.41 mm |
| Humid air, moist air, soil | 0.30 mm |
| Deicing chemicals | 0.18 mm |
| Seawater, seawater spray, wetting and drying | 0.15 mm |
| Water-retaining structures | 0.10 mm |

Cracks below these widths in the matching exposure usually do not need structural repair. They may still need sealing for appearance or leaks.

### 11.5 Repair Methods in Full Detail

#### A. Epoxy Injection (Structural Bonding)

**Use for:** Dormant cracks from about **0.05 mm to 6 mm** where strength must be restored. Restores the concrete to roughly monolithic condition. Cured epoxy bonds more strongly than the concrete itself, so a later failure typically happens beside the repair rather than through it.

**Not for:** Active cracks, actively leaking cracks (unless a moisture-tolerant epoxy is used), or cracks caused by ongoing corrosion.

**Materials:**
- Very low viscosity epoxy (roughly 100 to 500 centipoise) for hairline cracks
- Medium viscosity for wider cracks
- Paste or gel epoxy for surface capping and port setting

**Procedure:**
1. **Clean the crack.** Blow out with oil-free compressed air. Remove dirt, efflorescence, oil and loose material. Vacuum if needed. Do not use water unless the epoxy is moisture tolerant.
2. **Install injection ports.** Surface-mounted ports glued over the crack, or drilled ports angled to intersect the crack below the surface. Space ports roughly equal to the member thickness, commonly 150 to 300 mm apart, closer for fine cracks.
3. **Seal the surface.** Cover the crack face between ports with epoxy paste to stop leakage. On walls, seal both faces if accessible.
4. **Let the cap cure** per manufacturer (often a few hours).
5. **Inject from the lowest port** on vertical cracks, or from one end on horizontal cracks.
6. **Use low, steady pressure.** High pressure can blow off the surface seal or widen the crack. Fine cracks take patience.
7. **Advance port by port.** When epoxy appears at the next port, cap the current port and move injection to the next one.
8. **Cure fully.** Typically 1 to 7 days depending on resin and temperature.
9. **Remove ports and surface cap** by grinding or heating and scraping.
10. **Verify.** Take small cores across the crack to confirm full-depth penetration on critical work.

**Temperature limits:** Most epoxies need concrete and air above about **10 °C (50 °F)**. Below that they thicken, penetrate poorly and cure slowly.

#### B. Polyurethane Injection (Leak Sealing)

**Use for:** Wet, leaking or slightly moving cracks in basements, tunnels, tanks and below-grade walls.

**Types:**
- **Hydrophobic polyurethane:** Reacts with water to form rigid or semi-rigid closed-cell foam. Low shrinkage when dry. Better for long-term stability.
- **Hydrophilic polyurethane:** Absorbs water to form a flexible gel or foam. Very flexible. Can shrink if it dries out.

**Procedure:** Similar to epoxy injection, usually with drilled packers set at 45° into the crack from alternating sides. Water often is flushed through first to activate the resin.

**Limit:** Seals water but adds no structural strength.

#### C. Routing and Sealing (Active or Cosmetic Cracks)

**Use for:** Active cracks that will keep moving and non-structural surface cracks on slabs and walls.

**Procedure:**
1. Use a crack chaser saw or router to cut a groove along the crack, roughly **6 to 20 mm wide**.
2. Clean thoroughly with compressed air or a wire brush.
3. Insert a **bond breaker** (tape or backer rod) at the bottom so the sealant bonds only to the two side walls. A sealant stuck on three sides tears when the crack moves.
4. Fill with flexible sealant (polyurethane, silicone or polysulfide). For moving cracks aim for a sealant width to depth ratio of about **2:1**.
5. Tool the surface smooth.

#### D. Gravity Filling (Horizontal Surfaces)

**Use for:** Fine crack networks on bridge decks, parking garages and slabs. Cracks roughly **0.03 to 2 mm**.

**Materials:** High molecular weight methacrylate (HMWM) or very low viscosity epoxy.

**Procedure:**
1. Clean and dry the surface. Shot blast if possible.
2. Flood the surface with resin and broom it into cracks.
3. Allow time for penetration. Reapply over cracks that keep absorbing.
4. Broadcast sand onto the wet resin for skid resistance on traffic surfaces.

#### E. Stitching (Restoring Tensile Strength Across a Crack)

**Use for:** Cracks where tension must be carried across, such as cracked slabs, walls or masonry.

**Procedure:**
1. Drill holes on both sides of the crack.
2. Cut slots between holes.
3. Embed U-shaped steel stitching dogs, helical stainless bars or carbon fiber rods in epoxy or non-shrink grout.
4. **Vary stitch length and orientation.** Uniform stitches in a line create a new weak plane and the crack simply reappears at their ends.
5. Seal or inject the crack itself as well.

#### F. Drilling and Plugging

**Use for:** Straight vertical cracks in retaining walls or similar where water leakage is the problem.

**Procedure:** Drill a 50 to 75 mm hole centered along the full length of the crack and fill it with grout. The grout plug forms a key that blocks water and resists movement.

#### G. Dry Packing

**Use for:** Dormant cracks, holes and narrow slots with depth greater than width.

**Procedure:** Mix a very low water mortar (about 1 part cement to 2.5 to 3 parts sand, just damp enough to hold its shape when squeezed). Ram it into the cavity in thin layers with a hardwood stick and hammer. Moist cure for several days.

#### H. Partial-Depth Patching of Spalls and Delaminations

**Procedure:**
1. **Mark the area** by sounding. Extend boundaries about 75 to 150 mm past the damaged area.
2. **Saw cut the perimeter** about 10 to 20 mm deep with square edges. Avoid feather edges, which fail quickly.
3. **Remove deteriorated concrete** with chipping hammers (light weight, roughly 15 kg class or lighter near steel) or hydrodemolition.
4. **Roughen the surface** to a coarse profile. Abrasive blasting removes the bruised, microcracked layer left by chipping.
5. **Clean** all dust and debris.
6. **Pre-wet to saturated surface dry (SSD)** for cementitious repair material. The substrate should be damp with no standing water. This stops the old concrete from sucking water out of the patch.
7. **Apply bonding agent** if specified, or scrub a thin slurry coat of the repair mortar into the surface.
8. **Place the repair material** before the bond coat dries. Consolidate thoroughly.
9. **Finish and moist cure** for at least 3 to 7 days. Curing a thin patch matters even more than curing new concrete because the patch dries quickly.

#### I. Corrosion-Induced Cracking Repair

Sealing the crack without treating the steel guarantees recurrence.

1. Remove concrete along the corroded bars and **behind them**, leaving roughly 20 to 25 mm of clear space around the bar (or the aggregate size plus a margin) so repair material fully encases the steel.
2. Continue removal along the bar until clean, uncorroded steel is reached.
3. Clean the steel by abrasive blasting to remove all rust and scale.
4. **Check section loss.** If a bar has lost more than roughly 20 to 25% of its cross-section, add supplemental bars lapped onto sound steel.
5. **Prevent the "ring anode" or "halo" effect.** New patches often cause accelerated corrosion in the old concrete right around the patch edge. Install **embedded galvanic (sacrificial zinc) anodes** tied to the steel around the patch perimeter.
6. Apply the patch as in Method H.
7. For widespread chloride contamination consider **impressed current cathodic protection**, **electrochemical chloride extraction** or **realkalization** (for carbonation damage).
8. Seal the finished surface with a penetrating silane or siloxane sealer to cut further chloride and water ingress.

#### J. External Strengthening for Structural Cracks

- **Carbon fiber reinforced polymer (CFRP) sheets or strips** bonded to tension faces or wrapped around columns
- **Steel plate bonding**
- **External post-tensioning**
- **Section enlargement** (adding new reinforced concrete jacket)
- Requires engineering design. Injection alone does not fix an under-designed member.

#### K. Autogenous and Assisted Self-Healing

- For hairline cracks under about **0.1 to 0.2 mm**, keeping the concrete continuously wet for several weeks can seal them through continued hydration and calcite growth.
- **Surface-applied crystalline treatments** penetrate the surface and grow crystals in cracks when wet. Effective up to roughly 0.4 mm.
- Concrete built with lime clasts, crystalline admixtures or bacterial agents heals itself when water enters the crack.

### 11.6 Matching Method to Crack

| Situation | Best method |
|---|---|
| Dormant structural crack, dry, 0.05 to 6 mm | Epoxy injection |
| Leaking crack in basement or tank | Polyurethane injection |
| Active crack that will keep moving | Rout and seal with flexible sealant, or convert to a joint |
| Fine crack network on a deck or garage slab | Gravity fill with HMWM or epoxy |
| Crack needing tension capacity restored | Stitching plus injection |
| Hairline plastic shrinkage cracks | Wet curing, crystalline treatment or gravity fill |
| Crazing | Usually cosmetic. Penetrating sealer or thin overlay |
| Spalling or delamination | Partial-depth patch |
| Cracks along rebar with rust | Corrosion repair (Method I) |
| Structural overload cracks | Engineering assessment, injection plus external strengthening |
| ASR cracking | Reduce moisture (sealers, drainage), lithium treatments in some cases, then repair. Injection alone fails because expansion continues |
| Settlement cracks | Stabilize soil first (underpinning, piers, grout injection), then repair crack |

### 11.7 Principles of a "Perfect" Repair

1. **Fix the cause first.** Drainage, soil, overload, corrosion, ASR or restraint.
2. **Surface preparation decides success.** Most repair failures are bond failures from dirty, weak or smooth substrate. Sound, clean, rough concrete is mandatory.
3. **Material compatibility.** The repair material should match the existing concrete as closely as possible in:
   - **Stiffness (elastic modulus):** A much stiffer patch attracts load and cracks at the bond line.
   - **Thermal expansion:** Concrete expands about 10 × 10⁻⁶ per °C. Unfilled epoxy can be 5 to 10 times higher. Fine for thin injected cracks. Poor for large thick patches exposed to temperature swings.
   - **Shrinkage:** Use low-shrink or shrinkage-compensated repair mortars. Shrinking patches debond.
   - **Permeability:** A patch far less permeable than the surrounding concrete can trap moisture and shift corrosion to the patch edges.
4. **Moisture condition matches the material.** Dry substrate for most epoxies. SSD for cementitious mortars. Moisture-tolerant resins for damp conditions.
5. **Temperature control.** Respect minimum and maximum application temperatures for every product.
6. **Proper curing.** Cementitious repairs must be kept moist. Thin patches dry out fastest and need the most care.
7. **Quality verification:**
   - **Sounding** to confirm no hollow areas remain
   - **Pull-off bond tests** on patches (a common minimum target is about 1.0 to 1.5 MPa, or failure in the substrate rather than at the bond line)
   - **Cores** through injected cracks to confirm resin penetration
   - **Ultrasonic pulse velocity** before and after to compare
8. **Protect afterward.** Penetrating sealers, coatings, cathodic protection or drainage improvements keep the repair from failing for the same reason the original concrete did.

---

## 12. Key Takeaways

1. Concrete must stay **wet** to cure. Dry curing is never the reliable choice.
2. Salt water crystallization that heals cracks is real but depends on the **binder**, not the water alone.
3. With **Portland cement**, salt water produces mostly harmful crystals and corrodes steel.
4. With **lime + volcanic ash**, salt water drives the growth of tobermorite and phillipsite, which reinforce the concrete and seal cracks over centuries.
5. **Lime clasts from hot mixing** add a second self-healing system that works in any water.
6. Roman-style marine concrete trades **strength and speed** for **durability and self-repair**.
7. For modern reinforced structures, the best result is a pozzolan-rich Portland blend cured in **fresh water**, optionally with crystalline or bacterial healing agents and non-corroding reinforcement.
8. Recycling recovers **90 to 95%** of clean concrete as aggregate. It works best as road base and fill. In new structural concrete about **20 to 30% coarse replacement** is nearly undetectable while 100% replacement costs 10 to 30% of strength.
9. Recycling saves landfill space, quarry stone and trucking cost. It saves little carbon unless cement content also drops or the crushed material is carbonated.
10. Crack repair starts with **diagnosis**: type, active or dormant, width, depth, moisture and cause.
11. **Epoxy injection** restores strength in dormant cracks. **Polyurethane** stops leaks. **Rout and seal** handles moving cracks. **Corrosion cracks** need steel treatment and galvanic anodes, not just sealing.
12. The quality of surface preparation and material compatibility decides whether a repair lasts.
