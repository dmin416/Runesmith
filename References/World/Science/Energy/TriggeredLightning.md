# Triggered Lightning Harvest

> Earth reference / invent loot. Not locked law. Mana bolt / real-bolt scale: `ManaCast.md`. Storage vs capture: `Batteries.md`, `CleanestUsefulEnergyStorage.md`. Electricity Resistance: `../../../Progression/SkillsDesign.md`. Volcanic-island storm sites: `../../Geography/VolcanicIsland/FarmingSystems.md`, `../../Geography/VolcanicIsland/Resources.md`.

Terra **Electricity Resistance** cuts shock harm from a hit. Capturing a flash is an engineering / site problem, not a body skill. Most flash energy dissipates aloft; ground-end yield is a few solar panels of yearly output per launch station at realistic capture.

---

## Methods that work

**Rocket and wire (proven, used since the 1970s).** The standard setup is a one meter long solid fuel rocket with a 0.2 mm diameter copper wire that unspools behind it. The rocket climbs at about 200 m/s; once it reaches roughly 200 to 300 m, field enhancement at its tip launches an upward leader toward the cloud's negative charge region at 5 to 7 km. That leader vaporizes the wire and starts a continuous current of several hundred amperes from the cloud down the wire trace to the ground station. Launches happen only when the ground-level field under the storm is already strong (roughly 4 to 10 kV/m). In Florida summer storms about half of launches succeed.

**Other routes:**
- Tall grounded towers or masts on mountaintops trigger upward lightning on their own.
- Balloons or kites holding a grounded wire (Franklin's method scaled up).
- Lasers: the Säntis mountain experiment in Switzerland (2021, published 2023) guided several strikes along a laser path for about 50 m. Still experimental.

## Wire length

| Situation | Height where triggering happens | Wire carried |
|---|---|---|
| Florida summer storm | 200 to 300 m | 600 to 1,000 m spool |
| Japanese winter storm (low charge) | 100 to 200 m | 300 to 500 m |
| Weak or distant storm | 400 m+ | 1 km+ |

The governing factor is the potential difference across the wire's length: a few megavolts. One simulation found a grounded wire triggers above about 180 m once the ambient field across its length exceeds roughly 6.5 MV. Stronger field overhead means shorter wire.

**Survivability problem.** Thin trigger wire is destroyed every time. A conductor that survives a strike needs lightning-protection gauge copper (about 30 to 50 mm²). At 50 mm², copper weighs about 450 g per meter, so a 500 m permanent tether weighs around 225 kg. That requires a tethered aerostat or a tower rather than a rocket.

## Energy per strike

- Total energy of a cloud-to-ground flash: about 1 to 5 GJ (280 to 1,400 kWh).
- Most of that is spent heating the air channel kilometers above the ground: light, thunder, radio emission. Only a small fraction reaches the base of the channel.
- Energy deliverable to a ground-end load: roughly 0.1 to 5 MJ for a typical strike (0.03 to 1.4 kWh). Rare extreme strikes reach tens of MJ.
- Delivery is the second obstacle: 10 to 30 kA peaks with microsecond rise times overwhelm capacitor banks and converters. A 2007 commercial attempt (Alternative Energy Holdings) collected nothing usable.

## How often

| Location | Lightning rate |
|---|---|
| Hunga Tonga eruption, Jan 2022 (volcanic island) | Just over 192,000 flashes, peaking at 2,615 per minute |
| Previous storm record | 993 flashes per minute in a thunderstorm over the southern United States in 1999 |
| Ordinary thunderstorm | About one flash per minute at the low end; supercells reach hundreds per minute |
| Lake Maracaibo, Venezuela | ~230 flashes/km²/yr; storms on 140 to 260 nights per year |
| Kifuka, DR Congo | ~200 flashes/km²/yr |
| Bogor, Java (volcanic island) | 300+ thunderstorm days per year historically |
| Central Florida | 20 to 30 flashes/km²/yr; 80 to 100 storm days |

**Volcanic plume limits.** Eruption lightning is enormous but brief (hours to days) and mostly stays inside the plume. Hunga's flashes were the highest ever measured at 20 to 30 km above sea level, far out of reach of a ground wire. Smaller frequently erupting volcanoes such as Sakurajima produce plumes 3 to 5 km tall where near-vent lightning sits closer to the ground and a 300 to 1,000 m wire is plausible. A tropical volcanic island in the Indonesian pattern (Java) gets near-daily thunderstorms independent of eruptions, which makes it the better steady site.

## Yearly output estimate

A storm cell recharges in tens of seconds to minutes, so triggering runs at about one strike every few minutes while a strong cell sits overhead.

- Hotspot site with ~250 storm days: optimistically 2,000 to 5,000 triggers per year.
- At ~1 MJ captured per strike: 0.5 to 1.4 MWh per year.
- Theoretical ceiling with total capture of 5 GJ per flash: 3 to 7 GWh per year (unattainable since most energy dissipates aloft).

For comparison, a single 1 m² solar panel produces 200 to 400 kWh per year and a US household uses about 30 kWh per day. Realistic triggered-lightning harvest equals a few solar panels per launch station.

## Sources

- [USGS: Hunga eruption produced most intense lightning ever recorded](https://www.usgs.gov/news/science-snippet/tongas-hunga-eruption-produced-most-intense-lightning-ever-recorded)
- [AGU press release on Hunga lightning](https://news.agu.org/press-release/tongas-hunga-eruption-produced-the-most-intense-lightning-ever-recorded)
- [Sci.News: Hunga plume lightning rates](https://www.sci.news/othersciences/geoscience/tongas-hunga-volcano-eruption-plume-lightning-12024.html)
- [National Geographic: Record-setting lightning at Hunga](https://www.nationalgeographic.com/premium/article/record-setting-lightning-hunga-volcano-tonga)
- [US Patent 6597559: Lightning rocket](https://patents.justia.com/patent/6597559)
- [Canadian Patent 2205435: Balloon-wire lightning triggering](https://brevets-patents.ic.gc.ca/opic-cipo/cpd/eng/patent/2205435/summary.html)

## Terra readout (soft)

| Piece | Note |
|---|---|
| **Electricity Resistance** | Surviving a strike / arc; not harvest yield |
| **ManaCast 1 GJ** | Full cloud-to-ground flash scale; ground load sees ~0.1–5 MJ typical |
| **Volcanic island** | Tropical storm nights beat eruption plumes for steady harvest; Stardew-style Lightning Rod fantasy exceeds Earth capture |
| **Storage** | Microsecond kA peaks need supercaps / dump loads before batteries or mana stones |
