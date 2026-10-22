# Every Damage Type and Its Resistance

> **Ideas / taxonomy.** Maps real-world harm to resist skills. Full formulas, families, multi-mechanism math: `ResistanceImmunitySystem.md`. Live skill names and −10%/level math: `SkillsDesign.md`, `RolandResistanceTracks.md`. Sustenance leveling meters: `MultiMechanismResistance.md`. Radiation: `../World/Space/Radiation/`. Vision dazzle: `../World/Space/Radiation/RadiationVision.md`.

Not automatic law. Roland’s live tracks do not have to match these names 1:1. Use this table to decide **which track soaks which beat**.

## Core resistances (idea families)

| Family | Skills | Fused |
|---|---|---|
| **Thermal** | Heat, Cold | Temperature Immunity |
| **Kinetic** | Blunt, Sharp | Melee Immunity |
| **Bodily** | Pain, Poison, Alcohol | Bodily Immunity |
| **Sustenance** | Sleep, Thirst, Hunger, Suffocation | Sustenance Immunity |

Live note: Sharp on Roland’s grind sheet = pierce + slash. Sleep Resistance is a **need cut** on the live sheet; idea Sustenance defers natural-need drop to the Fused tier (live wins in chapters).

## Status effects (no tissue damage)

| Status | Caused by |
|---|---|
| **Blind** | Bright light, irritants in the eyes |
| **Deafen** | Loud noise |
| **Stun** | Electric shock, concussion |
| **Pain** | Pepper spray, tear gas, pain weapons |

Pain as a resist track soaks **felt** pain; status Pain here is the functional lock (can't act / eyes clamp). Both can apply.

## Physical

| Damage | Resistance |
|---|---|
| Punches, kicks, clubs, hammers | Blunt |
| Falls, vehicle crashes | Blunt |
| Crushing (rubble, machinery) | Blunt (+ Suffocation if breathing blocked) |
| Explosion blast wave | Blunt |
| Deep-sea pressure | Blunt |
| Concussion | Blunt + Stun |
| Whiplash, twisting, joint dislocation | Blunt |
| Bullets | Sharp + Blunt (shock cavity if it penetrates) |
| Arrows, spears, stabbing, needles | Sharp |
| Shrapnel | Sharp |
| Blades, claws, broken glass | Sharp |
| Saws, chainsaws | Sharp |
| Mauling, ripping, tearing | Sharp + Blunt |
| Animal bites | Sharp + Blunt + Poison (infection) |
| Road rash, scraping | Sharp + Heat (friction) |
| Extreme G-forces | Blunt + Suffocation |
| Loud noise | Blunt + Deafen |

## Thermal

| Damage | Resistance |
|---|---|
| Fire, flame | Heat |
| Hot liquids, steam | Heat |
| Hot surfaces, lava, molten metal | Heat |
| Friction burns | Heat |
| Heat stroke | Heat |
| Infrared, microwaves, lasers | Heat |
| Nuclear flash | Heat |
| Frostbite | Cold |
| Hypothermia | Cold |
| Liquid nitrogen, cryogenics | Cold |
| Freezing metal contact | Cold |

## Chemical

| Damage | Resistance |
|---|---|
| Acids, alkalis | Poison (+ Heat if concentrated) |
| Venom, plant and animal toxins | Poison |
| Drug overdose | Poison |
| Drinking alcohol | Alcohol |
| Heavy metals (lead, mercury) | Poison |
| Nerve agents | Poison |
| Blister agents (mustard gas) | Poison |
| Carbon monoxide | Suffocation |
| Cyanide | Poison |
| Allergic reaction | Poison + Suffocation (airway swelling) |
| Smoke inhalation / house-fire plume | **½ Suffocation, ⅖ Poison, ⅒ Heat** |
| Pepper spray, tear gas | Pain + Blind |

Live note: Roland also has a dedicated **Acid** grind track. Treat Acid as a Poison sub-family or a parallel until fused.

## Biological

| Damage | Resistance |
|---|---|
| Bacterial infection | Poison |
| Viral infection | Poison |
| Fungal infection | Poison |
| Parasites | Poison |
| Prions | Poison |
| Sepsis | Poison |
| Cancer | Sharp + Poison (damaged DNA) |

## Radiation

| Damage | Resistance |
|---|---|
| Gamma, X-rays, beta, solar and cosmic protons | **⅓ Sharp, ⅔ Poison** |
| Neutrons | Blunt |
| Alpha, heavy cosmic ions | Sharp |
| Swallowed or inhaled radioactive material | Sharp + Poison |
| UV | Poison |
| Bright light | Blind |

Aligns with low-LET ~⅓ direct / ~⅔ radical damage (`../World/Space/Radiation/Fundamentals.md`). Heat covers thermal radiation; it does **not** soak ionizing DNA damage.

## Electrical

| Damage | Resistance |
|---|---|
| Electrocution, lightning | Heat + Sharp + Suffocation |
| Taser | Pain (muscle lockup has no skill) |
| EMP | None (electronics only) |

Live note: Roland **Electricity** grind track owns the soak; split above is feel for what the track is buying.

## Deprivation

| Damage | Resistance |
|---|---|
| Drowning, choking, suffocation | Suffocation |
| Strangulation | Suffocation + Blunt |
| High altitude, thin air | Suffocation |
| Inert gas (nitrogen, helium) | Suffocation |
| Blood loss | Suffocation |
| Dehydration | Thirst |
| Starvation | Hunger |
| Sleep deprivation / forced sleep | Sleep |

Sleep Resistance is live. Ch 19 train locks **Suffocation Resistance** (holds + blood); Breath Control is optional later hold-length skill, not the train unlock. Not full **Sustenance Immunity**.

## Environmental extremes

| Damage | Resistance |
|---|---|
| Vacuum exposure | Blunt + Suffocation |
| Decompression sickness (the bends) | Sharp + Suffocation |
| Volcanic eruption | Heat + Poison + Blunt |
| Desert exposure | Heat + Thirst + Poison (UV) |
| Arctic exposure | Cold + Hunger |

## Outside physical damage

Fear, trauma and madness damage the mind, not the body. They need a separate mental resistance such as **Will** / Stress Resistance / Resilience (live Engineer grants).
