# Other Useful Skills

> **Ideas / design loot.** Not automatic law. Same Tier 1 → Tier 2 → fused Tier 3 pattern and **M** curve as `ResistanceImmunitySystem.md` / `SensingManaSoundSystem.md`. Live hubs win: `Skills.md`, `SkillsDesign.md`, `SkillRanks.md`, `RolandResistanceTracks.md`.
>
> Each line: two Tier 1 skills evolve separately, then fuse at Tier 3. The note after each line names the quantity M multiplies.

**Related idea files**
- Resist pairs (eight resists → four Fused): `ResistanceImmunitySystem.md` — Heat+Cold → Temperature Immunity; Blunt+Sharp → Melee Immunity; Poison+Alcohol → Pure Blood; Sleep+Pain → Iron Will
- Sensing / mana / smith / sound: `SensingManaSoundSystem.md`

---

## Conflicts and soft-ok (read first)

### Live wins

| Topic | Live lock | This idea |
|---|---|---|
| **Recovery** | One **Recovery → Rapid Recovery** flesh/blood track; no limb regrow | Split Wound + Blood → Regeneration with limb unlock |
| **Breath** | **Breath Control** (`hold = T0 × M_body × level`) | Breath Holding → Suffocation Immunity |
| **Mana refill** | **Mana Absorption** + **Mana Regulation** + **Mana Reinforcement** (store) | Mana Recovery / Endless Vigor line |
| **Electricity** | Roland grind: **Electricity Resistance** (`RolandResistanceTracks.md`) | Electric Resistance → Immunity (same family; keep live name) |
| **Enchant vs rune** | **Different crafts** in the world’s eyes | Enchanting → Runecraft fusion (wrong merge) |
| **Diagnosis** | **D-only**; not a craft unlock product | First Aid + Diagnosis → Healer’s Hands |
| **Parallel Thinking / Multitasking** | Separate skills; Parallel level = true parallel count | Fuse into Split Mind |
| **Dodging / Sword / etc.** | Live Basics and evolve prefixes | Parry/Dodge → Untouchable; Weapon Saint, etc. |
| **Running / Sprint** | Live Basics | Sprint + Marathon → Swift Body |
| **Marksmanship** | Live transfer skill | Aim → True Aim (park as Marksmanship depth) |

### Soft-ok

- Same **M** tier curve as the other idea files for *feel* on one skill’s depth.
- **Disease / Curse** as tracks outside Pure Blood (pathogen / curse gap).
- **Electric** current thresholds as feel for Electricity Resistance.
- **Stealth vs sensing** contest (detection range × √M style).
- **Reflexes** dividing reaction time as combat feel (do not override SpeedVsIntellect locks without a merge).
- Listing high-leverage LitRPG skills (Reflexes, Stealth, Night Vision, Stamina/Fatigue, Disease, Mental) as rewrite priorities for *scenes*, not automatic new cards.

### Still idea-only

- Most Fused names (Regeneration, Untainted, Abyssal Body, Ghost, Combat Precognition, …)
- Limb regrowth at Tier 3
- Enchanting/Runecraft merge; Artifact Creation
- Speed Learning multiplying skill XP without a separate dial pass (`SkillLevelCostMultiplier.md` / kill XP stay separate)

---

## Recovery

- **Wound Recovery → Rapid Healing** + **Blood Recovery → Iron Blood** → **Regeneration.** M multiplies healing speed and blood production. Limb regrowth unlocks at Tier 3.
  - *Live:* prefer **Recovery / Rapid Recovery**. Limb regrow stays idea-only.
- **Stamina Recovery → Second Wind** + **Mana Recovery** (if separate from Absorption) → **Endless Vigor.** M multiplies recovery rate from exertion.
  - *Live:* SP/MP regen sit on attributes / Regulation / Absorption; Reinforcement is not Mana Recovery.
- **Disease Resistance → Disease Immunity** + **Curse Resistance → Curse Immunity** → **Untainted.** M divides infection load and curse potency. This fills the pathogen gap left out of Pure Blood.
  - *Soft-ok as gap fillers.* Abyssal Corruption Resistance stays its own late track.

