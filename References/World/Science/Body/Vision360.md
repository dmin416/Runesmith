# 360-Degree Vision: Human Acuity, Cameras, Lenses, Magic Eyes and the Brain

Hub: `../Science.md`. Mental capacity (N men): `FocusCapacity.md`. Earth brain / LLM anchors: `CrystalMinds.md` Part 1. Fiber stock physics: `../Energy/FiberOptics.md`. Lens / radiance: `../Energy/Optics.md`. Speed / RT / pursuit limits: `SpeedPerception.md`. Crystal holding file: `CrystalMinds.md`. Nav: `Index.md`.

**Owns:** full-sphere optics, Rig A / Band B / Helm C, vision processing cost tables (Parts 8–9). Capacity bands and men-worth spend: `FocusCapacity.md`. Whole-brain neuron / watt anchors: `CrystalMinds.md` Part 1.

## Contents

- Core Rule
- Reference: Human Vision
- Part 1: Camera Counts and Minimum Camera Size
- Part 2: Rig A: Eight-Camera Full-Sphere Stereo Rig
- Part 3: Why Rig A Sends About 55,000 Times More Data Than an Eye
- Part 4: Squeezing the Full Sphere into a Small Visual Angle
- Part 5: Character Options
- Part 6: Band B: Magic Forehead Eye and Lens Headband
- Part 7: Helm C: The Magic Lens Helm
- Part 8: Processing Cost (Order-of-Magnitude Fiction Scaling)
- Part 9: A Man with the Mental Capacity of Ten Men
- Part 10: Practical Limits
- Part 11: Story Hooks
- Sources

### The three gear systems in this file

| Name | Geometry | Status |
|---|---|---|
| **Rig A** | 8 cameras pointed at the corners of a cube; full-sphere stereo | Technology design (Part 2) |
| **Band B** | 8 lenses in a horizontal ring around the head plus a crown lens; feeds the forehead eye | Magic gear (Part 6) |
| **Helm C** | Head-sized magic lens helm with an inner sensing coating | Magic gear, canon helmet (Part 7) |

The solid crystal orb in Part 7.2 is a physics-only alternate and is not canon.

---

## Core Rule

Vision has three separate limits. Raising one never raises the others.

| Limit | Set by | Meaning |
|---|---|---|
| **Capture** | Optics (aperture, lens quality) | The most detail that exists to be seen |
| **Processing** | Eye tier or brain capacity | How much of that detail is turned into usable sight |
| **Attention** | The conscious mind | How much of that sight is actually noticed |

Attention stays near human level unless the mind itself is expanded: about 4 tracked objects (soft estimate) and tens of bits per second of conscious recognition (soft estimate). **Seeing everything is not noticing everything.** No capture or processing tier in this file implies omniscience.

---

## Reference: Human Vision

### Acuity

| Measure | Value |
|---|---|
| Normal acuity | 20/20 (6/6); resolves about 1 arcminute |
| Detail at 1 m / 6 m | About 0.3 mm / 1.75 mm |
| Healthy young adult | Often 20/16 to 20/12 |
| Practical limit | About 20/10 (0.5 arcminute), set by cone spacing and pupil diffraction |
| Foveal cone spacing | About 2.5 micrometers |
| Hyperacuity (line alignment; reference only, not used for tiers) | 5 to 10 arcseconds |
| Legal blindness (US) | 20/200 or worse in the better eye with correction |
| Fovea width | 1 to 2 degrees |
| Acuity 10 / 30 degrees off center | About 20/100 / 20/400 |
| Single-eye field of view | About 160 by 135 degrees (about 5 steradians) |
| Daylight pupil | About 2 to 4 mm |
| Eye focal length / eyeball diameter | About 17 mm / 24 mm |
| Eagle comparison (reference only, not used for tiers) | About 20/5 (soft estimate; figures vary) |

### The aperture floor (applies to every lens in this file)

    angular resolution = 1.22 x wavelength / aperture diameter

| Target | Resolution | Minimum aperture (550 nm green light) |
|---|---|---|
| 20/40 | 2 arcminutes | 1.2 mm |
| 20/20 | 1 arcminute | 2.3 mm |
| 20/12 | 0.6 arcminute | 3.8 mm |
| 20/10 | 0.5 arcminute | 4.6 mm |

No sensor, material or lens style avoids this. The human pupil works at the same limit.

### Pathway and data

Photoreceptors to bipolar cells to retinal ganglion cells, then optic nerve, optic chiasm (half the fibers cross), lateral geniculate nucleus of the thalamus, optic radiations and primary visual cortex (V1) in the occipital lobe. The dorsal stream handles location and motion; the ventral stream handles recognition. The fovea is about 1 percent of the retina but takes roughly half of V1.

| Stage | Count or rate |
|---|---|
| Photoreceptors per eye | About 120 million rods and 6 million cones (126 million) |
| Optic nerve fibers per eye | About 1 million |
| Compression inside the retina | About 100 to 1 |
| Optic nerve data per eye | About 10 megabits per second |
| Both eyes | About 20 megabits per second |
| Conscious recognition | About 40 bits per second (soft estimate; published figures span roughly 10 to 40) |
| Attention | About 4 moving objects tracked at once (soft estimate; studies typically find 3 to 5) |

