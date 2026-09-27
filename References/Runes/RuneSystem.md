# Rune System Redesign

Basis for runes going forward (not frozen; dials stay open). Companion: setup mana in `RuneSetup.md`. Activation energy, path efficiency and heat: `Energy.md`. Named rune catalog and chapter first-seens: `Runes.md`.

The original story used binary circuitry for runes. That model is dropped for rewrite law.

New model: a rune is symbology plus intention plus physical or magical pathways for mana to flow through.

| Part | Role |
|---|---|
| Symbology | Names the function of each region of the pattern |
| Intention | Gives the pattern its purpose and output form |
| Pathways | The physical or magical routes mana flows through. Geometry sets flow, storage and concentration. |

## Engine Analogy

Like an engine diagram where fuel enters a combustion area and later parts turn the result into motion. Mana enters the pattern and converts into another form of energy and later regions turn that into motion or another output. Nothing has moving parts. The pattern can sit on paper or inside a sword. Stages are regions of the pattern with different jobs.

## Stage Map

| Stage | Job | Fire arrow |
|---|---|---|
| 1. Intake | Connects to the source (wielder or magic stone) | Wielder pays the fixed cost |
| 2. Feed line | Low-resistance route to the rest of the pattern | Blood-ink trace |
| 3. Reservoir | Wide or looped region that stores potential for fast release | Charges the burst |
| 4. Converter | Symbol cluster where mana becomes another form | Mana to heat |
| 5. Shaping | Directs the converted energy into a form and heading | Forward flight |
| 6. Emitter | Release point where a tip or edge concentrates potential | Arrow leaves the tip |
| 7. Waste path | Sheds heat lost along the way | Heat into the medium |
| 8. Recovery | Turbo loop on the waste path. Returns part of the waste to the Reservoir. | Waste heat spun back into the burst |
| 9. Resonator | Supercharger. Overlapping regions locked to one tone pull ambient mana into the Converter. | Pattern rings with the local fire tone |

Stages 8 and 9 appear only at rune score above 1 (Common Low and up). Lesser runes are linear and have neither. Cost, efficiency, ambient gain and heat numbers: see `Energy.md`.

**Story Ch 16 (trial Fire Orb, rewrite):** on-page as five regions of one linear Lesser chain (collector → fire converter → shape → constrain → velocity). Source used three parts plus binary / logic-gate talk; that model is dropped. Map loosely to Intake / Feed / Converter / Shaping / Emitter (constrain ≈ hold or waste control before release). Full stage names need not appear in prose.

## Rank Scale

**The five ranks:** Lesser, Common, Greater, Grand, Legendary. **The five qualities:** Lowest, Low, Intermediate, High, Highest. A rune is named rank first and quality second (Common Low). Rank sets the scale of the machine: size, complexity and working ceiling. Quality sets how well the machine is built and so the position inside the rank. Harmonics (next section) set efficiency inside the ceiling. Output stops at the ceiling except for overrun (below). Extra mana fed into a scroll adds output up to it (canon: amplification is rank-capped).

**Working ceiling = 10 J x 100^s** per activation or per run (power x run length for a sustained machine). Each rank is a band of 100 times from Lowest to Highest. Lowest of a rank equals Highest of the rank below (canon). Intermediate sits at 10 times the Lowest. Lesser steps: 10 J, 32 J, 100 J, 316 J, 1 kJ. Lesser Highest is the baseline anchor: **1 mana ≈ 10 J** paid (`Energy.md`, `../Science/ManaCast.md`). Copper sealed (η 0.80, G 1) yields **8 J** useful per mana; 100 mana → **800 J** useful. Open-air copper (G 3) yields **24 J** per mana at clean linear Highest. Story "about 100 MP" detonation beats are round Intermediate / open-air mixes, not a second constant.

**Overrun.** The ceiling is soft. Overcharging, a rune done exceptionally well, or a Highest quality can push output past it by up to about 5 times. A Lesser Highest rune can reach about 5 kJ, above a Common Low. This is how a Lesser Highest rune can be powerful.

| Rank | Ceiling, Lowest to Highest | Complexity | Examples |
|---|---|---|---|
| Lesser | 10 J to 1 kJ | One linear chain | Firecrackers (Low to Intermediate). Arrows and bolts (Intermediate to High). Wind blades, mana blades and shields (Intermediate to Highest). Small explosions (High to Highest). Fireworks (Highest). |
| Common | 1 kJ to 100 kJ | A few coupled stages | Elemental arrows (a Common Fire Arrow at 100 mana in open air yields 3 kJ, Common Low), fireballs, weapon runes |
| Greater | 100 kJ to 10 MJ | A full working machine | Siege engines (a 100 kg stone at 50 m/s is 125 kJ), forges, wall wards, mill and pump engines |
| Grand | 10 MJ to 1 GJ | A system of machines | Steam locomotive on a 10 minute run (0.9 GJ at 1.5 MW). Factory boilers. |
| Legendary | 1 GJ to 100 GJ | A whole vessel | Locomotive on an hour-long run (5.4 GJ). Airship on an 8 hour leg at 3.3 MW (95 GJ). Fortress-wide wards. |

