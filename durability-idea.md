# Durability mod idea

Goal: weapons break too fast. Make wear more realistic.

Chosen approach: per-weapon max durability, set from the real analogue's service life, the same way the damage tables use barrel length.

Steps:
1. Find the member on `WeaponSO` that holds max durability and how much is lost per shot. Not known yet because the game DLLs are not available here. A reflection probe that logs every "durab" field and property per weapon would answer it.
2. Build a table of analogue service life in rounds, using `weapon-analogues.md` for the analogues.
3. Convert service life to a max durability per weapon, scaled against the wiki durability values so the numbers stay in the game's range.
4. Apply it once at load, with a config multiplier per weapon and per type, defaults to 1.

Open questions:
- Whether wear per shot should also scale by caliber energy.
- Whether energy weapons are excluded, as in the damage mod.
- Whether `ItemAttributes.MaxDurability` modifiers are a safer route than editing the weapon directly.

Notes: `ItemAttributes.MaxDurability` and `ItemAttributes.DurabilityLoss` already exist and other mods in the repo use them.
