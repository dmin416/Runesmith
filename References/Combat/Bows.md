# Bows

> **Design loot.** Metal law: `../World/Materials/Metals.md`. Silk / resilin: `../World/Science/Biomaterials/BiologicalSilks.md`, `../World/Science/Biomaterials/RubberAndInsect.md`. Threat-ladder KE feel: `AttackScale.md` (longbow row ~100 J). Kinetic runes: `../Runes/Energy.md`. Story gear lists stay in `../../Story/Notes/Items.md`.
>
> No aluminum / petroleum laminate. Limb and string jobs use wood, horn, sinew, star steel, Needle Worm silk and resilin.

## What Makes a Bow Strong

- **Stored energy** is the area under the draw-force curve. For the same peak draw weight, a curve that rises early and stays high stores more than one that ramps up slowly.
- **Efficiency** is the share of stored energy the arrow actually gets. The rest goes into moving the limbs and string. Lighter limb tips and a lighter string mean more energy in the arrow.
- **Arrow mass** sets where that energy lands. Heavier arrows take more of the bow's energy and penetrate better. Lighter arrows fly faster and flatter but waste more energy in the limbs.
- **The archer** caps peak draw weight. A bow can only be as strong as the arm drawing it, unless a machine spans it.

## Shapes Ranked

**Storage factor** = stored energy ÷ (peak draw force × power stroke). A plain linear spring scores 0.5. The theoretical perfect bow holds full force through the whole draw and scores 1.0.

| Shape | Storage Factor | Efficiency | Strengths | Weaknesses |
|---|---|---|---|---|
| Straight longbow (self bow) | ~0.45-0.5 | 65-80% | Simple, durable, one material | Long. Stacks hard at full draw. Hand shock. |
| Flatbow | ~0.5 | 70-80% | Wide thin limbs spread stress, so it survives with weaker wood | Still long |
| Reflex-deflex | ~0.55 | 70-80% | More early draw weight, less hand shock | Harder to build stable |
| Working recurve | ~0.55-0.6 | 75-85% | Short, fast, smooth draw | Tips can twist if poorly built |
| **Static recurve with siyahs** (Turkish, Manchu, Hungarian) | ~0.6-0.65 | 75-85% | Rigid tip levers gain leverage late in the draw. No stack. Holds the traditional flight record: Ottoman flight shots passed 800 m. | Needs composite construction |
| **Compound (cams)** | ~0.7-0.8 | 80-90% | Cams reshape the curve toward rectangular. Let-off cuts holding force by 65-90% at full draw. | Machined parts, string and cable wear |
| Theoretical ideal | 1.0 | Limited by limb mass | Constant force through the whole draw | Only approachable with cams |

**Best traditional shape:** static recurve composite. **Best possible shape:** compound with cams designed as close to a rectangular curve as possible. Steam-era machining / invent shop path: `../World/Science/Invent/MedievalIndustrialization.md`. Compounds are buildable once cams, cables and precise axles exist.

## Limb Materials: Energy Storage

A limb stores energy per kg of roughly σ² ÷ (2Eρ): strength squared over stiffness times density. A bent limb only reaches about a third of that in practice, since stress varies through its thickness. Less limb mass for the same energy means faster limbs and higher efficiency.

| Material | Ideal Storage (J/kg) | Practical Limb Storage (J/kg) | Verdict |
|---|---|---|---|
| Spring steel | ~700 | ~240 | Worse than wood per kg. Explains why real steel bows were heavy and slow. |
| Yew | ~900 | ~300 | Classic longbow wood |
| Horn (compression side) | ~2,600 | ~870 | Belly layer of composite bows |
| Sinew (tension side) | ~3,700 | ~1,200 | Back layer of composite bows |
| **Pure star steel, hardened** | ~2,500 | ~830 | Composite-class storage with huge toughness. Ideal for crossbow prods. Uses inspirational star-steel strength band in `../World/Materials/Metals.md`. |
| Mythril | ~180 | ~60 | Far too heavy and stiff. Inlays only. |
| **Needle Worm silk in shellac matrix** (low-hysteresis bow grade) | ~10,000-20,000 | ~3,300-6,600 | Best limb material in the setting. Direct analog of modern fiberglass and carbon laminate limbs. |
| Adamantium | 0 | 0 | Doesn't bend. Can't be a limb. Locked cast-final / no-bend in `../World/Materials/Metals.md`. |

