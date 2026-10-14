# Terran year (365 days) desk ledger — Roland + Ned.
# Rules: SkillRanks.md · Attributes.md · ManaHands.md · MagicScrollMaking.md · Chapter21_5.md § Seat time
# Regen: python _gen_day_skill_year.py
from __future__ import annotations

from pathlib import Path

THRESH = [0, 1, 10, 50, 200, 1000, 5000, 20000, 100000, 500000, 2000000]
Q_MULT = {"Lowest": 1, "Low": 2, "Intermediate": 4, "High": 8, "Highest": 16}
ETA = {"Lowest": 0.20, "Low": 0.40, "Intermediate": 0.60, "High": 0.80, "Highest": 1.00}

TIP_SIP = 21.1  # MP/min clothed ~99%
DRAW_ARROW = 5.0  # min fluent
DRAW_BALL = 15.0
DESK_MIN = 600.0  # 10 h tip-sip capable
MA_SHARE, FB_SHARE, LB_SHARE = 0.70, 0.25, 0.05
HANDS_PER_SEAT = 6.0  # ManaHands.md: ~30g × 120s × 0.05 cm² → 6 uses / Hand / scroll

# Enter Ch 21.5 (Ch 19 train exit sheet)
ENTER_ATTR = {
    "Str": 49,
    "Agi": 64,
    "Dex": 72,
    "Vit": 72,
    "End": 81,
    "Int": 156,
    "Will": 147,
    "Cha": 12,
    "Luck": 7,
}

# Skill → attribute pads (+1 per level to each listed)
SKILL_ATTR = {
    "SleepRes": ("Vit", "End"),
    "HungerRes": ("Vit", "End"),
    "PainRes": ("Will", "End"),
    "PoisonRes": ("Vit", "End"),
    "HeatRes": ("Vit", "End"),
    "ColdRes": ("Vit", "End"),
    "Recovery": ("Vit", "End"),
    "Multitasking": ("Int", "Dex"),
    "Diagnosis": ("Int",),
    "Drawing": ("Dex",),
    "Technology": ("Dex", "Int"),
    # Shaping Int+2/Will+1 etc. already baked at enter ranks — only new levels pad
    "ManaShaping": ("Int", "Int", "Will"),  # +2 Int +1 Will per level → count Int twice
    "ManaRegulation": ("Int", "Will", "Will"),
}

SKIP_EXIT = 120  # 4 months; narrative skill floor for “make what he wants”


def level_from_cum(c: float) -> int:
    c = max(0.0, c)
    for L in range(9, 0, -1):
        if c >= THRESH[L]:
            return L
    return 0


def progress_in_rank(c: float) -> str:
    L = level_from_cum(c)
    if L >= 9:
        return f"L9→evo {(c - THRESH[9]) / (THRESH[10] - THRESH[9]) * 100:.1f}%"
    if L == 0:
        return "pre-L1"
    return f"L{L}→L{L+1} {(c - THRESH[L]) / (THRESH[L + 1] - THRESH[L]) * 100:.1f}%"


def resources(a: dict) -> tuple[int, int, int]:
    hp = a["Vit"] * 10 + a["End"] * 3
    sp = a["End"] * 10 + a["Str"] * 3 + a["Agi"] * 3
    mp = a["Int"] * 10 + a["Will"] * 4
    return hp, sp, mp


def phase_quality_mix(phase: str) -> dict:
    # After trial / first-night (2–3 tries): working seats always. Only quality rank moves.
    if phase == "A":
        return {"Lowest": 0.05, "Low": 0.35, "Intermediate": 0.45, "High": 0.15, "Highest": 0.0}
    if phase == "B":
        # Quality climb toward first Highest each + early stock
        return {"Lowest": 0.0, "Low": 0.10, "Intermediate": 0.30, "High": 0.45, "Highest": 0.15}
    if phase == "C":
        # keep/sell: mostly Highest (4-month exit still hits RS L8)
        return {"Lowest": 0.0, "Low": 0.0, "Intermediate": 0.05, "High": 0.25, "Highest": 0.70}
    return {"Lowest": 0.0, "Low": 0.0, "Intermediate": 0.0, "High": 0.25, "Highest": 0.75}


