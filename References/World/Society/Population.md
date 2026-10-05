# Terra Population Formulas

## Inputs

| Variable | Meaning | Values |
|---|---|---|
| P | Kingdom population | Any |
| M | Monster pressure | 0.5 safe heartland, 1 normal, 1.5 Caldris baseline, 2 frontier, 3 dungeon region |
| W | War state | 1 peace, 2 border war, 3 full mobilization |

## Rounding Rules

- Houses and settlements are whole numbers with a floor of 1: N = max(1, round(...))
- People are whole numbers
- Tier counts below 10 are shown as rates per million and never rounded up to 1

## Settlements

| Tier | Share of P | Size range | Typical size |
|---|---|---|---|
| Capital | 4% | 1 per kingdom | |
| Cities | 10% | 20,000 to 100,000 | 40,000 |
| Towns | 11% | 2,000 to 20,000 | 10,000 |
| Villages | 75% | 100 to 2,000 | 500 |

- Settlement count N = max(1, round(share × P ÷ typical size)), with halves rounding up
- Typical size sets the default count only; the size range sets which other layouts are allowed
- Urban population U = capital + cities + towns = 0.25 × P (U must be recalculated if the shares change)

## Royals and Nobility (counted with families)

| Group | Formula |
|---|---|
| Royal bloodline | R = max(15, 10 × log10(P) − 20) |
| High noble houses | max(1, round(P ÷ 50,000)) houses × 15 people |
| Minor noble houses | max(1, round(P ÷ 2,000)) houses × 8 people |
| Gentry houses (esquires, landed gentlemen) | max(1, round(P ÷ 1,000)) houses × 6 people |

Royal bloodline gives 30 at 100,000, 40 at 1,000,000 and 50 at 10,000,000.

## Population Split

Order of subtraction:

1. P' = P − nobility total
2. Villains V = 0.004 × P' × M (outside the workforce; they live off theft, raids and bounties on others, and grow with dungeon and monster chaos)
3. P'' = P' − V
4. Dependents (children, elderly, infirm) D = 0.40 × P''
5. Workforce L = 0.60 × P''
6. Military, adventurers, hunters, mages, runesmiths and civilian roles come out of L
7. Farmers = whatever remains of L

## Knights

Knights are dubbed fighters of any birth. They form an elite class separate from the standing army's rank and file.

| Group | Formula | Counted in |
|---|---|---|
| Total knights | P ÷ 1,000 | |
| Noble-born knights | 0.5 × total | Nobility (adds no people) |
| Commoner-dubbed knights | 0.5 × total | Workforce L |

## Military

| Group | Formula |
|---|---|
| Commoner-dubbed knights | 0.5 × P ÷ 1,000 |
| Standing army (knights not included) | 0.004 × P × W × (0.5 + 0.5M) |
| City guard | 0.008 × U |
| Royal guard (separate from the army) | 5 × R |
| Levies (war only) | 0.01 × P × (W − 1) |

Every soldier added in war comes out of farmers, since farmers are the remainder of L. Army expansion and levies both draw from the fields first.

## Adventurers and Hunters

Each person is one or the other, never both.

| Group | Definition | Formula |
|---|---|---|
| Adventurers | Guild-registered and ranked. Take quests, clear dungeons, travel between cities. | 0.01 × L × M |
| Hunters | Local and unranked. Cull goblin-grade monsters near home for ears, blood, parts and stones, plus meat from edible low monsters. **Never eaten:** goblins (and goblin-kin), ghouls, zombies, liches and other undead. All count as Bronze-level kill capacity. | 0.01 × L × M |

## Magic Path

Tier 1 mage is the prerequisite for both mages and runesmiths. Personal power is treasured above all else on Terra, so few mage-capable people give up combat growth to become runesmiths.

| Group | Formula |
|---|---|
| Mage-capable (Tier 1 or higher) | Mg = 0.004 × L |
| Runesmiths | r × Mg |
| Practicing mages | (1 − r) × Mg |

| Kingdom type | r |
|---|---|
| War-focused | 0.05 |
| Caldris default | 0.10 |
| Craft-focused | 0.15 to 0.20 |

Mages and runesmiths are counted on top of craftsmen, clergy and officials.

## Civilian Roles (share of L)

