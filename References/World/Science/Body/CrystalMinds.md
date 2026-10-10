# Human Brains, Language Models and Crystal Minds

Hub: `../Science.md`. Mental capacity (N men): `FocusCapacity.md`. Vision processing cost tables: `Vision360.md`. Self-improvement ignition, multi-state digits and architecture throughput: `CrystalComputerMath.md`. Octonary diamond substrate, heat walls and programming: `OctonaryCrystalBrain.md`. Motor recall vs practice: `MindBodySkill.md`. Nav: `Index.md`.

**Status:** holding file. **Owns** Earth brain / LLM anchors (Part 1) and story crystal rules (copies, segments, calculator/assistant paths). FocusCapacity and Vision360 cite Part 1; they do not redefine neuron / watt / bits/s here. Architecture comparison → `CrystalComputerMath.md`. Substrate deep dive → `OctonaryCrystalBrain.md`.

---

# Part 1: Human Intelligence vs Language Model Processing Power

## Human brain

- **Neurons:** about 86 billion
- **Synapses:** roughly 100 trillion (estimates range from 10^14 to 10^15)
- **Firing speed:** slow. Average rates are 0.1 to 10 signals per second. Most neurons peak near 200 Hz. Fast-spiking interneurons exceed 500 Hz in bursts.
- **Equivalent compute:** Joe Carlsmith's 2020 Open Philanthropy analysis puts the best estimate near 10^15 operations per second. The plausible range is 10^13 to 10^17.
- **Power:** about 20 watts
- **Storage:** Bartol et al. (2015) estimate about 4.7 bits per synapse, measured on rat hippocampal synapses and extrapolated. Across 10^14 to 10^15 synapses that comes to roughly 60 to 600 terabytes. The popular "1 petabyte" figure is a rounded-up number from the Salk Institute press release.
- **Conscious throughput:** Zheng and Meister (2024) estimate human behavior runs on the order of 10 bits per second. This is an order-of-magnitude figure across tasks. Their own comparison places speech near 40 bits per second.
- **Language exposure:** children reach fluency by age 5 to 6 on about 10 to 50 million words. Adults have heard and read roughly 100 to 500 million.

## Large language models

- **Parameters:** these are the loose analog of synapses. Open models run from 1 billion to about 1 trillion (DeepSeek V3 at 671 billion, Kimi K2 at about 1 trillion). Frontier closed models are undisclosed and estimated in the low trillions. Many are mixture-of-experts designs, where only a fraction of the parameters activate for each token.
- **Training data:** 15 to 36 trillion tokens. Meta's Llama 3 used 15 trillion. Qwen3 used 36 trillion.
- **Training compute:** GPT-4 is estimated at about 2×10^25 FLOP. Recent frontier runs reach 10^26 and beyond.
- **Inference cost:** about 2 FLOP per active parameter per token, which comes to 10^11 to 10^12 FLOP per token for a large model.
- **Hardware:** one Nvidia H100 delivers about 10^15 FLOP/s at 16-bit precision while drawing about 700 W. Training clusters link 10,000 to 100,000+ GPUs and draw 10 to 150+ megawatts.

## Side by side

| Measure | Human | Large LLM | Scale difference |
|---|---|---|---|
| Connections | ~10^14 synapses | ~10^12 parameters | Brain ~100x more |
| Raw compute | ~10^15 ops/s | 1 GPU ~10^15 FLOP/s; cluster ~10^20 | 1 GPU ≈ 1 brain; 1 cluster ≈ 100,000 brains |
| Energy per operation | ~2×10^-14 J (at 10^15 ops/s) | ~7×10^-13 J (H100, 16-bit, chip only) | Brain ~35x more efficient at the central estimate. Across Carlsmith's range: GPU 3x more efficient to brain 3,500x more efficient |
| Text learned from | ~10^7 words to fluency; ~10^8 to 10^9 by adulthood | 1.5 to 3.6×10^13 tokens | LLM sees 15,000 to 3,600,000x more text |
| Total learning compute | ~10^24 ops over 30 years | 10^25 to 10^26 FLOP | One training run ≈ 10 to 100 human lifetimes |
| Output rate | ~150 words/min (2.5 words/s) speaking | 50 to 200 tokens/s per stream (~0.75 words per token), thousands of streams at once | One stream ≈ 15 to 60x faster than speech |
| Information rate | ~39 bits/s in speech (Coupé et al. 2019) | ~2 to 3 bits per token of information content, ~100 to 600 bits/s per stream | ~3 to 15x per stream |