**Lesser size (set by crafter skill).** Even at low skill a Lesser rune fits easily on a paddle just under tennis racket size or on a single sword. With skill it fits a dagger. At the top of the basic skill (L9) it fits a playing card or an arrow, about the smallest any rune gets. Compression keeps the ceiling and cuts overrun headroom (canon: overload headroom drops).

**Power source (proposed).** Lesser runs on the wielder. An adult pool of 2000 mana gives about 60 kJ in open air, which reaches Common High (32 kJ) and nearly Common Highest (100 kJ). Common Highest needs about 3,300 mana at baseline yield (1.7 adult pools) so stone banks and ambient intake carry it and everything above. Baseline gains of 1 to 6 assume a hand-sized intake. Larger machines carry intakes sized to the machine and draw more (`Energy.md` section 3: draw is capped by intake size and local density). The wielder pays only the fixed start cost. Steam picture: the wielder opens the valve and the environment is the boiler.

## Harmonics and Resonance

A linear rune fires once through the stages in order. A resonant rune has stages that overlap. Overlapping regions share pathways and so share a tone. The pattern rings like an instrument and stages work together. Power comes from harmony as well as throughput and physical size.

- Turbo (Recovery). Waste exhaust spins a loop that feeds the intake. A share r of the path's own waste returns to the Reservoir.
- Supercharger (Resonator). The ringing overlap acts as a tuned intake that amplifies the ambient draw. Sealed space keeps gain 1 so resonance adds nothing there.
- Calling on natural mana. The rune does not force ambient mana. It sings the tone the environment answers to. This is how a rune calls on natural mana and the laws of magic.

Cost is never changed. Only η_eff and H_eff change output and waste.

### Rune score and tiers

**s = (rank index - 1) + quality fraction**

Rank index: Lesser 1, Common 2, Greater 3, Grand 4, Legendary 5. Quality fraction: Lowest 0, Low 0.25, Intermediate 0.5, High 0.75, Highest 1. s runs 0 to 5. Lesser Highest and Common Lowest both score 1 (canon). Common Highest and Greater Lowest both score 2.

**u = max(0, s - 1)** is the resonance score (0 to 4).

- **Lesser Lowest (s 0):** ugly, linear, wasteful and weak. A sloppy layout leaks 84 percent of the mana before it reaches the converter (λ 0.16) so the same attack costs 6.25 times as much as at Highest. Ceiling 10 J.
- **Lesser Highest (s 1):** linear, beautiful, efficient and still weak but can be powerful. A clean layout leaks nothing (λ 1) so it wastes only what its path material wastes. The 1 kJ ceiling keeps it weak against higher ranks but overrun lets it reach 5 kJ. It delivers the full baseline yield and matches a Common Lowest (canon).
- **Above s = 1:** resonance. Every step adds Recovery, tuning and ring-up.

### Formulas

- Layout efficiency: **λ = 0.16^(1 - s)** for s below 1 (0.4 at Intermediate). λ = 1 from s = 1 up.
- Recovery: **r = 0.125 x u**
- Effective efficiency: **η_eff = 1 - (1 - η x λ) x (1 - r) x (1 + d)**
- Effective gain factor: **H_eff = 1 + 0.25 x u x T**
- **Output = cost x 10 J x η_eff x [1 + (G - 1) x H_eff]**
- **Waste = cost x 10 J x (1 - η_eff)**
- Ring-up time: **0.75 s x u**. Linear runes fire instantly.

η path efficiency and G ambient gain: `Energy.md` section 3. T tuning. d discord. With s = 1 and d = 0 the result equals the untuned baseline.

### Natural mana tones

Natural mana carries a tone by element and by place. T is the match between the pattern's tone and the local tone of its element (0 to 1). Wielder affinity is the proposed source of T. A rune at 0 percent affinity still activates (canon: Lesser Fire Orb) with T = 0 and plain ambient gain.

### Layout efficiency and discord

