# Sensing, Mana and Sound Skills

> **Ideas / design loot.** Not automatic law. Live hubs win: `Skills.md`, `SkillsDesign.md`, `SkillRanks.md`, `../World/Science/Energy/Sound.md`. Direction: `../Ideas.md`, `../../Story/Notes/Early Logical Skills.md`.
>
> Use for feel tables and future evolve naming. Promote a row only when it **abides live rules** and a chapter needs it.

---

## Conflicts and soft-ok (read first)

### Live wins (do not replace)

| Topic | Live lock | This idea |
|---|---|---|
| **Diagnosis** | **D-only** transfer skill. Sees faults in systems. Caps L9; **Advanced Diagnosis** is a separate high tier, **not** an automatic evolve. Not earned by fusing Identify lines. | Tier 3 fusion of Appraise + Physician's Insight **named Diagnosis** |
| **Identify / Analyze** | Separate world skills. Analyze = first in-Terra unlock (formulas / how it works). Identify = names / tags. | Identify → Appraise; new **Examine** line; Analyze mostly absent |
| **Mana Sense** | Live aptitude; L9 early. Craft eyes / True Runic Sight / Eyes of Mana are separate later tracks | Mana Sense → Mana Sight → Mana Dominion |
| **Mana Shaping / Regulation** | Mage grants; Basic → evolved forms on class path | Shaping → Weaving; Regulation → Control; fuse to Dominion / Circulation |
| **Mana Absorption / Reinforcement** | Separate store skills (Ch 9.5). Reinforcement = body store / % max-MP pad while active | Absorption → Draw → Circulation; **Reinforcement missing** |
| **Echolocation** | Evolve → **Vibration Sense** (then Energy Sense in Sound.md). Not “Sonar” | Echolocation → Sonar → Resonance |
| **Sound Production** | Live Ch 19; pairs with Echo | → Sound Mastery → Resonance (naming parkable) |
| **Heat Sense** | Blacksmith’s Heat Sense live; Heat Resistance is separate | Heat Sense → Thermal Sight → Forge Sight |
| **Prefix ladder** | Basic / plain / Expert / … per `SkillRanks.md` | Generic Tier 1 / 2 / 3 with same M curve as resist ideas |

### Soft-ok (abides live; may use as feel)

- **M curve** 1.11×–10× / 11.1×–100× / 111×–1,000× as a *display* for sensitivity or precision on one skill’s L1–L9 → evolve → next evolve (same family as resist idea file).
- **Omnidirectional signals:** range × **√M**. **Echoes:** range × **M^(1/4)**. Error and read time ÷ M.
- **Tier unlocks new info kinds** that a multiplier alone cannot give (overlay vision, internal cracks, ultrasound band).
- **Sound Production power P** feeding echolocation range.
- **Heat Sense** as ±°C precision on glow / touch (not Heat Resistance).
- **Absorption rate vs Regulation safe throughput** (draw too fast without control → backlash). Live already separates Absorption and Regulation.
- **Stopped sharp → blunt** style thinking for sensing: a failed pierce of concealment still gives a weaker read (optional feel).

### Still idea-only

- Renaming Diagnosis as a **fusion** product; Examine / Physician's Insight as the path to it
- **Mana Dominion** rewriting or seizing foreign spells by M contest
- **Mana Circulation** near-zero sustained cast cost
- **Forge Sight** crystal-structure-in-real-time
- **Resonance** medical-ultrasound echolocation and shatter beams
- Treating Identify’s evolve as Appraise while ignoring Analyze

**Safer rewrite mapping if ever merged:** keep **Diagnosis** as D-only (maybe Examine/Physician as *flavor of what Diagnosis already does on bodies*). Put object depth on **Identify → Analyze / High Analyze** or Technology, not a second Diagnosis. Keep Echo evolve name **Vibration Sense**. Keep **Mana Reinforcement** beside Absorption.

---

## 1. Framework

### Tiers

| Tier | Levels | Multiplier (M) |
|---|---|---|
| Tier 1 | 1-9 | 1.11x to 10x |
| Tier 2 | 1-9 | 11.1x to 100x |
| Tier 3 | 1-9 | 111x to 1,000x |

- A Tier 1 skill at Lv9 evolves into its Tier 2 skill at Lv1.
- Two paired Tier 2 skills at Lv9 fuse into one Tier 3 skill at Lv1.

### Skill tree

| Tier 1 | Tier 2 | Tier 3 |
|---|---|---|
| Identify | Appraise | Diagnosis |
| Examine | Physician's Insight | Diagnosis |
| Mana Sense | Mana Sight | Mana Dominion |
| Mana Shaping | Mana Weaving | Mana Dominion |
| Mana Absorption | Mana Draw | Mana Circulation |
| Mana Regulation | Mana Control | Mana Circulation |
| Heat Sense | Thermal Sight | Forge Sight |
| Metal Understanding | Metal Insight | Forge Sight |
| Echolocation | Sonar | Resonance |
| Sound Production | Sound Mastery | Resonance |

