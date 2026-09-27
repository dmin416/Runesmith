# Rune Establishing Cost (Ideas)

Basis for setup mana going forward (not frozen; dials stay open). Companion to the rune redesign in `RuneSystem.md` (ranks, qualities, harmonics) and the energy baseline in `Energy.md` (activation cost, efficiency, heat). Activation, efficiency and heat rules stay in those files.

**The five ranks:** Lesser, Common, Greater, Grand, Legendary. **The five qualities:** Lowest, Low, Intermediate, High, Highest.

## Terms

| Term | Meaning |
|---|---|
| Setup | Mana the crafter pours once to establish the pathways in a material |
| Activation | Mana paid every cast. Fixed cost from the baseline. Scrolls add a filtration tax (canon, ../Ideas.md). |
| Charge | Mana that sits inside the rune after setup and can feed activation |

## Does the setup mana stay in the rune?

| Answer | Where it applies |
|---|---|
| No. It becomes structure and is gone. Activation is separate and paid every cast. | Default (P1) |
| Partly. A chosen share stays as charge in the Reservoir and feeds activation first. | P2 to P4 and P11 |
| Outside the rune. A socketed stone supplies part of the activation. | P5 |
| Not spent but locked. A standing reservation holds part of the pool while the rune runs. | P6 |
| Prepaid. The crafter pays activation too and the user pays only the start cost. | P9 and P10 |

## Recommended Default

**Setup = Base(rank) x C x S x M**

| Symbol | Meaning |
|---|---|
| Base | 1,000 for Lesser then 2,000 and 3,000 and 5,000 and 10,000 mana up the ranks |
| C | Complexity. Runs from 1 up to the next rank's base. More complex designs cost more. |
| S | Skill factor. 1 - 0.1 x skill level. Skilled crafters pay less. |
| M | Material factor. Harder metal costs more to set. |

**Quality does not enter the price.** Quality only says how poorly or well the machine was built. A poor car still needs the whole frame and wheels. A Lowest rune and a Highest rune of the same design cost the same to set.

Mana pools grow slowly in the story so setup climbs slowly too. Ceilings grow x100 per rank while base setup grows about x2.

| Rank | Base | Top complexity (C at k 1) | Stone terms | Adult pools | Solo pour at 20 mana per minute |
|---|---|---|---|---|---|
| Lesser | 1,000 | 2,000 (x2) | 1 cube (1000) | 0.5 | 50 min |
| Common | 2,000 | 3,000 (x1.5) | 0.93 marble (2145) | 1 | 1.7 h |
| Greater | 3,000 | 5,000 (x1.67) | 1.4 marbles | 1.5 | 2.5 h |
| Grand | 5,000 | 10,000 (x2) | 0.35 walnut (14,140) | 2.5 | 4.2 h |
| Legendary | 10,000 | 20,000 (x2, assumed) | 0.7 walnut | 5 | 8.3 h |

Figures show an unskilled crafter (S 1) with C 1 and copper.

- Rank is a price step. A Common Lowest rune costs twice a Lesser Highest rune for the same 1 kJ ceiling because it is a bigger frame built badly. A crafter buys the next rank only when able to build above the ceiling of the rank below.
- Setup against firing. An unskilled Lesser rune costs 10 full-power runs to set. Common costs 0.2 of a run. Greater and up cost a sliver of one run.

### Skill (reduces cost)

One crafting skill form per rank (canon: Basic Runecraft covers Lesser and evolved forms cover Common to Legendary). Each level cuts 10 percent with a cap of 90 percent at L9 (the shared ladder in ../Ideas.md). A form only discounts its own rank. A crafter without the form pays full base. The last 10 percent is the frame itself. The rest at L0 is scrap burned in botched pours (canon: failure burn rate).

| Skill level | S | Lesser (C 1) | Common (C 1) | Greater (C 1) | Lesser pour time |
|---|---|---|---|---|---|
| None or L0 | 1.0 | 1,000 | 2,000 | 3,000 | 50 min |
| L1 | 0.9 | 900 | 1,800 | 2,700 | 45 min |
| L3 | 0.7 | 700 | 1,400 | 2,100 | 35 min |
| L5 | 0.5 | 500 | 1,000 | 1,500 | 25 min |
| L7 | 0.3 | 300 | 600 | 900 | 15 min |
| L9 | 0.1 | 100 | 200 | 300 | 5 min |

