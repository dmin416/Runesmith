# Island Weather Calendar

Earth station calendar for a Big-Island-style volcanic island at about 19–20°N, mountains above 4,000 m, northeast trades, and an older ridge to the north. Real stations on Hawaiʻi Island and Maui anchor the zones. A value marked *representative* has no station and follows the documented pattern.

Design use: Dragnis-class islands. Biomes: `HawaiianBiomes.md`. Farm placement: `Farming.md`. Coast / channel wind atlas and beach-glider lift: `HawaiianWindsBeachGlider.md`. Equator sunlight (0°, not this latitude): `../../Space/EquatorialSunlight.md`. Hilo's 41% of possible sunshine and Honolulu's 68% match that sheet's cloud rows.

Terra's year is 361 days (`../Places.md`). Months, weeks and solstice dates below are an Earth year. Use the pattern. Do not paste January 1 onto the Terra calendar.

Two day-length cells in the week table were written 12h60 and 11h60. Those are 13h 00 (late July) and 12h 00 (late September).

## The climate engine

| Driver | How it works |
|---|---|
| Northeast trade winds | Blow 85–95% of the time in summer and 50–80% in winter. Steady 5–8 m/s off the open ocean. |
| Trade wind inversion | A warm, dry lid usually at about 1,500–2,200 m. Present 50–70% of the time overall. On trade-wind days, 80–90% of the time. Clouds pile up beneath it and cannot rise higher. |
| Windward slopes | Air is forced uphill and rains out. Rain peaks at about 600–900 m on most islands, and up to about 1,650 m on very tall mountains. |
| Leeward lowlands | Rain shadow. Many leeward coasts get under 20 in (500 mm) a year. |
| Kona slopes (sheltered west side) | Trades are blocked by the mountains. Afternoon sea breezes and upslope winds build clouds and showers. This is the only zone with a summer rainfall peak. |
| Above the inversion | Dry, sunny, cold, low humidity. Clouds usually sit below. |
| Kona storms | Winter low-pressure systems from the southwest. One or two a year (up to four or five; some winters none). Rain lasting hours to days, flooding on leeward sides, snow on summits. |
| Hurricanes and tropical storms | Season June–November. Tropical storms brush some part of the islands every year or two, most likely July–December. Direct hurricane hits are rare (a few per century). |
| Sea surface | Coolest about 75°F (24°C) late February to early April. Warmest about 82°F (28°C) late September to early October. |

Two seasons dominate:

- **Kau (summer), May–September:** reliable trades, windward showers, dry leeward coasts, afternoon clouds over Kona slopes, south-shore surf.
- **Hoʻoilo (winter), October–April:** weaker and more erratic trades, frontal passages, kona storms, the heaviest rain on every side, big north-shore surf, summit snow.

### Temperature drop with height

| Layer | Drop rate | Example |
|---|---|---|
| Below the inversion (humid) | ~5.8 °C per 1,000 m (~3.2 °F per 1,000 ft) | Hilo (sea level) 23.4 °C mean vs Volcano (1,200 m) 16.5 °C mean |
| Whole mountain average | ~4.9 °C per 1,000 m | Hilo 23.4 °C vs Mauna Kea summit (4,206 m) 2.7 °C mean |
| Daily range, coast | ~14–16 °F (8–9 °C) | |
| Daily range, high slopes | ~15–25 °F (8–14 °C) | Dry air above the inversion swings hardest |

## The zones

| Zone | Elevation | Real anchor | Annual rain | Character |
|---|---|---|---|---|
| A. Windward coast | 0–300 m | Hilo | 127 in (3,219 mm) | Rain on ~270 days, mostly night and early morning showers; 41% of possible sunshine |
| B. Windward rain belt / cloud forest | 600–1,700 m | Upslope from Hilo; Big Bog on Maui (1,650 m) | 150–400 in (*representative* 200 in) | Wettest land on the island; mist most afternoons |
| C. Windward uplands (rainforest edge) | ~1,200 m | Volcano / Hawaiʻi Volcanoes NP HQ | 96 in (2,444 mm) | Cool, misty, rain concentrated November–April |
| D. Fog belt / inversion zone | 1,500–2,400 m | Mauna Loa and Hualālai mid-slopes | 20–60 in plus fog drip | Cloud tops sit here; drizzle and fog in afternoons; often sunny by evening |
| E. Alpine zone (above the inversion) | 2,400–3,400 m | Haleakalā summit (3,055 m) | ~34 in (853 mm) | Sunny mornings, frost most nights in winter, very dry air |
| F. Summit (high alpine) | 4,000–4,200 m | Mauna Kea summit (4,206 m) | ~7–8 in (188–204 mm) | Driest place on the island; below freezing every night; snow in winter |
| G. Rain-shadow saddle / transition plateau | 800 m | Waimea | 33 in (831 mm) | Wet east edge and dry west edge within a few km; windy, cool, misty in winter |
| H. North tip (windward ridge, older volcano) | 0–1,600 m | Kohala | 60–150 in on windward valleys | Old eroded ridge; deep valleys catch trade showers |
| I. Leeward dry coast | 0–100 m | Kona airport (Keāhole); Puakō | 9–19 in (230–481 mm) | Hot, sunny, desert-like; Puakō is the driest inhabited spot (~9 in) |
| J. Kona slopes (coffee belt) | 300–900 m | Above Kailua-Kona | *Representative* ~60 in, summer peak | Sunny mornings; clouds build by noon; afternoon showers May–September |
| K. South coast (Kaʻū) | 0–300 m | Pāhala (280 m) | 49 in (1,240 mm) | Hot dry summers; wet November–January; site of the state record high (100 °F) |
| L. Leeward lee of an older island | 0–100 m | Honolulu, Kīhei (Maui), Lahaina | 11–16 in (280–417 mm) | Dry, sunny 68% of possible hours; winter is the only rainy season |

