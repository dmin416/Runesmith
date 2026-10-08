# Light Warfare: Escalation, Defense and Sensing

> **Design loot / inspiration.** Not locked law. Escalation feel for when warriors outrun mass projectiles and mages reach for light. Kit notes: `Lasers.md`. Think vs move: `SpeedVsIntellect.md`. Optics physics: `../World/Science/Energy/Optics.md`. Twenty more variables: `LightWarfareVariables.md`. Do not promote rows into live combat law unless a beat needs them.

## Phase 1: Speed Breaks Melee

Normal human reaction time is about 200 ms and nerve signals top out around 120 m/s. As warrior stats climb, they hit three physical walls.

- **Traction.** Acceleration is capped by friction and what the ground can hold. Past a point, warriors shatter stone and skid on dirt. Very fast warriors need claws, magic footing or flight.
- **Air.** Above roughly 340 m/s every limb movement makes a sonic boom. Drag rises with the square of speed and heating becomes a problem past Mach 3.
- **Collisions.** Two bodies meeting at 1 km/s carry artillery-level energy. Melee stops being swordplay and becomes impact physics. Material strength replaces skill as the limit.

Mages thinking faster get subjective time. A mage thinking 1,000x faster experiences a 1 ms bullet flight as a full second. Their limits become casting speed and how fast the spell itself travels.

## Phase 2: The Dodging Threshold

Any projectile with mass can be dodged if its flight time exceeds the target's reaction time plus the time to move one body width.

Example warrior: 10 ms reaction, moves 0.5 m in 5 ms. Anything arriving later than 15 ms gets dodged.

- Fireball at 50 m/s from 50 m: 1 second. Trivial.
- Spell at rifle speed (1,000 m/s) from 50 m: 50 ms. Dodged.
- Same spell from 15 m: 15 ms. Coin flip.

Pushing projectiles faster costs energy with the square of speed, so doubling velocity costs 4x the mana. Lightning is a tempting middle step but it follows conductive paths through air instead of aim.

**The realization point:** once warriors reach reaction times around 10 to 20 ms, every massive projectile fails at normal fighting ranges. Light crosses 100 m in 333 nanoseconds. Dodging after the shot stops existing. Mages likely find it through spells they already use: illusions (light manipulation), fire (thermal glow) and lightning (the flash).

## Phase 3: What Light Combat Looks Like

### Damage types

- **Continuous beam:** heats a spot and must stay on it. A moving target smears the heat across a wide area.
- **Pulsed beam:** dumps energy in nanoseconds. The surface flashes into plasma and drives a shockwave into the material, spalling armor from the inside. Motion doesn't help because there's no dwell time.
- **Cost:** a lethal burn through a human takes roughly tens of kilojoules on a small spot. A rifle bullet carries about 3 kJ. Light is less energy efficient than mass. Mages pay energy for certainty.

### Eyes go first

The eye's lens concentrates incoming light about 100,000x onto the retina. A few milliwatts causes permanent damage. Blinding a warrior at 1 km costs almost nothing compared to burning through him, so the first light wars are blinding wars.

### Range decides everything

- Tracking speed equals target speed divided by distance. A warrior at 300 m/s, 5 m away, crosses about 3,400° per second. At 1 km, it's under 20° per second. Close up, fast warriors outrun the mage's aim. At range, they're easy.
- Mages want distance. Warriors want contact.
- The horizon from eye height is about 4.7 km. From a 100 m tower it's about 36 km. Mages climb towers, hills and the sky.
- Focus depends on aperture. A 10 cm spell aperture can focus visible light to about a 1 cm spot at 1 km. Bigger spell lenses mean tighter beams at longer ranges.
- High power heats the air along the beam path, which defocuses it (thermal blooming). Fog, rain and dust scatter it.
- Light lag matters only at extreme scale. At 300 km against a target moving 10 km/s, the round trip of seeing and firing lets the target shift about 20 m. Leading the target returns.

### Wavelength choices

- **Microwave:** passes smoke and fog, cooks water inside the body, spreads wide unless the aperture is huge. Metal reflects it.
- **Infrared:** invisible, heats well, travels well through air.
- **Visible:** easy to aim, clean in clear air. Glows in smoke and reveals the shooter.
- **Ultraviolet:** air absorbs it within meters. Close range only.
- **X-ray and gamma:** ignore mirrors and most armor and kill cells internally. Soft X-rays die in air within meters. Hard gamma travels farther but is extremely hard to focus.

### Battlefield shape

- Line of sight is the front line. Forests, cities, trenches and tunnels are warrior territory.
- Smoke becomes permanent. Armies move inside obscurant clouds. Carbon smoke absorbs and water mist scatters.
- Armor goes polished and ablative.
- Mage duels resemble modern air combat. Whoever sees first wins. Firing through any dust exposes your position. Stealth means black, cold and silent.
- Mass returns for indirect fire. Warriors lob hypersonic objects over cover and the horizon, which straight beams can't follow.
- Decoys multiply: angled mirrors, false heat sources, illusions.
- The kill chain is detect, aim, fire. Defense attacks whichever step is slowest, usually detection.

## How Light Gets Blocked

1. **Reflection.** Polished metal reflects 90 to 98%. Layered dielectric mirrors reach 99.9% or more at specific wavelengths. The absorbed remainder still heats and dust or scratches become burn-through points. Attackers counter by switching wavelength.
2. **Ablation.** Sacrificial layers boil off. The vapor cloud shields the next layer from the beam. Protection scales with thickness.
3. **Obscurants.** Smoke, mist and dust in the path. Cheap and wide-area.
4. **Heat spreading.** Spinning or vibrating so the beam never sits on one spot. Beats continuous beams, fails against pulses.
5. **Refraction.** A shield shaped like a diverging lens spreads the beam and slashes intensity. A temperature or density gradient bends it away like a mirage. Physically the cleanest magic shield.
6. **Breaking line of sight.** Walls and terrain. Absolute.
7. **Destructive interference.** Requires a phase-perfect matching counterbeam and the energy just redistributes elsewhere. Impractical.

