# Refined Mana (Stillwire and Lightthread)

Working names for prestige craft products made by purifying and refining mana stone. Proposal / invent ladder. Do not paste Earth brand codes into prose.

**Companions:** `ManaStones.md` (raw tanks), `Batteries.md` (stone vs cell power), `../Metallurgy/CraftMetal.md` (mythril shop), `../../../Combat/ImpactRune.md` (temporary mass / weight), `../../../PotentialMagic/MassBoost.md` (mass up at fixed speed).

**Caldris readout:** not baseline consumer goods. Refining is rare skilled craft. Numbers below are prestige ceilings. Cheap Stillwire would break rail and airship economies.

---

## What mana converts into

Mana is condensed magic. Phase conversion into heat, charge, cold, motion or temporary mass is far cleaner than the matching Earth machine. Paid mana still hits the **1 mana = 10 J** peg first; rune paths also pay η_cond (`Energy.md`, `ManaCast.md`). The table is phase conversion after that.

| Converts into | Mana loss (phase step) | Best physical equivalent | Notes |
|---|---|---|---|
| Heat (fire phase) | ~0% | Resistance heater (~0% if waste heat is the goal) | Fire work still pays peg + η_cond upstream |
| Electricity (lightning phase) | <0.1% | Best generators: 1-2% | Needs a converter path or Stillwire loop |
| Cold (ice phase) | <0.1%. Absorbed heat returns into mana; no separate heat dump | Refrigerators must vent heat and pay extra work | Magic cheat vs Carnot dump |
| Kinetic motion | <0.1% | Electric motors 5-10%. Steam 80-90% | Lift / throw / Impact stroke use cast or path law for paid mana |
| Mass (weight / inertia) | Cost = added KE (and hold), not E = mc² | No cheap Earth analog | Temporary. See below |
| Structure (refined lattice) | Refine craft cost | No physical equivalent | Locks mana into durable material |

### Mass means weight, not summoned matter

Raising **mass / weight / inertia** on an existing object is already canon:

- `../../../PotentialMagic/MassBoost.md` - mass up at fixed speed; Effect = ½ × added mass × v²
- `../../../Combat/ImpactRune.md` - compressed mana = temporary head mass; stop feeding and it disperses swing-fast
- Gravity / heavy magic blurbs in Old `Combat/Spells.md` until absorbed

That is **not** free permanent matter from energy. Rest-mass E = mc² pricing does not apply; the spell pays the kinetic and hold costs above.

**Elemental bulk matter** (water, ice, earth and similar phase bodies) can appear from the matching elemental mana. Arbitrary summoned steel, food or corpses from raw mana do **not**.

---

## Stone ladder: raw → purified → refined

Raw mana stone is mana bound loosely in a quartz-like crystal (**2.65 kg/L**). Mass and tank size stay size-only (`ManaStones.md`). Quality does not change weight.

**Purify** strips dead mineral matrix. Outer volume can stay similar while the **mana fraction** rises, so usable mana per gram goes up without rewriting the 1 mana/mm³ rule for the mana-bearing volume.

**Refine** locks remaining mana into an ordered lattice. The lattice’s energy holds the structure together.

| Stage | Form | Density | Stores usable mana |
|---|---|---|---|
| Raw stone | Cloudy crystal, mineral-laced | 2.65 kg/L | Yes (volume tank) |
| Purified stone | Clearer crystal, less matrix | ~2.65 kg/L | Yes; more usable mana per gram than raw of equal outer size |
| Refined lattice | Glassy, metallic or clear by set | ~3.2 kg/L | **No** as a free tank. Locked into structure |

**Key rule:** refined mana is spent as fuel when you pull structural or conductive work out of the lattice. Drawing power from Stillwire or Lightthread **unravels** material back toward raw ambient mana. They are not rechargeable stones.

The lattice sets two ways, depending on how the refiner treats it.

---

## Stillwire (superconducting form)

**Vs mythril:** mined **mythril** (magically saturated Ag–Cu, pearlish silvery gold) remains the native superconducting path metal (`CraftMetal.md`; Old ManaMaterials until absorbed). **Stillwire** is a **stone-refined wire product**: consumable / unravel-risk stock for lines, windings and flywheels. Same superconducting physics story; different feedstock and economics. Do not invent a third unexplained room-temp superconductor. No metal path-% dial on either.

### How it is made

1. Purified stone is softened under a containment rune until it flows like hot wax.
2. An alignment rune pulls the lattice into long ordered chains.
3. The mass is drawn through a die into wire, then cooled slowly under the rune field.

