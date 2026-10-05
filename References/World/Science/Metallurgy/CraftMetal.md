# Craft Metal

Modern metallurgy aims with Caldris forge + magic. Named metal locks: `../../Materials/Metals.md`. Plastic work: `../Energy/Compression.md`. Products: `BlacksmithProducts.md`. Arrowheads: `Arrowheads.md`. Animal materials: `../Biomaterials/Biomaterials.md`. Earth alloys / carbon: `EarthAlloys.md`. Ores: `MetalOres.md`. Gem seats: `GemInlay.md`. Vacuum: `Vacuum.md`.

## Narrative

Magic gives even heat, pressure and clean faces. It does not wish-chemistries or skip soak time. Heat heats. Hands and barriers push, scour and mold. Knowledge picks the carbon and HT cycle.

## Detail

### Division of labor (locked)

| Job | Tool |
|---|---|
| Heat / soak | Heat, forge fire, heat runes |
| Force / vacuum boundary / scour / stir / geometry | Mana Hands, barrier molds |
| What alloy / HT to aim at | Knowledge |

**Constraints:** no outcome-by-intent (“purify”). No default lightning / induction / electrolysis forge. No time acceleration. Chemistry stays mundane.

### Barrier mold

Rigid mana cavity. Pour or Hands-push melt. Drop barrier after freeze. Cost = hold mana/s × freeze time + move-melt work.

Wins: no mold grit, live shape tweak, fights surface tension on wire-thin gauges (molten Cu ~**1.3 N/m**).

### Wire and springs

**Wire:** cast rod → cold-draw through narrowing dies (or staged plastic `E ≈ σ_flow × ε × V`). Cast-thin “wire” stays coarse/brittle.

**Springs:** drawn wire → coil on barrier mandrel → harden / quench / temper. Cast-to-shape coil is not a spring. Magic wins on even pitch and even soak, not skipping HT.

### Bonding

**Vacuum cold weld:** metallic bond, no HAZ, joint ≤ parent. Scour **inside vacuum** right before contact (oxide reforms in air in ns). Best: ductile similar metals.

**Hot diffusion:** ~**50–80%** melt T under pressure in vacuum. Bond **before** quench. After-quench bond softens steel and erases HT. Long soaks grow grain. Al oxide too stable without surface treatment.

| Metal | Bond | Quench after |
|---|---|---|
| Tool / med-C steel | Excellent ~800–1100 °C | Yes |
| Low-C / wrought | Bonds | Little quench gain |
| Tin bronze | ~600–800 °C | Cold work, not quench |
| Cast iron | Poor | Never oil quench |
| Porous sinter (&lt;95%) | - | Consolidate first |

### Mythril (shop)

Matches `Metals.md`: permanently converted **silver**. Shop frame ≈ Ag–Cu eutectic (~**72 Ag / 28 Cu**, melt ~**779 °C**). Pearlish warm silver. Work-hardens like silver alloy. Takes runes. **Not titanium.**

### Orihalcum (shop)

Matches `Metals.md`: permanently converted **gold**. Magic resistance = conversion %. Fights further cook; high purity needs deep dungeon or high altitude. No free enchantments; inlays possible but proximity interferes. Story: mage-hostile plate, antimagic fittings. Guild rank spelling **Orichalcum** is separate.

### Aurium (shop)

Matches `Metals.md`: permanently converted **copper**. Damps flowing mana; does not hard-block still mana. Linings for pipes, pumps, grips, casting rods. Low-grade COMMON-side industrial; high-grade steep.

### Darkiron / star iron · darksteel / star steel (shop)

Matches `Metals.md`: iron and steel conversion bands (dark → star). Prefer convert iron then carburize. Ordinary forge HT still applies until star grades change the story beat.

### Adamantium (shop)

Matches `Metals.md`: permanently converted **titanium**. **Once cast: indestructible.** Not a quench-and-temper forgeable supersteel. Hot Ti parent needs vacuum / inert / barrier (O/N brittle case).

- Shape is **final once cast and cooled**. No later cut, forge, quench-alter or repair  
- Form **mail links** (and other final shapes) **while setting**  
- After set: indestructible to ordinary force; destroy only by resonance / mana vibration  
- **No stretch. No bend.** Mail flexes at ring links only. Dead: Adamweave / cloth / `R_min`

### Blade / tool HT order

1. Powder consolidate if used  
2. Hot work  
3. Anneal  
4. Rough grind  
5. Austenitize + quench  
6. Sub-zero (salt-ice / Frost; deep cryo out of reach)  
7. Temper 2–3×  
8. Final grind cool  

