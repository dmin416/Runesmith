# Mana Shield Master Reference

> Terra Mana Shield consolidator. Canon cast law: `../../../Runes/Energy.md`. Live spell tables: `ManaCast.md` (Mana Shield section). Fight-scale map (head-on ×10 pool): `../../../Combat/AttackScale.md`. Spell blurbs: `../../../Combat/Spells.md`. Hands timing: `../../../Combat/MageDefense.md`. Ambient: `ManaConcentration.md`. Walking-house 100 m² glide-shield cost invent: `../Vehicle/WalkingHouse.md`. **Part 15 Fix List applied to AttackScale / ManaCast / Spells (hold drain kept at 0.3 J/s per N).** Nav: `Index.md`.

---

One file for Mana Shield physics on Terra. Canon rules from the story notes come first. The physics is built on those rules: every number is mana converted to joules at the canon peg, then run through the canon pool formula. Physics only adds what the notes leave open (slow loads, held weight, momentum, air, heat). Anything new or anything that changes the notes is collected in **Part 15: Fix List** at the end.

Conventions in every table:

* "Pool" means the clean head-on pool (Part 1.3). The notes' ×20 pool equals this pool at a 45° face.
* Standard comparison casts are 100 mana at open-ground ambient (1×), head-on.
* HOLD means the shield stops the whole attack. THROUGH means the attack passes (whole attacks only).
* Roland is INT 137, Shield 6. "Top tier" is a hypothetical INT 1000, Shield 9 benchmark.

---

# Part 1. Canon Rules

## 1.1 Mana to energy

* 1 mana = 10 J at the input.
* Body cast: useful J = mana × 10 × skill factor × INT factor × ambient.
* Rune or item: useful J = mana × 10 × quality × ambient. Never both paths.
* Skill factor: 0.3 at level 1, 1.0 at level 2, rising linearly to 3.0 at level 9 (+0.2857 per level).
* INT factor: (INT / 15)^0.8.
* Ambient: √(local mana thickness). Mana paid stays the same; output changes.
* Rune quality: 0.2 / 0.4 / 0.6 / 0.8 / 1.0. Waste (1 − quality) of input: half to air, half to host as heat and strain.
* Rune Mastery cuts mana paid 10% per level (cap 90%) before conversion. Voice, focus and overcharge change only mana in.
* Raw mana with no user ≈ 0.3 J. A spell pays for its effect while it exists and leaves no residual heat. A fire spell is an ignition source; existing fuel burns on its own energy.

## 1.2 Mana Shield

* One of the three basic mage spells (with Bolt and Arrow). Forms a blue bubble that settles into a hard disk over the front of the caster or an ally.
* Baseline cast 100 mana (Arrow 50, Bolt 25). Overcharge is more mana.
* Holding a bubble bleeds it. A disk has no area bleed.
* A lesser shield can be reshaped into an elemental face (earth wall and others) by editing the surface.
* Whole attacks only: if the pool is smaller than the hit, the hit goes through.

## 1.3 The pool (clean form)

```
Pool (J)   = 10 × mana × skill factor × INT factor × shape × hold × ambient
Shape      = √(0.2 m² / face area), capped at 1.0
Hit taken  = hit energy × sin²(glancing angle)
```

The notes write the pool with ×20 because a 45° face takes half the hit. In this file the ×2 lives in the angle rule instead, so it is never applied twice. A 45° face doubles effective capacity, which reproduces every number in the notes.

---

# Part 2. The Mechanism

## 2.1 One shell, two behaviors

A Mana Shield is one shell of shaped mana. It is not built from parts. The same shell behaves two ways at once:

* **Drag.** Through its thickness the shell grips moving matter like a dense fluid. The grip rises with speed. Fast matter (arrows, balls, fragments, blast wind) meets the shell at full strength.
* **Tension.** The shell also holds its shape against any push, fast or slow, at a fixed fraction of its strength.

Real analog: shear-thickening fluid (cornstarch "oobleck", impact-absorbing D3O pads, STF-treated Kevlar "liquid armor"). One material, stiff against a hammer, soft against a slow finger.

## 2.2 Grip: how much of the pool a hit meets

```
Drag share   S(v) = v² / (v² + 40²)
Grip         G(v) = 0.2 + 0.8 × S(v)        mundane matter
Grip         G    = 1.0                     skills and spells (mana meets mana)
Pool spent   = hit taken ÷ G(v)
Shield holds if pool ≥ hit taken ÷ G(v)
```

The 0.2 is the tension floor: even a dead-slow push meets a fifth of the pool. The 40 m/s midpoint puts arrows at about 70% grip, sword cuts at 30% and settling weight at 20%. Skills and spells are exempt, so chapter 14 works at any thrust speed.

| Speed | Drag share S(v) | Grip G(v) | Roland disk, 100 mana | Roland bubble, 100 mana | Typical |
|---|---|---|---|---|---|
| 1 m/s | 0.1% | 20.0% | 2.5 kJ | 450 J | Slow press, settling weight |
| 5 m/s | 1.5% | 21.2% | 2.7 kJ | 476 J | Shove, lunge |
| 10 m/s | 5.9% | 24.7% | 3.1 kJ | 554 J | Punch, charging beast |
| 15 m/s | 12.3% | 29.9% | 3.8 kJ | 670 J | Sword cut |
| 25 m/s | 28.1% | 42.5% | 5.3 kJ | 953 J | Javelin |
| 40 m/s | 50.0% | 60.0% | 7.5 kJ | 1.3 kJ | Midpoint |
| 50 m/s | 61.0% | 68.8% | 8.6 kJ | 1.5 kJ | Arrow, bolt |
| 100 m/s | 86.2% | 89.0% | 11.2 kJ | 2.0 kJ | Sling at max |
| 300 m/s | 98.3% | 98.6% | 12.4 kJ | 2.2 kJ | Musket, pistol |
| 800 m/s | 99.8% | 99.8% | 12.5 kJ | 2.2 kJ | Rifle |

## 2.3 Held load drains the pool

A shield holding back a steady force (a resting boulder, a person leaning, snow, wind, water, a slow blade pressed in) pays continuously:

```
Hold drain = 0.3 J per second per newton held
Bubble area bleed = 0.1% of starting pool per second per 6.28 m² (disk: none)
```

The slow blade works through this rule. A 40 kg lean on a knife (392 N) drains 118 W. Roland's 100-mana bubble lasts 19 s against it, then the blade slides in.