Zones B, D and H have annual rain and character only. They do not have a monthly station table.

## Monthly normals by zone

### A. Windward coast: Hilo (sea level)

| Month | High °F | Low °F | Rain (in) | Rain days | Cloud cover |
|---|---|---|---|---|---|
| Jan | 79 | 64 | 7.9 | 16 | 52% |
| Feb | 78 | 64 | 10.2 | 16 | 54% |
| Mar | 79 | 65 | 12.7 | 22 | 61% |
| Apr | 79 | 66 | 9.4 | 25 | 61% |
| May | 81 | 67 | 7.0 | 23 | 57% |
| Jun | 82 | 69 | 7.3 | 25 | 53% |
| Jul | 83 | 70 | 9.2 | 27 | 53% |
| Aug | 83 | 70 | 11.3 | 27 | 52% |
| Sep | 83 | 70 | 8.7 | 23 | 55% |
| Oct | 82 | 69 | 10.2 | 23 | 58% |
| Nov | 80 | 68 | 14.4 | 23 | 58% |
| Dec | 79 | 66 | 12.1 | 22 | 53% |

### C. Windward uplands: Volcano (~1,200 m)

| Month | High °F | Low °F | Rain (in) |
|---|---|---|---|
| Jan | 68.3 | 49.4 | 8.77 |
| Feb | 68.2 | 49.3 | 8.15 |
| Mar | 67.5 | 50.7 | 10.27 |
| Apr | 68.3 | 51.9 | 9.16 |
| May | 70.5 | 53.0 | 6.46 |
| Jun | 71.3 | 54.3 | 5.10 |
| Jul | 72.7 | 55.6 | 6.29 |
| Aug | 73.7 | 56.0 | 5.91 |
| Sep | 73.2 | 55.4 | 5.98 |
| Oct | 72.4 | 55.1 | 8.19 |
| Nov | 70.3 | 54.0 | 10.59 |
| Dec | 68.2 | 51.7 | 11.37 |

### E. Alpine zone: Haleakalā summit (~3,000 m)

| Month | High °F | Low °F | Rain (in) |
|---|---|---|---|
| Jan | 45.2 | 33.6 | 8.00 |
| Feb | 49.9 | 36.1 | 3.57 |
| Mar | 50.9 | 36.5 | 3.05 |
| Apr | 52.2 | 37.4 | 4.00 |
| May | 54.7 | 39.1 | 1.35 |
| Jun | 58.3 | 42.1 | 0.37 |
| Jul | 57.7 | 41.8 | 0.47 |
| Aug | 58.5 | 42.3 | 1.11 |
| Sep | 57.6 | 42.1 | 1.59 |
| Oct | 56.8 | 41.3 | 1.32 |
| Nov | 50.5 | 37.6 | 4.09 |
| Dec | 42.8 | 31.8 | 4.67 |

Record low 15 °F. Snow averages only a fraction of an inch a year at this height (mostly February). In 2019 snow reached as low as 1,900 m.

### F. Summit: Mauna Kea (4,206 m)

| Month | High °F | Low °F | Rain (in) | Record low °F |
|---|---|---|---|---|
| Jan | 42.0 | 26.3 | 0.81 | 19 |
| Feb | 42.5 | 26.1 | 0.24 | 12 |
| Mar | 40.3 | 24.9 | 1.05 | 18 |
| Apr | 41.4 | 26.2 | 0.50 | 18 |
| May | 47.5 | 29.0 | 0.92 | 12 |
| Jun | 49.3 | 29.4 | 0.14 | 23 |
| Jul | 50.9 | 30.3 | 0.29 | 22 |
| Aug | 49.9 | 30.9 | 0.77 | 17 |
| Sep | 50.5 | 31.3 | 0.51 | 23 |
| Oct | 43.8 | 29.5 | 0.58 | 20 |
| Nov | 45.1 | 27.8 | 1.04 | 20 |
| Dec | 42.7 | 27.6 | 0.52 | 17 |

