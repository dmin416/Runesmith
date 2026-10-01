# Mana Materials Science

Proposal note for path materials, fantasy metals and elemental craft. **Not fully locked.** Bookkeeping unit matches `Energy.md` (`1 mana = 10 J`). Earth alloy production: `../Science/Materials.md`. Ore map: `../Science/MetalOres.md`. Novel metal blurbs: `../Science/KitchenCraft.md`. Affinities: `../Progression/Attributes.md`. Path efficiencies in this file are the derived values. Values from `Energy.md` are not canon here.

**1 mana = 10 J.** Path cost never changes. Efficiency and ambient gain change **output** and **waste** only.

```
Useful = cost × 10 J × η_path × G
Waste_total = cost × 10 J × (1 − η_path)
```

Ambient gain `G` scales Useful only and never changes the mana paid. Ambient enters at the converter and does **not** cross the pathway. It adds useful and adds no path waste.

| Condition | G |
|---|---|
| Local drain (recently emptied zone) | **0.5** |
| Normal room | **1.0** |
| Open air | **3.0** |
| Mana-dense area | **6.0** |

Worked example: **100 mana** pulse at **95%** path efficiency (`Useful = 100 × 10 × 0.95 × G = 950 × G`).

| Condition | G | Useful |
|---|---|---|
| Local drain | 0.5 | **475 J** |
| Normal room | 1.0 | **950 J** |
| Open air | 3.0 | **2850 J** |
| Mana-dense area | 6.0 | **5700 J** |

Of `Waste_total`, about **half** stays in the path as heat. The rest leaves with the discharge. Temperature-rise estimates must use **path heat = 0.5 × Waste_total**, not the full waste.

---

## 1. One transport law

Mana path efficiency uses **one primary rule per mode**. Do not treat wire loss and gem absorption as two independent causes of the same η.

| Mode | What it covers | Rule |
|---|---|---|
| **Wire** | Metals and graphitic conductors | Pulsed / alternating flow in a surface layer. Loss scales with `sqrt(ρ × μ_r)`. Ferromagnetic hosts (iron, hardened steel) lose far more than nonmagnetic ones. |
| **Window** | Wide-gap crystals (diamond, adamantium, clear arcanite) | No free carriers. Loss from impurities and flaws only. |
| **Superconducting** | Mythril, red mithril, blue mithril, aether mithril alloy | Steady flow near lossless up to a critical current **Jc**. Pulses pay a **5%** AC-loss dial → **95%** path η (aether mithril **96%** dial). Past **Jc** the path **quenches**: it falls back toward titanium-alloy wire η and dumps stored / in-flight energy as heat. Quench is rare on gear-grade stock. |
| **Absorber** | Black mithril | Nanotextured black-body host. Absorbs every non-dark band (**~5%** path η). Dark band passes at high η (**~95%** dial). |
| **Soft channel** | Mana fiber (core + cladding) | Optical-fiber analog. Dial near **99%**. Hide / deep iron as cladding. Tight bends leak. |
| **Persistent store** | Etherium | Closed loop holds charge with negligible decay. Transfer out is a separate η. |
| **Biological relay** | Living body | Nerve-like regeneration along the path. Dial near **90–92%** (body ≈ **90%**). |

**Gem α is derived, not a second cause.** For a standard **10 cm** path, `α = −ln(η) / 10 cm` is only a visualization of the already-chosen η. Metals are not “glass with weird α.”

**Ink and blood.** Monster blood and hemolymph are **high-η traces** (~**90%**, same band as the body), not saline wires. Scroll ink works because blood (or blood + conductor powder) is a low-resistance path. The saline-only **0.2%** figure is discarded for mana paths. Blood remains a carrier fluid chemically; for path law it conducts.

---

## 2. Efficiency table (derived)

Waste per 100 mana below is `Waste_total` at G = 1. Path heat for dT ≈ half of that.

