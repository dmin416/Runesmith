# Ionizing Radiation Types

Part 2. Fundamentals: `Fundamentals.md`. Hub: `../Radiation.md`.

## Alpha particles

| Property | Value |
|---|---|
| Nature | Helium-4 nucleus (2p, 2n) |
| Charge | +2 |
| Mass | 3,727 MeV/c² (~7,300× electron) |
| Typical energy | 4–9 MeV from radioactive decay |
| Range in air | ~3–7 cm |
| Range in tissue | ~40–90 µm |
| LET | ~100–200 keV/µm (near RBE peak) |
| wR | 20 |
| Stopped by | Paper, dead outer skin (~20–40 µm) |

**Sources:** Rn-222 and daughters, Po-210, Pu-239, Am-241, U, Th. GCR ~12% helium nuclei (relativistic; penetrate deeply, unlike decay alphas).

**Physics:** Heavy, doubly charged; dense ionization; Bragg peak at end of range.

**Biology:** Harmless externally. Catastrophic internally (lung, bone, liver, kidney). Radon: second-leading cause of lung cancer worldwide. Po-210 poisoning (Litvinenko) killed via internal alpha dose of several Sv.

**Shielding:** Trivial externally. Internal protection = prevent intake.

## Beta-minus (electrons)

| Property | Value |
|---|---|
| Nature | High-speed electron from nucleus (n → p + e + antineutrino) |
| Charge | −1 |
| Mass | 0.511 MeV/c² |
| Energy | Continuous to E_max; average ≈ E_max/3 |
| Range in tissue | µm to ~1 cm |
| LET | ~0.2–2 keV/µm |
| wR | 1 |

| Isotope | E_max | Range in tissue |
|---|---|---|
| Tritium (H-3) | 0.0186 MeV | ~6 µm |
| Carbon-14 | 0.156 MeV | ~0.3 mm |
| Strontium-90 | 0.546 MeV | ~2 mm |
| Phosphorus-32 | 1.71 MeV | ~8 mm |
| Yttrium-90 | 2.28 MeV | ~11 mm |

Rule of thumb: range (g/cm²) ≈ E_max (MeV) / 2 for E_max > 0.8 MeV.

**Space:** Outer Van Allen electrons (0.1–10 MeV), Jupiter magnetosphere (Europa surface dose), GCR electrons (~1%).

**Biology:** Skin and eye lens externally. Beta burns (Chernobyl firefighters, Castle Bravo). Internally Sr-90 in bone, I-131 in thyroid.

**Shielding:** Few mm plastic/acrylic/aluminum first. Lead makes bremsstrahlung. Fraction ≈ 3.5×10⁻⁴ × Z × E_max (MeV).

## Beta-plus (positrons)

Antimatter electron. Annihilates → two 511 keV gammas at 180°. Sources: F-18 (PET), C-11, O-15, Na-22, rare K-40 branch, pair production, GCR positrons. PET ~7 mSv. Track like beta-minus plus annihilation gammas.

## Gamma rays

High-energy photons from excited nuclei. Charge/mass 0. Energy ~100 keV to several MeV (to TeV astrophysical). No fixed range; exponential attenuation. Low LET via secondary electrons. wR = 1.

**Sources:** Co-60, Cs-137, I-131, K-40, fission, neutron capture, detonations, solar flares, GRBs, pulsars.

**Photon interactions in water:**

| Mechanism | Dominant range | Physics |
|---|---|---|
| Photoelectric | < ~30 keV | Absorbed; ejects inner electron; ∝ Z³/E³ |
| Compton | ~30 keV to ~25 MeV | Partial energy to outer electron |
| Pair production | > 1.022 MeV; dominant > ~25 MeV | e⁺ + e⁻ near nucleus |
| Photonuclear | > ~8–10 MeV | Knocks neutrons from nuclei |

`I = I₀ · e^(−μx)`

| Source | Lead HVL | Concrete | Water |
|---|---|---|---|
| 100 keV X-ray | ~0.25 mm | ~1.5 cm | ~4 cm |
| Cs-137 (662 keV) | ~0.65 cm | ~4–5 cm | ~8 cm |
| Co-60 (1.25 MeV) | ~1.2 cm | ~6 cm | ~11 cm |

**Biology:** Whole-body penetration. Primary external ARS cause.

## X-rays

Photons from electron shells or bremsstrahlung. Same physics as gamma at equal energy. Medical/industrial/solar/spacecraft secondaries.

