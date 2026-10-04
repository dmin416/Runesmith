# Mana Cast Physics

Hub: `../Science.md`.
**Shared cast / path law:** `../../../Runes/Energy.md` (η(L), μ(INT), η_cond, G, mana-in, no-stack rules, voice baselines).
This file is spell-specific worked tables only (Bolt, Arrow, Shield, Hands, Ember, anchors).
Cast blurbs also in Old `Combat/Spells.md` until absorbed.

## Kinetic vs thermal mana (rough guide)

The dividing line in this system: **kinetic magic is still cheaper than bulk thermal work**, but mid/high casts now carry hundreds to thousands of joules so small melts get realistic. Latent heat and plasma remain the walls.

Mana per gram uses `mana = joules / (10 × η × μ)`.

### Joules per mana (k = 0.8)

`J/mana = 10 × η(L) × μ(INT)`

| INT | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 |
|---|---|---|---|---|---|---|---|---|---|
| 15 | 3.00 | 10.0 | 12.9 | 15.7 | 18.6 | 21.4 | 24.3 | 27.1 | 30.0 |
| 40 | 6.58 | 21.9 | 28.2 | 34.4 | 40.7 | 47.0 | 53.2 | 59.5 | 65.8 |
| 73 | 10.6 | 35.5 | 45.6 | 55.7 | 65.9 | 76.0 | 86.1 | 96.2 | 106 |
| 100 | 13.7 | 45.6 | 58.7 | 71.7 | 84.7 | 97.8 | 111 | 124 | 137 |
| 150 | 18.9 | 63.1 | 81.1 | 99.2 | 117 | 135 | 153 | 171 | 189 |
| 200 | 23.8 | 79.4 | 102 | 125 | 148 | 170 | 193 | 216 | 238 |
| 250 | 28.5 | 94.9 | 122 | 149 | 176 | 203 | 231 | 258 | 285 |
| 300 | 33.0 | 110 | 141 | 173 | 204 | 235 | 267 | 298 | 330 |
| 500 | 49.6 | 165 | 213 | 260 | 307 | 354 | 401 | 449 | 496 |
| 1,000 | 86.4 | 288 | 370 | 452 | 535 | 617 | 699 | 781 | 864 |

### Mana cost per gram of matter

| Transition | Energy per g | INT 40 L1 | INT 100 L1 | INT 500 L1 | INT 40 L9 | INT 100 L9 |
|---|---|---|---|---|---|---|
| Melt ice at 0 °C | 334 J | 51 | 24 | 7 | 5 | 2 |
| Heat water 20→100 °C | 334 J | 51 | 24 | 7 | 5 | 2 |
| Boil water at 100 °C | 2,257 J | 343 | 165 | 46 | 34 | 16 |
| Ice at 0 °C → steam | 3,009 J | 457 | 220 | 61 | 46 | 22 |
| Melt iron from 20 °C | ~1,160 J | 176 | 85 | 23 | 18 | 8 |
| Vaporize iron from 20 °C | ~8,300 J | 1,262 | 606 | 167 | 126 | 61 |
| Fully ionize air (plasma) | ~134,000 J | 20,380 | 9,792 | 2,702 | 2,038 | 979 |

### Scale check

- A gram of ice melt is a low double-digit mana cost at INT 40 L1 and a few mana at L9.
- Boiling and iron melts still eat serious mana. Plasma in bulk stays harsh. Thin spark channels stay cheap.

### Design levers for states of matter

1. **Cooling direction.** Removing heat is the rule that shapes ice magic. Charging mana equal to the heat moved makes freezing as costly as melting. Treating it as a heat pump that dumps the heat nearby makes the surroundings get hot, a good tell for ice mages. Deleting the heat outright is the cheapest option and breaks conservation.
2. **Latent heat is the wall.** Heating a solid to its melting point is often cheaper than the melt itself and boiling costs about seven times as much as melting for water. Casters who "almost" melt something are realistic. Steam magic should be rare and prestigious.
3. **Targeting efficiency.** A separate thermal efficiency, such as half of the kinetic path because heat spreads, would make fire mages specialists. A school or talent could restore the missing share.
4. **Phase shortcuts.** A spell that rearranges bonds without supplying the full latent heat, such as "unbinding" a solid, sidesteps the budget with a fixed mana cost per gram. That keeps physics intact for brute heating and gives skilled mages a way around it.

## Reference anchors (100 J and 10 kJ)

Feel guides for elemental and force effects. Match cast Useful energy to these rows.

### Reference anchors

