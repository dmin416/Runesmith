# Vacuum

Hub: `Science.md`. Cast law: `ManaCast.md`. Living resistance: hub ruling. Mana = J / (10 × η × μ). Physical steel chamber build (walls, seals, pumps, coatings): `SteelVacuumChamber.md`. Vacuum steps in alloy / carbon production: `Materials.md`. Forcefield vacuum over a fire (radiant HT): `VacuumForcefieldHeat.md`.

## Pump-down (correct ideal)

Pumping gas **out** of a chamber is not W = P₀ V₀ ln(P₀/P) (that diverges as P → 0 and models compressing the whole original charge).

Ideal:

W_min = P₀ V · [1 − x + x · ln(x)],  x = P / P₀

As P → 0, W_min → **P₀ V** (finite). Real pumps get slower near hard vacuum (outgassing, leaks, falling speed); fiction may add a narrative surcharge, not a thermodynamic infinity.

Flat upper bound / full vacuum: **W ≈ P_atm · V** (exact limit for perfect vacuum; upper bound for partial).

Example: 10 L full vacuum → 101,325 × 0.010 ≈ **1,013 J** (~101 mana at ημ 1).

## Expansion vs pumping

| Path | Cost idea |
|---|---|
| Naive expansion vs full P_atm for whole ΔV | E = P_atm × ΔV = P₀ V (1 − x) for going to pressure fraction x |
| Reversible pump-down | W_min = P₀ V [1 − x + x ln x] |
| Reversible expansion between same end states | Same as reversible pump |

Ratio (naive expansion / reversible pump) is largest **in proportion** at shallow vacuums (up to ~**19×** near x = 0.9) and largest **in absolute joules** near x ≈ **1/e** (~0.37). Gap → 0 at full vacuum and at no vacuum. Reward careful reversible casting of either method; punish only sloppy brute expansion that never lets trapped air help.

## Vacuum on a living target

**No cheap air-deny.** Vitality and the target's magic resist raw mana manipulation of the air around them. A vacuum / suffocate effect on a resisting person must:

1. Enclose the **whole body**.
2. Keep a **standoff shell** (air gap between boundary and skin).
3. **Seal to the ground** (or an equivalent closed volume). Partial head / limb pockets equalize through the rest of the body and fail.

Exception: the target has **no** ability to resist in any way except sitting inside otherwise impenetrable armor (no vitality push, no magic contest). Then a sealed armor interior or similar closed volume can be denied without the ground-seal shell.

Damage is pressure-differential injury. Joules mostly price **pulling** the vacuum, not wound gore.

### Injury sequence (corrected)

- **Eyes:** no globe rupture from decompression. Tear-film boil, conjunctival swelling, blur, possible surface frost. Never write eye-burst from vacuum.
- **Sinuses / middle ear:** ~20–50 kPa / ~35 kPa eardrum risk **only if venting is blocked** or decompression is unusually fast. NASA-style slow vent can leave aching ears only.
- **Lungs (dominant fast kill if breath-held):** ~**8–11 kPa** alveolar rupture → arterial gas embolism. Faster and more serious than ear folklore.
- **If breathing / venting:** ebullism near ~6.3 kPa; consciousness ~10–15 s; death over roughly a minute+ if held. Hypoxia / ebullism, not instant gore.
- **Skin:** 101 kPa does not rupture skin; swelling (up to ~2× limb volume in extreme exposure) and petechiae yes.
- **Skull:** not at risk from 101 kPa (~1000× below bone strength).

### Mana cost (thin full-body shell)

~2 cm standoff over ~1.8 m² + ground seal ≈ **0.05 m³** (about 10× a 5 L head pocket, not 300–400× a room).

W ≈ 101,325 × 0.05 ≈ **5,066 J**  
Mana = 5066 / (10 × η × μ) → ~**507 mana** at ημ 1; at INT 40 L2 (~21.9 J/mana) ≈ **231 mana**; at INT 500 L9 (~496 J/mana) ≈ **10 mana**.

Thin shell is cheaper volume but fragile: target motion or broken ground breaks the seal. If another system’s 5× robustness raises injury thresholds, apply it to lung / ebullism, not to invent eye rupture.

## Freeze-drying

Two stages:

1. **Freeze:** sensible heat to 0 °C + fusion **334 J/g** water (order **100–150 J/g** food from room temp, depending on start T and water fraction).
2. **Sublimate** below triple point (611 Pa): latent heat of sublimation ≈ **2,838 J/g** water. Do not sanity-check with 334 + 2,257 (that vaporization is at 100 °C). At 0 °C vaporization ≈ 2,501; 334 + 2,501 ≈ 2,835 ≈ 2,838.

Example: 100 g food, 70% water (70 g) → sublimation alone = 70 × 2,838 ≈ **198,660 J** (~19,866 mana at ημ 1). Batch craft / logistics, not mid-fight.

Real industrial plants: theoretical minimum ~**0.79 kWh/kg** water sublimated (~0.9 kWh/kg with freezing); measured ~**0.9–25 kWh/kg** (~**3–30×** ideal). Optional skill inefficiency multiplier for imperfect casters; master path can approach the thermodynamic floor.

## Cold boil (vacuum distillation / flash cool)

Partial pressure drop, not full vacuum. Pump with W_min(x), not flat P_atm V.

Rule of thumb: evaporating **1%** of liquid mass cools the rest ~**6 °C** (latent heat pulled from remaining liquid).

Latent heat at low T ≈ **2,501 J/g** (not ManaCast’s 2,257 at 100 °C boil row).

Example: cool 1 L water ~18 °C by boiling off 3% (30 g): 30 × 2,501 ≈ **75,030 J** (~7,503 mana at ημ 1; ~79% of freeze-drying that same 30 g at 334 J/g fusion + 2,838 J/g sublimation ≈ 95,160 J). Headspace pump-down is usually small beside latent heat.

**Apps:** heat-sensitive potion distill (rotary-evaporator analog), desalinate small volumes near body T, flash-chill wine / food / heatstroke moisture film.

## Void-Weld (vacuum cold welding)

Vacuum does not clean metal; it **prevents recontamination**. Bare metal in air reoxidizes in seconds.

### Sequential

1. Abrade / scour to bare metal (Sono-Alchemy or fine kinetic scour: `Sound.md` / `Kinetic.md`).
2. Seal vacuum on the joint volume before oxide reforms (`W ≈ P_atm · V` on a small joint volume). Low skill risks failure if too slow between steps.

### Concurrent (preferred)

Hold vacuum boundary first, scour **inside** it (abrasive KE = ½ m v² per grit, controlled stream). No air → no oxidation race. Cost = vacuum-hold mana/s + abrasive mana/s for scour duration. Skill gate: multitasking stable shell + directed scour (small/slow at low skill; larger/faster at high).

### Maintained seal (storage)

One clean-and-seal only lasts until the vacuum drops. Keeping a blade oxidation-free indefinitely is a continuous mana/s drain priced like heat-signature stealth in `Body.md` (Q_loss / (10 × η × μ) on the leak rate), not free with a one-shot clean. Use prep-before-fight for the instant version.

**Apps:** jam a lock, weld a portcullis, fuse a weapon in its sheath (sabotage), join parts as strong as the parent metal at the interface (not stronger), tarnish-free finish work. Joint ceiling and hot diffusion blade/tool cycles: `CraftMetal.md`.
