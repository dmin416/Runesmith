# Experience Curve

> **Live overall-level XP curve and craft payout tables.** Kill law / RaceMult: `Progression.md`, `RaceMult.md`. Skill ranks: `SkillRanks.md`. Class packages: `ClassPackages.md`. Ch 4–19 ledger: `../../Story/Notes/Experience.md`. Split from old `Levels.md` (no data dropped).

## XP sources (locked early anchors)

Awards are **straightforward**: flat or simple by action. Class does **not** change how much XP an action is worth. Class only decides which package you get when the overall bar rolls.

**Locked early anchors (live law)**

| Action | XP |
|---|---|
| Monster kill (solo, full credit) | **50 × monster level × RaceMult** |
| Goblin L1 (estate bravery) | **50** (RaceMult 1.0) |
| Goblin L2 / L3 / L4 (live) | **100 / 150 / 200** |
| Typical early forest goblin (~L4) | **200** (RaceMult 1.0) |
| First Kill achievement (on top of the kill) | **+200** (Chapter 4; not every kill) |
| First-time basic / lesser rune schematic at **[Highest]** | **1000** (quality ladder: **100 / 200 / 400 / 600 / 1000**; raise pays difference) |
| Repeat scrolls / practice crafts | much less than first schematic (story: ~20 regular, ~50 runic until retuned) |

**Goblin levels in early rewrite**

| Fight | Monster level | Notes |
|---|---|---|
| Arden bravery test (age 9) | **Goblin L1** (HP 117) | Explicit status screen; XP **50** |
| Weekly estate training | L1-tier training stock | Same pen as bravery test; **50** each |
| First Carwen forest group | **L2, L3 and L4** | Live XP **100 / 150 / 200**; Old ledger **51 / 52 / 53** quarantined in `../../Story/Notes/Experience.md` |
| Later same-day chase kills | **L4 / L5** then **L3 / L4** | Live **200 / 250** then **150 / 200**; day end **1000 / 2000** at L4 (`../../Story/Notes/Experience.md`) |
| Later Carwen forest nests | higher than estate, still common goblins | Levels not always shown; treat as low single digits unless the chapter names them |

Other notes:

- Monster kills (solo or party). Party XP ties to **ability and contribution**. Teaming with higher-tier people is allowed; a low cut still pays something. Idle spectating on the Chapter 11 spiked boar: Roland **6 XP** (**~1%** of the kill for being in the group; he could kill it alone if he tried). Active contribution raises his cut. People still prefer same-tier parties.
- Leveling skills and spells. Leveling a spell (e.g. Mana Bolt rank-up) can grant a popup XP award; Chapter 10 notes this is often **more** than trash goblin kills. Craft classes also gain XP by making items.
- Crafting / item creation. **First** successful schematic discovery pays the big 1000. Copying the same rune again does not.
- **Pre-class XP** (Chapter 4–6): kills and achievements before first ascension bank with a **½ penalty** when the class finally applies. Estate bravery **250** + **55** more L1 goblins (**2750**) = bank **3000** → **1500** applied. Ascension starts Mage L1 empty; bank lands **Mage L3** empty. The bank applies **once** at the first ascension only. It does **not** refill for later class changes. See `../../Story/Notes/Experience.md`.
- **Second Tier 1 class** (Chapter 10 talk): most people do not ascend at age 10. There is **no XP gain debuff**. Kill XP stays the same. More classes means you need **more total experience** because overall level keeps climbing on the shared bar to raise each class. Combat second T1s take longest to push through that climb; lighter crafting second T1s level faster but grant weaker packages.


## Experience curve (overall level)

### Source pacing (what we matched)

Source payouts were smaller (goblin ~15–20 XP, same **1000** first schematic). Rewrite keeps the **kill counts / time feel**, not the old raw numbers.

| Source beat | What happened | Implied cost (Source XP) |
|---|---|---|
| First adventurer day, Mage L3 | ~7 goblin ears; leveled once during the hunt | estate Mage doubles left **1250 / 1500**; hunt **263** finishes L3→L4 |
| ~3 months forest grind | L4 → **L20** | **1,000** goblin kills (Goblin Hunter lock) + spell/skill XP (`../../Story/Notes/Experience.md`); Old **1,481**/~53 Source pacing quarantined |
| Party dungeon arc | **half a year** with the girls toward Mage L25 (after **3 months** solo goblins) | higher XP/fight than forest goblins |
| First lesser schematic | **1000 XP** at **[Highest]** (quality ladder below); “couple of levels” if spent right after a fresh class (low L) | 1000 ≈ 1–2 levels near overall L2–L3 |
| Late Source | bar called “exponential” and stubborn | rewrite stays **linear**; high constant makes late levels slow without a second curve |

### Locked rules

1. XP needed to go from overall level **L → L+1** depends only on **L**, not on which class is main.
2. Formula is **linear** in L (Source’s late “exponential” talk is not used).
3. One shared XP pool. Class packages fire when the bar rolls.

### Formula (locked: pre-class L3 + half bank)

Anchor: bank **3000** (Ch 4 bravery 250 + **55** estate L1×50), half on apply = **1500**, Mage L1 empty → L3 empty. See `../../Story/Notes/Experience.md`.

```
XP_to_next(L) = 500 × L
```

