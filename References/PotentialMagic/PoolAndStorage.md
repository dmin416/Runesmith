# Pool And Storage

Hub: `PotentialMagic.md`. Kill paths: `KillEfficiency.md`. Ember / stones: `../World/Science/Energy/ManaCast.md`, `../World/Science/Energy/ManaStones.md`. Air cartridge: `../World/Science/Energy/Compression.md`.

Piercing still wins on pool energy. Stored gas pays off for **area blasts and defense**, not as the default kill method.

Fight capacity ≈ pool + (regen × time) + stored chemical energy.
Sustained kill rate ≈ regen ÷ (effect J per kill).
Mana drawn = effect J / (10 × η × μ).
"ημ 1" means η × μ = 1 (L2 at INT 15).

## Energy per kill (effect joules)

| Method | Goblin | Dragon |
|---|---|---|
| Boosted needle (0.3 cm) | ~80 J (~8 mana ημ 1) | 0.5 to 2.1 kJ (~50 to 208 mana ημ 1) |
| Boosted ball line shot | ~80 J each (~8 mana) | ~5 kJ (~500 mana) |
| Elemental Ball-scale blast | ~25 kJ each if 40 packed (~1 MJ total) | Not viable |

A 1,000 goblin wave at ~**80 J** each is ~80 kJ effect (~8,000 mana at ημ 1). Aiming and launch rate limit before pool does if pierce is used.

## What stored hydrogen adds

- 1 kg holds ~120 MJ burn. 1 L at 700 bar holds ~4.8 MJ. Compressed air at 200 bar holds ~0.1 MJ/L (~48× less). Fill work: `../World/Science/Energy/Compression.md` air cartridge style for air; water-split H₂ is ~142 MJ/kg ideal plus compress.
- Release / ignite: ~**10 J** Ember (~1 mana at ημ 1).
- A 1 L H₂ bottle can blast on the order of ~1 kg TNT equivalent for ~6 MJ of **prior** synthesis energy paid into storage. An equal-pool pure-mana ball is worse per joule already spent in the bottle. Round-trip synthesis losses are real; treat bottles as **overflow regen sinks**, not the primary kill budget.
- Do not apply the old "10% casting efficiency" tax on top. Mana to ignite is Ember-scale; mana to **create** the fuel is the synthesis joules / (10 η μ).

## Allocation

- **Pool:** needles and line shots for hordes and dragons.
- **Regen overflow:** fill bottles between fights.
- **Bottles:** blasts on shieldwalls, packed mobs behind cover and walls.
- **Defense:** a head-on Ward costs the attack's effect energy (mana = J / (10 η μ)). Angled shields follow `../World/Science/Energy/ManaCast.md` Mana Shield (45° absorbs half, so the focused disk pays J / (20 η μ)). Cheapest defense is often killing first.