Temper immediately after quench. Bond before quench.

### Local stock vs knowledge aim

**Have:** bloomery/finery, trip hammers, blister steel, pattern weld, bronze cast, color/magnetic check. Steam/mana industry exists; CPM powder does not sit on every anvil.

**Aim:** ~0.6–1.0% C for blades/springs; folding because stock was inconsistent, not magic folds.

### Bronze / steel / powder paths (gist)

**Bronze:** ~10–12% Sn (harder edge 14–17%). Vacuum cast cuts porosity. Cold-hammer edge. Still below steel for edge life.

**Steel:** finery → cementation → vacuum scrape + hot press composites → forge → normalize → austenitize → quench → sub-zero → temper.

**Powder (magic edge):** atomize melt (Hands shear jet) → vacuum tumble → blend → HIP-like Hands + Heat → full density → HT. Never quench porous powder. Full write-up: `MagicPowderMetallurgy.md` (dies/porosity/vacuum weld removed by magic; powder make + mage labor stay; Ag powder cooks to mythril faster).

| Metal | Harden | Relative quality |
|---|---|---|
| Bronze | Cold work | Lowest |
| Steel | Q+T | High |
| Powder steel | Q+T after dense | Highest retention + toughness |

### Forged vs cast hardware (hinges)

Same alloy (steel), forged vs flawless casting:

| Property | Forged advantage |
|---|---|
| Tensile | 5–15% (≈25% vs typical porous castings) |
| Yield | 10–20% |
| Fatigue | 30–50% |
| Impact toughness | 2–3× |
| Ductility (elongation) | 1.5–2× |

Perfect casting kills most porosity/shrinkage so static strength almost catches up. Remainder is grain: cast keeps coarse dendrites; forge breaks them into fine elongated grains.

**Circular knuckle:** wrap a strap around a pin and grain flow follows the curve. Hinge load is hoop stress so fibers run with the load. Fatigue and impact gains peak here. Cast grain is random with no preferred strong direction.

Limits: an unfused wrap can uncurl under heavy load; a forge weld holds about **70–90%** of parent. Across the grain a forging can be weaker than a casting; hinges rarely load that way.

**Cast iron vs wrought iron** (different metals, larger gap):

| | Tensile | Elongation | Shock |
|---|---|---|---|
| Cast iron | 150–250 MPa | ~0 | Shatters |
| Hammered wrought | 300–380 MPa | 25–35% | Bends first |

Hammered hinge ≈ **1.5–2×** tension and **10×+** slam resistance. Medieval door hinges were forged for this.

**Tin bronze:** cold hammer work-hardens to about **2–3×** as-cast hardness/strength. Ductility falls unless annealed between passes.

**Wrought iron vs steel** (strap / knuckle; yield decides bend-out-of-round):

| Material | Tensile MPa | Yield MPa | Elong. | vs wrought |
|---|---|---|---|---|
| Wrought iron | 290–380 | 170–240 | 25–35% | Baseline |
| Mild steel (0.15–0.25% C) | 400–450 | 250–370 | 25–35% | 1.2–1.4× T / 1.4–1.7× Y |
| Med-C normalized (0.45% C) | 570–620 | 310–400 | 15–20% | 1.6–2× T / ~1.8× Y |
| Med-C Q+T | 700–950 | 500–800 | 10–18% | 2.5–3× T / 3–4× Y |
| High-C / spring HT | 1,000–1,600 | 800–1,400 | 5–10% | 3.5–5× T / 4–6× Y |

Fatigue repeat stress ≈ wrought 150–180 MPa · mild ~200 · Q+T 350–450 (heavy door ≈ **2–2.5×** for steel). Wear: wrought ~100 HB; hardened steel 250–600 HB (pin/knuckle wear is the usual hinge fail). Mild toughness matches or beats wrought; over-hard high-C can snap on a sudden blow.

Wrought still wins on easy forge welding, slag-fiber rust slowing and fibrous crack arrest. Knuckle risks: transverse strength ~**70–80%** of along-fiber; wrong wrap splits on slag lines; bent too cold/tight delaminates (high-P cold-short cracks at room T).

**Ideal pre-modern hinge:** wrought strap and knuckle (weld + outdoor life) with a hardened steel pin (wear).

### Always

- Bond before quench  
- Scrape in vacuum right before contact  
- Never quench cast iron or porous stock  
- Temper right after quench  
- Grind cool  
- Joint ≤ parent; continuous grain beats welds  

## Open

- Void-Weld costs when Vacuum absorbs  