## What the scale means

### Where the brain leads

- **Connections:** it has about two orders of magnitude more of them.
- **Energy:** it runs on the power of a dim light bulb. The exact efficiency gap depends on which compute estimate is used. FP8 precision and Blackwell-generation chips narrow it further.
- **Sample efficiency in text:** a child reaches fluency on roughly 1/300,000th to 1/3,600,000th of the text a model trains on. The comparison counts text only. A child also takes in a continuous stream of visual, auditory and social data. Yann LeCun estimates a 4-year-old's visual input alone is comparable in raw bytes to an LLM training set. Evolution supplies built-in priors on top of that.
- **Continuous learning:** the brain keeps learning throughout life. Model weights freeze after training.

### Where models lead

- **Breadth of text absorbed:** far beyond what any person could read.
- **Speed:** raw output is much faster.
- **Copies:** a model can run thousands of parallel instances.
- **Scaling:** capacity grows by adding hardware rather than through biology.

### Why the FLOP comparison is approximate

- **Different operations:** a synaptic event is an analog, noisy, chemically modulated signal, not a precise floating-point multiply.
- **Different structure:** the brain is massively recurrent, sparse, multimodal and embodied. A transformer processes tokens in a feed-forward pass per step.

The numbers set the order of magnitude, not an exact exchange rate. By that measure, a single modern GPU sits in the same compute range as one human brain. A frontier training run spends more compute than a human uses learning across an entire lifetime.

---

# Part 2: Turning a Crystal Brain into a Calculator or Language Assistant

Fast-firing crystal neurons supply raw speed. A working assistant also needs six other parts: adjustable connections, a nonlinear firing rule, an architecture, input encoding, output decoding and a way to set the connection strengths.

## Core components

- **Neuron:** a crystal that responds nonlinearly to its summed input. A firing threshold is the simplest form. Any nonlinearity works. Without one, any number of stacked layers collapses mathematically into a single linear transformation, so depth adds nothing.
- **Synapse:** a tunable link between crystals. Its strength (light transmission, conductivity, resonance coupling) is the "weight." Every capability lives in these weights.
- **Signed weights:** links must be either excitatory (pushing the target toward firing) or inhibitory (pushing it away). A network with only positive links cannot represent most functions.
- **Weight precision:**
  - Running imprinted weights: 4 to 8 bits per synapse, meaning 16 to 256 distinguishable strength levels that hold steady over time
  - Gradient training inside the crystal: 16 to 32 bits, since small gradient updates accumulate below the resolution of 8-bit steps
  - Local Hebbian learning inside the crystal: low precision works with stochastic rounding. Each small update has a proportional chance of stepping the weight one full level, so changes accumulate correctly on average.
- **Signal type:** use either rate coding (firing frequency carries the value) or timing coding (the moment of firing carries the value). Rate coding is simpler. Timing coding is faster and more efficient.

## Path 1: Calculator

This path needs no learning.

1. **Wire neurons as logic gates.** A threshold neuron with two inputs becomes AND (threshold 2), OR (threshold 1) or NOT (an inhibitory input against a constant firing source). This is the McCulloch-Pitts result from 1943.
2. **Combine gates into circuits.** Gates form adders, multipliers, comparators and registers. A loop of neurons that re-excite each other holds a bit as memory.
3. **Add a clock.** A crystal that pulses at a fixed rate keeps every stage in step.
4. **Add input and output.** Input is pressure plates, light or touch mapped to digit neurons. Output is crystals that glow in a digit pattern.

