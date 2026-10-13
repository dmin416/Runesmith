# Magic Scroll Making Rules

> **Lock.** Spell costs, energy figures and spell descriptions: `../Combat/KineticSpellList.md`. Live cast voices / Bolt–Arrow tables: `../World/Science/Energy/ManaCast.md`, `Energy.md`. Named blurbs: `../Combat/Spells.md`. Shop coin: `ScrollEconomy.md`. Quality split (scroll grade ≠ rune `η_cond`): `ScrollAspects.md`.

## Scroll Groups

Scrolls are divided into two main groups:

1. Magic Scrolls
2. Runic Scrolls

## Magic Scrolls

Magic scrolls are more like an enchantment. The words of the chant needed to activate the magic are written on the scroll.

### Activation

Magic scrolls have to be used by mages because non-mages cannot push mana. The written words must be read. Reading them mobilizes the reader's mana to cast the spell.

### Scroll Durability

Normal paper burns up when the spell is cast. A magic scroll on normal paper is single use.

Magic paper lasts between 2 and 5 uses.

Magic paper has a threshold of mana it can bear. The tier of the paper determines its threshold.

### Paper Tiers

Paper tiers match spell tiers.

1. **Same tier:** Tier 1 paper can carry Tier 1 spells, the most basic spells. It can cast at least one and usually a couple.
2. **Lower tier spells:** Higher tier paper can carry more casts of lower tier spells.
3. **Higher tier spells:** Spells that require very high amounts of mana require paper of their tier or above. Lower tier paper cannot carry them. Every cast adds to the total mana that has passed through it. Once that total passes the threshold the paper burns up. A scroll that casts heavier or supercharged spells reaches its threshold in fewer uses.

### Requirements

Making a magic scroll requires castability of the spell. This means the scribe needs at least a Tier 1 mage class and the Mana Scribe class.

Making any scroll of Tier 2 or above requires a Tier 2 or above mage class with knowledge of the spell.

### Creation Process

1. Paper or another writing surface
2. Ink
3. Drawing the chant for the spell
4. Imbuing it with mana

### Creation Methods

Magic scrolls can be made in two ways:

1. **Write then imbue:** The chant is written out first and then imbued with mana.
2. **Imbue while writing:** The ink on the pen is imbued with mana and then written. This method is more difficult and requires more focus. It spreads out the mana usage so it is not all spent at once. It is the more common method.

### Creation Cost

Creating a magic (word) scroll costs the **same mana as casting** that designed spell, then **Basic Mana Scribing** cuts the pour:

```
list = cast_cost                         // designed voice / strength
S    = 1 − 0.1 × Mana_Scribing_L         // L0 = 1.0; L1 = 0.9; L9 = 0.1
paid = list × S
```

`cast_cost` is the designed cast cost of that scroll (normal spell voice, or a stronger designed voice).

Example: Mana Bolt **25** → L0 pay **25**, L1 pay **22.5**, L9 pay **2.5**. Fireball (Ball rung **400**) → L0 **400**, L1 **360**. Fair Intermediate shelf **3 LS 2 SS** (`ScrollEconomy.md`) still uses shop labor tables; retune if throughput feels wrong under full-cast craft.

**Craft XP (locked forward):** overall XP = **`cast_cost`** (ignore S). Word and runic share that XP rule. `../Progression/ExperienceCurve.md`.

Old `craft = 0.5 × cast` is **dead**.

### Elemental Affinity

The mage who imbues the spell imbues their elemental affinity into the paper.

### Paper

The paper does not need to be magical. Magic paper does not change the mana cost of creation. Any effect it has on creation is narrative. Magic material is harder to imbue because its latent mana disrupts the process. It requires more focus but no more mana. Non-magic paper is easier to imbue but burns up after one use.

Magic paper lasts between 2 and 5 uses instead of burning up after one. It burns up once the mana passed through it exceeds its threshold. The tier of the paper determines that threshold.

### Ink

Magic ink is something that helps establish the mana channel. It is imbued and then set into the scroll, paper or other surface.

Magic ink can be made from:

1. Mana stone
2. Beast blood
3. Human blood from a magical human

For mana stone ink, quality depends first on the amount of crushed mana stone in the ink and second on the quality of that stone.

