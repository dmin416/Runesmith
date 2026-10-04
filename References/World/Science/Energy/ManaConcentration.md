# Mana Concentration

Hub: `../Science.md`. Ambient gain G: `../../../Runes/Energy.md`.

Altitude curve for ambient mana density. Ground = 1×. Density rises with height (like air). Dungeons and spiritual sites are thicker than open air at the same altitude. Exact stack math is still open (below).

## Altitude table

| Altitude | Mana concentration |
|---|---|
| 249 mi (ISS orbit) | ~100,000,000,000× |
| 62 mi (space begins) | ~3,000,000× |
| 50 mi | 100,000× |
| 40 mi | 10,000× |
| 30 mi | 1,000× |
| 20 mi | 100× |
| 10 mi | 10× |
| 3.4 mi | 2× |
| 0 mi (ground) | 1× |

**Rule of thumb:** every 10 miles up, mana concentration multiplies by 10.

## Formula

```
M(h) = M₀ × e^(h / 5.3 mi)
```

`M₀` is ground-level concentration. `h` is altitude in miles.

## Use with G

Rune / item paths that drink outside mana can take G from this local concentration when a scene needs a number. Direct skill casts take no ambient G. Sealed patterns with no breath to the air sit at the no-intake floor.

## Open: dungeons and spiritual sites

**Locked feel:** Dungeons and spiritual places are denser than open ground at the same altitude. Density also rises nearer a dungeon core and on deeper floors (`../../Geography/Dungeons.md`).

**Not locked:** How that thickness combines with the altitude curve. Candidates (pick when a beat needs a number):

1. **Floor / site multiplier** on local `M(h)` (e.g. floor band × altitude baseline).
2. **Additive band** (altitude baseline + dungeon excess).
3. **Override band** inside the dungeon (ignore outdoor altitude; use a dungeon table).

Do not invent digits here. Ask before locking.
