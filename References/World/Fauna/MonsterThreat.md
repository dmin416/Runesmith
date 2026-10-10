# Monster Narrative Threat vs Human

> Species threat dial for prose. XP: `../../Progression/Levels.md` (`RaceMult`). Early ladder: `Creatures.md`. Fat cards: `Design/CreaturesDesign.md`.

**Axis:** narrative threat is how dangerous one adult specimen is to untrained average humans, counting body, venom, pack tactics and magic; an average unarmed adult human = **1.0** and the cap is **20**.

**Level note:** values are species baselines for one specimen at its reference level. Effective threat = baseline × g(L), capped at 20; the cap is a narrative ceiling, not an HP ceiling, so a L100 calamity-tier creature still reads at most as a Calamity Dragon on this dial. Equal threat does not mean equal level floor: floor bosses and named high-L elites carry hard level floors on top of the baseline (Wereboar ≥ L26; Goblin Leader L_ref **27**).

**g(level) stub:** g(L) = √(L ÷ L_ref). L_ref is **10** for every species unless the species has a level floor, in which case L_ref is that floor (Wereboar L_ref = **26**; Goblin Leader L_ref = **27**).

| L ÷ L_ref | 0.1 | 0.5 | 1 | 2 | 4 | 10 |
|---|---:|---:|---:|---:|---:|---:|
| g(L) | 0.32 | 0.71 | 1.0 | 1.41 | 2.0 | 3.16 |

**Pack policy:** every value is one specimen. Packs, swarms and colonies multiply separately at the encounter level; no baseline in this file includes pack size.

**RaceMult:** XP multipliers live in `Levels.md` and are not mirrored here, so the two laws stay independent.

**Raw input:** every threat value maps to a published number of average humans the specimen can fight at once. Below 1.0 the map is humans = threat ^ 3.85; from 1.0 up it interpolates log-linearly between the anchors in the scale table. The middle of the dial (1 to 5) carries most T1 and T2 content.

## Scale

| Threat | ≈ Humans at once | Party reading |
|---:|---:|---|
| **0.5** | 0.07 | a civilian wins most fights |
| **1** | 1 | duel |
| **2** | 4 | needs a small party |
| **3** | 10 | full party fight |
| **4** | 20 | steel-rank check |
| **5** | 40 | elite party check |
| **7** | 150 | town event |
| **10** | 1,000 | city event |
| **15** | 15,000 | kingdom event |
| **20** | 100,000 | calamity |

## Early ladder (`Creatures.md`)

Index only; canonical rows live in the family cards named in the Card column.

| Creature | Threat | ≈ Humans | Card | Basis |
|---|---:|---:|---|---|
| Dungeon Rat | **0.6** | 0.14 | Rodents | Bites and disease; weak alone |
| Fire Slime | **0.8** | 0.42 | Salamanders and slimes | Burns on contact; slow |
| Goblin | **0.9** | 0.67 | Goblinoids and kobolds | Armed and cunning; one goblin is roughly an even fight for a civilian |
| Baby Salamander | **0.9** | 0.67 | Salamanders and slimes | Hatchling fire bite |
| Needle Worm | **1.1** | 1.1 | Needle line and insects | Paralytic ambush outweighs its small body |
| Mountain Goblin | **1.25** | 1.4 | Goblinoids and kobolds | Highland stock; a clear notch above common goblins |
| Fiery Skeleton | **1.3** | 1.5 | Skeletons | Tireless with burning strikes |
| Myrmeke Worker | **1.3** | 1.5 | Needle line and insects | Giant-ant strength and mandibles; small baseline |
| Needle Moth | **1.4** | 1.7 | Needle line and insects | Adult stage; flight plus venom puts it above the worm |
| Myrmeke Soldier | **2.2** | 4.8 | Needle line and insects | Armor and acid; small baseline (mature soldier is its own row) |
| Spiked Boar | **2.7** | 7.6 | Boars | Dungeon animal, not farm stock: spiked hide, armored charge, dungeon aggression; party trash |
| Wereboar | **4.5** | 28 | Boars | Spiked Boar evolution; hairy tusked man; party elite; level floor L26 |