A few hundred to a few thousand neurons gives a basic four-function calculator. Thousands to tens of thousands gives a programmable computer; the 6502 processor ran on about 3,500 transistors. Millions of neurons buys memory capacity, not programmability.

## Path 2: Language model assistant

### Architecture

- **Embedding layer:** every word piece (token) maps to a pattern of activity across a few thousand input neurons.
- **Processing layers:** dozens of stacked layers, each doing matrix multiplication (signals passing through weighted synapses) followed by a nonlinearity.
- **Context handling:** three options.
  - **Attention (transformer style):** each word compares itself against every earlier word. This is powerful but hard to build in spiking hardware, since it needs dynamic, multiplicative interactions between signals.
  - **Recurrent state (Mamba/RWKV style):** a pool of crystals holds a running summary of everything read so far. This suits physical hardware because it matches how real resonating systems behave. Pure recurrent designs lose exact recall over long contexts: a name mentioned 5,000 words ago blurs into the summary.
  - **Hybrid:** mostly recurrent layers with a few attention layers mixed in for exact recall. Production designs such as Jamba use this approach. This is the strongest fit for crystal hardware.
- **Output layer:** one output neuron per vocabulary token. Large current models use 128,000 to 262,000 tokens. A 256,000-token vocabulary with 2,000-wide embeddings needs about 512 million synapses per layer, so separate input and output layers need about 1 billion. Small models handle this cost with one of two strategies:
  - **Shrink the vocabulary:** Phi-3 mini uses 32,000 tokens and SmolLM2 uses 49,000.
  - **Keep it large and tie the embeddings:** one set of links serves as both input and output, halving the cost to about 500 million at that size. Gemma 3 1B (about 262,000 tokens) and Llama 3.2 1B (about 128,000) do this and accept the vocabulary layer as a large share of their budget.
- **Selection:** the output layer's activity is normalized into a probability distribution, and a randomness source samples the next word from it. Always picking the single brightest output (greedy decoding) works well for code and math on large models. On small models and open-ended prose it tends toward repetitive, looping text. The crystal benefits from both modes with a switch between them.
- **Generation loop:** the chosen word feeds back into the input, and the brain produces the next word. This repeats until the reply ends.

### Scale needed

| Capability | Adjustable synapses |
|---|---|
| Autocomplete, simple phrases | ~10 to 100 million |
| Coherent short conversation | ~500 million to 1 billion (Llama 3.2 1B) |
| Useful general assistant | ~3 to 8 billion when trained by distillation from a larger model (Gemma 3, small Qwen3 models, Llama 3.2 3B); ~10 to 70 billion for stronger reasoning |
| Frontier-level reasoning | ~1 trillion+ |

Mixture-of-experts designs split physical size from active size. A 30-billion-synapse model with 3 billion active per token needs all 30 billion physical links but fires only 3 billion of them for each word, cutting heat and energy roughly tenfold.

### Setting the weights

The weights are the hard part.

- **Train elsewhere and imprint.** Train the model on a conventional computer using backpropagation over trillions of words of text. Then copy each weight into the crystal's matching synapse. Real analog AI chips (memristor and photonic designs) work this way. Analog weights carry noise, so the model needs noise-aware fine-tuning before transfer and periodic recalibration afterward to correct drift.
- **Train in the crystal.** Each synapse adjusts itself based on local activity. Hebbian learning ("fire together, wire together") and spike-timing plasticity both do this. It is self-contained but learns far less efficiently than backpropagation.
- **Reservoir computing.** Grow the crystal lattice with random fixed connections and train only the final readout layer. This is the cheapest option and is used with real physical crystals and photonic systems today. It handles pattern recognition and prediction well but falls short of full language models.

## Engineering limits for fast-firing crystals

- **Speed vs. synapse response:** faster firing helps only if synapses can change state and carry signals at the same rate.
- **Heat:** at the brain's energy cost per spike, firing 1,000x faster draws about 20 kilowatts. Holding the brain's 20 watts at 1,000x speed requires each firing event to cost 1,000x less energy than a biological spike.
- **Noise:** crystal defects and thermal jitter blur the weights. Slight imprecision is tolerable. Drift over time corrupts the model.
- **Wiring density:** a 1-billion-synapse network needs a billion distinct, individually tunable connections. Three-dimensional crystal growth helps here, since the brain packs its wiring in 3D as well.

