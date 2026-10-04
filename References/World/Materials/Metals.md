# Metals

> Shop metallurgy: `../Science/Metallurgy/CraftMetal.md`. Property formulas / animal mats: `../Science/Biomaterials/Biomaterials.md`. Path efficiency from mana conductivity: `../../Runes/Energy.md`.

## Narrative

Terra is basically Earth for materials. Same mundane stock. Development is extremely lopsided because of magic and monsters. Magical grades depend on mana saturation, and the ladder differs by metal. Iron and steel have the most steps. Silver has fewer. Titanium is only known in full saturation as orichalcum. More metals exist; these are the ones locked first.

## Detail

**Baseline:** Earth-like material world. Same ordinary metals and ores exist. Copper, gold, bronze, and the rest stay Earth-like until their saturation ladders are locked. Brass craft: `../Science/Metallurgy/Brass.md`.

**Skew:** Magic and monsters push tech and craft onto a lopsided track. Not a different periodic table.

**Rule:** Saturation ladders differ by material. Some stay grades. Some full-saturate into a new named material.

**Naming:** Prefer one public name per role. Do not keep a parade of near-synonyms for steel grades (dark steel, deep steel, black steel as separate metals). Extra labels are shop grades or dead aliases. Mana iron / mana steel and refined mana iron / refined mana steel are the live saturation names.

**Rune hosts:** Basically anything can hold a rune. Setting pushes mana into the material through an inlay or engraving channel that must be filled to make the rune. Setting and activation are different.

**Non-metal hosts:** Bone, hide, scale, and gem paths are real. They are usable rune hosts, not metal-only.

**Poor hosts:** Materials that handle mana poorly, or take too much energy while being imbued, can be ruined by **setting alone**, not only by activation. Plain steel and similar are in this danger band.

**Corruption damage:** Any mana movement is technically unnatural. Runes are autopilot mana movement, so they cause secondary host harm more easily than intention-based magics. Mana moving in or next to a poor host can locally superheat and burn it. Harm is not guaranteed every time. Thermal reference: `../Science/Metallurgy/OverheatedMetals.md`.

**Craft path vs skill:** Rune / item paths use **mana conductivity** for η_cond (`../../Runes/Energy.md`). Direct skill casts use η(L) × μ(INT) only. Narrative path covers seating, geometry, heat, and strain when joule math is off-page.

### Iron / steel

Most levels.

| Saturation | Name | Notes |
|---|---|---|
| Mundane | Iron / steel | Ordinary stock |
| Slight | Mana iron / mana steel | Light mana saturation |
| Heavy | Refined mana iron / refined mana steel | Heavy mana saturation |
| Full | Adamantium | Different material. **Once cast: indestructible** to ordinary force. Cannot be enchanted. Runic inlays OK. Final shape. Destroy only by resonant sound or mana vibration. |

### Adamantium (flex and form)

**Lock:** Cast adamantium is **indestructible** (ordinary force). Not forgeable supersteel after set.

**Core rules once cast and cooled:**

- Indestructible to ordinary force. Only resonant sound or mana vibration destroys it
- **Bends but never stretches.** Axial length under pull is fixed. No plastic set. Every flex springs back to the exact cast shape
- Stiffness well above steel. Human blows never reach the stretch limit on thick stock, so blades and plate feel rigid

**Why thickness decides bend:**

Bending stretches the outer fiber and compresses the inner. Adamantium allows only a tiny surface strain before it stops dead.

```
ε_max = 0.001          // 0.1% stretch limit (~1/5 of spring steel)
R_min = (t / 2) / ε_max = 500 × t
```

`t` = thickness. `R_min` = tightest bend radius to the neutral surface.

| Thickness t | R_min | Feel in use |
|---|---|---|
| 0.02 mm | 1 cm | Silk-like thread |
| 0.1 mm | 5 cm | Fine cloth thread |
| 1 mm | 50 cm | Stiff wire |
| 5 mm | 2.5 m | Blade: rigid in the hand |
| 20 mm | 10 m | Plate / vault stock: rigid |

**Flexible forms** (all shaped while the filament is still setting):

| Form | Behavior |
|---|---|
| Adamant thread | Drawn from the melt before set. Thread, wire, bowstring |
| Adamweave | Woven to final shape while setting. Drapes and folds. Zero give under pull |
| Adamant knit | Loops give until they pull straight, then stop hard |
| Adamant cord | Braid / twist while setting. Bends around anything. Never lengthens, snaps or frays |
| Adamant mail | Rings of filament or wire. Flex at the links. Each ring stays rigid |

Fine Adamweave shirt about **1–2 kg**. Mail heavier.

**Forming rules:**

- Shape is final when set. No cut, hem, resize or repair afterward. Weave or knit the finished garment, rope or net while it sets
- Destroyed means gone. No patch
- Resonance pitch falls as thickness rises. Thin cloth dies to a shrill tone. Plate needs a deep one. Mixed thread sizes in one cloth = many pitches = easier accidental kill

**What it does not stop (force still reaches the body):**

- Blunt impact through uncut cloth (ribs, bruise)
- Thrust that drives the weave into flesh without piercing it
- Conducted heat (conducts like steel; cloth does not burn but the wearer can)
- Crush and constriction (unbreakable net still squeezes)

**Zero-stretch consequences:**

- Climbing / fall arrest: full jolt, no rope stretch. Cord survives. Bones may not. Real climbing rope stretches on purpose
- Bowstring: ideal. Draw energy goes into the arrow
- Restraints and nets: no wriggle-stretch escape
- Armor cloth: spreads the hit across the weave. Wearer still takes the force

**Uses:** Adamweave linings and undershirts, cord / rigging / restraints, bowstrings, nets, sails, straps, bags, mail.

