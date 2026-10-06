# Mana Materials Science

> **Design loot.** Live locks: Energy.md (η_cond **20%** quality blocks; waste **½** ambient / **½** path heat+corruption), Magic.md, Runes.md. Metals: ../World/Materials/Metals.md (Ag mythril, Au orihalcum, Cu aurium, Fe/steel dark→star, Ti adamantium). Non-canon here: old host path-% tables; adamantium as forgeable post-set supersteel.

Proposal note for path materials, fantasy metals and elemental craft. **Not fully locked.** Bookkeeping unit matches `Energy.md` (`1 mana = 10 J`). Earth alloy production: `../World/Science/Metallurgy/EarthAlloys.md`. Ore map: `../World/Science/Metallurgy/MetalOres.md`. Metal names / conversion: `../World/Materials/Metals.md` (**wins**). Affinities: `../Progression/Attributes.md`. Host ladder and path feel live in `Energy.md`. Old path-% tables and **colored mythril brand metals** in this file are **non-canon**. Cookware production is Food-domain (`../Food/KitchenCraft.md`), not a metal-law source.

**1 mana = 10 J.** Path cost never changes. Narrative path feel and ambient change **output** and **waste** only.

```
Useful ≈ cost × 10 J × η_cond × A
A = √C    // live lock in Energy.md / ManaConcentration.md
```

η_cond follows rune **quality level** in Energy.md (**0.2 / 0.4 / 0.6 / 0.8 / 1.0**). Host feel narrative only. Bad runes: same cost / weak power, or high activation cost / average power. Of waste: **½** ambient / **½** into the weapon as heat damage and corruption (`Energy.md`). Temperature-rise estimates use the path half and real thermal conductivity, mass and geometry.

**Ambient:** use live `A = √C`. Old linear G bands are dead.

---

## 1. One transport law

Each host uses **one primary mode**. Do not stack wire loss and gem absorption as two independent causes of the same feel.

| Mode | What it covers | Rule |
|---|---|---|
| **Wire** | Metals and graphitic conductors | Pulsed / alternating flow in a surface layer. Ferromagnetic hosts (iron, hardened steel) waste harder than nonmagnetic ones. Exact % unset. |
| **Window / refuse** | Clear adamantium, some crystals | Adamantium carries little to no mana (clear glass). It is not a rune host. Orihalcum is a separate **block** mode (black velvet). |
| **Superconducting** | Mythril (plain name; elemental lean is a **mode**, not a separate brand metal) | Steady flow near lossless up to a critical current **Jc**. Pulses pay a little AC-loss feel. Past **Jc** the path can **quench** and dump heat. Quench is rare on gear-grade stock. Digits unset (`Energy.md` feel order). |
| **Absorber** | Dark-lean mythril **mode** (not a separate “black mythril” metal) | Soaks non-dark bands. Dark band passes cleanly. |
| **Soft channel** | Mana fiber (core + cladding) | Optical-fiber analog. Hide / darkiron as cladding. Tight bends leak. |
| **Persistent store** | Etherium | Closed loop holds charge with negligible decay. Transfer out is a separate step. |
| **Biological relay** | Living body and blood ink | Good living path between darksteel and star steel on feel. |

**Ink and blood.** Monster blood and hemolymph are living-path traces, not saline wires. Scroll ink works because blood (or blood + conductor powder) carries a usable channel. The saline-only path claim is discarded. Blood remains a carrier fluid chemically; for path law it conducts.

---

## 2. Host roles (path-% quarantined)

The old derived efficiency percent table is **non-canon**. Live order and story jobs: `Energy.md` / `EnergyDesign.md` section 2.

Short shop reminder, worst to best common path feel:

- **Iron** moves mana poorly and dies under strain.
- **Copper** is a decent mid host and spreads heat well.
- **Aurium** keeps copper flow and cuts leftover waste.
- **Steel** beats iron before conversion.
- **Darksteel** cleans up and endures better than steel.
- **Body / blood ink** are good living paths.
- **Star steel** is strong durable channel stock.
- **Mythril** is the best common clean host.
- **Orihalcum** blocks seating (black velvet). Never a rune host. MR = conversion %.
- **Adamantium** carries little to no mana (clear glass). Not a rune host. Cover over a real inlay only.

