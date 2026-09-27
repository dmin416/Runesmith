# Mana Energy Baseline

Electricity is the physical model for how mana moves. Mana is not electricity. Its conductivity ranking differs (section 2).

**Related:** spell cast joules with skill η and INT μ live in `../Science/ManaCast.md` (`1 mana ≈ 10 J` paid, Useful = mana × 10 × η × μ). This file is the **path / ambient / wear** baseline (cost × **10 J** × path efficiency × ambient gain). Resonant runes replace η and G with η_eff and H_eff from `RuneSystem.md`. Setup pour costs live in `RuneSetup.md` and do not add heat or strain. **10 J per mana is the locked standard** for cast and path formulas.

---

## 1. Electrical Reference (physics)

**Relations:** V = I × R. P = V × I = I² × R. E = P × t. R = ρ × L / A. Capacitor E = ½ C V². Inductor E = ½ L I².

**Transmission**
- Charge carriers drift under 1 mm/s. The push travels as a field wave at a large fraction of light speed. Mana analog: an impulse crossing the material is enough.
- Flow needs a potential difference and a closed path. An open end builds potential until the gap breaks down as a spark or arc (dry air about 3 kV/mm, damp or dirty surfaces less).
- Field concentrates at points and thin edges (lightning rods, corona discharge). An open end discharges first at a point.

**Heat**
- Joule heating P = I² R. Doubling flow quadruples heat. A conductor settles where heat generated equals heat shed.
- Metals resist more when hot (copper about 0.4 percent per K) so overheating runs away. Steel adds magnetic losses under fast-varying flow.
- Levers: thicker, shorter, better material, or higher potential with lower flow (needs better insulation).

**Storage and burst**
- Capacitor dumps in under a millisecond. Inductor spikes voltage when cut. Battery releases slowly.
- Slow charge then fast dump lets a small conductor deliver a violent release. The conductor carries only the charging flow.
- An arc dumps energy into a small air volume in microseconds and the air expands as a shock wave (thunder). No fuel needed. About 30 J to 1 kJ covers a firecracker to a small firework.

**Conversion at a load:** resistive element to heat. Filament to heat and light. Motor to motion. Coil to magnetic field. Arc to light, heat and shock. Every conversion wastes part of the input.

**Electrical resistivity (ohm-m, physics reference only):** silver 1.6e-8. copper 1.7e-8. gold 2.4e-8. brass 6e-8 to 9e-8. iron 1.0e-7. tin 1.1e-7. bronze about 1.5e-7. carbon steel 1.4e-7 to 2.0e-7. lead 2.2e-7. stainless about 7e-7. graphite about 1e-5. dry wood, paper, leather and glass 1e9 or more.

---

## 2. Mana Conductivity (canon)

Metals from worst to best: **iron, copper, steel, dark steel, mana steel, mythril, adamantium.** Worse paths waste more of the cost and strain faster. Better paths carry heavy flow with little waste.

The human body conducts at about 90 percent efficiency, between dark steel and mana steel (section 10). Monster blood is proposed at the same value and its placement stays open (section 12).

- The wielder's body conducts well so the wielder can be source or return.
- Scroll ink uses monster blood or other mana materials for a low-resistance trace. Ordinary or iron-based ink resists strongly.
- Longer or thinner paths resist more. A thin line of a poor conductor heats fiercely.
- Not yet placed: silver, gold, bronze, brass, tin, lead, bone, hide, scales, hemolymph.

---

## 3. Cost, Efficiency and Ambient Gain

Cost comes first and is fixed. A 100 mana spell costs 100 mana and a 50 mana spell costs 50 mana. Path material, environment, ambient mana and efficiency never change it. They only change output energy and waste.

**Output = cost × 10 J × path efficiency × ambient gain**

Reference: 100 mana paid is 1000 J at the converter input. Copper (80 percent) in a closed system delivers **800 J** useful and **200 J** waste. Cast-law Useful joules (`../Science/ManaCast.md`) use the same 10 J unit with spell η(L) and μ(INT) instead of path η.

