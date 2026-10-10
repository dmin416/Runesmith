# Skill Level Cost Multiplier

> **Design dial / rewrite lock.** Default field-use curve: `SkillRanks.md`. Ordinary clocks: `NormalPersonSkills.md`. Do not rewrite locked early chapter ranks unless a beat forces it.

## Rule

**If leveling already takes a long time under the normal cum-use table, keep it as is.**

**If a skill would otherwise climb absurdly fast** (spamable every few seconds, soft clicks, tiny pulses, trivial exposures), you **may** multiply the uses / skill-exp needed to gain the next rank by:

- **current skill level**, and / or
- **evolution tier** (Basic / plain / Expert / …)

So short skills get a brake. Long skills stay on the flat `SkillRanks.md` ladder.

## Default stays flat

Live default for most skills:

| Reach | Cum clean uses |
|---|---:|
| L1 … L9 | **1 / 10 / 50 / 200 / 1,000 / 5,000 / 20,000 / 100,000 / 500,000** |
| Evolve | **2,000,000** |

No level multiplier. No tier multiplier. Chapters already locked on this table keep it.

## When to turn the dial on

Use a multiplier only when **raw counting would break the story**:

- Soft mana clicks / Sound Production pulses every few seconds
- Tiny Absorption refill ticks that fire constantly
- Trivial Heat dumps into a cook pot
- Any skill where “clean use” is nearly free and continuous

Do **not** apply it by default to:

- Combat spells with real chant / MP cost
- Sword / Dodging / field technique (~40% clean)
- Resistance exposures that cost real flesh and Recovery
- Breath Control (already gated by held minutes)

Those already take long enough.

## Suggested shapes (pick per skill when needed)

Not a second global law. Choose one when a skill is marked “short climb” in its blurb.

| Dial | Effect | Feel |
|---|---|---|
| **× level** | Next rank needs `base_step × current_level` clean uses (or skill-exp) | Higher ranks dig in harder on spam skills |
| **× evolution tier** | Basic **×1**, plain **×2**, Expert **×3**, … on the whole step or whole cum bar | Evolved forms stay rare |
| **× level × tier** | Both | Only for the most spamable tracks |

**Base_step** = the “from the rank before” column in `SkillRanks.md` (×10, ×5, ×4, …), or an equivalent skill-exp chunk if a skill uses exp instead of uses.

Example (illustrative only): a spam skill at **L5** with **× level** might need **5×** the normal L5→L6 step (**5,000 → 25,000** clean) before L6. Tier **×2** on plain form would double that again if both dials are on.

## Skill-exp wording

Some notes say “exp needed to level up skills.” For this dial, treat **skill-exp** and **clean uses** as the same budget unless a skill’s blurb defines a separate exp currency. Class / kill XP (`Progression.md`) stays separate and is **not** multiplied by this dial.

## Story feel

- Long climbs (sword, resists, real casts): reader feels time and cost. Leave flat.
- Short climbs: without a brake, Roland hits L9 in a week of idle spam. Turn on level / tier multipliers so evolution still means something.

Mark the chosen dial on the skill’s `SkillsDesign.md` row (or chapter note) when first used. Do not silently retcon already printed ranks.
