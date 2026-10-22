# Hawaiian Island Winds and the Lift Physics of a 100 kg Beach Glider Pilot

> Earth invent loot. Compiled October 2026. Wind figures are typical climatological values from long-term airport, buoy and site records plus local sailing and soaring knowledge. Individual days vary widely. Physics tables computed from first principles. Not locked law.
>
> Weather calendar: `Weather.md`. Biomes / trades: `HawaiianBiomes.md`. Beach sand types: `Sands.md`. Perfect glider designs: `../../Science/Vehicle/PerfectGlider/Index.md`, `Hawaii.md`. Peak / summit traversal methods: `PeakTraversal.md`. Flight power: `../../Science/Energy/Flight.md`. Balloons / tethers / buoyancy ascent: `../../Science/Energy/LighterThanAir.md`. Roland glider wishlist: `../../../People/Roland/Goals.md`.

---

## Contents

1. Constants and baseline assumptions
2. Why Hawaii is windy: the trade wind machine
3. Seasonal and daily wind patterns
4. Non-trade regimes: kona winds, sea breezes, storms
5. Channel winds between the islands
6. Coast by coast, island by island wind atlas
7. Terrain and mountain airflow physics
8. The beach boundary layer and blowing sand
9. Lift fundamentals
10. Air density across Hawaiian conditions
11. Dynamic pressure and wind power
12. Airspeed needed to carry 100 kg
13. Effect of glider weight
14. Lift as a percentage of body weight in a beach wind
15. Raw lift force in kilograms
16. Wind speed needed to leave the ground
17. Location scenarios
18. Jump height and air time while partly supported
19. Glide performance by glider class
20. Aspect ratio, induced drag and best glide
21. Reynolds numbers
22. Ridge and cliff lift
23. Ground effect
24. Turns, load factor and gusts
25. Drag on the body and wing
26. Stability and control of very light wings
27. Comparisons with Hawaiian seabirds
28. Waves, swell and sea state from the same wind
29. History: dune gliders and beach flight
30. Hawaiian soaring and wind-sport sites
31. Formula sheet
32. Unit conversions

---

## 1. Constants and baseline assumptions

| Quantity | Value |
|---|---|
| Standard gravity g | 9.80665 m/s2 |
| Pilot mass | 100 kg (220.5 lb) |
| Pilot weight | 980.7 N (220.5 lbf) |
| Default glider mass | 5 kg (very light fabric wing) |
| Default all-up mass | 105 kg (1,029.7 N) |
| Baseline beach air density | 1.172 kg/m3 (26 C, 1015 hPa, 70% RH, sea level) |
| ISA sea-level density | 1.225 kg/m3 (15 C, dry) |
| Kinematic viscosity of warm air | about 1.6 x 10^-5 m2/s |
| Speed of sound at 26 C | about 347 m/s |
| Default lift coefficient CL | 1.0 (cambered fabric wing near max useful lift) |

Hawaiian beach air is about 4% thinner than the ISA textbook value because it is warm and humid. Water vapor (molar mass 18) is lighter than dry air (about 29), so humid air is less dense.

---

## 2. Why Hawaii is windy: the trade wind machine

- **North Pacific High.** A semi-permanent high-pressure cell sits northeast of the islands, typically near 30 to 40 N latitude. Air flows clockwise around it and outward toward the low pressure near the equator. Over Hawaii this flow arrives from the northeast to east: the northeast trade winds.
- **Hadley circulation.** Air rises at the equator (Intertropical Convergence Zone), flows poleward aloft, sinks near 30 N and returns toward the equator at the surface. Coriolis deflection turns that surface return flow to the right in the Northern Hemisphere, producing a wind from the northeast.
- **Trade wind inversion.** Sinking air warms by compression and caps the lower atmosphere with a temperature inversion, usually between about 1,500 and 2,500 m. Below it the air is moist and cloudy. Above it the air is dry and clear. This lid matters enormously for the islands: mountains taller than the inversion (Haleakala, Mauna Kea, Mauna Loa) poke through it and force the trades around them. Lower ranges (Koolau, Waianae, West Maui) let air over the top.
- **Typical trade wind speed:** 10 to 20 mph (4.5 to 9 m/s, 9 to 17 knots) over open water. Strong trade episodes reach 25 to 35 mph sustained with higher gusts, especially when a strong high passes north of the state.
- **Direction:** most often from 060 to 080 degrees (ENE). Shifts to E or ESE when the high sits farther east or south.
- **Persistence:** trades blow roughly 70% of the year overall and up to about 90% of the time in summer.

---

## 3. Seasonal and daily wind patterns

### 3.1 Month by month (approximate, statewide character, Honolulu-type exposed site)

| Month | Trade wind frequency | Typical mean speed (mph) | Character |
|---|---|---|---|
| January | about 50% | 9 | Fronts, kona episodes, north swell |
| February | about 55% | 10 | Variable, occasional strong post-frontal NE |
| March | about 70% | 11.5 | Trades returning, still frontal |
| April | about 75% | 12 | Trades building |
| May | about 80% | 12 | Steady trades |
| June | about 90% | 13 | Peak consistency begins |
| July | about 92% | 13.5 | Most reliable trades of the year |
| August | about 90% | 13.5 | Reliable, hurricane season peak |
| September | about 82% | 12 | Weakening, humid lulls |
| October | about 72% | 11 | Transition, first kona chance |
| November | about 60% | 10.5 | Wet season begins |
| December | about 55% | 10 | Fronts, variable winds |

### 3.2 Approximate long-term mean wind speeds at airports

| Station | Island | Mean (mph) | Notes |
|---|---|---|---|
| Kahului (OGG) | Maui | about 13 | Central valley venturi, among the windiest airports in the state |
| Lihue (LIH) | Kauai | about 12 | Windward east coast exposure |
| Honolulu (HNL) | Oahu | about 11 | Trades crossing the island plus south shore exposure |
| Kalaeloa (JRF) | Oahu | about 10 | Ewa plain funnel |
| Molokai (MKK) | Molokai | about 12 | Open central plain |
| Lanai (LNY) | Lanai | about 11 | Upland plateau |
| Hilo (ITO) | Hawaii | about 7 | Blocked by Mauna Kea and Mauna Loa |
| Kona (KOA) | Hawaii | about 6 to 7 | Deep lee, sea breeze and land breeze cycle |

### 3.3 Daily cycle

| Time | Windward coasts | Leeward coasts of small islands | Leeward coasts of Hawaii Island and SW Maui |
|---|---|---|---|
| Night to dawn | Trades steady, slightly lighter | Trades may spill down as gusty downslope flow | Land breeze drains downslope offshore, 3 to 8 mph |
| Morning | Steady | Building | Calm transition period |
| Midday to afternoon | Strongest, enhanced by heated land | Strongest, venturi zones peak | Sea breeze onshore from W/SW, 8 to 15 mph |
| Evening | Easing | Easing | Calm transition, then land breeze |

