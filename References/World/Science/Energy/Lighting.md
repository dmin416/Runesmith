# Lighting

Hub: `../Science.md`. Spectrum bands: `Waves.md`. Lasers / laser diodes / cavities / radiance: `Optics.md`, `../../../Combat/Lasers.md`. Mana-stone lamps (market gap): `../../Tech/Technology.md`. Generators / drivers: `Generators.md`. Perfect light-crystal + flywheel runtimes: `FlywheelApplications.md`. Silver reflectors / tarnish: `../Metallurgy/Silver.md`.

Every artificial light works by one of three methods: **heating something until it glows**, **exciting a gas**, or **exciting a solid**.

## Caldris filter

| Band | What exists |
|---|---|
| Street / home baseline | Candles, oil / fat lamps, hearth fire, torches. Magic stones already used as fuel and **light** for those who can afford them (`../../Tech/Technology.md`). Civilian mana-stone lamps as common household stock are still a sellable gap. |
| Magitech / invent | Arc and gas-discharge lamps once dynamos and sealed glass exist. Filament bulbs if tungsten wire and vacuum/inert fill are in reach. |
| Modern invent (prestige / late) | Fluorescent + phosphor, sodium vapor, LEDs, laser-phosphor headlights. Need semiconductor fabs or equivalent magic shortcuts; not street baseline. |

## Key terms

- **Lumens:** Total visible light output.
- **Efficacy (lm/W):** Light produced per unit of power.
- **Color temperature (K):** Warm (~2,700 K, yellowish) to cool (5,000–6,500 K, bluish).
- **CRI (0–100):** How accurately colors appear. Incandescent near 100. Good LEDs 90+.

## Incandescent and halogen

A tungsten filament heated to 2,500–3,000 °C glows across a broad spectrum. Most output is infrared. Only **2–5%** becomes visible light (**10–17 lm/W**). Halogen gas redeposits evaporated tungsten onto the filament, allowing a hotter, longer-lasting filament with a small efficiency gain. Color rendering is excellent.

Steampunk fit: glass bulb, vacuum or inert fill, dynamo or mana-stone power. Heat and short life are the walls.

## Limelight (oxyhydrogen on quicklime)

A block of calcium oxide heated by an oxyhydrogen flame to ~2,500°C. Lime melts near 2,600°C, so it glows hard instead of melting. Gurney found the effect; Drummond put it to survey and theater use in the 1820s ("in the limelight"). With reflectors, surveyors sighted over 100 km.

Caldris fit: flame + lime + mirror is period-plausible spotlight / signal gear once gas handling exists. Cavity and collimator math (why a mirrored tube does not make a laser): `Optics.md`.

## Gas discharge

Plasma in a tube. Needs a ballast or other current limit (plasma has negative resistance).

### Fluorescent tubes

- Low-pressure argon + a few milligrams of mercury; phosphor-coated tube.
- Arc ionizes gas → mercury emits **254 nm UV** → phosphor converts UV to visible.
- Mercury vaporizes at room temperature and puts ~60% of input into one UV line. Argon starts the arc, slows mercury atoms from the walls and protects electrodes.
- Electrons 10,000–20,000 °C; gas near room temperature (non-thermal plasma). Glass stays cool.
- **60–100 lm/W.** Dim in cold (mercury condenses). Mercury toxicity is the Earth phase-out reason; on Terra it is an alchemical / safety cost.

### Sodium vapor

Sodium emits at **589 nm** (near eye peak), so no phosphor is needed. Sodium is solid at room temperature and attacks ordinary glass; lamps need heat and chemical resistance.

| Type | Look | Efficacy | Notes |
|---|---|---|---|
| Low-pressure (LPS) | Deep orange (starts pink from neon) | Up to **200 lm/W** | Nearly monochromatic; CRI ~0. Easy to filter near observatories |
| High-pressure (HPS) | Pinkish gold | **100–150 lm/W** | Ceramic alumina tube; Na-Hg amalgam + xenon; CRI 20–25; grows / street lights |

Rated efficacy overstates night performance for dark-adapted eyes (favor blue-green; see deep orange poorly).

### Other discharge

- **Neon:** Red-orange directly. Other colors use other gases or phosphors.
- **Mercury vapor:** Bluish white. Obsolete on Earth.
- **Metal halide:** Bright white, good color. Stadiums, film, HID headlights. Minutes to warm up.

## LEDs (solid-state)

### How they work

Electrons sit in a **valence band**; free ones in a **conduction band**; a **band gap** between. **N-type** doping adds free electrons; **P-type** creates holes. An LED is a **PN junction**. Forward voltage pushes electrons and holes together; recombination releases a **photon**. Color = band gap.

| Color | Wavelength | Band gap | Forward V | Material |
|---|---|---|---|---|
| Infrared | 850–940 nm | ~1.4 eV | ~1.2–1.5 V | GaAs |
| Red | ~630 nm | ~2.0 eV | ~2.0 V | AlGaInP |
| Green | ~525 nm | ~2.4 eV | ~3.0 V | InGaN |
| Blue | ~450 nm | ~2.8 eV | ~3.0 V | InGaN |
| UV | under 400 nm | over 3.1 eV | 3.5 V+ | AlGaN |

Silicon cannot make efficient LEDs (indirect band gap → heat). Bright **blue** (1990s GaN path) unlocked white LEDs.