Frost is possible every night of the year. Snow can fall above about 3,350 m in any month, most often October–April. Precipitation here is mostly snow and hail in winter.

### G. Saddle / transition plateau: Waimea (816 m)

| Month | High °F | Low °F | Rain (in) |
|---|---|---|---|
| Jan | 72.6 | 50.4 | 4.74 |
| Feb | 72.2 | 50.6 | 3.76 |
| Mar | 72.5 | 51.7 | 3.84 |
| Apr | 73.3 | 52.8 | 3.08 |
| May | 74.0 | 54.3 | 1.74 |
| Jun | 74.5 | 55.4 | 1.34 |
| Jul | 74.6 | 56.4 | 1.97 |
| Aug | 75.7 | 57.1 | 2.27 |
| Sep | 76.8 | 56.9 | 0.89 |
| Oct | 76.8 | 55.2 | 1.89 |
| Nov | 74.7 | 54.2 | 2.94 |
| Dec | 72.1 | 52.3 | 4.22 |

Weather changes within a kilometer or two. The east side of town catches trade mist. The west side is ranch-dry.

### I. Leeward dry coast: Kona airport (sea level)

| Month | High °F | Low °F | Rain (in) |
|---|---|---|---|
| Jan | 81.6 | 68.2 | 2.40 |
| Feb | 81.2 | 68.0 | 1.50 |
| Mar | 82.2 | 70.0 | 1.77 |
| Apr | 83.0 | 70.6 | 1.38 |
| May | 83.5 | 71.6 | 2.01 |
| Jun | 85.0 | 73.6 | 0.98 |
| Jul | 86.0 | 74.1 | 0.71 |
| Aug | 86.9 | 75.1 | 1.38 |
| Sep | 86.8 | 74.6 | 0.83 |
| Oct | 86.0 | 74.1 | 1.34 |
| Nov | 84.2 | 71.8 | 1.30 |
| Dec | 82.5 | 69.4 | 2.83 |

### J. Kona slopes / coffee belt (300–900 m), *representative*

Temperatures are interpolated between Kona airport and Waimea using the island lapse rate.

| Month | High °F | Low °F | Rain (in) | Pattern |
|---|---|---|---|---|
| Jan | 77 | 60 | 3.5 | Mostly sunny; occasional winter fronts |
| Feb | 77 | 60 | 3.0 | Driest stretch; clear evenings |
| Mar | 77 | 61 | 4.0 | Kona storm rains possible |
| Apr | 78 | 62 | 4.5 | Afternoon clouds begin |
| May | 79 | 63 | 5.5 | Afternoon showers start most days |
| Jun | 80 | 64 | 6.5 | Clouds by 11 am; rain 2–5 pm |
| Jul | 81 | 65 | 7.0 | Wettest stretch; misty afternoons |
| Aug | 81 | 66 | 7.0 | Wettest stretch; warm humid nights |
| Sep | 81 | 65 | 6.0 | Showers tapering |
| Oct | 80 | 64 | 5.0 | Mixed |
| Nov | 79 | 63 | 4.0 | Clearer afternoons |
| Dec | 77 | 61 | 3.5 | Mostly sunny |

### K. South coast: Pāhala (280 m)

| Month | High °F | Low °F | Rain (in) |
|---|---|---|---|
| Jan | 78 | 63 | 5.37 |
| Feb | 78 | 62 | 4.22 |
| Mar | 78 | 63 | 4.11 |
| Apr | 78 | 64 | 3.19 |
| May | 79 | 65 | 2.38 |
| Jun | 80 | 67 | 1.87 |
| Jul | 81 | 67 | 3.57 |
| Aug | 82 | 68 | 3.28 |
| Sep | 82 | 68 | 4.04 |
| Oct | 81 | 67 | 4.67 |
| Nov | 80 | 66 | 6.53 |
| Dec | 78 | 67 | 5.64 |

### L. Leeward lee of an older island: Honolulu (sea level)

| Measure | Value |
|---|---|
| Annual mean high / low | 84.6 °F / 71.5 °F |
| Annual rain | 16.4 in (417 mm) on ~89 days |
| Wettest month | March, 2.36 in |
| Driest month | June, 0.50 in |
| Sunshine | 3,036 hours (68% of possible) |
| Record range | 52–95 °F |

## Month-by-month, all sides

### January

