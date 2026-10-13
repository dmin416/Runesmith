# Kinetic Spell List

> **Ideas / design loot.** Spells priced from kinetic energy and compression only. Not automatic law.
>
> Live cast law and Bolt / Arrow tables: `../Runes/Energy.md`, `../World/Science/Energy/ManaCast.md`. Named catalog: `Spells.md`. Form sizes: `BasicSpellShapes.md`. Shield absorb pools: `AttackScale.md`.

## Conflicts (read first)

| Topic | Live lock | This idea |
|---|---|---|
| **1 MP = 10 J** | Locked (`Energy.md`) | Same |
| **Mana Bolt voice steps** | Mental 10 … Normal **25** … Very loud 50 (`ManaCast.md`) | Flat **25 MP** as the Bolt rung (matches Normal). Other voice rungs not restated here |
| **Mana Arrow** | Voice costs **2× Bolt**; Normal **50**; pure kinetic (`ManaCast.md`) | Same 50 MP / 500 J model |
| **Bolt physics** | Worked as kinetic + chapter pop / wound feel | **Explosive** with compression multiplier `(MP ÷ 25)²` |
| **Mana Shield cost** | Formula / pool in `ManaCast.md` / `AttackScale.md`; not a flat 100 MP lock | Flat **100 MP** / 1,000 J absorb + deflect narrative |
| **Minimum cast** | No global 20 MP floor | **20 MP** minimum (shaping tax) |
| **Many utility spells** | Not on sheet (Push, Lift, Dash, …) | New catalog names |

Promote a row only when a chapter needs it and it abides live curves.

---

## Pricing Rules

- 1 MP = 10 J
- Moving mass: KE = ½ × mass × velocity²
- Lifting: Energy = mass × 9.81 × height
- Pushing, prying or crushing: Energy = force × distance
- Defensive constructs are priced by how much energy they can absorb before failing. Deflected or redirected energy does not count against them.
- Costs are raw mana usage at 100% efficiency. Runes divide by their efficiency. Mage casts apply skill and Intelligence multipliers.
- Reference body: 80 kg adult.
- Costs use clean numbers: 20, 25, 50, 75, 100, 150, 200, 250, 300, then steps of 100. Formula results round to the nearest clean number.
- Minimum spell cost is 20 MP. Shaping the magic costs energy so a spell that does less than 200 J of work still costs 20 MP.

## Nature of Magic

Explosive magic is more cost effective than other magic. Mana can be superimposed and super-compressed into an explosive charge in a way that normal matter cannot do cheaply.

### Explosive Compression

In an explosive spell the mana does two jobs at once. Part of it is the payload and part of it forms the shell that compresses the payload. More mana means a bigger payload and a stronger shell at the same time. The stronger shell squeezes the payload into a smaller space so energy density climbs with the square of the mana spent.

- **Compression multiplier:** (MP ÷ 25)²
- **Effective energy:** raw energy × compression multiplier
- **Blast radius:** grows in a straight line with MP. Doubling the mana doubles every blast radius.
- **Lethal radius:** MP × 0.005 m
- **Concussive radius:** MP × 0.0125 m (throws people off their feet and ruptures eardrums)
- **Harmless beyond:** MP × 0.025 m

Below 25 MP the multiplier drops under 1 and the compression costs more than it returns. That is why Mana Bolt is the cheapest explosive spell.

The multiplier only applies to explosive spells. Kinetic projectiles like Mana Arrow and Spear use raw energy.

| MP | Raw Energy | Multiplier | Effective Energy | TNT Equivalent | Lethal | Concussive | Harmless Beyond |
|---|---|---|---|---|---|---|---|
| 25 (Mana Bolt) | 250 J | 1× | 250 J | 0.06 g | 0.125 m | 0.3 m | 0.6 m |
| 50 | 500 J | 4× | 2 kJ | 0.5 g | 0.25 m | 0.6 m | 1.25 m |
| 100 | 1,000 J | 16× | 16 kJ | 4 g | 0.5 m | 1.25 m | 2.5 m |
| 200 | 2,000 J | 64× | 128 kJ | 31 g | 1 m | 2.5 m | 5 m |
| 400 (Mana Ball) | 4,000 J | 256× | 1 MJ | 245 g | 2 m | 5 m | 10 m |
| 800 | 8,000 J | 1,024× | 8.2 MJ | 2 kg | 4 m | 10 m | 20 m |
| 1,600 | 16,000 J | 4,096× | 65.5 MJ | 15.7 kg | 8 m | 20 m | 40 m |

For reference a hand grenade holds roughly 180 to 240 g of explosive. Mana Ball matches its blast without the fragments.

## Summary