## 2.4 Momentum goes to the caster

The shield stops the hit. The momentum still has to go somewhere. A held disk or worn bubble passes it to the caster as a shove (Part 5.3). Planting the shield into the ground (anchoring) sends it into the earth instead.

## 2.5 What passes the shell

| Thing | Passes? | Why |
|---|---|---|
| Still air, breath, breeze | Yes | Gas below ~10 m/s meets almost no drag |
| Smoke, poison gas, fine dust | Yes | Rides slow air |
| Gale and storm wind | Partly | Drag engages 20 to 85%; the rest blows through |
| Blast wind | Mostly no | Drag fully engaged at blast speeds |
| Rain, sparks, embers, water | No | Condensed matter |
| Arrows, balls, fragments | No | Drag kills speed |
| Slow hand or blade | Slowly | Only the tension floor and hold drain resist |
| Light, radiant heat | Yes | The shell ignores heat |
| Hot gas | Yes if unsealed | It is gas |

Sealing the shell (closing it to air) blocks smoke, gas and hot gas. The shell then carries the full push of wind and blast through hold drain. Occupants breathe trapped air.

## 2.6 Failure modes

| Mode | Trigger | Result |
|---|---|---|
| THROUGH | One hit needs more pool than remains | Attack passes whole; shield collapses |
| WORN DOWN | Many small hits spend the pool | Shield fails on the hit that exceeds what is left |
| DRAINED | Hold drain empties the pool | Load sinks through slowly |
| KNOCKBACK | Shield holds; momentum hits the caster | Caster shoved, thrown or killed while the shield is intact |

---

# Part 3. Reference Pools

## 3.1 Casters

| Caster | Skill factor | INT factor | Disk J per mana | Bubble J per mana | 100-mana disk | 100-mana bubble | Mana pool (INT x 10) |
|---|---|---|---|---|---|---|---|
| Fledgling (INT 15, Shield 1) | 0.300 | 1.000 | 3.0 | 0.5 | 300 J | 54 J | 150 + 4 x WIL |
| Apprentice (INT 40, Shield 2) | 1.000 | 2.192 | 21.9 | 3.9 | 2.2 kJ | 391 J | 400 + 4 x WIL |
| Journeyman (INT 73, Shield 3) | 1.286 | 3.546 | 45.6 | 8.1 | 4.6 kJ | 813 J | 730 + 4 x WIL |
| Roland (INT 137, Shield 6) | 2.143 | 5.868 | 125.7 | 22.4 | 12.6 kJ | 2.2 kJ | 1,370 + 4 x WIL |
| Veteran (INT 200, Shield 7) | 2.429 | 7.942 | 192.9 | 34.4 | 19.3 kJ | 3.4 kJ | 2,000 + 4 x WIL |
| Top tier (INT 1000, Shield 9) | 3.000 | 28.782 | 863.5 | 154.1 | 86.3 kJ | 15.4 kJ | 10,000 + 4 x WIL |

Notes' values (×20 form) are double these at 45°: Roland's 25 kJ disk and 4.5 kJ bubble.

## 3.2 Shape and size

| Shield | Face area | Shape factor | Fledgling J/mana | Roland J/mana | Top-tier J/mana | Roland mana per arrow | Roland mana per musket ball | Roland mana per trebuchet stone | Highest rune J/mana | Highest rune mana per arrow | Highest rune mana per trebuchet stone |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Focused disk | 0.2 m² | 1.0000 | 3.00 | 125.7 | 863.5 | 0.9 | 12 | 1,120 | 10.000 | 11 | 14,086 |
| Tower-shield plate | 0.6 m² | 0.5774 | 1.73 | 72.6 | 498.5 | 1.5 | 20 | 1,940 | 5.774 | 19 | 24,399 |
| Body plate | 1.0 m² | 0.4472 | 1.34 | 56.2 | 386.2 | 1.9 | 26 | 2,505 | 4.472 | 24 | 31,498 |
| Body bubble, 1 m hemisphere | 6.3 m² | 0.1784 | 0.54 | 22.4 | 154.1 | 4.9 | 65 | 6,279 | 1.784 | 61 | 78,955 |
| Full sphere, 1 m | 12.6 m² | 0.1262 | 0.38 | 15.9 | 108.9 | 6.9 | 92 | 8,880 | 1.262 | 86 | 111,659 |
| Squad dome, 1.5 m | 14.1 m² | 0.1189 | 0.36 | 15.0 | 102.7 | 7.3 | 98 | 9,418 | 1.189 | 92 | 118,432 |
| House dome, 4 m | 100.5 m² | 0.0446 | 0.13 | 5.6 | 38.5 | 19.4 | 260 | 25,115 | 0.446 | 244 | 315,819 |
| Hall dome, 10 m | 628.3 m² | 0.0178 | 0.05 | 2.2 | 15.4 | 48.6 | 651 | 62,789 | 0.178 | 611 | 789,546 |
| Block dome, 25 m | 3,927.0 m² | 0.0071 | 0.02 | 0.9 | 6.2 | 121.5 | 1,627 | 156,972 | 0.071 | 1,528 | 1,973,866 |

Rune columns use the rune path (10 × quality × shape), so skill and INT give no help. A house dome on highest-quality runes needs about 245 mana per arrow it stops.

## 3.3 Angle

| Glancing angle | Fraction taken | Capacity multiplier |
|---|---|---|
| 90° (head-on) | 100% | 1x |
| 60° | 75% | 1.3x |
| 45° | 50% | 2x |
| 30° | 25% | 4x |
| 20° | 11.7% | 8.5x |
| 15° | 6.7% | 15x |
| 10° | 3.0% | 33x |
| 5° | 0.8% | 132x |

The notes' deflection example checks out: a 1 kJ, 200 kg·m/s strike (20 kg at 10 m/s) turned by 20° costs sin²(20°) × 1 kJ = 117 J. With grip, a mundane 10 m/s strike costs 117 ÷ 0.247 = 474 J of pool. A skill strike costs the 117 J.

## 3.4 Ambient and overcharge

* Ambient 4× mana thickness = 2× output; 9× = 3×. Dungeons, spiritual sites and altitude raise it.
* Overcharge scales the pool linearly. Roland's scream overcharge to 150 to 200 mana gives a 3.4 to 4.5 kJ bubble head-on.

