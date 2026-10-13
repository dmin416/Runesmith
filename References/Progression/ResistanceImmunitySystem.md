# Resistance and Immunity Skill System

> **Ideas / design loot.** Not automatic law. Live hubs win: `SkillsDesign.md`, `Skills.md`, `SkillRanks.md`, `RolandResistanceTracks.md`, `ResistanceGrindRarity.md`. Goals: `../People/Roland/Goals.md`.
>
> Promote a row into `SkillsDesign.md` only when it **abides live rules** and a chapter needs it.
>
> Harm map and multi-mechanism math live in this file. Leveling meters for Sustenance (breath time / blood volume): `MultiMechanismResistance.md`.

---

## Conflicts and soft-ok (read first)

### Live wins (do not replace until accepted)

| Topic | Live lock | This idea |
|---|---|---|
| **Sleep Resistance** | −10% sleep **need** from L1 → Immunity to **1%** floor (`SkillsDesign.md`) | Natural sleep need drops only at **Sustenance Immunity** (conflicts) |
| **Heat / Cold / Poison / Pain / Alcohol** | −10% effect (or soft Alcohol) → Immunity floor where locked | Same M math for Resistance; Fused names and thresholds are new |
| **Breath Control** | `hold = T0 × M_body × level`; 1 min = 1 use | Suffocation Resistance: hold = **1 min × M**; separate leveling meters |
| **Starvation / thirst / hunger** | No separate Thirst / Hunger skills; Sleep is live | Thirst + Hunger + Sleep + Suffocation → **Sustenance Immunity** |
| **Fused names (old)** | n/a | **Pure Blood / Iron Will / Undying Body** retired; use **Bodily Immunity** / **Sustenance Immunity** |
| **Acid / Electricity** | Roland grind lock (`RolandResistanceTracks.md`) | Not in the four families; keep separate until written in |
| **Recovery** | Live evolve track | Not part of these families |

### Soft-ok

- Resistance L1–L9 = 10%–90% with **M = 1 / (1 − resistance)** matches live **−10% effect per level**.
- Immunity toward ~1% effect floor matches live Immunity wording as display.
- Blunt + Sharp → Melee; stopped sharp → blunt; access gating; split / parallel / gated rules.

### Still idea-only

- Fused tier and family fuse-when-all-Imm-L9 rule
- Thermal tolerance thresholds as hard zero-damage law
- Purge, pain switch, Sustenance natural-sleep table, Dormancy
- Thirst / Hunger / Suffocation as named skills (live Breath Control / Sleep stay until promote)

---

# 1. Core Framework

## Skill Tiers

| Tier | Levels | Resistance | Multiplier (M) |
|---|---|---|---|
| Resistance | 1-9 | 10% to 90% | 1.11x to 10x |
| Immunity | 1-9 | 91% to 99% | 11.1x to 100x |
| Fused | 1-9 | 99.1% to 99.9% | 111x to 1,000x |

- A Resistance skill at Lv9 evolves into the matching Immunity at Lv1.
- When every Immunity in a family reaches Lv9, they fuse into one Fused skill at Lv1. The Fused skill covers every damage type in the family.

## Multiplier by Level

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

## Skill Families

**Thermal**
- Heat Resistance → Heat Immunity
- Cold Resistance → Cold Immunity
- Both at Immunity Lv9 → **Temperature Immunity**

**Kinetic**
- Blunt Resistance → Blunt Immunity
- Sharp Resistance → Sharp Immunity
- Both at Immunity Lv9 → **Melee Immunity**

**Bodily**
- Pain Resistance → Pain Immunity
- Poison Resistance → Poison Immunity
- Alcohol Resistance → Alcohol Immunity
- All three at Immunity Lv9 → **Bodily Immunity**

**Sustenance**
- Sleep Resistance → Sleep Immunity
- Thirst Resistance → Thirst Immunity
- Hunger Resistance → Hunger Immunity
- Suffocation Resistance → Suffocation Immunity
- All four at Immunity Lv9 → **Sustenance Immunity**

## Threshold Rule

All thresholds in this document are for a baseline human body. Physical quality is applied separately.

Below the threshold the character takes no damage no matter how long the exposure lasts. Above it, convert the exposure to its effective value using M and read the result as if it happened to a normal human.

## Status Outcomes Have No Skill

Pain Resistance is the only skill that targets a status. Blindness, deafness and stun come from damage. Only the skill against that underlying damage helps.