The eye reaches 20/20 on 10 megabits per second by sending fine detail only from the fovea and moving the fovea 3 or more times per second.

**Unit used throughout:** one **normal eye** = 1 million optic nerve channels (post-retina, already compressed from about 126 million photoreceptors).

---

## Part 1: Camera Counts and Minimum Camera Size

### 1.1 Eye-shaped cameras needed for 360-degree vision

| Goal | Cameras |
|---|---|
| Horizontal ring, peripheral quality | 3 |
| Full sphere, single coverage (tetrahedral) | 4 |
| Full sphere with overlap (cube faces) | 6 |
| **Full sphere, stereo depth everywhere (Rig A)** | **8** |
| Horizontal ring of 2-degree foveal cameras | About 180 |
| Full sphere of 2-degree foveal cameras | About 13,000 by area; about 16,000 gap-free |
| Same, in stereo | About 32,000 |

### 1.2 How small a camera can reach human acuity

| Camera | Size | Best possible acuity |
|---|---|---|
| OmniVision OVM6948 (200 x 200 pixels) | 0.65 x 0.65 x 1.16 mm module | Worse than 20/90 |
| Princeton/UW metasurface camera | 0.5 mm wide | About 20/90 |
| Foveal-only 20/20 camera (2 degrees, 240 x 240 pixels) | 2.3 mm aperture, about 3.5 mm long | 20/20 (grain-of-rice size) |
| Full-field 150-degree 20/20 camera | About 1 cubic centimeter or more | 20/20 |

Sub-millimeter cameras cannot reach 20/20 at any pixel count. Pixel size is no longer the bottleneck (0.5 micrometer pixels ship in 200-megapixel phone sensors); aperture and wide-angle lens quality are.

---

## Part 2: Rig A: Eight-Camera Full-Sphere Stereo Rig

### 2.1 Layout

Eight cameras pointed at the corners of a cube. Every direction is seen by at least two cameras from different positions.

| Requirement | Angle from camera axis |
|---|---|
| Every direction covered once (nearest camera) | 54.7 degrees |
| Every direction covered twice (second-nearest camera) | 70.5 degrees |
| Design field per camera | 150 degrees total (75 degrees from axis) |

- **Baseline:** a rig sphere about 6 to 7 cm across gives neighbor spacing close to human eye spacing (63 mm).
- **Lens consequence:** each lens must hold 20/20 out to 70.5 degrees off axis. Edge sharpness drives the whole lens design.

### 2.2 The edge problem: aperture foreshortening

A flat aperture viewed at an angle shrinks by the cosine of the angle in one direction.

| Angle off axis | Apparent aperture width | Resolution (2.3 mm stop) |
|---|---|---|
| 0 degrees | 100% (2.3 mm) | 1.0 arcminute (20/20) |
| 54.7 degrees | 58% (1.3 mm) | 1.7 arcminutes (about 20/35) |
| 70.5 degrees | 33% (0.77 mm) | 3.0 arcminutes (about 20/60) |

Keeping 20/20 at 70.5 degrees with a fixed flat stop needs a stop about 6.9 mm wide.

### 2.3 Lens styles compared

**A. Conventional fisheye (multi-element glass, flat sensor)**
- **Shape:** large bulging front element, then 8 to 12 smaller elements; a cone narrowing toward the sensor.
- **Method:** bends wide rays onto a flat sensor; field-flattener elements fight the natural image curvature.
- **Weakness:** sharpness and brightness fall off at the edge. Diffraction-limited 150-degree performance at f/1.5 is beyond normal practice.
- **Size for this target:** 1.5 to 3 cm long.

**B. Eye-style (single gradient-index lens, curved sensor)**
- **Shape:** one lens behind a pupil, focusing onto a bowl-shaped sensor; a miniature eyeball.
- **Gradient index:** the human lens rises from about 1.36 to 1.39 at the surface to about 1.40 to 1.43 in the center, correcting aberrations internally.
- **Curved sensor:** matches the natural curved image of a simple lens and removes field flatteners. Commercial curved sensors exist. A curved-sensor prototype with a custom f/1.2 lens outperformed a high-end flat-sensor camera using a 50 mm f/1.2 lens.
- **Weakness:** the pupil still foreshortens at wide angles; each lens must match its sensor curvature.
- **Size:** focal length about 3.4 mm; eyeball about 5 to 6 mm across.

**C. Monocentric ball lens (best fit for full-field 20/20)**
- **Shape:** a glass sphere (low-index core, high-index shell) with every surface sharing one center; a marble.
- **Method:** a ray from 70 degrees off axis passes through the same optics as a ray from straight ahead. Quality is identical in every direction. The image forms on a spherical shell.
- **Reading the curved image:** a curved sensor, a fiber bundle to a flat sensor or an array of relay microcameras behind the ball. Relay cameras each carry their own stop, so foreshortening disappears and 20/20 holds to the edge.
- **Size:** ball about 4.5 mm (index 1.5, 3.4 mm focal length); camera head 7 to 10 mm; 12 to 15 mm with an enlarged central stop.
- **Weakness:** curved image surface is hard to read out; few commercial parts.

