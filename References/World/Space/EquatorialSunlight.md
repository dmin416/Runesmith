# Equatorial Sunlight

Clear-sky sunlight at the equator of an Earth-like world with medieval to Renaissance air. Bird clear-sky model, 1-minute steps, every day of an Earth year. Cloud rows are anchored on real places.

This sheet does not replace locked world facts.

- Terra's year is **361** days: 12 × 30 plus New Year's Day (`../World.md`). Annual kWh totals and the declination formula below use a **365**-day Earth year. Noon, hour and day-length rows are for a 24-hour Earth-sized day and still apply. Do not rebuild the calendar from this file.
- Axial tilt is assumed at **23.44°**. Terra's tilt is not separately locked.
- Caldris is temperate lowlands (`../Geography/Places.md`). These rows are the equator, not the kingdom.
- Round overhead clear-sky anchor stays **~1,000 W/m²** (`Radiation/NonIonizing.md`). Medieval-countryside equinox noon here is **1,051 W/m²**, inside that round thousand.
- Solar constant **1,361 W/m²** matches `Radiation/NonIonizing.md`.
- Moons stay the red moon and the blue moon (`Moons.md`). The night-light sketch at the bottom is not their albedo.

Assumptions for the model: sea level, humid tropical air (4.5 cm of water vapor), tropical ozone about 260 Dobson units.

## What medieval air means

| Air | Aerosol optical depth (500 nm) | Real-world analog |
|---|---|---|
| Pristine | 0.03 | Remote open ocean, high mountain air |
| Medieval countryside / remote coast | 0.06 | Pre-industrial air with only natural dust, sea salt and scattered wood fires |
| Pre-industrial global average | ~0.10 | Deserts, wildfires and farm burning included |
| Modern global average | ~0.13 | About 21% more aerosol than pre-industrial |
| Smoky medieval town | ~0.35 | Thousands of wood and charcoal hearths in a still valley |
| Modern polluted megacity | ~0.8 | Industrial haze |

Since pre-industrial times, black carbon has risen about 3.3×, sulfate 2.6× and nitrate 2.7×. Natural dust and sea salt dominated medieval skies. Soot and sulfate dominate modern haze.

At the equator, total sunlight on the ground in medieval air is only about 2% higher than today. The large differences are in the light itself: a stronger direct beam, less milky diffuse glow, a deeper blue sky, sharper shadows and much longer visibility.

## Sunlight above the atmosphere

Equator. Earth-year totals.

| Measure | Value |
|---|---|
| Solar constant | 1,361 W/m² |
| Annual total | 3,638 kWh/m² |
| 24-hour average | 415 W/m² |
| Highest daily totals | March and September equinoxes: ~10.4–10.5 kWh/m²/day |
| Lowest daily totals | June solstice: ~9.2 kWh/m²/day |
| December vs June | December is ~6% sunnier because the planet is closest to the sun in early January |

The equator gets two sunlight peaks a year (the equinoxes) and two dips (the solstices). Seasonal swing is small: about ±6% from the mean.

## Day, night and twilight

| Measure | Value |
|---|---|
| Day length (sunrise to sunset) | ~12 h 7 min every day of the year |
| Noon sun altitude | 90° (straight overhead) at equinoxes; 66.6° at solstices |
| Noon sun direction | South of overhead from late September to late March; north of overhead from late March to late September |
| Civil twilight (enough light to work) | ~21–23 min |
| Nautical twilight (horizon visible at sea) | ~45–49 min after sunset |
| Astronomical twilight (fully dark) | ~69–75 min after sunset |

The sun drops nearly straight down at the equator, so dusk is fast. Full dark arrives a little over an hour after sunset, compared with 1.5–2 hours in Europe in summer.

## Clear-sky sunlight at the ground

### Equinox noon (sun overhead)

| Air | Direct beam (W/m²) | Diffuse (W/m²) | Total on flat ground (W/m²) | Daily total (kWh/m²) | Annual clear-sky total (kWh/m²) |
|---|---|---|---|---|---|
| Pristine (0.03) | 985 | 74 | 1,059 | 7.79 | 2,695 |
| Medieval countryside (0.06) | 958 | 93 | 1,051 | 7.71 | 2,667 |
| Pre-industrial global mean (0.10) | 927 | 114 | 1,041 | 7.62 | 2,635 |
| Modern global mean (0.13) | 906 | 129 | 1,035 | 7.56 | 2,613 |
| Smoky medieval town (0.35) | 778 | 217 | 995 | 7.21 | 2,490 |
| Modern polluted megacity (0.8) | 574 | 357 | 932 | 6.71 | 2,315 |

Clean air puts about 92% of noon light into the direct beam. In a smoky town about 78% is direct. In a megacity barely 60%.