def avg_q(mix: dict) -> float:
    return sum(mix[k] * Q_MULT[k] for k in mix)


def s_factor(rs_L: int) -> float:
    return max(0.1, 1.0 - 0.1 * max(0, rs_L))


def expected_pay_wall(cast: float, draw: float, S: float, mix: dict) -> tuple[float, float]:
    """Mean pay MP and wall minutes for one seat under quality mix."""
    pay = wall = 0.0
    for q, share in mix.items():
        if share <= 0:
            continue
        p = (cast / ETA[q]) * S
        w = draw + p / TIP_SIP
        pay += share * p
        wall += share * w
    return pay, wall


def seat_time_day(rs_L: int, mix: dict) -> dict:
    S = s_factor(rs_L)
    pay_ma, wall_ma = expected_pay_wall(50.0, DRAW_ARROW, S, mix)
    pay_ball, wall_ball = expected_pay_wall(400.0, DRAW_BALL, S, mix)
    ma = (DESK_MIN * MA_SHARE) / wall_ma
    fb = (DESK_MIN * FB_SHARE) / wall_ball
    lb = (DESK_MIN * LB_SHARE) / wall_ball
    seats = ma + fb + lb
    mp = ma * pay_ma + fb * pay_ball + lb * pay_ball
    return {
        "ma": ma,
        "fb": fb,
        "lb": lb,
        "seats": seats,
        "mp": mp,
        "wall_ma": wall_ma,
        "wall_ball": wall_ball,
        "pay_ma": pay_ma,
        "pay_ball": pay_ball,
        "S": S,
    }


def apply_uses(cum: dict, daily: dict) -> dict[str, int]:
    """Apply uses; return {skill: levels_gained}."""
    gained: dict[str, int] = {}
    for k, u in daily.items():
        before = level_from_cum(cum.get(k, 0.0))
        if cum.get(k, 0) == 0 and u > 0:
            cum[k] = 1.0
            u = max(0.0, u - 1.0)
        cum[k] = cum.get(k, 0.0) + u
        after = level_from_cum(cum[k])
        if after > before:
            gained[k] = after - before
    return gained


def apply_attr_pads(attr: dict, gained: dict[str, int]) -> None:
    for skill, n in gained.items():
        pads = SKILL_ATTR.get(skill)
        if not pads:
            continue
        for _ in range(n):
            for a in pads:
                attr[a] += 1


roland_enter_cum = {
    "RuneScribing": 1.0,
    "Drawing": 1.0,
    "Understanding": 1.0,
    "Multitasking": 1000.0,  # L5
    "ManaHands": 500000.0,  # L9
    "ManaShaping": 20000.0,  # L7
    "ManaRegulation": 100000.0,  # L8
    "ManaScribing": 1.0,
    "RuneMastery": 1.0,
    "SleepRes": 5000.0,  # L6
    "HungerRes": 0.0,
    "PainRes": 1000.0,  # L5
    "HeatRes": 1000.0,
    "ColdRes": 1000.0,
    "SharpRes": 200.0,  # L4
    "BluntRes": 0.0,
    "PoisonRes": 5000.0,  # L6
    "SuffocationRes": 1000.0,
    "Recovery": 1000.0,  # L5 — Roland; Ned has his own Recovery night pack
    "ManaAbsorption": 500000.0,
    "ManaReinforcement": 500000.0,
    "Diagnosis": 200.0,  # L4
    "HeatSpell": 5000.0,  # L6
    "Technology": 20000.0,  # L7 — every rune/tech observe this skip
}