- **Sky and wind:** Trades only about 55% of days. Cold fronts sweep in from the northwest every 1–2 weeks, bringing a day of rain and blustery north winds, then cool clear air. Kona storm season is fully open.
- **Windward coast:** Showery nights, many bright mornings between fronts. 79/64 °F.
- **Rain belt and uplands:** Cool and wet. Volcano lows near 49 °F. Fireplace weather.
- **Fog belt:** Thick cloud during fronts. Clear crisp days after them.
- **Alpine and summit:** Coldest stretch. Summit highs about 42 °F, lows about 26 °F. Snow after fronts or kona lows can last days to weeks. Haleakalā-height peaks frosted many nights.
- **Leeward coast and Kona:** Sunniest place to be. This is also leeward wet season. A kona storm can dump several inches in a day.
- **South coast:** Wet season. Green pastures.
- **Ocean:** Sea about 77 °F. Biggest north-shore surf of the year. Humpback whales present.
- **Daylight:** about 11 h. Sunrise late.

### February

- **Sky and wind:** Trades about 60%. Frontal rains continue. The clearest air of the year falls between storms.
- **Windward:** Rainy but variable. 78/64 °F.
- **Uplands:** Volcano lows about 49 °F, the coldest month at mid-elevation.
- **Summit:** Coldest nights (record 12 °F). Snow most likely this month and March.
- **Leeward:** Kona coast driest winter month. Brilliant visibility.
- **Ocean:** Sea approaching its annual low. Whale peak. Large north swells.

### March

- **Sky and wind:** Trades about 65% and strengthening late in the month. The single wettest month on many windward stations, as trade showers and late fronts overlap.
- **Windward coast:** about 12.7 in at Hilo on about 22 days. Floods in gulches.
- **Uplands:** Volcano 10 in. Rain belt saturated. Waterfalls at maximum.
- **Summit:** Coldest daytime highs (about 40 °F). Late-season snowstorms common.
- **Leeward:** Honolulu-type leeward coasts' wettest month.
- **Ocean:** Sea at its coolest (about 75 °F) from late February to early April. Whales still present. North swells fading.
- **Equinox (about March 20):** 12 h day.

### April

- **Sky and wind:** Transition. Trades about 75% and steadier. Fronts become rare.
- **Windward:** Rain days peak (about 25 days at Hilo) though totals drop. Drizzly showers.
- **Fog belt:** Inversion lowers and strengthens. Classic cloud sea seen from above.
- **Summit:** Snow possible but melting quickly.
- **Leeward:** Afternoon clouds start appearing over Kona slopes.
- **South coast:** Drying out. Record 100 °F heat at Pāhala happened in late April.
- **Ocean:** Sea still cool. Whales depart. First south swells.

### May

- **Sky and wind:** Summer pattern locks in. Trades about 85%.
- **Windward coast:** Drier. 7 in at Hilo. Showers mostly at night and dawn.
- **Uplands:** Pleasant. Volcano 70/53 °F.
- **Fog belt:** Daily afternoon cloud band at 1,500–2,200 m. Clear above.
- **Alpine and summit:** Warming quickly. Summit highs about 48 °F. Snow rare.
- **Kona slopes:** Afternoon shower season begins.
- **Leeward coasts:** Hot, dry, brown grass.
- **Ocean:** South-shore surf season. Sea about 77 °F.
- **Sun overhead (about May 18–20 at 19.7°N):** Noon shadows vanish (Lahaina Noon).

### June

- **Sky and wind:** Trades about 90%. Most reliable weather of the year. Hurricane season opens June 1.
- **Windward:** Moderate showers. 82/69 °F.
- **Uplands:** Mild and drier. Volcano driest month (about 5 in).
- **Summit:** Driest month (0.14 in). Crystal-clear nights.
- **Alpine:** Haleakalā-height peaks almost rainless (0.4 in).
- **Kona slopes:** Clouds by late morning. Reliable afternoon rain.
- **Leeward coasts:** Driest month on most (Honolulu 0.5 in). Fire weather in dry grasslands.
- **Solstice (about June 21):** Longest day about 13 h 20 min.

### July

- **Sky and wind:** Trades about 93%, the steadiest month. Strongest channel winds between islands.
- **Windward coast:** Showers increase again. Rain on about 27 days, in short bursts.
- **Kona slopes:** Wettest stretch begins. Misty afternoons, humid nights.
- **Summit:** Warmest month. Snow almost never.
- **Leeward coasts:** Hot (86/74 °F at Kona). Kona coast driest month (0.7 in).
- **Ocean:** Sea warming past 80 °F. South swells. Tropical storm season becomes active.
- **Sun overhead again (about July 24–25).**

### August