## Goblinoids and kobolds

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Kobold | **0.7** | 0.25 | base |
| Crimson Kobold | **0.9** | 0.67 | subtype |
| Goblin | **0.9** | 0.67 | base |
| Gray Goblin | **1.1** | 1.1 | subtype |
| Kobold Warrior | **1.1** | 1.1 | warrior |
| Goblin Leader | **1.1** | 1.1 | T2 ambush leader (Ch 9.5 nest elite); L_ref **27** (about a tough human) |
| Mountain Goblin | **1.25** | 1.4 | subtype |
| Crimson Kobold Warrior | **1.4** | 1.7 | warrior |
| Goblin Shaman | **1.6** | 2.3 | caster |
| Hobgoblin | **1.8** | 3 | base |
| Hobgoblin Berserker | **2.5** | 6.3 | berserker |
| Goblin Captain | **3** | 10 | officer |
| Gray Hobgoblin Berserker | **3** | 10 | berserker |
| Goblin King | **3.5** | 14 | ruler |
| Bocanach (Adolescent) | **4.5** | 28 | adolescent |

## Humanoids, beast-men and giants

Wereboar: canonical row in Boars.

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Mushroom People | **0.8** | 0.42 |  |
| Mushroom Men | **0.9** | 0.67 |  |
| Lesser Troglodyte | **1.3** | 1.5 | lesser |
| Abyssal Cultist | **1.4** | 1.7 | caster |
| Lizardmen | **1.6** | 2.3 |  |
| Orc | **1.8** | 3 | base |
| Inferior Dragonewt | **2.3** | 5.3 | inferior |
| Red Orc | **2.3** | 5.3 | subtype |
| Doppelganger | **2.5** | 6.3 | infiltrator |
| Ogre | **3** | 10 |  |
| Werewolf | **3.5** | 14 |  |
| Minotaur | **4** | 20 |  |
| Oni | **4** | 20 |  |
| Red Orc High-Chieftain | **4.5** | 28 | ruler |
| Stone Giant | **6.5** | 110 |  |

## Boars

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Spiked Boar | **2.7** | 7.6 | dungeon base |
| Wereboar | **4.5** | 28 | evolution; L_ref 26 |

## Rodents

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Dungeon Rat | **0.6** | 0.14 | base |
| Giant Rat | **0.7** | 0.25 | base |
| Red Rat | **0.75** | 0.33 | subtype |
| Crimson Giant Rat | **1** | 1 | subtype |

## Needle line and insects

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Dungeon Bee | **0.6** | 0.14 | single; swarms rate higher |
| Needle Worm | **1.1** | 1.1 | larva |
| Myrmeke | **1.3** | 1.5 | generic = worker |
| Myrmeke Worker | **1.3** | 1.5 | small baseline |
| Needle Moth | **1.4** | 1.7 | adult |
| Abyssal Parasite | **1.5** | 2 | infests hosts |
| Giant Praying Mantis | **2** | 4 |  |
| Giant Spider | **2** | 4 |  |
| Myrmeke Soldier | **2.2** | 4.8 | small baseline |
| Volcanic Worm | **2.5** | 6.3 |  |
| Lava-spewing monster slug | **3.5** | 14 |  |
| Greater Mantodea | **4** | 20 | greater |
| Myrmeke Soldier (mature) | **4** | 20 | horse-sized Source form; permanent separate row |
| Volcanic Kamacuras | **5** | 40 | volcanic |
| Drachinid | **5.5** | 56 | dragon-spider |
| Myrmeke Queen | **6** | 77 | nest ruler |

## Wolves: common and elemental lines

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Adolescent Ash Wolf | **1.3** | 1.5 | adolescent |
| Adolescent Gemstone Wolf | **1.8** | 3 | adolescent |
| Ash Wolf / Ashen Wolf | **1.8** | 3 | adult |
| Adolescent Volcanic Wolf | **1.9** | 3.5 | adolescent |
| Flame Wolf | **2.2** | 4.8 | adult |
| Silver Wolf | **2.3** | 5.3 | adult |
| Gemstone Wolf | **2.4** | 5.8 | adult |
| Ice Wolf | **2.4** | 5.8 | adult |
| Volcanic Wolf | **2.5** | 6.3 | adult |
| Dire Wolf | **2.6** | 6.9 | dire |
| Dire Ash Wolf | **2.8** | 8.3 | dire |
| Volcanic Dire Wolf | **3.3** | 12 | dire |
| Solar Wolf | **4** | 20 | adult |
| Sunlight Wolf | **4.2** | 23 | adult |
| Sun Wolf | **4.5** | 28 | adult |
| Alpha Volcanic Dire Wolf | **4.8** | 35 | alpha |
| Alpha Mystical Dire Sapphire Wolf | **5** | 40 | mystical alpha |
| Blazing Alpha Volcanic Dire Wolf | **5.5** | 56 | blazing alpha |

