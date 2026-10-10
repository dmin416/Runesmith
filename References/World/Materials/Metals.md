# Metals

> Availability tags: `Materials.md`. Ambient altitude `C` / soak `A = √C`: `../Science/Energy/ManaConcentration.md`. Shop craft: `../Science/Metallurgy/CraftMetal.md`. Path η_cond: `../../Runes/Energy.md`.

## Narrative

Metals convert under mana concentration. Temporary charge bleeds off. Permanent conversion starts past a conductivity threshold and rises with time and soak. Names are **bands on one conversion meter**, not separate Earth elements. Living foundry / metal-slime conversion vessel: `../Fauna/Species/Slimes.md`.

## Detail

**Locks (parent lines):**
- **Silver → mythril** (Earth silver chemistry / mirrors: `../Science/Metallurgy/Silver.md`)
- **Gold → orihalcum**
- **Copper → aurium**
- **Iron → darkiron / star iron**
- **Steel → darksteel / star steel**
- **Titanium → adamantium**

Dead: mythril=titanium · orihalcum=titanium · adamantium=iron/steel.

**Rune hosts:** Almost anything can hold a rune. Poor hosts can burn from setting alone. Thermal: `../Science/Metallurgy/OverheatedMetals.md`. Aurium linings cut burn from flowing mana.

**Low-impact solids (not metal conversion lines):** **Clay**, **silicon / silica**, and **carbon** soak mana poorly. They charge less, convert less, and stay near their mundane properties under ordinary ambient (including most dungeon cooks). Use for molds, kiln body, glass/sand matrix, charcoal fuel that does not turn into magic metal, and inert carriers around hot mana work. They are not antimagic like orihalcum; they are simply stubborn and dull to mana.

### Ambient soak (same atmosphere as spells)

Metal absorption uses the same open-air `A = √C` as spells. **Law:** `../Science/Energy/ManaConcentration.md`. **Altitude / haze digit tables:** `../Space/Atmosphere.md`. Do not restate the ladder here.

Dungeons and spiritual sites hold **more pervasive** mana than the small floor-add formula alone suggests. Treat deep-delve / spiritual soak as a **narrative thickness** that can match high open-air cook bands without flying (`../Geography/Dungeons.md`). The floor `C = C(h) + k×(D/N)` ladder stays the mild spell-feel guide; metal cook in those places is story-weighted, not forced to that mild digit.

**Find vs cook:** dungeon hoards and mines more often yield **old already-converted metal** (geological / core-age soak) than metal that converted while an adventurer watched. Fresh in-delve cook still happens; it is the rarer story.

### Charge vs conversion

**Temporary charge:** metal near mana picks up a charge that bleeds away when it leaves. Still ordinary metal. Silver near a mage charges and discharges without converting.

**Permanent conversion:** only after soak passes that metal's threshold. Further above threshold → faster. Nears completion asymptotically:

- **90%** ≈ 3× the time to half
- **99%** ≈ 7× the time to half

```
Converted = 1 − exp(−speed × (A − threshold) × time)
```

Time in different rich places **adds**. A bar can cook partway in a dungeon and finish on an airship.

**Starting soak** (better conductors start lower). Read `A(h)` from `ManaConcentration.md` (`C = P₀/P`, then haze):

```
threshold_A ≈ 200 / conductivity_%_of_copper
start_h = lowest altitude where A(h) ≥ threshold_A
cook rate ∝ speed × max(0, A − threshold_A)
```

Dead: `start_altitude ≈ 20 mi × log₁₀(...)` (that assumed old `C = 10^(h/10)`).

Speed order once started: **gold > silver > copper > iron > steel > titanium**. Iron ≈ 4× titanium; 1% carbon steel ≈ 2× titanium.

### Conversion table

