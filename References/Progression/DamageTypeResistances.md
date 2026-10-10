# Every Damage Type and Its Resistance

> **Ideas / taxonomy.** Maps real-world harm to seven core resists + status effects. Live skill names and −10%/level math: `SkillsDesign.md`, `RolandResistanceTracks.md`. Broader ladder ideas: `ResistanceImmunitySystem.md`. Multi-mechanism projection (Survival family, splits): `MultiMechanismResistance.md`. Radiation split detail: `../World/Space/Radiation/`. Vision dazzle vs damage: `../World/Space/Radiation/RadiationVision.md`.

Not automatic law. Roland’s live tracks (Heat, Cold, Poison, Pain, Sleep, Acid, Electricity, Blunt, Sharp, …) do not have to match these names 1:1. Use this table to decide **which track soaks which beat**.

## Core resistances

| Resistance | Protects against |
|---|---|
| **Blunt** | Impact, crushing, pressure, shockwaves |
| **Pierce** | Penetration at a point, from spears down to particles snapping DNA |
| **Slash** | Cutting, tearing, scraping |
| **Heat** | Any damage from tissue getting too hot |
| **Cold** | Any damage from tissue getting too cold |
| **Poison** | All chemical and biological damage: toxins, corrosives, infection |
| **Deprivation** | Lack of something the body needs: oxygen, blood, water, food, sleep |

Live note: Sharp on Roland’s grind sheet = pierce + slash (`RolandResistanceTracks.md`). Sleep Resistance is a **need cut**, not HP soak; it still maps under Deprivation for taxonomy.

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
| Crushing (rubble, machinery) | Blunt |
| Explosion blast wave | Blunt |
| Deep-sea pressure | Blunt |
| Concussion | Blunt + Stun |
| Whiplash, twisting, joint dislocation | Blunt |
| Bullets | Pierce + Blunt (shockwave stretches surrounding tissue) |
| Arrows, spears, stabbing, needles | Pierce |
| Shrapnel | Pierce + Slash |
| Blades, claws, broken glass | Slash |
| Saws, chainsaws | Slash |
| Mauling, ripping, tearing | Slash + Blunt |
| Animal bites | Pierce + Blunt + Poison (infection) |
| Road rash, scraping | Slash + Heat (friction) |
| Extreme G-forces | Blunt + Deprivation (brain starved of blood) |
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
| Acids, alkalis | Poison |
| Venom, plant and animal toxins | Poison |
| Drug overdose, alcohol | Poison |
| Heavy metals (lead, mercury) | Poison |
| Nerve agents | Poison |
| Blister agents (mustard gas) | Poison |
| Carbon monoxide | Deprivation (Suffocation; Hb binding) |
| Cyanide | Poison (cellular respiration) |
| Allergic reaction | Poison + Deprivation (airway swelling) |
| Smoke inhalation / house-fire plume | **½ Deprivation, ⅖ Poison, ⅒ Heat** (`MultiMechanismResistance.md`) |
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
| Cancer | Pierce + Poison (damaged DNA) |

## Radiation

| Damage | Resistance |
|---|---|
| Gamma, X-rays, beta, solar and cosmic protons | **⅓ Pierce, ⅔ Poison** |
| Neutrons | Blunt |
| Alpha, heavy cosmic ions | Pierce |
| Swallowed or inhaled radioactive material | Pierce + Poison |
| UV | Poison |
| Bright light | Blind |

Aligns with low-LET ~⅓ direct / ~⅔ radical damage (`../World/Space/Radiation/Fundamentals.md`). Heat Resistance covers thermal radiation (IR, flash burns); it does **not** soak ionizing DNA damage (`RobustHeatHuman.md`, `RadiationVision.md`).

## Electrical

| Damage | Resistance |
|---|---|
| Electrocution, lightning | Heat (burns) + Pierce (current punches holes in membranes) + Stun (heart and nerve) |
| Taser | Stun |
| EMP | None (electronics only) |

Live note: Roland **Electricity** grind track owns the soak; split above is feel for what the track is buying.

## Deprivation

| Damage | Resistance |
|---|---|
| Drowning, choking, suffocation | Deprivation |
| Strangulation | Deprivation + Blunt |
| High altitude, thin air | Deprivation |
| Inert gas (nitrogen, helium) | Deprivation |
| Blood loss | Deprivation |
| Dehydration | Deprivation |
| Starvation | Deprivation |
| Sleep deprivation | Deprivation |

Breath Control and Sleep Resistance are live tools in this family; they are not full Deprivation Immunity. Projected fused track: **Undying Body** (`MultiMechanismResistance.md`).

## Environmental extremes

| Damage | Resistance |
|---|---|
| Vacuum exposure | Blunt (tissue swelling) + Deprivation |
| Decompression sickness (the bends) | Pierce (gas bubbles tear tissue) + Deprivation (bubbles block blood) |
| Volcanic eruption | Heat + Poison (gases) + Blunt (debris) |
| Desert exposure | Heat + Deprivation (dehydration) + Poison (UV) |
| Arctic exposure | Cold + Deprivation |

## Outside physical damage

Fear, trauma and madness damage the mind, not the body. They need a separate mental resistance such as **Will** / Stress Resistance / Resilience (live Engineer grants).
