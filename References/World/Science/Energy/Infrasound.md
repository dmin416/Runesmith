# Infrasound

> **Design loot / Earth physics.** Sound below about 20 Hz. Felt more than heard. Travels very far. Hard to make and hard to block. Not automatic law.
>
> Base equations, Q, Anti-Sound and Quickground: `Sound.md`. Bands: `Waves.md`. High end: `Ultrasonics.md`. Pressure effects on bodies: `Gradients.md`. Spin and vortices: `Spin.md`. Vestibular sense: `../Body/AccelerometersGyroscopesVestibular.md`. Cast law: `../../../Runes/Energy.md`, `ManaCast.md`.

## Shared cost law

- **1 MP = 10 J.** Raw MP below is J ÷ 10. Real casters divide by their conversion (`ManaHandPhysics.md` §2).
- **Stopping costs the same as starting** (`ManaHandPhysics.md` §10). This matters here more than for any other sound. See the reactive tax below.

## Basics

| Frequency | Wavelength in air | Note |
|---|---|---|
| 20 Hz | 17 m | Lowest organ notes. Edge of tone |
| 10 Hz | 34 m | Single pulses start to be felt as separate beats |
| 5 Hz | 69 m | Whole-body vibration range |
| 1 Hz | 343 m | Storm and volcano band |
| 0.2 Hz | 1.7 km | Ocean storm hum (microbaroms) |

**Range.** Air absorbs almost none of it. Large blasts and eruptions are heard by instruments around the whole planet. The Krakatoa pressure wave of 1883 circled the Earth several times. Wind and weather layers can duct it farther still.

**Walls do not stop it.** Blocking sound depends on wall mass per wavelength. At 10 Hz almost any wall is thin. Anti-sound works well at low pitch (`Sound.md`). That is the counter.

## Hearing and feeling

Rough human thresholds (vary by about 20 dB between people):

| Frequency | Threshold |
|---|---|
| 32 Hz | about 65 dB |
| 20 Hz | about 80 dB |
| 16 Hz | about 95 dB |
| 10 Hz | about 95 to 100 dB |
| 1 Hz | about 140 dB |

- Below about 20 Hz there is no tone. It feels like pressure in the ears or a throb.
- The body feels vibration about 20 to 40 dB above the hearing threshold.
- Loudness climbs fast near threshold. A small step up feels like a big one.

## Effects

| Level | Effect |
|---|---|
| Near threshold | Unease, pressure, a sense of presence in some people |
| 120 to 140 dB | Ear pressure, fatigue, annoyance. Dizziness or nausea in some |
| About 140 dB | Small temporary hearing loss in higher bands that fades quickly |
| About 140 dB at 40 Hz to about 160 dB at 3 Hz | Ear pain |
| Higher | Chest wall and breathing modulated. Gagging. Rare and huge sources only |

**Myths.** Infrasound does not reliably kill, liquefy organs or make people lose bowel control. The claim that 19 Hz vibrates the eyeball into seeing ghosts is contested. Treat unease as the dependable effect and pain as the ceiling.

## Making it costs volume

A small source next to a long wavelength barely radiates. What sets the level is how much air is moved back and forth (volume swing).

| Target | Radiated power | Volume swing per cycle | Raw MP/s radiated |
|---|---|---|---|
| 120 dB at 10 m, 10 Hz | about 1.2 kW | about 0.75 m³ | about 120 |
| 120 dB at 10 m, 20 Hz | about 1.2 kW | about 0.19 m³ | about 120 |
| 120 dB at 10 m, 5 Hz | about 1.2 kW | about 3 m³ | about 120 |
| 140 dB at 10 m, 10 Hz | about 120 kW | about 7.5 m³ | about 12,000 |

Lower pitch at the same level needs a bigger swing of air. A room-sized breath at 10 times a second makes 120 dB at 10 m.

### Reactive tax

Close to a small source the air mostly sloshes in and out without leaving. Physics returns that energy each cycle. **Under the braking rule a raw Mana Hands source pays to start and stop that slosh every half cycle.**

Extra cost for the 10 Hz, 120 dB at 10 m case:

| Source size (radius) | Air speed at source | Extra cost |
|---|---|---|
| 1 m | about 3.8 m/s | about 4.2 kW (3.5× the radiated power) |
| 3 m | about 0.4 m/s | about 1.4 kW |
| 10 m | about 0.04 m/s | about 0.4 kW |

**Avoid the tax with a resonator.** A tuned cavity or pipe lets the air spring and air mass trade the energy back and forth on their own. Mana only pays radiated power plus losses. The same logic as Q in `Sound.md`.

| Resonator | Pitch |
|---|---|
| 32 ft organ pipe (about 10 m) | about 16 Hz |
| Cellar or cave as a Helmholtz cavity (100 m³, 1 m² opening, 2 m neck) | about 4 Hz |
| Big drum or a gong | 20 to 60 Hz with infrasonic parts |

## Natural sources

| Source | Band | Note |
|---|---|---|
| Elephants | about 14 to 35 Hz | Rumbles carry several km. Also felt through the ground |
| Large whales | about 10 to 40 Hz in water | Hundreds of km through the deep sound channel |
| Tigers | Roar has infrasonic parts | Part of why a roar is felt |
| Ocean storms | about 0.2 Hz | Constant global hum |
| Volcanoes, avalanches, earthquakes, landslides | 0.1 to 20 Hz | Warn before they are seen |
| Meteors and big blasts | 0.1 to 10 Hz | Heard by instruments at continent range |
| Waterfalls, surf, wind over ridges | 1 to 20 Hz | Background floor |
| Large wingbeats | about 1 to 5 Hz | Big flying monsters pulse the air |

## Uses

- **Long Call.** Elephant-style signaling across several km. Receivers need sound or Vibration Sense tuned low (`Sound.md`).
- **Ground Line.** Drive it into the ground for seismic signals. Footsteps of armies, digging under walls and large beasts all show the same way.
- **Early Warning.** Listen for storms, avalanches, eruptions, landslides and big flyers before they arrive.
- **Dread Field.** Low steady infrasound near threshold for unease in a camp or a hall. Weak but hard to place.
- **Resonance Push.** Bridges and towers sway at about 0.1 to 5 Hz. A small push in time with the sway builds it up (resonant logic in `Sound.md`). Soldiers break step on bridges for this reason.
- **Tree Shake.** Mechanical shaking at about 10 to 30 Hz drops nuts and fruit for harvest.
- **Deep Water.** Low pitch in water reaches very far. Signals between boats or to a coast.

## Counters

- Anti-sound is cheap at low pitch (`Sound.md`).
- Distance matters less than usual. Shelter matters little.
- Detection is easy for anyone with low-band sense. The source is large and hard to hide.

## Open

- Whether the braking rule applies to oscillating air at all. `Sound.md` prices sound as radiated power with resonance help. This file applies the rule only to raw, untuned sources.
