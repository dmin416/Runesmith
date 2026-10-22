# Sonic Air Displacement

> **Ideas / design loot.** Air pushed at or near the speed of sound. What it costs, what fires it can put out, how loud it is and what else it can do. Priced from kinetic energy and shock relations. Not automatic law.
>
> Live cast law: `../Runes/Energy.md`, `../World/Science/Energy/ManaCast.md`. Sound equations and air to tissue loss: `../World/Science/Energy/Sound.md`. Fan sizing: `../World/Science/Energy/FanAirflow.md`. Pricing rules, explosive compression and the 20 MP floor: `KineticSpellList.md`. Shock and hearing notes: `LightWarfareVariables.md` (variable 10). Air density with altitude: `../World/Science/Energy/ManaConcentration.md`.

## Conflicts (read first)

| Topic | Live lock | This idea |
|---|---|---|
| **1 MP = 10 J** | Locked (`Energy.md`) | Same |
| **Cast law** | Useful J = mana × 10 × η(L) × μ(INT) × A | Same. Tables show raw MP (ημ = 1) first then a caster table |
| **20 MP minimum** | No global floor | The `KineticSpellList.md` idea floor is applied in the MP columns. The joule columns show the true physics |
| **Explosive compression** | `(MP ÷ 25)²` is an idea rule | Used only in the explosive comparison rows |
| **Acoustic efficiency, fire speeds** | Not on any sheet | Design numbers below. Marked where they are assumptions |

Constants: air ρ = 1.2 kg/m³, c = 343 m/s, γ = 1.4, p₀ = 101.3 kPa (`Sound.md` uses the same ρ and c).

## What "sonic displacement" means

Three effects share the name.

1. **Jet.** Air kept moving at speed v through a nozzle or a barrier tube. Cost is a power in watts.
2. **Slug.** One block of air launched once. Cost is an energy in joules.
3. **Shock pulse.** A slug shoved hard enough that its front steepens into a shock. Same energy cost as the slug. The effect is overpressure.

**Mach 1 is already a blast.** Air cannot be driven to 343 m/s without a shock forming in front of it. Air moving at c behind the front means a shock at Mach 1.77 with 250 kPa overpressure (2.5 atm). Anything slower is a hard wind or a weaker shock. The cost curves below hold for both.

## Minimum power

```
Jet power      P = ½ × ρ × A × v³
Slug energy    E = ½ × ρ × V × v²
Dynamic press  q = ½ × ρ × v²
Mana           = J ÷ (10 × η × μ × A_ambient)
```

There is no absolute minimum. Power scales with nozzle area. What is fixed is the cost per area and per volume at a given speed.

| Speed | Mach | Dynamic pressure | Jet power per cm² | Jet power per m² | Raw MP/s per cm² |
|---|---|---|---|---|---|
| 5 m/s | 0.015 | 15 Pa | 0.0075 W | 75 W | 0.00075 |
| 20 m/s | 0.06 | 240 Pa | 0.48 W | 4.8 kW | 0.048 |
| 50 m/s | 0.15 | 1.5 kPa | 7.5 W | 75 kW | 0.75 |
| 100 m/s | 0.29 | 6 kPa | 60 W | 600 kW | 6 |
| 200 m/s | 0.58 | 24 kPa | 480 W | 4.8 MW | 48 |
| **343 m/s** | **1.00** | **70.6 kPa** | **2.4 kW** | **24.2 MW** | **242** |

**Sonic floor by nozzle:**

- 24 W per mm² (2.4 MP/s)
- 2.4 kW per cm² (242 MP/s)
- 24 MW per m²

A needle jet of 0.1 mm² at Mach 1 is only 2.4 W. A palm-sized 100 cm² jet at Mach 1 is 242 kW.

**Slug floor by volume:** Mach 1 air carries 70.6 kJ/m³ (70.6 J per liter, 58.8 kJ/kg).

| MP | Energy | Air at Mach 1 | As a ball | Mass of air |
|---|---|---|---|---|
| 20 (floor) | 200 J | 2.8 L | 18 cm wide | 3.4 g |
| 25 (Bolt rung) | 250 J | 3.5 L | 19 cm wide | 4.3 g |
| 50 | 500 J | 7.1 L | 24 cm wide | 8.5 g |
| 100 | 1,000 J | 14 L | 30 cm wide | 17 g |
| 300 (Mana Pulse rung) | 3,000 J | 42 L | 43 cm wide | 51 g |
| 400 (Mana Ball rung) | 4,000 J | 57 L | 48 cm wide | 68 g |
| 800 | 8,000 J | 113 L | 60 cm wide | 136 g |

So one Mana Bolt of mana buys a beach-ball-sized puff of air moving at the speed of sound. Air is light. A Mach 1 slug is cheap per liter and weak per kilogram.

### Caster cost