## Wolves: ruby line

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Ruby Wolf Puppy | **0.6** | 0.14 | pup |
| Adolescent Ruby Wolf | **1.6** | 2.3 | adolescent |
| Ruby Hound | **2** | 4 | adult |
| Ruby Wolf | **2** | 4 | adult |
| Adolescent Mystical Ruby Wolf | **2.2** | 4.8 | mystical adolescent |
| Mana Ruby Wolf / Mystical Ruby Wolf | **2.8** | 8.3 | mystical adult |
| Ruby Dire Wolf / Dire Ruby Wolf | **3** | 10 | dire |
| Alpha Ruby Wolf | **3.3** | 12 | alpha |
| Mystical Dire Ruby Wolf / Mystical Ruby Dire Wolf | **3.8** | 17 | mystical dire |
| Alpha Dire Ruby Wolf / Alpha Ruby Dire Wolf | **4.5** | 28 | dire alpha |
| Alpha Mystical Dire Ruby Wolf | **5** | 40 | mystical alpha |
| Blazing Alpha Mystical Dire Ruby Wolf | **5.8** | 68 | blazing alpha |
| Lesser Mystical Ruby Fenrir | **8** | 280 | lesser fenrir |
| Mystical Ruby Fenrir | **10** | 1,000 | fenrir |

## Wolves: celestial and infernal canines

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Hellhound Puppy | **1.5** | 2 | pup |
| Canine Fiend | **2.8** | 8.3 |  |
| Hellhound | **3.3** | 12 | adult |
| Orthrus | **6** | 77 | two-headed |
| Cerberus | **8.5** | 390 | three-headed |
| Fenrir | **12** | 3,000 |  |
| Wolf of Eclipse | **13** | 5,100 |  |
| Greater Fenrir | **15** | 15,000 | greater |

## Beasts and mythic animals

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Horned Swamp Toad | **1.8** | 3 |  |
| Floral Cockatrice | **3** | 10 |  |
| Azure Lion | **3.5** | 14 |  |
| Cockatrice | **3.5** | 14 | petrifying |
| Unicorn | **4** | 20 |  |
| Storm Eagle | **4.5** | 28 |  |
| Griffin | **5** | 40 |  |
| Horned Thunder Liger (Thunderclaw) | **6** | 77 |  |
| Bladed Volcanic Xornotaurus | **7** | 150 |  |
| High Elemental Storm Eagle | **8** | 280 | high |
| Behemoth | **12** | 3,000 |  |
| Phoenix | **14** | 8,700 |  |

## Salamanders and slimes

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Slime | **0.7** | 0.25 | base |
| Fire Slime | **0.8** | 0.42 | fire |
| Baby Salamander | **0.9** | 0.67 | hatchling |
| Ooze | **1.6** | 2.3 |  |
| Salamander | **1.6** | 2.3 | adult |
| Flame Salamander | **2.2** | 4.8 | fire |
| Volcanic Salamander | **3** | 10 | volcanic |
| Ruby Salamander | **3.3** | 12 | ruby |

## Skeletons

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Flaming Skull | **1** | 1 | fire skull |
| Skeleton | **1** | 1 | base |
| Fiery Skeleton | **1.3** | 1.5 | fire base |
| Skeleton Soldier | **1.3** | 1.5 | soldier |
| Flaming Skeleton | **1.5** | 2 | fire |
| Skeleton Warrior / Advanced Skeleton | **1.5** | 2 | warrior |
| Blazing Skeleton | **1.7** | 2.6 | blazing |
| Skeleton Berserker | **1.8** | 3 | berserker |
| Blazing Skeleton Archer | **1.9** | 3.5 | blazing archer |
| Skeleton Spearmaster | **2** | 4 | spearmaster |
| Blazing Skeleton Warrior / Flaming Skeleton Soldier | **2.1** | 4.4 | blazing warrior |
| Skeleton Champion | **2.4** | 5.8 | champion |
| Infernal Skeleton / Infernal Flaming Skull | **2.6** | 6.9 | infernal base |
| Obsidian Skeleton | **3** | 10 | obsidian |
| Infernal Skeleton Berserker | **3.3** | 12 | infernal berserker |
| Infernal Skeleton Spearmaster | **3.5** | 14 | infernal spearmaster |
| Infernal Skeleton Guardian | **3.7** | 16 | infernal guardian |
| Infernal Skeleton Champion | **4** | 20 | infernal champion |
| Obsidian Skeleton Gargoyle | **4** | 20 | obsidian gargoyle |
| Stormborn Infernal Skeleton Axeman | **4.2** | 23 | stormborn |
| Molten Infernal Skeleton Berserker | **4.5** | 28 | molten |

