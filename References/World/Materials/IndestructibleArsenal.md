# The Indestructible Arsenal: Weapons and Armor From an Unbreakable Metal

Design loot / invent scenario. Not locked law. The material: a metal that cannot break, bend, flex, dent, wear, melt, chip or dull. It holds any shape it was made in forever. Density is set to steel (7.85 g/cm³) unless stated. It conducts heat and electricity like steel.

**Companions:** Perfectly rigid lock (= adamantium): `MaterialConsiderations.md`, `Metals.md`. Rigid hair filament physics: `UnbreakableHair.md`. Friction on no-bend stock: `../Science/Energy/FrictionNotes.md`. Flywheel energy: `../Science/Energy/FlywheelStorage.md`. Kinetic / projectiles: `../Science/Energy/Kinetic.md`, `../Science/Energy/Projectiles.md`. Light kit when plate fails: `../../Combat/LightArmorLoadout.md`. Hub: `Index.md`.

---

## 1. The Ground Rules

What indestructibility **changes**:

| Property | Consequence |
|---|---|
| Unlimited strength | Thinness is free. A blade or plate can be as thin as a hair and lose nothing. |
| Unlimited stiffness | No buckling. A 1 m needle 75 µm wide stays perfectly straight under any end load. |
| Edge never dulls | Edge radius can be made near atomic scale (≈ 1 nm) and stays there through any use. |
| No erosion | Projectiles keep 100 percent of their energy for the target. |
| No self-damage | Every joule goes outward. |

What indestructibility **does not change**:

| Physics that still applies | Consequence |
|---|---|
| **Momentum** | A hit on unbreakable armor still shoves the wearer. Big enough hits kill through acceleration alone. |
| **Heat** | It does not melt. It does conduct. Fire on the outside cooks the inside. |
| **Electricity** | It conducts. This is good (Faraday cage) or bad (contact shocks) depending on design. |
| **Mass** | Thin parts weigh almost nothing. A weightless weapon has no momentum of its own. Muscle or machines must supply all the force. |
| **Anchors and joints** | The weakest part of any indestructible system is whatever ordinary material holds it: the hand, the hinge, the bolt, the ground. |
| **No flex at all** | Springs, bows, whips and rope are impossible as solid pieces. Flexibility only comes from articulation: links, hinges, scales. |

---

## 2. The Physics Toolkit

### 2.1 Cutting cost scales with thickness, not sharpness
Once the edge is effectively perfect, the energy to cut is the energy to shove the blade's **body** through the gap it makes:

**Energy per square meter of cut surface = R × t**
R = material flow resistance, t = blade thickness.

| Blade thickness | Severing a human neck | Cutting 30 cm of 2 mm hardened plate | Cutting 1 m² of 70 mm tank armor |
|---|---|---|---|
| 10 µm (thinner than plastic wrap) | 11 J | 18 J | 40 kJ |
| 50 µm (a sheet of paper is about 100 µm) | 56 J | 90 J | 200 kJ |
| 75 µm (a hair) | 83 J | 135 J | 300 kJ |
| 300 µm | 334 J | 540 J | 1.2 MJ |
| 1 mm | 1,100 J | 1,800 J | 4 MJ |

Human swing energy reference:
- One-handed sword cut: 60 to 130 J
- Two-handed cut: 150 to 250 J
- Full-body axe swing: 200 to 400 J

**Rule:** any indestructible blade under about 50 µm thick cuts through a medieval breastplate in a single ordinary swing.

### 2.2 Edge pressure
A 1 nm edge radius pressed with 1 N per millimeter of edge produces about 1,000 GPa of contact stress before the target yields. Every known material yields at the edge instantly. Sharpness stops being a variable. Only thickness and force matter.

### 2.3 Momentum through armor
Velocity change for an 80 kg wearer fully stopping a projectile (rigid shell, no penetration). Bounce-back can double these.

