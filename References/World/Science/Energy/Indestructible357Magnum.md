# Nitroglycerin-Propelled .357 Magnum Snubnose (Indestructible Gun and Ammo)

> Earth invent loot. Closed-breech Gurney model for a high-explosive charge in an indestructible .357, energetic-material stability tables, subsonic propellant ranking, deflagration vs detonation. Not Caldris law and no manufacturing recipes. Powder chemistry / era feasibility: `GunpowderFirearms.md`, `ExplosivesHistory.md`. Firearm performance: `../../../Combat/Firearms.md`. Nav: `Index.md`.

## Model and Assumptions

- Cartridge: .357 Magnum case, usable volume ≈ 1.5 cm³
- Propellant: nitroglycerin, density 1.6 g/cm³ → charge C ≈ 2.4 g
- NG Gurney constant √(2E) ≈ 2.9 km/s → usable energy ≈ 4.2 MJ/kg × 2.4 g ≈ 10.1 kJ
- Bore area (0.357 in) A = 0.646 cm²
- Breech treated as infinitely rigid (closed-breech Gurney model)

## Terminal Velocity (Infinite Barrel)

V∞ = √(2E) / √(M/C + 1/3)

## Finite Barrel

Expansion ratio r = (V_chamber + A·L) / V_chamber

Fraction of Gurney energy delivered vs r (detonation product expansion data):

| Barrel | r | Energy fraction | Velocity fraction |
|---|---|---|---|
| 2 in | 3.2 | 0.83 | 0.91 |
| 3 in | 4.3 | 0.89 | 0.94 |
| 4 in | 5.4 | 0.92 | 0.96 |
| 6 in | 7.6 | 0.95 | 0.97 |
| 10 in | 12 | 0.97 | 0.98 |

## Projectile Mass Results (2 in Barrel)

| Projectile | M/C | V∞ | V at 2 in | KE at 2 in | Projectile momentum |
|---|---|---|---|---|---|
| 100 gr (6.5 g) | 2.7 | 1663 m/s | 1515 m/s (4970 fps) | 7.5 kJ | 9.8 N·s |
| 125 gr (8.1 g) | 3.4 | 1506 m/s | 1372 m/s (4500 fps) | 7.6 kJ | 11.1 N·s |
| 158 gr (10.2 g) | 4.3 | 1355 m/s | 1234 m/s (4050 fps) | 7.8 kJ | 12.6 N·s |
| 180 gr (11.7 g) | 4.9 | 1271 m/s | 1158 m/s (3800 fps) | 7.8 kJ | 13.5 N·s |
| 310 gr (20 g, tungsten-density) | 8.3 | 985 m/s | 897 m/s (2940 fps) | 8.0 kJ | 17.9 N·s |

Reference: standard .357 Magnum from 2 in ≈ 380 m/s, ≈ 0.6 kJ.

## Optimal Projectile Mass

- Energy transfer efficiency = (M/C) / (M/C + 1/3). It is already 91% at M/C = 3.4 so heavier bullets add only a few percent energy.
- Momentum keeps rising with mass: p ∝ √M at near-constant energy.
- With recoil irrelevant, the optimum is the heaviest projectile that fits the cylinder. A dense indestructible slug in the 250 to 310 gr range (M/C ≈ 7 to 8) maximizes energy and momentum together.
- For maximum velocity: 100 to 125 gr.

## Optimal Barrel Length

- Energy gain flattens past r ≈ 7. For .357 bore that is ≈ 6 in.
- 2 in to 6 in: +14% energy. 6 in to 10 in: +2%.
- Optimal: 5 to 6 in. Snubnose (2 in) captures 83%.

## Chamber Pressure and Acceleration

- Mean post-detonation chamber pressure ≈ 10 GPa (≈ 1.45 million psi). SAAMI .357 max is 241 MPa (35,000 psi). Ratio ≈ 40×.
- Reflected detonation pressure at the bullet base: transient peaks of 30 to 50 GPa.
- Initial force on base: F = P·A ≈ 650 kN. For 125 gr: a ≈ 8 × 10⁷ m/s² (≈ 8 million g).
- Barrel transit time (2 in): ≈ 50 to 70 µs.

## Recoil (Gun Mass 0.7 kg)

- Total momentum = projectile + gas (≈ C·V/2 in bore) + muzzle gas jet (≈ 1.5× multiplier for gas term after exit)
- 125 gr: ≈ 13 to 14 N·s → gun recoil velocity ≈ 19 m/s, recoil energy ≈ 130 J
- 310 gr: ≈ 20 N·s → ≈ 29 m/s, ≈ 290 J
- Normal .357 snub: ≈ 7 m/s, ≈ 17 J
- Impulse duration under 0.1 ms. Peak recoil force ≈ 150 to 250 kN.

