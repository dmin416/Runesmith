# Super-Energy Powder

> **Design loot / invent.** Not locked world law. Assumes nitrocellulose / nitroglycerin can carry magical energy multipliers. Densify-on-impact lives in `Piercing.md`. Do not invent D kit until a beat needs it.

## 12. Super-Energy Powder Scenario: 3x and 10x

Nitrocellulose and nitroglycerin carry 3 times or 10 times their normal energy. A mixed case covers nitrocellulose at 3x with nitroglycerin at 10x in a 50/50 double-base blend, which averages about 6.5x. Baseline is the .50 rifle with a 650 grain copper bullet.

### The Powder

| Powder | Energy per kg | TNT Equivalent per kg | Flame Temperature | Velocity Ceiling |
|---|---|---|---|---|
| Normal double-base | ~4.8 MJ | ~1.1 kg | ~3,000 to 3,500 K | ~5,500 to 6,500 fps |
| 3x | ~14.4 MJ | ~3.4 kg | ~7,000 to 9,000 K | ~9,500 to 11,000 fps |
| Mixed (~6.5x) | ~31 MJ | ~7.5 kg | ~12,000 to 18,000 K | ~14,000 to 16,000 fps |
| 10x | ~48 MJ | ~11.5 kg | ~15,000 to 25,000 K | ~17,000 to 20,000 fps |

Hotter gas expands faster, so the velocity ceiling rises with the square root of the energy. At 10x the gas is hotter than the surface of the sun and partly ionizes into plasma. The 10x ceiling matches lab light gas guns.

### Option A: Same Power, Smaller Cartridge

Keep the bullet at normal speed and cut the powder.

- **3x:** .50 BMG power from one third of the powder. The case shrinks to roughly the size of a .300 Winchester Magnum case. The 25mm 50,000 ft-lb tier fits in roughly a .50 BMG case.
- **10x:** .50 BMG power from one tenth of the powder. The case shrinks to roughly the size of a .44 Magnum case. A full round weighs about half as much. The 25mm 50,000 ft-lb tier fits in roughly a .300 Winchester Magnum case.
- Recoil stays nearly the same since the bullet carries most of the momentum. It drops slightly from the smaller gas mass.
- Barrel heat per shot stays normal.
- A soldier carries 3 to 10 times more shots for the same powder weight.

### Option B: Same .50 Rifle, Same Charge

| Powder | Velocity | Energy | Matches Tier | Chamber Pressure | Recoil (30 lb gun) |
|---|---|---|---|---|---|
| Normal | ~2,950 fps | ~12,600 ft-lbs | 10,000 | ~55,000 psi | ~95 ft-lbs |
| 3x | ~4,500 fps | ~29,000 ft-lbs | 30,000 | ~150,000+ psi | ~250 ft-lbs |
| Mixed (~6.5x) | ~6,000 fps | ~52,000 ft-lbs | 50,000 | ~350,000+ psi | ~490 ft-lbs |
| 10x | ~7,000 fps | ~70,000 ft-lbs | Beyond 50,000 | ~500,000+ psi | ~660 ft-lbs |

Efficiency drops as velocity climbs because the gas spends more energy pushing itself. That is why 10x energy gives about 5.5 times the bullet energy instead of 10.

### .50 Armor Penetration Under Option B

| Powder | Copper Alone | Hardened Steel Core | Adamantium Needle |
|---|---|---|---|
| Normal | ~12 to 15 mm | ~22 to 25 mm | ~65 mm |
| 3x | ~22 to 28 mm | ~30 to 35 mm | ~180 mm |
| Mixed (~6.5x) | ~32 to 40 mm | ~38 to 45 mm | ~320 mm |
| 10x | ~35 to 45 mm | ~40 to 50 mm | ~400 mm |

- Copper and steel gain less than expected. Above roughly 3,000 fps hardened steel shatters on hard plate. Above roughly 5,000 fps both metals splash against armor like a liquid jet, so penetration levels off near the bullet's own length.
- The adamantium needle never deforms, so it keeps converting the extra speed into depth. At 10x a .50 needle round defeats more armor than a WWII Tiger II front plate.

### Side Effects

