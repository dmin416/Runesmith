# Materials Reference: Processing and Science

Coverage: tungsten, carbon, bronze, steel, silver, copper, gold, titanium, tin, vanadium, iron, zinc, brass, sodium, sulfur, phosphorus and sea minerals.

Values are standard reference figures at room temperature and 1 atm unless stated. Alloy values are ranges because composition varies.

Hub: `Materials.md` (Terra tags). Abundance lists: `CommonElements.md`. Ore geography: `../Science/Metallurgy/MetalOres.md`. Grade physics / vacuum: `../Science/Metallurgy/EarthAlloys.md`. Alloy recipes: `../Science/Metallurgy/CommonAlloys.md`. Toxic swaps / disposal: `../Science/Metallurgy/ToxicMetalSubstitutes.md`. Focused metal notes: `../Science/Metallurgy/Brass.md`, `../Science/Metallurgy/Silver.md`, `../Science/Metallurgy/Titanium.md`, `../Science/Metallurgy/TitaniumProcessing.md`, `../Science/Metallurgy/CraftMetal.md`. Metallurgy nav: `../Science/Metallurgy/Index.md`. Science root: `../Science/Science.md`.

**Ownership:** this file = element science, history, fire temps, tech levels, hazards, nonmetals, seawater. Grade tables and melt checklists → `CommonAlloys.md`. Vacuum / grade physics → `EarthAlloys.md`. Canon Ti Kroll → `TitaniumProcessing.md`.

**Status:** design loot. Earth processing and property reference. Gate street stock with Materials.md tags.

---

## Contents

1. Quick Reference Tables
2. Core Processing Concepts
3. Precious and Ancient Metals: Gold, Silver, Copper, Tin
4. Iron and Steel
5. Zinc and Brass
6. Bronze
7. Refractory and Modern Metals: Titanium, Vanadium, Tungsten
8. Nonmetals: Carbon, Sulfur, Phosphorus
9. Sodium
10. Sea Minerals
11. Technology Level Requirements
12. Material Interconnections

---

## 1. Quick Reference Tables

### Physical Properties

| Material | Type | Symbol / Composition | Density (g/cm³) | Melting Point (°C) | Boiling Point (°C) | Mohs Hardness |
|---|---|---|---|---|---|---|
| Gold | Element | Au, Z=79 | 19.30 | 1,064 | 2,970 | 2.5-3 |
| Silver | Element | Ag, Z=47 | 10.49 | 962 | 2,162 | 2.5-3 |
| Copper | Element | Cu, Z=29 | 8.96 | 1,085 | 2,562 | 3 |
| Tin | Element | Sn, Z=50 | 7.29 | 232 | 2,602 | 1.5 |
| Iron | Element | Fe, Z=26 | 7.87 | 1,538 | 2,862 | 4 |
| Zinc | Element | Zn, Z=30 | 7.14 | 420 | 907 | 2.5 |
| Titanium | Element | Ti, Z=22 | 4.51 | 1,668 | 3,287 | 6 |
| Vanadium | Element | V, Z=23 | 6.11 | 1,910 | 3,407 | 6.7 |
| Tungsten | Element | W, Z=74 | 19.25 | 3,422 | 5,555 | 7.5 |
| Bronze | Alloy | Cu + ~12% Sn (typical) | 8.7-8.9 | 880-1,050 | n/a | 3-4 |
| Brass | Alloy | Cu + 30-40% Zn (typical) | 8.4-8.7 | 900-940 | n/a | 3-4 |
| Steel | Alloy | Fe + 0.05-2.1% C | 7.75-8.05 | 1,370-1,540 | n/a | 4-8 |
| Carbon (graphite) | Element | C, Z=6 | 2.09-2.23 | Sublimes ~3,640 | n/a | 1-2 |
| Carbon (diamond) | Element | C, Z=6 | 3.51 | Converts to graphite before melting at 1 atm | n/a | 10 |
| Sulfur | Element | S, Z=16 | 2.07 | 115 | 445 | 2 |
| Phosphorus (white) | Element | P, Z=15 | 1.82 | 44 | 281 | ~0.5 (waxy) |
| Phosphorus (red) | Element | P, Z=15 | 2.2-2.3 | Sublimes ~416-590 | n/a | ~2 |
| Sodium | Element | Na, Z=11 | 0.97 | 98 | 883 | 0.5 |
| Seawater | Mixture | ~35 g dissolved salts per kg | ~1.025 | Freezes ~-1.9 | ~100.6 | n/a |

### Conductivity (pure elements, ~20 °C)

| Element | Electrical Resistivity (nΩ·m) | Thermal Conductivity (W/m·K) |
|---|---|---|
| Silver | 15.9 | 429 |
| Copper | 16.8 | 401 |
| Gold | 22.1 | 318 |
| Sodium | 47.7 | 142 |
| Tungsten | 52.8 | 173 |
| Zinc | 59 | 116 |
| Iron | 97 | 80 |
| Tin | 115 | 67 |
| Vanadium | 197 | 31 |
| Titanium | 420 | 22 |

Lower resistivity means better electrical conduction. Diamond conducts heat better than any metal (~2,000 W/m·K) yet is an electrical insulator.

### Approximate Crustal Abundance

| Element | Parts per million in Earth's crust |
|---|---|
| Iron | ~56,000 |
| Sodium | ~23,600 |
| Titanium | ~5,650 |
| Phosphorus | ~1,050 |
| Sulfur | ~350 |
| Carbon | ~200 |
| Vanadium | ~120 |
| Zinc | ~70 |
| Copper | ~60 |
| Tin | ~2.3 |
| Tungsten | ~1.3 |
| Silver | ~0.075 |
| Gold | ~0.004 |

Abundance does not equal availability. Titanium is common yet was not produced as a metal until the 20th century because it is so hard to reduce. Tin is rare yet was traded across continents in the Bronze Age because its ore is easy to smelt.

### Typical Tensile Strength

| Material | Ultimate Tensile Strength (MPa) |
|---|---|
| Annealed copper | ~210 |
| Commercially pure titanium (Grade 2) | ~345 |
| Brass | ~300-550 |
| Bronze | ~350-650 |
| Mild steel | ~400-550 |
| Ti-6Al-4V titanium alloy | ~900-1,000 |
| Hardened tool steel | ~1,500-2,000+ |
| Drawn tungsten wire | Up to ~4,000 |

---

## 2. Core Processing Concepts

- **Ore:** Rock containing a mineral worth extracting. Most metals occur as oxides, sulfides, carbonates or silicates.
- **Beneficiation / concentration:** Raising ore grade before smelting. Methods include crushing, washing, gravity separation (panning, sluicing, jigging), magnetic separation and froth flotation.
- **Roasting:** Heating sulfide ore in air to convert it to oxide and drive off sulfur as SO₂.
- **Reduction:** Removing oxygen from a metal oxide. Carbon (as charcoal or coke) is the classic reducing agent and works as carbon monoxide gas inside the furnace.
- **Smelting:** Reduction at temperatures high enough to melt the metal or the waste.
- **Flux:** Material added to make waste rock melt into a fluid slag. Limestone is the standard flux for iron. Silica is used for copper.
- **Slag:** The glassy waste layer that floats on molten metal.
- **Cupellation:** Oxidizing lead away from silver or gold in a porous bone-ash or clay dish.
- **Leaching:** Dissolving a metal out of ore with a chemical solution (acid, cyanide, ammonia).
- **Electrowinning / electrorefining:** Using electric current to deposit pure metal from solution onto a cathode.
- **Electrolysis of molten salts:** Required for very reactive metals such as sodium, magnesium and aluminum.
- **Work hardening:** Metals become harder and more brittle as they are hammered or bent.
- **Annealing:** Heating and slow cooling (or for copper, any cooling) to restore softness.
- **Quenching:** Rapid cooling in water, brine or oil. Hardens steel. Softens copper and some brasses.
- **Tempering:** Reheating quenched steel to trade some hardness for toughness.
- **Sintering / powder metallurgy:** Pressing metal powder and heating below the melting point so particles bond. Essential for tungsten.
- **Alloy:** A mixture of a metal with other elements. Alloys are often harder and lower-melting than their base metal.

