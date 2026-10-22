# Superhuman Cancer Risk: A Biological Reference

> Earth invent loot / fiction biology reference. Cancer risk by power type (healing, strength, speed, radiation, shapeshifting, etc.), Peto's paradox, multistage math, detection/treatment complications, game CRS option. Not Caldris law. Tissue-loss and Recovery speed: `TissueLossRecovery.md`. Soft-tissue heal cycles: `BluntTraumaHealing.md`, `BurnsHealing.md`, `PiercingSlicingWounds.md`. Cellular control / regen multiples: `CellularControl.md`. Radiation biology: `../../Space/Radiation/BiologicalEffects.md`, `../../Space/Radiation/RobustHeatHuman.md`. Recovery skills: `../../../Progression/SkillsDesign.md`. Nav: `Index.md`.

---

## 1. Core Principle

Cancer is a failure of cellular control. A cell picks up a series of mutations (usually 3 to 7 "driver" mutations) that disable its brakes (tumor suppressors such as TP53, RB1, APC) and jam its accelerators (oncogenes such as KRAS, MYC, EGFR). The cell then divides without limit, evades the immune system, recruits blood vessels and eventually invades other tissue.

Every superpower can be evaluated with four questions:

1. **Does it increase the number of cell divisions?** More divisions mean more copying errors.
2. **Does it increase the mutation rate per division?** Radiation, reactive oxygen species, mutagenic origins.
3. **Does it improve DNA repair?** Fewer errors survive into daughter cells.
4. **Does it improve immune surveillance or cell suicide (apoptosis)?** Damaged cells get removed before they become tumors.

Questions 1 and 2 push risk up. Questions 3 and 4 push risk down. The net balance decides the outcome.

## 2. The Math That Makes This Dangerous

### Armitage-Doll Multistage Model
Cancer incidence rises roughly with the mutation rate raised to the power of the number of required mutations:

- Incidence ∝ (mutation rate)^k × (age)^(k-1)
- k is typically 4 to 7 depending on cancer type

**Consequence:** Doubling the mutation rate does not double cancer risk. For a cancer needing 6 hits it multiplies risk by about 2^6 = 64. A tenfold mutation increase in a 6-hit cancer gives about a million-fold increase in theory. Real numbers get capped by death from the first tumor. The reverse also holds: halving the mutation rate cuts risk to about 1/64.

This is why small biological tweaks to a superhuman produce extreme outcomes in either direction.

### Stem Cell Division Correlation
Tomasetti and Vogelstein (2015, 2017) showed lifetime cancer risk across tissues tracks closely with the total number of stem cell divisions in that tissue. Their 2017 analysis attributed about two thirds of cancer-driving mutations to random replication errors rather than environment or heredity. A power that multiplies stem cell divisions multiplies the dominant source of cancer.

### Baseline Human Lifetime Risk
- Roughly 40% of men and 39% of women in the US develop cancer at some point.
- Roughly 1 in 5 people die of it.
- Any superhuman multiplier applies to this baseline.

### Height and Cell Number
Taller people have more cells. Large studies (Million Women Study, Green et al. 2011) found about a 16% rise in cancer risk per 10 cm of height. A superhuman at 2.5 m tall or with dense hyperplastic tissue starts at elevated risk before any other factor.

## 3. Peto's Paradox: The Central Problem for Superhumans

A blue whale has about 1000 times more cells than a human and lives about as long. By cell count alone whales should almost all die of cancer. They don't. Across species, cancer rates barely scale with body size or lifespan.

The answer is evolution. Large long-lived animals spent millions of years acquiring extra tumor suppression. Examples:

| Species | Cancer Defense |
|---|---|
| African elephant | About 20 copies of TP53 (humans have 1). Damaged cells self-destruct readily. Also reactivated LIF6 gene, which kills cells with DNA damage. |
| Bowhead whale | Lives 200+ years. Enhanced DNA repair, high levels of the repair-boosting protein CIRBP, duplications of repair genes such as PCNA and ERCC1. |
| Naked mole rat | High-molecular-mass hyaluronan around cells prevents crowding growth. Extra-sensitive contact inhibition through p16. Near-zero cancer rates. |
| Blind mole rat | Cells that start overgrowing release interferon-beta and trigger mass cell death in the cluster. |
| Bats | Long-lived for their size. Tight control of inflammation and strong DNA damage responses. |
| Axolotl | Regenerates whole limbs, spinal cord and parts of the heart with unusually low tumor rates. |
| Planarian flatworm | Fully regenerates from fragments. Uses tight stem cell control and constant tissue turnover. |
| Hydra | Biologically near-immortal. Constant stem cell renewal with very low tumor formation. |

