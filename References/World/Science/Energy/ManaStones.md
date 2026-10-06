# Mana Stones

Hub: `../Science.md`.
**Lock file for stone law:** `../../Materials/MonsterCores.md`.
Street prices: `../../Society/Economy.md`.
Chemical cells vs stones: `Batteries.md`.

## Mana stones (size and quality)

Stone law (capacity, dump, input, Q): `../../Materials/MonsterCores.md`. Tables below use that law. Do not re-lock rates here.

**Named sizes below are the street pegs** (real piece volume → mana). MonsterCores level→**volume** is only a rough band feel. Street pegs win exact capacity.

### Standard stones (Q1)

| Stone | Capacity | Input (mana/min) | Sustainable (mana/s) |
|---|---|---|---|
| Rice grain | 19 | 42 | 0.7 |
| Needle Worm tiny (**½** rice) | **~9.5** | ~26 | ~0.4 |
| Goblin leader (5× rice volume) | **95** | ~123 | ~2.0 |
| Pea (7 mm) | 180 | 154 | 2.6 |
| Cube (10 mm) | 1,000 | 600 | 10 |
| Marble (16 mm) | 2,145 | 804 | 13 |
| Walnut (30 mm) | 14,140 | 2,830 | 47 |
| Golf ball (43 mm) | 41,630 | 5,810 | 97 |
| Fist (80 mm) | 268,080 | 20,110 | 335 |

### .45 Colt size anchors (geometry → capacity and recharge)

**.45 Colt bullet** (255 gr, 0.452" diameter, ~0.70" long) and **full loaded cartridge** (1.600" overall, 0.480" body). Rim left out of cartridge figures. Oval ≈ two-thirds the matching cylinder volume.

**Formulas:** cylinder V = πr²L, SA = 2πr² + 2πrL. Prolate spheroid a = L/2, b = r; V = (4/3)πab²; SA = 2πb²[1 + (a / (b·e))·arcsin(e)], e = √(1 − b²/a²).

| Piece | Shape | Volume | Surface area | Capacity (1×) | Input | Sustainable |
|---|---|---|---|---|---|---|
| Bullet | Cylinder | 0.112 in³ (1.84 cm³) | 1.32 in² (8.48 cm²) | **1,840** | 848 /min | **14.1** /s |
| Bullet | Oval (prolate) | 0.075 in³ (1.23 cm³) | 0.886 in² (5.72 cm²) | **1,230** | 572 /min | **9.5** /s |
| Bullet | Actual (255 gr lead) | 0.089 in³ (1.46 cm³) | n/a | **1,460** | - | - |
| Cartridge | Cylinder | 0.290 in³ (4.74 cm³) | 2.77 in² (17.9 cm²) | **4,740** | 1,790 /min | **29.8** /s |
| Cartridge | Oval (prolate) | 0.193 in³ (3.16 cm³) | 1.96 in² (12.7 cm²) | **3,160** | 1,270 /min | **21.2** /s |

**Vs standard stones:** actual bullet tank (**1,460**) sits between **Cube (1,000)** and **Marble (2,145)**. Oval bullet sustain (**9.5**/s) matches a Cube. Full-cartridge oval (**3,160**) is about **1.5×** a Marble and still far under **Walnut (14,140)**.

### Implications

- Stones are renewable. Constant low-level enchantments sit at or under sustainable draw (MonsterCores).
- A stone twice the diameter holds eight times the mana.
- Cutting a fist core into rice-sized pieces raises total recharge about **29×** at the same total capacity (more SA).
- Artificial stones: space / max-`C` cook under pressure (`MonsterCores.md`). Clay–silica–carbon seeds preferred; not the cheap rice market.

### Quality examples (Q from MonsterCores)

| Fist core | Capacity | Mass | Input (mana/min) |
|---|---|---|---|
| 1× common | 268,080 | 710 g | 20,110 |
| 10× dragon grade | 268,080 | 710 g | 110,605 |

High-grade stones top off faster, not bigger or heavier. Size owns capacity and mass. Grade owns refill amp.

### Weight and quality

Mass from **volume × density** only (MonsterCores). Density stays quartz-like at every grade.

```
ρ  = 2.65 g/cm³                    fixed (quartz-like), all grades
m  = ρ × V                         V in cm³ → m in grams
   = 2.65 × V
```

`V` in mm³: `m (g) = 0.00265 × V_mm³`.

| Stone | Volume | Mass (any Q) |
|---|---|---|
| Rice grain | 0.019 cm³ | **0.050 g** |
| Marble | 2.15 cm³ | **5.7 g** |
| Walnut | 14.14 cm³ | **~37 g** |
| Fist | 268 cm³ | **710 g** |

| Grade (story) | Q | What changes |
|---|---|---|
| Lesser | **0.5** | Slower refill |
| Common | **1** | Baseline recharge |
| High | **2** | Faster refill |
| Highest | **3** | Faster |
| Intermediate / Greater band | **5** | Faster |
| Legendary / dragon-grade | **10** | Fastest refill; same mass and tank |

Identify, a recharge test, or a shop grading device reads Q. Weighing alone does not.

**Market (guild buy):** `../../Society/PriceCatalog.md`. Size physics and the Q ladder stay in this file. A pure volume rule would price a 16 mm marble near 2.3 SG. The catalog does not.

### Vs chemical batteries

Full tables (Wh/kg ratios, sustainable homes, sharding): `Batteries.md` **Mana Stone vs Battery Performance**.

Any-grade stone ≈ **1,050 Wh/kg** and **2,780 Wh/L** (mass fixed by size). Beats commercial cells; matches projected practical Li-air by mass. Higher Q raises refill amp per kilogram, not Wh/kg. Stones are mana tanks (area-gated recharge; dump setup-gated), not voltage sources. Prestige wire / fiber from stone: `RefinedMana.md`.