| Path | Mode | Efficiency | Waste per 100 mana |
|---|---|---|---|
| Silicon iron (electrical steel) | wire | 10.7% | 893 J |
| Ductile cast iron | wire | 22.3% | 777 J |
| Carbon fiber (along fibers) | wire | 34.3% | 657 J |
| Wrought iron | wire | 34.7% | 653 J |
| Durium | wire | 36.8% | 632 J |
| Iron (pure) | wire | 37.2% | 628 J |
| Deep iron | wire | 37.6% | 624 J |
| Durasteel | wire | 38.5% | 615 J |
| Aether durasteel | dial | 40.0% | 600 J |
| Hide (dry leather) | cladding dial | 40.0% | 600 J |
| Deep steel | wire | 40.2% | 598 J |
| Hardened steel (1095) | wire | 41.5% | 585 J |
| Graphite (electrode) | wire | 48.0% | 520 J |
| Tungsten carbide-cobalt | wire | 63.7% | 363 J |
| Titanium alloy (Ti-6Al-4V) | wire | 66.7% | 333 J |
| Bone | dial | 70.0% | 300 J |
| Scales (ordinary) | dial | 70.0% | 300 J |
| Nitinol (austenite) | wire | 74.2% | 258 J |
| Dark steel (austenitic) | wire | 75.0% | 250 J |
| Mana steel (austenitic) | wire | 75.9% | 241 J |
| Tungsten heavy alloy | wire | 76.4% | 236 J |
| Titanium (grade 2) | wire | 78.0% | 220 J |
| Graphite (oriented, in-plane) | wire | 80.5% | 195 J |
| Lead | wire | 85.1% | 149 J |
| Cupronickel (90/10) | wire | 85.7% | 143 J |
| Bronze | wire | 87.1% | 129 J |
| Gold (18k) | wire | 88.3% | 117 J |
| Tin | wire | 88.5% | 115 J |
| Electrum | wire | 89.2% | 108 J |
| Blood / hemolymph / monster blood | biological | **90%** | **100 J** |
| Human body (relay) | biological | **90–92%** | **80–100 J** |
| Brass | wire | 91.3% | 87 J |
| Orichalcum (golden titanium) | wire (reduced) | **66.7%** | 333 J |
| Tungsten (pure) | wire | 91.9% | 81 J |
| Gold (24k) | wire | 94.6% | 54 J |
| Deep silver | wire | 94.9% | 51 J |
| Sterling silver | wire | 95.0% | 50 J |
| Mythril | superconducting | 95.0% | 50 J |
| Red / blue mithril | superconducting | 95.0% | 50 J |
| Arcanite (reserved) | window dial | 95.0% | 50 J |
| Copper (C10100) | wire | **95.2%** | **48 J** |
| Silver (fine) | wire | 95.4% | 46 J |
| Aether mithril alloy | superconducting | 96.0% | 40 J |
| Graphene (doped sheet) | wire | 96.3% | 37 J |
| Diamond | window | 97.0% | 30 J |
| Red mythril (flame + heat recycle) | superconducting + recycle | **97.0%** effective | **30 J** |
| Adamantium | window | 98.0% | 20 J |
| Etherium (transfer) | persistent | 99.0% | 10 J |
| Soft channel (mana fiber) | soft | 99.0% | 10 J |
| Black mithril (non-dark bands) | absorber | 5.0% | 950 J |
| Black mithril (dark band) | absorber | ~95% | ~50 J |
| Orichalcum (thick bulk / armor) | reduced wire | ~negligible through | High resistivity; thin foil still leaks |
| Resistium | additive | host | host |

**Wire formula (metals, dial constant kept):**  
`η = 1 / (1 + 0.05 × sqrt((ρ / ρ_Cu) × μ_r))` with `ρ_Cu = 1.7×10⁻⁸ Ω·m`. Copper lands at about **95%** (table **95.2%**).

**Red mythril heat recycle:** base superconducting path is **95%** (`Waste_total` **50 J** per 100 mana). About **40%** of `Waste_total` is recycled as useful fire mana through a selective thermal emitter (thermophotovoltaic analog dial). The recycle draws on **both** the path-heat share and the discharge-heat share of that waste, not path heat alone, so the **20 J** return stays consistent with the half-waste bookkeeping. Returned useful ≈ **20 J** so net waste ≈ **30 J** and effective η ≈ **97%**.