| Energy | Real-world equivalent |
|---|---|
| 100 J | A hard punch; a .22 LR bullet (~140 J); lifting 10 kg 1 m |
| 10 kJ | ~2/3 of a .50 BMG round; 2.4 food calories; lifting an 80 kg person ~13 m |

### Classical and derived elements

| Element | 100 J | 10 kJ |
|---|---|---|
| **Fire** | A lighter flame for 1 to 2 seconds; a tenth of a match | ~10 matches burned at once; ~0.2 g of gasoline; a hand-sized 2nd/3rd degree burn if dumped fast |
| **Water** (kinetic) | 1 L of water at 14 m/s; a hard shove from a hose blast | 10 L at 45 m/s or 100 L at 14 m/s; knocks a person off their feet into a wall |
| **Ice** (freezing) | Freezes ~0.3 g of water; a frosted fingertip | Freezes ~25 g of room-temp water; an ice cube or a frostbitten patch of skin |
| **Ice** (shard) | 10 g shard at 140 m/s; roughly an arrow hit | 1 kg spike at 140 m/s; punches through a torso |
| **Lightning** | About half a defibrillator shock; can stop a heart | ~1/100,000 of a real bolt; lethal arc with burns, a loud crack and flash |
| **Earth/Stone** | 1 kg rock at 14 m/s; a hard-thrown brick | 100 kg boulder at 14 m/s; like being hit by a car at low speed |
| **Air/Wind** | 1 m³ of air at 13 m/s; a gust that staggers | 1 m³ of air at 130 m/s; a focused blast that throws a person flat |
| **Metal** | A .22 LR round | A heavy rifle round or ~3 hunting rifle shots |
| **Steam** | Boils off ~0.04 g of water; a painful puff | ~4 g of scalding steam; a face-scalding blast |
| **Magma** | The heat of ~0.08 g of lava | The heat of ~8 g of lava; a marble-sized glowing blob |
| **Sound** (over 1 second) | ~129 dB at 1 m; painful, like a gunshot at arm's length | ~149 dB at 1 m; ruptured eardrums, jet engine up close |
| **Light** (laser/flash) | A camera flash; a focused pulse blinds or burns a spot | A 10 kW laser for 1 second; burns through thin sheet metal |
| **Wood/Nature** (growth) | Grows ~6 mg of dry wood; a sprout twitches | Grows ~0.6 g of dry wood; a small twig. Growing plants is extremely energy expensive |
| **Wood/Nature** (lash) | A whip-like vine strike | A vine or root slamming with car-impact force |

### Light, dark, life and death

| Element | 100 J | 10 kJ |
|---|---|---|
| **Light/Holy** (radiant heat) | A brief searing flash | A burst that chars skin and blinds |
| **Dark/Shadow** (draining heat) | Chills a spot of skin; a cold touch | Pulls enough heat to frostbite a limb segment |
| **Life/Healing** | 1 second of a resting human's metabolism | ~100 seconds of metabolism; enough raw energy to build roughly 1 to 2 g of new tissue. Closes a cut but not a wound |
| **Death/Necrotic** | Destroys a coin-sized patch of cells | Kills a fist-sized mass of tissue; necrotic wound |

### Force and cosmic elements

| Element | 100 J | 10 kJ |
|---|---|---|
| **Force/Arcane** | A punch-strength invisible shove | A telekinetic hit with rifle-round energy spread across a body; breaks bones |
| **Gravity** | Lift a 10 kg object 1 m; drop a person 13 cm | Lift a person ~4 stories; slam them down from that height (often lethal) |
| **Space** (teleport via lift-equivalent) | Moves 10 kg a meter "uphill" | Moves a person ~13 m of vertical displacement |
| **Time, Mind, Fate, Dream, Illusion** | No physical energy analog; use Force or Gravity numbers as a casting-cost baseline | Same approach at 100× scale |

### Scaling rule of thumb

- 100 J: an injury or a trick. Matches a punch or light gunfire.
- 10 kJ: a kill shot on an unarmored person or a serious wound on an armored one.
- 1 MJ: about 100× beyond 10 kJ; destroys a car or collapses a room.
- 1 GJ: a real lightning bolt; levels a house.

## Mana Bolt speaking levels

Blunt bean/egg. **Pop = kinetic = Useful** from the shared cast law.

```
Useful = mana × 10 × η(L) × μ(INT)
Speed = √(2 × Useful / 0.084 kg)
Ram pressure = ½ ρ v²    (ρ = 2,000 kg/m³)
```

"Pop" is swelling energy at contact. Goblin: head 3 kg, skull failure 3.3 kN, contact 1.5 ms.

### Speaking levels (mana; same spell L)