- **Sky and wind:** Trades about 92%. Hurricane season peak begins.
- **Windward coast:** One of the wetter months (11 in at Hilo) from tropical moisture riding the trades.
- **Uplands:** Warmest nights (Volcano 56 °F).
- **Kona slopes:** Peak afternoon rain.
- **Summit:** Mildest nights (about 31 °F). Still freezing most nights.
- **Leeward:** Hottest stretch. Leeward record heat days reach the low 90s °F.
- **Hazard:** Tropical storm or hurricane remnants can bring 10–20+ in of rain to windward and southeast slopes in a day.

### September

- **Sky and wind:** Trades about 85%, weakening at month's end. Hurricane peak continues.
- **All coasts:** Hottest and most humid. Muggy when trades fail.
- **Waimea and transition zones:** Driest month (0.9 in).
- **Kona slopes:** Showers tapering.
- **Summit:** Warmest nights of the year. First early-season snow possible late month.
- **Ocean:** Sea at its warmest (about 82 °F) late September to early October.
- **Equinox (about September 22).**

### October

- **Sky and wind:** Wet season begins. Trades about 75% with more frequent lulls. First fronts and kona lows possible.
- **Windward:** Rain increasing (10 in at Hilo).
- **Uplands:** Wetter. Mist returns at Volcano.
- **Summit:** Snow season opens. Highs drop sharply (about 44 °F).
- **Leeward:** First winter showers. Humid, hazy calm days when trades stop, and volcanic smog spreads west if a vent is erupting.
- **Ocean:** Sea still about 81–82 °F. First large north swells. Tropical systems still possible.

### November

- **Sky and wind:** Trades about 65%. Fronts every week or two. One of the wettest months everywhere.
- **Windward coast:** Wettest month at Hilo (14.4 in, up to 15.5 in in older normals).
- **Uplands:** Volcano 10.6 in.
- **South coast:** Wettest month at Pāhala (6.5 in).
- **Summit:** Snowstorms common. Ice on roads.
- **Leeward:** Kona storms can flood leeward coasts.
- **Ocean:** Big north swells. Hurricane season ends November 30.

### December

- **Sky and wind:** Trades about 58%. Kona storm peak. Fronts and upper-level lows.
- **Windward:** Very wet (12 in at Hilo). Flash floods.
- **Uplands:** Volcano's wettest month (11.4 in). Chilly (51 °F lows).
- **Alpine:** Haleakalā-height peaks coldest month (32 °F mean low). Frost and occasional snow.
- **Summit:** Snow likely after any storm.
- **Leeward:** Kona coast wettest month (2.8 in).
- **Ocean:** Whales return. Giant north swells. Sea about 79 °F.
- **Solstice (about December 21):** Shortest day about 10 h 58 min.

## Daily rhythm on a typical trade-wind day

| Time | Windward coast | Rain belt | Fog belt | Summit | Leeward coast | Kona slopes |
|---|---|---|---|---|---|---|
| Pre-dawn | Passing showers | Drizzle | Clear, cold | Freezing, stars, dead calm | Clear, warm | Clear |
| 6–9 am | Rainbows, clearing | Mist lifting | Bright sun on frost (upper part) | Sunny, below freezing early | Sunny, calm | Sunny |
| 9 am–noon | Cumulus building | Clouds thickening | Cloud sea forming below | Sunny, dry, intense UV | Sunny, sea breeze starts | Clouds forming on upper slopes |
| Noon–3 pm | Partly cloudy | Rain likely | Cloud tops rising into it; fog | Sunny, cold wind | Hottest, breezy | Clouds overhead; showers |
| 3–6 pm | Showers on hills | Steady rain | Fog and drizzle | Clear | Clouds over the mountain behind | Heaviest rain |
| Evening | Clearing at the shore | Rain easing | Clearing above clouds | Freezing again | Calm, clear | Clearing |
| Night | Showers return | Showers | Clear | Coldest | Mild | Mild, damp |

## Week by week

Columns: sea surface °F, chance a day has trade winds, Hilo weekly rain, *representative* coffee-belt weekly rain, leeward dry-coast weekly rain, Volcano (1,200 m) nightly low, summit (4,200 m) nightly low, day length at 19.7°N.

