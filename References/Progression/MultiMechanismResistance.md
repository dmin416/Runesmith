# Multi-Mechanism Damage: Projected Resistance

> **Ideas / design loot.** Hypothetical extension of `ResistanceImmunitySystem.md` for damage that hits through more than one mechanism. Adds the **Survival** family for deprivation. Live hubs win: `SkillsDesign.md`, `RolandResistanceTracks.md`, `SkillRanks.md`. Damage-type map: `DamageTypeResistances.md`. Radiation splits: `../World/Space/Radiation/`. Vision dazzle: `../World/Space/Radiation/RadiationVision.md`.

Promote a row into live law only when a chapter needs it and it abides existing curves.

## Conflicts (read first)

| Topic | Live lock | This idea |
|---|---|---|
| **Breath / oxygen** | Breath Control: `hold = T0 × M_body × skill_level`; **1 min held = 1 use** (`SkillsDesign.md`) | Suffocation: effect **1 min × M**; leveling **time** for apnea / bad air, **volume %** for hemorrhage |
| **Sleep / food / water** | Sleep Resistance cuts **need** (−10%/level → Immunity floor) | Sleep is a **Survival fuse parent** (with Suffocation / Starvation). Live Sleep wins until promote |
| **Deprivation** | No Undying Body / fused Survival track | **Undying Body** = multi-fuse (**2+** deprivation Imm L9). Also claimed sleep vs Mind → Iron Will |
| **Status** | Pain Resistance is a live track | Blind / Deaf / Stun still have no dedicated skill (matches `RadiationVision.md`) |
| **Sharp vs Pierce/Slash** | Roland Sharp = pierce + slash | This file says Sharp for gates and radiation thirds |

Soft-ok for prose framing when it matches live Heat/Cold/Poison/Pain M feel. Do not silently replace Breath Control or Sleep Resistance.

---

## 1. Survival family: Undying Body tree

Same tiers and M as every other family in `ResistanceImmunitySystem.md` (Resistance → Immunity → Fused).

**Unlike Thermal / Kinetic / Bodily / Mind (exactly two parents), Undying Body is a multi-fuse:** any **two or more** deprivation Immunities at L9 can combine. More parents can merge in later. Coverage is the **union** of whatever was fused in.

### Tree

```
Suffocation Resistance  →  Suffocation Immunity (L9) ──┐
Starvation Resistance   →  Starvation Immunity (L9)  ──┼─→  Undying Body (Fused L1)  →  Undying Body L9
Sleep Resistance        →  Sleep Immunity (L9)      ──┘         ▲
                                                                │
                    (optional later parents) ────────────────────┘
```

Alt fused name: **Self-Sustaining**.

**Deprivation parent set (current):** Suffocation Immunity, Starvation Immunity, Sleep Immunity. Room for more Survival Imm names later (same multi-fuse rule).

| Step | Requirement | Result |
|---|---|---|
| 1 | Climb each wanted branch Resistance → evolve at **2,000,000** → Immunity L1 | Separate Imm tracks |
| 2 | Climb each of those Immunities to **L9** (**500,000** uses each) | Imm L9 parents ready |
| 3 | **Any 2+** Imm L9 from the deprivation set | Fuse → **Undying Body** L1; coverage = union of those parents |
| 4 | Another deprivation Imm L9 while Undying Body already exists | **Merge in:** that column joins the fused skill; Undying Body **level stays**; parent Imm name is consumed |
| 5 | Climb Undying Body (**500,000** uses) | **Undying Body** L9 (M = 1,000×) on every column it owns |

Branches level independently. First fuse can be any pair (or all three at once). Full deprivation package needs **all three** parents in (at fuse or by later merge). Slowest missing parent sets when a column unlocks.

### Coverage by stage

| Skill name | Oxygen / hypoxia | Blood loss | Food / water | Sleep |
|---|---|---|---|---|
| **Suffocation** Res / Imm | Yes | Yes (as O₂ delivery failure) | No | No |
| **Starvation** Res / Imm | No | No | Yes | No |
| **Sleep** Res / Imm | No | No | No | Yes |
| **Undying Body** | Only if Suffocation was a parent | Only if Suffocation was a parent | Only if Starvation was a parent | Only if Sleep was a parent |

