# Optics

Hub: `../Science.md`. Light bands: `Waves.md`. Room / street light tech: `Lighting.md`. Glass / quartz / clear stocks: `../../Materials/TranslucentMaterials.md`. Fight use: `../../../Combat/Lasers.md`. Escalation inspiration (not locked): `../../../Combat/LightWarfare.md`, `../../../Combat/LightWarfareVariables.md`. Pulsed power: `Generators.md`. Flywheel + light-crystal beams / air ceilings: `FlywheelApplications.md`.

## Water-lens telescope (potential)

Concise gist for Mana Hands / ice-water optics or craft: a single lens only focuses; it does not magnify distant objects usefully on its own. Seeing far things up close needs two water lenses acting as a telescope: a large, gently curved front lens (objective) with a long focal length and a small, tightly curved back lens (eyepiece) with a short focal length. Magnification = f_objective / f_eyepiece.

### Objective lens (front, large)

Using lensmaker's equation for water (n = 1.33) with symmetric curvature, R = 2(n−1)f:

- Focal length: 1 m
- Radius of curvature: ≈ 0.66 m per surface
- Diameter: ≈ 0.5 m (bigger diameter = sharper resolution and more light but more mass to hold steady)
- Edge sag (how much the surface curves relative to flat, using sag ≈ D²/8R): ≈ 4.7 cm rise across that 0.5 m width, a shallow, gentle curve

### Eyepiece lens (back, small)

- Focal length: 0.1 m
- Radius of curvature: ≈ 0.066 m per surface
- Diameter: ≈ 5 cm
- Edge sag: ≈ 4.7 mm, a much tighter curve packed into a smaller width

### Result

That pairing gives 10× magnification (1 m ÷ 0.1 m). Spacing between the two lenses should sit close to f_objective + f_eyepiece ≈ 1.1 m for the image to focus properly.

### Scaling

Want more magnification: shrink the eyepiece's focal length rather than growing the objective, since that ratio drives everything. Want a wider field of view or more light-gathering: grow the objective's diameter; holding its focal length fixed makes the curve proportionally shallower and easier to hold steady.

## Lasers (steampunk-plausible physics)

Laser chips and fiber lasers need modern factories. The types below do not. Combat loadouts and counters: `../../../Combat/Lasers.md`.

### How every laser works

1. **Something that glows:** gas, crystal or metal vapor
2. **Power to make it glow:** electricity, a bright flash or a chemical reaction
3. **Two mirrors:** bounce the light into one tight beam. One mirror leaks a little light out. That leak is the beam.

### Types that fit steampunk / magitech shops

| Laser | Color | Efficiency | Strength | Steampunk fit |
|---|---|---|---|---|
| Ruby crystal | Red (visible) | Under 1% | Strong single pulses, slow to refire | Excellent. First laser ever built (1960). Synthetic ruby existed by 1902. Needs a flash tube and charged capacitors |
| Copper vapor | Green and yellow (visible) | About 1% (best visible gas laser) | Very bright rapid pulses | Very good. Ceramic tube heated to about 1,500°C by high-voltage zaps |
| CO2 + nitrogen + helium | Invisible infrared | 10 to 20% | Highest steady power. Scales to hundreds of thousands of watts | Good. Glass tubes, high voltage, pumps to flow gas |
| Carbon monoxide | Invisible infrared | Can beat CO2 when kept very cold | High | Fair. Needs heavy cooling |
| Nitrogen (runs on plain air) | Ultraviolet (invisible) | Low | Tiny pulses only | Excellent build fit, weak weapon |
| Chemical (hydrogen fluoride) | Invisible infrared | Power comes from chemicals, not electricity | Enormous | Alchemy-style war machine. Toxic fuel |

### Eye sensitivity (visible)

- **In total darkness**, the eye can notice a flash of about 5 to 10 light particles. A single rod cell reacts to just one.
- **Brightness range:** starlight to bright sun is about 100 trillion times. The eye handles this by slowly adjusting, not all at once. At any one moment it only handles a range of about 10,000 times.
- **Most sensitive color:** yellow-green. At that color, 1 watt of light equals 683 lumens, the highest possible (`Waves.md`).