## TNT Substitution

TNT √(2E) ≈ 2.44 km/s, density 1.6 g/cm³. Multiply all velocities by 0.84 and all energies by 0.71.

---

# Energetic Materials: Stability, Energy Density and Alternatives

## Energy and Physical Data

| Material | Type | Heat of explosion (MJ/kg) | Density (g/cm³) | Energy per volume (MJ/L) | Detonation velocity (m/s) |
|---|---|---|---|---|---|
| Black powder | Low explosive | 3.0 | 0.9 to 1.0 (bulk) | ≈ 3 | None (deflagrates) |
| Smokeless, single-base | Propellant | 3.5 to 4.0 | 0.9 to 1.0 (bulk) | ≈ 3.5 | None (deflagrates) |
| Smokeless, double-base | Propellant | 4.5 to 5.2 | 0.9 to 1.0 (bulk) | ≈ 4.6 | None (deflagrates) |
| TNT | High explosive | 4.6 | 1.65 | 7.6 | 6,900 |
| Nitroglycerin | High explosive | 6.3 | 1.60 | 10.1 | 7,700 |
| PETN | High explosive | 6.0 | 1.77 | 10.6 | 8,400 |
| RDX | High explosive | 5.8 | 1.82 | 10.6 | 8,750 |
| HMX | High explosive | 5.9 | 1.91 | 11.3 | 9,100 |
| CL-20 | High explosive | 6.3 | 2.04 | 12.9 | 9,500 |

## Stability and Sensitivity

| Material | Impact sensitivity (BAM, lower = more sensitive) | Long-term stability | Heat behavior | Main hazards |
|---|---|---|---|---|
| Black powder | ≈ 10 J | Indefinite if dry | Ignites ≈ 300 °C | Spark, friction, static |
| Smokeless powder | Very insensitive | 20 to 50+ years with stabilizer | Burns, does not detonate in normal use | Autocatalytic decay and self-ignition once stabilizer is depleted |
| TNT | 15 J | Decades, extremely stable | Melts 81 °C, decomposes ≈ 240 °C | Needs a booster to detonate. Exudes impurities over time. |
| Nitroglycerin | 0.2 J | Poor. Decomposes autocatalytically if impure or acidic. | Freezes 13 °C, thawing is hazardous. Ignites ≈ 200 °C. | Shock, impact, friction, heat. Most sensitive material on the list. |
| PETN | 3 J | Very good | Melts 141 °C | Impact, friction |
| RDX | 7.5 J | Very good | Melts with decomposition ≈ 205 °C | Moderate impact |
| HMX | 7.4 J | Excellent | Stable to ≈ 280 °C | Moderate impact |
| CL-20 | 4 J | Good. Crystal form changes affect sensitivity. | ≈ 210 °C | Impact, friction, high cost |

## Performance in the Indestructible .357 Gun (Relative to Nitroglycerin)

Fixed case volume, so energy scales with density × Gurney energy.

| Material | Gurney √(2E) (km/s) | Relative energy | Relative velocity | 125 gr at 2 in |
|---|---|---|---|---|
| TNT | 2.44 | 0.73 | 0.85 | ≈ 3,850 fps |
| Nitroglycerin | 2.9 | 1.00 | 1.00 | ≈ 4,500 fps |
| PETN | 2.93 | 1.13 | 1.06 | ≈ 4,780 fps |
| RDX | 2.93 | 1.16 | 1.08 | ≈ 4,850 fps |
| HMX | 2.97 | 1.25 | 1.12 | ≈ 5,030 fps |
| CL-20 | 3.1 | 1.46 | 1.21 | ≈ 5,430 fps |

Smokeless powder in the same gun reaches ≈ 1,250 fps at 2 in because it burns too slowly for a short barrel and loads at lower density.

## Gun Propulsion Alternatives (Non High-Explosive)

| Method | Practical muzzle velocity ceiling | Limit |
|---|---|---|
| Smokeless powder | ≈ 1.5 to 2 km/s | Gas sound speed, barrel pressure |
| Triple-base / nitramine propellants | ≈ 2 km/s | Same, burns cooler with less erosion |
| Liquid propellants | ≈ 2 to 2.5 km/s | Ignition control |
| Electrothermal-chemical (ETC) | ≈ 2.5 km/s | Power supply |
| Two-stage light gas gun (hydrogen) | 7 to 8 km/s | Size, single-shot |
| Railgun | 2.5 to 3.5 km/s fielded, higher in lab | Rail erosion, power |

## Summary

