import json
from collections import defaultdict
from pathlib import Path

root = Path(r"c:\Users\Admin\Desktop\Main\Runesmith")
rows = json.loads((root / "References/SourceLoot/PriceInventoryMechanical.json").read_text(encoding="utf-8"))


def classify(r):
    s = r["snippet"].lower()
    prices = ", ".join(r["prices"])
    if "7 large copper" in s and ("meal" in s or "porridge" in s or "whole thing cost" in s):
        return "Inn meal", "7 large copper", "5 large copper coins", "REPLACE"
    if "4 small silver" in s and "stone" in s:
        return "Rice/tiny mana stone", "4 small silver each", "2 small silver coins each", "REPLACE"
    if "mana arrow" in s and ("one small silver" in s or "1 small silver" in s) and "went for" in s:
        return "Mana Arrow shop", "1 SS", "3 small silver coins", "REPLACE"
    if "fire arrow" in s and "three small silver" in s and "tier 2" in s:
        return "Fire Arrow shop dialogue", "3 SS", "6 small silvers", "REPLACE"
    if "fireball" in s and "six small silver" in s:
        return "Fireball shop talk", "~6 SS", "one large silver", "REPLACE"
    if "blank" in s and "9 small silver" in s:
        return "Blank pack x10", "9 SS", "5 SS pack + ink beat", "REPLACE"
    if "2 to 4 small silver" in s and "fire arrow" in s:
        return "Word Fire Arrow appraiser", "2-4 SS", "about 6 small silver coins", "REPLACE"
    if "up to 9 small silver" in s and "scroll" in s:
        return "Runic Fire Arrow High", "~9 SS", "up to 10 small silver coins", "REPLACE"
    if "six or seven times" in s:
        return "Dusty runic multiple", "6-7x", "about three times", "REPLACE"
    if "5%" in s and "month" in s and ("save" in s or "discount" in s or "lodging" in s):
        return "Monthly lodging discount", "5%", "10%", "REPLACE"
    return "(unclassified coin mention)", prices, "KEEP (no lock)", "KEEP"


lines = [
    "# Source Price Inventory (Mechanical + Rules)",
    "",
    "Coin-phrase pre-pass. Subagent Part01-07 merge into `PriceInventory.md`.",
    "",
    "| SourceFile | Line | ApproxChapter | Item | OldPrice | ApprovedPrice | Action |",
    "|---|---:|---|---|---|---|---|",
]
actions = defaultdict(int)
for r in rows:
    item, old, approved, action = classify(r)
    actions[action] += 1
    snip = r["snippet"].replace("|", "/")
    ch = r["ch"] or "?"
    lines.append(
        f"| {r['file']} | {r['line']} | {ch} | {item} | {old} | {approved} | {action} |"
    )

lines.append("")
lines.append(f"Total mechanical rows: {len(rows)}. Actions: {dict(actions)}")
path = root / "References/SourceLoot/PriceInventoryMechanical.md"
path.write_text("\n".join(lines), encoding="utf-8")
print("wrote", path, "rows", len(rows), dict(actions))
