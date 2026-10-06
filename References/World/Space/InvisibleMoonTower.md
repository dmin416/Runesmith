# Invisible Moon-Throwing Tower

> **Planning feel, not locks.** Hub: `Space.md`. Adamantium law: `../Materials/Metals.md` (cast-final, ~0 expansion, extreme heat conduction, rings). Orbit energy compare: `OrbitEnergy.md`. Moons: `Moons.md`.

Figures here are planning feel for an invisible co-rotating adamantium tower that throws payloads toward the Moon.

## The Key Fact

**Wall thickness doesn't affect visibility. Diameter and surface brightness do.** Adamantium is indestructible at any size, so the only reasons to make the tower wide are payload and climber clearance. Invisibility comes from two things: a diameter too narrow for the eye to resolve and a surface too dark to shine.

## What People Can See

| Situation | Detection Limit |
|---|---|
| **Dark line against daytime sky, naked eye** | ~0.5 arcsecond wide (~2.4 millionths of a radian). Real telephone wires stay visible to about this angle. |
| **Dark line, through a telescope** | ~25× thinner (~0.02 arcsecond), limited by air turbulence |
| **Sunlit line against twilight or night sky** | Width barely matters. A sunlit line at 483 km stays visible unless the surface reflects less than ~0.03% of light, which is Vantablack-class black. Smooth metal is far worse: it flashes like a mirror. |

**Two rules follow:**

1. **Taper:** diameter at every height stays below 0.5 arcsecond as seen from the nearest possible observer.
2. **Super-black:** every sunlit surface is a light trap reflecting under ~0.03%, with no smooth glinting faces.

## Taper Rule

Diameter limit = 2.4 × 10⁻⁶ × distance to the nearest observer. This assumes a 2 km exclusion zone around the base.

| Height | Max Diameter (Naked Eye) | Max Diameter (Telescope-Proof) |
|---|---|---|
| Ground (2 km fence) | ~5 mm | ~0.2 mm |
| 10 km | ~2.4 cm | ~1 mm |
| 100 km | ~24 cm | ~1 cm |
| 483 km | ~1.2 m | ~5 cm |
| 10,000 km | ~24 m | ~1 m |
| 35,786 km (geostationary) | ~86 m | ~3.6 m |
| 44,600 km | ~107 m | ~4.5 m |

The tower flares like a trumpet: needle-thin at the ground, wide at the top. Telescope-proofing the lower 100 km leaves no room for climbers, so if telescopes are common, the base region also needs restricted access.

## Height Needed to Reach the Moon

A co-rotating tower top already moves eastward with the Earth, faster the higher it goes. The arm supplies the rest.

**Δv arm must add** = lunar-transfer speed at that height minus tower-top speed. Absolute release speed ≈ tower top + Δv. Arm length uses rotary-arm peak accel at the tip (`L ≈ (Δv)² / a`), not a constant-accel rail (`s = v² / 2a`).

| Tower Height | Tower Top Speed | Δv Arm Must Add | Arm for Cargo (~32 g tip) | Arm for People (~4 g tip) |
|---|---|---|---|---|
| 483 km | 0.50 km/s | ~10.2 km/s | ~333 km | ~2,650 km |
| 2,000 km | 0.61 km/s | ~9.0 km/s | | ~2,100 km |
| 10,000 km | 1.19 km/s | ~5.6 km/s | | ~810 km |
| 35,786 km (geostationary) | 3.07 km/s | ~1.05 km/s | | **~28 km** |
| **~44,600 km** | **3.72 km/s** | **None** | Just let go | Just let go, ~0.03 g |

Above geostationary height the tower hangs outward in tension instead of standing in compression. Adamantium doesn't care which. At ~44,600 km tip speed matches a Hohmann-class transfer that reaches lunar distance; release needs no arm.

## Builds

| | **Cargo Build** | **Middle Build** | **Passenger Build** |
|---|---|---|---|
| Height | 483 km | 35,786 km (geostationary) | ~44,600 km |
| Launch | ~333 km arm at ~32 g tip | ~28 km arm at ~4 g tip | Release from the top. No arm. ~0.03 g. |
| Diameter | 5 mm base → 1.2 m top | 5 mm base → ~86 m top | 5 mm base → ~107 m top |
| Mass (1 µm wall, ~4.6 g/cm³) | ~4 t | ~22,000 t | ~34,500 t |
| Riders | Cargo only | People | People |
| Climb time at 200 km/h | ~2.5 hours | ~7.5 days | ~9 days |
| Base loads | Wind moment ~400× smaller than a 10 m-class visible sky tower | Low wind, plus a daily sunlight-pressure moment | Low wind, plus a daily ~3 × 10¹¹ N·m from sunlight pressure on ~2,400 km² of tower |
| Arm visibility | Arm diameter ≤ ~36 cm (its low tip passes 150 km up) | Small arm at great distance | No arm |

## Concealment Details

| Giveaway | Fix |
|---|---|
| **Foundation** | Crown disc and root fully underground. Only a 5 mm needle exits the surface inside a fenced 2 km zone. |
| **Sunlit glow** | Light-trap surface texture formed in the titanium film before soak conversion. Real Vantablack reaches ~0.035%. No polished faces anywhere. |
| **Climbers and payloads** | Small and super-black. Lower-atmosphere transits at night. Near the equinoxes, the whole tower column above the base sits in Earth's shadow at local midnight. Near the solstices, upper sections of the tall builds stay sunlit at midnight, so super-black matters there. |
| **Shadow** | None. A 1 m object at 483 km blocks only ~0.02% of sunlight on the ground and casts no sharp shadow. |
| **Star blinks** | Stars sweep behind the tower in ~0.03 s, lost in normal twinkling |
| **Ice** | Thin wires collect ice in supercooled clouds very efficiently. The needle would grow a visible white sleeve. A water-shedding surface texture helps. Ice forms inside cloud, where it's hidden. The risk is the sleeve lingering after the cloud clears until sunlight melts it. |
| **Lightning** | Adamantium is a metal-line heat conductor; treat it as electrically conductive unless a beat invents otherwise. A bare needle would pull perfectly vertical bolts every storm. Fix with insulation / breakaway path design (coat, segmented dielectric sleeve, or divertor), not an "insulating adamantium" variant, unless that Soft is reopened. |
| **Airships** | An invisible indestructible needle slices through any airship envelope it touches. The flight routes around it have to be closed. |

## Launch Windows

- The Moon's orbit tilts 18-29° from the equator. An equatorial tower throws in the equatorial plane, so the Moon is only reachable while it crosses that plane: about **twice a month, a few days each time**.
- Within each window, the release point lines up with the right direction once per day.
- Travel time to the Moon runs ~3-5 days.
- A small dark payload in flight is as invisible as an unlit satellite.

## Open

- Promote any figure into a lock only when a beat needs it
- Lightning concealment vs conductive adamantium (coat / divertor design)
- Telescope-common worlds vs climber clearance in the lower 100 km
- Equatorial site politics and the 2 km fence
- Relationship to any later visible "sky tower" set piece
