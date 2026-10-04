# Energy

Spell-specific worked tables: `../World/Science/Energy/ManaCast.md`. Altitude density: `../World/Science/Energy/ManaConcentration.md`. Stone size / mass tables: `../World/Science/Energy/ManaStones.md`. Stone law: `../World/Materials/MonsterCores.md`. Metals / hosts: `../World/Materials/Metals.md`.

Design companions: `EnergyDesign.md` (electrical analogy, wear stages, body-path proposals; path-% non-canon), `RuneSystem.md`, `RuneSetup.md`, `ManaMaterials.md`, `Nature.md`. Live lock: mythril = saturated silver / Ag–Cu; **orichalcum = antimagic** (magical titanium / refuse); **cast adamantium = indestructible**; η_cond = feel order in this file. Future spell idea math: `../PotentialMagic/PotentialMagic.md` (design loot; same cast law).

## Narrative

Mana is an energy that saturates the world. It is both a particle and a spiritual thing. **Mana is like air:** it fills the world as a fluid density field, and **density rises with altitude**. It also gathers thick in dungeons, spiritual places, and materials. It can pass through most anything, and it can also touch things if desired. Any mana movement is technically unnatural, even when it does no harm. When it passes through or alongside materials, it may spontaneously impart more energy than it is exerting. Compressed with intention, it can gain mass, though like any compression it wants to reach equilibrium. Raw mana is weak on its own. With a user it can rise by that user's multiplier, a mix of Intelligence and skill level. Only people with mana affinity have a mana pool. Everyone else carries only about air-level mana in the body, enough to sustain life. People also have a life force level set by life force, soul, and strength. Runic energy is mana.

## Detail

### Nature

**What it is:** Energy that saturates the world. Particle and spiritual at once.

**Where it gathers / density:** Like air. **Density increases with altitude** (thicker higher up). Curve: `../World/Science/Energy/ManaConcentration.md`. Also thick in dungeons, spiritual places, and saturated materials. Sea-level outdoor air is thinner mana than a mountain. Upper atmosphere is richest on the open sky.

**Passage:** Can pass through most anything.

**Touch:** Can also touch things if desired.

**Compression:** With intention, compressed mana can gain mass. It wants equilibrium, same as ordinary compression.

**Movement:** Any form of mana movement is technically unnatural. It may not harm anything. The unnatural part is still true.

**Material interaction:** Mana passing through or alongside materials may spontaneously impart more energy than it is exerting.

**Insulation:** Mana can insulate, but needs an insulation rune that spends energy to hold the barrier.

**Barriers:** Mana can form invisible barriers against mana, kinetic force, air, sound, elements, and similar.

**Raw floor:** About **0.3 J** as raw energy at worst.

**Joule peg:** **1 mana = 10 J** base.

**Direct cast law (locked):**

```
Useful (J) = mana × 10 × η(L) × μ(INT)

η(1)   = 0.3
η(L)   = 1 + (L - 2) × 2/7      // L2 = 1.0, L9 = 3.0
μ(INT) = (INT / 15)^0.8         // INT 15 = 1×
```

| L | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| η | 0.30 | 1.00 | 1.29 | 1.57 | 1.86 | 2.14 | 2.43 | 2.71 | 3.00 |

η is a level power factor, not a 0–1 cap. Combined INT × level feel lands about **1× to 10×** in normal bands.

**Voice / mana-in (Bolt baseline):** Mental 10, Whisper 15, Quiet 20, Normal 25, Loud 40, Very loud 50. Voice only sets mana spent. Overcharge = mana used. Spell-specific voice tables (Arrow 2× Bolt, etc.): `../World/Science/Energy/ManaCast.md`.

**Mana-in channels (what sets mana spent):** Voice/volume, emotional intensity / focus / skill, and overcharge all only change **how much mana** goes into the cast. They do not change η(L) or μ(INT). A whisper from a furious focused caster and a shout from a calm one can land on the same mana total and the same joules.

**Body processing:** The human body is excellent at handling mana. Effective processing scales with Intelligence and physical robustness.

**Mana veins:** Mages have mana veins. Power management matters. Lose control and the flow can rage locally and wreck flesh (arm-blowout style from dumping too many casts at once).

**Mage tolerance:** Because mages already hold mana, their bodies tolerate mana flow better than plain metal hosts.

**Wielder as path:** A caster’s body can be the source or return for a rune path.

**Runes:** Runic energy is mana. Same substance, rules-based use.

**Ink:** Blood or mana ink carries a usable path. Ordinary ink is like writing with water: almost no usable channel. Monster blood can work as path material; quality depends on the blood.

### Pools

**Mana pool:** Only people with mana affinity have one. Size comes from stats. No fixed adult number.

**No affinity:** Body mana stays near air level. That amount sustains life. No pool to spend.

**Life force:** Separate from the mana pool. Level tracks life force / soul / strength.

**Stamina (SP):** Body resource. Same-cost alternate fuel for **runes**. Usually recovers faster than mana. Same rune cost paid from SP tires the body harder because SP also runs muscle and breath.

**Bottoming out:** Emptying any pool (MP, SP, or other) can make anyone really sick.

### Cost

**Normal magic:** Has a basic cost. Intention and chant shape the cast. Can be cast weaker (less cost, less power) or stronger (more push, more power) around that basic cost.

**Runes:** Cost = minimum of the rune’s own minimum and the maximum mana channeled in. Stamina can pay the same cost instead of mana.