### Fire Temperatures for Reference

| Heat Source | Approximate Max Temperature (°C) |
|---|---|
| Campfire | 600-900 |
| Charcoal pit or open hearth, no bellows | ~900-1,000 |
| Charcoal furnace with bellows | 1,100-1,300 |
| Bloomery furnace | 1,200-1,400 |
| Crucible steel furnace | ~1,500-1,600 |
| Coke blast furnace | 1,500-2,000 at the tuyeres |
| Electric arc furnace | 3,000+ in the arc |

---

## 3. Precious and Ancient Metals

### 3.1 Gold (Au)

**Science**
- Atomic number 79. Face-centered cubic (FCC) crystal.
- Noble metal: does not oxidize or tarnish in air or water. Dissolves in aqua regia (3:1 HCl:HNO₃), in cyanide solutions with oxygen and in mercury (amalgam).
- Most malleable metal. One gram can be beaten into a sheet of roughly 1 m². Gold leaf can be ~0.1 µm thick and transmits greenish light.
- Yellow color comes from relativistic effects on its electrons that shift light absorption into the blue.
- Formed in neutron star mergers and supernovae through the rapid neutron capture (r-process).

**Occurrence**
- Usually found native (as the metal), often alloyed with silver (natural alloy with >20% silver is called electrum).
- Lode gold: veins in quartz. Placer gold: grains and nuggets eroded into rivers.
- Also locked in sulfide minerals such as pyrite and arsenopyrite ("refractory" gold) and as tellurides.

**Processing: Historical**
- **Panning and sluicing:** Gold's density (19.3) lets water wash away lighter sand. Sheepskins in streams caught fine gold (a possible origin of the Golden Fleece myth).
- **Crushing and washing:** Quartz ore was crushed in mortars or stamp mills and then washed.
- **Amalgamation:** Crushed ore mixed with mercury. Gold dissolves into the mercury. The amalgam is heated to boil off mercury (357 °C), leaving sponge gold. Highly toxic.
- **Cementation (parting):** Salt and brick dust packed with gold and heated to remove silver as silver chloride. Used by ancient Lydians for coinage.
- **Parting with acid:** Nitric acid dissolves silver from gold-silver alloys. Works best when silver is ~3 parts to 1 part gold ("quartation").

**Processing: Modern**
- **Cyanide leaching** (MacArthur-Forrest process, 1887): 4Au + 8NaCN + O₂ + 2H₂O → 4Na[Au(CN)₂] + 4NaOH.
- Gold is recovered from solution by activated carbon (carbon-in-pulp or carbon-in-leach) or by zinc dust precipitation (Merrill-Crowe).
- **Heap leaching** for low-grade ore: cyanide solution trickled through piles of crushed rock.
- Refractory ores are first roasted, pressure-oxidized or bio-oxidized by bacteria to free gold from sulfides.
- **Refining:** Miller process bubbles chlorine through molten gold to ~99.5%. Wohlwill process electrolyzes in chloroauric acid to 99.999%.
- **Assay:** Fire assay (melt with lead flux, cupel the lead away, weigh the bead) remains the standard.

**Alloys and Purity**
| Karat | Gold Content |
|---|---|
| 24k | 99.9% |
| 22k | 91.7% |
| 18k | 75.0% |
| 14k | 58.3% |
| 10k | 41.7% |

Copper makes rose gold. Palladium or nickel makes white gold. Silver makes green-yellow gold.

**Uses:** Currency, jewelry, electronics contacts, dentistry, radiation and heat shielding (spacecraft visors), catalysis.

**Hazards:** Metallic gold is inert. Processing hazards are mercury vapor and cyanide.

---

### 3.2 Silver (Ag)

**Science**
- Atomic number 47. FCC crystal.
- Highest electrical conductivity, thermal conductivity and visible-light reflectivity of any element.
- Tarnishes by reacting with sulfur compounds (H₂S) to form black silver sulfide (Ag₂S), not by oxidation.
- Silver ions are antimicrobial (the oligodynamic effect).
- Silver halides darken in light, the basis of film photography.

**Occurrence**
- Native silver, acanthite/argentite (Ag₂S), horn silver (AgCl) and silver-bearing galena (lead sulfide).
- Most silver today is a byproduct of lead, zinc, copper and gold mining.

**Processing: Historical**
- **Lead smelting and cupellation:** Silver-bearing lead ore smelted to lead bullion. Bullion heated in a porous bone-ash cupel with air blown over it at ~1,000 °C. Lead oxidizes to litharge (PbO), which is absorbed or skimmed. Silver remains as a bright bead. Used since ~3000 BCE.
- **Liquation:** Lead added to silver-bearing copper. Heated just above lead's melting point so silver-rich lead drains away from solid copper. Then cupelled.
- **Patio process** (1554, Bartolomé de Medina, Mexico): Crushed ore mixed with mercury, salt and copper sulfate on open courtyards, trampled by mules for weeks. Silver forms amalgam. Mercury is distilled off. Drove the Spanish colonial silver economy.
- **Parkes process** (1850): Zinc added to molten lead. Silver concentrates in the zinc, which floats as a crust. Zinc is distilled away.

**Processing: Modern**
- Recovered from anode slimes during copper and lead electrorefining.
- Cyanide leaching for silver ores.
- Electrolytic refining (Moebius or Balbach-Thum cells) reaches 99.99%.

**Alloys:** sterling / Britannia / coin and solder grades in `../Science/Metallurgy/CommonAlloys.md`. Shop reactivity and optics: `../Science/Metallurgy/Silver.md`.

**Uses:** Currency, jewelry, mirrors, electrical contacts, solar panels, brazing alloys, photography, antimicrobial coatings.

**Hazards:** Chronic ingestion of silver compounds causes argyria (permanent blue-gray skin).

---

### 3.3 Copper (Cu)

**Science**
- Atomic number 29. FCC crystal.
- Second-best electrical conductor. Standard wiring metal.
- Reddish color. Forms a green patina (basic copper carbonate and sulfate) outdoors over years.
- Work-hardens quickly. Softens when annealed regardless of cooling speed (unlike steel).
- Antimicrobial surface.

**Occurrence**
- Native copper (Lake Superior region, historically).
- Oxide and carbonate ores: malachite (green), azurite (blue), cuprite (red).
- Sulfide ores: chalcopyrite (CuFeS₂, most important today), chalcocite (Cu₂S), bornite.
- Modern ores often contain only 0.5-1% copper.

**Processing: Historical**
- **Cold hammering of native copper** (~8000 BCE onward).
- **Smelting of oxide/carbonate ores** (~5000 BCE): Malachite heated with charcoal at ~1,100 °C in a crucible or small furnace. Carbon monoxide reduces it to metal.
- **Sulfide smelting:** Ore roasted to drive off sulfur, then smelted. Repeated roast-and-smelt cycles produced matte and eventually "black copper" (~95%).
- **Arsenical copper:** Smelting mixed arsenic ores produced harder copper alloys before tin bronze.

