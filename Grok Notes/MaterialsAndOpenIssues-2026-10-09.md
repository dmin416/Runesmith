# Materials and Open Issues - 2026-10-09

**Scratch notes from Grok Bot.** This note is located in `Grok Notes/` only and is not story canon. Compiled 2026-10-09 per David's request.

## Purpose

This note provides (1) a recheck of remaining open issues after recent main-branch updates, and (2) a compiled inventory of all metals, minerals, and materials in the story, sorted into well-researched versus needing more research categories.

---

## 1. Open Issues Still Live on Main Branch

Verified against current main branch files as of 2026-10-09. Fixed items from the 2026-10-06 hygiene note (CrossCheck RaceMult and Science paths) are dropped.

### Issue A: Notes Source XP formula (one mention)

**Where:** `Story/Notes/Notes.md` line 123

**What's wrong:** Ch 9 Source comparison still mentions the old formula:
- "XP uses live `50 × L` (Source `49 + level` discarded)."

**Canon:** Live formula is `50 × L × RaceMult` in `References/Progression/Levels.md` and `Story/Notes/Experience.md`. The mention correctly notes the old formula is discarded, but the new formula statement is incomplete.

**Proposed fix (line 123):** Replace the XP clause with:
```
XP uses live `50 × L × RaceMult` (Source `49 + level` discarded).
```

### Issue B: Notes Ch 20 dusty Fire Arrow compare

**Where:** `Story/Notes/Notes.md` line 248

**What's wrong:** Dusty shelf comparison still reads:
- Runic Fire Arrow **2 LS** vs regular **3 SS** (~**6-7×**)

**Canon:** From `Story/Notes/StoryPrices.md` and `References/Runes/ScrollEconomy.md`:
- Regular Fire Arrow: **6 SS** (not 3 SS)
- Dusty runic Fire Arrow: **2 LS** vanity
- Fair High Common runic Fire Arrow: **10 SS**

**Actual ratios:**
- 2 LS vs 6 SS = **3.3×** (not 6-7×)
- Fair High 10 SS is the clean target (~1.7× regular)

**Proposed fix (line 248):** Replace the Exeor's section with:
```
- **Exeor's Magic Emporium** (3-story; auto doors; potions/scroll/staff sign). Regular scroll prices similar. Dusty runic section (Orb of Light, Fire Arrow, Aqua Ball): Orb of Light ≥1 LS; runic Fire Arrow **2 LS** vs regular **6 SS** (~**3.3×** for Low/dusty vanity markup) because Runesmith + long craft time. Fair High Common runic Fire Arrow (10 SS) is the clean target buyers should use.
```

### Issue C: Ideas Open - regular vs runic scroll craft

**Where:** `References/Ideas.md` line 359

**What's wrong:** Still marked incomplete:
```
- **Regular vs runic scroll craft (open):** Drawing / making **regular magic scrolls** (incantation / word / mana-ink path) is different from **runic scrolls**. Ch 21 already shows Diagnosis blank on regulars and different laws; timings differ (~10 min Mana Arrow vs ~45 min Fire Orb runic). Still need to learn and lock the full difference (skills, process, what Drawing covers for each, Identify readout, materials). Not locked yet.
```

**Canon:** `References/Runes/ScrollEconomy.md`, `References/Runes/ScrollCraftScrapes.md`, `References/Runes/Magic.md` now carry extensive side-by-side lock:
- Word scrolls: mana-only fuel, frozen cast, grade from power injected, Diagnosis blank
- Runic scrolls: mana or stamina, user-powered machine, amp to rank ceiling, Drawing works
- Skills: Basic Mana Scribing for word; Basic Rune Scribing for runic
- Timings: ~10 min Mana Arrow vs ~45 min Fire Orb runic (locked)
- Costs: full word-scroll cost engine in ScrollEconomy

**Proposed fix (two options):**

**Option (a) - Narrow the Open wording to remaining gaps:**
```
- **Regular vs runic scroll craft (narrow open):** Word vs runic laws are largely locked (ScrollEconomy / ScrollCraftScrapes / Magic carry cost engine, skills, fuel, amp, Diagnosis blank on regulars, Drawing on runics, timings). Remaining open: exact activation energy digits for Common Fire Arrow (filtration / SP path), whether Edelgard shelf is mostly P1 empty vs mixed P9 prepaid, exact runic blank/ink mat cost (~2 SS/High placeholder).
```

