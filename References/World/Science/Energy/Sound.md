# Sound

Hub: `../Science.md`. Bands / ozone: `Waves.md`. Cast law: `ManaCast.md`. Skills cap **L9**. Mana = J / (10 × η × μ); Mana/s = P / (10 × η × μ). Ultrasonic dryer tone vs echolocation: `QuietBlowDryer.md`. D's vibration-sense goal: `../../../../People/Roland/Goals.md`.

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

## Speed

Round trip for a there-and-back echo: t = 2d / c. Wavelength: λ = c / f (`Waves.md`).

**Air.** Dry air at sea level depends on temperature, not pressure. c ≈ 331 + 0.6 T(°C). **0 °C → 331 m/s. 20 °C → 343 m/s. 40 °C → 355 m/s.** Moist air is a little faster, on the order of 1 m/s. Cabin clicks and the radiating-surface formula use **343 m/s**.

**Water.** Fresh water at **20 °C ≈ 1,480 m/s** (~**4.3×** air). About **1,400 m/s** near freezing and about **1,530 m/s** at 40 °C. Seawater is a little faster, about **1,520 m/s**. Soft tissue sits in the same band, about **1,540 m/s**. Speed is close to flesh. The loss above is the impedance jump, not the speed.

**Ground.** Solids carry three waves. Compression (P) is what "speed of sound in rock" means. Shear (S) does not travel in air or water and runs about half to three-fifths of P in rock. Surface waves (what a footfall and a floorboard are) run a little under S.

| Path | Speed | 10 m echo |
|---|---|---|
| Dry air, 20 °C | 343 m/s | 58 ms |
| Fresh water, 20 °C | ~1,480 m/s | ~14 ms |
| Seawater | ~1,520 m/s | ~13 ms |
| Loose soil, surface wave | ~100–300 m/s | ~70–200 ms |
| Loose dry soil, compression | ~200–800 m/s | ~25–100 ms |
| Water-filled soil, compression | ~1,500 m/s | ~13 ms |
| Sedimentary rock, compression | ~2,000–4,500 m/s | ~4–10 ms |
| Granite / basalt, compression | ~5,000–6,500 m/s | ~3–4 ms |
| Wood, along the grain | ~3,000–5,000 m/s | ~4–7 ms |
| Cortical bone, along the shaft | ~3,000–4,000 m/s | ~5–7 ms |
| Steel bar | ~5,100 m/s | ~4 ms |

Solid rock compression at **3,000–6,000 m/s** is the combat shorthand (**10–15×** air): `../../../Combat/LightWarfare.md`. Soft ground is the exception. A surface wave in loose soil can be **slower than air**. Fill that soil with water and the compression wave jumps toward water speed. The shear and the surface wave stay slow.

Wood across the grain is slower than along it, closer to **1,000–2,000 m/s**. A steel bar is the thin-rod speed. Bulk steel is closer to **5,900 m/s**. No acoustic speed is locked for mythril, star steel, orihalcum, aurium, or adamantium.

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

Heat gradient ↔ high-amplitude sound, no moving parts (~30–41% of Carnot in real devices; runs reverse as a cooler). Tune a forge / campfire / Heat so waste heat feeds other sound apps when heat and acoustic scales match. Cross-link Heat and `../Body/Body.md` heat stealth ↔ Sound.

### Resonant shattering

Brute fracture energy: E_punch = 1.5 × R × A × t (`ManaCast.md`). Resonance does **not** divide total energy by Q. Drive force / instantaneous mana rate falls ~1/Q; energy to reach fracture amplitude still paid. Practical model: total mana ≈ E_brute / (10 η μ), delivered over ring-up τ = 2Q/ω₀, with optional per-cycle loss ~(2π/Q)×E_stored. Glass/crystal Q ~**100–1000**; mana stones plausibly high-Q. High-Q = tiny looking draw, long wind-up.

### Echolocation → Vibration Sense → Energy Sense

Mana cheap (sound rates above). Bottleneck is attention / cortex. Each name hard-caps at L9. Evolve at **2,000,000** clean uses. Echolocation reads sound returns. Vibration Sense reads the same returns through skin and hair, and through the ground. Energy Sense is the next evolve: a general read of whatever carries energy (heat, mana, living fields), not one animal trick. Rank card: `../../../Progression/SkillsDesign.md`. Chapter 19 needle-catch drill uses **one click every ~4 s** (~**22,000**/week → Sound / Echo **L7**) and Breath Control: `../../../../Story/Notes/Skills.md`. Ideas alt names (Sonar / Resonance) and √M / M^1/4 tables: `../../../Progression/SensingManaSoundSystem.md` (live evolve names stay Vibration / Energy Sense).

Q sharpens frequency resolution. Air–stone is fine. Air–tissue interior still needs coupling. A 10 m return is ~58 ms in air, ~14 ms in water, and a few milliseconds through rock. Loose soil can be slower than the air click. A few seconds between clicks is enough to read a cabin-scale return and still leave attention for other work.