Examine is a new skill in this idea. It supplies the biological half of Diagnosis. **Live:** Diagnosis already covers machine + body fault reads for Roland; do not invent Examine as a required gate to Diagnosis.

### Sensing rules

- M multiplies sensitivity. The weakest detectable signal drops to 1/M.
- Signals that spread in all directions fade with the square of distance, so detection range grows by √M.
- Echoes fade with the fourth power of distance, so echolocation range grows by M^(1/4).
- M divides measurement error and reading time.
- Each tier unlocks new kinds of information that a multiplier alone cannot produce.

*(Soft-ok physics.)*

### √M reference

| Lv | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| 1 | 1.05 | 3.33 | 10.5 |
| 5 | 1.41 | 4.47 | 14.1 |
| 9 | 3.16 | 10 | 31.6 |

---

## 2. Examination line

### Identify → Appraise (objects, materials, devices)

**What M multiplies:** readable complexity, concealment it can pierce and reading speed.

- **Readable complexity ≤ M**
- **Reading time = 10 s × complexity / M**
- **Concealment pierced when its strength ≤ M**

Complexity scale:

| Complexity | Example |
|---|---|
| 1 | Knife, rope, simple tool |
| 3 | Crossbow, basic lock |
| 10 | Firearm, clock |
| 30 | Engine |
| 100 | Vehicle, printing press |
| 1,000 | Ship, factory line, computer |

Identify Lv9 reads firearms and clocks. Appraise Lv9 reads vehicles. Diagnosis Lv9 reads ships and computers. *(Idea naming; live Diagnosis is not this product.)*

**Identify (Tier 1) reveals:** name, material, purpose, quality grade, visible damage and whether the item is enchanted.

**Appraise (Tier 2) adds:** internal mechanism, hidden flaws, maker, age, value, enchantment effects and how to operate it.

### Examine → Physician's Insight (living bodies)

**What M multiplies:** sensitivity. A condition is detected when its signs are at least 1/M as strong as an obvious case. Reading time = 10 s / M.

**Examine (Tier 1) reveals:** species, approximate age, sex, visible injuries, fatigue, intoxication and an overall health grade.

**Physician's Insight (Tier 2) adds:** internal injuries, internal bleeding, illness, poison type and dose, pregnancy, organ function, cause and prognosis.

### Diagnosis (Tier 3)

**Fusion:** Appraise Lv9 + Physician's Insight Lv9

- Complete functional understanding of any body or machine. This includes anything that combines the two, such as cybernetics, constructs, golems and cursed or enchanted bodies.
- Shows what is wrong, why it happened, how it will progress and what will fix it.
- Detects faults at 1/M of an obvious case. Lv1 detects 1/111. Lv9 detects 1/1,000, enough to find an early-stage tumor or a microscopic fatigue crack.
- Readable complexity reaches 1,000 at Lv9.

**Live conflict:** Roland already has Diagnosis at transfer. Treat this block as *power fantasy for a world-class diagnostician*, or as flavor for **Advanced Diagnosis**, not as his unlock path.

---

## 3. Mana Sense → Mana Sight

**What M multiplies:** sensitivity, so range grows by √M.

**Range = 3 m × √(S × M)**, where S is source strength relative to an average person's mana.

| Tier / Lv | Person (S = 1) | Strong spell (S = 100) | Great source (S = 10,000) |
|---|---|---|---|
| Tier 1 Lv5 | 4.2 m | 42 m | 424 m |
| Tier 1 Lv9 | 9.5 m | 95 m | 949 m |
| Tier 2 Lv5 | 13 m | 134 m | 1.3 km |
| Tier 2 Lv9 | 30 m | 300 m | 3 km |
| Tier 3 Lv5 | 42 m | 424 m | 4.2 km |
| Tier 3 Lv9 | 95 m | 949 m | 9.5 km |

**Mana Sense (Tier 1) reveals:** presence, direction, distance, rough strength and whether a spell is active or dormant.

**Mana Sight (Tier 2) adds:**
- Mana becomes visible as an overlay on normal sight.
- Element or affinity of a source.
- Mana flow inside bodies and objects.
- Individuals recognized by mana signature.
- Residual traces of past spells.
- Illusions of strength ≤ M are seen through.

*(Soft-ok as feel for Sense depth / later Eyes of Mana. Do not require renaming live craft-eye skills.)*

---

## 4. Mana Shaping → Mana Weaving

**What M multiplies:** precision, complexity and speed.

- **Shaping error = baseline / M.** Constructs are more stable and misfire less.
- **Max spell complexity = M components.** Baseline is a single-component spell.
- **Cast time = baseline / √M**

