# Fiber Optics: How It Works and the Physical Properties of the Glass

Hub: `Optics.md` (lenses, lasers, radiance). Waves / bands: `Waves.md`. Fused silica feedstock context: `../Metallurgy/SilicaSand.md`. Translucent stocks: `../../Materials/TranslucentMaterials.md`. Science root: `../Science.md`.

**Status:** design loot. Earth telecom / fused-silica fiber reference. Not Terra street stock unless a chapter invents a route.

---

## 1. How Fiber Optic Transmission Works

### 1.1 Structure of a fiber

| Layer | Material | Typical diameter | Purpose |
|---|---|---|---|
| Core | Germanium-doped fused silica | 8 to 10 µm (single-mode); 50 or 62.5 µm (multimode) | Carries the light |
| Cladding | Pure or fluorine-doped fused silica | 125 µm | Lower refractive index that confines light to the core |
| Primary coating | Soft UV-cured acrylate | about 190 µm | Cushions the glass against microbending |
| Secondary coating | Hard UV-cured acrylate | 250 µm (200 µm in reduced-diameter fiber) | Abrasion and handling protection |
| Tight buffer (optional) | PVC, nylon or similar polymer | 900 µm | Easier handling in indoor cords |

The core and cladding are one continuous piece of glass. Only their chemistry differs.

### 1.2 Refraction

Light slows down inside a transparent material. The refractive index `n` is the ratio of the speed of light in vacuum to its speed in the material:

```
n = c / v
```

When light crosses a boundary between two materials it bends according to Snell's law:

```
n1 · sin(θ1) = n2 · sin(θ2)
```

Angles are measured from the normal (a line perpendicular to the boundary).

### 1.3 Total internal reflection

When light travels from a higher index material (core, n1) toward a lower index material (cladding, n2) the refracted ray bends away from the normal. Past a certain angle of incidence the refracted ray would need to bend beyond 90°, which is impossible, so 100% of the light reflects back into the core. That threshold is the critical angle:

```
θc = arcsin(n2 / n1)
```

Example with typical single-mode values (n1 = 1.4682, n2 = 1.4629):

```
θc = arcsin(0.99639) ≈ 85.1° from the normal
```

Any ray traveling within about 4.9° of the fiber axis inside the core is trapped. Because the angle window is so narrow the light must be launched almost straight down the fiber.

### 1.4 Numerical aperture and acceptance angle

The numerical aperture (NA) describes the cone of light the fiber can accept from outside:

```
NA = sqrt(n1² − n2²) = sin(θa)
```

| Fiber | Typical NA | Acceptance half-angle in air |
|---|---|---|
| Standard single-mode | 0.12 to 0.14 | about 7° to 8° |
| 50 µm multimode | 0.20 | about 11.5° |
| 62.5 µm multimode | 0.275 | about 16° |
| Plastic optical fiber | 0.5 | about 30° |

### 1.5 Modes (the wave picture)

The zigzag ray model is a simplification. Light actually travels as a set of allowed electromagnetic field patterns called modes. The number of modes depends on the normalized frequency (V-number):

```
V = (2π · a / λ) · NA
```

- `a` is the core radius
- `λ` is the wavelength

If V is below 2.405 only one mode propagates and the fiber is single-mode at that wavelength. The wavelength where V equals 2.405 is the cutoff wavelength. Standard single-mode fiber has a cabled cutoff below 1260 nm so it is single-mode across all telecom bands.

For step-index multimode fiber the mode count is roughly `V² / 2`. A 50 µm core with NA 0.2 at 850 nm has V ≈ 37 which supports several hundred modes.

Part of each mode's field extends a short distance into the cladding as an evanescent field. This is why cladding quality matters and why bends can leak light (Section 4).

### 1.6 Step-index vs graded-index

- **Step-index:** the index changes abruptly at the core/cladding boundary. Used in all standard single-mode fiber.
- **Graded-index:** the core index is highest at the center and falls off roughly parabolically toward the edge. Rays that travel farther from the axis move through lower index glass and therefore travel faster. This lets steep zigzag paths and straight paths arrive at nearly the same time, which greatly reduces modal dispersion. All modern multimode fiber (OM2 to OM5) is graded-index.

### 1.7 Sending and receiving data