**Processing: Modern (Sulfide Route, ~80% of production)**
1. **Crushing and grinding** to fine powder.
2. **Froth flotation:** Chemicals make copper minerals water-repellent. Air bubbles carry them to the surface. Concentrate reaches ~25-35% Cu.
3. **Smelting** at ~1,200 °C with silica flux produces copper matte (Cu₂S·FeS, ~50-70% Cu). Iron goes to slag.
4. **Converting:** Air blown through matte oxidizes remaining iron and sulfur. Produces blister copper (~98.5%), named for SO₂ blisters on its surface.
5. **Fire refining** removes oxygen and sulfur. Copper is cast into anodes.
6. **Electrorefining:** Anodes dissolve in sulfuric acid/copper sulfate. Pure copper (99.99%) plates onto cathodes. Gold, silver and platinum collect in anode slime.

**Processing: Modern (Oxide Route, ~20%)**
- Heap leaching with sulfuric acid, solvent extraction and electrowinning (SX-EW).

**Uses:** Wiring, motors, plumbing, heat exchangers, roofing, coins, alloys (bronze, brass, cupronickel, beryllium copper).

**Hazards:** Toxic in excess and highly toxic to aquatic life. Smelting releases SO₂ and arsenic.

---

### 3.4 Tin (Sn)

**Science**
- Atomic number 50.
- Two common allotropes:
  - **White (β) tin:** Metallic, tetragonal, stable above 13.2 °C.
  - **Gray (α) tin:** Brittle, powdery, diamond-cubic, forms slowly below 13.2 °C. The conversion is called **tin pest** and is fastest around -30 to -40 °C.
- Makes a crackling sound when bent ("tin cry") from crystal twinning.
- Low melting point (232 °C) and resists corrosion.

**Occurrence**
- Almost entirely from cassiterite (SnO₂), a heavy (density ~7) black or brown mineral.
- Occurs in granite-related veins and in placer deposits ("stream tin") because its weight concentrates it in riverbeds.
- Rare globally. Historical sources included Cornwall, Brittany, Iberia, Bohemia, Central Asia and Southeast Asia.

**Processing: Historical**
- Stream tin panned or sluiced from gravels.
- Smelted with charcoal in small shaft furnaces at ~1,000-1,200 °C: SnO₂ + 2C → Sn + 2CO.
- One of the easiest metals to smelt from its ore.
- **Liquation refining:** Crude tin heated on a sloped hearth just above 232 °C. Pure tin melts and runs off. Iron-rich and copper-rich impurities stay solid.
- **Poling:** Stirring molten tin with green wood poles. Escaping gases carry impurities to the surface.

**Processing: Modern**
- Gravity separation and flotation to concentrate.
- Reverberatory or electric furnace smelting with carbon.
- Refining by liquation, poling or electrolysis to 99.9%+.

**Alloys**
- Bronze (with copper).
- Pewter: 85-99% tin with antimony and copper (older pewter contained lead).
- Solder: Traditional 63Sn/37Pb eutectic melts at 183 °C. Modern lead-free SAC solder is tin with silver and copper.
- Babbitt metal: Tin-antimony-copper bearing alloy.
- Tinplate: Steel coated with thin tin for cans.

**Uses:** Solder, tinplate, bronze, pewter, float glass production (molten tin bath), organotin chemicals.

**Hazards:** Metallic tin has low toxicity. Organotin compounds are highly toxic.

---

## 4. Iron and Steel

### 4.1 Iron (Fe)

**Science**
- Atomic number 26. Most abundant element in Earth by mass (~32%, concentrated in the core).
- Ferromagnetic below its Curie point of 770 °C.
- Allotropes by temperature:
  - **α-iron (ferrite):** Body-centered cubic (BCC) below 912 °C. Holds very little carbon.
  - **γ-iron (austenite):** FCC from 912 to 1,394 °C. Holds up to 2.14% carbon.
  - **δ-iron:** BCC from 1,394 °C to melting at 1,538 °C.
- These phase changes are the reason steel can be heat-treated.
- Rusts readily: iron + oxygen + water → hydrated iron(III) oxide. Rust is porous and flakes, so corrosion continues.