Voice sets how much mana you feed the cast. Power follows the cast law on that mana. **Overcharging a spell is equal to the mana used** (any amount; loud / very loud are just named rungs on that scale).

| Voice | Mana | L1 @ INT 40 | L1 @ INT 73 | L9 @ INT 40 |
|---|---|---|---|---|
| Mental | 10 | 66 J | 106 J | 658 J |
| Whisper | 15 | 99 J | 160 J | 986 J |
| Quiet | 20 | 132 J | 213 J | 1,315 J |
| Normal | 25 | 164 J | 266 J | 1,644 J |
| Loud | 40 | 263 J | 426 J | 2,630 J |
| Very loud | 50 | 329 J | 532 J | 3,288 J |

### Output by INT (normal voice, 25 mana)

| INT | L1 | L2 | L5 | L9 | L1 speed | L9 speed |
|---|---|---|---|---|---|---|
| 15 | 75 J | 250 J | 464 J | 750 J | 42 m/s | 134 m/s |
| 40 | 164 J | 548 J | 1,018 J | 1,644 J | 62 m/s | 198 m/s |
| 73 | 266 J | 887 J | 1,646 J | 2,660 J | 80 m/s | 252 m/s |
| 100 | 342 J | 1,140 J | 2,118 J | 3,421 J | 90 m/s | 286 m/s |
| 200 | 596 J | 1,986 J | 3,689 J | 5,957 J | 119 m/s | 377 m/s |
| 500 | 1,240 J | 4,133 J | 7,675 J | 12,398 J | 172 m/s | 543 m/s |

### Goblin kill thresholds (normal voice, 25 mana)

Orbit skull failure ~**32 J** and eye-entry burst ~**63 J** both clear on **L1** from INT 40 up on a normal cast (L1 INT 40 ≈ 164 J). Weakspot aim still matters more than raw joules at low level. Whisper is 0.6× normal mana; mental is 0.4×. Temple hits fail earlier than vault hits.

Overcharge = mana spent. Named voices are convenience labels, not a separate formula.

## Mana Arrow

Pure kinetic projectile with **no pop**. Condensed mana shaped as an arrow with hidden razor vanes.

### Base stats

| Property | Value |
|---|---|
| Size | 4 mm × 400 mm (5.03 cm³) |
| Mass | 40 g |
| Effective density | ~7,950 kg/m³ |
| Hydrodynamic reach (soft tissue) | ~1,101 mm |
| Damage type | Kinetic and slicing |

Shaft mass stays **40 g** at any thickness (condensed mana). Speed and kinetic energy do not depend on shaft width. Effective density rises as the shaft narrows.

```
Hydrodynamic reach = L × √(ρ_shaft / ρ_tissue)     (ρ_tissue = 1,050 kg/m³)
```

At 400 mm and ~7,950 kg/m³ this is 400 × √(7,950/1,050) ≈ **1,101 mm**. Treat as condensed-mana fiction (the long-rod rule is hypervelocity on Earth). A goblin torso (~140 mm) and a human torso (~220 mm) sit inside this limit on a soft path.

### Energy

Same cast law as Mana Bolt. Pure kinetic (no pop). Mass 40 g. **Voice costs are 2× Bolt** for the same named rung. Overcharge = mana spent.

```
Kinetic = mana × 10 × η(L) × μ(INT)
Speed = √(2 × Kinetic / 0.04 kg)
```

| Voice | Mana (Arrow) | vs Bolt |
|---|---|---|
| Mental | 20 | 2× |
| Whisper | 30 | 2× |
| Quiet | 40 | 2× |
| Normal | 50 | 2× |
| Loud | 80 | 2× |
| Very loud | 100 | 2× |

| Mana | Spell L | INT | Kinetic | Speed |
|---|---|---|---|---|
| 50 | 1 | 40 | 328 J | 128 m/s |
| 50 | 2 | 40 | 1,096 J | 234 m/s |
| 50 | 5 | 40 | 2,035 J | 319 m/s |
| 50 | 9 | 40 | 3,288 J | 405 m/s |
| 50 | 1 | 73 | 532 J | 163 m/s |
| 50 | 5 | 73 | 3,293 J | 406 m/s |
| 50 | 9 | 73 | 5,320 J | 516 m/s |
| 50 | 9 | 100 | 6,843 J | 585 m/s |

Warbow arrows fly about 55–65 m/s; compound about 80–95 m/s. A normal Arrow already far exceeds that on L1 mid INT.


### Punch cost (4 mm shaft)

```
E_punch = 1.5 × R × A × t
A = 0.1257 cm²
```

