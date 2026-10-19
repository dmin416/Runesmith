# Mana Hands

**Canon lock** for the Mana Hands spell track. Sheet / prose name stays **Mana Hands** (also Mana Hand / mage hand). Not Mana Control (that is Regulation’s evolve: `SensingManaSoundSystem.md`).

Joule work table: `../World/Science/Energy/ManaCast.md` § Mana Hands. Thin catalog: `../Combat/Spells.md`. Rank curve base: `SkillRanks.md`.

## Forms

| Tier | Form | \(R\) at L9 | Feel |
|---|---|---|---|
| T1 | **Mana Hands** | 0.1 (0.9 done) | Body-taught: grab, refill, cook |
| T2 | **Mana Mind** | 0.01 | Thought-shaped multi-point / ink |
| T3 | **Mana Heart** | 0.001 | Will-tied sustain |
| T4 | **Mana Soul** | 0.0001 | Deep / many grips; rare |

## Mana ↔ joules

```
μ(INT) = (INT / 15)^0.8
A      = √C

mana_ideal = Useful_J / (10 × μ(INT) × A)
mana_paid  = mana_ideal × R
```

Useful_J from lift / throw / hold physics (`ManaCast.md`). Hands do **not** use Bolt \(\eta(L)\). Skill efficiency is \(R\) only.

## Efficiency \(R\)

Unskilled \(R = 1\). Each form’s L1–L9 takes equal bites of that tier’s decade.

| Form | \(R\) L1 → L9 | Step |
|---|---|---|
| Hands | 0.9 → … → 0.1 | 0.1 |
| Mind | 0.09 → … → 0.01 | 0.01 |
| Heart | 0.009 → … → 0.001 | 0.001 |
| Soul | 0.0009 → … → 0.0001 | 0.0001 |

Mana efficiency for the same job ≈ \(1/R\). Form L9 checkpoints: Hands **10×** · Mind **100×** · Heart **1000×** · Soul **10000×** vs unskilled tax.

## Every level upgrades everything

Each rank steps **all** axes together (same decade bite):

| Axis | Improves |
|---|---|
| Efficiency | \(R\) down one step |
| Accuracy | less bias vs intent |
| Precision | tighter scatter |
| Stability | less drift / tremor / fade |
| Mass / range / grips | also still scaled by Int |

**Accuracy / precision / stability** are where the force goes (not MP). Definitions: mean-on-target · repeat scatter · hold-over-time. Control slop follows the same decade idea as \(R\). Drawing / Multitasking / Shaping / Regulation / Scribing still stack on top.

**Evolve continuity:** prior form L9 is a **floor** on every axis. New form L1 takes the first step of the next decade (\(R\): 0.1 → 0.09 at Mind L1). Cum uses restart; power does not. No single-axis-only evolves.

## Level-up / evolve

Cum clean uses on the **current form name** (`SkillRanks.md` curve). Evolve at **2,000,000** → next form L1.

| Reach | Cum uses |
|---|---|
| L1 | 1 |
| L2 | 10 |
| L3 | 50 |
| L4 | 200 |
| L5 | 1,000 |
| L6 | 5,000 |
| L7 | 20,000 |
| L8 | 100,000 |
| L9 | 500,000 |
| Evolve | **2,000,000** |

### Uses per completed action

```
mass_units = ceil(mass_g / 100)     // weight rounds UP only
uses      += mass_units × time_s × area_cm²
```

One action = one finished intent (scribe a rune, hold the scroll up, set a crate, turn a skewer). Not micro-pulses. Area = mana contact patch (cm²). Time = attended seconds. Failures 0. Concurrent actions score separately. Clean ~**70%**.

| Action | uses |
|---|---|
| 100 g × 1 s × 1 cm² | **1** |
| 20 g × 1 s × 1 cm² | **1** (mass ceiled) |
| 1 kg × 1 s × 100 cm² | **1,000** |
| Scribe one rune (~30 g × 120 s × 0.05 cm²) | **6** |
| Hold that scroll up (~30 g × 5 s × 50 cm²) | **250** |

### Gates

| Band | Condition |
|---|---|
| L1–L6 | Volume |
| L7–L9 | Peak variety (fine / heavy-large / combat-speed) in the mix |
| Evolve | **2,000,000** uses + recent peak variety |
| Soul L9 | Track cap |

### Time within one form

Light ~**300**/day · scribe ~**2,000**/day · heavy ~**20,000**/day. 30-day months.

| Milestone | Cum | ~300/day | ~2,000/day | ~20,000/day |
|---|---|---|---|---|
| → L5 | 1,000 | ~3 days | ~0.5 day | — |
| → L7 | 20,000 | ~2 months | ~10 days | ~1 day |
| → L8 | 100,000 | ~11 months | ~1.7 months | ~5 days |
| → L9 | 500,000 | ~4.6 years | ~**8 months** | ~**25 days** |
| Fresh → evolve | 2,000,000 | ~18 years | ~**2.7 years** | ~**3.3 months** |
| After L9 → evolve | +1,500,000 | ~14 years | ~**2.1 years** | ~**2.5 months** |

### Full path Hands → Mind → Heart → Soul