**Two axes:**
- **Path η:** how cleanly mana flows (this table).
- **Mana damage resistance:** how fast runes burn from lattice damage under flow (deep iron/steel, resistium, tungsten). High resistance ≠ high η.
- Deep iron and deep steel get about **10 times** more rune life from the radiation-damage axis (mana resistance). Pattern fade from heat is a separate axis and deep metals do not gain from it. Later sections point here instead of restating the full sentence.

---

## 3. Fantasy metals (story-aligned)

### Deep iron / deep steel
ODS-like: mana-rich stock, hard to melt (magical blast furnaces), harder to inscribe. Still magnetic → **low η**. Rune-life bonus: see section 2 (radiation-damage axis only).

### Dark steel / mana steel
Nonmagnetic austenitic hosts → **high η** (~75–76% on this dial). Best common rune channels in steel weapons (convert channel zone; keep hardened bulk).

### Mythril
**Magically saturated silver–copper alloy** (near Ag–Cu eutectic frame). Look: **pearlish** light silvery gold. Reusable runic gear. Mana mode: **superconducting** (section 1) from the saturation, not from mundane Ag–Cu alone. **Not titanium.** Unrelated to orichalcum’s golden-titanium shop lock.

- Steady flow near lossless up to a high **Jc**.
- Pulses pay ~**5%** AC-loss dial → **95%** path η.
- **Quench is rare** on gear-grade stock. If it quenches, fall back toward ordinary poor-wire η (titanium-alloy band is the Earth dial for that fallback only) and dump heat. Do not treat quench as the normal failure of a mithril wand.
- **Pattern stability:** written patterns follow Néel-Arrhenius fading. **Δ** is the stability factor and characteristic lifetime is about **1×10⁻⁹ s × e^Δ**. **Wipe T** is the temperature where that lifetime collapses to minutes or less (ordering / Curie analog). Gear-grade mythril aims for **Δ ≈ 45 or more**, which survives combat heat near **350 K** for days to years. A forge fire can still erase a pattern. That is a forge hazard, not a fight tax. Heat fade is not the deep-metal resistance axis (section 2).

Shop notes: `../Science/CraftMetal.md` (Mythril). Sterling / eutectic metallurgy pointers: `../Science/Materials.md`.#### Superconducting windings (invent / prestige apps)

A superconducting winding is a coil of wire made from superconducting material. Like a copper winding, it carries current to create a magnetic field. The difference is that current flows with zero resistance (mythril / aether-mithril path mode).

**What zero resistance does**
- **No heat:** copper windings lose energy as heat (I²R loss). A superconducting winding loses nothing on steady DC however much current it carries.
- **Persistent current:** with the coil's ends joined in a closed loop, current circulates forever with no power supply. SMES coils and MRI magnets work this way. Etherium is the dedicated persistent-store metal; mythril windings can hold a persistent electrical current in the coil loop.
- **Much higher current density:** copper carries about 2 to 10 A/mm² before overheating. Current Earth superconductors carry 100 to 1,000+ A/mm². Gear-grade mythril still has a **Jc** ceiling (section 1); aether mithril aims higher.
- **Stronger fields:** more current in less space creates far stronger magnetic fields from a compact coil.

**Earth limits vs Caldris mythril**
- **Critical temperature:** Earth superconductors need cooling to between -269 °C and about -200 °C. Room-temperature mythril removes the cooling plant.
- **Critical field and critical current:** above a certain field or current, superconductivity collapses (a quench). Stored energy then turns into heat at once and can destroy the coil. Mythril **keeps Jc / quench** (rare on gear stock). Do not write it as perfect unlimited current.
- **Magnetic pressure:** strong fields push the windings outward. Adamantium or deep high-strength frames contain this; orichalcum is mana-resistant cladding / anvil damp, not the winding itself.
- **AC losses:** Earth superconductors lose a little when current changes quickly. Mythril pulses already pay the **5%** AC-loss dial. Steady DC is near lossless.