**Option (b) - Close out if sufficient:**
```
- **Regular vs runic scroll craft:** Locked. Word scrolls (mana-only, frozen cast, Diagnosis blank, Basic Mana Scribing) vs runic scrolls (mana or stamina, amp-capable, Drawing, Basic Rune Scribing). Cost engine, skills, process, materials in ScrollEconomy / ScrollCraftScrapes / Magic. Open decisions (activation digits, P9 prepaid mix, exact runic mat cost) can defer until those beats are written.
```

---

## 2. Materials Inventory

All metals, minerals, and notable materials named in References, sorted into two buckets.

### 2.A. Well-Researched / Mostly Locked

Materials with clear conversion law, Earth anchor, story role locked, or substantial filed research.

#### Metals - Conversion Line (MAGIC)

| Material | Earth Anchor | Terra Form | Role | Main File Path |
|---|---|---|---|---|
| **Mythril** | Silver (Ag) | Converted Ag (grades by %) | ~10% lighter than steel, sword-grade strength, extreme conductivity; best common rune host below aetherium | `References/World/Materials/Metals.md` |
| **Orihalcum** | Gold (Au) | Converted Au | Magic resistance = % conversion; antimagic shield stock; never a rune host | `References/World/Materials/Metals.md` |
| **Aurium** | Copper (Cu) | Converted Cu | Damps flowing mana; cuts waste; industrial insulator for pipes/grips/wraps | `References/World/Materials/Metals.md` |
| **Darkiron / Star Iron** | Iron (Fe) | Converted Fe (<80% / ≥80%) | Mana-friendlier and tougher under damage as % rises; still ferromagnetic | `References/World/Materials/Metals.md` |
| **Darksteel / Star Steel** | Steel | Converted steel (<80% / ≥80%) | Prime melee adventurer stock; conversion improves mana flow in channels and endurance under rune damage | `References/World/Materials/Metals.md` |
| **Adamantium** | Titanium (Ti) | Converted Ti | Cast-final indestructible; extreme hardness; heat spreader; ~0 expansion; sound-resonance weakness; never a rune host | `References/World/Materials/Metals.md` |
| **Durium** | Vanadium (V) | V-line metal from dark blue ore | Crude brittle / refined strong; base for durasteel | `References/World/Materials/Metals.md` |
| **Durasteel** | Vanadium carbide (VC) | Darksteel + 20-35% vol durium carbide | Steel-weight cermet; armor, tools, prestige hammers, golems | `References/World/Materials/Metals.md` |
| **Aether Durasteel** | V-line | Durasteel + thin aether phase | Fire-gear refine; slightly lighter | `References/World/Materials/Metals.md` |

#### Metals - Mundane (COMMON)

| Material | Role | Notes |
|---|---|---|
| **Copper (Cu)** | COMMON coin and craft metal | Early smelting stock; decent mana path |
| **Iron / Steel** | COMMON baseline forge metal | Wrought iron, hardened steel, carburized steel |
| **Silver (Ag)** | COMMON coin and craft metal | Charges near mages without converting to mythril |
| **Gold (Au)** | COMMON coin and craft metal | Decorative metal |
| **Tin (Sn)** | COMMON alloying metal | Bronze component |
| **Bronze** | COMMON alloy | Cu + Sn; early forge stock and coin metal |
| **Brass** | COMMON alloy | Cu + Zn via calamine cementation; process in `References/World/Science/Metallurgy/Brass.md` |

#### Metals - Specialty & Prestige (MAGIC / SPECIALTY)

| Material | Earth Anchor | Role | Main File Path |
|---|---|---|---|
| **Etherium** | NbTi analog | Persistent-current store; tower cores; clean transfer; mixes raise Jc/storage | `References/World/Materials/Metals.md` |
| **Star Silver** | Sterling-like | Clean silver-copper feel with radiation-hard rune-life bonus | `References/World/Materials/Metals.md` |
| **Resistium** | ODS additive | Inherits host path feel; raises rune life on lattice-damage axis | `References/World/Materials/Metals.md` |
| **Arcanite** | Reserved crystal | Prestige; diamond-class hardness; clean cleavage; placeholder | `References/World/Materials/Metals.md` |
| **Ebonite** | Shadow ore | Separate black ore line; unrefined/refined grades | `References/World/Materials/Metals.md` |
| **Tungsten** | W | SPECIALTY; powder-metallurgy path; tools that hold edge at red heat | `References/World/Science/Metallurgy/MetalOres.md` |
| **Molybdenum** | Mo | SPECIALTY; cheaper partial substitute for tungsten in steel | `References/World/Science/Metallurgy/MetalOres.md` |
| **Chromium** | Cr | SPECIALTY; ferrochrome for stainless (not baseline cookware) | `References/World/Science/Metallurgy/MetalOres.md` |
| **Nickel** | Ni | SPECIALTY; hydromet electrowinning and alloy paths | `References/World/Science/Metallurgy/Nickel.md` |
| **Platinum group** | Pt, Pd, Ir, Os, Rh | SPECIALTY; placer nuggets; extreme heat for casting | `References/World/Science/Metallurgy/MetalOres.md` |