Figures here assume a clean linear rune (Lesser Highest). Rune rank and grade replace path efficiency and ambient gain with η_eff and H_eff. Formula: rune file, Harmonics and Resonance (when locked).

The converter draws ambient mana from the air and land. An open system has a large reservoir. A closed pattern with no intake is self-constrained and gets gain 1.

| Path | Efficiency (proposed) | Output per 100 mana (gain 1) | Waste per 100 mana | Strain capacity (kJ waste per kg, proposed) |
|---|---|---|---|---|
| Iron | 60 percent | 600 J | 400 J | 70 |
| Copper (reference) | 80 percent | 800 J | 200 J | 140 |
| Steel | 85 percent | 850 J | 150 J | 210 |
| Dark steel | 88 percent | 880 J | 120 J | 280 |
| Mana steel | 92 percent | 920 J | 80 J | 560 |
| Mythril | 95 percent | 950 J | 50 J | 1120 |
| Adamantium | 98 percent | 980 J | 20 J | 2240 |
| Human body | 90 percent | 900 J | 100 J | burst tolerance only (section 10) |
| Monster blood | 90 percent (placement open) | 900 J | 100 J | not set |

**Waste works like a gun.** A gun wastes most of its propellant energy yet still delivers high force. Here waste leaves two ways. Most exits with the discharge. The rest stays in the path as heat (proposed 50 percent of waste). Waste also strains the path directly (section 7). Ambient gain acts at the converter after the path so it adds output and adds no waste.

| Environment | Gain (proposed) |
|---|---|
| Sealed or warded space | 1 |
| Indoors | 1.5 |
| Open air | 3 |
| Mana-dense area | 6 |
| Recently drained area | 1 to 1.5 |

- Extra output comes from ambient mana so energy is conserved. Ambient mana enters at the converter and never crosses the pathway.
- Ambient mana is finite and locally depleted by use. It recovers as mana spreads in. Rapid recasting in one spot trends toward gain 1.
- Draw is capped by intake size and local density.

---

## 4. Caster Pools and Recovery

Cost is identical from either pool. Stamina is the smaller pool so the same cost tires the body more. Stamina also runs breathing and muscle while mana does not.

Example pools for an adult man: mana 2000, stamina 300 (proposed).

| Cost | Share of mana | Share of stamina |
|---|---|---|
| 50 | 2.5 percent | 17 percent |
| 125 | 6.3 percent | 42 percent |
| 150 | 7.5 percent | 50 percent |

**Mana recovery (proposed).** Mana returns from the ambient supply through skin and lungs. It works like an attractive force pulling through an opening: the larger the force the faster the recovery. Empty to full takes T = 9 hours in open air for every body.

| Analogy | What it contributes |
|---|---|
| Gravity | Pull grows with the attracting mass. More internal mana means a stronger pull. |
| Magnetism | Flux through a surface is field strength times area. The field comes from the internal mana and permeability sets how well flux passes. |
| Vacuum | Suction draws the surroundings in through an opening. The opening's area caps the flow. |

| Term | Limits | Symbol |
|---|---|---|
| Force | How hard the tank pulls. Internal mana plus a baseline pull. | F = M + b × P |
| Absorptive surface | How much can enter. Skin and lungs relative to an adult man of 175 cm. | S = (height / 175 cm)² |
| Permeability | How well mana passes through tissue, in adult-man equivalents. | Rob |

**Rate (mana/h) = k × S × Rob × F = a × (M + b × P)** with a = k × S × Rob and k = 0.25 per hour.

- M: current mana. P: maximum mana, set by intelligence.
- **b = 1 / (e^(a × T) − 1)** is the baseline pull as a fraction of P. It fixes empty to full at exactly T for any S, Rob and P.
- Time to full from M = ln((P + b × P) / (M + b × P)) / a hours.
- Absorption speeds up at every fill level. Larger S × Rob gives a smaller baseline pull and a sharper rise as the tank fills.

