# Chain Mail as One Collaborative Rune

> **Design loot.** Live locks: Energy.md (eta_cond feel order, no path-%), Magic.md, Runes.md. Metals: ../World/Materials/Metals.md (Ag mythril, Au orihalcum, Cu aurium, Fe/steel dark→star, Ti adamantium). Stone rates: ../World/Science/Energy/ManaStones.md + ../World/Materials/MonsterCores.md (dump setup-gated, not SA-capped; recharge area-gated). Non-canon here: path-% dials; adamantium as forgeable post-set supersteel.

Research note: one shirt-wide rune network that pools rice-grain stones across links into the struck point. Path vs cast Useful: `Energy.md` / `../World/Science/Energy/ManaCast.md`. Strike energy bands: `../Combat/AttackScale.md`.

**Assumptions:** the same rice stone (**19** mana; Input **42** mana/min = **0.7** mana/s sustainable recharge) and **25,000** links (about **0.6 m²**, roughly **1** link per **25 mm²**). One stone per link unless noted. **Dump is setup-gated** (`MonsterCores.md`): the stone sheet has no SA burst column. Do **not** read Input **42** mana/min as **42** mana/s dump. Refill from ambient or body over time is separate from rune logic. Useful joules use the rune path `mana × 10 × η_cond × A` (`Energy.md`). The tables below are Highest quality on open ground (η_cond = 1, A = 1), so Useful equals the raw joules.

## Whole-shirt totals

| Measure | Raw | Useful (η_cond = 1, A = 1) |
|---|---|---|
| Stored capacity | 475,000 mana (4.75 MJ) | 4.75 MJ |
| Max recharge (all stones at full sustainable input) | 17,500 mana/s | full refill in ~27 s |
| Peak dump | Setup-gated (craft dial); not `25,000 × 42` | Same |

Checks: **25,000 × 19 = 475,000**; **25,000 × 0.7 = 17,500**/s recharge; Useful = mana × **10 J** × η_cond × A. Old “**1.05 M** mana/s peak” came from misreading Input **42**/min as **/s** and is dead.

## Pooled delivery to one impact

If the rune routes mana from surrounding links to the struck point, the stones within a radius all contribute. How hard each stone dumps in the hit window is **setup-limited**, not SA-tabled. For order-of-magnitude feel, treat the design dial as “this setup dumps about **D** mana/s per stone into the path during the impact,” then scale by link count. A **5 ms** impact spends `D × 0.005` mana per contributing stone.

Example if the craft dial is set so each stone dumps **~40** mana/s for the hit window only (labeled assumption, not a stone-sheet lock):

| Pool radius | Links | Assumed dump | Raw energy in 5 ms | Useful (η_cond = 1, A = 1) |
|---|---|---|---|---|
| 5 cm | ~310 | ~12,400 mana/s | ~620 J | ~620 J |
| 10 cm | ~1,250 | ~50,000 mana/s | ~2.5 kJ | ~2.5 kJ |
| 20 cm | ~5,000 | ~200,000 mana/s | ~10 kJ | ~10 kJ |

Per link at that dial: about **2 J** raw (**40** mana/s × **0.005** s × **10 J**/mana). Pooling moves that energy to where the hit lands. That range covers heavy pick, war hammer and bolt strikes and reaches into the territory of enemies that punch through plate (`AttackScale.md`). Change **D** and every row scales with it; recharge math below does not.

## Recharge cost per hit

At the example dial (**40** mana/s for **5 ms**), each stone gives up **0.2** mana per hit (about **1%** of its tank), whatever the radius. At the **0.7** mana/s input limit that refills in about **0.3 s** per stone. The **10 cm** case spends about **250** mana total. A street body at MP **210** absorbs about **6.2** mana/h when empty and fills in **9 h** (`EnergyDesign.md`), so that hit is about a day of body absorb, not minutes. Ambient pull through the stones is the practical source. Body-only recharge of a fully drained shirt (**475,000** mana) is thousands of those pools.

## Passive power

Rune logic upkeep drains the same stones that supply burst. Per-link passive draw sets how long the network lasts without refill:

| Passive draw per link | Network draw | Empty from full in |
|---|---|---|
| 0.001 mana/s | 25 mana/s | ~5.3 h |
| 0.01 mana/s | 250 mana/s | ~32 min |
| 0.1 mana/s | 2,500 mana/s | ~3.2 min |

Passive draw must stay well under the **0.7** mana/s input limit per stone so surplus remains for recharging after hits. A design that idles near **0.001** mana/s and wakes on strain keeps most of the tank available for impacts.

## Verdict

- Pooling changes the result from a rounding error to a meaningful local boost. The limit is how hard the **setup** dumps and how fast the rune conducts to the struck point, not an SA output formula on the stone.
- Energy scales with stone count inside the pool radius, so one stone per **4** links cuts each row's energy by **4** at the same radius and dial, and cuts stone cost to **12,500 SS** (at **2 SS**/rice). Matching the earlier energy at that density needs a larger radius or a harder dump dial.
- Tables are Highest quality on open ground (η_cond = **1**, A = **1**), so Useful equals raw joules. A lower quality uses η_cond from `Energy.md` (0.2 to 1.0). Do not multiply a rune path by direct-cast η(L).
- Ambient mana density decides how quickly the shirt recovers between fights, so a high-mana location suits this setup best.
