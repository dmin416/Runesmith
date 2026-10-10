# Resistance and Immunity Skill System

> **Ideas / design loot.** Not automatic law. Live hubs win: `SkillsDesign.md`, `Skills.md`, `SkillRanks.md`, `RolandResistanceTracks.md`, `ResistanceGrindRarity.md`. Goals: `../People/Roland/Goals.md`.
>
> Use freely for feel, thresholds, and future evolve flavor. Promote a row into `SkillsDesign.md` only when it **abides live rules** and a chapter needs it.
>
> Harm → which resist soaks it: `DamageTypeResistances.md`. Multi-mechanism math + Survival family: `MultiMechanismResistance.md`.

---

## Conflicts and soft-ok (read first)

### Live wins (do not replace until accepted)

| Topic | Live lock | This idea |
|---|---|---|
| **Sleep Resistance** | −10% sleep **need** from L1 → Immunity to **1%** floor (`SkillsDesign.md`) | Mind family; natural sleep need only drops at **Iron Will** (conflicts) |
| **Heat / Cold** | −10% **effect** / level → Immunity to **1%** floor | Tolerance °C/K tables via M (cells survive real T; not insulation). Alternate model, not a silent replace |
| **Poison / Pain / Alcohol** | −10% effect (or soft Alcohol) → Immunity floor where locked | Same M math for Resistance tier; Fused / Purge / pain-switch are new |
| **Breath Control** | `hold = T0 × M_body × level`; 1 min = 1 use | Optional performance appendix only |
| **Recovery** | Live evolve track | Optional Wound Recovery appendix only |
| **Acid / Electricity** | Roland grind lock (`RolandResistanceTracks.md`) | Not in the four families below yet; keep separate until a family is written |

### Soft-ok (abides live; may use as feel without promoting Fused)

These match the live Resistance curve or already-locked tracks. Safe for notes and prose framing:

- **Resistance L1–L9 = 10%–90% resist** with **M = 1 / (1 − resistance)** is the same shape as live **−10% effect per level** (L9 → 10% effect left, M = 10).
- **Immunity** continuing toward a **~1% effect** floor matches live “Immunity to 1% floor” as a *display*; exact Immunity L1–L9 percents here are idea detail until printed.
- **Blunt + Sharp** kinetic pair (Sharp = pierce + slash): already locked in `RolandResistanceTracks.md`.
- **Momentum rule**, **whole-body blunt**, **stopped sharp → blunt check**: good physics; use in fights.
- **Access gating** at high ranks: matches `ResistanceGrindRarity.md` (ordinary life stops supplying doses).
- **Poison / Alcohol / Pain** as **effective = raw / M**: same family as live % effect.

### Still idea-only (cool, not law)

- **Fused** tier and names (**Temperature Immunity**, **Melee Immunity**, **Pure Blood**, **Iron Will**)
- Thermal **tolerance** thresholds as hard “no damage below °C” law (may conflict with simple % harm)
- **Purge**, **pain switch**, Iron Will **hours-of-sleep** table (Sleep need already live on Resistance)
- Performance ladders in the appendix (Aim, Climbing, etc.)

---

## 1. Core framework

### Skill tiers

| Tier | Levels | Resistance | Multiplier (M) |
|---|---|---|---|
| Resistance | 1-9 | 10% to 90% | 1.11x to 10x |
| Immunity | 1-9 | 91% to 99% | 11.1x to 100x |
| Fused | 1-9 | 99.1% to 99.9% | 111x to 1,000x |

- A Resistance skill at Lv9 evolves into the matching Immunity at Lv1.
- **Most families:** two paired Immunities at Lv9 fuse into one Fused skill at L1 (covers both types).
- **Survival exception:** **Undying Body** is a **multi-fuse** (2 or more deprivation Immunities). Full rule: `MultiMechanismResistance.md`.

### Multiplier by level

**M = 1 / (1 - resistance)**

