# Terra's Atmosphere Layers

Hub: `Space.md`. Ambient mana vs altitude: `../Science/Energy/ManaConcentration.md`. Flight / air density: `../Science/Energy/Flight.md`. World size lock: `../World.md` (Earth-sized planet).

Terra uses Earth-like layer heights and weather physics. Open-air mana follows **pressure** (`C = P₀ / P(h)`) to the thermopause / exobase, then **haze number density** through the exosphere / geocorona to the solar-wind floor. Layer names below are the air-structure map. Digits: `../Science/Energy/ManaConcentration.md`.

## Troposphere

**Surface to about 7.5 miles** (about 5 miles at the poles and 11 miles at the equator)

- Holds about 75 to 80% of the atmosphere's mass and nearly all water vapor
- All weather happens here
- Temperature drops with altitude to about -60°F at the top
- Upper boundary: the tropopause
- Open-air mana: mild. About `C ≈ 2` at 3.4 mi; tropopause about `C ≈ 5`

## Stratosphere

**7.5 to 31 miles**

- Contains the ozone layer (about 9 to 22 miles), which absorbs most UV radiation
- Temperature rises with altitude because of that ozone, reaching about 32°F at the top
- Very stable air with little vertical mixing
- Weather balloons top out here at around 20 to 25 miles
- Upper boundary: the stratopause
- Open-air mana: about `C ≈ 10` at 10 mi through `~10^3` at 30 mi. Balloon top about `C ~ 360`

## Mesosphere

**31 to 53 miles**

- Coldest layer, dropping to about -130°F or lower at the top
- Meteors burn up here
- Noctilucent clouds form near 50 miles
- Too high for balloons and too low for satellites, so it is the least studied layer
- Upper boundary: the mesopause
- Open-air mana: about `C ~ 10^3` (30 mi) through `~10^5` (50 mi)

## Thermosphere

**53 to about 370 miles** (ranges 310 to 620 miles depending on solar activity)

- Temperatures reach 2,000 to 3,600°F or more, yet it would feel freezing because the gas is so thin
- Auroras glow here, mostly between 60 and 200 miles
- The Kármán line at 62 miles, the conventional start of space, sits near its bottom
- Orbital stations sit within it around 250 miles when the story uses that band. One-person LEO budget: `Orbit/LowEarthOrbitHabitat.md`
- Upper boundary: the thermopause
- Open-air mana: `P₀/P` law. Kármán about `C ~ 3×10^6`. Exobase about `C ~ 10^12`. Thermosphere scale height is large, so vacuum hardens slowly

## Exosphere

**About 370 to 6,200 miles**

- Mostly hydrogen and helium
- Particles are so sparse they rarely collide and follow arcing paths; some escape Terra entirely
- Effectively outer space for all practical purposes
- Upper boundary: fades into the solar wind
- Open-air mana: haze regime. `C = C_exo × (n_exo / n)`. Near-exobase climb is tiny (about `1.2×10^12` → `~1.7×10^12` by 6,200 mi)

## Geocorona

**Extends to about 391,000 miles**

- A faint halo of hydrogen glowing in ultraviolet light
- Reaches past typical lunar distance (about 239,000 miles), so Terra's moons technically pass through it
- Open-air mana: haze keeps thinning toward the **solar-wind floor** near lunar distance (`C_max ≈ 8.5×10^17`). Past that, flat

## Overlapping Region: Ionosphere

**About 30 to 600 miles**

- Not a separate layer but an electrically charged zone spanning the mesosphere, thermosphere and lower exosphere
- Created by solar radiation stripping electrons from atoms
- Reflects radio waves, which enables long-distance shortwave communication
- Mana law does not replace ionization; ambient `C` follows atmosphere then haze law unless a beat adds spiritual thickness

## Beyond the Atmosphere: Magnetosphere

- Terra's magnetic field extends about 40,000 miles toward the Sun and stretches millions of miles in a tail on the night side
- Shields the atmosphere from the solar wind
- Past this lies interplanetary space