The ~1,000 W/m² overhead anchor in `Radiation/NonIonizing.md` is this band rounded. Medieval countryside noon is 1,051. Modern global-mean noon is 1,035.

### Hour by hour, equinox, medieval countryside (AOD 0.06)

| Local solar time | Sun altitude | Direct beam (W/m²) | Diffuse (W/m²) | Total on flat ground (W/m²) |
|---|---|---|---|---|
| 6:00 / 18:00 | 0° | 0 | 0 | 0 |
| 7:00 / 17:00 | 15° | 644 | 53 | 220 |
| 8:00 / 16:00 | 30° | 818 | 72 | 481 |
| 9:00 / 15:00 | 45° | 894 | 82 | 714 |
| 10:00 / 14:00 | 60° | 933 | 88 | 896 |
| 11:00 / 13:00 | 75° | 952 | 92 | 1,011 |
| 12:00 | ~90° | 958 | 93 | 1,051 |

The direct beam stays above 800 W/m² from 8 am to 4 pm. Two-thirds of the day's energy arrives between 9 am and 3 pm.

### Month by month, clear sky

Mid-month. Daily columns are kWh/m²/day. Clear-sky surface light is about 74% of top-of-atmosphere light in medieval air. Annual sums of these days are Earth-year sums.

| Month | Noon sun altitude | TOA | Pristine | Medieval | Modern | Medieval noon total (W/m²) |
|---|---|---|---|---|---|---|
| Jan | 68.7° S | 10.00 | 7.38 | 7.30 | 7.15 | 997 |
| Feb | 76.7° S | 10.35 | 7.68 | 7.60 | 7.45 | 1,037 |
| Mar | 87.2° S | 10.48 | 7.81 | 7.73 | 7.57 | 1,053 |
| Apr | 80.6° N | 10.18 | 7.57 | 7.49 | 7.34 | 1,021 |
| May | 71.2° N | 9.62 | 7.12 | 7.04 | 6.90 | 961 |
| Jun | 66.7° N | 9.25 | 6.81 | 6.74 | 6.60 | 920 |
| Jul | 68.5° N | 9.36 | 6.91 | 6.84 | 6.70 | 933 |
| Aug | 76.2° N | 9.86 | 7.31 | 7.24 | 7.09 | 987 |
| Sep | 87.8° N | 10.30 | 7.67 | 7.59 | 7.44 | 1,034 |
| Oct | 80.4° S | 10.33 | 7.68 | 7.60 | 7.45 | 1,036 |
| Nov | 70.9° S | 10.05 | 7.43 | 7.35 | 7.20 | 1,003 |
| Dec | 66.7° S | 9.85 | 7.26 | 7.18 | 7.03 | 980 |

### Altitude and humidity

| Condition | Equinox daily total | Noon total |
|---|---|---|
| Sea level, humid, medieval air | 7.71 kWh/m² | 1,051 W/m² |
| Sea level, drier air (2 cm water vapor) | 7.91 kWh/m² | 1,077 W/m² |
| 2,500 m highland, pristine, dry | 8.18 kWh/m² | 1,107 W/m² |

Thinner, drier air above a mountain town adds about 6% more sunlight than a humid coast.

## Clouds

Pollution barely moves the equatorial total. Clouds decide it. Cloud amount is treated as the same in medieval times as now, because clouds are natural.

| Place type | Real-world example | Annual sunlight on ground | Share of clear-sky potential |
|---|---|---|---|
| Clear-sky ceiling (medieval air) | Model | ~2,670 kWh/m² | 100% |
| Equatorial rainforest / maritime city | Singapore | ~1,580 kWh/m² | ~60% |
| Leeward tropical coast | Honolulu: 68% of possible sunshine hours | ~70–80% of clear sky | |
| Windward tropical rain coast | Hilo: 41% of possible sunshine hours | ~50–55% of clear sky | |
| Equatorial desert or rain-shadow highland | Dry plateaus | ~80–90% of clear sky | |

Typical equatorial pattern: clear mornings, towering cumulus by late morning, afternoon thunderstorms, clearing evenings. A 19–20°N Big Island calendar (Hilo, Kona, summit, week by week) is `../Geography/VolcanicIsland/Weather.md`. This sheet stays the equator. Two rainy seasons a year as the tropical rain belt passes overhead twice.

Clean pre-industrial air has fewer particles for droplets to form on. Clouds form with fewer, larger droplets, so they are slightly less white and rain out a little more easily than modern polluted clouds.

## Light under clean medieval skies