| Lv | Resistance | Immunity | Fused |
|---|---|---|---|
| 1 | 10% / 1.11x | 91% / 11.1x | 99.1% / 111x |
| 2 | 20% / 1.25x | 92% / 12.5x | 99.2% / 125x |
| 3 | 30% / 1.43x | 93% / 14.3x | 99.3% / 143x |
| 4 | 40% / 1.67x | 94% / 16.7x | 99.4% / 167x |
| 5 | 50% / 2x | 95% / 20x | 99.5% / 200x |
| 6 | 60% / 2.5x | 96% / 25x | 99.6% / 250x |
| 7 | 70% / 3.33x | 97% / 33.3x | 99.7% / 333x |
| 8 | 80% / 5x | 98% / 50x | 99.8% / 500x |
| 9 | 90% / 10x | 99% / 100x | 99.9% / 1,000x |

Each tier repeats the same curve at ten times the scale of the tier before it.

### Skill families

**Thermal**
- Heat Resistance → Heat Immunity
- Cold Resistance → Cold Immunity
- Heat Immunity Lv9 + Cold Immunity Lv9 → **Temperature Immunity** (alt name: Thermal Immunity)

**Kinetic**
- Blunt Resistance → Blunt Immunity
- Sharp Resistance → Sharp Immunity
- Blunt Immunity Lv9 + Sharp Immunity Lv9 → **Melee Immunity** (alt name: Kinetic Immunity; also covers falls and bullets)

**Bodily**
- Poison Resistance → Poison Immunity
- Alcohol Resistance → Alcohol Immunity
- Poison Immunity Lv9 + Alcohol Immunity Lv9 → **Pure Blood**

**Mind**
- Sleep Resistance → Sleep Immunity
- Pain Resistance → Pain Immunity
- Sleep Immunity Lv9 + Pain Immunity Lv9 → **Iron Will**

*(Idea naming. Live Sleep already cuts sleep **need** on the Resistance tier; do not defer that to Iron Will in chapters.)*

**Survival** (full tree: `MultiMechanismResistance.md`)
- Suffocation Resistance → Suffocation Immunity
- Starvation Resistance → Starvation Immunity
- Sleep Resistance → Sleep Immunity *(live Sleep track; Survival fuse parent when promoted)*
- **Any 2+** of those Immunities at L9 → **Undying Body** (alt: Self-Sustaining); more can merge in later
- Coverage = union of parents (O₂/blood, food/water, sleep). Sleep into Undying Body conflicts with Mind → Iron Will; pick one fuse path for Sleep before promote.

*(Breath Control stays outside this tree until promoted.)*

### Threshold rule

All thresholds in this document are for a baseline human body. Physical quality is applied separately.

Below the threshold the character takes no damage no matter how long the exposure lasts. Above it, convert the exposure to its effective value using M and read the result as if it happened to a normal human.

*(Idea. Live Heat/Cold/Poison usually speak in % effect, not hard “below threshold = zero.” Use thresholds as landmarks unless promoted.)*

---

## 2. Thermal family (tolerance model)

These skills do **not** insulate. Heat and cold flow into the body at the normal rate. The tissue reaches the real temperature of the source. The skill lets the cells survive that temperature.

Consequences:
- Clothing and gear burn or freeze normally. Hair and nails count as body and are protected.
- Metal armor heats up at the normal rate.
- A hot skill-holder's skin can burn whoever touches it.
- Body water stays functional inside the threshold. It does not boil or form ice crystals.
- Insulation is not part of this system. An insulating effect can exist as a separate skill or item.

### Heat formulas

- **Tissue damage threshold (°C) = 37 + 7 × M**
- **Core limit (heatstroke) (°C) = 37 + 3 × M**
- **Over threshold: effective temperature (°C) = 37 + (T - 37) / M**

Baseline human burn times at a given tissue temperature:

| Tissue Temp | Time to Burn |
|---|---|
| 44°C | Hours |
| 50°C | About 5 minutes |
| 55°C | About 30 seconds |
| 60°C | About 5 seconds |
| 70°C | About 1 second |
| 100°C+ | Instant |

### Heat thresholds

| Lv | Heat Resistance | Heat Immunity | Temperature Immunity |
|---|---|---|---|
| 1 | 45°C | 115°C | 814°C |
| 2 | 46°C | 125°C | 912°C |
| 3 | 47°C | 137°C | 1,038°C |
| 4 | 49°C | 154°C | 1,206°C |
| 5 | 51°C | 177°C | 1,437°C |
| 6 | 55°C | 212°C | 1,787°C |
| 7 | 60°C | 270°C | 2,368°C |
| 8 | 72°C | 387°C | 3,537°C |
| 9 | 107°C | 737°C | 7,037°C |