Examples:
- Suffocation Imm L9 + Starvation Imm L9 → Undying Body with O₂, blood, food/water. **No sleep column** until Sleep Imm L9 merges in.
- Suffocation + Sleep → O₂, blood, sleep. Still needs food/water from Starvation merge.
- All three Imm L9 → full package at first fuse.

Once a column is on Undying Body, **one M** applies to every owned column. Pre-fuse tables below still use that branch’s own M.

**Beside the tree (live until promote):**
- **Breath Control** = technique hold length (`T0 × M_body × level`). Not a Survival resist. Do not replace with Suffocation until promoted.
- **Sleep Resistance** is both the live need track and a **Survival fuse parent** (via Sleep Immunity). All-nighters bank Sleep until that Imm is fused or merged into Undying Body; afterward sleep debt banks Undying Body and need = normal ÷ M.
- **Iron Will** (Mind: Sleep Imm + Pain Imm) is a different fuse. Sleep Imm can feed **either** Undying Body **or** Iron Will, not both. Pain stays on Mind either way.

### Suffocation Resistance → Suffocation Immunity

**Branch job:** anything that starves tissue of oxygen: drowning, choking, smoke, vacuum, thin air, blood loss, a stopped heart and blood chokes.

- **Breath-hold (conscious without oxygen) = 1 min × M**
- **Brain damage onset without oxygen = 4 min × M**
- **Blood choke unconsciousness = 10 s × M**
- **Survivable blood loss = 1 − (0.6 / M)**
- **Unimpaired altitude:** functions normally when oxygen is at least **70% of sea level ÷ M**

| Lv | Suffocation Resistance | Suffocation Immunity | Undying Body |
|---|---|---|---|
| 1 | 1.1 min / 4.4 min | 11 min / 44 min | 1.9 h / 7.4 h |
| 2 | 1.3 min / 5 min | 13 min / 50 min | 2.1 h / 8.3 h |
| 3 | 1.4 min / 5.7 min | 14 min / 57 min | 2.4 h / 9.5 h |
| 4 | 1.7 min / 6.7 min | 17 min / 67 min | 2.8 h / 11 h |
| 5 | 2 min / 8 min | 20 min / 80 min | 3.3 h / 13 h |
| 6 | 2.5 min / 10 min | 25 min / 100 min | 4.2 h / 17 h |
| 7 | 3.3 min / 13 min | 33 min / 133 min | 5.6 h / 22 h |
| 8 | 5 min / 20 min | 50 min / 200 min | 8.3 h / 33 h |
| 9 | 10 min / 40 min | 100 min / 400 min | 17 h / 67 h |

(Breath-hold / brain damage onset)

| Tier | Survivable blood loss |
|---|---|
| Resistance Lv1 | 46% |
| Resistance Lv5 | 70% |
| Resistance Lv9 | 94% |
| Immunity Lv9 | 99.4% |
| Undying Body Lv9 | 99.94% |

Baseline: **40%** blood loss is lethal.

| Situation | Oxygen |
|---|---|
| Sea level | 100% |
| Denver | ~83% |
| La Paz, Bolivia | ~64% |
| Everest summit | ~33% (Resistance Lv6 for no impairment) |
| House fire after flashover | Near 0% |
| Underwater, vacuum | 0% |

### Starvation Resistance → Starvation Immunity

**Branch job:** lack of food and water only. Not oxygen, blood, or sleep.

- **Survival without water = 3 days × M**
- **Survival without food (with water) = 45 days × M**
- **Daily food and water needed = normal ÷ M**

| Tier | Without water | Without food | Daily need |
|---|---|---|---|
| Resistance Lv1 | 3.3 days | 50 days | 90% |
| Resistance Lv5 | 6 days | 90 days | 50% |
| Resistance Lv9 | 30 days | 15 months | 10% |
| Immunity Lv5 | 2 months | 2.5 years | 5% |
| Immunity Lv9 | 10 months | 12 years | 1% (20 kcal, 25 ml water) |
| Undying Body Lv5 | 1.6 years | 25 years | 0.5% |
| Undying Body Lv9 | 8 years | 123 years | 0.1% |

### Undying Body (Fused)

**What it is:** the Survival family’s fused **deprivation resistance** skill. Multi-fuse (2+ parents), not a fixed pair. Consumes the parent Immunity names that went in; later Imm L9 parents can still merge.

**What it can cover** (only columns whose parent was fused or merged; one M for all owned columns):