| Metal | Becomes | Cond. vs Cu | thr_A | Starts above (open air) | Notes |
|---|---|---|---|---|---|
| Silver | **Mythril** | ~105% | ~1.9 | ~6 mi (`A` ~2) | First to start. Best common rune host below aetherium |
| Copper | **Aurium** | 100% | ~2.0 | ~6–7 mi | Close behind silver |
| Gold | **Orihalcum** | ~70% | ~2.9 | ~9 mi (`A` ~2.8) | Fastest once started. MR = % conversion |
| Iron | **Darkiron** → **star iron** | ~17% | ~12 | ~21 mi (`A` ~12) | Holds mana poorly vs Ag/Cu |
| Steel (~1% C) | **Darksteel** → **star steel** | ~10% | ~20 | ~26 mi (`A` ~20) | Carbon slows cook. Prefer convert iron then carburize |
| Titanium | **Adamantium** | ~3.5% | ~57 | ~36 mi (`A` ~57; between 31–40 mi) | Slowest. Cast-final |

### Mythril (silver)

Any permanently converted silver is **mythril**. Quality = conversion band.

| Quality | Conversion |
|---|---|
| Low mythril | <25% |
| Standard mythril | 40–60% |
| Fine mythril | >80% |
| True mythril | >95% |
| Pure mythril | 100% |

**Sell (locked feel):** gear-grade mythril is **~10% lighter than steel**, **stronger than steel** (enough for a sword on its own), and **extremely conductive**. Conductivity / mana path is still why runic gear prefers it. It is not titanium-light.

Open air: no mythril below ~6 mi (`A` under thr). Dungeons / spiritual sites are the low sources. Elemental alignment stays **mythril** (no separate red-mythril brand).

Shop frame is often Ag–Cu eutectic. Look: **pearlish** light silvery gold. Reusable runic gear and blades. **Not titanium.** Unrelated to orihalcum (converted gold) and adamantium (converted Ti, cast-final).

Mana path mode is **superconducting** from conversion, not from mundane Ag–Cu alone (transport law: `../../Runes/ManaMaterials.md` section 1; feel order: `../../Runes/Energy.md`). Conversion expands the lattice as that path opens, so density falls to about **90% of steel** by gear grade (same mass, more volume; same-size piece handles ~10% lighter).

- Steady flow near lossless up to a high **Jc**. Pulses pay a little AC-loss feel. Digits unset.
- **Quench is rare** on gear-grade stock. If it quenches, fall back toward ordinary poor-wire feel and dump heat. Do not treat quench as the normal failure of a mythril wand.
- **Pattern stability:** written patterns follow Néel-Arrhenius fading. **Δ** is the stability factor and characteristic lifetime is about **1×10⁻⁹ s × e^Δ**. **Wipe T** is the temperature where that lifetime collapses to minutes or less (ordering / Curie analog). Gear-grade mythril aims for **Δ ≈ 45 or more**, which survives combat heat near **350 K** for days to years. A forge fire can still erase a pattern. That is a forge hazard, not a fight tax. Heat fade is separate from dark/star rune-life resistance (`../../Runes/ManaMaterials.md` section 2).

**Element lean (modes on plain mythril, not separate brand metals):** fire / water / dark-absorber / aether-phase.

#### Superconducting windings (invent / prestige apps)

Mythril can hold a persistent electrical current in a coil. SMES, MRI, motors, and Meissner bearings: `../Science/Energy/Generators.md`. Ceiling motor: `../Science/Energy/ElectricMotors.md`.

### Orihalcum (gold)

Any permanently converted gold is **orihalcum**. Magic resistance equals conversion % from the first moment. High-grade orihalcum is a different material from gold. Gold conducts electricity well; orihalcum still blocks mana. Mana conductivity does not follow electrical conductivity (`../../Runes/Energy.md`).

| Conversion | Magic resistance |
|---|---|
| 25% | 25% |
| 50% | 50% |
| 75% | 75% |
| 100% | 100% |

Orihalcum resists mana, so it fights further conversion. Nature stalls at low grades; high purity needs overwhelming concentration (deep dungeon cook or high altitude). Enchanting it is like projecting a movie onto black velvet: the image is swallowed and nothing seats. Refuses free enchantments; proximity still interferes with nearby work.

**Spelling:** metal = **orihalcum**. Guild rank name **Orichalcum** can stay as rank spelling.

- Thick plate and armor pass almost no mana at high conversion %. Thin foil still leaks.
- In a mostly-mythril anvil, a little orihalcum **blocks** stray forge mana.
- Full orihalcum kit is rare prestige: mage-hostile, empty of free enchantments.
- **Never** a rune host. **Mythril is unrelated.** **Adamantium is converted Ti**, not this.

