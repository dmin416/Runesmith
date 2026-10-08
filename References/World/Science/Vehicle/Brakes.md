# Brakes

Hub: `Index.md`. Tires and wheels: `Wheels.md`. Roads: `Roads.md`. Pedal and seat: `Positions.md`. Axle motors that can also brake: `../Energy/ElectricMotors.md`, `../Energy/Generators.md`.

A brake turns motion into heat, into stored energy, or into a locked hold. The best one is the one that matches the job. A shoe that can park a wagon is the wrong brake for a fast wheel, and a hot racing disc cannot hold a vehicle once the fluid pressure leaks away.

## What actually stops the vehicle

The tire, the hoof, or the rail contact sets the limit. A brake that can lock the wheel is already strong enough. Past that, more pad area does not shorten the stop. It only adds heat capacity and a way to modulate.

On dry firm ground a wheeled vehicle with good rubber can stop near **0.8 to 1 g**. Slicks and downforce go higher. Iron tires on hard dirt or stone are much lower, often a few tenths of a g before the wheel skids. Wet, mud, and ice are worse. A locked wheel stops slower than a wheel that is still rolling and biting, and a locked wheel does not steer.

So the best service brake is the one that can **just exceed** the contact limit, then be eased off so the wheel keeps turning. Cadence (press and release by hand) is the human version. A mechanical anti-lock device does the same faster. Aircraft had mechanical anti-lock long before road cars did.

## Energy and heat

Kinetic energy is `½ m v²`. Double the speed and the brake swallows four times the energy.

| Stop | Energy |
|---|---|
| 1,000 kg from 10 m/s (36 km/h) | 50 kJ |
| 1,000 kg from 20 m/s (72 km/h) | 200 kJ |
| 1,000 kg from 40 m/s (144 km/h) | 800 kJ |

One stop from town speed barely warms a metal drum. The failure is a **long descent** or many stops in a row. Power the brake must reject on a hill:

`P ≈ m g × grade × speed`

A 1,000 kg vehicle on a 10% grade at 10 m/s dumps about **10 kW** the whole way down. That heat goes into shoes, drums, discs, and then the air. If it cannot leave, the lining glazes, the fluid boils, or the drum grows away from the shoes and the pedal sinks.

Weight shifts forward as soon as you brake. Fronts do most of the work on a fast stop. A rear-only brake locks the rear first, the back end steps out, and on a horse vehicle the carriage runs into the team. Bias the force forward as speed and expected deceleration rise. At walking pace, rear shoes are enough.

## Best by job

| Job | Best brake | Why |
|---|---|---|
| Park a wagon on a grade | Sprag, chained wheel, or a ratchet shoe | Holds with no pressure and no driver. One direction only is fine. |
| Keep a coach off the horses' heels | Breeching on the wheelers, plus a modulated rear shoe | The animals are the service brake. The shoe stops the carriage overrunning them. Do not lock the tire. |
| Dirty road, weak shop | External shoe or an enclosed drum | Mud does not oil an open disc as badly when the rubbing surface is inside a drum. |
| Shortest stop from speed | Vented discs sized to lock the tire, plus modulation or anti-lock | Linear, cool faster than a drum, easy to bias front-heavy. |
| Long hill | Something that is not the wheel brake: engine drag, regen, or a water-cooled drum | Friction brakes are a heat sink. A hill is a furnace. |
| Repeated hard stops | Vented disc, or regen with friction only at the end | Thermal mass and airflow. |
| Hold still if power dies | Spring-applied, power-released | Loss of steam, mana, or pressure sets the brake. Elevators and trains use this. A hydraulic disc does the opposite: lose pressure and it lets go. |
| Aircraft landing | Spoilers (put weight on the wheels) + carbon or steel brakes + anti-lock. Reverse thrust if there is an engine | The wheel brake is the heat sink for a rejected takeoff. Wings that still fly unload the tires and waste the brakes. |
| Rail | Axle disc or regen for service. Magnetic track brake for emergency. Mechanical park | Tread brakes stop the train and chew the wheel. |
| Speed where air matters | Air brake, parachute, or a flap stood on edge | Strong when fast. Nothing at a walk. |

## Friction brakes, weakest shop to strongest stop

**Drag shoe and sprag.** A wood or iron block on the tire, or a bar that digs in if the wagon rolls back. Smith work. Wears the tire, fades, and grabs. Right for parking and for a steep village street. Wrong as the only brake on a vehicle that can outrun a horse.

**Spoon on the tread.** Same idea, levered. Bicycle-era. Wet tires lose it.

**Band.** A strap around a drum, pulled tight. Strong in one rotation because the drum helps tension the strap, weak in the other. Winches, cranes, early cars, some hubs. Install it for the direction you must hold. A band that grabs can pitch the driver.

**External shoe.** A block pressed on the outside of a drum or the tire. The mail-coach brake. Rods and a hand lever, no fluid. Near-reach for Caldris once there is a pinned shaft and a shoe. Pair it with a ratchet so the driver can hold it while using both hands on the reins (`Positions.md`).