- **Bullet deformation:** At mixed and 10x pressure, a plain copper bullet gets squashed and swaged in the barrel. Steel cores, heavy jackets or the adamantium needle hold up. Slower-burning grain shapes spread the push and lower peak pressure.
- **Air friction:** Above roughly 5,000 fps (Mach 4.5) the bullet heats up from air friction and sheds speed faster. It still arrives far faster than any normal round at combat ranges.
- **Barrel heat under Option B:** Indestructible does not mean heat-proof. At 10x a steel-weight .50 barrel climbs roughly 35°C per shot. After 15 to 20 quick shots it glows red. At 3x it takes roughly 50 to 60 quick shots.
- **Muzzle flash and blast:** At 3x the flash lights up a night battlefield. At 10x it is a blinding plasma burst like a lightning strike, with a blast that ruptures normal eardrums nearby.
- **Storage:** One kilogram of 3x powder hits like 3.4 kg of TNT. One kilogram of 10x powder hits like 11.5 kg of TNT. A supply cart carrying 100 kg of 10x powder is over a ton of TNT on wheels.
- **Era:** Nothing changes about the raw materials or production. Only the energy changes, so both medieval and Victorian producers get the same multiplier.

---

## Super-Energy Powder Formulas

### Inputs

- **M_c** = cellulose energy multiplier
- **M_g** = glycerin energy multiplier
- **f_c** and **f_g** = share of nitrocellulose and nitroglycerin in the powder. They add up to 1. Single-base powder is f_c = 1.
- **p** = powder amount relative to a normal charge. 1 is normal. 0.5 is half.

The multiplier is assumed to carry through nitration into the finished powder.

### Formula 1: Effective Multiplier

**M = (f_c × M_c) + (f_g × M_g)**

Example: 50/50 blend with cellulose at 3x and glycerin at 10x gives M = (0.5 × 3) + (0.5 × 10) = 6.5.

### Formula 2: Powder Needed for Normal Power

**p = 1 / M**

Cellulose, glycerin, acid, wash water, solvent and stabilizer all scale by the same p.

### Formula 3: Power from Any Powder Amount

**Bullet energy = Normal energy × (M × p)^0.75**

**Velocity = Normal velocity × (M × p)^0.375**

The 0.75 exponent accounts for efficiency loss as the gas spends more energy pushing itself at higher speed.

### Formula 4: Powder Needed for a Target Energy

**p = (Target energy / Normal energy)^1.33 / M**

Example: 50,000 ft-lbs from a .50 with 10x powder gives p = (50,000 / 12,600)^1.33 / 10 = about 0.63, so 63 percent of a normal charge.

### Formula 5: Velocity Ceiling

**Ceiling ≈ 6,000 fps × √M**

### Formula 6: Side Effects

- **Chamber pressure** ≈ Normal pressure × M × p
- **Recoil** ≈ Normal recoil × (M × p)^0.85
- **Barrel heat per shot** ≈ Normal heat × M × p
- **TNT equivalent per kg of powder** ≈ 1.15 × M
- **Shots per kg of powder** = Normal shots × 1 / p

### Acid

**Acid needed = Normal acid × p**

Acid strength stays the same. The multiplier changes how much energy the material holds, not its chemistry, so nitrating a kilogram of cellulose or glycerin consumes the same acid as always. Less raw material means proportionally less acid. A 10x powder at normal power needs one tenth the acid.

Production heat during nitration stays normal. The finished powder is M times more dangerous per kilogram in storage and handling.

### Quick Lookup

| M × p | Energy Factor | Velocity Factor |
|---|---|---|
| 1 | 1.00 | 1.00 |
| 2 | 1.68 | 1.30 |
| 3 | 2.28 | 1.51 |
| 5 | 3.34 | 1.83 |
| 6.5 | 4.07 | 2.02 |
| 10 | 5.62 | 2.37 |

### Worked Examples: .50 Rifle

Normal charge is about 15 g of powder for 12,600 ft-lbs at 2,950 fps.

| Scenario | M | p | Powder | Acid | Bullet Energy | Velocity |
|---|---|---|---|---|---|---|
| Normal | 1 | 1 | 15 g | 100% | 12,600 ft-lbs | 2,950 fps |
| 3x, same power | 3 | 0.33 | 5 g | 33% | 12,600 ft-lbs | 2,950 fps |
| 3x, full charge | 3 | 1 | 15 g | 100% | ~28,700 ft-lbs | ~4,450 fps |
| Mixed, same power | 6.5 | 0.15 | 2.3 g | 15% | 12,600 ft-lbs | 2,950 fps |
| Mixed, full charge | 6.5 | 1 | 15 g | 100% | ~51,300 ft-lbs | ~5,950 fps |
| 10x, same power | 10 | 0.1 | 1.5 g | 10% | 12,600 ft-lbs | 2,950 fps |
| 10x, half charge | 10 | 0.5 | 7.5 g | 50% | ~42,100 ft-lbs | ~5,390 fps |
| 10x, full charge | 10 | 1 | 15 g | 100% | ~70,800 ft-lbs | ~7,000 fps |

---