A Lesser firecracker rune at L9 costs 100 mana or about one goblin leader stone (95).

### Complexity (raises cost)

**C = R^k** where R is the next rank's base divided by this rank's base (Lesser 2, Common 1.5, Greater 1.67, Grand 2, Legendary 2 assumed). k runs 0 to 1 inside a rank. C 1 is the plain reference design of the rank. At k 1 the cost reaches the plain base of the next rank. References: Lesser firecracker, Common elemental arrow, Greater single machine, Grand single engine, Legendary single hull.

| Driver | k added | Ranks |
|---|---|---|
| Shaped emitter (arrow point, edge, spread) | 0.20 | All |
| Hold or timing logic (sustained shield, delayed burst) | 0.20 | All |
| Reservoir storage loop | 0.20 | All |
| Extra branch off the main chain | 0.10 each | All |
| Recovery loop | 0.25 | Common and up |
| Resonator | 0.35 | Common and up |
| Locked overlap | 0.05 each | Common and up |
| Unlocked overlap (adds discord) | 0.02 each | Common and up |
| Extra subsystem | 0.10 each | Greater and up |

| Design | Drivers | k | C | Setup at L0 | Setup at L9 |
|---|---|---|---|---|---|
| Lesser firecracker | None | 0 | 1.00 | 1,000 | 100 |
| Lesser arrow or bolt | Emitter | 0.20 | 1.15 | 1,149 | 115 |
| Lesser shield | Emitter and hold | 0.40 | 1.32 | 1,320 | 132 |
| Lesser wind or mana blade | Emitter and hold and 1 branch | 0.50 | 1.41 | 1,414 | 141 |
| Lesser small explosion | Emitter and hold and Reservoir | 0.60 | 1.52 | 1,516 | 152 |
| Lesser fireworks | Emitter and hold and Reservoir and 3 branches | 0.90 | 1.87 | 1,866 | 187 |
| Common elemental arrow | None (reference) | 0 | 1.00 | 2,000 | 200 |
| Common weapon rune with Recovery | Recovery | 0.25 | 1.11 | 2,213 | 221 |
| Common fireball | Hold and Reservoir | 0.40 | 1.18 | 2,352 | 235 |
| Common resonant elemental | Recovery and Resonator and 2 locked overlaps | 0.70 | 1.33 | 2,656 | 266 |

### Material factor

M = sqrt(strain capacity / 140). Capital against running cost. Better metal costs more to set and sheds less waste every cast.

| Metal | M | Lesser firecracker at L0 | Waste per mana (1 - η) |
|---|---|---|---|
| Iron | 0.71 | 710 | 0.40 |
| Copper | 1.00 | 1,000 | 0.20 |
| Steel | 1.22 | 1,220 | 0.15 |
| Dark steel | 1.41 | 1,410 | 0.12 |
| Mana steel | 2.00 | 2,000 | 0.08 |
| Mythril | 2.83 | 2,830 | 0.05 |
| Adamantium | 4.00 | 4,000 | 0.02 |

Mythril costs 4 times iron to set and wastes one eighth as much per cast.

## Optional Modifiers

| ID | Idea | Rule | Effect |
|---|---|---|---|
| O1 | Fineness premium | +25 percent per size step down (sword to dagger to card) | Card costs 1.56 times. Matches the canon that compression cuts headroom. |
| O2 | Site density | Setup draws ambient like activation. Cost / sqrt(G). | Sealed 1.00. Indoors 0.82. Open air 0.58. Dense 0.41. Forges sit on mana-rich ground. |
| O3 | Pour rate and rush | 20 mana per minute. Pouring twice as fast adds 50 percent mana. | Time is a cost. Rushing burns extra mana. |
| O4 | Team pour | N crafters pour in parallel with 1 percent sync loss per extra crafter | 20 crafters run at 0.81 x 20 = about 16 times the solo speed. |

