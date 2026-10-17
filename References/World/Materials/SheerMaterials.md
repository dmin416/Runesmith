# Sheer Materials, One-Way Viewing, Concealing Garments and Thermal Comfort

> Earth reference / invent loot. Not locked law. Fabrics / hides: `Materials.md`, `TranslucentMaterials.md`. Clothing eras: `../Science/Invent/ClothingTechnology.md`. Concealing history: `../Science/Invent/ConcealingGarments.md`. Heat / cold / UPF under cover: `../Science/Invent/ClothingThermal.md`. One-way mirrors / coatings: `../Science/Energy/Optics.md`. Breathable waterproof: `PermeationBarriers.md`. Insulation: `InsulationMaterials.md`. Ned silk / biomaterials: `../Science/Biomaterials/BiologicalSilks.md`. Caldris street clothes follow `../Tech/Technology.md`.

Nav: `Index.md`.

## Contents

1. The Physics of Sheer Materials
2. Sheer Fabric Types and Construction
3. A History of Sheer Fabrics
4. One-Way Mirrors (pointer: Optics.md)
5. One-Way Fabrics, Screens and Veils
6. Concealing Garments in History (pointer: ConcealingGarments.md)
7. Heat and Cold Under Covering Garments (pointer: ClothingThermal.md)
8. Sun, UV and Coverage (pointer: ClothingThermal.md)
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

Coatings, lighting ratio, detection and Faraday isolators: `../Science/Energy/Optics.md` (One-Way Mirrors). Glass pack: `GlassScience.md`, `TranslucentMaterials.md`.

One-way **fabrics and screens** stay in §5 below.

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

Veiling laws and garments by culture: `../Science/Invent/ConcealingGarments.md`. Clothing eras: `../Science/Invent/ClothingTechnology.md`.

---

## 7. Heat and Cold Under Covering Garments

Clo, sweat, layering and climate under cover: `../Science/Invent/ClothingThermal.md`. Insulation ladder: `InsulationMaterials.md`.

---

## 8. Sun, UV and Coverage

UPF, coverage and sun under garments: `../Science/Invent/ClothingThermal.md` (Sun, UV and Coverage).

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
