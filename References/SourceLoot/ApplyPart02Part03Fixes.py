from pathlib import Path

ROOT = Path(r"c:\Users\Admin\Desktop\Main\Runesmith\References\Source")

fixes = {
    # Part02 lock conflicts (EconomyDesign superseded list)
    "141-150.md": [
        (
            "Yes, it will cost … one small gold coin.",
            "Yes, it will cost … three large silver coins.",
        ),
        (
            "A whole small gold coin?",
            "Three large silver coins?",
        ),
    ],
    "151-160.md": [
        (
            "He placed five small gold coins on the counter and the large person quickly swiped it.",
            "He placed two small gold coins on the counter and the large person quickly swiped it.",
        ),
        (
            "not be able to return without paying another five small gold coins.",
            "not be able to return without paying another two small gold coins.",
        ),
    ],
    "131-140.md": [
        (
            "just for that you can have it for twenty small gold coins.",
            "just for that you can have it for eight small gold coins.",
        ),
        (
            "This was more money than he was given by his old adventurer party. He was able to survive half a year on that while also crafting scrolls and now this crystal ball cost more than that.",
            "This was still a hard bite out of his crafting budget. He had survived half a year on the party gift while also crafting scrolls and now this crystal ball wanted a big cut of what he had left.",
        ),
        (
            "How about ten.",
            "How about four.",
        ),
        (
            "Ten? Do you want to rob this old gnome young man? Eighteen!",
            "Four? Do you want to rob this old gnome young man? Eight!",
        ),
        (
            "New enchanted ones cost ten! Twelve.",
            "New enchanted ones cost four! Six.",
        ),
        (
            "finally Roland was able to barter down to fourteen and a half.",
            "finally Roland was able to barter down to six.",
        ),
    ],
    # Part03 Black Rose = better-inn band
    "201-210.md": [
        (
            "There be, four small silver for the night, if ye want food with it it will be five.",
            "There be, two small silver for the night, if ye want food with it it will be three.",
        ),
        (
            "After dropping the four small silver coins he was given a key with a number attached to it.",
            "After dropping the two small silver coins he was given a key with a number attached to it.",
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
            print(f"HIT {name}: {old[:70]}")
        else:
            # try ellipsis variants
            print(f"MISS {name}: {old[:70]!r}")
    if text != orig:
        path.write_text(text, encoding="utf-8")
        print(f"wrote {name}")