### Aurium (copper)

Converted copper. Mundane copper is already a **decent mana path**. Aurium keeps that and **cuts waste**: it damps / contains flowing mana so less junk energy burns the host or leaks sideways. Not a hard block like orihalcum.

| | Still mana | Flowing mana |
|---|---|---|
| Aurium | Passes | Contained and damped (less waste) |
| Orihalcum | Blocked | Blocked |

`Insulation ≈ conversion` (burn vs bare metal falls as % rises). Ideal linings for mana pipes, pumps, grips, casting rods, stone wraps. Copper is COMMON, so low-grade aurium is industrial stock; high-grade is steep.

### Darkiron / star iron (iron)

| Conversion | Name |
|---|---|
| <80% | **Darkiron** |
| ≥80% | **Star iron** |

Same property line; dark look vs name at 80%. Mana-friendlier and tougher under damage as % rises. Meteoric iron that cooked in space for ages often falls as **star iron** (live “star metal” finds lean this way).

ODS-like mana-rich Fe stock. Hard to melt (magical blast furnaces). Harder to inscribe than ordinary iron. Still ferromagnetic (poor path feel vs austenitic hosts: `../../Runes/ManaMaterials.md` section 2).

### Darksteel / star steel (steel)

| Conversion | Name |
|---|---|
| <80% | **Darksteel** |
| ≥80% | **Star steel** |

Prime melee adventurer stock. Conversion improves **mana flow** in channels and **endurance under rune damage** (strain / burn resistance rises with %). Carbon slows conversion: smiths convert **iron → star iron**, then forge steel, faster than cooking blade steel at altitude. Darkiron → darksteel the same way.

Nonmagnetic austenitic hosts when the channel zone is converted. Cleaner path feel than ferromagnetic iron-line steel. Best common rune channels in steel weapons: convert the channel zone; keep hardened bulk elsewhere. Darksteel sits under star steel on the Energy.md ladder (`../../Runes/Energy.md`).

### Adamantium (titanium)

Converted titanium. **Molten: cast once.** After set: indestructible to ordinary force. No forge, cut, or reshape. Destroy only by resonant sound / mana vibration. Every piece must be cast in final form. Mundane titanium is not street stock.

**Enchanting:** adamantium carries little to no mana. Enchanting it is like projecting a movie onto clear glass: the image passes through and will not stick and its indestructible cast-final construction will not take alteration. It is not a rune host. It makes a great indestructible cover over a proper rune inlay in a real path metal underneath.

Extreme hardness and stiffness at weapon weight. Diamond-like thermal spreading plus mana-supported hardness. Orihalcum tools work by **starving mana support** at the contact face so brittle cleavage becomes possible on unfinished stock. Inscription stays hardest of the commons.

#### Form (cast-final)

**Locks:**
- **No stretch in any way.** No axial give, no elastic lengthening, no outer-fiber strain, no plastic set
- **No bend.** Solid adamantium never curves. Rod, wire, pole, plate, blade, vault: cast shape only
- Dead: `ε_max` / `R_min`, Adamweave, adamant cloth, knit, thread drapes, cord that “bends around” by filament flex

**Adamant mail:** the flexible product. Cast rings (or links) while setting; join into mail before they finish set. **Flex is only at the links.** Each ring is rigid, unstretchable adamantium. Shirt / hauberk / curtain armor, not cloth.

**Does not stop:** blunt through mail, thrust that drives rings into flesh, conducted heat, crush/constriction.

Infernal forge talk in Source maps to pre-set work or cutting mana support, not post-set quench-and-temper steel.

**Uses:** mail armor, mail curtains, linked screens, rigid cast parts (poles, plate, blades, vault stock, tower members, flywheel rims / axles / housings).

**Firearms invent (cast-final jobs):**
- **Barrel / chamber:** adamantium does not erode under hot powder gas. Double-base smokeless becomes the strongest practical propellant because barrel wear is gone. Chamber pressure is no longer limited by the tube; recoil, the shooter's body and the projectile surviving the pressure are the limits. Indestructible does not mean heat-proof: a steel-weight .50 barrel still climbs tens of °C per hot shot.
- **Penetrator needle:** `../../Combat/Firearms.md`. The barrel line above is the metal law. Powder choice: `../Science/Energy/GunpowderFirearms.md`.

