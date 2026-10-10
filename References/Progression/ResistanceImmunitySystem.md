# Resistance and Immunity Skill System (Idea)

> **Unread idea / design loot.** Not reviewed. **Not a lock.** Do not replace live body resists until accepted. Live hubs: `Skills.md`, `SkillsDesign.md`, `Attributes.md`, `SkillRanks.md`. Goals wishlist: `../People/Roland/Goals.md`.

Parked framework for Resistance → Immunity → Fused tiers with multiplier **M = 1 / (1 − resistance)** and worked thermal / kinetic / bodily / performance tables.

---

## Conflicts with live law (read first)

Most of this is okay as direction loot. These rows already have live rewrite math and **win** until this file is promoted:

| Topic | Live lock | This idea |
|---|---|---|
| **Sleep Resistance** | −10% sleep **need** per level → Sleep Immunity to **1%** floor (`SkillsDesign.md`, `Ideas.md`) | Part of Bodily family; Pure Body also cuts sleep need by hours table |
| **Heat / Cold Resistance** | −10% **effect** per level → Immunity to **1%** floor (`SkillsDesign.md`) | Tolerance temperatures via M (cells survive real T; not insulation) |
| **Poison Resistance** | −10% toxin effect per level (`SkillsDesign.md`) | Effective dose = dose / M |
| **Breath Control** | `hold = T0 × M_body × BreathControl_level` with **1 min held = 1 use** (`SkillsDesign.md`, Ch 19 / Goals) | Renamed ladder Breath Holding → Suffocation Immunity → Fused; M from resistance % curve |
| **Recovery / Rapid Recovery** | Live evolve track in Skills | Wound Recovery → Rapid Healing → Fused with regrowth unlock |
| **Marksmanship** | Live combat skill | Aim → True Aim → Fused (separate idea ladder) |

**Breath holds:** already in file. Prefer live **Breath Control** name and body×level formula for chapters. This idea's oxygen-efficiency M table is optional alternate or evolve flavor if merged later.

**Shared shape that already matches live:** L1–L9 then evolve; −10%/level toward a high Immunity band is the same *family* of curve this idea stretches into Fused (99.1–99.9%).

---

## 1. Core framework

### Skill tiers

| Tier | Levels | Resistance | Multiplier (M) |
|---|---|---|---|
| Resistance | 1-9 | 10% to 90% | 1.11x to 10x |
| Immunity | 1-9 | 91% to 99% | 11.1x to 100x |
| Fused | 1-9 | 99.1% to 99.9% | 111x to 1,000x |

- A Resistance skill at Lv9 evolves into the matching Immunity at Lv1.
- Two paired Immunities at Lv9 fuse into one Fused skill at Lv1. The Fused skill covers both damage types.

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
- Blunt Immunity Lv9 + Sharp Immunity Lv9 → **Melee Immunity** (alt name: Kinetic Immunity, since it also covers falls and bullets)

**Bodily**
- Toxin Resistance → Toxin Immunity
- Sleep Resistance → Sleep Immunity
- Toxin Immunity Lv9 + Sleep Immunity Lv9 → **Pure Body** (alt name: Inviolate Vessel)

### Threshold rule

All thresholds in this document are for a baseline human body. Physical quality is applied separately.

Below the threshold the character takes no damage no matter how long the exposure lasts. Above it, convert the exposure to its effective value using M and read the result as if it happened to a normal human.

---

## 2. Thermal family (tolerance model)

These skills do not insulate. Heat and cold flow into the body at the normal rate. The tissue reaches the real temperature of the source. The skill lets the cells survive that temperature.

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

### Whole-body rule

Blunt injury comes from compression, shear and acceleration. The brain hits the skull, organs tear from their attachments and blood vessels rupture. Blunt tolerance applies to every tissue, including the brain and internal organs. Skin-only toughness does not prevent concussion.

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

Blunt Immunity Lv9 survives a fall from any height uninjured.

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

### What it looks like

Sledgehammer to the chest at high Blunt tiers: a dull thud like hitting a sandbag. The flesh dimples and springs back with no bruise. The body staggers back as far as a normal person's would. The shirt can still tear. The hammer may rebound hard enough to jar the swinger's wrists.

Hit by a truck: launched, tumbles 20 m and gets up. Clothes are shredded and carried gear breaks.

Pinned under rubble: no injury, yet still trapped. Breathing only works if Strength can lift the ribs against the weight.

---

## 4. Bodily family

### Toxin formulas

- **Effective dose = actual dose / M**
- Doses are per kilogram of body mass, as in standard toxicology.
- A dose of N lethal doses acts like N / M lethal doses.
- Optional rule: the holder can voluntarily lower the skill to let a substance through (alcohol, medicine).