**Two axes:**
- **Path feel:** how cleanly mana flows (Energy.md ladder).
- **Mana damage resistance:** how fast runes burn from lattice damage under flow (darkiron / darksteel / star grades, resistium, tungsten). High resistance ≠ clean path feel.
- Dark / star iron-steel get about **10 times** more rune life from the radiation-damage axis. Pattern fade from heat is a separate axis and those grades do not gain from it.

**Fire-lean mythril heat recycle (story mode, not a red-mythril brand):** some of the path-half waste heat can return as useful fire mana through a selective thermal emitter. Digits open. Path-heat share stays **½** of total waste (`Energy.md`).

---

## 3. Fantasy metals

Metal conversion bands, specs, durium, etherium, resistium, mythril wipe **T**, and superconducting windings: `../World/Materials/Metals.md`. Shop forge behavior: `../World/Science/Metallurgy/CraftMetal.md`. Superconducting **mode** for mythril stays in section 1 above.

---

## 4. Temperature rise (path heat)

Path heat share, `dT` estimate, and relative host order: `../World/Science/Metallurgy/OverheatedMetals.md` (section **Path heat (mana pulse)**). Waste feel ladder: `Energy.md`.

---

## 5. Runic weapons

Channel classes, inlay rule, and worked geometry: `../Combat/Weapons.md` (section **Runic weapons (channel classes)**).

---

## 6. Elemental bands and imbuing

### Affinities
T1 sheet: **Fire, Wind, Earth, Water**. Higher tier: **lightning, gravity** and others as their own affinities.

**Color liberty (affinity dial, not metal brands):** Fire ≈ red/IR, Earth ≈ yellow/ochre, Wind ≈ green, Water ≈ blue. **Aether** = all bands (alloy special). **Dark** = absorbs non-dark bands (dark-lean mythril **mode**). Aether and Dark are **not** T1 affinity rows. Do **not** invent red/blue/black mythril as separate forge metals; `Metals.md` quality bands win.

**Lightning is not Fire+Wind.** A Fire+Wind layered pair may make an unstable hot/light effect with another name. The Lightning affinity stays a separate unlock.

### Imbue continuum
| Stage | Binding idea | Stability |
|---|---|---|
| Loose | Ordinary metal soaked in elemental mana | Minutes to hours; refresh often |
| Bound | Radiation-hard / carbide-like hold | Survives use; softens in forge heat |
| Native | Lattice / intermetallic (mythril-class) | Separate material; only near-melt disturbs |

Orihalcum **cannot** be imbued. Shape first then imbue when using loose/bound stages.

Opposite bands (Fire↔Water, Earth↔Wind) in one lattice strain it. Layered / multiphase stacks hold pairs.

### What each element does
| Element | Band | Imbue effect | Best host lean |
|---|---|---|---|
| Fire | Red / infrared | Raises melting point and emissivity. Can recycle waste heat as fire mana | Tungsten, graphite, mythril (fire lean) |
| Earth | Yellow / ochre | Raises density and hardness. Cuts expansion and wear. Can raise rune life on the radiation-damage axis | Vanadium / VC (durium line), tungsten alloys, WC-Co, darkiron / star iron |
| Wind | Green | Cuts density. Raises stiffness per weight and strike response | High-stiffness light alloys, nitinol, carbon fiber |
| Water | Blue | Raises specific heat and corrosion immunity. Self-healing lean | Cupronickel, bronze, mythril (water lean) |
| Aether | All four | Passes every band with least loss | Etherium, aether durasteel |
| Dark | Absorbs non-dark | Soaks non-dark mana | Dark-lean mythril (mode, not a separate brand metal) |

### Imbue levels (dials)
Each level respects a real ceiling. Exact numbers are dials.

| Element | Level I | Level II | Level III |
|---|---|---|---|
| Fire | Melt +150 K, emissivity 0.6, **10%** heat recycled | +400 K, 0.8, **25%** | +900 K, 0.95, **40%** (fire-lean mythril recycle ceiling) |
| Water | Specific heat ×1.15 | ×1.4 | ×1.8 |
| Wind | Specific stiffness ×1.2 | ×1.8 | ×3.6 |
| Earth | Density ×1.1, hardness ×1.2, expansion /1.5, rune life ×2 | ×1.4, ×1.6, /3, ×5 | ×2.3, ×2.5, /10, ×10 |

Earth's rune-life multiplier is the radiation-damage axis (section 2). It does not change heat-fade behavior. Earth imbue and darksteel do **not** multiply: total rune-life bonus from the radiation-damage axis is **capped at ×10** (darkiron/darksteel alone, Earth III alone or any stack).

