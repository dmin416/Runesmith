# Sustenance Leveling Meters

> **Ideas / design loot.** Family trees, damage map, multi-mechanism math, and worked examples live in `ResistanceImmunitySystem.md` (Thermal / Kinetic / Bodily / **Sustenance**). This file only keeps **leveling meters** for Suffocation (and fused Sustenance) so breath and blood do not share one false clock.
>
> Live hubs win: `SkillsDesign.md`, `SkillRanks.md`, Breath Control, Sleep Resistance.

Retired names from older drafts: **Undying Body**, **Survival** family, **Starvation** (split into **Thirst** + **Hunger**), **Pure Blood**, **Iron Will**. Use **Sustenance Immunity** and **Bodily Immunity**.

---

## Sustenance tree (pointer)

```
Sleep Resistance       → Sleep Immunity (L9) ──────┐
Thirst Resistance      → Thirst Immunity (L9) ─────┤
Hunger Resistance      → Hunger Immunity (L9) ─────┼─→ Sustenance Immunity
Suffocation Resistance → Suffocation Immunity (L9) ┘
```

Fuse when **all four** Immunities are at Lv9 (`ResistanceImmunitySystem.md`).

---

## Clean-use units (flat `SkillRanks.md`)

| Deprivation | Unit | Notes |
|---|---|---|
| **Breath / hypoxia** (airway, ambient O₂, circulatory stop without bleed) | **15 s** under load = 1 use | 1 min held = **4** uses. Live Breath Control still uses **1 min = 1 use** until promote. |
| **Blood loss** (volume leaves the body) | **1% of full blood volume** lost and survived = 1 use | Fractions count. Adult ~5 L → **~50 mL ≈ 1% ≈ 1 use**. |
| **Sleep debt** | **15 s** awake past remaining need = 1 use | Banks Sleep until fused; then Sustenance. |
| **Thirst / Hunger** | Still open (day / meal / hour under deficit) | Lock when a chapter needs it. |

**Do not double-count** the same hemorrhage as both volume % and hypoxic seconds. Blood choke with no external loss = **time**. Open bleeding = **volume**.

Stay under **survivable blood loss** for the current M, or the session kills instead of ranking. Recovery / potions refill the tank; refill is not a use.

---

## Pace (projected)

**Breath / hypoxia (15 s = 1 use)**

| Pace | Time / day | Uses / day | → Res L5 | → Res L9 | → Imm L9 (~2.5M) |
|---|---:|---:|---|---|---|
| Ch 19 grill intensity | ~140 min | ~560 | ~2 days | ~2.4 yr | ~12 yr |
| Hard daily drill | 60 min | 240 | ~4 days | ~5.7 yr | ~28 yr |
| Field / mixed life | 15 min | 60 | ~17 days | ~23 yr | ~114 yr |

**Blood volume only (1% = 1 use)**

| Pace | Volume / day | Uses / day | → Res L5 | → Res L9 |
|---|---:|---:|---|---|
| Soft drains | ~1% | ~1 | ~3 yr | career+ |
| Hard Recovery grind | ~5% | ~5 | ~200 days | ~274 yr |

Breath is the practical Suffocation climb. Blood is Recovery-gated and slower.

---

## Cross-links

- Full system: `ResistanceImmunitySystem.md`
- Damage taxonomy: `DamageTypeResistances.md`
- Live Breath Control / Sleep: `SkillsDesign.md`