**Role in a flywheel / motor stack**
- **Motor/generator:** superconducting windings on the stator create a strong field. The rotor's magnets (or its own superconducting windings) turn through it. Charging speeds the rotor up and discharging slows it down.
- **Magnetic bearings:** superconductors push out magnetic fields (Meissner) and can lock magnets in place (flux pinning). This holds the rotor centered with no contact. Orichalcum plates are **mana-resistant** cladding (poor conductors), not superconducting bearings. Do not confuse reduced-η shield stock with winding current.
- **Efficiency:** with no winding I²R loss, conversion between motion and electricity sits above 99% on the electrical side. Remaining losses are bearings, windage, and power electronics / rune converters.

Companions: `../Science/Batteries.md` (stone vs cell power), `../Science/RefinedMana.md` (Stillwire stone-refined wire; Lightthread), stone sockets as the mana feed.

**Variants:**
- **Red mithril:** fire band / cuprite-lava ore. Superconducting base **95%**. With heat recycle (section 2) effective **97%**.
- **Blue mithril:** short / water-lean band. Superconducting **95%**.
- **Black mithril:** **absorber** mode (section 1). Non-dark bands ~**5%**. Dark band ~**95%**.
- **Aether mithril:** etherium phase. Superconducting **96%** dial. Higher Jc / storage.

### Orichalcum
**Golden titanium** handling lock (`../Science/CraftMetal.md`). Goldish prestige metal. Mana mode: **reduced wire** at the titanium band (**~66.7%**, same dial as Ti-6Al-4V). This is the fantasy metal that owns titanium's poor mana conductivity and titanium shop chemistry. **Mythril is unrelated.**

- Poor channel. **Never** a rune host or written-pattern metal. Cannot be imbued.
- Thick plate and armor pass almost no mana (Source anti-magic armor / anvil story). Thin foil still leaks.
- In a mostly-mithril anvil, a little orichalcum **damps** stray forge mana and cuts deterioration (low η sinks less into the tool).
- Full orichalcum kit is rare prestige: mage-hostile, and empty of enchantments.

### Adamantium
Window-mode top path (~**98%**). Diamond-like thermal spreading + mana-supported hardness.

**Forge story (aligned with novel):** heat **does** enter, but high **k** dumps it into tongs, anvil and air. Smiths must pour **infernal** power and fire-resist skill to keep the whole thermal mass at forging T. That is why records talk of deaths in the heat, not because the piece cannot be heated at all.

Orichalcum tools work by **starving mana support** in the hard skeleton (low-η contact dumps the boost) so brittle cleavage becomes possible. Inscription stays hardest of the commons.

### Durium / durasteel / aether durasteel
Durium: hard brittle carbide/boride-like (dark blue ore sheen). Durasteel: durium particles in deep-steel matrix (cermet). Alone, slightly better than deep steel on the radiation-damage axis (section 2). Etherium mix pushes enchant life toward mithril. Aether durasteel adds a thin mana-active phase for fire-gear buffs; still a poor wire.

### Etherium
Persistent-current store. Tower cores stay mostly **stationary** because motion bleeds pinned flux. Mixes raise Jc / storage and lower toughness. Over-Jc **quench** dumps the store as heat. Transfer η ~**99%** dial.

### Deep silver / arcanite / resistium
Deep silver: high-η silver-copper with deep-style life bonus on the radiation-damage axis (section 2). Arcanite: reserved prestige crystal (window dial if treated as clear insulator). Resistium: ODS-style **additive**, inherits host η, raises rune life on the radiation-damage axis (section 2).

---

## 4. Temperature rise (path heat only)

For a **5 g** trace and **one 100 mana** pulse:

`Q_path ≈ 0.5 × (1 − η) × 1000 J`  
`dT ≈ Q_path / (m × c)`

Examples (order of magnitude):

| Path | η | Waste_total | Path heat | c (J/kg·K) | dT |
|---|---|---|---|---|---|
| Iron | ~37% | ~630 J | ~315 J | ~450 | ~**140 K** |
| Copper | ~95% | ~48 J | ~24 J | ~385 | ~**12 K** |
| Orichalcum | 66.7% | 333 J | ~167 J | ~520 | ~**64 K** |
| Mythril | 95% | 50 J | ~25 J | ~500 | ~**10 K** |
| Lead | 85.1% | 149 J | ~75 J | ~129 | ~**116 K** |

