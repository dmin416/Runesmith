# Cookware and Knives

> **Food domain.** Material picks and kitchen physics for pans and blades. Production methods: `KitchenCraft.md`. Gear lists: `KitchenKit.md`. Seasoning / enamel / metal-pan care: `BioFriendlyNonStick.md`. Metal **law** stays in `../World/Materials/Metals.md` (wins on conflict). Potency pans: `MagicalMeatCookware.md`.
>
> **Setting constraints:** no aluminum, no petroleum, no synthetic nonstick. Recommendations use the setting's metals, glass enamel (silica does not convert) and Needle Worm materials.
>
> **Lock vs feel:** Adamantium kitchen consequences that follow from locked heat / expansion / cast-final law in `Metals.md` are design here. Thermal rows marked **suggested** for mythril / aurium / orihalcum / star iron-steel match the inspirational physical banner in `Metals.md` (not rewrite locks until promoted).

## How Cookware Works

| Property | What It Does in a Pan |
|---|---|
| **Thermal conductivity (k)** | Spreads heat sideways from the flame so the pan has no hot spots. |
| **Thickness** | Spreading power is roughly k × thickness. A thick mediocre conductor can beat a thin good one. |
| **Thermal mass (density × specific heat × thickness)** | Heat stored in the pan. High mass keeps temperature up when cold food hits it (searing). Low mass reacts fast when the flame changes (sauces). |
| **Diffusivity** | How fast the whole pan responds to a change in heat. |
| **Reactivity** | Acids (wine, tomato, vinegar) pull iron and copper into food. Copper leaching is toxic, so copper pans are always lined. Sulfur (eggs, onions) tarnishes silver. |
| **Surface** | No synthetic nonstick exists. Release comes from seasoning (fat baked into a hard polymer film), glass enamel or proper preheating. |
| **Warping** | Uneven heating makes metal expand unevenly. Thin steel warps on big burners. |
| **Handle heat** | A good conductor carries heat straight into the handle. |

## Cookware Material Data