Toxin landmarks:

| Tier | Effect |
|---|---|
| Resistance Lv5 (2x) | A lethal snakebite becomes serious illness |
| Resistance Lv9 (10x) | One lethal dose causes mild symptoms. Ten lethal doses kill. |
| Immunity Lv5 (20x) | Most single poisonings do nothing noticeable |
| Immunity Lv9 (100x) | 10-20 g of cyanide is survivable. One hundred death cap mushrooms are survivable. |
| Pure Body Lv9 (1,000x) | Survives up to a thousand lethal doses of anything |

Alcohol scales the same way. A character at M = 10 needs ten times as many drinks to feel the same effect.

### Sleep formulas

Sleep Resistance and Sleep Immunity cover forced sleep and drowsiness from substances, magic and fatigue effects. Natural sleep need stays the same until the Fused tier.

- **Sedatives: effective dose = actual dose / M**
- **Sleep magic: effective potency = spell potency / M.** The target falls asleep only if effective potency is 1 or higher.
- **Forced sleep duration = normal duration / M**
- Medical anesthesia needs M times the normal dose unless the holder voluntarily lowers the skill.

**Live note:** rewrite Sleep Resistance already cuts **natural sleep need** by −10%/level. This idea parks forced-sleep math here and moves natural need into Pure Body. Merge carefully.

### Pure Body (Fused)

- M of 111x to 1,000x against toxins, sedatives and forced sleep.
- Natural sleep need drops by level:

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

Disease and pathogens are outside this family.

---

## 5. Training

### Training sources

- **Heat:** saunas, kitchens, forges, fire-walking, volcanic regions, fire magic
- **Cold:** ice baths, winter exposure, high altitude, frost magic, cryogenic monsters
- **Blunt:** sparring, fall training, iron-body conditioning, combat, siege weapons
- **Sharp:** blade conditioning, combat, arrow fire, gunfire at high tiers
- **Toxin:** controlled dosing (mithridatism), venomous monsters, alchemical poisons
- **Sleep:** sedatives, sleep magic, forced wakefulness under fatigue effects

### Access gating

At high levels, ordinary life stops supplying stimuli that come anywhere near the threshold. Growth requires seeking out forges, lava fields, cryogenic zones, terminal-velocity falls, siege weapons or monster venom. This creates natural plot hooks for progression.

---

## Shared rules (performance skills)

- These use the same tiers and multipliers as the resistance skills: Lv1-9 at 1.11x-10x, the evolved tier at 11.1x-100x and Fused at 111x-1,000x.
- M multiplies one performance quantity per skill. When that quantity is energy, speed rises by √M.
- A multiplier can only scale what a human body already does. Things a human body cannot do at any speed, like regrowing a limb, sealing a severed artery or sticking to a ceiling, unlock at a set tier instead.

### Breath Holding → Suffocation Immunity

**What M multiplies:** oxygen efficiency. The body burns oxygen at 1/M the normal rate. The brain tolerates low oxygen M times longer.

**Baseline:** a 60 s hold at rest, 20 s under hard exertion, and about 10 s to blackout from a blood choke.

| Tier | Lv5 | Lv9 |
|---|---|---|
| Breath Holding | 2 min | 10 min |
| Suffocation Immunity | 20 min | 1 h 40 min |
| Fused | 3 h 20 min | 16 h 40 min |

- Breath Holding Lv9 matches elite freedivers, who hold about 10 min.
- Exertion and chokes scale the same way. At Lv9, a character can fight for over 3 min on one breath and stays conscious for 100 s in a blood choke.
- At Lv7, the summit of Everest feels like sea level.
- Shock from blood loss is oxygen starvation, so this skill also slows its effects.
- **Pairing:** Suffocation Immunity + Pressure Immunity (a new skill) → Abyssal Body, covering the deep sea and vacuum.

**Live:** prefer **Breath Control** (`SkillsDesign.md`) for chapter math until this is merged.

### Aim → True Aim

**What M multiplies:** precision. Aiming error drops to 1/M, so the distance at which a target can be hit reliably grows by M.

**Baseline reliable torso hit:** handgun at 10 m, rifle fired standing at 100 m, thrown object at 10 m.

| Tier | Lv5 (handgun / rifle) | Lv9 (handgun / rifle) |
|---|---|---|
| Aim | 20 m / 200 m | 100 m / 1 km |
| True Aim | 200 m / 2 km | 1 km / 10 km |
| Fused | Max projectile range | Max projectile range |