| Outcome | Cause | Skill that helps |
|---|---|---|
| Blind | Bright flash (dazzle) | None. Normal eye function |
| Blind | Retinal or corneal burn | Heat (eyes one level lower) |
| Blind | Chemical in eyes | Poison (eyes one level lower) |
| Blind | Pepper spray, tear gas | Pain (eye clamping is a pain reflex) |
| Deaf | Eardrum rupture, loud noise | Blunt (ears one level lower) |
| Stun | Concussion | Blunt |
| Stun | Blood choke | Suffocation |
| Stun | Electric muscle lockup (Taser) | None. Pain covers the pain only |
| Knocked out | Heart or breathing stopped by current | Suffocation keeps the brain alive |

---

# 2. Thermal Family (Tolerance Model)

These skills do not insulate. Heat and cold flow into the body at the normal rate. The tissue reaches the real temperature of the source. The skill lets the cells survive that temperature.

Consequences:
- Clothing and gear burn or freeze normally. Hair and nails count as body and are protected.
- Metal armor heats up at the normal rate.
- A hot skill-holder's skin can burn whoever touches it.
- Body water stays functional inside the threshold. It does not boil or form ice crystals.
- Insulation is not part of this system. An insulating effect can exist as a separate skill or item. Earth materials and contact effusivity: `../World/Materials/InsulationMaterials.md`.

## Heat Formulas

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

## Heat Thresholds

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

## Cold Formulas

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

## Cold Thresholds

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

## Worked Example: Hand in an 800°C Campfire

- Heat Resistance Lv9 (M = 10): effective 113°C. Burns instantly.
- Heat Immunity Lv5 (M = 20): effective 75°C. Burns in about a second.
- Heat Immunity Lv8 (M = 50): effective 52°C. Burns in a few minutes.
- Heat Immunity Lv9 (M = 100): effective 45°C. Hours before any damage.
- Temperature Immunity Lv1 (M = 111): under threshold. No damage, indefinitely.

---

# 3. Kinetic Family

## Momentum Rule

These skills do not cancel momentum. A hammer still moves the target, a truck still launches them and a fall still ends in a sudden stop. Knockback is the same as for a normal person of the same mass. Holding ground depends on footing, mass and Strength.

## Whole-Body Rule

Blunt injury comes from compression, shear and acceleration. The brain hits the skull, organs tear from their attachments and blood vessels rupture. Blunt tolerance applies to every tissue, including the brain and internal organs. Skin-only toughness does not prevent concussion.

## Weak Points

Eyes, ear canals and the lining of the mouth and throat use the multiplier one level lower than the skill.

## Blunt Formulas

- **Concussion: 80 g × M**
- **Rib fracture: 2,000 N × M**
- **Skull fracture: 5,000 N × M**
- **Chest crush becomes dangerous: about 300 kg × M**
- **Uninjured impact speed: 7 × √M m/s**
- **Blast lung injury: 100 kPa × M**
- **Eardrum rupture: 35 kPa × M one level lower** (weak point)

## Uninjured Impact Speed

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

## Force Thresholds at Each Tier's Lv9

| | Resistance Lv9 | Immunity Lv9 | Melee Immunity Lv9 |
|---|---|---|---|
| Concussion | 800 g | 8,000 g | 80,000 g |
| Rib fracture | 20 kN | 200 kN | 2 MN |
| Skull fracture | 50 kN | 500 kN | 5 MN |
| Chest crush | 3 t | 30 t | 300 t |

Blast landmarks:

| Blast | Overpressure |
|---|---|
| Windows shatter | ~7 kPa |
| Eardrums rupture (baseline) | ~35 kPa |
| Buildings collapse | ~35-70 kPa |
| Lung injury (baseline) | ~100 kPa |

## Sharp Formulas

Skin is the main barrier against cutting and piercing. Once skin is breached, fat and muscle part easily. Humans are far weaker against sharp force than blunt force.

- **Puncture or cut force: 20 N × M**
- **Bullet stop velocity: 60 × √M m/s**
- Armor-piercing rounds treat the target as one level lower.
- A superhuman attacker's force scales with their Strength multiplier.

## Sharp Thresholds

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
| Grenade fragments | About 1,200-1,500 m/s |

Key points:
- Sharp Immunity Lv5: casual knife attacks fail. Committed stabs still penetrate.
- Sharp Immunity Lv8: 9mm stops at the skin.
- Sharp Immunity Lv9: blades driven by normal human strength fail. All handguns stop.
- Melee Immunity Lv3: 7.62x39 stops.
- Melee Immunity Lv6: 5.56 and .50 BMG stop.
- Melee Immunity Lv9: all small arms and grenade fragments stop.

## Stopped Weapons Become Blunt