| Wk | Dates | Sea °F | Trade odds | Hilo rain (in/wk) | Kona slopes (in/wk) | Kona coast (in/wk) | Volcano low °F | Summit low °F | Day length | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Jan 01–Jan 07 | 78 | 56% | 2.1 | 0.8 | 0.58 | 50 | 27 | 10h 59 | whales; N swell season; biggest N surf; kona-storm risk; summit snow possible |
| 2 | Jan 08–Jan 14 | 77 | 55% | 1.9 | 0.8 | 0.55 | 50 | 26 | 11h 02 | whales; N swell season; biggest N surf; kona-storm risk; summit snow possible |
| 3 | Jan 15–Jan 21 | 77 | 55% | 1.8 | 0.8 | 0.52 | 49 | 26 | 11h 05 | whales; N swell season; biggest N surf; kona-storm risk; summit snow possible |
| 4 | Jan 22–Jan 28 | 76 | 57% | 2.0 | 0.8 | 0.48 | 49 | 26 | 11h 10 | whales; N swell season; biggest N surf; kona-storm risk; summit snow possible |
| 5 | Jan 29–Feb 04 | 76 | 58% | 2.3 | 0.8 | 0.48 | 49 | 26 | 11h 16 | whales; N swell season; biggest N surf; kona-storm risk; summit snow possible |
| 6 | Feb 05–Feb 11 | 76 | 59% | 2.4 | 0.8 | 0.43 | 49 | 26 | 11h 22 | whales; N swell season; biggest N surf; kona-storm risk; summit snow possible |
| 7 | Feb 12–Feb 18 | 76 | 60% | 2.5 | 0.8 | 0.38 | 49 | 26 | 11h 29 | whales; N swell season; biggest N surf; kona-storm risk; summit snow possible |
| 8 | Feb 19–Feb 25 | 75 | 61% | 2.7 | 0.8 | 0.39 | 50 | 26 | 11h 36 | whales; N swell season; biggest N surf; kona-storm risk; summit snow possible; coldest sea |
| 9 | Feb 26–Mar 04 | 75 | 62% | 2.6 | 0.8 | 0.37 | 50 | 26 | 11h 43 | whales; N swell season; biggest N surf; kona-storm risk; summit snow possible; coldest sea |
| 10 | Mar 05–Mar 11 | 75 | 64% | 2.7 | 0.8 | 0.38 | 50 | 25 | 11h 51 | whales; N swell season; kona-storm risk; summit snow possible; coldest sea |
| 11 | Mar 12–Mar 18 | 75 | 65% | 2.9 | 0.9 | 0.40 | 51 | 25 | 11h 59 | whales; N swell season; kona-storm risk; summit snow possible; coldest sea |
| 12 | Mar 19–Mar 25 | 75 | 67% | 2.7 | 0.9 | 0.38 | 51 | 25 | 12h 07 | whales; N swell season; kona-storm risk; summit snow possible; equinox; coldest sea |
| 13 | Mar 26–Apr 01 | 75 | 70% | 2.5 | 1.0 | 0.36 | 51 | 25 | 12h 15 | whales; N swell season; kona-storm risk; summit snow possible; coldest sea |
| 14 | Apr 02–Apr 08 | 75 | 72% | 2.4 | 1.0 | 0.35 | 52 | 26 | 12h 23 | whales; N swell season; kona-storm risk; summit snow possible; coldest sea |
| 15 | Apr 09–Apr 15 | 75 | 74% | 2.3 | 1.0 | 0.33 | 52 | 26 | 12h 31 | whales; N swell season; kona-storm risk; summit snow possible; coldest sea |
| 16 | Apr 16–Apr 22 | 75 | 76% | 2.1 | 1.1 | 0.34 | 52 | 27 | 12h 39 | whales; N swell season; kona-storm risk; summit snow possible |
| 17 | Apr 23–Apr 29 | 76 | 79% | 2.0 | 1.1 | 0.38 | 52 | 27 | 12h 46 | whales; N swell season; kona-storm risk; summit snow possible |
| 18 | Apr 30–May 06 | 76 | 81% | 1.8 | 1.2 | 0.40 | 53 | 28 | 12h 53 | whales; N swell season; S swells; kona-storm risk; summit snow possible |
| 19 | May 07–May 13 | 76 | 83% | 1.7 | 1.2 | 0.43 | 53 | 29 | 12h 59 | S swells |
| 20 | May 14–May 20 | 77 | 85% | 1.6 | 1.3 | 0.44 | 53 | 29 | 13h 05 | S swells; Kona-slope afternoon showers; sun directly overhead at noon |
| 21 | May 21–May 27 | 77 | 86% | 1.6 | 1.3 | 0.39 | 53 | 29 | 13h 10 | S swells; Kona-slope afternoon showers |
| 22 | May 28–Jun 03 | 77 | 88% | 1.6 | 1.4 | 0.33 | 54 | 29 | 13h 14 | S swells; hurricane season; Kona-slope afternoon showers |
| 23 | Jun 04–Jun 10 | 78 | 89% | 1.7 | 1.5 | 0.29 | 54 | 29 | 13h 17 | S swells; hurricane season; Kona-slope afternoon showers |
| 24 | Jun 11–Jun 17 | 78 | 90% | 1.7 | 1.5 | 0.24 | 54 | 29 | 13h 19 | S swells; hurricane season; Kona-slope afternoon showers |
| 25 | Jun 18–Jun 24 | 78 | 91% | 1.8 | 1.5 | 0.22 | 55 | 30 | 13h 19 | S swells; hurricane season; Kona-slope afternoon showers; solstice |
| 26 | Jun 25–Jul 01 | 79 | 91% | 1.9 | 1.6 | 0.20 | 55 | 30 | 13h 19 | S swells; hurricane season; Kona-slope afternoon showers |
| 27 | Jul 02–Jul 08 | 79 | 92% | 1.9 | 1.5 | 0.18 | 55 | 30 | 13h 17 | S swells; hurricane season; Kona-slope afternoon showers |
| 28 | Jul 09–Jul 15 | 80 | 93% | 2.0 | 1.6 | 0.17 | 55 | 30 | 13h 14 | S swells; hurricane season; Kona-slope afternoon showers |
| 29 | Jul 16–Jul 22 | 80 | 93% | 2.1 | 1.6 | 0.18 | 56 | 30 | 13h 10 | S swells; hurricane season; Kona-slope afternoon showers |
| 30 | Jul 23–Jul 29 | 80 | 93% | 2.2 | 1.6 | 0.21 | 56 | 31 | 13h 05 | S swells; hurricane season; Kona-slope afternoon showers; sun directly overhead at noon |
| 31 | Jul 30–Aug 05 | 81 | 92% | 2.4 | 1.6 | 0.25 | 56 | 31 | 13h 00 | S swells; hurricane season; hurricane peak; Kona-slope afternoon showers |
| 32 | Aug 06–Aug 12 | 81 | 92% | 2.5 | 1.6 | 0.28 | 56 | 31 | 12h 53 | S swells; hurricane season; hurricane peak; Kona-slope afternoon showers |
| 33 | Aug 13–Aug 19 | 81 | 92% | 2.5 | 1.6 | 0.31 | 56 | 31 | 12h 47 | S swells; hurricane season; hurricane peak; Kona-slope afternoon showers |
| 34 | Aug 20–Aug 26 | 81 | 90% | 2.4 | 1.5 | 0.28 | 56 | 31 | 12h 39 | S swells; hurricane season; hurricane peak; Kona-slope afternoon showers |
| 35 | Aug 27–Sep 02 | 82 | 89% | 2.3 | 1.5 | 0.25 | 56 | 31 | 12h 32 | S swells; hurricane season; hurricane peak; Kona-slope afternoon showers |
| 36 | Sep 03–Sep 09 | 82 | 87% | 2.2 | 1.5 | 0.23 | 56 | 31 | 12h 24 | S swells; hurricane season; hurricane peak; Kona-slope afternoon showers |
| 37 | Sep 10–Sep 16 | 82 | 85% | 2.1 | 1.4 | 0.20 | 55 | 31 | 12h 16 | S swells; hurricane season; hurricane peak; Kona-slope afternoon showers; warmest sea |
| 38 | Sep 17–Sep 23 | 82 | 83% | 2.1 | 1.4 | 0.21 | 55 | 31 | 12h 08 | S swells; hurricane season; hurricane peak; Kona-slope afternoon showers; equinox; warmest sea |
| 39 | Sep 24–Sep 30 | 82 | 81% | 2.2 | 1.3 | 0.24 | 55 | 31 | 12h 00 | S swells; hurricane season; hurricane peak; Kona-slope afternoon showers; warmest sea |
| 40 | Oct 01–Oct 07 | 82 | 79% | 2.2 | 1.2 | 0.26 | 55 | 30 | 11h 52 | N swell season; hurricane season; kona-storm risk; summit snow possible; warmest sea |
| 41 | Oct 08–Oct 14 | 82 | 76% | 2.3 | 1.2 | 0.29 | 55 | 30 | 11h 44 | N swell season; hurricane season; kona-storm risk; summit snow possible; warmest sea |
| 42 | Oct 15–Oct 21 | 82 | 74% | 2.4 | 1.1 | 0.30 | 55 | 29 | 11h 36 | N swell season; hurricane season; kona-storm risk; summit snow possible; warmest sea |
| 43 | Oct 22–Oct 28 | 82 | 72% | 2.6 | 1.1 | 0.30 | 55 | 29 | 11h 29 | N swell season; hurricane season; kona-storm risk; summit snow possible |
| 44 | Oct 29–Nov 04 | 81 | 70% | 2.9 | 1.0 | 0.31 | 54 | 29 | 11h 22 | N swell season; hurricane season; kona-storm risk; summit snow possible |
| 45 | Nov 05–Nov 11 | 81 | 67% | 3.1 | 1.0 | 0.31 | 54 | 28 | 11h 16 | N swell season; hurricane season; kona-storm risk; summit snow possible |
| 46 | Nov 12–Nov 18 | 81 | 65% | 3.4 | 0.9 | 0.30 | 54 | 28 | 11h 10 | N swell season; hurricane season; kona-storm risk; summit snow possible |
| 47 | Nov 19–Nov 25 | 80 | 63% | 3.2 | 0.9 | 0.39 | 53 | 28 | 11h 06 | N swell season; hurricane season; kona-storm risk; summit snow possible |
| 48 | Nov 26–Dec 02 | 80 | 62% | 3.1 | 0.9 | 0.47 | 53 | 28 | 11h 02 | whales; N swell season; biggest N surf; hurricane season; kona-storm risk; summit snow possible |
| 49 | Dec 03–Dec 09 | 80 | 60% | 2.9 | 0.8 | 0.54 | 52 | 28 | 10h 59 | whales; N swell season; biggest N surf; kona-storm risk; summit snow possible |
| 50 | Dec 10–Dec 16 | 79 | 58% | 2.8 | 0.8 | 0.62 | 52 | 28 | 10h 57 | whales; N swell season; biggest N surf; kona-storm risk; summit snow possible |
| 51 | Dec 17–Dec 23 | 79 | 58% | 2.6 | 0.8 | 0.62 | 51 | 27 | 10h 56 | whales; N swell season; biggest N surf; kona-storm risk; summit snow possible; solstice |
| 52 | Dec 24–Dec 31 | 78 | 57% | 2.4 | 0.8 | 0.60 | 51 | 27 | 10h 57 | whales; N swell season; biggest N surf; kona-storm risk; summit snow possible |