| Stage | Hardware | Notes |
|---|---|---|
| Transmitter | VCSEL (850 nm, multimode); DFB or tunable laser (1310/1550 nm, single-mode) | LEDs are used only in older or very low speed links |
| Modulation | On-off keying, PAM4, coherent QAM | Coherent systems encode data in amplitude, phase and polarization |
| Multiplexing | CWDM (20 nm spacing, 18 channels from 1271 to 1611 nm); DWDM (50 or 100 GHz grid, 80 to 96+ channels in the C-band) | Each wavelength carries an independent signal |
| Amplification | Erbium-doped fiber amplifiers (C and L bands); Raman amplification | Boosts light directly without converting to electricity |
| Receiver | PIN photodiode or avalanche photodiode (APD) | Coherent receivers mix the signal with a local laser and use DSP to undo dispersion |

Terrestrial long-haul spans between amplifiers are typically 80 to 100 km. Submarine cables use repeaters every 50 to 80 km.

### 1.8 Speed of light in fiber

With a group index of about 1.468 light travels at roughly 204,000 km/s in solid-core fiber (about 68% of the vacuum speed). That equals about **4.9 µs of latency per kilometer**. Hollow-core fiber guides light mostly through air and cuts that to about 3.3 µs/km.

---

## 2. The Glass: Composition and Manufacturing

### 2.1 Composition

Optical fiber is made from **fused silica** (SiO₂), an amorphous network of silicon-oxygen tetrahedra with no crystal structure. It is far purer than any natural or commercial window glass.

| Dopant | Effect on refractive index | Where used |
|---|---|---|
| Germanium dioxide (GeO₂) | Raises | Core of most fibers |
| Phosphorus pentoxide (P₂O₅) | Raises | Some multimode cores; aids processing |
| Fluorine | Lowers | Cladding of pure-silica-core fiber; trench layers in bend-insensitive fiber |
| Boron trioxide (B₂O₃) | Lowers | Stress rods in polarization-maintaining fiber |

The index difference between core and cladding is tiny:

```
Δ = (n1 − n2) / n1
```

- Single-mode: Δ ≈ 0.35%
- 50 µm multimode: Δ ≈ 1%
- 62.5 µm multimode: Δ ≈ 2%

Impurities are controlled to extreme levels. Transition metals such as iron, copper and chromium are held below about 1 part per billion. Hydroxyl (OH, from water) is held below about 1 ppb in low-water-peak fiber.

### 2.2 Why the glass is so pure

The raw materials are not sand. Silicon tetrachloride (SiCl₄) and germanium tetrachloride (GeCl₄) are purified as liquids by distillation then vaporized and reacted with oxygen at high temperature. Metal impurities have much lower vapor pressures so they get left behind. The resulting soot deposits as ultra-pure glass.

### 2.3 Preform fabrication

| Process | Method |
|---|---|
| MCVD (Modified Chemical Vapor Deposition) | Gases flow inside a rotating silica tube heated from outside; layers deposit on the inner wall; tube is collapsed into a solid rod |
| OVD (Outside Vapor Deposition) | Soot is deposited onto the outside of a rotating target rod; rod is removed; soot body is sintered into clear glass |
| VAD (Vapor Axial Deposition) | Soot grows axially from the end of a seed rod; allows very large preforms |
| PCVD (Plasma Chemical Vapor Deposition) | Microwave plasma drives deposition inside a tube; very precise index profiles for multimode fiber |

### 2.4 Drawing

1. The preform (often 15 cm or more in diameter and over 2 m long) is lowered into a furnace at the top of a draw tower.
2. The tip is heated to about 1900 to 2100 °C until it softens and a gob of glass falls under gravity, pulling a thin strand behind it.
3. A laser micrometer measures the diameter continuously. Draw speed is adjusted to hold the cladding at 125 ± 0.7 µm.
4. Liquid acrylate coatings are applied immediately (before the bare glass touches anything) and cured with UV lamps.
5. The fiber is proof tested and wound onto spools.

Modern draw speeds reach 2,000 to 3,000+ meters per minute. A single large preform yields thousands of kilometers of fiber. The cross-section geometry of the preform is preserved exactly in the finished fiber at a scale reduction of roughly 1,000:1.

### 2.5 Historical progress in transparency