---

# Part 4. Mage Combat

Same caster attacking and defending: spell energy and shield pool use the same skill × INT × ambient multiplier, so mana trades directly.

| Attack (same caster) | Attack mana | Attack energy | Disk mana to stop, head-on | Disk mana at 45° | Bubble mana to stop |
|---|---|---|---|---|---|
| Mana Bolt | 25 | 3.1 kJ (Roland) | 25 | 12.5 | 140 |
| Mana Arrow | 50 | 6.3 kJ (Roland) | 50 | 25 | 280 |
| Overcharged Arrow | 100 | 12.6 kJ (Roland) | 100 | 50 | 560 |
| Heavy spell | 150 | 18.9 kJ (Roland) | 150 | 75 | 841 |

* A head-on disk trades 1:1 with the attacker's mana. Angled at 45° it trades 2:1 in the defender's favor.
* A bubble needs 5.6 times the attacker's mana. Bubbles are for surprise and all-around cover, not for dueling.
* Different casters: multiply by the ratio of their skill × INT factors. Roland's factor (12.6) is 5.7 times an INT 40 apprentice's (2.2); his 25-mana Bolt equals that apprentice's 143-mana disk.

---

# Part 5. Weapons

## 5.1 Projectiles

| Threat | Mass | Speed | KE | Grip | Pool needed (head-on) | Fledgling disk | Roland bubble | Roland disk | Top-tier bubble | Top-tier disk | Roland disk mana | Roland bubble mana |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sling bullet | 50 g | 35 m/s | 31 J | 54.7% | 56 J | HOLD | HOLD | HOLD | HOLD | HOLD | 0.4 | 2.5 |
| War arrow (bodkin) | 60 g | 50 m/s | 75 J | 68.8% | 109 J | HOLD | HOLD | HOLD | HOLD | HOLD | 0.9 | 4.9 |
| Heavy crossbow bolt | 80 g | 50 m/s | 100 J | 68.8% | 145 J | HOLD | HOLD | HOLD | HOLD | HOLD | 1.2 | 6.5 |
| Javelin | 800 g | 30 m/s | 360 J | 48.8% | 738 J | THROUGH | HOLD | HOLD | HOLD | HOLD | 5.9 | 33 |
| Pilum | 900 g | 25 m/s | 281 J | 42.5% | 662 J | THROUGH | HOLD | HOLD | HOLD | HOLD | 5.3 | 30 |
| Ballista bolt | 1 kg | 60 m/s | 1.8 kJ | 75.4% | 2.4 kJ | THROUGH | THROUGH | HOLD | HOLD | HOLD | 19 | 106 |
| Onager stone | 25 kg | 30 m/s | 11.2 kJ | 48.8% | 23.1 kJ | THROUGH | THROUGH | THROUGH | THROUGH | HOLD | 183 | 1,028 |
| Trebuchet stone | 90 kg | 45 m/s | 91.1 kJ | 64.7% | 140.9 kJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | 1,120 | 6,279 |
| Pistol ball | 15 g | 250 m/s | 469 J | 98.0% | 478 J | THROUGH | HOLD | HOLD | HOLD | HOLD | 3.8 | 21 |
| Musket ball .69 | 32 g | 300 m/s | 1.4 kJ | 98.6% | 1.5 kJ | THROUGH | HOLD | HOLD | HOLD | HOLD | 12 | 65 |
| Rifle (.303 / 7.92 class) | 10.5 g | 800 m/s | 3.4 kJ | 99.8% | 3.4 kJ | THROUGH | THROUGH | HOLD | HOLD | HOLD | 27 | 150 |
| Heavy rifle (.50 BMG class) | 42 g | 890 m/s | 16.6 kJ | 99.8% | 16.7 kJ | THROUGH | THROUGH | THROUGH | THROUGH | HOLD | 132 | 743 |
| Cannonball, 6 lb | 3 kg | 450 m/s | 273.4 kJ | 99.4% | 275.1 kJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | 2,188 | 12,262 |
| Grenade fragment | 2 g | 1200 m/s | 1.4 kJ | 99.9% | 1.4 kJ | THROUGH | HOLD | HOLD | HOLD | HOLD | 11 | 64 |

## 5.2 Wear: hits per 100-mana cast

| Threat | Pool spent per hit | Roland disk (12.6 kJ) | Roland bubble (2.2 kJ) | Top-tier bubble (15.4 kJ) |
|---|---|---|---|---|
| War arrow | 109 J | 115 | 20 | 141 |
| Crossbow bolt | 145 J | 86 | 15 | 105 |
| Sword cut | 1.1 kJ | 11 | 1 | 13 |
| Pistol ball | 478 J | 26 | 4 | 32 |
| Musket ball | 1.5 kJ | 8 | 1 | 10 |
| Rifle | 3.4 kJ | 3 | 0 | 4 |
| Grenade fragment | 1.4 kJ | 8 | 1 | 10 |

Sustained fire against one cast:

| Fire source | Pool drain | Roland disk lasts | Roland bubble lasts | Top-tier bubble lasts |
|---|---|---|---|---|
| 10 archers, 6 arrows/min each | 109 W | 115.3 s | 20.6 s | 141.3 s |
| 50 archers, 6 arrows/min each | 545 W | 23.1 s | 4.1 s | 28.3 s |
| 10 muskets, 3 rounds/min each | 730 W | 17.2 s | 3.1 s | 21.1 s |
| 10 rifles, 15 rounds/min each | 8.4 kW | 1.5 s | 0.3 s | 1.8 s |
| Machine gun, 500 rounds/min | 28.0 kW | 0.4 s | 0.1 s | 0.5 s |

Archers barely trouble a disk. Firearms in numbers strip any shield in seconds; personal firearms are niche on Terra, which is part of why shields still rule the battlefield.

## 5.3 Knockback on the caster (85 kg)