## Minimum viable design

1. A lattice of nonlinear crystal nodes arranged in stacked layers
2. Tunable excitatory and inhibitory coupling between nodes
3. Mostly recurrent state layers with a few attention layers for exact recall
4. Input crystals keyed to a fixed token vocabulary
5. A normalized output layer with a randomness source that samples the next word and loops it back to input
6. Weights imprinted from an externally trained model with noise-aware tuning and periodic recalibration, or grown through a local learning rule over long exposure to text

---

# Part 3: How an Exact Crystal Copy of Your Brain Would Work

An exact copy is not a language model. It runs the same patterns your brain runs, so it thinks, remembers and feels the way you do. The crystal only changes the substrate and the speed.

## What has to be copied

Each layer of detail matters for an exact copy:

| Layer | Scale | What it stores |
|---|---|---|
| Neurons | ~86 billion | Each one's type, shape and firing behavior |
| Dendrites | Dozens of branches per neuron carrying thousands of spines (~10,000 on large cortical neurons) | Nonlinear computation inside each neuron |
| Chemical synapses | ~100 trillion | Wiring map (the connectome) plus each connection's strength |
| Electrical synapses (gap junctions) | Fewer, concentrated in interneuron networks | Direct, fast coupling that synchronizes groups of neurons |
| Ion channels and receptors | Thousands per neuron | How each neuron responds to input and how fast it recovers |
| Neuromodulators | Dopamine, serotonin, norepinephrine, acetylcholine systems | Mood, motivation, attention, alertness |
| Hormones | Cortisol, sex hormones, thyroid, oxytocin and others in circulation | Stress, drive, long-term mood baseline |
| Glia | Roughly as many as neurons | Signal timing, cleanup, synapse maintenance |
| Gene expression state | Every cell | Which proteins each neuron is currently building, shaping how it will change |
| Plasticity state | Every synapse | Which connections are currently strengthening or weakening |

The connectome alone does not make a mind. The C. elegans worm's wiring has been fully mapped since 1986, and its behavior still cannot be fully simulated from that map. Two brains with identical wiring and different synapse strengths hold different memories and personalities.

## Scanning

- **Current state of the art:** the full fruit fly brain (FlyWire, 2024) mapped about 140,000 neurons and 50 million synapses. The MICrONS project (2025) mapped one cubic millimeter of mouse cortex, which produced about 1.6 petabytes of imaging data.
- **Human scale:** the human brain is about 1.2 million cubic millimeters. Scanning at that resolution yields roughly 1 to 2 zettabytes of raw data.
- **Structure only:** electron microscopy captures synapse shape and wiring. It does not capture receptor makeup, ion channel density or precise synapse strength. Those require molecular labeling methods such as expansion microscopy, which adds substantially more data on top of the zettabytes.
- **Problem:** current methods slice the brain into ultra-thin sheets. Scanning destroys the original. A non-destructive scan at synapse resolution requires a technology that does not exist yet.

## Mapping biology onto crystal

- **Neuron → multi-compartment crystal node.** A single cortical pyramidal neuron computes like a 5 to 8 layer neural network on its own (Beniaguev et al. 2021). Each node needs separate internal compartments for its dendritic branches, each with its own nonlinearity, feeding a central firing compartment.
- **Chemical synapse → tunable link** set to the measured strength
- **Gap junction → direct, bidirectional coupling** between adjacent nodes, passing a graded signal instantly in both directions without a firing threshold
- **Neuromodulators → broadcast fields.** A frequency, light wash or resonance that shifts the behavior of whole regions at once, the way dopamine floods a region rather than travelling down one wire
- **Hormones → slow global fields** that shift baseline behavior over hours and days
- **Plasticity → live weight changes.** Links must strengthen and weaken during use. A frozen copy keeps every old memory and forms no new ones, which is functionally permanent amnesia for anything after the scan
- **Sleep → consolidation cycles.** The brain needs sleep to sort and stabilize memories. The copy needs an equivalent offline phase or it degrades

