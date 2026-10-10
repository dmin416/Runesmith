# Space Radiation

Earth-reference radiation science for orbit / deep-space planning and robust-body design. Atmosphere / magnetosphere: `Atmosphere.md`. Habitats: `Orbit/`. Hub: `Space.md`. Nav: `Index.md`.

Terra has not locked different GCR / belt numbers yet. Use Earth-system figures until a world file says otherwise.

## Pack

| File | Holds |
|---|---|
| [Radiation/Fundamentals.md](Radiation/Fundamentals.md) | Definition, units, wR / wT, LET, RBE, DNA damage timeline |
| [Radiation/Ionizing.md](Radiation/Ionizing.md) | Alpha through neutrinos, secondaries, antimatter |
| [Radiation/NonIonizing.md](Radiation/NonIonizing.md) | UV through ELF; IR burn / flux tables; microwave SAR |
| [Radiation/Environments.md](Radiation/Environments.md) | Earth, space, Jupiter moons, extremes, nuclear partition |
| [Radiation/BiologicalEffects.md](Radiation/BiologicalEffects.md) | ARS, organ thresholds, late effects, cross-species LD50 |
| [Radiation/ShieldingAndLimits.md](Radiation/ShieldingAndLimits.md) | Areal density, SPE/GCR attenuation, astronaut career / acute limits, simple R_a / R_c |
| [Radiation/RobustHeatHuman.md](Radiation/RobustHeatHuman.md) | Heat vs ionizing physics; T1/T2 heat resistance; R_total model; scenarios |
| [Radiation/RadiationVision.md](Radiation/RadiationVision.md) | Damage immunity vs sight: flash blindness still works; phosphenes without harm |

Body / heat physiology cross-link: `../Science/Body/Body.md`.

## Quick orbit numbers

| Location | Dose rate |
|---|---|
| Earth surface | ~0.008 mSv/day |
| ISS (LEO) | ~0.25–0.5 mSv/day |
| Lunar surface | ~1.4 mSv/day |
| Deep space | ~1.8 mSv/day |
| Mars surface | ~0.65–0.7 mSv/day |
| Europa surface | ~5.4 Sv/day |
| Io surface | ~36 Sv/day |

NASA career limit **600 mSv** (3% REID). Untreated human LD50 ≈ **4.5 Sv**. Detail: `Radiation/ShieldingAndLimits.md`, `Radiation/BiologicalEffects.md`.