# Every night since tame (Ch 12 → 21.5 enter), soft ~200 nights, every skill Ned can.
# Night band (camp/inn): moon ~15, tail/horn ~12, blunt/sharp ~10, spike ~25, silk ~15,
# climb ~15, spring ~6 (reload), seal ~12, poison ~8 soft, pain ~20, heat/cold ~12,
# camo always-on (~60–80/day), formation ~10, absorb ~10, acid prod ~8, acid spray ~6,
# Ned Recovery ~15 (blood meal / tip cycle restore; distinct from Seal wound-knit).
ned_enter_cum = {
    "Ned_SpikeThrowing": 45000.0,  # L7 deep
    "Ned_Silk": 5500.0,  # L6
    "Ned_Stealth": 120000.0,  # L8 — always-on camo
    "Ned_Climbing": 40000.0,  # L7
    "Ned_SpringCharge": 6500.0,  # L6
    "Ned_Seal": 5500.0,  # L6 — wound seal / regeneration
    "Ned_Recovery": 5500.0,  # L6 — body restore from blood meals / tip cycle
    "Ned_PoisonRes": 3500.0,  # L5
    "Ned_PainRes": 6000.0,  # L6
    "Ned_HeatRes": 5500.0,  # L6
    "Ned_ColdRes": 5500.0,  # L6
    "Ned_BluntRes": 5500.0,  # L6
    "Ned_SharpRes": 5500.0,  # L6
    "Ned_TailBash": 5500.0,  # L6
    "Ned_HornPierce": 5500.0,  # L6
    "Ned_MoonCurl": 6000.0,  # L6
    "Ned_NeedleFormation": 2500.0,  # L5 — tip bed regrow after harvest
    "Ned_NeedleAbsorb": 2500.0,  # L5 — swallow tips / foreign needles
    "Ned_AcidProduction": 2000.0,  # L5 — gland fill from spike feedstock
    "Ned_AcidSpray": 1600.0,  # L5 — aimed board spit (no face/eyes)
}

roland_cum = dict(roland_enter_cum)
ned_cum = dict(ned_enter_cum)
attr = dict(ENTER_ATTR)
rows = []
overall_xp = 7329.0
schematic_left = 27000.0
pour_xp_total = 0.0
# Soft class: notes “a few levels” this skip — bank XP, grant at most +3 Scribe L by skip exit
scribe_L = 1
scribe_attr_budget = 3

