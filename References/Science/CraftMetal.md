# Craft Metal

How to apply modern metallurgy knowledge with Caldris tools + magic when making metal goods. Hub: `Science.md`. Plastic work: `Compression.md`. Vacuum weld: `Vacuum.md`. Ember / Frost / Hands: `ManaCast.md`. Kinetic pours: `Kinetic.md`. Era: `../World/Technology.md` (magitech / early industrial overlay; smith craft still uses bloomery-grade stock locally).

**Division of labor (locked)**
- **Ember / forge fire / heat runes:** heat and soak. Do not invent forge heat as pure Mana Hands friction unless the beat is showing off.
- **Mana Hands / barrier molds:** force, pressure, vacuum boundary, scour, stir, even geometry.
- **Knowledge:** what carbon / alloy / HT cycle to aim at. Magic supplies precision and repeatability, not wish-chemistry.

**Toolkit constraints (craft path)**
- No outcome by intent (“clean,” “purify,” “refine”). Motion and heat do the work (scrape, cavitation, Ember soak, cementation chemistry).
- No lightning / induction / electrolysis as a default forge path.
- No time acceleration. Soak and diffusion run at real duration. Sustained pressure costs sustained focus.
- Chemistry stays mundane (oxides, cementation, quench response).

---

## Barrier mold

Rigid mana boundary as mold cavity. Molten metal poured or telekinetically pushed in; barrier dropped after solidify. Cost: barrier hold mana/s for freeze time + move melt (KE / lift equations).

Advantages: no mold contamination, no cracked mold, live shape adjust before freeze.

**Surface tension:** molten copper ~**1.3 N/m** (order similar for many liquid metals). Negligible in wide channels; fights wire-thin gauges (beading, necking, rounded profile). Barrier can actively push back and hold true cylinders at gauges a passive physical mold loses.

## Wire

Cast thin channel ≠ true wire. Cast grain is coarse, more brittle, worse bend life and conductivity per section. Correct path:

1. Cast a **rod** (barrier mold).
2. Cold-draw through narrowing barrier dies, or stage plastic thinning E ≈ σ_flow × ε × V.

Air-cool copper rods freely (no quench requirement like some steels). Skipping the draw is what produces bad “wire.”

## Springs

Cast-to-shape coil is not a spring (no cold-work / heat-treat structure → bends and stays bent). Correct:

1. Start from **drawn** wire.
2. Coil on a barrier mandrel (even pitch / diameter).
3. Harden + quench + temper (Ember heat; Frost Breath or quench bath). Magic wins on **even geometry and even temperature** along the whole coil, not on skipping steps.

---

## Bonding (vacuum and hot diffusion)

### Vacuum (cold) welding

True metallic bond. No filler. No heat-affected zone. Joint can **match** parent metal at the interface, **not exceed** it. Strongest “joint” is still continuous grain (forged or cast as one piece). Detail + costs: `Vacuum.md` (Void-Weld).

- Rough surfaces → contact area is a fraction of nominal unless pressure flattens asperities. Microvoids start cracks.
- Best: ductile similar metals (Al, Cu, Au, Ag). Hard / brittle / dissimilar pairs bond poorly.
- Needs atomically clean faces. In air, oxide reforms in nanoseconds. **Scour inside the vacuum** right before contact.
- Alternatives: diffusion bonding, friction stir, explosion weld, electron beam (Earth refs); in-story prefer vacuum scour + hot press.

### Hot vacuum bonding (diffusion)

1. Heat to roughly **50–80%** of melting T under pressure in vacuum (Ember / forge soak; Hands squeeze).
2. Asperities creep flat; atoms diffuse; seam can vanish under a microscope. Pressure is required, not optional.
3. Vacuum + heat dissolves oxides in steels and titanium. Aluminum oxide is too stable (surface treatment or interlayers).
4. Once bonded, the interface is sealed. Air only scales the outside. Cool in protective atmosphere or vacuum to avoid decarb / scale.
5. Oil quench only helps alloys that respond. Hardenable steels can quench from bonding T if it is above austenitizing. **Temper afterward.**
6. Long hot soaks grow grains and hurt toughness. Quench risks distortion and cracking at thin sections / sharp corners.

**Rule:** any diffusion bond happens **before** the quench. Bonding after quench softens the steel and erases HT.

### Which metals benefit

| Metal | Bond | Quench after bond |
|---|---|---|
| Fully dense powder steel | Excellent (HIP-like consolidate) | Best when dense |
| Alloy / tool / medium-carbon steel | Excellent at ~800–1100 °C | Strong benefit |
| Martensitic stainless (410 / 420) | Bonds | Hardens |
| Aluminum bronze | Resists bonding; can still HT | Quench + temper possible |
| Low-carbon steel / wrought iron | Bonds well | Little quench gain |
| Tin bronze | Bonds ~600–800 °C | No quench harden (cold work instead) |
| Austenitic stainless (304 / 316) | Bonds | Does not harden |
| Cast iron | Bonds poorly | Do not oil quench |

Porous sinter (**under ~95% density**) soaks oil and should not be oil-quenched. Consolidate to full density first.

---

## Blade / tool treatment order

Modern reference order (apply with Ember + Hands + mundane baths):