At L5: **2500 XP** ≈ **12.5 × L4 goblins** (empty bar; RaceMult 1.0 → **200** each). First-day forest kills alone are a small slice; spell/skill XP and denser hunting carry the early adventurer grind (Chapter 9–10).

| Current L | XP to reach L+1 | Goblins @ 200 (empty bar) | First schematic 1000 |
|---|---|---|---|
| 1 | 500 | 2.5 | 2 levels |
| 5 | 2500 | **12.5** | 0.4 level |
| 10 | 5000 | 25 | 0.2 level |
| 20 | 10000 | 50 | 0.1 level |
| 25 | 12500 | 62.5 | 0.08 level |
| 28 | 14000 | 70 | 0.07 level |
| 50 | 25000 | 125 | 0.04 level |
| 75 | 37500 | 187.5 | 0.03 level |
| 100 | 50000 | 250 | 0.02 level |
| 125 | 62500 | 312.5 | 0.02 level |

**Schematic check:** after class change at low overall L (e.g. L2–L3), **1000 XP** is about **two levels**. At Mage L25 it is a small fraction of a level. Spell/skill XP still matters early (Chapter 10: spell rank-ups often beat trash goblin kills).

### Cumulative XP (from L1 up to level N)

```
XP_total_to_reach(N) = 500 × (1 + 2 + … + (N−1))
                     = 250 × (N−1) × N
```

| Reach overall | Total XP from L1 | Rough L4-goblin-equivalents (÷200) |
|---|---|---|
| 25 (one T1 maxed) | **150,000** | ~750 |
| 50 | **612,500** | ~3,063 |
| 75 (25+50) | **1,387,500** | ~6,938 |
| 125 (25+50+50) | **3,875,000** | ~19,375 |

XP already spent stays spent. Goblin-counts are a yardstick only. Real paths mix dungeon mobs, skill XP, schematics and quests.

**L4→L20 (Ch 9.5, locked):** **1,000** goblins incl. **8** T2 ambush leaders (L27, RaceMult **1.5**) + nest leaders + Shaman → kill XP **90,975** → **Mage L20**. Ledger: `../../Story/Notes/Experience.md`.

### Sample grind checks

| Action | XP | At L5 (need 2500) | At L25 (need 12500) | At L50 (need 25000) |
|---|---|---|---|---|
| Goblin L1 (RaceMult 1.0) | 50 | tiny | tiny | tiny |
| Goblin L4 (RaceMult 1.0) | 200 | ~1/12.5 level | ~1/62.5 level | ~1/125 level |
| First basic/lesser rune schematic | 1000 | 0.4 level | 0.08 level | 0.04 level |
| First Common rune schematic (e.g. Fire Arrow) | **2000** (2× lesser) | 0.8 level | 0.16 level | 0.08 level |
| Mana Arrow scroll (repeat craft) | 20 | tiny | tiny | tiny |
| Fire Orb runic scroll (repeat) | 50 | tiny | tiny | tiny |
| Person L55 (pool `50 × L`) | **2750** | ~1.10 level | ~0.22 level | ~0.11 level |
| Tier 2 fencer L55 (Roland share; Ch 14) | **479** | ~0.19 level | ~0.04 level | ~0.02 level |

**Lesser schematic XP by quality (locked):** payout is the quality’s listed XP the first time that schematic reaches that quality. Raising the same lesser schematic to a higher quality pays only the **difference** up to the new tier (never stacks full tiers). Straight to Highest pays **1000**. No further XP past Highest on that schematic.

| Quality | XP (first time at that quality) | Diff from prior |
|---|---:|---:|
| Lowest | **100** | n/a |
| Low | **200** | **+100** |
| Intermediate | **400** | **+200** |
| High | **600** | **+200** |
| Highest | **1000** | **+400** |

Ch 19 Fire Orb: memory **[High] +600** then **[Highest] +400** = **1000**.

Chapter 26 common schematic stacking: Intermediate common = **1000 XP**; then perfecting to Highest adds another **1000** (total **2000** = **2×** lesser Highest). Going straight to Highest also pays **2000**. No further XP for redoing the same schematic past that cap. Perfect common schematic from a shop sample pays **2×** lesser (`../Combat/Spells.md` Fire Arrow).

Chapter 21 timing: regular Mana Arrow ~**10 min** / 20 XP; Fire Orb runic ~**45 min** / 50 XP (imperfect). Five regular scrolls ≈ one runic's time for more XP; schematics still dominate leveling. Shop breach curses: `../Runes/ScrollEconomy.md`. Common schematics pay **2×** lesser (`Progression.md`).

Chapter 14 narration: common Tier 2 packages grow about **×1.5** vs Tier 1 (forward-only on new levels). Fresh T2 physicals still burn hard on active skills (**stamina**; Gale Step and similar). A coordinated T1 party deep into second classes can beat a green T2. **Ch 14 lock:** Arden watcher fencer is overall **L55** (not green); Becky / Sahildr / Reyna overall **~45**; Roland Mage **L25**. Party coordination + skill waste still beats him.

### Optional later tweaks (not locked)

- Monster XP scaled by level gap can sit on top of flat base values.
- If the curve still feels fast or slow after a few written arcs, change only the constant **500** (keep linear). Halving to **250 × L** would cut every cost in half.