for day in range(1, 366):
    rs_L = level_from_cum(roland_cum["RuneScribing"])
    mt_L = level_from_cum(roland_cum["Multitasking"])
    concurrent_hands = max(2, mt_L)
    hp, sp, mp_pool = resources(attr)

    if day <= 14:
        phase = "A"
        mix = phase_quality_mix(phase)
        q_avg = avg_q(mix)
        # Discovery volume; clean always (trial/first-night already taught seating)
        raw = 8.0 + day * 0.35
        clean_rate = 1.0
        seats = raw
        ma = fb = lb = 0.0
        S = s_factor(max(1, rs_L))
        # Orb/Bolt cast 25; mean η from Low/Int mix ~0.55
        mp_paid = seats * (25 / 0.55) * S
        wall_ma = wall_ball = 0.0
        cast_for_xp = 25.0
    elif day <= 35:
        phase = "B"
        mix = phase_quality_mix(phase)
        q_avg = avg_q(mix)
        # Quality climb + early Arrow/Ball stock; never fails — only rank
        st = seat_time_day(rs_L, mix)
        ma, fb, lb = st["ma"], st["fb"], st["lb"]
        seats = st["seats"]
        raw = seats
        clean_rate = 1.0
        mp_paid = st["mp"]
        wall_ma, wall_ball = st["wall_ma"], st["wall_ball"]
        cast_for_xp = MA_SHARE * 50 + FB_SHARE * 400 + LB_SHARE * 400
        S = st["S"]
    else:
        phase = "C" if day <= SKIP_EXIT else "D"
        mix = phase_quality_mix(phase)
        q_avg = avg_q(mix)
        st = seat_time_day(rs_L, mix)
        ma, fb, lb = st["ma"], st["fb"], st["lb"]
        seats = st["seats"]
        raw = seats
        clean_rate = 1.0
        mp_paid = st["mp"]
        wall_ma, wall_ball = st["wall_ma"], st["wall_ball"]
        cast_for_xp = MA_SHARE * 50 + FB_SHARE * 400 + LB_SHARE * 400
        S = st["S"]

    # --- Roland daily uses (rules) ---
    rs_uses = seats * q_avg
    drawing_uses = rs_uses
    understanding = (1.0 if day <= 25 else (0.12 if day <= 90 else 0.04)) * min(4.0, q_avg)
    mt_uses = seats * (1.2 + 0.25 * concurrent_hands)  # attention split, no quality×
    # Hands: 6 uses/Hand/finished seat × concurrent Hands (no quality×)
    hands_uses = seats * HANDS_PER_SEAT * concurrent_hands
    shaping = seats * 1.0  # linear
    regulation = 60.0 + seats * 0.15  # tip-sip pulses, linear
    absorb = regulation * 0.85
    reinf = regulation * 0.45
    mana_scribing = 0.15 if day % 17 == 0 else 0.0
    rune_mastery = 0.05
    # Technology: every observe of runes + desk tech (ink, press, tools, pathways)
    technology = seats * q_avg + 12.0

    # Sleep: T0=8h, sleep ~4h; soft-repeat so exit ~L7 @ skip (printed +1)
    sleep_L = level_from_cum(roland_cum["SleepRes"])
    need_h = 8.0 * (1.0 - 0.10 * sleep_L)
    sleep_h = 4.0
    ignored_h = max(0.0, 8.0 - sleep_h)
    raw_sleep = (ignored_h * 3600.0) / 15.0
    # soft-repeat after first ~2 h ignored same day
    dense = min(ignored_h, 2.0) * 240.0
    thin = max(0.0, ignored_h - 2.0) * 240.0 * 0.12
    sleep_uses = dense + thin
    # hard soft toward printed L7 through skip; after exit allow slow climb
    if day <= SKIP_EXIT and roland_cum["SleepRes"] + sleep_uses > 20000:
        sleep_uses = max(0.0, 20000 - roland_cum["SleepRes"])

    # Hunger: one-meal band ~70–85; zero-food every 11th day = 100
    hunger = 100.0 if day % 11 == 0 else (72.0 if day <= 3 else 78.0)
    # Pain: patch + starve-ache → L6 by 4-month exit (clears 5k)
    pain = 36.0 if day > 7 else 22.0
    heat = 18.0 + min(6.0, day * 0.015)
    cold = 16.0 + min(6.0, day * 0.015)
    jab = 5.0 if day > 30 else 4.0
    sharp = jab
    blunt = jab * 0.9
    poison = jab * 0.7
    suff = 1.2 if day % 2 == 0 else 0.7
    recovery = 2.0 + (1.0 if day % 5 == 0 else 0.0)
    diagnosis = seats * 0.85 * q_avg
    heat_spell = 1.0 if day % 3 == 0 else 0.4

    roland_daily = {
        "RuneScribing": rs_uses,
        "Drawing": drawing_uses,
        "Understanding": understanding,
        "Multitasking": mt_uses,
        "ManaHands": hands_uses,
        "ManaShaping": shaping,
        "ManaRegulation": regulation,
        "ManaScribing": mana_scribing,
        "RuneMastery": rune_mastery,
        "SleepRes": sleep_uses,
        "HungerRes": hunger,
        "PainRes": pain,
        "HeatRes": heat,
        "ColdRes": cold,
        "SharpRes": sharp,
        "BluntRes": blunt,
        "PoisonRes": poison,
        "SuffocationRes": suff,
        "Recovery": recovery,
        "ManaAbsorption": absorb,
        "ManaReinforcement": reinf,
        "Diagnosis": diagnosis,
        "HeatSpell": heat_spell,
        "Technology": technology,
    }

    # Ned
    moon = 25.0 + day * 0.04
    clash = (20.0 + min(12.0, day * 0.025)) * 0.55
    ned_jabs = (8.0 + (2.0 if day > 30 else 0.0)) * 0.5
    silk = 12.0 + min(8.0, day * 0.02)
    ned_daily = {
        "Ned_MoonCurl": moon,
        "Ned_TailBash": clash,
        "Ned_HornPierce": clash,
        "Ned_BluntRes": clash * 0.9,
        "Ned_SharpRes": clash * 0.9,
        "Ned_SpikeThrowing": ned_jabs + clash * 0.25,
        "Ned_Silk": silk,
        # Camouflage always-on (scarf + room); soft-repeat still pays a dense day band
        "Ned_Stealth": 72.0,
        "Ned_Climbing": 6.0,
        "Ned_SpringCharge": 2.0,
        "Ned_Seal": clash * 0.4 + ned_jabs * 0.2 + 2.0,
        "Ned_Recovery": 12.0 + min(4.0, day * 0.02),  # blood meal + tip-cycle restore
        "Ned_PoisonRes": 3.0 + (1.0 if day % 3 == 0 else 0.0),
        "Ned_PainRes": clash * 0.8 + ned_jabs * 0.5 + moon * 0.15,
        "Ned_HeatRes": 10.0 + min(4.0, day * 0.01),
        "Ned_ColdRes": 8.0 + min(4.0, day * 0.01),
        "Ned_NeedleFormation": 8.0 + min(4.0, day * 0.01),
        "Ned_NeedleAbsorb": 8.0 + min(4.0, day * 0.01),
        "Ned_AcidProduction": 6.0 + min(3.0, day * 0.01),
        "Ned_AcidSpray": 5.0 + min(2.0, day * 0.01),
    }

    schem = 0.0
    if schematic_left > 0 and day <= 55:
        schem = min(schematic_left, 27000 / 40.0)
        schematic_left -= schem
    # Craft XP = cast × quality_mult (ignore S/η)
    pour = seats * cast_for_xp * q_avg
    pour_xp_total += pour
    overall_xp += schem + pour

    # Soft few Scribe levels from XP (Dex/Int/Will +1 each) — max +3 by skip exit
    if day <= SKIP_EXIT and scribe_attr_budget > 0 and overall_xp > 13000 * (scribe_L + 1):
        # very soft: only when bar would clearly clear another gate
        if overall_xp > 50000 * scribe_L:
            scribe_L += 1
            scribe_attr_budget -= 1
            attr["Dex"] += 1
            attr["Int"] += 1
            attr["Will"] += 1

    g_r = apply_uses(roland_cum, roland_daily)
    g_n = apply_uses(ned_cum, ned_daily)
    apply_attr_pads(attr, g_r)
    hp, sp, mp_pool = resources(attr)

    row = {
        "day": day,
        "phase": phase,
        "seats": round(seats, 2),
        "raw": round(raw, 2),
        "clean_rate": round(clean_rate, 3),
        "ma": round(ma, 2),
        "fb": round(fb, 2),
        "lb": round(lb, 2),
        "mp_paid": round(mp_paid, 1),
        "mp_pool": mp_pool,
        "hp": hp,
        "sp": sp,
        "q_avg": round(q_avg, 2),
        "S": round(S, 2),
        "wall_ma": round(wall_ma, 2),
        "wall_ball": round(wall_ball, 2),
        "hands_n": concurrent_hands,
        "mt_L": mt_L,
        "rs_L": level_from_cum(roland_cum["RuneScribing"]),
        "Int": attr["Int"],
        "Will": attr["Will"],
        "Vit": attr["Vit"],
        "End": attr["End"],
        "Dex": attr["Dex"],
        "overall_xp": int(overall_xp),
        "schem_xp": round(schem, 1),
        "pour_xp": round(pour, 1),
        "scribe_L": scribe_L,
    }
    for k, u in roland_daily.items():
        row[f"{k}_u"] = round(u, 2)
        row[f"{k}_c"] = round(roland_cum[k], 1)
        row[f"{k}_L"] = level_from_cum(roland_cum[k])
    for k, u in ned_daily.items():
        row[f"{k}_u"] = round(u, 2)
        row[f"{k}_c"] = round(ned_cum[k], 1)
        row[f"{k}_L"] = level_from_cum(ned_cum[k])
    rows.append(row)