Heat landmarks:

| Source | Temperature |
|---|---|
| Hot tap water | 50-60°C |
| Fresh coffee | 70-85°C |
| Boiling water | 100°C |
| Frying oil | 175-190°C |
| Home oven at max | 250-290°C |
| Wood-fired oven | 400-480°C |
| Campfire | 600-900°C |
| Lava | 1,100-1,200°C |
| Steel melting | 1,370-1,510°C |
| Tungsten melting | 3,422°C |
| Sun's surface | 5,500°C |
| Lightning channel | About 30,000°C |

### Cold formulas

Cold uses absolute temperature (Kelvin) because absolute zero is a hard floor. A linear scale would hit that floor during the Resistance tier.

- **Tissue damage threshold (K) = 271 / (0.9 + 0.1 × M)**
- **Core limit (hypothermia) (K) = 308 / (0.9 + 0.1 × M)**
- **Over threshold: effective temperature (K) = T × (0.9 + 0.1 × M)**, capped at 310 K
- °C = K - 273

Baseline human frostbite times by wind-chill temperature:

| Wind Chill | Time to Frostbite |
|---|---|
| -10°C | Low risk |
| -28°C | About 30 minutes |
| -40°C | About 10 minutes |
| -48°C | About 5 minutes |
| -55°C | Under 2 minutes |

Contact with cold metal or cryogenic liquid is much faster than air at the same temperature.

### Cold thresholds

| Lv | Cold Resistance | Cold Immunity | Temperature Immunity |
|---|---|---|---|
| 1 | -5°C | -138°C | 22.6 K |
| 2 | -9°C | -147°C | 20.2 K |
| 3 | -13°C | -157°C | 17.8 K |
| 4 | -19°C | -168°C | 15.4 K |
| 5 | -27°C | -180°C | 13.0 K |
| 6 | -37°C | -193°C | 10.5 K |
| 7 | -53°C | -209°C | 7.9 K |
| 8 | -80°C | -227°C | 5.3 K |
| 9 | -130°C | -248°C | 2.7 K |

Cold landmarks:

| Source | Temperature |
|---|---|
| Coldest recorded on Earth | -89°C |
| Liquid nitrogen | -196°C (77 K) |
| Liquid hydrogen | 20 K |
| Liquid helium | 4.2 K |
| Deep space | 2.7 K |

Cold Resistance covers every natural climate on Earth by Lv8-9. Heat climbs slower against its hazards because fire and lava sit far above body temperature. Temperature Immunity Lv9 handles both the sun's surface and deep space.

### Worked example: hand in an 800°C campfire

- Heat Resistance Lv9 (M = 10): effective 113°C. Burns instantly.
- Heat Immunity Lv5 (M = 20): effective 75°C. Burns in about a second.
- Heat Immunity Lv8 (M = 50): effective 52°C. Burns in a few minutes.
- Heat Immunity Lv9 (M = 100): effective 45°C. Hours before any damage.
- Temperature Immunity Lv1 (M = 111): under threshold. No damage, indefinitely.

---

## 3. Kinetic family

### Momentum rule

These skills do not cancel momentum. A hammer still moves the target, a truck still launches them and a fall still ends in a sudden stop. Knockback is the same as for a normal person of the same mass. Holding ground depends on footing, mass and Strength.

*(Soft-ok.)*

### Whole-body rule

Blunt injury comes from compression, shear and acceleration. The brain hits the skull, organs tear from their attachments and blood vessels rupture. Blunt tolerance applies to every tissue, including the brain and internal organs. Skin-only toughness does not prevent concussion.

*(Soft-ok.)*

### Weak points

Eyes, ear canals and the lining of the mouth and throat use the multiplier one level lower than the skill.

### Blunt formulas

- **Concussion: 80 g × M**
- **Rib fracture: 2,000 N × M**
- **Skull fracture: 5,000 N × M**
- **Chest crush becomes dangerous: about 300 kg × M**
- **Uninjured impact speed: 7 × √M m/s**

### Uninjured impact speed