**The superhuman problem:** A person who gains powers in a single event (accident, serum, mutation, magic) receives the capability without the co-evolved suppression. Unless the origin includes repair and surveillance upgrades, every power that adds cells, divisions or metabolic stress adds raw cancer risk with no counterbalance.

A born mutant whose lineage carried powers for generations could plausibly have evolved suppression. A lab-made or accident-made superhuman almost certainly has not.

## 4. Power-by-Power Breakdown

### 4.1 Healing Factor / Regeneration
**Risk direction: Strongly up (unless paired with repair)**

- Every wound closed means millions to billions of new cells. A character healing a gunshot wound in minutes compresses weeks of division into minutes.
- Fast division leaves less time for DNA proofreading checkpoints. Speed itself raises errors per division.
- Chronic wounds in humans develop cancer. **Marjolin's ulcer** is an aggressive squamous cell carcinoma arising in old burn scars and chronic wounds. Chronic liver injury leads to cirrhosis and then hepatocellular carcinoma.
- Pathologist Harold Dvorak (1986) described tumors as "wounds that do not heal." Tumors hijack the same growth signals used in healing. A permanently active healing program is a permanently active tumor support program.
- Regeneration requires **telomerase** to keep cells dividing past the Hayflick limit (about 50 divisions). About 85 to 90% of cancers reactivate telomerase. A healer with always-on telomerase has removed one of the body's biggest cancer barriers.
- **Tumor recognition problem:** A tumor is made of the body's own cells. A healing factor has no reason to classify it as damage. It may supply it with blood vessels and growth signals.
- **Treatment problem:** Surgery removes the tumor. The healing factor regrows the surrounding tissue. Any remaining cancer cells regrow with it. Chemotherapy damage gets repaired, including in the tumor.

**Possible saving grace:** If the healing factor works by restoring a template (resetting tissue to a stored "correct" state) rather than by dividing cells, mutations get erased every time healing triggers. This version is close to cancer-immune. The writer decides which mechanism applies.

**Estimate:**
- Division-based healer with no repair upgrade: 5x to 50x baseline. Cancer likely by age 40 to 50 with heavy combat use.
- Template-reset healer: near zero.

### 4.2 Super Strength (Muscle-Based)
**Risk direction: Up**

- Hypertrophy and hyperplasia mean more cells.
- Driven by growth hormone, IGF-1, testosterone and mTOR signaling. All four drive cancer growth.
- **Acromegaly** (excess growth hormone) roughly doubles colon cancer risk and raises thyroid cancer risk.
- **Laron syndrome** (growth hormone receptor defect) is the reverse case. An Ecuadorian cohort studied over decades had almost no cancer. Growth signaling is a major dial.
- Anabolic steroid abusers show liver tumors (hepatic adenomas, hepatocellular carcinoma) and possibly testicular and prostate effects.
- Bone density increase means more bone remodeling and higher osteosarcoma pressure.

**Estimate:** 1.5x to 4x baseline depending on how much the strength relies on growth signaling. Strength from denser protein structure or non-biological force generation carries little added risk.

### 4.3 Super Speed / Hypermetabolism
**Risk direction: Up**

- Running at extreme speed requires enormous ATP production.
- Mitochondria leak reactive oxygen species (ROS) during energy production. ROS oxidize DNA (the 8-oxoguanine lesion is a classic mutation source).
- Metabolism scaled 10x to 100x produces proportionally more oxidative damage unless antioxidant systems scale with it.
- Massive caloric intake required. High insulin and IGF-1 exposure from constant eating raises risk further.
- Faster cell turnover in gut lining (to process food volume) means more intestinal divisions. Colorectal cancer becomes a top concern.
- If the character's whole biology runs faster, their effective "age" for cancer purposes accumulates faster than calendar age.

**Estimate:** 2x to 20x baseline. Colon, liver and blood cancers lead.

### 4.4 Radiation-Origin Powers
**Risk direction: Strongly up**

