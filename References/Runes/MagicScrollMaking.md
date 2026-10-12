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

Creating a magic scroll costs half the mana cost of casting the spell. This mana imbues the magic ink into the paper.

```
craft_mana = 0.5 × cast_cost
```

`cast_cost` is the designed cast cost of that scroll (normal spell voice, or a stronger designed voice).

Example: A normal Mana Bolt costs **25 MP** to cast so its scroll costs **12.5 MP** to make. Fireball (Ball rung **400 MP**) costs **200 MP** to make. Fair Intermediate shelf **3 LS 2 SS** (`ScrollEconomy.md`).

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

Ink can also simply be powerful blood. Ink rules are more narrative than rigid.

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
| Mana Arrow | 250 | 125 | 84 | 63 | 50 |
| Mana Shield | 500 | 250 | 167 | 125 | 100 |
| Mana Ball | 2,000 | 1,000 | 667 | 500 | 400 |
| Spear Spells | 2,000 | 1,000 | 667 | 500 | 400 |

Bases for this table: Bolt **25**, Arrow **50**, Shield **100**, Ball / Spear **400**. Live body-cast Shield formula may differ (`ManaCast.md`); this sheet is the runic same-power activation ladder.

### Mana Input

Every rune has a lowest amount of mana needed to activate it. The user can supercharge it or add more mana because a rune is an artificial mana circuit.

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
- Do not set magic-scroll **power** from crafter `μ(INT)` alone. Power is **designed**; cast cost scales with it; craft is **half** that cast cost.
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
