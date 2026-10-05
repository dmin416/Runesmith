# Mana Concentration

Hub: `../Science.md`. Cast / ambient boost: `../../../Runes/Energy.md`. Air layers / digit tables: `../../Space/Atmosphere.md`. Moons: `../../Space/Moons.md`. Dungeon add-on: `../../Geography/Dungeons.md`. Metals / stones using `A`: `../../Materials/Metals.md`, `../../Materials/MonsterCores.md`.

## Narrative feel (locked)

Mana drifts toward thinner air and higher spiritual worth (osmosis / "friends seeing a party"). Open-air concentration tracks **how empty the local medium is**. Through the bound atmosphere that means lower pressure. Past the thermopause / exobase it means thinner particle haze in the exosphere and geocorona, until the **solar-wind / interplanetary floor**. Terra uses Earth-like atmosphere and near-space densities. More in dungeons and spiritual sites when the story says so. Not a vacuum suck.

Weather, ozone, meteors, geosync landmarks and orbital hardware live in `../../Space/Atmosphere.md`. This file is only ambient concentration `C` and useful boost `A` **law**.

**Spell and rune activation:** ambient raises **useful** output only. Cost mana paid stays the same.

```
C  = relative concentration vs open ground (C₀ = 1)
A  = √C
Useful *= A
```

Partial boost, not linear with `C`. Example: `C = 4` → `A = 2`; `C = 100` → `A = 10`.

## Law (scientific)

Two matched regimes, then a hard floor.

### 1. Bound atmosphere (surface → exobase)

```
P₀ = sea-level pressure ≈ 101,325 Pa
P(h) = ambient pressure at altitude h  // Terra ≈ Earth standard atmosphere
C(h) = P₀ / P(h)
A(h) = √C(h)
h_exo ≈ 370 mi                    // thermopause / exobase
```

Hydrostatic gas. In an exponential atmosphere `log C` is nearly linear with height; scale height `H` changes by layer. Thermosphere: large `H`, slow climb.

### 2. Particle haze (exobase → interplanetary floor)

Above the exobase, collisions are rare and hydrostatic `P` stops being the right ladder. Vacuum purity follows **number density** of the residual haze (mostly light atoms), continuous with the exobase value:

```
C_exo = C(h_exo) ≈ 1.2×10^12
n(h)  = haze number density
C(h)  = C_exo × (n_exo / n(h))
n(h)  = max( n_exo × exp(-(h - h_exo) / H_haze) , n_sw )
```

Planning anchors (Earth-like):

```
H_haze ≈ 17,700 mi     // long geocorona scale height; near-exobase climb is tiny
n_sw ≈ 5–10 cm⁻³       // solar wind / interplanetary medium near Terra
n_exo / n_sw ≈ 7×10^5  // density drop from exobase into that floor
C_max = C_exo × (n_exo / n_sw) ≈ 8.5×10^17
A_max = √C_max ≈ 9.2×10^8
```

`H_haze` is set so the haze reaches the solar-wind floor near **lunar distance (~239,000 mi)**. Past that, deeper geocorona / interplanetary space stays at `C_max` (the medium does not get emptier than the solar wind for this law).

**Kármán line (62 mi / 100 km):** conventional start of space. Still under regime 1 (`P₀/P`). Residual pressure ~`3×10^-2` Pa (`C ~ 3×10^6`).

**Solar activity:** thermosphere and near-exobase densities swing with the star. Table values are quiet / standard planning digits.

Shop vacuum craft: `../Metallurgy/Vacuum.md`.

**Altitude / geosync / layer digit tables:** `../../Space/Atmosphere.md` (not duplicated here).

**Moons:** both hang near lunar distance at haze / solar-wind floor (`C` near `C_max`). Catalogs: `../../Space/Moons.md`.

**Metal permanent conversion / artificial stones:** same `A` in `../../Materials/Metals.md` and `../../Materials/MonsterCores.md`.

**Dungeon thickness:** mild spell-feel floor add `C = C(h) + k×(D/N)` in `../../Geography/Dungeons.md`. Dungeon mana is more pervasive narratively; metal cook / finds: `../../Materials/Metals.md` (old converted stock more common than fresh cook).

**Spiritual sites (locked feel):** narrative saturation between ordinary ambient and dungeon thickness, maybe a little higher than ambient. No fixed `D` digit table.

## Recovery / absorb / activation use

Pool regen, no-pool bodies, radiation-class forced absorb, and “useful not cost” cast rules: `../../../Runes/Energy.md` only. Do not restate here.