| Hit stopped on a held shield | Momentum | Caster Δv (85 kg) | Like falling |
|---|---|---|---|
| War arrow | 3.0 N·s | 0.04 m/s | 0.00 m |
| Musket ball | 9.6 N·s | 0.11 m/s | 0.00 m |
| Rifle | 8.4 N·s | 0.10 m/s | 0.00 m |
| Sword cut | 45.0 N·s | 0.53 m/s | 0.01 m |
| Two-hand maul | 120.0 N·s | 1.41 m/s | 0.10 m |
| Notes deflection example (20 kg, 10 m/s) | 200.0 N·s | 2.35 m/s | 0.28 m |
| Couched lance | 720.0 N·s | 8.47 m/s | 3.66 m |
| Wereboar charge | 1,200.0 N·s | 14.12 m/s | 10.16 m |
| Charging horse | 5,000.0 N·s | 58.82 m/s | 176.36 m |
| Cannonball, 6 lb | 1,215.0 N·s | 14.29 m/s | 10.41 m |
| Trebuchet stone | 4,050.0 N·s | 47.65 m/s | 115.71 m |

A held shield that stops a lance, a wereboar or a cannonball still flings the caster like a long fall. Anchoring the shield into the ground, or deflecting, is the only safe answer to heavy momentum.

## 5.4 Melee and beasts

| Threat | Mass | Speed | KE | Grip | Pool needed (head-on) | Fledgling disk | Roland bubble | Roland disk | Top-tier bubble | Top-tier disk | Roland disk mana | Roland bubble mana |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Punch | 3 kg | 10 m/s | 150 J | 24.7% | 607 J | THROUGH | HOLD | HOLD | HOLD | HOLD | 4.8 | 27 |
| Kick | 8 kg | 10 m/s | 400 J | 24.7% | 1.6 kJ | THROUGH | HOLD | HOLD | HOLD | HOLD | 13 | 72 |
| Dagger thrust | 2 kg | 6 m/s | 36 J | 21.8% | 165 J | HOLD | HOLD | HOLD | HOLD | HOLD | 1.3 | 7.4 |
| Slow knife press | 40 kg | 1 m/s | 20 J | 20.0% | 100 J | HOLD | HOLD | HOLD | HOLD | HOLD | 0.8 | 4.4 |
| Arming sword cut | 3 kg | 15 m/s | 338 J | 29.9% | 1.1 kJ | THROUGH | HOLD | HOLD | HOLD | HOLD | 9.0 | 50 |
| Longsword thrust | 4 kg | 8 m/s | 128 J | 23.1% | 555 J | THROUGH | HOLD | HOLD | HOLD | HOLD | 4.4 | 25 |
| Battle axe | 5 kg | 15 m/s | 562 J | 29.9% | 1.9 kJ | THROUGH | HOLD | HOLD | HOLD | HOLD | 15 | 84 |
| Warhammer spike | 4 kg | 15 m/s | 450 J | 29.9% | 1.5 kJ | THROUGH | HOLD | HOLD | HOLD | HOLD | 12 | 67 |
| Two-hand maul | 10 kg | 12 m/s | 720 J | 26.6% | 2.7 kJ | THROUGH | THROUGH | HOLD | HOLD | HOLD | 22 | 121 |
| Bayonet lunge | 15 kg | 5 m/s | 188 J | 21.2% | 883 J | THROUGH | HOLD | HOLD | HOLD | HOLD | 7.0 | 39 |
| Couched lance | 80 kg | 9 m/s | 3.2 kJ | 23.9% | 13.6 kJ | THROUGH | THROUGH | THROUGH | HOLD | HOLD | 108 | 605 |
| Bear swipe | 25 kg | 10 m/s | 1.2 kJ | 24.7% | 5.1 kJ | THROUGH | THROUGH | HOLD | HOLD | HOLD | 40 | 226 |
| Wereboar charge | 150 kg | 8 m/s | 4.8 kJ | 23.1% | 20.8 kJ | THROUGH | THROUGH | THROUGH | THROUGH | HOLD | 165 | 927 |
| Charging horse | 500 kg | 10 m/s | 25.0 kJ | 24.7% | 101.2 kJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | 805 | 4,510 |
| Charging bull (horns) | 700 kg | 8 m/s | 22.4 kJ | 23.1% | 97.1 kJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | 772 | 4,327 |
| Battering ram, crewed | 600 kg | 4 m/s | 4.8 kJ | 20.8% | 23.1 kJ | THROUGH | THROUGH | THROUGH | THROUGH | HOLD | 184 | 1,029 |
| Loaded wagon | 2 t | 5 m/s | 25.0 kJ | 21.2% | 117.8 kJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | 936 | 5,249 |
| Steam locomotive 100 t | 100 t | 8.3 m/s | 3.4 MJ | 23.3% | 14.8 MJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | 117,552 | 658,879 |

The slow knife press holds at first contact (100 J of pool). It wins through hold drain over the next 19 s against a Roland bubble.

---

# Part 6. Heavy Things

## 6.1 Boulders

The last two columns show how long the remaining pool holds the boulder's weight after catching it.