- The origin event is a mutagen. Any person surviving a dose large enough to rewrite their biology received far more radiation than needed to seed cancer.
- Standard estimate: about 5% added lifetime cancer mortality per sievert of whole-body exposure.
- Doses above 4 to 5 sieverts are typically fatal from acute radiation syndrome. A fictional survivor of higher doses has massive scattered DNA damage in every surviving cell.
- Leukemia appears first (2 to 10 years after exposure in atomic bomb survivors). Solid tumors follow over decades.
- If the character remains radioactive or emits radiation, their own tissue receives ongoing exposure.

**Estimate:** 10x to near-certain cancer within 10 to 20 years unless the transformation included radiation resistance.

**Radiation resistance precedents:**
- *Deinococcus radiodurans* bacteria survive about 5000 Gy by reassembling shattered chromosomes with highly efficient repair and manganese-based protection of repair proteins.
- Tardigrades produce **Dsup** (damage suppressor) protein, which binds DNA and shields it. Human cells engineered with Dsup showed about 40% less X-ray damage in lab tests.

A radiation-powered character with Deinococcus-style repair could be the most cancer-resistant superhuman of all.

### 4.5 Genetic Mutation Powers (Born Mutants)
**Risk direction: Variable**

- If the power gene arose by random mutation, the same mechanism (unstable DNA, faulty repair) may affect other genes. Real cancer predisposition syndromes (Lynch syndrome, Li-Fraumeni, BRCA) show how one bad repair gene raises lifetime risk to 50 to 90%.
- If the power trait evolved over generations, suppression may have evolved too (see Peto's paradox).
- A "power gene" that keeps itself active by constantly altering DNA (a mutator mechanism) is a cancer generator.

**Estimate:** 0.5x to 10x baseline depending on lineage age and mechanism.

### 4.6 Invulnerability / Durable Skin
**Risk direction: Down for external causes, unchanged for internal**

- Blocks UV (skin cancer), many carcinogens and external radiation.
- Does nothing about replication errors, which drive roughly two thirds of mutations.
- **Treatment problem:** Surgeons cannot cut. Biopsies cannot be taken. Needles cannot deliver chemotherapy. Imaging may fail if tissue is unusually dense. Internal tumors grow undetected and untreatable.

**Estimate:** 0.6x to 1x baseline. Mortality from cancer is higher than incidence suggests because treatment is impossible.

### 4.7 Solar-Powered / Energy-Absorbing Biology
**Risk direction: Depends on mechanism**

- If cells absorb UV and ionizing radiation as fuel, the energy must not reach DNA. Requires biochemistry that intercepts photons before they cause damage.
- If absorption is imperfect, constant energy intake means constant DNA damage.
- If the energy also powers repair, the character could repair faster than damage accumulates.

**Estimate:** Near zero if the system is "designed" coherently. Very high if it is a crude absorption.

### 4.8 Shapeshifting
**Risk direction: Very strongly up**

- Changing shape requires remodeling or replacing huge amounts of tissue. Every transformation is a regeneration event.
- Cells must lose and regain identity (dedifferentiation). Dedifferentiation is a hallmark of aggressive cancers.
- Mass rearrangement of tissue risks cells ending up in the wrong place, the definition of metastasis.
- Potential upside: A shapeshifter who consciously controls cells could find and eliminate tumors.

**Estimate:** 10x to 100x baseline with no control mechanism. Near zero with conscious cellular control.

### 4.9 Size Changing (Growing)
**Risk direction: Up if cells multiply, neutral if cells enlarge**

- Growing by adding cells: Each growth cycle is massive division. A 20 m giant has about 1000x more cells than baseline.
- Growing by enlarging existing cells or adding non-living mass: Little cancer effect.
- Repeated growth and shrinkage cycles mean repeated destruction and regrowth of tissue.

### 4.10 Psychic and Brain-Based Powers
**Risk direction: Mild up (speculative)**

- Brain hypermetabolism produces more oxidative stress.
- Neurons rarely divide, so neuron-based tumors are rare. Glial cells divide and give rise to gliomas. Increased glial support for an overactive brain could raise glioma risk.
- Most psychic power systems are non-biological in fiction, which leaves risk at baseline.

### 4.11 Elemental Projection (Fire, Lightning, Ice)
**Risk direction: Localized up**

- Heat near tissue causes repeated burn injury and repair (Marjolin-type risk at emission sites such as hands).
- Electrical discharge causes tissue damage and repeated repair cycles.
- Cold causes freeze-thaw cell death and regrowth.
- If emission sites are protected, risk stays near baseline.

### 4.12 Duplication / Cloning
**Risk direction: Up per body**

- Each duplicate body built by cell division carries fresh replication errors.
- If duplicates merge back and share memory and tissue, mutations from every body pool into one.

### 4.13 Cybernetic Enhancement
**Risk direction: Mild up**

- Foreign bodies in tissue cause chronic inflammation. Chronic inflammation drives cancer.
- Real precedents: breast implant associated anaplastic large cell lymphoma (BIA-ALCL). Rare sarcomas around metal implants.
- Power sources near tissue (radioisotope batteries) add radiation exposure.
- Immunosuppressants used to prevent rejection reduce cancer surveillance. Organ transplant recipients on immunosuppression have 2x to 4x overall cancer risk and far higher skin cancer risk.

**Estimate:** 1.2x to 4x baseline. Much higher if immunosuppressed.

### 4.14 Enhanced Immune System
**Risk direction: Down**

- The immune system already kills many early cancer cells (immunosurveillance). Cancer only succeeds after evading it.
- Enhanced natural killer cells and T cells catch tumors earlier.
- Caveat: Overactive immunity causes chronic inflammation and autoimmune damage. Chronic inflammation raises cancer risk in tissues such as the colon (ulcerative colitis) and liver.

**Estimate:** 0.2x to 0.7x baseline if regulated. Higher than baseline if it causes chronic inflammation.

### 4.15 Enhanced DNA Repair / Elephant-Style Suppression
**Risk direction: Strongly down**

- Multiple TP53 copies: cells with damage self-destruct.
- Faster, more accurate repair enzymes.
- Better checkpoint control during division.
- Due to the multistage math, even a modest repair improvement drops risk enormously.

**Estimate:** 0.01x to 0.3x baseline.

**Trade-off:** Over-aggressive apoptosis kills healthy cells too. Possible costs: faster aging of tissues, poor wound healing, infertility, low stem cell reserves. Mouse experiments with hyperactive p53 produced cancer-resistant mice that aged prematurely. Cancer resistance and fast healing pull in opposite directions.

### 4.16 Magic-Based Powers
**Risk direction: Setting-dependent**

- If magic draws on the user's biology (mana metabolism, life force), it behaves like hypermetabolism.
- If magic restores the body to a pattern, it erases mutations.
- If magic is external energy channeled through the body, it behaves like radiation unless channeled cleanly.
- A setting with magical healing creates a question: does healing magic cure cancer or feed it? Both answers produce interesting world consequences.

## 5. Summary Risk Table

| Power Type | Relative Lifetime Risk | Main Cancers |
|---|---|---|
| Division-based healing factor | 5x to 50x | Skin, liver, blood, sarcoma at frequent injury sites |
| Template-reset healing factor | ~0x | None meaningful |
| Muscle-based super strength | 1.5x to 4x | Colon, thyroid, liver, prostate, bone |
| Super speed / hypermetabolism | 2x to 20x | Colon, liver, blood |
| Radiation origin, no resistance | 10x to near-certain | Leukemia first, solid tumors later |
| Radiation origin with resistance | 0.05x to 0.5x | Rare |
| Born mutant, new mutation | 2x to 10x | Varies |
| Born mutant, old lineage | 0.5x to 1x | Varies |
| Invulnerable skin | 0.6x to 1x (high mortality) | Internal organs |
| Shapeshifter, no control | 10x to 100x | Any tissue, early metastasis |
| Shapeshifter, cell control | ~0x | None |
| Size growth by cell addition | Scales with cell count | Any |
| Psychic | ~1x to 1.5x | Glioma |
| Elemental projection | 1x to 3x | Skin and sarcoma at emission sites |
| Cybernetic | 1.2x to 4x | Lymphoma, sarcoma near implants, skin if immunosuppressed |
| Enhanced immunity | 0.2x to 0.7x | Inflammation-linked if overactive |
| Enhanced DNA repair | 0.01x to 0.3x | Rare |

Multipliers are estimates for fiction and game design built from the biology above. Stacked powers combine: a speedster with a division-based healing factor compounds both risks.

## 6. Detection and Treatment Complications

### Detection
- Healing factors mask early symptoms such as bleeding, pain and weight loss.
- Enhanced endurance hides fatigue, a common early symptom.
- Dense or invulnerable tissue blocks imaging and biopsy.
- Non-standard biology makes blood markers meaningless. A superhuman's normal PSA or CEA levels may not match human reference ranges.

### Treatment
| Treatment | Complication |
|---|---|
| Surgery | Invulnerable skin blocks it. Healing factor regrows tumor margins. |
| Chemotherapy | Enhanced liver clears drugs before they act. Healing factor repairs tumor damage. Dosing tables are useless. |
| Radiation therapy | Radiation-resistant characters resist therapy. Radiation-origin characters may gain power or become unstable. |
| Immunotherapy | Works best on enhanced-immunity characters. May trigger overactive immune storms. |
| Targeted therapy | Superhuman tumors may carry unique mutations no existing drug targets. |

### Possible Superhuman-Specific Solutions
- Temporarily suppressing the healing factor (power dampener, specific drug) during treatment.
- Using a healer's own regeneration after aggressive treatment that would kill a normal patient (lethal-dose chemotherapy followed by regeneration).
- A telepath or biokinetic identifying individual cancer cells.
- Organ replacement by a regenerator: removing a cancerous organ and growing a fresh one.

## 7. Unusual Scenarios

### Cancer as Power Source
A tumor with unlimited growth could be the origin of regeneration. Cancer cells already have the traits a healer wants: unlimited division, telomerase activity, resistance to death, self-made blood supply. A character whose power is a controlled cancer walks a permanent line between superhuman and terminal.

### Transmissible Superhuman Cancer
Real transmissible cancers exist:
- **Tasmanian devil facial tumor disease** spreads through bites.
- **Canine transmissible venereal tumor** has spread among dogs for about 11,000 years. It is the oldest known continuous cell lineage.

A superhuman cancer carrying the power genes could spread through blood or bites and grant warped partial powers to the host before killing them.

### Immortal Cell Lines
HeLa cells (taken from Henrietta Lacks in 1951) still divide in labs worldwide. Samples from a deceased superhuman's tumor could persist indefinitely and become the basis for serums, cloning or power transfer.

### Power Loss from Treatment
If powers depend on the same pathways as cancer (telomerase, growth signaling, suppressed apoptosis), shutting down those pathways to cure cancer may also strip the powers. A character may have to choose between powers and survival.

### Long-Lived Characters
A superhuman living 300 years with human-level suppression faces cancer risk scaling with age raised to the 4th to 6th power. By age 200 cancer becomes almost unavoidable without bowhead-style repair. Long-lived species in fiction need explicit cancer defenses to stay plausible.

## 8. Simple Game Mechanic Option

**Cancer Risk Score (CRS):**
- Start at 0.
- Division-based healing: +3
- Muscle growth strength: +1
- Hypermetabolism: +2
- Radiation origin: +4
- Shapeshifting without control: +4
- Cybernetics: +1 (+2 more if immunosuppressed)
- Enhanced DNA repair: -4
- Enhanced immunity: -2
- Template-reset healing: set to -5 regardless of other factors

**Annual check:** Roll d100 each in-game year after age 30. Cancer develops on a roll at or below (CRS × 2) + (age ÷ 10). A negative CRS means no check is needed.

**Heavy power use:** Each major regeneration event (limb regrowth, near-death recovery) adds +1 to that year's threshold.

## 9. Key Takeaways

1. Powers that add cells, divisions or metabolic load raise cancer risk. Powers that add repair or immunity lower it.
2. Multistage cancer math makes small biological changes produce massive risk swings.
3. Sudden-origin superhumans lack the evolved suppression large long-lived animals have.
4. Healing factors are the highest-risk common power unless they work by template reset.
5. Fast healing and cancer resistance biologically oppose each other. Getting both requires a deliberate mechanism.
6. Treatment becomes extremely difficult for durable, regenerating or non-standard biology.
7. Nature already provides working cancer defenses (elephant TP53, whale repair, mole rat hyaluronan, tardigrade Dsup, Deinococcus repair) that make plausible superhuman designs.
