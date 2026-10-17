# Sheer Materials, One-Way Viewing, Concealing Garments and Thermal Comfort

> Earth reference / invent loot. Not locked law. Fabrics / hides: `Materials.md`, `TranslucentMaterials.md`. Clothing eras: `../Science/Invent/ClothingTechnology.md`. Breathable waterproof: `PermeationBarriers.md`. Insulation: `InsulationMaterials.md`. Ned silk / biomaterials: `../Science/Biomaterials/BiologicalSilks.md`. Caldris street clothes follow `../Tech/Technology.md`.

Nav: `Index.md`.

## Contents

1. The Physics of Sheer Materials
2. Sheer Fabric Types and Construction
3. A History of Sheer Fabrics
4. One-Way Mirrors
5. One-Way Fabrics, Screens and Veils
6. Concealing Garments in History
7. Heat and Cold Under Covering Garments
8. Sun, UV and Coverage
9. Garments That Conceal and Ventilate at Once
10. Quick Reference Tables
11. Key Formulas

---

## 1. The Physics of Sheer Materials

### 1.1 What "sheer" actually means

A material is sheer when a meaningful share of light passes through it with its direction still intact, so shapes on the far side stay recognizable. Two different quantities get confused here:

- **Total transmittance**: how much light makes it through at all.
- **Direct (specular) transmittance vs diffuse transmittance**: whether the light that makes it through keeps its original direction (image-forming) or gets scrambled (glow without an image).

Frosted glass has high total transmittance yet almost no direct transmittance. It is bright yet not see-through. Chiffon may pass less total light than frosted glass yet a large portion of what passes goes straight through the gaps, so it shows shapes.

Energy is conserved at every surface:

**R + T + A = 1** (reflected + transmitted + absorbed fractions)

### 1.2 The two paths light takes through fabric

1. **Through the gaps (interstices)** between yarns. This light is untouched. It carries the image.
2. **Through the fibers themselves.** Each fiber is a tiny transparent or translucent cylinder. Light refracts and partially reflects at every fiber/air boundary. After crossing dozens of fibers inside a yarn its direction is randomized, so it emerges as diffuse glow.

A third share is absorbed by dyes and pigments. A fourth is scattered back toward the viewer on the lit side, which is the key to privacy effects (Sections 4 and 5).

### 1.3 Openness and cover factor

**Openness factor** is the percentage of fabric area that is open hole. The window shade industry sells it directly:

| Openness | View through | Privacy (daytime) | Glare/heat control |
|---|---|---|---|
| 1% | Low | Highest | Highest |
| 3% | Moderate | High | High |
| 5% | Good | Moderate | Moderate |
| 10% | Very good | Lower | Lower |
| 14% | Excellent | Low | Low |

**Peirce cover factor** for woven fabric: in each direction the fractional cover is roughly yarn diameter divided by yarn spacing.

- Warp cover: c₁ = d₁ / p₁
- Weft cover: c₂ = d₂ / p₂
- Total fractional cover: **C = c₁ + c₂ − c₁c₂**
- Open area: **1 − C = (1 − c₁)(1 − c₂)**

Example: if yarns fill 60% of the width in both directions, C = 0.6 + 0.6 − 0.36 = 0.84. The fabric is 16% open. If yarns fill 80% each way, open area falls to 4%. Small changes in yarn thickness or spacing swing see-through dramatically because the effect multiplies across both directions.

### 1.4 Yarn fineness units

- **Denier**: grams per 9,000 m of yarn or filament.
- **Tex**: grams per 1,000 m. **Decitex (dtex)**: grams per 10,000 m. 1 denier ≈ 1.11 dtex.
- **Cotton count (Ne)**: number of 840-yard hanks per pound. Higher number means finer yarn. This is the inverse of denier logic.
- **Microfiber**: any filament finer than about 1 denier (about 1.1 dtex).

Filament diameter from denier:

**d (µm) ≈ 11.9 × √(denier / ρ)** where ρ is fiber density in g/cm³.

| Example | Density | Approx. diameter |
|---|---|---|
| 1 denier nylon | 1.14 | ~11 µm |
| 1 denier polyester | 1.38 | ~10 µm |
| Single silk filament (bave half) | 1.33 | ~10 to 13 µm |
| 15 denier nylon monofilament (sheer hosiery) | 1.14 | ~43 µm |
| Human hair (for comparison) | n/a | ~50 to 100 µm |

### 1.5 Refractive index and why fibers scatter

At each boundary between two transparent materials, a fraction of light reflects. At normal incidence (Fresnel):

**R = ((n₁ − n₂) / (n₁ + n₂))²**

For a typical fiber (n ≈ 1.55) in air (n = 1.00): R ≈ 4.7% per surface. One fiber has two surfaces. A yarn bundle 50 fibers thick presents about 100 surfaces plus curved geometry that bends light sideways. The result: nearly all light entering a yarn exits scrambled.

Approximate refractive indices (fibers are often birefringent, meaning two values depending on polarization relative to the fiber axis):

| Material | n (parallel to axis) | n (perpendicular) |
|---|---|---|
| Polyester (PET) | ~1.72 | ~1.54 |
| Nylon 6,6 | ~1.58 | ~1.52 |
| Silk | ~1.59 | ~1.54 |
| Cotton | ~1.58 | ~1.53 |
| Wool | ~1.55 | ~1.55 |
| Acrylic | ~1.51 | ~1.51 |
| Polypropylene | ~1.52 | ~1.49 |
| Glass fiber | ~1.52 to 1.55 | same |
| PTFE | ~1.35 | ~1.35 |
| Water | 1.33 | n/a |
| Titanium dioxide (rutile) | ~2.6 to 2.9 | n/a |

Higher birefringence and higher index contrast with the surroundings both increase scattering. Polyester's strong birefringence is one reason it whitens and hides more than its weight suggests.

### 1.6 Why wet fabric turns transparent

When water replaces air between fibers, the index mismatch drops from 1.55 vs 1.00 to 1.55 vs 1.33:

R(water) ≈ ((1.55 − 1.33) / 2.88)² ≈ 0.6% per surface

That is roughly 8 times less reflection per boundary. Scattering collapses and light passes through fibers instead of bouncing around inside them. Three other effects pile on:

- Surface tension pulls wet fabric flat against skin, removing the air gap.
- Water films bridge neighboring fibers, merging many small surfaces into fewer large ones.
- Skin color and shadow now sit directly against the fabric where diffusion has no distance to blur them.

The same index-matching principle makes paper translucent when oil soaks in and makes a grease spot visible on a paper bag.

### 1.7 Distance from the surface: the proximity effect

Diffusing layers blur by an amount proportional to the gap between the layer and the object behind it. A frosted shower door shows a hand pressed against the glass sharply yet turns a person 30 cm back into a vague shape. The same rule applies to fabric:

- Fabric touching the body reveals contours and color.
- Fabric hanging a few centimeters away blurs them heavily.
- Linings, slips and loose drape conceal by adding distance, not only by adding material.

### 1.8 Delustrants and fiber shape

Synthetic fibers come in luster grades set by added titanium dioxide (TiO₂), a pigment with very high refractive index:

| Grade | TiO₂ content (approx.) | Look |
|---|---|---|
| Bright | 0 to 0.1% | Glassy, more transparent |
| Semi-dull | ~0.3% | Most common apparel grade |
| Dull / full dull | ~1 to 2% | Matte, chalky, more opaque |

Cross-section shape matters as well:

- **Round**: most transparent, can look plasticky.
- **Trilobal**: sparkles like silk, scatters more.
- **Hollow**: traps air, scatters strongly, insulates.
- **Microfiber**: more fiber surfaces per gram, so more scattering at equal weight.

### 1.9 Color, darkness and the veiling glow

A sheer lit from the viewer's side scatters light back toward the viewer. That scattered light acts as a bright veil laid over whatever is behind.

- **White or pale sheers** scatter strongly. In daylight from outside they glow and hide the interior.
- **Black or dark sheers** absorb most scattered light. The veiling glow is weak, so objects behind remain visible. This is why dark window screens are easier to see through than bright aluminum ones.
- **Backlighting defeats almost any sheer.** A person standing in front of a bright window in a pale dress becomes a silhouette because light from behind passes straight through the gaps and nothing on the near side competes with it.

### 1.10 Contrast through a sheer layer

If two points behind a fabric have luminances L₁ and L₂, the fabric's direct transmittance is T and the fabric's own scattered glow toward the viewer is L_f:

**Perceived contrast = T(L₁ − L₂) / (T(L₁ + L₂) + 2L_f)**