| Material | k (W/m·K) | Thermal Mass (MJ/m³·K) | Diffusivity (m²/s) | Density (g/cm³) | Reactivity |
|---|---|---|---|---|---|
| Silver | 429 | 2.47 | 1.7 × 10⁻⁴ | 10.49 | Mostly inert. Tarnishes with sulfur. |
| Mythril (suggested: keeps silver's heat path) | ~430 | ~2.4 | ~1.8 × 10⁻⁴ | 9.8-10.5 | Same as silver |
| Copper | 401 | 3.45 | 1.2 × 10⁻⁴ | 8.96 | Reacts with acid. Must be lined. |
| Aurium (suggested) | ~390 | ~3.4 | ~1.1 × 10⁻⁴ | 8.7 | Same as copper. Harder, so it dents less. |
| Gold | 318 | 2.49 | 1.3 × 10⁻⁴ | 19.32 | Inert |
| Orihalcum (suggested) | ~300 | ~2.5 | ~1.2 × 10⁻⁴ | 18.8 | Inert |
| Iron | 80 | 3.53 | 2.3 × 10⁻⁵ | 7.87 | Reacts with acid. Rusts. Seasons well. |
| Cast iron | ~50 | 3.3 | 1.5 × 10⁻⁵ | 7.2 | Reacts with acid. Rusts. Seasons well. Cracks if dropped or shocked. |
| Carbon steel | ~50 | 3.85 | 1.3 × 10⁻⁵ | 7.85 | Reacts with acid. Rusts. Seasons well. |
| Star iron / star steel (suggested) | ~50-80 | ~3.5-3.8 | ~1.5-2.3 × 10⁻⁵ | 7.8 | As iron/steel. Far tougher, never cracks. |
| Titanium | 22 | 2.35 | 9.4 × 10⁻⁶ | 4.51 | Inert |
| **Adamantium** (from `Metals.md` heat lock) | ~3,000 | 2.39 | 1.25 × 10⁻³ | 4.6 | Inert (titanium parent) |
| Tin (lining) | 67 | 1.6 | 4 × 10⁻⁵ | 7.3 | Inert. Melts at 232 °C. |
| Glass enamel | ~1 | ~2 | ~5 × 10⁻⁷ | ~2.5 | Inert |

### Spreading Power and Thermal Mass (Pan Base)

| Base | Spreading (k × mm) | vs Cast Iron | Thermal Mass (kJ/m²·K) | Character |
|---|---|---|---|---|
| Cast iron, 5 mm | 250 | 1× | 16.5 | Slow, uneven, holds heat |
| Carbon steel, 2 mm | 100 | 0.4× | 7.7 | Fast, uneven |
| Copper, 2.5 mm | 1,000 | 4× | 8.6 | Fast, even |
| Silver / mythril, 2.5 mm | ~1,070 | 4.3× | 6.2 | Fastest mundane, even |
| Adamantium, 2 mm | 6,000 | 24× | 4.8 | Fastest possible, perfectly even |
| Adamantium, 8 mm | 24,000 | 96× | 19.1 | Holds more heat than cast iron and still perfectly even |

## Adamantium in the Kitchen

Follows from locked adamantium heat / expansion / cast-final law in `Metals.md`.

- **Perfectly even.** The whole pan, walls included, sits at one temperature. No hot spots under any flame.
- **Never warps.** Zero thermal expansion. A big griddle stays dead flat over any fire.
- **Inert.** No lining needed for acid cooking.
- **Light.** An 8 mm adamantium skillet weighs about the same as a 5 mm cast iron one (~2.5-3 kg at 28 cm) while holding more heat.
- **Cannot be enameled.** Glass expands ~9 ppm/K. Adamantium expands zero, so enamel spalls off. It does not need enamel.
- **Seasoning.** Cast a fine texture into the cooking surface so seasoning has something to grip.
- **Hot handles.** Heat crosses 30 cm of adamantium in about a minute. Handles must be wood, Needle Worm chitin or a hollow star steel tube, fixed with star steel rivets through cast-in holes or cast around a shrink-fit collar.
- **It rings.** Adamantium pots clang loudly.

## Pots and Pans by Type

| Item | Job | Real Best (No Aluminum) | Setting: Best Mundane | Setting: Best Magical | Ultimate |
|---|---|---|---|---|---|
| **Skillet / frying pan** | Searing, frying. Needs heat reserve. | Seasoned cast iron or thick carbon steel | Seasoned cast iron | Seasoned star iron. Same cooking as cast iron, never cracks from drops or cold water. | 8 mm adamantium with textured cast surface |
| **Sauté pan / saucepan / saucier** | Sauces, reductions. Needs fast, even response. | 2.5-3 mm copper lined with tin or silver | Tin- or silver-lined copper | Aurium lined with orihalcum foil. Dent-resistant, inert, copper-class response. | 2 mm adamantium. More even and faster than copper, no lining. |
| **Stockpot** | Boiling, stock. Water does most of the work. Only the base needs spreading. | Steel body with thick copper disc base | Steel body, brazed copper disc base | Darksteel body, aurium disc base | Adamantium. Light and no scorching at the base. Overkill. |
| **Dutch oven / braiser** | Long braises, oven work, acid foods. Needs heat retention and a nonreactive surface. | Enameled cast iron | Enameled cast iron (silica enamel) | Enameled star iron. Survives drops that crack cast iron. | 6-8 mm adamantium. Inert with no enamel to chip. |
| **Wok** | Very high heat, fast tossing. Relies on a hot center and cooler sides for resting food. | Thin seasoned carbon steel | Thin seasoned carbon steel | Thin seasoned star steel. Light, tough, never dents. | Star steel. Adamantium is wrong for a wok: perfect evenness erases the heat zones the technique depends on. |
| **Griddle / plancha** | Large flat surface, steady heat. Steel warps at this size. | Thick carbon steel plate | Thick carbon steel plate | Thick star steel plate | 8-10 mm adamantium. Never warps, perfectly even edge to edge. |

## Rune-Heated Cookware

- A single small mythril heating rune bolted under an adamantium pan heats the entire pan evenly. Adamantium's conductivity does the spreading, so one point source is enough.
- An etherium cell powers it. Aurium wraps the leads to prevent mana burn.
- The rune plate is bolted on, not cast in. Adamantium pours at ~1,700 °C and would melt mythril (~1,150 °C).
- Copper-class pans (aurium) take the same rune but spread heat about 7× worse than adamantium at equal thickness.

## How Knives Work

| Property | What It Does |
|---|---|
| **Hardness** | Resists edge rolling and denting. Kitchen knives run 58-66 HRC (about 650-860 HV). |
| **Toughness** | Resists chipping. Hardness and toughness normally trade against each other. |
| **Wear resistance** | Hard carbide particles in the steel keep the edge working longer. More carbide means longer life and harder sharpening. |
| **Edge stability** | Fine grain and small carbides hold a keener, thinner edge. Large carbides tear out of a very thin edge. |
| **Geometry** | Thinner edges at lower angles cut far better. Only hard, tough steel survives thin geometry. |
| **Corrosion** | Carbon steel rusts and reacts with acidic food. Historically, silver fruit knives were used because steel blackened fruit and tainted the taste. |
| **Sharpening** | An abrasive must be harder than the hardest phase in the blade to cut it efficiently. |

## Knife Material Data

Star-steel hardness / toughness rows follow inspirational grade tables in `Metals.md`. Durasteel / durium carbide follow the locked vanadium / VC anchor there.

| Material | Edge Hardness | Toughness | Wear Resistance | Sharpening | Verdict |
|---|---|---|---|---|---|
| Mundane 1095 carbon steel | 58-62 HRC | Moderate | Moderate | Easy on any stone | Classic baseline |
| Darksteel (~50%, 1095 base) | ~64 HRC (~800 HV) | Good (K_IC ~34) | Good | Corundum stones | Strong upgrade |
| Star steel, pure (1095 base) | ~67 HRC (~900 HV) | Exceptional (K_IC ~60) | High | Corundum stones | Best sharpenable kitchen steel possible. Thin, keen edges that don't chip. |
| Durasteel | 900-1,300 HV matrix, 2,800 HV carbides | Low (K_IC ~10-15) | Extreme | Corundum barely touches the carbides. Needs durium carbide or adamantium. | Longest working life. Coarser edge, chips at thin geometry unless clad. |
| Mythril | ~180 HV | High | Low | Easy | Fruit and table knives. Nonreactive, no taste transfer. |
| **Adamantium** | Beyond measurement | Never fails | Never dulls | Only through its weakness (magic or sound) | Ultimate. Shaped and honed once, sharp forever. |
| Orihalcum, aurium | Soft | High | Low | Easy | Not knife metals. Bolsters and fittings only. |

### Adamantium Blades

- **Edge limit.** A cast edge is only as fine as the mold. Real fine casting leaves edges around several microns wide, about the sharpness of a dull utility knife. A razor-keen kitchen edge is under 1 micron.
- **Finishing.** The edge gets its final hone through the weakness: a runesmith's flow rune or a tuned resonant hone. After that it never dulls.
- **Geometry.** It can't chip or roll, so the edge can go thinner and lower-angle than any steel survives.
- **No flex.** Useless for fillet and boning knives, which need spring.
- **Light.** Blades run about 40% lighter than steel. A star steel handle or bolster adds balance weight.
- **Cold to the touch.** High conductivity pulls heat from the hand like diamond does.

## Knives by Type

| Knife | Job | Best Mundane | Best Magical | Ultimate |
|---|---|---|---|---|
| **Chef's knife** | General cutting, thin keen edge | Hardened 1095 | San-mai: pure star steel core at ~67 HRC, darksteel cladding | Adamantium, weakness-honed |
| **Paring knife** | Small precise work | Hardened 1095 | Pure star steel | Adamantium, weakness-honed |
| **Slicer / carving** | Long clean cuts | Hardened 1095 | Pure star steel | Adamantium, weakness-honed |
| **Bread knife** | Serrated sawing | Hardened 1095 | Star steel | Adamantium with cast-in serrations. Serrations are hard to sharpen anyway, so casting them sharp forever is ideal. Needs no honing. |
| **Fillet / boning** | Flexes around bone | Spring-tempered 1095 | Spring-tempered star steel | Spring-tempered star steel. Adamantium can't flex. |
| **Cleaver** | Chopping bone, needs mass | Thick soft-tempered carbon steel | Thick star steel | Star steel body with an adamantium edge insert. Steel cast around the insert shrinks onto it for a permanent grip. Real analog is a carbide-tipped saw. |
| **Skinning / hide knife** | Monster hides, scales, abrasive work | Hardened 1095 | San-mai: durasteel core, darksteel cladding. Cladding stops chips spreading. Carbides outlast scale and grit. | Adamantium |
| **Fruit / table knife** | Acidic food, no taste transfer | Silver | Mythril | Mythril or adamantium |

## Sharpening

| Abrasive | Hardness | Cuts |
|---|---|---|
| Quartz whetstone (novaculite) | ~1,100 HV, Mohs 7 | Mundane steel, darksteel |
| Corundum / emery stone | ~2,000 HV, Mohs 9 | Everything up through pure star steel |
| Arcanite (reserved) | ~2,600 HV, Mohs 9.5 | Durasteel, slowly |
| Durium carbide grit | ~2,800 HV, Mohs 9-9.5 | Durasteel properly. Sharpen durium with durium. |
| Adamantium file or lap | Beyond measurement | Everything except adamantium. Cast teeth never wear, so one file lasts forever. |

Durasteel only sharpens well on durium carbide grit or adamantium. Real high-vanadium knife steels have the same problem with natural stones and need diamond abrasives.