R in MPa, t in cm, E in J. Cost scales with diameter squared (4 mm = 25% of an 8 mm shaft). Mana to pay that joule cost: `mana = joules / (10 × η(L) × μ(INT))`.

| Material | R | Thickness | Joules | Mana L1 INT 40 | Mana L2 INT 40 |
|---|---|---|---|---|---|
| Goblin skin | 15 MPa | 2 mm | 0.6 J | 0.1 | 0.03 |
| Hobgoblin skin | 30 MPa | 4 mm | 2.2 J | 0.3 | 0.1 |
| Cow hide | 40 MPa | 4 mm | 3.0 J | 0.5 | 0.1 |
| Hardened leather | 60 MPa | 5 mm | 5.6 J | 0.9 | 0.3 |
| Mail | 350 MPa | 1.5 mm | 9.9 J | 1.5 | 0.5 |
| Dog-sized ant | 180 MPa | 3 mm | 10.2 J | 1.6 | 0.5 |
| Dog-sized mantis | 250 MPa | 3 mm | 14.1 J | 2.1 | 0.6 |
| Brigandine | 500 MPa plate + ~40 MPa backing | 1.5 mm + 3 mm | 16 J | 2.4 | 0.7 |
| Iron (2 mm) | 700 MPa | 2 mm | 26 J | 4.0 | 1.2 |
| Steel (1 mm) | 1,400 MPa | 1 mm | 26 J | 4.0 | 1.2 |
| Car-sized ant plate | 180 MPa | 18 mm | 61 J | 9.3 | 2.8 |
| Car-sized mantis plate | 250 MPa | 18 mm | 85 J | 12.9 | 3.9 |
| Mythril | 3,500 MPa | 1 mm | 66 J | 10.0 | 3.0 |
| Adamantium (cast-final) | 3,500 MPa | 1 mm | 66 J | 10.0 | 3.0 |

Brigandine is **not** 500 MPa through 4.5 mm (that would be ~42 J). It is hard plate plus soft backing.

### Hardness gate

Tip and vanes share one gate: they only bite when hardness **H ≥ 1.5 × R**. Below that the tip blunts or shatters and vanes chip or skate. Hardness does not depend on shaft width.

```
H(INT) = 600 × ln(1 + INT / 100) / ln(1.4)     MPa
Max R cleared = H / 1.5
```

**Joule costs apply only after the gate clears.** A through-shot near the tip limit may open a hole and still fail to slice if the vanes do not clear R.

| INT | H | Max R cleared |
|---|---|---|
| 15 | 249 MPa | 166 MPa |
| 25 | 398 MPa | 265 MPa |
| 40 | 600 MPa | 400 MPa |
| 73 | 977 MPa | 651 MPa |
| 100 | 1,236 MPa | 824 MPa |
| 200 | 1,959 MPa | 1,306 MPa |
| 500 | 3,195 MPa | 2,130 MPa |
| 1,000 | 4,276 MPa | 2,851 MPa |
| 2,000 | 5,429 MPa | 3,619 MPa |

Minimum INT to clear R: goblin skin **2** / hardened leather **6** / dog ant **17** / dog mantis **24** / mail **35** / brigandine plate **53** / iron **81** / steel **225** / mythril **1,800**.

At **INT 40** (max R 400 MPa): leather and mail are open; **brigandine plate, iron, steel and mythril are closed** even if joules would allow them. Example: 50 mana at INT 40 gives ~328 J, enough joules for steel, but the hardness gate still blocks steel until INT ~225.

### Slicing fletchings

Three razor vanes at 120°. Each is 60 mm long and reaches 20 mm from the shaft with a 0.5 mm edge. Visible fletching looks only ~8 mm wide.

- Tip punches a ~0.4 cm hole; vanes cut a three-armed star slit ~4 cm across on a through-shot.
- Slicing only on through-shots. A stopped arrow gets tip/shaft damage and a small entry cut.
- A head shot that lodges against the back of the skull never engages the vanes. Tip alone kills at about **8 J**.
- Vane cost does not change with shaft width.

| Layer | Toughness | Blade cost |
|---|---|---|
| Skin (2 mm) | 1.5 J/cm² | 1.8 J per wall |
| Muscle | 0.2 J/cm² | 1.2 J per cm |
| Lung / liver / bowel / brain | 0.1 J/cm² | 0.6 J per cm |

#### Goblin kill paths (through and through, between ribs)

Mana from cast law (`mana = joules / (10 × η × μ)`). Soft kills are cheap; hardness gate still decides armor.