**Seating / setting:** Pushing a rune into a host can strain or ruin that host. Seating is not free of wear.

**Cast vs item:** Body skill casts and rune / item converters both use the **10 J** peg. Ambient helps more when the pattern can drink local mana density (thicker at altitude). Direct casts and rune paths use **different efficiency sources** (see Waste and control).

**Resonant runes:** High-grade / resonant work can use its own effective factors later (deep craft pass).

**Ambient gain G (rune / item paths only):** G tracks **local mana density**. Density is like air and **rises with altitude**. Altitude curve: `../World/Science/Energy/ManaConcentration.md`. Dungeons and spiritual sites are also dense. A pattern that can drink outside mana hits harder in denser air. Direct skill casts take **no** ambient G. A rune with no outside intake (fully sealed / no breath to the air) cannot drink density and sits at the no-intake floor.

**Local drain:** Not an everyday rule. Only at world-class / crazy plot scale.

**Burst:** One huge dump can wreck a weak path or vein section in a single cast.

### Temporary magic

Magical phenomena that are not enchanted or runed are temporary. Earth walls, ice, fire, and similar hit hard while they exist, then fade fast. A fireball can cost the same as a shield and feel grenade-scale while active, but when the spell ends the ground is not baked and bodies are not lava. Mana pays the spell effect, not lasting leftover real-world energy. Fire and similar break hard joule ladders; treat scale as narrative feel, not thermal inventory after the spell is gone.

**Fire's chemical energy is not the spell's energy.** A fire spell is an ignition source. With fuel present the fuel's own energy follows and is not part of the spell budget. With no fuel the fire is capped by the spell's Useful output. Do not scale mana cost by how energetic fire is in general.

### Recovery

**Mana (mages):** Rate depends on mana left and total pool. Old equation family kept:

| Term | Meaning | Symbol |
|---|---|---|
| Force | How hard the tank pulls. Current mana plus a baseline pull. | `F = M + b × P` |
| Absorptive surface | Skin and lungs vs a 175 cm adult reference. | `S = (height / 175 cm)²` |
| Permeability | How well mana passes tissue (adult-man equivalents). | `Rob` |

- Rate (mana/h) = `k × S × Rob × F = a × (M + b × P)` with `a = k × S × Rob` and `k = 0.25` per hour.
- `M`: current mana. `P`: maximum pool (from stats).
- `b = 1 / (e^(a × T) − 1)` sets empty→full time `T` for a given body.
- Time to full from `M` = `ln((P + b × P) / (M + b × P)) / a` hours.
- Absorption speeds up as the tank fills.
- Recovery scales with local mana density: higher altitude denser, plus dungeon / spiritual richness. Same air-like density law.

**Stamina:** Body-based. Usually recovers faster than mana.

### Waste and control

**Peg:** **1 mana = 10 J** at the converter input. Cost is paid first and does not change. Efficiency only changes useful output and waste.

**Two pathways (do not stack):**

| Pathway | Efficiency comes from | Formula feel |
|---|---|---|
| Direct skill cast | Skill level η(L) and Intelligence μ(INT) | `Useful = mana × 10 × η(L) × μ(INT)` |
| Rune / item path | **Mana conductivity** of the channel, then ambient density gain G | `Useful = mana × 10 × η_cond × G` |

These two rows are **alternatives, not a chain.** Never multiply η(L)/μ(INT) with η_cond/G on the same cast. Spell-worked tables: `../World/Science/Energy/ManaCast.md`.

**Stat-grant skills are never a multiplier.** Mana Shaping, Mana Regulation, Mana Absorption, Mana Reinforcement and kin only hand out flat INT/WIL (or similar). They raise output only by feeding `μ(INT)`. No second "shaping efficiency" term.

**Cost reducers act before conversion.** Rune Mastery (−10%/level, capped −90%) lowers mana **paid**. It is not a second output multiplier. It can stack with mana-in channels because both only touch the mana figure that then runs through exactly one pathway row above.

Electricity is the physical model for how mana **moves**. Mana is not electricity. Mana conductivity ranking is its own ladder (not ohm-meter copy-paste).

#### Mana conductivity (rune / item paths)

η_cond is **mana conductivity** of the channel, not a caster power rank. Worse conductors waste more as heat and strain. Better conductors carry heavy flow cleanly. Geometry still matters: longer or thinner paths resist more.

**Feel order (worst → best common path):**

iron → copper → steel → mana steel → body / blood ink → refined mana steel → mythril → adamantium (inlay)

Orichalcum refuses / antimagic. Direct casts never use η_cond. A mythril wand does not buff Mana Bolt; it wastes less on the **rune path**.

When a scene needs a number, set η_cond from that feel (and real conductivity analogy if useful).

**Waste:** Most waste leaves with the discharge. The rest stays in the path as heat and strain. Poor conductivity + high flow burns hosts. Burst dumps can wreck a weak path in one shot.

#### Narrative path (when you are not doing joule math)

Seating quality, channel fill, heat under flow, strain, plate life, whether the inlay holds. Skill and setup still matter on the **paid mana** side (Rune Mastery discounts cost; sloppy seating ruins hosts). Craft ladders: `../World/Materials/Metals.md`.

## Open

- Numeric η_cond when a beat needs it
- How dungeon / spiritual thickness stacks on the altitude curve when a beat needs it