#### Stone Materials (MAGIC)

| Material | Type | Role | Main File Path |
|---|---|---|---|
| **Arcanium** | Stone-metal from cores | Less refined; brittle ceramic with metallic give; disperses instead of melting | `References/World/Materials/Metals.md` (table), `References/World/Materials/MonsterCores.md` |
| **Aetherium** | Stone-metal from cores | Purer/lighter than arcanium; draws to fiber (mana fiber-optic feel) | `References/World/Materials/Metals.md` (table), `References/World/Materials/MonsterCores.md` |
| **Monster Cores / Mana Stones** | Gem-like crystals | Fuel, craft, runic slots, lamps; capacity ~1 mana/mm³; size from level curve; quality ladder | `References/World/Materials/MonsterCores.md` |

#### Non-Metal Materials (COMMON build and craft)

| Material | Type | Role |
|---|---|---|
| **Stone** | COMMON build | Cut/rubble, town walls |
| **Mortar / Lime** | COMMON build | Mortar binding |
| **Sand / Gravel** | COMMON build | Construction aggregate |
| **Brick / Clay** | COMMON build | Raw/fired/tile/pots |
| **Wood** | COMMON build | Framing/roofs/frontier OK |
| **Glass** | COMMON craft | Blown, uneven; windows by wealth |
| **Leather** | COMMON craft | Hide and armor stock |
| **Linen / Wool** | COMMON craft | Cloth stock |
| **Hemp / Rope** | COMMON craft | Cordage |
| **Parchment / Vellum** | COMMON craft | Writing stock |
| **Paper** | COMMON craft | Craftsman rag/hand stock |
| **Charcoal** | COMMON craft | Fuel reductant |

#### Low Mana Soak Materials

| Material | Property | Role | Main File Path |
|---|---|---|---|
| **Clay** | Low soak | Molds, refractory, insulator body; stays mostly itself under ordinary ambient | `References/World/Materials/Materials.md` |
| **Silicon / Silica** | Low soak | Sand, quartz, glass feed; barely converts | `References/World/Materials/Materials.md` |
| **Carbon** | Low soak | Charcoal, graphite, diamond-class C; does not turn into magic metal | `References/World/Materials/Materials.md` |

#### Biomaterials (COMMON and MAGIC)

| Material | Type | Role | Main File Path |
|---|---|---|---|
| **Hide / Bone / Scale** | COMMON beast | Mundane livestock and craft stock | `References/World/Materials/Materials.md` |
| **Magical Hide / Bone** | MAGIC beast | N× / monster grades from magical beasts | `References/World/Science/Biomaterials/Biomaterials.md` |
| **Silk (insect/spider)** | MAGIC beast | Bind, travel lines, snares, later load-bearing weave | `References/World/Science/Biomaterials/BiologicalSilks.md` |
| **Chitin** | Biomaterial | Tough polysaccharide; wing membranes, eye lenses clear; hardened in shells | `References/World/Materials/TranslucentMaterials.md` |
| **Chitosan** | Biomaterial | Modified chitin; dissolves in acid; flexible transparent film | `References/World/Materials/TranslucentMaterials.md` |

#### Glass and Translucent Materials

| Material | Type | Role | Main File Path |
|---|---|---|---|
| **Soda-lime glass** | Glass | Cheap everyday clarity; windows, bottles | `References/World/Materials/TranslucentMaterials.md` |
| **Borosilicate glass** | Glass | Lab glassware, cookware, lamp covers; resists thermal shock | `References/World/Materials/TranslucentMaterials.md` |
| **Fused silica** | Glass | UV optics, furnace tubes; handles 1,000°C+ | `References/World/Materials/TranslucentMaterials.md` |
| **Quartz** | Crystal | Crystalline SiO₂; Mohs 7; piezoelectric; oscillators, optics | `References/World/Materials/TranslucentMaterials.md` |
| **Diamond** | Crystal | Pure carbon; Mohs 10; best thermal conductor; cutting tools, heat spreaders | `References/World/Materials/TranslucentMaterials.md` |
| **Sapphire** | Crystal | Corundum (Al₂O₃); watch crystals, armored windows, LED substrates | `References/World/Materials/TranslucentMaterials.md` |