`J per mana = 10 × η(L) × μ(INT)`. Open ground, A = 1.

| Caster | J per mana | Mach 1 jet, mana/s per cm² | Mach 1 jet, 100 cm² | Mach 1 slug, mana per liter |
|---|---|---|---|---|
| INT 15, L1 | 3.0 | 807 | 80,700 | 23.5 |
| INT 15, L2 (raw) | 10 | 242 | 24,200 | 7.1 |
| INT 40, L2 | 21.9 | 110 | 11,000 | 3.2 |
| INT 40, L9 | 65.8 | 37 | 3,680 | 1.1 |
| INT 100, L9 | 136.9 | 18 | 1,770 | 0.5 |

A fledgling with about 200 MP holds under one second of a 1 cm² Mach 1 jet at raw cost. A slug is the realistic way to use sonic air. A sustained sonic jet is a late-game or machine-fed effect.

**Altitude:** cost is linear in air density. At 3,000 m (ρ ≈ 0.91) the joule cost is about 24% lower. Mana density rises with altitude and the ambient factor A helps further (`ManaConcentration.md`).

**Inside a fire:** hot gas has a higher sound speed (about 690 m/s at 1,200 K). Speed relative to the air matters for cost. Mach 1 relative to a flame is faster than 343 m/s.

### Real anchors

| Device | Jet power | Note |
|---|---|---|
| Handheld leaf blower | about 0.5 to 1 kW | 70 m/s over a large nozzle. Scatters coals and fans fires |
| Shop compressed air nozzle | low kW at choke | About Mach 1 at the tip. 100 to 115 dB at arm's length |
| Turbojet (about 25 kN thrust, 600 m/s exhaust) | about 8 MW | ½ × thrust × exhaust speed. Basis of the "Big Wind" oil fire rigs |

## Shock pulse table

Air pushed at piston speed u. Overpressure from the exact normal shock relations. Peak level uses 20 µPa. Above about 194 dB (1 atm) the number is a pressure, not a sound.

| Push speed u | Shock Mach | Overpressure | Peak level | Wind behind the front (q) | Effect |
|---|---|---|---|---|---|
| 2 m/s | 1.004 | 0.8 kPa | 152 dB | negligible | Candle snuffed |
| 10 m/s | 1.018 | 4.2 kPa | 167 dB | 0.06 kPa | Windows crack (about 1 to 7 kPa) |
| 20 m/s | 1.036 | 8.6 kPa | 173 dB | 0.25 kPa | Windows break. Loose shutters go |
| 50 m/s | 1.09 | 22.6 kPa | 181 dB | 1.7 kPa | Light panels and doors fail. Wind alone is 1.2 kN on a person |
| 75 m/s | 1.14 | 35 kPa | 185 dB | 4.2 kPa | Eardrum rupture threshold (about 35 kPa) |
| 100 m/s | 1.19 | 49 kPa | 188 dB | 7.9 kPa | Eardrums rupture. About 5.6 kN of wind on a person |
| 200 m/s | 1.41 | 117 kPa | 195 dB | 41 kPa | Lung injury range. About 29 kN of wind on a person |
| **343 m/s** | **1.77** | **250 kPa** | **202 dB** | **163 kPa** | Blast class. About 114 kN of wind on a person |

Weak shock rule: overpressure ≈ ρ c u = 412 Pa per m/s.

Wind force on a person assumes 0.7 m² frontal area and a drag coefficient of 1. Injury thresholds are rough and come from longer blasts. **A few-liter slug is only about a millisecond long** so it injures less than the table says. A slug hundreds of liters long meets the table. Making the pulse long is paid in volume (the slug table above).

## Sound it makes

### Jets

Acoustic power ≈ efficiency × jet power with efficiency ≈ 0.001 × M⁵ (nominal 0.1% at Mach 1). Choked or supersonic jets add shock noise that pushes it toward 0.5%.

Table is for a 1 cm² nozzle. Level at 1 m is free field (`Lp = Lw − 11`).

| Speed | Jet power | Acoustic power | Sound power level | Level at 1 m |
|---|---|---|---|---|
| 50 m/s | 7.5 W | 0.5 µW | 57 dB | 46 dB (quiet room) |
| 100 m/s | 60 W | 0.13 mW | 81 dB | 70 dB (loud conversation) |
| 200 m/s | 480 W | 32 mW | 105 dB | 94 dB (shout) |
| 343 m/s | 2.4 kW | 2.4 W | 124 dB | 113 dB (nominal) to 120 dB (shock noise) |

- Area ×10 adds 10 dB. Distance ×10 removes 20 dB.
- A palm-sized (100 cm²) Mach 1 jet is about 133 dB at 1 m. Pain starts near 130 dB.
- Character: a hiss rising to a roar. A choked jet adds a screech.

### Slugs and shock pulses