| Measure | Clean medieval air | Modern hazy air |
|---|---|---|
| Noon illuminance in full sun | ~110,000–120,000 lux | ~100,000–110,000 lux |
| Noon photosynthetic light (PAR) | ~2,100–2,200 µmol/m²/s | ~2,000–2,100 µmol/m²/s |
| Sky color | Deep cobalt overhead, pale only near the horizon | Paler, whitish blue |
| Shadows | Hard-edged, very dark | Softer, washed with haze glow |
| Visibility | Often 100–250 km; distant mountains crisp | Often 20–60 km |
| Sun's disk | Sharp, almost white, with little halo | Glowing halo of scattered light |
| Sunsets | Clean yellows and oranges; deep reds only after volcanic eruptions or fires | Smeared oranges and reds from haze |
| UV index at noon, clear day | 11–14+ (extreme) at sea level; 15–20+ in high tropical mountains | Slightly lower (haze filters a little UV) |

Sunburn time for fair skin at equatorial noon is about 10–15 minutes. The general surface band in `Radiation/NonIonizing.md` is 15–60 minutes. The short end of that band is this equatorial noon. Unfiltered orbital UV is a different case and stays in that file.

Shade at midday, broad hats, loose layered clothing, a rest through the worst noon, and work at dawn and late afternoon are the practical answers.

## Events that dim a clean sky

| Event | Effect |
|---|---|
| Large volcanic eruption (Samalas 1257, Tambora 1815 class) | Global haze for 1–3 years; several percent less direct sun; red sunsets; cooler summers worldwide |
| Regional wildfire or slash-and-burn season | Aerosol depth jumps to 0.5–1+ for weeks downwind |
| Desert dust outbreaks | Yellow-brown sky; aerosol depth 0.5–2 near the source |
| Local volcano (Hawaii-style) | Sulfur haze downwind of active vents |
| Town hearth smoke on still mornings | Local haze trapped under a temperature inversion; clears by late morning |

## Night light

Earth's full moon gives about 0.1–0.3 lux and reflects about 12% of sunlight. End of civil twilight is about 3.4 lux.

The pastel-moon sketch reflects 50–90% of sunlight. Pink is albedo about 0.6. Blue ice is albedo about 0.85.

| Source | Illuminance at full phase |
|---|---|
| Earth's Moon (for scale) | ~0.25 lux |
| Pink moon (albedo ~0.6) | ~1.2 lux |
| Blue ice moon (albedo ~0.85) | ~1.7 lux |
| Both together | ~3 lux |
| End of civil twilight (for comparison) | ~3.4 lux |

Under both full moons at those albedos, night looks like the moment just after sunset: color faintly visible, paths and faces clear, large print almost readable. Clean medieval air makes this crisper, with sharp moon shadows.

Terra's locked moons are the red moon and the blue moon (`Moons.md`). Their color is surface rock and dust. Albedo is not set there, so this ~3 lux row stays a sketch until a beat locks it.

## Formulas

Earth-year form. `day` is the Earth day number, not a Terra calendar date.

| Quantity | Formula |
|---|---|
| Sun's declination | δ ≈ 23.44° × sin(360° × (day − 81) / 365) |
| Noon sun altitude at equator | 90° − \|δ\| |
| Sun altitude at equator | sin(alt) = cos δ × cos(hour angle) |
| Hour angle | 15° per hour from solar noon |
| Top-of-atmosphere on flat ground | 1,361 × (1 + 0.033 cos(360° × day/365)) × sin(alt) |
| Air mass | ≈ 1 / sin(alt) above 15°; Kasten-Young near the horizon |
| Direct beam through haze | I = I₀ × e^(−τ × air mass) (simplified) |
| Illuminance | ~110 lumens per W of sunlight |
| PAR | ~45% of total sunlight × 4.57 µmol/J |

## Sources

- Change in global aerosol composition since preindustrial times (Tsigaridis et al. 2006): https://acp.copernicus.org/articles/6/5143/2006/acp-6-5143-2006.html
- IPCC AR6 WG1 Figure 6.8 (aerosol optical depth history): https://www.ipcc.ch/report/ar6/wg1/figures/chapter-6/figure-6-8
- pvlib clear-sky models: https://pvlib-python.readthedocs.io/en/v0.14.0/reference/generated/pvlib.clearsky.ineichen.html
- climlab insolation: https://climlab.readthedocs.io/en/main/api/climlab.solar.insolation.html
- Brian Rose, insolation notes: https://www.atmos.albany.edu/facstaff/brose/classes/ATM623_Spring2015/Notes/Lectures/Lecture11%20--%20Insolation.html
- Singapore solar potential (EMA): https://ema.gov.sg/resources/faqs/energy-supply/solar/what-is-the-potential-of-solar-energy-in-singapore
- Climate of Hawaii: https://en.wikipedia.org/wiki/Climate_of_Hawaii
