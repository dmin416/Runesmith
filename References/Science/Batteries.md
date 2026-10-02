# Battery Technology

Earth ladder from the first cell to lithium-air. Home-buildable, industrial and laboratory builds. Use for invent beats and for comparing chemical storage to mana stones. Do not paste Earth brand names into prose unless the story invents them.

**Accuracy:** solid popular engineering summary. Wh/kg bands and dates are order-of-magnitude.

**Caldris readout** (`../World/Technology.md`): craftsman + early-industrial magitech. **Near-reach invents:** voltaic pile, Daniell, Leclanché / zinc-carbon wet or dry cells, simple zinc-air demos (if KOH / salts and carbons exist). **Harder:** NiFe (caustic KOH), any lithium or molten-sodium chemistry (dry rooms, fire risk, no consumer market). **Not the usual energy path:** mana stones and runic reservoirs already fill portable power. Chemical cells matter for Earth-knowledge invents, non-mana gadgets, or when a mage wants voltage without a stone socket.

Companion: `ManaStones.md` (tank math), `../Runes/Energy.md` (1 mana ≈ 10 J), `RefinedMana.md` (Stillwire / Lightthread prestige craft), `WritingTools.md` / `Materials.md` (graphite / carbon).

---

## Mana Stone vs Battery Performance

Numbers follow locked stone law (`ManaStones.md`, `../Runes/Energy.md`). Stones store **mana**. A path or rune converts it to electricity or work. **Mass is size-only** (2.65 g/cm³). Quality does not change weight.

### Stone law

- **Energy:** 1 mana = 10 J. Capacity = 1 mana per mm³ of stone.
- **Throughput (output):** `Q × SA` mana/s (SA in mm²)
- **Recharge (input):** `((Q + 1) / 2) × SA` mana/min
- **Sustainable draw:** input ÷ 60 mana/s. The stone never empties at or below this rate.

### Common stone baseline (Q 1)

| Measure | Value |
|---|---|
| Energy by mass | ~1,050 Wh/kg |
| Energy by volume | ~2,780 Wh/L (10 J/mm³) |
| Density | 2.65 kg/L (quartz) |

Energy density does not change with size or quality. Power per kilogram rises as stones get smaller (more area per volume) or as Q rises (same mass, faster dump).

### Stone sizes at Q 1

| Stone | Cap (mana) | Energy | Mass | Burst power | Full dump time | Sustainable power | Full recharge |
|---|---|---|---|---|---|---|---|
| Rice | 19 | 0.05 Wh | 0.05 g | 420 W | 0.45 s | 7 W | ~27 s |
| Marble | 2,145 | 6 Wh | 5.7 g | 8 kW | 2.7 s | 134 W | ~2.7 min |
| Walnut | 14,140 | 39 Wh | 37 g | 28 kW | 5 s | 470 W | ~5 min |
| Fist | 268,080 | 745 Wh | 0.71 kg | 201 kW | 13 s | 3.4 kW | ~13 min |

### Q 10 (dragon) fist

Same **710 g** and **745 Wh** as Common. Q only multiplies rates.

| Measure | Value |
|---|---|
| Burst power | ~2 MW (×10) |
| Burst per kg | ~2,840 kW/kg |
| Full dump time | ~1.3 s |
| Recharge input | ×5.5 |
| Full recharge | ~2.4 min |
| Sustainable power | ~18 kW (~25 kW/kg) |
| Capacity / Wh/kg | Unchanged (745 Wh, ~1,050 Wh/kg) |

### Energy comparison (Common stone)

Ratios show how many times more energy the stone holds. Values above 1 mean the stone wins.

| Battery | Wh/kg | Wh/L | Stone ratio (mass) | Stone ratio (volume) |
|---|---|---|---|---|
| Alkaline | 100-150 | 300-500 | 7-10.5× | 5.6-9× |
| Lithium-ion | 100-270 | 250-700 | 3.9-10.5× | 4-11× |
| Lithium iron phosphate | 90-180 | 220-450 | 5.8-11.7× | 6-12.6× |
| Silicon-anode Li-ion | 300-500 | 800-1,300 | 2.1-3.5× | 2.1-3.5× |
| Solid-state lithium metal | 350-500 | 800-1,000 | 2.1-3× | 2.8-3.5× |
| Lithium primary | 280-500 | 500-1,200 | 2.1-3.8× | 2.3-5.6× |
| Zinc-air | 300-450 | 1,000-1,600 | 2.3-3.5× | 1.7-2.8× |
| Lithium-sulfur | 400-600 | 400-600 | 1.75-2.6× | 4.6-7× |
| Lithium-air (projected practical) | 1,000-1,700 | n/a | 0.6-1.05× | n/a |
| Lithium-air (theoretical with discharge product) | ~3,500 | n/a | 0.3× | n/a |
| Gasoline (chemical) | ~12,000 | ~9,700 | 0.09× | 0.29× |
| Gasoline (useful work after engine losses) | 2,500-3,500 | n/a | 0.3-0.42× | n/a |