#### Heat and sound (follows from no-bend stiffness)

**Why it conducts heat so well:** heat in a solid moves as lattice vibrations (phonons) plus free electrons. Phonon conduction scales with sound speed and with how far a vibration travels before scattering. A stiffer lattice carries vibration faster. A lattice that never yields is also almost perfectly elastic, so vibrations scatter far less and travel farther. Diamond is the real example: the stiffest common material is also the best heat conductor. Adamantium sits past diamond on stiffness, so it sits past diamond on conductivity.

"Doesn't bend" applies at the scale of hands, hammers and siege engines. Atoms still vibrate at atomic scale, which is how heat and sound move through it.

**Why expansion is ~0:** thermal expansion comes from uneven atomic vibration pushing atoms apart. A lattice that holds its shape against all force holds it against heat too.

| Material | Conductivity (W/m·K) | Diffusivity (m²/s) | Expansion (ppm/K) | Sound speed (m/s) |
|---|---|---|---|---|
| Titanium (CP) | ~22 | ~9×10⁻⁶ | 8.6 | ~6,100 |
| Steel | ~45–50 | ~1.2×10⁻⁵ | ~12 | ~5,900 |
| Copper | ~400 | ~1.1×10⁻⁴ | 16.5 | ~4,700 |
| Diamond | ~2,200 | ~1.2×10⁻³ | ~1 | ~18,000 |
| **Adamantium** | **~3,000** | **~1.25×10⁻³** | **~0** | **~20,000** |

Planning anchors (set piece, ~Ti density **~4.6 g/cm³**): tensile / hardness = no ordinary failure (indenter fails); pours molten ~**1,700 °C**; after set, no melt under ordinary forge heat. Specific heat ~**0.52 J/g·K**.

**Heat spread time (rough, t ≈ L² / diffusivity):**

| Distance | Titanium | Steel | Adamantium |
|---|---|---|---|
| Through 3 mm plate | ~1 s | ~0.75 s | <0.01 s |
| Across 30 cm | ~3 hours | ~2 hours | ~70 s |
| Across 1 m | ~1.3 days | ~1 day | ~13 min |

**Consequences (locked feel):**
- **No hot spots.** Flame on one point spreads across the whole piece fast. A torch on a blade tip warms the hilt within a minute or two.
- **Plate armor is a heat spreader.** The plate never fails to fire or frost. It pulls that heat or cold across the whole suit and into the wearer. A thick insulating underlayer (padded gambeson, Needle Worm silk, wool) is mandatory.
- **Mail spreads heat far less than plate.** Links touch only at small contact points, so heat crosses link to link slowly.
- **Heat sinks.** Ideal for cooling plates, quench blocks and forge tooling. Pairs with etherium tower cores (over-Jc quench dumps heat). Adamantium cladding over a mana-path metal also pulls mana-burn heat away from hot spots.
- **No thermal shock.** Near-zero expansion means it never warps or cracks from sudden heating or cooling.
- **Joint mismatch.** Steel rivets and mounts expand in heat while adamantium does not, so joints tighten or loosen with temperature. Steel cast around an adamantium part shrinks onto it as it cools (strong shrink-fit for hilts and mounts).
- **Exact-size casting.** It sets with no shrink, so molds need no shrinkage allowance. High conductivity freezes it fast against mold walls; pours must be fast into preheated molds.
- **It rings.** Near-zero internal damping means a struck plate rings like a bell for a long time. Adamantium-armored fighters are loud in combat.
- **Kitchen.** Even heat, no warp, inert surface, hot handles, ringing pots. Full pan / knife picks: `../../Food/CookwareAndKnives.md`.

**What indestructible means:** shape and structure hold under any ordinary force. Edges never dull. Force still transmits through it. A war hammer on adamantium plate leaves the plate untouched while the wearer still takes the momentum (concussions, bruising, broken bones under it).

#### Weakness / working method (locked destroy path)

