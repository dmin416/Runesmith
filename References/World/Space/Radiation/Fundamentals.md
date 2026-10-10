# Radiation Fundamentals

Part 1. Hub: `../Radiation.md`. Pack: `Index.md`.

## Definition

Radiation is energy traveling through space as electromagnetic waves (photons) or as moving particles. The single most important dividing line is whether one quantum carries enough energy to strip an electron from an atom.

- **Ionizing radiation:** above ~10 eV per quantum (biological convention; ~124 nm wavelength). Water itself ionizes at 12.6 eV (~98 nm). Breaks chemical bonds directly, creates free radicals, damages DNA.
- **Non-ionizing radiation:** below ~10 eV. Cannot break bonds by ionization. Damages tissue through photochemistry (UV), heating (IR, microwave, RF) or induced electrical currents (ELF).

## Units

| Quantity | SI unit | Legacy unit | Meaning |
|---|---|---|---|
| Absorbed dose | Gray (Gy) = 1 J/kg | rad (1 rad = 0.01 Gy) | Raw energy deposited per kg of tissue |
| Equivalent dose | Sievert (Sv) | rem (1 rem = 0.01 Sv) | Absorbed dose × radiation weighting factor (wR) |
| Effective dose | Sievert (Sv) | rem | Equivalent dose summed across organs × tissue weighting factors (wT); estimates whole-body cancer risk |
| Gray-Equivalent | Gy-Eq | none | NASA unit for tissue damage (deterministic effects) using RBE instead of wR |
| Activity | Becquerel (Bq) = 1 decay/s | Curie (Ci) = 3.7×10¹⁰ Bq | How radioactive a source is |
| Exposure | C/kg | Roentgen (R) = 2.58×10⁻⁴ C/kg | Ionization produced in air by X/gamma rays |
| Fluence | particles/cm² | none | Number of particles crossing an area |
| Linear Energy Transfer (LET) | keV/µm | none | Energy deposited per micrometer of track |
| Relative Biological Effectiveness (RBE) | ratio | none | Dose of 250 kV X-rays ÷ dose of test radiation producing the same effect |

## Radiation weighting factors (ICRP 103)

| Radiation | wR |
|---|---|
| Photons (X, gamma) | 1 |
| Electrons, positrons, muons | 1 |
| Protons, charged pions | 2 |
| Alpha particles, fission fragments, heavy ions | 20 |
| Neutrons | 2.5 to 20 (continuous function of energy, peaks ~20 near 1 MeV) |

Neutron weighting function:

```
En < 1 MeV:        wR = 2.5 + 18.2 · exp(−[ln(En)]² / 6)
1 ≤ En ≤ 50 MeV:   wR = 5.0 + 17.0 · exp(−[ln(2En)]² / 6)
En > 50 MeV:       wR = 2.5 + 3.25 · exp(−[ln(0.04En)]² / 6)
```

## Tissue weighting factors (ICRP 103)

| Tissue | wT |
|---|---|
| Red bone marrow, colon, lung, stomach, breast, remainder tissues | 0.12 each |
| Gonads | 0.08 |
| Bladder, esophagus, liver, thyroid | 0.04 each |
| Bone surface, brain, salivary glands, skin | 0.01 each |

## LET, RBE and oxygen effect

- **Low LET (<10 keV/µm):** photons, electrons, high-energy protons, muons. Ionizations spaced far apart. Damage sparse and mostly repairable.
- **High LET (>10 keV/µm, up to thousands):** alpha particles, heavy ions, neutron recoil protons, fission fragments. Dense tracks. Clustered, hard-to-repair DNA damage.
- **RBE peaks near 100 keV/µm.** Spacing between ionizations (~2 nm) matches DNA double-helix width, so both strands break at once. Above ~100 keV/µm, energy is wasted on cells already killed (overkill) and RBE drops.
- **Oxygen Enhancement Ratio (OER):** oxygen locks in radical damage. Low-LET is 2.5–3× more damaging to well-oxygenated tissue than hypoxic tissue. High-LET shows OER ≈ 1.

## Timeline of damage

| Stage | Timescale | Events |
|---|---|---|
| Physical | 10⁻¹⁸ to 10⁻¹⁵ s | Ionization and excitation of atoms |
| Physicochemical | 10⁻¹⁵ to 10⁻¹² s | Water radiolysis: H₂O → •OH, e⁻(aq), H•, H₃O⁺ |
| Chemical | 10⁻¹² to 10⁻⁶ s | Radicals diffuse a few nm, attack DNA, proteins, lipids; H₂O₂ forms |
| Early biological | Seconds to hours | Enzymatic repair, checkpoints, apoptosis signaling |
| Tissue | Days to weeks | Stem cell depletion, acute radiation syndrome |
| Late | Months to years | Fibrosis, cataract, vascular disease |
| Stochastic | Years to decades | Cancer, hereditary mutations |

## DNA damage per Gray per cell (low-LET)

| Lesion | Count per Gy per cell |
|---|---|
| Base damage | >1,000 |
| Single-strand breaks | ~1,000 |
| DNA-protein crosslinks | ~150 |
| Double-strand breaks | ~20–40 |

**Direct vs indirect:**
- Low LET: ~1/3 direct, ~2/3 indirect (hydroxyl radicals from water)
- High LET: majority direct; radicals recombine before reaching DNA

**Repair pathways:** BER, NER, SSBR, NHEJ (fast, error-prone), HR (accurate, S/G2 only), MMEJ (backup, highly error-prone).

## Deterministic vs stochastic

| | Deterministic (tissue reactions) | Stochastic |
|---|---|---|
| Cause | Mass cell death | Mutation in a surviving cell |
| Threshold | Yes | No (linear no-threshold assumed) |
| Severity scales with dose | Yes | No; probability scales with dose |
| Examples | Radiation sickness, burns, cataract, sterility | Cancer, hereditary disease |
| Risk coefficient | Threshold-based | ~5% lifetime fatal cancer per Sv (ICRP nominal ~5.5%) |