### Power comparison

| Source | Burst power (kW/kg) | Recharge |
|---|---|---|
| Li-ion energy cell | 0.3-1 | 30 min to several hours from a charger |
| Li-ion power cell | 2-10 | 15-60 min from a charger |
| Supercapacitor | 10-20 | Seconds from a charger |
| Fist stone, Q 1 | ~284 | ~13 min from ambient mana |
| Walnut stone, Q 1 | ~755 | ~5 min from ambient mana |
| Marble stone, Q 1 | ~1,400 | ~2.7 min from ambient mana |
| Fist stone, Q 10 | ~2,840 | ~2.4 min from ambient mana |

| Source | Indefinite output (kW/kg) |
|---|---|
| Any battery | 0 (must be recharged externally) |
| Fist stone, Q 1 | ~4.7 |
| Walnut stone, Q 1 | ~12.6 |
| Marble stone, Q 1 | ~23.6 |

### Summary

- **Energy:** beats every commercial battery by 2× to 12×. Matches projected lithium-air. Loses to theoretical battery limits and gasoline. Wh/kg stays ~1,050 at every Q (mass fixed).
- **Burst power:** 14× to 140× a supercapacitor per kilogram at Q 1. Higher Q multiplies amp at the same mass.
- **Sustained power:** no battery equivalent. A Q 1 fist stone runs 3.4 kW indefinitely, about 2.7 average US homes.
- **Sharding:** splitting a stone keeps total capacity and multiplies surface area. Sustainable power per kilogram scales with 1/radius.
- **Not electricity by default.** Voltage needs a converter path or rune. Wear lands on the path, not as battery cycle fade.
- **Market:** hunt / buy / slot stones; no gigafactory.

### Rule of thumb

| Need | Prefer |
|---|---|
| Dense reusable mana for gear / spells | Mana stone (walnut+ for ~100 kJ-class dumps; fist for MJ-class) |
| True electrical voltage without mana | Voltaic / Daniell / dry cell invent |
| Consumer portable on Earth terms | Alkaline → Li-ion ladder (this file) |
| Absolute ceiling Wh/kg fantasy | Li-air theory, or Common stones already near practical Li-air |

---

## Summary Table

| Era | Battery | Chemistry | Energy density (Wh/kg) | Notes |
|---|---|---|---|---|
| ~250 BC to AD 650 | "Baghdad battery" | Copper/iron in acidic liquid | Negligible | Disputed. May never have been used as a battery |
| 1800 | Voltaic pile | Zinc/copper discs with brine-soaked cloth | Negligible | First true battery (Alessandro Volta) |
| 1836 | Daniell cell | Zinc/copper with two electrolytes | ~10 | Stable voltage. Powered telegraphs |
| 1866 | Leclanché cell | Zinc/manganese dioxide wet cell | ~20 | Precursor to the dry cell |
| 1886 | Zinc-carbon dry cell | Zinc/MnO₂ paste | 35-100 | First portable consumer battery |
| 1901 | Nickel-iron | Nickel/iron/alkaline | 30-50 | Edison battery. Nearly indestructible |
| 1959 | Alkaline | Zinc/MnO₂/potassium hydroxide | 100-150 | Standard AA/AAA (Lewis Urry) |
| 1960s | Silver-oxide | Zinc/silver oxide | 130 | Watch and calculator button cells |
| 1960s | Sodium-sulfur | Molten sodium/sulfur at ~300 °C | 150-240 | Grid storage. Must run hot |
| 1970s | Lithium primary | Lithium metal with MnO₂ or thionyl chloride | 280-500 | Non-rechargeable. Long shelf life |
| 1970s | Zinc-air (primary) | Zinc/oxygen from air | 300-450 | Hearing aid cells |
| 1989 | Nickel-metal hydride (NiMH) | Nickel/metal hydride alloy | 60-120 | Early hybrids |
| 1991 | Lithium-ion | Graphite anode/lithium metal oxide cathode | 100-270 | Phones, laptops, EVs |
| 1996 | Lithium iron phosphate (LFP) | Graphite/LiFePO₄ | 90-180 | Safer. Longer-lived |
| 1997 | Lithium polymer | Li-ion with gel/polymer electrolyte | 100-265 | Flexible pouch shapes |
| 2020s | Silicon-anode Li-ion | Silicon-rich anode | 300-500 | Drones, aerospace |
| 2023 | Sodium-ion | Hard carbon/sodium layered oxide | 100-160 | No lithium or cobalt |
| Mid-2020s | Solid-state lithium metal | Lithium metal anode with solid electrolyte | 350-500 | Pilot production |
| Emerging | Lithium-sulfur | Lithium/sulfur | 400-600 practical (2,600 theoretical) | Short cycle life |
| Emerging | Aluminum-air | Aluminum/oxygen | 300-1,300 practical (8,100 theoretical) | Mechanically refueled |
| Theoretical | Lithium-air with graphene cathode | Lithium/oxygen, graphene porous cathode | 1,000-1,700 projected practical. ~3,500 theoretical with discharge product. ~11,400 lithium alone | Top of the chart |