| Projectile | Momentum | Wearer Δv | Outcome inside unbreakable armor |
|---|---|---|---|
| 9 mm pistol | 2.8 N·s | 0.035 m/s | A tap |
| 5.56 NATO | 3.8 N·s | 0.047 m/s | A tap |
| 7.62 × 51 | 8.1 N·s | 0.10 m/s | A firm poke |
| .50 BMG | 41 N·s | 0.51 m/s | A hard shove |
| 20 mm cannon | 100 N·s | 1.25 m/s | Knocked off feet |
| 30 mm GAU-8 round | 425 N·s | 5.3 m/s | Thrown several meters. A burst is a beating. |
| Full-auto GAU-8, 1 second (≈ 65 rounds) | ≈ 27,600 N·s | Far beyond survivable | Launched at highway speed and beyond |
| 120 mm APFSDS | ≈ 7,600 N·s | 95 m/s | Killed by acceleration: thousands of g |
| 155 mm shell (inert) | ≈ 34,400 N·s | 430 m/s | Pulped inside an intact suit |

With 2 cm of padding, peak acceleration ≈ Δv² / (2 × 0.02 m). At 5.3 m/s that is about 72 g for a few milliseconds: survivable. At 95 m/s it is about 23,000 g.

---

## 3. Blades

### 3.1 The Hair Rapier (Filament Estoc)
**Build:** A single 75 µm filament, 1 m long, set in a heavy steel collet hilt with a full cup guard.

| Stat | Value |
|---|---|
| Blade mass | 0.035 g |
| Total weapon mass | 0.6 to 0.9 kg (all hilt) |
| Tip force to pierce any plate armor ever made | under 20 N |
| Tip force to pierce a Level IV ceramic plate | about 141 N |
| Visibility | Invisible past arm's length |

**The thrust:** Passes through any armor, any shield, any helmet, any door with a fencer's lunge. Leaves a 75 µm pinhole. Against flesh it is acupuncture. A heart thrust does nothing measurable. The rapier's thrust is only lethal when aimed at a target that dies from a pinhole: a phone battery, a pacemaker, a pressure suit, an insulin pump, an implanted chip.

**The cut:** Where it becomes horrifying. A draw cut within 10 to 20 cm of the guard delivers the 83 J needed to sever a neck. Leverage is the limit:

| Contact point from guard | Max cutting force (60 N·m wrist) | What it cuts in one draw |
|---|---|---|---|
| 5 cm | 1,200 N | Limbs through bone, sword blades, mail, thin plate |
| 15 cm | 400 N | Neck, wrist, unarmored limbs |
| 50 cm | 120 N | Flesh 4 to 8 cm deep |
| 100 cm (tip) | 60 N | Skin, shallow cut, clothing |

**The parry:** An opponent's steel sword striking the filament near the guard is cut. Edge-on contact starts at about 1 mm of blade thickness, needing roughly 300 N to begin cutting. A committed swing delivers 2 to 5 kN at impact. The incoming blade is sliced partway or fully through and the severed half keeps flying. Parrying far up the filament fails: a 1.5 kN strike at 50 cm puts 750 N·m on the wrist, which no wrist holds, so the filament is shoved aside.

**Fighting style:** Close range, guard-forward, draw cuts and sword-severing parries. Thrusts reserved for electronics. The opponent cannot see the blade, cannot gauge its reach and loses their weapon on contact.

**Hazards:** No scabbard can hold it. A rigid tube scabbard (indestructible itself, 1 m) is mandatory. Sheathing by feel risks cutting through the scabbard throat if it is ordinary material.

### 3.2 The Foil Sword
**Build:** Conventional longsword profile (90 cm × 4 cm) at 50 µm thickness. Atomic edge on both sides.

| Stat | Value |
|---|---|
| Blade mass | 14 g |
| Hilt + pommel for balance | 1 to 1.3 kg |
| Neck severing energy | 56 J |
| Plate breastplate cut (30 cm of 2 mm) | 90 J |

**What it does:** Every swing cuts through any wearable armor in history as if it were not there. A two-handed cut (≈ 200 J) passes through a plate cuirass, the gambeson beneath and the torso beneath that. Wider than the hair rapier so it is visible edge-on as a glint and invisible face-on as a line.

**Why the width helps:** The 4 cm blade face gives a broad parrying surface and real leverage control. It cuts on contact anywhere along the edge. The hair rapier only cuts where pressure is high enough near the guard.