## Hazard calendar

| Hazard | Season | Where it hits hardest |
|---|---|---|
| Flash floods | October–April; any time with stalled showers | Windward gulches; leeward slopes during kona storms |
| Kona storms | October–April, 1–2 per year | Leeward and south sides; summits get snow |
| Cold fronts | November–March, every 1–2 weeks | North and northwest sides |
| Summit snow and ice | October–April (possible any month above 3,350 m) | Above about 3,000 m; record low snow line about 1,900 m |
| Hurricanes / tropical storms | June–November (storms most likely July–December; peak August–September) | Southeast and south sides first; windward rain totals extreme |
| Downslope wind storms | Winter, during strong trades or kona lows | Leeward foothills; gusts 60–100 mph in rare events |
| Wildfire | May–October | Leeward grasslands, saddle plateau |
| Big surf | North shores October–April; south shores May–September | Exposed coasts |
| Tornadoes / waterspouts | Rare, about 1 per year statewide | Any coast during winter storms |
| Volcanic smog (if a vent is active) | Worst when trades stop (winter calm and kona winds) | Leeward and south sides |

## Year-to-year swings

| Pattern | Effect |
|---|---|
| El Niño winter | Drought on most sides; fewer kona storms; higher hurricane odds the following season |
| La Niña winter | Wetter winter; more trades and fronts |
| Long-term (decadal) cycles | Multi-decade wetter or drier periods; recent decades trended drier with fewer northeast trade days |

