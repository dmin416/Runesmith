# Mana Stones

Hub: `Science.md`.
Street prices: `../World/Economy.md`.
Shirt-wide rice-stone pool (mail collaborative rune): `../Runes/ChainMailCollaborative.md`.

## Mana stones (size and quality)

**Capacity** comes from size only: about **1 mana per mm³** of stone volume.

**Rates (quality 1×):**
- **Output:** 1 mana per second per mm² of surface area
- **Input (recovery):** 1 mana per minute per mm² of surface area
- **Sustainable draw:** input ÷ 60. A stone drawn at or below this rate never empties.

### Standard stones (1×)

| Stone | Capacity | Output (mana/s) | Input (mana/min) | Sustainable (mana/s) |
|---|---|---|---|---|
| Rice grain | 19 | 42 | 42 | 0.7 |
| Needle Worm tiny (**½** rice) | **~9.5** | ~26 | ~26 | ~0.4 |
| Goblin leader (5× rice volume) | **95** | ~123 | ~123 | ~2.0 |
| Pea (7 mm) | 180 | 154 | 154 | 2.6 |
| Cube (10 mm) | 1,000 | 600 | 600 | 10 |
| Marble (16 mm) | 2,145 | 804 | 804 | 13 |
| Walnut (30 mm) | 14,140 | 2,830 | 2,830 | 47 |
| Golf ball (43 mm) | 41,630 | 5,810 | 5,810 | 97 |
| Fist (80 mm) | 268,080 | 20,110 | 20,110 | 335 |

### .45 Colt size anchors (Earth geometry → stone rates)

**.45 Colt bullet** (255 gr, 0.452" diameter, ~0.70" long) and **full loaded cartridge** (1.600" overall, 0.480" body). Rim left out of cartridge figures. Oval ≈ two-thirds the matching cylinder volume.

**Formulas:** cylinder V = πr²L, SA = 2πr² + 2πrL. Prolate spheroid a = L/2, b = r; V = (4/3)πab²; SA = 2πb²[1 + (a / (b·e))·arcsin(e)], e = √(1 − b²/a²).

| Piece | Shape | Volume | Surface area | Capacity (1×) | Output | Input | Sustainable |
|---|---|---|---|---|---|---|---|
| Bullet | Cylinder | 0.112 in³ (1.84 cm³) | 1.32 in² (8.48 cm²) | **1,840** | 848 /s | 848 /min | **14.1** /s |
| Bullet | Oval (prolate) | 0.075 in³ (1.23 cm³) | 0.886 in² (5.72 cm²) | **1,230** | 572 /s | 572 /min | **9.5** /s |
| Bullet | Actual (255 gr lead) | 0.089 in³ (1.46 cm³) | n/a | **1,460** | — | — | — |
| Cartridge | Cylinder | 0.290 in³ (4.74 cm³) | 2.77 in² (17.9 cm²) | **4,740** | 1,790 /s | 1,790 /min | **29.8** /s |
| Cartridge | Oval (prolate) | 0.193 in³ (3.16 cm³) | 1.96 in² (12.7 cm²) | **3,160** | 1,270 /s | 1,270 /min | **21.2** /s |

**Vs standard stones:** actual bullet tank (**1,460**) sits between **Cube (1,000)** and **Marble (2,145)**. Oval bullet sustain (**9.5**/s) matches a Cube. Full-cartridge oval (**3,160**) is about **1.5×** a Marble and still far under **Walnut (14,140)**.

### Implications

- Burst power is gated by output; capacity is the tank.
- Stones are renewable. Constant low-level enchantments sit at or under sustainable draw.
- Larger stones hold more. A stone twice the diameter holds eight times the mana.
- Input is area-based, so cutting a fist core into rice-sized pieces raises total input about **29×** while keeping total capacity the same. Shards regenerate fast; whole cores store deep.

### Quality (dump and refill)

**Quality does not raise capacity or mass.** Size owns the tank and the weight. Grade speeds output and input, with dump ahead of refill:

```
Output = Q × SA                 mana/s
Input  = ((Q + 1) / 2) × SA     mana/min
Sustainable = Input / 60        mana/s
```

At **Q = 1** this matches the baseline rates (1 mana/s and 1 mana/min per mm²). A **10×** (dragon-grade) stone dumps **10×** harder and takes input **5.5×** faster. Capacity and mass stay size-only.

| Fist core | Capacity | Mass | Output (mana/s) | Input (mana/min) | Sustainable (mana/s) |
|---|---|---|---|---|---|
| 1× common | 268,080 | 710 g | 20,110 | 20,110 | 335 |
| 10× dragon grade | 268,080 | 710 g | 201,100 | 110,605 | 1,843 |

High-grade stones are high-amp feeds that also top off faster, not bigger or heavier batteries. Size owns capacity and mass. Grade owns output and input.

### Weight and quality

Mass comes from **volume × density** only. **Quality does not change weight.** Density stays quartz-like at every grade.

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
| Lesser | **0.5** | Slower dump / refill |
| Common | **1** | Baseline rates |
| High | **2** | Faster dump / refill |
| Highest | **3** | Faster |
| Intermediate / Greater band | **5** | Faster |
| Legendary / dragon-grade | **10** | Fastest amp; same mass and tank |

Identify, a dump-rate test, or a shop grading device reads Q. Weighing alone does not.

**Market (guild buy):** size still dominates the sticker through the **leader** band (linear with volume; see `../World/Economy.md`). **Above leader**, guilds use **stepped size bands** (not linear mm³): a Common **16 mm** marble (~113× rice volume) sells around **1.5–4 LS** (mid **~2 LS**), not the ~2.3 SG a pure volume rule would imply. Quality is a multiplier on that size band:

```
Price ≈ Price_size(V) × Q
```

So a Common marble at ~**2 LS** mid-band becomes ~**20 LS** at dragon Q **10**, same volume and mass. Rates still follow the dump/refill formulas above.

### Vs chemical batteries

Full tables (Wh/kg ratios, kW/kg burst, sustainable homes, sharding): `Batteries.md` **Mana Stone vs Battery Performance**.

Any-grade stone ≈ **1,050 Wh/kg** and **2,780 Wh/L** (mass fixed by size). Beats commercial cells; matches projected practical Li-air by mass. Higher Q raises amp per kilogram, not Wh/kg. Stones are mana tanks (area-gated dump/refill), not voltage sources. Prestige wire / fiber from stone: `RefinedMana.md`.