**Lock:** destroy / soften after set only by **resonant sound / mana vibration** (same family as the Blaha–Langenecker acoustic softening analog). Each casting has its own resonant frequency; a sustained tone at that frequency softens or shatters it. Tuned tools (singing chisels, resonant presses) soften a line or zone for shaping or a clean cut. **Adamant mail:** every link rings at a slightly different frequency, so one tone breaks only a few links. **Plate** is one frequency, so one tone threatens the whole piece.

The stiffness that makes adamantium a top heat conductor also gives the ~20 km/s sound speed and near-zero damping that lets resonant vibration build. Heat physics already supports the sound weakness.

Inspirational alternate (not locked): electroplastic / forced dense mana current through a zone to loosen the lattice (runesmith-only work; armored fighters fear strong mages). Do not use unless a beat reopens this lock.

#### Handling (works with the locked weakness)

- **Cast to net shape.** Mold design is the real craft. Holes, slots, threads and edge geometry get cast in.
- **Cast sharp, stay sharp.** A blade edge cast into the mold never dulls.
- **Mechanical joining.** Star steel or darksteel rivets through cast-in holes. Other metals cast around adamantium for hilts, mounts and frames.
- **Cast-in-place chain.** Each new mail link is cast closed through already-set links.
- **Cladding.** Adamantium covers a real mana-path metal underneath.
- **Ordinary moving and lifting.** Light enough (Ti density band) for normal handling.

### Durium and durasteel

**Earth anchor: vanadium.** Durium is Terra’s vanadium-line magic metal. The hard particle inside durasteel is **durium carbide**, the analog of **vanadium carbide (VC, ~2,800 HV)**. Dead: tungsten-carbide density model (old ~12.5 g/cm³ durium / ~9–10 g/cm³ durasteel).

**Why vanadium (not W / Cr / Mo):**
- Real high-wear tool and knife steels (CPM 10V, S90V, 15V) use hard VC particles in a tough steel matrix. Same job as durasteel.
- Vanadium metal is steel-gray with a bluish tint; many vanadium compounds are blue. Durium ore’s dark blue sheen follows.
- Pure vanadium is fairly ductile. Small C / N / O make it badly brittle, so crude cavern-smelted durium is brittle on its own; clean refined durium is much stronger than iron.
- Historic wootz / Damascus research: trace vanadium in Indian ore formed carbide bands behind pattern and edge-holding. Fits Roland upgrading a forge from a mine find.

| Option | Hard particle | Why it fits less |
|---|---|---|
| **Vanadium** | VC ~2,800 HV | Best match |
| Tungsten | WC ~2,200–2,600 HV | Classic cermet, but heavy and gray; would make durasteel ~20–25% heavier than steel |
| Chromium | Cr carbides ~1,500–1,800 HV | Softer; reads as stainless / corrosion |
| Molybdenum | Mo carbides ~1,500–2,000 HV | Bluish-gray ore, but real role is hot strength more than wear |

**Durium:** refined vanadium-line metal from dark-blue ore (looks iron-like at a glance). Crude smelt = brittle; refined metal ≫ iron strength. **Durasteel:** darksteel matrix + **20–35% vol** durium carbide particles (cermet). Alone, only a little better than darksteel on rune-life from lattice damage under flow (`../../Runes/ManaMaterials.md` section 2). Etherium mix pushes enchant life toward mythril. **Aether durasteel** adds a thin mana-active phase for fire-gear buffs; still a poor wire.

| Material | Density (g/cm³) | Tensile (MPa) | Mohs | Vickers HV | Melting (°C) |
|---|---|---|---|---|---|
| Durium, refined metal | **~6.0** | **~800** | **~6.5** | **~250** | **~1,910** |
| Durium carbide (particle) | **~5.7** | brittle | **~9–9.5** | **~2,800** | **~2,800** |
| Durasteel (darksteel + 20–35% carbide by vol) | **~7.3–7.5** | **1,200–1,600** | **8–8.5** | **900–1,300** | Matrix limited |

Durasteel weighs about the same as ordinary steel (not 20–25% heavier). Weapons, armor, and golem parts keep normal handling weight.

### Etherium

