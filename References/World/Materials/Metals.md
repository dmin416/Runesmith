# Metals

> Availability tags: `Materials.md`. Ambient altitude `C` / soak `A = √C`: `../Science/Energy/ManaConcentration.md`. Shop craft: `../Science/Metallurgy/CraftMetal.md`. Path η_cond: `../../Runes/Energy.md`. Structural steel / aluminum EE-EC: `BuildingMaterials.md`. Deep production / strengthening: `BuildingMetals.md`.

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

Converted titanium. **Molten: cast once.** After set: indestructible to ordinary force. No forge, cut, or reshape. Destroy by casting-key resonance (street) or electron overload melt (rare). Every piece must be cast in final form. Mundane titanium is not street stock. Earth invent feel for rigid / unbreakable shafts and gears (geometry and traction still limit): `../Science/Vehicle/ShaftJointTransmission.md`.

**Enchanting / runes (locked):** adamantium **can** be enchanted and runed. The frozen lattice makes it a **stiff host**: seating takes more work, more setup skill and usually more paid mana than mythril or star steel because the metal will not yield, anneal or take a casual groove after set. Groove geometry is cast in at pour, or cut only by carefully driving the casting key along a line (singing chisel / resonant press). Once seated, the path geometry never warps and the piece never dulls, so finished adamantium runic gear is prestige-permanent. Mythril stays the easier clean everyday host. Cladding a softer path metal under an adamantium shell remains a valid simpler build.

Extreme hardness and stiffness at weapon weight. Electron heat spreading plus mana-supported hardness. Orihalcum tools work by **starving mana support** at the contact face so brittle cleavage becomes possible on unfinished stock. Post-set inscription is hardest of the commons (resonance tools or cast-in grooves).

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
- **Barrel / chamber:** adamantium does not erode under hot powder gas. Zero expansion means no heat warp or accuracy drift. Double-base smokeless becomes the strongest practical propellant because barrel wear is gone. Chamber pressure is no longer limited by the tube; recoil, the shooter's body and the projectile surviving the pressure are the limits. Low heat storage means barrel temperature climbs faster per shot, so cook-off risk arrives sooner without a water jacket or a heavy cladding sink.
- **Penetrator needle:** `../../Combat/Firearms.md`. The barrel line above is the metal law. Powder choice: `../Science/Energy/GunpowderFirearms.md`.

#### Heat and sound (frozen lattice)

**Premise (locked):** after set, adamantium atoms do not vibrate. No phonons. No thermal expansion. Ordinary force cannot shift lattice sites. Heat and ordinary electrical conduction live in the free-electron sea. One deliberate exception is the piece's **casting key** (single allowed acoustic mode; see destroy paths).

**Why it still spreads heat:** with no phonon scattering, cold adamantium is an exceptional electrical conductor (~**2.4 nΩ·m** at 300 K, about 7× better than copper). Wiedemann–Franz then yields thermal conductivity ~**3,000 W/m·K**, carried entirely by electrons (planning figure kept). Heat **storage** collapses to electronic heat capacity ~**20 J/kg·K** at 300 K (rises roughly with temperature), against titanium's ~520. High κ and low c_p give extreme thermal diffusivity ~**0.03 m²/s** (~25× diamond).

**Why expansion is 0:** thermal expansion needs uneven lattice vibration. Frozen sites do not push apart.

| Material | Conductivity (W/m·K) | Diffusivity (m²/s) | Expansion (ppm/K) | Stiffness band / sound speed (m/s) |
|---|---|---|---|---|
| Titanium (CP) | ~22 | ~9×10⁻⁶ | 8.6 | ~6,100 |
| Steel | ~45–50 | ~1.2×10⁻⁵ | ~12 | ~5,900 |
| Copper | ~400 | ~1.1×10⁻⁴ | 16.5 | ~4,700 |
| Diamond | ~2,200 | ~1.2×10⁻³ | ~1 | ~18,000 |
| **Adamantium** | **~3,000** | **~0.03** | **0** | **~20,000** (key / stiffness band) |

Planning anchors (set piece, density **~4.51 g/cm³**): tensile / hardness = no ordinary failure (indenter fails); pours molten ~**1,700 °C**; after set, no melt under ordinary forge heat; electrical resistivity ~**2.4 nΩ·m** at 300 K, rising with electron temperature squared (runaway past a high threshold); **no corrosion** (surface atoms cannot leave).

