"""Apply approved Source reprice rules across all Source range files."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"c:\Users\Admin\Desktop\Main\Runesmith\References\Source")

# (compiled or str pattern, replacement, flags). Longer / more specific first.
# Use both ASCII and curly apostrophe variants where needed.
APOST = "['\u2019]"

REPLACEMENTS: list[tuple[str, str]] = [
    # Meal
    (
        r"The whole thing cost him 7 large copper coins",
        "The whole thing cost him 5 large copper coins",
    ),
    # Rice stone early
    (
        r"went for 4 small silver coins each",
        "went for 2 small silver coins each",
    ),
    (
        r"went for four small silver coins each",
        "went for 2 small silver coins each",
    ),
    # Mana Arrow shelf
    (
        r"went for one small silver coin",
        "went for three small silver coins",
    ),
    (
        r"went for 1 small silver coin",
        "went for three small silver coins",
    ),
    # Fire Arrow shop Q
    (
        rf"only cost three small silvers when it{APOST}s a tier 2 spell while this mana arrow spell costs 1 small silver",
        "only cost six small silvers when it's a tier 2 spell while this mana arrow spell costs three small silvers",
    ),
    (
        rf"only cost three small silvers when it{APOST}s a tier 2 spell while this Mana Arrow spell costs 1 small silver",
        "only cost six small silvers when it's a tier 2 spell while this Mana Arrow spell costs three small silvers",
    ),
    # Fireball
    (
        r"fireball spell it would cost about six small silver",
        "fireball spell it would cost about one large silver",
    ),
    (
        r"Fireball spell it would cost about six small silver",
        "Fireball spell it would cost about one large silver",
    ),
    # Blank pack + margin beat (ASCII apostrophe version)
    (
        rf"The ten blank scrolls cost him 9 small silver, which put them at 9 large copper coins apiece\. So if he managed to sell them all at the price of the mana arrow spell in this shop he would only be making one small silver coin\. He probably wouldn{APOST}t be making any money if he added the price of the magic ink into the mix\.",
        "The ten blank scrolls cost him 5 small silver, which put them at 5 large copper coins apiece. Ink for ten Mana Arrows would run about another 10 small silver. Sold at the shop's Intermediate price of three small silver each that left some coin for labor, but without a store contract he would eat auction cuts and cartel blank prices. Lowest and Low grades barely paid a scribe's day. He probably would not clear real wages going solo on regulars.",
    ),
    # Triple -> twice for 6 vs 3
    (
        r"The cost of this spell was triple what the inferior one cost\.",
        "The cost of this spell was about twice what the inferior one cost.",
    ),
    # Regular compare
    (
        r"regular fire arrow spell scroll that went for 3 small silver coins",
        "regular Fire Arrow spell scroll that went for 6 small silver coins",
    ),
    (
        r"A regular intermediate fire arrow spell went for 2 to 4 small silver coins",
        "A regular Intermediate Fire Arrow spell went for about 6 small silver coins",
    ),
    (
        r"A regular Intermediate Fire Arrow spell went for 2 to 4 small silver coins",
        "A regular Intermediate Fire Arrow spell went for about 6 small silver coins",
    ),
    # Appraiser High
    (
        r"up to 9 small silver coins, not bad",
        "up to 10 small silver coins, not bad",
    ),
    (
        rf"If the [\"'\u2018\u2019]high[\"'\u2018\u2019] rated scroll could go for up to 9 small silver coins then this one could even go for double, maybe even triple\.",
        "If the High rated scroll could go for up to 10 small silver coins then this one could sit around 12 to 15 small silver.",
    ),
    # Multiple
    (
        r"costs six or seven times as much",
        "costs about three times as much",
    ),
    # Monthly lodging 5% -> 10%
    (
        r"monthly fee that would save him about 5%",
        "monthly fee that would save him about 10%",
    ),
    (
        r"pay a monthly fee that would save him about 5%",
        "pay a monthly fee that would save him about 10%",
    ),
    (
        r"save him about 5%",
        "save him about 10%",
    ),
]


def main() -> None:
    files_changed = 0
    total_hits = 0
    log: list[str] = []
    for path in sorted(ROOT.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        text = path.read_text(encoding="utf-8")
        orig = text
        file_hits = 0
        for pattern, repl in REPLACEMENTS:
            text, n = re.subn(pattern, repl, text, flags=re.IGNORECASE)
            file_hits += n
        if text != orig:
            path.write_text(text, encoding="utf-8")
            files_changed += 1
            total_hits += file_hits
            log.append(f"{path.name}: {file_hits}")
    print(f"files_changed={files_changed} total_hits={total_hits}")
    for line in log:
        print(line)


if __name__ == "__main__":
    main()