| Spell | Energy | Mana Usage |
|---|---|---|
| Mana Wedge (door) | 100 J | 20 MP (minimum) |
| Mana Pull (disarm) | 100 J | 20 MP (minimum) |
| Mana Needle | 200 J | 20 MP |
| Mana Blade | 200 J | 20 MP |
| Mana Step | 250 J | 25 MP |
| Mana Push | 250 J | 25 MP |
| Mana Pull (person) | 250 J | 25 MP |
| Mana Bolt | 250 J | 25 MP |
| Mana Wedge (steel bar or rubble) | 500 J | 50 MP |
| Mana Hammer | 500 J | 50 MP |
| Mana Shot | 500 J | 50 MP |
| Mana Arrow | 500 J | 50 MP |
| Mana Bind | 1,000 J | 100 MP |
| Mana Dash | 1,000 J | 100 MP |
| Mana Shield | 1,000 J | 100 MP |
| Mana Crush | 1,500 J | 150 MP |
| Mana Barrier | 2,000 J | 200 MP |
| Mana Pulse | 3,000 J | 300 MP |
| Mana Ball | 4,000 J | 400 MP |
| Spear Spells | 4,000 J | 400 MP |
| Mana Lift | Scales | mass × height × 0.98 MP |
| Mana Cushion | Scales | mass × fall height × 0.98 MP |

Real-world reference points: a longbow arrow carries about 80 to 150 J. A 9mm pistol round carries about 500 J. A 5.56mm rifle round carries about 1,700 J.

## Core Spells

### Mana Bolt

Mana Bolt is one of the most basic attacks. It is the cheapest explosive spell.

- **Cost:** 25 MP (250 J)
- **Size:** about the size of an egg
- **Compression:** 1×. Mana Bolt sits at the break-even point where compression starts paying for itself.
- **Explosive equivalent:** about 0.06 g of TNT, roughly one standard firecracker
- **Blast radius:** lethal only within about 12 cm, which is why the delayed burst inside a wound matters so much. Harmless beyond about 60 cm.
- **Behavior:** flies forward and then blows up a moment after impact regardless of whether it has penetrated or not. The short delay lets it sink into soft targets before it bursts.
- **Against bare flesh or cloth:** the burst happens inside the wound which makes it far worse than the same energy on the surface.
- **Against leather:** may partly sink in. Bursts with a hard concussive hit that bruises and staggers.
- **Against mail or plate:** bursts on the surface. Dents and rattles the wearer but rarely gets through.
- **Role:** the standard opening attack for new mages. A fledgling mage with about 200 MP can cast it eight times.

### Mana Arrow

Mana Arrow is a pure kinetic projectile that works like a bullet. It does not explode.

- **Cost:** 50 MP (500 J)
- **Model:** 8 g equivalent at 354 m/s, about the same as a 9mm pistol round
- **Behavior:** small, fast and straight. Punches a narrow wound channel.
- **Against bare flesh, cloth or leather:** goes through or lodges deep like a pistol round.
- **Against mail:** often stopped or slowed enough to leave a bruise and broken rings.
- **Against plate:** dents it but rarely gets through.
- **Role:** the precise follow-up to Mana Bolt. It trades the Bolt's burst for reach and accuracy.

### Mana Shield

Mana Shield normally costs 100 MP. It absorbs up to 1,000 J before failing.

Mana shields are more narrative than rigid. A shield does not absorb all of an attack's energy. It deflects or redirects most of it and only absorbs the part that hits it head on. This matters most against explosives and spears. A Mana Ball bursts in every direction so only a small share of its blast meets the shield. A Spear can be glanced aside if the shield is angled against it. A 1,000 J shield can survive attacks far stronger than 1,000 J this way.

### Mana Ball

Mana Ball is the pure mana form of the Ball spells. Elemental versions convert part of the mana into an element. It is closer to a grenade than a firecracker.

- **Cost:** 400 MP (4,000 J), sixteen Mana Bolts' worth of energy
- **Size:** the visible ball looks big but nearly all of its mana sits in a small core at the center
- **Compression:** the core holds the same amount of mana compressed to the point of absurdity. That extreme compression is what lets the burst cover a large enough area for the attack to be worthwhile.
- **Compression:** 256×, turning 4,000 J of raw energy into about 1 MJ of effective blast
- **Explosive equivalent:** about 245 g of TNT, a hand grenade's blast without the fragments
- **Behavior:** flies forward and bursts on impact in every direction. It trades the Mana Bolt's penetration for spread.
- **Within about 2 m:** can kill or cripple unarmored people. Knocks armored people down and breaks wooden shields.
- **Within about 5 m:** a hard concussive blow that throws people off their feet and ruptures eardrums.
- **Beyond about 10 m:** loud and startling but mostly harmless.
- **Role:** a true area attack. A fledgling mage with about 200 MP cannot cast it. Sixteen Mana Bolts cost the same mana but Mana Ball's compression makes it about 256 times stronger.

### Spear Spells

Spear spells are pure kinetic projectiles built for penetration. They do not explode.