### Why lasers are so dangerous to eyes

The lens focuses incoming light onto a tiny spot on the back of the eye. This concentrates it about **100,000 times**. A 1 milliwatt laser pointer focused this way hits the retina harder than staring straight at the sun.

Lumens are misleading for lasers. A flashlight spreads its lumens over a wide area. A laser packs them into a dot.

| Laser | Lumens |
|---|---|
| 5 mW red pointer | About 0.4 |
| 5 mW green pointer | About 3 to 4 |
| 1 W green laser | About 600 (like a 50-watt household bulb, crushed into one pinpoint) |

Green looks about 5 times brighter than red at the same power. **Best blinder:** copper vapor (green). **Best burner:** CO2 mix.

### What a normal eye can endure (visible light)

| Power | Effect |
|---|---|
| Under 1 mW | Safe for a glance. The blink reflex protects you |
| 1 to 5 mW | Glare. Harm only if stared at |
| 5 to 500 mW | Can cause permanent damage within a blink. Strong flash blindness |
| 500 mW and up | Instant permanent damage. Even reflections off walls can injure |
| Short pulses | A few millionths of a joule in one billionth of a second can tear the retina |
| About 0.5 W glance | Rough permanent-damage mark used in combat notes |
| Burning skin, cloth, wood | Hundreds to thousands of watts held on target |
| Military-scale destruction | 50,000 watts and up |

### Invisible infrared (CO2-class)

Never reaches the retina. It burns the clear front surface of the eye instead. That surface can take roughly **1,000 times** more power than the retina before damage. So CO2 is a weak blinder and a strong burner.

### Limits

- **Heat:** Most power becomes waste heat. Needs cooling. Water jackets, steam systems and flowing gas fit the setting.
- **Air:** Steady beams heat the air, which bends and spreads the beam. Fog, smoke, rain and dust scatter it.
- **Plasma:** Very strong short pulses turn air into glowing plasma, which blocks the beam. Clean air breaks down around 100 billion watts per square centimeter for short pulses. Dusty air breaks down about 100 times easier.

### Power feed

Dynamos or generators charge capacitor banks (Leyden-jar style), then dump into flash tubes or discharge tubes. Generator detail: `Generators.md`.

## Laser gas feedstock (1800s technology)

Collecting the working gases for CO2 and copper-vapor lasers with period chemistry.

### Nitrogen (from air)

- **Burn out the oxygen:** Push air through a tube of red-hot copper. The copper grabs the oxygen. Out comes nearly pure nitrogen with a little argon. Done in the 1890s.
- **Liquid air:** Squeeze air, cool it, let it expand suddenly. Repeat until it turns liquid. Nitrogen boils off first when warmed. Invented 1895.

### Carbon dioxide (easiest)

- **Breweries:** Fermenting beer or wine gives off nearly pure carbon dioxide.
- **Lime kilns:** Baking limestone or chalk releases it.
- **Acid on chalk:** Acid on limestone, chalk or baking soda. Used by 1700s and 1800s soda water makers.
- **Storage:** Squeezed into iron tanks, it turns liquid at room temperature. Sold bottled in the 1880s.

### Helium (hardest)

- **Natural gas wells:** Some hold up to 7 or 8% helium. Chill the gas until everything else turns liquid. Helium stays a gas.
- **Radioactive rocks:** Cleveite and monazite sand trap helium. Crushing and heating them or soaking them in acid releases it. First collected this way in 1895.
- **Air:** Useless. Only about 5 parts per million.
- **Optional:** The first CO2 lasers ran on just carbon dioxide and nitrogen. Helium makes them stronger and faster firing. Without it, use more cooling and faster gas flow.

### Copper vapor laser

- **Copper:** Solid chunks sit inside the tube. The heat turns them to vapor.
- **Neon:** Needed as a helper gas. Comes from the same liquid air process as nitrogen.

### Reusing gas

- Pipe the gas in a loop: laser, cooler, back to laser.
- Carbon dioxide slowly breaks down, so top off with fresh gas over time.