| Role | Share |
|---|---|
| Monster tamers and herders | 4% |
| Laborers (ditch, porters, miners) | 12% |
| Craftsmen | 11% |
| Industrial (steam and rail) | 3% |
| Merchants | 4% |
| Servants (including noble households) | 7% |
| Church of Solaria clergy and healers | 1.5% |
| Officials and guild staff | 1% |
| Scribes and copyists (no mass printing) | 1% |
| Entertainers and other | 1% |

Civilian shares total 45.5% of L.

## Farmers

Farmers = L − civilian shares − commoner-dubbed knights − standing army − city guard − royal guard − levies − adventurers − hunters − practicing mages − runesmiths

## Tier Falloff

Count at tier n (1 lowest) = Total × f^(N−n) ÷ (sum of f^k for k = 0 to N−1)

| Group | Tiers N | f | Divisor |
|---|---|---|---|
| Adventurers (guild ranks) | 8 | 4 | 21,845 |
| Villains (equivalent power rank) | 8 | 4 | 21,845 |
| Mages | 5 | 5 | 781 |
| Runesmiths (highest rune rank they can craft) | 5 | 5 | 781 |

Guild ranks (Source lock, eight): Bronze → Steel → Silver → Gold → Platinum → Mithril → Orichalcum → Adamantium. Detail: `../../Progression/AdventurerRanks.md`.

Rune ranks: Lesser, Common, Greater, Grand, Legendary

## Caldris Example: P = 1,000,000, M = 1.5, W = 1

### Intermediate values

| Value | Result |
|---|---|
| Nobility total | 10,340 |
| P' | 989,660 |
| Villains V | 5,938 |
| P'' | 983,722 |
| Dependents D | 393,489 |
| Workforce L | 590,233 |
| Urban U | 250,000 |
| Mage-capable Mg | 2,361 |

### Settlements

| Tier | Population | Count |
|---|---|---|
| Capital | 40,000 | 1 |
| Cities | 100,000 | 3 averaging 33,000 (allowed range: 1 at 100,000 up to 5 at 20,000) |
| Towns | 110,000 | 11 |
| Villages | 750,000 | 1,500 |

### Counts

| Group | Count |
|---|---|
| Royal bloodline | 40 |
| High nobility (20 houses) | 300 |
| Minor nobility (500 houses) | 4,000 |
| Gentry (1,000 houses) | 6,000 |
| Noble-born knights (inside nobility) | 500 |
| Villains and criminals | 5,938 |
| Dependents | 393,489 |
| Commoner-dubbed knights | 500 |
| Standing army | 5,000 |
| City guard | 2,000 |
| Royal guard | 200 |
| Adventurers | 8,853 |
| Hunters | 8,853 |
| Practicing mages | 2,125 |
| Runesmiths | 236 |
| Monster tamers | 23,609 |
| Laborers | 70,828 |
| Craftsmen | 64,926 |
| Industrial (steam and rail) | 17,707 |
| Merchants | 23,609 |
| Servants | 41,316 |
| Church of Solaria clergy and healers | 8,853 |
| Officials and guild staff | 5,902 |
| Scribes and copyists | 5,902 |
| Other | 5,902 |
| Farmers | 293,909 (49.8% of workforce) |

Under arms in peace: 8,200 (0.82% of P), counting all 1,000 knights, army, city guard and royal guard.

### Full Mobilization (W = 3)

| Group | Count |
|---|---|
| Standing army | 15,000 (+10,000 from farmers) |
| Levies | 20,000 (from farmers) |
| Total under arms with all knights and guards | 38,200 (3.8% of P) |
| Farmers | 263,909 (44.7% of workforce) |

### Guild Ranks

| Rank | Adventurers | Villains |
|---|---|---|
| Bronze | 6,640 | 4,454 |
| Steel | 1,660 | 1,113 |
| Silver | 415 | 278 |
| Gold | 104 | 70 |
| Platinum | 26 | 17 |
| Mithril | about 6 to 7 (6.5 per million) | about 4 to 5 (4.3 per million) |
| Orichalcum | about 1 to 2 (1.6 per million) | about 1 (1.1 per million) |
| Adamantium | under 1 (0.4 per million) | under 1 (0.3 per million) |

### Magic Tiers

