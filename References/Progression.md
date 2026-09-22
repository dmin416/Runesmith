# Progression

Training timelines for battlefield endurance and heavy craft work. These are physical capacity ranges, not class or level curves.

For class levels, skill levels, XP and tier multipliers, see `Levels.md`.

Attribute and **skill technique** age tracks are below.

## Battlefield endurance

Functional battlefield endurance takes roughly 6 to 12 months of consistent training for a sword fighter and 1 to 3 years for an archer on a true war bow. Armored fighting adds another 6 to 12 months on top.

Real battles were bursts of a few minutes of intense fighting separated by pauses and pushing matches. Endurance mostly meant fast recovery between bursts (aerobic base) plus heat and hydration tolerance. Adrenaline masks fatigue during the fight and the crash afterward is severe.

Marching under load mattered as much as swinging. Soldiers spent most days walking with 20 to 30 kg and modern basic training builds that base in 8 to 12 weeks.

### Sword, shield or polearm

- Weeks 1 to 4: 15 to 20 minute bouts. Grip, forearm and shoulder fatigue is the limit.
- Months 2 to 4: 30 to 60 minutes of drills and sparring. Cardio replaces arm strength as the bottleneck.
- Months 6 to 12: Repeated 2 to 3 minute all-out rounds with short recovery. This mirrors real combat and marks a fighter who can last through a battle.
- Armor (15 to 30 kg): roughly doubles energy cost. Heat becomes the main threat.

### Bow

- 30 to 40 lb: a comfortable shooting rate within months.
- 60 to 80 lb: 1 to 2 years of regular practice.
- 100+ lb war bow: 3 or more years historically. English archers started in boyhood and developed lopsided musculature and bone changes.
- A sustained rate of 6 to 10 arrows a minute for several minutes needs back and shoulder endurance well beyond peak draw strength.

## Smithing endurance

A novice reaches full-day capacity in roughly 3 to 6 months of consistent daily work. Full durability for heavy, sustained work takes 1 to 2 years.

- Weeks 1 to 2: 1 to 2 hours a day. Forearm and grip fatigue is the limit. Technique improves fast as the grip relaxes and wasted effort drops.
- Weeks 3 to 8: 3 to 4 hours a day. Forearms, shoulders and back build muscular endurance. Blisters turn to calluses.
- Months 3 to 6: 5 to 8 hours a day. Legs, core and heat tolerance catch up. A full shift becomes sustainable.
- Year 1 to 2: Long heavy days (striking, forging large stock) without cumulative fatigue. Tendons, ligaments and joints finish adapting.

Muscle adapts in weeks but tendons and connective tissue take months. Ramping too fast produces tendinitis in the elbow and wrist, which is the usual way novices stall. Adding about 10 to 20 percent more hammer time each week keeps the ramp safe.

Technique also does much of the work. Using hammer rebound, a loose grip and hip drive cuts the energy cost of each blow enough that a skilled smith outlasts a stronger novice.

Historical apprentices started around age 12 to 14 and worked full days from the beginning. They were productive within about a year and physically seasoned by 2 to 3 years, though with more injuries and attrition than a graduated ramp produces.

## Attribute scale (child to adult)

Real-world calibration for what physical attribute numbers mean. Not a class or XP curve. See `Attributes.md` for what each stat does in-system.

**Untrained adult man average = 15** on each physical (STR / VIT / END / AGI / DEX), or condensed index **15**. That is the street baseline. Trained growth tracks and skill bonuses sit on top.

For agility specifically: **AGI 15** means he sprints as fast as a normal untrained adult man (about **6 m/s** / ~13 mph). Below 15 is slower than that man. Above 15 is faster. There is no Earth athletic ceiling past that point.

### Height, weight and arm length (linear band)

For bodies from **150 cm / 40 kg** to **200 cm / 100 kg**:

```
Weight = 40 + 1.2 × (height − 150)
```

Rate: **1.2 kg per cm**. Every 5 cm of height adds 6 kg.

Segment lengths use standard anthropometric ratios: upper arm **0.186 H**, forearm **0.146 H**, hand **0.108 H**.