| Lv | Blunt Resistance | Blunt Immunity | Melee Immunity |
|---|---|---|---|
| 1 | 27 km/h | 84 km/h | 266 km/h |
| 2 | 28 km/h | 89 km/h | 282 km/h |
| 3 | 30 km/h | 95 km/h | 301 km/h |
| 4 | 33 km/h | 103 km/h | 326 km/h |
| 5 | 36 km/h | 113 km/h | 356 km/h |
| 6 | 40 km/h | 126 km/h | 398 km/h |
| 7 | 46 km/h | 145 km/h | 460 km/h |
| 8 | 56 km/h | 178 km/h | 563 km/h |
| 9 | 80 km/h | 252 km/h | 797 km/h |

Impact landmarks:

| Impact | Speed |
|---|---|
| 2.5 m fall | 25 km/h |
| 12 m fall (four stories) | 56 km/h |
| 25 m fall, car at city speed | 80 km/h |
| 50 m fall, unrestrained highway crash | 113 km/h |
| Terminal velocity (any fall height) | About 200 km/h |
| Bullet train | 300 km/h |
| Airliner at cruise | 800-900 km/h |

Blunt Immunity Lv9 survives a fall from any height uninjured. *(Idea landmark.)*

### Force thresholds at each tier's Lv9

| | Resistance Lv9 | Immunity Lv9 | Melee Immunity Lv9 |
|---|---|---|---|
| Concussion | 800 g | 8,000 g | 80,000 g |
| Rib fracture | 20 kN | 200 kN | 2 MN |
| Skull fracture | 50 kN | 500 kN | 5 MN |
| Chest crush | 3 t | 30 t | 300 t |

### Sharp formulas

Skin is the main barrier against cutting and piercing. Once skin is breached, fat and muscle part easily. Humans are far weaker against sharp force than blunt force.

- **Puncture or cut force: 20 N × M**
- **Bullet stop velocity: 60 × √M m/s**
- Armor-piercing rounds treat the target as one level lower.
- A superhuman attacker's force scales with their Strength multiplier.

### Sharp thresholds

| Lv | Sharp Resistance | Sharp Immunity | Melee Immunity |
|---|---|---|---|
| 1 | 22 N / 63 m/s | 222 N / 200 m/s | 2,220 N / 632 m/s |
| 2 | 25 N / 67 m/s | 250 N / 212 m/s | 2,500 N / 671 m/s |
| 3 | 29 N / 72 m/s | 286 N / 227 m/s | 2,860 N / 717 m/s |
| 4 | 33 N / 78 m/s | 334 N / 245 m/s | 3,340 N / 775 m/s |
| 5 | 40 N / 85 m/s | 400 N / 268 m/s | 4,000 N / 849 m/s |
| 6 | 50 N / 95 m/s | 500 N / 300 m/s | 5,000 N / 949 m/s |
| 7 | 67 N / 109 m/s | 666 N / 346 m/s | 6,660 N / 1,095 m/s |
| 8 | 100 N / 134 m/s | 1,000 N / 424 m/s | 10,000 N / 1,342 m/s |
| 9 | 200 N / 190 m/s | 2,000 N / 600 m/s | 20,000 N / 1,897 m/s |

Sharp landmarks:

| Attack | Force or Velocity |
|---|---|
| Sharp knife tip through skin | 10-50 N |
| Committed one-handed stab | 500-1,000 N |
| Overhand or two-handed stab | Up to about 2,000 N |
| 9mm handgun | About 360 m/s |
| .357 Magnum | About 440 m/s |
| 7.62x39 rifle | About 715 m/s |
| .50 BMG | About 890 m/s |
| 5.56 rifle | About 940 m/s |

Key points:
- Sharp Immunity Lv5: casual knife attacks fail. Committed stabs still penetrate.
- Sharp Immunity Lv8: 9mm stops at the skin.
- Sharp Immunity Lv9: blades driven by normal human strength fail. All handguns stop.
- Melee Immunity Lv3: 7.62x39 stops.
- Melee Immunity Lv6: 5.56 and .50 BMG stop.
- Melee Immunity Lv9: all small arms stop.

### Stopped weapons become blunt

A blade or bullet that fails to pierce delivers its force as blunt trauma on a small area. That hit is checked against the blunt skill.
- A stopped handgun round hits like a heavy punch.
- A stopped rifle round hits like a sledgehammer.
- A greatsword that cannot cut becomes an iron club.

A Sharp-only character is cut-proof yet breakable. A Blunt-only character shrugs off hammers while a knife still slides in. Melee Immunity removes both gaps.

