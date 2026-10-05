# Energy

Spell-specific worked tables: `../World/Science/Energy/ManaCast.md`. Altitude density: `../World/Science/Energy/ManaConcentration.md`. Stone size / mass tables: `../World/Science/Energy/ManaStones.md`. Stone law: `../World/Materials/MonsterCores.md`. Metals / hosts: `../World/Materials/Metals.md`.

Design companions: `EnergyDesign.md` (electrical analogy, wear stages, body-path proposals), `RuneSystem.md`, `RuneSetup.md`, `ManaMaterials.md`, `Nature.md`. Live lock: Ag→mythril; Au→orihalcum (MR=% / antimagic); Cu→aurium; Fe/steel→dark→star; Ti→adamantium cast-final (`../World/Materials/Metals.md`); η_cond = quality ladder in **20%** blocks (Lowest **0.2** → Highest **1.0**); host feel is narrative only. Future spell idea math: `../PotentialMagic/PotentialMagic.md` (design loot; same cast law).

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
Useful (J) = mana × 10 × η(L) × μ(INT) × A

η(1)   = 0.3
η(L)   = 1 + (L - 2) × 2/7      // L2 = 1.0, L9 = 3.0
μ(INT) = (INT / 15)^0.8         // INT 15 = 1×
A      = √C                     // ambient; open ground A = 1
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

**Mana pool:** Only people with mana affinity have one. Size comes from stats (`../Progression/Attributes.md`). Street bare all-15 example is **MP 210**; there is no separate universal “adult pool = 2000.”

**No affinity:** Body mana stays near air level. That amount sustains life. No pool to spend.

**Life force:** Separate from the mana pool. Level tracks life force / soul / strength.

**Stamina (SP):** Body resource. Same-cost alternate fuel for **runes** (including runic scrolls). Not a substitute for **word / magic scrolls** (those need mana). Usually recovers faster than mana. Same rune cost paid from SP tires the body harder because SP also runs muscle and breath.

**Bottoming out:** Emptying any pool (MP, SP, or other) can make anyone really sick.

### Cost

**Normal magic:** Has a basic cost. Intention and chant shape the cast. Can be cast weaker (less cost, less power) or stronger (more push, more power) around that basic cost.

**Runes:** Cost = minimum of the rune’s own minimum and the maximum mana channeled in. Stamina can pay the same cost instead of mana.

**Seating / setting:** Pushing a rune into a host can strain or ruin that host. Seating is not free of wear.

**Cast vs item:** Body skill casts and rune / item converters both use the **10 J** peg. Ambient osmosis boosts useful output for **both** via `A = √C` (see below). Pathways still use different skill vs conductivity terms (see Waste and control).

**Resonant runes:** High-grade / resonant work can use its own effective factors later (deep craft pass).

**Ambient osmosis (spells and rune activation):** Mana prefers thinner air and higher spiritual worth (altitude, dungeons, holy/cursed sites, anywhere narrative marks thick). Not a vacuum: the field does not empty into the caster. Paid mana cost is unchanged; ambient only boosts **useful** output a partial amount.

Relative concentration `C` vs open-ground baseline `C₀ = 1`. Law: `../World/Science/Energy/ManaConcentration.md`. Altitude digits: `../World/Space/Atmosphere.md`. Dungeon / spiritual additive: `../World/Geography/Dungeons.md`.

```
A = √(C / C₀) = √C
```

Kinetic-style: concentration ×4 → power ×2, not ×4. Ground open air: `A = 1`.

Both pathways multiply by `A` after their own efficiency term. Fully sealed runes with no breath to the air sit at the no-intake floor (`A = 1` unless the beat says the seal still feels the room).

**Local drain:** Not an everyday rule. Only at world-class / crazy plot scale.

**Burst:** One huge dump can wreck a weak path or vein section in a single cast.

### Temporary magic

Magical phenomena that are not enchanted or runed are temporary. Earth walls, ice, fire, and similar hit hard while they exist, then fade fast. A fireball can cost the same as a shield and feel grenade-scale while active, but when the spell ends the ground is not baked and bodies are not lava. Mana pays the spell effect, not lasting leftover real-world energy. Fire and similar break hard joule ladders; treat scale as narrative feel, not thermal inventory after the spell is gone.

**Fire's chemical energy is not the spell's energy.** A fire spell is an ignition source. With fuel present the fuel's own energy follows and is not part of the spell budget. With no fuel the fire is capped by the spell's Useful output. Do not scale mana cost by how energetic fire is in general.

### Recovery and who can absorb

**No mana pool → no active absorb.** People without a class mana pool (pre-Mage / pre-Acolyte and anyone else without a working pool) do **not** pull ambient mana into themselves on purpose. They have nothing to fill.

**Mana-rich places can still help them:** a dense / spiritually thick field may ease the body and spirit (rest, recovery feel, narrative healing). That is **not** stored mana. When they leave, they do **not** carry a fuller tank; they never had one.

**Forced / unnatural absorb is radiation-class danger.** Using Mana Sense (or similar) to see ambient mana and then **moving** that natural mana into a body that cannot hold it is unnatural. It poisons or kills (original Roland's death; D's early scare). Treat like radiation: visible / tangible mist does not make it safe to drink. Safe ambient absorb starts with a real pool (Mage, Acolyte, or equivalent).

**Mana (with a pool):** Rate depends on mana left and total pool. Old equation family kept:

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
- Recovery scales with local mana density: higher altitude denser, plus dungeon / spiritual richness (`A` / `C` feel; denser field → faster refill).

**Stamina:** Body-based. Usually recovers faster than mana.

### Waste and control