**D. Metasurface (flat nano-structured lens)**
- **Shape:** a flat chip of millions of nanoscale pillars.
- **Example:** the Princeton/UW camera, 0.5 mm wide with 1.6 million pillars.
- **Weakness:** a 0.5 mm aperture caps it near 20/90. Strongly chromatic; color and field correction get harder as the aperture grows. Best used as a thin corrector layer.

**E. Compound eye (insect style)**
- Thousands of lenslets with tiny apertures. Matching human acuity would need a dome on the order of meters across. Ruled out for acuity; useful for wide motion detection.

| Style | Shape | Edge sharpness | Parts | Size per camera | Fit for 20/20 to 70.5 degrees |
|---|---|---|---|---|---|
| Fisheye | Cone, bulging front | Poor to fair | 8 to 12 | 1.5 to 3 cm | Weak |
| Eye-style GRIN | Miniature eyeball | Fair | 1 to 2 | 5 to 6 mm | Moderate |
| Monocentric | Marble | Excellent | 2 to 3 shells | 7 to 15 mm | Strong |
| Metasurface | Flat chip | Fair | Very few | 2.3 mm+ needed | Weak today |
| Compound eye | Faceted dome | Very poor | Thousands | Meters | No |

### 2.4 Focus

- **Fixed focus:** a 2.3 mm aperture at 3.4 mm focal length focused at about 8 m keeps 4 m to infinity within 1 arcminute of blur.
- **Close range:** reading distance shifts focus about 0.05 mm, so close work needs adjustment.
- **Eye-like solution:** electrowetting liquid lenses change shape with voltage, refocusing from a few centimeters to infinity in under 20 milliseconds with no moving parts.

### 2.5 Recommended Rig A build

| Element | Choice |
|---|---|
| Main lens | Two-shell monocentric ball |
| Focus | Electrowetting liquid lens layer |
| Image capture | Curved sensor shell (simplest) or relay microcameras (sharpest edges) |
| Camera head | About 1 cm each |
| Full rig | 8 heads on a sphere about 6 to 7 cm across |

### 2.6 Data: brute force (20/20 everywhere)

8 cameras at about 230 megapixels each = about 1.84 gigapixels.

| Frame rate | Bit depth | Raw rate |
|---|---|---|
| 30 fps | 10-bit | About 550 gigabits per second |
| 60 fps | 10-bit | About 1.1 terabits per second |
| 120 fps | 12-bit | About 2.65 terabits per second |

| Compression | Ratio | Rate at 30 fps |
|---|---|---|
| Lossless | 2:1 | About 275 gigabits per second |
| Visually lossless, low latency | 10:1 | About 55 gigabits per second |
| Consumer streaming | 100:1 or more | About 5 gigabits per second |

### 2.7 Data: foveated (copying the eye)

| Component | Spec | Raw rate (10-bit) |
|---|---|---|
| 8 wide cameras | About 2 MP each at 5 arcminutes per pixel, 30 fps | About 4.8 gigabits per second |
| 2 steerable foveal cameras | 240 x 240 pixels, 2 degrees, 20/20, 120 fps | About 0.14 gigabits per second |
| **Total** | About 16 MP | **About 5 gigabits per second** |
| Compressed | Consumer streaming | About 50 to 100 megabits per second |

**Event-based sensors** report only pixels whose brightness changes, like the retina. In mostly static scenes this cuts data one to two more orders of magnitude, near the human optic nerve rate.

| System | Data rate |
|---|---|
| Human, both eyes | About 20 megabits per second |
| Foveated Rig A, compressed | About 50 to 100 megabits per second |
| Foveated Rig A, raw | About 5 gigabits per second |
| Brute-force Rig A, raw | About 550 gigabits to 2.65 terabits per second |

---

## Part 3: Why Rig A Sends About 55,000 Times More Data Than an Eye

**Comparison basis:** Rig A raw pixels versus one eye's optic nerve (about 1 million fibers, after the retina has already compressed its 126 million photoreceptors). Against the photoreceptors themselves, Rig A has only about 15x more sample points.

### 3.1 Factor build

| Step | Factor | Running total of samples | Versus 1 million fibers |
|---|---|---|---|
| Eye's own field (5 steradians) sampled at a uniform 1 per arcminute | | About 59 million | 59x |
| Expand the field to the full sphere (12.57 steradians) | x 2.5 | About 149 million | 149x |
| Nyquist sampling (2 per arcminute, 4 per square arcminute) | x 4 | About 594 million | 594x |
| Camera overlap (8 cones covering the sphere about 3.1 times) | x 3.1 | About 1.84 billion | 1,840x |
| Data per sample: 10 bits x 30 fps = 300 bits per second, versus about 10 bits per second per fiber | x 30 | | **About 55,000x** |