**Heat equalize time (rough, t ≈ L² / diffusivity):**

| Distance | Titanium | Steel | Adamantium |
|---|---|---|---|
| Through 5 mm plate | ~3 s | ~2 s | **<1 ms** |
| Across 0.5 m | ~8 hours | ~6 hours | **~8 s** |
| Across 1 m | ~1.3 days | ~1 day | **~30 s** |

**Consequences (locked feel):**
- **Conduit, not buffer.** Outer face temperature appears on the inner face almost at once. Sustained fire or dragon breath cooks the wearer faster than steel. A brief flame lick or hot strike spikes the inner face but stores little energy (a sting). After leaving the heat, the plate sheds and cools in seconds.
- **No hot spots.** Flame on one point equalizes across the piece in seconds, not minutes.
- **Plate armor needs insulation.** Gambeson, Needle Worm silk or wool underlayer is mandatory for fire/frost work.
- **Mail spreads heat far less than plate.** Links touch only at small contact points.
- **Heat sinks / quench / motors.** Excellent steady-state spreader and fast path into a real thermal mass (water channel, copper block). Poor surge sponge alone. Quench blocks want a sink behind them. Pairs with etherium tower cores; cladding pulls mana-burn heat off path metals.
- **Faraday / eddy behavior.** Plate and shells conduct so well that external fields and lightning tend to flow around the wearer. Changing magnetic fields drive strong eddy currents: slot motor cages and frames (`../Science/Energy/ElectricMotors.md`) or treat solid shells as deliberate brakes / shields.
- **No thermal shock / joint mismatch / exact-size casting.** Same as before: no warp from heat; steel mounts expand against it; molds need no shrink allowance; pours must be fast into preheated molds.
- **Strike sound.** A hit is a dull thud (rigid-body shove into the wearer). Energy that lands in the key builds a **pure sustained hum** at that casting's note. Internal damping is zero; air radiation and contact with padding / body set the real Q. Long fights leave ringing harnesses. Stored / racked gear is easier to sing apart than worn armor. Attacker's ordinary weapon may ring; the plate does not clang like a steel bell.
- **Kitchen / tongs / anvils.** Even, instant pans (thin stored heat; searing wants a strong burner). Tong handles heat in seconds: insulated grips mandatory. Anvil face: perfect rebound because the hammer or workpiece stores the spring; the adamantium does not absorb impact. Full pan / knife picks: `../../Food/CookwareAndKnives.md`.
- **Chemically inert.** No oxide scale, no acid dissolve after set. Basis for slime-proof kits (`../Fauna/Slimes.md`).

**What indestructible means:** shape and structure hold under any ordinary force. Edges never dull. Force still transmits through it. A war hammer on adamantium plate leaves the plate untouched while the wearer still takes the momentum (concussions, bruising, broken bones under it). Joints, rivets of lesser metal, straps and the body remain the weak points.

#### Destroy paths (ranked)

**1. Resonance (street / locked primary).** Soften or shatter by driving the piece's **casting key** (single allowed mode, fixed at set by shape and mass). Same family as Blaha–Langenecker acoustic softening. Internal Q is infinite; air and contact losses leave a very narrow but finite tuning window, so forge **ledgers** (or a matching fork) matter. Tuned tools (singing chisels, resonant presses) soften a line or zone. **Plate / blade:** one key threatens the whole piece. **Mail:** each link has its own key, so one tone breaks only a few links. Keys use the locked ~**20 km/s** stiffness band in a **bending-mode** model (bass / baritone for swords and shields; curved plates run higher than flat estimates):

| Object (rough) | Key (planning) |
|---|---|
| Greatsword ~1.3 m × 6 mm | ~75 Hz |
| Longsword ~1.0 m × 5 mm | ~105 Hz |
| Dagger ~0.3 m × 4 mm | ~900 Hz |
| Breastplate panel ~0.4 m × 2 mm (flat) | ~260 Hz |
| Tower shield ~1.5 m × 4 mm (flat) | ~35 Hz |

