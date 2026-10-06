# Compressed Time Through Stimulation

> **Design loot.** Cost model under fermentation and aging speedups in `MagicalCooking.md`. No free time-accel version. Cast law: `../Runes/Energy.md` (**1 mana = 10 J**). Temporary mass: `../PotentialMagic/MassBoost.md`, `../Combat/ImpactRune.md`. Mana pool: `../Progression/Attributes.md`. Tough-cut / collagen wall: `MagicalMeatCookware.md`.

Lazy time magic speeds a process up time machine style by hand waving every requirement so nothing else changes. Time manipulation exists in this world but is not available to the practitioner. Acceleration comes from supplying every input and stimulating every participant until the process runs N times faster. Every flow lands on the ledger.

**Scope:** This file is the cost model under the fermentation and aging speedups in `MagicalCooking.md`. Any "speed up fermentation / aging" effect there is priced here. No free version exists.

**Canon pegs:**
- `../Runes/Energy.md`: 1 mana = 10 J. Useful = mana × 10 × η × A. Use the skill cast η or the rune η_cond, never both.
- Impact / MassBoost: compressed mana mass disperses when the feed stops.

---

## 1. The Core Rule

Stimulation never reduces what a process consumes or releases. Totals stay fixed. Rates multiply by the compression factor N.

| Flow | Natural case | Compressed by N |
|---|---|---|
| Food / substrate | Same total | Delivered N× faster |
| Oxygen, CO2, water, light | Trickles in by diffusion or daylight | N× flux through the same surfaces |
| Metabolic heat | Leaks away passively for free | N× power. Passive loss covers less of it |
| Toxic byproducts (ethanol, acid, salt stress) | Accumulate slowly | Hit lethal thresholds N× sooner |
| Cell machinery | Fixed max speed per enzyme and per division | Must be bolstered past its ceiling |
| Developmental programs | Staged by signals over time | Each stage must be driven in order |

Four walls appear in every case:

1. **Heat removal**
2. **Transport** through surfaces (gas, water, light), including shear, foam and pressure at high flux
3. **Biological speed caps**
4. **Divergent side reactions**: slow chemistry responds unevenly to heat so blunt heating warps the product. `MagicalMeatCookware.md`'s "tough cuts need time" is the same wall: collagen conversion and muscle protein reactions diverge when forced with heat alone.

---

## 2. Pricing Formula

All energy in this file is joules. Convert to mana with the `../Runes/Energy.md` peg:

> **mana = Useful ÷ (10 × η × A)**

Useful for a batch:

> **Useful = Q_cool + E_light + E_bolster + E_transport + E_temp_mass**

| Term | Meaning |
|---|---|
| Q_cool | Heat that must be actively removed (Section 3.5) |
| E_light | Direct mana energy fed to photosynthesis in place of photons |
| E_bolster | Energy driving organisms past their natural ceiling (Section 3.1) |
| E_transport | Work moving air, water and gas through the batch |
| E_temp_mass | Upkeep on mana-made temporary mass for its whole lifetime (Section 3.2) |

**Cast waste heat:** every cast loses (1 − η) of its spent energy as path waste at the work site. That waste joins Q_cool. A low-η caster pays twice: once in mana and again in extra cooling.

### Mana reference at η × A = 1

Baseline mage pool uses the canon mana pool formula (mages only): MP = (Intelligence × 10) + (Willpower × 4), with average stat 15 (`../Progression/Attributes.md`). A Tier 1 mage at Int 15 and Will 15 has (15 × 10) + (15 × 4) = 210 MP = 2,100 J. Class and skill bonuses raise this.

All figures in this table are planning feel at order-of-magnitude accuracy.

| Batch | Useful floor | Mana | Baseline mage pools |
|---|---|---|---|
| Vinegar 20 L, 720× | ~10.7 MJ cooling | ~1,070,000 | ~5,100 |
| Wine 20 L, 240× | ~2.4 MJ cooling | ~240,000 | ~1,140 |
| Lettuce head, ~45×, cooling only (light prepaid as stored sunlight) | ~4.4 MJ cooling | ~440,000 | ~2,100 |
| Lettuce head, ~45×, cooling + direct mana light | ~4.4 MJ cooling + ~4.4 MJ light | ~880,000 | ~4,200 |
| Oak, 100× (planning feel) | ~0.8 to 2 TJ light + cooling | ~80 to 200 billion | ~400 million to 1 billion |