| Path | Joules | Mana L1 INT 40 | Mana L2 INT 40 | Time to death |
|---|---|---|---|---|
| Neck (carotids and jugulars) | 13 J | 2.0 | 0.6 | 10 to 30 s |
| Chest through the heart | 17 J | 2.6 | 0.8 | 10 to 60 s |
| Chest through the lung | 17 J | 2.6 | 0.8 | 1 to 5 min |
| Abdomen through the liver | 17 J | 2.6 | 0.8 | 2 to 10 min |
| Thigh (femoral vessels) | 25 J | 3.8 | 1.1 | 1 to 3 min |

A rib in the path adds roughly **20 J**.

#### Full slicing pass through armor

| Armor | Punch | Vane slit | Total | Mana L1 INT 40 | Mana L2 INT 40 | Gate |
|---|---|---|---|---|---|---|
| Hardened leather | 5.6 J | 9 J | 14.6 J | 2.2 | 0.7 | open from INT 6 |
| Mail | 9.9 J | 16 J | 25.9 J | 3.9 | 1.2 | open from INT 35 |
| Steel (1 mm) | 26 J | 42 J | 68 J | 10.3 | 3.1 | **closed until INT ~225** |

If the vanes stall, the arrow lodges with vanes outside and no slicing happens.

### Car-sized insects

Dog-sized ants and mantises fall to a single arrow anywhere once joules and hardness clear (INT **17** / **24**). Headshots always work.

Car-sized specimens have **18 mm** plate. Weakspots fall at any casting INT.

| Weakspot | R | Thickness | Joules |
|---|---|---|---|
| Joint membrane (neck / leg root / waist) | 30 MPa | 0.5 mm | 0.28 J |
| Compound eye | 100 MPa | 1 mm | 1.9 J |
| Antenna base | 100 MPa | 1 mm | 1.9 J |

```
Plate depth per arrow = Kinetic / (0.1885 × R)   cm
```

| Cast @ INT 40 | Kinetic | Arrows for ant plate (61 J) | Arrows for mantis plate (85 J) |
|---|---|---|---|
| 50 mana L1 (normal) | 328 J | 1 | 1 |
| 50 mana L2 | 1,096 J | 1 | 1 |

One arrow clears ant plate at **61 J** (~9 mana at L1 INT 40, or ~3 mana at L2) and mantis plate at **85 J** (~13 mana at L1 INT 40, or ~4 mana at L2), if hardness already clears (true by INT 24+).

### Elemental versions

Element takes share **f** of kinetic K; punch keeps `(1 − f) × K`. At L1 INT 40 a normal Arrow (50 mana) is ~328 J; a 4 mm shaft can put a large elemental share into fire/cold/wind and still punch mail (9.9 J).

| Element | Mechanism | Effect at 328 J |
|---|---|---|
| Fire | Momentum becomes heat | Ignites cloth and hair at about 10 J. Coagulates about 4 cm³ of tissue. Seared cuts seal and reduce bleeding |
| Cold | Momentum becomes heat removal | Freezes about 0.8 g of tissue. Suits a brittle wound rim or a slowed limb |
| Wind | Wide slash | Cuts a ~60 cm slash about 25 cm deep in flesh. Armor stops it completely |
| Water | Pressure sheet | Needs v above √(2R / 1,000) with R in MPa and water density 1,000 kg/m³: skin **173 m/s**, leather **346 m/s**, mail **837 m/s**. Sheet volume = E / R |
| Stone | Spike | 40 g spike carries the share as KE. Tip yields near 150 MPa. Passes hide and leather; shatters on carapace and harder |

### Katana comparison

Katana edge hardness ~**400 MPa** clears R up to **267 MPa** (matches an arrow around INT **25**). A katana swing carries about **125 J**. It cuts through mantis carapace and fails on mail and harder. A goblin neck takes about **56 J** (soft tissue ~11 J and vertebra ~45 J). A mana-infused katana uses the same `H(INT)` curve as the arrow tip.

See also Old `Combat/Spells.md` (Mana Bolt, Mana Arrow) until absorbed.

## Ember

Ignition energy needed at the target. Ember pays Useful joules into heat at a point; match the row to what he is trying to light.