# --- write CSV ---
out = Path(__file__).resolve().parent
csv_path = out / "Chapter21_5DaySkillYear.csv"
keys = list(rows[0].keys())
with csv_path.open("w", encoding="utf-8", newline="") as f:
    f.write(",".join(keys) + "\n")
    for r in rows:
        f.write(",".join(str(r[k]) for k in keys) + "\n")

rexit, r365 = rows[SKIP_EXIT - 1], rows[364]
d1 = rows[0]
hp0, sp0, mp0 = resources(ENTER_ATTR)
hpex, spex, mpex = rexit["hp"], rexit["sp"], rexit["mp_pool"]
hp365, sp365, mp365 = r365["hp"], r365["sp"], r365["mp_pool"]

# --- write MD ---
L: list[str] = []
L += [
    "# Chapter 21.5 — Terran Year Skill Ledger (365 Days)",
    "",
    "Full rewrite on locked mana / skill / attribute rules. **Every Terran day** scored. Story skip exit **~4 months / day 120**; days 121–365 are year-ledger only.",
    "",
    "| Source | Rule |",
    "|---|---|",
    "| `SkillRanks.md` | Cum clean uses; quality × **1/2/4/8/16** on graded seats; quality-only after seating is known |",
    "| `MagicScrollMaking.md` | `paid = (cast / η) × S`; S = **1 − 0.1 × RS_L**; craft XP = cast × quality (ignore S/η) |",
    "| `Chapter21_5.md` § Seat time | wall = draw + paid/tip-sip; tip-sip **21.1 MP/min**; Arrow draw **5 min**; Ball **15 min**; Phase C **70/25/5** MA/FB/LB |",
    "| `ManaHands.md` | **6** uses / Hand / finished seat; × concurrent Hands (= MT L, floor 2); **no** quality× |",
    "| `Attributes.md` | HP/SP/MP formulas; skill pads **+1 × level** on favored attrs |",
    "| Technology | Every rune + desk-tech observe; uses = seats × q_avg + **12**/day |",
    "",
    "CSV (all columns): `Chapter21_5DaySkillYear.csv`. Regen: `_gen_day_skill_year.py`.",
    "",
    "## Phases",
    "",
    "| Days | Phase | Desk |",
    "|---|---|---|",
    "| **1–14** | **A** | Discovery (Orb/Bolt heavy; quality only) |",
    "| **15–35** | **B** | Quality climb → first Highest each; early stock |",
    "| **36–120** | **C** | Seat-time keep/sell mix (skip exit ~d120) |",
    "| **121–365** | **D** | Same habit through year end (ledger only) |",
    "",
    "## Enter sheet (Ch 19 → 21.5)",
    "",
    f"| | Str | Agi | Dex | Vit | End | Int | Will | Cha | Luck | HP | SP | MP |",
    f"|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    f"| Enter | {ENTER_ATTR['Str']} | {ENTER_ATTR['Agi']} | {ENTER_ATTR['Dex']} | {ENTER_ATTR['Vit']} | {ENTER_ATTR['End']} | {ENTER_ATTR['Int']} | {ENTER_ATTR['Will']} | {ENTER_ATTR['Cha']} | {ENTER_ATTR['Luck']} | {hp0} | {sp0} | {mp0} |",
    f"| @120 | {ENTER_ATTR['Str']} | {ENTER_ATTR['Agi']} | {rexit['Dex']} | {rexit['Vit']} | {rexit['End']} | {rexit['Int']} | {rexit['Will']} | {ENTER_ATTR['Cha']} | {ENTER_ATTR['Luck']} | {hpex} | {spex} | {mpex} |",
    f"| @365 | {ENTER_ATTR['Str']} | {ENTER_ATTR['Agi']} | {r365['Dex']} | {r365['Vit']} | {r365['End']} | {r365['Int']} | {r365['Will']} | {ENTER_ATTR['Cha']} | {ENTER_ATTR['Luck']} | {hp365} | {sp365} | {mp365} |",
    "",
    f"MP spend math uses formula pool (**{mp0}** enter). Tip-sip ceiling **~12,650 MP / 10 h**.",
    "",
    "## Exit ranks",
    "",
    "### Roland @120 / @365",
    "",
    "| Skill | L@120 | Cum@120 | Progress@120 | L@365 | Cum@365 | Progress@365 |",
    "|---|---:|---:|---|---:|---:|---|",
]
for k in roland_enter_cum:
    L.append(
        f"| {k} | {rexit[f'{k}_L']} | {rexit[f'{k}_c']} | {progress_in_rank(rexit[f'{k}_c'])} | "
        f"{r365[f'{k}_L']} | {r365[f'{k}_c']} | {progress_in_rank(r365[f'{k}_c'])} |"
    )