Adult man (S = 1, Rob = 1, a = 0.25, P = 2000):

| Start fill | Rate | Time to full |
|---|---|---|
| 0 percent | 59 mana/h | 9 h |
| 10 percent | 109 mana/h | about 6.5 h |
| 30 percent (70 percent drained) | 209 mana/h | about 4 h |
| 50 percent | 309 mana/h | about 2.4 h |
| 70 percent | 409 mana/h | about 1.3 h |
| 90 percent | 509 mana/h | about 0.4 h |

- Rate at a given fill scales with P. Times do not depend on P.
- Environment scales T by 3 / gain: sealed 27 h, indoors 18 h, open air 9 h, mana-dense 4.5 h. A recently drained area recovers slowly.

---

## 5. Fire's Energy Is Not the Spell's Energy

- 1 kg of dry wood holds about 16 MJ. A 150 mana spell through steel in open air outputs about 4.8 kJ, roughly 1/3300 of that.
- A fire spell is an ignition source. With fuel present the fuel's own energy follows and is not part of the spell. With no fuel the fire is capped by the spell's output.
- Cost is never scaled by how energetic fire is in general.

---

## 6. Scale Ladder

Output at the reference path in a closed system. Multiply by gain for other environments.

| Cost | Output | Comparable |
|---|---|---|
| 3 | 30 J | Ignites a small patch of paper |
| 10 | 100 J | Hunting bow shot (arrow motion 60 to 120 J) |
| 100 | 1 kJ | One burning match (about 1 BTU) |
| 200 to 500 | 2 to 5 kJ | Large firework burst |
| 10,000 | 100 kJ | About 25 g of TNT |

---

## 7. Wear and Failure

**Strain is the primary wear. Heat is secondary.**

- **Strain (corruption).** Waste energy passing through a path damages it directly at any temperature. Path life in casts = mass × strain capacity / waste per cast. Strain shows as dulled or mottled metal and rising resistance with no heat tint. Damaged paths lose efficiency which raises waste which raises strain. Sharp corners and narrow sections concentrate strain.
- **Heat.** Retained heat raises temperature and speeds strain. Heat damage follows the stages below. Each component has a rated flow at a safe steady temperature.
- **Burst limit.** A single cast fails the first section whose waste per kg exceeds its burst tolerance. Waste concentrates in narrow sections and small masses so those fail first. Metals: 4 percent of strain capacity per cast (iron 2800 J/kg to adamantium 89,600 J/kg, proposed). Living tissue: about 430 J/kg (section 10).

| Stage | Effect | Threshold |
|---|---|---|
| 1. Warming | Retained heat | Under 100 C |
| 2. Material damage | Wax and resin soften. Steel loses temper. | Wax 50 to 70 C. Steel 200 to 400 C. |
| 3. Ignition | Organics burn | Paper about 230 C. Wood 250 to 300 C. Cotton about 250 C. |
| 4. Melting | Metal separates | Tin 232 C. Lead 327 C. Copper 1085 C. Steel 1370 to 1500 C. |
| 5. Vaporization | Thin conductor hit by a large pulse (a fuse) | Depends on mass and pulse |
| 6. Breakdown | Arc through air or an insulator | Dry air about 3 kV/mm |

Other wear: thermal cycling fatigues joints and bends. Oxidation adds surface films that raise resistance. Loose or dirty joints heat first.

---

## 8. Mapping

| Electricity | Steam | Mana |
|---|---|---|
| Voltage | Boiler pressure | Mana potential |
| Current | Flow rate | Mana flow |
| Resistance | Narrow or rough pipe | Material mana resistance |
| Conductor | Pipe | Mana-conductive material |
| Insulator | Seal | Mana-blocking material |
| Source | Boiler | Wielder, magic stone or ambient supply |
| Capacitor or battery | Sealed tank | Magic stone or reservoir |
| Load | Piston | Rune converter stage |
| Fuse | Safety valve | Sacrificial trace such as a scroll |
| Ground | Vent | Dissipation into air, earth or water |
| Waste | Exhaust | Waste (heat and strain) |