Overlap note: pure cone geometry gives about 3.0x (about 1.76 billion samples at 220 MP per camera). The 3.1x and 1.84 billion used here include fisheye mapping margin at about 230 MP per camera. All figures in this chain are approximate.

Against both eyes (about 20 megabits per second) the gap is about 27,500x.

**Why the first step is 59x:** the eye's 1 million fibers already cover its whole field. Only the fovea is sampled at 20/20; the periphery pools many receptors per fiber. Rig A samples every direction at foveal density. (This is different from the 13,000 in Part 1.1, which counts fovea-sized camera patches, not samples.)

### 3.2 Why each eye sends so little

- **Foveation:** fine detail only in the center 2 degrees.
- **Retinal compression:** edges and contrast instead of raw brightness.
- **Change detection:** most ganglion cells go nearly quiet for static scenes.
- **Sparse spikes:** a few spikes instead of continuous 10-bit numbers.

### 3.3 Why the cameras send so much

- Every pixel reports full brightness every frame.
- Edge pixels get center resolution.
- Overlap sends each scene point about 3 times.
- No processing at the sensor.

Foveation removes most of the 59x density step inside the covered field. The sphere expansion, Nyquist sampling and overlap steps remain unless a design drops them (for example by sampling the periphery coarsely or removing overlap). Event sensors remove most of the 30x repetition step.

---

## Part 4: Squeezing the Full Sphere into a Small Visual Angle

This part is about squeezing all 360 degrees into the angle a screen fills in the viewer's eye. It is not a judgment of display quality: a 4K TV showing normal video is fine. A 4K TV showing the entire sphere at once compresses the world about 11x.

    compression = 360 degrees / screen width in degrees (as seen by the viewer)
    effective acuity = 20/(20 x compression)

| Screen as seen by viewer | Example | Compression | Effective acuity of the world | Pixels needed (2 per arcminute) |
|---|---|---|---|---|
| 32 degrees wide | 65-inch TV at 2.5 m | 11.25x | 20/225 | 3,840 x 1,920 (7.4 MP) |
| 60 degrees wide | Large monitor up close | 6x | 20/120 | 7,200 x 3,600 (26 MP) |
| 100 degrees wide | Home theater front row | 3.6x | 20/72 | 12,000 x 6,000 (72 MP) |
| 120 degrees wide | Practical flat-screen limit | 3x | 20/60 | 14,400 x 7,200 (104 MP) |
| 180 degrees wide | Curved half-dome | 2x | 20/40 | 21,600 x 10,800 (233 MP) |
| 360 degrees wide | Full dome around viewer | 1x | 20/20 | 43,200 x 21,600 (933 MP) |

Map is equirectangular (2:1). At 32 degrees, a 4K screen already carries everything the viewer can resolve; the extra capture is invisible. Flat screens can't pass about 120 degrees without heavy stretching and can't reach 180. With the eyes held still, only the 2-degree fovea is sharp; on the 65-inch TV that patch covers 22.5 degrees of the world.

**1:1 dome:** at 2 m radius, 0.29 mm pixel pitch gives about 594 million pixels, the unique information in the sphere. The flat map's 933 MP is larger because equirectangular layouts stretch the poles.

**Alternatives:** head-tracked display (about 6,000 x 6,000 per eye for 100 degrees at 1 per arcminute); eye-tracked foveated display (a few megapixels per frame). A flat screen also removes stereo depth.

---

## Part 5: Character Options

Per the Core Rule: don't send the brain the whole sphere. A processing layer filters first, then delivers a normal-sized feed plus alerts.

| Option | How it works | Data to brain | Drawback |
|---|---|---|---|
| 1. Foveated sphere with alerts (recommended) | Rig A layout at low resolution plus 2 steerable 20/20 foveal cameras; processor flags motion, faces, weapons | About normal | Only 2 directions sharp at once |
| 2. Squeezed sphere | 360 x 180 compressed into the normal field; 2.25x squeeze gives about 20/45 | Unchanged | Distortion for weeks; weaker depth |
| 3. Prey-animal vision | Sensors on the sides of the head | Normal | Low detail; depth only in a narrow forward strip |
| 4. Motion-only rear sense | Rear sensors send only change events | Kilobits to a few megabits per second | A still enemy is invisible |
| 5. Four foveas | 4 steerable sharp cameras matching the attention limit | About double | Needs neural augmentation; headaches |
| 6. Recall buffer | Last 30 to 60 seconds stored at full resolution | Normal plus replays | Reaction comes after the moment |
| 7. Expanded visual cortex | Added brain tissue or coprocessor | Several times normal | Calories, heat, migraines |

**Best combination:** Option 1 for daily sight, Option 4 for rear awareness and Option 6 for replay. Each works as cyberware, mutation or enchantment.

---

## Part 6: Band B: Magic Forehead Eye and Lens Headband

### 6.1 Concept

A single magic eye on the forehead receives the combined view of a headband ring of lenses through magic fiber optics.

| Layer | Core Rule limit | Upgrade path |
|---|---|---|
| Headband lenses | Capture | Better or larger lenses |
| Magic fiber optics | None (lossless transmission) | None needed |
| Magic forehead eye | Processing | Eye tiers |
| His mind | Attention | Only by expanding the mind (Part 9) |