### 3.3 The Razor Chakram
**Build:** 20 cm diameter ring, 50 µm thick at the edge, thickening to a 200 g weighted inner rim.

- Thrown at 30 m/s: ≈ 90 J linear plus spin energy
- Cuts soft tissue at 2 kJ/m², bone at 30 kJ/m²
- Enough to pass through a neck, a forearm or a rifle stock at throwing distance
- **Cannot be caught.** Catching it with a glove means losing fingers. Retrieval needs a rigid hook through the center hole.

### 3.4 The Flywheel Saw
Real flywheels explode when rim speed exceeds what the material can hold together. Indestructible flywheels have **no speed limit except bearings and air**.

**Build:** 1 m diameter, 10 kg indestructible disc with an atomic rim edge, spinning inside a vacuum housing with a cutting slot.

| Rim speed | Stored energy | TNT equivalent |
|---|---|---|---|
| 300 m/s | 225 kJ | 0.05 kg |
| 1,000 m/s | 2.5 MJ | 0.6 kg |
| 5,000 m/s | 62.5 MJ | 15 kg |
| 10,000 m/s | 250 MJ | 60 kg |

At 10,000 m/s the saw holds enough energy to cut through **830 m²** of 70 mm tank armor with a 1 mm rim or **25,000 m²** with a 30 µm rim. Pressing it against a battleship opens a slot from deck to keel.

**Problem:** gyroscopic stiffness. At 10,000 m/s rim speed, angular momentum is ≈ 25,000 kg·m²/s. Turning the disc's axis at 1 radian per second takes 25,000 N·m of torque. It must ride on a gimbal and be steered only in its own plane. A person carrying it gets thrown around by every attempt to turn.

**Bonus:** a perfect energy battery for railguns, lasers or vehicles.

### 3.5 Filament Claws
**Build:** Four 15 cm hair-thin filaments set into a gauntlet across the knuckles.

- Short length eliminates the leverage problem. Full fist force (≈ 500 to 1,000 N in a strike) reaches the cutting line.
- A punch drives four parallel 75 µm cuts 15 cm deep through anything in front of the fist that resists less than about 1,000 N per contact. Flesh, bone, wood, car doors, sheet metal.
- Stops at armor plate thicker than a few millimeters where line loads hit 300 kN/m.

### 3.6 The Unparryable Shears
Two indestructible foil blades on a pivot. Bolt cutters with zero kerf loss and perfect edges. Hand-squeezed with a long lever, they close through rebar, padlock shackles, chain links and rifle barrels.

---

## 4. Lines, Nets and Wires

### 4.1 The Road Wire
A 30 m filament anchored in bedrock across a road at chest or neck height. A car at 60 km/h passes through and loses less than 15 percent of its energy. A tank at 54 km/h loses about 15 percent and its turret is separated. Anchor loads: tens of kilonewtons for cars, about 410 kN per anchor for a tank.

### 4.2 The Dicing Screen (Active Armor Against Rockets)
**Build:** A frame of hair filaments at 5 cm spacing mounted 50 cm in front of a vehicle, like slat armor.

**Against an RPG-7 warhead (85 mm, ≈ 2.6 kg at 115 to 300 m/s, 17 to 120 kJ):**
- Each filament crossing the warhead slices a full longitudinal plane through it: about 0.077 m² of aluminum and steel at 75 kJ/m², roughly 5.7 kJ per filament
- Two filaments cross a typical warhead. Total cut energy about 12 kJ.
- The warhead passes through in strips. The nose fuze is cut. The copper cone liner is split into segments before the charge fires. Split and asymmetric liners form broken, wandering jets that lose most of their penetration.

**Against people:** a fence nobody walks through twice.

**Against drones:** quadcopters entering the screen are sliced into ribbons along with their batteries. Perfect anti-FPV-drone netting.

### 4.3 The Garrote
Two handles, 60 cm of filament. Needs about 3 N per millimeter of contact for flesh. Wrapped around a target and pulled with 300 N, it cuts. No strength or skill threshold. Extremely dangerous to the user: the handles must be indestructible too or the filament cuts through them.

### 4.4 The Monowhip (Articulated Micro-Chain)
A solid filament cannot be a whip because it cannot flex. A **chain** of rigid links can.