| Target | Energy needed |
|---|---|
| Spark in spirit or lamp oil fumes | 0.2–0.3 mJ |
| Spark in flour or grain dust cloud (mill, granary) | 10–100 mJ |
| Black powder (loose grains) | 10–50 mJ |
| Steel-style hot spark (1 mg at 1,000 °C) | 0.5 J |
| Amadou fungus or char cloth | 3–5 J |
| Punk wood or dry rot | 5–10 J |
| Sulfur match tip | 5–10 J |
| Candle wick (tallow or beeswax) | 20–50 J |
| Parchment corner | 30–60 J |
| Hair or fur tuft | 20–50 J |
| Dry leaves (handful) | 100–300 J |
| Oil-soaked rag or tow | 50–100 J |
| Pitch-soaked torch head | 100–300 J |
| Tinder bundle, dry grass (1 g) | 350–500 J |
| Bird's nest tinder bundle (10 g) | 3–5 kJ |
| Kindling twig surface | 300–600 J |
| Hemp rope end | 300–800 J |
| Linen or wool clothing edge | 500 J–2 kJ |
| Dry straw or hay surface | 1–3 kJ |
| Thatch roof patch | 3–10 kJ |
| Pool of lamp oil (open flame, no wick) | 1–5 kJ |
| Tar or pitch barrel surface | 5–20 kJ |
| Split log (sustained flame) | 20–50 kJ |
| Oak beam or door (sustained flame) | 100–500 kJ |
| Green wood branch | 50–200 kJ |
| Damp tinder (per 1 g, 10% water) | add 225 J |
| Wet wood (per 10 g water to drive off) | add 25 kJ |

## Mana Hands

Move objects with mana. Visible hands are optional. Work done by a telekinetic lift, push or throw. Hold rows use continuous drain (J/s).

| Action | Energy |
|---|---|
| Flip a page, snuff a candle | <0.1 J |
| Untie a knot, slide a bolt | 0.5–1 J |
| Turn a key in a lock | 0.5–1 J |
| Pull a lever | 1–3 J |
| Open a door | 2–5 J |
| Carry a scroll 100 m | 1–5 J |
| Pump a forge bellows (one stroke) | 20–40 J |
| Lift a 1 kg object 1 m | 9.8 J |
| Lift a 1.5 kg sword 1 m | 15 J |
| Yank a sword from a grip | 20–50 J |
| Draw a longbow to full (stored energy) | 80–100 J |
| Draw a warbow to full (stored energy) | 100–150 J |
| Throw a dagger at 15 m/s | 25 J |
| Throw an arrow by hand at bow speed | 60–150 J |
| Throw a 1 kg rock at 10 m/s | 50 J |
| Throw a 1 kg rock at 20 m/s | 200 J |
| Knock a standing man off balance | 50–100 J |
| Ring a church bell (one swing) | 200–500 J |
| Lift a 20 kg crate 1 m | 196 J |
| Crank a heavy crossbow to full | 200–300 J |
| Throw a 5 kg stone at 15 m/s | 560 J |
| Pull a rider from the saddle | 200–400 J |
| Lift an 80 kg person 1 m | 785 J |
| Draw a 10 L bucket up a 10 m well | 980 J |
| Drag a 20 kg crate 10 m on stone | ~1 kJ |
| Lift an 80 kg person onto a 3 m wall | 2.4 kJ |
| Lift a 500 kg horse 1 m | 4.9 kJ |
| Catch an 80 kg person falling 10 m | 7.8 kJ |
| Lift a 1-ton stone block 1 m | 9.8 kJ |
| Pull a 500 kg loaded cart 100 m on road | ~10 kJ |
| Raise a 500 kg portcullis 3 m | 14.7 kJ |
| Raise a 2-ton drawbridge | ~40 kJ |
| Hold 1 kg (proposed rule) | 1 J/s |
| Hold 20 kg (proposed rule) | 20 J/s |
| Hold 80 kg (proposed rule) | 78 J/s |
| Hold 500 kg (proposed rule) | 490 J/s |

Hold rows are **grip / restraint** only. Airborne hover and flight use the power equations in `Flight.md` (η and μ apply; no separate expensive/cheap fiat).

## Mana Shield

Barrier hit count from the shared cast law, scaled by shield area and hold time. **Baseline cast = 100 mana** (2× normal Arrow, 4× normal Bolt). Overcharge = mana spent.

**Fight-scale map** (physical tip KE vs shield pools, worked Ch 14 lock): `../../../Combat/AttackScale.md`.

```
N = floor( 20 × M × η(L) × μ(INT) × S × R / J )

M      = shield mana
J      = threat energy (J)
η(1)   = 0.3
η(L)   = 1 + (L - 2) × 2/7              // L2-L9
μ(INT) = (INT / 15)^0.8
S      = √(0.2 / A)                     // A = shield area, m²
R      = 1 - (0.1 × A × t) / M          // t = seconds held
```

The leading **20** is `2 × 10`: paid joules per mana times the focused 45° absorb share (50% of threat). Whole attacks only; round down.