| Boulder | Mass | Case | KE | Grip | Pool needed | Fledgling disk | Roland bubble | Roland disk | Top-tier bubble | Top-tier disk | Roland disk holds it for | Roland bubble holds it for |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.3 m granite | 38 kg | resting | 0 J | - | 0 J | HOLD | HOLD | HOLD | HOLD | HOLD | 111.9 s | 20.0 s |
| 0.3 m granite | 38 kg | dropped 2 m | 749 J | 21.9% | 3.4 kJ | THROUGH | THROUGH | HOLD | HOLD | HOLD | 81.5 s | - |
| 0.3 m granite | 38 kg | dropped 10 m | 3.7 kJ | 28.7% | 13.0 kJ | THROUGH | THROUGH | THROUGH | HOLD | HOLD | - | - |
| 0.3 m granite | 38 kg | rockslide 15 m/s | 4.3 kJ | 29.9% | 14.4 kJ | THROUGH | THROUGH | THROUGH | HOLD | HOLD | - | - |
| 0.5 m granite | 177 kg | resting | 0 J | - | 0 J | HOLD | HOLD | HOLD | HOLD | HOLD | 24.2 s | 4.3 s |
| 0.5 m granite | 177 kg | dropped 2 m | 3.5 kJ | 21.9% | 15.8 kJ | THROUGH | THROUGH | THROUGH | THROUGH | HOLD | - | - |
| 0.5 m granite | 177 kg | dropped 10 m | 17.3 kJ | 28.7% | 60.3 kJ | THROUGH | THROUGH | THROUGH | THROUGH | HOLD | - | - |
| 0.5 m granite | 177 kg | rockslide 15 m/s | 19.9 kJ | 29.9% | 66.6 kJ | THROUGH | THROUGH | THROUGH | THROUGH | HOLD | - | - |
| 1.0 m granite | 1,414 kg | resting | 0 J | - | 0 J | HOLD | HOLD | HOLD | HOLD | HOLD | 3.0 s | 0.5 s |
| 1.0 m granite | 1,414 kg | dropped 2 m | 27.7 kJ | 21.9% | 126.6 kJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | - | - |
| 1.0 m granite | 1,414 kg | dropped 10 m | 138.7 kJ | 28.7% | 482.6 kJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | - | - |
| 1.0 m granite | 1,414 kg | rockslide 15 m/s | 159.0 kJ | 29.9% | 532.6 kJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | - | - |
| 2.0 m granite | 11,310 kg | resting | 0 J | - | 0 J | HOLD | HOLD | HOLD | HOLD | HOLD | 0.4 s | 0.1 s |
| 2.0 m granite | 11,310 kg | dropped 2 m | 221.9 kJ | 21.9% | 1.0 MJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | - | - |
| 2.0 m granite | 11,310 kg | dropped 10 m | 1.1 MJ | 28.7% | 3.9 MJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | - | - |
| 2.0 m granite | 11,310 kg | rockslide 15 m/s | 1.3 MJ | 29.9% | 4.3 MJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | - | - |
| 3.0 m granite | 38,170 kg | resting | 0 J | - | 0 J | HOLD | HOLD | HOLD | HOLD | HOLD | 0.1 s | 0.0 s |
| 3.0 m granite | 38,170 kg | dropped 2 m | 748.9 kJ | 21.9% | 3.4 MJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | - | - |
| 3.0 m granite | 38,170 kg | dropped 10 m | 3.7 MJ | 28.7% | 13.0 MJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | - | - |
| 3.0 m granite | 38,170 kg | rockslide 15 m/s | 4.3 MJ | 29.9% | 14.4 MJ | THROUGH | THROUGH | THROUGH | THROUGH | THROUGH | - | - |

Why boulders break shields: a falling boulder moves at 6 to 15 m/s, where grip is 22 to 30%. A 1 m boulder dropped 2 m carries 28 kJ and needs 127 kJ of pool. Even a stopped boulder then empties the shield through hold drain in seconds.

## 6.2 Buildings and snow on a 1 m bubble

Weight is the load over the bubble's 3.14 m² footprint.

| Load on a 1 m bubble | Areal mass | Weight on bubble | Hold drain | Roland bubble (2.2 kJ) lasts | Top-tier bubble (15.4 kJ) lasts | Collapse drop | Pool needed to catch the drop |
|---|---|---|---|---|---|---|---|
| 1 m dry snow | 150 kg/m² | 4.6 kN | 1.4 kW | 1.6 s | 11.1 s | - | - |
| 1 m wet snow | 400 kg/m² | 12.3 kN | 3.7 kW | 0.6 s | 4.2 s | - | - |
| Timber roof + ceiling | 250 kg/m² | 7.7 kN | 2.3 kW | 1.0 s | 6.7 s | 3 m | 101.2 kJ |
| Timber house, 1 story | 350 kg/m² | 10.8 kN | 3.2 kW | 0.7 s | 4.8 s | 3 m | 141.7 kJ |
| Brick house, 1 story | 800 kg/m² | 24.7 kN | 7.4 kW | 0.3 s | 2.1 s | 3 m | 323.9 kJ |
| Concrete slab | 1,000 kg/m² | 30.8 kN | 9.2 kW | 0.2 s | 1.7 s | 3 m | 404.8 kJ |
| 3-story brick | 2,400 kg/m² | 74.0 kN | 22.2 kW | 0.1 s | 0.7 s | 3 m | 971.6 kJ |

No story-scale shield holds up a building. A collapsing roof needs 100+ kJ to catch and then drains any bubble in seconds. Shields buy the second it takes to dive clear.

---

# Part 7. Explosions

## 7.1 Blast

Blast load: Kinney-Graham overpressure and impulse (surface burst), converted to the energy of the blast wind stopped on the face. Disk faces the blast (0.2 m²). Bubble catches its 3.14 m² cross-section.

| Charge (TNT eq.) | Distance to face | Overpressure | Blast wind | Engaged | Disk needs | Bubble needs | Roland disk (12.6 kJ) | Roland bubble (2.2 kJ) | Top-tier bubble (15.4 kJ) |
|---|---|---|---|---|---|---|---|---|---|
| 0.1 kg grenade | 1 m | 276 kPa | 362 m/s | 99% | 1.9 kJ | 30.0 kJ | HOLD | THROUGH | THROUGH |
| 0.1 kg grenade | 2 m | 58 kPa | 113 m/s | 89% | 336 J | 5.3 kJ | HOLD | THROUGH | HOLD |
| 0.1 kg grenade | 3 m | 26 kPa | 57 m/s | 67% | 107 J | 1.7 kJ | HOLD | HOLD | HOLD |
| 0.1 kg grenade | 5 m | 12 kPa | 27 m/s | 31% | 23 J | 366 J | HOLD | HOLD | HOLD |
| 0.1 kg grenade | 10 m | 5 kPa | 12 m/s | 8% | 2 J | 35 J | HOLD | HOLD | HOLD |
| 1 kg satchel | 1 m | 1,528 kPa | 981 m/s | 100% | 14.5 kJ | 227.4 kJ | THROUGH | THROUGH | THROUGH |
| 1 kg satchel | 2 m | 328 kPa | 405 m/s | 99% | 4.8 kJ | 75.3 kJ | HOLD | THROUGH | THROUGH |
| 1 kg satchel | 3 m | 128 kPa | 213 m/s | 97% | 1.9 kJ | 29.8 kJ | HOLD | THROUGH | THROUGH |
| 1 kg satchel | 5 m | 42 kPa | 87 m/s | 83% | 478 J | 7.5 kJ | HOLD | THROUGH | HOLD |
| 1 kg satchel | 10 m | 13 kPa | 30 m/s | 36% | 63 J | 993 J | HOLD | HOLD | HOLD |
| 7 kg shell fill | 1 m | 5,219 kPa | 1,862 m/s | 100% | 56.7 kJ | 890.1 kJ | THROUGH | THROUGH | THROUGH |
| 7 kg shell fill | 2 m | 1,393 kPa | 934 m/s | 100% | 26.2 kJ | 411.0 kJ | THROUGH | THROUGH | THROUGH |
| 7 kg shell fill | 3 m | 574 kPa | 569 m/s | 100% | 14.4 kJ | 226.1 kJ | THROUGH | THROUGH | THROUGH |
| 7 kg shell fill | 5 m | 176 kPa | 267 m/s | 98% | 5.1 kJ | 79.9 kJ | HOLD | THROUGH | THROUGH |
| 7 kg shell fill | 10 m | 39 kPa | 81 m/s | 80% | 807 J | 12.7 kJ | HOLD | THROUGH | HOLD |