*(Soft-ok.)*

### What it looks like

Sledgehammer to the chest at high Blunt tiers: a dull thud like hitting a sandbag. The flesh dimples and springs back with no bruise. The body staggers back as far as a normal person's would. The shirt can still tear. The hammer may rebound hard enough to jar the swinger's wrists.

Hit by a truck: launched, tumbles 20 m and gets up. Clothes are shredded and carried gear breaks.

Pinned under rubble: no injury, yet still trapped. Breathing only works if Strength can lift the ribs against the weight.

---

## 4. Bodily family

### Poison Resistance → Poison Immunity

- **Effective dose = actual dose / M**
- Doses are per kilogram of body mass, as in standard toxicology.
- A dose of N lethal doses acts like N / M lethal doses.
- Methanol and other toxic alcohols count as poison. Drinking alcohol is covered by Alcohol Resistance.
- Sedatives are checked against both Poison (body harm) and Sleep (drowsiness).

*(Effective dose / M is soft-ok with live % toxin effect.)*

Poison landmarks:

| Tier | Effect |
|---|---|
| Poison Resistance Lv5 (2x) | A lethal snakebite becomes serious illness |
| Poison Resistance Lv9 (10x) | One lethal dose causes mild symptoms. Ten lethal doses kill. |
| Poison Immunity Lv5 (20x) | Most single poisonings do nothing noticeable |
| Poison Immunity Lv9 (100x) | 10-20 g of cyanide is survivable. One hundred death cap mushrooms are survivable. |
| Pure Blood Lv9 (1,000x) | Survives up to a thousand lethal doses of anything |

### Alcohol Resistance → Alcohol Immunity

- **Effective BAC = actual BAC / M**
- Optional rule: the holder can voluntarily lower the skill to enjoy a drink.

Baseline effects by blood alcohol content (BAC):

| BAC | Effect |
|---|---|
| 0.05% | Relaxed, mildly loosened |
| 0.08% | Impaired, legal driving limit in many places |
| 0.15% | Heavily drunk |
| 0.30% | Stupor, blackout |
| 0.40%+ | Potentially lethal |

Standard drinks within one hour for a 70 kg adult to feel 0.08% (baseline 4 × M):

| Tier | Lv5 | Lv9 |
|---|---|---|
| Alcohol Resistance | 8 | 40 |
| Alcohol Immunity | 80 | 400 |
| Pure Blood | 800 | 4,000 |

- From Alcohol Immunity onward, a character cannot physically drink enough to get drunk.
- Hangover severity = baseline / M.
- Alcohol poisoning uses the same effective BAC.

### Pure Blood (Fused)

**Fusion:** Poison Immunity Lv9 + Alcohol Immunity Lv9

- M of 111x to 1,000x against all poisons and intoxicants.
- Unlocks Purge: the holder can expel any substance from the body at will through sweat, breath or vomiting.

*(Idea-only.)*

---

## 5. Mind family

### Sleep Resistance → Sleep Immunity

Covers forced sleep and drowsiness from substances, magic and fatigue effects.

**Live conflict:** chapters already cut **natural sleep need** on Sleep Resistance (−10%/level). Do not wait for Iron Will to apply that. This section’s “natural sleep need stays the same until Fused” is **idea-only** and loses to live.

Idea extras still parkable:
- **Sedatives: effective dose = actual dose / M**
- **Sleep magic: effective potency = spell potency / M.** The target falls asleep only if effective potency is 1 or higher.
- **Forced sleep duration = normal duration / M**
- Medical anesthesia needs M times the normal dose unless the holder voluntarily lowers the skill.

### Pain Resistance → Pain Immunity

- **Effective pain = raw pain / M**
- Raw pain uses a 0-10 scale that continues past 10 for extreme injuries.

*(Soft-ok with live −10% felt pain.)*

Raw pain by injury:

| Injury | Raw Pain |
|---|---|
| Paper cut | 1-2 |
| Stubbed toe | 3-4 |
| Deep cut | 5-6 |
| Broken bone | 7-8 |
| Kidney stone, major burn | 9-10 |
| Amputation, crushed limb | 12-15 |
| Torture, burned alive | 20+ |

Effects of effective pain:

| Effective Pain | Effect |
|---|---|
| 1-3 | Distracting |
| 4-6 | Penalties to concentration and fine skills |
| 7-8 | Severe. Most actions impaired. |
| 9-10 | Incapacitating |
| 10+ | Pain shock, fainting |

Examples:
- Pain Resistance Lv5 (2x): a broken bone acts as 4.
- Pain Resistance Lv9 (10x): an amputation acts as 1.2-1.5.
- Pain Immunity Lv9 (100x): torture at 20 acts as 0.2.

Rules:
- The skill reduces suffering, not awareness. The holder still knows where and how badly they are hurt.
- Injuries still impair function mechanically. A broken leg cannot bear weight at any level.
- Pain Immunity Lv1 unlocks a pain switch: the holder can turn pain fully on or off at will. *(Idea-only.)*

### Iron Will (Fused)

**Fusion:** Sleep Immunity Lv9 + Pain Immunity Lv9

- M of 111x to 1,000x against forced sleep, sedation and pain.
- Pain-based torture and interrogation fail completely.
- Natural sleep need drops by level *(idea table; live already drops need on Sleep Resistance)*:

| Lv | Sleep Needed per Day |
|---|---|
| 1 | 7 h |
| 2 | 6.5 h |
| 3 | 6 h |
| 4 | 5.5 h |
| 5 | 5 h |
| 6 | 4 h |
| 7 | 3 h |
| 8 | 2 h |
| 9 | 1 h |

---

## 6. Training

### Training sources

- **Heat:** saunas, kitchens, forges, fire-walking, volcanic regions, fire magic
- **Cold:** ice baths, winter exposure, high altitude, frost magic, cryogenic monsters
- **Blunt:** sparring, fall training, iron-body conditioning, combat, siege weapons
- **Sharp:** blade conditioning, combat, arrow fire, gunfire at high tiers
- **Poison:** controlled dosing (mithridatism), venomous monsters, alchemical poisons
- **Alcohol:** heavy drinking, strong spirits, alchemical liquors
- **Sleep:** sedatives, sleep magic, forced wakefulness under fatigue effects
- **Pain:** hard conditioning, injury, endurance drills

### Access gating

At high levels, ordinary life stops supplying stimuli that come anywhere near the threshold. Growth requires seeking out forges, lava fields, cryogenic zones, terminal-velocity falls, siege weapons or monster venom. This creates natural plot hooks for progression.

*(Soft-ok; see `ResistanceGrindRarity.md`.)*

---

## Appendix: performance skills (optional park)

Same M tiers. Not resistance law. Prefer live **Breath Control** / **Recovery** / **Marksmanship** names until merged.

### Shared rules

- M multiplies one performance quantity per skill. When that quantity is energy, speed rises by √M.
- A multiplier can only scale what a human body already does. Things a human body cannot do at any speed unlock at a set tier instead.

### Breath Holding → Suffocation Immunity

**What M multiplies:** oxygen efficiency. Live chapters: **Breath Control**.

**Baseline:** a 60 s hold at rest, 20 s under hard exertion, and about 10 s to blackout from a blood choke.

| Tier | Lv5 | Lv9 |
|---|---|---|
| Breath Holding | 2 min | 10 min |
| Suffocation Immunity | 20 min | 1 h 40 min |
| Fused | 3 h 20 min | 16 h 40 min |

### Aim → True Aim

**What M multiplies:** precision. Prefer live **Marksmanship**.

### Throwing → Cannon Arm

**What M multiplies:** energy to the thrown object (speed × √M).

### Climbing → Sheer Climb

**What M multiplies:** grip and climbing stamina.

### Wound Recovery → Rapid Healing / Blood Recovery → Iron Blood

Prefer live **Recovery** / **Rapid Recovery**. Fused regrowth stays idea-only.

---

## Cross-links

- Live Sleep / Heat / Cold / Poison / Pain / Alcohol / Breath: `SkillsDesign.md`
- Roland grind tracks (incl. Acid / Electricity / Blunt / Sharp): `RolandResistanceTracks.md`
- How rare deliberate torture grinds are: `ResistanceGrindRarity.md`
- Thin skill law: `Skills.md`
- Body M for breath/blood: `Attributes.md`
- Other useful M lines: `OtherUsefulSkillsSystem.md`
- Sense / mana / sound ideas: `SensingManaSoundSystem.md`
- Direction loot: `../Ideas.md`