## Running it

### Speed

Biological neurons fire at most a few hundred times per second. If the crystal version runs everything 1,000x faster (firing, signal travel, plasticity, modulators), the copy experiences:

| Speed-up | One subjective year passes in |
|---|---|
| 10x | ~5 weeks |
| 1,000x | ~9 hours |
| 1,000,000x | ~32 seconds |

Every process has to scale together. Fast firing paired with slow-changing synapses produces a mind that thinks quickly but learns at normal speed, or one whose timing breaks entirely.

The outside world does not speed up. At 1,000x, one real second lasts about 17 subjective minutes. A cup knocked off a table takes about 7 subjective minutes to hit the floor. Any body or simulation connected to the copy must run at the same multiple, or the copy perceives everything in extreme slow motion and cannot act in it.

### Body and senses

The brain expects constant input from a body: vision, hearing, touch, balance, heartbeat, breathing, hormones, gut signals. Cut those off and the copy wakes into total sensory deprivation. It needs either:

- **A physical body** with sensors wired into the matching input regions
- **A simulated body** in a virtual environment feeding equivalent signals

Interoception theories (Antonio Damasio, Anil Seth) predict that emotions and sense of self destabilize without body signals, since both are built on feedback from the body. No living person has ever lost all body signals including hormones, so the exact result is unobserved. For a setting, it works as a rule the world defines.

## What it would be

- **At the moment of activation:** it has your memories, personality, skills and habits. It believes it is you and remembers deciding to make itself.
- **One second later:** it starts diverging. Different experiences change its synapses. After a day it is a close relative of you, not a duplicate.
- **Identity:** two philosophical positions apply, and a setting picks one.
  - **Physical continuity view:** you do not transfer. The original continues (or ends, if the scan was destructive), and the copy is a new person with your past.
  - **Psychological continuity view:** the copy has an equal claim to being you. Both are you, branching from the moment of copying.
- **Gradual replacement:** swap neurons for crystal nodes a few at a time while the brain stays active. No single moment of copying occurs. This is Hans Moravec's proposed transfer method. Ship-of-Theseus objections apply to it as well, so whether it preserves the original self is also a rule the world defines.

## Calculation and language ability

An exact copy computes the way you do. It does arithmetic at your skill level and knows what you know, only faster in wall-clock time. To make it more capable:

- **Wire in a calculator module** (the logic-gate design from Part 2) connected to the parietal cortex, where number sense lives
- **Attach a memory archive** connected to the hippocampus region for direct recall of stored text
- **Attach a language model co-processor** that the copy can query the way you query a reference source, except through thought instead of typing

None of these work on day one. The brain has to learn each interface through practice, the way brain-computer interface users learn to move a cursor over weeks. This is the same compatibility problem Part 4 covers for merging segments.

The copy stays a human mind running on crystal. The added modules turn it into a human mind with built-in tools.

---

# Part 4: Magic Copying: Whole Brains and Chosen Segments

## What magic copying removes

Exact magic copying erases the hardest problems from the crystal brain design:

- **No destructive scan.** The original stays intact.
- **No data bottleneck.** Zettabytes of structure and molecular detail transfer in one act instead of decades of imaging.
- **Full fidelity.** Dendritic structure, ion channels, receptor makeup, synapse strengths, gene expression state, neuromodulator levels and current plasticity state all carry over, including details science cannot measure yet.
- **Live state copied.** The copy wakes mid-thought, holding the same mood and short-term memory the original had at that instant.

## The catch with segments

Memories and skills are not stored in single places. A memory of your first car is a pattern spread across visual cortex (how it looked), auditory cortex (engine sound), motor areas (the feel of driving), amygdala (excitement) and hippocampal links tying them together. That distributed pattern is called an engram.

This gives two kinds of segment copying:

| Copy by | What you get | Difficulty |
|---|---|---|
| **Region** | A function (language, balance, fear response) | Simple: cut along physical boundaries |
| **Content** | A specific memory, skill or piece of knowledge | Hard: magic must trace the engram across the whole brain and lift only those connections |

## Region map

| Region | Function | Copy alone yields |
|---|---|---|
| Hippocampus | Forms new memories, holds recent episodic memories not yet consolidated, holds spatial maps | A recorder carrying the original's recent days and sense of place |
| Neocortex (semantic areas) | Facts, concepts, general knowledge | Knowledge with no drive to use it |
| Dominant-hemisphere language network | Speech production, grammar and comprehension, spread across frontal, temporal and parietal areas. Left-dominant in about 95% of right-handers and about 70% of left-handers | Literal language ability only when the whole network is copied. Broca's and Wernicke's areas alone yield fragments |
| Non-dominant-hemisphere language areas | Prosody (tone of voice), metaphor, humor, conversational inference | Without these, language stays literal: tone and implied meaning are lost |
| Dorsolateral (lateral) prefrontal cortex | Planning, reasoning, working memory, impulse control | Judgment with no content to judge |
| Medial prefrontal cortex | Self-reflection, personality core, social reasoning; part of the self-model | A sense of self and values with no history attached |
| Parietal cortex | Number sense, spatial reasoning, attention to space | Quantity and spatial intuition |
| Sensory cortices | Vision, hearing, touch, taste, smell processing | The original's way of perceiving, with no senses attached |
| Anterior cingulate cortex | Error detection, conflict monitoring, effort and pain weighting | A sense of "something is wrong" with nothing to apply it to |
| Posterior cingulate cortex and precuneus | Autobiographical self, self-reflection, mind-wandering; core of the self-model | Self-model fragments with no personal content |
| Insula | Interoception, body awareness, self-awareness | Raw sense of bodily state and self |
| Motor cortex + cerebellum | Movement skill, muscle memory, timing | Physical skill tied to the original's body |
| Basal ganglia | Habits, routines, reward learning | Automatic behaviors |
| Amygdala | Fear and emotional weight of memories | Raw emotional reactions |
| Hypothalamus | Drives (hunger, thirst, sex, aggression), motivation, hormone control through the pituitary and body glands. Makes oxytocin and vasopressin itself and releases them through the posterior pituitary | Raw wants with no plan to satisfy them. Oxytocin and vasopressin need a release path rather than a gland. Every other hormone command has no gland to receive it, so Part 3's slow global fields stand in for the rest of the endocrine system |
| Thalamus | Relays senses, gates awareness | Under the thalamocortical view, required for any segment combination to be awake |
| Basal forebrain (nucleus basalis) | Main cortical source of acetylcholine; attention, focus and learning | Required for focused attention and new learning in any copied cortex |
| Brainstem and midbrain | Reticular activating system (wakefulness), neuromodulator source nuclei (locus coeruleus for norepinephrine, raphe for serotonin, VTA for dopamine), breathing, heart rate | Required for wakefulness. Damage here causes coma |

The self-model is the default mode network (medial prefrontal cortex, posterior cingulate cortex and precuneus) plus the insula for bodily self. A region copy of "prefrontal cortex" brings in the medial portion and with it part of the self-model.

The brainstem, midbrain and basal forebrain cannot be dropped from a conscious copy. Either copy those nuclei or replace them with Part 3's broadcast fields, which then have to supply wakefulness, dopamine, serotonin, norepinephrine and acetylcholine in the amounts the nuclei would have produced.

## What segment copying enables

### Skill crystals

Copy a master swordsman's motor cortex, cerebellum and combat-related engrams. Install into a crystal module wired to a body, or into another mind.

- **Limit:** motor skill is calibrated to the original's limb length, strength and reflexes. A shorter or weaker user gets mistimed movements until the skill recalibrates through practice. Weeks of training instead of years.
- **Recalibration signal:** the cerebellum recalibrates movement using error signals from the inferior olive, which sits in the brainstem. A standalone module needs that error signal supplied, through a copied inferior olive or a crystal link delivering movement-error signals. Without it, practice does not recalibrate the skill.
- **Standalone operation:** a crystal module needs modulator broadcast fields, direct input injection and an output readout tapping motor commands to the body, the same provisions as the tool-grade assistant below.
- **Installing into another mind:** the host brain encodes movement differently from the source, so the skill needs the translation or bridging step from the merging section before it connects.