| Year | Milestone |
|---|---|
| 1966 | Charles Kao and George Hockham predict that glass with loss below 20 dB/km would make long-distance optical communication practical |
| 1970 | Corning (Maurer, Keck, Schultz) achieves about 17 dB/km |
| 1979 | About 0.2 dB/km at 1550 nm, near the theoretical limit for silica |
| Present | Standard fiber: 0.17 to 0.20 dB/km; pure-silica-core ultra-low-loss: about 0.15 dB/km; record solid-core: about 0.14 dB/km |
| 2025 | Hollow-core (nested antiresonant) fiber reported below 0.1 dB/km at 1550 nm |

At 0.2 dB/km half the light remains after 15 km.

---

## 3. Optical Properties of the Glass

### 3.1 Refractive index

| Property | Value |
|---|---|
| Pure fused silica index at 1550 nm | about 1.444 |
| Pure fused silica index at 633 nm | about 1.457 |
| Effective group index of standard single-mode fiber at 1550 nm | about 1.468 |
| Thermo-optic coefficient (dn/dT) | about 1 × 10^-5 per °C |

### 3.2 Attenuation by wavelength

| Band | Wavelength range | Typical loss | Common use |
|---|---|---|---|
| 850 nm window | 800 to 900 nm | 2.3 to 3.0 dB/km (multimode) | Short-reach data center links |
| O-band | 1260 to 1360 nm | 0.32 to 0.35 dB/km | Access networks, data center single-mode |
| E-band | 1360 to 1460 nm | 0.28 to 0.31 dB/km in low-water-peak fiber | Contains the water peak at 1383 nm |
| S-band | 1460 to 1530 nm | about 0.22 dB/km | CWDM, some amplified systems |
| C-band | 1530 to 1565 nm | 0.17 to 0.20 dB/km | DWDM long-haul (lowest loss region) |
| L-band | 1565 to 1625 nm | 0.19 to 0.22 dB/km | DWDM expansion |
| U-band | 1625 to 1675 nm | rising | Monitoring (OTDR) |

### 3.3 Loss mechanisms

| Mechanism | Cause | Behavior |
|---|---|---|
| Rayleigh scattering | Microscopic density and composition fluctuations frozen into the glass when it solidifies | Proportional to 1/λ⁴. Dominant loss at short wavelengths. Sets the floor across the C-band |
| Infrared absorption | Vibrations of Si-O bonds | Rises steeply above about 1600 nm |
| Ultraviolet absorption | Electronic transitions in the glass | Significant only in the visible and UV |
| Water (OH) absorption | Hydroxyl ions bonded into the glass | Peak at 1383 nm with smaller peaks at 1240 nm and 950 nm. Eliminated in G.652.D low-water-peak fiber |
| Metal impurities | Fe, Cu, Cr, Ni ions | Broad absorption bands. Negligible in modern fiber |
| Bending losses | Macrobends and microbends | See Section 4 |
| Splice and connector losses | Misalignment, gaps, contamination | See Section 9 |

The C-band has the lowest loss because it sits in the valley between falling Rayleigh scattering and rising infrared absorption.

### 3.4 Dispersion (pulse spreading)

| Type | Cause | Typical value |
|---|---|---|
| Modal dispersion | Different modes travel different path lengths | Multimode only. Limits multimode reach to hundreds of meters at high speed |
| Chromatic (material) dispersion | Refractive index varies with wavelength, so different colors in a pulse travel at different speeds | Combined with waveguide dispersion below |
| Waveguide dispersion | Fraction of light in core vs cladding varies with wavelength | Combined chromatic total: zero near 1310 nm in standard fiber; about 17 ps/(nm·km) at 1550 nm |
| Polarization mode dispersion (PMD) | Slight non-circularity and stress in the core make two polarizations travel at slightly different speeds | Modern fiber: below 0.1 ps/√km. Older fiber can be several times worse |

Dispersion is managed with dispersion-shifted fibers, dispersion-compensating modules or (in modern coherent systems) digital signal processing at the receiver.

### 3.5 Nonlinear effects

Light is concentrated in a very small area (effective area about 80 µm² in standard single-mode fiber) so even milliwatts produce intense fields.