---

## 9. Worked Cases

### A. Fire arrow (100 mana, copper, closed system: 1000 J)

Open air (gain 3) triples every energy figure and multiplies speed by about 1.7. Speed v = √(2E / m) at 20 g. A bow arrow flies at 60 to 90 m/s.

| Split | Motion | Heat | Speed |
|---|---|---|---|
| Slow and hot | 50 J | 950 J | about 70 m/s |
| Balanced | 100 J | 900 J | about 100 m/s |
| Fast | 250 J | 750 J | about 160 m/s |
| Very fast and cool | 500 J | 500 J | about 225 m/s |

Balanced split at the target:
- Dry wood needs about 240 J per cm³ to reach ignition so 900 J covers 3 to 4 cm³.
- Flesh at 3.5 J/g/K: 10 g rises about 26 K (past the 60 C damage threshold). 3 g rises about 86 K and chars.
- Heat alone rarely kills. The motion pierces and the flame ignites cloth, hide, wood, thatch and hair.
- A 2 kg steel breastplate rises under 1 K. Plate ignores the fire. Only the motion matters against it.
- Energy scales linearly with cost and gain. Heat delivered falls with distance so range is a heat budget.

### B. Sword explosive spell (150 mana, open air, gain 3)

Feed line runs down the blade and the emitter sits at the tip where potential concentrates. The burst converts stored charge into a rapid discharge that heats and expands the air at the tip. Burst energy goes into the air. The blade takes strain from waste and heat from the retained half (1 kg blade at 490 J/K, no cooling).

| Blade path | Efficiency | Output (gain 3) | Output sealed (gain 1) | Heat per cast | Casts to strain limit |
|---|---|---|---|---|---|
| Iron | 60 percent | 3375 J | 1125 J | 0.77 K | about 90 |
| Copper | 80 percent | 4500 J | 1500 J | 0.38 K | about 370 |
| Steel | 85 percent | 4781 J | 1594 J | 0.29 K | about 750 |
| Dark steel | 88 percent | 4950 J | 1650 J | 0.23 K | about 1200 |
| Mana steel | 92 percent | 5175 J | 1725 J | 0.15 K | about 3700 |
| Mythril | 95 percent | 5344 J | 1781 J | 0.10 K | about 12,000 |
| Adamantium | 98 percent | 5513 J | 1838 J | 0.04 K | about 60,000 |

- Strain limits a blade long before heat does. Iron reaches 190 K of heat after about 250 casts with no cooling and its strain limit is about 90.
- A rounded or damaged tip concentrates less and weakens the burst. A film of blood or other mana material on the blade lowers surface resistance. Grip material sets how much flow passes from the wielder into the blade.

### C. Scroll that bursts into flame

Paper carries no meaningful mana flow so flow follows the ink line. A thin trace concentrates power in a tiny mass and paper conducts heat poorly. About 30 J into 0.1 g of paper reaches ignition (about 230 C). A 3 mana scroll delivers about 30 J at the reference rate and about 90 J in open air.

The scroll is a fuse that is also the load. It burns when flow exceeds what the trace carries and it is single-use by nature. Stronger or fresher monster blood or mana steel, mythril or adamantium powder in the ink delays ignition. Wider traces spread heat. Mineral-treated paper resists ignition longer.

### D. Enchanted metal plate

Plate life is set by strain first. Life in casts = mass × strain capacity / waste per cast so a thicker plate and a better metal last longer. Iron fails first. Copper and steel last moderately. Dark steel and mana steel last long. Mythril and adamantium are effectively permanent.

Heat is secondary. Retained heat warms the plate each use and speeds strain. Narrow sections and sharp corners are hot spots. A corrupted plate looks dulled or mottled. It loses efficiency and runs warmer than before. Eventually a joint loosens or a section opens. Running below the rated flow lasts far longer. Repair means re-plating the pattern or replacing fittings.