1. Oxygen / hypoxia (breath-hold, altitude, smoke, vacuum, stopped heart) — from **Suffocation**
2. Blood loss — from **Suffocation**
3. Food and water — from **Starvation**
4. Sleep — from **Sleep**

Effect numbers: use the branch tables above at **Undying Body’s** M for owned columns, plus when sleep is owned:

- **Daily sleep needed = normal ÷ M** (soft-ok with live Sleep Resistance −10%/level → floor)
- M = **111× (L1) → 1,000× (L9)**
- **Dormancy** (unlock at first fuse): voluntary suspended animation. All *owned* Survival timers **×10** while dormant. Waking takes one minute. Not free sleep credit; chosen shut-down.

**Who banks uses where**

| Situation | Banks this skill | Meter |
|---|---|---|
| Breath-hold, smoke, altitude, vacuum, blood *choke* (no bleed), stopped breathing | **Suffocation** → **Undying Body** (if O₂ owned) | **Time** |
| Hemorrhage, drain, donation, wound volume actually lost | **Suffocation** → **Undying Body** (if blood owned) | **Volume %** |
| Fasting, desert thirst, siege hunger | **Starvation** → **Undying Body** (if food/water owned) | Food/water (open) |
| All-nighter / sleep debt | **Sleep** Res/Imm → **Undying Body** (if sleep owned) | **Time** |

**Clean-use units (flat `SkillRanks.md`)**

Two different meters on the same Suffocation / Undying Body bar. Use the one that matches the stress. **Do not double-count** the same hemorrhage as both volume and hypoxic seconds. Extra apnea *on top of* a drain (holding breath while already short on blood) may still add time uses.

| Deprivation | Unit | Notes |
|---|---|---|
| **Breath / hypoxia** (airway, ambient O₂, circulatory stop without bleed) | **15 s** under load = 1 use | 1 min held = **4** uses. Partial seconds add up. |
| **Blood loss** (volume leaves the body) | **1% of full blood volume** lost and survived = 1 use | Fractions count (0.2% = 0.2 use). % of *that body’s* normal full volume, not a fixed mL. Adult ~5 L → **~50 mL ≈ 1% ≈ 1 use**. |
| **Sleep debt** | **15 s** awake past remaining need = 1 use | Same time clock as breath. |
| **Food / water** | Still open | Lock when a chapter needs it. |

Blood choke / strangulation with no external loss = **time** (delivery stopped, tank still full). Open bleeding = **volume**.

Stay under **survivable blood loss** for the current M, or the session kills instead of ranking. Recovery / potions refill the tank so volume can be spent again; refill itself is not a use. Soft same-mode repeats may taper like other resists.

### Training sources

| Track | Sources |
|---|---|
| **Suffocation** | Freediving, breath-hold drills, high altitude, smoke ruins, drowning traps, water monsters, **bleeding / blood drains** |
| **Starvation** | Fasting, desert crossings, sieges, long expeditions |
| **Sleep** | All-nighters, siege watches, forced marches, sedative push-through (live Sleep Resistance grind) |
| **Undying Body** | Any owned column’s sources after fuse/merge; high ranks: sealed tombs, deserts, vacuum, near-lethal blood loss, multi-day wakefulness |

### Leveling pace (projected)

Flat curve. No short-climb brake. Path counts are in the tree table above. Breath and blood both fill Suffocation (then Undying Body); they are not the same daily rate.

**Breath / hypoxia only (15 s = 1 use)**

| Pace | Held / hypoxic time / day | Uses / day | → Res L5 (1k) | → Res L9 (500k) | → Imm L1 (2M) | → Imm L9 (~2.5M) |
|---|---:|---:|---|---|---|---|
| Ch 19 grill intensity | ~140 min | ~560 | **~2 days** | **~2.4 yr** | **~10 yr** | **~12 yr** |
| Hard daily drill | 60 min | 240 | ~4 days | ~5.7 yr | ~23 yr | ~28 yr |
| Field / mixed life | 15 min | 60 | ~17 days | ~23 yr | ~91 yr | ~114 yr |

**Blood volume only (1% lost = 1 use)**

Recovery-gated. Ordinary donation pace is far slower; with Recovery / potions a dedicated grind can re-lose a few percent per day.