A blade, bullet or fragment that fails to pierce delivers its force as blunt trauma on a small area. That hit is checked against the Blunt skill.
- A stopped handgun round hits like a heavy punch.
- A stopped rifle round hits like a sledgehammer.
- A greatsword that cannot cut becomes an iron club.

A Sharp-only character is cut-proof yet breakable. A Blunt-only character shrugs off hammers while a knife still slides in. Melee Immunity removes both gaps.

## What It Looks Like

Sledgehammer to the chest at high Blunt tiers: a dull thud like hitting a sandbag. The flesh dimples and springs back with no bruise. The body staggers back as far as a normal person's would. The shirt can still tear. The hammer may rebound hard enough to jar the swinger's wrists.

Hit by a truck: launched, tumbles 20 m and gets up. Clothes are shredded and carried gear breaks.

Pinned under rubble: no injury, yet still trapped. Breathing only works if Strength can lift the ribs against the weight.

---

# 4. Bodily Family

## Pain Resistance → Pain Immunity

- **Effective pain = raw pain / M**
- Raw pain uses a 0-10 scale that continues past 10 for extreme injuries.

Raw pain by injury:

| Injury | Raw Pain |
|---|---|
| Paper cut | 1-2 |
| Stubbed toe | 3-4 |
| Deep cut | 5-6 |
| Broken bone | 7-8 |
| Pepper spray in the eyes | ~8 |
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
- Pain Immunity Lv1 unlocks a pain switch: the holder can turn pain fully on or off at will.

## Poison Resistance → Poison Immunity

- **Effective dose = actual dose / M**
- Doses are per kilogram of body mass, as in standard toxicology.
- A dose of N lethal doses acts like N / M lethal doses.
- Methanol and other toxic alcohols count as poison. Drinking alcohol is covered by Alcohol Resistance.
- Sedatives are checked against both Poison (body harm) and Sleep (drowsiness).
- Infections count as poison (pathogens damage the body through toxins).

Poison landmarks:

| Tier | Effect |
|---|---|
| Poison Resistance Lv5 (2x) | A lethal snakebite becomes serious illness |
| Poison Resistance Lv9 (10x) | One lethal dose causes mild symptoms. Ten lethal doses kill. |
| Poison Immunity Lv5 (20x) | Most single poisonings do nothing noticeable |
| Poison Immunity Lv9 (100x) | 10-20 g of cyanide is survivable. One hundred death cap mushrooms are survivable. |
| Bodily Immunity Lv9 (1,000x) | Survives up to a thousand lethal doses of anything |

## Alcohol Resistance → Alcohol Immunity

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
| Bodily Immunity | 800 | 4,000 |

- From Alcohol Immunity onward, a character cannot physically drink enough to get drunk.
- Hangover severity = baseline / M.
- Alcohol poisoning uses the same effective BAC.

## Bodily Immunity (Fused)

**Fusion:** Pain Immunity Lv9 + Poison Immunity Lv9 + Alcohol Immunity Lv9

- M of 111x to 1,000x against pain, poisons and intoxicants.
- Pain-based torture and interrogation fail completely.
- Unlocks Purge: the holder can expel any substance from the body at will through sweat, breath or vomiting.

---

# 5. Sustenance Family

## Sleep Resistance → Sleep Immunity

Covers forced sleep and drowsiness from substances, magic and fatigue effects. Natural sleep need stays the same until the Fused tier.

*(Live conflict: chapters already cut natural sleep need on Sleep Resistance. Do not wait for Sustenance Immunity in printed prose.)*

- **Sedatives: effective dose = actual dose / M**
- **Sleep magic: effective potency = spell potency / M.** The target falls asleep only if effective potency is 1 or higher.
- **Forced sleep duration = normal duration / M**
- Medical anesthesia needs M times the normal dose unless the holder voluntarily lowers the skill.

## Thirst Resistance → Thirst Immunity

- **Survival without water = 3 days × M**
- **Daily water needed = 2.5 L / M**

| Lv | Thirst Resistance | Thirst Immunity | Sustenance Immunity |
|---|---|---|---|
| 1 | 3.3 days | 33 days | 11 months |
| 2 | 3.8 days | 38 days | 1 year |
| 3 | 4.3 days | 43 days | 1.2 years |
| 4 | 5 days | 50 days | 1.4 years |
| 5 | 6 days | 60 days | 1.6 years |
| 6 | 7.5 days | 75 days | 2.1 years |
| 7 | 10 days | 100 days | 2.7 years |
| 8 | 15 days | 150 days | 4.1 years |
| 9 | 30 days | 300 days | 8.2 years |

## Hunger Resistance → Hunger Immunity