- Most stable: TNT, HMX, black powder (if dry).
- Least stable: nitroglycerin.
- Highest energy density: CL-20, then HMX.
- Best for the indestructible gun: CL-20 (+21% velocity over NG). HMX is the best balance of energy and stability.

---

# Subsonic Rounds: Best Propellant From the List

## Energy Needed at 1,050 fps (Subsonic)

| Bullet | Muzzle energy |
|---|---|
| 125 gr | 415 J |
| 158 gr | 525 J |
| 230 gr | 765 J |
| 310 gr | 1,030 J |

Every propellant on the list carries far more energy per case than this. The deciding factors are consistency at low charge, complete burn at low pressure and case fill.

## Ranking for Subsonic, All Weights

| Rank | Propellant | Result | Reason |
|---|---|---|---|
| 1 | Smokeless, double-base | Best | Fast formulations burn completely at low pressure. Consistent velocity. Clean. |
| 2 | Smokeless, single-base | Very good | Same behavior, slightly lower energy. Better for heavy bullets in gas guns. |
| 3 | Black powder | Good | Low energy density means a full case at subsonic charge, zero position sensitivity. Heavy fouling, smoke and flash. Bad with suppressors. |
| 4 | Triple-base / nitramine | Fair | Low flash and cool burning. Burn rate too slow for full combustion at subsonic pressures in small arms. |
| 5 | Liquid propellant | Fair | Charge is precisely meterable for any weight. Ignition at small volumes is inconsistent. |
| 6 | Nitroglycerin, PETN, RDX, HMX, CL-20 | Poor | Subsonic charge is a tiny fraction of a gram sitting in a mostly empty case. Detonating into air wastes energy in a shock wave. Small mass errors produce large velocity spread. |
| 7 | TNT | Worst | Charges this small are below TNT's critical diameter so it fails to detonate or burns erratically. |

## Non-Chemical Alternatives

| Method | Subsonic suitability | Reason |
|---|---|---|
| Railgun | Excellent | Velocity set electrically for any bullet weight. No propellant gas. |
| Electrothermal-chemical (ETC) | Very good | Electrical input tunes velocity precisely. |
| Light gas gun | Poor | Built for extreme velocity. Overkill and inefficient at subsonic speed. |

## Answer

- Best chemical propellant for subsonic, all weights: double-base smokeless powder
- Best for full-case consistency: black powder
- Best overall method: railgun (exact velocity control for every weight)
- Worst: the high explosives, TNT last

---

# Nature of Propellants and High Explosives

| Type | What it is | How it releases energy |
|---|---|---|
| Black powder | Mechanical mixture of a separate oxidizer and separate fuels | Deflagrates. Burns from grain surfaces, rate set by grain size and pressure. About 45% of the mass ends up as solid residue, which is the smoke and fouling. |
| Single-base smokeless | Nitrocellulose colloided into solid grains. Fuel and oxidizer are in the same molecule. | Deflagrates layer by layer from the grain surface. Burn rate is controlled by grain shape, size and surface coatings. Almost entirely converts to gas. |
| Double-base smokeless | Nitrocellulose with nitroglycerin dissolved into it as a solid colloid | Same surface burning as single-base with more energy and a hotter flame. The nitroglycerin is locked into a solid that burns instead of existing as a shock-sensitive liquid. |
| Triple-base | Double-base with nitroguanidine added | Burns cooler with less flash and less barrel erosion. Used mainly in artillery. |
| High explosives | Single molecules with fuel and oxidizer bonded together: nitrate esters (NG, PETN), nitroaromatics (TNT), nitramines (RDX, HMX, CL-20) | Detonate. A supersonic shock wave travels through the material and triggers reaction in microseconds. Propellants burn at millimeters to centimeters per second at the surface. Explosives react at kilometers per second throughout. |

The core distinction is deflagration versus detonation. The same chemistry can do either depending on physical form and confinement. That is why nitroglycerin works in a gun only once it is bound into a solid colloid.

## Historical Feasibility for a Renaissance-Era Person

Black powder was made throughout the Renaissance with period technology. The historical bottleneck was saltpeter supply. Natural deposits were scarce in Europe, so states ran nitre beds and saltpeter collectors that took months to years to produce usable quantities. Mills exploded regularly.

Smokeless powder was not achievable with Renaissance technology. It first appeared in 1884 (Vieille's Poudre B) and double-base powders followed with Nobel's ballistite in 1887 and British cordite in 1889. It depended on 19th-century industrial chemistry: concentrated acids at high purity, precise temperature control, solvents and chemical stabilizers to stop the product from decomposing in storage. Early nitrocellulose factories suffered catastrophic explosions until stabilization was understood in the 1860s to 1880s.

Full timeline and feasibility ladder: `ExplosivesHistory.md`.