- **Cost:** 400 MP (4,000 J), the same as Mana Ball
- **Model:** 0.5 kg equivalent at 126 m/s. Heavier and longer than an arrow so it keeps driving after impact. Energy is a bit above a full-power rifle round.
- **Behavior:** concentrates all of its energy on one target where Mana Ball spreads it over an area.
- **Against bare flesh, cloth or leather:** passes clean through and can hit whatever stands behind.
- **Against mail:** punches through.
- **Against plate:** pierces most plate and can pin the wearer.
- **Against shields:** a straight hit can break through. An angled Mana Shield can glance it aside.
- **Role:** the armor breaker and the answer to a single heavily protected target.

## Offense

### Mana Needle

A tiny ultra-compressed point fired at high speed. Pierces instead of exploding.

- Model: 2.5 g equivalent at 400 m/s
- Energy: 200 J
- Mana Usage: 20 MP

### Mana Shot

A spread of small compressed pellets. Weak at range but strong up close.

- Model: 10 pellets of 1.6 g equivalent at 250 m/s (50 J each)
- Energy: 500 J
- Mana Usage: 50 MP

### Mana Hammer

A blunt compressed impact with no detonation. Built for knockdowns and breaking armor or doors.

- Model: 10 kg battering ram equivalent at 10 m/s
- Energy: 500 J
- Mana Usage: 50 MP

### Mana Blade

A thin compressed edge that cuts instead of hitting. Priced per slash.

- Model: 1 kg effective sword mass at 20 m/s
- Energy: 200 J
- Mana Usage: 20 MP per slash

### Mana Crush

Pressure folding inward on a target from all sides. Enough to break ribs or dent plate armor.

- Model: 15,000 N over 10 cm
- Energy: 1,500 J
- Mana Usage: 150 MP

## Control

### Mana Push

A flat shove for knockback with no damage.

- Model: 80 kg person pushed to 2.5 m/s
- Energy: 250 J
- Mana Usage: 25 MP

### Mana Pull

The same vector reversed to yank something toward the caster.

- Disarm: 2 kg weapon at 10 m/s = 100 J = 20 MP (minimum)
- Person: 80 kg pulled to 2.5 m/s = 250 J = 25 MP

### Mana Bind

Compressed rings that clamp limbs or pin a target. Priced by the struggle it can absorb.

- Model: absorbs about 5 seconds of all-out struggling at 200 W
- Energy: 1,000 J
- Mana Usage: 100 MP

### Mana Pulse

A radial ring burst around the caster that clears space when surrounded. Expensive because most of the energy spreads into empty space.

- Model: ring 2 m out and 1.8 m tall (22.6 m² of surface). One person blocks about 0.7 m² or 3% of it. Staggering each person at 1.5 m/s takes about 90 J on that person.
- Energy: 3,000 J
- Mana Usage: 300 MP
- Full knockback at Mana Push strength (2.5 m/s): about 800 MP


## Utility and Movement

### Mana Step

A brief compressed platform to stand on in midair. Priced by the landing it absorbs.

- Model: 80 kg stepping down onto it from 32 cm
- Energy: 250 J
- Mana Usage: 25 MP

### Mana Dash

A kinetic shove on the caster for a burst of movement.

- Model: 80 kg caster launched to 5 m/s
- Energy: 1,000 J
- Mana Usage: 100 MP

### Mana Cushion

A decelerating field that slows falls or incoming impacts.

- Formula: mass (kg) × fall height (m) × 9.81 ÷ 10, rounded to a clean number with a 20 MP minimum
- 80 kg from 3 m: 2,354 J = 250 MP
- 80 kg from 5 m: 3,924 J = 400 MP
- 80 kg from 10 m: 7,848 J = 800 MP

### Mana Lift

Steady force for moving objects at a distance.

- Formula: mass (kg) × height (m) × 9.81 ÷ 10, rounded to a clean number with a 20 MP minimum
- 10 kg raised 2 m: 196 J = 20 MP
- 80 kg person raised 2 m: 1,570 J = 150 MP
- Holding still costs nothing in pure physics because no work is done. Any upkeep comes from efficiency losses.

### Mana Wedge

Outward pressure to pry apart doors, bars or rubble.

- Door: 5,000 N over 2 cm = 100 J = 20 MP (minimum)
- Bending a 2 cm mild steel bar 90°: about 500 J = 50 MP
- Raising a 200 kg slab of rubble 25 cm: about 500 J = 50 MP

### Mana Barrier

A larger static form of Mana Shield covering an area or doorway. Priced by what it can absorb. Size does not change the physics cost but capacity does.

- Model: absorbs 2,000 J before failing. Like Mana Shield it deflects most of an explosion or spear so it can hold against a Mana Ball or Spear.
- Energy: 2,000 J
- Mana Usage: 200 MP