Treat the burst as sound radiated by a fraction `f` of the slug energy over a time `τ`. Design assumption: `f` = 5% and `τ` = 5 ms. Use the point source equation from `Sound.md`: `I = P / (4 π r²)`, `L = 10 log₁₀(I / 10⁻¹²)`.

| MP | Energy | Level at 1 m | At 10 m | At 100 m | At 1 km (no absorption) | Radius to 140 dB |
|---|---|---|---|---|---|---|
| 20 | 200 J | 142 dB | 122 dB | 102 dB | 82 dB | 1.3 m |
| 25 | 250 J | 143 dB | 123 dB | 103 dB | 83 dB | 1.4 m |
| 100 | 1,000 J | 149 dB | 129 dB | 109 dB | 89 dB | 2.8 m |
| 400 | 4,000 J | 155 dB | 135 dB | 115 dB | 95 dB | 5.6 m |
| 1,600 | 16,000 J | 161 dB | 141 dB | 121 dB | 101 dB | 11 m |

- Character: a crack or a bang. A Mana Bolt rung of air is a loud firecracker. Heard well past a kilometer on open ground.
- Walls and ground add up to about 6 dB. Air absorption trims the high pitch over distance.
- 140 dB is the usual impulse threshold for immediate hearing injury. 120 dB is uncomfortable. 130 dB is pain.
- **The caster is inside the radius.** At 25 MP the caster's own ears sit near the 140 dB line at 1.4 m. Guard options: a barrier shell around the ears, a nozzle that vents away from the head, or a low pitch anti-sound pulse (cheap at low frequency per `Sound.md`).

### Fire by sound alone

Plane wave particle speed `u = Δp / (ρ c)`. For a candle at 2 m/s rms:

- Pressure 824 Pa rms (152 dB)
- Intensity ρ c u² = 1.6 kW/m²
- A 0.1 m² source needs about 165 W. That is about 16.5 MP/s at ημ = 1

Low pitch works best because the same speed gives a bigger air swing (`ξ = u / 2πf`, about 6 mm rms at 50 Hz). Lab work on low-frequency sound (roughly 30 to 60 Hz) has put out small contained fires at close range. It does not scale to open large fires.

## Fires it can put out

### How a flame goes out

1. **Blow-off.** Air flowing past the flame strips heat and radicals faster than burning makes them. Works on small flames.
2. **Vapor flush.** A pulse carries the flame and the fuel vapor away from the fuel for a moment. The oil well method.
3. **Fuel scatter.** The fuel itself is blown apart or away.

**Wind also feeds fire.** A gentle flow over a campfire or a log bed adds oxygen and makes it burn harder. Only a fast, short push helps. A flame blown out can relight at once if the fuel is hot or the vapor is above flash point. Gasoline relights from a spark. Lamp oil and diesel are slower to relight.

### Design model

Flame buoyant speed scale `√(g × L)`. Blow-off needs a few times that. Candle: 0.63 m/s scale and about 2 m/s to blow out (a puff of breath).

```
Swept slug       V = 2 × W² × L        (W flame width, L flame height)
Energy           E = ½ × ρ × V × v²
Raw MP           = E ÷ 10  (apply the 20 MP floor and clean numbers)
Explosive route  MP = (E ÷ 10 × 625)^(1/3)   (idea rule, KineticSpellList.md)
```

Speeds above the candle are design assumptions, scaled with flame size and stiffened for fuel that relights.

| Fire | Heat output | Flame (W × L) | Air speed at fire | Swept volume | Energy | Kinetic slug MP | Explosive route MP | Result |
|---|---|---|---|---|---|---|---|---|
| Candle, match or lamp wick | about 0.1 kW | 1 × 4 cm | 2 m/s | 8 mL | 0.00002 J | **20** (floor) | 20 (floor) | Out |
| Torch (rag or pitch) | about 10 kW | 15 × 40 cm | 8 m/s | 18 L | 0.7 J | **20** (floor) | 20 (floor) | Out. Tar torches resist |
| Campfire | about 100 kW | 0.8 × 0.7 m | 50 m/s | 0.9 m³ | 1.3 kJ | **150** | 50 | Flame out. Coals live and scatter. Relights |
| Pool fire, 1 m² (diesel or oil) | about 2 MW | 1.1 × 4 m | 100 m/s | 10 m³ | 61 kJ | **6,100** | 150 | Out if the liquid is cool enough not to relight |
| Pool fire, 10 m² | about 20 MW | 3.6 × 9 m | 150 m/s | 230 m³ | 3.1 MJ | **310,000** | 600 | Same. Only the explosive route is affordable |

**Pattern:** kinetic air costs rise with swept volume × speed². Past a campfire the explosive compression route is far cheaper. This is why the real world uses dynamite on large fires.

### Beyond the table