- Linear layout: sloppy pathways leak mana before the converter. λ is the share that gets through: 0.16 at Lowest, 0.25 at Low, 0.4 at Intermediate, 0.63 at High and 1 at Highest. The same attack costs 1/λ times as much. Material efficiency cannot repair a leaking layout.
- Resonant layout: overlapping regions lock when their tones share whole-number ratios. Locked overlap adds nothing to d. Each unlocked overlap adds discord to d.
- Discord raises waste by the factor (1 + d) and can drag η_eff below the path's own η.
- Red faults under the Debugger mark leaks (low λ) and discord (d).
- Skilled crafting cleans the layout and locks the overlaps.

### Ring-up and ring-down

- Full Recovery and Resonance need the ring-up time. Release before it ends scales r and H_eff by the elapsed fraction (turbo lag).
- After a cast the pattern rings down over the same time. A recast during ring-down resumes at the remaining fraction so rapid repeated fire skips the lag.
- Resonant draw depletes local ambient mana like any other draw.

### Substrate

Path material is the instrument. Timbre: iron thuds, copper hums, steel rings, dark steel tolls, mana steel and mythril chime, adamantium sings pure. Recovery returns a share of the path's own waste and never more so the substrate sets the ceiling.

Lower waste means proportionally lower heat and strain on the path. Legendary Highest halves the path's waste per cast. A leaking layout multiplies it (same attack case below).

### Worked cases

Copper (η 0.80), open air (G 3). Clean linear baseline yield: **24 J** per mana (10 × 0.80 × 3). Yield per mana shows efficiency only. Output stops at the ceiling before any overrun.

- Lesser Lowest (s 0): η_eff 0.128. Yield 3.8 J with 8.7 J waste. The 10 J ceiling is reached at about 2.6 mana.
- Lesser Highest (s 1): yield 24 J with 2.0 J waste. The 1 kJ ceiling is reached at about **42 mana**.
- Common Highest (s 2), T 1: η_eff 0.825. Yield 28.9 J with 1.75 J waste.
- Legendary Highest (s 5), T 1: η_eff 0.90. Yield 45 J (1.88x vs sealed path) with 1.0 J waste.
- Legendary Highest, T 0.5: yield 36 J.
- Legendary Highest, sealed space (G 1): yield 9 J from the turbo alone.

### Same attack, same size

Steel sword (η 0.85) with a 1 kg blade and a Lesser rune of identical size. Highest costs 50 mana for the attack and Intermediate costs 125 mana (anchor), which sets Intermediate λ at 0.4. Both deliver **425 J** at the converter (**1275 J** in open air) so the extra 75 mana of the Intermediate is pure waste.

| | Highest | Intermediate |
|---|---|---|
| Cost | 50 mana | 125 mana |
| Input | 500 J | 1250 J |
| Waste | 75 J (15 percent) | 825 J (66 percent) |
| Waste in mana | 7.5 | 82.5 |
| Retained heat | 38 J (0.08 K) | 413 J (0.84 K) |
| Casts to strain limit | about 2800 | about 250 |

- Waste ratio is 11 to 1 on steel: 2.5 x (1 - 0.4η) / (1 - η). Iron 4.75, copper 8.5, mythril 31, adamantium 76. A better path widens the gap.
- Path life falls in the same ratio on identical size.
- Cost of the same attack by quality: Lowest 313, Low 198, Intermediate 125, High 79, Highest 50 mana.

## Visible Designs and Magical Vision

- Any design visible to the ordinary eye is decorative or a display of the runesmith's skill. It is not the working pattern.
- Magical vision shows the working circuits as an overlay of pathways crossing and overlapping.
- A skilled crafter can turn the circuitry itself into art so the overlay forms an image. Beauty is the tell of a clean layout at every rank. In a resonant rune it is also the look of a locked overlap.
- An unskilled crafter produces a jumbled mess of pathways. The jumble is a leaking layout (low λ) in a linear rune and discord (high d) in a resonant one.
- Linear runes are silent. Resonant runes sing. The tone is sensed magically. Higher rank rings louder and longer. Locked patterns sound clean and discordant patterns sound rough.
- Decoration does not change what the circuits do.

## Open Dials

- Ceiling base of 10 J and the band of 100 times per rank.
- Overrun of about 5 times and whether overcharge, craft quality and Highest quality stack or share one cap.
- Power source per rank and how intake size scales with the machine.
- Slopes: r = 0.125 per point of u and H_eff = 0.25 per point of u.
- Ring-up scale of 0.75 s per point of u.
- Layout efficiency of 0.16 at Lesser Lowest (0.4 at Intermediate is anchored by 125 versus 50 mana).
- Size of d per unlocked overlap.
- Whether T comes from wielder affinity or locale or both.
- Whether high-rank tones are audible to ordinary ears.
- Reconcile Debugger red/green/blue vision (`TempRunes.md`) with leaks (λ) and discord (d) as red faults.