| Effect | Description |
|---|---|
| Self-phase modulation | The pulse's own intensity changes the refractive index (Kerr effect) and distorts its phase |
| Cross-phase modulation | One wavelength channel's intensity distorts the phase of neighboring channels |
| Four-wave mixing | Channels combine to generate new interfering frequencies. Worst in fiber with zero dispersion in the operating band |
| Stimulated Brillouin scattering | Acoustic waves reflect power backward. Threshold of only a few milliwatts for narrow-linewidth lasers |
| Stimulated Raman scattering | Power shifts from shorter to longer wavelengths. Also exploited for Raman amplification |

Large-effective-area fibers (110 to 150 µm²) reduce nonlinear effects on long submarine and terrestrial routes.

### 3.6 Photosensitivity

Germanium-doped glass changes its refractive index when exposed to intense UV light. Writing a periodic pattern into the core creates a **fiber Bragg grating** which reflects one narrow wavelength. Gratings are used as filters, laser mirrors and sensors.

---

## 4. Bending

### 4.1 Two kinds of bending loss

| Type | Scale | Causes |
|---|---|---|
| Macrobending | Visible curves (radius from millimeters to centimeters) | Tight routing in trays, sharp corners, kinks, pinched cables |
| Microbending | Microscopic random deformations of the fiber axis (micrometers) | Coating defects, uneven pressure inside cables, temperature contraction of coatings, rough surfaces pressing on fiber |

### 4.2 Why bends leak light

- **Ray picture:** bending the fiber changes the angle at which light hits the outer wall. On the outside of the bend the angle of incidence drops below the critical angle and light refracts out through the cladding.
- **Wave picture:** a mode's field must travel around the bend as a unit. On the outer side of the bend the evanescent tail in the cladding would need to move faster than light can travel in the cladding glass. That portion detaches and radiates away.

Longer wavelengths have larger mode fields that extend farther into the cladding so **1550 nm and 1625 nm are much more bend-sensitive than 1310 nm**. Technicians test at 1625 nm specifically to reveal bends that would not show up at 1310 nm.

Bend leakage is also used deliberately:
- Clip-on fiber identifiers bend a fiber slightly to detect traffic and direction.
- Bend-based taps can extract a small fraction of light, which is a physical-layer security concern.

### 4.3 Bend-insensitive fiber (ITU-T G.657)

Bend-insensitive designs use a smaller mode field and often a low-index **trench** (a fluorine-doped ring) in the cladding around the core that reflects leaking light back inward.

Maximum macrobend loss (per ITU-T specification):

| Category | Bend radius | Turns | Max loss at 1550 nm | Max loss at 1625 nm |
|---|---|---|---|---|
| G.652.D (standard) | 30 mm | 100 | 0.1 dB at 1625 nm only | 0.1 dB |
| G.657.A1 | 15 mm | 10 | 0.25 dB | 1.0 dB |
| G.657.A1 | 10 mm | 1 | 0.75 dB | 1.5 dB |
| G.657.A2 / B2 | 15 mm | 10 | 0.03 dB | 0.1 dB |
| G.657.A2 / B2 | 10 mm | 1 | 0.1 dB | 0.2 dB |
| G.657.A2 / B2 | 7.5 mm | 1 | 0.5 dB | 1.0 dB |
| G.657.B3 | 10 mm | 1 | 0.03 dB | 0.1 dB |
| G.657.B3 | 7.5 mm | 1 | 0.08 dB | 0.25 dB |
| G.657.B3 | 5 mm | 1 | 0.15 dB | 0.45 dB |

G.657.A fibers are fully compatible with standard G.652.D fiber. G.657.B fibers prioritize bend performance and may not meet every G.652 parameter.

### 4.4 Mechanical bending limits

Optical loss is one limit. Mechanical stress is the other. Bending stretches the outer surface of the glass. The surface strain is:

```
ε = r / R
```

- `r` = glass radius (62.5 µm for standard 125 µm fiber)
- `R` = bend radius

| Bend radius | Surface strain | Consequence |
|---|---|---|
| 50 mm | 0.125% | Safe indefinitely |
| 25 mm | 0.25% | Near the long-term reliability guideline |
| 15 mm | 0.42% | Acceptable for short lengths |
| 10 mm | 0.63% | Acceptable for a few loops over short lengths |
| 7.5 mm | 0.83% | Elevated long-term failure risk |
| 5 mm | 1.25% | Above typical proof-test strain; occasional breaks expected over time |
| 2.5 mm | 2.5% | High probability of fracture over days to months |
| about 1 mm | 5% to 6% | Immediate fracture |