---

## Survival

- **Breath Holding → Suffocation Immunity** + **Pressure Resistance → Pressure Immunity** → **Abyssal Body.** M multiplies oxygen efficiency and pressure tolerance. Tier 3 survives the deep sea and vacuum.
  - *Live:* **Breath Control**. Pressure track is new idea.
- **Hunger Resistance → Fasting** + **Thirst Resistance → Arid Body** → **Self-Sustaining.** M multiplies time survivable without food or water. Baseline about **3 weeks** without food and **3 days** without water.
- **Fatigue Resistance → Tireless** + **Exertion Endurance** → merges cleanly with Iron Will or stands alone. M multiplies time to exhaustion.
  - *Idea;* live Endurance attr and Iron Will (resist idea) are not this skill.
- **Radiation Resistance → Radiation Immunity.** M divides effective dose in sieverts. Useful for magic-crystal or alchemical radiation settings.
- **Electric Resistance → Electric Immunity.** M multiplies the current needed to stop the heart. Baseline about **0.1 A** across the chest. Pairs with Temperature Immunity for lightning.
  - *Soft-ok feel for live **Electricity Resistance**.* Do not invent a second named Electric track.

---

## Mental

- **Fear Resistance → Fearless** + **Charm Resistance → Charm Immunity** → **Unshakable Mind.** M divides the potency of fear, intimidation, charm and mind-control effects.
  - *Overlaps Goals **Mental Resistance** wishlist.*
- **Illusion Resistance** feeds into Mana Sight already. It can also stand alone.
- **Memory → Perfect Recall.** M multiplies retention time and detail. Tier 2 grants eidetic memory.
  - *Overlaps Knowledge Retention / Brilliant perks; park carefully.*
- **Focus → Concentration** + **Parallel Thinking → Multitasking** → **Split Mind.** M multiplies the number of simultaneous tasks or spells held.
  - *Live conflict:* Parallel Thinking and Multitasking stay separate; Parallel level = true parallel count (`FocusCapacity.md`).
- **Speed Reading → Speed Learning.** M multiplies learning speed for books and skills. Interacts with existing XP math.
  - *Overlaps Hastened Reading / Fast Learning.* Do not multiply kill XP or flat skill-use tables without a dial pass.

---

## Combat execution

- **Aim → True Aim** + **Throwing → Cannon Arm** → **Deadeye.** Already worked out in the resist/performance appendix park.
  - *Live:* **Marksmanship** + **Basic Throwing**.
- **Reflexes → Reaction** + **Prediction → Foresight** → **Combat Precognition.** M divides reaction time. Baseline **200–250 ms**, so Tier 1 Lv9 is **20–25 ms** and Tier 3 Lv9 is **0.2 ms**, fast enough to track bullets.
  - *Check `../Combat/SpeedVsIntellect.md` before promoting; Int already cuts simple RT.*
- **Parry → Deflection** + **Dodge → Evasion** → **Untouchable.** M multiplies the attack speed that can be reliably blocked or avoided.
  - *Live:* **Basic Dodging** (and shield/weapon skills).
- **Weapon Mastery (per weapon class) → Grandmaster.** M multiplies precision and divides wasted motion. Two classes fused yield **Weapon Saint**, which applies to any weapon.
- **Unarmed Combat → Martial Art** + **Grappling → Submission** → **Body Weapon.**
  - *Live:* **Basic Hand to hand**.
- **Stealth → Silent Step** + **Presence Concealment → Vanish** → **Ghost.** M divides the noise, scent and visual signal the holder gives off. Detection range by enemies shrinks by √M. Contests directly with sensing skills.
  - *Live:* **Basic Sneaking**. Soft-ok contest framing vs Sense M.

---

## Movement

- **Climbing → Sheer Climb** + **Balance → Perfect Balance** → **Wall Walker.** Already worked out in performance appendix park.
  - *Live:* **Basic Climbing**.