**Physics check:** A moving chain pressing a target with curvature radius r applies a line load of λv²/r (λ = mass per meter). To cut flesh it needs about 3 kN/m:

| Chain diameter | Linear density | Tip speed needed to cut flesh (wrap radius 5 cm) |
|---|---|---|---|
| 75 µm hair chain | 0.035 g/m | ≈ 2,070 m/s (impossible) |
| 0.5 mm chain | 1.5 g/m | ≈ 810 m/s |
| 1 mm chain | 6.2 g/m | ≈ 570 m/s |
| 2 mm chain | 25 g/m | ≈ 400 m/s |

A bullwhip's tip routinely breaks the sound barrier at 400 to 700 m/s. **A 1 to 2 mm indestructible micro-chain whip with knife-edged links cuts flesh on the crack.** A hair-thin whip is too light to cut anything. Thicker is better here because momentum grows with area while cutting cost grows only with width.

### 4.5 The Bead Curtain
A doorway hung with dozens of 2 m hair filaments, each free-hanging from a pivot. A free filament weighs 0.07 g and simply swings aside when touched. **Harmless.** Lock the pivots and it becomes a dicing screen. Unlocked or locked is invisible to anyone approaching.

---

## 5. Polearms, Levers and Siege

### 5.1 The 100 ft Hair Pike
A clamped 30.48 m filament. Reach no army can match. Damage from the end: pinholes. Damage from sweeping: limited to about 3.3 N at the tip by leverage and almost nothing past 3 rad/s by air drag. **As a pike it is a 30 m invisible pin.** As a fixed barrier staked into the ground, it is a 30 m cutting fence.

### 5.2 The Rigid Lance Problem
Real cavalry lances were built to shatter. Shattering capped the impact force at a few kilonewtons. An indestructible lance never shatters.
- Horse and rider: ≈ 600 kg at 9 m/s, 5,400 N·s
- Lance hits something that holds (an indestructible shield, a wall, bedrock): the full momentum routes through the rider's arm and saddle
- Rider (≈ 100 kg) stopping over 10 cm of body compression: ≈ 40 kN through the shoulder
- **Result:** the indestructible lance unhorses or breaks its own rider on any solid hit. It needs a shock-absorbing couch mount or a deliberate breakaway grip.

### 5.3 The Perfect Trebuchet
A trebuchet arm loses energy to flexing and to its own mass. An indestructible arm built as a thin hollow truss weighs a fraction of a timber arm with zero flex. Efficiency rises from about 60 to 70 percent toward 85 to 90 percent. Same counterweight, longer range.

### 5.4 The Pry Bar That Never Bends
Normal crowbars bend before a vault door gives. An indestructible bar transfers every newton of leverage into the door, frame or hinge. With a 2 m bar and 1 kN on the handle, the jaw sees 20 to 50 kN. Doors, hinges and frames fail. The bar never does.

---

## 6. Projectiles and Guns

### 6.1 Non-Eroding Flechettes
Hair-thin to 1 mm darts that never deform. They pass through anything but leave pinholes. Excellent against electronics, batteries, fuel cells, optics and sensor heads. Poor against people.

### 6.2 Non-Deforming Bullets
An indestructible bullet does not expand, fragment or tumble apart. Wounds look like ice-pick wounds. Armor penetration is perfect up to the energy limit. Best paired with a deliberately unstable shape so it yaws hard after entry.

### 6.3 The Paper Barrel Gun
Barrel walls can be 0.1 mm thick. Chamber pressure has no structural limit. The gun weighs almost nothing.

**Recoil problem:** a 7.62 rifle round produces about 12 N·s of recoil momentum including gas.

| Gun mass | Recoil velocity | Recoil energy into shoulder |
|---|---|---|---|
| 4 kg (normal rifle) | 3 m/s | 18 J |
| 0.5 kg (paper barrel) | 24 m/s | 144 J |

A featherweight indestructible rifle kicks like being hit with a baseball bat. It needs a muzzle brake, a recoil mass or a mount.