| Pace | Volume lost / day (of full tank) | Uses / day | → Res L5 (1k) | → Res L9 (500k) | → Imm L9 (~2.5M) |
|---|---:|---:|---|---|---|
| Soft (Ned nibble / small drains) | ~1% | ~1 | ~3 yr | ~1,370 yr | legendary |
| Hard Recovery grind | ~5% | ~5 | ~200 days | ~274 yr | still career+ |
| Extreme (potions, near current survivable cap) | ~10% | ~10 | ~100 days | ~137 yr | still career+ |

Breath is the practical Suffocation climb. Blood is scarcer, dangerous, and mostly spices the bar unless Recovery is the whole training plan. A single bad fight that dumps **20%** volume is **20** uses if survived; it does not equal 20 minutes of holds.

**Undying Body L1→L9:** **500,000** deprivation uses on the fused name (any *owned* type). ~8 h sleep debt ≈ **1,920** uses. Breath + sleep move the bar fast; blood adds in % chunks. Cost to first fuse depends on how many parents you bring (2 or 3 Imm L9 tracks). Merging a late parent does not reset Undying Body level. Calendar follows the slowest parent you still need (often Starvation).

---

## 2. Status outcomes have no skill

Pain Resistance is the only skill that targets a status. Blindness, deafness and stun come from damage; only the skill against that damage helps.

| Outcome | Cause | Skill that helps |
|---|---|---|
| Blind | Bright flash (dazzle) | None. Normal eye function |
| Blind | Retinal or corneal burn | Heat (eyes one level lower) |
| Blind | Chemical in eyes | Poison (eyes one level lower) |
| Blind | Pepper spray, tear gas | Pain (eye clamping is a pain reflex) |
| Deaf | Eardrum rupture, loud noise | Blunt (ears one level lower) |
| Stun | Concussion | Blunt (80 g × M) |
| Stun | Blood choke | Suffocation (10 s × M) |
| Stun | Electric muscle lockup (Taser) | None. Pain covers the pain only |
| Knocked out | Heart or breathing stopped by current | Suffocation keeps the brain alive |

---

## 3. Five ways damage combines

| Type | What happens | Example |
|---|---|---|
| **Split** | One damage pool divided across mechanisms | Radiation, electrocution |
| **Parallel** | One event, several separate hazards | Explosion, house fire |
| **Gated** | Second mechanism only works if the first succeeds | Snakebite, poisoned blade |
| **Converted** | Blocked damage turns into another type | Stopped bullet becomes Blunt |
| **Amplified** | One injury weakens defense against another | Burned skin is easier to cut |

---

## 4. Split damage

```
Effective amount = actual amount × Σ (fᵢ / Mᵢ)
M_eff = 1 / Σ (fᵢ / Mᵢ)
```

- `fᵢ` = fraction of damage from each mechanism (fractions add to 1)
- `Mᵢ` = multiplier of the skill covering that mechanism
- No levels in a mechanism → M = 1
- A component under its own skill's threshold contributes 0

### Weakest link rule

The lowest skill dominates. An unleveled fraction caps the whole defense:

**M_eff can never exceed 1 / f_unleveled**

| Unleveled fraction | Maximum M_eff |
|---|---|
| 50% | 2× |
| 30% | 3.33× |
| 10% | 10× |
| 1% | 100× |

Leveling one skill to Fused tier does almost nothing if its partner stays at zero.

---

## 5. Parallel damage

Each hazard is checked separately against its own skill. Injuries stack. The worst one usually decides survival.

**Bleeding rule:** every Sharp wound that bleeds adds a Suffocation check for blood loss.

---

## 6. Gated damage

The gate (usually Sharp) must fail before the payload enters the body.

- **Gate fails:** full payload, checked against its own skill
- **Gate holds:** stopped weapon becomes Blunt; payload only touches skin

**Skin contact dose = payload × A**

| Payload | Absorption through intact skin (A) |
|---|---|
| Snake venom, most animal venoms | ~0 (proteins cannot cross skin) |
| Most plant toxins, ingested poisons | ~0.01–0.1 |
| Nerve agents (VX), hydrofluoric acid, skin-penetrating solvents | ~1 (gate does nothing) |

Weak points (eyes, mouth, ear canal) absorb fully. Spitting cobra venom in the eyes bypasses the gate.

---

## 7. Converted damage

Existing rule: a stopped blade or bullet delivers its force as Blunt on a small area.

