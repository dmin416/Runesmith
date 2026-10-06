# Handoff

You are continuing the Runesmith rewrite foundation in `c:\Users\admin\Desktop\Main\Runesmith`.

## Job

Lock live canon under `References/`. Rewrite prose: `Story/Chapters/`. Treat `References/Source/` as Source dump loot. `Old/` is gone. Do not invent chapters from Source alone. Trust disk paths (`Test-Path` / dir), not Cursor Grep ghosts of deleted files. Continue without asking when the next step is clear. Do not say "fixed"; if you botch something, apologize for being a retard only.

## Live tree (canon)

`References/{Combat,Food,Items,People,PotentialMagic,Progression,Runes,World,Source/,SourceLoot/,OpenFixes.md,Handoff.md,Ideas.md}`

- World holds Materials, Fauna, Geography, Society, Tech, Science/ (+ `*Design.md` fat companions where present)
- Science is under `World/Science/` (Energy, Metallurgy, Biomaterials, Body, Invent, Vehicle)
- Food holds kitchen craft / kit / meat cook (not Metallurgy)
- People cast hub: `References/People/People.md`
- Narrative threat dial: `World/Fauna/MonsterThreat.md`

## Hard locks (do not reopen)

- Kill XP: `XP_kill = 50 × killed_L × RaceMult`. `XP_to_next = 500 × L`. RaceMult table in `Progression/Levels.md` (goblin **1.0**; people **1.0**; Spiked Boar **1.5**; Wereboar **2.0** min L26; Needle Worm **0.5**; Needle Moth **2.0**; …). Party early cut ~**1%** idle / ~**1/4** active. No half-cut on class change. Pre-class bank ½ only.
- Rune η_cond: quality **20%** blocks (Lowest **0.2** → Highest **1.0**). `Useful = mana × 10 × η_cond × A`. Waste: **½** ambient / **½** weapon heat+corruption. Host feel narrative only.
- Ch 4–19 XP ledger locked in `Story/Notes/Experience.md` (Ch 9.5 **1,000** → Mage L20; Ch 13 **342** kills → Mage L25; reclass bank **1479 → 2479 → 3479**).
- Tiers: T1 25, T2 50, T3 75, T4+ 100 each.
- Metal conversion (`Materials/Metals.md`): **Ag → mythril**; **Au → orihalcum** (MR = %); **Cu → aurium**; **Fe → darkiron / star iron**; **steel → darksteel / star steel**; **Ti → adamantium** (cast-final). Dead: mythril=Ti, orihalcum=Ti, adamantium=Fe/steel.
- Ambient altitude: `C = P₀/P(h)` in bound air; haze `C = C_exo × n_exo/n` to solar-wind floor; `A = √C` (`ManaConcentration.md`). Same soak for spells and metal cook.
- Cores: ~1 mana/mm³; street pegs in ManaStones.md. **Stone size = monster level** (`MonsterCores.md`); never Old 1/30 chief→leader-stone. Never eaten: goblins/goblin-kin + undead.
- Diagnosis (not Debugger). Helci 18 workshop; T1 Scout / T2 Hunter / T3 Ranger / T2 Assassin.
- Guild ranks: 8. Wayland = person; Albrook = place. Steel shrink ~2%.
- Terra Earth-sized; 24h day; two moons (red/blue) hang near each other; year **361** days (12×30 + New Year's Day).
- Materials hub: `World/Materials/Materials.md` (COMMON base metals + build; MAGIC conversion lines mythril/orihalcum/aurium/dark-star Fe-steel/adamantium; stone arcanium → aetherium).
- Monster meat tastes good but spoils fast. Personal firearms not widespread (high-class archer ≈ cannon); ship magic cannons exist.
- Ambient: spells + runes `A = √C`. Dungeon: `C = C(h) + k×(D/N)`, `D` = boss tier (T1→1…). Spiritual sites: narrative between ambient and dungeon, maybe a little higher than ambient (no fixed `D`).
- No mana pool → no active absorb. Rich fields may heal body/spirit; no stored mana on leaving. Forced absorb = radiation-class poison.

## Source loot

`References/Source/`: raw Source dump (72 range files). `References/SourceLoot/`: Creatures (261), Places (89), RolandStatus (96), Materials (131 + live naming gate).