1. Powder consolidate (HIP-like) if using powder path
2. Hot work (forge / roll)
3. Anneal
4. Rough grind / machine
5. Austenitize and quench
6. Sub-zero (salt–ice or Frost / expansion cold; deep cryo is out of reach)
7. Temper two or three cycles
8. Final grind and edge (grind cool; overheating draws the temper)

Temper immediately after quench to avoid cracking.

---

## Local stock + modern aim

**What local smithing usually has:** bloomery / blast + finery, trip hammers, cementation blister steel, pattern welding / piling, bronze casting, water / brine / oil quench, color + magnetic austenite check. Caldris also has steam / mana-stone industry (`Technology.md`); that does not put CPM powder on every anvil.

**What knowledge aims at:** ~**0.6–1.0% C** for hardenable blade / spring steel; near-zero C wrought vs 2%+ cast; later alloying (Cr, Ni, Mn, V) when ores or trade allow. Folding exists because stock was inconsistent, not because folds are magic.

---

## Bronze goods

1. Smelt copper and tin. Alloy ~**88–90% Cu / 10–12% Sn** (gun-metal). **14–17% Sn** for harder brittle edges.
2. Melt with even Ember soak (closed shell helps).
3. Cast under vacuum to cut gas porosity. Preheat molds to avoid cold shuts. Barrier mold optional.
4. Optional composite: high-tin edge on low-tin core. Scrape both faces in vacuum and press hot.
5. Anneal (dull red, slow cool). Cold-hammer the edge for work hardening (main strength path). Re-anneal when cracks start.
6. High-tin (~20%) can quench from ~600–700 °C and temper for a tougher edge.
7. Grind and polish.

**Best gain:** low porosity, uniform grain from hammer/anneal cycles, hard edge on tough core. Still below steel for edge hardness and retention.

## Steel goods

1. Bloomery / blast → finery wrought iron. Hammer slag out.
2. Cementation → blister steel. Pile high-C edge on low-C spine.
3. Scrape every face **inside vacuum** and press hot (full bond vs flux-filled forge weld).
4. Forge to shape. Normalize (cherry red, air cool). Anneal. Rough grind.
5. Austenitize (Ember soak to cherry / non-magnetic). Bonding + austenitize can be one heat into the quench.
6. Quench in agitated oil (tough grades) or agitated brine (simple high-C). Hands stir for even quench.
7. Sub-zero (salt–ice / Frost). Temper 2–3× by oxide color (straw edge, blue-purple spine).
8. Final grind cool.

**Best gain:** clean low-slag stock, fully bonded composite, small grain, full martensite after proper HT.

## Powdered steel (magic edge)

Renaissance anvils have no real powder metallurgy. Bloom hammering is the nearest mundane cousin. True powder steel needs magic (`Telekinetic atomization` below).

1. Smelt + carburize. Judge carbon by fracture grain / tests.
2. Make powder (grind or spin-atomize in vacuum).
3. Tumble in vacuum (attrition strips oxide skins).
4. Blend to target (C, Mn, available ores).
5. Pack in sealed can / barrier shell. Pull vacuum.
6. Consolidate: Ember heat + isostatic Hands squeeze → full density (diffusion bond in one cycle). Optional tough core in same cycle.
7. Hot work for shape. Anneal. Rough grind.
8. Austenitize. Fast agitated oil quench. Sub-zero. Temper 2–3×. Final grind cool.

**Best gain:** full density, fine uniform carbides, no slag streaks, clean composite cores. Highest edge retention with toughness when HT is right.

Never quench porous powder. Never bond after the quench.

---

## Telekinetic atomization (powder)

Force melt through an orifice while a high-velocity gas / kinetic shear jet breaks the stream into droplets.

| Property | Steel (order) |
|---|---|
| Melt | ~1370–1530 °C |
| Surface tension | ~1.6–1.9 N/m (higher than copper; needs more shear for same droplet size; helps round droplets) |
| Molten density | ~7000 kg/m³ |
| Orifice | ~2–6 mm industrial → powder ~10–500 μm |

Continuous power: W = F_shear × v_relative for pour duration. Finer powder → higher relative velocity → higher power. Mana-barrier nozzle does not melt or erode at steel T (real ceramic/refractory liners do).

### Powder metallurgy (compact → full density)

Atomized powder → compact (Hands pressure / die) → sinter or HIP-like hot isostatic squeeze below melt until necks bond and density is full. Magic’s win is **even green density** and **even soak**, same as springs.

---

## Comparison (blades)

| Metal | Main hardening | Best quality gained | Relative quality |
|---|---|---|---|
| Bronze | Cold work (or quench high-tin) | Toughness and corrosion resistance | Lowest |
| Steel | Quench and temper | Hardness + toughness | High |
| Powdered steel | Quench and temper after full density | Uniform carbides; best retention + toughness | Highest |

## Rules that always hold

- Bond before the quench. Never after.
- Scrape inside the vacuum right before contact. That step decides bond quality.
- Never quench cast iron or porous material.
- Temper immediately after quenching.
- Grind cool. Overheating the edge draws the temper.
- Joint ≤ parent metal. Continuous grain beats any weld.
