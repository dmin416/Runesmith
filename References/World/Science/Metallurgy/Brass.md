# Brass

Copper–zinc alloy craft: melt rules, work bands, fittings. Overheat / fume: `OverheatedMetals.md`. Mundane metal world: `../../Materials/Metals.md`. Copper tube work: `CopperPipe.md`. Grade catalog: `CommonAlloys.md`. Vacuum / science: `EarthAlloys.md` (Brass). Zn / cementation history: `../../Materials/MaterialsProcessing.md` §5. Lead-free free-cut swaps: `ToxicMetalSubstitutes.md`.

## Narrative

Brass is the fitting and cold-draw metal. Zinc content picks the work path. Zinc also sets the main hazard: it boils out of the melt and the weld pool.

## Detail

### What the zinc fraction does

| Band | Zn (approx.) | Example | Work |
|---|---|---|---|
| Alpha | under ~37% | 70/30 cartridge | Cold work, draw, spin. Poor hot forge (mid-temp brittle band) |
| Alpha–beta | ~40% | 60/40 Muntz | Hot forge and extrude well. Stiffer cold |
| Leaded free-cut | +2–3% Pb | C360 | Clean chips for machining. Fittings stock |

Color moves red-gold → yellow as Zn rises. Above ~38% Zn the harder beta phase appears, which is why 60/40 hot-works easily.

### Melt and cast

```
T_melt_Cu = 1085 °C
T_boil_Zn = 907 °C
T_pour_brass ≈ 950–1050 °C
```

**Order:** melt copper first. Add zinc last, just before pour. Cover with charcoal or borax. Skim dross. Charge a few percent extra zinc for burn-off.

**Calamine (availability COMMON; process here):** old name for Zn ore. British usage ≈ smithsonite (ZnCO₃); American ≈ hemimorphite (hydrous Zn silicate). Name via Medieval Latin *calamina* ← Latin *cadmia* / Greek *kadmeia*.

**Cementation (no metallic Zn):** crushed calamine + charcoal + copper in sealed crucibles, heated. Zn vapor from the ore diffuses into Cu → brass ~**20–30% Zn**. Caps around **28–30% Zn**. Metallic Zn smelt is later / SPECIALTY street stock; do not assume pure Zn ingots for baseline brass.

**Cast routes:** sand (valves, hardware), lost wax (detail), die (volume small parts), centrifugal (bushings, tubes).

### Hot vs cold work

| Mode | Temp / note |
|---|---|
| Hot forge / stamp (α–β) | ~650–800 °C |
| Hot extrude | Rod, tube, profiles |
| Cold: roll, draw, spin, deep draw, stamp | Work-hardens |
| Anneal | ~425–700 °C. Below ~525 °C no glow. Top of band: dull red in dim light. Quench or air cool both soften (cooling rate does not set soft state) |
| Stress relieve | ~250–300 °C after heavy cold work. Stops season cracking (ammonia stress corrosion) |

### Machine and join

- Tools: sharp, zero or slightly negative rake. Positive rake grabs
- High speed. Fluid optional. Threads and taps cut clean → fittings dominance
- Soft solder: plumbing / electrical
- Braze / silver solder: strong instrument joints
- Weld: hard. Zinc boils out. Usual path TIG + silicon-bronze filler. Ventilate (metal fume fever)
- Mechanical: rivets, threads, press fits

### Finish

Pickle (dilute sulfuric or citric) for firescale. Polish (tripoli → rouge). Patinas: liver of sulfur (brown–black), ammonia fume (blue-green), ferric nitrate (red-brown). Lacquer / wax or Ni / Cr plate against tarnish.

### Fittings (craft readout)

**Make:** cut bar → hot-forge blank → machine threads / seats / bores → clean / tumble → optional plate.

**Water rules (Earth / shop logic):** lead-free grades for drinking water where that law matters. DZR (dezincification-resistant) where water would leach Zn.

| Joint | Install note |
|---|---|
| NPT thread | PTFE tape or dope. Hand tight + 1–3 wrench turns |
| Compression | Ferrule bites tube. Hand tight + ~½–1 turn. No tape on those threads |
| Flare 45° SAE | Flare tube to cone. Gas / refrigerant |
| Push-to-connect | Deburr. Mark insertion depth |
| Barb + clamp | Hose |

**Galvanic:** avoid direct brass–aluminum contact. Dielectric union on steel water-heater joints.

### Caldris invent filter

Early smith culture can reach cementation brass and sand-cast / forged fittings without modern Zn metal if calamine exists. Cartridge deep-draw, CNC, and push-fit plastics stay invent or import. Zinc fume and season cracking still apply in any forge that cold-works then stores brass near ammonia sources (stables, latrines, some cleansers).

## Open

- Copper pipe / tube companion file from MostRecentNotes
- Deeper vacuum-melt brass detail: `EarthAlloys.md` if a precision beat needs it