```
Full arm (shoulder to fingertip) = 0.44 × height
Elbow to fingertip               = 0.254 × height
```

Every 5 cm of height adds **2.2 cm** of full arm length.

| Height | Weight | Upper arm | Forearm | Hand | Elbow→tip | Full arm |
|---|---|---|---|---|---|---|
| 150 cm | 40 kg | 27.9 | 21.9 | 16.2 | 38.1 | 66.0 |
| 155 cm | 46 kg | 28.8 | 22.6 | 16.7 | 39.4 | 68.2 |
| 160 cm | 52 kg | 29.8 | 23.4 | 17.3 | 40.6 | 70.4 |
| 165 cm | 58 kg | 30.7 | 24.1 | 17.8 | 41.9 | 72.6 |
| 170 cm | 64 kg | 31.6 | 24.8 | 18.4 | 43.2 | 74.8 |
| 175 cm | 70 kg | 32.6 | 25.6 | 18.9 | 44.5 | 77.0 |
| 180 cm | 76 kg | 33.5 | 26.3 | 19.4 | 45.7 | 79.2 |
| 185 cm | 82 kg | 34.4 | 27.0 | 20.0 | 47.0 | 81.4 |
| 190 cm | 88 kg | 35.3 | 27.7 | 20.5 | 48.2 | 83.6 |
| 195 cm | 94 kg | 36.3 | 28.5 | 21.1 | 49.6 | 85.8 |
| 200 cm | 100 kg | 37.2 | 29.2 | 21.6 | 50.8 | 88.0 |

Segment columns are in cm.

**Throw geometry:** full arm is the pivot-to-tip distance for a **shoulder**-pivoted swing. Elbow→tip is the pivot-to-tip distance for the **elbow**-pivoted forearm case; add tube length past the hand to get exit distance L. Example: at 180 cm, elbow→tip ≈ 45.7 cm; a tube that exits near 91 cm from the elbow extends about 45 cm past the fingertips.

Use weight when sprint KE needs a mass (`KE = ½mv²`). The AGI equal-mass speed column still assumes ~80 kg (about **183 cm** on this line). Roland’s age-9 height **4'7"** (~140 cm) sits below this band; do not force the adult line onto small children without a separate curve.

### Sickly 5-year-old baseline (Roland transfer)

Matches early Chapter 1–2 physicals (sheet values; AGI/DEX may already include small skill pads):

| Attribute | Value |
|---|---|
| Strength | 4 |
| Vitality | 4 |
| Endurance | 4 |
| Agility | 8 |
| Dexterity | 8 |

Condensed average ~**6**.

### Stats by age (daily training and decent nutrition)

Body baseline from age plus steady training. **Not** the untrained civilian curve. Skill traits (Technology, Tinkerer, etc.) can push a sheet above these numbers, especially Dexterity.

| Age | STR | VIT | END | AGI | DEX | Avg |
|---|---|---|---|---|---|---|
| 5 | 4 | 4 | 4 | 8 | 8 | 6 |
| 6 | 7 | 7 | 6 | 11 | 11 | 8 |
| 7 | 9 | 9 | 8 | 13 | 13 | 10 |
| 8 | 11 | 11 | 10 | 15 | 15 | 12 |
| 9 | 13 | 13 | 12 | 16 | 16 | 14 |
| 10 | 15 | 14 | 13 | 17 | 16 | 15 |
| 11 | 17 | 15 | 15 | 18 | 17 | 16 |
| 12 | 19 | 16 | 17 | 19 | 17 | 18 |
| 13 | 22 | 17 | 19 | 20 | 18 | 19 |
| 14 | 25 | 18 | 21 | 21 | 18 | 21 |
| 15 | 28 | 19 | 23 | 22 | 19 | 22 |
| 16 | 31 | 20 | 24 | 22 | 19 | 23 |
| 17 | 33 | 21 | 25 | 23 | 20 | 24 |
| 18 | 35 | 21 | 26 | 23 | 20 | 25 |
| 19 | 37 | 22 | 27 | 24 | 20 | 26 |
| 20 | 38 | 22 | 27 | 24 | 21 | 26 |
| 21 | 39 | 22 | 28 | 24 | 21 | 27 |