| Tier / Lv9 | Components | Cast Time |
|---|---|---|
| Tier 1 | 10 | 32% |
| Tier 2 | 100 | 10% |
| Tier 3 | 1,000 | 3.2% |

**Mana Shaping (Tier 1):** shapes the caster's own mana within touch range of the body.

**Mana Weaving (Tier 2) adds:**
- **Shaping reach = 1 m × M.** Lv1 reaches 11 m. Lv9 reaches 100 m.
- **Concurrent spells = √M, rounded down.** Lv1 holds 3. Lv9 holds 10.

### Mana Dominion (Tier 3)

**Fusion:** Mana Sight Lv9 + Mana Weaving Lv9

- Reads and reshapes external mana, including other casters' active spells.
- Unravels or seizes a foreign spell in a contest of multipliers. The higher M wins.
- Since Tier 3 starts at 111x, Mana Dominion beats every Tier 2 caster.
- Concurrent spells reach 31 at Lv9. Reach reaches 1 km at Lv9.

*(Idea-only power spike. Live Rune Authority / Manaflow Authority sit on class, not this fusion.)*

---

## 5. Mana Absorption and Mana Regulation

### Mana Absorption → Mana Draw

**What M multiplies:** absorption rate.

**Full pool refill time = 8 h / M × (normal density / local density)**

| Tier | Lv5 | Lv9 |
|---|---|---|
| Mana Absorption | 4 h | 48 min |
| Mana Draw | 24 min | 4.8 min |
| Tier 3 | 2.4 min | 29 s |

**Mana Absorption (Tier 1):** draws ambient mana while resting.

**Mana Draw (Tier 2) adds:** absorbs while moving and fighting, and draws from concentrated sources such as crystals, ley lines and spent spell residue.

Absorbing faster than Mana Regulation's safe throughput causes backlash.

*(Soft-ok split rate vs safe throughput. Live Absorption already cycles in combat; exact 8 h baseline is idea.)*

### Mana Regulation → Mana Control

**What M multiplies:** efficiency and safe throughput.

- **Extra spell cost from leakage = 100% / M.** An untrained caster spends double a spell's ideal cost.
- **Safe throughput = baseline × M.** Mana moved faster than this damages the caster's channels with pain, burns and mana burn.

| Tier | Lv5 Extra Cost | Lv9 Extra Cost |
|---|---|---|
| Mana Regulation | +50% | +10% |
| Mana Control | +5% | +1% |
| Tier 3 | +0.5% | +0.1% |

**Mana Control (Tier 2) adds:** suppression of the holder's own mana signature. Sensors with a lower M cannot detect the holder.

**Live:** Rune Mastery and class cost cuts also exist; do not double-count without a merge pass. **Mana Reinforcement** stays its own skill.

### Mana Circulation (Tier 3)

**Fusion:** Mana Draw Lv9 + Mana Control Lv9

- Absorbs and spends at the same time in a closed loop.
- When ambient mana supports the draw rate, sustained casting costs only leakage (0.1% to 0.9%).
- Absorption can no longer cause overload.

*(Idea-only.)*

---

## 6. Smithing senses

### Heat Sense → Thermal Sight

**What M multiplies:** temperature precision.

**Baseline:** an experienced smith reads steel by glow color to about ±50°C in good light.

**Error = ±50°C / M**

| Tier | Lv5 | Lv9 |
|---|---|---|
| Heat Sense | ±25°C | ±5°C |
| Thermal Sight | ±2.5°C | ±0.5°C |
| Forge Sight | ±0.25°C | ±0.05°C |

Glow color reference:

| Color | Temperature |
|---|---|
| Faint red | 500°C |
| Dull red | 600°C |
| Cherry red | 750°C |
| Orange | 900°C |
| Yellow | 1,100°C |
| White | 1,300°C+ |

**Heat Sense (Tier 1):** reads glowing metal by sight. Reads non-glowing objects by touch or close proximity.

**Thermal Sight (Tier 2) adds:**
- Reads any temperature at a glance, including objects below glowing heat.
- Reads the full piece, core and surface, so uneven heating is visible.
- Heat appears as a visual overlay. Warm bodies stand out in darkness.

*(Soft-ok precision table for Blacksmith’s Heat Sense depth.)*

### Metal Understanding → Metal Insight

**What M multiplies:** composition precision and flaw detection.

**Baseline:** an experienced smith's spark test estimates carbon content to about ±0.2% and finds surface flaws about 1 mm across.

| Tier / Lv9 | Carbon Precision | Smallest Flaw |
|---|---|---|
| Metal Understanding | ±0.02% | 0.1 mm |
| Metal Insight | ±0.002% | 10 µm |
| Forge Sight | ±0.0002% | 1 µm |