**Powdering a magic stone (Ch 21.5 Notes):** intact stones are normally extremely robust and durable. Roland finds two ways to get powder. (1) **Drain** all mana out of the stone → it becomes crumbly and powders cleanly. (2) **Overload** it hard → also shatters, but extremely violent, noisy, and hard to collect the pieces. Drain is the practical ink path.

Ink can also simply be powerful blood. Ink rules are more narrative than rigid. Cheap beast blood on Terra is **Trox blood** (substance lock: `../World/Science/Body/BloodNotes.md` § Trox). Not cow or ox.

**Ch 21.5 (chapter):** Roland reads street cheap ink as a **magical substrate + crushed magic stones**. Shop cheap bottle under Sense matches dank/fetid mana color of goblins and sewer rats; thin, dark, rust / dried-iron smell. He plans to brew his own rather than keep buying.

**Ch 21.5 (Notes):** Homemade ink = **his blood + Ned's blood + powdered goblin cores** from his stone-bank stock (powder via drain-to-crumbly; overload shatter works but violent/noisy/hard to collect). Not Trox / butcher blood. Fire Orb on rough hide reaches trial-level working seating fast; pour cost ~same band, quality clearly above trial/shop-cheap. Water segment isolated from Aqua Ball and light from Orb of Light basically at once after that. Form kit after Arrow + Ball + Orb: shared Orb/Bolt shape, Ball (bigger), Arrow; small-mana compression → Bolt, moderate-mana compression → Ball. System Mana Bolt has no detect-contact rune; pop = compression undoing on denser-than-air hit. Ratio experiments: segment size ratios dominate processing; forced ratio tweaks barely nudge size/effect and are inefficient; whole-diagram shrink cuts mana in and power out; enlarging the simple compression alone tends to implode Bolt rather than a fiercer explosion. Component swaps succeed far better: Aqua Ball → Fireball almost laughably easy; same for water arrow and light ball; lazy unmodified-ratio grafts still Diagnosis-readable unless the paper spontaneously burns (occasional). Skill rise gives a vague clock-mechanism feel for how other runes might need to change and familiarity on sight, not a brain dump (`RuneCauseEffect.md`, `../Combat/BasicSpellShapes.md`).

**Quality-only seating (Ch 21.5):** Trial Fire Orb took **~3** tries to Highest; first night in town took **~2–3** tries to a working scroll. **After that**, seating is known — every try finishes a scroll. The only question is **quality rank** (Lowest → … → Highest). New sibling forms climb **fast and linearly** (circle→square). Mats die to quality remakes and refuse-below-High, not fail cascades.

**Seat time (Ch 21.5 Notes lock):** `wall ≈ draw + paid / tip_sip`. Tip-sip **~21.1 MP/min**; known Arrow draw **~5 min**; Ball draw **~15 min**; `paid = (cast / η) × S`. Highest Arrow wall **~6 min**; Highest Fireball wall **~21–26 min** (RS L4–L7). Phase C mix **~70%** Mana Arrow keep / **~25%** Fireball sell / **~5%** Light Ball → **~85** clean seats/day at RS **L8**, **~1.7–3k MP**/day (draw-limited, under **~12.6k** tip-sip ceiling). Skip exit **~4 months / d120**. **Prefill:** when MP or SP is full, overflow may preload **personal keep** or **gift** scrolls only (**1.31 ×** activation); sell-line Fireballs stay empty. Seat counts unchanged. Full table: `../../Story/Notes/Chapter21_5.md`.

The main purpose of better magic ink is to allow more mana. Ink quality determines the amount of mana that can flow into the spell. Better ink carries more mana which raises the upper threshold for the highest level of spell that can be made.

Better ink can also reduce the mana cost of making the scroll.

Ink does not affect spell complexity. Complexity depends only on the scribe's knowledge, the writing and the accuracy of the runes.

### Spell Power

Magic scrolls are as powerful as the mage who made them designs them to be. More mana means a stronger spell but a higher cost to cast it.

Example: A normal Mana Bolt scroll costs **25 MP** to cast. A supercharged Mana Bolt scroll written by an archmage is twice as powerful and costs **50 MP** to cast.

Shop device grades Lowest → Highest rate designed attacking value / cast cost. They are **not** rune `η_cond` and **not** a seating-inefficiency dial.