These are floors before bolstering, transport and cast waste. High compression is a mana stone and runic vat operation, not a personal pool operation.

---

## 3. What Magic Supplies and What It Costs

### 3.1 Bolstering Organisms

Magic can push microbes and plants past their natural limits:

- Enzyme turnover speed
- Cell division speed
- Tolerance to ethanol, acid, salt and heat
- Gas and water uptake through membranes, roots and stomata

Feeding and ideal conditions get a process to its natural ceiling N_c for ingredient cost only. Bolstering pays only for the part past that ceiling.

> **Bolster power** P_b = k_b × m_living × (N ÷ N_c − 1)
>
> **Bolster total** E_bolster = P_b × (t_natural ÷ N) + cast waste

k_b is a world-tunable constant (joules per second per kg of living tissue per unit of overdrive). Power climbs with N. Total energy rises steeply just past N_c and then levels off because the compressed duration shrinks as N grows:

> **As N → ∞, E_bolster → k_b × m_living × t_natural ÷ N_c**

High N is not free on bolstering. It hits this ceiling while cooling keeps climbing because passive loss shrinks as 1/N.

What bolstering does **not** change:

- **Stoichiometry.** Bolstered yeast still makes the same CO2 and heat per gram of sugar. Bolstered Acetobacter still needs the same oxygen per gram of ethanol.
- **Energy end state.** Bolstering work ends up as heat. E_bolster adds directly to Q_cool.

### 3.2 Created Mass Is Temporary Mass

From Impact / MassBoost: compressed mana mass disperses when the feed stops. Created water, oxygen or CO2 is **paid continuous temporary mass**, not permanent matter. It costs upkeep every second it exists (E_temp_mass) and vanishes the moment the feed ends.

This produces the product rule as a direct consequence of existing law:

> **Anything that ends up in the final product must be real matter from the world. Mana-made mass is limited to scaffolding roles that leave before the feed stops.**

Safe uses of created mass: coolant, evaporative cooling, transport medium, flushing waste.

Unsafe uses: water inside lettuce cells or dough, oxygen bonded into acetic acid, carbon fixed into plant tissue. When the feed stops these disperse out of the product: the plant wilts, the bread dries, the vinegar weakens and the plant loses structural mass.

### 3.3 Real Water and Gases

Real means sourced from the world, by ambient intake or from storage:

- **Gases:** continuous real air forced through a culture is fine. Stored real CO2 from a brewery vent is fine. Mana-made gas that ends up in the product is not.
- **Water:** drawn from a well, reservoir, ground or air.

**Condensing water from air:**
- Releases ~2.26 MJ of condensation heat per kg, which joins Q_cool
- A closed 50 m³ room at 20°C and 50% humidity holds only ~0.43 kg of water vapor
- A single lettuce head at full compression needs ~10 L. Large pulls require outdoor air intake or a real water supply

### 3.4 Sun Energy

**Stored sunlight** (collected into stones over real time and area, released later)
- Pre-paid energy. The ledger tracks collection area × days, not mana
- 1 mol of photosynthetic photons ≈ 0.22 MJ
- A sunny summer day delivers ~40 to 60 mol per m²

**Direct mana energy into photosynthesis** (skipping photons)
- Bypasses leaf light saturation (~600 to 1,000 µmol/m²/s for lettuce) and photodamage
- Costs E_light ≥ the equivalent photon energy, priced through the mana formula
- Either way, most absorbed energy becomes heat. Plants store only a small fraction as biomass

### 3.5 Cooling

**Passive loss offsets cooling.** A vessel sheds heat to its surroundings for free. Active cooling pays only the remainder:

> **Q_cool = max(0, Q_total + cast waste − P_passive × t_natural ÷ N)**

**Passive power is roughly constant (W). Passive energy shed during the batch scales as 1/N.**

At low N passive loss covers almost everything. At high N the compressed duration is too short and nearly all heat must be removed actively. This is why cooling cost climbs with N even though total heat is fixed.

**Floor for active removal:**

- **Kitchen lock (default):** Useful ≥ Q_cool. Simple and conservative.
- **Earth rigor (refrigerator limit):** Useful ≥ Q_cool × (T_hot − T_cold) ÷ T_cold, with temperatures in kelvin. When the culture is warmer than the air it dumps into, this floor approaches zero and the real wall becomes heat transfer surface: fins, water jackets or circulating coolant. Use this version only if the setting wants refrigeration engineering to matter.

### 3.6 Who Does It