- **Survival without food (with water) = 45 days × M**
- **Daily food needed = 2,000 kcal / M**

| Lv | Hunger Resistance | Hunger Immunity | Sustenance Immunity |
|---|---|---|---|
| 1 | 50 days | 1.4 years | 13.7 years |
| 2 | 56 days | 1.5 years | 15.4 years |
| 3 | 64 days | 1.8 years | 17.6 years |
| 4 | 75 days | 2.1 years | 20.6 years |
| 5 | 90 days | 2.5 years | 24.7 years |
| 6 | 113 days | 3.1 years | 30.8 years |
| 7 | 150 days | 4.1 years | 41 years |
| 8 | 225 days | 6.2 years | 61.6 years |
| 9 | 450 days | 12.3 years | 123 years |

## Suffocation Resistance → Suffocation Immunity

Covers anything that starves tissue of oxygen: drowning, choking, smoke, vacuum, thin air, blood loss, a stopped heart and blood chokes.

- **Breath-hold (conscious without oxygen) = 1 min × M**
- **Brain damage onset without oxygen = 4 min × M**
- **Blood choke unconsciousness = 10 s × M**
- **Survivable blood loss = 1 - (0.6 / M)**
- **Unimpaired altitude: functions normally when oxygen is at least 70% of sea level / M**

| Lv | Suffocation Resistance | Suffocation Immunity | Sustenance Immunity |
|---|---|---|---|
| 1 | 1.1 min / 4.4 min | 11 min / 44 min | 1.9 h / 7.4 h |
| 2 | 1.3 min / 5 min | 13 min / 50 min | 2.1 h / 8.3 h |
| 3 | 1.4 min / 5.7 min | 14 min / 57 min | 2.4 h / 9.5 h |
| 4 | 1.7 min / 6.7 min | 17 min / 67 min | 2.8 h / 11 h |
| 5 | 2 min / 8 min | 20 min / 80 min | 3.3 h / 13 h |
| 6 | 2.5 min / 10 min | 25 min / 100 min | 4.2 h / 17 h |
| 7 | 3.3 min / 13 min | 33 min / 133 min | 5.6 h / 22 h |
| 8 | 5 min / 20 min | 50 min / 200 min | 8.3 h / 33 h |
| 9 | 10 min / 40 min | 100 min / 400 min | 17 h / 67 h |

(Breath-hold / brain damage onset)

| Tier | Survivable blood loss |
|---|---|
| Baseline | 40% |
| Resistance Lv1 | 46% |
| Resistance Lv5 | 70% |
| Resistance Lv9 | 94% |
| Immunity Lv9 | 99.4% |
| Sustenance Immunity Lv9 | 99.94% |

Oxygen landmarks:

| Situation | Oxygen |
|---|---|
| Sea level | 100% |
| Denver | ~83% |
| La Paz, Bolivia | ~64% |
| Everest summit | ~33% (Resistance Lv6 for no impairment) |
| House fire after flashover | Near 0% |
| Underwater, vacuum | 0% |

## Sustenance Immunity (Fused)

**Fusion:** Sleep Immunity Lv9 + Thirst Immunity Lv9 + Hunger Immunity Lv9 + Suffocation Immunity Lv9

- M of 111x to 1,000x against forced sleep, sedation, thirst, hunger and oxygen loss.
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

- Unlocks Dormancy: voluntary suspended animation. Thirst, Hunger and Suffocation timers ×10 while dormant. Waking takes one minute.

---

# 6. Damage Map

## Physical

| Damage | Skill |
|---|---|
| Punches, kicks, clubs, hammers | Blunt |
| Falls, vehicle crashes | Blunt |
| Crushing (rubble, machinery) | Blunt (+ Suffocation if breathing is blocked) |
| Explosion blast wave | Blunt |
| Deep-sea pressure | Blunt |
| Concussion | Blunt |
| Whiplash, twisting, joint dislocation | Blunt |
| Loud noise | Blunt (ears one level lower) |
| Bullets | Sharp (+ Blunt for the shock cavity if it penetrates) |
| Arrows, spears, stabbing, needles | Sharp |
| Blades, claws, broken glass, saws | Sharp |
| Shrapnel | Sharp |
| Mauling, tearing | Sharp + Blunt |
| Animal bites | Sharp + Blunt + Poison (infection) |
| Road rash, scraping | Sharp + Heat (friction) |
| Extreme G-forces | Blunt + Suffocation (brain starved of blood) |

## Thermal