Lead still risks melt if pulses stack before heat leaves. Lead/tin “one pulse melts” claims must use the **50% path-heat** share and real cooling. Stacked pulses without pause remain dangerous.

---

## 5. Runic weapons

| Class | Construction | Failure |
|---|---|---|
| A. Engraved plain steel | Groove in ferromagnetic steel | Hot channel, electromigration-like pits, few charges |
| B. Mana-inlaid steel | Channel converted to austenitic mana/dark steel | Leakage into bulk; slow wear. Best mundane default |
| C. Magical monolith | Pattern written in mithril / adamantium / etc. | Heat above ordering / wipe T fades pattern. Keep cool |
| D. Orichalcum layer | Shield / anvil insert | Never the channel. Titanium-family shop failures (work-hardening, air contamination case) |

**Inlay rule:** same-metal phase conversion beats foreign-metal inlay (avoids galvanic attack at the border).

Deep steel stays hot (low η). Rune-life bonus: section 2. **Mana steel channel** runs cooler. **Mithril / adamantium** barely warm and stay reusable if kept under wipe T. **Orichalcum** is shield or anvil only.

### Worked channel (path heat)

Channel **2 mm** wide, **1 mm** deep, **60 cm** long (**1.2 cm³**). One **100 mana** pulse. `Q_path = 0.5 × Waste_total`.

| Channel material | η | Mass | Waste_total | Path heat | Peak rise |
|---|---|---|---|---|---|
| Plain hardened steel | 41.5% | 9.4 g | 585 J | 292 J | ~**66 K** |
| Deep steel | 40.2% | 9.4 g | 598 J | 299 J | ~**68 K** |
| Durasteel | 38.5% | 9.2 g | 615 J | 308 J | ~**67 K** |
| Aether durasteel | 40.0% | 9.2 g | 600 J | 300 J | ~**65 K** |
| Dark steel (austenitic) | 75.0% | 9.4 g | 250 J | 125 J | ~**27 K** |
| Mana steel (austenitic) | 75.9% | 9.4 g | 241 J | 120 J | ~**26 K** |
| Orichalcum | 66.7% | 10.3 g | 333 J | 167 J | ~**31 K** |
| Mythril | 95.0% | 6.0 g | 50 J | 25 J | ~**8 K** |
| Red mithril (no recycle) | 95.0% | 7.2 g | 50 J | 25 J | ~**7 K** |
| Red mythril (with recycle) | 97.0% eff. | 7.2 g | 30 J | 15 J | ~**4 K** |
| Blue mithril | 95.0% | 9.6 g | 50 J | 25 J | ~**9 K** |
| Aether mithril alloy | 96.0% | 6.6 g | 40 J | 20 J | ~**7 K** |
| Adamantium | 98.0% | 6.0 g | 20 J | 10 J | ~**3 K** |

Orichalcum is a **poor** mana path (~67%) and never the weapon channel because a rune cannot hold in it.

---

## 6. Elemental bands and imbuing

### Affinities
T1 sheet: **Fire, Wind, Earth, Water**. Higher tier: **lightning, gravity** and others as their own affinities.

**Color liberty (dial):** Fire ≈ red/IR, Earth ≈ yellow/ochre, Wind ≈ green, Water ≈ blue. **Aether** = all bands (alloy special). **Dark** = absorbs non-dark bands (black mithril special). Aether and Dark are **not** T1 affinity rows.

**Lightning is not Fire+Wind.** A Fire+Wind layered pair may make an unstable hot/light effect with another name. The Lightning affinity stays a separate unlock.

### Imbue continuum
| Stage | Binding idea | Stability |
|---|---|---|
| Loose | Ordinary metal soaked in elemental mana | Minutes to hours; refresh often |
| Bound | Deep-style / carbide-like hold | Survives use; softens in forge heat |
| Native | Lattice / intermetallic (mythril-class) | Separate material; only near-melt disturbs |

Orichalcum **cannot** be imbued. Shape first then imbue when using loose/bound stages.

