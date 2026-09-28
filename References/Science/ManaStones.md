# Mana Stones

Hub: `Science.md`.
Street prices: `../World/Economy.md`.

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

**Quality does not raise capacity.** Size owns the tank. Grade speeds output and input, with dump ahead of refill:

```
Output = Q × SA                 mana/s
Input  = ((Q + 1) / 2) × SA     mana/min
Sustainable = Input / 60        mana/s
```

At **Q = 1** this matches the baseline rates (1 mana/s and 1 mana/min per mm²). A **10×** (dragon-grade) stone dumps **10×** harder and takes input **5.5×** faster. Capacity stays volume-only.

| Fist core | Capacity | Output (mana/s) | Input (mana/min) | Sustainable (mana/s) |
|---|---|---|---|---|
| 1× common | 268,080 | 20,110 | 20,110 | 335 |
| 10× dragon grade | 268,080 | 201,100 | 110,605 | 1,843 |

High-grade stones are high-amp feeds that also top off faster, not bigger batteries. Size owns capacity. Grade owns output and input.

### Weight and quality

Mass comes from **volume × density**. Quality raises density (tighter crystal packing) without growing the tank.

```
ρ₀ = 2.65 g/cm³                    baseline (Common / Q = 1), quartz-like
ρ  = ρ₀ × Q                        g/cm³
m  = ρ × V                         V in cm³ → m in grams
   = 2.65 × Q × V
Q  = ρ / ρ₀                        from weigh + size (or Identify)
```

`V` in mm³: `m (g) = 0.00265 × Q × V_mm³`.

| Grade (story) | Q | Density | Rice grain (0.019 cm³) | Marble (2.15 cm³) | Fist (268 cm³) |
|---|---|---|---|---|---|
| Lesser | **0.5** | 1.33 g/cm³ | 0.025 g | 2.9 g | 355 g |
| Common | **1** | 2.65 g/cm³ | 0.050 g | 5.7 g | 710 g |
| High | **2** | 5.3 g/cm³ | 0.10 g | 11 g | 1,400 g |
| Highest | **3** | 8.0 g/cm³ | 0.15 g | 17 g | 2,100 g |
| Intermediate / Greater band | **5** | 13.3 g/cm³ | 0.25 g | 28 g | 3,600 g |
| Legendary / dragon-grade | **10** | 26.5 g/cm³ | 0.50 g | 57 g | 7,100 g |

Masses are grams throughout (formula `m = ρ × V` with V in cm³).

Same outer size, heavier stone → higher Q. Same mass, smaller stone → denser → higher Q.

**Market (guild buy):** size still dominates the sticker through the **leader** band (linear with volume; see `../World/Economy.md`). **Above leader**, guilds use **stepped size bands** (not linear mm³): a Common **16 mm** marble (~113× rice volume) sells around **1.5–4 LS** (mid **~2 LS**), not the ~2.3 SG a pure volume rule would imply. Quality is a multiplier on that size band:

```
Price ≈ Price_size(V) × Q
```

So a Common marble at ~**2 LS** mid-band becomes ~**20 LS** at dragon Q **10**, same volume. Rates still follow the dump/refill formulas above.
