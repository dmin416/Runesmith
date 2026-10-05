# Flywheel Energy Applications

Hub: `../Science.md`. Storage sizes: `FlywheelStorage.md`. Pair / drain bottleneck (mundane): `Generators.md`. Air / eye / steampunk lasers: `Optics.md`, `../../../Combat/Lasers.md`. Room light ladder: `Lighting.md`.

## Magic lossless stack (fiction assumption)

This sheet assumes a **prestige / late invent** stack that bypasses the mundane generator bottleneck in `Generators.md`:

- Indestructible counter-rotating flywheel pairs (`FlywheelStorage.md`)
- Motor/generator of indestructible materials
- Wiring of perfectly conducting magical silver: **zero resistance, zero loss** (electrical path; not mana η_cond)
- **Magical light crystal:** electricity → light at **100%** efficiency, **no heat** at the emitter
- For laser use, the crystal emits a coherent single-color **green** beam (~500 nm)

Under this stack, energy reaches the crystal with no step losses and **discharge rate is unlimited**, so any beam power is available instantly. Mundane cryogenic copper generators do **not** get this; they stay power-capped.

## Flywheel sets (energy reminder)

| Set | Mass | At 0.1c | At 0.9c |
|---|---|---|---|
| Small rim pair | 2 × 20 g | ~17.5 TJ | ~4.3 PJ |
| Big rim pair | 2 × 20 kg | ~17.5 PJ | ~4.3 EJ |
| Drum pair | 2 × 5,000 kg | ~2.25 EJ | ~353 EJ |

0.9c rim stretch still conflicts with adamantium no-stretch (`FlywheelStorage.md` Open).

---

# Laser

## Why this stack is ideal

Real lasers waste heat (often only 30–50% of electricity becomes light). The crystal makes no heat, silver has no resistance and the flywheel can dump at any rate. Limits left: **stored energy**, **beam optics** and **the air the beam travels through**.

## Power classes

| Beam | Power | Feel |
|---|---|---|
| Laser pointer | ~5 mW | Handheld glare / toy |
| Industrial cutter | 1–10 kW | Cuts steel plate |
| Military demonstrator | 50–300 kW | Drones / small rockets |
| Heavy beam | ~10 MW | Beyond fielded Earth lasers |
| Fortress beam | ~1 GW | Large power-plant class output in one beam |
| Siege beam | ~1 TW | Continent-scale electricity, one beam |

## Continuous beam duration

| Beam power | Small 0.1c | Small 0.9c | Big 0.1c | Big 0.9c | Drum 0.1c | Drum 0.9c |
|---|---|---|---|---|---|---|
| 5 mW | ~111M yr | ~27B yr | ~111B yr | ~27T yr | ~14T yr | ~2.2Q yr |
| 100 kW | ~5.5 yr | ~1,350 yr | ~5,500 yr | ~1.35M yr | ~713k yr | ~112M yr |
| 10 MW | ~20 days | ~13.5 yr | ~55 yr | ~13,500 yr | ~7,100 yr | ~1.1M yr |
| 1 GW | ~4.9 h | ~49 days | ~203 days | ~135 yr | ~71 yr | ~11,200 yr |
| 1 TW | ~17.5 s | ~71 min | ~4.9 h | ~49 days | ~26 days | ~11 yr |

## Pulse shots

| Shot class | Pulse energy | Pulse length | Peak power |
|---|---|---|---|
| Sidearm | 50 kJ | 1 ms | 50 MW |
| Rifle | 500 kJ | 1 ms | 500 MW |
| Heavy | 5 MJ | 5 ms | 1 GW |

Pulse lengths keep peak power under the ~**1.2 GW** self-focusing limit for green (~500 nm) in air (below).

