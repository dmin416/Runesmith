# Optics

Hub: `../Science.md`. Light bands: `Waves.md`. Room / street light tech: `Lighting.md`. Glass / quartz / clear stocks: `../../Materials/TranslucentMaterials.md`. Telecom fiber / fused-silica properties: `FiberOptics.md`. Fight use: `../../../Combat/Lasers.md`. Escalation inspiration (not locked): `../../../Combat/LightWarfare.md`, `../../../Combat/LightWarfareVariables.md`. Pulsed power: `Generators.md`. Flywheel + light-crystal beams / air ceilings: `FlywheelApplications.md`. Mirror metal: `../Metallurgy/Silver.md`. Sheer fabrics / one-way cloth: `../../Materials/SheerMaterials.md`.

Earth-physics anchors below (atmosphere glints, cavities, radiance). Not Terra spell law.

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

## Atmosphere glint (sun in a window from ten miles)

### What the bright spot is

A dusk hillside spark seen while facing away from the sunset is usually the setting sun reflecting off a distant window, not the sun itself. The pink band opposite the sun with blue above is the **Belt of Venus** (backscattered sunset light). A darker blue-gray band under it is often Earth's shadow on the atmosphere.

### Sun to the window

- Distance ~150 million km; light travel ~8.3 minutes.
- At the horizon, air mass ~38 times overhead. **Rayleigh** scatter ∝ 1/λ⁴: blue (450 nm) scatters ~4.4× more than red (650 nm), so the long path goes orange-red.
- **Refraction** bends light down ~0.57° at the horizon (sun width ~0.53°). When the disk appears to touch the horizon, it is already geometrically below it.

### Reflection

- Angle of incidence = angle of reflection. Only a pane at the right tilt sends the beam to the viewer.
- Ordinary glass (n ~1.5) reflects ~4% per surface head-on; double-pane has four surfaces; low-e coatings and grazing angles raise reflectance.
- A flat mirror preserves **radiance**. The glint has sun-surface brightness × glass reflectance.
- Sun spans 0.53°. At 16 km a full solar image would be ~148 m across. A 1–2 m window is smaller, so the whole pane is edge-to-edge sun-bright: like a small hole into the sun's face.

### Crossing ten miles (~16.1 km)

- Travel time ~54 µs.
- Earth curvature drop ≈ d²/(2R) ≈ 20 m at 16.1 km (R = 6,371 km). Refraction cuts hidden height to ~17 m. The window needs hillside elevation.
- Haze (Mie) softens contrast and milks the far shore pink.

### Vertical streak on water

Ripples are tiny mirrors. Facets with the right tilt flash toward the viewer (**glitter path**). At low angle, tilt moves the flash point far along the line of sight but little sideways, so the path stretches vertical (same geometry as sun/moon paths). Calm water keeps it thin. Water (n = 1.33) reflects ~2% head-on and >50% at grazing angles.

### Camera through glass

Interior reflections, smudges, and flare can mark the near pane. The glint core often clips white on the sensor while the water streak keeps the true orange-red.

## Integrating sphere (flashbang in a mirrored ball)

### Short answer

No laser exits a pinhole in a perfectly reflective sphere. The hole glows as a small, uniform point spraying a wide cone.

### What a laser needs

1. **Gain medium** with population inversion.
2. **Stimulated emission** (same wavelength, direction, polarization, phase).
3. **Resonator** that selects one axis (usually two facing mirrors).
4. **Output coupler** (one leaky mirror).

A flashbang is broadband, all-directions, random phase (hot metal powder as a thermal source). A sphere has no preferred axis and no gain. Mirrors only redirect.

### What happens

A reflective cavity with a small port is an **integrating sphere**. After a few bounces, light fills every direction. Rays leave the hole at every exterior angle.

For perfect walls:

- Average bounces before escape ≈ surface area / hole area.
- Mean chord = 4V/S = 4r/3.
- Decay time constant τ = 4V / (c × A_hole).

Example: r = 1 m, hole diameter 1 mm → ~16 million bounces, ~21,000 km path, τ ≈ 71 ms. The flash is milliseconds; the pinhole glows dimmer longer. With perfect walls and no absorbers, all light eventually exits the hole.

### Radiance / étendue limit

Passive optics (mirrors, lenses, holes, tubes) cannot raise radiance above the source. That is conservation of étendue and follows the second law: passive concentration of thermal light hotter than the source would be a free heat pump. A directional beam from random light needs a pumped gain medium.

A small hole in a closed cavity is the textbook **blackbody**. If hot smoke and particles absorb and re-emit many times, the hole spectrum approaches an ideal glow at that temperature (Planck, 1900).

Practical: best dielectric mirrors ~99.999% R still lose a little each bounce. A real flashbang also dumps pressure and hot gas.

## Limelight, tunnels, and searchlights

Limelight as a lamp: `Lighting.md`. Optics here is what cavities and tubes do to its radiance.

### Continuous limelight in a sphere

Light builds until leak power equals input. Interior approaches blackbody at the lime temperature (~2,800 K) and cannot exceed it: the lime absorbs returning light as readily as it emits. Flame needs gas feed and a steam vent.