| Damage | Skill |
|---|---|
| Fire, flame, hot liquids, steam | Heat |
| Hot surfaces, lava, molten metal | Heat |
| Friction burns, heat stroke | Heat |
| Infrared, microwaves, lasers, nuclear flash | Heat |
| Frostbite, hypothermia | Cold |
| Liquid nitrogen, cryogenics, freezing metal | Cold |

## Chemical and Biological

| Damage | Skill |
|---|---|
| Acids, alkalis | Poison (+ Heat for concentrated acid) |
| Venom, toxins, heavy metals | Poison |
| Drug overdose | Poison |
| Nerve agents, blister agents | Poison |
| Carbon monoxide alone | Suffocation (Hb binding) |
| Cyanide alone | Poison (cellular respiration) |
| House-fire smoke (inhaled plume) | ½ Suffocation, ⅖ Poison, ⅒ Heat |
| Allergic reaction | Poison + Suffocation (airway swelling) |
| Pepper spray, tear gas | Pain (minor Poison) |
| Drinking alcohol | Alcohol |
| Sedatives | Poison + Sleep |
| Bacterial, viral, fungal, parasitic infection | Poison |
| Cancer | Sharp + Poison (damaged DNA) |

## Radiation

| Damage | Skill |
|---|---|
| Gamma, X-rays, beta, solar and cosmic protons | ⅓ Sharp, ⅔ Poison |
| Neutrons | Blunt |
| Alpha, heavy cosmic ions | Sharp |
| Swallowed or inhaled radioactive material | Sharp + Poison |
| UV | Poison |

## Electrical

| Damage | Skill |
|---|---|
| Electrocution, lightning | Heat (burns) + Sharp (current punches holes in cell membranes) + Suffocation (heart or breathing stops) |
| Taser | Pain (muscle lockup has no skill) |

## Deprivation

| Damage | Skill |
|---|---|
| Drowning, choking, suffocation | Suffocation |
| Strangulation | Suffocation + Blunt |
| High altitude, inert gas | Suffocation |
| Blood loss | Suffocation |
| Dehydration | Thirst |
| Starvation | Hunger |
| Sleep deprivation, forced sleep | Sleep |

## Environmental Extremes

| Damage | Skill |
|---|---|
| Vacuum exposure | Blunt (tissue swelling) + Suffocation |
| Decompression sickness (the bends) | Sharp (gas bubbles tear tissue) + Suffocation (bubbles block blood flow) |
| Volcanic eruption | Heat + Poison (gases) + Blunt (debris) |
| Desert exposure | Heat + Thirst + Poison (UV) |
| Arctic exposure | Cold + Hunger |

## Not Physical Damage

Fear, trauma and madness damage the mind, not the body. They need a separate mental skill.

---

# 7. Multi-Mechanism Damage

## Five Ways Damage Combines

| Type | What happens | Example |
|---|---|---|
| **Split** | One damage pool divided across mechanisms | Radiation, electrocution |
| **Parallel** | One event, several separate hazards | Explosion, house fire |
| **Gated** | Second mechanism only works if the first succeeds | Snakebite, poisoned blade |
| **Converted** | Blocked damage turns into another type | Stopped bullet becomes Blunt |
| **Amplified** | One injury weakens defense against another | Burned skin is easier to cut |

## Split Damage

**Effective amount = actual amount × Σ (fᵢ / Mᵢ)**

**Combined multiplier: M_eff = 1 / Σ (fᵢ / Mᵢ)**

- fᵢ = fraction of damage from each mechanism (fractions add to 1)
- Mᵢ = multiplier of the skill covering that mechanism
- A mechanism the character has no levels in uses M = 1
- A component under its own skill's threshold contributes 0

**Weakest link rule:** M_eff can never exceed 1 / f_unleveled.

| Unleveled fraction | Maximum M_eff |
|---|---|
| 50% | 2x |
| 30% | 3.33x |
| 10% | 10x |
| 1% | 100x |

Leveling one skill to Fused tier does almost nothing if its partner stays at zero.

| Damage | Split |
|---|---|
| Gamma, X-ray, beta, protons | ⅓ Sharp, ⅔ Poison |
| Criticality accident (neutron + gamma) | ½ Blunt, ⅙ Sharp, ⅓ Poison |
| Electrocution, lightning | ½ Heat, ⅕ Sharp, 30% Suffocation |
| Carbon monoxide alone | Suffocation |
| Cyanide alone | Poison |
| House-fire smoke (inhaled plume) | ½ Suffocation, ⅖ Poison, ⅒ Heat |
| Concentrated acid | 70% Poison, 30% Heat (local heating can approach boiling) |

## Parallel Damage

Each hazard is checked separately against its own skill. Injuries stack. The worst one usually decides survival.