As L_f grows (bright light on the viewer's side, pale fabric), contrast heads toward zero and the scene vanishes. As L_f drops (dim viewer side, dark fabric), contrast approaches the unobstructed value. Every privacy effect in this document follows from this one relationship.

### 1.11 Viewing angle

Yarns have thickness. Viewed head-on, gaps are fully open. Viewed at an angle, the yarns on one side of each gap shadow it, shrinking the projected opening. Thick, open fabrics lose transparency quickly with angle. Thin, flat fabrics such as organza hold it longer. Sheer curtains look more opaque from a street-level angle than from straight across.

### 1.12 Viewing distance and the eye

The pupil is 2 to 8 mm wide. Typical yarn spacing in a veil or screen is 0.1 to 1 mm.

- **Mesh close to the eye** is badly out of focus. Each point in the scene sends light into the pupil around the threads, so the threads reduce brightness and contrast without blocking the image. This is why a face veil, fencing mask, screen door or beekeeper veil is easy to see out of.
- **Mesh far from the eye** is in focus. The eye resolves around 1 arcminute, about 0.3 mm at 1 m, so the texture becomes visible and interferes with whatever is behind it.

Combined with lighting (1.10), this creates a strong asymmetry: the wearer of a veil sees out easily while a distant observer sees mostly fabric.

### 1.13 Moiré

Two overlapping regular meshes produce moiré bands. For two identical gratings of pitch p rotated by a small angle θ:

**Moiré period P = p / (2 sin(θ/2))**

A tiny rotation creates large, slow-moving bands. Layered sheer curtains and tulle skirts shimmer this way. "Watered" moiré silk is made deliberately by pressing two layers of ribbed silk together under heat so one imprints a crushed pattern on the other.

### 1.14 Wavelengths beyond visible light

- Visible light spans about 380 to 750 nm.
- Many dyes that look black absorb visible light yet transmit near-infrared (750 to 1,400 nm). Thin, dark synthetic fabrics can appear translucent in near-infrared imaging. Swimwear and athletic wear makers sometimes add carbon black or IR-blocking linings for this reason.
- In the thermal infrared (8 to 14 µm) nearly all common fabrics are opaque. Thermal cameras show the temperature of the fabric surface, which runs warmest where fabric touches skin.
- Polyethylene is a notable exception, transparent in the thermal infrared (see 7.10).

---

## 2. Sheer Fabric Types and Construction

### 2.1 Construction methods

- **Plain weave**: simple over/under. Sheer when yarns are fine and spaced apart.
- **Leno (gauze) weave**: pairs of warp yarns twist around each weft, locking open spaces so they cannot slide shut. Stable mesh.
- **Net / bobbinet**: yarns twisted into a hexagonal mesh. True bobbinet is very stable and transparent.
- **Knit (warp knit, weft knit)**: loops instead of interlacing. Tricot, power mesh and hosiery.
- **Lace**: decorative openwork made by needle, bobbin or machine.
- **High-twist (crepe) yarns**: alternating S-twist and Z-twist yarns kink against each other, creating a pebbly texture and irregular gaps.

### 2.2 Fabric glossary

| Fabric | Usual fiber | Construction | Character | Name origin / note |
|---|---|---|---|---|
| Chiffon | Silk, polyester, nylon | Plain weave, crepe yarns | Soft, fluid, slightly rough | French *chiffe*, rag or flimsy cloth |
| Georgette | Silk, polyester | Like chiffon, heavier crepe | Crinkled, springy, more opaque | Often credited to dressmaker Georgette de la Plante |
| Organza | Silk, nylon, polyester filament | Plain weave, tightly twisted filament | Crisp, stiff, shiny | Origin debated, possibly Urgench on the Silk Road |
| Organdy | Cotton | Plain weave, acid or starch finish | Crisp cotton version of organza | |
| Voile | Cotton, polyester | Plain weave, high-twist yarns | Soft, light, matte | French for veil |
| Batiste | Cotton, linen | Fine plain weave, often mercerized | Soft, smooth, semi-sheer | Linked to Baptiste, a weaver of Cambrai |
| Cambric | Linen, cotton | Fine dense plain weave | Smooth, slight sheen | From Cambrai, France |
| Lawn | Linen, cotton | Fine plain weave, crisp finish | Light, slightly stiff | From Laon, France |
| Muslin (fine) | Cotton | Plain weave | Ranges from airy to coarse | Associated with Mosul; finest from Bengal |
| Gauze | Cotton, silk | Leno or loose plain weave | Open, light | Possibly from Gaza |
| Marquisette | Cotton, polyester | Leno weave | Stable open mesh | Curtains, mosquito netting |
| Tulle | Nylon, silk, polyester | Hexagonal net | Light, airy, holds shape | From Tulle, France |
| Bobbinet | Cotton, nylon | Machine hexagonal net | Very transparent, stable | Machine patented by John Heathcoat, 1808 to 1809 |
| Point d'esprit | Nylon, cotton | Tulle with woven dots | Romantic, textured | |
| Mousseline | Silk, wool, cotton | Fine plain weave | Between chiffon and organza | French for muslin |
| Habotai (China silk) | Silk | Light plain weave | Smooth, semi-sheer | Japanese *habutae* |
| Crepe de chine | Silk, polyester | Plain weave, crepe weft | Semi-sheer in light weights | |
| Dotted Swiss | Cotton | Sheer ground with dots | Light, playful | |
| Sheer hosiery | Nylon, spandex | Weft knit | Elastic, translucent | Measured in denier |
| Power mesh | Nylon, spandex | Warp knit | Stretch, firm | Shapewear, athletic panels |
| Sharkstooth scrim | Cotton, polyester | Open leno-like weave | Opaque front-lit, clear back-lit | Theater |

### 2.3 Hosiery denier scale

| Denier | Appearance |
|---|---|
| 5 to 10 | Ultra-sheer, almost invisible |
| 10 to 15 | Sheer |
| 15 to 30 | Semi-sheer |
| 30 to 40 | Semi-opaque |
| 40 to 70 | Opaque |
| 70+ | Thick opaque |

---

## 3. A History of Sheer Fabrics

### 3.1 Ancient Egypt

Elite Egyptians wore extremely fine linen, sometimes called "royal linen." Art from the New Kingdom, especially the Amarna period, shows bodies plainly visible through pleated linen garments. Surviving examples have very high thread counts, achieved with flax spun by hand on drop spindles. Fineness signaled wealth since the labor involved was enormous.

### 3.2 Kos and Rome

The island of Kos produced *Coa vestis*, a sheer silk-like cloth made from wild silkworm cocoons. Pliny the Elder credited a woman named Pamphile of Kos with inventing the technique of unwinding and weaving it. Roman moralists including Seneca complained that such garments could not honestly be called clothing since they concealed nothing. Later Chinese silk imported along trade routes was sometimes unraveled and rewoven into thinner gauzes in the eastern Mediterranean.

### 3.3 Han China

The Mawangdui tombs (sealed around 168 BCE) held a plain silk gauze robe about 128 cm long with a sleeve span near 190 cm that weighs roughly 49 grams. It remains one of the most celebrated demonstrations of ancient reeling and weaving skill.

### 3.4 Bengal muslin

Dhaka in Bengal produced the finest cotton fabric ever recorded. It came from a local cotton variety called Phuti karpas grown along the Meghna River. The fibers were too short for most spinning methods, so spinners worked in high humidity, sometimes on boats or near water, to keep the fibers supple. Poetic names described the grades:

- *Ab-i-rawan*: running water
- *Shabnam*: evening dew
- *Baft-hava*: woven air

A popular legend says a Mughal princess was scolded for immodesty while wearing several layers of it. The industry collapsed in the 18th and 19th centuries under colonial trade policies and competition from industrial cloth, and the plant variety was nearly lost. A revival project in Bangladesh has worked since the 2010s to reidentify the plant and recreate the textile.

### 3.5 Medieval and early modern Europe

Fine linen veils, wimples and headdresses used lawn and cambric. Lace emerged in the 16th century in Venice and Flanders, with needle lace and bobbin lace traditions branching into famous regional styles (Venetian point, Brussels, Mechlin, Valenciennes, Alençon, Chantilly).

### 3.6 The Regency muslin craze

Between roughly 1795 and 1820, thin white muslin gowns inspired by classical statuary dominated European fashion. Satirists joked about "muslin disease," the colds supposedly caught by women wearing so little in northern winters. Shawls of cashmere and wool became essential companions for warmth.

### 3.7 Machines

- **1808 to 1809**: John Heathcoat patents the bobbinet machine, making true net cheaply.
- **Around 1813**: John Levers develops the machine that becomes the Leavers lace machine.
- Machine net and lace turn veils, curtains and trims into everyday goods.

### 3.8 Synthetic fibers

- **1890s to 1910s**: rayon (viscose) offers "artificial silk."
- **1935**: Wallace Carothers' team at DuPont develops nylon.
- **1939 to 1940**: nylon stockings launch nationally in the US. Huge crowds line up on release day in May 1940.
- **World War II**: nylon is diverted to parachutes and military goods. Women paint seams on bare legs. Postwar shortages trigger "nylon riots" in 1945 to 1946.
- **1941**: polyester (PET) is patented in Britain by Whinfield and Dickson.
- **1958**: spandex is invented at DuPont by Joseph Shivers (sold as Lycra).

### 3.9 Sheer as statement

The 1960s brought sheer blouses onto runways, most famously Yves Saint Laurent's 1968 designs. The "naked dress" became a recurring red-carpet genre from the 1990s onward. Sheer layering, mesh panels and visible-lining construction remain staples in fashion today.

---

## 4. One-Way Mirrors

### 4.1 What they are

A "one-way mirror" (also two-way mirror, half-silvered mirror, observation glass) is a pane with a partially reflective coating. Common coatings:

- **Thin metal films**: aluminum, silver, chromium, titanium or nickel alloys, a few to tens of nanometers thick. Some light reflects, some passes and some is absorbed by the metal.
- **Dielectric stacks**: alternating layers of high-index and low-index materials (such as TiO₂ and SiO₂). Very little absorption. Reflection is tuned by interference.

Typical observation glass reflects a large share of light and transmits a smaller share. Exact splits vary by product.

### 4.2 The secret: it is not actually one-way

Passive optical materials obey **reciprocity**: transmittance from side A to side B equals transmittance from B to A. A one-way mirror lets exactly as much light through in each direction.

Reflectance can differ slightly between the two faces when the coating absorbs light (metal on glass looks a bit different from each side), yet transmission never differs.

There is also a thermodynamic reason. If a passive pane let light through only one way, placing it between two rooms at equal temperature would let radiant energy pile up on one side, making one room hotter than the other with no energy input. That violates the second law of thermodynamics.

### 4.3 How the illusion works: lighting ratio

The effect depends entirely on one side being far brighter than the other. Each viewer sees two things superimposed:

- Light from their own side, reflected by the coating.
- Light from the other side, transmitted through the coating.

**Worked example.** Reflectance R = 0.60, transmittance T = 0.12. The bright room has luminance 100. The dark observation room has luminance 10.

| Viewer | Reflected light seen | Transmitted light seen | Ratio | Result |
|---|---|---|---|---|
| In bright room | 0.60 × 100 = 60 | 0.12 × 10 = 1.2 | 50 : 1 | Sees a mirror |
| In dark room | 0.60 × 10 = 6 | 0.12 × 100 = 12 | 1 : 2 | Sees through |

Installers usually recommend that the observed side be lit at least 8 to 10 times brighter than the observation side. Observation rooms use dim lighting, dark walls and dark clothing, with no screens or lamps visible behind observers.

### 4.4 Reversal

Switch the lighting and the effect reverses. Buildings with mirrored windows look opaque in the day yet become fully visible from the street at night when interior lights are on. Reflective window film behaves exactly the same way.

### 4.5 Detecting observation glass

- **The fingernail test is unreliable.** Touching a nail to an ordinary back-silvered mirror shows a gap from the glass thickness, while touching a one-way mirror shows no gap. Front-surface mirrors (used in some decor and optics) also show no gap, so the test produces false alarms.
- **Darken your side.** Cupping hands around the eyes and pressing against the glass removes reflected light, so any lit space behind becomes visible.
- **Light from your side.** A flashlight pressed to the glass can illuminate a space behind it.
- **Mounting.** A mirror recessed into the wall with a space behind it differs from one hung on a solid wall.
- **Knocking.** A hollow cavity behind sounds different from a solid wall, though this is not definitive.

### 4.6 Uses

- Police interrogation and observation rooms
- **Gesell dome**: an observation dome developed by Arnold Gesell at Yale for watching children's development without disturbing them
- **Teleprompters**: a beam splitter at 45° reflects text toward the presenter while the camera looks through it
- Retail security and casino surveillance
- Smart mirrors with displays behind the glass
- Infinity mirrors (two partial mirrors facing each other)
- Mirrored sunglasses: the wearer's eyes sit in shade, so outsiders see reflection while the wearer sees out

### 4.7 True one-way optics

Real nonreciprocal devices exist, though none suit windows:

- **Faraday isolators** use magneto-optic materials in a magnetic field plus polarizers. Used in lasers and fiber optics to block back-reflections.
- **Time-modulated or nonlinear devices** break reciprocity under special conditions in research settings.

These handle narrow beams under controlled conditions, not room-sized scenes.

---

## 5. One-Way Fabrics, Screens and Veils

### 5.1 The same rule applies

Fabric and mesh create one-way effects through the same lighting asymmetry plus the proximity effect (1.12). The bright side's scattered glow hides the dim side. The dim side's viewer sees through gaps toward the bright side.

### 5.2 Sheer curtains

- **Daytime**: outside is bright. The curtain's outer face scatters daylight toward the street, hiding the room. Occupants see out.
- **Night**: the room is lit. The curtain glows from inside and the street sees silhouettes and often detail.
- **Dual-faced and metallized sheers** push the effect further. A light or reflective outer face scatters exterior light. A dark inner face absorbs interior light so it adds little glow when viewed from inside.

### 5.3 Solar screens and shades

PVC-coated polyester or fiberglass shade fabrics come in openness factors (1.3) and colors:

| Fabric color face | View out | Daytime privacy | Heat rejection |
|---|---|---|---|
| Dark (black, charcoal, bronze) | Best | Lower | Absorbs more heat at the window |
| Light (white, beige) | Lower, more glare | Higher | Reflects more solar heat |
| Dual (light out, dark in) | Good | Good | Good |

### 5.4 Insect screens

Charcoal and black screens are easier to see through than bright aluminum because they produce less veiling glow. Some screens are made deliberately dark for this reason.

### 5.5 Perforated "one-way vision" film

Developed in the 1980s, this vinyl is used on bus and storefront windows:

- The outer face carries a printed graphic on a white base.
- The inner face is black.
- Holes cover a set fraction of the area (common splits are 50/50, 60/40 or 70/30 print to hole).

From outside, the bright printed surface dominates and the holes read as tiny dark dots. From inside, the black surface adds almost no glow, the holes are near the eye and out of focus, and the outside world is visible. At night with lights on inside, the effect weakens or reverses.

### 5.6 Theater scrim

Sharkstooth scrim is the stage version of a one-way fabric:

- **Lit from the front** at a steep angle, the scrim looks like a solid painted wall.
- **Lights bleed in behind** and the front light fades, and the scrim seems to dissolve, revealing a scene behind.

Bobbinet scrims are more transparent and used for misty, dreamlike layering.

### 5.7 Veils and masks

- **Face veils** (mourning veils, birdcage veils, the mesh eye panel of the Afghan chadari) sit close to the eyes, so the wearer sees through defocused mesh. Observers farther away see focused fabric, and the wearer's face is usually in shade under the head covering.
- **Beekeeping veils** often use a black mesh face panel even when the rest of the suit is white. The black mesh is easier to see through. Light colors elsewhere tend to provoke bees less.
- **Fencing masks** use fine metal mesh. In a bright venue the fencer's face is unseen while the fencer sees the opponent clearly.
- **Hunting blinds** use shoot-through mesh windows with dark interiors.
- **Car window tint** is rated by visible light transmission (VLT). Very dark tints work like one-way glass in daylight yet hamper the driver's view at night.

### 5.8 Architectural screens

- **Mashrabiya** (Arab world): wooden latticework window screens. Occupants, traditionally women in many households, could see the street while staying unseen. Screens also cut glare, passed breezes and sometimes held clay water jars for evaporative cooling.
- **Jali** (South Asia): pierced stone or wood lattices common in Mughal and Rajput architecture. They provide privacy, filtered light and airflow, while the stone's mass moderates temperature.
- **Shoji** (Japan): translucent paper panels diffuse light without giving a clear view. These are diffusers rather than one-way screens.

---

## 6. Concealing Garments in History

### 6.1 Why people cover

- **Religious or moral codes**: modesty rules, sacred spaces, devotional practice.
- **Status signaling**: veiling as a mark of respectable or elite status, sometimes forbidden to lower classes.
- **Protection**: sun, sand, wind, insects, cold, dust.
- **Anonymity**: carnival, social freedom, crime, protest, espionage.
- **Mourning**: visible withdrawal from social life.
- **Ceremony**: weddings, initiations, coronations.
- **Military and hunting**: camouflage and concealment.
- **Occupational**: beekeeping, welding, hazmat, cleanrooms, medicine.

### 6.2 Ancient Near East

The **Middle Assyrian Laws** (tablets from around the 12th to 11th centuries BCE) contain one of the oldest written veiling rules. Married women and certain respectable women were required to veil in public. Enslaved women and prostitutes were forbidden to veil and faced harsh punishments for doing so. Veiling here marked legal and social status.

### 6.3 Greece and Rome

- **Greece**: women often drew the himation (mantle) over the head and sometimes the lower face in public. Scholar Lloyd Llewellyn-Jones has argued that veiling in Greece was far more widespread than older scholarship assumed.
- **Rome**: married women wore the palla, a mantle often pulled over the head. Brides wore the *flammeum*, a flame-colored veil. Priests covered their heads during sacrifice.

### 6.4 Byzantine and Sasanian worlds

Elite women in both empires commonly veiled. These customs influenced practices in the early Islamic societies that conquered or neighbored them.

### 6.5 Islamic traditions

The Quran's verses on modest dress (often cited are 24:31, mentioning the *khimar*, and 33:59, mentioning the *jilbab*) are interpreted in many ways across schools and cultures. Garments include:

| Garment | Region | Description |
|---|---|---|
| Hijab | Worldwide | Headscarf covering hair and neck |
| Niqab | Arabian Peninsula, elsewhere | Face veil leaving the eyes visible |
| Burqa / chadari | Afghanistan, Pakistan | Full-body garment with a mesh grille over the eyes |
| Chador | Iran | Large semicircle of cloth held closed by hand |
| Haik | Maghreb | Large white wrap, often with a separate face cloth |
| Battoulah | Gulf, southern Iran | Stiff face mask, often with a metallic sheen from indigo dye |
| Abaya | Gulf, worldwide | Loose overgarment, usually black |
| Jilbab | Indonesia, elsewhere | Varies: outer robe or long headscarf |

### 6.6 Men who veil

- **Tuareg** men of the Sahara wear the *tagelmust*, a long cloth wrapped around head and face, from adulthood. Women traditionally do not veil the face. Indigo dye from the cloth rubs onto skin, giving rise to the name "blue people." The veil protects against sand and sun and carries strong social meaning about respect and reserve.
- **Almoravids**: the 11th-century Sanhaja Berber dynasty was known as *al-mulaththamun*, "the veiled ones," because their men wore face veils.
- **Keffiyeh / shemagh**: Middle Eastern head cloths that can be wrapped across the face against sun and dust.

### 6.7 Christian Europe

- **Wimple and gorget**: medieval women wrapped linen around the neck and chin, framing the face (especially 12th to 14th centuries).
- **Nuns' habits** preserve versions of these coverings.
- **Mantilla**: lace head covering in Spain, prominent from the 17th century onward and worn for church and formal occasions.
- **Chapel veils**: Catholic women commonly covered their heads at Mass until the late 1960s, and some still do.
- The New Testament passage 1 Corinthians 11 is the classic textual basis for Christian head covering.

### 6.8 Jewish traditions

Married women in Orthodox communities often cover their hair with a **tichel** (headscarf), **snood** or **sheitel** (wig), based on rabbinic interpretation of modesty laws.

### 6.9 South Asia

**Ghoonghat** (a sari end or scarf drawn over the head and face) and **purdah** (seclusion and screening of women) were practiced by Hindu and Muslim communities in various regions. The jali screens of Section 5.8 are the architectural counterpart.

### 6.10 East Asia

- **Joseon Korea**: women of different classes wore the **jangot**, a coat worn over the head, or the **sseugae-chima**, a skirt worn over the head, to cover the face outdoors. Upper-class women sometimes wore the **neoul**, a veil hanging from a hat.
- **Japan, Heian and Kamakura periods**: traveling women wore the **ichime-gasa**, a wide hat with the **mushi-no-tareginu**, a sheer veil of silk or ramie hanging all around. It concealed the face and kept away insects (the name literally refers to insects). The **kazuki** was a kimono draped over the head.
- **Kuroko**: kabuki stagehands dressed entirely in black, a convention signaling "invisible." Their outfits shaped the popular image of the black-clad ninja, which has little historical basis.

### 6.11 The Americas

- **Tapadas limeñas** of colonial Lima, Peru (16th to 19th centuries) wore the *saya* (a fitted skirt) and *manto* (a shawl drawn over the head and face) leaving only one eye visible. The anonymity gave women unusual social freedom. Authorities attempted repeated bans without lasting success.
- **Anti-mask laws** in the US date at least to New York's 1845 law, aimed at tenant farmers in the Anti-Rent War who disguised themselves while resisting landlords. Later laws targeted masked groups such as the Ku Klux Klan.

### 6.12 Masks for anonymity and complexion

- **Venice**: the **bauta** (a white mask with a jutting chin allowing speech and eating, worn with a tricorn hat and tabarro cloak) and the **moretta** (a black oval velvet mask held by a button between the teeth, leaving the wearer silent). Masking was permitted for long portions of the year and was regulated by law.
- **England and France, 16th and 17th centuries**: women wore the **vizard** (visard), a black velvet mask, to protect the complexion from sun and wind. Some were also held by a button bitten between the teeth.
- **Plague doctor**: the beaked mask is associated with 17th-century physician Charles de Lorme, though how widely it was worn is debated.

### 6.13 Mourning

Victorian widows wore "widow's weeds," including heavy veils of matte black **crape** (crêpe), for a year or more of deep mourning before stepping down to lighter mourning. Courtaulds built an industrial fortune on mourning crape.

### 6.14 Travel, work and protection

- **Motoring veils and dusters** (early 1900s): open cars threw dust, so women tied gauze veils over hats and faces.
- **Beekeeping veils** date back centuries in various forms.
- **Balaclava**: knit hoods sent to British troops during the Crimean War (1854) and named after the Battle of Balaclava.
- **Ghillie suits**: developed by Scottish gamekeepers. The **Lovat Scouts** used them militarily during the Second Boer War (1899 to 1902).
- **Havelock**: a cloth hat cover with a neck flap, named after British general Henry Havelock and used in India in the 1850s.
- **Modern protective gear**: welding hoods, hazmat suits, cleanroom "bunny suits," surgical hoods.

### 6.15 Modern sun and swim coverings

- **Burkini**: full-coverage swimwear designed in 2004 by Aheda Zanetti in Australia.
- **Facekini**: full-head swim masks popularized on beaches around Qingdao, China, for sun and jellyfish protection.
- **UPF hoodies, sun sleeves and neck gaiters** for outdoor sports.

### 6.16 Modern legal landscape

Several countries restrict full face coverings in public, beginning with France's 2010 law (in force 2011), followed by Belgium and others. Other countries have historically required covering. These laws remain politically contested, with arguments framed around security, social integration, religious freedom and personal autonomy.

---

## 7. Heat and Cold Under Covering Garments

### 7.1 The body's heat balance

The standard heat balance equation:

**S = M − W − (C + R + K + E + Res)**

- **S**: heat storage (positive means body temperature is rising)
- **M**: metabolic heat production
- **W**: external mechanical work
- **C**: convection (air moving across skin or clothing)
- **R**: radiation (to and from surroundings and sun)
- **K**: conduction (contact with surfaces)
- **E**: evaporation of sweat
- **Res**: respiratory heat and moisture loss

Clothing alters C, R, K and E. It cannot change M except by making movement harder.

### 7.2 Units

- **1 met** = 58.2 W per m² of body surface, about 100 W for a resting adult.
  - Sitting: ~1 met. Walking: ~2 to 3 met. Heavy labor: 4 to 6+ met.
- **1 clo** = 0.155 m²·K/W of thermal resistance. Originally defined as the insulation keeping a resting person comfortable at about 21°C in still air, roughly a business suit.
- Still air conducts heat at about 0.026 W/(m·K). One clo equals the resistance of roughly a **4 mm layer of perfectly still air**.
- A long-standing rule of thumb gives clothing about **4 clo per inch** (about 1.6 clo per cm) of total thickness, including trapped air. Most insulation is the air, not the fiber.

| Outfit | Approx. clo |
|---|---|
| Nude | 0 |
| Shorts | 0.1 |
| Shorts and T-shirt | 0.3 |
| Light summer clothing | 0.5 |
| Trousers and long-sleeve shirt | 0.6 |
| Business suit | 1.0 |
| Heavy winter street clothing | 1.5 to 2.0 |
| Arctic gear | 3 to 4+ |
| Sleeping bag (expedition) | 8 to 10+ |

### 7.3 Skin and core

- Core temperature: about 37°C.
- Mean skin temperature in comfort: about 33 to 34°C.
- When air and surroundings exceed skin temperature (roughly 35°C), convection and radiation **add** heat instead of removing it. Sweat evaporation becomes the only cooling route.

### 7.4 Sweat physics

- Latent heat of evaporation at skin temperature: about **2,420 J per gram**.
- Evaporating 1 liter per hour removes about **670 W**, more than six times resting heat output.
- Acclimatized adults may sweat 1 to 2 L per hour, sometimes more in very hard work.
- **Only evaporated sweat cools.** Sweat that drips off or soaks clothing without evaporating removes almost no heat.
- Sweat evaporating at the skin cools most efficiently. Sweat wicked into fabric and evaporating at the outer surface draws part of its heat from the surrounding air instead of the skin, lowering efficiency. This is why heavy wicking layers in extreme heat do not cool as well as bare or thinly covered wet skin.

### 7.5 Evaporative resistance and breathability

Fabrics are tested on a heated, sweating plate (ISO 11092) to measure **Ret**, evaporative resistance in m²·Pa/W:

| Ret | Rating |
|---|---|
| 0 to 6 | Very breathable |
| 6 to 13 | Breathable |
| 13 to 20 | Moderately breathable |
| 20+ | Low breathability |

The **Woodcock permeability index**:

**i_m = (R_ct / R_et) × S**, where S ≈ 60.6 Pa/K

i_m ranges from 0 (impermeable) to 1 (free evaporation). Ordinary garments sit around 0.3 to 0.5.

### 7.6 Solar heat load

- Direct sunlight at ground level can reach about **1,000 W/m²** at high sun on a clear day.
- Solar energy at the surface is roughly 5% ultraviolet, 43% visible and 52% near-infrared.
- Hot sand and pavement also reflect sunlight and radiate thermal energy upward.
- A person standing in strong sun can absorb well over 100 W extra, a big addition to the 100 W resting baseline.

Clothing intercepts this load at the fabric surface. Heat absorbed there partly escapes to the air by convection and radiation before reaching skin. The larger the air gap and the more air moves through it, the more heat is shed before it arrives.

### 7.7 The Bedouin black robe study

In 1980, Shkolnik, Taylor, Finch and Borut published a study in *Nature* titled "Why do Bedouins wear black robes in hot deserts?" Volunteers stood in the Negev desert sun in black robes, white robes, a tan army uniform or shorts only.

Findings:

- Black robes absorbed more solar energy and their outer surface ran several degrees hotter than white ones (around 6°C).
- **Heat gain at the skin was the same** for black and white robes.
- The extra heat in black robes was carried off by stronger convection inside the loose garment. Hot air rose and exited at the neck while cooler air entered at the hem (a chimney effect), helped by wind.
- The person in shorts only gained the most heat.

Lessons: in dry desert sun, **coverage and looseness** matter more than color, and covering beats exposing skin. Color matters more in tight garments where the heated fabric sits against skin.

### 7.8 Color in depth

- **Visible color** describes only the 43% of solar energy in the visible band. Many dyes behave differently in near-infrared. Some dark fabrics reflect much near-infrared and run cooler than expected. Others absorb it.
- **Thermal emissivity** (ability to radiate heat in the far infrared) is about 0.9 for nearly all fabrics regardless of color. A black shirt and a white shirt radiate body heat away equally.
- **Metallized fabrics** have low emissivity (0.05 to 0.3). They reflect radiant heat and also radiate little, which is why emergency "space blankets" keep people warm and why metallized firefighter proximity suits reflect fire radiation.
- **Black goat-hair tents** of the Bedouin create deep shade. The loose weave lets hot air escape in dry weather, and the hair swells when wet to tighten the weave against rain.

### 7.9 Loose vs tight

| Feature | Loose garments | Tight garments |
|---|---|---|
| Air gap | Large, insulates against hot air and absorbed solar heat | Minimal |
| Ventilation | Bellows (pumping) effect as limbs move, chimney effect | Little air exchange |
| Sweat handling | Evaporation at skin, vapor exits through openings | Fabric must wick or skin stays wet |
| Solar heat | Absorbed at fabric, largely shed before reaching skin | Conducts straight into skin |
| Cold weather | Drafty unless closed at openings | Retains a thin warm layer, less insulation overall |
| Best for | Hot dry sun, hot humid air | Active sports, base layers in cold |

**Openings matter.** Air enters and leaves through neck, cuffs and hem. Opening them in heat and sealing them in cold can shift a garment's effective insulation dramatically. Walking and wind can cut a garment's insulation by a third to a half compared with standing in still air.

### 7.10 Fibers and their behavior

**Moisture regain** (water absorbed at standard conditions, about 21°C and 65% relative humidity):

| Fiber | Regain (approx.) | Behavior |
|---|---|---|
| Wool | 13 to 16% | Absorbs vapor, releases heat of sorption, insulates when damp, odor resistant |
| Viscose / rayon (incl. "bamboo") | 11 to 13% | Very absorbent, cool feel, slow drying, weak when wet |
| Linen | ~12% | Absorbs and releases moisture fast, stiff so it stands off the skin, high thermal conductivity, feels cool |
| Silk | ~11% | Light, smooth, mild warmth, absorbent |
| Cotton | ~8.5% | Comfortable, absorbent, dries slowly, clings when wet |
| Nylon | ~4 to 4.5% | Strong, dries quickly, can feel clammy |
| Acrylic | ~1.5% | Wool-like bulk, low absorbency |
| Spandex | ~1.3% | Stretch, usually blended |
| Polyester | ~0.4% | Barely absorbs, dries fast, wicks when engineered with channels or finishes |
| Polypropylene | ~0% | Hydrophobic, wicks by capillary action, very fast drying |

Key points:

- **Wool and heat of sorption**: when wool absorbs water vapor it releases heat. Stepping from a dry warm room into cold humid air, a wool garment warms slightly as it takes up moisture.
- **"Cotton kills"** is a hiker's phrase. Wet cotton loses most of its insulation and drains heat as it slowly dries, a hypothermia risk in cold wet conditions.
- **Linen in heat**: loose, crisp and conductive, it is one of the best traditional hot-weather fabrics.
- **Merino** wool finer than about 24 µm feels soft rather than itchy because fine fibers bend instead of poking skin.

### 7.11 Cool-touch and radiative textiles

- **Cool-touch fabrics** are rated by **q-max** (peak heat flux when skin first touches fabric). High thermal effusivity fabrics like linen, some nylons with mineral additives and ultra-high-molecular-weight polyethylene feel cool on contact.
- **Infrared-transparent textiles**: human skin at about 306 K radiates most strongly near **9.5 µm** (Wien's law: 2,898 µm·K ÷ 306 K). Polyethylene is transparent at that wavelength. Stanford researchers (Hsu and colleagues, *Science*, 2016) made a nanoporous polyethylene textile that blocks visible light yet lets body infrared escape. Skin under it ran about 2°C cooler than under cotton in tests.
- **Phase change materials (PCMs)**: microcapsules of waxes that melt and solidify near skin temperature, absorbing and releasing heat. Originally researched for NASA in the 1980s and sold commercially afterward. They buffer short temperature swings rather than providing sustained cooling.
- **Evaporative cooling garments**: cooling towels, vests and neck wraps soaked in water. Very effective in dry heat, weak in humid heat.

### 7.12 Head, face and neck

- The head and shoulders take the most direct solar load when the sun is high.
- **Brimmed hats** shade face and neck. Ventilated crowns let hot air escape.
- **Neck flaps** (havelock style, legionnaire caps, keffiyeh drapes) block sun on a very heat-sensitive area.
- The **face is highly sensitive** to temperature. Cooling the face with air or water produces outsized relief in perceived comfort. Covering the face in heat feels warmer than the small physical heat change would suggest.
- **Face coverings** slightly warm and humidify inhaled air. In cold, scarves and balaclavas protect airways and skin. In heat, this mild effect adds discomfort more than real heat stress.
- **Wet cloth over head and neck** is a traditional desert technique. Evaporation cools the cloth and the skin beneath.

### 7.13 Covering by climate

| Climate | Best approach | Reasoning |
|---|---|---|
| Hot and dry, strong sun (desert) | Cover fully with loose, light, flowing garments. Head and neck covered. Light colors or loose dark colors. | Blocks solar load and hot-air convective gain. Sweat evaporates fast anyway. Covering cuts water loss and sunburn. |
| Hot and humid (tropics) | Minimal or very open, loose and highly breathable coverage. Linen, open weaves, mesh panels. | Evaporation is limited by humid air, so any vapor barrier hurts. Airflow is the priority. |
| Hot and humid with strong sun | Loose, light, open-weave long sleeves with UPF rating plus a wide hat. | Balances sun protection against evaporation. |
| Mild with sun | Light layers, sun hat. | UV protection without overheating. |
| Cold and dry | Layering: wicking base, insulating middle, windproof outer. Cover extremities. | Trapped still air insulates. Wind is the main enemy. |
| Cold and wet | Wool or synthetics only, waterproof-breathable shell, no cotton next to skin. | Wet insulation fails. Evaporative chilling is severe. |
| Extreme cold (arctic) | Thick layered loft, vapor barrier liners optional, full face coverage, mittens over gloves. | Skin freezes quickly. Moisture from sweat can freeze inside insulation. |

### 7.14 Layering in cold

- **Base layer**: moves sweat off skin. Merino, polyester or polypropylene.
- **Mid layer**: traps air. Fleece, wool, down, synthetic insulation.
- **Shell**: blocks wind and rain. Waterproof-breathable membranes such as expanded PTFE or polyurethane.
- **Vapor barrier liners**: impermeable layers worn near the skin in extreme cold so sweat cannot freeze inside insulation. Effective but clammy.
- **Down fill power**: cubic inches occupied by one ounce of down. 600 is good, 800+ is premium. Down loses most loft when wet.
- **Ventilate before sweating**: unzipping during exertion prevents moisture buildup that would later chill the body.

**Wind chill** (US National Weather Service formula, °F and mph):

**WC = 35.74 + 0.6215T − 35.75V^0.16 + 0.4275T·V^0.16**

At 0°F with a 20 mph wind, wind chill is about −22°F. Covering exposed skin is the main defense against frostbite.

### 7.15 Heat stress measurement

**Wet Bulb Globe Temperature (WBGT)**, outdoors in sun:

**WBGT = 0.7 T_nwb + 0.2 T_g + 0.1 T_db**

- T_nwb: natural wet bulb (humidity and air movement)
- T_g: black globe temperature (radiant heat)
- T_db: dry bulb (air temperature)

Occupational guidelines (ACGIH) add **clothing adjustment factors** to WBGT for garments that trap heat. Approximate values:

| Clothing | Adjustment (°C added to WBGT) |
|---|---|
| Woven work clothes | 0 |
| Cloth coveralls | 0 |
| Double-layer woven clothing | +3 |
| SMS polypropylene coveralls | +0.5 |
| Polyolefin coveralls | +1 |
| Limited-use vapor-barrier coveralls | +11 |

A vapor-barrier suit turns a moderate day into a dangerous one because it blocks evaporation, the only cooling route in heat.

### 7.16 Heat illness signs

| Condition | Typical signs | Response |
|---|---|---|
| Heat cramps | Painful muscle spasms during or after exertion | Rest, fluids with electrolytes |
| Heat exhaustion | Heavy sweating, weakness, dizziness, nausea, headache, cool clammy skin | Move to shade, loosen or remove layers, cool with water, fluids |
| Heat stroke | Confusion, collapse, very high body temperature (above ~40°C), hot skin that may be dry or sweaty | Medical emergency: call emergency services, cool rapidly (cold water immersion is the most effective method) |

Heavy covering garments, especially those that block evaporation, raise risk during exertion in heat. Loosening and opening garments is the first step when overheating.

---

## 8. Sun, UV and Coverage

### 8.1 UPF

**Ultraviolet Protection Factor (UPF)** measures how much UV a fabric blocks. UPF 50 means about 1/50 (2%) of UV passes through.

| UPF | UV blocked | Rating |
|---|---|---|
| 15 to 24 | 93.3 to 95.8% | Good |
| 25 to 39 | 96.0 to 97.4% | Very good |
| 40 to 50+ | 97.5 to 98%+ | Excellent |

Standards include AS/NZS 4399 (Australia/New Zealand), ASTM D6603 (US labeling) and EN 13758 (Europe).

### 8.2 What raises UPF

- **Tighter construction**: less open area. This is the single largest factor.
- **Darker and more saturated colors**: absorb more UV.
- **Fiber type**: polyester absorbs UV strongly. Unbleached cotton contains natural compounds that absorb UV better than bleached white cotton.
- **Heavier and thicker fabric**.
- **UV absorber finishes**, TiO₂ or zinc oxide particles.
- **Fluorescent brighteners**: laundry additives that absorb UV and can raise UPF over repeated washes.

### 8.3 What lowers UPF

- **Wetness**: cotton loses much of its protection when wet as fiber scattering drops (Section 1.6).
- **Stretching**: pulls yarns apart and opens gaps.
- **Wear and washing**: thins fabric and loosens structure in some cases.

### 8.4 Typical values

- White cotton T-shirt: often around UPF 5 to 7, lower when wet.
- Sheer chiffon or voile: typically low, often below UPF 10.
- Denim: very high, frequently in the hundreds or more.
- Purpose-made UPF shirts: 30 to 50+.

### 8.5 Sheer versus sun

Sheer garments cut glare and some heat yet usually give weak UV protection. Their open area lets UV straight through. A sheer covering offers modesty and comfort in light sun yet is a poor substitute for sunscreen or UPF fabric in strong sun. Window glass blocks most UVB yet passes much UVA, so skin can still be affected through car and home windows.

---

## 9. Garments That Conceal and Ventilate at Once

Many traditional and modern designs solve the apparent contradiction between covering and staying cool:

- **Loose flowing robes** (thobe, dishdasha, kaftan, jellabiya, abaya): full coverage with chimney and bellows ventilation.
- **Mesh eye panels** (chadari): vision and airflow through a concealing panel.
- **Insect veils** (Heian mushi-no-tareginu, beekeeping veils, mosquito net hoods): conceal and protect while allowing airflow and sight.
- **Tagelmust**: wrapped in multiple loose layers that trap a humid microclimate around the nose and mouth, reducing moisture loss in dry desert air while blocking sand.
- **Mashrabiya and jali**: architectural versions offering privacy plus breeze.
- **Modern mesh-paneled sportswear**: opaque fabric where coverage matters, open mesh at heat-dumping zones (underarms, upper back, sides).
- **Layered sheers**: two or more sheer layers stacked loosely conceal far better than one layer of double weight, since scattering compounds and the gap between layers blurs whatever lies beneath (proximity effect), while airflow still passes through.
- **Light outer, dark inner** construction: some sun garments and umbrellas use a reflective or light outer face with a darker inner face. The outer face rejects sunlight and the inner face absorbs stray light, reducing glare on the wearer's face.

---

## 10. Quick Reference Tables

### 10.1 Approximate fiber densities

| Fiber | Density (g/cm³) |
|---|---|
| Polypropylene | 0.91 |
| Nylon | 1.14 |
| Acrylic | 1.17 |
| Spandex | ~1.2 |
| Wool | 1.31 |
| Silk | 1.33 |
| Polyester | 1.38 |
| Viscose | 1.52 |
| Cotton | 1.54 |
| Linen | 1.50 |
| Glass | 2.5 |

### 10.2 Thermal emissivity

| Surface | Emissivity (thermal IR) |
|---|---|
| Human skin | ~0.98 |
| Most fabrics (any color) | ~0.85 to 0.95 |
| Polyethylene film (thin) | Partly transparent, low effective emissivity |
| Aluminized fabric | ~0.05 to 0.3 |
| Polished aluminum | ~0.05 |

### 10.3 Thermal conductivity

| Material | k (W/m·K) |
|---|---|
| Still air | 0.026 |
| Down cluster (in use) | ~0.03 to 0.04 |
| Wool fiber (solid) | ~0.2 |
| Cotton fiber (solid) | ~0.2 to 0.3 |
| Polyester (solid) | ~0.15 to 0.2 |
| Water | ~0.6 |
| Skin | ~0.3 to 0.5 |

Water conducts heat about 23 times better than still air. Wet clothing loses insulation for this reason.

### 10.4 One-way effect checklist

| To see out without being seen | To be seen through less at night |
|---|---|
| Keep your side darker than the other | Use opaque linings or blackout layers |
| Use dark interior surfaces | Close curtains before lights go on |
| Use light or reflective outer faces | Add a second layer with an air gap |
| Stay close to the mesh or veil | Use dull, high-TiO₂ or tightly woven fabrics |

### 10.5 Things that make a sheer fabric more see-through

- Wetness
- Contact with skin
- Backlighting
- Dark colors when viewed from a dim side
- Bright (non-delustered) round filaments
- Stretching
- Viewing head-on
- Viewing from close range

### 10.6 Things that make it less see-through

- Lining or layering with an air gap
- Bright light on the viewer's side
- Pale colors facing the light
- Delustrants and microfibers
- Crepe or high-twist yarns
- Oblique viewing angles
- Moiré from multiple layers
- Distance from the fabric

---

## 11. Key Formulas

| Purpose | Formula |
|---|---|
| Energy balance at a surface | R + T + A = 1 |
| Fresnel reflectance (normal incidence) | R = ((n₁ − n₂) / (n₁ + n₂))² |
| Total woven cover factor | C = c₁ + c₂ − c₁c₂ |
| Open area | 1 − C = (1 − c₁)(1 − c₂) |
| Filament diameter | d (µm) ≈ 11.9 √(denier / ρ) |
| Contrast through a veil | T(L₁ − L₂) / (T(L₁ + L₂) + 2L_f) |
| Moiré period | P = p / (2 sin(θ/2)) |
| Observer sees (one-way mirror) | R × L_own side + T × L_other side |
| Wien's peak wavelength | λ_max (µm) = 2,898 / T (K) |
| Body heat balance | S = M − W − (C + R + K + E + Res) |
| Clo | 1 clo = 0.155 m²·K/W |
| Met | 1 met = 58.2 W/m² |
| Thermal resistance of a layer | R = thickness / k |
| Sweat cooling power | P (W) = mass evaporated (g/s) × 2,420 J/g |
| Woodcock permeability index | i_m = (R_ct / R_et) × 60.6 Pa/K |
| WBGT outdoors | 0.7 T_nwb + 0.2 T_g + 0.1 T_db |
| Wind chill (°F, mph) | 35.74 + 0.6215T − 35.75V^0.16 + 0.4275T·V^0.16 |
| UV transmitted through fabric | ≈ 1 / UPF |