### Mirrored tunnel on the hole

A ray keeps its angle to the tube axis on every bounce. Light that enters at 60° exits at 60°. Same wide spray as a bare hole.

### Black tunnel (collimator)

Only near-axial rays exit. Angled light hits walls and dies.

- Beam spread ≈ hole diameter / tunnel length (radians).

### Numbers: 1 cm hole, 1 m black tunnel, 2,800 K

- Blackbody exitance σT⁴ ≈ 3.49 MW/m²; radiance ≈ 1.11 MW/m²·sr⁻¹.
- Hole area 7.85×10⁻⁵ m² → power into tunnel ~274 W.
- Étendue ≈ (area)² / (length)² ≈ 6.2×10⁻⁹ m²·sr → beam power ~7 mW (~0.5 mW visible; ~8% of 2,800 K is 380–750 nm).
- Spread ~0.01 rad (~0.6°); ~10 m wide at 1 km.
- The other ~274 W heats the tunnel. Mostly a heater with a faint beam.

A ~5 mW laser pointer at ~1 mrad is ~1 m spot at 1 km, all visible: roughly ~1,000× brighter on target per unit area than this tunnel limelight.

### How searchlights win

Radiance is fixed by the source. Sending more power at a given spread needs a **larger emitting aperture**. A limelight at the focus of a large curved mirror makes the whole mirror face glow at source radiance. Still incoherent mixed light. Only gain makes laser light.

---

## One-Way Mirrors

### What they are

A "one-way mirror" (also two-way mirror, half-silvered mirror, observation glass) is a pane with a partially reflective coating. Common coatings:

- **Thin metal films**: aluminum, silver, chromium, titanium or nickel alloys, a few to tens of nanometers thick. Some light reflects, some passes and some is absorbed by the metal.
- **Dielectric stacks**: alternating layers of high-index and low-index materials (such as TiO₂ and SiO₂). Very little absorption. Reflection is tuned by interference.

Typical observation glass reflects a large share of light and transmits a smaller share. Exact splits vary by product.

### The secret: it is not actually one-way

Passive optical materials obey **reciprocity**: transmittance from side A to side B equals transmittance from B to A. A one-way mirror lets exactly as much light through in each direction.

Reflectance can differ slightly between the two faces when the coating absorbs light (metal on glass looks a bit different from each side), yet transmission never differs.

There is also a thermodynamic reason. If a passive pane let light through only one way, placing it between two rooms at equal temperature would let radiant energy pile up on one side, making one room hotter than the other with no energy input. That violates the second law of thermodynamics.

### How the illusion works: lighting ratio

The effect depends entirely on one side being far brighter than the other. Each viewer sees two things superimposed:

- Light from their own side, reflected by the coating.
- Light from the other side, transmitted through the coating.

**Worked example.** Reflectance R = 0.60, transmittance T = 0.12. The bright room has luminance 100. The dark observation room has luminance 10.

| Viewer | Reflected light seen | Transmitted light seen | Ratio | Result |
|---|---|---|---|---|
| In bright room | 0.60 × 100 = 60 | 0.12 × 10 = 1.2 | 50 : 1 | Sees a mirror |
| In dark room | 0.60 × 10 = 6 | 0.12 × 100 = 12 | 1 : 2 | Sees through |

Installers usually recommend that the observed side be lit at least 8 to 10 times brighter than the observation side. Observation rooms use dim lighting, dark walls and dark clothing, with no screens or lamps visible behind observers.

### Reversal

Switch the lighting and the effect reverses. Buildings with mirrored windows look opaque in the day yet become fully visible from the street at night when interior lights are on. Reflective window film behaves exactly the same way.

### Detecting observation glass

- **The fingernail test is unreliable.** Touching a nail to an ordinary back-silvered mirror shows a gap from the glass thickness, while touching a one-way mirror shows no gap. Front-surface mirrors (used in some decor and optics) also show no gap, so the test produces false alarms.
- **Darken your side.** Cupping hands around the eyes and pressing against the glass removes reflected light, so any lit space behind becomes visible.
- **Light from your side.** A flashlight pressed to the glass can illuminate a space behind it.
- **Mounting.** A mirror recessed into the wall with a space behind it differs from one hung on a solid wall.
- **Knocking.** A hollow cavity behind sounds different from a solid wall, though this is not definitive.

### Uses

- Police interrogation and observation rooms
- **Gesell dome**: an observation dome developed by Arnold Gesell at Yale for watching children's development without disturbing them
- **Teleprompters**: a beam splitter at 45° reflects text toward the presenter while the camera looks through it
- Retail security and casino surveillance
- Smart mirrors with displays behind the glass
- Infinity mirrors (two partial mirrors facing each other)
- Mirrored sunglasses: the wearer's eyes sit in shade, so outsiders see reflection while the wearer sees out

### True one-way optics

Real nonreciprocal devices exist, though none suit windows:

- **Faraday isolators** use magneto-optic materials in a magnetic field plus polarizers. Used in lasers and fiber optics to block back-reflections.
- **Time-modulated or nonlinear devices** break reciprocity under special conditions in research settings.

These handle narrow beams under controlled conditions, not room-sized scenes.

---