- **Sprint → Burst** + **Endurance Running → Marathon** → **Swift Body.** Sprint M multiplies power, so top speed grows by √M. Marathon M multiplies sustainable distance.
  - *Live:* **Basic Sprint** / **Basic Running**.
- **Swimming → Aquatic** + **Breath Holding's Tier 2** → alternate route to Abyssal Body.
- **Jumping → Leap** + **Fall Control → Featherfall** → **Skywalk.** Leap M multiplies jump energy, so height grows by M. Featherfall divides effective landing speed.

---

## Extra senses

- **Night Vision → Darksight** + **Far Sight → Eagle Eye** → **True Sight.** Night Vision M multiplies light sensitivity. Far Sight multiplies visual resolution.
  - *Do not collide with True Runic Sight / Eyes of Mana naming.*
- **Keen Hearing → Acute Hearing** + **Keen Smell → Scent Tracking** → **Beast Senses.** M multiplies sensitivity, so range grows by √M. Scent Tracking reads trail age and lets the holder follow individuals.
- **Danger Sense → Intuition** + **Killing Intent Sense → Hostility Reading** → **Sixth Sense.** M multiplies warning time before an attack.
- **Spatial Awareness → 360° Perception.** Pairs with Echolocation as an alternate route to Resonance.
  - *Live Echo evolve stays Vibration Sense / Energy Sense (`Sound.md`).*

---

## Crafting and utility

- **Smithing → Master Smith** + **Forge Sight** → crafting quality ceiling.
  - *Live:* Forging / Smithing Mastery / Runecraft class path. Forge Sight is sensing-idea only.
- **Alchemy → Transmutation** + **Herbology → Plant Knowledge** → **Grand Alchemy.** M multiplies yield and potency and divides impurity.
- **Enchanting → Runecraft** + **Mana Weaving** → **Artifact Creation.** M multiplies enchantment capacity of an item.
  - *Live conflict:* enchanting ≠ runecrafting. Do not fuse into one skill.
- **Cooking → Gourmet** + **Butchery → Monster Dissection** → **Feast Craft.** Food that grants temporary buffs.
  - *Live:* **Cooking**; Food lore in `../Food/`.
- **First Aid → Surgery** + **Diagnosis** → **Healer's Hands.** M multiplies treatment speed and divides complication rate.
  - *Live:* Diagnosis is D-only and already medical-flavored; do not gate it behind First Aid.
- **Tailoring, Leatherworking, Carpentry, Masonry, Engineering** each follow the same quality-ceiling pattern.

---

## Social

- **Persuasion → Silver Tongue** + **Lie Detection → Truth Sense** → **Heart Reading.** Truth Sense M divides the smallest tell detectable.
- **Leadership → Command** + **Teaching → Mentorship** → **Inspire.** M multiplies morale effects and the learning speed of students.
- **Languages → Polyglot** + **Sound Mastery's mimicry** → native-level accent in any tongue.
  - *Sound Mastery is sensing-idea; live Sound Production is click/ping first.*

---

## Leverage (story priority, not law)

The ones with the most leverage in a LitRPG are **Reflexes**, **Stealth**, **Night Vision**, **Stamina Recovery**, **Fatigue Resistance**, **Disease Resistance** and **Mental Resistance**. These come up in almost every fight or scene. Crafting and social skills carry slower plot arcs instead.

When picking rewrite scenes for Roland, prefer leveraging skills he **already has** (Dodging, Sneaking, Sleep/Pain/Poison, Diagnosis, Marksmanship, Absorption) before inventing new named cards from this list.

---

## Cross-links

- Resist eight / four Fused: `ResistanceImmunitySystem.md`
- Sense / mana / sound / forge sight: `SensingManaSoundSystem.md`
- Roland Acid / Electricity / Blunt / Sharp: `RolandResistanceTracks.md`
- Live catalog: `SkillsDesign.md`
- Int / RT combat feel: `../Combat/SpeedVsIntellect.md`
- Parallel count: `../World/Science/Body/FocusCapacity.md`