Strength and endurance accelerate hardest between ages 12 and 16 as puberty adds muscle mass plus heart and lung size. Agility and dexterity flatten after 15 since skill and nervous system development finish early. At 21 the overall average of **27** is **1.8×** the untrained adult man (**15**).

Age 10 on this track already matches the untrained adult **index** (avg 15), with a more agile / less STR-heavy shape than a soft civilian.

### Stat to real output

**Working draft. Rough. Use for now.**

Most stats are linear. Agility is mechanical burst power first, sprint speed second.

```
Power:          P ≈ 25 × AGI   watts
Equal-mass run: v = 6 × √(S / 15)   m/s
```

**Why watts:** average power to build sprint KE (ignore drag and limb churn) is `P ≈ KE / t`.

| | Mass | Top speed | Body KE | Time to top | Avg power |
|---|---|---|---|---|---|
| Street man | 80 kg | 6 m/s | ½ × 80 × 6² = **1,440 J** | ~4 s | 1,440 / 4 ≈ **360 W** |
| Usain Bolt | 94 kg | 12.4 m/s | ½ × 94 × 12.4² ≈ **7,227 J** | ~6 s | 7,227 / 6 ≈ **1,200 W** |

KE ratio 7,227 / 1,440 ≈ **×5.0**. Speed alone gives (12.4/6)² ≈ ×4.27. Bolt’s extra mass (94/80 ≈ ×1.18) finishes the ×5. Power ratio is only **×3.3** (1200 / 360) because he takes longer to finish accelerating.

**AGI landmarks**

| Landmark | AGI | Power (25 W × AGI) | Equal-mass sprint `v = 6√(S/15)` |
|---|---|---|---|
| Street man | **15** | **375 W** (~360 W) | **6.0 m/s** |
| Bolt-class power | **48** | **1,200 W** | **10.7 m/s** at equal 80 kg |
| Equal-mass 12.4 m/s | **64** | 1,600 W | **12.4 m/s** |
| Clean ×5 KE at 80 kg | **75** | 1,875 W | **13.4 m/s** |

Compromise: **AGI tracks watts** (15 → street, 48 → Bolt’s ~1200 W). The equal-mass √S speed column is what the sheet uses when body mass is treated as stable (~80 kg). Real Bolt’s 12.4 m/s needs his extra mass and longer accel window on top of that power; the sheet does not force AGI 48 to equal 12.4 m/s under equal mass. No artificial speed cap.

Equivalently `v ≈ 1.549 × √S` on the equal-mass column.

| Stat | Real measure | Conversion | Untrained adult (S = 15) | Sickly 5-year-old |
|---|---|---|---|---|
| STR | Max deadlift | 6 kg × S | 90 kg | S 4 = 24 kg |
| VIT | Natural lifespan | 3 years × S | 45 years | S 4 = 12 years |
| END | VO2 max | 0.2 L/min × S | 3 L/min | S 4 = 0.8 L/min |
| AGI | Burst power / sprint | 25 W × S; v = 6√(S/15) | 375 W; 6 m/s | S 8 ≈ 200 W; 4.4 m/s |
| DEX | Pegboard pegs (right hand) | 1 peg × S | 15 pegs | S 8 = 8 pegs |
| INT | Working memory (digit span) | 0.5 digits × S | 7.5 digits | see mental track |
| WILL | Effective life experience | 2 years × S | 30 years | see mental track |

Other equal-mass checks: S 21 → 7.1 m/s (525 W). S 40 → 9.8 m/s (1,000 W). S 100 → 15.5 m/s (2,500 W).

VIT → lifespan is abstract constitution potential, not a doctor’s forecast for a child.

World name for the experience / resolve attribute is **Willpower** (not Wisdom). Draft tables that say WIS mean Willpower.

### Real output by age (trained track)

Same conversions on the age table (AGI uses √S):