**Bleeding rule:** every Sharp wound that bleeds adds a Suffocation check for blood loss.

## Gated Damage

The gate (usually Sharp) must fail before the payload enters the body.

- **Gate fails:** full payload, checked against its own skill
- **Gate holds:** stopped weapon becomes Blunt; payload only touches skin

**Skin contact dose = payload × A**

| Payload | Absorption through intact skin (A) |
|---|---|
| Snake venom, most animal venoms | ~0 (proteins cannot cross skin) |
| Most plant toxins, ingested poisons | ~0.01-0.1 |
| Nerve agents (VX), hydrofluoric acid, skin-penetrating solvents | ~1 (gate does nothing) |

Weak points (eyes, mouth, ear canal) absorb fully. Spitting cobra venom in the eyes bypasses the gate.

## Converted Damage

- Stopped blade, bullet or fragment: Blunt hit on a small area
- Hollow-point or tumbling bullet that penetrates: Sharp wound + Blunt check for the internal shock cavity
- Gear over its own heat limit: molten or burning gear becomes a new Heat source stuck to the skin

## Amplified Damage

| Condition | Effect |
|---|---|
| Burned skin (Heat threshold exceeded) | Sharp one level lower at that area |
| Frozen tissue (Cold threshold exceeded) | Sharp and Blunt one level lower at that area (brittle) |
| Burned or frozen weak point (eyes, mouth) | Two levels lower |
| Body over heat threshold during Poison or radiation exposure | Effective dose ×2 |
| Alcohol + sedative together | Combined effect ×1.5 |
| Body over heat threshold while suffocating | Suffocation timers ÷2 |
| Body below cold core limit while suffocating | Suffocation timers ×2 |

## Mechanisms With No Skill

| Mechanism | Found in |
|---|---|
| Dazzle from bright light | Flashbangs, nuclear flash, lasers below burn level |
| Muscle lockup from current | Taser, electric fences |

---

# 8. Worked Examples

## Gamma Radiation (split)

Baseline LD50 = 4.5 Sv.

| Build | M_eff | LD50 |
|---|---|---|
| Poison Immunity Lv9 alone | 2.9x | 13 Sv |
| Poison Immunity Lv9 + Sharp Resistance Lv5 | 5.8x | 26 Sv |
| Poison Immunity Lv9 + Melee Immunity Lv9 | 143x | 643 Sv |
| Bodily Immunity Lv9 + Melee Immunity Lv9 | 1,000x | 4,500 Sv |

## Criticality Accident (split)

Baseline: ~17 Sv is fatal.

| Build | M_eff | Effective dose | Outcome |
|---|---|---|---|
| None | 1x | 17 Sv | Fatal |
| Blunt Immunity Lv9 + Poison Immunity Lv9, no Sharp | 5.7x | 3 Sv | Moderate radiation sickness, survives |
| Melee Immunity Lv9 + Bodily Immunity Lv9 | 1,000x | 0.017 Sv | Nothing |

## Electrocution / Lightning (split)

Lightning usually stops the heart and breathing. The heart often restarts on its own; breathing does not. Most deaths come from the brain starving of oxygen afterward.

| Build | M_eff |
|---|---|
| Heat Immunity Lv9 + Sharp Immunity Lv9, no Suffocation | 3.26x |
| Heat, Sharp and Suffocation all at Resistance Lv9 | 10x |
| Heat, Sharp and Suffocation all at Immunity Lv9 | 100x |
| Temperature Immunity Lv9 + Melee Immunity Lv9 + Suffocation Immunity Lv9 | 270x |
| Temperature Immunity Lv9 + Melee Immunity Lv9 + Sustenance Immunity Lv9 | 1,000x |

With Suffocation Immunity Lv5, a struck character stays conscious for 20 minutes with stopped breathing, long enough for it to restart. Muscle lockup during the strike happens at every level.

## House Fire (parallel + smoke split)

A structure fire is several hazards at once. Only the inhaled smoke plume is a split (fractions add to 1).

**Smoke ratios:** CO and oxygen failure in the plume dominate → **½ Suffocation**. HCN, acid gases, aldehydes → **⅖ Poison**. Hot gases and soot cook the airway → **⅒ Heat**.

| Hazard | Kind | Skill / split | Projection |
|---|---|---|---|
| Room heat before flashover (100-300°C) | Parallel | Heat | Heat Immunity Lv6 (212°C) to Lv7 (270°C) |
| Flashover (600°C+) | Parallel | Heat | Heat Immunity Lv9 (737°C) |
| Inhaled smoke plume | Split | ½ Suffocation, ⅖ Poison, ⅒ Heat | Full Imm on all three → 100x; fused caps → 1,000x |
| Oxygen-starved pocket (near 0% O₂) | Parallel | Suffocation | Suffocation Immunity Lv5 gives ~20 minutes |
| Falling debris (if the building fails) | Parallel | Sharp / Blunt | Only if that beat happens |

