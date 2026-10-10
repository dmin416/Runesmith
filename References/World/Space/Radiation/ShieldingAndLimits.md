# Shielding and Limits

Orbit-planning numbers: areal density, SPE/GCR attenuation, astronaut limits, simple robust R_a / R_c. Full type physics: `Ionizing.md`. Environments: `Environments.md`. Heat–radiation hypothesis: `RobustHeatHuman.md`. Hub: `../Radiation.md`.

Terra has not locked different GCR / belt numbers yet.

## Astronaut limits

**Career (cancer risk):** NASA career limit **600 mSv**. From risk of exposure-induced death (REID) for a 35-year-old female (most susceptible group). Threshold is **3% REID**. ESA and Roscosmos use roughly **1,000 mSv** career limits.

**Short-term (tissue damage):** NASA short-term limit **250 mSv** to blood-forming organs over **30 days**. Skin and eye lens have separate higher limits (~**1.5 Gy** and **1 Gy** per 30 days).

**Comparison:** DOE occupational limit is **50 mSv/yr**. Astronaut exposures run one to two orders of magnitude higher than terrestrial radiation workers.

Long-term cancer risk ≈ **5%** lifetime fatal cancer per Sv. That produces NASA's number: 3% risk ÷ 5%/Sv = **0.6 Sv**.

A typical six-month ISS mission delivers ~**40–90 mSv**. A Mars mission would expose astronauts to around **1000 mSv** unless shielding cuts it.

## Acute whole-body quick table

| Dose | Effect |
|---|---|
| <250 mSv | No symptoms; minor blood changes detectable above ~100 mSv |
| 0.5–1 Sv | Blood count drop, mild fatigue |
| 1–2 Sv | Mild radiation sickness; nausea in a minority |
| 2–4 Sv | Moderate sickness, hair loss, infection risk |
| 4–5 Sv | LD50/60 without treatment (half die within 60 days) |
| 6–8 Sv | Mostly fatal even with intensive care |
| 10–20 Sv | Gut lining destroyed; death in ~2 weeks |
| >50 Sv | Nervous system collapse; death in hours to 2 days |

Full ARS table: `BiologicalEffects.md`.

## Shielding

Measured as areal density (**g/cm²**), mass per area of surface.

| Barrier | Approx. areal density |
|---|---|
| EVA suit | ~0.3–1 g/cm² |
| Spacecraft hull (ISS, Orion) | ~5–20 g/cm² including equipment |
| Orion storm shelter (crew packs stowage around themselves) | ~20–30 g/cm² |
| 2–3 m lunar regolith | ~300–500 g/cm² |
| Earth's atmosphere | ~1,000 g/cm² |

### Effectiveness by radiation type

| Shielding (aluminum) | SPE dose reduction | GCR dose reduction |
|---|---|---|
| Suit (~0.5 g/cm²) | ~10–30% (stops low-energy protons only) | ~0% |
| 5 g/cm² | ~70–80% | ~10% |
| 10 g/cm² | ~90% | ~15–20% |
| 20 g/cm² | ~95%+ | ~25–30% |
| 50 g/cm² | ~99% | ~35–40%, then plateaus |

Solar protons stop easily. Galactic cosmic rays are heavy nuclei near light speed: they shatter in the shield and spray secondary neutrons, so thick metal hits diminishing returns. Hydrogen-rich materials (water, polyethylene) outperform aluminum by roughly **20–30%** per unit mass. A suit protects against essentially nothing except electrons and the softest protons. An SPE during EVA is mission-ending or lethal.

### Attenuation approximations

```
SPE:  D(x) = D₀ · e^(−x/λ)                 λ ≈ 4–8 g/cm² (aluminum)
GCR:  D(x) = D₀ · [(1−f) + f · e^(−x/λ)]   f ≈ 0.4, λ ≈ 15 g/cm²
```

`x` = shield areal density, `D₀` = unshielded dose. The GCR form captures the floor: about **60%** of the dose penetrates any practical thickness.

## Simple robust-body formulas

Radiation tolerance splits into two traits. They fail by different mechanisms. Expanded heat–radiation model: `RobustHeatHuman.md`.

### Acute tolerance

```
LD50_robust = LD50_base × R_a
P(death) = 1 / (1 + (LD50_robust / D)^k)
```

- `LD50_base` = **4.5 Sv** untreated, ~**6.5 Sv** with modern medical care
- `k` ≈ **6–8**
- `R_a` = acute resistance factor

### Chronic / cancer tolerance

```
D_career = 0.6 Sv × R_c        (at 3% REID)
```

- `R_c` = cancer resistance factor (tumor suppressor redundancy, repair fidelity)

### Dose-rate repair

```
D_eff(t) = (Ḋ / λ) · (1 − e^(−λt))       λ = ln2 / t_half
```

`t_half` ≈ **20–30 days** for human marrow recovery.

### Time to limit

```
t_max = (D_limit × R) / (Ḋ_unshielded × S)
```

`S` = fraction of dose passing the shielding.

### Reference R_a

| Organism / condition | R_a (vs untreated human) |
|---|---|
| Average human | 1 |
| Human with intensive care / marrow transplant | ~1.5 |
| Mouse | ~1.7 |
| Goldfish | ~4–5 |
| Cockroach | ~15 |
| Fruit fly | ~140 |
| Tardigrade | ~1,000 |
| *Deinococcus radiodurans* | ~3,000+ |

### Days until career limit (600 mSv × R_c), unshielded

| Environment | R_c = 1 | R_c = 2 | R_c = 5 |
|---|---|---|---|
| ISS (0.4 mSv/day) | 1,500 days | 3,000 days | 7,500 days |
| Mars surface (0.67) | 896 days | 1,791 days | 4,478 days |
| Lunar surface (1.4) | 429 days | 857 days | 2,143 days |
| Deep space (1.8) | 333 days | 667 days | 1,667 days |
| Europa (5,400) | 2.7 hours | 5.3 hours | 13.3 hours |

**Europa acute:** base human reaches LD50 (4.5 Sv) in ~**20 hours**. `R_a = 5` ~**4 days**. `R_a = 1,000` ~**2.3 years**.

## Sources

- [National Academies: NASA Should Update Astronaut Radiation Exposure Limits](https://www.nationalacademies.org/news/nasa-should-update-astronaut-radiation-exposure-limits-improve-communication-of-cancer-risks)
- [NASA NTRS: Space Radiation Protection (Simonsen)](https://ntrs.nasa.gov/api/citations/20250006168/downloads/ASCEND%20Simonsen%20draft%201.pdf)
- [Sky at Night: New radiation limits for astronauts](https://www.skyatnightmagazine.com/news/new-radiation-limits-for-astronauts-could-make-spaceflight-farer/)