**Build categories used below**

- **Home-buildable:** assembled from hardware store, auto parts or chemistry supply materials.
- **Industrial:** requires dry rooms, inert gas, high temperature or toxic material handling. The production process is described.
- **Laboratory:** exists only as research cells.

---

## 1. Baghdad Battery (~250 BC to AD 650)

**Home-buildable**

**Materials:** clay jar about 13 cm tall, copper sheet, iron rod, wax or asphalt, vinegar or grape juice.

1. Roll the copper sheet into a tube that fits inside the jar. Seal one end with a copper disc set in wax or asphalt.
2. Stand the tube upright in the jar.
3. Suspend the iron rod in the center of the tube so it does not touch the copper. Hold it with a wax or asphalt plug at the top.
4. Fill the tube with vinegar.

**Output:** 0.5 to 2 V at a few milliamps. Copper is positive. Iron is negative.

---

## 2. Voltaic Pile (1800)

**Home-buildable**

**Materials:** zinc discs or galvanized washers, copper discs or US pennies minted before 1982 (95% copper), cardboard or felt discs, strong salt water or vinegar.

1. Soak the cardboard discs in salt water.
2. Stack in repeating order: copper, wet cardboard, zinc. Each set of three is one cell.
3. Clamp the stack between two insulated plates.
4. Attach a wire to the bottom copper disc (positive) and the top zinc disc (negative).

**Output:** 0.7 to 1 V per cell. Ten cells light a red LED.

---

## 3. Daniell Cell (1836)

**Home-buildable**

**Materials:** glass jar, unglazed porous clay pot, copper sheet, zinc strip, copper sulfate, zinc sulfate (dilute salt water works as a weaker substitute).

1. Line the inside wall of the jar with the copper sheet. Fill the jar with saturated copper sulfate solution.
2. Set the porous pot in the center. Fill it with zinc sulfate solution.
3. Place the zinc strip in the pot.
4. Connect copper (positive) and zinc (negative).

**Output:** 1.1 V, very steady. Add copper sulfate crystals to extend run time.

**Gravity cell variant:** no porous pot. Copper sits at the bottom in dense copper sulfate solution. Zinc hangs at the top in lighter zinc sulfate solution. The density difference keeps the layers apart.

---

## 4. Leclanché Cell (1866)

**Home-buildable**

**Materials:** glass jar, porous pot, zinc rod, carbon rod, manganese dioxide powder, graphite powder, ammonium chloride.

1. Mix manganese dioxide and graphite powder. Pack the mix around the carbon rod inside the porous pot.
2. Fill the jar with saturated ammonium chloride solution.
3. Set the pot in the jar. Place the zinc rod in the solution beside it.
4. Connect carbon (positive) and zinc (negative).

**Output:** about 1.5 V. Recovers voltage after resting. Suited to doorbells and telegraphs.

---

## 5. Zinc-Carbon Dry Cell (1886)

**Home-buildable**