Ordinary spider-type silk loses much of its stored energy as heat on recoil. Bow-grade Needle Worm silk has to be a low-hysteresis grade. Resilin returns about 95% and works as a thin energy-return layer (`../World/Science/Biomaterials/RubberAndInsect.md`).

## Rigid Parts: Where Adamantium Belongs

| Part | Best Material | Why |
|---|---|---|
| Riser (handle) | Adamantium with a resilin damping layer | Perfectly rigid and light. Undamped, it would ring like a bell after every shot. |
| Siyahs (static recurve tips) | Adamantium | Rigid levers that should weigh as little as possible. Cast with lashing grooves and rivet holes. |
| Cams and axles | Adamantium axles in star steel bushings | Zero wear, zero deformation, perfect cam geometry forever |
| String and cables | Needle Worm silk, high-modulus low-stretch grade | Light string adds efficiency. Stretch wastes energy. Real analog is Dyneema. |
| Arrow shaft, traditional bow | Wood or silk composite | Must flex correctly around the riser |
| Arrow shaft or bolt, compound or crossbow | Adamantium hollow tube | Never breaks, reusable forever. A center-shot bow or crossbow doesn't need shaft flex. |
| Armor-piercing head | Adamantium bodkin | Never deforms, so every joule stays focused on the point |
| Cheap armor-piercing head | Durasteel bodkin | Hard enough to stay pointed on impact. Brittleness matters little on a single-use head. |
| Hunting broadhead | Star steel or adamantium | Tough wide edge, or permanently sharp |

## Draw Force Dial (Strength)

**Design dial:** peak draw force scales about **245 N (55 lbf) per 15 Strength**. Street baseline STR 15 sits on the strong side of untrained hunting-bow feel; retune later only if a beat needs softer street bows. Power stroke **0.6 m**. Arrow mass scales with draw weight (real archery practice), so arrow speed holds around **90-100 m/s** while energy climbs.

Storage × efficiency used for the table: static recurve mid-band (~0.625 × ~0.80), compound mid-high (~0.75 × ~0.88).

| Strength | Peak Draw | Static Recurve Arrow Energy | Compound Arrow Energy | Arrow Mass (Compound) |
|---|---|---|---|---|
| 15 (average) | 245 N (55 lbf) | ~73 J | ~97 J | ~21 g |
| 30 | 490 N (110 lbf) | ~146 J | ~195 J | ~42 g |
| 45 (English warbow class) | 735 N (165 lbf) | ~219 J | ~292 J | ~63 g |
| 75 | 1,225 N (275 lbf) | ~365 J | ~487 J | ~105 g |
| 150 | 2,450 N (550 lbf) | ~729 J | ~975 J | ~210 g |

A real 150 lbf English warbow put about 120-130 J into a ~95 g arrow. A Strength 150 archer with an ideal compound puts nearly 1 kJ into an arrow the weight of a light javelin. `AttackScale.md` longbow ~100 J is the street-band threat row (matches STR 15 compound / strong static).

**Limb mass for the Strength 150 compound (~1,150 J stored):**

| Limb Material | Limb Mass Needed |
|---|---|
| Yew | ~3.8 kg (too slow, efficiency collapses) |
| Pure star steel | ~1.4 kg |
| Horn-sinew | ~1.2 kg |
| Needle Worm silk composite | ~0.2-0.35 kg |

Only silk composite keeps the limbs light enough to hold high efficiency at superhuman draw weights.

## Crossbows: Past the Archer's Limit

- Spanning devices (windlass, cranequin) multiply force mechanically, so draw weight is no longer capped by Strength.
- Short power stroke (~15 cm) means very high draw force for modest energy. A medieval 1,000 lbf steel crossbow stored about 330 J and delivered around 150 J, since its heavy steel prod wasted most of the energy.
- A pure star steel prod stores about 3.5× more energy per kg than mundane spring steel. That lightens the prod and raises efficiency sharply.
- A recurved silk-composite prod is lighter still and gives the strongest crossbow possible.

## Beyond Physical Limits

Canon mana converts into kinetic motion with little loss. A kinetic rune adds energy beyond any limb material or archer. Mythril rune lines run on inlays in the riser, since adamantium can't host runes, and an etherium cell powers them. Past that point, the limits become arrow survival under acceleration and the archer's mana budget rather than bow physics. Useful pricing follows `../Runes/Energy.md` (η_cond × A).

## Open

- Soften STR 15 → 55 lbf if street bows need to read lighter
- Promote bow-grade Needle Worm silk (low-hysteresis) into biomaterial locks when Ned / silk craft beats need it
- Compound invent timing vs Caldris shop tech
