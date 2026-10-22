# Perfect Glider: Powered Versions

Hub: [PerfectGlider.md](PerfectGlider.md).

Engines, motors, batteries, solar cells and fuel are not cast and keep their real mass. Each setup below lists its mass budget inside the stated total. Cast propellers, shafts and gears count as zero.

## Design A

| Power source | Mass budget | Range | Time aloft |
|---|---|---|---|
| Two riders pedaling | Crew 200 kg | Near level flight. Needs ~500 W, two trained riders give ~500 W | 1 to 2 hours of hard effort |
| Gasoline, flown light | Crew 200 + engine 5 + fuel 50 = 255 kg | **~13,900 km** at 59 km/h | ~10 days |
| Gasoline, fuel in place of ballast | Crew 200 + engine 5 + fuel 295 = 500 kg | **~61,000 km** at 83 km/h | ~30 days. Crew endurance is the real limit |
| Battery | Crew 200 + motor 2 + battery 100 (25 kWh) = 302 kg | **~1,400 km** | ~22 hours |
| Solar assist | Crew 200 + cells 1 + motor 2 = 203 kg | Glide extender only | Near-level flight for an hour or two around noon |

- Powered flight should be done light. At 500 kg with 50 kg of fuel the range is only ~7,200 km. The same fuel at 255 kg goes ~13,900 km.
- Honolulu to Tokyo is 6,100 km. Honolulu to San Francisco is 3,900 km. Both are within the light gasoline range.
- Solar cells only fit on the root sleeves and the pod top (~2.3 m², see "Where solar cells go" below). Peak output is ~455 W against ~570 W needed at crew weight. At noon that cuts sink to almost nothing.

## Design B

| Power source | Mass budget (100 kg total) | Range | Time aloft |
|---|---|---|---|
| Human | | Impossible. Needs 2.9 to 3.8 kW | |
| Gasoline prop | Pilot 80 + engine 5 + fuel 10 + gear 5 | 1,420 km shelled, 800 km exposed | 8 to 11 hours |
| Battery prop | Pilot 75 + motor 2 + battery 20 (5 kWh) + gear 3 | 180 km shelled, 100 km exposed | 1.1 to 1.4 hours |
| Two small jet turbines | Pilot 85 + turbines 2 + fuel 10 + gear 3 | 127 km shelled, 53 km exposed | 34 to 60 minutes |

Jets give the most thrust for their size and the least range. A ~5 hp propeller engine goes farthest.

## Design C

| Power source | Mass budget (100 kg total) | Range | Time aloft |
|---|---|---|---|
| **Human** | **Pilot up to ~95 kg** | **30 to 115 km** | **1 to 4 hours** |
| Battery prop | Pilot 85 + motor 1 + battery 5 (1.25 kWh) + gear 9 | 154 km shelled, 123 km exposed | ~4 to 4.5 hours |
| Solar, shelled | Pilot 85 + cells 0.6 + motor 1 + gear 13 | Unlimited in good sun | ~6.5 hours a day of level flight (about 9 am to 3:30 pm), glide extender otherwise |
| Solar, exposed | Pilot 85 + cells 0.3 + motor 1 + gear 14 | Glide extender only | Effective glide ratio ~140 at noon |

- Design C is the only design a person can power alone.

## Where solar cells go

- **Only on skins that never slide.** Every sleeve except the root sleeve slides against its neighbor each time the wing is packed or deployed. Cells there would be abraded every cycle and would also eat the clearance budget ([Joints](Joints.md)).
- **Usable surfaces:** the upper skin of the two root sleeves, the top of the pod or pilot shell and the root sleeves of the tail.

| Design | Cell area | Peak output | Needed for level flight | Result |
|---|---|---|---|---|
| A (crew weight) | ~2.3 m² (root sleeves 0.5 + pod 1.8) | ~455 W | ~570 W | Near-level at noon only |
| C shelled | ~1.7 m² (root sleeves 0.9 + shell 0.8) | ~340 W | ~230 W | Level flight ~6.5 hours a day |
| C exposed | ~0.9 m² (root sleeves only) | ~180 W | ~270 W | Glide extender only |

Cells are ~0.35 kg/m², recessed flush into the skin. A clip-on cell blanket over the outer sleeves adds area but creates steps and drag that push performance below the Real tables.