A bend-insensitive fiber can carry light around a 5 mm radius with little loss but that does not mean the glass can survive there for decades. Long-term mechanical reliability is why minimum bend radius rules exist even for bend-insensitive fiber.

Bare fiber can be tied into a loose knot momentarily. Pulling the knot tight snaps it.

### 4.5 Cable bend radius rules (industry practice, e.g. TIA-568)

| Condition | Minimum bend radius |
|---|---|
| Static (installed, no tension) | 10 × cable outer diameter |
| Dynamic (during pulling, under tension) | 20 × cable outer diameter |
| 900 µm tight-buffered or 250 µm fiber in trays | 25 to 30 mm typical for standard fiber; 7.5 to 15 mm for bend-insensitive fiber per manufacturer |

### 4.6 Microbending control

The dual-layer coating is designed specifically against microbending:
- **Primary coating:** very soft (modulus about 1 MPa) to absorb small lateral forces.
- **Secondary coating:** hard (modulus about 1 GPa) to resist abrasion and distribute external loads.

Temperature changes cause microbending because the coatings and cable plastics shrink far more than the glass does in cold weather (Section 6).

---

## 5. Strength and Durability

### 5.1 Mechanical properties of fused silica

| Property | Value |
|---|---|
| Density | 2.20 g/cm³ |
| Young's modulus | about 72 to 73 GPa |
| Shear modulus | about 31 GPa |
| Poisson's ratio | 0.16 to 0.17 |
| Theoretical (flaw-free) strength | about 14 to 20 GPa |
| Measured strength of pristine fiber in liquid nitrogen | about 14 GPa |
| Median tensile strength of coated fiber at room temperature | about 5 to 5.5 GPa (700 to 800 kpsi) |
| Strain at break | about 5% to 7% |
| Mohs hardness | about 6 |
| Behavior | Perfectly elastic until sudden brittle fracture. No plastic yielding |

### 5.2 How strong that is

The cross-section of 125 µm glass is about 1.23 × 10^-8 m². At 5 GPa the breaking load is about **60 N (roughly 6 kg)** for a single fiber thinner than a hair.

Per unit weight silica fiber is several times stronger than high-tensile steel wire (steel wire about 2 GPa at 7.85 g/cm³ versus silica about 5 GPa at 2.2 g/cm³).

### 5.3 Why glass breaks at all: surface flaws

Glass fails from microscopic surface cracks (Griffith flaws). Stress concentrates at the crack tip. A crack only tens of nanometers deep can cut strength by a factor of 10 or more.

- Strength is statistical and follows a Weibull distribution.
- **Longer fiber is weaker on average** because it is more likely to contain a severe flaw somewhere along its length.
- Touching, scratching or dust on bare glass instantly creates flaws. This is why coatings go on before the fiber touches any surface during manufacturing.

### 5.4 Proof testing

Every meter of fiber is stretched under a set load right after manufacture. Any section with a flaw weaker than the proof level breaks and is discarded.

| Proof level | Stress | Strain | Load on 125 µm fiber |
|---|---|---|---|
| Standard | 100 kpsi (0.69 GPa) | about 1% | about 8.5 N |
| High reliability (submarine and some aerospace) | 200 kpsi (1.38 GPa) and higher | about 2% | about 17 N |

### 5.5 Static fatigue (stress corrosion)

Glass under constant stress slowly weakens over time when moisture is present. Water molecules react with the strained Si-O bonds at crack tips and break them, letting cracks grow.

- Rate is governed by the stress corrosion susceptibility parameter `n`, typically about 20 for acrylate-coated fiber.
- A small increase in stress produces a dramatic decrease in lifetime because time-to-failure scales roughly with stress raised to the power of `-n`.
- Common design guideline: long-term applied stress should stay at or below about **one fifth of the proof stress** (about 0.2% strain for 100 kpsi proof-tested fiber) for a 25 to 40 year life. Short-term stress during installation is typically allowed up to about 40% to 60% of proof stress.