### 6.4 Hypervelocity Without Wear
Railgun rails erode after a few shots at 2 to 3 km/s. Indestructible rails do not. Light-gas guns with indestructible barrels take unlimited pressure. The limit becomes the propellant's sound speed and power supply. Realistic muzzle speeds: 7 to 10 km/s. A 1 kg indestructible slug at 10 km/s carries 50 MJ (≈ 12 kg TNT) and keeps every joule of it for the target.

### 6.5 Hair Darts From Above
A filament with a 1 kg nose weight dropped 100 m arrives with about 980 J. It passes through any vehicle except frontal tank armor. Drop a pallet of them over a vehicle park and every battery, fuel cell, radio and computer below gets pinned through.

---

## 7. Armor

### 7.1 Foil Plate
Full articulated harness in 0.1 mm indestructible sheet.

| Stat | Value |
|---|---|
| Body surface coverage | ≈ 1.9 m² |
| Mass of plates | ≈ 1.5 kg (historic plate harness: 20 to 30 kg) |
| Penetration resistance | Absolute |
| Weak points | Joints, gaps, neck opening, eye slits |
| Momentum limit | See section 2.3. Rifle fire is a tap. Autocannons throw the wearer. Tank rounds kill through acceleration. |

**Joint design:** Rigid plates cannot bend, so every joint is a lames-and-rivets articulation. Gaps exist wherever plates slide. A hair rapier finds those gaps. Covering them takes the next layer.

### 7.2 Micro-Mail Fabric
Rings of 20 µm indestructible wire with 15 µm openings. Drapes like silk.

| Stat | Value |
|---|---|
| Areal mass | ≈ 0.12 kg/m² |
| Full bodysuit | ≈ 0.25 kg |
| Blocks | Every blade, every needle, every hair weapon, every projectile wider than 15 µm |
| Fails at | Blunt trauma. The fabric cannot stretch or tear but it can be pushed into the body. A rifle bullet presses a cone of fabric deep into flesh. |

**The answer:** Micro-mail as the base layer for coverage. Foil plates over the torso and head to spread impact force. Padding between them.

### 7.3 The Foil Shield
60 cm round, 0.2 mm thick. Mass 0.44 kg. Stops anything. The arm holding it does not. A .50 BMG hit transfers 41 N·s into the shield arm in about a millisecond: tens of kilonewtons of peak force. The shield is fine. The shoulder dislocates. Shields need a brace strap and a body-weight stance.

### 7.4 Heat and Electricity
- **Fire:** The suit does not melt. It does conduct. Napalm or thermite on the outside heats the inside within seconds. Needs an insulating liner (aerogel, ceramic felt).
- **Lightning and electrical attacks:** A fully enclosing conductive shell is a Faraday cage. Current flows around the outside. The wearer survives lightning, tasers and EMP.
- **Lasers:** A polished indestructible surface never pits or roughens, so it stays a mirror forever. Most of the beam reflects. The absorbed fraction conducts heat inward.
- **Microwaves and radio:** Blocked completely. The wearer's radio needs an external antenna.

### 7.5 Blast
Overpressure flows through every gap and slams the whole suit as a unit. A sealed indestructible suit protects against fragments completely and against overpressure partly. Close to a large charge the wearer is thrown as a rigid body.

---

## 8. Vehicles and Fortresses

### 8.1 The Foil-Skinned Tank
1 mm of indestructible skin over a normal tank. Mass penalty: a few hundred kilograms. Every anti-tank weapon on Earth fails to penetrate. Momentum from a 120 mm APFSDS round (7,600 N·s) moves a 60 tonne tank by **0.13 m/s**. The tank barely rocks.

**Mass is the defense multiplier.** The heavier the protected object, the less the momentum matters. Indestructible armor is close to perfect on tanks, ships and buildings. It is only partial on people.

**Remaining threats:**
- Heat: a sustained fire or thermite pile cooks the crew through conduction
- Mobility kills: tracks, road wheels and running gear that are not indestructible
- Optics and sensors: anything that must look outward needs a window
- Mines: the hull survives. Crew inside take the full acceleration of being flipped.