| Shot | Small 0.1c | Small 0.9c | Big 0.1c | Big 0.9c | Drum 0.1c | Drum 0.9c |
|---|---|---|---|---|---|---|
| Sidearm 50 kJ | ~350M | ~85B | ~350B | ~85T | ~45T | ~7.1Q |
| Rifle 500 kJ | ~35M | ~8.5B | ~35B | ~8.5T | ~4.5T | ~710T |
| Heavy 5 MJ | ~3.5M | ~850M | ~3.5B | ~850B | ~450B | ~71T |

One sidearm shot per second nonstop: small pair at 0.1c lasts ~**11 years**.

## Burning through material

Energy to bore a **1 cm** wide hole through **1 cm** of material if the beam's full energy couples into the target.

| Material | Melt through | Vaporize through |
|---|---|---|
| Water / ice | n/a | ~2 kJ |
| Aluminum | ~2 kJ | ~30 kJ |
| Steel | ~6 kJ | ~51 kJ |
| Tungsten | ~11 kJ | ~80 kJ |

A 50 kJ sidearm vaporizes a clean 1 cm hole through 1 cm of steel. Melting is cheaper than vaporizing. Full coupling holds in vacuum; in air, surface plasma can shield the target.

## Spot size and range

Spot diameter ≈ **2.4 × λ × range ÷ aperture** (λ ~500 nm green).

| Range | 2 cm aperture (sidearm) | 10 cm (rifle) | 1 m (fortress) |
|---|---|---|---|
| 10 m | ~0.6 mm | ~0.1 mm | ~0.01 mm |
| 100 m | ~6 mm | ~1.2 mm | ~0.1 mm |
| 1 km | ~6 cm | ~1.2 cm | ~1.2 mm |
| 10 km | ~61 cm | ~12 cm | ~1.2 cm |
| 100 km | ~6 m | ~1.2 m | ~12 cm |
| 1,000 km | ~61 m | ~12 m | ~1.2 m |
| Moon distance | ~23 km | ~4.7 km | ~470 m |

Near the ground, turbulence limits useful aperture to roughly **~10 cm** without adaptive optics (larger lens alone ≈ rifle column).

## Intensity (1 cm spot)

| Continuous power | Intensity | Through air |
|---|---|---|
| 10 kW | ~1.3×10⁴ W/cm² | Propagates; blooming sets range |
| 1 MW | ~1.3×10⁶ W/cm² | Near plasma ignition at target / dust |
| 1 GW | ~1.3×10⁹ W/cm² | Plasma blocks; vacuum only |
| 1 TW | ~1.3×10¹² W/cm² | Vacuum only |

Sunlight at Terra surface ~0.1 W/cm². A 1 GW beam in a 1 cm spot is ~13 billion× brighter.

---

## Atmospheric limits

Air ceilings (independent of stored energy). Complements plasma notes in `Optics.md`.

### Continuous-wave

1. **Thermal blooming:** past an optimum, more power heats air faster than it clears; intensity on target can fall.
2. **Plasma ignition / absorption waves:** ~10⁶–10⁷ W/cm² at target or dust (CO2-class; higher for shorter λ) → plasma travels back up the beam and blocks delivery.
3. **Diffraction:** min spot ~ λ × range ÷ aperture.
4. **Turbulence:** useful aperture capped by Fried parameter (~few cm to ~10 cm near ground) without adaptive optics.
5. **Weather:** fog, rain, dust, smoke → exponential loss; heavy fog can kill most wavelengths in tens to hundreds of meters.

### Pulsed

1. **Breakdown:** air ionizes ~10⁹ W/cm² (ns CO2), ~10¹¹ (ns 1 µm), ~10¹²–10¹³ (ps), ~10¹³–10¹⁴ (fs). Aerosols lower by 10–100×.
2. **Plasma shielding:** rest of pulse absorbed; ns pulses can launch a detonation wave back up the beam. At 10.6 µm dense plasma can reflect; at 1 µm and shorter it absorbs.
3. **Self-focusing:** above ~3 GW peak at 800 nm (scales ~λ²); at ~500 nm green ≈ **1.2 GW**. Extra power filaments instead of one clean beam.
4. **Intensity clamping:** filaments lock near ~5×10¹³ W/cm².
5. **Rep rate:** heated channel needs milliseconds to clear; faster → blooming on following pulses.