## Undead and spirits of the dead

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Zombie | **0.9** | 0.67 |  |
| Fungal Zombie | **1.2** | 1.3 |  |
| Ghost | **1.8** | 3 | incorporeal |
| Ghoul | **2** | 4 |  |
| Mummy | **2.3** | 5.3 |  |
| Abyssal Ghoul | **2.8** | 8.3 |  |
| Phantom | **2.8** | 8.3 |  |
| Specter | **3** | 10 |  |
| Mana Phantom | **3.3** | 12 |  |
| Venomous High Ghoul | **3.6** | 15 | high |
| Vampire | **5** | 40 |  |

## Liches

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Lich | **7** | 150 | base |
| Infernal Lich | **9** | 530 | infernal |
| Purgatory Lich | **10** | 1,000 | purgatory |
| Draconic Lich | **11** | 1,700 | draconic |
| Lich King | **13** | 5,100 | ruler |

## Dragon-kin and dragons

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Dragon (egg) | **0** | 0 | egg |
| Amphiptere | **3.5** | 14 |  |
| Undead Amphiptere | **3.8** | 17 | undead |
| Corrupted Undead Amphiptere | **4.5** | 28 | corrupted undead |
| Undead Draconian | **4.8** | 35 | undead |
| Undead Drake | **5** | 40 | undead |
| Drake | **5.2** | 46 | base |
| Wyvern | **6** | 77 |  |
| Flame Wyvern | **6.8** | 130 | fire |
| Drake King | **7** | 150 | ruler |
| Lindwurm | **7** | 150 |  |
| Lesser Dragon Shade Stalker | **7.3** | 180 | shade |
| Skeletal Lesser Dragon | **7.5** | 210 | skeletal |
| Venomous Forest Wyrm | **7.5** | 210 | venomous |
| Undead Lesser Dragon | **7.8** | 250 | undead |
| Wyrm | **7.8** | 250 |  |
| Lesser Dragon | **8** | 280 | lesser |
| High-Fungalfang Lindwurm | **8.3** | 340 | high |
| Infernal Wyrm | **9** | 530 | infernal |
| Dragon Shade Stalker | **9.5** | 730 | shade |
| Hydra Tortoise | **9.5** | 730 |  |
| Hydra | **10** | 1,000 |  |
| Undead Draconic Lord | **10** | 1,000 | undead lord |
| Corrupted Undead Draconic Lord | **10.5** | 1,300 | corrupted undead lord |
| Draconic Lord | **11.5** | 2,300 | lord |
| Dragon | **12** | 3,000 | true dragon |
| Black Dragon | **13.5** | 6,700 | chromatic |
| Red Dragon | **13.5** | 6,700 | chromatic |
| Infernal Dragon | **16** | 22,000 | infernal |
| Volcanic Hydra Tortoise Titan | **17** | 32,000 | titan |
| Calamity Dragon | **20** | 100,000 | cap |

## Demons and devils

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Pale Imp | **1.1** | 1.1 | lesser |
| Imp | **1.4** | 1.7 | lesser |
| Lesser Spiked Devil | **2.6** | 6.9 | lesser |
| Incubus | **3** | 10 | charm |
| Succubus | **3** | 10 | charm |
| Spiked Devil | **3.3** | 12 |  |
| Chain Devil | **3.6** | 15 |  |
| Devil | **4** | 20 |  |
| Demon | **4.5** | 28 |  |
| Blade Demon | **5** | 40 |  |
| Blazing Blade Demon | **5.6** | 59 | blazing |
| Lord of Fury | **12** | 3,000 | demon lord |

## Abyssal horrors and shades

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Lesser Abyssal Abomination | **5** | 40 | lesser |
| Abomination | **5.5** | 56 |  |
| Infernal Shade | **5.5** | 56 | infernal |
| Shade Stalker | **5.5** | 56 |  |
| Abyssal Abomination | **7** | 150 |  |
| Shade Terror | **7** | 150 |  |
| High Shade Terror | **8.5** | 390 | high |
| Mantis-shaped abyssal horror | **9** | 530 |  |
| Eldritch Horror | **12** | 3,000 |  |