| Stat | Real measure | Age 5 | Age 10 | Age 15 | Age 21 |
|---|---|---|---|---|---|
| STR | Max deadlift | 24 kg | 90 kg | 168 kg | 234 kg |
| VIT | Natural lifespan | 12 years | 42 years | 57 years | 66 years |
| END | VO2 max | 0.8 L/min | 2.6 L/min | 4.6 L/min | 5.6 L/min |
| AGI | Sprint speed | 4.4 m/s | 6.4 m/s | 7.3 m/s | 7.6 m/s |
| DEX | Pegboard pegs (right hand) | 8 pegs | 16 pegs | 19 pegs | 21 pegs |

Late teens on this track read as serious athletes versus the untrained adult at S = 15. High skill-padded AGI keeps climbing without a hard ceiling; diminishing returns come from the square root alone.

## Mental attributes (adult mind)

**Roland track.** Adult mind in a child body under the same daily loop (including **4 hours of reading**). Body row is pure mental baseline before skills, traits and class packages. See `StatusBreakdown.md`.

Willpower 15 equals the **30 years of life experience** the mind already carries. Intelligence is limited by brain hardware rather than knowledge, so the child starts slightly under the adult value until the brain matures.

### Stats by age (adult mind, daily training, 4 hours reading)

| Age | INT | WILL | Avg of all 7 stats |
|---|---|---|---|
| 5 | 12 | 15 | 8 |
| 6 | 13 | 17 | 10 |
| 7 | 15 | 19 | 12 |
| 8 | 16 | 21 | 14 |
| 9 | 17 | 23 | 16 |
| 10 | 18 | 25 | 17 |
| 11 | 19 | 26 | 18 |
| 12 | 20 | 27 | 19 |
| 13 | 21 | 28 | 21 |
| 14 | 22 | 29 | 22 |
| 15 | 22 | 30 | 23 |
| 16 | 23 | 31 | 24 |
| 17 | 24 | 32 | 25 |
| 18 | 24 | 33 | 26 |
| 19 | 25 | 33 | 27 |
| 20 | 25 | 34 | 27 |
| 21 | 26 | 35 | 28 |

Avg of all 7 = (STR + VIT + END + AGI + DEX + INT + WILL) / 7 using the physical age table plus this mental row. Charisma and Luck are not in that average.

### Real output (mental)

| Stat | Real measure | Age 5 | Age 10 | Age 15 | Age 21 |
|---|---|---|---|---|---|
| INT | Digit span | 6 | 9 | 11 | 13 |
| WILL | Effective experience | 30 years | 50 years | 60 years | 70 years |

- **Intelligence:** starts under the adult value at age 5 since working memory depends on brain development. It reaches **15 at age 7** and keeps climbing because daily reading and problem solving train it. Growth slows after puberty as the brain finishes maturing.
- **Willpower:** starts at the full adult value and gains **2 per year through age 10**. Each real year of life adds experience while roughly **2,200 novels** of vicarious experience and daily fighting and climbing decisions add more. After age 10 the gain drops to **1 per year** since the reading volume stays constant while returns diminish.
- **Age 21:** INT **26** is **1.73×** the average adult man and WILL **35** is **2.33×**.

Skills and traits still stack on top (Debugger, Technology, Reading, Mana Sense, Logical Thinker, etc.). Class packages add Mage Int/Will on top of this body row.

**Rewrite note:** older Chapter 2 notes used bare Int 11 and Will 8. Use this table instead (age 5: Int 12, Will 15). Retcon early sheets when touching those chapters.

## Skill levels (technique only)

Skill **level measures technique only**: form, efficiency, timing and decision making. Body size and strength affect results but **do not** raise the level. A small elite technician can sit at a high skill level and still lose a contest of raw force to a bigger amateur.

Aligns with `Levels.md` / `Ideas.md`: skills rank **L1–L9**, then evolve. L9 is the hard max for that skill name.

### Technique landmarks

| Level | Meaning |
|---|---|
| **L5** | Dedicated adult amateur |
| **L7** | Competitive or professional |
| **L9** | Pinnacle of normal human technique |