### E. Copper paddle firing fire arrows (story case)

Assumptions: a copper plate slightly smaller than a tennis racket at about 0.45 kg (heat capacity about 180 J/K for any metal at this mass) with 100 mana per arrow. Retained heat is half of waste. Ambient gain adds output and does not change waste.

| Paddle metal | Waste per arrow | Heat per arrow | Arrows to strain limit |
|---|---|---|---|
| Iron | 400 J | 1.1 K | about 79 |
| Copper | 200 J | 0.6 K | about 315 |
| Steel | 150 J | 0.4 K | about 630 |
| Dark steel | 120 J | 0.3 K | about 1050 |
| Mana steel | 80 J | 0.2 K | about 3150 |
| Mythril | 50 J | 0.14 K | about 10,000 |
| Adamantium | 20 J | 0.06 K | about 50,000 |

Copper: many arrows fly before the plate is warm (about 60 rapid arrows for 35 K) and hot (about 120 for 70 K). The plate sheds heat to the air between volleys. The strain limit arrives near 315 arrows. Corruption is the main cause of damage and heat only speeds it.

---

## 10. Human Body as a Path

The body conducts like a fine metal (90 percent efficiency, **100 J** of waste per 100 mana) and breaks like flesh. Living tissue tolerates about 430 J of waste per kg of section per cast (proposed) against 2800 to 89,600 J/kg for metals.

- Waste concentrates in narrow sections and at the emitter. Proposed shares: torso and shoulder 15 percent, upper arm 15, forearm 20, wrist and hand 50.
- A cast fails the first section whose waste per kg exceeds tolerance. Limits scale linearly with robustness.
- Injury is strain (corruption). Heat is negligible: at 500 mana the hand retains about 125 J which warms 0.72 kg of tissue by about 0.05 K.
- Tissue below its limit is assumed to recover. Above the limit it takes lasting damage.

**Character at 1.3 adult men, 500 mana burst (500 J total waste)**

| Section | Mass | Share | Waste | Load per kg | Mana to reach 430 J/kg |
|---|---|---|---|---|---|
| Torso and shoulder | 13 kg | 15 percent | 75 J | 6 J/kg | about 37,000 |
| Upper arm | 2.6 kg | 15 percent | 75 J | 29 J/kg | about 7500 |
| Forearm | 1.56 kg | 20 percent | 100 J | 64 J/kg | about 3400 |
| Wrist and hand | 0.72 kg | 50 percent | 250 J | 347 J/kg | about 620 |

- Every cast below about 620 mana loads the hand under tolerance and the rest of the body far under it.
- At about 620 mana the wrist and hand reach tolerance and injury begins. At about 1240 mana the hand loads at double tolerance and is mangled while the forearm stays intact.
- Robustness is in adult-man equivalents for a 140 cm body and scales with height cubed as he grows (210 cm is 3.4 times).
- Output at 90 percent: 500 to 1000 mana yields about 4.5 to 9 kJ in a closed system and about 13.5 to 27 kJ in open air.
- Fix: place a high-tolerance metal in the final section so the peak waste lands in metal. A 0.5 kg mythril focus tolerates about 22 kJ of waste per cast.

**Instantaneous channel limit.** Mana expands and contracts explosively so a cast is not limited by intake or recovery. Three things limit it: mental focus, robustness and the tissue's capacity to withstand.

- **Focus cap = 473 × Foc** mana in one instant. Foc is mental focus in adult-man equivalents and does not scale with body size. A cast also cannot exceed current mana M.
- **Physical cap = (430 J/kg × 0.55 kg × Rob) / (0.5 × 10 J × (1 − η))** mana at the hand, about **473 × Rob** for the human body (η = 0.90). Tissue tolerance, hand mass and hand waste share set the top. Conductivity sets the waste per mana so higher η raises the cap. Injury begins at the cap and the hand is mangled at twice the cap.
- **Safe channel = min(focus cap, physical cap).** Channeling between the physical cap and the focus cap is possible and injures. Above the focus cap the cast cannot be held and fizzles (proposed).

