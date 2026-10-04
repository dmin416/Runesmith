# Structural Forge

Hammers, beams, pipe, swords, steel grades and bronze. How a small shop with vacuum seam fusion punches above a rolling mill. Copper tube detail: `CopperPipe.md`. Vacuum craft: Old `Vacuum.md` / `CraftMetal.md` until pulled. Overheat: `OverheatedMetals.md`.

## Narrative

A sword needs one smith. Conventionally rolled I-beams and seamless pipe need a mill. Perfect vacuum seam fusion moves the bottleneck to **clean steel supply**. Shaping becomes three plates or one curved plate with fused joints as strong as parent metal.

## Detail

### Industrial hammers (force ladder)

| Type | How it hits | Note |
|---|---|---|
| Board / rope drop | Gravity only | Simple. Limited by weight × height |
| Steam hammer | Steam lift; double-acting also drives down | 1800s giants (tens to 100+ ton class) |
| Pneumatic power hammer | Motor + air | Shop smithy workhorse |
| Hydraulic / electro-hydraulic | Precision heavy forge | Modern heavy standard |
| Counterblow | Two rams meet | Cancels foundation recoil. Peak single blows ~1000 kJ class |

Biggest forgings leave hammers for **hydraulic presses** that squeeze through-thickness (hammering mostly works the surface).

### I-beams

**Mill path:** bloom → reheat ~1200 °C → roughing + universal mill → cool / straighten / saw. Power in thousands of horsepower. Pre-mill: riveted plate + angle built-up beams.

**Vacuum-weld path:** beam = **web + two flanges**, three flat strips, two seams.

Needs: clean low/med carbon (~0.2–0.25%), flat stock (trip / power hammer enough), square bare-metal edges, alignment jig, straightedge / square / calipers.

Sequence: steel → flatten → fuse shorts to length → cut → grind faces → jig → vacuum weld both seams → check.

**Wins:** no HAZ warp from ordinary weld, arbitrary length/taper/curve, stack thin plate into thick flanges. **Limit:** steel tonnage and cleanliness, not the join trick.

### Steel pipe

**Mill / historic:** butt-weld skelp through bell die; lap-weld over mandrel; Mannesmann pierce seamless; ERW; UOE / spiral for large OD; spun cast iron for mains.

**Vacuum-weld path:** flat plate → cylinder → one longitudinal seam (= seamless performance if the fuse is perfect).

```
P_burst ≈ 2 × σ × t / D_outer     // Barlow
```

End-to-end fused lengths need no threads. Fittings from cut/fused segments. Diameter limited by bend ability, not pierce mills.

Copper pipe (hand wrap + fuse friendly): see `CopperPipe.md`. Vs steel: copper weaker / better corrosion and heat transfer; steel for high pressure and large OD.

### Swords (shop scale)

Forge ~1100–1200 °C. Medium–high carbon ~0.6–0.8%. Quench harden, temper ~200–300 °C. Optional trip / pneumatic hammer. One smithy. Same vacuum shop that builds beams can still make blades; carbon grade differs (structural mild vs blade high-carbon).

### Steel carbon ladder

| Band | C (approx.) | Job |
|---|---|---|
| Wrought iron | <0.08% + slag fibers | Soft, tough, easy forge-weld |
| Mild / low | 0.05–0.25% | Beams, pipe, plate |
| Medium | 0.3–0.6% | Axles, tools, hammer heads |
| High | 0.6–1.0% | Swords, knives, springs |
| Ultra-high | 1.0–2.0% | Files, wootz, specialty |
| Cast iron | >2% | Cast only. Not forgeable |

**Heat treat:** harden (above ~750–850 °C, quench) → temper (150–650 °C trade hardness for toughness). Anneal = slow cool soft. Normalize = air cool grain refine.

**Make steel (era ladder):** bloomery → crucible / cementation → blast + fine/puddle → Bessemer / open hearth → BOF / EAF. Inputs: ore, charcoal or coke, limestone flux, refractories, air blast.

### Bronze

Cu + Sn. Classic ~88/12. Melt ~950 °C (below copper). Tin is the scarce trade metal.

| Alloy feel | Sn | Note |
|---|---|---|
| Tool / sword | ~10% | Work-harden edges by hammering |
| Standard | ~12% | General cast |
| Bell | ~20–25% | Hard, brittle, rings |

No quench harden. Work harden only. Heavier than steel (~8.8 vs 7.85). Weaker / less stiff → short or leaf blades historically. Cast detail wins.

| | Bronze | Steel |
|---|---|---|
| Melt | ~950 °C | ~1370–1510 °C |
| Shape | Cast | Forge / roll |
| Harden | Cold hammer | Quench + temper |
| Corrosion | Patina | Rusts |
| Ore | Cu + rare Sn | Iron almost everywhere |

Vacuum fuse: bronze–bronze structures; bronze–steel hybrids (blade + fittings, shaft + bearing). Wet galvanic: steel side dies faster → coat or isolate.

### Caldris invent filter

Bloomery / crucible / trip-hammer smithy is in era. Vacuum seam fusion is a magic/craft breakthrough that lets a workshop fake mill products. Do not hand-wave clean tonnage. Brass and copper water lines still follow `Brass.md` / `CopperPipe.md`.

## Open

- Exact vacuum-weld mana / joule costs when CraftMetal is absorbed
- Rolling-mill vs vacuum shop economy beats