Added projections:
- **Hollow-point or tumbling bullet that penetrates:** Sharp wound + Blunt check for the internal shock cavity
- **Stopped explosive fragment:** Blunt hit
- **Gear over its own heat limit:** molten or burning gear becomes a new Heat source stuck to the skin

---

## 8. Amplified damage

| Condition | Effect at the injured area |
|---|---|
| Burned skin (Heat threshold exceeded) | Sharp uses one level lower |
| Frozen tissue (Cold threshold exceeded) | Sharp and Blunt use one level lower (brittle) |
| Burned or frozen weak point (eyes, mouth) | Two levels lower |
| Body over heat threshold during Poison or radiation exposure | Effective dose ×2 (heat cripples cell repair) |
| Alcohol + sedative together | Combined effect ×1.5 (synergy) |
| Body over heat threshold while suffocating | Suffocation timers ÷2 (hot tissue burns oxygen faster) |
| Body below cold core limit while suffocating | Suffocation timers ×2 (cold slows oxygen use; cold-water drowning survivors) |

---

## 9. Blast projection

The base system has no overpressure rule. Projected:
- **Lung injury: 100 kPa × M** (Blunt)
- **Eardrum rupture: 35 kPa × M one level lower** (Blunt, weak point)

| Blast | Overpressure |
|---|---|
| Windows shatter | ~7 kPa |
| Eardrums rupture (baseline) | ~35 kPa |
| Buildings collapse | ~35–70 kPa |
| Lung injury (baseline) | ~100 kPa |

---

## 10. Damage splits

| Damage | Split |
|---|---|
| Gamma, X-ray, beta, protons | ⅓ Sharp, ⅔ Poison |
| Neutrons | Blunt |
| Alpha, heavy cosmic ions | Sharp |
| UV | Poison |
| Criticality accident (neutron + gamma) | ½ Blunt, ⅙ Sharp, ⅓ Poison |
| Electrocution, lightning | ½ Heat, ⅕ Sharp, 30% Suffocation (heart or breathing stops) |
| Carbon monoxide alone | **Suffocation** (binds hemoglobin; O₂ delivery fails) |
| Cyanide alone | **Poison** (blocks cellular respiration) |
| **House-fire smoke** (inhaled plume) | **½ Suffocation, ⅖ Poison, ⅒ Heat** (see House fire) |
| Concentrated acid | 70% Poison, 30% Heat (local heating can approach boiling) |
| Pepper spray, tear gas | Pain, minor Poison |

---

## 11. Mechanisms with no skill

| Mechanism | Found in |
|---|---|
| Dazzle from bright light | Flashbangs, nuclear flash, lasers below burn level |
| Muscle lockup from current | Taser, electric fences |

---

## 12. Worked examples

### Gamma radiation (split)

Baseline LD50 = 4.5 Sv.

| Build | M_eff | LD50 |
|---|---|---|
| Poison Immunity Lv9 alone | 2.9× | 13 Sv |
| Poison Immunity Lv9 + Sharp Resistance Lv5 | 5.8× | 26 Sv |
| Poison Immunity Lv9 + Melee Immunity Lv9 | 143× | 643 Sv |
| Pure Blood Lv9 + Melee Immunity Lv9 | 1,000× | 4,500 Sv |

### Criticality accident (split)

Baseline: ~17 Sv is fatal.

| Build | M_eff | Effective dose | Outcome |
|---|---|---|---|
| None | 1× | 17 Sv | Fatal |
| Blunt Imm Lv9 + Poison Imm Lv9, no Sharp | 5.7× | 3 Sv | Moderate sickness, survives |
| Melee Imm Lv9 + Pure Blood Lv9 | 1,000× | 0.017 Sv | Nothing |

### Electrocution / lightning (split)

Lightning usually stops the heart and breathing. The heart often restarts; breathing does not. Most deaths come from the brain starving of oxygen afterward.

| Build | M_eff |
|---|---|
| Heat Imm Lv9 + Sharp Imm Lv9, no Suffocation | 3.26× (capped by unleveled 30%) |
| Heat, Sharp, Suffocation all Resistance Lv9 | 10× |
| Heat, Sharp, Suffocation all Immunity Lv9 | 100× |
| Temperature Imm + Melee Imm + Undying Body, all Lv9 | 1,000× |