| Tier | Mages | Runesmiths |
|---|---|---|
| 1 / Lesser | 1,700 | 189 |
| 2 / Common | 340 | 38 |
| 3 / Greater | 68 | about 7 to 8 (7.6 per million) |
| 4 / Grand | 13 to 14 (13.6 per million) | 1 to 2 (1.5 per million) |
| 5 / Legendary | 2 to 3 (2.7 per million) | 1 per 3 million (0.3 per million) |

One or two Grand runesmiths per million people keeps trains a kingdom-level investment. A Legendary runesmith appears about once per 3 million people, so royal airships stay very rare.

## Monster Supply Requirement

### Loot values

| Variable | Meaning | Value |
|---|---|---|
| E | Goblin ear bounty (Economy.md) | 5 lc (50 sc) |
| S | Rice-grain magic stone (Economy.md) | 2 ss (200 sc) |
| d | Stone drop rate | 1 in 5 |
| H | Blood and parts per goblin (locked; mostly blood for conduction ink / priming) | 30 SC (3 LC) |
| w | Unskilled day wage (Economy.md) | 5 to 10 lc (50 to 100 sc) |

### Formulas

- Average goblin value G = E + H + d × S = 120 sc
- Kills per hunter per year to match a laborer K = **361** × w ÷ G (Caldris year)
- Goblin-grade hunters Hg = Hunters + Bronze adventurers
- Required kills per year = Hg × K
- Stones per year = Required kills × d

### Caldris result

| Wage | K | Hg | Kills per year | Stones per year |
|---|---|---|---|---|
| 5 lc | 150.42 | 15,495 | 2,330,706 | 466,141 |
| 10 lc | 300.83 | 15,495 | 4,661,413 | 932,283 |

Dungeons and monster spawns must replace about **2.3 to 4.7** million goblin-grade monsters per million people every year or hunters starve out and the loot economy collapses. Villains add no kills; they skim value from hunters and merchants through theft and raids.

Ecology, carrying capacity, bargain tiers and **given-area worksheet:** `../Fauna/MonsterPopulation.md`.

## Historical Comparison

| Measure | Caldris | Historical reference | Verdict |
|---|---|---|---|
| Agricultural workforce (farmers plus tamers) | 53.8% | England 78% in 1381, 64% in 1600, 47% in 1700 | Matches late 1600s England, fitting steam, rail and tamed monster farming |
| Nobility and gentry with families | 1.0% of P | Usually 1% to 3% in England and France; extremes from 0.1% to 10% | Inside the normal range |
| Knights | 1 per 1,000 | England c.1300: about 1,250 to 1,500 dubbed knights for 4.5 to 5 million people (1 per 3,500) | About 3.5 times England; justified by monsters, dungeons and skill-based fighter jobs |
| Clergy | 0.9% of P | About 1% in medieval estimates | Matches |
| Cities of 20,000 or more | 14% of P or slightly more (large towns can reach 20,000) | Europe 1300: about 5% in cities over 10,000 | Well above medieval; matches rail-era Europe |
| Peacetime armed forces | 0.82% of P (8,200) | Medieval kingdoms kept almost no standing army; early modern states 0.5% to 1% | Early modern level |
| Full war mobilization | 3.8% of P | Medieval field armies rarely topped 0.5% of P; 18th-century peak militarized states reached a few percent | Possible only through rail and storage bag logistics |
| Dependents | 39.3% of P | Pre-industrial populations ran 35% to 40% under age 15 plus elderly | Matches |
| Kingdom size | 1,000,000 | Scotland under 1 million, England 4 to 5 million, France 15 to 20 million around 1300 | Small to mid kingdom, fitting a fragmented map |

## Kingdom Fragmentation

Low barriers to personal power cap how large a realm stays unified. Kingdom count on Terra = Terra population ÷ 1,000,000 as a baseline.

| Kingdom breaker | Per million |
|---|---|
| Mithril+ adventurers (Mithril / Orichalcum / Adamantium) | ~8.5 |
| Mithril+ villains | ~5.7 |
| Legendary mages | 2.7 |
| Legendary runesmiths | 0.3 |
| Total | about 17 |

About 17 individuals per million can found or break a kingdom on their own, which keeps realms near this size. Pure Adamantium alone is under 1 per million (matches Source “countable on one hand” talk).
