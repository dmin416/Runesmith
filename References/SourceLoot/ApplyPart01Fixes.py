from pathlib import Path

ROOT = Path(r"c:\Users\Admin\Desktop\Main\Runesmith\References\Source")

fixes = {
    "11-20.md": [
        (
            "'So I need to kill two goblins to even have enough for a single meal... guess life doesn't count for much here. I should have asked that guild attendant about how much I can get for a goblin mana stone...I'll ask her after I get this job done.'",
            "'So I need to kill one goblin just to cover a meal like that... guess life doesn't count for much here. I should have asked that guild attendant about how much I can get for a goblin mana stone... I'll ask her after I get this job done.'",
        ),
        (
            "it was two small silvers for a night, and five large copper coins extra if he wanted breakfast to go with that.",
            "it was one small silver for a night, and five large copper coins extra if he wanted breakfast to go with that.",
        ),
        (
            "This was the price of more than a monthly income of a whole commoner household. Most people were only able to earn one small gold coin per month.",
            "This was the price of about five months of a commoner household. Most commoner households only brought in about four large silver coins per month.",
        ),
    ],
    "61-70.md": [
        (
            "\u201c1 wee gold coin' fer a one way trip, grub will cost extra. Ye'll 'ave t' sleep wit' th' other lads below deck\u2026 Or ye can come t' me cabin instead.\u201d",
            "\u201c5 large silver coins fer a one way trip, grub will cost extra. Ye'll 'ave t' sleep wit' th' other lads below deck\u2026 Or ye can come t' me cabin instead.\u201d",
        ),
    ],
    "71-80.md": [
        (
            "The price reflected that it was well over a hundred small gold coins.",
            "The price reflected that. It was well over thirty small gold coins.",
        ),
        (
            "Thanks to this small piece of paper and over 100 small gold coins he was now the proud owner of a run-down farm.",
            "Thanks to this small piece of paper and over 30 small gold coins he was now the proud owner of a run-down farm.",
        ),
        (
            "gathering up a hundred small gold coins would be something that would take years.",
            "gathering up thirty small gold coins would be something that would take years.",
        ),
    ],
}

for name, reps in fixes.items():
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    orig = text
    for old, new in reps:
        if old in text:
            text = text.replace(old, new)
            print(f"HIT {name}: {old[:60]}")
        else:
            print(f"MISS {name}: {old[:80]!r}")
    if text != orig:
        path.write_text(text, encoding="utf-8")
        print(f"wrote {name}")