### Band-pass feel (dial)
A host passes its own band with less waste and other bands with more. In-band feel cleans up at higher imbue levels. Off-band feel gets worse. Absolute multipliers stay open.

Good hosts gain little from band matching. Poor hosts gain a lot in-band and lose a lot off-band. Orihalcum refuses imbue and written runes at every level (MR = %). Thick orihalcum stock passes almost no bulk mana. Etherium transfer shows little band preference.

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
| Orihalcum | none | Cannot be imbued |
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
| Mythril | none required for SC path; element lean is mode only | Native superconducting host (`Metals.md`) |
| CP titanium | Water | Bound |
| WC-Co / tungsten heavy / pure W | Earth / Fire (W) | Bound / native |
| Durium / durium carbide (V / VC anchor) | Earth | Bound / native (carbide) |
| Lead and tin | Water or Earth | Loose |
| Etherium / aether durasteel | Aether | Native / bound |
| Adamantium | none | Cannot be imbued (clear glass; not a path host; cover only) |
| Durasteel / darkiron / star iron | Earth | Bound |
| Darksteel / star steel | Unaspected | Loose |
| Arcanite / resistium | Unaspected | n/a |

---

## 7. Elemental mana without affinity (craft path)

Roland (0% affinities) can still craft elemental runes/scrolls.

### Converter runes
Conversion of pure mana into Fire, Earth, Wind or Water is a **phase change**. The conversion step itself costs nothing and makes no waste heat: mana in equals mana out. The only cost is the normal path feel of the rune and metal it runs through.

Converters cover **craft and metalwork only**. Affinity still gates elemental class spells (the T2 elemental mage abilities).

- A character with **no elemental affinity** can make elemental mana from pure mana with a converter rune alone.
- **Density gate:** below a set mana density the stream stays pure and above it the stream converts.
- Elemental stone or ambient mana of the matching element may lower that threshold. They are optional helpers, not requirements.
- Reverse (element → pure) is allowed under the same rules.
- Orihalcum cannot hold a converter. Place converters on mythril / star steel / steel beside orihalcum cladding if needed.

### Stone powder in metal
Crushed magic stone in an alloy follows the stone rules: **capacity scales with volume** and **transfer rate scales with area**. Crushed particles do **not** inherit full stone dump rates.

Solid stone holds about **1000 mana per cm³** of stone (`1 mana per mm³`). Alloy stone is hard-capped at **100 mana per cm³ of stone volume** (one tenth of solid stone) so a stone-loaded blade is not a mana bank.

| Stone fraction (volume) | Cap per cm³ of finished alloy |
|---|---|
| 5% | **5 mana/cm³** |
| 15% | **15 mana/cm³** |
| 30% | **30 mana/cm³** |

Insulating particles raise resistivity slightly. Orihalcum matrix (MR block) never charges a stone inside unless the stone is pre-charged then sealed (mana vault).

### Soak depth
Loose imbue soaks deepest at forging heat then must be trapped by cooling under flow. Bound stays near the surface unless thin stock. Native needs melt alloying or extreme near-melt treatment.

---

## 8. Consistency checklist

- Cost fixed. Path feel and ambient `A = √C` change output and waste only. Old linear G bands are dead.
- Path heat / corruption = **½** of waste; ambient = **½**. η_cond from Energy.md quality table.
- Modes: wire, refuse/block, superconducting, absorber, soft, persistent, biological.
- Blood/ink = living-path band. Scrolls work.
- Copper = decent mid host. Ladder lives in Energy.md.
- Dark / star Fe-steel = radiation-damage resistance (~10× life, section 2 only). Heat fade is a separate axis.
- Austenitic = cleaner conductor than ferromagnetic iron-line stock.
- Orihalcum = converted gold; MR = %; black velvet block. Never rune host.
- Adamantium = converted Ti, cast-final; clear glass, little to no mana. Cover over real inlay. Not a path host.
- Mythril reusable at combat heat. Quench rare. Forge fire can still wipe.
- Fire-lean mythril mode may recycle some waste heat as fire mana. Digits open. No separate color-mythril brands.
- Converter phase change is free. Path feel still applies. Density gate required. Stone/ambient optional threshold helpers. Affinity still gates T2 elemental class spells.
- Lightning stays its own affinity. Fire+Wind pair is not Lightning.