### 8.2 The Indestructible Dome Bunker
A 0.5 mm indestructible hemisphere over a bunker, keyed into bedrock.
- **Bombs, missiles, artillery, bunker busters:** No penetration. Penetrators stop at the skin and dump their energy outside.
- **Nuclear surface burst:** The dome holds. Overpressure loads the dome and transfers to its foundation. The foundation rock fails before the dome does. Thermal flash heats the skin. Ground shock travels up from below where the dome does not reach.
- **Correct design:** Indestructible floor as well as roof, forming a sealed sphere floating in the ground, with shock isolation springs (non-indestructible, so they can flex) between the sphere and the living space.

### 8.3 The Unsinkable Ship
A 2 mm indestructible hull cannot be holed by torpedoes, mines or shells. A torpedo's blast still lifts and whips the ship. In a real ship that whipping breaks the keel. In an indestructible hull with no keel to break, the hull flexes zero and the crew inside get thrown against the deck. Interior fittings tear loose. The hull itself floats forever.

---

## 9. Matchups

| Attacker | Defender | Result |
|---|---|---|---|
| Hair rapier thrust | Foil plate | No penetration. Tip skates across the surface. Probes for a gap. |
| Hair rapier thrust | Micro-mail (15 µm openings) | No penetration. Two unbreakables meet. Wielder feels a solid stop. |
| Hair rapier thrust | Micro-mail with 100 µm openings | Slips through between rings. Mesh pitch decides everything. |
| Foil sword | Foil sword | Neither cuts. Edges ride each other with zero wear. Pure fencing skill. |
| Foil sword | Ordinary steel sword | Steel sword severed on any hard parry or bind |
| Flywheel saw | Foil-skinned tank | No cut. The saw's rim stops against the skin and its stored energy tries to throw the saw, the tank or both. |
| Flywheel saw | Ordinary tank | Opens it like a can |
| Dicing screen | Infantry | Impassable. Nearly invisible. |
| Dicing screen | Foil-armored infantry | Armored parts stop at the screen. Gaps and joints get cut. |
| 120 mm APFSDS | Foil-armored soldier | Armor perfect. Soldier dead from acceleration. |
| 120 mm APFSDS | Foil-skinned tank | Armor perfect. Crew rattled. Tank fine. |
| Road wire | Foil-skinned tank | Tank stops dead against the wire. Anchors take the full momentum. Whichever anchor is weaker rips out of the ground. |

---

## 10. Universal Weaknesses of Indestructible Gear

1. **It cannot be resized, repaired, sharpened or modified.** Whatever shape it was made in is permanent. Armor must fit perfectly from day one.
2. **It cannot be destroyed.** Lost filaments are permanent hazards. A dropped hair rapier lying in grass is an invisible blade forever.
3. **It cannot be blunted.** Training weapons do not exist. Every sparring match is live.
4. **Thin means weightless.** Hair and foil weapons carry no momentum. All force comes from the wielder through the grip.
5. **The grip is ordinary.** Hilts, collets, rivets, straps, anchors, hinges, foundations and the human body all fail first.
6. **Momentum and heat pass straight through.** Indestructible does not mean invulnerable.
7. **It cannot flex.** No springs, no bows, no rope, no whips without articulation.

---

## 11. The Most Wicked Designs, Ranked

| Rank | Item | Why |
|---|---|---|
| 1 | **Flywheel saw** | Stored energy without limit, released through a perfect edge. A handheld battleship cutter. |
| 2 | **Dicing screen** | Defeats rockets, drones and infantry at once. Nearly invisible. Costs a few grams of filament. |
| 3 | **Foil-skinned heavy vehicle** | Immune to penetration. Mass makes momentum irrelevant. |
| 4 | **Foil sword** | Every swing cuts through any armor ever worn. |
| 5 | **Road wire** | Turns enemy kinetic energy against itself. |
| 6 | **Micro-mail bodysuit + foil plate** | Blocks every blade and bullet a person can carry. Weighs under 2 kg. |
| 7 | **Hair rapier** | Invisible, severs swords, kills electronics through walls. Weak as a killing thrust. |
| 8 | **Micro-chain monowhip** | Cuts on the crack. Terrifying. Hard to control. |
| 9 | **Filament claws** | Short and brutal. Leverage problem solved by being short. |
| 10 | **Hair darts and flechettes** | Precision equipment kill. Near-useless against people. |