**Materials:** zinc cup or zinc sheet formed into a cup, carbon rod (salvaged from a dead zinc-carbon D cell), manganese dioxide powder, graphite powder, ammonium chloride or zinc chloride, flour or starch, paper, wax.

1. Make a paste of ammonium chloride solution thickened with flour. Coat paper with it. Line the inside of the zinc cup with the coated paper. This is the separator.
2. Mix manganese dioxide and graphite at roughly 8:1 by weight. Dampen with ammonium chloride solution until it packs like wet sand.
3. Stand the carbon rod in the center of the cup. Pack the mix firmly around it.
4. Seal the top with melted wax. Leave the rod tip exposed.

**Output:** 1.5 V.

**Industrial method:** zinc cans are deep-drawn, lined with starch-paste or coated-paper separators, filled with pressed cathode mix around a carbon rod, sealed with asphalt or plastic and jacketed.

---

## 6. Nickel-Iron (1901)

**Home-buildable with difficulty. Potassium hydroxide is strongly caustic.**

**Materials:** nickel hydroxide powder, graphite or nickel flake, iron powder or iron oxide, perforated nickel-plated steel tubes or pockets, 20 to 25% potassium hydroxide solution (lithium hydroxide additive improves life), steel or plastic container.

1. **Positive plate:** pack nickel hydroxide mixed with nickel flake or graphite into perforated tubes. Mount the tubes on a steel frame.
2. **Negative plate:** pack iron powder or iron oxide into perforated flat pockets. Mount on a frame.
3. Interleave the plates with insulating spacers. Place them in the container.
4. Fill with potassium hydroxide solution.
5. Form with several full charge and discharge cycles.

**Output:** 1.2 V per cell. Survives overcharge, deep discharge and decades of use.

---

## 7. Alkaline (1959)

**Industrial**

1. **Can:** nickel-plated steel can, serving as the positive terminal.
2. **Cathode:** electrolytic manganese dioxide and graphite are pressed into rings and inserted against the can wall.
3. **Separator:** non-woven fabric tube inserted inside the cathode ring.
4. **Anode:** zinc powder in a potassium hydroxide gel is injected into the center.
5. **Current collector:** a brass nail is pushed into the anode gel through a plastic seal.
6. **Closure:** the can is crimped shut and labeled.

**Output:** 1.5 V.

---

## 8. Silver-Oxide (1960s)

**Industrial**

1. **Cathode:** silver oxide mixed with graphite, pressed into a pellet.
2. **Anode:** zinc powder gel.
3. **Electrolyte:** potassium hydroxide (high drain) or sodium hydroxide (low drain, longer life).
4. **Assembly:** stacked in a steel button can with separator and gasket, then crimped.

**Output:** 1.55 V.

---

## 9. Sodium-Sulfur (1960s)

**Industrial only. Molten sodium reacts violently with water and air.**

1. **Separator:** beta-alumina ceramic tube, sintered at about 1,600 °C. It conducts sodium ions while blocking electrons.
2. **Anode:** liquid sodium fills the inside of the ceramic tube.
3. **Cathode:** sulfur impregnated into carbon felt surrounds the tube.
4. **Case:** sealed steel housing with corrosion-resistant lining.
5. **Operation:** modules are insulated and heated to 300 to 350 °C to keep both electrodes molten.

**Output:** 2.08 V per cell.

---

## 10. Lithium Primary (1970s)

**Industrial. Lithium metal ignites in contact with water.**

**Lithium manganese dioxide (Li-MnO₂):**

1. Heat-treated manganese dioxide is mixed with carbon and binder, then pressed onto a stainless steel or aluminum mesh.
2. Lithium foil is rolled thin and pressed onto a current collector.
3. Electrodes are wound with a polypropylene separator in a dry room below 1% humidity.
4. Organic electrolyte (lithium perchlorate in propylene carbonate and dimethoxyethane) is added. The can is sealed.

**Output:** 3.0 V.

**Lithium thionyl chloride (Li-SOCl₂):** thionyl chloride serves as both cathode material and electrolyte. A porous carbon electrode collects current. Output is 3.6 V with the highest energy density of any common primary cell.

---

## 11. Zinc-Air (1970s)

**Home-buildable**

**Materials:** zinc powder or zinc sheet, activated carbon, potassium hydroxide solution (strong salt water for a weaker version), stainless steel or nickel mesh, coffee filter, PTFE plumber's tape, small binder amount (PTFE suspension or white glue).