The disk takes a small slice of the blast; the bubble takes the whole cross-section. Against explosives, a disk turned toward the charge beats a bubble whose cross-section is 16 times larger.

## 7.2 Fragments

Assumed grenade: 300 fragments of 2 g at 1,200 m/s (1.4 kJ each, each one a whole attack).

| Distance | Fragments into 1 m bubble | Fragment energy into bubble | Fragments into facing disk | Energy into disk |
|---|---|---|---|---|
| 2 m | 18.8 | 27.0 kJ | 1.19 | 1.7 kJ |
| 3 m | 8.3 | 12.0 kJ | 0.53 | 764 J |
| 5 m | 3.0 | 4.3 kJ | 0.19 | 275 J |
| 10 m | 0.8 | 1.1 kJ | 0.05 | 69 J |
| 20 m | 0.2 | 270 J | 0.01 | 17 J |

At 3 m a grenade puts about 8 fragments (12 kJ) into a Roland bubble that can stop one. The disk sees half a fragment.

## 7.3 Explosive spells

Skill and spell blasts are exempt from grip. A Blast fill meets the full pool. Canon makes explosive magic cost-effective through superimposed mana, so a blast spell is the efficient way to break a shield of equal mana.

---

# Part 8. Fire, Heat and Air

## 8.1 Fire

| Threat | Result |
|---|---|
| Fire spell, flame jet | Blocked as an attack; fire spells are ignition sources |
| Burning fuel splashed on the shield | Blocked, then clings and burns on the outer surface on its own energy |
| Hot smoke and combustion gas, unsealed | Diffuses in with the air |
| Radiant heat | Passes through untouched |

## 8.2 Radiant heat through the shell

| Radiant flux | Effect on bare skin |
|---|---|
| 1.6 kW/m² | Tolerable indefinitely |
| ~4 to 5 kW/m² | Pain in 15 to 20 s |
| ~10 kW/m² | Blistering in seconds |
| 12.5 kW/m² | Wood ignites with a pilot flame |
| Tens to 100+ kW/m² | Flame surface of a large fire |

Burning pitch or oil coating a bubble sits within a meter of the caster. The shield is untouched; the caster cooks. Fire that sticks is a shield-breaker's tool. (Terra has no petroleum; pitch, tallow, plant oils and fats fill the role.)

## 8.3 Sealed air supply

| Space | Volume | One person at rest | One person at hard exertion |
|---|---|---|---|
| 1 m bubble (hemisphere) | ~2.0 m³ | ~4 h | ~1 h |
| 1 m full sphere | ~4.1 m³ | ~8 h | ~2 h |
| 4 m house dome | ~134 m³ | ~11 days; 20 people ~13 h | ~2.8 days |

Time to 3% CO₂ (heavy breathing, headache). Rest 0.25 L/min CO₂, hard work ~1 L/min.

---

# Part 9. Weather and Water

## 9.1 Wind on a 1 m bubble (unsealed)

| Wind | Speed | Engaged | Push on 1 m bubble | Hold drain | Roland bubble lasts | Top-tier bubble lasts | Breeze inside |
|---|---|---|---|---|---|---|---|
| Breeze | 5 m/s | 2% | 0 N | 0 W | 337 min | 2,313 min | 5 m/s |
| Gale | 20 m/s | 20% | 77 N | 23 W | 97 s | 11 min | 18 m/s |
| Category 1 hurricane | 33 m/s | 40% | 424 N | 127 W | 18 s | 121 s | 25 m/s |
| Category 3 hurricane | 50 m/s | 61% | 1,467 N | 440 W | 5 s | 35 s | 31 m/s |
| Category 5 hurricane | 70 m/s | 75% | 3,554 N | 1,066 W | 2 s | 14 s | 35 m/s |
| EF5 tornado | 90 m/s | 84% | 6,508 N | 1,952 W | 1 s | 8 s | 37 m/s |

Shields are poor storm shelters. Slow wind passes through; fast wind engages and drains the pool. A low wall or a cellar outlasts any bubble in a hurricane.

## 9.2 Water

Water is condensed matter: the shell blocks all of it and pays hold drain on the full push.

| Water | Push on 1 m bubble | Hold drain | Roland bubble lasts | Top-tier bubble lasts |
|---|---|---|---|---|
| River current 1 m/s | 0.8 kN | 0.24 kW | 9.5 s | 65.4 s |
| River current 2 m/s | 3.1 kN | 0.94 kW | 2.4 s | 16.3 s |
| Flash flood 5 m/s | 19.6 kN | 5.89 kW | 0.4 s | 2.6 s |
| Submerged, sealed (buoyancy of 2.1 m³) | 20.5 kN | 6.16 kW | 0.4 s | 2.5 s |

A Mana Shield does not make a diving bell. Underwater, buoyancy alone drains a Roland bubble in under a second.

---

# Part 10. Falling

## 10.1 Ordinary falls

The caster lands on a shield placed beneath. Pool is only half the problem; the shield's give sets the g-load.

| Fall | Impact speed | KE (85 kg) | Grip | Pool needed head-on | Roland disk mana head-on | Roland disk mana at 45° | Landing g over 0.15 m give |
|---|---|---|---|---|---|---|---|
| 3 m | 7.7 m/s | 2.5 kJ | 23% | 11.0 kJ | 87 | 44 | 20 g |
| 10 m | 14.0 m/s | 8.3 kJ | 29% | 29.0 kJ | 231 | 115 | 67 g |
| 30 m | 24.3 m/s | 25.0 kJ | 42% | 60.3 kJ | 479 | 240 | 200 g |
| Terminal velocity (skydiver) | 55.0 m/s | 128.6 kJ | 72% | 177.8 kJ | 1,414 | 707 | 1,028 g |

Above about 10 m, enough pool still means lethal deceleration unless the shield gives far more than 0.15 m. Flight magic and balloon buoyancy save fallers. A shield alone does not.

