# Energy Pumping

> **Design loot / Earth physics.** Pump instead of produce. Moving heat, water, molecules and charge that already exist costs far less than making them. Not automatic law.
>
> Cast law: `../../../Runes/Energy.md`, `ManaCast.md`. Mana Hands pricing and the braking rule: `ManaHandPhysics.md`. Water lift and taps: `Pumps.md`. Compress / expand cycles: `Compression.md`. Vacuum and latent heat: `../Metallurgy/Vacuum.md`. Sorting by spin: `Spin.md`. Pressure and concentration drives: `Gradients.md`. Fluid layers: `Shear.md`.

## Shared cost law

- **1 MP = 10 J.** Raw MP below is J ÷ 10. A real caster divides by η(L) × μ(INT) × A for spells or pays the Hands rate with waste R (`ManaHandPhysics.md`).
- **Stopping costs the same as starting.** Damping motion pays the full energy removed, the same as putting it into motion. No refunds (`ManaHandPhysics.md` §10). A pump that slows a fluid or a gas pays for the slowing too.
- **No pump beats physics.** Every scheme below has a hard floor (Carnot for heat, the minimum work of separation for molecules, qV for charge). Mana can approach the floor. It cannot pass it unless the setting says so.

## 1. Heat pumping

Making heat from mana costs 1 J per J (Heat spell, Fire converter). Moving heat from cold to hot costs only the work `W = Q ÷ COP`.

```
Cooling  COP_carnot = T_cold ÷ (T_hot − T_cold)
Heating  COP_carnot = T_hot  ÷ (T_hot − T_cold)        (temperatures in kelvin)
Real     COP ≈ grade × COP_carnot
```

Real Earth heat pumps run at about **40 to 60% of Carnot** (most near 50%). Design default: a mana heat pump runs at **grade 0.5**. Skill may raise it later. Not locked.