### 6.2 Band B geometry

- **8 lenses spaced 45 degrees apart** in a horizontal ring; neighbors about 6.9 cm apart (human eye spacing is 6.3 cm).
- Each lens covers 150 degrees, so every horizontal direction is seen by 3 to 4 lenses.
- **Crown lens:** the ring misses straight up beyond 75 degrees above the horizon; a ninth lens on the crown closes it.
- **Below:** the body blocks most of the downward view; no lens is placed there.
- **Lens grade** follows the aperture floor (Reference): 1.2 mm for 20/40, 2.3 mm for 20/20, 3.8 mm for 20/12, 4.6 mm for 20/10.

### 6.3 Magic fiber optics

Mundane fused-silica bend / loss / cable types: `../Energy/FiberOptics.md`. Lens and radiance background: `../Energy/Optics.md`. Band B strands are magic lossless carriers; they are not Earth fiber stock.

- Each strand carries its lens's full image without loss. Mundane imaging bundles would need about 230 million fibers per lens for 20/20, a bundle about 6 cm thick.
- A cut strand blinds that lens's sector until repaired.

### 6.4 Eye tiers

**Derivation:** the unique sphere holds about 149 million samples at 1 per arcminute and about 594 million at Nyquist (2 per arcminute). This file uses Nyquist, so 20/20 everywhere = about **600 normal eyes**. Every other tier follows:

    load (normal eyes) = 600 x (20/X)^2   for whole-sphere acuity 20/X

| Tier | Whole-sphere acuity | Load | What he experiences |
|---|---|---|---|
| 0 | 20/400 | 1.5 | Shapes and motion all around |
| 1 | 20/200 | 6 | Tells a person from an animal behind him |
| 2 | 20/100 | 24 | Recognizes known faces at a few meters |
| 3 | 20/60 | 66 | Reads large signs in any direction |
| 4 | 20/40 | 150 | Driving-grade sight everywhere |
| 5 | 20/20 | 600 | Normal sharp vision in every direction |
| 6 | 20/10 | 2,400 | Beyond human limit; needs 4.6 mm lenses |

### 6.5 Stereo rule

Overlapping lenses already capture two or more views of every direction. Depth costs processing (fusing the views), not capture.

| Depth mode | Cost |
|---|---|
| Coarse depth from overlap and head motion | Free; included in every tier |
| Depth at the focus spot | Doubles the spot's cost (usually small) |
| **Full stereo:** depth at tier acuity across the whole sphere | x 2 load |

### 6.6 Focus spot

The eye can concentrate on a spot at full lens quality on top of its tier. Cost:

    spot load = (full-sphere load at lens acuity) x (spot area in square degrees / 41,253)

| Spot | Lens acuity | Cost |
|---|---|---|
| 2 degrees wide | 20/20 (Band B) | About 0.05 normal eyes (trivial) |
| 2 degrees wide | 20/1 (Helm C) | About 18 normal eyes |
| Spot affordable on 6 eyes | 20/1 (Helm C) | About 1.15 degrees wide |

Up to about 4 spots at once (attention limit).

### 6.7 Weaknesses

- Mud, rain, a hat or a cut strand blinds a sector. Enemies who understand the band will target it.
- Without the band: one forehead eye with no depth perception.

---

## Part 7: Helm C: The Magic Lens Helm

### 7.1 Why magic is required (real-physics background)

**Hollow fishbowl helmet** (30 cm across, 1 cm thick, concentric surfaces):

    power = -(n - 1) x t / (n x R x (R - t)) = -0.16 diopters (n = 1.5)

Weaker than the smallest eyeglass prescription (0.25 diopters). A real shell does nothing optically. Weight: about 3.1 kg acrylic, 6.6 kg glass.

**A real helmet lens cannot focus onto its own wall.** A curved glass surface focuses distant light at n x R / (n - 1) behind it: 3 radii for n = 1.5, exactly 2 radii (the far surface) for n = 2.0, 1 radius only for infinite index. The focus always lands at or past the center, where the head is.

### 7.2 Physics-only alternate (not canon): solid crystal orb

A solid index-2.0 glass sphere worn above the head focuses every direction onto the opposite point of its own surface.

| Property | 15 cm orb |
|---|---|
| Focal length | 7.5 cm |
| f-number | f/0.5 |
| Diffraction resolution | 0.92 arcseconds (air-limited to about 3 on the ground) |
| Weight | About 8.8 kg |
| Sun concentration | About 47,000 suns on a 0.7 mm spot (welding-torch intensity) |
| Depth | None; one viewpoint |

Too heavy, self-burning and without stereo. Discarded in favor of Helm C.

### 7.3 Helm C canon rule

Helm C is head-sized (about 25 cm) with a magical sensing coating on the inside. **The enchantment rule:** for any viewing direction, the helm treats its full projected disk (25 cm) as one clean entrance pupil and delivers that direction's image to the coating, routing light around the head. A thin physical shell cannot do this; the enchantment does. Every direction therefore gets a 25 cm aperture.