## 10.2 Falling from space (100 kg occupant, tight 1 m full-sphere hull)

What hits the shell on the way down:

1. **Ram pressure.** At hypersonic speed air piles into a shock ahead of the shell. Front-face pressure is ~1.84 × dynamic pressure.
2. **Shock-layer plasma.** Air through the shock is heated to roughly 6,000 to 8,000 K at orbital speed (7.8 km/s) and ~10,000 to 11,000 K at lunar-return speed (11 km/s). Radio-type sensing blacks out.
3. **Convective heating.** Hot gas scrubbing the surface. Blocked by a sealed shell.
4. **Radiative heating.** Shock-layer light. Negligible below ~9 km/s; serious at 11 km/s; lethal at meteoric speed. Passes the shell.
5. **Deceleration.** Every newton of drag is a newton held. Hold drain pays it and the occupant feels it.

**Hull mode (correct):** sealed shell, drag set to ignore air. Cost is hold drain on the drag force for the whole descent. **Catch mode (fatal):** the shell tries to stop the air itself and must absorb the occupant's entire kinetic energy (3 GJ from orbit).

| Scenario | Peak decel | Peak ram pressure | Total drag impulse | Hold cost, whole descent | Roland mana (15.9 J/mana) | Top-tier mana (108.9 J/mana) | Catch-mode energy |
|---|---|---|---|---|---|---|---|
| 39 km stratospheric jump | 1.4 g | 1.8 kPa | 439 kN·s | 132 kJ | 8,280 | 1,210 | 4.3 MJ |
| Drop from 100 km | 4.1 g | 5.0 kPa | 506 kN·s | 152 kJ | 9,560 | 1,400 | 44 MJ |
| Orbital entry, shallow (−1.5°) | 7.7 g | 9.4 kPa | 1,204 kN·s | 361 kJ | 22,700 | 3,320 | 3.1 GJ |
| Orbital entry, steep (−10°) | 26.8 g | 32.7 kPa | 1,196 kN·s | 359 kJ | 22,600 | 3,300 | 3.1 GJ |
| Lunar-return speed (11 km/s, −6.5°) | 20.0 g | 24.5 kPa | 1,520 kN·s | 456 kJ | 28,700 | 4,190 | 6.1 GJ |

Dropping the shell once subsonic below ~25 km cuts orbital cost to the entry burn alone: ~780 kN·s, 234 kJ, ~14,700 mana for Roland, ~2,150 for top tier. Ambient mana thickens with altitude, so the high-altitude part is cheaper than open-ground numbers show.

Occupant limits: ~4 to 6 g comfortable for minutes lying flat, ~15 g for seconds, John Stapp's 46.2 g sled run (1954) for a fraction of a second. Steep entry (26.8 g sustained) kills regardless of mana. Meteoric entry (700+ g) kills instantly.

Landing: terminal speed under a 1 m sphere is 33 m/s. Stopping 100 kg from 33 m/s needs ~104 kJ of pool (Roland disk ~830 mana head-on) and pulls ~370 g over 0.15 m of give. A 4 m bubble falls at 8.2 m/s but costs ~6,200 mana for Roland to hold through a 1 km descent (shape 0.045). Space falls are top-tier work.

Reference: Felix Baumgartner's 2012 jump from 39 km reached 1,357.6 km/h (377 m/s) in a streamlined suit. A 1 m shell's larger area holds the same jump to 293 m/s.

---

# Part 11. Layered Shields (Optional Technique)

The default Mana Shield is one shell. A caster can cast more than one at once. This is a separate technique with extra cost and complexity.

## 11.1 Cost

| Rule | Value |
|---|---|
| Each added shell | 1.5× the mana of the shell before it for the same pool |
| Two shells | 2.5× one cast |
| Three shells | 4.75× |
| Four shells | 8.1× |
| Concentration | Each shell held separately; losing focus drops the outermost first |
| Bleed | Each bubble bleeds on its own area |

## 11.2 Spaced versus bonded

**Bonded** (shells pressed together over the same face): pools add against one whole attack.

**Spaced** (gap between shells): each shell checks the whole attack on its own. Under the whole-attacks rule a failed outer shell passes the attack intact to the next. Spaced shells are never stronger per hit than bonded ones. They buy two things: **standoff** (a charge or impact fuze trips on the outer shell, so the inner shell sits farther from the blast) and **redundancy** (losing the outer shell leaves a live inner one).

Real analog: the Whipple shield on spacecraft and spaced armor on tanks.

## 11.3 When layering is worth it

Layering costs more mana than overcharging for the same pool (2.5× for double pool versus 2× by overcharge). It earns its cost only when:

* overcharge is capped below the pool needed;
* explosives threaten (spaced standoff);
* different shapes are needed at once: a bubble for all-around arrows plus a disk in front for the heavy hit. Roland: 100-mana bubble + 150-mana disk = 250 mana. In front, bonded, the pools add to 14.8 kJ: enough for a couched lance (13.6 kJ) that would break either alone.

---

# Part 12. Runes

## 12.1 Cost and host heat (shield for the 100-mana bill, 1 kJ useful)

| Quality | Mana paid | Input | Waste | Into host | Steel plate 200 g | Copper 200 g | Silver 200 g |
|---|---|---|---|---|---|---|---|
| Lowest 0.2 | 500 | 5 kJ | 4 kJ | 2 kJ | +22 °C | +26 °C | +43 °C |
| Low 0.4 | 250 | 2.5 kJ | 1.5 kJ | 750 J | +8 °C | +10 °C | +16 °C |
| Intermediate 0.6 | 167 | 1.67 kJ | 667 J | 333 J | +3.6 °C | +4.3 °C | +7.1 °C |
| High 0.8 | 125 | 1.25 kJ | 250 J | 125 J | +1.4 °C | +1.6 °C | +2.7 °C |
| Highest 1.0 | 100 | 1 kJ | 0 | 0 | none | none | none |

Per activation, before cooling. Ten fast activations on a lowest-grade silver plate add ~430 °C. Silver is the best conductor and the first to cook.

## 12.2 Lesser rune shield (1 kJ ceiling) against mundane threats

