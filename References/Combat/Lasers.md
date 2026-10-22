# Lasers

> **Design loot.** Physics, types, power tables and gas feedstock: `../World/Science/Energy/Optics.md`. Aiming vs speed: `SpeedVsIntellect.md`. Escalation / sensing inspiration (not locked): `LightWarfare.md`, `LightWarfareVariables.md`. Power banks: `../World/Science/Energy/Generators.md`. Flywheel + lossless green crystal (prestige): `../World/Science/Energy/FlywheelApplications.md`. Era baseline: `../World/Tech/Technology.md`.

Directed-light weapons for a steampunk / magitech shop path. Not street baseline kit.

## Core idea

- Light travels about 300,000 km per second. Nothing living can dodge it once it is aimed.
- The weak point is aiming. A fast-thinking operator who can track a superhuman closes that gap.
- Blinding takes far less energy than burning. Against a fast enemy, blinding is the most efficient use of a laser.

## Best overall design

- **Blinding weapon:** Copper vapor laser, green, rapid pulses, aimed by a high-INT / mentalist operator. Pair with a ruby laser for a second color so one filter goggle does not stop both.
- **Damage weapon:** Flowing CO2 + nitrogen + helium laser, water or steam cooled. Most efficient and most powerful steampunk-plausible burner.
- **Power source:** Generators or dynamos feeding banks of capacitors (Leyden-jar style).

## Advantages against fast superhumans

- Cannot be outrun once on target.
- Flash blindness lasts after the beam stops, buying time.
- Invisible beams (infrared) give no warning flash before hitting.
- Even a nearly indestructible target can still be blinded by a cheap, weak visible laser. Only burning or destroying the eyes needs the big burner.

## Toughness vs blinding (key split)

Toughness and sight are separate.

1. **Permanent damage scales with toughness.** If eye tissue is 10× tougher, it takes roughly 10× the power to burn it.
2. **Blinding does not scale with toughness.** Glare and flash blindness happen because the light-sensing chemicals get used up. That is chemistry, not tissue strength. A tougher eye that still sees normally gets dazzled by the same weak beam as anyone else.
3. **The lens still focuses ~100,000×.** Toughness does not change the optics. Without built-in filtering, the light still concentrates.
4. **Holding the beam wins over time.** If tougher tissue does not also shed heat faster, a steady beam keeps building heat until it burns through.

| Toughness | Glare and flash blindness | Instant permanent damage |
|---|---|---|
| Normal (1×) | A few mW | About 0.5 W |
| 10× | Same: a few mW | About 5 W |
| 100× | Same: a few mW | About 50 W |
| 1,000× | Same: a few mW | About 500 W |

### What actually protects against blinding

- **Faster blinking or pupil shrinking:** Reacts before much light gets in. Pulsed lasers still beat this.
- **Faster recovery:** Light-sensing chemicals refill quickly, so flash blindness lasts a split second instead of minutes.
- **Natural eye filters:** Like built-in tinted goggles. Blocks some colors, which is why two laser colors beat it.

## Counters

- **Colored goggles:** A filter can block one laser color. Two colors (green copper vapor + red ruby) beat a single filter.
- **Blinking:** A normal blink takes about a quarter second. A superhuman may blink or squint faster. Pulsed lasers strike faster than any blink.
- **Polished armor or mirrors:** Reflect the beam.
- **Smoke or fog:** Scatter the beam (same air limits as `../World/Science/Energy/Optics.md`).

## Quick effect ladder

| Goal | Prefer | Notes |
|---|---|---|
| Glare / flash blind | Copper vapor (green) | Eye focuses visible light ~100,000×. A few mW; toughness does not help |
| Permanent eye damage | Visible (green best) | About 0.5 W at 1× toughness; scales with tissue toughness |
| Burn flesh / kit | CO2 mix | Hundreds to thousands of watts held on target; IR hits cornea, not retina |
| Military burn | CO2 mix | 50,000 W and up |

Eye sensitivity, lumen notes and full endurance table: `../World/Science/Energy/Optics.md`.