## Golems and constructs

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Wooden Soldier | **1.3** | 1.5 | soldier |
| Wooden Warrior | **1.8** | 3 | warrior |
| Mimic | **2.6** | 6.9 | ambush |
| Wooden Soldier Captain | **2.6** | 6.9 | captain |
| Floating Golem | **3** | 10 |  |
| Golem | **3.2** | 11 | base |
| Gargoyle | **3.3** | 12 |  |
| Rock Golem | **3.5** | 14 |  |
| Wooden Commander | **3.5** | 14 | commander |
| Stone Golem | **4** | 20 |  |
| Battle Golem | **4.2** | 23 |  |
| Spider Golem | **4.5** | 28 |  |
| Ruby Golem | **5** | 40 |  |
| Iron Golem | **5.3** | 49 |  |
| Wooden Lord Commander | **5.3** | 49 | lord commander |
| Volcanic Golem | **5.8** | 68 |  |
| High Stone Golem | **6** | 77 | high |
| Obsidian Golem | **6** | 77 | obsidian line |
| High Stone Golem Guard | **6.3** | 94 | high guard |
| Runic Golem | **6.8** | 130 |  |
| Golem Lord | **7.5** | 210 | lord |
| Giant Golem | **8** | 280 | giant |
| Titan | **16** | 22,000 | primordial |

## Elementals, spirits, fey and plants

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Fairy | **0.8** | 0.42 |  |
| Wisp | **0.8** | 0.42 |  |
| Will-o'-the-Wisp | **1.2** | 1.3 | lure |
| Mana Ink Elemental | **2.4** | 5.8 |  |
| Artificial Spirit | **2.5** | 6.3 |  |
| Dryad | **2.8** | 8.3 |  |
| Living Tree | **3.5** | 14 |  |
| Fire Elemental / Water Elemental / Wind Elemental | **4.5** | 28 |  |
| Earth Elemental | **4.8** | 35 |  |
| Corrupted Flesh-Eating Tree | **5** | 40 | corrupted |
| Treant | **6.5** | 110 |  |
| Greater Fire Elemental | **7** | 150 | greater |
| Tower Spirit | **8** | 280 | bound |

## Aquatic

| Form | Threat | ≈ Humans | Stage |
|---|---:|---:|---|
| Monster Fish | **1.6** | 2.3 |  |
| Soul Carp | **3** | 10 | spirit |
| Serpent | **3.3** | 12 |  |
| Spirit Carp | **3.8** | 17 | spirit |
| Sea Serpent | **5.5** | 56 |  |
| Sea tentacle-shark | **5.8** | 68 |  |
| High Spirit Carp | **6** | 77 | high spirit |
| Azure Scaled Sea Serpent | **6.3** | 94 |  |
| Kraken | **14** | 8,700 |  |
| Leviathan | **18** | 47,000 |  |

## Appendix: mundane animals

Converted from `animal_strength.md` through the same map. Wild boar (**2**) sits clearly below Spiked Boar (**2.7**).

| Animal | Threat | ≈ Humans |
|---|---:|---:|
| Mosquito | **0.017** | ≪0.01 |
| Ant | **0.032** | ≪0.01 |
| Moth | **0.042** | ≪0.01 |
| Bee | **0.055** | ≪0.01 |
| Spider | **0.058** | ≪0.01 |
| Wasp | **0.067** | ≪0.01 |
| Praying Mantis | **0.091** | ≪0.01 |
| Hornet | **0.091** | ≪0.01 |
| Centipede | **0.12** | ≪0.01 |
| Worm | **0.13** | ≪0.01 |
| Bat | **0.14** | ≪0.01 |
| Lizard | **0.15** | ≪0.01 |
| Fish | **0.17** | ≪0.01 |
| Frog | **0.18** | ≪0.01 |
| Scorpion | **0.2** | ≪0.01 |
| Toad | **0.2** | ≪0.01 |
| Snake | **0.24** | ≪0.01 |
| Carp | **0.25** | ≪0.01 |
| Venomous Toad | **0.3** | 0.01 |
| Piranha | **0.3** | 0.01 |
| Rat | **0.36** | 0.02 |
| Tortoise | **0.36** | 0.02 |
| Turtle | **0.36** | 0.02 |
| Vulture | **0.46** | 0.05 |
| Hawk | **0.52** | 0.08 |
| Owl | **0.55** | 0.1 |
| Eagle | **0.61** | 0.15 |
| Viper | **0.66** | 0.2 |
| Fox | **0.7** | 0.25 |
| Deer | **1.1** | 1.2 |
| Wolf | **1.5** | 2 |
| Boar | **2** | 4 |
| Shark | **2.4** | 6 |
| Horse | **2.6** | 7 |
| Lion | **2.8** | 8 |
| Bear | **3** | 10 |
| Tiger | **3** | 10 |
| Elephant | **5** | 40 |
| Wooly Mammoth | **5.3** | 50 |
| Whale | **5.6** | 60 |