With Suffocation Immunity Lv5, a struck character stays conscious **20 minutes** with stopped breathing, long enough for it to restart. Muscle lockup during the strike still happens at every level.

### House fire (parallel + one smoke split)

A structure fire is **several hazards at once**, not one damage pool. Check each row. Only the **inhaled smoke plume** is a split (fractions add to 1).

**Why those smoke ratios:** most civilian fire deaths are inhalation. CO and oxygen starvation in the plume dominate → **½ Suffocation**. HCN, acid gases, aldehydes, and chemical lung injury → **⅖ Poison**. Hot gases and glowing soot cook the airway → **⅒ Heat** (lungs/airway as weak point: Heat one level lower on that part if you track it). Pure ½/½ CO–cyanide undercounts CO and ignores airway heat; leaving any of the three unleveled still caps the plume hard.

| Hazard | Kind | Skills / split | Projection |
|---|---|---|---|
| Room heat before flashover (100–300°C air / radiant) | Parallel | **Heat** | Heat Imm Lv6 (212°C) to Lv7 (270°C) |
| Flashover (600°C+ enclosure) | Parallel | **Heat** | Heat Imm Lv9 (~737°C tissue band) |
| **Inhaled smoke plume** (CO + HCN + irritants + hot gas) | **Split** | **½ Suffocation, ⅖ Poison, ⅒ Heat** | See M_eff table below |
| Oxygen-starved pocket (post-flashover, near 0% O₂) | Parallel | **Suffocation** | Pure timer; Imm Lv5 → ~20 min conscious |
| Falling debris / glass (if the building fails) | Parallel | Sharp / Blunt | Only if that beat happens |

**Smoke plume M_eff** (`M_eff = 1 / Σ (fᵢ / Mᵢ)`):

| Build | M_eff vs plume | Note |
|---|---:|---|
| None | 1× | Normal lethal smoke |
| Poison Imm Lv9 only | ~1.7× | Unleveled ½ Suff + ⅒ Heat (cap 1/0.6 ≈ 1.7×) |
| Suffocation Imm Lv9 only | ~2.0× | Unleveled ⅖ Poison + ⅒ Heat (cap 1/0.5 = 2×) |
| Heat Imm Lv9 only | ~1.1× | Almost worthless alone on smoke |
| Poison Imm Lv9 + Suffocation Imm Lv9, no Heat | ~9× (cap **10×**) | Unleveled ⅒ Heat |
| Heat + Poison + Suffocation, all Imm Lv9 | **100×** | Full coverage; fractions sum to 1, no leftover |
| Temperature Imm + Pure Blood + Undying Body (O₂ owned), all Lv9 | **1,000×** | Fused caps on every smoke column |

**Full walkthrough (all damage types covered):** Heat Imm Lv9 (or Temperature Imm) + Poison Imm Lv9 (or Pure Blood) + Suffocation Imm / Undying Body with O₂. Room heat and flashover sit under Heat thresholds; plume is ~100×–1,000×; low-O₂ pocket is a Suffocation timer. Searches the building and walks out. Missing **any** of the three smoke skills leaves a 10%–50% unleveled slice and the plume still bites.

### Drowning in ice water (parallel, amplified)

| Build | Projection |
|---|---|
| None | Conscious ~1 min; cold extends brain survival somewhat |
| Cold Res Lv9 + Suffocation Res Lv9 | No cold damage; 10 min breath-hold, 40 min to brain damage |
| Suffocation Imm Lv9, no Cold | Hypothermia sets in, but cold doubles timers: 200 min breath-hold |

### Grenade (parallel)

| Hazard | Skill | Projection |
|---|---|---|
| Fragments ~1,200–1,500 m/s | Sharp | Melee Imm Lv8 stops most; Lv9 stops all |
| Overpressure at close range | Blunt | Blunt Imm tiers prevent lung injury |
| Eardrums | Blunt (one level lower) | Deafness before lung injury |
| Flash | None (dazzle) | Temporary blindness at every level |
| Fragment wounds that bleed | Suffocation | Blood loss check |

### Snakebite (gated)

Treat a fang like a knife tip (10–50 N).

| Sharp skill | Result |
|---|---|
| None | Full venom dose vs Poison |
| Sharp Res Lv5 (40 N) | Most bites fail; venom on skin does nothing |
| Sharp Res Lv9 (200 N) | All snakebites fail |
| Any level, venom spat into eyes | Full dose through the weak point |