## Geosynchronous orbit

**About 22,236 miles above Terra's surface** (about 26,200 miles from Terra's center). At that distance a satellite completes one orbit in 23 hours 56 minutes, matching Terra's rotation.

### Where it falls relative to the layers

- About 3.5 times higher than the outer edge of the exosphere (6,200 miles)
- Inside the geocorona, which extends to about 391,000 miles
- Inside the magnetosphere on the Sun-facing side (about 40,000 miles)
- Within the outer radiation belt, so gear there needs radiation hardening (or magic equivalent)
- About 90 times higher than a ~250 mi orbital station and roughly a tenth of the way to the moons (~239,000 miles)
- Open-air mana: still haze regime, well below the solar-wind floor (`../Science/Energy/ManaConcentration.md`; about `C ~ 4×10^12`)

### Geosynchronous vs geostationary

- **Geosynchronous:** Any orbit with a period matching Terra's rotation. It can be tilted relative to the equator, so the satellite traces a figure-eight in the sky over the course of a day.
- **Geostationary:** A special case that is circular and directly above the equator. The satellite appears fixed at one point in the sky.

### What uses it

- Communications and sky-cast / relay dishes that can point at one spot permanently
- Weather watchers that stare at the same hemisphere continuously
- Military early-warning and relay craft when the story needs them

### Retirement

Dead satellites cannot be deorbited easily from that height. Instead they are pushed about 190 miles higher into a "graveyard orbit" to keep the geostationary belt clear.

Living requirements and one-person mass budget: `Orbit/GeosynchronousHabitat.md`.

## Layer vs open-air mana (quick)

| Layer | Height band | Open-air `C` feel |
|---|---|---|
| Troposphere | 0 to ~7.5 mi | `~1` to `~5` |
| Stratosphere | ~7.5 to 31 mi | `~5` to `~10^3` |
| Mesosphere | 31 to 53 mi | `~10^3` to `~10^5` |
| Thermosphere | 53 to ~370 mi | Kármán `~3×10^6` → exobase `~10^12` (slow) |
| Exosphere / geocorona | above ~370 mi | haze to solar-wind floor `~8.5×10^17` near lunar distance |
| Geosynchronous | ~22,236 mi | haze mid-band `~4×10^12`; fixed-sky relays |

Law formulas: `../Science/Energy/ManaConcentration.md`. Dungeon additive `D/N/k`: `../Geography/Dungeons.md`.

## Open-air mana digit tables

> Full `C`/`A` digits for planning. Law formulas stay in `../Science/Energy/ManaConcentration.md`.

### Altitude table (open-air `C`)

### Bound atmosphere (`C = P₀/P`)

| Altitude | Layer / landmark | P (approx) | C | A = √C |
|---|---|---|---|---|
| 370 mi | Exobase / thermopause | ~8×10^-8 Pa | ~1.2×10^12 | ~1.1×10^6 |
| 310 mi | Upper thermosphere | ~3×10^-7 Pa | ~3.3×10^11 | ~5.8×10^5 |
| 249 mi | Orbital station band | ~1.4×10^-6 Pa | ~7.1×10^10 | ~2.7×10^5 |
| 200 mi | Thermosphere (aurora upper) | ~6×10^-6 Pa | ~1.7×10^10 | ~1.3×10^5 |
| 100 mi | Mid thermosphere | ~3×10^-4 Pa | ~3.4×10^8 | ~1.8×10^4 |
| 62 mi | Kármán (space begins) | ~3.3×10^-2 Pa | ~3.0×10^6 | ~1.7×10^3 |
| 60 mi | Near Kármán | ~5.8×10^-2 Pa | ~1.7×10^6 | ~1.3×10^3 |
| 53 mi | Mesopause | ~0.42 Pa | ~2.4×10^5 | ~490 |
| 50 mi | Upper mesosphere | ~0.97 Pa | ~1.0×10^5 | ~320 |
| 40 mi | Mesosphere | ~12 Pa | ~8.6×10^3 | ~93 |
| 31 mi | Stratopause | ~81 Pa | ~1.3×10^3 | ~35 |
| 30 mi | Upper stratosphere | ~99 Pa | ~1.0×10^3 | ~32 |
| 25 mi | Mid stratosphere (balloon top) | ~280 Pa | ~360 | ~19 |
| 22 mi | Ozone top band | ~540 Pa | ~190 | ~14 |
| 20 mi | Mid stratosphere | ~870 Pa | ~120 | ~11 |
| 11 mi | Equatorial tropopause | ~7.9 kPa | ~13 | ~3.6 |
| 10 mi | Lower stratosphere | ~10 kPa | ~10 | ~3.2 |
| 9 mi | Ozone start band | ~13 kPa | ~7.7 | ~2.8 |
| 7.5 mi | Tropopause (typical) | ~19 kPa | ~5.3 | ~2.3 |
| 5 mi | Polar tropopause band | ~35 kPa | ~2.9 | ~1.7 |
| 3.4 mi | Mid troposphere | ~51 kPa | ~2.0 | ~1.4 |
| 0 mi | Surface | 101.3 kPa | 1 | 1 |