### Daily loop (about 13 waking hours and 11 hours of sleep)

Assumed schedule behind the age-5-to-21 stat track and the skill table below. Real instruction and self-correction are available (Arden drills, library, field use).

| Block | Time per cycle | Cycles per day | Daily total |
|---|---|---|---|
| Train until tired | 1.75 hours | 4 | 7 hours |
| Read until mentally tired | 1 hour | 4 | 4 hours |
| Eat | 0.5 hours | 4 | 2 hours |

Over five years that comes to about **12,800 hours of training** and **7,300 hours of reading**. Splitting training into four sessions with food between them is close to ideal for a child, since distributed practice builds technique faster than one long session and frequent meals cover the recovery load. The stat progression from ages 5 to 21 in this file holds under this schedule.

### Early Basic skills by age (trained track)

Levels shown are technique ranks at that birthday under the daily loop. `0` = not unlocked yet.

| Skill | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|
| Basic Running | 0 | 3 | 5 | 7 | 8 | 9 |
| Basic Sprint | 0 | 3 | 5 | 7 | 8 | 9 |
| Basic Hand to Hand Combat | 0 | 3 | 5 | 6 | 7 | 8 |
| Basic Climbing | 0 | 4 | 6 | 8 | 9 | 9 |
| Basic Throwing | 0 | 3 | 5 | 7 | 8 | 9 |
| Basic Sneaking | 0 | 3 | 5 | 6 | 7 | 8 |
| Basic One-Handed Swordsmanship | 0 | 2 | 4 | 6 | 7 | 8 |
| Basic Leather Armor Proficiency | 0 | 3 | 5 | 6 | 8 | 9 |
| Reading Proficiency (normal child) | 0 | 4 | 6 | 8 | 9 | 9 |

For **Roland** (adult mind in a child body), use the transmigrator Reading table below, not this row.

### What changed from the first technique table

- **Reading (normal child):** four hours a day at about 200 words per minute is roughly 17 million words a year and about 87 million over five years. That volume supplies the vocabulary and reference knowledge that held reading at L8 before, so **L9 arrives at age 9**. Roland is faster; see transmigrator table.
- **Climbing:** reaches **L9 at age 9** from the added volume.
- **Running, Sprint and Throwing:** reach **L9 at age 10** since repetition count is the main limit on clean mechanics.
- **Hand to Hand, Sneaking and Sword:** stop at **L8** because the last level needs varied skilled opponents and real field experience that solo daily repetition cannot supply.
- **Leather Armor:** reaches **L9 at age 10** (daily drill in armor; Vitality + Endurance pads). Was a narrow L6 side skill in the first table.

### Reading by age (adult mind, child body, 4 hours daily)

**Roland track.** An avid adult novel reader starts at **L7** and about **300 words per minute**. The child body trims that slightly at age 5 since eye tracking and stamina are still developing. Vocabulary, inference and reference knowledge are already present. What remains is training the eyes and pacing.

| Age | Level | Speed (wpm) | Words read in the year ahead |
|---|---|---|---|
| 5 | 7 | 270 | 27 million |
| 6 | 8 | 350 | 34 million |
| 7 | 9 | 430 | 41 million |
| 8 | 9 | 500 | 47 million |
| 9 | 9 | 570 | 53 million |
| 10 | 9 | 640 | n/a |

The five years add up to about **200 million words**, or roughly **2,200 novels** at 90,000 words each.

**What changes from the normal child row**

- **Level:** L9 arrives at **age 7** instead of age 9. The mind already carries the vocabulary, inference skill and reference knowledge that a normal child needs years of reading to build.
- **Speed:** 640 wpm at age 10 sits at the top of normal human reading with full comprehension. It passes the average adult novel reader (300 wpm) by more than double.
- **Age 5 drag:** the child body holds speed about 10% under the adult starting point until eye movement and reading stamina mature around age 7.
- **After L9:** the level stays fixed (pinnacle of normal technique). Speed is the only number that keeps climbing and it flattens near **700 wpm** because past that point comprehension starts to fall.

