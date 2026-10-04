# Steel Vacuum Chamber

Earth shop / build reference for a physical steel vacuum vessel. Mana pump-down costs and living-target vacuum rules stay in `Vacuum.md`. Metallurgy and welds: `CraftMetal.md`.

## Structure

Atmospheric pressure is about **14.7 psi** on every surface. The shell must resist that load without buckling.

- A flat face of **12 × 12 inches** carries roughly **2,100 lbf**.
- Cylinders are the preferred shape. Curved walls distribute the load evenly.
- Domed or dished ends are stronger than flat ends.
- Flat lids need thick plate or rib bracing across the back.
- External pressure design follows buckling rules (ASME Section VIII Division 1 external pressure charts) and not simple hoop stress.
- Rule of thumb: a **12 inch** diameter cylinder with **1/8 inch** stainless wall and stiffening rings handles full vacuum. A **1/4 inch** flat plate lid at **12 inch** diameter needs support or thicker stock.

## Material

**Stainless steel (304 or 316)**

- Resists corrosion and cleans easily.
- Low outgassing.
- Best choice for high vacuum.

**Mild steel**

- Cheaper and easier to weld.
- Rusts on bare surfaces. Rust holds water vapor and releases it slowly under vacuum.
- Suitable for rough vacuum with an interior coating.

## Welds and seals

- Use continuous TIG welds on the vacuum side with clean low-porosity beads.
- Weld on the inside to reduce trapped volume.
- Avoid blind seams. Trapped gas behind a seam causes virtual leaks that act like real leaks for weeks.
- Viton or Buna O-rings in a machined groove (lightly greased) work for rough to medium vacuum down to about **10⁻⁶ Torr**.
- KF (NW) flanges are the common hobby standard.
- ConFlat copper gasket flanges are used for ultra-high vacuum (below **10⁻⁸ Torr**).

## Cleaning

- Degrease with solvent and then wipe with alcohol.
- Ultra-high vacuum needs chemical cleaning and a bakeout at **150 to 250 °C**.

## Interior coatings for mild steel

### Lacquer

- Thin film that blocks moisture and prevents surface rust.
- Easy to brush or spray. Dries hard.
- Organic polymer so it outgasses solvents and vapors under vacuum.
- Limited to rough vacuum at about **1 Torr to 0.1 Torr**.
- Thin coats cure best and outgas least. Thick coats retain solvent for months.
- Suited to workshop degassing chambers.

### Glaze (glass or porcelain enamel)

- Fired onto the steel to form a hard nonporous glass layer.
- Does not shed vapor like organic coatings.
- Smooth and chemically inert with strong corrosion resistance. Same principle as glass-lined reactor tanks.
- Brittle. A chip exposes bare steel. Thermal shock or impact can crack it.
- Higher cost and needs careful handling.

## Comparison

| Option | Cost | Vacuum level | Notes |
|---|---|---|---|
| Lacquer on mild steel | Low | Rough (1 to 0.1 Torr) | Quick and simple. Outgasses. |
| Glaze on mild steel | Medium to high | Medium to high | Clean interior. Fragile if chipped. |
| Bare stainless | High | High to ultra-high | No coating to outgas. |

## Pumping technology

| Range | Pressure | Pump |
|---|---|---|
| Rough | 760 to 1 Torr | Rotary vane, scroll or diaphragm |
| Medium | 1 to 10⁻³ Torr | Two-stage rotary vane |
| High | 10⁻³ to 10⁻⁸ Torr | Turbomolecular or diffusion pump backed by a roughing pump |
| Ultra-high | below 10⁻⁸ Torr | Ion pump, cryopump, or turbo with bakeout and titanium sublimation |

## Gauges

- Rough vacuum: Pirani or thermocouple gauge.
- High vacuum: cold cathode or ionization gauge.

## Energy required

Ideal pump-down work is **not** `P·V·ln(P₁/P₂)` (that models compressing the whole original charge and diverges as P → 0). Locked formula in `Vacuum.md`:

```
W_min = P₀ V · [1 − x + x · ln(x)],  x = P / P₀
```

As P → 0, `W_min → P₀ V` (finite). Full vacuum upper bound: **W ≈ P_atm · V**.

Example: **1 cubic foot** (0.0283 m³) from 1 atm to **1 mTorr** (`x ≈ 1.3×10⁻⁶`) is about **P₀ V ≈ 2.9 kJ** (~0.8 Wh). Real pumps use far more due to inefficiency, outgassing, leaks and run time.

Practical pump power:

- Rotary vane or scroll pump: about **200 to 750 W** (1/4 to 1 HP). A **1 cubic foot** chamber reaches roughly **50 mTorr** in a few minutes.
- Turbopump: adds **50 to 300 W** plus a controller. Reaches **10⁻⁶ Torr** in tens of minutes to hours.
- Ion pump: under **100 W** at steady state with high startup power.
- Bakeout for ultra-high vacuum is the dominant energy cost at several hundred to several thousand watts for hours to days.

## Safety

- Implosion is the main hazard. Steel chambers fail by buckling.
- Viewports need rated thickness and a shield. Never use glass or thin acrylic without rating.
- Vent oil-sealed pump exhaust outdoors.

## Practical hobby routes

- Commercial **5 gallon** stainless pressure vessel used as a chamber with a rated clear lid and a two-stage rotary vane pump and gauge: reaches the **29+ inHg** range for a few hundred dollars.
- Welded stainless build with KF ports and a turbopump: reaches high vacuum for a few thousand dollars.