| Shape | A | S | R |
|---|---|---|---|
| Focused disk | 0.2 m² | 1 | 1 (no area bleed) |
| Semicircle | 6.28 m² | 0.178 | 1 - 0.628 t / M |

### Threat energies (J)

| Threat | J |
|---|---|
| Longbow arrow | 100 |
| Warbow arrow | 125 |
| Heavy crossbow bolt | 200 |
| Thrown javelin | 200 |
| Greatsword or warhammer | 300 |
| Volley, 10 warbow arrows | 1,250 |
| Ogre club | 3,400 |
| Ballista bolt | 6,000 |
| Horse and rider at canter | 19,000 |
| Dragon claw | 35,000 |
| Trebuchet stone | 90,000 |

### Profiles (focused disk, k = 0.8)

| Profile | INT | L | Effective pool 50 mana (20 M η μ) | Effective pool 100 mana |
|---|---|---|---|---|
| Novice | 15 | 1 | 300 J | 600 J |
| Apprentice | 40 | 2 | 2,190 J | 4,380 J |
| Journeyman | 73 | 3 | 4,560 J | 9,120 J |
| Adept | 100 | 5 | 8,470 J | 16,940 J |
| Master | 200 | 7 | 19,300 J | 38,600 J |
| Archmage | 500 | 9 | 49,600 J | 99,200 J |

### Whole attacks (focused disk, 50-mana shield)

| Threat | J | Novice | Apprentice | Journeyman | Adept | Master | Archmage |
|---|---|---|---|---|---|---|---|
| Longbow arrow | 100 | 3 | 21 | 45 | 84 | 193 | 496 |
| Warbow arrow | 125 | 2 | 17 | 36 | 67 | 154 | 396 |
| Heavy crossbow bolt | 200 | 1 | 10 | 22 | 42 | 96 | 248 |
| Thrown javelin | 200 | 1 | 10 | 22 | 42 | 96 | 248 |
| Greatsword or warhammer | 300 | 1 | 7 | 15 | 28 | 64 | 165 |
| Volley, 10 warbow arrows | 1,250 | 0 | 1 | 3 | 6 | 15 | 39 |
| Ogre club | 3,400 | 0 | 0 | 1 | 2 | 5 | 14 |
| Ballista bolt | 6,000 | 0 | 0 | 0 | 1 | 3 | 8 |
| Horse and rider at canter | 19,000 | 0 | 0 | 0 | 0 | 1 | 2 |
| Dragon claw | 35,000 | 0 | 0 | 0 | 0 | 0 | 1 |
| Trebuchet stone | 90,000 | 0 | 0 | 0 | 0 | 0 | 0 |

### Whole attacks (focused disk, 100-mana shield, baseline)

| Threat | J | Novice | Apprentice | Journeyman | Adept | Master | Archmage |
|---|---|---|---|---|---|---|---|
| Longbow arrow | 100 | 6 | 43 | 91 | 169 | 386 | 992 |
| Warbow arrow | 125 | 4 | 35 | 72 | 135 | 308 | 793 |
| Heavy crossbow bolt | 200 | 3 | 21 | 45 | 84 | 193 | 496 |
| Thrown javelin | 200 | 3 | 21 | 45 | 84 | 193 | 496 |
| Greatsword or warhammer | 300 | 2 | 14 | 30 | 56 | 128 | 330 |
| Volley, 10 warbow arrows | 1,250 | 0 | 3 | 7 | 13 | 30 | 79 |
| Ogre club | 3,400 | 0 | 1 | 2 | 4 | 11 | 29 |
| Ballista bolt | 6,000 | 0 | 0 | 1 | 2 | 6 | 16 |
| Horse and rider at canter | 19,000 | 0 | 0 | 0 | 0 | 2 | 5 |
| Dragon claw | 35,000 | 0 | 0 | 0 | 0 | 1 | 2 |
| Trebuchet stone | 90,000 | 0 | 0 | 0 | 0 | 0 | 1 |

### Human weapons

