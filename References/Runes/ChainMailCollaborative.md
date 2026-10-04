# Chain Mail as One Collaborative Rune

> **Design loot.** Live locks: Energy.md (eta_cond feel order, no path-%), Magic.md, Runes.md. Metals: ../World/Materials/Metals.md. Non-canon here: path-% dials, dark/deep steel names, mythril-as-titanium, orichalcum as reduced-eta wire, adamantium as forgeable supersteel.

Research note: one shirt-wide rune network that pools rice-grain stones across links into the struck point. Stone rates: `../World/Science/Energy/ManaStones.md`. Path vs cast Useful: `Energy.md` / `../World/Science/Energy/ManaCast.md`. Strike energy bands: `../Combat/AttackScale.md`.

**Assumptions:** the same rice stone (**19** mana, **42** mana/s burst, **0.7** mana/s sustainable input) and **25,000** links (about **0.6 m²**, roughly **1** link per **25 mm²**). One stone per link unless noted. Refill from ambient or body over time is separate from rune logic. Useful joules use **η = 3** as a direct-cast upper bound (see Verdict).

## Whole-shirt totals

| Measure | Raw | Useful (η = 3) |
|---|---|---|
| Stored capacity | 475,000 mana (4.75 MJ) | 14.25 MJ |
| Peak burst output | 1.05 M mana/s (10.5 MW) | 31.5 MW |
| Max input (all stones at full sustainable rate) | 17,500 mana/s | full refill in ~27 s |

Checks: **25,000 × 19 = 475,000**; **25,000 × 42 = 1.05 M**/s; **25,000 × 0.7 = 17,500**/s; Useful = mana × **10 J** × η.

## Pooled delivery to one impact

If the rune routes mana from surrounding links to the struck point, the stones within a radius all contribute. A **5 ms** impact gives:

| Pool radius | Links | Burst | Raw energy in 5 ms | Useful (η = 3) |
|---|---|---|---|---|
| 5 cm | ~310 | 13,200 mana/s | ~660 J | ~2 kJ |
| 10 cm | ~1,250 | 52,500 mana/s | ~2.6 kJ | ~7.9 kJ |
| 20 cm | ~5,000 | 210,000 mana/s | ~10.5 kJ | ~31.5 kJ |

Per link, the gain is still about **2 J** raw (**42** mana/s × **0.005** s × **10 J**/mana). Pooling moves that energy to where the hit lands, which turns roughly **30 J** from an isolated cluster into kilojoules. That range covers heavy pick, war hammer and bolt strikes and reaches into the territory of enemies that punch through plate (`AttackScale.md`).

## Recharge cost per hit

Each stone gives up only **0.21** mana per **5 ms** hit (about **1.1%** of its tank), whatever the radius. At the **0.7** mana/s input limit that refills in about **0.3 s** per stone. The **10 cm** case spends about **262** mana total. Body regen (about **0.2** mana/s from a full refill in a few hours) would take roughly **22 minutes** to cover it, so ambient pull through the stones is the practical source. Body-only recharge of a fully drained shirt (**475,000** mana) would take weeks.

## Passive power

Rune logic upkeep drains the same stones that supply burst. Per-link passive draw sets how long the network lasts without refill:

| Passive draw per link | Network draw | Empty from full in |
|---|---|---|
| 0.001 mana/s | 25 mana/s | ~5.3 h |
| 0.01 mana/s | 250 mana/s | ~32 min |
| 0.1 mana/s | 2,500 mana/s | ~3.2 min |

Passive draw must stay well under the **0.7** mana/s input limit per stone so surplus remains for recharging after hits. A design that idles near **0.001** mana/s and wakes on strain keeps most of the tank available for impacts.

## Verdict

- Pooling changes the result from a rounding error to a meaningful local boost and the limit shifts from stone output to how fast the rune can conduct mana to the struck point.
- Energy scales with stone count inside the pool radius, so one stone per **4** links cuts each row's energy by **4** at the same radius and cuts stone cost to **12,500 SS** (at **2 SS**/rice). Matching the earlier energy at that density needs a radius twice as large.
- **η = 3** comes from the direct-cast law. A rune path uses path **η × ambient G** instead (`Energy.md`), so useful figures could land lower while raw figures hold.
- Ambient mana density decides how quickly the shirt recovers between fights, so a high-mana location suits this setup best.