**2. Electron overload melt (rare / high-end).** Dump enough energy into the electron sea faster than the piece can radiate it away. Bonds fail and the piece **melts / flashes** near electron temperature **~11,600–16,700 K** with no glow-and-sag warning: vapor/plasma burst and pressure wave. Ordinary fire (~2,000 K) never reaches it. Needs runaway lightning, massive induction or focused heat/electric magic. Small currents pass almost freely; past the resistivity runaway, heating spikes.

**Energy requirement (locked planning, uniform heat-up):** electronic heat only, U ≈ ½ γ T² with titanium γ ≈ 3.35 mJ/mol·K². Cast law: **1 mana = 10 J** (`../../Runes/Energy.md`).

| Threshold | Electron T | Energy per kg | Mana per kg | ~0.75 kg longsword |
|---|---|---|---|---|
| Lower (≈1 eV nonthermal) | ~11,600 K | **~4.7 MJ/kg** | **~470,000 mana/kg** | **~350,000 mana** (~3.5 MJ) |
| Upper (Ti cohesive energy) | ~16,700 K | **~9.8 MJ/kg** | **~980,000 mana/kg** | **~730,000 mana** (~7.3 MJ) |

Street read: same ballpark as vaporizing ordinary steel by energy, but **power-gated**. Near threshold the piece radiates on the order of **~300 MW/m²** (~tens of MW for a sword face), so the dump must beat that loss rate. Slow heating never catches up. Local overload can melt a pit or hole; whole-piece melt wants uniform induction or full-body discharge.

**Mana friction Heat + mental focus:** unaided spot size from `../Science/Body/FocusCapacity.md`:

```
d = 100 μm / M
m = ρ d³                 // ρ ≈ 4.51 g/cm³; cube nugget
mana ≈ (4.7e5 to 9.8e5) × m_kg   // lower / upper melt table
```

Because adamantium is an electron **conduit**, heat from a spot on a large piece equalizes into the whole casting in microseconds to milliseconds. Mana friction on attached plate does **not** cheaply melt a 10 μm pit while the sword stays cold. Practical uses of fine focus:

1. **Detached speck / filing / cast bead** of size ~d: melt that nugget for ~mana above (usually << 1 mana).
2. **Whole piece:** pay the full piece mass × mana/kg (and the power gate), no matter how sharp the mind.
3. **Resonance cut** still beats melt for shaping attached stock.

| M | d | Nugget mass | Mana (lower–upper) |
|---|---|---|---|
| 1× | 100 μm | ~4.5 μg | ~0.002–0.004 |
| 10× | 10 μm | ~4.5 ng | ~2×10⁻⁶ – 4×10⁻⁶ |
| 20× | 5 μm | ~0.56 ng | ~3×10⁻⁷ – 6×10⁻⁷ |

Detached-nugget melt is trivial in mana. Killing a 0.75 kg blade is still ~350k–730k mana plus power.

**3. Radiation saturation (Soft doom clock only).** Extreme prolonged particle flux can transmute sites or trap helium without lattice relaxation. Natural background never matters. Not a street destroy path; open until a beat needs it.

Dead as post-set ordinary paths: forge heat, campfire melting, acid, grinding, quench-and-temper.

#### Handling (works with the locked weakness)

- **Cast to net shape.** Mold design is the real craft. Holes, slots, threads, edge geometry and the casting key are fixed at set.
- **Cast sharp, stay sharp.** A blade edge cast into the mold never dulls.
- **Record the key.** Smith ledgers (or a fork cut to the note) are the death note of that casting.
- **Mechanical joining.** Star steel or darksteel rivets through cast-in holes. Other metals cast around adamantium for hilts, mounts and frames.
- **Cast-in-place chain.** Each new mail link is cast closed through already-set links.
- **Cladding (optional).** Adamantium can cover a softer mana-path metal, or take the path itself as a stiff host.
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
| Adamantium | Frozen lattice; stiff rune host (hard seating); electron heat; resonance / electron-melt | Prestige runic gear; also valid as shell over a softer path |
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

- Converted-% host feel vs **rune-quality** η_cond (rune quality ladder already locked in `Energy.md`; not scroll quality)
- Absolute cook `speed` / `K_%` digits (finish table is landmark planning only)
- Ebonite geography
- Guild-rank spelling Orichalcum vs metal orihalcum (keep both unless prose confuses)
- Promote any inspirational physical row above only when a scene needs that digit
- Adamantium radiation-saturation doom clock (method 3) stays Soft until a beat needs fluence / ledger-drift digits

