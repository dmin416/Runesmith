# Monster Cores

> Size / mass / recharge tables: `../Science/Energy/ManaStones.md`. Dump is setup-gated, not SA-capped (this file). Foundations locked. Optional later: Old Economy stone price sweeps, battery invent numbers.

## Narrative

Monsters drop mana stones / cores that sell and power craft. Beast materials and common metals / build stock: `Materials.md`. Cores are also the feedstock line for magic-stone materials: **arcanium** (less refined) and **aetherium** (better / refined). Small cores are common enough that stacking many of them is tempting, but most runes cannot handle multiple intakes, so a pile of goblin cores is not a free power plant.

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

**LOCKED: stone size = monster level (this curve), not job title.** Nest “chief,” darker leader, shaman, and similar hierarchy words do **not** set stone size. A L8 chief drops an L8-sized core (early street: rice-band). Leader-band volume needs about **L27+** on this curve (or a body-size mod that pushes volume up). Never use Old **1/30 of kills = leader stone** math.

**Early street rounding:** Wild goblin cores below true rice volume still sell on the **rice-grain** peg (**2 SS**) unless the species is a known tiny (Needle Worm **½** rice). From about **L27** up, use **leader-band** (**5×** rice, **1 LS**) when the curve says so.

**Body-size modifiers (on top of level):**

- **Smaller than normal for their level:** core runs **smaller** but **higher quality**.
- **Much bigger than normal for their level:** core can run **bigger**, or **higher quality**, or a mix.
- **Super monsters (dragons and peers):** can have **large and high quality** stones together.

**Evolved monsters:** One or more evolutions → always have a core. More evolutions → larger / denser tendency (still read through the level curve + mods).

**Mana Sense:** Can detect a stone in a corpse without cutting.

**Quality:** Stones rate on a quality / rank ladder (same language family as runes). Size owns the tank. Grade speeds recharge (with surface area). Dump is not surface-capped. Body-size modifiers above can trade size for quality.

**Capacity (volume):** About **1 mana per mm³** of stone volume. Size owns the tank. Grade does not inflate capacity or mass.

**Rates:**

- **Output (dump):** Not surface-capped. How hard a stone can be dumped is not limited by an SA output formula. Quality and the setup still matter in practice; there is no hard “1 mana/s per mm²” ceiling on dump.
- **Input / sustainable (recharge):** Same thing. Surface area and quality. SA in mm². At Q1, about **1 mana/min per mm²**. General: `Input = ((Q + 1) / 2) × SA` mana/min. Draw at or below that recharge rate and the stone never empties.

Capacity stays size-only. Shards refill faster than one big core of the same total volume (more total surface).

**Uses:** Fuel (including trains), craft, runic slots, lamps. Civilian mana-stone lamps stay uncommon; D can still make and sell them. Chemical cells vs stones: `../Science/Energy/Batteries.md`.

**Trains:** Small pouch cores cannot run a locomotive from tank alone. Engines use large stones with continuous ambient recharge (about melon / ~1.4×10⁷ mm³ and up on the level curve, or special fire-attuned stock). A **fire-attuned** stone of sufficient size is more efficient locomotive fuel than wood.

**Refine:** Real ladder (`Metals.md`): cores → **arcanium** (less refined) → **aetherium** (better). Two materials, not one name with two labels.

**Artificial stones (space cook):** Monster drops are the street baseline. Prestige / invent path: grow or press artificial mana stones in near-space / orbital altitude where open-air `C` is extreme (`../Science/Energy/ManaConcentration.md`). The working idea is **max ambient saturation plus pressure** (mechanical crush, barrier shell, or both) so a seed lattice densifies into stone-grade stock instead of bleeding off as temporary charge. Clay / silica / carbon matrices are natural candidates because they barely convert (`Materials.md`); metals would try to become mythril / orihalcum / adamantium instead of staying a stone. Output competes with refined **arcanium → aetherium**, not with cheap rice-grain drops. Digits and shop recipe stay open until a beat needs them.

**Moon ores (natural space soak):** Terra's red and blue moons sit near the open-air `C` floor. Deposit split and craft feel: `../Space/Moons.md`.

**Dungeon vs wild:** Both can drop. No special “fake dungeon stone” rule locked yet.

**Early drop feel (chance only, not size):** Wild about **1/5**. Dungeon about **1/2**. Not a universal law for every monster. Stronger monsters are more likely to drop. Evolved → always (above). Size still comes from **level**, never from “was this a chief.”

**Multi-intake limit:** Most runes cannot handle multiple intakes. That is the main reason not to wire a bajillion small goblin cores into one pattern.

## Open

- Battery and shard economics (beyond the surface note above)
- Artificial space-stone recipe digits (pressure, seed mass, yield vs monster cores)