**Metal Understanding (Tier 1):** identifies metal and alloy type by sight, touch or sound. Reads carbon content, hardness grade and surface flaws.

**Metal Insight (Tier 2) adds:** internal cracks, inclusions, grain size, internal stress, heat-treatment state and trace elements.

*(Park beside Technology / Fabrication / Diagnosis on metal, not as required new named skills.)*

### Forge Sight (Tier 3)

**Fusion:** Thermal Sight Lv9 + Metal Insight Lv9

- Watches crystal structure change in real time during heating, quenching and hammering.
- Knows the exact result of a heat treatment before starting it.
- Predicts where and when a finished piece will fail.
- Works on every metal, including magical alloys.

*(Idea-only.)*

---

## 7. Sound skills

### Echolocation → Sonar

**What M multiplies:** echo sensitivity, so range grows by M^(1/4).

**Baseline:** a trained blind person using tongue clicks detects a person-sized object at about 5 m.

**Range = 5 m × (M_echo × P)^(1/4)**, where P is the Sound Production power multiplier (1 without it).

| Tier / Lv | Echolocation Alone | With Sound Production at Same Level |
|---|---|---|
| Tier 1 Lv5 | 6 m | 7 m |
| Tier 1 Lv9 | 9 m | 16 m |
| Tier 2 Lv5 | 11 m | 22 m |
| Tier 2 Lv9 | 16 m | 50 m |
| Resonance Lv5 | | 71 m |
| Resonance Lv9 | | 158 m |

Detail is limited by sound wavelength. Tongue clicks around 3 kHz resolve about 11 cm. Ultrasound at 100 kHz from Sound Mastery resolves about 3.4 mm.

**Echolocation (Tier 1) reveals:** shape, size, distance, gaps and openings.

**Sonar (Tier 2) adds:** motion and speed, surface hardness and material from echo texture, and full function underwater.

**Live evolve name:** **Vibration Sense** (`SkillsDesign.md`, `Sound.md`). Use Sonar as alt flavor or underwater specialty, not a silent rename.

### Sound Production → Sound Mastery

**What M multiplies:** acoustic power and pitch precision.

- **Volume gain = 10 × log10(M) dB**
- **Carry distance = baseline × √M**
- **Pitch error = ±50 cents / M**

**Baseline:** a loud shout reaches 100 dB at 1 m, carries about 200 m in quiet open air and holds pitch to about ±50 cents.

| Tier / Lv | Volume at 1 m | Carries | Pitch |
|---|---|---|---|
| Tier 1 Lv5 | 103 dB | 280 m | ±25 cents |
| Tier 1 Lv9 | 110 dB | 630 m | ±5 cents |
| Tier 2 Lv5 | 113 dB | 900 m | ±2.5 cents |
| Tier 2 Lv9 | 120 dB | 2 km | ±0.5 cents |
| Tier 3 Lv5 | 123 dB | 2.8 km | ±0.25 cents |
| Tier 3 Lv9 | 130 dB | 6.3 km | ±0.05 cents |

Sound landmarks:

| Level | Effect |
|---|---|
| 120 dB | Pain threshold |
| 130 dB | Hearing damage in seconds |
| 140 dB | Jet engine at close range |
| 150-160 dB | Eardrum rupture |

**Sound Production (Tier 1):** full vocal range across every register. Sustained output without strain.

**Sound Mastery (Tier 2) adds:**
- Infrasound and ultrasound, from 10 Hz to 100 kHz.
- Exact mimicry of any voice, animal or machine within range.
- Directional projection, adding 10 dB along the aimed line.

*(Soft-ok dB / √M carry as feel. Live Ch 19 is mana clicks + tongue, not shout spam.)*

### Resonance (Tier 3)

**Fusion:** Sonar Lv9 + Sound Mastery Lv9

- Echolocation reads internal structure, seeing inside walls, chests and bodies like medical ultrasound. This pairs naturally with Diagnosis.
- Focused sound beams add 20 dB along the aimed line, reaching 150 dB at Lv9. That ruptures eardrums at close range.
- Matching an object's resonant frequency shatters glass and cracks brittle materials like ice and thin stone.
- Concussive sound stuns targets within the beam.

*(Idea-only. Live Vibration Sense / Energy Sense stay the Echo evolve path.)*

---

## Cross-links

- Live Diagnosis / Identify / Analyze / Mana / Sound / Heat Sense: `SkillsDesign.md`
- Echo physics and evolve ladder: `../World/Science/Energy/Sound.md`
- Resist M twin: `ResistanceImmunitySystem.md`
- Short-climb brake for spam senses: `SkillLevelCostMultiplier.md`
- Other useful M lines: `OtherUsefulSkillsSystem.md`
- Early logical skill timing: `../../Story/Notes/Early Logical Skills.md`
