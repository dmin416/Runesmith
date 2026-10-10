# Crystal Computer Math

Hub: `CrystalMinds.md` (brains, LLMs, crystal copies). Full octonary substrate / heat / programming stack: `OctonaryCrystalBrain.md`. Focus capacity: `FocusCapacity.md`. Science root: `../Science.md`. Nav: `Index.md`.

**Owns:** self-improvement ignition thresholds and binary / trinary / hexanary / octonary comparison. Story crystal rules → `CrystalMinds.md`. Substrate deep dive → `OctonaryCrystalBrain.md`.

**Status:** design loot. Numbers are Earth-scale engineering bounds for crystal computing and self-improving lattices. Pair with CrystalMinds architecture talk; do not treat as live story lock until a chapter uses them.

---

## 1. Minimum Processing Power for Self-Improvement

Three distinct thresholds:

- **Blind improvement (evolution):** Near zero processing. Requires only self-copying with heritable variation plus selection. Real-world precedent: the Cairns-Smith clay hypothesis, in which mineral crystals copying their own defect patterns may have been Earth's first "genes." Progress happens on geological timescales.
- **Learning (adapting within one lifetime):** Roughly insect scale. A honeybee handles navigation, learning and signaling with about 1 million neurons and about 10^9 synapses, or roughly 10^10 to 10^11 synaptic events per second.
- **Deliberate redesign (modeling its own structure and rewriting it):** Roughly human scale or above. Human brain estimates run from 10^14 to 10^16 operations per second with about 10^14 synapses of storage.

Storage is not the bottleneck for crystal life. A cubic centimeter holds about 10^22 to 10^23 atoms. If one lattice site in a billion acts as a bit, that gives 10^13 to 10^14 bits per cm³, near human synapse count. The real constraint is the thinking medium:

- Thought through crystal growth and defect migration: millions of times slower than neurons.
- Electronic or phonon switching: gigahertz to terahertz, far faster than neurons at about 100 to 1,000 Hz.

**Ignition point:** the crystal can simulate a change to its own lattice faster and more cheaply than it can physically grow and test that change. Below that line, improvement is blind trial and error. Above it, each improvement speeds up the next. For a lattice at electronic speeds, the line sits near insect-to-small-mammal scale, around 10^12 to 10^13 operations per second.

## 2. Multi-State Digits in Cubic Crystals

Cubic symmetry supplies six equivalent directions (±x, ±y, ±z). A defect or off-center atom displaced along any of them gives a six-state digit. All six positions are identical in energy, so each state is equally stable. One hexanary digit holds log₂(6) ≈ 2.58 bits.

The six states split into 3 × 2: which axis (ternary) times which end (binary).

Diamond's tetrahedral bonding favors other counts:

| States | Source |
|---|---|
| 4 | The four tetrahedral bond directions (real NV centers point along one of four orientations) |
| 3 | NV center spin states (combined with orientation: 12 states per defect) |
| 6 | Displacement along ±x, ±y, ±z via split interstitials or substitutional atoms |
| 12 | The twelve edge-center directions of the cube |

More states per site narrows the energy barrier between neighboring states, so thermal jostling flips digits more often. Diamond's stiff lattice and high barriers make base 6 or base 12 plausible without unusual error correction.

## 3. Four Architectures Compared

### Assumptions

- Volume: 1 cm³
- Node size: one logic node per 5 nm cube (8 × 10^18 nodes)
- Clock: 1 GHz
- Energy per switching event: 100 kT at room temperature (about 4 × 10^-19 J)

| Type | States | Links per node | Geometry |
|---|---|---|---|
| Binary | 2 | 3 (1 in, 2 out) | Fan-out tree |
| Diamond trinary | 3 | 4 (1 in, 3 out) | Diamond tetrahedral bonds |
| Hexanary | 6 | 6 (1 in, 5 out) | Cube faces |
| Octonary | 8 | 8 bidirectional | Cube corners (±⟨111⟩ directions) |

### Storage per cm³

| Type | Bits per digit | Storage | Cube matching a human brain (10^14 bits) |
|---|---|---|---|
| Binary | 1.00 | 8.0 × 10^18 (1.0 EB) | 232 µm wide |
| Trinary | 1.58 | 1.3 × 10^19 (1.6 EB) | 199 µm |
| Hexanary | 2.58 | 2.1 × 10^19 (2.6 EB) | 169 µm |
| Octonary | 3.00 | 2.4 × 10^19 (3.0 EB) | 161 µm |

### Throughput and Routing

| Type | Bits out per node per tick | Peak bits/s per cm³ | Distinct paths over 10 hops |
|---|---|---|---|
| Binary | 2.0 | 1.6 × 10^28 | 1,024 |
| Trinary | 4.8 | 3.8 × 10^28 | 59,049 |
| Hexanary | 12.9 | 1.0 × 10^29 | 9.8 million |
| Octonary | 24.0 | 1.9 × 10^29 | 282 million |

Octonary paths use 7 choices per hop since the eighth link leads back the way the signal came.

### Heat Ceiling

- Every node firing at once: about 3.3 GW per cm³.
- Binary peak at the Landauer limit (theoretical minimum): about 46 MW.
- A working crystal mind must run sparse like a brain.

At a 20 W budget (human brain power):

| Type | Bits/s at 20 W | Multiple of a human brain |
|---|---|---|
| Binary | 4.8 × 10^19 | ~5,000 to 50,000× |
| Trinary | 7.7 × 10^19 | ~8,000 to 77,000× |
| Hexanary | 1.2 × 10^20 | ~12,000 to 120,000× |
| Octonary | 1.4 × 10^20 | ~14,000 to 140,000× |

Active fraction at 20 W: about 1 node in 170 million at any moment.

### Self-Improvement Ignition Point

Threshold: 10^12 to 10^13 operations per second with about 10^12 bits of memory (roughly mouse scale).

| Requirement | Value |
|---|---|
| Power | ~4 µW |
| Crystal size (binary) | ~50 µm cube |
| Crystal size (octonary) | ~35 µm cube |
| Nodes switching per nanosecond | ~10,000 |

Memory sets the size. The result is a mind about the size of a dust mote.

### Architecture Consequences

- **Binary 1-in/2-out:** Pure fan-out tree with no built-in return path. Feedback needs separate return wiring, so self-checking is slow and costly.
- **Trinary and hexanary:** More branching but still one-way flow, like water through a delta.
- **Octonary bidirectional:** Any signal can loop back to verify or revise its own output. Recurrence is the core requirement for self-modeling, so this design reaches the ignition point with the fewest nodes. The cost is 8 states per site with narrower energy barriers between states. Diamond's stiff lattice handles that better than almost any other material.