Mechanism options: Mana Hands squeeze and release a pocket of gas (the `Compression.md` cycle), or mana sorts fast molecules from slow ones (Maxwell's demon). The demon still pays an information cost (Landauer limit) that lands it back at Carnot. Neither is free.

| Job | T cold → T hot | Carnot COP | COP at grade 0.5 | Work per 1 kJ moved |
|---|---|---|---|---|
| Keep a body cool in 40 °C air | 33 °C skin → 40 °C | 44 | 22 | 46 J |
| Warm a room from 0 °C outside | 0 °C → 20 °C | 14.7 | 7.3 | 136 J |
| Heat a bath from 10 °C water | 10 °C → 40 °C | 10.4 | 5.2 | 192 J |
| Chill meat, dump at 30 °C | 2 °C → 30 °C | 9.8 | 4.9 | 204 J |
| Freeze to −5 °C, dump at 30 °C | −5 °C → 30 °C | 7.7 | 3.8 | 261 J |
| Boil water from 20 °C | 20 °C → 100 °C | 4.7 | 2.3 | 429 J |
| Oven at 250 °C | 20 °C → 250 °C | 2.3 | 1.1 | 879 J |
| Forge at 1,200 °C | 20 °C → 1,200 °C | 1.25 | 0.6 | 1,600 J (worse than direct heat) |

**Rule:** pump near ambient, burn far from it. Heat pumping wins big within about 100 °C of the surroundings. Above roughly 250 °C direct heat is as cheap or cheaper.

If the heat already flows downhill (a 33 °C body in 30 °C air) the pump only speeds it up. Cost is close to the fan or contact work.

### Worked jobs

| Job | Heat moved | Pumped (grade 0.5) | Raw MP pumped | Direct heat or no option |
|---|---|---|---|---|
| Chill 1 kg meat 30 → 2 °C | 98 kJ | 20 kJ | 2,000 | No direct cold. Frost converter is the rune route |
| 1 kg water 20 °C → ice at −5 °C | 428 kJ | 112 kJ | 11,200 | Same |
| 150 L bath 10 → 40 °C | 18.8 MJ | 3.6 MJ | 360,000 | 1.88 million MP as direct heat |
| Cool a working body (300 W into 40 °C air) | 300 W | 14 W | 1.4 MP/s | Sweat or nothing |
| 1 kg water 20 → 100 °C | 334 kJ | 143 kJ | 14,300 | 33,400 MP direct |

The body-cooling row is the standout. A heat-pump cloak in a desert costs about 1.4 MP/s raw. A mid-game caster (INT 40, L9, about 66 J per mana) pays about 0.2 MP/s. The dumped heat leaves from a hot patch. That patch shows to heat-sight (`../Body/Body.md` heat stealth).

## 2. Water and fluid pumping

`Pumps.md` owns devices. Mana pricing:

```
Lift      E = ρ × g × h × V           (1 m³ water up 10 m = 98 kJ = 9,800 raw MP)
Push      E = Δp × V                  (1 L at 1 bar extra = 100 J)
Flow      E = ½ × ρ × V × v²  then pay it again to stop it (damping law)
```

- **Never stop what you can redirect.** Water sent through a pipe and allowed to drain onward pays acceleration once. Water caught and halted pays twice.
- **Hydraulic ram trick.** Let gravity accelerate the water. Mana only works the valve. Valve timing costs under 1 J per stroke.
- **Suction limit stays.** A mana pump pulling from above still loses the column past about 10.3 m (`Pumps.md`). Push from below or lift in buckets.

## 3. Moving liquid instead of boiling it

Evaporating water costs 2,257 J per gram. Pushing liquid water out of a material costs only pressure × volume.

| Job | Evaporate it | Push or spin it out | Ratio |
|---|---|---|---|
| Dry 0.5 kg of water from a cloak | 1.13 MJ (113,000 MP) | 50 to 500 J at 0.1 to 1 MPa (5 to 50 MP) | about 2,000× to 20,000× |
| Dry wet tinder (per g water) | 2,257 J | 0.1 to 1 J | same |

Pressure or spin (`Spin.md`, a spin dryer reaches about 400 g) removes the free water. A residue held in fibers by capillary forces still needs evaporation or time. Machine-spun cotton still holds about half its dry weight in water. Hand-wrung cloth holds about its own weight. The "Dry / Wick" idea spell in `../../../Ideas.md` should squeeze and spin first and only evaporate the remainder.

## 4. Molecule pumping (separation)

Sorting molecules has a minimum work set by thermodynamics (`W_min = −nRT Σ x ln x` for ideal mixtures). It is usually tiny next to boiling.

| Job | Minimum work | Real Earth practice | Boil or burn route |
|---|---|---|---|
| Fresh water from seawater | 1.06 kWh/m³ at 50% recovery (3.8 kJ per L, about 380 MP) | Reverse osmosis 3 to 4.5 kWh/m³ | Distill 2.26 MJ per L (226,000 MP) |
| 3 L drinking water a day from the sea | 11.4 kJ (1,140 MP) | 3 to 4× that | 6.8 MJ |
| Pure oxygen pulled from air | 3.9 kJ per mol (121 kJ per kg) | Oxygen concentrators far above | None |
| Salt brine concentrated | Rises as brine thickens | Solar ponds | Boil |

- **Mechanism:** a mana membrane that passes water and stops salt (reverse osmosis). Or Hands sorting by spin (`Spin.md` centrifuge). Or the demon at molecule scale. All land on the same floor.
- **Oxygen enrichment:** a few liters of 40% oxygen around a fire or a forge raise flame temperature. Around a person it helps at altitude. Pure oxygen raises fire risk sharply.
- **Purity cost climbs.** The last 1% of impurity costs more than the first 90%. Reagent-grade work in `../../Materials/MaterialPurification.md` should expect the curve.

## 5. Charge pumping

Moving charge uphill against a voltage is electricity. Energy is `E = q × V`. Power is `P = V × I`.

| Job | Energy | Raw MP |
|---|---|---|
| Static spark that you feel (about 10 kV, 100 pF) | about 5 mJ | under 0.001 |
| 60 W bulb lit by driven current | 60 W | 6 MP/s |
| Copper plating, 10 g at about 0.5 V | about 15 kJ | 1,500 |
| Split water for 1 kg hydrogen | 142 MJ | 14.2 million |
| Aluminum metal, 1 kg (about 2.1 V theoretical) | about 23 MJ | 2.3 million |

- Friction already separates charge (static from rubbed fur or amber). Friction magic is a natural charge pump. Van de Graaff and Wimshurst machines are the Earth analogs.
- Charge pumping is cheap at high voltage and low current (sparks, igniters, electrostatic dust removal). It is expensive at low voltage and high current (electrolysis, smelting).
- Lightning yield and storms: `TriggeredLightning.md`. Motors and generators: `ElectricMotors.md`, `Generators.md`.

## Quick ladder

| Pump | Best use | Avoid |
|---|---|---|
| Heat | Cooling bodies, food, rooms. Warming baths and rooms | Forges and smelting (burn instead) |
| Water | Lift, irrigation, drainage, redirecting flow | Catching and stopping fast water |
| Liquid squeeze | Drying cloth, leather, tinder, herbs | Bound water (needs time or heat) |
| Molecule | Drinking water, oxygen, brine, purification | Chasing the last fraction of purity |
| Charge | Sparks, ignition, static tricks, plating | Hydrogen and aluminum at scale |

## Open

- Pump grade curve by skill (0.5 default here).
- Whether a Chill converter rune is a heat pump (dumps heat somewhere) or a true cold source. `../../../Ideas.md` "Chill Touch" draws heat into the pool. Physics says the heat must go somewhere.