Opposite bands (Fire↔Water, Earth↔Wind) in one lattice strain it. Layered / multiphase stacks hold pairs.

### What each element does
| Element | Band | Imbue effect | Best host lean |
|---|---|---|---|
| Fire | Red / infrared | Raises melting point and emissivity. Can recycle waste heat as fire mana | Tungsten, graphite, red mythril |
| Earth | Yellow / ochre | Raises density and hardness. Cuts expansion and wear. Can raise rune life on the radiation-damage axis | Tungsten alloys, WC-Co, adamantium, deep iron |
| Wind | Green | Cuts density. Raises stiffness per weight and strike response | Titanium, nitinol, carbon fiber |
| Water | Blue | Raises specific heat and corrosion immunity. Self-healing lean | Cupronickel, bronze, CP titanium, blue mithril |
| Aether | All four | Passes every band with least loss | Etherium, aether mithril, aether durasteel |
| Dark | Absorbs non-dark | Soaks non-dark mana | Black mithril |

### Imbue levels (dials)
Each level respects a real ceiling. Exact numbers are dials.

| Element | Level I | Level II | Level III |
|---|---|---|---|
| Fire | Melt +150 K, emissivity 0.6, **10%** heat recycled | +400 K, 0.8, **25%** | +900 K, 0.95, **40%** (red mythril recycle ceiling) |
| Water | Specific heat ×1.15 | ×1.4 | ×1.8 |
| Wind | Specific stiffness ×1.2 | ×1.8 | ×3.6 |
| Earth | Density ×1.1, hardness ×1.2, expansion /1.5, rune life ×2 | ×1.4, ×1.6, /3, ×5 | ×2.3, ×2.5, /10, ×10 |

Earth's rune-life multiplier is the radiation-damage axis (section 2). It does not change heat-fade behavior. Earth imbue and deep steel do **not** multiply: total rune-life bonus from the radiation-damage axis is **capped at ×10** (deep alone, Earth III alone or any stack).

### Band-pass efficiency (dial)
A host passes its own band with less waste and other bands with more. Waste multipliers: in-band **0.9 / 0.75 / 0.6** at levels I / II / III. Off-band **1.1 / 1.3 / 1.6**. Waste capped at **95%**.

| Host | Base η | I in / off | II in / off | III in / off |
|---|---|---|---|---|
| Copper (C10100) | 95.2% | 95.7% / 94.7% | 96.4% / 93.8% | 97.1% / 92.3% |
| Mythril | 95.0% | 95.5% / 94.5% | 96.2% / 93.5% | 97.0% / 92.0% |
| Mana steel (austenitic) | 75.9% | ~78% / ~73% | ~82% / ~69% | ~86% / ~62% |
| Hardened steel | 41.5% | 47.4% / 35.6% | 56.1% / 24.0% | 64.9% / 6.4% |

Good conductors gain little. Poor conductors gain a lot in-band and lose a lot off-band. Orichalcum stays at the **titanium reduced-η band (~66.7%)** at every imbue level and still refuses written runes. Thick stock passes almost no bulk mana. Etherium transfer (~**99%**) shows no band preference.

### Pair combinations (layered only)
| Pair | Result | Note |
|---|---|---|
| Fire + Water | Steam | Heat spreads along the piece almost instantly |
| Fire + Earth | Magma | Hot and heavy |
| Wind + Fire | Spark gale | Light, fast and hot. **Not** the Lightning affinity |
| Wind + Water | Frost | Tough when cold |
| Earth + Water | Tide stone | Stable and self-healing lean |
| Earth + Wind | Resonant | Bell-like long ring |

All pairs are layered or multiphase. A uniform lattice cannot hold opposite bands cleanly.