### 5.6 Zero-stress aging

Even unstressed fiber slowly loses strength in hot humid conditions as water attacks the glass surface through the coating. Effects are minor in normal conditions. Hermetic (carbon or metal) coatings block moisture for harsh environments.

### 5.7 Compression and crush

Silica is far stronger in compression than tension. Fibers inside cables almost never fail from direct compression. The risk from crushing is bending and microbending of fibers between hard surfaces, which causes optical loss and tensile stress on the outer side of the bend.

### 5.8 Stripped fiber

Once the coating is stripped for splicing or terminating the glass is extremely vulnerable. Any contact causes flaws. That is why splices are covered with heat-shrink protection sleeves containing a steel or ceramic rod.

### 5.9 Service life

Properly installed fiber has a design life of **25 to 40 years** and much fiber installed in the 1980s still works. Most field failures come from mechanical damage to the cable (digging, rodents, vehicles) rather than glass aging.

---

## 6. Thermal Properties

| Property | Value |
|---|---|
| Coefficient of thermal expansion | about 0.55 × 10^-6 per °C (one of the lowest of any material) |
| Thermal conductivity | about 1.38 W/(m·K) |
| Specific heat | about 740 J/(kg·K) |
| Strain point | about 950 to 1070 °C (varies with OH content and grade) |
| Annealing point | about 1040 to 1140 °C |
| Softening point | about 1585 to 1665 °C |
| Draw temperature | about 1900 to 2100 °C |
| Melting point | None in the strict sense. Amorphous glass softens gradually as viscosity drops |

### 6.1 Coating temperature ratings

| Coating | Continuous operating range |
|---|---|
| Standard dual acrylate | −40 to +85 °C |
| High-temperature acrylate | up to about 150 °C |
| Silicone | up to about 200 °C |
| Polyimide | up to about 300 °C |
| Aluminum | up to about 400 °C |
| Gold | up to about 700 °C |
| Carbon (hermetic layer beneath another coating) | Adds moisture and hydrogen resistance rather than heat resistance |

The glass itself survives well above any coating rating. The coating is almost always the temperature limit.

### 6.2 Temperature effects on performance

- **Cold:** coatings and cable plastics contract much more than glass (polymers expand 100 to 200 times more per degree). That squeezes the fiber, causes microbending and raises loss, particularly at 1550 and 1625 nm. Cables are tested by cycling down to −40 °C or lower.
- **Heat:** speeds up stress corrosion and coating aging. Light travel time changes by about 40 ps per km per °C (relevant for precise timing systems).
- **Fiber Bragg gratings** shift about 10 pm per °C at 1550 nm, which is the basis of fiber temperature sensors.

### 6.3 Fire

Glass does not burn. Cable jackets do. Indoor cables carry fire ratings:
- **OFNP** (plenum): low smoke and flame spread for air-handling spaces
- **OFNR** (riser): for vertical shafts between floors
- **LSZH** (low smoke zero halogen): produces no corrosive halogen gas

---

## 7. Environmental and Chemical Behavior

| Factor | Effect | Mitigation |
|---|---|---|
| Water and humidity | Drives stress corrosion; adds OH absorption if it reaches the glass | Coatings; gel or water-swellable tape in cables |
| Hydrogen | Diffuses into glass and absorbs light (peaks near 1240 nm and long-wavelength rise). Can form permanent OH bonds | Hermetic carbon coatings; hydrogen-scavenging gels in submarine cables |
| Ionizing radiation | Creates color centers that darken the glass (radiation-induced attenuation). Ge-doped and P-doped glass are especially sensitive | Pure-silica-core fiber with fluorine-doped cladding for nuclear, space and military use |
| Hydrofluoric acid | Dissolves silica rapidly | Used deliberately to etch fiber for sensors and tapers |
| Strong hot alkalis | Slowly attack silica | Rarely encountered in service |
| Most other chemicals | Fused silica is highly inert | None needed |
| Ultraviolet sunlight | Degrades cable jackets rather than glass | UV-stabilized black jackets for outdoor cable |
| Freezing water in ducts | Ice expansion can crush cables | Water-blocked cable; duct drainage |
| Rodents, insects, sharks | Gnaw or bite cables | Steel tape or glass yarn armor; deep burial |

