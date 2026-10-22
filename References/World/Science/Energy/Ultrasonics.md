# Ultrasonics

> **Design loot / Earth physics.** Sound above about 20 kHz. Inspection, imaging, cleaning, welding, drilling hard stone, mist, degassing and quiet signals. Not automatic law.
>
> Base equations, Q, air to tissue loss, Whisper Beam, Stone-Breaker, Sono-Alchemy and echolocation: `Sound.md`. Bands: `Waves.md`. Quiet dryer tone: `QuietBlowDryer.md`. Low end: `Infrasound.md`. Levitation: `AcousticLevitation.md`. Shear and emulsions: `Shear.md`. Cast law: `../../../Runes/Energy.md`, `ManaCast.md`.

## Shared cost law

- **1 MP = 10 J.** Raw MP below is J ÷ 10. Real casters divide by their conversion (`ManaHandPhysics.md` §2).
- **Pay the radiated power plus losses.** Ultrasonic sources are large next to their wavelength. The air they shake carries the energy away instead of bouncing it back. The braking rule (`ManaHandPhysics.md` §10) adds little here. See `Infrasound.md` for where it bites.
- **Air to tissue loses about 1000×** (`Sound.md`). Every body and solid effect below needs **contact or a coupling medium** (water, oil, gel).

## Why go ultrasonic

| Gain | Reason |
|---|---|
| Fine detail | Resolution is about one wavelength. Higher pitch sees smaller things |
| Tight beams and focus | Small wavelength next to the source gives a narrow beam |
| Small swing, high power | Same intensity needs less movement as pitch rises (`Sound.md`) |
| Silent to people | Above about 20 kHz. Dogs, cats, rodents and bats still hear it |
| Cavitation | Strong pressure swings tear bubbles open in liquid |

| Cost | Reason |
|---|---|
| Short range in air | Absorption climbs with pitch |
| Poor entry into bodies through air | Impedance jump (`Sound.md`) |

## Wavelength and detail

| Medium | Frequency | Wavelength | Smallest detail |
|---|---|---|---|
| Air | 20 kHz | 17 mm | about 1 cm |
| Air | 40 kHz | 8.6 mm | about 5 mm |
| Air | 100 kHz | 3.4 mm | about 2 mm |
| Soft tissue | 1 MHz | 1.5 mm | about 1 mm |
| Soft tissue | 10 MHz | 0.15 mm | about 0.1 mm |
| Steel | 1 MHz | 5.9 mm | a few mm |
| Steel | 5 MHz | 1.2 mm | about 1 mm |

## Range in air

Rough absorption at room temperature. Humidity changes it.

| Frequency | Absorption | Loses 20 dB in |
|---|---|---|
| 20 kHz | about 0.5 dB/m | about 40 m |
| 40 kHz | about 1.3 dB/m | about 15 m |
| 100 kHz | about 3.5 dB/m | about 6 m |
| 200 kHz | about 8 dB/m | about 2.5 m |

Echolocation sweet spot stays **40 to 100 kHz** at **5 to 30 m** (`Sound.md`). In water and solids ultrasound travels much farther.

## Who hears it

| Listener | Upper limit |
|---|---|
| Adult human | 15 to 20 kHz |
| Dog | about 45 kHz |
| Cat | about 65 to 80 kHz |
| Rodents | about 90 kHz |
| Bats | up to about 200 kHz. Calls reach about 140 dB at 10 cm |
| Dolphins | about 150 kHz |
| Many moths | hear bat calls and dive away |

Silent to people is not silent. Animal-sense monsters, guard dogs and bat-like scouts hear it.

## Body safety (airborne)

Strong airborne ultrasound above about 110 to 120 dB can bring headaches, nausea, fatigue and ringing in some people. Published exposure limits range from about 110 dB to about 145 dB depending on frequency and source. Contact ultrasound is a different matter: it enters the body fully and can heat or cut tissue.

## Uses

### Inspection and measurement (contact)

| Job | Frequency | Note |
|---|---|---|
| Flaw detection in metal | 1 to 10 MHz | Finds hidden cracks, voids and bad welds about a wavelength across. Oil or water couplant |
| Thickness gauge | 1 to 10 MHz | Wall thickness of pipes, tanks and armor from one side |
| Weld and casting check | 2 to 5 MHz | Porosity and lack of fusion |
| Rangefinding (air) | 40 kHz | 2 cm to a few m |
| Tank level and flow | 40 kHz to MHz | Read a tank from outside |