## Runic Scrolls

Runic scrolls use runes instead of drawn chants. The runes are actual artificial magical pathways.

### Activation

The user does not need to be a mage to cast a runic spell. Non-mages cannot push mana, which is why they cannot use magic scrolls and must use runic scrolls instead. How the spell is powered depends on its style.

### Runic Spell Styles

Runic spells have two styles:

1. **Absorbing:** The user activates it and the runes draw power from the user to cast the spell. Mages can push their mana through the runes. Non-mages power it with their stamina.
2. **Preloaded:** The spell is already stored in the runes. The scroll creator or item creator preloads it. The moment the user activates it the stored spell is released. Activation can be narrative or physical, such as squeezing it, tearing it, holding it out in front of the user or adding one small symbolic piece of energy.

### Rune Efficiency

Runes are as efficient as they have been designed to be. Efficiency is a quality grade. It is separate from spell tiers. Efficiency is divided into 20% blocks from lowest to highest:

1. Lowest: 20%
2. Low: 40%
3. Intermediate: 60%
4. High: 80%
5. Highest: 100%

Runes below Highest have lower efficiency. For the same payment they produce less power. More usually they cost more for the same power.

### Runic Activation Cost by Efficiency

Rune cost for the same power = base MP ÷ efficiency, rounded up to whole MP.

| Spell | 20% | 40% | 60% | 80% | 100% |
|---|---|---|---|---|---|
| Mana Bolt | 125 | 63 | 42 | 32 | 25 |
| Orb (Fire Orb / Orb of Light rung) | 125 | 63 | 42 | 32 | 25 |
| Mana Arrow | 250 | 125 | 84 | 63 | 50 |
| Mana Shield | 500 | 250 | 167 | 125 | 100 |
| Mana Ball | 2,000 | 1,000 | 667 | 500 | 400 |
| Spear Spells | 2,000 | 1,000 | 667 | 500 | 400 |

Bases for this table: Bolt **25**, **Orb 25**, Arrow **50**, Shield **100**, Ball / Spear **400**. Same designed mana bill for Orb and Bolt. Runic geometry: shared Orb/Bolt shaping; Bolt = small-mana compression, Ball = moderate-mana compression, Orb = soft restraint; Bolt pop is compression undoing, not a contact-detect rune (`../Combat/BasicSpellShapes.md`, `RuneCauseEffect.md`). Live body-cast Shield formula may differ (`ManaCast.md`); this sheet is the runic same-power activation ladder.

### Mana Input

Every rune has a lowest amount of mana needed to activate it. The user can supercharge it or add more mana because a rune is an artificial mana circuit.

### Runic scroll craft: paid cost (good → bad)

Word-scroll craft is full cast × Mana Scribing S (above). **Runic** scroll pours use the same-power list, then Rune Scribing S:

```
list = cast_cost / η_cond          // η_cond = quality 0.20 … 1.00
S    = 1 − 0.1 × Rune_Scribing_L   // L0 = 1.0; L1 = 0.9; L9 = 0.1
paid = list × S                    // clean pour, no botch
```

**Craft XP** = `cast_cost × quality_mult` (ignore S and η for the XP line). Quality mult: Lowest **1** · Low **2** · Intermediate **4** · High **8** · Highest **16** (`../Progression/SkillRanks.md`). S and η still change **what you pay**, not the base cast in the XP product.

| Quality | η_cond | List vs cast | Feel |
|---|---|---|---|
| Highest | 1.00 | **1×** | Clean machine; pay near designed cast × S |
| High | 0.80 | **1.25×** | Good shop work |
| Intermediate | 0.60 | **~1.67×** | Competent pass; trial success band |
| Low | 0.40 | **2.5×** | Sloppy but usable |
| Lowest | 0.20 | **5×** | Barely seated; expensive for the boom |

**Skill band (clean pour):** L1 cuts **10%**; L9 cuts **90%** (pay one-tenth of list). Class “eases learning” does **not** cut this bill.

#### Orb / Bolt rung worked (`cast = 25`)