### 7.4 Resolution by environment

| Environment | Limit | Acuity | Versus 20/20 |
|---|---|---|---|
| Daytime near the ground | Air shimmer, about 3 arcseconds | About 20/1 | 20x sharper |
| Hot ground or desert | 5 to 10 arcseconds | 20/2 to 20/3 | 6 to 12x |
| Still night air | About 1 arcsecond | About 20/0.3 | 60x |
| Vacuum | Diffraction, 0.55 arcseconds | About 20/0.2 | 110x |

### 7.5 What he can see in daytime (capture limit, every direction)

| Distance | Smallest detail | Example |
|---|---|---|
| 10 m | 0.15 mm | Individual hairs, fine print |
| 100 m | 1.5 mm | Eye color, expressions, lip movement |
| 500 m | 7 mm | Face recognition (20/20 manages about 25 m) |
| 1 km | 1.5 cm | License plates, what someone holds |
| 5 km | 7 cm | Clothing colors, posture, gestures |

Horizon on flat ground at standing height: about 4.8 km. From a height, haze limits view to 20 to 50 km on a clear day. Per the Core Rule, this is what exists to be seen; how much he takes in depends on his tier and focus spots.

### 7.6 Depth

The 25 cm aperture gives views 25 cm apart (4x human spacing) and records ray direction like a light-field camera.

| Distance | Human depth precision | Helm C depth precision |
|---|---|---|
| 100 m | About 15 m | About 0.6 m |
| Maximum depth range | About 650 m | About 17 km |

He can refocus after the fact and see past thin obstacles such as branches or fences.

### 7.7 Night vision

About 1,275x the light of a dark-adapted pupil. Starlight looks like dusk; moonlight like an overcast day. Stars about 7.8 magnitudes fainter than the naked eye (30,000 to 50,000 visible versus about 9,000). Moon craters down to about 2 km; Jupiter's bands and moons; Saturn's rings.

### 7.8 Limits

- **Processing:** full daytime capture is about 240 billion samples (240,000 normal eyes). See Part 8.
- **Sun:** the helm gathers about 49 W of sunlight and focuses it onto the coating.
- **Flashes:** 1,275x more light makes flashbangs and muzzle flashes 1,275x harsher unless the coating self-dims.
- **Below:** the body hides most of the view more than about 45 degrees down.

---

## Part 8: Processing Cost (Order-of-Magnitude Fiction Scaling)

**Label:** brains do not scale linearly from channels to cortex grams to food. These tables are game physics for story costs, anchored to real human figures and scaled linearly. Treat every number as an order of magnitude.

### 8.1 Anchors

Whole-brain neuron / watt / bits/s: `CrystalMinds.md` Part 1. Vision-specific rows below feed the tier tables; cortex count matches that file (86 billion whole brain, ~20 W).

| Measure | Value |
|---|---|
| V1 | About 140 million neurons per hemisphere; about 40 V1 neurons per thalamic relay neuron |
| Cerebral cortex | About 16 to 23 billion neurons (16 billion used here) |
| Share of cortex used for vision | About 25 to 35 percent (about 5 billion neurons) |
| Whole brain | About 86 billion neurons, 1.4 kg, 20 W (Earth anchors: CrystalMinds Part 1) |
| Vision's share | About 350 g and 5 W |

### 8.2 Cost of one normal eye

| Resource | Per normal eye |
|---|---|
| Visual cortex neurons | 2.5 billion |
| Tissue | 175 g |
| Power | 2.5 W |
| Food | About 50 kcal per day |
| Incoming data | 10 megabits per second |

### 8.3 Tier costs (single coverage; full stereo doubles)

| Tier | Load | Neurons | Human cortices | Tissue | Power | Food per day | Data in |
|---|---|---|---|---|---|---|---|
| Human vision | 2 | 5 billion | 0.3 | 350 g | 5 W | About 100 kcal | 20 Mbit/s |
| 0 | 1.5 | 3.75 billion | 0.23 | 260 g | 3.75 W | About 77 kcal | 15 Mbit/s |
| 1 | 6 | 15 billion | About 1 | 1.05 kg | 15 W | About 310 kcal | 60 Mbit/s |
| 2 | 24 | 60 billion | About 4 | 4.2 kg | 60 W | About 1,240 kcal | 240 Mbit/s |
| 3 | 66 | 165 billion | About 10 | 11.6 kg | 165 W | About 3,400 kcal | 660 Mbit/s |
| 4 | 150 | 375 billion | About 23 | 26 kg | 375 W | About 7,700 kcal | 1.5 Gbit/s |
| 5 | 600 | 1.5 trillion | About 94 | 105 kg | 1.5 kW | About 31,000 kcal | 6 Gbit/s |
| 6 | 2,400 | 6 trillion | About 375 | 420 kg | 6 kW | About 124,000 kcal | 24 Gbit/s |

