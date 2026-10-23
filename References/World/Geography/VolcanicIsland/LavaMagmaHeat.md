# Lava, Magma and Volcanic Heat

> **Earth physics / design loot.** What lava and magma are, how hot and how fast, how far radiant heat reaches, what heat does to bodies and gear, how lava can be stopped and what it can be used for. Earth anchors. Not Caldris law.
>
> Gases (CO₂, SO₂, H₂S, laze): `VolcanicGases.md`. Island geology and lava resources: `Resources.md`. Minerals: `HawaiianMinerals.md`. Albrook dungeon: `../Places.md`, `../Dungeons.md`. Damage sorting and resistances: `../../../Progression/ResistanceImmunitySystem.md`, `../../../Progression/DamageTypeResistances.md`. Heat pumping and cooling cost: `../../Science/Energy/EnergyPumping.md`. Heat engines from a gradient: `../../Science/Energy/Gradients.md`. Metal overheating: `../../Science/Metallurgy/OverheatedMetals.md`.

## Shared cost law

- **1 MP = 10 J.** Raw MP below is J ÷ 10. Real casters divide by their conversion (`../../Science/Energy/ManaHandPhysics.md` §2).
- **Heat flows downhill for free.** Cooling lava with water or air only costs the work of moving the water or air. Mana pays only if mana itself is made to soak up the heat.

## Magma and lava

- **Magma** is molten rock underground with gas dissolved in it, mostly water and carbon dioxide. Hawaiian-type chambers sit a few km down.
- **Lava** is magma that reaches the surface. Gas comes out as it rises. Gas plus stiff magma gives explosions. Gas plus runny magma gives fountains and flows.

| Type | Temperature | Stiffness | Behavior |
|---|---|---|---|
| **Basalt** (Hawaiʻi, Dragnis) | about 1,100 to 1,250 °C | Runny. About 10,000 to 100,000× water | Fountains, rivers and tubes. Flows can run 150 km or more |
| **Andesite** | about 800 to 1,000 °C | Much stiffer | Thick short tongues. More explosive |
| **Rhyolite** | about 700 to 900 °C | Far stiffer still | Domes and violent eruptions |

More silica means cooler, stiffer and more explosive lava.

### Flow forms

| Form | Look | Note |
|---|---|---|
| **Pāhoehoe** | Smooth, ropy, glassy skin | Hotter and gassier. Advances in toes and lobes. Builds tubes |
| **ʻAʻā** | Rough heaps of sharp clinker | Forms as lava cools or is stirred. Terrible to walk on. Shreds boots |
| **Lava tube** | A roofed river | Insulated. Lava cools only about **0.3 to 1 °C per km**. Carries hot lava tens of km |
| **Lava lake** | A pool in a crater | Constant glow and heat |
| **Fountain** | Spray tens to hundreds of m high | Makes Pele's hair (glass threads) and Pele's tears (glass drops) |

### Speed

| Case | Speed |
|---|---|
| Pāhoehoe toes | Meters per hour |
| Ordinary flow front | A walk or slower |
| Channel or steep slope | Meters per second |
| Nyiragongo 1977 (very fluid, steep) | Reported **60 to 100 km/h**. The fastest on record |

Most flows can be outwalked. The danger is being cut off, not being chased.

### Crust

A skin forms within seconds to minutes. Hours-old crust on pāhoehoe can sometimes be crossed in thick boots. It can break through to molten lava below. The surface of a crusted flow still runs a few hundred °C.

## Radiant heat

Glowing surfaces radiate `q = ε × σ × T⁴` (ε about 0.9).

| Surface | Radiant output |
|---|---|
| Fresh basalt, 1,150 °C | about 210 kW/m² |
| 1,000 °C | about 134 kW/m² |
| 800 °C (dull red) | about 68 kW/m² |
| 600 °C (faint glow) | about 30 kW/m² |
| 400 °C (crusted, dark) | about 10.5 kW/m² |
| 200 °C | about 2.6 kW/m² |

**At a distance** (rough, facing the glow):

| Distance | 10 m wide fresh flow | 100 m lava lake |
|---|---|---|
| 5 m | about 105 kW/m² | |
| 10 m | about 42 kW/m² | about 200 kW/m² |
| 20 m | about 12 kW/m² | |
| 50 m | about 2 kW/m² | about 105 kW/m² |
| 100 m | about 0.5 kW/m² | about 42 kW/m² |
| 200 m | | about 12 kW/m² |
| 500 m | | about 2 kW/m² |

**Body limits for bare skin** (sources vary by several seconds to tens of seconds):

| Radiant load | Effect |
|---|---|
| about 1 kW/m² | Strong tropical sun |
| about 2.5 kW/m² | Firefighter working limit for skin |
| about 4.5 to 5 kW/m² | Second-degree burn in about 30 to 40 s |
| about 6.4 kW/m² | Pain in about 8 s, blisters in about 18 s |
| about 10 kW/m² | Burns in seconds |

Ordinary clothing triples the time to pain at about 5 kW/m². Burns come fast where the heat lands on bare skin: face, hands, neck.

**Rule of thumb:** stand about **5 flow widths away** from fresh lava for long work. A lava lake pushes that out to hundreds of meters.

## Heat and the body

| Fact | Number |
|---|---|
| Heat stroke | Core above about 40 °C |
| Peak sweat | about 1 to 1.5 L/h. If it all evaporates it sheds about 1 kW |
| Water for hard work in heat | about 0.5 to 1.5 L/h |
| Dry air vs wet air | Dry heat is far more bearable. A dry sauna at 80 to 100 °C is tolerated for minutes. Humid air at 50 °C can kill |
| Breathing very hot air | Burns the airway. Masks and cooled air help |

