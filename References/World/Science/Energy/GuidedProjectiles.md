# Guided Projectiles and Turning Limits

Hub: `../Science.md`. Ballistics / throw tables: `Projectiles.md`. Arrowheads: `../Metallurgy/Arrowheads.md`. Earth encyclopedia for invent / munition beats. Do not paste brand programs into Terra prose as local tech unless the story invents them.

## EXACTO (.50 BMG guided bullet)

EXACTO (Extreme Accuracy Tasked Ordnance) was a DARPA program built by Teledyne Scientific and tested in 2014 and 2015.

- A sighting system tracks both the target and the bullet in flight.
- The bullet carries a small optical sensor and tiny control surfaces that it moves while in flight.
- Guidance makes small corrections for wind, shooter error and target movement. It does not make sharp turns.
- In tests, an untrained shooter hit moving targets with it.
- The electronics have to survive an enormous shock when the round is fired, which was one of the main engineering challenges.

## Wire-Guided Missiles (TOW type)

TOW stands for Tube-launched, Optically tracked, Wire-guided.

- The gunner keeps the crosshairs on the target for the whole flight.
- A sensor on the launcher tracks an infrared beacon on the back of the missile.
- The launcher measures how far the missile is from the gunner's line of sight. It sends steering corrections down two thin wires that unspool behind the missile.
- The missile adjusts its control surfaces to get back onto the line.
- Limits: range is capped by wire length, about 3 to 4 km. The missile is fairly slow (subsonic to transonic). The gunner has to stay exposed until impact.
- Older systems such as the Soviet Sagger made the gunner steer the missile by hand with a joystick.

## Sidewinder (AIM-9)

Named after a rattlesnake that hunts by sensing heat.

- An infrared seeker in the nose locks onto heat, originally engine exhaust.
- It is fire-and-forget. After launch it steers itself using proportional navigation. Instead of chasing the target directly, it turns to keep the angle to the target constant, which puts it on a collision course.
- Small "rollerons" on the tail fins are wheels spun by the airflow. They act as gyroscopes to stop the missile from rolling.
- The AIM-9X uses an imaging seeker that sees the shape of the target rather than a single hot spot, which makes it harder to fool with flares. It also uses thrust vectoring and can be aimed by where the pilot looks through a helmet sight.

## Mechanical Guidance vs Computer Guidance

Guidance does not require a digital computer. Many systems were fully mechanical, pneumatic or analog electronic.

### Fully mechanical or pneumatic systems

**Whitehead torpedo (1860s onward)**
- A hydrostatic valve sensed water pressure to hold depth.
- A pendulum linked to the valve damped porpoising up and down.
- From the 1890s an air-driven gyroscope (the Obry gyroscope) held a straight heading by moving the rudder.
- No electronics at all.

**Kettering Bug (1918, American WWI aerial torpedo)**
- A preset gyroscope held the course.
- An aneroid barometer held the altitude.
- A mechanical counter tallied engine revolutions. The operator calculated the revolutions needed to reach the target using distance, wind speed and direction.
- When the count was reached, a cam released the wings and shut off the engine. The fuselage then fell onto the target as a bomb.
- Built in small numbers and never used in combat.

**V-1 flying bomb (WWII)**
- A gyroscopic autopilot driven by compressed air controlled the rudder and elevator.
- A magnetic compass corrected the gyroscope's heading.
- A barometric altimeter held altitude.
- A small propeller in the nose spun in the airflow and counted down distance. At zero it triggered the dive.
- Entirely mechanical and pneumatic. No computer.

### Analog electronic systems (no digital computer)

**Early Sidewinder (AIM-9B, 1950s)**
- The seeker was itself a spinning gyroscope with a rotating patterned disc (a reticle) in front of the detector.
- The pattern turned the heat source into a pulsing signal. The timing of the pulses told the missile which direction the target was.
- Simple analog circuits turned that signal directly into fin movement.
- The rollerons were and still are purely mechanical.
- Its reputation came from how few parts it had compared to rival missiles of the era.

**Early wire-guided missiles (X-7, Sagger)**
- The gunner was the computer. A joystick sent signals down the wire straight to the control surfaces.
- The German X-7 of WWII and the Soviet Sagger worked this way.

**V-2 rocket (WWII)**
- Gyroscopes sensed attitude. An analog electronic circuit (some versions used radio beams) moved graphite vanes in the exhaust and the fins.
- An integrating accelerometer cut the engine at the right speed for the planned range.

### Systems that need digital computers

- Modern TOW launchers and fire control.
- AIM-9X imaging seeker, which has to process a picture rather than a single signal.
- EXACTO, which has to compute corrections in a fraction of a second on a projectile moving faster than sound.
- GPS and terrain-matching cruise missiles.

### Pattern

Mechanical and pneumatic guidance can hold a heading, altitude and preset distance. It cannot see or track a target. Homing on a moving target requires a sensor. The earliest homing sensors worked with simple analog circuits. Digital computers became necessary once sensors produced images, once corrections had to happen extremely fast, or once guidance had to combine several sources at once.

## Limits on Turning at Ballistic Speeds

The core equation is turn radius = v² / lateral acceleration.

- **Speed squared:** doubling speed needs four times the sideways force for the same turn. At Mach 2.5 (about 850 m/s), even a 40 g pull gives a turn radius of about 1.8 km.
- **Structure:** airframes and electronics can only take so many g. Missiles generally range from about 30 to 60+ g.
- **Control surface stall:** fins stop producing lift past a certain angle, usually around 15 to 20 degrees.
- **Air density:** fins push against air. Thin air at high altitude means less turning force. In space there is none, so thrusters or thrust vectoring are required.
- **Drag:** hard turns bleed speed quickly, which shrinks remaining range and maneuvering ability.
- **Response time:** sensors, computers and actuators all add lag. At hundreds of meters per second, a few milliseconds of delay matters.
- **Size:** a bullet has tiny fins and very little room for actuators or power. Guided bullets correct by meters over long distances rather than curving around obstacles.
- **Heating:** at hypersonic speeds, friction heats leading edges and fins. This limits how hard a vehicle can maneuver without damage.