**Internal drum.** Shoes expand inside a drum. Sealed from mud. The leading shoe is self-energizing, so the stop is strong for the pedal force and can pull unevenly. Heat makes the drum grow, the shoe loses contact, and the same pedal does less. Good park brake. A poor choice once stops are fast and repeated. A water drip on the drum is the old mountain fix.

**Disc.** Pads squeeze a plate from both sides. The plate throws heat into the air, especially if it is vented (two faces with fins between). The pedal feel stays put as it gets hot. It wants more force than a self-energizing drum unless the caliper piston is large or a booster helps. Open discs wear in grit. They are still the best ordinary friction brake for a fast road wheel.

**Carbon-carbon.** The disc and the pad are both carbon. Light, and still working at temperatures that soften a steel disc. Aircraft rejected-takeoff brakes and some race cars. They bite poorly until hot. Best for one huge energy dump, not for a cold village stop.

**Carbon-ceramic.** A ceramic composite disc with conventional pads. Works cold and hot, very light, very costly. Best road or race disc when mass and fade both matter and the shop can make it. Prestige, not a first invent.

Linings, in the order a shop should meet them: wood, leather, then a woven or sintered metal shoe. Asbestos fiber was the Earth industrial lining. It is a lung poison. Do not use it as the craft path.

Fluid, if the link is hydraulic: water works until it boils and then the pedal sinks. A high-boiling oil resists that. Boiling points to remember: plain water 100 °C, a poor glycol fluid around 200 °C dry and much lower once it has drunk water, better fluids toward 230 to 260 °C dry. Seals and a reservoir are the real invent. Rods and cables skip this failure.

## Brakes that are not friction

**Animal breeching.** The horse sits into a strap around the quarters and holds the pole back. Best service brake on any vehicle that still has a team. The wheel brake is the backup and the park.

**Engine drag.** Close the throttle on a piston engine and the wheels turn the compression. A diesel compression-release brake (a Jake brake) opens the exhaust valve at the top of the stroke and throws the compression away, so the engine becomes a pump. Strong on a descent. Noisy. Useless if the drive is disconnected, and useless on a freewheeling hub.

**Regenerative.** The wheel motor is a generator (`ElectricMotors.md`, `Generators.md`). Energy goes into a battery, a mana stone, a flywheel, or a resistor grid if the store is full. Best service brake wherever an axle motor already exists: no lining wear, no fade until the store refuses more power. Typical regen is a gentle stop, on the order of a few tenths of a g, limited by the motor and by what the store will accept. The hard stop and the park still need friction. A full stone with no dump resistor is a brake that has quit.

**Eddy current.** A copper or aluminum disc (or the rail) moves through a magnetic field and the induced currents drag. No contact, no wear, silent. Force falls to **zero at zero speed**, so it cannot park and it fades out of the last part of the stop. Best as a high-speed helper beside a friction brake. Mythril field coils make the magnet small. They do not remove the need for a shoe that can hold still.

**Magnetic track brake.** A shoe pulled down onto the rail. Friction plus some eddy effect. Violent and effective. Emergency, not daily wear.

**Air brake and parachute.** Drag grows with speed squared. Best above the speed where a wheel's contact patch is already at its limit, and on aircraft. A parachute is a one-pull device. An air brake is a surface you can open and close.

**Reverse thrust.** Engines or a reversible pitch throw air or water forward. Aircraft and ships. It unloads nothing by itself: the wheels still need weight on them.

## Failures that define "best"

- **Fade:** lining outgasses, fluid boils, or a drum expands. The driver's answer is to get the heat out (vent, water, shorter application) or to stop using friction (regen, engine, air).
- **Grab:** self-energizing band or leading shoe pulls harder the moment it bites. Dangerous on one side only. A disc is more honest.
- **Leak-off:** hydraulic and air brakes release when the pressure leaves. Spring-applied brakes do not. Anything that parks overnight wants a mechanical ratchet or a spring.
- **One wheel only:** yaws toward the braked side. Fit pairs.
- **Locked wheel on a steerable axle:** steering dies. Lock the rear and the vehicle swaps ends. Modulation matters more than raw force.
- **Inboard brake** (on the axle, not the hub): less unsprung mass, so the suspension works better (`Suspension.md`). It cools worse and is harder to reach. Best on a light fast vehicle with a clean axle. Worst in mud.

## Caldris filter

| Band | Brake |
|---|---|
| Baseline | Breeching, a drag shoe or sprag, maybe a levered shoe on the hind tires of a good coach. Many carts have nothing but the team. |
| Near-reach | Rod or cable, external shoe or band, ratchet park, shoes in pairs. Friction damper thinking from `Suspension.md` is the same shop. |
| Invent | Internal drum, then a vented disc once a flat rotor and a caliper can be bored. Hydraulic lines after seals exist. Regen the moment an axle dynamo exists. |
| Prestige | Anti-lock, carbon discs, eddy-current helpers, spring-applied fail-safe on a powered vehicle. |

A mana-stone dump of axle power is the story brake that beats friction on a hill. Keep a shoe that still works when the stone is full, the rune is dark, or the vehicle is parked.