**Radiant load swamps sweat.** At 20 m from a 10 m fresh flow a person facing it takes about 12 kW/m². Over about 0.9 m² of exposed front that is about **12 kW**, twelve times what sweat can shed.

### Protection and cost

| Defense | Effect |
|---|---|
| **Distance** | Cheapest. Load falls fast with distance |
| **Reflective outer layer** | Polished metal or aluminized cloth reflects most radiant heat. Firefighter proximity suits work this way |
| **Shield or screen** | Blocks the line of sight. Crouch behind it |
| **Heat-pump cooling** | Pumping 12 kW out to 60 °C air at grade 0.5 costs about 2.1 kW of work (about **210 MP/s raw**). Too costly alone |
| **Reflect first, then pump** | Reflect 90% and the pump only handles about 1.2 kW (about **21 MP/s raw**) |
| **Fire Resistance** | Skill and rune tracks in `../../../Progression/ResistanceImmunitySystem.md`. Chapter flame-resistance runes already block slime spit and fire attacks |

## What heat does to gear

| Item | Trouble starts | Note |
|---|---|---|
| **Paper (scrolls, maps)** | about 220 to 250 °C | Chars and ignites. Roland's scroll kit is the weak point |
| Wood | about 250 to 300 °C | Chars. Ignites with a flame or spark |
| Cotton | about 400 °C | Ignites on its own |
| Wool | about 570 °C | Resists. Better outer layer than cotton |
| Leather | a few hundred °C | Stiffens, shrinks and chars |
| Tin and soft solder | about 230 °C | Melts |
| Lead | 327 °C | |
| Tempered steel | about 200 to 300 °C and up | Loses its temper and its edge (`../../Science/Metallurgy/OverheatedMetals.md`) |
| Zinc | 420 °C | |
| Aluminum | 660 °C | |
| Silver | 962 °C | |
| Gold | 1,064 °C | |
| Copper | 1,085 °C | |
| Iron | 1,538 °C | Fresh basalt cannot melt it |

## Lava as a resource

- **Stored heat.** Cooling 1 m³ of lava to room temperature releases about **4.7 GJ**. A tube or lake is a free furnace and a heat engine (`../../Science/Energy/Gradients.md`, `../../Science/Energy/StirlingEngines.md`, `../../Science/Energy/SteamEngines.md`).
- **Nonferrous casting.** At 1,150 °C lava melts tin, lead, zinc, aluminum, silver, gold and copper. It does not melt iron.
- **Mineral wool and basalt fiber.** Molten basalt spun into fiber gives insulation and tough cloth. Pele's hair is the natural version.
- **Obsidian.** Volcanic glass takes edges far finer than steel. Brittle.
- **Sulfur, salts and minerals** crust around vents (`Resources.md`).
- **Cooking and bathing.** Steam vents and hot springs.

## Stopping or steering lava

- **Water.** At Heimaey, Iceland, in 1973 crews pumped about **6.2 million tonnes of seawater** onto the advancing Eldfell flow. It stopped short of the harbor.
- **The math.** To solidify 1 m³ of basalt it must lose about 250 °C plus its heat of freezing, about **1.9 GJ**. Water that boils off soaks up about 2.6 MJ per kg. So about **730 kg of water fully boiled per m³**. Most sprayed water runs off. Real use needs more.
- **Mana cost.** The lava does the boiling. Mana only lifts and sprays the water. Lifting 730 kg of water 10 m costs about 72 kJ (about **7,200 MP raw per m³ of lava frozen**). Making mana soak up the heat instead would cost about 190 million MP per m³.
- **Barriers and diversion.** Earth walls and trenches can steer slow flows. Explosives have been used to breach channels and tubes with mixed results.
- **Plug a tube.** Collapse a tube roof upstream and the flow breaks out somewhere new.

## Other volcanic hazards

| Hazard | Note |
|---|---|
| **Pyroclastic flow** | Ground-hugging cloud of hot gas and rock. Average about 100 km/h, peaks reported to 700 km/h. About 200 to 700 °C, up to about 1,000 °C. Unsurvivable in the open |
| Lahar | Volcanic mudflow. Fast, heavy, buries valleys |
| Volcanic bombs | Blobs and blocks thrown from vents |
| Ash | Glass shards. Hurts lungs and eyes. Wet ash collapses roofs |
| Steam blast | Magma meets groundwater. Sudden explosions with no lava showing |
| Ocean entry | Laze (acid steam plus glass) and littoral explosions (`VolcanicGases.md`) |
| Gas pooling | Carbon dioxide in hollows, tubes and caves (`VolcanicGases.md`) |
| Ground cracks | Hidden voids, thin crust, collapsing tube roofs |

## Dungeon heat ladder (design, not law)

Albrook's dungeon grows hotter with depth (`../Places.md`). Earth limits for air temperature:

| Air temperature | Unprotected people |
|---|---|
| 35 to 45 °C | Hard work for an hour or two with water and rest |
| 45 to 60 °C | Short shifts only. Fatal if humid |
| 60 to 100 °C | Minutes, dry air only. Skin and eyes suffer |
| 100 to 200 °C | Seconds to a minute with heavy protection |
| 220 °C and up | Paper and scrolls char. Wood follows near 300 °C |

Radiant heat from glowing rock adds to any air temperature above.

## Open

- How mana stones, monster cores and rune ink behave at high heat.
- Albrook floor temperatures by depth.
- Whether dungeon lava follows Earth physics or dungeon rules.