### Absolute ceiling

Through air: highest traveling intensity ~10¹³–10¹⁴ W/cm² (fs filament). CW far lower. Higher only at a focus on the target or in vacuum.

### For the flywheel laser

- **Energy is never the bottleneck in air.** Even the small pair outstores what one path can deliver.
- **One path has a ceiling.** Past blooming / plasma ignition, extra power wastes or blocks.
- **More beams, not bigger beams.** Separate apertures; combined intensity at target can still ignite plasma.
- **Pulse length:** keep peak under ~1.2 GW green to avoid filamentation.
- **Rate:** hundreds of shots/s per path at most before the channel degrades.
- **Weather wins** within tens to hundreds of meters in fog/smoke.
- **Vacuum** removes atmospheric ceilings; only diffraction and stored energy remain.

### Visibility

Pure beam invisible from the side in clean air. High power: scatter, heated air and plasma make it visible.

---

# Lighting (crystal)

Perfect white converter ≈ **300 lm/W**. Pure green max **683 lm/W** (eye peak; `Lighting.md`, `Waves.md`). Table uses **white**.

| Light source | Lumens | Crystal power |
|---|---|---|
| Candle | ~12 | ~0.04 W |
| ~60 W incandescent equivalent | ~800 | ~2.7 W |
| Bright room | ~3,000 | ~10 W |
| Streetlight | ~10,000 | ~33 W |
| Sports stadium | ~150 million | ~500 kW |
| City of 1M, all lighting | ~6 billion | ~20 MW |
| Full daylight over 1 km² | ~100 billion | ~330 MW |
| Full daylight over 100 km² | ~10 trillion | ~33 GW |

Crystal stays cool. Illuminated surfaces still absorb and warm.

| Application | Small 0.1c | Small 0.9c | Big 0.1c | Big 0.9c | Drum 0.1c | Drum 0.9c |
|---|---|---|---|---|---|---|
| Household bulb (~2.7 W) | ~205k yr | ~50M yr | ~205M yr | ~50B yr | ~26B yr | ~4.1T yr |
| Sports stadium | ~1.1 yr | ~271 yr | ~1,100 yr | ~271k yr | ~143k yr | ~22M yr |
| City 1M lighting | ~10 days | ~6.8 yr | ~28 yr | ~6,800 yr | ~3,600 yr | ~559k yr |
| Daylight 1 km² | ~15 h | ~148 days | ~1.7 yr | ~406 yr | ~214 yr | ~33.6k yr |
| Daylight 100 km² | ~9 min | ~14.5 days | ~6 days | ~4.1 yr | ~2.1 yr | ~336 yr |

Caldris street baseline stays flame / mana-stone (`Lighting.md`) until this crystal stack is invented.

---

# General electrical loads

Scale anchors (Earth-like cities; Terra kingdoms ~1M people at Caldris example).

| Load | Power |
|---|---|
| Average home | ~1.2 kW |
| City of 1M, all electricity | ~1.5 GW |
| Electric vehicle | ~0.6 MJ per km |

| Application | Small 0.1c | Small 0.9c | Big 0.1c | Big 0.9c | Drum 0.1c | Drum 0.9c |
|---|---|---|---|---|---|---|
| Average home | ~460 yr | ~113k yr | ~460k yr | ~113M yr | ~59M yr | ~9.3B yr |
| City of 1M | ~3.2 h | ~33 days | ~135 days | ~90 yr | ~48 yr | ~7,500 yr |
| EV range | ~29M km | ~7.1B km | ~29B km | ~0.75 ly | ~0.4 ly | ~62 ly |

---

## Open

- Whether magical silver / light crystal are invent-path or PotentialMagic only
- Adaptive optics availability for fortress apertures in atmosphere
- Sync pulse / blinding doctrine in `Combat/Lasers.md` when this stack shows up in story
