# Metals

> Availability tags: `Materials.md`. Ambient altitude `C` / soak `A = √C`: `../Science/Energy/ManaConcentration.md`. Shop craft: `../Science/Metallurgy/CraftMetal.md`. Path η_cond: `../../Runes/Energy.md`.

## Narrative

Metals convert under mana concentration. Temporary charge bleeds off. Permanent conversion starts past a conductivity threshold and rises with time and soak. Names are **bands on one conversion meter**, not separate Earth elements.

## Detail

**Locks (parent lines):**
- **Silver → mythril**
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

Open air: no mythril below ~6 mi (`A` under thr). Dungeons / spiritual sites are the low sources. Elemental alignment stays **mythril** (no separate red-mythril brand).

Shop frame is often Ag–Cu eutectic. Look: **pearlish** light silvery gold. Reusable runic gear. **Not titanium.** Unrelated to orihalcum (converted gold) and adamantium (converted Ti, cast-final).

Mana path mode is **superconducting** from conversion, not from mundane Ag–Cu alone (transport law: `../../Runes/ManaMaterials.md` section 1; feel order: `../../Runes/Energy.md`).

- Steady flow near lossless up to a high **Jc**. Pulses pay a little AC-loss feel. Digits unset.
- **Quench is rare** on gear-grade stock. If it quenches, fall back toward ordinary poor-wire feel and dump heat. Do not treat quench as the normal failure of a mythril wand.
- **Pattern stability:** written patterns follow Néel-Arrhenius fading. **Δ** is the stability factor and characteristic lifetime is about **1×10⁻⁹ s × e^Δ**. **Wipe T** is the temperature where that lifetime collapses to minutes or less (ordering / Curie analog). Gear-grade mythril aims for **Δ ≈ 45 or more**, which survives combat heat near **350 K** for days to years. A forge fire can still erase a pattern. That is a forge hazard, not a fight tax. Heat fade is separate from dark/star rune-life resistance (`../../Runes/ManaMaterials.md` section 2).

**Element lean (modes on plain mythril, not separate brand metals):** fire / water / dark-absorber / aether-phase.

#### Superconducting windings (invent / prestige apps)

A superconducting winding is a coil of wire made from superconducting material. Like a copper winding, it carries current to create a magnetic field. The difference is that current flows with zero resistance (mythril / aether-mythril path mode).

**What zero resistance does**
- **No heat:** copper windings lose energy as heat (I²R loss). A superconducting winding loses nothing on steady DC however much current it carries.
- **Persistent current:** with the coil's ends joined in a closed loop, current circulates forever with no power supply. SMES coils and MRI magnets work this way. Etherium is the dedicated persistent-store metal; mythril windings can hold a persistent electrical current in the coil loop.
- **Much higher current density:** copper carries about 2 to 10 A/mm² before overheating. Current Earth superconductors carry 100 to 1,000+ A/mm². Gear-grade mythril still has a **Jc** ceiling; aether mythril aims higher.
- **Stronger fields:** more current in less space creates far stronger magnetic fields from a compact coil.

**Earth limits vs Caldris mythril**
- **Critical temperature:** Earth superconductors need cooling to between -269 °C and about -200 °C. Room-temperature mythril removes the cooling plant.
- **Critical field and critical current:** above a certain field or current, superconductivity collapses (a quench). Stored energy then turns into heat at once and can destroy the coil. Mythril **keeps Jc / quench** (rare on gear stock). Do not write it as perfect unlimited current.
- **Magnetic pressure:** strong fields push the windings outward. Adamantium or high-strength frames contain this; orihalcum is mana-resistant cladding / anvil damp, not the winding itself.
- **AC losses:** Earth superconductors lose a little when current changes quickly. Mythril pulses pay a little AC-loss feel. Steady DC is near lossless.

**Role in a flywheel / motor stack**
- **Motor/generator:** superconducting windings on the stator create a strong field. The rotor's magnets (or its own superconducting windings) turn through it. Charging speeds the rotor up and discharging slows it down.
- **Magnetic bearings:** superconductors push out magnetic fields (Meissner) and can lock magnets in place (flux pinning). This holds the rotor centered with no contact. Orihalcum plates are **mana-resistant** cladding (MR block), not superconducting bearings. Do not confuse shield stock with winding current.
- **Efficiency:** with no winding I²R loss, conversion between motion and electricity sits above 99% on the electrical side. Remaining losses are bearings, windage, and power electronics / rune converters.

Companions: `../Science/Energy/Batteries.md` (stone vs cell power), `../Science/Energy/RefinedMana.md` (Stillwire stone-refined wire; Lightthread), stone sockets as the mana feed.

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
- **Penetrator needle:** tungsten-dense cast needle about one third of the caliber in diameter, four calibers long, about a quarter of the bullet's weight, seated in a copper (or brass) slug. On armor impact the soft metal flattens and strips; the needle keeps going on a tiny point. It never blunts, bends or shatters. Hole is narrow (~4–8 mm). Behind armor it kills what it hits and throws some spall, with less wide damage than a copper bullet that gets through. Against flesh the copper still wounds; the needle separates and overpenetrates. Dig it out of a wreck and seat it in a fresh copper bullet. If density is only steel-like, cut needle penetration figures by about 60%. Full tier tables: `../../Combat/Firearms.md`.

### Durium and durasteel

**Durium:** hard brittle carbide/boride-like ore (dark blue sheen). **Durasteel:** durium particles in a darksteel matrix (cermet). Alone, slightly better than darksteel on rune-life from lattice damage under flow (`../../Runes/ManaMaterials.md` section 2). Etherium mix pushes enchant life toward mythril. **Aether durasteel** adds a thin mana-active phase for fire-gear buffs; still a poor wire.

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
| Mythril | Excellent flow | Rune host (Ag line) |
| Aurium | Damps flowing mana | Pipes, grips, wraps (Cu line) |
| Orihalcum | Antimagic = % | Shield stock (Au line) |
| Darkiron / star iron | Rising with % | Fe line |
| Darksteel / star steel | Rising with % | Melee blades / plate |
| Adamantium | Little/no mana; hard to alter (cast-final) | Indestructible cover over a real rune inlay |
| Durium / durasteel / aether durasteel | Earth-lean matrix; poor wire | Cermet armor and prestige hammers |
| Arcanium / aetherium | Stone refine line | `MonsterCores.md` |
| Etherium | Persistent store; clean transfer | Tower cores, mixes |
| Star silver / resistium | Host-dependent | Rune-life additives |
| Arcanite | Reserved crystal | Prestige |

### Ebonite (shadow ore)

Separate from Fe conversion. Own black ore line. Unrefined / refined grades as before when a beat needs them.

## Open

- Converted-% host feel vs quality η_cond (quality ladder already locked in `Energy.md`)
- Absolute cook `speed` / `K_%` digits (finish table is landmark planning only)
- Ebonite geography
- Guild-rank spelling Orichalcum vs metal orihalcum (keep both unless prose confuses)