**Appearance:** pale silver with a faint blue sheen. It floats above lodestone. A Stillwire ring over a magnet hovers and locks (Meissner / flux pinning).

**Flavor science:** Earth superconductors need electron pairs that heat easily breaks. Stillwire’s mana lattice binds those pairs so forge-hot running stays superconducting until the critical temperature band.

| Property | Stillwire | Best physical material |
|---|---|---|
| Critical temperature | ~1,000 °C | About -135 °C (cuprates at normal pressure) |
| Lattice unraveling point | ~3,500 °C | Tungsten melts at 3,422 °C |
| Critical field | ~1,000 T | REBCO tape: 100+ T near absolute zero |
| Current capacity | ~10,000 A/mm² | Copper: 2-10 A/mm². REBCO: 1,000-5,000 A/mm² |
| Tensile strength | ~200 GPa | Graphene ~130 GPa. Carbon fiber ~6 GPa. Steel 1-2 GPa |
| Resistance (steady DC) | Zero | Copper loses ~5-10% on long lines |

**What one wire carries:** 1 mm² Stillwire at 10,000 A and 1,000 V → **10 MW** through pencil-lead cross-section.

**Yield:** 1 kg refined lattice → about **310 m** of 1 mm² wire.

**Storage potential:** at 200 GPa and 3.2 kg/L, a Stillwire flywheel or stressed coil rim can approach **~17,000 Wh/kg** (σ/ρ order). About **16×** a Common mana stone by mass and above gasoline’s chemical Wh/kg. Prestige only.

**Uses**
- Zero-loss power lines along railways
- Motors and generators with almost no winding loss
- Magnetic bearings, levitation tracks and airship lift assists
- Magnets far stronger than lodestone
- High-density flywheel and coil storage

**Limits**
- Superconductivity stops above ~1,000 °C and returns on cooling (unless the lattice is damaged).
- Lattice unravels into raw mana above ~3,500 °C.
- Drawing stored structural / coil energy spends the wire.
- Jc / quench still exist in principle; gear mythril dials stay the safer reusable path for wands and etched weapons.

Winding physics detail: Old `Runes/ManaMaterials.md` until absorbed.

---

## Lightthread (optical fiber form)

**Vs mana fiber:** soft mana fiber carries **mana**. Lightthread carries **light and optical signals only**. Keep them distinct.

### How it is made

1. Refined lattice is set clear rather than metallic. A calming rune keeps the lattice from conducting.
2. A rod of clear refined lattice (core) is sleeved in a tube of purified stone (cladding).
3. The rod is heated and drawn into a hair-thin thread, the same way silica fiber is pulled from a preform.

**Appearance:** clear and slightly opalescent. Light entering one end glows faintly along cut edges and exits the far end.

**Flavor science:** total internal reflection. Real silica loses light to impurities and frozen density ripples. The refined lattice is ordered enough that scatter stays tiny.

| Property | Lightthread | Real silica fiber |
|---|---|---|
| Diameter | ~125 µm | 125 µm |
| Loss | ~0.01 dB/km | ~0.2 dB/km |
| Distance before light halves | ~300 km | ~15 km |
| Distance before light drops to 1% | ~2,000 km | ~100 km |
| Tensile strength | ~200 GPa | ~5 GPa pristine |
| Unraveling or melting | ~3,500 °C | ~1,600 °C |

**Yield:** 1 kg refined lattice core → about **25 km** of thread.

**Uses**
- **Light-telegraph:** coded flashes along railway lines. One relay can cover a kingdom ~500 km across.
- **Lightpipes:** daylight into mines, dungeons and ship holds.
- **Rune signaling:** flash rune at one end triggers a light-sensitive rune at the other. Remote switches and alarms without power wires.

**Limits**
- Light only. No mana bus and no power delivery.
- Unravels into raw mana above ~3,500 °C.
- Spending structural energy (if used as stressed cable) unravels stock the same way Stillwire does.

---

## Summary

| Material | Role | Strength |
|---|---|---|
| Mana stone | Stores energy; ambient recharge | ~1,050 Wh/kg. Size tank; Q = amp |
| Mythril (mined) | Reusable superconducting path / gear | Jc, rare quench, shop Ag–Cu lock |
| Stillwire | Moves electricity with zero DC loss; prestige structure | ~10 MW through 1 mm². SC to ~1,000 °C. Unravels if spent or overheated |
| Lightthread | Moves light and signals | ~300 km before light halves. Survives ~3,500 °C. Optical only |
| Mass boost / Impact | Temporary weight on existing objects | KE / hold cost. Not summoned matter |