**Occurrence**
- Hematite (Fe₂O₃, red), magnetite (Fe₃O₄, black, magnetic), goethite and limonite (hydrated oxides, yellow-brown), siderite (FeCO₃).
- **Bog iron:** Iron oxides precipitated in wetlands by bacteria. Major early source in northern Europe.
- **Meteoritic iron:** Iron-nickel metal from meteorites. Used before smelting existed (e.g., Tutankhamun's dagger).

**Processing: Historical**
- **Bloomery** (~1200 BCE onward in the Near East):
  - Clay shaft furnace charged with alternating layers of charcoal and roasted ore.
  - Bellows push temperatures to ~1,200-1,300 °C. Iron does not fully melt.
  - CO reduces the ore in solid state. Slag melts and drains.
  - Result is a spongy **bloom** of iron mixed with slag.
  - Bloom is reheated and hammered repeatedly to squeeze out slag and consolidate the metal into **wrought iron**.
  - Carbon content is uneven. Some parts are effectively steel.
- **Blast furnace** (China ~5th century BCE; Europe ~1300s CE):
  - Taller furnace with stronger air blast reaches temperatures that fully melt iron.
  - Molten iron absorbs ~4% carbon, producing **pig iron / cast iron**. Brittle but castable.
  - Limestone flux binds impurities into slag.
- **Coke smelting** (Abraham Darby, 1709): Coke (baked coal) replaced charcoal. Removed the limit set by forest supply.
- **Finery forge and puddling** (Henry Cort, 1784): Molten pig iron stirred in a reverberatory furnace so air burns out carbon. Produced wrought iron at industrial scale.

**Processing: Modern**
- **Blast furnace chemistry:**
  - C + O₂ → CO₂; CO₂ + C → 2CO
  - Fe₂O₃ + 3CO → 2Fe + 3CO₂
  - CaCO₃ → CaO + CO₂; CaO + SiO₂ → CaSiO₃ (slag)
- Hot metal (~4.5% C) is tapped and sent to steelmaking.
- **Direct reduced iron (DRI):** Ore reduced in solid state by natural gas or hydrogen. Feeds electric arc furnaces.

**Forms of Iron**
| Product | Carbon Content | Character |
|---|---|---|
| Wrought iron | <0.08% plus slag fibers | Tough, forgeable, weldable, rust-resistant for iron |
| Steel | 0.05-2.1% | Strong, heat-treatable |
| Cast iron | 2.1-4.5% | Hard, brittle, castable, good in compression |

**Hazards:** Carbon monoxide in furnaces. Iron overdose is dangerous to children.

---

### 4.2 Steel

**Science**
- Iron alloyed with carbon (0.05-2.1%) and often other elements.
- Strength comes from carbon atoms in the iron lattice and from carbide (Fe₃C, cementite) particles.
- **Iron-carbon phase diagram key points:**
  - **727 °C (A1, lower critical):** Below this, steel is ferrite + cementite.
  - **0.76-0.8% C (eutectoid):** Cooling austenite slowly at this composition forms pearlite, layered ferrite and cementite.
  - **1,147 °C, 4.3% C (eutectic):** Lowest melting point of iron-carbon alloys. Basis of cast iron.
- **Microstructures:**
  - **Pearlite:** Slow cooling. Moderate strength.
  - **Bainite:** Intermediate cooling. Strong and tough.
  - **Martensite:** Rapid quench from austenite. Carbon trapped in a distorted body-centered tetragonal lattice. Very hard and brittle.
  - **Tempered martensite:** Quenched then reheated. Hard and tough.
- **Magnet test:** Steel becomes nonmagnetic near its hardening temperature (Curie point 770 °C). Smiths use this to judge quench heat for plain carbon steels.

**Carbon grades, temper colors, HT schedules and alloy recipes:** `../Science/Metallurgy/CommonAlloys.md`. Grade physics and vacuum steel: `../Science/Metallurgy/EarthAlloys.md`. Coal-shop HT practice: `../Science/Metallurgy/TraditionalBlacksmithing.md`.

**Processing history (gist)**
- Bloomery selection, carburizing, pattern welding, cementation / blister, Huntsman crucible and wootz / tamahagane routes made workable steel before mass air-blast processes.
- Industrial mass steel: Bessemer → open hearth → basic oxygen furnace (~70% today) and electric arc furnace on scrap / DRI. Continuous casting then rolling.

**Uses:** Construction, vehicles, ships, tools, weapons, machinery, cookware, medical instruments.

---

## 5. Zinc and Brass

### 5.1 Zinc (Zn)

**Science**
- Atomic number 30. Hexagonal close-packed (HCP) crystal.
- Brittle at room temperature. Malleable between 100 and 150 °C.
- **Boils at 907 °C**, below the temperature needed to reduce its ore. This is the central problem of zinc smelting.
- More reactive than iron, so it corrodes first when the two touch. This **sacrificial protection** is the basis of galvanizing.
- Essential human nutrient.

**Occurrence**
- Sphalerite (ZnS, "zinc blende"), main ore today.
- Smithsonite (ZnCO₃) and hemimorphite. Historically both were called **calamine**.
- Usually found with lead and silver ores.

**Processing: Historical**
- **Problem:** In an open furnace, zinc vapor escapes and burns to white zinc oxide ("philosopher's wool"). Ancient smelters found it as a furnace deposit but could not collect the metal.
- **Indirect use:** Calamine was used to make brass without isolating zinc (see cementation below).
- **Downward distillation** (Zawar, India, from roughly the 9th-12th centuries CE): Clay retorts filled with roasted ore and charcoal were inverted over condenser vessels. Zinc vapor dripped down into a cool chamber and condensed as liquid metal.
- **China** produced zinc in quantity by the 1600s.
- **Europe:** William Champion patented a distillation process in England in 1738.

**Processing: Modern**
- **Roast-Leach-Electrowin (~90% of production):**
  1. Sphalerite roasted to zinc oxide (ZnO) at ~900-1,000 °C. SO₂ captured to make sulfuric acid.
  2. ZnO leached in sulfuric acid.
  3. Solution purified with zinc dust to remove copper, cadmium, cobalt and nickel.
  4. Electrolysis plates zinc onto aluminum cathodes at 99.99% purity.
- **Imperial Smelting Process:** Blast furnace with lead splash condenser. Recovers zinc and lead together.

**Uses**
- Galvanizing steel (hot-dip in molten zinc at ~450 °C). Over half of all zinc use.
- Brass and other alloys. Die-casting alloys (Zamak).
- Batteries, zinc oxide (sunscreen, rubber vulcanization, paint), roofing.

**Hazards:** Inhaling fresh zinc oxide fume causes **metal fume fever** (flu-like illness) in welders and brass founders.

---

### 5.2 Brass

**Science**
- Copper-zinc alloy. Usually 5-45% zinc.
- **Phases:**
  - **α-brass** (<~35-37% Zn): FCC, ductile, cold-workable. Ideal for drawing and stamping.
  - **α-β (duplex) brass** (~37-45% Zn): Harder, best hot-worked.
- Color shifts from reddish (low zinc) to golden yellow (high zinc).
- Good acoustic properties, low friction, does not spark against steel easily, machines well.
- Melting point (~900-940 °C) is close to zinc's boiling point. Zinc fumes off during melting and must be replaced.

**Grades and melt recipes:** `../Science/Metallurgy/CommonAlloys.md`. Caldris shop melt / fittings: `../Science/Metallurgy/Brass.md`. Vacuum melt science: `../Science/Metallurgy/EarthAlloys.md` (Brass). Lead-free swaps: `../Science/Metallurgy/ToxicMetalSubstitutes.md`.

**Processing history (gist)**
- **Cementation:** sealed calamine + charcoal + copper below copper melt; Zn vapor diffuses into solid Cu (cap ~28-33% Zn). Roman orichalcum coins used this route.
- **Speltering:** once metallic zinc existed, Cu melt + Zn direct alloy allowed higher, precise Zn.
- **Modern:** induction melt Cu, add Zn last, cast billets, extrude / roll / draw. Heavy scrap recycle.

**Uses:** Musical instruments, ammunition, plumbing, locks, valves, decorative hardware, marine fittings, low-friction gears.

**Failure Modes**
- **Dezincification:** Zinc leaches out in some waters, leaving weak porous copper.
- **Season cracking:** Stress corrosion cracking in ammonia environments (identified in British cartridge cases in India).

---

## 6. Bronze

**Science**
- Classically copper-tin alloy, usually 5-20% tin. The standard tin bronze is ~88% Cu, 12% Sn.
- Tin dissolves in copper's α-phase up to roughly 14% at equilibrium. Higher tin forms hard brittle δ-phase.
- Harder and stronger than copper. Melts lower than copper, which improves casting.
- Expands slightly on solidifying, so it fills molds and captures fine detail.
- Low friction. Resists seawater corrosion. Develops a stable green patina.
- Low-tin bronze can be hammer-hardened. Bronze Age sword edges were cold-worked for hardness.
- Color shifts from copper-red toward silvery white as tin increases.

**Historical Development**
- **Arsenical bronze** (~4000 BCE onward): Copper with 1-5% arsenic. Harder than copper but fumes are toxic.
- **Tin bronze** (~3300 BCE onward in the Near East): Defined the Bronze Age. Required long-distance tin trade because tin ore is rare.
- **Bronze Age collapse** (~1200-1150 BCE) disrupted tin trade networks. Iron, which uses locally available ore, spread afterward.

**Types and recipes:** bell, gunmetal, phosphor, aluminum and silicon bronzes in `../Science/Metallurgy/CommonAlloys.md`. Lead-free bearing / statuary swaps: `../Science/Metallurgy/ToxicMetalSubstitutes.md`.

**Processing history (gist)**
- Co-smelt Cu+Sn ores, mix metals in a crucible (~1,100 °C), or cement cassiterite into molten copper with charcoal.
- Cast in open stone, two-piece molds or lost-wax. Finish by hammer, anneal, grind, polish.
- Modern: induction melt with P deoxidizers; sand, investment, continuous and centrifugal casting.

**Uses:** Bearings and bushings, ship propellers, sculpture, bells, cymbals, springs, electrical connectors, medals, historical weapons and armor.

---

## 7. Refractory and Modern Metals

### 7.1 Titanium (Ti)

**Science**
- Atomic number 22.
- **Allotropes:** α-titanium (HCP) below 882 °C. β-titanium (BCC) above.
- Density 4.51 g/cm³: about 57% of steel's density with comparable strength in alloy form. Highest strength-to-weight ratio of common structural metals.
- Forms a thin, self-healing TiO₂ layer that makes it extremely corrosion resistant, including in seawater and chlorine.
- Biocompatible: bone grows onto it (osseointegration). Standard for implants.
- Low thermal and electrical conductivity for a metal.
- **Anodizing** thickens the oxide layer. Light interference produces blue, purple, gold and other colors without dyes.
- At high temperature it absorbs oxygen, nitrogen and hydrogen, which embrittle it. Can burn in pure nitrogen.

**Occurrence**
- Ilmenite (FeTiO₃) and rutile (TiO₂). Often concentrated in beach sands.
- 9th most abundant element in the crust.
- Over 90% of titanium ore becomes TiO₂ white pigment, not metal.

**Why It Was Hard to Produce**
- Carbon cannot cleanly reduce TiO₂. It forms titanium carbide and leaves oxygen dissolved in the metal.
- Molten titanium reacts with almost every crucible material.
- Discovered 1791 (William Gregor). Named 1795 (Martin Klaproth). First pure metal 1910 (Matthew Hunter, sodium reduction).

**Industrial sponge / mill (canon Kroll, Hunter, VAR, grades):** `../Science/Metallurgy/TitaniumProcessing.md`. Geology and USGS: `../Science/Metallurgy/Titanium.md`. Low-tech invent path: `../Science/Metallurgy/TitaniumBootstrap.md`. Grade physics: `../Science/Metallurgy/EarthAlloys.md`. Alloy tables: `../Science/Metallurgy/CommonAlloys.md`.

Batch Mg (or Na) reduction of TiCl₄ makes porous sponge that must be vacuum-remelted. That chain, not ore scarcity, sets the metal price.

**Fabrication notes:** argon shield for welds; heat stays at the tool edge so machining galls; fines and powder are flammable.

**Uses:** Aircraft airframes and engines, spacecraft, implants, chemical plants, desalination, sporting goods, jewelry, pigment.

---

### 7.2 Vanadium (V)

**Science**
- Atomic number 23. BCC crystal.
- Hard, silvery-gray, ductile when pure.
- Forms compounds in four oxidation states with distinct colors in solution: +2 violet, +3 green, +4 blue, +5 yellow. Named after Vanadís (the Norse goddess Freyja) for this color range.
- Forms hard vanadium carbide (VC) in steel. Small amounts refine grain size.

**History**
- Discovered 1801 by Andrés Manuel del Río in Mexico. Rediscovered and named in 1830 by Nils Sefström.
- Pure metal first isolated in 1867 (Henry Roscoe).
- Ford Model T (1908) used vanadium steel for lightweight strength.

**Occurrence**
- Vanadiferous titanomagnetite (main source). Also vanadinite, patronite and carnotite.
- Concentrated in some crude oils, coal and oil sands. Recovered from combustion residues.
- Main producers: China, Russia, South Africa, Brazil.

**Processing**
1. **Source material:** Usually slag from steelmaking with vanadium-bearing iron ore, or ore concentrate.
2. **Salt roasting:** Roasted with sodium carbonate or sodium chloride at ~800-900 °C to form water-soluble sodium vanadate.
3. **Leaching:** Water or dilute acid dissolves the vanadate.
4. **Precipitation:** Ammonium salts precipitate ammonium metavanadate.
5. **Calcination:** Heated to form vanadium pentoxide (V₂O₅), the main commercial product.
6. **Ferrovanadium:** V₂O₅ reduced with aluminum (aluminothermic reaction) together with iron for steelmaking.
7. **Pure vanadium:** Calcium reduction of V₂O₅, aluminothermic reduction plus vacuum refining, or the iodide (van Arkel) process.

**Uses**
- ~85-90% goes into steel: high-strength low-alloy steel, tool steel, chrome-vanadium wrenches, rebar.
- Titanium alloy Ti-6Al-4V.
- V₂O₅ catalyst for sulfuric acid production (contact process).
- Vanadium redox flow batteries for grid storage.

**Hazards:** V₂O₅ dust is toxic and irritates the respiratory tract.

---

### 7.3 Tungsten (W)

**Science**
- Atomic number 74. BCC crystal.
- **Highest melting point of any metal (3,422 °C)** and highest boiling point of any element.
- Density 19.25 g/cm³, nearly identical to gold (used in counterfeit gold bars).
- Among the lowest thermal expansion of pure metals.
- Brittle at room temperature. Its ductile-to-brittle transition sits well above room temperature. Ductile tungsten requires heavy mechanical working.
- Oxidizes in air above ~400-500 °C. The oxide becomes volatile at high temperature. Hot tungsten needs inert gas or vacuum.
- **Tungsten carbide (WC):** Mohs ~9, density ~15.6. One of the hardest practical engineering materials.

**Names**
- "Tungsten" is Swedish for "heavy stone."
- Symbol **W** from **wolfram**. German tin smelters found the mineral wolframite reduced their tin yield, "devouring tin like a wolf."

**History**
- Isolated 1783 by the Elhuyar brothers in Spain, who reduced tungsten oxide with charcoal.
- Ductile tungsten wire developed by William Coolidge at General Electric (1909). Made incandescent light bulbs practical.

**Occurrence**
- Wolframite ((Fe,Mn)WO₄) and scheelite (CaWO₄). Scheelite fluoresces blue-white under UV, which helps prospectors.
- China produces ~80% of world supply.

**Processing**
1. **Concentration:** Gravity separation (both ores are dense), flotation for scheelite, magnetic separation for wolframite.
2. **Digestion:** Wolframite with hot sodium hydroxide. Scheelite with soda ash in autoclaves. Produces sodium tungstate solution.
3. **Purification:** Solvent extraction or ion exchange converts it to ammonium tungstate.
4. **Crystallization:** Ammonium paratungstate (APT), the main traded intermediate.
5. **Calcination:** APT heated to tungsten oxide (WO₃ or "blue oxide").
6. **Hydrogen reduction:** Oxide reduced by hydrogen at ~700-1,000 °C in tube furnaces. Produces tungsten metal powder. Particle size is controlled by temperature and gas flow.
7. **Consolidation (powder metallurgy):** Melting is impractical. Powder is pressed into bars and sintered by passing electric current through them (~3,000 °C), or sintered in hydrogen furnaces.
8. **Working:** Sintered bars hot-swaged and drawn into wire or rolled into sheet. Working makes it more ductile.

**Tungsten Carbide Production**
- Tungsten powder mixed with carbon black and heated to ~1,400-1,600 °C to form WC.
- **Cemented carbide:** WC powder mixed with 3-12% cobalt binder, pressed and liquid-phase sintered at ~1,350-1,500 °C.

**Uses**
- Cemented carbide cutting tools, drill bits, mining tools (~60% of use).
- Tool steels (high-speed steel: classic T1 grade is 18% W, 4% Cr, 1% V).
- Light bulb filaments, X-ray tube targets, TIG welding electrodes, rocket nozzles.
- Armor-piercing penetrators, counterweights, radiation shielding.
- Heavy alloys (tungsten with nickel-iron or nickel-copper binder).

**Hazards:** Fine dust inhalation. Cobalt in cemented carbide grinding dust causes "hard metal lung disease."

---

## 8. Nonmetals

### 8.1 Carbon (C)

**Science**
- Atomic number 6. Forms four bonds, which allows chains, rings and the whole basis of organic chemistry.
- **Allotropes:**
  | Form | Structure | Key Properties |
  |---|---|---|
  | Graphite | Stacked sheets of hexagons | Soft, lubricating, conducts electricity along sheets |
  | Diamond | 3D tetrahedral network | Hardest natural material, best thermal conductor, electrical insulator |
  | Amorphous carbon | Disordered | Charcoal, soot, lampblack, coke |
  | Graphene | Single graphite sheet | Extremely strong, highly conductive |
  | Fullerenes | Closed cages (C₆₀) | Molecular carbon |
  | Nanotubes | Rolled graphene | Very high tensile strength |
- Graphite is the stable form at surface conditions. Diamond is metastable but converts extremely slowly.
- Does not melt at 1 atm. Graphite sublimes at ~3,640 °C.
- **Carbon-14:** Radioactive isotope with a half-life of ~5,730 years. Basis of radiocarbon dating.

**Occurrence**
- Coal, petroleum, natural gas, limestone and dolomite (carbonates), atmospheric CO₂, all living matter.
- Natural graphite in metamorphic rock (the Borrowdale deposit in England supplied early pencils from the 1500s).
- Diamonds form ~150-200 km deep and reach the surface in kimberlite pipes. Also found in placer gravels.

**Processing: Charcoal**
- Wood heated with limited air (pyrolysis) at ~300-500 °C or higher.
- Water, tar and volatile gases drive off. Leaves ~70-90% carbon.
- **Traditional clamp kiln:** Wood stacked in a mound, covered with turf and earth, lit through a central flue and allowed to smolder for days. Colliers watched it constantly to prevent flare-ups.
- Yields only ~15-25% of wood mass. Large-scale ironmaking stripped forests.
- **Hardwood charcoal** is denser and preferred for smelting. **Willow or alder charcoal** was preferred for gunpowder.

**Processing: Coke**
- Coal baked at ~1,000-1,100 °C without air for 12-36 hours.
- Drives off volatiles (coal gas, tar, ammonia). Leaves strong porous carbon that holds up under the weight of a blast furnace charge.

**Processing: Other Forms**
- **Lampblack / carbon black:** Collected soot from burning oils. Used in inks and tires.
- **Activated carbon:** Charcoal treated with steam at ~800-1,000 °C or chemicals to create huge internal surface area (500-1,500 m²/g). Used for filtering.
- **Synthetic graphite** (Acheson process): Petroleum coke heated electrically to ~2,500-3,000 °C.
- **Synthetic diamond:**
  - HPHT: ~5-6 GPa and ~1,300-1,600 °C with a metal catalyst.
  - CVD: Methane and hydrogen plasma deposits diamond layer by layer at low pressure.
- **Carbon fiber:** Polyacrylonitrile (PAN) fibers stabilized in air at ~200-300 °C, carbonized at ~1,000-1,500 °C in inert gas and optionally graphitized at up to ~3,000 °C.

**Uses:** Fuel, reducing agent for metals, steel alloying, electrodes, lubricants, pencils, abrasives and cutting tools (diamond), filters, composites, gunpowder.

**Hazards:** Carbon monoxide from incomplete combustion. Coal and charcoal dust can explode.

---

### 8.2 Sulfur (S)

**Science**
- Atomic number 16. Pale yellow, brittle, odorless solid (the "rotten egg" smell is hydrogen sulfide, H₂S).
- Forms S₈ rings.
- **Allotropes:**
  - **Rhombic (α):** Stable below 95.3 °C.
  - **Monoclinic (β):** Stable from 95.3 °C to melting at ~119 °C.
  - **Plastic sulfur:** Rubbery chains made by pouring molten sulfur into cold water.
- Molten sulfur behaves unusually: it becomes far more viscous around 160-190 °C as rings open into long polymer chains, then thins again at higher temperature.
- Burns with a blue flame to sulfur dioxide (SO₂).
- Electrical insulator.
- Historically called **brimstone** ("burning stone").

**Occurrence**
- Native sulfur near volcanoes and fumaroles and in salt dome caprock.
- Sulfide minerals (pyrite, galena, sphalerite, chalcopyrite) and sulfates (gypsum).
- Hydrogen sulfide in "sour" natural gas and crude oil.

**Processing: Historical**
- Hand-collected from volcanic deposits.
- **Sicilian calcarone:** Sulfur ore piled in sloping kilns. Part of the sulfur was burned to melt the rest, which ran out at the bottom. Wasteful and produced choking SO₂.
- **Distillation/refining:** Crude sulfur melted or sublimed. Vapor condensed as **flowers of sulfur** (fine powder).
- Recovered as a byproduct of roasting sulfide ores.

**Processing: Frasch Process (1894 to early 2000s)**
- Three concentric pipes drilled into underground deposits.
- Superheated water (~165 °C) melts the sulfur.
- Compressed air pushes molten sulfur to the surface at >99% purity.
- Largely abandoned once petroleum sources took over.

**Processing: Claus Process (dominant today)**
- Recovers sulfur from hydrogen sulfide removed from natural gas and oil refining.
- Step 1: Burn one-third of H₂S: 2H₂S + 3O₂ → 2SO₂ + 2H₂O
- Step 2: React with remaining H₂S over a catalyst: 2H₂S + SO₂ → 3S + 2H₂O
- Over 90% of modern sulfur comes from this route.

**Sulfuric Acid (main use)**
- Historically "oil of vitriol," made by heating green vitriol (iron sulfate) or by the lead chamber process.
- **Contact process (modern):**
  1. Burn sulfur to SO₂.
  2. Oxidize SO₂ to SO₃ over V₂O₅ catalyst at ~400-450 °C.
  3. Absorb SO₃ in concentrated sulfuric acid to form oleum.
  4. Dilute oleum to the desired strength.
- Sulfuric acid is the most produced industrial chemical in the world.

**Uses**
- Sulfuric acid (~85-90% of sulfur use), mostly for phosphate fertilizer.
- Rubber vulcanization (Goodyear, 1839).
- Black powder: classic ratio 75% potassium nitrate, 15% charcoal, 10% sulfur.
- Fungicides, matches, pharmaceuticals, metal leaching.

**Hazards:** SO₂ and H₂S are toxic. H₂S deadens the sense of smell at high concentration. Sulfur dust is explosive. Burning sulfur is hard to extinguish.

---

### 8.3 Phosphorus (P)

**Science**
- Atomic number 15. Never found free in nature because it is too reactive.
- **Allotropes:**
  | Form | Structure | Properties |
  |---|---|---|
  | White (yellow) | P₄ tetrahedra | Waxy, glows in the dark, ignites in air ~30 °C, extremely toxic |
  | Red | Polymeric chains | Stable, less toxic, does not self-ignite |
  | Violet (Hittorf's) | Complex polymer | Intermediate |
  | Black | Layered sheets | Most stable, semiconductor, made under high pressure |
- White phosphorus glow is **chemiluminescence** from slow oxidation, not phosphorescence.
- White phosphorus converts to red when heated to ~250-300 °C without air.
- Stored under water because it does not react with water but burns in air.
- Essential to life: DNA and RNA backbones, ATP, cell membranes, bones and teeth (hydroxyapatite).

**History**
- Discovered 1669 by Hennig Brand in Hamburg while seeking the philosopher's stone.
- **Brand's method:** Boiled down large quantities of urine, let it putrefy, reduced it to a paste and heated it strongly with sand and charcoal. Phosphorus vapor condensed under water. Yield was tiny (roughly a few grams from many hundreds of liters).
- 1769-1771: Gahn and Scheele found phosphorus in bone. Production shifted to **bone ash** treated with sulfuric acid, then heated with charcoal.
- 1888: Electric furnace process using phosphate rock.

**Occurrence**
- Phosphate rock (fluorapatite and other apatites) in sedimentary deposits.
- Guano and bone historically.
- Morocco (with Western Sahara) holds roughly 70% of world reserves.

**Processing: Elemental Phosphorus (Thermal Process)**
- Phosphate rock, silica (sand) and coke heated in an electric arc furnace at ~1,400-1,500 °C:
  - 2Ca₃(PO₄)₂ + 6SiO₂ + 10C → 6CaSiO₃ + 10CO + P₄
- Phosphorus vapor condensed under water as white phosphorus.
- Very electricity-intensive.

**Processing: Wet Process (Fertilizer Route, main use)**
- Phosphate rock reacted with sulfuric acid → phosphoric acid + gypsum.
- Waste **phosphogypsum** is stockpiled in huge stacks because it is mildly radioactive.
- Phosphoric acid neutralized with ammonia to make fertilizers (MAP, DAP) or treated to make superphosphate.

**Uses**
- Fertilizer (~80-90% of phosphate rock).
- Matches: Red phosphorus on the striking strip of safety matches. White phosphorus matches were banned in the early 20th century.
- Food-grade phosphoric acid (soft drinks), detergents (now restricted), flame retardants, steel and bronze deoxidizing (phosphor bronze), pesticides.
- Military incendiaries and smoke screens (white phosphorus).

**Hazards**
- White phosphorus burns cause deep chemical and thermal injury. Re-ignites when exposed to air.
- Chronic exposure caused **"phossy jaw"** (jaw bone necrosis) in 19th-century match workers.
- Some organophosphates are pesticides and nerve agents.

---

## 9. Sodium (Na)

**Science**
- Atomic number 11. Alkali metal. BCC crystal.
- Soft enough to cut with a knife. Freshly cut surface is silvery and tarnishes in seconds.
- Density below water (0.97). Floats.
- Reacts violently with water: 2Na + 2H₂O → 2NaOH + H₂. Heat can ignite the hydrogen.
- Stored under mineral oil or inert gas.
- Burns with an intense yellow-orange flame. The yellow sodium D-lines (~589 nm) dominate sodium vapor lamps and color any flame contaminated with salt.
- 6th most abundant element in Earth's crust. Essential for nerve signaling and fluid balance in animals.
- Never occurs as a free metal in nature.

**Occurrence**
- Halite (rock salt, NaCl), seawater and brines.
- Trona and natron (sodium carbonates). Natron was used in Egyptian mummification and early glass.
- Feldspars (albite) and other silicates.

**History**
- Isolated 1807 by Humphry Davy through electrolysis of molten sodium hydroxide using a large voltaic pile.
- **Deville process** (1850s): Sodium carbonate reduced with carbon in iron retorts at ~1,100 °C or higher. Sodium vapor distilled off. Used to make sodium for early aluminum production.
- **Castner process** (late 1880s): Electrolysis of molten sodium hydroxide.

**Processing: Downs Cell (1924, dominant today)**
- Electrolysis of molten sodium chloride.
- Calcium chloride added to lower the melting point from 801 °C to ~600 °C.
- Cathode (iron or steel ring): Na⁺ + e⁻ → Na (liquid sodium rises and is collected).
- Anode (graphite, center): 2Cl⁻ → Cl₂ + 2e⁻.
- A steel mesh diaphragm keeps sodium and chlorine apart so they do not recombine.

**Key Sodium Compounds and Their Production**
| Compound | Common Name | Production |
|---|---|---|
| NaCl | Salt | Mining, solar evaporation, vacuum evaporation of brine |
| NaOH | Lye, caustic soda | Chlor-alkali electrolysis of brine |
| Na₂CO₃ | Soda ash, washing soda | Solvay process (brine + ammonia + CO₂) or trona mining. Historically from plant ash and the Leblanc process |
| NaHCO₃ | Baking soda | From Solvay process or soda ash + CO₂ |
| NaNO₃ | Chile saltpeter | Atacama Desert deposits |
| Na₂SiO₃ | Water glass | Silica fused with soda ash |

**Uses of the Metal**
- Reducing agent for titanium, zirconium and other metals.
- Coolant in fast breeder nuclear reactors (liquid over a wide temperature range, good heat transfer).
- Sodium vapor street lamps.
- NaK (sodium-potassium alloy) liquid at room temperature for heat transfer.
- Organic synthesis and drying solvents.

**Hazards:** Sodium fires are Class D. Water, CO₂ and many foams make them worse. Dry sand, sodium chloride powder or graphite-based extinguishers are used.

---

## 10. Sea Minerals

### 10.1 Composition of Seawater

- Average salinity ~35 g of dissolved salts per kg of seawater (3.5%).
- Ratios of the major ions are nearly constant worldwide (Marcet's principle / principle of constant proportions).

**Major Dissolved Constituents (at 35 salinity)**
| Ion | g/kg seawater | % of dissolved salts |
|---|---|---|
| Chloride (Cl⁻) | 19.35 | ~55.0 |
| Sodium (Na⁺) | 10.78 | ~30.6 |
| Sulfate (SO₄²⁻) | 2.71 | ~7.7 |
| Magnesium (Mg²⁺) | 1.28 | ~3.7 |
| Calcium (Ca²⁺) | 0.41 | ~1.2 |
| Potassium (K⁺) | 0.40 | ~1.1 |
| Bicarbonate (HCO₃⁻) | ~0.14 | ~0.4 |
| Bromide (Br⁻) | 0.067 | ~0.2 |
| Strontium (Sr²⁺) | 0.008 | ~0.02 |
| Borate/Boron | ~0.0045 (as B) | ~0.01 |
| Fluoride (F⁻) | 0.0013 | <0.01 |

**Notable Trace Elements**
| Element | Approximate Concentration |
|---|---|
| Lithium | ~0.18 mg/L |
| Iodine | ~0.06 mg/L |
| Uranium | ~3.3 µg/L (billions of tonnes total in the ocean) |
| Gold | Parts-per-trillion range or lower |

- Fritz Haber tried to extract gold from seawater in the 1920s to pay German war reparations. Actual concentrations proved far too low.

### 10.2 Solar Evaporation and Sea Salt

**Precipitation Sequence (Usiglio, 1849)**
As seawater evaporates, salts crystallize in order of increasing solubility:

| Stage | Approx. Remaining Volume | Mineral Precipitated |
|---|---|---|
| 1 | ~50% | Calcium carbonate (CaCO₃) and iron oxides |
| 2 | ~20% | Gypsum (CaSO₄·2H₂O) |
| 3 | ~10% | Halite (NaCl), the bulk of sea salt |
| 4 | <~4% | Magnesium sulfate (epsomite), potassium and magnesium chlorides |

The leftover liquid after halite is **bittern**: bitter, magnesium-rich and potassium-rich.

**Saltworks Process**
1. Seawater fed into large shallow **concentrating ponds**.
2. Sun and wind evaporate water. Carbonate and gypsum settle out in early ponds.
3. Brine density tracked in degrees Baumé (°Bé). Seawater starts at ~3.5 °Bé.
4. Brine moved to **crystallizer pans** at ~25-26 °Bé, where halite precipitates.
5. Harvesting usually stops near ~29-30 °Bé so bitter magnesium salts do not contaminate the salt.
6. Salt raked, washed and dried.

**Traditional Methods**
- **Fleur de sel:** Delicate crystals skimmed by hand from the brine surface in calm weather.
- **Boiling (salt pans and salterns):** Brine boiled in lead or iron pans over fires. Used in cold climates.
- **Sleeching:** Salt-soaked sand collected from tidal flats and washed with seawater to make concentrated brine before boiling.
- **Seaweed ash:** Burned to recover salts.

**Sea Salt vs Refined Salt**
- Unrefined sea salt is ~95-98% NaCl plus magnesium, calcium, potassium sulfates and chlorides and moisture.
- Refined table salt is ~99%+ NaCl, often with added iodine and anti-caking agents.

### 10.3 Industrial Extraction from Seawater and Brines

**Magnesium (Dow Process, from 1941)**
1. Lime (from heated oyster shells, limestone or dolomite) added to seawater.
2. Magnesium hydroxide precipitates: Mg²⁺ + Ca(OH)₂ → Mg(OH)₂ + Ca²⁺.
3. Mg(OH)₂ filtered and dissolved in hydrochloric acid to form MgCl₂.
4. Dried MgCl₂ electrolyzed in molten form at ~700 °C. Magnesium metal and chlorine produced.
- Seawater supplied much of the Allied wartime magnesium for aircraft and incendiaries.
- Magnesium hydroxide from seawater is still used for refractory bricks.

**Bromine**
1. Brine acidified.
2. Chlorine oxidizes bromide: 2Br⁻ + Cl₂ → Br₂ + 2Cl⁻.
3. Air or steam blows bromine out.
4. Captured with sulfur dioxide, then re-released with chlorine for purification.
- Dead Sea and underground brines (Arkansas) are much richer sources than open seawater.

**Potassium**
- Recovered from bittern as sylvite (KCl) and carnallite (KMgCl₃·6H₂O). Major Dead Sea operation.
- Used as potash fertilizer.

**Magnesium Chloride (Nigari)**
- Concentrated bittern rich in MgCl₂.
- Traditional Japanese tofu coagulant. Also used for de-icing and dust control.

**Iodine**
- Seaweeds concentrate iodine thousands of times above seawater levels.
- Discovered 1811 by Bernard Courtois in seaweed ash while making saltpeter.
- Historically produced by burning kelp. Now mostly from Chilean nitrate deposits and Japanese natural gas brines.

**Soda and Potash from Sea Plants**
- Ash of saltwort, glasswort and kelp (**barilla** and **kelp ash**) was a major source of sodium carbonate for glass and soap until the Leblanc process (~1790s).

**Lithium**
- Present at low concentration. Seawater extraction is experimental.
- Commercial lithium comes from salt flat brines (evaporation ponds) and hard rock ores.

**Desalination Byproducts**
- Reverse osmosis and distillation plants produce concentrated brine with roughly double seawater salinity. Research aims to recover magnesium, lithium and other minerals from it.

### 10.4 Seafloor Mineral Deposits

| Deposit | Contents | Location |
|---|---|---|
| Manganese (polymetallic) nodules | Manganese, nickel, copper, cobalt, rare earths | Abyssal plains (e.g., Clarion-Clipperton Zone, Pacific) |
| Cobalt-rich crusts | Cobalt, manganese, platinum, tellurium | Seamount flanks |
| Seafloor massive sulfides | Copper, zinc, lead, gold, silver | Hydrothermal vents ("black smokers") at mid-ocean ridges |
| Phosphorites | Phosphate | Continental shelves |
| Placer deposits | Tin, gold, diamonds, titanium sands | Shallow coastal waters (Namibia diamonds, Indonesian tin) |
| Aragonite and shell sand | Calcium carbonate | Bahamas and tropical banks |

Nodules grow only a few millimeters per million years.

---

## 11. Technology Level Requirements

| Material | Earliest Practical Method | Max Heat Needed | Key Barrier |
|---|---|---|---|
| Gold | Panning native metal | ~1,064 °C to melt | None for placer gold |
| Copper | Native metal / charcoal smelting | ~1,100 °C | Bellows-driven furnace |
| Silver | Cupellation of lead ore | ~1,000 °C | Lead smelting knowledge |
| Tin | Charcoal smelting of cassiterite | ~1,000-1,200 °C | Finding rare ore |
| Bronze | Alloying copper and tin | ~1,100 °C | Tin trade |
| Iron (wrought) | Bloomery | ~1,200-1,300 °C | Forging skill to consolidate bloom |
| Iron (cast) | Blast furnace | ~1,500 °C | Strong air blast, large furnace |
| Steel | Carburizing, crucible, bloomery selection | ~1,200-1,600 °C | Carbon control, heat treatment knowledge |
| Zinc | Retort distillation with condenser | ~1,000-1,200 °C | Zinc vaporizes in open furnaces |
| Brass | Cementation with calamine | ~1,000 °C | Sealed crucibles |
| Carbon (charcoal) | Clamp kiln | ~300-500 °C | Wood supply |
| Sulfur | Collection near volcanoes, melting | ~120 °C | Locating deposits |
| Phosphorus | Urine or bone ash with charcoal | ~1,000+ °C | Chemistry knowledge, extreme danger |
| Sea salt | Solar evaporation or boiling | Sun or fire | Suitable climate or fuel |
| Sodium | Carbothermic reduction of soda (Deville) or electrolysis | ~1,100+ °C | Sealed iron retorts or electricity |
| Vanadium | Chemical extraction + aluminothermic or calcium reduction | Varies | Advanced chemistry, aluminum or calcium metal |
| Tungsten | Reduction of oxide powder | ~700-1,000 °C to reduce, ~3,000 °C to sinter | Cannot be melted by fire. Needs powder metallurgy and electric heating |
| Titanium | Kroll process | ~1,000 °C plus vacuum/argon melting | Chlorine chemistry, magnesium metal, inert atmosphere |

---

## 12. Material Interconnections

- **Carbon** reduces iron, copper, tin, zinc and phosphorus ores. Carbon content defines iron vs steel vs cast iron.
- **Sulfur** is a byproduct of copper, zinc and lead smelting and becomes sulfuric acid for leaching zinc and copper and for phosphate fertilizer.
- **Vanadium** catalyzes sulfuric acid production, strengthens steel and forms part of Ti-6Al-4V titanium alloy.
- **Tungsten** and vanadium both go into high-speed tool steel.
- **Sodium** historically reduced titanium (Hunter process) and aluminum (Deville). Sodium carbonate and sodium hydroxide digest tungsten and vanadium ores.
- **Sea minerals** supply sodium (via salt), magnesium (for the Kroll titanium process), chlorine (for titanium tetrachloride), bromine, potassium and iodine.
- **Zinc** separates silver from lead (Parkes process), precipitates gold from cyanide (Merrill-Crowe) and protects steel (galvanizing).
- **Lead** (not on the list) is the carrier for silver and gold in cupellation and fire assay.
- **Copper** is the base of bronze and brass. Copper refining yields silver and gold from anode slime.
- **Tin** plus copper made bronze. Tin coats steel (tinplate).
- **Phosphorus** deoxidizes bronze (phosphor bronze) and is an impurity that makes steel brittle when cold ("cold short").
- **Sulfur** is an impurity that makes steel crack when hot ("hot short"). Manganese counteracts it.
- **Limestone** (calcium carbonate, also a seawater precipitate) fluxes iron smelting and supplies lime for magnesium extraction.