| Procedure | Effective dose |
|---|---|
| Dental X-ray | ~0.005 mSv |
| Chest X-ray | ~0.02–0.1 mSv |
| Mammogram | ~0.4 mSv |
| Head CT | ~2 mSv |
| Abdomen/pelvis CT | ~8–10 mSv |
| Cardiac CT angiography | ~10–15 mSv |

## Neutrons

Charge 0. Mass 939.6 MeV/c². Free mean life ~880 s. wR 2.5–20 by energy.

| Class | Energy |
|---|---|
| Thermal | ~0.025 eV |
| Epithermal | 0.025 eV–~10 keV |
| Intermediate | 10–100 keV |
| Fast | 0.1–20 MeV (fission ~2 MeV avg; D-T 14.1 MeV) |
| High-energy | >20 MeV to GeV |

**Sources:** Fission, detonations, criticality, fusion, Cf-252, Am-Be, spallation, cosmic secondaries (aircraft + spacecraft hull).

**Tissue:** Elastic scatter (H recoils = high LET dose for fast n); inelastic; capture (¹H(n,γ) 2.22 MeV; ¹⁴N(n,p)); activation (²³Na → ²⁴Na dose estimate; ³²S(n,p) in hair).

**Criticality examples:** Daghlian ~5 Sv (25 days); Slotin ~10 Gy/~21 Sv (9 days); Ouchi ~16–20 Sv (83 days).

**Shielding:** (1) moderate with H-rich material, (2) capture with B-10 / Li-6 / Cd, (3) stop capture gammas with lead/dense concrete. Lead alone is poor. Water is excellent.

## Protons

H nucleus. wR = 2. SPE 10 MeV–GeV; GCR peaks ~1 GeV. LET ~0.2 keV/µm at 1 GeV → ~80 keV/µm at end of track.

| Energy | Range in water |
|---|---|
| 10 MeV | ~1.2 mm |
| 30 MeV | ~9 mm |
| 100 MeV | ~7.7 cm |
| 200 MeV | ~26 cm |
| 1 GeV | ~3.3 m (most collide before stop) |

**Sources:** GCR ~87% by count; SPE; inner Van Allen / SAA; proton therapy 70–250 MeV.

**Biology:** Fast SPE protons low-LET (RBE ~1.1–1.5); end-of-track high-LET. Large SPEs = primary acute ARS threat in space. Bragg peak used in therapy.

## Heavy ions (HZE)

Nuclei heavier than He. ~1% of GCR by count. LET scales Z²/β². Fe-56 at 1 GeV/n ~150 keV/µm (~676× a proton at same speed). wR = 20.

Track: nm core + mm penumbra of delta rays. Hit rate deep space: every cell nucleus traversed by proton/secondary every few days; by HZE every few months.

**Effects:** Clustered lesions, complex rearrangements, phosphenes (Apollo/ISS), rodent CNS deficits at tens of mGy, CVD, cataracts, high carcinogenesis per Gy.

**Fragmentation:** HZE shatter in shields → lighter fragments + neutrons (GCR shielding plateau). Prefer H-rich shields. No practical thickness eliminates GCR.

## Muons

Mass 105.7 MeV/c² (~207× e). Life 2.2 µs. Sea-level ~1/cm²/min, ~4 GeV mean. Cosmic pion daughters. Dominant sea-level cosmic dose (~0.3–0.4 mSv/yr total cosmic). Low LET; negligible hazard. Penetrates hundreds of m of rock.

## Pions

π± 139.6 MeV/c² (26 ns); π⁰ 135.0 (→ two gammas). wR = 2 charged. GCR secondaries. Negative-pion therapy trialed historically.

## Fission fragments

~170 MeV kinetic total. Range ~10–25 µm. LET thousands keV/µm. wR = 20. Internal only (inhaled/ingested actinides). Fragments stay highly radioactive.

## Secondary radiation

Bremsstrahlung (∝ Z²); delta rays; characteristic X-rays; spallation products; Cherenkov (harmless light; signals intense field); capture gammas; activation products.

## Neutrinos

Cross-section ~10⁻⁴⁴ cm². Solar flux ~6.5×10¹⁰ /cm²/s. Effectively zero dose. Supernova burst lethal only within a few AU (everything else kills first).

## Antimatter in fields

GCR antiprotons ~1 per 10⁴ protons. Annihilation ~1.88 GeV mostly as pions. Negligible natural dose. Positrons: above.