L += [
    "",
    "### Ned @120 / @365",
    "",
    "| Skill | L@120 | Cum@120 | Progress@120 | L@365 | Cum@365 | Progress@365 |",
    "|---|---:|---:|---|---:|---:|---|",
]
for k in ned_enter_cum:
    L.append(
        f"| {k} | {rexit[f'{k}_L']} | {rexit[f'{k}_c']} | {progress_in_rank(rexit[f'{k}_c'])} | "
        f"{r365[f'{k}_L']} | {r365[f'{k}_c']} | {progress_in_rank(r365[f'{k}_c'])} |"
    )
L += [
    "",
    "## XP",
    "",
    f"- Enter bar **7329** → d120 **{rexit['overall_xp']}** → d365 **{r365['overall_xp']}**",
    f"- Pour XP year ≈ **{pour_xp_total:.0f}** (+ **27000** schematics)",
    f"- Soft Scribe levels (attr pads only): enter L1 → d120 **L{rexit['scribe_L']}** (capped +3)",
    "",
    "## Every Terran day (1–365)",
    "",
    "Seats / MA / FB / LB from wall = draw + (cast/η)×S / **21.1**. Hands = seats × **6** × concurrent Hands. Technology = seats × q_avg + **12**.",
    "",
]

MONTHS = [
    (1, 31, "Month 1 — d1–31"),
    (32, 61, "Month 2 — d32–61"),
    (62, 92, "Month 3 — d62–92"),
    (93, 122, "Month 4 — d93–122 (skip exit ~d120)"),
    (123, 153, "Month 5 — d123–153 (ledger only)"),
    (154, 183, "Month 6 — d154–183"),
    (184, 214, "Month 7 — d184–214"),
    (215, 244, "Month 8 — d215–244"),
    (245, 275, "Month 9 — d245–275"),
    (276, 305, "Month 10 — d276–305"),
    (306, 335, "Month 11 — d306–335"),
    (336, 365, "Month 12 — d336–365"),
]