| Operator | Efficiency source | Strength | Weakness |
|---|---|---|---|
| Kitchen mage | Skill cast η | Flexible, can rebalance pathways mid-batch | Limited by personal MP and attention |
| Runic vat | Rune η_cond | Continuous, runs on mana stones, repeatable | Fixed to one process and one pathway balance |
| Mage running a runic vat | Rune η_cond for the vat feed, skill η for the mage's own casts | Precision plus endurance | Each energy path uses one η only. The two never stack on the same path |

---

## 4. Per-Process Bills

### 4.1 Vinegar: 20 L at 6%, 1 month → 1 hour (720×)

| Item | Amount | Source |
|---|---|---|
| Ethanol | ~1 kg | Real wine or beer |
| Oxygen | 0.7 kg | Real air, continuously forced through |
| Heat released | ~10.7 MJ (~493 kJ per mol ethanol) | Q_cool |
| Heat power | ~4 W natural → **~3 kW compressed** | Active cooling |
| Oxygen turnover | Water holds ~8 mg/L, so dissolved O2 is replaced ~4,000 times in the hour | Forced aeration |
| Biology | Acetobacter die above ~35°C and die quickly if oxygen stops | Bolster heat and oxygen tolerance |

Uncooled, 20 L climbs ~2°C per minute and the culture is dead in under 10 minutes.

**Transport violence:** thousands of oxygen turnovers per hour means violent sparging. Bubble shear strips the bacterial film, foam rises out of the vessel and dead zones between bubbles go anoxic locally. Bolstered uptake does not fix shear or foam.

**Cheap sweet spot:** at 30× (1 day) heat power is ~124 W. A 20 L vessel in a water bath sheds that passively, so Q_cool ≈ 0 and the batch costs ingredients plus aeration work.

### 4.2 Wine / Beer: 20 L at 22 Brix, 10 days → 1 hour (240×)

| Item | Amount | Source |
|---|---|---|
| Sugar | 4.4 kg | Real fruit, honey or malt |
| Products | ~2.1 kg ethanol + ~1,070 L CO2 gas | CO2 vents at ~18 L per minute |
| Heat released | ~2.4 MJ | Q_cool |
| Heat power | ~3 W natural → **~670 W compressed** | Active cooling |
| Biology | Real immobilized yeast tops out ~50 g ethanol/L/h. This needs ~110 | Bolster yeast ~2× past any packable density |

Uncooled, the must rises ~29°C and kills the yeast.

**Transport violence:** CO2 at ~18 L per minute foams the vessel over, builds pressure in a sealed vessel and carries yeast out with the foam. Needs wide headspace, a gas draw and a pressure relief path.

**Cheap sweet spot:** at 10× (1 day) heat power is ~28 W, which a vessel sheds passively.

### 4.3 Aging Wine or Spirits: 10 years → 1 day (3,650×)

Aging is non-living chemistry: esterification, oxidation, wood extraction.

**Heat-only route** (activation energy ~60 kJ/mol):
- Requires ~155°C in a pressure vessel
- Reactions with different activation energies accelerate by different amounts
- Result tastes cooked, not aged

**Accounted route:**
- Stimulate each reaction pathway separately at its own multiplier
- Oxygen: natural barrel ingress is ~20 to 40 mg per liter per year, so ten years totals only ~200 to 400 mg per liter. Finding that oxygen is trivial. **The skill gate is metering it** evenly at ~8 to 17 mg per liter per hour without local overdose. A pocket of excess oxygen oxidizes that region before the rest catches up
- Wood extraction stimulated as its own pathway

Energy bill is small. Precision is the cost.

### 4.4 Soy Sauce: 100 kg moromi, 1 year → 1 day (365×)

| Stage | Natural limit | Heat-only problem | Accounted fix |
|---|---|---|---|
| Koji mold growth | ~2 days, self-heats | Overheats easily | Bolster mold, cool continuously |
| Protease breakdown of protein | Enzymes denature ~50 to 55°C | Can't heat past this | Bolster enzyme turnover at stable temperature |
| Salt-tolerant yeast and lactic bacteria in 18% brine | Already stressed and slow | Heat kills them | Bolster division and salt tolerance |
| Maillard browning | Heat route needs ~76°C for 365× | Destroys the proteases | Stimulate as a separate pathway |

No single temperature satisfies all four. Each stage needs targeted stimulation.

### 4.5 Sourdough