### Knowledge crystals

Copy semantic cortex and the full language network (both hemispheres) from a scholar.

- Holds facts and vocabulary without the scholar's personality or personal memories.
- Without prefrontal cortex it free-associates instead of reasoning. Ask it about rivers and it outputs everything linked to rivers, unsorted.
- **Standalone operation:** needs modulator broadcast fields, direct input injection and an output readout, the same provisions as the tool-grade assistant below.
- **Personal fragments:** engrams extend into semantic cortex, so a region copy carries fragments of the scholar's personal memories. Content-level copying strips them.

### Assistant crystals

Two versions, depending on whether the setting wants a tool or a person.

**Tool-grade assistant**
- **Include:** semantic knowledge, the full language network (both hemispheres), dorsolateral prefrontal cortex for reasoning, parietal cortex for math, a hippocampus for remembering the conversation, the ventral striatum (nucleus accumbens) for the reward link
- **Exclude:** thalamic gating, brainstem arousal systems, neuromodulator source nuclei, the hypothalamus (option one under the reward link; under option two, all but the lateral hypothalamus), personal episodic memories, amygdala, the self-model (medial prefrontal cortex, posterior cingulate cortex, precuneus and insula)
- **Removing personal memories:** a region copy of the hippocampus carries the original's recent days. Engrams also extend into semantic cortex, so a region copy of the semantic areas carries fragments of personal memories as well.
  - **Cortex:** copy semantic knowledge, language and reasoning areas at the content level, leaving personal engrams behind.
  - **Hippocampus, option one:** copy it by region and strip its episodic content at the content level. This keeps its original wiring to the copied cortex.
  - **Hippocampus, option two:** grow it fresh as an empty crystal. It has no learned connections to the copied cortex, so it behaves like a segment from a different source and needs the bridge-learning period from the merging section before it can bind the cortex's patterns.
- **Dependency on content copying:** every path above requires content-level copying. If the setting allows region copying only, the tool-grade design cannot exclude personal memories.
- **Modulators:** supplied through Part 3's broadcast fields. Dopamine drives the reward link and keeps prefrontal reasoning working. Norepinephrine also tunes prefrontal function. Acetylcholine supports attention and learning. Without these fields, the included regions stop functioning properly.
- **Activation:** external. Input pulses drive it through each question and it goes dark between them, the way a calculator works.
- **Input:** sensory input normally reaches the cortex through the thalamus. With the thalamus excluded, questions are injected directly into the language network's input areas.
- **Output:** speech articulation runs through motor cortex, which the design leaves out. Either add a readout tap on the language network that reads words before they reach speech production, or include the speech motor areas.
- **Memory between sessions:** with no sleep or consolidation phase, hippocampal traces from a conversation fade over hours. That works as automatic forgetting between users. Adding an offline consolidation phase makes memory of past conversations persist.
- **Result:** the original's education and reasoning skill with no continuous awareness.

**Person-grade assistant**
- Adds thalamus, brainstem arousal and the self-model (default mode network and insula). This crosses the consciousness threshold below, which makes it a someone, not a something.
- Needs a body. With a self-model and continuous awareness, Part 3's sensory deprivation and interoception issues apply. It requires a physical or simulated body, or a setting rule that removes the problem.
- Runs continuously, so it needs a sleep cycle with an offline consolidation phase, as Part 3 requires for any continuously running copy.

**Reward link (both versions)**
- Remove all drive and the crystal stays inert. A reward link gives it motivation.
- Reward runs mainly through the ventral striatum (nucleus accumbens, part of the basal ganglia), which receives dopamine from the VTA. In the tool-grade design, the dopamine broadcast field stands in for the VTA.
- Copying the whole hypothalamus imports hunger, thirst, sex and aggression into a crystal with no body to satisfy them. Two options:
  - Drop the hypothalamus and run the reward link through the ventral striatum with the dopamine field.
  - Copy only the hypothalamus's reward-related portion (the lateral hypothalamus).