## Where the mana lives

| ID | Model | Setup mana | Activation | Notes |
|---|---|---|---|---|
| P1 | Spent structure (default) | Consumed into the pathways | Fully separate. Wielder or stone pays every cast. | Pathways are the whole value. Simplest bookkeeping. Everything below is optional on top. |
| P2 | Standing charge | Setup spent plus an optional fill of the Reservoir | Draws charge first then the wielder | Capacity 1 mana per mm³ (stone figure as placeholder). A sword Reservoir of 500 mm³ holds 500 mana or 10 casts at 50. Storing costs 1.31 mana per mana (body 0.90 x intake 0.85). |
| P3 | Trickle refill | P2 plus slow ambient intake refills the charge | As P2 | Rate = intake area x local density. Idle weapons top up on mana-rich ground. |
| P4 | Leak | P2 with charge decay of 2 percent per day | As P2 | 30 days leaves 55 percent. Prevents hoarding. Prepaid weapons need topping. |
| P5 | Stone slot | Setup plus 10 percent for the socket | Stone supplies 40 percent (canon) so a 50 mana cast costs the wielder 30 | Stone capacity is area-based and quality does not raise it (../Science/ManaStones.md). |
| P6 | Standing reservation | Setup spent | Passive runes lock part of the pool while running. Example: 10 percent of the pool per piece (canon: 100 on a 1000 pool). | Upkeep is a locked pool with no drain. An adult pool of 2000 locks 200 per piece. |
| P7 | Maker bond | Setup leaves the maker's signature in the pattern | Maker pays 10 percent less. Others pay full. | Rewards keeping a signature weapon. Sale changes the bond. |
| P8 | Material-paid setup | Ink or paste made from stone dust or monster blood pays part of setup at 70 percent recovery | Separate | A pea stone (180) yields 126 mana which covers a Lesser firecracker rune at L9 (100). A cube (1000) yields 700. |
| P9 | Prepaid scroll | Setup plus the activation charge poured by the crafter | User pays only the start cost | Total = setup + 1.31 x activation. Common Fire Arrow at L5: 1,000 + 131 = 1,131 mana. Differs from the canon default where the user pays through filtration. |
| P10 | Prepaid filtration | Crafter pays the filtration tax at craft time | User pays pattern cost only | Non-mage scrolls get cheaper for the user. Mastery still discounts the pattern share. Differs from canon where the safety tax is real user mana. |
| P11 | Overrun charge (craft-time empower) | Extra charge stored in the Reservoir | Prepays overrun up to about 5 times the ceiling | 1.31 mana per stored mana. Break risk rises with the charge (canon: Empower and Overload). |

A hybrid dial f (share of setup that stays as charge) spans P1 (f 0) to full battery (f 1). Suggested options: 0, 0.2 and 0.5.

## Changing a rune after it is set

Costs use the crafter's current setup (C and S and M applied).

| ID | Operation | Cost | Notes |
|---|---|---|---|
| C1 | Mend | 0.5 x setup x fraction broken | Restores pathways only. A Lesser firecracker at L5 (500) with 20 percent broken costs 50. Canon repair about 3 LS. |
| C2 | Duplicate | 50 percent of setup | Lesser firecracker at L5 costs 250 (canon: Lesser Rune Duplication). |
| C3 | Quality upgrade | 25 percent of setup per step | Lowest to Highest is 100 percent because the badly built parts are rebuilt. Chance-based (canon: overuse risks damage). |
| C4 | Rank up | Base difference x C x S of the new rank | Lesser to Common costs 1,000 at L0 or 100 at Common L9. The old frame is reused. |
| C5 | Retune | 25 percent of setup | Moves the rune to a new natural tone. |
| C6 | Compress | Fineness premium difference (O1) plus 25 percent | Re-sets into a smaller form. Headroom drops. |
| C7 | Empower | No setup. Charge only (P11). | Break risk. |
| C8 | Erase | No refund | Stored charge returns at 0.90 (body efficiency). |