**Focus-formed channels (rare).** A mage with a weak body and overwhelming intellect and focus can form mana channels through the body along the path to the emitter. Few can. Channels are insulated pipes made of mana. Mana on mana wastes far less than any metal and the pipe holds its waste so little reaches the tissue.

- **Channel efficiency η_ch = 0.99** (proposed).
- **Physical cap with channels = 473 × Rob × (1 − η_body) / (1 − η_ch) = 4730 × Rob** mana. Ten times the bare cap.
- **Focus upkeep:** the pipes take a quarter of focus (proposed) and leave 0.75 × the focus cap to hold the cast.
- **Safe channel with channels = min(0.75 × 473 × Foc, 4730 × Rob)** while focus holds. Example: Rob 0.3 and Foc 3 give a bare cap of about 142 and a safe channel of about 1064 with channels.
- **Rebound.** If focus breaks or the mana in the channel runs out the pipe collapses and half of the carried energy discharges into the tissue (proposed). Severity = 0.5 × mana in the channel / bare physical cap. Below 1 is harmless. Injury begins at 1 and the hand is mangled at 2. The example carrying 1064 has a severity of about 3.75 and the limb is destroyed. Lower loads rebound proportionally less.

---

## 11. Rules

1. Cost is fixed by the spell. Path, material, environment and efficiency change output and waste and never the cost.
2. Output never exceeds converter input plus ambient mana drawn.
3. Flow needs a potential difference and a path. Every material has a conductivity rank and every path an efficiency below 100 percent.
4. Waste leaves with the discharge or stays in the path as heat. Waste also strains the path directly.
5. Strain is the primary wear and heat is secondary. Heat damage follows the section 7 thresholds. A single cast also fails the first section whose waste per kg exceeds its burst tolerance.
6. Points and thin edges concentrate potential. Stored energy releases far faster than it was stored.
7. Ambient mana is finite and locally depleted and recovers over time. A closed pattern with no intake gets no gain.
8. Fire's own chemical energy is not part of the spell.
9. Cost is identical from mana or stamina. Stamina is the smaller pool so it tires the caster faster.
10. Mana absorption rises with the mana already in the tank. Empty to full takes 9 hours in open air for every body.
11. Instantaneous channel is capped by mental focus and injures above the physical cap set by robustness and tissue tolerance.
12. Focus-formed channels (rare) carry mana in mana with little waste and raise the safe channel above the physical cap while focus holds. Loss of focus or an emptied channel rebounds part of the carried energy into the tissue.

---

## 12. Open Dials

- Return path: closed loop through the wielder or one-way dissipation at the load.
- Storage: whether magic stones act as capacitors (fast dump) or batteries (slow release) or both by grade.
- Potential scale: higher potential lowers waste but needs better insulation. Set how high craftsmen can push it.
- Ambient mana: gain per environment, recovery rate after a cast, intake size limit per rune grade.
- Waste split: share retained as heat (proposed 50 percent).
- Strain capacity per kg for each metal (proposed values in section 3).
- Pools: maximum mana is set by intelligence and is not modeled here. Stamina size and stamina recovery. Mana recovery constant k (0.25 per hour) and open-air empty-to-full time T (9 h).
- Skills system: skill level could raise efficiency and strain capacity without breaking conservation.
- Human path: tissue burst tolerance (430 J/kg proposed), waste share per section and strain recovery rate.
- Body growth: robustness scales with height cubed from the 140 cm baseline and continues past 210 cm (proposed).
- Focus: mana per 1.0 Foc (**473** proposed) and the fizzle rule above the focus cap.
- Channels: efficiency (0.99), focus upkeep (0.25) and rebound share (0.5), all proposed.
- Placement of monster blood in the metal order. The human body is set at 90 percent.
- Unplaced materials: see section 2.