**Smoke plume M_eff:**

| Build | M_eff vs plume |
|---|---:|
| None | 1x |
| Poison Imm Lv9 only | ~1.7x |
| Suffocation Imm Lv9 only | ~2.0x |
| Heat Imm Lv9 only | ~1.1x |
| Poison + Suffocation Imm Lv9, no Heat | ~9x (cap 10x) |
| Heat + Poison + Suffocation, all Imm Lv9 | **100x** |
| Temperature Imm + Bodily Imm + Sustenance Imm, all Lv9 | **1,000x** |

Heat Immunity Lv9 + Bodily Immunity + Suffocation Immunity Lv5 (or full Sustenance) walks through a burning building, searches it and walks out. Missing any of the three smoke skills leaves a leftover slice that still bites.

## Drowning in Ice Water (parallel, amplified)

| Build | Projection |
|---|---|
| None | Conscious ~1 min |
| Cold Resistance Lv9 + Suffocation Resistance Lv9 | No cold damage; 10 min breath-hold, 40 min to brain damage |
| Suffocation Immunity Lv9, no Cold skill | Hypothermia sets in, cold doubles timers: 200 min breath-hold |

## Grenade (parallel)

| Hazard | Skill | Projection |
|---|---|---|
| Fragments at ~1,200-1,500 m/s | Sharp | Melee Immunity Lv8 stops most; Lv9 stops all |
| Overpressure at close range | Blunt | Blunt Immunity tiers prevent lung injury |
| Eardrums | Blunt (one level lower) | Deafness before lung injury |
| Flash | None | Temporary blindness at every level |
| Fragment wounds that bleed | Suffocation | Blood loss check |

## Snakebite (gated)

Treat a fang like a knife tip (10-50 N).

| Sharp skill | Result |
|---|---|
| None | Full venom dose, checked against Poison |
| Sharp Resistance Lv5 (40 N) | Most bites fail; venom on skin does nothing |
| Sharp Resistance Lv9 (200 N) | All snakebites fail |
| Any level, venom spat into eyes | Full dose through the weak point |

## Poisoned Blade (gated)

| Sharp holds? | Result |
|---|---|
| No | Wound + full poison dose / Poison M + bleeding check |
| Yes, ordinary poison | Blunt bruise + poison × 0.01-0.1 on skin |
| Yes, contact nerve agent | Blunt bruise + full dose; only Poison protects |

## Acid Attack (split + threshold)

| Build | Projection |
|---|---|
| Poison Immunity Lv9, no Heat skill | M_eff 3.3x; heat burns from the reaction remain |
| Poison Immunity Lv9 + Heat Resistance Lv9 (107°C) | Heat component under threshold → M_eff 100x |
| Acid in the eyes | Poison one level lower |

## Pepper Spray (Pain)

Raw eye pain ~8. Eyes use one level lower.

| Build | Effective pain | Result |
|---|---|---|
| None | 8 | Eyes clamp shut, blinded |
| Pain Resistance Lv9 (eyes act as Lv8, 5x) | 1.6 | Eyes stay open; stinging and tears only |
| Pain Immunity Lv1+ | Pain switch off | No effect |

## Spiked Drink (amplified)

A knockout dose of sedative (potency 1.0) in a drink at 0.15% BAC.

**Breathing failure index = 1.5 × (effective BAC / 0.40% + effective sedative / lethal sedative dose)**. An index of 1 or higher stops breathing and the Suffocation timer starts.

| Build | Sleep potency | Effective BAC | Breathing index |
|---|---|---|---|
| None | 1.0 (knocked out) | 0.15% | 0.71 (dangerous) |
| Alcohol, Sleep, Poison Resistance Lv5 | 0.5 (stays awake, drowsy) | 0.075% | 0.36 |
| Bodily Immunity + Sleep Immunity Lv9 | ~0 | ~0 | ~0 |

## Frozen Limb Struck by a Hammer (amplified)

A limb pushed past the Cold threshold freezes solid. Blunt and Sharp drop one level at that limb. A hammer that bounces off a healthy arm can shatter a frozen one.

## Buried Under Rubble (parallel)