## Sources

- Hawaiʻi Rainfall Atlas: https://rainfall.geography.hawaii.edu/rainfall
- Climate of Hawaii: https://en.wikipedia.org/wiki/Climate_of_Hawaii
- Present climate of Hawaiʻi (Teacher-Friendly Guide): https://geology.teacherfriendlyguide.org/index.php/climate-w/climate-presenthawaii-w
- Trade wind climatology (Garza et al. 2012): https://www.soest.hawaii.edu/MET/Hsco/publications/2012.4.pdf
- Summer leeside rainfall over Hawaiʻi: https://scholarspace.manoa.hawaii.edu/items/749b4610-1525-4203-a561-5ab2015e46a4/full
- Mountain fog on Mauna Loa: https://www.wrrc.hawaii.edu/publication/a-climatology-of-mountain-fog-on-mauna-loa-hawaii-island/
- Hilo climate normals: https://www.climate-zone.com/climate/us/hilo/
- Kailua-Kona climate: https://en.wikipedia.org/wiki/Kailua,_Hawaii_County,_Hawaii
- Volcano climate: https://en.wikipedia.org/wiki/Volcano,_Hawaii
- Waimea climate: https://en.wikipedia.org/wiki/Waimea,_Hawaii_County,_Hawaii
- Pāhala climate: https://en.wikipedia.org/wiki/P%C4%81hala,_Hawaii
- Mauna Kea summit climate: https://en.wikipedia.org/wiki/Mauna_Kea
- Haleakalā summit climate: https://en.wikipedia.org/wiki/Haleakal%C4%81