#### Hawaiian / Volcanic Island Minerals (Well-Researched)

| Material | Type | Role | Main File Path |
|---|---|---|---|
| **Titanomagnetite sand** | Iron ore | 45-58% Fe in magnetic concentrate; 5-15% TiO₂; best young-island ore | `References/World/Geography/HawaiianMinerals.md` |
| **Laterite / ferruginous crust** | Iron ore | 35-55% Fe as goethite/hematite; old wet uplands | `References/World/Geography/HawaiianMinerals.md` |
| **Olivine** | Magnesium mineral | Green sand; Mg and Ni source; foundry sand | `References/World/Geography/HawaiianMinerals.md` |
| **Basalt** | Rock | Building stone, cast basalt, rock wool, basalt fiber | `References/World/Geography/HawaiianMinerals.md` |
| **Coral / Limestone** | Mineral | CaO source on old islands; lime burning practical | `References/World/Geography/HawaiianMinerals.md` |
| **Pumice / Cinder** | Volcanic | Lightweight aggregate, scrub, road metal | `References/World/Geography/HawaiianMinerals.md` |
| **Peridot** | Gem | Olivine in nodules; gem and tradable | `References/World/Geography/HawaiianMinerals.md` |

---

### 2.B. Needs More Research

Materials with open sections, inspirational-only digits, design-loot tags, thin notes, conflicting anchors, or explicit Open lists.

#### Metals - Open Details

| Material | What's Open | Main File Path |
|---|---|---|
| **Mythril grades** | Inspirational physical table (density, tensile, Mohs, Vickers, melting) marked "inspirational only" and not locked; promote only when scene needs digit | `References/World/Materials/Metals.md` (line ~350) |
| **Darkiron / Star Iron grades** | Inspirational physical table marked "inspirational only" | `References/World/Materials/Metals.md` (line ~363) |
| **Darksteel / Star Steel grades** | Inspirational multipliers marked "inspirational only" | `References/World/Materials/Metals.md` (line ~377) |
| **Orihalcum / Aurium pure** | Inspirational physical table | `References/World/Materials/Metals.md` (line ~393) |
| **Durium / Durasteel / Etherium** | Inspirational physical table; "prefer locked V-line table" | `References/World/Materials/Metals.md` (line ~399) |
| **Conversion-% host feel** | Absolute cook speed/K_% digits unset; finish table is landmark planning only | `References/World/Materials/Metals.md` (line 419 Open) |
| **Ebonite geography** | Geography unset | `References/World/Materials/Metals.md` (line 422 Open) |
| **Metallic Zinc** | SPECIALTY invent; retort process in Brass.md; do not assume street ingots | `References/World/Materials/Materials.md`, `References/World/Science/Metallurgy/Brass.md` |
| **Mundane Titanium** | Not street stock; sponge Ti / Kroll plate is SPECIALTY invent path | `References/World/Materials/Materials.md` |

#### Mana Materials and Rune Path (Design Loot)

| Material | What's Open | Main File Path |
|---|---|---|
| **ManaMaterials.md host path-% tables** | Non-canon; old host path-% tables quarantined; colored mythril brand metals (red/blue/black mythril) non-canon | `References/Runes/ManaMaterials.md` (line 6 "Design loot") |
| **Imbue levels** | Dials; each level respects ceiling but exact numbers are dials | `References/Runes/ManaMaterials.md` (line 113) |
| **Band-pass feel** | Absolute multipliers open | `References/Runes/ManaMaterials.md` (line 126) |
| **Fire-lean mythril heat recycle** | Digits open; story mode | `References/Runes/ManaMaterials.md` (line 60) |
| **Mythril wipe T** | Δ stability factor and wipe temperature digits unset | `References/World/Materials/Metals.md` (line 90) |
| **Adamantium weakness alternate** | Electroplastic / forced mana current stays Soft unless reopened | `References/World/Materials/Metals.md` (line 425 Open) |

#### Monster Cores and Stone Refine

| Material | What's Open | Main File Path |
|---|---|---|
| **Artificial stones (space cook)** | Digits and shop recipe open until beat needs them | `References/World/Materials/MonsterCores.md` (line 70, line 84 Open) |
| **Battery and shard economics** | Beyond surface note | `References/World/Materials/MonsterCores.md` (line 84 Open) |