| Pour | η | S | **Paid** | Notes |
|---|---|---|---|---|
| Best clean (Highest L9) | 1.00 | 0.1 | **2.5** | Master scribe, perfect schematic |
| Good clean (Highest L1) | 1.00 | 0.9 | **22.5** | First ranks, perfect pattern |
| Intermediate L1 | 0.60 | 0.9 | **~38** | Solid working scroll |
| Lowest L1 | 0.20 | 0.9 | **~113** | Weak seating; still a controlled pour |
| Lowest L0 (no skill) | 0.20 | 1.0 | **125** | Full list |

**Botch / cascade (worse than Lowest):** a runaway ink feed or wrong pour method can burn far past the Lowest list. Effective η falls below **20%**. Scale:

```
η_eff ≈ (cast × S) / mana_burned
botch_vs_Lowest ≈ mana_burned / (cast / 0.20 × S)
```

#### Chapter 16 Fire Orb trial (worked example)

Pool ≈ **2292**. Temp skills **L1**. Designed Orb **25**.

| Attempt | What happened | Paid (read) | Implied |
|---|---|---|---|
| 1st | Slow hand pour; Diagnosis red / fail (“turd”) | **~113** if Lowest clean (“frugal”) | Paid for a bad seating; scroll unusable |
| 2nd | Mana-hand cascade / Pollock | **~¼ pool ≈ 573** (on-page) | η_eff ≈ **4%** (~**5×** Lowest L1 bill, ~**15×** Intermediate L1) |
| 3rd | Methodical pass; scroll works | **~38** if Intermediate L1 | Clean Intermediate; not another ¼ |

Session total under that read: **~113 + 573 + 38 ≈ 724** (~**32%** of pool). On-page “another ¼” on the success is looser narrative; Intermediate L1 is the cost law for a competent working scroll.

**Takeaway:** good process spans about **2.5 → 125** MP on the Orb/Bolt rung (Highest L9 → Lowest L0). Bad process is unbounded upward: one cascade can cost **many times** a Lowest pour and still fail. Mats and time die with fails; XP only lands on a finished scroll at `cast_cost`.

### Scroll Durability

Runes on a scroll are almost always destroyed within one use.

## Casting Damage

Casting a spell damages the material it passes through. The type of damage depends on the material.

1. Paper burns.
2. Steel suffers corruption and turns brittle the way it does at very high temperatures.
3. Bronze and brass get hot overall and eventually wear down. They can also suffer corruption like steel where hyper-focused local heating causes damage or microfractures.

Metals have durability. Unlike paper they survive multiple casts. Magic metal is harder to imbue for the same reason as magic paper: its latent mana disrupts the process. It requires more focus but no more mana. Each cast adds corruption or wear until the metal fails. Every metal reacts a little differently. Detailed notes for each metal are kept separately (`../World/Materials/Metals.md`, `ManaMaterials.md`, `Energy.md`).

### Corruption

Corruption is localized damage. It is not just the metal getting hot. A single particle of mana shoots through the metal mana channel and damages the nearby metal, similar to radiation hurting a person as it punches through.

## Maker Sheets (economy)

Baseline classed pools for shop throughput (`ScrollEconomy.md`):

| Scroll tier | Classes | INT / Will | MP = `day_mana` |
|---|---|---|---|
| T1 | Mage L25 + Mana Scribe L25 on body **15/15** | **65 / 65** | **910** |
| T2 | + Elemental Mage L25 | **115 / 115** | **1,610** |

Workday **10 hours** seated. Spendable craft mana / workday **= MP**.

## Forbidden

- Do not treat magic-scroll craft as `spell × I` seating waste.
- Do not set magic-scroll **power** from crafter `μ(INT)` alone. Power is **designed**; cast cost scales with it; word craft list is **full** cast, then Mana Scribing S.
- Do not use dead `craft = 0.5 × cast`.
- Do not require magical paper for creation. Magic stock changes focus and use-count, not craft MP.
- Do not treat scroll device grade as rune `η_cond`.
- Do not invent LC-per-mana tariffs.

## Cross-links

- Quality names vs rune efficiency: `ScrollAspects.md`
- Prices / labor: `ScrollEconomy.md`
- Families / buyer fuel: `Magic.md`
- Spell→scroll vs rune gate: `SpellToCraftGate.md`
- Craft scrapes: `ScrollCraftScrapes.md`
- Paper stock: `../World/Science/Invent/Paper.md`
- Class packages: `../Progression/ClassPackages.md`