Persistent-current store. Tower cores stay mostly **stationary** because motion bleeds pinned flux. Mixes raise Jc / storage and lower toughness. Over-Jc **quench** dumps the store as heat. Transfer feel is very clean. Digits unset. Path mode: persistent store (`../../Runes/ManaMaterials.md` section 1).

### Star silver, arcanite, and resistium

**Star silver:** clean silver-copper feel with radiation-hard rune-life bonus on the lattice-damage axis (`../../Runes/ManaMaterials.md` section 2). **Arcanite:** reserved prestige crystal. **Resistium:** ODS-style **additive**; inherits host path feel, raises rune life on the lattice-damage axis (section 2).

### Altitude vs time (open-air finish bands)

Cook is excess soak, not a log-altitude cheat:

```
(A − threshold_A) × time × speed ≈ K_%     // K_50 ≈ ln 2; K_90 ≈ ln 10; K_99 ≈ ln 100
```

Fixed % → 10× time allows ~1/10 the excess `A` (read new height from `ManaConcentration.md`). Faster metal (gold) finishes nearer its start height; titanium needs huge excess `A` or geological time.

**Planning anchors** (continuous open-air soak ≈ **1 year**). Heights are table landmarks, not the old `+20 mi × log₁₀` ladder.

| Metal | ~50% / 1 yr | ~80% / 1 yr | ~99% / 1 yr |
|---|---|---|---|
| Gold | ~12 mi (`A` ~4) | ~20 mi (`A` ~11) | ~30 mi (`A` ~32) |
| Silver | ~15 mi | ~22 mi (`A` ~14) | ~35 mi |
| Copper | ~18 mi | ~25 mi (`A` ~19) | ~40 mi (`A` ~93) |
| Iron | ~50 mi (`A` ~320) | ~62 mi Kármán (`A` ~1.7×10³) | ~100 mi (`A` ~1.8×10⁴) |
| Steel (1% C) | ~55 mi | ~62–100 mi | ~200 mi (`A` ~1.3×10⁵) |
| Titanium | ~100 mi | ~249 mi orbit (`A` ~2.7×10⁵) | ~370 mi+ / moon floor |

Gold / silver / copper can finish high grades in atmosphere on long cooks. Iron / steel want mesosphere–space or dungeon-equivalent `C`. Titanium high grades want orbit, moon soak, or deep dungeon. Moon ores at solar-wind floor are geological cooks (`ManaConcentration.md`; deposit split `../Space/Moons.md`).

Dungeon / spiritual soak is **narrative-pervasive**: a sea-level deep delve or holy/cursed site can match a high open-air cook band without flying. Mild floor `ΔC` digits are spell-feel only. Loot bias: **find old converted stock** more often than watch metal finish cooking on the trip.

### Story consequences

- Low-grade orihalcum common in dungeon **hoards** (old cook); high-grade wants long open-air cook, ~20–30 mi, or a narratively thick delve / spiritual site
- Low-grade aurium cheap (COMMON Cu); high-grade conduits costly
- Mythril: dungeon/spiritual finds and low sources; open air ≥~6 mi
- Star iron (≥80%): Kármán-band year cook, meteors, moon iron, or dungeon-equivalent narrative soak; darkiron from shorter high-ground / delve cooks
- Star steel: mostly forged from star iron; darksteel = affordable melee band
- Adamantium: hardest; year-scale high % is orbital / exobase; Terra crust deposits near nonexistent; moon / meteor Ti paths exist; dungeon adamantium is almost always **old find**, not fresh cook
- Silver near mages charges without converting → mythril stays rare

### Property anchors (planning)

Mundane Earth-like rows unchanged in feel. Named magic stock:

| Material | Mana / magic | Role |
|---|---|---|
| Mythril | Extreme conductivity / excellent flow; ~10% lighter than steel; sword-grade strength | Rune host / blades (Ag line) |
| Aurium | Damps flowing mana | Pipes, grips, wraps (Cu line) |
| Orihalcum | Antimagic = % | Shield stock (Au line) |
| Darkiron / star iron | Rising with % | Fe line |
| Darksteel / star steel | Rising with % | Melee blades / plate |
| Adamantium | Little/no mana; hard to alter (cast-final) | Indestructible cover over a real rune inlay |
| Durium / durasteel / aether durasteel | Earth-lean matrix; poor wire; **V / VC** density (steel-weight durasteel) | Cermet armor, tools, prestige hammers, golems |
| Arcanium / aetherium | Stone refine line | `MonsterCores.md` |
| Etherium | Persistent store; clean transfer | Tower cores, mixes |
| Star silver / resistium | Host-dependent | Rune-life additives |
| Arcanite | Reserved crystal | Prestige |