Heating of land raises the pressure gradient between land and sea in the afternoon. Venturi zones (Maui's central valley, Maalaea, South Kohala) commonly peak between about 1 pm and 5 pm.

---

## 4. Non-trade regimes

| Regime | Direction | When | Speeds | Effects |
|---|---|---|---|---|
| Kona wind | S to SW (opposite of trades) | Mostly October to April, a few times per year | 10 to 30 mph, stronger in kona lows | Windward coasts go calm or offshore, leeward coasts get onshore wind and surf, vog spreads to Oahu and Maui |
| Kona low | Cyclonic, S to SW then shifting | Winter, about 1 to 4 per year | Gusts 40 to 70+ mph possible on exposed slopes | Heavy rain, flash floods, strong downslope gusts on north and west slopes |
| Cold front passage | Shifts to N and NW behind front | November to April | Post-frontal NE often 20 to 30 mph | North-facing coasts exposed, temperature drops a few degrees |
| Sea breeze / land breeze | Onshore by day, offshore at night | Any day with weak trades, always on Kona coast | 5 to 15 mph | Builds cumulus over slopes in the afternoon |
| Upper trough / light and variable | Variable | Any season | Under 8 mph | Muggy, convective showers |
| Downslope windstorm | Down the lee slopes | Strong trades plus low inversion | Gusts 50 to 80+ mph locally | Lahaina, Kula, Waianae and South Kohala gusts (August 2023 easterly gusts drove the Lahaina fire) |
| Tropical cyclone | Any | June to November | Iniki (1992, Kauai): Category 4, sustained about 145 mph | Rare direct hits; more often passing storms boost trades and surf |
| Summit westerlies | W to SW aloft | Winter jet stream | Mauna Kea and Haleakala summits commonly 20 to 40 mph, occasionally 100+ mph gusts | Above the inversion, independent of surface trades |

---

## 5. Channel winds between the islands

Air squeezed between two mountainous islands accelerates (venturi and corner effects). Channels typically run 5 to 15 mph stronger than open-ocean trades.

| Channel | Between | Width (approx.) | Max depth (approx.) | Typical trade wind behavior |
|---|---|---|---|---|
| Kaulakahi | Kauai and Niihau | 27 km | about 1,000 m | Modest acceleration, Niihau is low |
| Kaieiewaho (Kauai Channel) | Oahu and Kauai | 116 km | about 3,300 m | Wide and deep, open-ocean trades, big seas |
| Kaiwi (Molokai Channel) | Oahu and Molokai | 42 km | about 700 m | Notoriously rough, 20 to 30 mph common, Molokai Hoe and Molokai 2 Oahu race course |
| Kalohi | Molokai and Lanai | 15 km | about 260 m | Strong, steep wind chop |
| Pailolo | Maui and Molokai | 14 km | about 250 m | Strong, funnel between West Maui and East Molokai |
| Auau | Maui and Lanai | 15 km | under 100 m | Sheltered by surrounding islands, the Lahaina Roads anchorage, often lighter |
| Kealaikahiki | Lanai and Kahoolawe | 29 km | about 300 m | Moderate, trades wrapping around Maui |
| Alalakeiki | Maui and Kahoolawe | 11 km | about 250 m | Gusty, the exit of the Maalaea funnel |
| Alenuihaha | Maui and Hawaii | 48 km | about 1,900 m | The strongest channel, squeezed between Haleakala (3,055 m) and Kohala/Mauna Kea, 25 to 40 mph not unusual |

---

## 6. Coast by coast, island by island wind atlas

Speeds are typical trade wind day values. "Onshore" means wind blowing from sea toward land. "Side-shore" means wind blowing along the beach. "Offshore" means wind blowing from land out to sea.

### 6.1 Kauai (Kawaikini 1,598 m, Waialeale 1,569 m)

| Coast / location | Exposure to NE trades | Typical speed (mph) | Character |
|---|---|---|---|
| North Shore: Hanalei, Princeville, Haena, Kilauea | Side-onshore | 10 to 18 | Cliffs and valleys add gusts; winter north swell |
| Anahola | Onshore | 12 to 20 | Exposed reef and beach |
| East Side: Kapaa, Wailua, Lihue | Onshore | 12 to 20 | Steady, Lihue airport mean about 12 |
| Nawiliwili / Kalapaki | Side-onshore | 10 to 16 | Harbor partly sheltered by Haupu Ridge |
| Mahaulepu | Side-shore | 15 to 22 | One of the windiest Kauai beaches, ancient dunes |
| Poipu / Koloa | Side-offshore | 10 to 18 | Trades wrapping around the SE corner |
| Hanapepe / Port Allen | Offshore to side | 8 to 15 | Lee, dry, downslope gusts in strong trades |
| Waimea / Kekaha | Lee, side-shore along coast | 6 to 15 | Wind bends to blow along the coast, sunny |
| Barking Sands / Polihale | Lee, side-shore | 8 to 18 | Large dunes, sand squeaks when dry; afternoon wind along the coast |
| Na Pali Coast | Complex lee and corner flow | 5 to 25 | Cliffs up to about 1,000 m, rotor and gusts, accelerated corner winds near Kee and Polihale ends |
| Kokee / Waimea Canyon rim | Upland | 5 to 20 | Valley up-flow in the afternoon |

### 6.2 Niihau (Paniau 381 m)

| Coast / location | Exposure | Typical speed (mph) | Character |
|---|---|---|---|
| East and NE coasts | Onshore | 15 to 22 | Low island barely disturbs the trades |
| West coast | Side to offshore | 12 to 20 | Little lee shelter because terrain is low |
| Lehua islet | Fully exposed | 15 to 25 | Sea bird colony, open ocean wind |

### 6.3 Oahu (Kaala 1,227 m in the Waianae Range, Konahuanui 960 m in the Koolau Range)

| Coast / location | Exposure | Typical speed (mph) | Character |
|---|---|---|---|
| Kahuku Point / Turtle Bay | Fully exposed corner | 15 to 25 | Kahuku wind farms sit here for a reason |
| North Shore: Sunset, Waimea, Haleiwa, Mokuleia | Side-onshore to side-shore | 8 to 18 | Waianae and Koolau ends give partial shelter west of Haleiwa; Mokuleia is a glider (sailplane) and skydiving site at Dillingham Airfield |
| Kaena Point | Accelerated corner | 15 to 25 | Wind wraps the western tip; dune reserve |
| Laie / Hauula / Kaaawa | Onshore | 12 to 20 | Steady, cliffs immediately inland |
| Kaneohe Bay | Onshore | 12 to 20 | Bay plus sandbar, sailing and kiting |
| Kailua / Lanikai | Onshore to side-onshore | 12 to 22 | Oahu's main kitesurf and windsurf beach; steady, clean flow |
| Waimanalo | Onshore | 12 to 20 | Koolau cliffs inland produce strong ridge lift |
| Makapuu / Sandy Beach / Hawaii Kai | Accelerated SE corner | 15 to 28 | Corner acceleration; Makapuu cliffs are Oahu's classic hang gliding and paragliding ridge |
| Nuuanu Pali Lookout | Gap wind through the Koolau | 25 to 50 gusts | Air squeezed through a notch, famous for near-gale gusts on ordinary trade days |
| South Shore: Diamond Head, Waikiki, Ala Moana | Side-shore to side-offshore | 10 to 18 | Diamond Head is a windsurfing and kite spot; Waikiki itself is mostly light side-offshore |
| Honolulu Harbor / Sand Island / Keehi Lagoon | Side-offshore | 12 to 20 | Keehi is a kite and windsurf flat-water spot |
| Ewa / Kapolei / Kalaeloa | Funnel exit | 12 to 20 | Trades pour through the Schofield saddle between the two ranges |
| Central plateau: Wahiawa, Schofield | Funnel | 10 to 20 | Saddle accelerates air |
| Waianae Coast: Nanakuli, Maili, Makaha | Lee of Waianae Range | 5 to 12 | Lightest coast on the island, afternoon sea breeze, downslope gusts in strong trades |

### 6.4 Molokai (Kamakou 1,512 m)

| Coast / location | Exposure | Typical speed (mph) | Character |
|---|---|---|---|
| West End: Papohaku, Kaluakoi, Kepuhi | Side-shore to onshore | 15 to 25 | Flat, open, very windy, dry |
| Moomomi (NW) | Onshore | 15 to 25 | Active coastal dune field built by the trades; fossil bird bones in dune sediments |
| Kalaupapa Peninsula / north cliffs | Onshore | 12 to 22 | Sea cliffs around 1,000 m, among the tallest in the world; massive ridge lift and rotor in the cliff lee |
| Halawa (east end) | Onshore | 12 to 20 | Pailolo channel exposure |
| Kaunakakai / south shore | Side-offshore | 10 to 20 | Shallow reef flats, afternoon wind along the shore |
| Hoolehua plain (central) | Open | 12 to 20 | Airport, farmland, steady |

### 6.5 Lanai (Lanaihale 1,026 m)

| Coast / location | Exposure | Typical speed (mph) | Character |
|---|---|---|---|
| Shipwreck Beach (Kaiolohia) / NE coast | Onshore | 15 to 25 | Kalohi channel wind; wrecks driven ashore by trades and current |
| Polihua (north) | Side-onshore | 15 to 25 | Wide sand beach, strong wind, blowing sand |
| Keomuku / east coast | Side-shore | 12 to 20 | Abandoned village coast |
| Garden of the Gods (Keahiakawelo) | Upland exposed | 15 to 25 | Wind-eroded boulder landscape |
| Hulopoe / Manele (south) | Lee | 5 to 15 | Sheltered bay |
| Kaumalapau (west) | Lee | 5 to 12 | Harbor in the lee |

### 6.6 Maui (Haleakala 3,055 m, Puu Kukui 1,764 m)

| Coast / location | Exposure | Typical speed (mph) | Character |
|---|---|---|---|
| Kanaha / Spreckelsville / Kahului | Side-onshore, valley venturi | 15 to 30 | Central isthmus funnel between two volcanoes; world-class windsurfing and kitesurfing |
| Hookipa / Paia | Side-onshore | 15 to 28 | Windsurfing wave-sailing capital |
| Haiku / Peahi (Jaws) | Onshore cliffs | 12 to 22 | Big-wave site; cliffs produce strong upslope flow |
| Hana / East Maui windward | Onshore | 10 to 20 | Rainforest coast, very wet |
| Kipahulu / Kaupo | Wrap-around, gap winds | 10 to 25 | Kaupo Gap channels wind down from the crater |
| Maalaea / Maalaea Bay | Funnel exit | 20 to 35 afternoon | Among the windiest spots in the state; harbor famous for afternoon howlers |
| North Kihei | Side-offshore | 15 to 28 afternoon | Calm mornings, roaring afternoons |
| South Kihei / Wailea / Makena | Partial lee | 8 to 18 | Afternoon wind wraps from Maalaea; mornings glassy |
| La Perouse / Ahihi-Kinau | Lee, lava coast | 8 to 20 | Gusty, lava rock |
| Lahaina / Kaanapali | Lee of West Maui | 5 to 12 typical | Usually calm; downslope gust events in strong easterly flow |
| Kapalua / Honolua | NE exposure | 12 to 22 | Wind wraps the NW corner |
| Waihee / Kahakuloa (north) | Onshore cliffs | 12 to 22 | Rugged, ridge flow |
| Upcountry Kula / Polipoli (about 1,800 to 2,000 m) | Upland, west-facing | 5 to 20 | Paragliding launches; afternoon upslope breeze plus trade wrap |
| Haleakala summit | Above the inversion most days | 10 to 40 | Westerlies aloft in winter; very different from coastal trades |

### 6.7 Kahoolawe (Puu Moaulanui 452 m)

| Coast / location | Exposure | Typical speed (mph) | Character |
|---|---|---|---|
| NE and E coasts | Onshore | 15 to 25 | Barely blocked by low terrain |
| Interior plateau | Open | 15 to 25 | Wind erosion stripped topsoil after overgrazing; red dust plumes visible from Maui |
| W and S coasts | Side to offshore | 12 to 20 | Island is a cultural reserve with access controlled by the Kahoolawe Island Reserve Commission |

### 6.8 Hawaii Island (Mauna Kea 4,207 m, Mauna Loa 4,169 m, Hualalai 2,521 m, Kohala 1,670 m, Kilauea 1,247 m)

| Coast / location | Exposure | Typical speed (mph) | Character |
|---|---|---|---|
| Upolu Point / Hawi / North Kohala | Fully exposed corner | 20 to 30 | Alenuihaha exit; wind turbines at Hawi |
| Pololu / Waipio / Hamakua cliffs | Onshore | 10 to 20 | Tall sea cliffs, upslope flow |
| Hilo | Partially blocked windward | 5 to 12 | Trades split around the huge volcanoes; night land breeze off Mauna Kea |
| Puna / Kalapana / Kapoho | Onshore | 8 to 16 | Lava coast, steady but moderate |
| Ka Lae (South Point) | Accelerated corner | 20 to 30 | Wind farm; trees grow bent; southernmost point of the United States |
| Punaluu / Kau coast | Side-onshore | 12 to 22 | Black sand beach |
| Papakolea (Green Sand Beach) | Exposed | 15 to 25 | Olivine sand cone eroded by waves and wind |
| Kawaihae / Puako / Waikoloa / Mauna Kea Beach (South Kohala) | Gap wind between Kohala and Mauna Kea | 15 to 35 afternoon gusts | Waimea saddle funnel; strong offshore to side-offshore gusts, "Kawaihae winds" |
| Waimea town (about 800 m) | Saddle | 15 to 25 | Misty, windy ranch country |
| Kailua-Kona / Keauhou / Kealakekua / Honaunau | Deep lee of Mauna Loa and Hualalai | 3 to 10 | Trades nearly absent; daily sea breeze onshore and nighttime land breeze; island wake eddies offshore |
| Pohakuloa / Saddle Road | High saddle | 10 to 25 | Wind squeezed between Mauna Kea and Mauna Loa |
| Mauna Kea summit | Above inversion | 10 to 40 typical | Westerlies, winter jet stream, observatory wind records |

The lee of Hawaii Island creates a wake hundreds of kilometers long. Satellite images show paired lee vortices and a calm strip of ocean extending west of Kona. Ocean temperatures in the wake run slightly warmer because the calm lets surface water stratify.

---

## 7. Terrain and mountain airflow physics

### 7.1 Froude number: over or around?

The Froude number Fr = U / (N h), where U is wind speed, N is the Brunt-Vaisala (buoyancy) frequency and h is barrier height. When Fr is well below 1 the air lacks the kinetic energy to climb over and splits around the barrier. Hawaiian trades below the inversion are strongly stable, so N near 0.01 per second is a fair estimate.

| Barrier | Peak (m) | Trade speed U (m/s) | Froude no. U/(N h), N=0.01/s | Regime |
|---|---|---|---|---|
| Waianae Range (Oahu) | 1200 | 7 | 0.58 | Partial blocking, splitting at low levels |
| Koolau Range (Oahu) | 900 | 8 | 0.89 | Partial blocking, splitting at low levels |
| West Maui Mountains | 1760 | 8 | 0.45 | Partial blocking, splitting at low levels |
| Haleakala (Maui) | 3055 | 8 | 0.26 | Strong blocking, flow splits around |
| Kohala Mountain | 1670 | 8 | 0.48 | Partial blocking, splitting at low levels |
| Mauna Kea / Mauna Loa | 4170 | 7 | 0.17 | Strong blocking, flow splits around |
| Mt Waialeale-Kawaikini (Kauai) | 1590 | 7 | 0.44 | Partial blocking, splitting at low levels |
| East Molokai (Kamakou) | 1510 | 8 | 0.53 | Partial blocking, splitting at low levels |
| Lanaihale (Lanai) | 1026 | 8 | 0.78 | Partial blocking, splitting at low levels |

### 7.2 Effects observed on the islands

| Effect | Mechanism | Hawaiian examples |
|---|---|---|
| Corner acceleration | Flow splitting around a blocking mountain speeds up at the edges | Upolu Point, Ka Lae, Makapuu, Kaena Point, Kahuku |
| Gap / venturi wind | Mass continuity through a narrowing | Maui isthmus, Pali Lookout, Waimea saddle, Schofield saddle |
| Lee calm and wake | Blocked flow leaves a sheltered zone downwind | Kona coast, Waianae coast, Lahaina |
| Lee vortices | Flow separation shedding counter-rotating eddies | Off Kona, off Maui's SW coast |
| Downslope windstorm | Air spilling over a ridge under a low inversion accelerates down the lee | Lahaina, Kula, Waianae, Kawaihae |
| Orographic rain | Forced lifting cools and condenses | Waialeale (one of the rainiest places on Earth, about 11 m per year historically), Hilo, Hana |
| Rain shadow | Air descends, warms and dries in the lee | Kawaihae, Kihei, Kekaha, Waianae, Kahoolawe, Lanai |
| Ridge lift | Wind deflected upward by a slope | Makapuu, Kalaupapa cliffs, Koolau, Hamakua cliffs |
| Rotor | Turbulent recirculation behind steep ridges | Behind Na Pali, Koolau crest lee side, Kalaupapa cliff lee |

---

## 8. The beach boundary layer and blowing sand

### 8.1 Wind speed near the ground

Wind slows toward the surface because of friction. The logarithmic profile u(z) = u_ref ln(z/z0) / ln(z_ref/z0) estimates speeds at different heights. Table: wind at various heights when the standard 10 m anemometer reads 20 mph.

| Surface | z0 (m) | Wind at 0.5 m (mph) | 1 m | 2 m | 3 m | 5 m |
|---|---|---|---|---|---|---|
| Calm open water | 0.0002 | 14.5 | 15.7 | 17.0 | 17.8 | 18.7 |
| Smooth wet sand | 0.0003 | 14.2 | 15.6 | 16.9 | 17.7 | 18.7 |
| Dry beach sand | 0.001 | 13.5 | 15.0 | 16.5 | 17.4 | 18.5 |
| Beach with low dunes | 0.01 | 11.3 | 13.3 | 15.3 | 16.5 | 18.0 |
| Grass/naupaka strand | 0.03 | 9.7 | 12.1 | 14.5 | 15.9 | 17.6 |
| Scattered ironwood/kiawe | 0.2 | 4.7 | 8.2 | 11.8 | 13.8 | 16.5 |

A glider held at chest height (about 1.3 to 1.5 m) on a smooth beach feels roughly 80 to 85% of the forecast 10 m wind. Trees or buildings upwind cut that sharply and add turbulence.

### 8.2 Sand saltation threshold (Bagnold)

Threshold friction velocity u*t = A sqrt(((rho_s - rho_a) / rho_a) g d), with A about 0.1. Hawaiian beaches carry three main sand types: calcareous white sand (coral, shell, coralline algae, foraminifera), basalt black sand and olivine green sand.

| Grain size (mm) | Grain type | Threshold friction velocity u* (m/s) | 10 m wind to start blowing sand (m/s) | mph |
|---|---|---|---|---|
| 0.125 | porous calcareous white sand | 0.158 | 4.1 | 9.2 |
| 0.125 | basalt black sand | 0.174 | 4.5 | 10.1 |
| 0.125 | olivine green sand | 0.186 | 4.8 | 10.8 |
| 0.25 | porous calcareous white sand | 0.224 | 5.8 | 13.0 |
| 0.25 | basalt black sand | 0.246 | 6.4 | 14.3 |
| 0.25 | olivine green sand | 0.263 | 6.8 | 15.3 |
| 0.5 | porous calcareous white sand | 0.317 | 8.2 | 18.5 |
| 0.5 | basalt black sand | 0.348 | 9.1 | 20.3 |
| 0.5 | olivine green sand | 0.372 | 9.7 | 21.6 |
| 1.0 | porous calcareous white sand | 0.448 | 11.7 | 26.1 |
| 1.0 | basalt black sand | 0.493 | 12.8 | 28.7 |
| 1.0 | olivine green sand | 0.525 | 13.7 | 30.6 |

On typical trade wind days of 15 to 25 mph, dry fine white sand blows freely. Black and green sands are denser and stay put longer. Wet sand needs much stronger wind because of capillary cohesion. Saltating grains bounce at heights mostly under 30 cm, which is why blowing sand stings shins rather than faces.

---

## 9. Lift fundamentals

**Lift equation:** L = 0.5 x rho x V^2 x S x CL

| Symbol | Meaning | Unit |
|---|---|---|
| L | Lift force, perpendicular to the relative wind | N |
| rho | Air density | kg/m3 |
| V | Airspeed (wind speed plus any running speed into the wind) | m/s |
| S | Wing area | m2 |
| CL | Lift coefficient | dimensionless |

**To leave the ground:** L must equal the total weight W = (pilot mass + glider mass) x g.

**Key facts:**

- Lift scales with the square of airspeed. Doubling the wind quadruples lift.
- Lift scales linearly with area. Doubling the wing doubles lift.
- What matters is airspeed, not ground speed. A 15 mph headwind plus a 10 mph run gives 25 mph airspeed.
- A wing standing still in steady wind generates lift exactly as if it were flying through still air at that speed. This is how kites and kiting on paragliders work.

**Typical lift coefficients:**

| Surface | Usable CL | CL max (approx.) | Stall angle (approx.) |
|---|---|---|---|
| Flat rigid plate, low aspect ratio | 0.5 to 0.8 | 0.8 to 1.1 | 15 to 40 deg (low AR stalls late) |
| Flat tarp or sheet (flexes, flutters) | 0.4 to 0.7 | 0.8 | Poorly defined |
| Single-surface cambered fabric | 0.8 to 1.2 | 1.3 | 12 to 18 deg |
| Ram-air paraglider | 0.6 to 1.0 in flight | 1.1 to 1.3 | Collapses or stalls near 15 to 20 deg |
| Hang glider (double surface) | 0.6 to 1.1 | 1.3 to 1.5 | 14 to 18 deg |
| Cambered rigid airfoil (sailplane) | 0.3 to 1.2 | 1.4 to 1.6 | 14 to 16 deg |

---

## 10. Air density across Hawaiian conditions

| Condition | Elev (m) | Sea-level-equiv T (C) | Sea-level P (hPa) | RH % | Density (kg/m3) | vs typical beach |
|---|---|---|---|---|---|---|
| Beach, cool winter morning | 0 | 22 | 1018 | 65 | 1.194 | 101.9% |
| Beach, typical day | 0 | 26 | 1015 | 70 | 1.172 | 100.0% |
| Beach, hot humid afternoon | 0 | 31 | 1013 | 75 | 1.146 | 97.8% |
| Kona low passing (low pressure) | 0 | 27 | 1005 | 85 | 1.153 | 98.4% |
| Makapuu-type ridge launch | 300 | 25 | 1015 | 70 | 1.143 | 97.6% |
| Polipoli-type upland launch | 1900 | 18 | 1015 | 60 | 1.005 | 85.8% |
| Haleakala summit | 3055 | 10 | 1015 | 40 | 0.922 | 78.7% |
| Mauna Kea summit | 4205 | 4 | 1015 | 30 | 0.838 | 71.5% |

Lift drops in direct proportion to density. A launch at Mauna Kea's summit needs about 25% more airspeed squared, or roughly 12% more airspeed, than the same wing at the beach.

---

## 11. Dynamic pressure and wind power

Dynamic pressure q = 0.5 rho V^2 is the force per square meter the wind can exert on a surface facing it when CL or CD equals 1.

| Wind (mph) | m/s | km/h | knots | Dynamic pressure q (Pa) | q as kgf per m2 | Beaufort | Wind power (W/m2) |
|---|---|---|---|---|---|---|---|
| 5 | 2.24 | 8.0 | 4.3 | 2.9 | 0.30 | 2 | 7 |
| 10 | 4.47 | 16.1 | 8.7 | 11.7 | 1.19 | 3 | 52 |
| 15 | 6.71 | 24.1 | 13.0 | 26.3 | 2.69 | 4 | 177 |
| 20 | 8.94 | 32.2 | 17.4 | 46.8 | 4.78 | 5 | 419 |
| 25 | 11.18 | 40.2 | 21.7 | 73.2 | 7.46 | 6 | 818 |
| 30 | 13.41 | 48.3 | 26.1 | 105.4 | 10.74 | 6 | 1413 |
| 35 | 15.65 | 56.3 | 30.4 | 143.4 | 14.62 | 7 | 2244 |
| 40 | 17.88 | 64.4 | 34.8 | 187.3 | 19.10 | 8 | 3349 |
| 45 | 20.12 | 72.4 | 39.1 | 237.1 | 24.17 | 8 | 4769 |
| 50 | 22.35 | 80.5 | 43.4 | 292.7 | 29.84 | 9 | 6542 |

At 20 mph each square meter of wing with CL 1.0 carries about 5 kgf. A 100 kg person plus 5 kg wing therefore needs about 21 m2 of wing at 20 mph with no running.

---

## 12. Airspeed needed to carry 100 kg

All-up mass 105 kg. Each cell shows the airspeed in m/s and mph at which lift equals weight. Wing loading is total mass divided by area.

| Area (m2) | Wing loading (kg/m2) | CL 0.6 (m/s / mph) | CL 0.8 | CL 1.0 | CL 1.2 | CL 1.4 |
|---|---|---|---|---|---|---|
| 2 | 52.5 | 38.3 / 86 | 33.1 / 74 | 29.6 / 66 | 27.1 / 61 | 25.1 / 56 |
| 4 | 26.2 | 27.1 / 61 | 23.4 / 52 | 21.0 / 47 | 19.1 / 43 | 17.7 / 40 |
| 6 | 17.5 | 22.1 / 49 | 19.1 / 43 | 17.1 / 38 | 15.6 / 35 | 14.5 / 32 |
| 8 | 13.1 | 19.1 / 43 | 16.6 / 37 | 14.8 / 33 | 13.5 / 30 | 12.5 / 28 |
| 10 | 10.5 | 17.1 / 38 | 14.8 / 33 | 13.3 / 30 | 12.1 / 27 | 11.2 / 25 |
| 12 | 8.8 | 15.6 / 35 | 13.5 / 30 | 12.1 / 27 | 11.0 / 25 | 10.2 / 23 |
| 14 | 7.5 | 14.5 / 32 | 12.5 / 28 | 11.2 / 25 | 10.2 / 23 | 9.5 / 21 |
| 16 | 6.6 | 13.5 / 30 | 11.7 / 26 | 10.5 / 23 | 9.6 / 21 | 8.9 / 20 |
| 18 | 5.8 | 12.8 / 29 | 11.0 / 25 | 9.9 / 22 | 9.0 / 20 | 8.4 / 19 |
| 20 | 5.2 | 12.1 / 27 | 10.5 / 23 | 9.4 / 21 | 8.6 / 19 | 7.9 / 18 |
| 22 | 4.8 | 11.5 / 26 | 10.0 / 22 | 8.9 / 20 | 8.2 / 18 | 7.6 / 17 |
| 25 | 4.2 | 10.8 / 24 | 9.4 / 21 | 8.4 / 19 | 7.7 / 17 | 7.1 / 16 |
| 28 | 3.8 | 10.2 / 23 | 8.9 / 20 | 7.9 / 18 | 7.2 / 16 | 6.7 / 15 |
| 32 | 3.3 | 9.6 / 21 | 8.3 / 19 | 7.4 / 17 | 6.8 / 15 | 6.3 / 14 |
| 36 | 2.9 | 9.0 / 20 | 7.8 / 17 | 7.0 / 16 | 6.4 / 14 | 5.9 / 13 |
| 40 | 2.6 | 8.6 / 19 | 7.4 / 17 | 6.6 / 15 | 6.1 / 14 | 5.6 / 13 |

---

## 13. Effect of glider weight

Required airspeed in mph at CL 1.0 for a 100 kg pilot as glider mass rises. "Very light" fabric wings weigh 2 to 5 kg. Paragliders weigh 4 to 7 kg. Hang gliders weigh 20 to 35 kg.

| Area (m2) | +0 kg glider (mph) | +2 kg | +5 kg | +10 kg | +20 kg | +30 kg |
|---|---|---|---|---|---|---|
| 2 | 64.7 | 65.4 | 66.3 | 67.9 | 70.9 | 73.8 |
| 4 | 45.8 | 46.2 | 46.9 | 48.0 | 50.1 | 52.2 |
| 6 | 37.4 | 37.7 | 38.3 | 39.2 | 40.9 | 42.6 |
| 8 | 32.4 | 32.7 | 33.2 | 33.9 | 35.4 | 36.9 |
| 10 | 28.9 | 29.2 | 29.7 | 30.4 | 31.7 | 33.0 |
| 12 | 26.4 | 26.7 | 27.1 | 27.7 | 28.9 | 30.1 |
| 14 | 24.5 | 24.7 | 25.1 | 25.7 | 26.8 | 27.9 |
| 16 | 22.9 | 23.1 | 23.4 | 24.0 | 25.1 | 26.1 |
| 18 | 21.6 | 21.8 | 22.1 | 22.6 | 23.6 | 24.6 |
| 20 | 20.5 | 20.7 | 21.0 | 21.5 | 22.4 | 23.3 |
| 22 | 19.5 | 19.7 | 20.0 | 20.5 | 21.4 | 22.2 |
| 25 | 18.3 | 18.5 | 18.8 | 19.2 | 20.1 | 20.9 |
| 28 | 17.3 | 17.5 | 17.7 | 18.1 | 18.9 | 19.7 |
| 32 | 16.2 | 16.3 | 16.6 | 17.0 | 17.7 | 18.4 |
| 36 | 15.3 | 15.4 | 15.6 | 16.0 | 16.7 | 17.4 |
| 40 | 14.5 | 14.6 | 14.8 | 15.2 | 15.9 | 16.5 |

A 30 kg hang glider adds about 14% to the required airspeed versus a 0 kg ideal wing. The weight penalty matters far less than the area choice.

---

## 14. Lift as a percentage of body weight in a beach wind

Pilot standing still on the beach, wing held at its best lift angle into the wind. Values above 100% mean the pilot is lifted off the sand. All-up mass 105 kg.

### 14.1 Cambered fabric wing, CL 1.0

| Area (m2) | 10 mph | 15 mph | 20 mph | 25 mph | 30 mph | 35 mph | 40 mph |
|---|---|---|---|---|---|---|---|
| 2 | 2% | 5% | 9% | 14% | 20% | 28% | 36% |
| 4 | 5% | 10% | 18% | 28% | 41% | 56% | 73% |
| 6 | 7% | 15% | 27% | 43% | 61% | 84% | 109% |
| 8 | 9% | 20% | 36% | 57% | 82% | 111% | 146% |
| 10 | 11% | 26% | 45% | 71% | 102% | 139% | 182% |
| 12 | 14% | 31% | 55% | 85% | 123% | 167% | 218% |
| 14 | 16% | 36% | 64% | 99% | 143% | 195% | 255% |
| 16 | 18% | 41% | 73% | 114% | 164% | 223% | 291% |
| 18 | 20% | 46% | 82% | 128% | 184% | 251% | 327% |
| 20 | 23% | 51% | 91% | 142% | 205% | 279% | 364% |
| 22 | 25% | 56% | 100% | 156% | 225% | 306% | 400% |
| 25 | 28% | 64% | 114% | 178% | 256% | 348% | 455% |
| 28 | 32% | 72% | 127% | 199% | 287% | 390% | 509% |
| 32 | 36% | 82% | 146% | 227% | 327% | 446% | 582% |
| 36 | 41% | 92% | 164% | 256% | 368% | 501% | 655% |
| 40 | 45% | 102% | 182% | 284% | 409% | 557% | 728% |

### 14.2 Flat sheet or tarp, CL 0.7

| Area (m2) | 10 mph | 15 mph | 20 mph | 25 mph | 30 mph | 35 mph | 40 mph |
|---|---|---|---|---|---|---|---|
| 2 | 2% | 4% | 6% | 10% | 14% | 19% | 25% |
| 4 | 3% | 7% | 13% | 20% | 29% | 39% | 51% |
| 6 | 5% | 11% | 19% | 30% | 43% | 58% | 76% |
| 8 | 6% | 14% | 25% | 40% | 57% | 78% | 102% |
| 10 | 8% | 18% | 32% | 50% | 72% | 97% | 127% |
| 12 | 10% | 21% | 38% | 60% | 86% | 117% | 153% |
| 14 | 11% | 25% | 45% | 70% | 100% | 136% | 178% |
| 16 | 13% | 29% | 51% | 80% | 115% | 156% | 204% |
| 18 | 14% | 32% | 57% | 90% | 129% | 175% | 229% |
| 20 | 16% | 36% | 64% | 99% | 143% | 195% | 255% |
| 22 | 18% | 39% | 70% | 109% | 158% | 214% | 280% |
| 25 | 20% | 45% | 80% | 124% | 179% | 244% | 318% |
| 28 | 22% | 50% | 89% | 139% | 201% | 273% | 357% |
| 32 | 25% | 57% | 102% | 159% | 229% | 312% | 407% |
| 36 | 29% | 64% | 115% | 179% | 258% | 351% | 458% |
| 40 | 32% | 72% | 127% | 199% | 287% | 390% | 509% |

### 14.3 Cambered wing, CL 1.0, pilot jogging 5 m/s (11.2 mph) into the wind

| Area (m2) | 10 mph | 15 mph | 20 mph | 25 mph | 30 mph | 35 mph | 40 mph |
|---|---|---|---|---|---|---|---|
| 2 | 10% | 16% | 22% | 30% | 39% | 49% | 60% |
| 4 | 20% | 31% | 44% | 60% | 77% | 97% | 119% |
| 6 | 31% | 47% | 66% | 89% | 116% | 146% | 179% |
| 8 | 41% | 62% | 88% | 119% | 154% | 194% | 238% |
| 10 | 51% | 78% | 111% | 149% | 193% | 243% | 298% |
| 12 | 61% | 94% | 133% | 179% | 231% | 291% | 357% |
| 14 | 71% | 109% | 155% | 208% | 270% | 340% | 417% |
| 16 | 82% | 125% | 177% | 238% | 309% | 388% | 477% |
| 18 | 92% | 140% | 199% | 268% | 347% | 437% | 536% |
| 20 | 102% | 156% | 221% | 298% | 386% | 485% | 596% |
| 22 | 112% | 171% | 243% | 327% | 424% | 534% | 655% |
| 25 | 128% | 195% | 276% | 372% | 482% | 606% | 745% |
| 28 | 143% | 218% | 310% | 417% | 540% | 679% | 834% |
| 32 | 163% | 249% | 354% | 476% | 617% | 776% | 953% |
| 36 | 184% | 281% | 398% | 536% | 694% | 873% | >999% |
| 40 | 204% | 312% | 442% | 595% | 771% | 970% | >999% |

---

## 15. Raw lift force in kilograms-force (CL 1.0, standing still)

Useful for intuition: compare to 100 kg body mass.

| Area (m2) | 10 mph | 15 mph | 20 mph | 25 mph | 30 mph | 35 mph | 40 mph |
|---|---|---|---|---|---|---|---|
| 2 | 2 | 5 | 10 | 15 | 21 | 29 | 38 |
| 4 | 5 | 11 | 19 | 30 | 43 | 58 | 76 |
| 6 | 7 | 16 | 29 | 45 | 64 | 88 | 115 |
| 8 | 10 | 21 | 38 | 60 | 86 | 117 | 153 |
| 10 | 12 | 27 | 48 | 75 | 107 | 146 | 191 |
| 12 | 14 | 32 | 57 | 90 | 129 | 175 | 229 |
| 14 | 17 | 38 | 67 | 104 | 150 | 205 | 267 |
| 16 | 19 | 43 | 76 | 119 | 172 | 234 | 306 |
| 18 | 21 | 48 | 86 | 134 | 193 | 263 | 344 |
| 20 | 24 | 54 | 96 | 149 | 215 | 292 | 382 |
| 22 | 26 | 59 | 105 | 164 | 236 | 322 | 420 |
| 25 | 30 | 67 | 119 | 187 | 269 | 366 | 478 |
| 28 | 33 | 75 | 134 | 209 | 301 | 409 | 535 |
| 32 | 38 | 86 | 153 | 239 | 344 | 468 | 611 |
| 36 | 43 | 97 | 172 | 269 | 387 | 526 | 688 |
| 40 | 48 | 107 | 191 | 298 | 430 | 585 | 764 |

A 40 m2 wing in a 40 mph wind generates over 1,000 kgf. That is the scale of force behind kite and paraglider dragging accidents: no person can hold that by grip strength.

---

## 16. Wind speed needed to leave the ground

CL 1.0, all-up mass 105 kg. Running into the wind subtracts directly from the wind speed needed.

| Area (m2) | Wind needed standing still (mph) | Wind needed with 5 m/s jog | With 7 m/s run | With 9 m/s sprint |
|---|---|---|---|---|
| 2 | 66.3 | 55.1 | 50.7 | 46.2 |
| 4 | 46.9 | 35.7 | 31.2 | 26.8 |
| 6 | 38.3 | 27.1 | 22.6 | 18.2 |
| 8 | 33.2 | 22.0 | 17.5 | 13.0 |
| 10 | 29.7 | 18.5 | 14.0 | 9.5 |
| 12 | 27.1 | 15.9 | 11.4 | 6.9 |
| 14 | 25.1 | 13.9 | 9.4 | 4.9 |
| 16 | 23.4 | 12.3 | 7.8 | 3.3 |
| 18 | 22.1 | 10.9 | 6.4 | 2.0 |
| 20 | 21.0 | 9.8 | 5.3 | 0.8 |
| 22 | 20.0 | 8.8 | 4.3 | 0.0 |
| 25 | 18.8 | 7.6 | 3.1 | 0.0 |
| 28 | 17.7 | 6.5 | 2.1 | 0.0 |
| 32 | 16.6 | 5.4 | 0.9 | 0.0 |
| 36 | 15.6 | 4.4 | 0.0 | 0.0 |
| 40 | 14.8 | 3.6 | 0.0 | 0.0 |

---

## 17. Location scenarios

Combining the atlas with the lift equation. CL 1.0, 105 kg all-up mass.

| Location scenario | Wind (mph) | Wing area (m2) | Lift % standing | Lift % with 5 m/s jog | Wind for full lift standing (mph) | Outcome at CL 1.0 |
|---|---|---|---|---|---|---|
| Kailua Beach, Oahu | 15 | 8 | 20% | 62% | 33.2 | Lightened only |
| Kailua Beach, Oahu | 15 | 16 | 41% | 125% | 23.4 | Airborne with jog |
| Kailua Beach, Oahu | 15 | 22 | 56% | 171% | 20.0 | Airborne with jog |
| Kanaha, Maui afternoon | 22 | 8 | 44% | 100% | 33.2 | Airborne with jog |
| Kanaha, Maui afternoon | 22 | 14 | 77% | 175% | 25.1 | Airborne with jog |
| Kanaha, Maui afternoon | 22 | 22 | 121% | 275% | 20.0 | Airborne standing |
| Maalaea, Maui strong day | 30 | 6 | 61% | 116% | 38.3 | Airborne with jog |
| Maalaea, Maui strong day | 30 | 12 | 123% | 231% | 27.1 | Airborne standing |
| Moomomi, Molokai | 20 | 10 | 45% | 111% | 29.7 | Airborne with jog |
| Moomomi, Molokai | 20 | 18 | 82% | 199% | 22.1 | Airborne with jog |
| Upolu Point, Hawaii Island | 25 | 8 | 57% | 119% | 33.2 | Airborne with jog |
| Upolu Point, Hawaii Island | 25 | 14 | 99% | 208% | 25.1 | Airborne with jog |
| Kailua-Kona sea breeze | 8 | 22 | 16% | 92% | 20.0 | Lightened only |
| Kailua-Kona sea breeze | 8 | 36 | 26% | 151% | 15.6 | Airborne with jog |
| Poipu, Kauai | 14 | 18 | 40% | 130% | 22.1 | Airborne with jog |
| Waikiki side-shore | 12 | 20 | 33% | 122% | 21.0 | Airborne with jog |

---

## 18. Jump height and air time while partly supported

A strong standing jump launches the body center of mass at about 3.1 m/s, enough for about 0.5 m of rise in normal gravity. If a wing carries a fraction of the weight, the effective gravity drops and the same jump goes higher and lasts longer. The table assumes lift stays constant through the jump.

| Lift as % of weight | Felt weight (kg) | Effective gravity (m/s2) | Peak height from 0.5 m-class jump (m) | Air time (s) |
|---|---|---|---|---|
| 0% | 100 | 9.81 | 0.50 | 0.64 |
| 25% | 75 | 7.35 | 0.67 | 0.85 |
| 50% | 50 | 4.90 | 1.00 | 1.28 |
| 60% | 40 | 3.92 | 1.25 | 1.60 |
| 70% | 30 | 2.94 | 1.67 | 2.13 |
| 80% | 20 | 1.96 | 2.50 | 3.19 |
| 85% | 15 | 1.47 | 3.33 | 4.26 |
| 90% | 10 | 0.98 | 5.00 | 6.39 |
| 95% | 5 | 0.49 | 10.00 | 12.77 |
| 98% | 2 | 0.20 | 25.00 | 31.93 |

At 90% support the pilot experiences one-tenth of normal gravity: a 0.5 m hop becomes a 5 m float lasting over 6 seconds. Real lift does not stay constant because wind changes with height (section 8) and the wing angle changes as the body rises, so the effect is less tidy in practice. Gusts at high support fractions make the ride abrupt.

---

## 19. Glide performance by glider class

Glide ratio L/D equals horizontal distance per unit of height lost in still air. Sink rate equals airspeed divided by L/D.

| Glider class | L/D | Trim airspeed (m/s) | mph | Sink (m/s) | Glide from 1 m (m) | 3 m | 10 m | 30 m | 100 m | 300 m |
|---|---|---|---|---|---|---|---|---|---|---|
| Flat tarp/sheet | 2.0 | 8.0 | 18 | 4.00 | 2 | 6 | 20 | 60 | 200 | 600 |
| Cloth delta toy-style | 3.0 | 8.0 | 18 | 2.67 | 3 | 9 | 30 | 90 | 300 | 900 |
| Foil kite flown as wing | 5.0 | 9.0 | 20 | 1.80 | 5 | 15 | 50 | 150 | 500 | 1500 |
| Speedwing 8-12 m2 | 4.5 | 14.0 | 31 | 3.11 | 4 | 14 | 45 | 135 | 450 | 1350 |
| Mini-wing 13-18 m2 | 6.0 | 11.0 | 25 | 1.83 | 6 | 18 | 60 | 180 | 600 | 1800 |
| Beginner paraglider | 8.5 | 10.5 | 23 | 1.24 | 8 | 26 | 85 | 255 | 850 | 2550 |
| Competition paraglider | 12.0 | 11.5 | 26 | 0.96 | 12 | 36 | 120 | 360 | 1200 | 3600 |
| Beginner hang glider | 10.0 | 10.0 | 22 | 1.00 | 10 | 30 | 100 | 300 | 1000 | 3000 |
| Topless hang glider | 15.0 | 11.0 | 25 | 0.73 | 15 | 45 | 150 | 450 | 1500 | 4500 |
| Rigid-wing hang glider | 19.0 | 12.0 | 27 | 0.63 | 19 | 57 | 190 | 570 | 1900 | 5700 |
| Training sailplane | 30.0 | 25.0 | 56 | 0.83 | 30 | 90 | 300 | 900 | 3000 | 9000 |
| Open-class sailplane | 60.0 | 30.0 | 67 | 0.50 | 60 | 180 | 600 | 1800 | 6000 | 18000 |

From a 3 m beach dune a beginner paraglider glides about 25 m in still air. Into a 15 mph headwind the ground distance shrinks because the headwind subtracts from ground speed. A wind equal to the trim airspeed makes the glider hover in place over the ground.

---

## 20. Aspect ratio, induced drag and best glide

Aspect ratio AR = span^2 / area. Induced drag coefficient CDi = CL^2 / (pi e AR). Maximum L/D = 0.5 sqrt(pi e AR / CD0).

| Planform | Aspect ratio | CD0 (incl. pilot) | Oswald e | Theoretical max L/D | CL at best glide |
|---|---|---|---|---|---|
| Flat square sheet | 1.0 | 0.1 | 0.6 | 2.2 | 0.43 |
| Small delta | 2.5 | 0.06 | 0.7 | 4.8 | 0.57 |
| Speedwing | 3.5 | 0.045 | 0.75 | 6.8 | 0.61 |
| Beginner paraglider (flat AR) | 5.0 | 0.035 | 0.8 | 9.5 | 0.66 |
| Competition paraglider | 7.0 | 0.03 | 0.82 | 12.3 | 0.74 |
| Hang glider | 7.0 | 0.025 | 0.8 | 13.3 | 0.66 |
| Rigid wing | 10.0 | 0.02 | 0.85 | 18.3 | 0.73 |
| Sailplane | 25.0 | 0.01 | 0.9 | 42.0 | 0.84 |

Long, narrow wings beat short, wide ones for glide. Short wide wings handle gusts and tolerate high angles of attack better, which is why beginner wings and speedwings trade glide for forgiveness.

---

## 21. Reynolds numbers

Re = V c / nu. Below about 100,000 airfoils lose efficiency through laminar separation bubbles. Every human-scale glider sits well above that, so full-scale aerodynamics apply.

| Surface | Chord (m) | Re at 5 m/s | 10 m/s | 15 m/s |
|---|---|---|---|---|
| Frigatebird wing | 0.25 | 7.81e+04 | 1.56e+05 | 2.34e+05 |
| Speedwing | 1.6 | 5.00e+05 | 1.00e+06 | 1.50e+06 |
| Paraglider | 2.6 | 8.12e+05 | 1.62e+06 | 2.44e+06 |
| Hang glider (mean) | 1.8 | 5.62e+05 | 1.12e+06 | 1.69e+06 |
| Flat 2x2 m sheet | 2.0 | 6.25e+05 | 1.25e+06 | 1.88e+06 |

---

## 22. Ridge and cliff lift

Wind meeting a slope is deflected upward. Vertical velocity near the slope face is roughly wind speed x sin(slope angle). Real updraft peaks a short distance upwind of and above the crest, often exceeding these values by 20 to 50% for smooth, long ridges.

| Slope angle (deg) | 10 mph wind: updraft (m/s) | 15 mph | 20 mph | 25 mph | 30 mph |
|---|---|---|---|---|---|
| 5 | 0.39 | 0.58 | 0.78 | 0.97 | 1.17 |
| 10 | 0.78 | 1.16 | 1.55 | 1.94 | 2.33 |
| 15 | 1.16 | 1.74 | 2.31 | 2.89 | 3.47 |
| 20 | 1.53 | 2.29 | 3.06 | 3.82 | 4.59 |
| 25 | 1.89 | 2.83 | 3.78 | 4.72 | 5.67 |
| 30 | 2.24 | 3.35 | 4.47 | 5.59 | 6.71 |
| 35 | 2.56 | 3.85 | 5.13 | 6.41 | 7.69 |
| 40 | 2.87 | 4.31 | 5.75 | 7.18 | 8.62 |
| 45 | 3.16 | 4.74 | 6.32 | 7.90 | 9.48 |
| 60 | 3.87 | 5.81 | 7.74 | 9.68 | 11.61 |

A paraglider sinks about 1.0 to 1.2 m/s and a hang glider about 0.9 to 1.1 m/s. Sustained soaring therefore needs updraft above those values, which in practice means a 15+ mph wind on a slope steeper than about 25 to 30 degrees. Makapuu's cliffs and Kalaupapa's sea cliffs exceed this easily on normal trade days. A 3 m beach dune produces a thin band of lift only a few meters deep: enough to hover a light wing kited at arm's length, not enough to climb meaningfully.

---

## 23. Ground effect

Near the surface, the ground blocks the downwash and wingtip vortices. Induced drag drops. McCormick's approximation: phi = (16 h/b)^2 / (1 + (16 h/b)^2), where h is height and b is span.

| Height / span | Induced drag factor (phi) | Induced drag reduction |
|---|---|---|
| 0.02 | 0.09 | 91% |
| 0.05 | 0.39 | 61% |
| 0.1 | 0.72 | 28% |
| 0.15 | 0.85 | 15% |
| 0.2 | 0.91 | 9% |
| 0.3 | 0.96 | 4% |
| 0.4 | 0.98 | 2% |
| 0.5 | 0.98 | 2% |
| 0.75 | 0.99 | 1% |
| 1.0 | 1.00 | 0% |

For a 10 m span wing, ground effect is meaningful below about 5 m and dramatic below about 1 m. Skimming low along a beach in steady wind stretches a glide noticeably. Lift at a given angle of attack also increases slightly in ground effect.

---

## 24. Turns, load factor and gusts

### 24.1 Banked turns

Load factor n = 1 / cos(bank). Stall speed rises with the square root of n.

| Bank (deg) | Load factor n | Stall speed multiplier | Stall speed on 20 m2, CL 1.0 (mph) | Apparent mass on wing (kg) |
|---|---|---|---|---|
| 0 | 1.00 | 1.000 | 21.0 | 105 |
| 10 | 1.02 | 1.008 | 21.1 | 107 |
| 20 | 1.06 | 1.032 | 21.6 | 112 |
| 30 | 1.15 | 1.075 | 22.5 | 121 |
| 40 | 1.31 | 1.143 | 24.0 | 137 |
| 45 | 1.41 | 1.189 | 24.9 | 148 |
| 50 | 1.56 | 1.247 | 26.2 | 163 |
| 60 | 2.00 | 1.414 | 29.7 | 210 |
| 70 | 2.92 | 1.710 | 35.9 | 307 |

### 24.2 Vertical gust response

A sudden upward gust U raises the angle of attack. Load increment Delta n = rho V a U S / (2 W), with lift curve slope a = 2 pi AR / (AR + 2). Values below for a 20 m2 wing, AR 5, 105 kg all-up.

| Airspeed (m/s), 20 m2 AR 5 | 1 m/s vertical gust | 2 m/s | 3 m/s | 4 m/s | 5 m/s |
|---|---|---|---|---|---|
| 8 | +0.41 | +0.82 | +1.23 | +1.63 | +2.04 |
| 10 | +0.51 | +1.02 | +1.53 | +2.04 | +2.55 |
| 12 | +0.61 | +1.23 | +1.84 | +2.45 | +3.06 |

A 3 m/s thermal or gust edge adds about a quarter of a g to a light wing at low speed. Light wings with high area per kilogram respond the most to gusts. This is the physical reason ultralight wings feel twitchy in rough beach wind.

---

## 25. Drag on the body and wing

Drag D = 0.5 rho V^2 S CD.

| Wind (mph) | Standing person drag (kgf, CD 1.1, 0.75 m2) | Prone harnessed (kgf, CD 1.0, 0.35 m2) | Wing drag 20 m2 at CD 0.12 (kgf) |
|---|---|---|---|
| 10 | 1.0 | 0.4 | 2.9 |
| 15 | 2.2 | 0.9 | 6.4 |
| 20 | 3.9 | 1.7 | 11.5 |
| 25 | 6.2 | 2.6 | 17.9 |
| 30 | 8.9 | 3.8 | 25.8 |
| 35 | 12.1 | 5.1 | 35.1 |
| 40 | 15.8 | 6.7 | 45.8 |

A standing person in a 30 mph wind feels about 17 kgf of push. Lying prone in a harness cuts the frontal area roughly in half. Body drag is the single largest drag source on paragliders and hang gliders at low speed.

---

## 26. Stability and control of very light wings

| Concept | Physics | Practical consequence for a beach wing |
|---|---|---|
| Center of pressure travel | On a flat or cambered plate, the point where lift acts moves with angle of attack | Flat sheets pitch violently, which is why they tumble instead of gliding |
| Pendulum stability | Pilot hangs well below the wing (paragliders 6 to 8 m, hang gliders about 1.5 m) | Low center of gravity rights the wing automatically |
| Reflex camber | Trailing edge turned up | Lets flying wings self-trim without a tail |
| Sweep and dihedral | Wingtips behind and above the center | Yaw and roll stability on hang gliders |
| Weight shift control | Pilot moves the center of gravity | Hang gliders and some ultralights steer this way; slow response on heavy pilots |
| Brake / trailing edge control | Pulling the trailing edge down raises local CL and drag | Paraglider steering and flare |
| Mass ratio | Wing mass vs air mass it moves | A 3 kg wing reacts instantly to gusts; a 30 kg glider smooths them out |
| Tethered (kited) wing | Line tension adds a restoring force | Kiting on a beach is how paraglider pilots practice ground handling |
| Collapse | Ram-air wings need internal pressure | Turbulence or low angle of attack folds the fabric |
| Flutter | Aeroelastic coupling of fabric and flow | Loose tarps flog and lose most lift |

---

## 27. Comparisons with Hawaiian seabirds

Stall speeds estimated at CL 1.2.

| Flyer | Mass (kg) | Wing area (m2) | Wing loading (kg/m2) | Stall speed at CL 1.2 (mph) |
|---|---|---|---|---|
| Great frigatebird (iwa) | 1.4 | 0.37 | 3.8 | 16.3 |
| Laysan albatross (moli) | 3.0 | 0.38 | 7.9 | 23.5 |
| Red-tailed tropicbird | 0.75 | 0.1 | 7.5 | 22.9 |
| White tern (manu-o-ku) | 0.11 | 0.05 | 2.2 | 12.4 |
| Hawaiian hawk (io) | 0.5 | 0.13 | 3.8 | 16.4 |
| 100 kg pilot + 5 kg wing, 10 m2 | 105 | 10 | 10.5 | 27.1 |
| Same on 16 m2 | 105 | 16 | 6.6 | 21.4 |
| Same on 22 m2 | 105 | 22 | 4.8 | 18.3 |
| Same on 28 m2 | 105 | 28 | 3.8 | 16.2 |
| 100 kg + 30 kg hang glider, 14 m2 | 130 | 14 | 9.3 | 25.5 |
| Sailplane, 450 kg on 10.5 m2 | 450 | 10.5 | 42.9 | 54.7 |

The great frigatebird (iwa) has the lowest wing loading of any bird relative to its size, about 3.8 kg/m2, and can stay aloft for weeks. The Laysan albatross (moli) uses dynamic soaring: it harvests energy from the wind gradient just above the waves. A 105 kg pilot-plus-wing system on about 13 m2 matches the albatross's wing loading. Matching the frigatebird would take about 28 m2 for a 105 kg system, which is beginner paraglider size. The 1902 Wright glider sat in the same range.

---

## 28. Waves, swell and sea state from the same wind

| Wind (mph) | Beaufort | Open-ocean wave height (fully developed, approx.) | Sea appearance |
|---|---|---|---|
| 5 | 2 | 0.2 m | Small wavelets |
| 10 | 3 | 0.6 m | Scattered whitecaps begin |
| 15 | 4 | 1.0 m | Frequent whitecaps |
| 20 | 5 | 2.0 m | Moderate waves, many whitecaps, some spray |
| 25 | 6 | 3.0 m | Large waves, extensive whitecaps |
| 30 | 7 | 4.0 m | Sea heaps up, streaks of foam |
| 40 | 8 | 5.5 m | Long high waves, spindrift |

Trade wind swell arrives on east-facing shores most of the year at 1 to 2.5 m and periods of 6 to 9 seconds. North shores receive winter swell generated by distant North Pacific storms (periods 12 to 20 seconds, faces sometimes 10 to 15 m at Waimea, Peahi and Mavericks-type outer reefs). South shores receive summer swell from Southern Hemisphere storms. Kona winds bring short, choppy waves to west and south shores.

Wind and water are connected for any glider pilot on a beach: steady onshore wind arriving over open ocean has very low turbulence because water is smooth, making beaches some of the cleanest launch sites anywhere.

---

## 29. History: dune gliders and beach flight

| Pioneer | Years | Site | Wing area | Glider mass | Notes |
|---|---|---|---|---|---|
| Otto Lilienthal | 1891 to 1896 | Artificial hill near Berlin and Rhinow hills | about 13 to 20 m2 | about 20 kg | Over 2,000 flights; weight-shift control; died after a stall in 1896 |
| Octave Chanute and Augustus Herring | 1896 | Indiana Dunes, Lake Michigan shore | about 13 to 17 m2 | about 10 to 15 kg | Biplane hang glider; dune winds off the lake |
| Wright brothers | 1900 to 1902 | Kill Devil Hills dunes, Kitty Hawk, North Carolina | 1902 glider about 28 m2 | about 50 kg | Chose the site for steady sea winds and soft sand; flew hundreds of glides in 1902 |
| John J. Montgomery | 1883 to 1905 | California hills and coast | varied | varied | Early controlled glides, tandem-wing designs |
| Francis Rogallo | 1948 onward | NASA and private work | varied | very light | Flexible delta wing that later became the modern hang glider |
| Dave Kilbourne, John Dickenson and others | 1960s to 1970s | Coastal dunes and ridges worldwide | about 15 to 20 m2 | about 18 to 25 kg | Birth of modern hang gliding |
| Paragliding pioneers | 1978 onward | French Alps | about 20 to 30 m2 | about 5 to 7 kg | Ram-air canopies adapted from skydiving |
| Hawaii hang gliding | 1970s onward | Makapuu, Oahu | standard hang gliders | 20 to 30 kg | Makapuu became a world-famous ridge for long soaring flights |

Kitty Hawk averaged roughly 13 mph winds during the Wrights' season. The 1902 glider at 28 m2 carrying about 120 kg needed about 21 mph of airspeed at CL around 0.8: a moderate wind plus a short run, matching the tables above.

---

## 30. Hawaiian soaring and wind-sport sites

| Site | Island | Sport | Wind need |
|---|---|---|---|
| Makapuu cliffs | Oahu | Hang gliding, paragliding | NE to E trades 12 to 25 mph |
| Waimanalo / Koolau ridge | Oahu | Paragliding | Steady trades |
| Dillingham Airfield, Mokuleia | Oahu | Sailplanes, skydiving | Trades, plus ridge lift off the Waianae Range |
| Kailua Beach | Oahu | Kitesurfing, windsurfing | 12 to 22 mph |
| Diamond Head | Oahu | Windsurfing, kitesurfing | 15+ mph |
| Kanaha Beach Park | Maui | Kitesurfing, windsurfing | 15 to 30 mph |
| Hookipa | Maui | Wave windsurfing | 18 to 30 mph |
| Polipoli and Kula launches | Maui | Paragliding, tandem tours | Light trades, afternoon upslope |
| Maalaea / Kihei | Maui | Kitesurfing, speed sailing | 20 to 35 mph afternoons |
| Anini / Kapaa | Kauai | Windsurfing, kite | 12 to 20 mph |
| Upolu / Kohala coast | Hawaii | Experienced kite and windsurf | 20 to 35 mph |
| Kawaihae / Puako | Hawaii | Kite in gap winds | Gusty, advanced |
| Moomomi / West Molokai | Molokai | Kite, remote | 15 to 25 mph |

Honolulu (HNL) Class B airspace covers much of southern Oahu. Hawaii also hosts restricted airspace around military installations such as Kaneohe MCBH, Pacific Missile Range Facility on Kauai and Pohakuloa Training Area. FAA Part 103 governs unpowered ultralight vehicles (hang gliders and paragliders) in the United States: under 155 lb empty for unpowered, single occupant, daylight only, no flight over congested areas.

---

## 31. Formula sheet

| Purpose | Formula |
|---|---|
| Lift | L = 0.5 rho V^2 S CL |
| Drag | D = 0.5 rho V^2 S CD |
| Required airspeed for level flight | V = sqrt(2 W / (rho S CL)) |
| Required wing area | S = 2 W / (rho V^2 CL) |
| Wing loading | W/S |
| Glide ratio | L/D = horizontal distance / height lost |
| Sink rate | v_sink = V / (L/D) |
| Induced drag coefficient | CDi = CL^2 / (pi e AR) |
| Total drag polar | CD = CD0 + CL^2 / (pi e AR) |
| Max L/D | 0.5 sqrt(pi e AR / CD0) |
| Min sink CL | sqrt(3 pi e AR CD0) |
| Aspect ratio | AR = b^2 / S |
| Load factor in turn | n = 1 / cos(bank) |
| Turn radius | r = V^2 / (g tan(bank)) |
| Stall speed in turn | V_s,turn = V_s sqrt(n) |
| Dynamic pressure | q = 0.5 rho V^2 |
| Wind power density | P/A = 0.5 rho V^3 |
| Air density (moist) | rho = p_d / (R_d T) + p_v / (R_v T), R_d = 287.06, R_v = 461.50 J/(kg K) |
| Pressure with altitude | p = p0 (1 - 2.25577e-5 h)^5.25588 |
| Log wind profile | u(z) = (u* / 0.4) ln(z / z0) |
| Ridge updraft (approx.) | w = U sin(theta) |
| Froude number | Fr = U / (N h) |
| Reynolds number | Re = V c / nu |
| Ground effect factor | phi = (16 h/b)^2 / (1 + (16 h/b)^2) |
| Gust load increment | Delta n = rho V a U S / (2 W) |
| Bagnold sand threshold | u*t = 0.1 sqrt(((rho_s - rho_a)/rho_a) g d) |
| Effective gravity with partial lift | g_eff = g (1 - L/W) |
| Jump peak height | h = v0^2 / (2 g_eff) |

---

## 32. Unit conversions

| From | To | Multiply by |
|---|---|---|
| mph | m/s | 0.44704 |
| knots | m/s | 0.514444 |
| km/h | m/s | 0.277778 |
| m/s | mph | 2.23694 |
| m/s | knots | 1.94384 |
| knots | mph | 1.15078 |
| m2 | ft2 | 10.7639 |
| kg | lb | 2.20462 |
| N | lbf | 0.224809 |
| kgf | N | 9.80665 |
| Pa | psf (lb/ft2) | 0.0208854 |
| m | ft | 3.28084 |
| kg/m3 | slug/ft3 | 0.00194032 |
| hPa (mb) | inHg | 0.02953 |

## Terra readout (soft)

| Piece | Note |
|---|---|
| **Weather.md** | Calendar / inversion / rain; this file is coast atlas + beach-wing lift |
| **PerfectGlider Hawaii** | Design A/B/C channel crossings; use these tables for 100 kg beach / ridge days |
| **Sands.md** | White / black / green sand types feed the Bagnold thresholds here |
| **Kona lee** | Calmest launch window for human-powered Design C |
| **Makapuu-class cliffs** | Ridge soar when trades 12–25 mph and slope 25°+ |