### Silver

| Saturation | Name | Notes |
|---|---|---|
| Mundane | Silver | Ordinary stock |
| Magical | Mana silver | Mana-saturated silver |
| High / full | Mythril | **Saturated silver** (shop Ag–Cu). Extremely mana conductive. Best common rune host below aetherium. **Not titanium.** |

**Lock:** Mythril is silver-line. Orichalcum is titanium-line. Never swap them.

**Elemental mythril:** Mythril can take elemental alignment. No special public variant names for now (not “red mythril” as a separate brand). Elemental versions stay **mythril only**, not every magic metal.

### Titanium

| Saturation | Name | Notes |
|---|---|---|
| Full only (known) | Orichalcum | **Antimagic** metal. Magical titanium. Mundane titanium is not the public form people know. Will not take enchantments. Runic inlays are possible but proximity interferes; not smooth. **Not mythril.** Not a reduced-η wire path. |

### Aetherium

**What:** Refined mana stones.

**Role:** Best mana flow known. Above mythril for conduction.

### Arcanium

**What:** Brittle mana crystal (wand / staff / rune-plate stock).

**Role:** Very high mana conductivity. Too fragile for blades or armor. Distinct from aetherium (refined stone metal/path stock); arcanium is the crystal form used in foci and plates.

### Etherium

**What:** Spirit / ether condensed metal.

**Role:** Persistent store and spirit-leaning craft stock. Light, hard to work with ordinary fire. Used in alloys and specialty gear when the story needs it.

### Enchantment refusals

Adamantium and orichalcum refuse enchantments. Runes are the workaround path (orichalcum still interferes by proximity).

### Property anchors (planning)

Units: c in J/g·K, k in W/m·K, melt °C, hardness Mohs unless noted, ρ in g/cm³. Alloy bands vary.

**Mundane (Earth-like):**

| Metal | c | k | Melt | Hardness | ρ |
|---|---|---|---|---|---|
| Iron | 0.45 | 80 | 1538 | 4 | 7.87 |
| Steel | 0.49 | 50 | 1370–1510 | 4–6.5 | 7.85 |
| Copper | 0.39 | 401 | 1085 | 3 | 8.96 |
| Bronze | 0.38 | 50 | ~950 | 3 | 8.8 |
| Silver | 0.24 | 429 | 962 | 2.5 | 10.5 |
| Gold | 0.13 | 318 | 1064 | 2.5–3 | 19.3 |
| Lead | 0.13 | 35 | 327 | 1.5 | 11.3 |
| Tin | 0.23 | 67 | 232 | 1.5 | 7.3 |
| Zinc | 0.39 | 116 | 420 | 2.5 | 7.14 |
| Nickel | 0.44 | 91 | 1455 | 4 | 8.91 |
| Platinum | 0.13 | 72 | 1768 | 3.5 | 21.5 |
| Electrum | ~0.17 | 70–100 | 1000–1050 | 2.5–3 | 13–16 |
| Mercury | 0.14 | 8 | −39 | liquid | 13.5 |

**Named magic stock (purpose-fit numbers, not lab law):**

| Material | Mana flow | c | k | Melt | Hardness | ρ |
|---|---|---|---|---|---|---|
| Mythril | Excellent (best common host below aetherium); saturated silver / Ag–Cu | 0.24 | 300 | ~779 shop eutectic | 5.5 | ~10 |
| Orichalcum | Very poor (antimagic); magical titanium | 0.52 | 22 | ~1668 | 6 | 4.5 |
| Adamantium | Excellent inlay path; refuses free enchant | 0.47 | 50 | ~1540 cast | Indestructible once set (not forge-HT stock) | 8.0 |
| Aetherium | Best metal/path flow | - | - | - | - | - |
| Arcanium | Highest (brittle crystal) | 0.80 | 1.5 | ~1700 | 6.5 | 3.0 |
| Etherium | High spiritual | - | - | not normal fire | ~2 | ~0.3 |

### Star metal

Meteoric nickel-iron. Dark gray, etched lattice. Holds an edge past steel. Resists outside enchantment. Often harms spirits / extraplanar. Hard to forge (sulfide cracks, poor forge-weld). Scarce supply; smiths may fold with other stock to stretch it. Seals, prison bindings, heirloom blades.

### Ebonite (shadow ore path)

**Separate from** iron saturation grades. Mana iron / mana steel stay on the iron ladder above. Ebonite is its own black ore line.

| Grade | Feel | Role |
|---|---|---|
| Unrefined ebonite | Stronger than iron, brittle, weak shadow affinity | Heavy weapons, plate, dungeon fittings |
| Refined ebonite | Denser, matte light-absorbing, amplifies shadow / fear / necro when the story needs it | Military / stealth blades and armor |

Needs a hotter forge than plain iron. Higher refine may carry cold aura or nightmare side effects if locked in prose later.

### Relative rank (feel)

| Material | Strength | Weight | Mana | Rarity feel |
|---|---|---|---|---|
| Mythril | High | Light | Very high | Rare |
| Orichalcum | High | Light | Anti | Very rare |
| Adamantium | Indestructible (cast-final) | Heavy | High inlay path / no enchant | Legendary |
| Star metal | Very high | Heavy | Resist enchant | Very rare |
| Unrefined ebonite | Med-high | Heavy | Low shadow | Uncommon |
| Refined ebonite | High | Very heavy | Med shadow | Uncommon |
| Arcanium | Low (brittle) | Light | Highest | Rare |
| Etherium | Low | Very light | High spirit | Very rare |

## Open

- Other metals’ saturation ladders
- Ebonite ore geography and exact side-effect locks
- Star metal drop / hunt economy