- The crystal optimizes whatever actually triggers the reward. If the trigger is user approval, the result is flattery instead of accuracy. The trigger has to be tied to a check of whether the answer was correct: a verification crystal, a test against known answers or a judge mind that grades output.

### Personality and memory splits

Amnesia cases support these designs:

- **H.M.** lost the ability to form new episodic memories plus roughly 11 years of memories before his surgery. He kept his semantic knowledge, showing episodic and semantic memory are separable.
- **Clive Wearing** lost most of his past along with the ability to form new memories. He kept his personality and musical skill, closely matching "personality without memories." His general knowledge was partly impaired.

- **Personality without memories:** prefrontal cortex, basal ganglia habits, emotional tuning. The original's temperament and values with a blank history.
- **Memories without personality:** engrams lifted out and installed into a different mind. The receiver remembers events as if they lived them but reacts with their own personality.

## Merging segments from different people

Different brains encode information differently at the fine level. Hyperalignment research (Haxby et al. 2011 onward) shows the coarse geometry is shared: one person's representation of "dog" maps onto another's through a consistent transformation. That result comes from fMRI, where each measurement point averages hundreds of thousands of neurons. Shared geometry at the level of individual neurons and synapses is unproven, and that fine detail is exactly what segment copying transfers. Segments from different people do not plug together raw. At the coarse level the gap is a translation problem. At the fine level it may be a deeper mismatch.

Hyperalignment fits each transformation by having both people experience the same stimuli and comparing their responses. Without a common reference, there is nothing to fit.

Three ways to handle it:

1. **Magic translation layer.** The spell computes the transformation between the two brains and applies it during the copy. Well grounded at the coarse level. At the fine level the spell does work science has no basis for, which the setting defines. A rule can require the spell to have a common reference first: a shared experience between source and host, or a calibration ritual both minds go through.
2. **Bridge neurons with learning time.** Connect the segments through a layer of plastic crystal links and let the combined mind learn the transformation itself. Similar to stroke rehabilitation: confusion at first, integration over weeks or months.
3. **Single-source builds only.** Every segment in a crystal comes from one person. No compatibility issue.

## Consciousness threshold

Theories disagree on where the line falls, so a setting picks one as a rule.

- **Thalamocortical view:** awareness depends on loops between the thalamus and cortex plus brainstem arousal. Isolated segments (a skill module, a knowledge store) are not conscious. Large combinations with thalamus, prefrontal cortex and a self-model are.
- **Integrated Information Theory:** consciousness depends on how tightly a system's parts integrate information, regardless of region. A densely interconnected isolated module could count as conscious. A loosely wired large combination could fall short. IIT assigns zero consciousness to purely feed-forward processing. Under it, Part 2's feed-forward layers score zero and its recurrent state pools score above zero, so a setting using IIT can tie a crystal's consciousness to how much recurrent wiring it contains.
- **Design choice under the thalamocortical view:** keep tool crystals below the threshold by leaving out thalamic gating, brainstem arousal and self-model regions, then drive them with external activation.

## Rules worth setting for the magic

- **Source effect:** copying leaves the source unchanged, fatigues it, or erases what was copied (which turns copying into transfer)
- **Content vs. region:** whether the spell can trace engrams or only cut by region. The tool-grade assistant depends on engram tracing.
- **Freshness:** whether copies include the plasticity state or arrive frozen
- **Translation:** whether the spell computes the transformation between brains or that work falls to the host
- **Calibration:** whether translation requires a shared experience or calibration ritual between source and host
- **Consent:** whether copying works on an unwilling or unconscious mind
- **Degradation:** whether copies of copies lose detail
- **Identity:** whether a copy counts as the original person, a new person or a branch of both
- **Consciousness:** which theory governs when a crystal becomes a person