Light beams pass through each other without interacting in air. A laser can't shoot down another laser.

## Laser-Blocking Shades

These exist in real life. Laser safety goggles use **notch filters** that block a narrow color band and pass the rest. Optical density (OD) rates them: OD 5 passes 1/100,000 of the beam and OD 7 passes 1/10,000,000. Blocking a green laser makes the world look magenta-tinted while staying fully visible.

### Limits

- OD is a ratio, not a cap. An OD 7 filter against a 1 MW beam still passes 100 mW, enough to blind. Filter strength must scale with attack power.
- Each blocked wavelength removes a color. Enough notches against a multi-color or tunable attacker produce black glasses. Broadband white light can't be notched at all.
- Absorptive filters heat up and burn through. Reflective filters handle far more power.
- Some dyes bleach at high intensity and turn transparent, the exact opposite of what's needed.
- Glare inside the lens and eye washes out vision near the beam even when most of it is blocked.

### Saturation

Light doesn't fill up a filter. Each wavelength is blocked or passed independently and a blocked laser doesn't reduce other colors getting through. The only failure modes are heat damage, chemical bleaching and glare.

### The better design: optical limiters

Certain materials (reverse saturable absorbers, some fullerene and carbon nanotube suspensions) stay clear at normal brightness and go dark above an intensity threshold within nanoseconds. Placed at a focal point, they darken only the spot where the beam hits and leave the rest of the scene clear. This blocks by intensity, so switching colors doesn't beat it.

### Magic version

Pass any light below a set intensity per point and reflect anything above it. Reflecting instead of absorbing avoids heat. Remaining counters are overwhelming power to destroy the lens, wavelengths outside its coverage such as X-rays, or simply aiming at the body.

### Lasers fired from the wearer's own eyes

The shades must be one-way. Real optical isolators use Faraday rotation in a magnetic field to pass light in one direction and block the return. A magical equivalent passes the outgoing beam while limiting incoming light.

## Sensing While Blind

### Echolocation

- Sound in air moves at 343 m/s. An echo from 10 m returns in 58 ms and from 100 m in 0.58 s.
- Detail depends on wavelength. Bats use high frequencies for millimeter-scale detail. Some blind humans echolocate with tongue clicks.
- Too slow against fast warriors. Anyone moving supersonic outruns their own noise and arrives silently. Clicking also broadcasts your position.

### Seismic sense

- Vibration through rock moves 3,000 to 6,000 m/s, 10 to 15x faster than sound in air.
- Elephants, scorpions and sand vipers hunt this way. A heavy fast warrior pounding stone is a seismic event.
- Best passive sense for ground combat. Useless against fliers.

### Feeling light on skin

- Light pressure is tiny. Full sunlight pushes about 5 micronewtons per square meter and reflected light is far weaker. Pressure sensing is hopeless.
- Skin senses radiant heat, but without lenses there's no image, only "brighter in this direction."
- The fix is turning skin into an eye. Brittle stars grow microlenses on their skeletons, sea urchins use their whole body as a compound eye with spines for shading and octopus skin contains light-sensitive proteins. A body covered in tiny lensed photoreceptors sees in every direction at light speed. Destroying the eyes no longer blinds it.

### Magnetism

- Changes in magnetic and electric fields travel at light speed.
- Earth's field is about 50 microtesla. A human heart produces about 100 picotesla at the chest, roughly 500,000x weaker and the field drops with the cube of distance. Sensing an unarmored body's own magnetism takes extreme sensitivity even at touching range.
- Iron changes the picture. Armor and weapons distort Earth's field, the same way navies detect submarines. An armored warrior is detectable from meters to tens of meters.
- Birds and sea turtles sense magnetism as compass direction, not images.

### Electric field sense

- Bodies carry static charges of hundreds to thousands of volts and shift the local electric field as they move.
- Bumblebees sense flower charges. Sharks sense nanovolt fields in water.
- In air this works at about meter range and passes through non-conductive walls.

## Faster and Stranger Senses

- **Thermal infrared:** bodies glow brightest around 9 to 10 micrometers. Pit vipers see it. Works in total darkness and thin smoke at light speed. Glass and water block it.
- **Radar:** active radio or microwave. Penetrates smoke, fog, rain, foliage and some walls. Reveals the user.
- **Terahertz:** sees through clothing and thin non-metals.
- **Gravity:** changes travel at light speed and nothing shields it. A 100 kg person at 1 m pulls about 7 billionths of a meter per second squared, which lab gravimeters can detect with long averaging. A refined magical gravity sense detects mass through walls, darkness, smoke and illusions. The strongest strategic sense available.
- **Air flow:** fish lateral lines detect displacement waves from moving bodies. Limited to sound speed.
- **Prediction:** nothing physical beats light. The last frontier is time before the event: muscle tension, breathing, weight shift, gaze direction, mana gathering. Fast-thinking mages read the windup. If mana disturbances propagate instantly, mana sense becomes the only sense faster than light and the decisive military asset. It also breaks causality, which opens the door to true precognition.

## The Endgame

1. Warriors outspeed mass, so mages adopt light.
2. Light makes reaction irrelevant, so combat moves to the steps before firing: detection and aim.
3. Defense shifts from dodging to denying the line of sight: smoke, terrain, mirrors and limiters.
4. Ground battles are fought blind inside smoke using seismic, thermal, radar and gravity senses.
5. The side that is hardest to perceive wins. Stealth beats armor.