**Human cortices** = neurons ÷ 16 billion (one person's whole cerebral cortex). It counts cortex-equivalents, not people. Normal human vision uses about 0.3 of one cortex.

**Thresholds**
- A normal man's visual capacity (2 eyes) covers Tier 0 only. Tier 1 needs 3x his visual capacity.
- Tier 1 needs about one entire human cortex for vision alone.
- Tier 3 needs about ten human cortices: the "ten men" of Part 9.
- Tier 2 adds about 60 percent to a man's daily food. Tier 5 is beyond food and needs mana or another power source.

### 8.4 Helm C full capture

| Condition | Samples | Load | Human cortices | Tissue | Power | Data in |
|---|---|---|---|---|---|---|
| Daytime (20/1) | About 240 billion | About 240,000 | About 37,500 | About 42 tonnes (a loaded semi-truck) | About 600 kW (more than a semi-truck engine) | About 2.4 Tbit/s |
| Still night (20/0.3) | About 2.1 trillion | About 2.1 million | About 330,000 | About 370 tonnes | About 5.3 MW (a large wind turbine) | About 21 Tbit/s |
| Vacuum (20/0.2) | About 7.1 trillion | About 7.1 million | About 1.1 million | About 1,240 tonnes | About 18 MW | About 71 Tbit/s |

Full stereo doubles each row.

**Human cortices** = neurons ÷ 16 billion cortical neurons.

### 8.5 Consequences

- **The magic eye must be the processor.** Above Tier 0 the eye does the work of a visual cortex and hands the mind a summary.
- **Attention never grows** with tiers (Core Rule).
- **Helm C's full capture is permanently out of reach** for one mind. Its practical use is a 20/1 focus spot (Part 6.6) layered on his tier.

---

## Part 9: A Man with the Mental Capacity of Ten Men

**Capacity:** 10× men-worth from `FocusCapacity.md` (spend rules and Multitasking / Parallel Thinking live there). Fiction scaling as in Part 8: ten men ≈ 160 billion cortical neurons; a normal man's visual share (5 billion) ≈ 2 normal eyes. Tables below are vision allocation at that budget, not a second capacity ladder.

### 9.1 Allocation options

| Option | Split | Visual capacity | Everything else |
|---|---|---|---|
| A. Proportional | Normal ratios scaled 10x | 20 normal eyes | 10x memory, reasoning, multitasking |
| B. Vision-heavy | All 9 extra cortices go to sight | About 60 | Normal man |
| C. Balanced | Half the extra to sight | About 31 | About 5.5x normal |
| D. Ten parallel minds | 10 streams, each a normal man | 2 per stream, 20 total | 10 trains of thought |

### 9.2 What each can bear (load as percent of visual capacity)

| Tier | Load | A (20) | B (60) | C (31) |
|---|---|---|---|---|
| 0 (20/400) | 1.5 | 8% | 3% | 5% |
| 1 (20/200) | 6 | 30% | 10% | 19% |
| 1, full stereo | 12 | 60% | 20% | 39% |
| 2 (20/100) | 24 | **120%** | 40% | 77% |
| 2, full stereo | 48 | 240% | 80% | 155% |
| 3 (20/60) | 66 | 330% | **110%** | 213% |
| 4 (20/40) | 150 | 750% | 250% | 484% |
| 5 (20/20) | 600 | 3,000% | 1,000% | 1,935% |

### 9.3 Sustainable ceilings

- **A:** Tier 1 full stereo all day; Tier 2 in short bursts.
- **B:** Tier 2 full stereo all day; Tier 3 in bursts.
- **C:** Tier 2 all day; Tier 1 full stereo with headroom.
- **D:** each mind holds one Band B sector with its own focus spot: **10 sharp 20/20 points at once** with a Tier 1 periphery. Attention scales too: about 40 tracked objects and about 10x a normal man's conscious recognition rate. **This is the real combat upgrade.** Raw acuity helps him see more; ten minds help him notice more.

### 9.4 With Helm C (20/1 focus spots)

Spot sizes assume the whole visual capacity goes to the spot (Part 6.6 formula).

| Option | 20/1 spot |
|---|---|
| A | One spot about 2 degrees wide |
| B | One spot about 3.6 degrees wide |
| D | Up to 10 spots about 0.6 degrees wide, aimed in different directions |

### 9.5 Body cost

| Resource | Normal man | Ten men |
|---|---|---|
| Brain power | 20 W | 200 W |
| Brain food | About 410 kcal per day | About 4,100 kcal per day |
| Total daily food | About 2,000 kcal | About 5,700 kcal |
| Brain mass | 1.4 kg | 14 kg (needs magic housing or a larger skull) |
| Head heat | Normal | Like a 200 W bulb inside the skull |

### 9.6 Overload effects

| Load | Effect |
|---|---|
| 100 to 150% | Headaches, narrowing vision, slowed reactions |
| 150 to 300% | Periphery drops out, nosebleeds, seconds-long bursts only |
| Above 300% | Blackout or seizure |

Bursts work like sprinting: a few seconds of overload followed by recovery.

---

## Part 10: Practical Limits

| Limit | Affects | Detail |
|---|---|---|
| **Latency** | Rig A | Human sight takes roughly 50 to 100 ms to reach V1. A camera pipeline adds up to 33 ms per frame at 30 fps plus processing. Delays much past about 20 ms between head motion and image cause nausea. Magic fiber is instant. |
| **Vestibular mismatch** | Squeezed sphere, Band B, Helm C | When the view does not move as the inner ear expects (a rear view in a forward eye), expect motion sickness. Adaptation takes days to weeks, as with inverting-goggle experiments. |
| **Glare and exposure** | All | A full sphere always contains the sun in daytime. Sun to deep shadow spans far more range than one sensor exposure. Each sector needs its own exposure, which leaves brightness seams between sectors. |
| **Event-sensor color** | Option 4, event Rig A | Most event sensors are monochrome. Color needs a second conventional sensor. |
| **Rain and mud** | Rig A, Band B | A single 2 to 5 mm raindrop covers a 2.3 mm lens completely. Helm C's 25 cm aperture shrugs off droplets with only slight contrast loss. |
| **Rolling shutter** | Rig A | Fast head turns or vibration skew the image. Combat use needs global-shutter sensors. |
| **Chromatic aberration** | Wide lenses | Color fringing is worst at the field edge. Two-glass monocentric lenses correct it; metasurfaces suffer most. |
| **Stitching parallax** | Rig A, Band B | Offset lenses see near objects from different positions, causing seams for anything within a few meters. |

---

## Part 11: Story Hooks

- **Who cuts the fiber:** a single severed strand blinds one Band B sector. A knowing enemy attacks from that side.
- **The sun spot as a tell:** Helm C's coating takes a 49 W focused sunspot. A visible glow or scorch on the inner coating gives away where the sun sits relative to him. The helm's large glass glints like a sniper scope at kilometers.
- **Alert flood:** crowds, markets and chaotic fights overload threat alerts. He sees everyone and notices no one.
- **Food and mana as the tier gate:** Tier 2 means eating 60 percent more. Tier 5 needs a mana source; losing it drops him tiers mid-fight.
- **Bursts with a price:** Tier 3 or a wide 20/1 spot for a few seconds, then nosebleed and recovery.
- **Still enemies:** a motion-only rear sense misses anyone who freezes.
- **Flashbangs:** Helm C's 1,275x light gathering turns a flash into a disabling blow unless the coating self-dims in time.
- **Rain:** Band B goes partly blind in a downpour; Helm C does not.
- **Option D as the real upgrade:** ten parallel minds beat raw acuity. He becomes impossible to flank, not just sharp-eyed.

---

## Sources

### Peer-reviewed or reference

- Retina data rate (Koch et al., Current Biology 2006, via Penn release): https://www.sciencedaily.com/releases/2006/07/060726180933.htm
- V1 neuron count and LGN ratio (Scholarpedia): http://www.scholarpedia.org/article/Area_V1
- Cortical neuron counts and V1 density (PNAS): https://www.pnas.org/doi/10.1073/pnas.1010356107
- Share of cortex used for vision (Current Biology): https://www.sciencedirect.com/science/article/pii/S0960982204009352
- Crystalline lens gradient index (Journal of Modern Optics): https://www.tandfonline.com/doi/abs/10.1080/09500340.2011.565888
- Wide-field monocentric light field camera (CVPR): http://www.computationalimaging.org/wp-content/uploads/2017/04/LFMonocentric.pdf
- Curved CMOS sensor prototype camera (Optica OPN, reporting Optics Express): https://www.optica-opn.org/home/newsroom/2017/june/throwing_a_curve_at_cmos_sensors/
- Metasurface camera (Nature Communications, via Princeton): https://www.princeton.edu/news/2021/12/02/researchers-shrink-camera-size-salt-grain
- Electrowetting variable-focus lens (Optical Review): https://link.springer.com/article/10.1007/s10043-005-0255-z

### Manufacturer

- OmniVision OVM6948: https://www.businesswire.com/news/home/20201116005500/en/OmniVision-and-Almalence-Add-SuperResolution-to-World%E2%80%99s-Smallest-Camera-Module-for-Endoscopic-Medical-Imaging
- Liquid lens autofocus speed (Pixelink): https://www.navitar.com/products/pixelink-cameras/aufofocus-cameras

### Illustrative (news, preprints, patents)

- Conscious visual recognition rate (arXiv preprint): https://arxiv.org/pdf/2503.18804
- Human lens gradient index roadmap (arXiv preprint): https://arxiv.org/pdf/2411.14606
- Monocentric lens designs (patent): https://patents.google.com/patent/WO2014074202A2/en
- Samsung ISOCELL HP5, 0.5 micrometer pixels: https://interestingengineering.com/ces-2026/samsung-smallest-200mp-camera
- OV6948 200 x 200 resolution: https://www.neatorama.com/2023/03/06/Behold-The-World-s-Smallest-Camera/
- Silina curved sensors: https://optics.org/news/12/5/4
- Curve commercial curved sensor: https://petapixel.com/2020/12/14/the-first-commercially-ready-curved-cmos-sensor-has-been-developed/

### Soft estimates used for fiction

Eagle acuity, conscious recognition rate and the 4-object attention limit vary across studies and are used here as round story figures.