### Exosphere / geocorona haze (`C = C_exo × n_exo/n`)

| Altitude | Landmark | C | A = √C | Notes |
|---|---|---|---|---|
| 370 mi | Exobase | ~1.2×10^12 | ~1.1×10^6 | Haze starts; matched to atmosphere |
| 1,000 mi | Inner exosphere | ~1.2×10^12 | ~1.1×10^6 | Almost flat (huge scale height) |
| 6,200 mi | Outer exosphere fade band | ~1.7×10^12 | ~1.3×10^6 | Still only a mild step |
| 20,000 mi | Deep haze | ~3.6×10^12 | ~1.9×10^6 | |
| 22,236 mi | Geosynchronous belt | ~4.1×10^12 | ~2.0×10^6 | Fixed-sky orbit (`../../Space/Atmosphere.md`) |
| 50,000 mi | Far geocorona | ~2.0×10^13 | ~4.4×10^6 | |
| 100,000 mi | Far geocorona | ~3.3×10^14 | ~1.8×10^7 | |
| ~239,000 mi | Lunar distance | ~8.5×10^17 | ~9.2×10^8 | Near solar-wind floor |
| 391,000 mi+ | Geocorona extent / interplanetary | ~8.5×10^17 | ~9.2×10^8 | **Floor.** No further open-air gain |

**Feel:** mountains / airships mild (`A` ~1.4 to 3). Kármán ~`1,700`. Orbital ~`3×10^5`. Exobase ~`10^6`. Whole near-exosphere haze barely moves. Real gain in the haze is on the way out toward the moons / solar wind, then flat.

## Layer feel (planning)

| Band | Height | Mana story use |
|---|---|---|
| Troposphere | 0 to ~7.5 mi | Weather-layer pressure. Mild `C` |
| Stratosphere | ~7.5 to 31 mi | `C` hundreds to ~10^3 |
| Mesosphere | 31 to 53 mi | `C` into 10^5 |
| Kármán | 62 mi | Space under `P₀/P` |
| Thermosphere | 53 to ~370 mi | Slow `C` climb to exobase |
| Exosphere / geocorona | 370 mi to ~lunar distance | Density haze; very slow at first, then up to solar-wind floor |
| Interplanetary floor | past ~lunar / geocorona | Flat at `C_max` |
| Ionosphere (overlap) | ~30 to 600 mi | Charged air / radio; does not replace this law |
| Dungeon / spiritual | any height | Additive thickness on top of `C(h)` (below) |

Air / haze thins as mana `C` rises. Thin air still hurts breath and lift (`Flight.md`, `../../Space/Atmosphere.md`). Mana richness is not free oxygen.

**Moons:** both sit near lunar-distance solar-wind floor. Deposit catalogs: `Moons.md`.