Hastened Reading and similar skills can sit on top of this as further time cuts or comfort at high speed. They do not push Reading Proficiency past L9. Evolution to a higher reading skill is a separate gate.

### What the age 10 levels mean as technique

- **Running L9:** pinnacle distance form. Stride, cadence, breathing and pacing on mixed terrain are fully cleaned up. Speed is still limited by the child’s legs and lungs.
- **Sprint L9:** pinnacle sprint mechanics. Start, drive phase, arm action and relaxation at top speed are fully cleaned up. Only body size separates the result from an elite adult sprinter.
- **Hand to Hand L8:** precise footwork, distance control, timing, feints and combinations with sound defense. Damage is limited by mass. L9 waits on varied skilled sparring partners.
- **Climbing L9:** the pinnacle (from age 9). Route reading, weight transfer, three point contact and rest positions are flawless. Children learn balance and body control fastest here.
- **Throwing L9:** full body mechanics, release timing and target leading are fully cleaned up. Range is limited by arm strength while accuracy technique is at the human ceiling for this Basic skill.
- **Sneaking L8:** controlled foot placement, use of cover, shadow and noise masking, and patient movement. L9 needs experience against skilled observers in real field conditions.
- **One-Handed Swordsmanship L8:** cuts, guards, footwork and feints are high competitive / near-professional technique. L9 needs more sparring against varied skilled adults and adapting mid fight under pressure.
- **Leather Armor L9:** fitting, adjusting and moving fluidly in armor for long periods. Hits the technique ceiling with the daily drill loop.
- **Reading L9 (Roland):** pinnacle from **age 7**. At age 10, about 640 wpm with full comprehension. Level no longer rises. Speed may still creep toward ~700 wpm.

Skills that depend almost entirely on body awareness and repetition (climbing, running mechanics, throwing form) can hit L9 on this schedule. Skills that need opponents or unpredictable conditions (hand to hand, sword, sneaking) cap at L8 until sparring and field experience catch up. Reading for Roland is mind-first: L9 early, then speed only.

### Marksmanship at transfer (Earth firearms, adult mind)

**Assumptions:** one 2-hour session a month with about 100 rounds. Ten years is 120 sessions, about **240 hours** and **12,000 rounds**.

**Where it lands (technique only)**

| Practice style | Level | What the technique looks like |
|---|---|---|
| Self taught, live fire only | L5 | Safe handling, solid grip and stance, consistent groups at moderate range. Flaws like a mild trigger jerk or anticipation stay in place |
| Occasional coaching or a few classes | L6 | Fundamentals are clean with decent speed and accuracy together |
| Monthly range plus 15 minutes of dry fire at home | L6 to L7 | Trigger press and sight tracking stay sharp between sessions, which mimics far more volume |

**Why it stays low**

- **Hours alone say L7.** 240 hours matches the L7 mark of 200 to 400 hours on the earlier curve.
- **Spacing cuts the value.** A month between sessions means the first 20 to 30 minutes go to relearning what faded, so the effective practice time is closer to 150 hours.
- **No feedback loop.** Without a coach or shot timer, bad habits fossilize and nothing corrects them. Most casual shooters plateau at L4 to L5 after the first year and stay there for decades.
- **Real world match:** this is the typical lifelong recreational shooter. Decent and safe with reliable groups, but well short of competitive level.

**The child with an adult mind**

- **L5 by session 3 or 4.** The mind skips the concept phase and applies corrections on its own.
- **L7 by year 10.** Self correction closes the feedback gap that holds most casual shooters back, though the monthly spacing still caps it below L8.
- **Body limit:** a .22 rifle or light pistol removes the strength restriction until the stat progression catches up.

**Rewrite default:** Marksmanship transfers at **L7** (Dexterity +7). Not L3.

**Rewrite note:** older chapter screens that park every Basic combat skill at L9 by age 10, or that used the first softer technique table, are outdated. Retcon those sheets when touching those chapters (e.g. Chapter 7 skill list). Use the transmigrator Reading table for Roland, not the normal-child Reading row. Use Marksmanship **L7** at transfer, not L3.