**Bulk rise: 5 hours → 30 minutes (10×)**
- Heat and CO2 are modest
- The real limit is gluten. Dough stretches by slow viscoelastic relaxation. 10× gas production tears the network instead of inflating it
- Gluten is not alive, so bolstering microbes doesn't help. The dough structure needs its own stimulation
- Dough water must be real or the bread dries out when the feed stops

**Starter from scratch: 1 to 2 weeks**
- Microbial succession: populations rise and die off as the pH drops
- Compressing it means compressing an ecological contest, not just feeding it
- Bolstering the wrong organism early produces a contaminated or unstable starter

### 4.6 Lettuce: 300 g head, ~45 days → 1 day

| Item | Amount | Source |
|---|---|---|
| Dry matter | ~15 g | Built from inputs below |
| CO2 fixed | ~22 g (~11 L) | Real CO2 only |
| Water | ~10 L through the plant | Real water for tissue. Created water only for evaporative cooling |
| Light | ~20 mol photons ≈ 4.4 MJ | Stored sunlight ≈ one sunny summer day over ~0.4 m², or direct mana light |
| Light intensity if delivered as photons | ~5,800 µmol/m²/s (~3× full sun nonstop) | Requires bolstered leaves or direct energy feed |
| Heat | ~51 W per plant for 24 h | Q_cool |
| Cell division | ~17 doublings. Natural minimum ~8.5 days | Bolster cell cycle to ~1.4 h |
| Root and stomata flow | Can't naturally pass 10 L in a day | Bolster uptake |

**Developmental programs:** cell count is not the whole plant. Leaf initiation, leaf count, head formation and tissue quality (texture, sweetness, bitterness) are staged by hormonal and light signals over time. Bolstering mitosis alone produces a large weak plant: loose, watery, bitter or bolting. Each developmental stage must be driven in order.

### 4.7 Oak Tree: 100 years → 1 year

| Item | Amount | Source |
|---|---|---|
| Dry wood | ~5 tonnes | Built from inputs below |
| Stored chemical energy | ~90 GJ | From light |
| Light needed | ~0.4 to 1 TJ in one year ≈ 12 to 30 kW continuous | Stored sunlight or direct mana light |
| Water | ~2,000 tonnes over a century → ~5.5 tonnes per day | Real water |
| CO2 | ~8 tonnes | Real CO2 |
| Heat | Most of the light energy | Q_cool at similar kW scale |
| Development | Heartwood, density, fruiting age are staged programs | Stimulate stages in sequence |

A century of growth in a year is a small industrial operation in energy terms.

---

## 5. Summary

| Cost category | Scales with | Notes |
|---|---|---|
| Ingredients | Fixed totals | Must be real for anything kept in the product |
| Cooling | Total heat minus passive loss, which shrinks as N rises | Includes metabolic heat, bolstering heat and cast waste |
| Light energy | Fixed totals, delivered N× faster | Stored sunlight is pre-paid by collection area × days |
| Water / gases | Fixed totals, N× flux | Created mass only for scaffolding, paid as upkeep |
| Bolstering | Power ∝ living mass × overdrive past N_c | Total levels off at high N. Adds heat |
| Transport | N× flux | Shear, foam and pressure grow faster than volume |
| Pathway precision | Number of competing reactions | A skill cost more than an MP cost |

## 6. Failure Modes

The first thing to fail is never the magic. It is the cooling, the oxygen line, the gluten or the stage balance.

| Failure | Cause |
|---|---|
| Cooked wine, boiled-tasting soy | Heat used in place of per-pathway stimulation |
| Dead vinegar | Cooling lag or a gap in aeration |
| Cell stripping | Bubble shear from violent sparging |
| Foam-over | CO2 or air flux exceeding headspace |
| Local anoxia | Dead zones between bubbles at high oxygen demand |
| Torn bread | Gas production outrunning gluten relaxation |
| Wilting lettuce, dried bread, weakening vinegar | Created mass dispersing out of the product after the feed stops |
| Big weak plant | Mitosis bolstered without driving developmental stages |
| Over-oxidized spirit | Uneven oxygen metering during aging |

**Low-skill result:** the failures above.
**High-skill result:** the real product, matching natural flavor and structure.

Craft skill tiers matter more than raw MP. Raw mana pays for heat and light. Skill pays for balancing pathways, choosing what to bolster, metering inputs and keeping created mass out of the product. Moderate compression near the natural ceiling is cheap. High compression is an industrial undertaking.
