# Leftover Hygiene — 2026-10-06 Re-Audit

Draft hygiene note packing the leftover research-note issues that are still open after the 2026-10-06 re-audit, with ready-to-paste proposed fixes so David can apply them himself (or ask later).

**Only this file changed. No changes outside `Grok Notes/`.**

---

## Context

Earlier audit issues addressed path-link fixes, OpenFixes dropped, Conflicts culled, StoryPrices↔ScrollEconomy aligned, Magic.md filled, adult MP 210, Mastery −10%/level. This note covers what's still open on main after those updates.

**What was already fixed (do not re-open):**
- StoryPrices ↔ ScrollEconomy alignment (Mana Arrow 3 SS, Fire Arrow 6 SS, Fireball ≈1 LS)
- Magic.md / ScrollEconomy / ScrollCraftScrapes side-by-side lock
- Adult MP 210 (`References/Progression/Attributes.md`)
- Mastery −10%/level (`References/Ideas.md`)
- Conflicts / OpenFixes cleanup

---

## Still Open Issues

### 1. CrossCheck RaceMult

**Where:** `Story/Notes/CrossCheck.md` line 79

**What's wrong:** XP quick rules still say:
- Spiked boar **10**
- Wereboar **20**

**Canon:** Live `50 × L × RaceMult` in `References/Progression/Levels.md`, `Story/Notes/Experience.md`, `References/Handoff.md`:
- Spiked Boar RaceMult **1.5**
- Wereboar RaceMult **2.0**

**Proposed fix (line 79):** Replace the line:

```
- Kill XP: `50 × killed_L × RaceMult` (`Progression.md` / `Levels.md`). Goblin **1.0**; rat **0.2**; worm **0.5**; moth **2.0**; spiked boar **10**; wereboar **20**; people **1.0**. Ch 14 L55 pool **2750** / Roland **479**.
```

with:

```
- Kill XP: `50 × killed_L × RaceMult` (`Progression.md` / `Levels.md`). Goblin **1.0**; rat **0.2**; worm **0.5**; moth **2.0**; spiked boar **1.5**; wereboar **2.0**; people **1.0**. Ch 14 L55 pool **2750** / Roland **479**.
```

**Note:** Ch 11 CrossCheck row already uses 1.5 correctly (line 120).

---

### 2. CrossCheck Science paths

**Where:** `Story/Notes/CrossCheck.md` lines 53-54

**What's wrong:** Still lists old paths:
- `References/Science/Science.md`
- `References/Science/ManaCast.md`

**Canon:** Live tree is `References/World/Science/...`:
- `References/World/Science/Science.md`
- `References/World/Science/Energy/ManaCast.md`

**Proposed fix (lines 53-54):** Replace:

```
| Science / Earth tech anchors | `References/Science/Science.md` |
| Mana Bolt joule / Int curve | `References/Science/ManaCast.md`, chapter fight beats |
```

with:

```
| Science / Earth tech anchors | `References/World/Science/Science.md` |
| Mana Bolt joule / Int curve | `References/World/Science/Energy/ManaCast.md`, chapter fight beats |
```

---

### 3. Notes Source XP formulas

**Where:** `Story/Notes/Notes.md` (multiple places)

**What's wrong:** Still has old Source formulas:
- Ch 9: `49 + level`
- Ch 13: Wereboar `999 + level`
- Needle Moth: `99 + level`

**Canon:** `50 × L × RaceMult` in `References/Progression/Levels.md` and `Story/Notes/Experience.md`:
- Common goblin: L4 × 1.0 → solo **200**
- Wereboar: L26 × 2.0 → solo **2,600**
- Needle Moth: L18 × 2.0 → solo **1,800**
- Needle Worm: L16 × 0.5 → solo **400**

**Proposed fix:** Search `Story/Notes/Notes.md` for these old formulas and replace with worked examples using `50 × L × RaceMult`:

**Example Ch 9 passage** (if it mentions `49 + level`):
```
Wereboar L26 × RaceMult 2.0 → solo 2,600 XP
Needle Moth L18 × RaceMult 2.0 → solo 1,800 XP
Needle Worm L16 × RaceMult 0.5 → solo 400 XP
```

*(Search the file for `49 + level`, `999 + level`, `99 + level` and replace with the above examples matching the correct levels and multipliers from `Experience.md`.)*

---

### 4. Notes Ch 20 dusty Fire Arrow compare

**Where:** `Story/Notes/Notes.md` Ch 20 section

**What's wrong:** Dusty shelf comparison still reads:
- Runic Fire Arrow **2 LS** vs regular **3 SS** (~6–7×)

**Canon:** From `Story/Notes/StoryPrices.md` and `References/Runes/ScrollEconomy.md`:
- Regular Fire Arrow: **6 SS** (not 3 SS)
- Dusty runic Fire Arrow: **2 LS** vanity
- Fair High Common runic Fire Arrow: **10 SS**

**Actual ratios:**
- 2 LS vs 6 SS ≈ **3.3×** (not 6–7×)
- Fair High 10 SS is the clean target (~1.7× regular)

**Proposed fix:** Replace the Ch 20 dusty compare passage with:

```
Dusty shelf runic Fire Arrow (2 LS) is vanity markup over regular word Fire Arrow (6 SS) — about 3.3× for a Low/dusty runic. Fair High Common runic Fire Arrow (10 SS) is the clean target buyers should use: ~1.7× above regular, amp-capable.
```

---

### 5. Ideas Open: regular vs runic craft

**Where:** `References/Ideas.md` line 358 (approximate)

**What's wrong:** Still marks the process incomplete:
```
- **Regular vs runic scroll craft (open):** Drawing / making **regular magic scrolls** (incantation / word / mana-ink path) is different from **runic scrolls**. Ch 21 already shows Diagnosis blank on regulars and different laws; timings differ (~10 min Mana Arrow vs ~45 min Fire Orb runic). Still need to learn and lock the full difference (skills, process, what Drawing covers for each, Identify readout, materials). Not locked yet.
```

**Canon:** `References/Runes/ScrollEconomy.md`, `References/Runes/ScrollCraftScrapes.md`, `References/Runes/Magic.md` now carry extensive side-by-side lock:
- Word scrolls: mana-only fuel, frozen cast, grade from power injected, Diagnosis blank
- Runic scrolls: mana or stamina, user-powered machine, amp to rank ceiling, Drawing works
- Skills: Basic Mana Scribing for word; Basic Rune Scribing for runic
- Timings: ~10 min Mana Arrow vs ~45 min Fire Orb runic (locked)
- Costs: full word-scroll cost engine in ScrollEconomy

**Proposed fix (two options for David):**

**Option (a) — Narrow the Open wording to remaining gaps:**
```
- **Regular vs runic scroll craft (narrow open):** Word vs runic laws are largely locked (ScrollEconomy / ScrollCraftScrapes / Magic carry cost engine, skills, fuel, amp, Diagnosis blank on regulars, Drawing on runics, timings). Remaining open: exact activation energy digits for Common Fire Arrow (filtration / SP path), whether Edelgard shelf is mostly P1 empty vs mixed P9 prepaid, exact runic blank/ink mat cost (~2 SS/High placeholder).
```

**Option (b) — Close out if sufficient:**
```
- **Regular vs runic scroll craft:** Locked. Word scrolls (mana-only, frozen cast, Diagnosis blank, Basic Mana Scribing) vs runic scrolls (mana or stamina, amp-capable, Drawing, Basic Rune Scribing). Cost engine, skills, process, materials in ScrollEconomy / ScrollCraftScrapes / Magic. Open decisions (activation digits, P9 prepaid mix, exact runic mat cost) can defer until those beats are written.
```

---

### 6. Optional: EconomyDesign Spiked Boar stone

**Where:** `References/World/Society/Economy/EconomyDesign.md` (approximate line in Spiked Boar/Wereboar section)

**What's wrong:** Prices Spiked Boar / Wereboar chest at **100 LC (1 LS)** as leader-sized shorthand, but doesn't cite the body-size mod law.

**Canon:** `References/World/Fauna/Creatures.md` line 21:
```
Chest stone can reach leader-band volume via **body-size mod**, not title (`MonsterCores.md`).
```

**Proposed fix:** Add a one-line cite in EconomyDesign Spiked Boar row:

```
Spiked Boar L8 chest stone can reach leader-band volume (~1 LS) via body-size mod (Creatures.md), not title.
```

This clarifies the L8 @ 1 LS isn't a title law violation.

---

### 7. Optional soft: ManaMaterials

**Where:** `References/Runes/ManaMaterials.md` line 143 onward (Natural lean map)

**What's wrong:** Header defers to Metals; still lists old natural lean map with imbue forms for Earth Ag/Au/Ti, etc. Pre-conversion vs post-conversion split unclear.

**Canon:** `References/World/Materials/Metals.md` conversion lock:
- Ag → mythril
- Au → orihalcum (never hosts)
- Ti → adamantium (clear glass, never hosts)

**Proposal:** Add a clarifying note at the top of the Natural lean map (line ~142) **only if useful**:

```
**Pre- vs post-conversion split:** Earth materials (silver Ag, gold Au, titanium Ti) show natural lean as **pre-conversion** imbue hosts. After conversion (Ag → mythril, Au → orihalcum, Ti → adamantium), the **conversion lock** in `Metals.md` wins: orihalcum and adamantium never host runes. Mythril is native superconducting host (mode, not lean). Do not invent new material law from this table.
```

**Note:** This is optional and soft. ManaMaterials is marked "design loot" and already states Metals.md wins. Only add the note if confusion risk is real.

---

## Suggested Apply Order

Checklist for David:

1. **CrossCheck one-liners first** (RaceMult 1.5/2.0; Science paths)
2. **Notes hygiene** (Notes.md Source XP formulas; Ch 20 dusty compare)
3. **Ideas Open narrow/close** (regular vs runic craft — pick option (a) or (b))
4. **Optional EconomyDesign cite** (Spiked Boar body-size mod)
5. **Optional ManaMaterials note** (pre/post conversion split clarifier)

---

**End of note. Ready to apply whenever David wants.**