| Fire | Heat output | Verdict |
|---|---|---|
| House or room fire | 5 to 50 MW | A blast knocks the flame out of the room for seconds. Fuel and embers remain. Relights. Not an extinguisher |
| Wildfire front | 1 to 100 MW per meter of front | Cannot be blown out. Fuel breaks and removal only |
| Oil or gas well blowout | about 0.5 to 1 GW | The flame is a momentum jet. Needs a Mach 1 class blast at the base |

**Well fire anchors:**

- Dynamite method: a charge of a few hundred kg of explosive, commonly cited as about 250 kg for one famous 1962 fire. In idea pricing 1 kg of TNT is about 640 MP and 250 kg is about 4,000 MP as one explosive spell. Lethal radius is MP × 0.005 m, about 20 m.
- Jet engine method: about 8 MW of jet power for minutes. At ημ = 1 that is 800,000 MP/s. A caster would run it with a mana stone bank or a machine, not a pool.

### Quick cost ladder (raw MP)

| Goal | Spell | Raw MP |
|---|---|---|
| Snuff candles, a lantern, a match | One Mach 1 puff | 20 (floor) |
| Flame out on a campfire | 50 m/s sweep | 150 |
| Kill a 1 m² oil pool fire | Explosive route | 150 |
| Kill a 10 m² oil pool fire | Explosive route | 600 |
| Kill a well fire | Explosive route | about 4,000 |

## Potential

- **Pinch snuff.** One 20 MP puff for candles and lamps from across a room. A cheap stealth tool for darkening a room.
- **Air knife.** A 50 to 100 m/s thin jet (0.75 to 6 MP/s per cm²) cleans dust and chips, dries blades and clears sawdust from a cut.
- **Smoke and gas clearing.** 1 to 3 m/s over a 1 m² doorway is only about 1 to 16 W. A cheap draft to clear a cellar or a forge hall.
- **Fire break pulse.** Knocks the flame off a small blaze long enough to stamp it out. Pair with cooling for embers.
- **Air cannon.** A free slug rolls itself into a vortex ring that travels many diameters before it fades. A barrier tube keeps a Mach 1 slug coherent all the way to the target.
- **Whip crack.** The cheapest sonic boom. A bullwhip tip of 0.5 to 1 g at about 350 m/s carries 31 to 61 J. That is 3 to 6 MP raw and the 20 MP floor in practice. The crack is the tip's own shock.
- **Stun bang.** A 100 MP slug is about 149 dB at 1 m from the burst and about 140 dB at 2.8 m. Rings ears and staggers. Hearing damage is real and permanent at the high end.
- **Sonic Lance and Sonic Boom.** The `Ideas.md` names are a narrow jet or a directed slug. The jet table and the shock table price both.
- **Alarm horn.** 100 W of acoustic output is about 130 dB at 1 m and still about 70 dB at 1 km before absorption. Rune horns can span a valley.
- **Anti-sound.** The reverse of everything above. Cancels low pitch footsteps and hooves cheaply. Poor at high pitch (`Sound.md`).
- **Kiln, forge and bellows draft.** A steady 2 to 5 m/s stream at fan scale (`FanAirflow.md`) outdoes a person with a bellows for almost no mana.

## Limits and hazards

### Poor at shoving bodies

To launch an 80 kg person to 2.5 m/s with air that stops against them the slug must carry that momentum (200 kg m/s). The energy is `½ × p × v`, so the faster the air the worse the deal.

| Slug speed | Air mass | Energy | Raw MP | Versus Mana Push (25 MP) |
|---|---|---|---|---|
| 10 m/s | 20 kg | 1,000 J | 100 | 4× |
| 20 m/s | 10 kg | 2,000 J | 200 | 8× |
| 50 m/s | 4 kg | 5,000 J | 500 | 20× |
| 100 m/s | 2 kg | 10,000 J | 1,000 | 40× |
| 343 m/s | 0.58 kg | 34,300 J | 3,430 | 137× |

Sonic air is for speed, area, fire and sound. Mana Push is the right shove.

### Other limits

- **Air to tissue loss.** Sound in air barely enters the body (about 0.1% transmits). The eardrum and lungs are exposed to air and still take the blast. Organs behind skin do not take a pure airborne tone (`Sound.md`).
- **Backdraft and flashover.** Pushing fresh air into a sealed hot room can make it flash.
- **Embers and burning liquid.** A blast scatters coals and sprays burning oil or grease. A kitchen grease fire becomes a spray.
- **Smoke and heat go with the air.** The blast moves them onto bystanders.
- **Reignition.** The fire is out for a moment only unless the fuel is cooled or the flash point is safe.
- **Position giveaway.** A Mach 1 slug is audible to a kilometer.
- **Range.** A free slug loses speed within a few of its own diameters. Longer reach needs a barrier tube or a vortex ring.