Upgrade payback on the steel sword attack: Intermediate to Highest saves 75 mana per cast (125 to 50) and costs two steps or 50 percent of setup. A Lesser firecracker rune at L0 pays back 500 in 6.7 casts. At L9 it pays back 50 in 0.7 casts.

## Worked cases

| Case | Setup at L0 | Setup at L5 | Setup at L9 | Solo pour at L9 |
|---|---|---|---|---|
| Copper paddle firecracker (Lesser, C 1.00) | 1,000 | 500 | 100 | 5 min |
| Steel sword mana blade (Lesser, C 1.41, M 1.22) | 1,732 | 866 | 173 | 9 min |
| Card-size arrow (Lesser, C 1.15, O1 1.56, copper) | 1,795 | 897 | 179 | 9 min |
| Common Fire Arrow scroll (Common, C 1.00) | 2,000 | 1,000 | 200 | 10 min |
| Common fireball (C 1.18) | 2,352 | 1,176 | 235 | 12 min |
| Siege engine at 125 kJ (Greater, C 1.17, copper) | 3,497 | 1,748 | 350 | 18 min |
| Steam locomotive 10 min run (Grand, C 1.52) | 7,579 | 3,789 | 758 | 38 min |
| Airship 8 h leg (Legendary, C 1.87) | 18,661 | 9,330 | 1,866 | 93 min |

## Considerations

- Early tension. A Lesser rune costs 900 at L1 or 0.45 of an adult pool (canon: running out of mana while crafting basic runes is a main early tension). At 20 mana per minute that is 45 min which matches the canon Fire Orb runic scroll at about 45 min if that scroll sits at C 1.
- Scroll day. A Common Fire Arrow costs 2,000 at L0. Canon 5 to 6 a day costs 5,500 at L5 (2.75 adult pools) against a daily regen of 2.67 pools (9 h empty to full). That matches the canon L5 grind (Ch 22) and drains hard. The crafter finishes at zero and takes the canon headache and next-day regen debuff. At L9 the same day costs 1,100 or 0.55 of a pool.
- Quality is free at build. Every crafter builds the best quality reachable. Skill and comprehension gate the reach and mana does not.
- Skill drives price. An L9 crafter sets the same rune for one ninth of an L1 crafter's mana (100 against 900 at Lesser) so masters undercut novices by nine times before wages. Scroll price can track setup mana (canon: runic Fire Arrow costs 6 to 7 times a regular scroll).
- Setup is small next to a run. An airship setup costs 9 adult pools at L0 (0.9 pool at L9) against a 95 GJ run. Stone banks and ambient intake carry activation (rune file, Power source) and setup stays a crafter's job. Team pour (O4) only buys speed.
- Setup adds no heat and no strain. Wear stays as in the baseline.
- Mastery discounts activation only (canon), for both items and scrolls. It never touches setup cost.
- Setup cost has exactly one discount channel per medium, never two stacked together. Items: **Runecraft**'s skill-level S factor only. Scrolls: the **Runic Mana Scribe** class card's −3%/class-level term only (self-bounded at −75%, T1 caps at L25) — **Basic Rune Scribing** does not also discount setup cost; its skill levels grant a different, non-cost bonus (`Progression/Skills.md`).

## Open Dials

- Base progression of 1,000 and 2,000 and 3,000 and 5,000 and 10,000. Legendary top complexity assumes x2.
- The adult pool of 2000 is a proposal. Every pool share above moves with it.
- Complexity driver sizes. Skill ladder of 10 percent per level.
- Pour rate of 20 mana per minute (fits the canon Fire Orb time at L1).
- Charging efficiency (0.85 intake) and leak rate (2 percent per day) and stone slot socket cost (10 percent).
- Fineness premium (25 percent per step) and site exponent (0.5) and team sync loss (1 percent per extra crafter).
- Quality upgrade at 25 percent per step and rank-up reuse of the old frame.
- Metal Reservoir capacity. Canon gives stone only (1 mana per mm³) so metals use it as a placeholder.
- Scroll media factor. Paper and parchment have no M yet so scrolls use M 1.
- Whether prepaid scrolls (P9 and P10) belong in canon or stay a premium variant.