1. **Air cathode:** mix activated carbon with a small amount of binder. Press it onto the steel mesh. Cover the outer face with plumber's tape. The tape lets air in and keeps liquid from leaking out.
2. **Separator:** coffee filter soaked in electrolyte.
3. **Anode:** zinc powder mixed into electrolyte as a paste, or a zinc sheet.
4. **Stack:** zinc, separator, carbon cathode. Keep the taped side open to air.
5. Connect the mesh (positive) and zinc (negative).

**Output:** 1.2 to 1.4 V.

**Industrial method:** zinc powder gel fills a button can. A cathode of carbon, manganese oxide catalyst and PTFE sits under air holes covered by a sealing tab. Pulling the tab activates the cell.

---

## 12. Nickel-Metal Hydride (1989)

**Industrial**

1. **Negative electrode:** hydrogen-absorbing alloy (AB5 type such as lanthanum-nickel with rare earths) coated onto nickel foam or perforated nickel-plated steel.
2. **Positive electrode:** nickel hydroxide with cobalt additives pasted onto nickel foam.
3. **Assembly:** wound with a polypropylene separator into a cylindrical can.
4. **Electrolyte:** potassium hydroxide.
5. **Sealing and formation:** sealed with a safety vent, then cycled to activate the alloy.

**Output:** 1.2 V.

---

## 13. Lithium-Ion (1991)

**Industrial. Small coin cells can be assembled in a laboratory glovebox.**

1. **Cathode slurry:** active material (lithium cobalt oxide, NMC or NCA) is mixed with carbon black and PVDF binder in NMP solvent.
2. **Anode slurry:** graphite is mixed with carbon black and CMC/SBR binder in water.
3. **Coating:** cathode slurry is coated onto aluminum foil. Anode slurry is coated onto copper foil. Both are oven-dried.
4. **Calendering:** coated foils are roll-pressed to precise thickness and density, then slit to width.
5. **Assembly:** in a dry room, electrodes are wound (cylindrical and prismatic cells) or stacked (pouch cells) with a porous polyethylene/polypropylene separator.
6. **Electrolyte fill:** lithium hexafluorophosphate dissolved in carbonate solvents (EC, DMC, EMC) is injected.
7. **Sealing:** the can or pouch is sealed.
8. **Formation:** slow first charges build the solid electrolyte interphase (SEI) layer on the anode. Cells are aged for weeks and graded by capacity.

**Output:** 3.6 to 3.7 V nominal.

---

## 14. Lithium Iron Phosphate (1996)

**Industrial**

Same production line as lithium-ion with these changes:

1. **Cathode material:** lithium iron phosphate is synthesized as nanoparticles and coated with carbon, since the raw material conducts electricity poorly.
2. Cathode coating, assembly and formation follow the lithium-ion process.

**Output:** 3.2 V nominal. Thousands of cycles. Resistant to thermal runaway.

---

## 15. Lithium Polymer (1997)

**Industrial**

Same electrode production as lithium-ion with these changes:

1. **Electrolyte:** liquid electrolyte is absorbed into a polymer matrix (commonly PVDF-HFP) to form a gel.
2. **Assembly:** electrode and separator layers are laminated into a flat stack.
3. **Packaging:** the stack is heat-sealed in an aluminum-laminated plastic pouch instead of a metal can.

**Output:** 3.7 V nominal. Can be made thin and in custom shapes.

---

## 16. Silicon-Anode Lithium-Ion (2020s)

**Industrial**

Same production line as lithium-ion with a modified anode:

1. **Anode material:** silicon nanoparticles, silicon-carbon composites, silicon oxide or silicon nanowires replace some or all graphite. Silicon swells up to 300% when charged, so nanoscale structures are required to prevent cracking.
2. **Binder:** elastic binders such as polyacrylic acid hold the anode together through swelling.
3. **Nanowire method:** silicon nanowires are grown directly on the current collector by chemical vapor deposition (used by Amprius).
4. **Prelithiation:** extra lithium is added to the anode before assembly to offset losses in the first cycle.

**Output:** 3.6 to 3.7 V nominal.

---

## 17. Sodium-Ion (2023)

**Industrial**

Same production line as lithium-ion with these changes:

1. **Anode:** hard carbon made by pyrolyzing biomass, resins or coal pitch at 1,000 to 1,500 °C.
2. **Cathode:** layered sodium metal oxide, Prussian white or a polyanion compound.
3. **Current collectors:** aluminum foil on both electrodes. Sodium does not alloy with aluminum, so copper is unnecessary.
4. **Electrolyte:** sodium hexafluorophosphate in carbonate solvents.
5. Cells can be stored and shipped at 0 V.

**Output:** about 3.0 to 3.2 V nominal.

---

## 18. Solid-State Lithium Metal (Mid-2020s)

**Industrial (pilot production)**

1. **Solid electrolyte:** sulfide (such as argyrodite Li₆PS₅Cl), oxide (such as LLZO garnet) or polymer. Sulfides release hydrogen sulfide on contact with moisture, so production runs in argon or ultra-dry rooms.
2. **Composite cathode:** active cathode material is mixed with solid electrolyte powder and conductive carbon, then coated or pressed.
3. **Separator layer:** a thin solid electrolyte film is cast or pressed between electrodes.
4. **Anode:** thin lithium metal foil. In anode-free designs, bare copper is used and lithium plates onto it from the cathode during the first charge.
5. **Pressing:** layers are pressed at high pressure to maintain solid-to-solid contact. Finished cells are held under stack pressure.

**Output:** 3.7 to 4.0 V nominal.

---

## 19. Lithium-Sulfur (Emerging)

**Industrial (early production)**

1. **Sulfur host:** sulfur is melted at about 155 °C and infused into porous carbon so it fills the pores.
2. **Cathode:** the sulfur-carbon composite is mixed with binder and coated onto aluminum foil.
3. **Anode:** lithium metal foil.
4. **Electrolyte:** ether-based (dioxolane and dimethoxyethane) with LiTFSI salt and lithium nitrate additive. The additive protects the lithium surface from dissolved polysulfides.
5. **Assembly:** stacked in pouch cells in a dry room.

**Output:** about 2.1 V nominal. Main problem is the polysulfide shuttle, where dissolved sulfur compounds migrate and erode capacity.

---

## 20. Aluminum-Air (Emerging)

**Home-buildable (simple version)**

**Materials:** aluminum foil, activated charcoal, saturated salt water, paper towel, wire.

1. Lay a sheet of aluminum foil flat.
2. Place a paper towel soaked in saturated salt water on the foil.
3. Pile damp activated charcoal on the paper towel. Keep it from touching the foil.
4. Press one wire into the charcoal (positive). Clip another to the foil (negative).

**Output:** 0.5 to 1 V per cell. Several in series run a small LED or motor.

**Industrial method:**

1. **Anode:** aluminum alloyed with small amounts of gallium, indium or tin to prevent the oxide layer that normally stops aluminum from reacting.
2. **Air cathode:** carbon with manganese oxide or silver catalyst, backed by a PTFE breathable membrane.
3. **Electrolyte:** potassium hydroxide or saline solution, often circulated.
4. **Refueling:** spent aluminum plates are removed and replaced. The aluminum hydroxide product is sent back to smelters for recycling.

---

## 21. Lithium-Air with Graphene Cathode (Theoretical)

**Laboratory**

1. **Graphene oxide production:** graphite is oxidized in sulfuric acid and potassium permanganate (Hummers method), then exfoliated into graphene oxide sheets.
2. **Porous cathode:** graphene oxide is freeze-dried or hydrothermally reduced into an aerogel or foam. This creates a light, conductive scaffold with a very large internal surface.
3. **Catalyst (optional):** the graphene is doped with nitrogen or decorated with ruthenium, platinum or manganese oxide particles to speed the oxygen reactions.
4. **Assembly in argon glovebox:** lithium metal foil anode, glass-fiber separator soaked in ether electrolyte (TEGDME with LiTFSI), graphene cathode on a perforated current collector.
5. **Oxygen supply:** the cell is sealed with an oxygen inlet. Research cells use pure dry oxygen, since moisture and carbon dioxide in ambient air poison the reaction.
6. **Operation:** discharge forms lithium peroxide inside the graphene pores. Charging decomposes it back to lithium and oxygen.

**Output:** about 2.7 V on discharge. Current lab cells last tens to a few hundred cycles. A practical version needs an air-purifying membrane, a stable electrolyte and a protected lithium anode.