### Poisoned blade (gated)

| Sharp holds? | Result |
|---|---|
| No | Wound + full poison ÷ Poison M + bleeding check |
| Yes, ordinary poison | Blunt bruise + poison × 0.01–0.1 on skin |
| Yes, contact nerve agent | Blunt bruise + full dose; only Poison protects |

### Acid attack (split + threshold)

| Build | Projection |
|---|---|
| Poison Imm Lv9, no Heat | M_eff 3.3×; heat burns from the reaction remain |
| Poison Imm Lv9 + Heat Res Lv9 (107°C) | Heat under threshold → M_eff 100× |
| Acid in the eyes | Poison one level lower |

### Pepper spray (Pain)

Raw eye pain ~8. Eyes use one level lower.

| Build | Effective pain | Result |
|---|---|---|
| None | 8 | Eyes clamp shut, blinded |
| Pain Res Lv9 (eyes act as Lv8, 5×) | 1.6 | Eyes stay open; stinging and tears only |
| Pain Imm Lv1+ | Pain switch off | No effect |

### Spiked drink (amplified)

Knockout sedative (potency 1.0) in a drink at 0.15% BAC.

**Breathing failure index = 1.5 × (effective BAC ÷ 0.40% + effective sedative ÷ lethal sedative dose)**. Index ≥ 1 stops breathing; Suffocation timer starts.

| Build | Sleep potency | Effective BAC | Breathing index |
|---|---|---|---|
| None | 1.0 (knocked out) | 0.15% | 0.71 (dangerous) |
| Alcohol, Sleep, Poison Res Lv5 | 0.5 (awake, drowsy) | 0.075% | 0.36 |
| Iron Will + Pure Blood | ~0 | ~0 | ~0 |

### Frozen limb struck by a hammer (amplified)

Limb past Cold threshold freezes solid. Blunt and Sharp drop one level at that limb. A hammer that bounces off a healthy arm can shatter a frozen one.

### Buried under rubble (parallel)

| Hazard | Skill | Projection |
|---|---|---|
| Crushing weight | Blunt | Blunt Imm Lv1 handles ~3.3 t uninjured |
| Breathing against the load | Suffocation | Suffocation Imm Lv9 lasts 100 min per breath |
| Days trapped | Starvation | Starvation Res Lv5 survives 6 days without water |

### Desert exposure (parallel)

| Hazard | Skill | Projection |
|---|---|---|
| Air and sand ~50°C | Heat | Heat Res Lv5 (51°C) prevents damage |
| Water loss | Starvation | Starvation Res Lv9: 30 days without water |
| Unfiltered sun UV | Poison | Sunburn reduced by Poison M |

### Vacuum exposure (parallel)

| Hazard | Skill | Projection |
|---|---|---|
| No oxygen | Suffocation | Undying Body Lv9: 17 h conscious |
| Tissue swelling | Blunt | Blunt Resistance tiers |
| Sun-side heat / shade-side cold | Heat / Cold | Temperature Immunity covers both |
| Radiation | Split | Pure Blood + Melee Immunity |

### Nuclear detonation (parallel)

| Hazard | Skill |
|---|---|
| Thermal flash | Heat |
| Dazzle | None |
| Blast wave, being thrown | Blunt |
| Flying glass and debris | Sharp |
| Prompt radiation | Split: ⅓ Sharp, ⅔ Poison (neutron portion Blunt) |
| Firestorm oxygen loss | Suffocation |
| Fallout | Split + Poison (inhaled particles bypass skin) |

Fused Melee, Temperature, Pure Blood and Undying Body together cover every hazard. The flash still blinds temporarily.

---

## 13. Quick rules

1. Split damage: `M_eff = 1 / Σ (fᵢ / Mᵢ)`. The weakest skill dominates.
2. Any unleveled fraction caps total protection at `1 / f_unleveled`.
3. Parallel hazards are checked separately; the worst one decides survival.
4. Sharp is the gate for injected payloads. Venoms fail if the skin holds.
5. Stopped weapons and fragments become Blunt.
6. Burned or frozen areas drop one level; weak points drop one more.
7. Bleeding wounds trigger Suffocation checks.
8. Blindness, deafness and stun have no skill. Only the skill against the underlying damage helps. Pain is the one exception.
9. Dazzle and electric muscle lockup affect every build.