| Threat | Energy |
|---|---|
| Thrown dagger | 20–40 J |
| Thrown rock | 20–50 J |
| Dagger stab | 20–60 J |
| Rapier thrust | 30–60 J |
| Headbutt | 30–60 J |
| Shortbow arrow | 30–50 J |
| Hunting bow arrow | 40–60 J |
| Quarterstaff strike | 50–100 J |
| Spear thrust | 50–100 J |
| Sword cut | 60–130 J |
| Club or cudgel | 80–150 J |
| Light crossbow bolt | 80–120 J |
| Longbow arrow | 80–120 J |
| Punch | 100–150 J |
| Kick | 100–200 J |
| Warbow arrow | 100–150 J |
| Axe or mace blow | 100–200 J |
| Thrown axe | 100–150 J |
| Sling bullet | 100–300 J |
| Flail | 150–250 J |
| Heavy crossbow bolt | 150–250 J |
| Thrown javelin | 150–250 J |
| Two-handed greatsword or warhammer | 200–400 J |
| Halberd or poleaxe | 200–400 J |
| Arbalest bolt | 200–400 J |
| 20 kg rock dropped 10 m from a wall | ~2 kJ |
| Battering ram (500 kg, crewed) | 2–3 kJ |
| Heavy battering ram (1 ton) | 4–5 kJ |
| Scorpion bolt | 1–3 kJ |
| Ballista bolt | 2–10 kJ |
| Mangonel or onager stone | 5–30 kJ |
| Trebuchet stone (90 kg) | ~90 kJ |

### Mounted

| Threat | Energy |
|---|---|
| Horse kick | 500 J–1 kJ |
| Mounted sword cut (with horse speed) | 200–500 J |
| Horse and rider at trot (600 kg, 4 m/s) | ~5 kJ |
| Horse and rider at canter (600 kg, 8 m/s) | ~19 kJ |
| Couched lance charge (effective at tip) | 10–20 kJ |
| Horse and rider at full gallop (600 kg, 12 m/s) | ~43 kJ |

### Magic

Match live Bolt / Arrow casts from the cast law (voice mana × 10 × η × μ). Examples at current law:

| Threat | Energy |
|---|---|
| Mana Bolt, mental 10 mana (INT 40 L1) | ~66 J |
| Mana Bolt, normal 25 mana (INT 40 L1) | ~164 J |
| Mana Bolt, normal 25 mana (INT 40 L9) | ~1,644 J |
| Mana Arrow, normal 50 mana (INT 40 L1) | ~328 J |
| Mana Arrow, normal 50 mana (INT 40 L9) | ~3,288 J |
| Rice grain core rupture | 190 J |
| Walnut core rupture | 141 kJ |
| Standard fist core rupture | 2.7 MJ |

Core rupture rows are **mana cores / mana stones**, not jewelry gems. Unbreakable-gem seat craft (`../Metallurgy/GemInlay.md`) does not apply to cores.

### Monsters

| Threat | Energy |
|---|---|
| Rat or bat bite | <1 J |
| Wolf bite | 10–30 J |
| Goblin club | 50–100 J |
| Goblin thrown spear | 50–100 J |
| Hobgoblin sword | 100–200 J |
| Horse or bull kick | 500 J–1 kJ |
| Bear swipe | 500 J–1.5 kJ |
| Wolf pounce (40 kg, 10 m/s) | ~2 kJ |
| Dire wolf pounce (100 kg, 12 m/s) | ~7 kJ |
| Ogre club (30 kg club at 15 m/s) | ~3.4 kJ |
| Troll claw swipe | 1–3 kJ |
| Minotaur charge (300 kg, 8 m/s) | ~10 kJ |
| Wyvern tail strike | 5–10 kJ |
| Bear charge (300 kg, 12 m/s) | ~22 kJ |
| Bull charge (700 kg, 8 m/s) | ~22 kJ |
| Giant thrown boulder (100 kg, 20 m/s) | ~20 kJ |
| Giant club (200 kg club at 15 m/s) | ~22 kJ |
| Dragon claw | 20–50 kJ |
| Dragon tail sweep | 50–200 kJ |
| Dragon bite (driven by neck and body) | 50–150 kJ |
| Dragon diving strike (5 tons, 30 m/s) | ~2.25 MJ |

### Heat

| Threat | Heat energy |
|---|---|
| Torch jab (1 second contact) | 200–500 J |
| Burning arrow (pitch-wrapped head) | 1–3 kJ |
| Fire pot or oil flask splash | 20–100 kJ |
| Boiling water, 1 L | ~300 kJ (from 20 °C) |
| Hot oil poured from a wall, 1 L at 200 °C | ~330 kJ |
| Molten lead, 1 kg | ~60 kJ |
| Burning building (radiant, per second at 5 m) | 10–50 kJ per m² |
| Dragon fire breath (per second of exposure) | 1–10 MJ |

### Deflection

| Impact angle | Share of energy absorbed |
|---|---|
| 90° (head-on) | 100% |
| 60° | 75% |
| 45° | 50% |
| 30° | 25% |
| 15° | 7% |

See also `../../../Combat/Spells.md` (Ember, Mana Hands, Mana Shield).