### Ebonite (shadow ore)

Separate from Fe conversion. Own black ore line. Unrefined / refined grades as before when a beat needs them.

---

## Inspirational physical numbers (NOT LOCKED)

> **Big note — inspirational only.** Tables below are Earth-anchored planning feel for scenes that need a digit. They are **not** rewrite locks. Locked law stays in the sections above (conversion lines, cook order, mana roles, adamantium cast-final / heat / sound weakness, vanadium–durium link). Prefer locked text on conflict. Promote a row into a lock only when a beat needs that number. Later invent stocks (perfectly rigid stock, mana nitinol, diamond-class heat sinks): `MaterialConsiderations.md`. Perfect-material motors: `../Science/Energy/ElectricMotors.md`.

### Mundane baselines (Earth, room temp, annealed unless noted)

`../Science/Metallurgy/EarthAlloys.md`. Terra conversion grades stay below.

### Suggested conversion scaling (inspirational)

Conversion does not add mass. Mana restructures the lattice. Most lines: density shifts only slightly while strength and hardness climb. **Mythril exception:** density falls with conversion as the superconducting lattice opens (locked sell: gear-grade ~**10% lighter than steel**).

- **Density, melting point:** linear. `P(c) = P0 + (P100 − P0) × c`
- **Strength, hardness, toughness:** back-loaded. `P(c) = P0 + (P100 − P0) × c^1.5`
- `c` = conversion fraction (0–1). Half conversion ≈ **~35%** of the strength gain (why fine / pure cost so much).

### Mythril (from silver) — inspirational grades

Low grades stay soft and drawable. Fine / pure take an edge and hold sword loads above ordinary blade steel; still take wire and fine inscription. **Extreme conductivity** remains the runic sell.

| Grade | Conversion | Density (g/cm³) | Tensile (MPa) | Mohs | Vickers HV | Melting (°C) |
|---|---|---|---|---|---|---|
| Silver | 0% | 10.49 | 150 | 2.5 | 25 | 962 |
| Low | ~20% | 9.50 | ~450 | 3.5 | ~120 | ~1,000 |
| Standard | ~50% | 8.40 | ~1,000 | 5.5 | ~350 | ~1,055 |
| Fine | ~85% | 7.30 | ~1,900 | 7 | ~700 | ~1,120 |
| Pure | 100% | 7.05 | ~2,200 | 7.5 | ~800 | ~1,150 |

Steel ≈ **7.85 g/cm³**. Pure mythril ≈ **7.05** (~**10%** lighter). Fine / pure tensile and hardness sit above ordinary hardened blade steel (~1,750 MPa / ~750 HV).

### Darkiron / star iron (from iron) — inspirational grades

Higher melt is the “hard to melt” feel. Still ferromagnetic.

| Grade | Conversion | Density (g/cm³) | Tensile (MPa) | Mohs | Vickers HV | Melting (°C) |
|---|---|---|---|---|---|---|
| Iron | 0% | 7.87 | 260 | 4 | 70 | 1,538 |
| Darkiron | ~50% | 7.84 | ~560 | 4.7 | ~170 | ~1,645 |
| Star iron | 80% | 7.82 | ~860 | 5.4 | ~270 | ~1,710 |
| Star iron, pure | 100% | 7.80 | ~1,100 | 6 | ~350 | ~1,750 |

### Darksteel / star steel (from steel) — inspirational multipliers

Steel has no single baseline; apply to the parent grade.

- Tensile: `× (1 + 0.8 c^1.5)`
- Hardness: `× (1 + 0.2 c^1.5)` (hardened steel is already near its ceiling)
- Fracture toughness K_IC: `× (1 + 2 c^1.5)` — **real sell:** mundane steel trades toughness for hardness; star steel breaks that trade
- Melting: `+ 200 c` °C
- Density: 7.85 → ~7.80

