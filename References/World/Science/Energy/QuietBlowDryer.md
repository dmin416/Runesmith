# The Quiet Blow Dryer

> **Design loot.** Not a lock. Fan sizing math: `FanAirflow.md`. Perfectly rigid housing: `../../Materials/MaterialConsiderations.md`. Sound power: `Sound.md`. Cast law: `../../../Runes/Energy.md` (1 mana = 10 J). Silk wrap: `../Biomaterials/BiologicalSilks.md`.

### Short Answer

Heating is the energy hog, not moving the air. A typical blow dryer puts about 95% of its power into heat and only a few watts into the air's actual motion. The best design dries with lots of gentle, dry, warm-ish air instead of blasting heat, and it recaptures heat instead of throwing it into the room.

### Where a Blow Dryer's Energy Goes

| Part | Typical Power | Share |
|---|---|---|
| Heating element | ~1,000 to 1,700 W | ~90 to 95% |
| Fan motor | ~50 to 100 W | ~5% |
| Actual kinetic energy in the air stream | ~5 to 10 W | Under 1% |

- **Heating:** Resistive heating turns nearly 100% of its power into heat, but most of that heat blows past the hair into the room.
- **Air motion:** About 13 to 20 liters of air per second at 20 to 30 m/s carries only a few watts of kinetic energy. The fan's inefficiency costs more than the motion itself.

### Mana Cost (1 mana = 10 J)

| Method | Energy | Mana |
|---|---|---|
| Standard 1,800 W dryer, 1 second | 1,800 J | 180 |
| Standard dryer, 5 minutes | 540,000 J | 54,000 |
| Evaporating 40 g of water with pure heat input | ~90,000 J | ~9,000 |
| Fan only, 30 W, 10 minutes | 18,000 J | 1,800 |
| Absorbent towel wrap first | ~0 | ~0 |

A fledgling mage's 200 mana runs a standard dryer for about one second.

### Why It Can Be Far Cheaper

- **Evaporation doesn't need added heat:** Dry room air pulls water out of hair using heat already in the room. Heat only speeds it up.
- **Dry air matters more than hot air:** Low humidity drives evaporation. Hot humid air dries poorly, while cool dry air dries well.
- **Most dryer heat is wasted:** It blows away into the room instead of into the hair.

### Best Low-Energy Drying Approach

1. **Absorbent wrap first:** A needle worm silk microfiber wrap pulls out most of the water at zero energy cost.
2. **High flow, low heat:** Large volume of gentle air at about 40 to 50°C instead of a hot blast.
3. **Dry the air:** A desiccant cartridge or a cold condensing plate strips moisture so the air keeps absorbing water.
4. **Recapture heat:** A heat pump moves heat instead of making it, cutting heating energy to a third or a quarter. Heat-pump clothes dryers work this way.
5. **Enclose it:** A hood or bonnet that recirculates warm, dried air keeps the heat at the hair instead of losing it to the room.

An enclosed, recirculating, dehumidifying hood can use 5 to 10 times less energy than a handheld dryer.

### Quiet Air-Moving Technology

#### Noise Sources

- **Jet noise:** Turbulence at the nozzle. Rises with roughly the 8th power of outlet speed, so halving outlet speed cuts it dramatically.
- **Blade tone:** The whine from blades passing at a fixed rate.
- **Motor noise and vibration:** Hum and rattle through the housing.

#### Quiet Design

- **Large, slow fan:** A bigger fan spinning slower moves the same air far more quietly than a small fast one.
- **Centrifugal blower:** Backward-curved squirrel-cage blowers are among the quietest for moving steady air.
- **Low outlet speed, wide outlet:** Moves the same volume with far less turbulence.
- **Uneven blade spacing:** Spreads the blade tone so it doesn't form a single whine.
- **Air amplifier nozzle:** Uses a thin fast jet along a curved surface to pull in surrounding room air, multiplying flow with a smaller, quieter fan. Bladeless fans use this.
- **Lined ducts:** Needle worm silk felt or wax-sealed absorbent lining soaks up turbulence noise.
- **Vibration mounts:** Resilin mounts isolate the motor from the housing.
- **Perfectly rigid shell:** The perfectly rigid material doesn't vibrate or resonate, so a housing made from it blocks motor noise and holds heat in (`../../Materials/MaterialConsiderations.md`).

#### Ultrasonic Note

Pushing blade tone above 20 kHz makes it silent to humans, which modern high-speed dryers do. Mustelids and many animals hear well above that, so Agni would hear it. D's echolocation would pick it up too (`Sound.md`).

### Magic vs. Technology

- **Sound is cheap:** A loud dryer only puts out a tiny fraction of a watt as sound. Quieting it with good engineering costs almost nothing.
- **Heat is expensive:** The real mana drain is heating, and a sound shield does nothing about that.
- **Best choice:** Technology for both. Absorbent wrap, gentle dried air, recaptured heat and a large slow blower with lined ducts make a dryer that is quiet and needs only a small fraction of the mana. Magic is better spent on the small heating step than on blocking sound.