**Peg:** **1 mana = 10 J** at the converter input. Paid mana runs through one pathway. Efficiency (and bad-rune cost bloat) set useful output and waste.

**Two pathways (do not stack):**

| Pathway | Efficiency comes from | Formula feel |
|---|---|---|
| Direct skill cast | Skill η(L), Intelligence μ(INT), ambient `A` | `Useful = mana × 10 × η(L) × μ(INT) × A` |
| Rune / item path | Rune quality level → η_cond, host feel, ambient `A` | `Useful = mana × 10 × η_cond × A` |

These two rows are **alternatives, not a chain.** Never multiply η(L)/μ(INT) with η_cond on the same cast. Both may take the same ambient `A = √C`. Spell-worked tables: `../World/Science/Energy/ManaCast.md`.

**Stat-grant skills are never a multiplier.** Mana Shaping, Mana Regulation, Mana Absorption, Mana Reinforcement and kin only hand out flat INT/WIL (or similar). They raise output only by feeding `μ(INT)`. No second "shaping efficiency" term.

**Cost reducers act before conversion.** Rune Mastery (−10%/level, capped −90%) lowers mana **paid**. It is not a second output multiplier. It can stack with mana-in channels because both only touch the mana figure that then runs through exactly one pathway row above.

Electricity is the physical model for how mana **moves through material** (flow, paths, waste heat, burst dumps). Mana is not electricity. **Mana conductivity is entirely narrative** and does **not** follow electrical conductivity. Prime example: gold is an excellent electrical conductor, but converted **orihalcum** is antimagic and will not carry a rune path at all.

#### Mana conductivity (rune / item paths)

**Primary dial: rune quality level** (Lowest → Low → Intermediate → High → Highest; see `RuneSystem.md`). Locked as straight **20%** blocks of useful mana (`η_cond`). Waste = the rest (`1 − η_cond`) as heat / stray discharge.

| Quality | η_cond | Useful share | Waste share |
|---|---:|---:|---:|
| Lowest | **0.20** | 20% | 80% |
| Low | **0.40** | 40% | 60% |
| Intermediate | **0.60** | 60% | 40% |
| High | **0.80** | 80% | 20% |
| Highest | **1.00** | 100% | ~0% (practically no waste) |

Example at open ground (`A = 1`): **100** mana paid → converter input **1,000 J** → Intermediate Useful **600 J** / waste **400 J**.

Bad / low-quality runes can also show:

1. **Same activation cost, weak power:** paid mana is normal; low η_cond softens Useful (table above).
2. **High activation cost, average power:** the rune's **minimum** cost is bloated; you pay more to reach only middling Useful. Average output, expensive start.

Host material is a second **narrative** feel axis (dirty iron vs clean mythril), not a second percent ladder. Geometry still matters: longer or thinner paths resist more *and* heat worse.

**Heat away (scientific):** Waste still heats the channel. How fast that heat leaves uses real thermal conductivity, mass and geometry (`EnergyDesign.md`, `../World/Science/Metallurgy/OverheatedMetals.md`).

**Common path hosts (feel by job, not electrical rank):**

- **Iron:** workable but dirty. Heats and strains under flow.
- **Copper:** decent everyday path. Easy industrial stock.
- **Aurium:** keeps flow and **cuts waste** (damps / contains). Pipes, grips, linings. Detail: `../World/Materials/Metals.md`.
- **Steel / darksteel / star steel:** weapon and tool channels. Dark/star stock holds up better under rune damage / strain than plain steel.
- **Body / blood ink:** living path. Excellent handling; still breaks like flesh.
- **Mythril:** cleanest common host for reusable runic gear.
- **Orihalcum:** antimagic. Prime proof that mana conductivity ignores electricity: gold conducts current well; orihalcum swallows mana. Enchanting it is like projecting a movie onto black velvet: the image is swallowed and nothing seats. Not a rune host.
- **Adamantium:** carries little to no mana. Enchanting it is like projecting a movie onto clear glass: the image passes through and will not stick and its indestructible cast-final body will not take alteration. Not a rune host. It makes a great indestructible cover over a proper rune inlay (mythril or other real path metal underneath).

Direct casts never use η_cond. A mythril wand does not buff Mana Bolt; it only helps the **rune path** seated on it.

**Waste (locked):** Total waste = paid converter input × `(1 − η_cond)` (before ambient; `A` boosts Useful only). Split that waste **50 / 50**:

| Share | Goes where | Feel |
|---|---|---|
| **½** | Ambient | Leaves into the field / with the discharge as loose heat and stray mana |
| **½** | Weapon / path | Stays in the host as **heat damage** and **corruption** (strain, channel burn, rune rot) |

Example: Intermediate (`η_cond = 0.6`), **100** mana, `A = 1` → Useful **600 J**; waste **400 J** → **200 J** ambient + **200 J** into the weapon. Low quality + high flow cooks and corrupts hosts. Burst dumps can wreck a weak path in one shot. Heat-away after that uses real thermal conductivity, mass and geometry (`OverheatedMetals.md`).

#### Narrative path (when you are not doing joule math)

Seating quality, channel fill, heat under flow, strain, plate life, whether the inlay holds. Skill and setup still matter on the **paid mana** side (Rune Mastery discounts cost; sloppy seating ruins hosts). Craft ladders: `../World/Materials/Metals.md`.

## Open

None on η_cond / spiritual sites.

**Spiritual sites (locked feel):** as saturated as the narrative calls for, between ordinary ambient and dungeon thickness, maybe a little higher than ambient. No fixed `D` table. Dungeon floor ops stay in `../World/Geography/Dungeons.md`; `C`/`A` law: ManaConcentration.md.