| Base | Conversion | Tensile (MPa) | Mohs | Vickers HV | K_IC (MPa√m) |
|---|---|---|---|---|---|
| 1095 hardened | 0% | ~1,750 | 7–8 | ~750 | ~20 |
| 1095 darksteel | ~50% | ~2,250 | ~8 | ~800 | ~34 |
| 1095 star steel | 80% | ~2,750 | ~8 | ~860 | ~49 |
| 1095 star steel, pure | 100% | ~3,150 | 8+ | ~900 | ~60 |
| 1045 star steel, pure | 100% | ~1,070 | ~5.5 | ~205 | ~150+ |

Pure hardened star steel holds the toughness of a mundane medium-carbon steel at blade-edge hardness.

### Orihalcum and aurium (pure) — inspirational

| Magical | Density (g/cm³) | Tensile (MPa) | Mohs | Vickers HV | Melting (°C) | Notes |
|---|---|---|---|---|---|---|
| Orihalcum | 18.8 | ~520 | 4.5 | ~160 | ~1,350 | Malleable at low/standard for cladding foil. Heavy. Cladding over a frame, not a frame. |
| Aurium | 8.7 | ~520 | 4 | ~140 | ~1,200 | Seamless tube / sheet linings. Work-hardened bronze range. |

### Related magic materials — inspirational physicals

Durium / durasteel **vanadium / VC** densities and HV in the locked Durium section above win over any older WC sheet. Rows here are feel only.

| Magical | Density (g/cm³) | Tensile (MPa) | Mohs | Vickers HV | Heat limit (°C) | Notes |
|---|---|---|---|---|---|---|
| Arcanium | ~3.3 | ~250 | 6.5 | ~650 | Disperses ~1,200 | Stone-metal. Brittle ceramic with a little metallic give. Disperses instead of melting (condensed mana will not stay condensed). |
| Aetherium | ~3.0 | ~650 | 7 | ~850 | Disperses ~1,500 | Purer / lighter than arcanium. Draws to fiber (mana fiber-optic feel). |
| Etherium | ~6.2 | ~900 cold-drawn | 5 | ~250 | Melts ~1,900 | NbTi-superconductor-wire feel. Ductile enough for tower-core coils. |
| Durium (refined metal) | ~6.0 | ~800 | ~6.5 | ~250 | Melts ~1,910 | Prefer locked V-line table above. |
| Durium carbide | ~5.7 | brittle | ~9–9.5 | ~2,800 | Melts ~2,800 | VC analog particle. |
| Durasteel | ~7.3–7.5 | 1,200–1,600 | 8–8.5 | 900–1,300 | Matrix limited | Steel-weight cermet; 20–35% vol carbide. Prefer locked table above. |
| Aether durasteel | ~7.0–7.4 | 1,200–1,600 | 8–8.5 | 900–1,300 | Matrix limited | Durasteel + thin aether phase; slightly lighter. |
| Star silver | ~10.1 | ~450 | 3.5 | ~120 | Melts ~900 | Sterling-like; lower melt than mythril from Cu content. |
| Resistium | ~5.0 (powder) | n/a (additive) | 7.5 | ~700 | Stable past host melt | ODS-style. Dose ~0.3–1.0% by weight; +20–40% hot strength / creep without changing host density much. |
| Arcanite | ~3.6 | n/a (crystal) | 9.5 | ~2,600 | Disperses ~2,000 | Reserved prestige. Diamond-class hardness; clean cleavage. Placeholder. |
| Ebonite | ~10.8 | ~700 | 6.5 | ~400 | Melts ~1,900 | Baseline grade only. |

## Open

- Converted-% host feel vs quality η_cond (quality ladder already locked in `Energy.md`)
- Absolute cook `speed` / `K_%` digits (finish table is landmark planning only)
- Ebonite geography
- Guild-rank spelling Orichalcum vs metal orihalcum (keep both unless prose confuses)
- Promote any inspirational physical row above only when a scene needs that digit
- Inspirational alternate adamantium weakness (forced mana current / electroplastic) stays Soft unless reopened