| Step | Uses | \(R\) after | ~2,000/day | ~20,000/day |
|---|---|---|---|---|
| Hands → L9 | 500,000 | 0.1 | ~8 months | ~25 days |
| Hands L9 → **Mind** L1 | +1,500,000 | 0.09 | ~+2.1 years | ~+2.5 months |
| Mind → L9 | 500,000 | 0.01 | ~8 months | ~25 days |
| Mind L9 → **Heart** L1 | +1,500,000 | 0.009 | ~+2.1 years | ~+2.5 months |
| Heart → L9 | 500,000 | 0.001 | ~8 months | ~25 days |
| Heart L9 → **Soul** L1 | +1,500,000 | 0.0009 | ~+2.1 years | ~+2.5 months |
| Soul → L9 | 500,000 | 0.0001 | ~8 months | ~25 days |

**To Soul L9:** **6,500,000** uses ≈ **~8.9 years** at 2,000/day, **~11 months** at 20,000/day.

**Pace:** Hands L9 inside a year of adventuring/utility is normal. Each evolve is a long wall; L9 inside a decade is the chapter of mastering that band. Evolves always upgrade.

**Roland (Ch 13+):** **Mana Hands L9** (≥500k). Next wall: Hand bar to **2M** → **Mana Mind** (up to ~1.5M left ≈ ~2.1 years scribe / ~2.5 months heavy). Drawing / Multitasking / Scribing still improve ink on top of the Hand-decade floor.

**Ch 23 passive always-on (tip-sip hold):** ~**290 kg** clothed total across concurrent Hands; still/skin ~**370–390 kg**; Multitasking **L7** → **7** Hands. Full note: `../../Story/Notes/Capabilities/ManaHandsPassive.md`.

## Ink craft: two methods (soft lock)

Both assume Roland ~**10×** mind (`../World/Science/Body/FocusCapacity.md`), Hands **L9**, Calligraphy / Drawing already past street mm work. Several-millimeter lines are not a Mind-evolve gate. Quill baseline: `../World/Science/Invent/WritingTools.md`.

### Growth pattern (from his tests)

Story clocks, not ordinary-human Drawing years:

| Beat | Speed |
|---|---|
| Ch 15 Detonation | Diagnosis + Calligraphy → **[Highest]** schematic in **~1 hour** first redraw |
| Ch 16 Runic Mana Scribe trial | Book in **minutes**; first Fire Orb scroll fails (half glass); **Mana Hand overlay/press try same sitting** (cascades ~¼ MP, Pollock mess); second quill pass **succeeds before last sand** |
| Ch 18 Impact | Overlay copy during Sahildr’s **~30 min** nap → **[Highest]** + Drawing L1 |
| Ch 19 Fire Orb schematic | Memory redraw **over 1 hour** → **[High]** (first assembly from memory, **not** diagram complexity); thin-sheet same session → **[Highest]** |
| Ch 21 first word / practice Fire Orb | Bolt word scroll in **a few minutes**; practice runic Orb same night |

Pattern: **first attempt messy / slow, second attempt same sitting works** when the image and skills are already there. Lowest lesser runes are simple marks; long first draws are **learning and putting unseen pieces together**, not inherent complexity. Class card **learning-ease while scribing** speeds clean schematics. Hands ink methods follow that curve, not NormalPersonSkills year columns.

### 1. Pen mode

One Hand (or tip) is the **pen**: hold / shape a bead of ink and **draw** the path on hide another Hand keeps taut (third Hand can feed ink). Continuous stroke. Same eye–effector loop as quill, new actuator.

| Milestone | Clock once he drills it |
|---|---|
| First ugly working Lesser | **Same day** (often attempt 2, trial-shaped) |
| Maintain several-mm lines on purpose | **~a few days to ~1 week** of real use |
| Clean batch / High seating by pen | **~2–4 weeks** as the daily method |

Bottleneck: path stability over the whole inscription time. Multitasking split across tip + hide (+ reservoir).

### 2. Press mode (printing / linoleum feel)

Hands build or hold a **relief matrix** (ink shaped as the rune, or a soft plate inked like lino), then **press** onto hide in one contact. Ch 16 already tried the cousin move (mana overlay laid on skin) and failed on **feed control** (cascade), not on the idea.

| Milestone | Clock once he drills it |
|---|---|
| First ugly transfer that seats | **Same day to a few days** (matrix + no-cascade pour) |
| Clean several-mm prints on purpose | **~a few days to ~1 week** |
| Repeat copies from one matrix | **seconds per press** after the matrix is good; re-ink between pulls |

Bottleneck: controlled transfer without the trial cascade, and flat press without smear. Once the matrix exists, throughput beats pen. Bad matrix reprints the same error forever until remade.

### Which when

| Job | Prefer |
|---|---|
| One-off schematic, Highest fiddly paths, learning a new sample | **Pen** |
| Same Common scroll many times, comet batches, street ammo | **Press** |
| Fine sub-mm / dense Greater boards later | Pen or press at **Mind+**; not required for several-mm Lessers / Commons |

Press does **not** skip Rune Scribing / quality seating. It only changes how ink meets hide.
