# Dungeons

## Narrative

Dungeons are magical places run by dungeon cores. Dead monsters and humans can be absorbed as nourishment so the dungeon can spawn more foes. Damaging or removing a core is forbidden. Destroying one wrecks the dungeon and likely anyone still inside.

## Detail

**Core:** Real. Each dungeon has one.

**Job:** Feeds the dungeon mana. Shapes monsters, materials, mines, and layout by where and what the core is.

**Form:** Often a floating orb toward the dungeon center. Heavy mana. Not a normal crafted artifact. Not simply “alive” in a clean sense either.

**Origins (in-world theories):** Mana-rich formation. Evolved monsters. Divine leftovers. Half-living machines. Truth not fully settled in public knowledge.

**Law:** Forbidden to damage or remove. Destruction annihilates the dungeon and probably anyone still inside. Countries treat cores as income engines.

**Appearance:** New dungeons can form when mana density is right.

**Wild contrast:** Outside monsters are not the same as dungeon-spawned ones.

**Absorption:** Dead living beings can be slowly absorbed. That nourishes spawn. Early talk is known lore; later story treats cores as real objects.

**Layout patterns (kept):** Maze entry. Open biome floors. Stair throats (wild monsters cannot enter; tamed companions can). Boss chambers with long respawn / guild appointments.

**Density:** Mana in dungeons is **more pervasive** than open air of the same altitude. Density rises nearer the core and on deeper floors. Magical materials can spawn in dungeon mines. Metal stock there is usually **old already-converted find** more often than metal that cooked during the delve (`../Materials/Metals.md`).

**Spell-feel floor ladder** (mild additive on open-air altitude `C(h)`, then `A = √C`). Open-air `C(h)` law: `../Science/Energy/ManaConcentration.md`. Digit tables: `../Space/Atmosphere.md`. This ladder is the light combat / cast guide. Deep-delve **metal soak** may be narrated thicker than these mild digits when the beat needs high-grade cook parity with altitude bands. **Spiritual sites** are not on this floor ladder: narrative saturation between ambient and dungeon, maybe a little higher than ambient (`ManaConcentration.md` / `Energy.md`).

```
D = boss monster tier number (T1 → 1, T2 → 2, T3 → 3, T4+ → 4…)
N = floor count of that dungeon
k = floor you are on (1 = first monster / delve floor; hub/entrance before floors may use k = 0)
ΔC_floor = D / N          // sea-level concentration units per floor
C = C(h) + k × (D / N)
A = √C
```

**Examples (sea-level, C(h) = 1, spell-feel):**
- Boss T1 (`D = 1`), 10 floors: +0.1 per floor → floor 10: `C = 2`, `A = √2 ≈ 1.41`
- Boss T5-band (`D = 5`), 10 floors: +0.5 per floor → floor 10: `C = 6`, `A = √6 ≈ 2.45`

Deepest floor always adds **+D** total over open air at that altitude on this mild ladder, no matter how `N` slices it.

**If boss tier unknown:** use the highest tier the dungeon is built for / strongest expected boss band. Truly unknown side holes with no legend default to **D = 1** until a boss band is named.

**Albrook Dungeon (locked feel):** ~**10** labyrinth floors (`PlacesDesign.md`). Crazy high boss / Infernal Dragon link → use a **high D** (S-band / dragon-tier when the link is believed), not D = 1. Early floors stay mild because `ΔC = D/N` is small when **N** is large. Example at sea level if **D = 5**, **N = 10**: floor 1 `C = 1.5` (`A ≈ 1.22`); floor 10 `C = 6` (`A ≈ 2.45`). Deepest floor still totals **+D** over open air.

**Spiritual sites (no floors):** narrative between ambient and dungeon, maybe a little higher than ambient (`ManaConcentration.md` / `Energy.md`). No fixed `D` table.

**Named maps:** `DungeonDesign.md` (Carwen floors and stair throats).

**Kill volume / dungeon yield vs wild flood:** `../Fauna/MonsterPopulation.md`.
