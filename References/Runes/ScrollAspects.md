# Scroll Quality vs Rune Quality (Lock)

> **Do not conflate.** Scroll quality and rune quality are different measures. Same five grade names (Lowest → Highest) do not make them the same dial.

## Rune quality

**What it is:** how perfect the rune is (pathway seating, form fidelity).

**What it does:** sets **efficiency** on the rune / item path: `η_cond` in `Energy.md` (Lowest **0.20** → Highest **1.00** in 20% blocks).

**What it is not:** spell tier / rune rank. Not scroll attacking strength. Not host-metal "feel."

## Scroll quality

**What it is:** a device-checked grade of the scroll product’s **overall strength** (word scrolls and runic scrolls both use the label).

**What it is not:** how perfect a rune drawing is. Not `η_cond`. Not spell tier / rune rank by itself.

Chapter prose still says more mana into writing → stronger scroll. Craft law below is rewrite notes: **efficiency**. Until chapters are rewritten, chapter prose wins on-page.

## Craft mana = spell cost / efficiency (Lock)

Word-scroll craft seats a finished cast. The scribe pays the **spell’s mana cost** at Highest efficiency, and **pays extra** when seating is poor.

```
pour = spell_cost ÷ η_craft
```

| Scroll quality | η_craft | Pour (× spell cost) |
|---|---|---|
| Lowest | **0.20** | **×5** |
| Low | **0.40** | **×2.5** |
| Intermediate | **0.60** | **×1.667** |
| High | **0.80** | **×1.25** |
| Highest | **1.00** | **×1** |

Same 20% blocks as rune `η_cond` names; this dial is **craft seating efficiency** (`η_craft`), not rune path `η_cond`.

**T1 Mana Arrow:** spell cost **50** (`ManaCast.md` normal voice). Pours: Lowest **250** / Low **125** / Intermediate **≈83.3** / High **62.5** / Highest **50**.

**T2 Fire Arrow:** spell cost **50** (Arrow-scale until ManaCast pins elemental voice). Same pour row as Mana Arrow.

**T2 Fireball:** spell cost **100** (craft lock; body voice still open in ManaCast). Pours: **500 / 250 / ≈166.7 / 125 / 100**.

Low quality costs **more** mana and still grades weak. Highest costs the spell once and grades strong. Fair shelf tags: High/Highest **above** Intermediate (scarcity); Lowest/Low **below** Intermediate (junk loss). Full coin tables: `ScrollEconomy.md`.

## Baseline word scribes (Lock)

**15 is the untrained adult body**, not a classed scribe (`../Progression/Attributes.md`, `Training.md`). Classes add packages (`ClassPackages.md`).

### T1 scrolls (Mana Arrow and other T1 word)

Requires **Mage + Mana Scribe**.

| Layer | INT | Will |
|---|---|---|
| Body (street adult) | **15** | **15** |
| Mage L25 | **+25** | **+25** |
| Mana Scribe L25 | **+25** | **+25** |
| **Total** | **65** | **65** |

**MP = 910** (`INT×10 + Will×4`). Skill pads (Calligraphy, Regulation, …) not in this floor.

### T2 scrolls (Fire Arrow, Fireball, …)

Requires **T2 elemental Mage** (affinity path) after Mage + Mana Scribe.

| Layer | INT | Will |
|---|---|---|
| Body | **15** | **15** |
| Mage L25 | **+25** | **+25** |
| Mana Scribe L25 | **+25** | **+25** |
| Elemental Mage L25 (T2 ×1.5→**+2**/level) | **+50** | **+50** |
| **Total** | **115** | **115** |

**MP = 1,610**.

### Workday / regen

| Dial | Lock |
|---|---|
| Workday | **10 hours** seated |
| Spendable craft mana / workday | **= MP** (one pool + light seated top-up; not max still-skin multi-fill) |
| T1 `day_mana` | **910** |
| T2 `day_mana` | **1,610** |

Mage card / Blessed (INT ≥ 40 on these sheets) stay narrative recovery. Economy meter is `day_mana` above.

**Bind:** pool binds. Mana Arrow ~**10 min** does not bind Intermediate+ on these sheets.

## Other dials (still separate)

| Dial | Notes |
|---|---|
| **Materials** | Blank, ink, host |
| **Crafter** | Skills, affinity gates |
| **Tier / rank** | Spell tier 1–5, or rune rank Lesser → Legendary |
| **User fuel** | Word: mana to read. Runic: mana or stamina; amp to rank ceiling |

## Forbidden

- Do not treat scroll quality as rune quality or as `η_cond`.
- Do not treat rune quality as scroll attacking strength.
- Do not use bare INT/Will **15** as a classed scribe.
- Do not make Highest pour the most mana. Highest is **η = 1**; Lowest pays **×5** spell cost.
- Do not invent LC-per-mana tariffs.

## Cross-links

- Prices / labor engine: `ScrollEconomy.md`
- Craft scrapes: `ScrollCraftScrapes.md`
- Families: `Magic.md`
- Rune efficiency: `Energy.md`
- Rank ceilings: `RuneSystem.md`
- Class packages: `../Progression/ClassPackages.md`
- Resources: `../Progression/Attributes.md`