### Natural lean map
| Material | Natural lean | Imbue form |
|---|---|---|
| Bronze | Water | Loose |
| Copper (C10100) | Fire | Loose |
| Brass | Wind | Loose |
| Orichalcum | none | Cannot be imbued |
| Cupronickel | Water | Loose |
| Fine / sterling silver | Wind | Loose |
| 24k gold | Earth | Bound |
| 18k gold / electrum | Earth (and Wind for electrum) | Loose |
| Ductile / wrought iron | Earth | Bound / loose |
| Silicon iron | Wind | Loose |
| 1095 steel | Fire | Loose |
| Carbon fiber / graphene | Wind | Bound |
| Diamond | Earth | Native |
| Graphite | Fire | Bound |
| Ti-6Al-4V / nitinol | Wind | Bound / native |
| Mythril | none required for SC path | Native superconducting host |
| CP titanium | Water | Bound |
| WC-Co / tungsten heavy / pure W | Earth / Fire (W) | Bound / native |
| Lead and tin | Water or Earth | Loose |
| Red mithril | Fire | Native |
| Blue mithril | Water | Native |
| Black mithril | Dark | Native |
| Aether mithril / etherium / aether durasteel | Aether | Native / bound |
| Adamantium | Earth | Native |
| Durasteel / deep iron / deep steel | Earth | Bound |
| Dark steel / mana steel | Unaspected | Loose |
| Arcanite / resistium | Unaspected | n/a |

---

## 7. Elemental mana without affinity (craft path)

Roland (0% affinities) can still craft elemental runes/scrolls.

### Converter runes
Conversion of pure mana into Fire, Earth, Wind or Water is a **phase change**. The conversion step itself costs nothing and makes no waste heat: mana in equals mana out. The only cost is the normal path efficiency of the rune and metal it runs through.

Converters cover **craft and metalwork only**. Affinity still gates elemental class spells (the T2 elemental mage abilities).

- A character with **no elemental affinity** can make elemental mana from pure mana with a converter rune alone.
- **Density gate:** below a set mana density the stream stays pure and above it the stream converts.
- Elemental stone or ambient mana of the matching element may lower that threshold. They are optional helpers, not requirements.
- Reverse (element → pure) is allowed under the same rules.
- Orichalcum cannot hold a converter. Place converters on mythril / mana-steel / steel beside orichalcum cladding if needed.

### Stone powder in metal
Crushed magic stone in an alloy follows the stone rules: **capacity scales with volume** and **transfer rate scales with area**. Crushed particles do **not** inherit full stone dump rates.

Solid stone holds about **1000 mana per cm³** of stone (`1 mana per mm³`). Alloy stone is hard-capped at **100 mana per cm³ of stone volume** (one tenth of solid stone) so a stone-loaded blade is not a mana bank.

| Stone fraction (volume) | Cap per cm³ of finished alloy |
|---|---|
| 5% | **5 mana/cm³** |
| 15% | **15 mana/cm³** |
| 30% | **30 mana/cm³** |

Insulating particles raise resistivity slightly. Orichalcum matrix (reduced η) never charges a stone inside unless the stone is pre-charged then sealed (mana vault).

### Soak depth
Loose imbue soaks deepest at forging heat then must be trapped by cooling under flow. Bound stays near the surface unless thin stock. Native needs melt alloying or extreme near-melt treatment.

---

## 8. Consistency checklist

- Cost fixed. η and G change output and waste only. G bands: drain **0.5**, room **1.0**, open air **3.0**, dense **6.0**.
- Path heat ≈ half of waste. Discharge carries the rest.
- Modes: wire, window, superconducting, absorber, soft, persistent, biological. Gem α is derived.
- Blood/ink ~90%. Scrolls work.
- Copper path η about **95%** (derived). Energy.md η values are not used here.
- Deep = radiation-damage resistance (~10× life, section 2 only). Heat fade is a separate axis.
- Austenitic = conductor.
- Orichalcum = golden titanium shop + titanium-band reduced η. Shield / anvil damp. Never rune host. Present in η table, fantasy metals, temperature table, channel table, imbue rules, converters and stone vault.
- Adamantium forge = infernal power against fast heat spreading.
- Mythril reusable at combat heat. Quench rare. Forge fire can still wipe.
- Red mythril **97%** = **95%** path + **40%** waste-heat recycle as fire mana.
- Converter phase change is free. Path η still applies. Density gate required. Stone/ambient optional threshold helpers. Affinity still gates T2 elemental class spells.
- Lightning stays its own affinity. Fire+Wind pair is not Lightning.