for start, end, title in MONTHS:
    L += [
        f"### {title}",
        "",
        "| Day | Ph | Seats | MA | FB | LB | MP paid | Pool | Q× | S | RS L | RS cum | Hands u | Hands L | MT L | Sleep L | Hung L | Pain L | Tech L | Int | Will | Vit | End | XP day |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for d in range(start, end + 1):
        r = rows[d - 1]
        xp_day = int(r["schem_xp"] + r["pour_xp"])
        L.append(
            f"| {d} | {r['phase']} | {r['seats']} | {r['ma']} | {r['fb']} | {r['lb']} | {r['mp_paid']} | {r['mp_pool']} | "
            f"{r['q_avg']} | {r['S']} | {r['RuneScribing_L']} | {r['RuneScribing_c']} | {r['ManaHands_u']} | "
            f"{r['ManaHands_L']} | {r['Multitasking_L']} | {r['SleepRes_L']} | {r['HungerRes_L']} | {r['PainRes_L']} | "
            f"{r['Technology_L']} | {r['Int']} | {r['Will']} | {r['Vit']} | {r['End']} | {xp_day} |"
        )
    L.append("")

L += [
    "## Cross-links",
    "",
    "- `Chapter21_5.md` · `SkillRanks.md` · `Attributes.md` · `ManaHands.md` · `MagicScrollMaking.md` · `NedStatus.md` · `ResistanceGrindBurnFreeze.md`",
    "",
]

md_path = out / "Chapter21_5DaySkillYear.md"
md_path.write_text("\n".join(L) + "\n", encoding="utf-8")

print(f"Wrote {csv_path} ({len(rows)} days)")
print(f"Wrote {md_path}")
print(
    f"d120 seats={rexit['seats']} MA={rexit['ma']} FB={rexit['fb']} MP={rexit['mp_paid']} "
    f"q={rexit['q_avg']} S={rexit['S']}"
)
print(
    f"RS @120 L{rexit['RuneScribing_L']} cum={rexit['RuneScribing_c']} | "
    f"Tech L{rexit['Technology_L']} cum={rexit['Technology_c']} | "
    f"Sleep L{rexit['SleepRes_L']} Hung L{rexit['HungerRes_L']} Pain L{rexit['PainRes_L']}"
)
print(
    f"Hands @120 L{rexit['ManaHands_L']} cum={rexit['ManaHands_c']} | "
    f"attrs Vit/End/Dex/Int/Will @120 {rexit['Vit']}/{rexit['End']}/{rexit['Dex']}/{rexit['Int']}/{rexit['Will']} MP={rexit['mp_pool']}"
)