### White LEDs

- **Blue + yellow phosphor (YAG:Ce):** most common. Red phosphors warm the tint / raise CRI.
- **RGB chips:** tunable; spectral gaps hurt CRI.
- **Violet + phosphors:** smooth high-CRI spectrum.
- Stokes loss: blue→lower colors wastes ~20–25% as heat.

### Efficiency and heat

- Good white LEDs **150–200+ lm/W** (theory for quality white ~250–350).
- **Efficiency droop** at high current (Auger). High-power fixtures use many chips run gently.
- **Green gap:** green less efficient than blue/red (indium strain).
- Beam carries almost no IR; ~half the power still becomes heat at a tiny chip → heat sink required.
- Fade, not pop: **L70 ~50,000 h** (to 70% output). Cheap bulbs die from heat or driver failure first.

### Structure of a standard 5 mm LED

- Two legs into the plastic dome. One ends in a reflector **cup** (usually cathode); the other in a post.
- Chip (die) ~0.25 mm sits in the cup on conductive silver epoxy.
- Gold bond wire ~25 µm from top pad to the post.
- Clear epoxy or silicone forms the lens.

Current path: anode leg → post → bond wire → top of chip → p-layer → junction → n-layer → silver epoxy / cup → cathode leg. The crystal is the bridge; the wire only touches the top.

**Chip variants:** red/amber on conductive substrates (one wire, current straight down). Blue/white on sapphire (insulating): two top contacts, sideways current, hot-spot risk. High-power often **flip-chip** (solder bumps, no bond wire; better heat).

Wavelength (nm) ≈ 1240 / band gap (eV). Reflector cup redirects side light up. White = blue chip + yellow phosphor (YAG:Ce typical).

### Drivers and packages

Current rises exponentially with voltage (diode law). Roughly ×10 current per ~90–120 mV until series resistance bites. Example: 20 mA at 2.0 V may exceed 50 mA at 2.2 V.

**Thermal runaway:** forward voltage falls ~2 mV/°C. Fixed voltage → more current → more heat. Drive by **current**, not voltage.

- Series resistor: R = (V_supply − V_f) / I. Example: (5 − 2) / 0.020 = 150 Ω.
- Constant-current driver for high-power.

T_junction = T_ambient + (θ_JA × power). Most junctions rated ~125–150°C max. Cheap drivers → 100/120 Hz flicker. Dim via lower current or PWM.

Packages: through-hole indicators; SMD strips/panels; **COB** (many chips, one phosphor); filament-style strips.

### Overload and death

1. **Droop:** high current density → more Auger (non-radiative) recombination; more heat per lumen.
2. **Slow death:** dislocations grow; phosphor shifts white toward blue; encapsulant yellows; electromigration of contacts. Arrhenius rule of thumb: +10°C halves life. Life often **L70** (hours to 70% output).
3. **Sudden death:** bond wire melts open; junction shorts; die cracks; encapsulant expands and tears the wire.

**Pulsed:** peak current can far exceed continuous if duty is low and the chip cools between pulses (PWM, IR remotes). Datasheet example class: 20 mA continuous, 100 mA peak at 10% duty / 0.1 ms pulses.

**Other failures:** reverse voltage (~5 V typical limit); ESD (blue/white/UV fragile); **silver sulfidation** of plated cups/frames (sulfur through silicone → black reflector, dim even with healthy chip; rubber, industrial air, hot springs); silver dendrite shorts in humidity under bias (`Silver.md`).

### Uses beyond room light

Displays / backlights; IR remotes and night vision; UV-C disinfection / UV-A curing; grow lights; vehicle lamps (faster than filament for brake visibility).

## LEDs vs laser diodes

Same PN family; lasers add cavity + population inversion. Below threshold a laser diode behaves as an LED. Combat / steampunk beam weapons: `Optics.md` (ruby, copper vapor, CO2; not diode fabs).

**Laser + phosphor:** blue laser on phosphor → very bright white per area (premium headlights, projectors). Retina risk stays laser-class if the beam escapes; LED light spreads and weakens with distance.

Types (Earth): edge-emitting, VCSEL, superluminescent. Wavelengths: telecom 1310/1550 nm; optical media 780/650/405 nm. Older green pointers: IR pump + frequency doubling to 532 nm.

## Other

- **OLED:** Organic layers across a panel. Screens. Costly / shorter-lived for general lighting.
- **Induction lamps:** Electrodeless fluorescent driven by an external magnetic field. Very long life (60k–100k h).

## Efficacy ladder (quick)

| Source | lm/W (order) | Caldris band |
|---|---|---|
| Candle / oil | ~0.1–1 | Baseline |
| Incandescent | 10–17 | Invent / magitech |
| Limelight | hotspot radiance, not lm/W street | Survey / theater invent |
| Halogen | slightly above incandescent | Invent |
| Fluorescent | 60–100 | Late invent |
| HPS | 100–150 | Late invent |
| LPS | up to 200 | Late invent (bad CRI) |
| White LED | 150–200+ | Prestige invent |
| Mana-stone lamp | narrative; stone economics | Present gap product |

## Open

- Mana-stone lamp efficacy vs stone drain when a beat sells them
- Whether Caldris street lighting stays flame / stone or picks up arc lamps in craft cities