| Hazard | Skill | Projection |
|---|---|---|
| Crushing weight | Blunt | Blunt Immunity Lv1 handles ~3.3 t uninjured |
| Breathing against the load | Suffocation (Strength to lift the ribs) | Suffocation Immunity Lv9 lasts 100 min per breath |
| Days trapped | Thirst, Hunger | Thirst Resistance Lv5 survives 6 days without water |

## Desert Exposure (parallel)

| Hazard | Skill | Projection |
|---|---|---|
| Air and sand at ~50°C | Heat | Heat Resistance Lv5 (51°C) prevents damage |
| Water loss | Thirst | Thirst Resistance Lv9: 30 days without water |
| Unfiltered sun UV | Poison | Sunburn reduced by Poison M |

## Vacuum Exposure (parallel)

| Hazard | Skill | Projection |
|---|---|---|
| No oxygen | Suffocation | Suffocation Immunity Lv9: 100 min conscious. Sustenance Immunity Lv9: 17 h; ×10 in Dormancy |
| Tissue swelling | Blunt | Blunt Resistance tiers handle it |
| Sun-side heat / shade-side cold | Heat / Cold | Temperature Immunity covers both |
| Radiation | Split | Bodily Immunity + Melee Immunity |

## Nuclear Detonation (parallel)

| Hazard | Skill |
|---|---|
| Thermal flash | Heat |
| Dazzle | None |
| Blast wave, being thrown | Blunt |
| Flying glass and debris | Sharp |
| Prompt radiation | Split: ⅓ Sharp, ⅔ Poison (neutron portion Blunt) |
| Firestorm oxygen loss | Suffocation |
| Fallout | Split + Poison (inhaled particles bypass skin) |

Melee Immunity, Temperature Immunity, Bodily Immunity and Sustenance Immunity together cover every hazard. The flash still blinds temporarily.

---

# 9. Training

## Training Sources

- **Heat:** saunas, kitchens, forges, fire-walking, volcanic regions, fire magic
- **Cold:** ice baths, winter exposure, high altitude, frost magic, cryogenic monsters
- **Blunt:** sparring, fall training, iron-body conditioning, combat, siege weapons
- **Sharp:** blade conditioning, combat, arrow fire, gunfire at high tiers
- **Pain:** hard conditioning, injury, endurance drills
- **Poison:** controlled dosing (mithridatism), venomous monsters, alchemical poisons
- **Alcohol:** heavy drinking, strong spirits, alchemical liquors
- **Sleep:** sedatives, sleep magic, forced wakefulness under fatigue effects
- **Thirst:** desert crossings, water rationing, sieges
- **Hunger:** fasting, long expeditions, sieges
- **Suffocation:** freediving, breath-hold drills, high altitude, smoke-filled ruins, drowning traps, water monsters

## Access Gating

At high levels, ordinary life stops supplying stimuli that come anywhere near the threshold. Growth requires seeking out forges, lava fields, cryogenic zones, terminal-velocity falls, siege weapons, monster venom, deep water, mountain peaks, sealed tombs or long deserts. This creates natural plot hooks for progression.

---

# 10. Quick Rules

1. M = 1 / (1 - resistance). Each tier is ten times the scale of the last.
2. Below threshold: no damage, indefinitely. Above: divide the exposure by M.
3. Weak points (eyes, ears, mouth) use one level lower.
4. Split damage: M_eff = 1 / Σ (fᵢ / Mᵢ). The weakest skill dominates.
5. Parallel hazards are checked separately; the worst one decides survival.
6. Sharp is the gate for injected payloads. Venoms fail if the skin holds.
7. Stopped weapons and fragments become Blunt.
8. Burned or frozen areas drop one level.
9. Bleeding wounds trigger Suffocation checks.
10. Blindness, deafness and stun have no skill. Only the skill against the underlying damage helps. Pain is the one exception.
11. Dazzle and electric muscle lockup affect every build.
12. A family fuses when **every** Immunity in that family is at Lv9 (two, three, or four parents).

---

## Cross-links

- Live Sleep / Heat / Cold / Poison / Pain / Alcohol / Breath: `SkillsDesign.md`
- Roland grind tracks (incl. Acid / Electricity / Blunt / Sharp): `RolandResistanceTracks.md`
- How rare deliberate torture grinds are: `ResistanceGrindRarity.md`
- Sustenance leveling meters (breath time / blood volume %): `MultiMechanismResistance.md`
- Taxonomy hub (may lag names): `DamageTypeResistances.md`
- Thin skill law: `Skills.md`
- Body M for breath/blood: `Attributes.md`
- Other useful M lines: `OtherUsefulSkillsSystem.md`
- Sense / mana / sound ideas: `SensingManaSoundSystem.md`
- Direction loot: `../Ideas.md`