---

## 8. Electrical and Magnetic Properties

| Property | Value |
|---|---|
| Electrical conductivity | Insulator (volume resistivity of fused silica about 10^18 Ω·cm at room temperature) |
| Dielectric constant | about 3.8 |
| Dielectric strength | Very high |
| Electromagnetic interference | Immune. Light is unaffected by radio, motors or power lines |
| Crosstalk | Essentially none between separate fibers |
| Ground loops and lightning conduction | Not carried by all-dielectric cables |
| Sparking | None, which makes fiber suitable for explosive atmospheres |
| Faraday effect | Small. A magnetic field rotates light polarization, which is used in fiber-optic electric current sensors |

All-dielectric self-supporting (ADSS) cable hangs directly on high-voltage power towers. Optical ground wire (OPGW) places fibers inside the grounding conductor at the top of transmission lines.

---

## 9. Joining and Terminating Fiber

### 9.1 Cleaving

Fiber is cut by scoring the glass with a diamond or tungsten carbide blade then applying tension so a crack propagates straight across. A good cleave produces a mirror-flat end within 0.5° to 1° of perpendicular.

### 9.2 Splicing

| Method | How it works | Typical loss |
|---|---|---|
| Fusion splice | Fibers are aligned (often by core imaging) then melted together with an electric arc | 0.02 to 0.05 dB |
| Mechanical splice | Fibers are butted together in a precision sleeve with index-matching gel | 0.1 to 0.3 dB |

### 9.3 Connectors

| Property | Typical value |
|---|---|
| Insertion loss per mated pair | 0.1 to 0.5 dB |
| Return loss, UPC polish | ≥ 50 dB |
| Return loss, APC polish (8° angled end face) | ≥ 60 to 65 dB |
| Common types | LC, SC, MPO/MTP (multi-fiber), ST and FC (older) |

A flat glass-to-air interface reflects about 4% of the light (Fresnel reflection, about −14.7 dB). Physical contact polishes press the cores together to eliminate the air gap. APC connectors angle the end face so any reflection is directed out of the core.

**Contamination is the leading cause of fiber link problems.** A single dust particle on a 9 µm core can block or scatter a large fraction of the light and can be burned into the end face by high-power lasers. Connectors should be inspected with a fiber microscope and cleaned before every mating.

---

## 10. Cable Construction

| Cable type | Description | Typical use |
|---|---|---|
| Loose tube | 250 µm fibers float in gel-filled or dry tubes with slight excess length, so cable stretch and temperature changes do not strain the glass | Outdoor and long-haul |
| Tight buffered | Each fiber has a 900 µm buffer; no tubes | Indoor, patch cords |
| Ribbon | 12 fibers bonded side by side; enables mass fusion splicing | High-count cables |
| Rollable ribbon | Ribbons bonded intermittently so they roll into a compact bundle | Very high-count data center and backbone cables (thousands of fibers) |
| Armored | Steel tape, steel wire or interlocking metal armor | Direct burial, rodent areas, industrial |
| ADSS | All-dielectric with aramid strength members | Aerial on power lines |
| OPGW | Fibers inside a stainless tube within the steel/aluminum ground wire | Top of high-voltage transmission lines |
| Submarine | Fibers in a steel tube, surrounded by steel wire strength members, copper power conductor and polyethylene insulation; extra steel armor near shore | Undersea links |

### 10.1 Strength members

- **Aramid yarn (Kevlar):** flexible tensile strength for indoor and aerial cables
- **Fiberglass-reinforced plastic (FRP) rods:** stiffness and anti-buckling; dielectric
- **Steel wires or rods:** heavy tensile loads and armor

The strength members take pulling load so the glass does not. Typical maximum installation tension is about 2,700 N (600 lbf) for outside-plant cable and a few hundred newtons for indoor cable.

### 10.2 Submarine cable notes

- Repeaters are powered through the cable's copper conductor at up to about 15 kV DC.
- Deep-sea sections are about 17 to 25 mm in diameter. Armored shore sections can exceed 50 mm.
- Fiber is proof tested at 200 kpsi or higher because repairs require a ship.

---

## 11. Fiber Types Summary

### 11.1 Single-mode