Roland fit: check blades, castings and rune channels for internal cracks before they fail (`../Metallurgy/RunicBladeChannels.md`). Pulses are milliwatts to watts. Interpretation is the skill gate. No acoustic speed is locked for the magic metals (`Sound.md`).

### Imaging the body (contact)

- 2 to 15 MHz through gel or water. Detail about 0.15 to 1.5 mm.
- Tissue absorbs about 0.5 to 1 dB per cm per MHz. Higher pitch sees finer detail but shallower.
- Shows organs, fluid, bleeding, stones, pregnancy, foreign bodies and bone surfaces. Not behind bone or gas.
- Power is low. Skill is reading the image (Echolocation and Vibration Sense in `Sound.md`).

### Therapy and surgery (contact)

| Use | Intensity | Effect |
|---|---|---|
| Physio heating | 1 to 3 W/cm² | Deep warmth in muscle and joints |
| Focused ablation (HIFU) | 1,000 to 10,000 W/cm² at the focus | Burns a spot deep inside with no cut |
| Stone breaking | Focused shock pulses | Stones and clots. Stone-Breaker in `Sound.md` |

Hostile interior effects meet living resistance (`../Science.md`).

### Liquids

| Job | Frequency | Power | Raw MP |
|---|---|---|---|
| Cleaning bath | 20 to 40 kHz | about 10 to 20 W per liter | 1 to 2 MP/s per liter |
| Emulsify, homogenize | 20 kHz probes | tens to hundreds of W | Pairs with `Shear.md` |
| Degas liquids and metal melts | 20 kHz | tens of W to kW | Fewer bubbles in castings and resin |
| Small even crystals (sugar, salt, drugs) | 20 to 40 kHz | tens of W | Seeds many crystals at once |
| Sono-chemistry | 20 to 40 kHz | tens of W | `Sound.md` Sono-Alchemy |

**Degassing molten metal** cuts porosity in aluminum and other castings. Useful for the forge (`../Metallurgy/MagicPowderMetallurgy.md`, `../Metallurgy/StructuralForge.md`).

### Mist

Droplet size from a vibrating liquid surface falls with frequency.

| Frequency | Droplet size | Use |
|---|---|---|
| 20 kHz | about 55 µm | Coarse spray |
| 40 kHz | about 35 µm | Spray coating, fuel mist |
| 1.7 MHz | about 3 µm | Fog, humidifier, medicine you breathe |

A few tens of watts make a room of fog. Fog screens hide movement and scatter light (`Optics.md`). Cool mist also cools a camp by evaporation.

### Solids

| Job | Frequency and swing | Note |
|---|---|---|
| Plastic welding | 20 to 40 kHz, 20 to 60 µm | Under 1 s per weld. Hundreds of J |
| Thin metal welding | 20 to 40 kHz | Foil, wire and rivets bond cold |
| Ultrasonic drilling | 20 kHz, 15 to 50 µm, abrasive slurry | Clean holes in glass, ceramic and gemstone. Diamond grit cuts diamond |
| Ultrasonic knife | 20 to 40 kHz | Cuts cake, cheese, rubber and cloth without drag |

Roland fit: drill and shape gem seats without cracking the stone (`../Metallurgy/GemInlay.md`).

### Signals and touch

- **Dog whistle.** About 23 to 54 kHz. Commands only animals hear.
- **Whisper Beam.** Modulated ultrasound that becomes audible along a narrow beam (`Sound.md`).
- **Mid-air touch.** Focused 40 kHz pulsed at about 200 Hz feels like a tap on the skin. Mana Hands do this cheaper but ultrasound can be built into a rune device.
- **Covert ping.** A party with sound-sense can talk in 40 kHz chirps people cannot hear. Bats, dogs and some monsters can.

## Potential

- **Flaw Read.** Contact ping that maps cracks inside metal, wood or stone.
- **Body Read.** Contact imaging through water or gel. Bleeding, stones, foreign bodies.
- **Clean Bath.** 1 to 2 MP/s per liter to strip grime from jewelry, tools and blades.
- **Gem Drill.** Hole and seat gems without fracture.
- **Cold Weld.** Seal wire, foil and rivets without a torch.
- **Degas.** Cleaner castings, resin and potion bases.
- **Fog Bank.** Fine mist for cover or cooling.
- **Dog Line.** Commands to trained animals that people cannot hear.

## Open

- Acoustic speeds of mythril, aurium, orihalcum and star steel for Flaw Read.
- Whether a skilled caster can couple ultrasound into a body without gel (a thin mana coupling layer).