#### Biomaterials - Thin or Placeholder

| Material | What's Open | Main File Path |
|---|---|---|
| **Dead-loot N× sheets** | Horn, chitin, bone sheets when scene needs one | `References/World/Science/Biomaterials/Biomaterials.md` (line 121 Open) |
| **Monster grades beyond Ned** | Template given; need case-by-case fill | `References/World/Science/Biomaterials/Biomaterials.md` |

#### Hawaiian / Volcanic Island Minerals - Open Processes

| Material | What's Open | Main File Path |
|---|---|---|
| **Route H1 Ti residue upgrade** | Upgrade to 60-80% TiO₂ for chlorinator; digits open | `References/World/Geography/HawaiianMinerals.md` (line 300) |
| **Vanadium recovery** | Outline only; salt roast and precipitation steps need test | `References/World/Geography/HawaiianMinerals.md` (line 449) |
| **Aluminum soda sinter** | Ratio 1:0.3 to 1:0.5 range; exact digits open | `References/World/Geography/HawaiianMinerals.md` (line 489) |
| **Silica purification from olivine** | Acid leach and alkali fusion paths outlined; exact yields open | `References/World/Geography/HawaiianMinerals.md` (line 556) |
| **Silicon metal routes** | Magnesiothermic, aluminothermic, carbothermic; silane route marked "toxic, pyrophoric" | `References/World/Geography/HawaiianMinerals.md` (line 563) |
| **Elemental phosphorus** | White P is pyrophoric and poison; do not run without hazard plan | `References/World/Geography/HawaiianMinerals.md` (line 662) |

#### Translucent Materials - Preindustrial Substitutes

| Material | What's Open | Main File Path |
|---|---|---|
| **Silicone** | Requires advanced chemistry or magical equivalent; rune that forces quartz to "unknot" | `References/World/Materials/TranslucentMaterials.md` (line 137) |
| **Acrylic / Polycarbonate** | Petroleum and natural gas chemicals; not preindustrial | `References/World/Materials/TranslucentMaterials.md` (line 187) |

#### Materials with Conflicting or Thin Anchors

| Material | Issue | Main File Path |
|---|---|---|
| **Moon ores (red/blue)** | Ages of space-ambient soak; prestige when reachable; not a new Earth element; deposit split in Moons.md | `References/World/Materials/Materials.md` (line 26) |
| **Stillwire / Lightthread** | Mentioned as invent; no detail file yet | `References/World/Materials/Materials.md` (line 26) |

#### Source Loot Materials (Retune Only)

| Material | Status | Main File Path |
|---|---|---|
| **Source color mythril grades** | Non-canon as forge metals (black/blue/crimson/red mythril); live: plain mythril with elemental lean as mode only | `References/SourceLoot/Materials.md` (line 5 "Non-canon as forge metals") |
| **Source metal names** | Full Source material scan; spelling gate to live lock; do not copy Source names into live law | `References/SourceLoot/Materials.md` |

#### Open Research Lists in Ideas.md

`References/Ideas.md` contains multiple Open sections on materials, craft, and interactions that are marked incomplete or deferred.

---

## 3. Suggested Next-Research Order

Top 3-5 gaps to prioritize:

1. **Adamantium invent digits** - Resonant frequency destruction method, tuned tools (singing chisels), and plate vs mail vulnerability. Digits for quench-dump heat spreader feel and exact-size casting shrinkage. Locked feel is strong; exact numbers open.

2. **Mythril superconducting digits** - Jc ceiling, AC-loss feel for pulses, quench conditions on gear-grade stock, Δ stability factor and wipe T. Pattern stability Néel-Arrhenius lifetime formula is given (~1×10⁻⁹ s × e^Δ) but Δ ≈ 45 and wipe T ~350 K need scene validation.

3. **Artificial mana stone recipe** - Space-cook pressure + seed lattice to densify into stone-grade stock. Max ambient saturation plus pressure (mechanical crush, barrier shell, or both). Clay/silica/carbon matrix candidates. Output competes with arcanium → aetherium refine. Digits and shop recipe open until a beat needs them.

4. **Route H1 Ti residue to chlorinator feed** - Upgrade nonmagnetic tail from 30-50% TiO₂ to 60-80% via acid leach (HCl or H₂SO₄). Links to TitaniumProcessing.md chlorination and Kroll. Young volcanic island supply chain.

5. **Ebonite geography and refine grades** - Separate from Fe conversion. Own black ore line. Unrefined/refined grades mentioned but geography and refine process unset.

---

**End of note.**