| Standard | Name | Key feature |
|---|---|---|
| G.652.D | Standard single-mode (OS2) | Zero dispersion near 1310 nm; low water peak; the most widely deployed fiber |
| G.653 | Dispersion-shifted | Zero dispersion moved to 1550 nm; suffers from four-wave mixing in DWDM (largely obsolete) |
| G.654.E | Cutoff-shifted, large effective area | Ultra-low loss and low nonlinearity for long-haul and submarine |
| G.655 / G.656 | Non-zero dispersion-shifted | Small controlled dispersion at 1550 nm to suppress four-wave mixing |
| G.657.A / B | Bend-insensitive | Tight routing in homes, buildings and enclosures |

### 11.2 Multimode

| Grade | Core | Bandwidth at 850 nm | 10 Gb/s reach | 100GBASE-SR4 reach |
|---|---|---|---|---|
| OM1 | 62.5 µm | 200 MHz·km | 33 m | Not supported |
| OM2 | 50 µm | 500 MHz·km | 82 m | Not supported |
| OM3 | 50 µm | 2000 MHz·km | 300 m | 70 m |
| OM4 | 50 µm | 4700 MHz·km | 400 m | 100 m |
| OM5 | 50 µm | 4700 MHz·km (plus specified up to 953 nm) | 400 m | 100 m; designed for short-wavelength WDM |

### 11.3 Specialty fiber

| Type | Description |
|---|---|
| Plastic optical fiber (POF) | PMMA core about 1 mm wide; loss in the range of 0.15 dB per meter; cheap and flexible; used in cars and home networks |
| Polarization-maintaining | Stress rods create deliberate birefringence that holds polarization for sensors and lasers |
| Photonic crystal fiber | Pattern of air holes along the length controls guidance; enables unusual dispersion and nonlinear behavior |
| Hollow-core fiber | Light travels mostly in air; about 30% lower latency; very low nonlinearity; now reaching record low loss |
| Multicore fiber | Several cores in one cladding for space-division multiplexing |
| Few-mode fiber | Deliberately carries a small number of modes as separate data channels |
| Doped active fiber | Erbium, ytterbium or thulium doped for amplifiers and fiber lasers |

---

## 12. Safety

- **Invisible light:** telecom wavelengths (1310 and 1550 nm) and 850 nm are invisible or nearly so. A fiber or connector that looks dark may still be carrying hazardous laser power. Never look into a fiber end or connector. Use a power meter or inspection scope with filtering.
- **High-power systems:** amplified DWDM and Raman systems can carry hundreds of milliwatts to watts, enough to burn skin, ignite contamination or damage connectors.
- **Glass slivers:** cleaved fiber scraps are nearly invisible and easily penetrate skin, where they are very difficult to remove. Dispose of scraps in a sealed container. Do not eat or drink in the work area.

---

## 13. Quick Reference Numbers

| Item | Value |
|---|---|
| Cladding diameter | 125 µm |
| Coated fiber diameter | 250 µm (200 µm reduced) |
| Single-mode core / mode field diameter | about 8.2 µm core; 9.2 µm MFD at 1310 nm; 10.4 µm at 1550 nm |
| Multimode core | 50 or 62.5 µm |
| Refractive index | about 1.444 to 1.468 |
| Critical angle (single-mode) | about 85° from normal |
| Loss at 1550 nm | 0.17 to 0.20 dB/km |
| Loss at 1310 nm | 0.32 to 0.35 dB/km |
| Chromatic dispersion at 1550 nm | about 17 ps/(nm·km) |
| Latency | about 4.9 µs/km (solid core); 3.3 µs/km (hollow core) |
| Tensile strength | about 5 GPa (breaking load about 60 N) |
| Proof test | 100 kpsi (about 1% strain) standard |
| Young's modulus | about 72 GPa |
| Density | 2.20 g/cm³ |
| Thermal expansion | 0.55 × 10^-6 per °C |
| Softening point | about 1600 °C |
| Instant-break bend radius | about 1 mm |
| Recommended long-term bend radius (standard fiber) | 25 to 30 mm |
| Cable bend radius | 10 × OD static; 20 × OD under tension |
| Fusion splice loss | 0.02 to 0.05 dB |
| Connector loss | 0.1 to 0.5 dB |
| Design life | 25 to 40+ years |