| Threat | Pool needed head-on | Head-on | At 45° | At 30° |
|---|---|---|---|---|
| Arrow | 109 J | HOLD | HOLD | HOLD |
| Pistol ball | 478 J | HOLD | HOLD | HOLD |
| Sword cut | 1.13 kJ | THROUGH | HOLD | HOLD |
| Musket ball | 1.46 kJ | THROUGH | HOLD | HOLD |
| Two-hand maul | 2.71 kJ | THROUGH | THROUGH | HOLD |
| Rifle | 3.4 kJ | THROUGH | THROUGH | HOLD |
| Couched lance | 13.6 kJ | THROUGH | THROUGH | THROUGH |

## 12.3 Town and house domes

Large domes run on runes and stored mana, not a single caster. From the shape table, a highest-quality 4 m house dome spends ~245 mana per arrow and ~316,000 mana per trebuchet stone. A 25 m block dome spends ~1,500 mana per arrow. Arrows across a whole siege add up to real mana-stone budgets; a single trebuchet stone is a city's reserve.

---

# Part 13. Counters

| Target | Best counter | Why |
|---|---|---|
| Any bubble | Grenade or satchel within 2 to 3 m | Bubble catches the whole blast cross-section |
| Any bubble | Two or three quick strikes | Wear: a Roland bubble stops one sword cut |
| Any bubble | Lean on it | Hold drain: 19 s for a 40 kg lean on Roland's bubble |
| Disk | Flank it | Disk covers the front only |
| Disk | Heavy momentum (lance, beast, ram) | Holds the hit, knocks the caster down or worse |
| Any shield | Falling weight: boulder, roof, beam | Grip ~22%; then hold drain |
| Any shield | Massed firearms | Wear in seconds |
| Any shield | Burning pitch that clings | Radiant heat passes |
| Any shield | Gas or smoke, unsealed | Passes with the air |
| Any shield | Flood or deep water | Hold drain on the full push |
| Any caster | Spell of equal mana against a bubble | Bubble needs 5.6× the mana |

---

# Part 14. Formula Reference

```
Body cast J            = mana × 10 × skill × (INT/15)^0.8 × √ambient
Rune J                 = mana × 10 × quality × √ambient
Skill factor           = 0.3 (L1), 1.0 + (L−2) × 2/7 (L2 to L9)
Pool (head-on)         = 10 × mana × skill × INT factor × shape × hold × √ambient
Shape                  = min(1, √(0.2 / face area))
Angle                  = hit × sin²(glancing angle)
Drag share             S(v) = v² / (v² + 40²)
Grip                   G(v) = 0.2 + 0.8 × S(v)   (skills, spells: G = 1)
Pool spent per hit     = hit taken ÷ G(v)
Hold drain             = 0.3 J/s per newton held
Bubble bleed           = 0.1% of starting pool per s per 6.28 m²
Knockback              = Δv_caster = m × v ÷ M_caster
Landing deceleration   = v² ÷ (2 × give)
Layering               = shell n costs 1.5^(n−1) × base mana
Rune waste             = (1 − quality) × input; half to host
```

---

# Part 15. Fix List

Items that change, clarify or extend the notes. Ordered by impact. **Status:** applied to `AttackScale.md`, `ManaCast.md`, and `Spells.md` (hold drain kept at **0.3 J/s per N**, not halved).

| # | Where | Issue | Fix | Status |
|---|---|---|---|---|
| 1 | `ManaCast.md`, `AttackScale.md` (pool formula) | The ×20 pool assumes a 45° face; the angle rule halves the hit again at 45°. Same angle counted twice | Write the pool as 10 × mana × … (head-on). Keep 45° = ×2 in the angle rule only | Applied |
| 2 | Chapter 14 | Under the notes as written, the 150 to 200 mana overcharged bubble (6.7 to 9.0 kJ) stops the whole 3 to 7 kJ Gale-Step tip; the pierce rests entirely on the detonation | With fix 1 the overcharged bubble is 3.4 to 4.5 kJ head-on and the tip pierces on its own. The disk still stops it. On-page detonation still stands | Applied |
| 3 | Mana Shield notes | "Bubble settles into a hard disk over the front" does not say at what angle | State the disk settles at 45° by default | Applied |
| 4 | `ManaCast.md` (shape) | Shape factor only given as two values (1.0, 0.18) | Write shape = min(1, √(0.2 / area)) | Applied |
| 5 | `AttackScale.md` | Energy-only rule cannot explain shields failing to boulders, rams and slow blades | Add grip G(v); skills and spells at G = 1 | Applied |
| 6 | `ManaCast.md` (hold) | "Holding a bubble bleeds it" has no rate; "hold" appears in the pool formula undefined | Bleed 0.1% of starting pool per s per 6.28 m². Hold drain 0.3 J/s per N | Applied |
| 7 | Same | Hold drain constant sets weather, water and space costs | Kept **0.3** (storms / water deadly to shields). Halve later only if story needs gale-proof bubbles | Kept 0.3 |
| 8 | Whole-attacks rule | Undefined: what a failed shield does to the attack; whether a stopped attack spends pool | Stopped hit spends Hit÷G; failed shield collapses; attack passes whole | Applied |
| 9 | Overcharge | No cap stated | Soft street cap ~2× baseline (scream band) | Applied |
| 10 | Layering | Not in notes | Optional technique in ManaCast / ManaShield Part 11 | Applied |
| 11 | Shield give | No stopping distance for the shell | Disk ~0.05 m, bubble ~0.15 m | Applied |
| 12 | Momentum | Notes do not say where blocked momentum goes | Held → caster; anchored → ground | Applied |
| 13 | Selectivity | Notes do not say what passes a shield | Air/gas/heat pass; matter/water blocked; sealing optional | Applied |
| 14 | Altitude canon | "Shield costs the same at any altitude" reads as conflicting with the ambient factor | Mana paid same; output × √ambient | Applied |
| 15 | Bubble area | 6.28 m² is a 1 m hemisphere. Airborne / underwater needs a full sphere | Full sphere 12.57 m², shape 0.126 | Applied |
| 16 | Chapter 27 elemental faces | Wall faces need a size-based cost | Door-sized ~6 m² → shape ~0.18 | Applied |
| 17 | Runes | Lowest-quality runes dump heat into the host; silver cooks fastest | Already covered by rune waste law in `Energy.md` / ManaCast Part 12 of this file | No new rule |
| 18 | Explosive canon | Blast fills meet shields at full pool (spell) | Explosive spells ignore grip (G = 1) | Applied |
