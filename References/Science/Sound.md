# Sound

Hub: `Science.md`. Bands / ozone: `Waves.md`. Cast law: `ManaCast.md`. Skills cap **L9**. Mana = J / (10 × η × μ); Mana/s = P / (10 × η × μ).

## Power equations

L = 10 log₁₀(I / I₀), I₀ = 10⁻¹² W/m²  
I = I₀ · 10^(L/10)  
Point source: I = P / (4 π r²)  
P = I₀ · 10^(L/10) · 4 π r²  
E = P · t  
Radiating surface: I = 2 π² ρ c f² ξ²  (ρ ≈ 1.2 kg/m³, c ≈ 343 m/s)

- Fixed ξ: intensity scales f² (higher pitch costs more energy).
- Fixed I: ξ scales 1/f (higher pitch needs less physical swing).
- **Q:** Q = 2π E_stored / E_dissipated per cycle = f₀ / Δf. Resonance gives ~Q× static amplitude for a given force → drive **force** toward a target amplitude falls ~1/Q. Energy to reach that stored energy is still paid. Hold power ≈ 2π f₀ E_stored / Q. Ring-up τ = 2Q / ω₀ (high-Q = cheap to drive, slow to fully excite).

**Air → tissue / water:** Z_air ≈ 412 rayl, Z_tissue ≈ 1.5 MRayl. Transmission T = 4 Z₁ Z₂ / (Z₁+Z₂)² ≈ **0.1%** (~**1000×** loss). Interior body effects need **contact or coupling medium** (gel, water, submerged). Add ~1000× mana if forcing an airborne interior effect anyway.

Example: 1 s at 120 dB, 5 m out → I = 1 W/m² → P ≈ 4π×25 ≈ **314 W** → **314 J** (~31 mana/s at ημ 1).

## Applications (potential)

### Whisper Beam (parametric / directional)

Modulated ultrasound that demodulates along a narrow beam (~3 dB per distance doubling vs 6 dB omnidirectional). Power vs omnidirectional shout ≈ (4π r²) / (beam cross-section) → often **100–1000×** less. Private battlefield whisper, bounce off a wall.

### Anti-Sound (ANC)

Emit inverse wave at the silence point. Cost ≈ generating that amplitude locally (same P formula on a small zone). Cancellable zone ~ fraction of a wavelength: **cheap at low f** (footsteps, hoofbeats, drums, siege rumble), **poor at high f** (sword ring, door click). Opposite cost profile from resonant shatter.

### Stone-Breaker / Inner Shatter

Focused ultrasound (lithotripsy / histotripsy). **Contact or coupling only.** Heal: stones, clots, small tumors. Harm: liquefy organ with no external mark. Armor, thick cloth or no touch counters. Hostile interior harm also faces living resistance (`Science.md` hub).

### Levitation Lattice

Standing-wave nodes trap objects ≲ λ/2 (~**4 mm** at 40 kHz). Hold-node power is modest (not destructive intensity). Apps: containerless alchemy droplets, suspend keys / gems / darts. Not person-scale.

### Sono-Alchemy

Cavitation in **liquid**: hot-spot chemistry, emulsify, strip contamination, ultrasonic weld of plastics / thin metal. Cost driver is **cavitation threshold intensity** of the fluid (surface tension, dissolved gas), then P and E = P·t over the cleaned area. Frequency sets bubble size / gentleness (higher f → smaller, safer on enamel/skin), not an automatic “ultrasound is expensive” multiplier. Real cleaners / scalers: tens to low hundreds of watts.

**Teeth (ultrasonic scaling):** ~25–30 kHz, ~**30 W** device-class draw (includes tool losses; total crown surface of 28 teeth is only ~**0.008–0.01 m²**, so a pure area×threshold rebuild could be lower). Mana/s = 30 / (10 η μ). INT 40 L2 (~21.9 J/mana) ≈ **1.4 mana/s**. Precision is the gate (over-amplitude tears gum). Self: water in own mouth. Other person: barrier tongue-depressor holds lips + contains water, then cavitate in the water.

**Blade blood / rust:** same threshold logic, larger area → low single-digit to low tens of mana per pass. Heavy oxidation costs more time, not a different school.

**Apps:** brew/emulsify potions and inks fast, clean wounds/blades, spot-weld rivets / jewelry / wire.

### Dry sonic cleaning

Not cavitation. Vibration overcomes particle adhesion (van der Waals on fine dust). Effective on dust / dry flakes / loose dirt. **Ineffective** on oils, sweat, grease (need solvent or true cavitation). Supplement to washing, not a full no-water shower unless the setting departs from the mechanism.

### Quickground

Vibrate water-saturated soil past a **threshold acceleration** → grains lose contact → temporary liquid (earthquake liquefaction / pile-driver analog). Same vibration on drier soil **compacts / hardens**. Apps: sink a charge line or siege tower; harden a muddy road for your own column. Low-f, high-ξ end of the intensity equations.

### Singing Flame (thermoacoustic)

Heat gradient ↔ high-amplitude sound, no moving parts (~30–41% of Carnot in real devices; runs reverse as a cooler). Tune a forge / campfire / Ember so waste heat feeds other sound apps when heat and acoustic scales match. Cross-link Insulation / Ember ↔ Sound.

### Resonant shattering

Brute fracture energy: E_punch = 1.5 × R × A × t (`ManaCast.md`). Resonance does **not** divide total energy by Q. Drive force / instantaneous mana rate falls ~1/Q; energy to reach fracture amplitude still paid. Practical model: total mana ≈ E_brute / (10 η μ), delivered over ring-up τ = 2Q/ω₀, with optional per-cycle loss ~(2π/Q)×E_stored. Glass/crystal Q ~**100–1000**; mana stones plausibly high-Q. High-Q = tiny looking draw, long wind-up.

### Echolocation (skill-gated, L9 cap)

Mana cheap (sound rates above). Bottleneck is attention / cortex. Caps at **L9**.

| Skill | Rough reps | Capability |
|---|---|---|
| L1 | — | Full attention; little else while active |
| L2–L4 | hundreds of pulses | Walk / defend; poor fight; miss fine detail |
| L5–L7 | thousands | Gross detection near-auto; attention for fine ID |
| L8–L9 | tens of thousands | Fully automatic spatial sense while fighting / casting |

Signature Recognition sub-skills from reps against specific cues (footsteps, voice, breath, heartbeat). Sighted casters compete with vision for the same processing unless eyes closed / blind (trained blind echolocators use visual cortex for the image).

### Sonic identification of structures

Low-energy diagnostic ping (single-digit mana or less at ημ 1 for a detectable return). Solid rings clean; crack / void / foreign mass shifts pitch, decay or splits peaks. Same L9 ladder as echolocation, specialized on structure types:

| Skill | Capability |
|---|---|
| L1 | Solid vs hollow only |
| L2–L4 | Material type + rough void size |
| L5–L7 | Cracks / seams / weak points for a follow-up shatter or compression strike |
| L8–L9 | Fine detail: natural flaw vs hidden trap / false wall / concealed lock |

Q sharpens frequency resolution. Air–stone is fine. Air–tissue interior still needs coupling.