- Thrown objects follow the handgun column.
- **Aim** removes only shooter error. The weapon's own spread still applies. That spread keeps a typical handgun to torso hits within about 400 m and a good rifle within about 1.5 km.
- **True Aim** adds intuitive ballistics. Error from wind, bullet drop and leading a moving target also drops to 1/M.
- **Fused** extends to the projectile itself. The weapon's own spread shrinks too, so range is limited only by how far the projectile flies.

### Throwing → Cannon Arm

**What M multiplies:** energy delivered to the thrown object, so speed rises by √M. The skill also protects the arm from its own forces.

**Baseline:** an average adult throws a baseball at about 90 km/h. Pro pitchers reach about 160 km/h.

| Tier | Lv5 | Lv9 |
|---|---|---|
| Throwing | 127 km/h | 285 km/h |
| Cannon Arm | 400 km/h | 900 km/h |
| Fused | 1,270 km/h | 2,850 km/h |

- Throwing Lv7 matches pro pitchers.
- A baseball thrown at Cannon Arm Lv9 carries about 4,500 J. That is more than a 7.62 NATO rifle round. At Fused Lv9 it carries about 45,000 J, more than double a .50 BMG round.
- Without air, range would grow by M. Above about 100 m/s, drag dominates, so real range grows far slower.
- At the top tiers, soft objects break apart from the throw. Dense objects like iron or stone survive.
- **Pairing:** True Aim + Cannon Arm → Deadeye.

### Climbing → Sheer Climb

**What M multiplies:** grip and climbing stamina. The hold size needed drops to 1/M. Time on the wall grows by M.

**Baseline:** an average adult needs ladder-like holds about 2-3 cm deep and can hang for about 30 s.

| Tier | Lv5 | Lv9 |
|---|---|---|
| Climbing | 1-1.5 cm edges, 1 min hang | 2-3 mm edges, 5 min hang |
| Sheer Climb | Rough brick, bark, stone | Smooth concrete, plaster, ice |
| Fused | Overhangs | Ceilings, indefinitely |

- Climbing Lv9 matches the world's best rock climbers.
- At the Sheer Climb tier, grip works off surface texture instead of holds.
- Friction alone cannot hold a body to glass or a ceiling, so Fused unlocks adhesion. At Lv1 the climber holds onto vertical glass and polished metal.
- **Pairing:** Sheer Climb + Balance (a new skill) → Wall Walker.

### Wound Recovery → Rapid Healing

**What M multiplies:** healing speed.

**Baseline:** a shallow cut heals in 10 days, a deep laceration in 4 weeks and a broken bone in 8 weeks.

| Tier | Lv5 (cut / laceration / bone) | Lv9 (cut / laceration / bone) |
|---|---|---|
| Wound Recovery | 5 d / 2 wk / 4 wk | 1 d / 3 d / 6 d |
| Rapid Healing | 12 h / 34 h / 3 d | 2.4 h / 7 h / 13 h |
| Fused | 72 min / 3.4 h / 7 h | 14 min / 40 min / 80 min |

- Scars form normally through Wound Recovery Lv9. Rapid Healing heals without scarring.
- Fused unlocks regrowth of what a human body cannot replace: limbs, organs, nerves and teeth. A limb regrows in about 100 days at Lv1 and about 11 days at Lv9.
- Healing costs the same total calories and protein at any speed. Faster healing packs that cost into hours, which causes ravenous hunger. A starved body stops healing until fed.

### Blood Recovery → Iron Blood

**What M multiplies:** clotting speed and blood production.

**Baseline:** a small cut stops bleeding in 2-10 min. Replacing 500 mL of lost blood takes about 6 weeks. Losing about 40% of total blood, around 2 L, is lethal without treatment.

| Tier | Lv5 (500 mL replaced) | Lv9 (500 mL replaced) | Lv9 small-cut clotting |
|---|---|---|---|
| Blood Recovery | 3 wk | 4 d | 12-60 s |
| Iron Blood | 2 d | 10 h | 1-6 s |
| Fused | 5 h | 1 h | Near instant |

- Natural clotting cannot close a severed major artery. Arterial self-sealing unlocks at Iron Blood Lv1.
- Making blood needs raw material. Every 500 mL takes about 250 mg of iron, so heavy use demands meat, organ meat or other iron sources.
- Tolerance to blood loss comes from Breath Holding's oxygen efficiency, not from this skill.
- **Pairing:** Rapid Healing + Iron Blood → Regeneration.

---

## Cross-links

- Live Sleep / Heat / Poison / Breath Control: `SkillsDesign.md`
- Thin skill law: `Skills.md`
- Body M for breath/blood: `Attributes.md`
- Roland breath / recovery goals: `../People/Roland/Goals.md`
- Redesign park: `SkillsRedesign.md`
- Direction loot: `../Ideas.md`
