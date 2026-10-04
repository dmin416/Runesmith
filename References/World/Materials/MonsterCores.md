# Monster Cores

> Size / mass / recharge tables: `../Science/Energy/ManaStones.md`. Dump is setup-gated, not SA-capped (this file). Foundations locked. Optional later: Old Economy stone price sweeps, battery invent numbers.

## Narrative

Monsters drop mana stones / cores that sell and power craft. This is a major world economy and tech thread. Small cores are common enough that stacking many of them is tempting, but most runes cannot handle multiple intakes, so a pile of goblin cores is not a free power plant.

## Detail

**What:** Gem-like crystals that form inside some monsters. Sellable. Used for craft and fuel. Look like gems; they are **not** unbreakable jewelry gems. Cores can rupture (energy dump). Seat craft for true unbreakable gems: `../Science/Metallurgy/GemInlay.md`. Rupture joules: `../Science/Energy/ManaCast.md`.

**Price:** Tracks physical size / mana density more than how hard the kill was.

**Early size bands:**

| Band | Scale | Early peg |
|---|---|---|
| Rice-grain | Common small core | **2 SS** |
| Leader | About **5×** rice volume | **1 LS** |

**Level → volume (baseline):** Rough band feel only. Typical core **volume** (≈ mana capacity) from monster level. Same curve as before, stated as volume not diameter:

`V_mm³ ≈ (π/6) × (L² / 125)³`

Capacity ≈ **V** mana at **1 mana/mm³**. Width is whatever shape the stone has; do not size cores by assuming a perfect sphere.

| L | V / mana (feel) | Band |
|---|---|---|
| 20 | ~17 | rice-scale |
| 27 | ~100 | leader floor (~5× rice volume; leaders at least ~L27) |
| 50 | ~4k | marble / Silver hunt |
| 53 | ~6k | Myrmeke Soldier band |
| 100 | ~268k | fist |
| 163 | ~4.8M | big boss |
| 300 | ~195M | boulder |
| ~350+ | ~520M | crazy apex (~1 m class if round) |

**Named street sizes and exact capacity** live in `../Science/Energy/ManaStones.md` (rice **19** mana, marble **2,145**, and so on). The level line only says which volume band a level tends toward. Drop chance still rises with strength separately.

**Body-size modifiers (on top of level):**

- **Smaller than normal for their level:** core runs **smaller** but **higher quality**.
- **Much bigger than normal for their level:** core can run **bigger**, or **higher quality**, or a mix.
- **Super monsters (dragons and peers):** can have **large and high quality** stones together.

**Evolved monsters:** One or more evolutions → always have a core. More evolutions → larger / denser tendency.

**Mana Sense:** Can detect a stone in a corpse without cutting.

**Quality:** Stones rate on a quality / rank ladder (same language family as runes). Size owns the tank. Grade speeds recharge (with surface area). Dump is not surface-capped. Body-size modifiers above can trade size for quality.

**Capacity (volume):** About **1 mana per mm³** of stone volume. Size owns the tank. Grade does not inflate capacity or mass.

**Rates:**

- **Output (dump):** Not surface-capped. How hard a stone can be dumped is not limited by an SA output formula. Quality and the setup still matter in practice; there is no hard “1 mana/s per mm²” ceiling on dump.
- **Input / sustainable (recharge):** Same thing. Surface area and quality. SA in mm². At Q1, about **1 mana/min per mm²**. General: `Input = ((Q + 1) / 2) × SA` mana/min. Draw at or below that recharge rate and the stone never empties.

Capacity stays size-only. Shards refill faster than one big core of the same total volume (more total surface).

**Uses:** Fuel (including trains), craft, runic slots, lamps. Civilian mana-stone lamps stay uncommon; D can still make and sell them. Chemical cells vs stones: `../Science/Energy/Batteries.md`.

**Trains:** Small pouch cores cannot run a locomotive from tank alone. Engines use large stones with continuous ambient recharge (about melon / ~1.4×10⁷ mm³ and up on the level curve, or special fire-attuned stock). A **fire-attuned** stone of sufficient size is more efficient locomotive fuel than wood.

**Refine:** Refining toward aetherium is real (`Metals.md`).

**Dungeon vs wild:** Both can drop. No special “fake dungeon stone” rule locked yet.

**Early drop feel (lowest tier):** Wild about **1/5**. Dungeon about **1/2**. Not a universal law for every monster. Stronger monsters are basically more likely to drop.

**Multi-intake limit:** Most runes cannot handle multiple intakes. That is the main reason not to wire a bajillion small goblin cores into one pattern.

## Open

- Battery and shard economics (beyond the surface note above)
