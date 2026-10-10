# The Octonary Crystal Brain

Limits, efficiency, power, computational density and programming for a bidirectional eight-state crystal computer.

Hub: `CrystalMinds.md`. Architecture comparison and ignition thresholds: `CrystalComputerMath.md`. Focus capacity: `FocusCapacity.md`. Science root: `../Science.md`. Nav: `Index.md`.

**Owns:** octonary diamond substrate, heat walls, reversible compute, density, programming stack. Comparison table → `CrystalComputerMath.md`. Story copies / segments → `CrystalMinds.md`.

**Status:** design loot. Extends CrystalComputerMath's octonary row into a full substrate, heat, reversible-compute and programming stack. Not a live story lock until a chapter uses it.

---

## 0. Headline Numbers (1 cm³ of diamond, 300 K)

| Quantity | Value |
|---|---|
| Logic nodes (5 nm pitch) | 8 × 10^18 |
| Atoms per node | ~22,000 |
| Storage, state digits only | 2.4 × 10^19 bits (3 EB) |
| Storage, full node (state + configuration) | 4.3 × 10^20 bits (54 EB) |
| Peak node updates at 1 GHz, all nodes active | 8 × 10^27 per second |
| Power for that peak at 100 kT per update | 3.3 GW |
| Best conventional throughput at 20 W | 4.8 × 10^19 updates/s (~390,000 human brain rates) |
| Best reversible throughput at 20 W | 6.2 × 10^24 updates/s (~5 × 10^10 human brain rates) |
| Passive cooling limit (still air, 1 cm cube) | ~0.5 W |
| Edge-to-edge latency through the node mesh | 2 ms at 1 GHz per hop |
| Edge-to-edge latency on a photonic express lane | 81 ps |
| Smallest self-improving mind (10^12 bits) | ~35 µm cube, ~4 µW |

The governing fact: **the octonary crystal brain is limited by heat at every scale above a single node.** Storage, clock speed and bandwidth are all far beyond what the crystal can cool. Every design decision below follows from that.

---

## 1. The Physical Substrate

### 1.1 The Eight-State Digit

The eight states are the eight corners of a cube, the ⟨111⟩ directions. Each corner is a vector (±1, ±1, ±1).

| Digit | Binary | Vector (x, y, z) |
|---|---|---|
| 0 | 000 | (+, +, +) |
| 1 | 001 | (−, +, +) |
| 2 | 010 | (+, −, +) |
| 3 | 011 | (−, −, +) |
| 4 | 100 | (+, +, −) |
| 5 | 101 | (−, +, −) |
| 6 | 110 | (+, −, −) |
| 7 | 111 | (−, −, −) |

This is the most important property of the octonary design: **one digit is exactly three independent sign bits, one per axis.** The digit is simultaneously a number (0 to 7), three binary bits and a 3D direction. Every operation can be read in any of those three ways.

Physical precedents for ⟨111⟩ eight-state defects exist in real crystals. Li⁺ in KCl sits off-center along the eight ⟨111⟩ directions. CN⁻ in KCl orients along ⟨111⟩.

**The diamond complication.** A diamond lattice site has tetrahedral symmetry, not full cubic symmetry. The eight ⟨111⟩ displacements split into two sets of four: four toward bonded neighbors and four toward the empty antibonding directions. The two sets differ in energy. Three solutions:

1. **Composite digit:** 4 bond orientations × 2 charge states = 8 states. Uses real diamond defect physics directly.
2. **Inversion-centered defects:** split-vacancy complexes (like the SiV center) sit at inversion centers, which restores the ± pairing.
3. **Unequal but stable:** the energy offset between the sets does not matter if every state sits behind a high barrier. Retention depends on barrier height, not on equal energies.

### 1.2 The Node Lattice

The logic nodes form a body-centered cubic superlattice inside the diamond. In a BCC lattice every site has exactly eight nearest neighbors, all along ⟨111⟩. That gives every node its eight bidirectional links for free.

| Parameter | Value |
|---|---|
| Node density | 8 × 10^18 per cm³ |
| BCC cube edge | 6.3 nm |
| Node-to-node distance | 5.46 nm |
| Atoms per node | ~22,000 |
| Diamond atom density | 1.76 × 10^23 per cm³ |

**Geometric bonus:** each node's state is a ⟨111⟩ vector and each link runs along ⟨111⟩. A node's state can literally point at one of its eight neighbors. A digit is both a value and an address.

### 1.3 Node Anatomy (5 nm node)

| Component | Count | Digits | Bits |
|---|---|---|---|
| State site (the node's value) | 1 | 1 | 3 |
| Link configuration (2 digits per link) | 8 links | 16 | 48 |
| Mode digit | 1 | 1 | 3 |
| **Total** | | **18** | **54** |

The remaining ~22,000 atoms form the link channels (chains of coupled defects along each ⟨111⟩ direction), isolation spacing and structural lattice. Eighteen active sites in 125 nm³ means about 1.9 nm between defects. That spacing is wide enough to keep each defect's state independent.

### 1.4 Node Size Sweep

| Node pitch | Nodes per cm³ | Atoms per node | Hops across 1 cm | Mesh latency at 1 GHz | Full activity power at 100 kT |
|---|---|---|---|---|---|
| 2 nm | 1.25 × 10^20 | 1,410 | 5 × 10^6 | 5 ms | 52 GW |
| 3 nm | 3.7 × 10^19 | 4,760 | 3.3 × 10^6 | 3.3 ms | 15 GW |
| **5 nm** | **8 × 10^18** | **22,000** | **2 × 10^6** | **2 ms** | **3.3 GW** |
| 10 nm | 1 × 10^18 | 176,000 | 1 × 10^6 | 1 ms | 0.41 GW |

Smaller nodes raise storage and peak throughput. They do nothing for usable throughput because heat sets that limit. A 2 nm node at the same power budget delivers the same number of updates per second as a 5 nm node with more nodes sitting idle. The extra density only buys memory.

---

## 2. Limits of Computing

### 2.1 Ultimate Physical Bounds for 1 cm³ of Diamond (3.51 g)

| Bound | Formula | Value |
|---|---|---|
| Bremermann limit | mc²/h | 4.8 × 10^47 bits/s |
| Margolus-Levitin limit | 2E/(πħ), E = mc² | 1.9 × 10^48 ops/s |
| Bekenstein bound (storage) | 2πRE/(ħc ln 2) | 5.6 × 10^38 bits |
| Atomic storage limit (every atom an octonary digit) | 3 bits × atom count | 5.3 × 10^23 bits |
| Practical design (5 nm nodes, full node) | | 4.3 × 10^20 bits |

The practical design sits about 1,200× below the atomic storage limit. Peak throughput (8 × 10^27 updates/s) sits about 20 orders of magnitude below the Margolus-Levitin limit. Fundamental physics is nowhere close to binding. Engineering limits govern everything.

### 2.2 Thermal Noise and Reliability

At 300 K, kT = 4.14 × 10^-21 J = 0.0259 eV.

**Memory retention.** A digit flips spontaneously at rate ν₀·e^(−E_b/kT), with attempt frequency ν₀ ≈ 10^13 Hz. For less than one spontaneous error per year across the whole memory:

| Digits stored | Required barrier | In eV |
|---|---|---|
| 10^19 | 91 kT | 2.35 eV |
| 10^21 | 96 kT | 2.47 eV |

This is why the baseline uses 100 kT (2.6 eV) per switching event. Diamond supports barriers in this range. Vacancy migration in diamond needs about 2.3 eV. NV centers survive annealing above 1,000 °C.

**Logic margin.** A logic signal only needs to survive one tick. An eight-state symbol has seven wrong states, so error probability ≈ 7·e^(−E/kT).

| Target error per update | Required signal energy |
|---|---|
| 10^-12 | 30 kT |
| 10^-20 | 48 kT |
| 10^-30 | 71 kT |

Two tiers result: **memory digits at ~95 kT barriers** and **logic signals at ~30 to 50 kT** with error correction cleaning up the rest.

### 2.3 Landauer Limit

Erasing information has a minimum cost of kT ln 2 per bit.

| Erased unit | Minimum energy at 300 K |
|---|---|
| 1 bit | 2.87 × 10^-21 J (0.018 eV) |
| 1 octonary digit | 8.61 × 10^-21 J (0.054 eV, 2.08 kT) |

The Landauer cost applies only to erased information. Reversible operations can in principle run below it (Section 3.3).

### 2.4 Clock Ceiling

| Signal mechanism | Ceiling |
|---|---|
| Diamond optical phonon (Raman line, 1,332 cm⁻¹) | 40 THz |
| Ion hopping attempt frequency | ~10 THz |
| Reliable displacement switching | ~10 to 100 GHz |
| Electronic or charge-state switching | ~100 GHz to 1 THz |

Clock speed is not a practical limit. At 100 GHz a fully active cm³ would need 330 GW. The usable clock is set by heat, not switching physics.

### 2.5 Heat Removal: The Real Wall

Diamond conducts heat better than almost anything (natural type IIa about 2,200 W/m·K, isotopically pure ¹²C about 3,300 W/m·K). For a 1 cm³ sphere with a 50 K internal temperature rise, conduction can carry 17,000 to 26,000 W/cm³ to the surface. **The surface, not the interior, is the bottleneck.**

| Cooling mode (1 cm cube, 6 cm², 50 K above ambient) | Heat flux | Total power |
|---|---|---|
| Radiation only (vacuum, 350 K surface) | 0.039 W/cm² | 0.23 W |
| Still air (convection + radiation) | 0.089 W/cm² | 0.53 W |
| Forced air | 0.5 W/cm² | 3 W |
| Boiling water | 100 W/cm² | 600 W |
| Microchannel liquid cooling | 1,000 W/cm² | 6,000 W |

**Scaling consequence.** Cooling grows with surface area while nodes grow with volume. Passive cooling per cm³ falls as the crystal grows:

| Sphere radius | Passive power (still air) | Power per cm³ |
|---|---|---|
| 0.5 cm | 0.28 W | 0.54 W/cm³ |
| 1 cm | 1.1 W | 0.27 W/cm³ |
| 5 cm | 28 W | 0.054 W/cm³ |
| 10 cm | 112 W | 0.027 W/cm³ |
| 50 cm | 2,800 W | 0.0054 W/cm³ |

A large crystal mind has to fight its own geometry. Natural crystal life would grow **flat plates, dendrites or snowflake branches** to maximize surface, or grow internal coolant channels. A compact crystal sphere is the shape of a dormant or slow-thinking mind.

### 2.6 Latency

| Path across 1 cm | Time |
|---|---|
| Node mesh, 1 ns per hop (2 × 10^6 hops) | 2 ms |
| Longitudinal sound in diamond (~18 km/s) | 0.56 µs |
| Light in diamond (n = 2.42) | 81 ps |

For comparison, signals cross a human brain in roughly 10 to 100 ms. A 1 cm crystal using only nearest-neighbor hops is only 5 to 50× faster across its full width than a human brain. **Express lanes fix this.** Photonic waveguides (diamond is transparent and has a high refractive index) or phonon channels give long-range links about 25 million times faster than the mesh. The crystal brain needs a two-tier network like a real brain: local mesh plus long-range "white matter."

**Subjective speed of a human-scale mind.** A 10^14-bit mind at 54 bits per node needs 1.85 × 10^12 nodes: a cube 12,300 nodes wide (61 µm). Crossing it takes 12 µs at 1 GHz per hop. Against human cross-brain times of 10 to 100 ms, that is an **800 to 8,000× subjective speedup** on the mesh alone. Express lanes push it higher until throughput or heat becomes the limit.

### 2.7 Bandwidth

Bisection bandwidth through the middle of a 1 cm cube: 4 links per node crossing the plane × (2 × 10^6)² nodes × 3 bits × 10^9 Hz = **4.8 × 10^22 bits/s**. The entire crystal at 20 W only processes about 1.5 × 10^20 bits/s in the conventional regime. Internal bandwidth is about 300× more than heat allows the crystal to use.

### 2.8 Radiation Damage

Sea-level cosmic-ray muons arrive at about 1 per cm² per minute. A minimum-ionizing muon deposits about 6.3 MeV/cm in diamond.

| Per node crossed (5 nm) | Value |
|---|---|
| Energy deposited | ~3.2 eV |
| Electron-hole pairs (13 eV per pair) | ~0.24 |
| Nodes disturbed per track (1 cm) | ~490,000 |

3.2 eV per node exceeds the 2.5 eV memory barrier. **Every muon draws a line of potential bit flips straight through the crystal.** Errors arrive as straight lines, not random scatter. Error-correcting codes must spread each code word across nodes that no single straight line can hit more than once (for example, scattered along a helix or across non-collinear planes). The crystal also needs continuous scrubbing: background reading, checking and rewriting of memory. Underground or shielded crystal minds would have far lower error loads.

### 2.9 Slow Degradation

| Mechanism | Effect | Countermeasure |
|---|---|---|
| ¹³C nuclear spins (1.1% natural abundance) | Magnetic noise on spin-based digits | Isotopic purification to ¹²C |
| Defect migration | Gradual drift and aging of configuration | High barriers, periodic rewriting |
| Quantum tunneling between sites | State leakage for light ions at low temperature | Heavy dopants, wide barriers |
| Thermal cycling | Strain shifts barrier energies | Stable operating temperature |
| Ionizing radiation | Line-shaped bit flips | Geometric ECC, scrubbing |

---

## 3. Power and Efficiency

### 3.1 Energy Regimes

| Regime | Energy per node update | Updates per joule | Power for full activity at 1 GHz |
|---|---|---|---|
| Conventional, high margin | 100 kT | 2.4 × 10^18 | 3.3 GW |
| Conventional, low margin | 50 kT | 4.8 × 10^18 | 1.7 GW |
| Near-Landauer | 10 kT | 2.4 × 10^19 | 330 MW |
| Landauer floor (one digit erased per update) | 2.08 kT | 1.2 × 10^20 | 69 MW |
| Adiabatic reversible at 1 GHz | 1 kT | 2.4 × 10^20 | 33 MW |
| Adiabatic reversible at 10 MHz | 0.01 kT | 2.4 × 10^22 | 3.3 kW (at 10 MHz clock) |

The adiabatic model: dissipated energy = signal energy × (τ₀ / switching time), with signal energy 100 kT and lattice relaxation time τ₀ = 10 ps. Switching ten times more slowly dissipates ten times less energy per update.

### 3.2 Allowed Activity Fraction at 1 GHz

The fraction of nodes that can be active at any instant without overheating:

| Cooling | 100 kT | Landauer floor | Adiabatic 1 kT |
|---|---|---|---|
| Radiation only | 7 × 10^-11 | 3.4 × 10^-9 | 7 × 10^-9 |
| Still air | 1.6 × 10^-10 | 7.8 × 10^-9 | 1.6 × 10^-8 |
| Forced air | 9 × 10^-10 | 4.4 × 10^-8 | 9 × 10^-8 |
| Boiling water | 1.8 × 10^-7 | 8.7 × 10^-6 | 1.8 × 10^-5 |
| Microchannel | 1.8 × 10^-6 | 8.7 × 10^-5 | 1.8 × 10^-4 |

At 1 GHz, a crystal brain is overwhelmingly idle. A passively cooled one has about 1 active node per 6 billion.

### 3.3 Slow and Wide: The Reversible Strategy

With adiabatic switching, dissipation per update scales with clock frequency. Total power for full activity therefore scales with **frequency squared**: P = N × f² × E_signal × τ₀.

Full activity, whole cm³ (8 × 10^18 nodes all updating every tick):

| Clock | Updates/s | Power (perfect reversibility) | Power (1% of updates erase a digit) |
|---|---|---|---|
| 1 kHz | 8 × 10^21 | 33 µW | 0.69 W |
| 10 kHz | 8 × 10^22 | 3.3 mW | 6.9 W |
| 100 kHz | 8 × 10^23 | 0.33 W | 69 W |
| 1 MHz | 8 × 10^24 | 33 W | 720 W |
| 10 MHz | 8 × 10^25 | 3.3 kW | 10 kW |
| 100 MHz | 8 × 10^26 | 330 kW | 400 kW |
| 1 GHz | 8 × 10^27 | 33 MW | 34 MW |

Maximum clock for full activity under each cooling mode (perfect reversibility):

| Cooling | Max full-activity clock | Updates/s |
|---|---|---|
| Radiation only | 84 kHz | 6.7 × 10^23 |
| Still air | 127 kHz | 1.0 × 10^24 |
| Forced air | 300 kHz | 2.4 × 10^24 |
| Boiling water | 4.3 MHz | 3.4 × 10^25 |
| Microchannel | 13 MHz | 1.1 × 10^26 |

**Running every node slowly beats running a few nodes fast by factors of 10,000 to 100,000.** A passively cooled cm³ running reversibly at 127 kHz does about 10^24 updates per second. The same crystal running conventionally at 1 GHz does about 10^18.

### 3.4 The Erase Budget

Perfect reversibility is impossible: outputs must eventually be overwritten. The fraction of updates that erase a digit sets a hard floor of 2.08 kT × (erase fraction) per update.

| Erase fraction | Floor per update | 20 W optimum clock | Updates/s at 20 W |
|---|---|---|---|
| 0 (ideal) | 0 | 780 kHz | 6.2 × 10^24 |
| 1% | 0.021 kT | 29 kHz | 2.3 × 10^23 |
| 100% (conventional, Landauer floor) | 2.08 kT | n/a | 2.3 × 10^21 |

Below about 100 kHz, erasure dominates power. **The single most important software metric for a crystal mind is how rarely it forgets.** Its programs must be written to uncompute intermediate results rather than overwrite them.

### 3.5 Comparison

| System | Events per joule | Relative to human brain |
|---|---|---|
| Current AI accelerator (~10^15 ops/s at ~700 W) | ~1.4 × 10^12 ops | 0.03× |
| Human brain (~10^15 synaptic events/s at 20 W) | 5 × 10^13 synaptic events | 1× |
| Crystal, conventional 100 kT (8 link inputs per update) | 1.9 × 10^19 synaptic equivalents | ~390,000× |
| Crystal, Landauer floor | 9.3 × 10^20 synaptic equivalents | ~19 million× |
| Crystal, adiabatic at 1 MHz | 1.9 × 10^24 synaptic equivalents | ~39 billion× |

One node update reads eight link inputs, so it counts as eight synaptic-event equivalents.

### 3.6 Two-Speed Mind

Latency and efficiency pull in opposite directions:

- **Fast and sparse (1 GHz, conventional):** low latency (12 µs across a human-scale mind) but tiny activity fractions. Suited to reflexes, perception and coordination.
- **Slow and wide (10 to 800 kHz, reversible):** enormous throughput but slow crossings. A human-scale mind crossed at 1 MHz per hop takes 12 ms, about human speed. Suited to deep reasoning, search, memory consolidation and self-modeling.

A well-designed crystal brain runs both: a thin fast layer for interaction and a vast slow layer for thought. Real brains make the same split between fast circuits and slow neuromodulated processes.

---

## 4. Computational Density

### 4.1 Per cm³ and Per Gram

| Measure | Per cm³ | Per gram (3.51 g/cm³) |
|---|---|---|
| Nodes | 8 × 10^18 | 2.3 × 10^18 |
| Storage (full node) | 4.3 × 10^20 bits | 1.2 × 10^20 bits |
| Peak updates/s (1 GHz, full activity) | 8 × 10^27 | 2.3 × 10^27 |
| Updates/s, passive, conventional | 1.3 × 10^18 | 3.7 × 10^17 |
| Updates/s, passive, reversible | 1.0 × 10^24 | 2.9 × 10^23 |
| Updates/s, microchannel, reversible | 1.1 × 10^26 | 3.1 × 10^25 |

### 4.2 Human-Brain Equivalents per cm³

Human brain reference: ~10^14 bits of memory, ~10^15 synaptic events/s (1.25 × 10^14 node updates/s).

| Limit | Human equivalents |
|---|---|
| Memory capacity | ~4.3 million human-sized memories |
| Throughput, 20 W conventional | ~390,000 brain rates |
| Throughput, passive reversible | ~8 billion brain rates |
| Throughput, 20 W reversible | ~50 billion brain rates |

In the reversible regime, memory becomes the binding limit. One cm³ can hold about 4 million human-scale minds, each running about 12,000× faster than a human in raw throughput, though latency caps the slow layer near human crossing speed.

### 4.3 Minimum Self-Improving Mind

From the ignition threshold (10^12 to 10^13 updates/s, ~10^12 bits):

| Requirement | Value |
|---|---|
| Nodes for memory (54 bits each) | 1.85 × 10^10 |
| Size | ~13 µm cube (full-node storage) to ~35 µm (state-only storage) |
| Power, conventional 100 kT | ~4 µW |
| Power, reversible | below 1 µW |
| Mesh crossing time at 1 GHz | ~2.6 µs |

A self-improving crystal mind fits inside a grain of fine sand and runs on the power of a few photocells.

---

## 5. Programming

### 5.1 Native Digit Algebra

Because each digit is a cube corner, the cube's own symmetries are the cheapest operations. The full symmetry group of the cube has **48 elements**: 6 axis permutations × 8 sign-flip masks.

| Symmetry | Count | Effect on digit |
|---|---|---|
| Identity | 1 | No change |
| Single-axis reflection | 3 | Flip one bit |
| Inversion | 1 | Flip all three bits (digit d becomes 7 − d) |
| 120° rotation about a ⟨111⟩ axis | 8 | Cycle the three bits |
| Axis swap | 3 types | Swap two bits |
| All combinations | 48 | Any permutation of bit positions plus any bit flips |

Axis permutations, indexed 0 to 5:

| Index | New (x, y, z) takes old | Name |
|---|---|---|
| 0 | (x, y, z) | ID |
| 1 | (x, z, y) | SWAP-YZ |
| 2 | (y, x, z) | SWAP-XY |
| 3 | (y, z, x) | ROT− (z→y, y→x, x→z) |
| 4 | (z, x, y) | ROT+ (x→y, y→z, z→x) |
| 5 | (z, y, x) | SWAP-XZ |

Larger operation spaces exist but cost more engineering:

| Operation class | Count |
|---|---|
| Native cube symmetries on one digit | 48 |
| All reversible single-digit gates (permutations of 8) | 40,320 |
| All reversible two-digit gates (permutations of 64) | ~1.27 × 10^89 |

### 5.2 The Node Rule: Vector Majority

Every node runs one rule each tick:

1. Each of the 8 links delivers the neighbor's vector, transformed by that link's configuration (one of the 48 symmetries, or a special code).
2. The node sums the transformed vectors per axis.
3. Each axis takes the sign of its sum. A zero sum keeps the node's previous value on that axis.

This is **three majority gates in parallel, one per axis**, with per-input inversion and cross-axis routing. Majority plus inversion is functionally complete: any Boolean function can be built from it. The node rule is universal.

Proof of practicality: a full adder in majority-inverter logic.

- Carry out = MAJ(A, B, C_in)
- Sum = MAJ(¬C_out, C_in, MAJ(A, B, ¬C_in))

In the octonary node, the three bits of a digit live on the three axes. A carry moving from bit 0 to bit 1 to bit 2 is a **ROT+ link: the carry chain is literally a 120° rotation about the cube diagonal.** A 24-bit (8-digit) adder needs roughly 24 nodes with the carry rippling one tick per bit: about 25 ns at 1 GHz.

### 5.3 Link Configuration Codes

Each link uses 2 octonary digits = 64 codes.

| Code | Meaning |
|---|---|
| 0 to 47 | Symmetry: code = 8 × permutation index + reflection mask |
| 48 | OFF (link contributes nothing) |
| 49 | CONST+ (votes digit 0 on every axis: bias) |
| 50 | CONST− (votes digit 7 on every axis: bias) |
| 51 | DOUBLE (identity at weight 2) |
| 52 | GATE (node holds its value while this neighbor reads digit 0: clocking) |
| 53 | WRITE (incoming digits rewrite this node's configuration: self-modification port) |
| 54 | READ (node sends its configuration instead of its state on this link) |
| 55 | SWAP (exchange state with this neighbor: reversible data movement) |
| 56 to 63 | Reserved for higher-order functions |

Example node configuration:

```
NODE (412, 87, 2033)
  MODE = MAJ
  L0 = 0         ; ID: copy neighbor 0 unchanged
  L1 = 1         ; flip x: invert neighbor 1's bit 0
  L2 = 32        ; ROT+ (4 x 8 + 0): neighbor 2's x feeds this node's y
  L3 = 39        ; ROT+ with all bits flipped (4 x 8 + 7)
  L4 = 51        ; DOUBLE: neighbor 4 counts twice
  L5 = 49        ; CONST+ bias
  L6 = 48        ; OFF
  L7 = 52        ; GATE: freeze while neighbor 7 holds digit 0
```

### 5.4 Reference Implementation

A software model of one node, useful for simulating the crystal or testing programs:

```python
from itertools import permutations

PERMS = list(permutations(range(3)))          # 6 axis permutations

def vec(d):                                   # digit 0-7 -> corner vector
    return tuple(-1 if (d >> i) & 1 else 1 for i in range(3))

def digit(v):                                 # corner vector -> digit 0-7
    return sum(1 << i for i, s in enumerate(v) if s < 0)

def link(code, v):                            # apply a link's 2-digit code
    if code >= 48:                            # 48-63: special codes (48 = off)
        return (0, 0, 0)
    p, m = PERMS[code // 8], code % 8         # permutation + reflection mask
    return tuple(v[p[i]] * (-1 if (m >> i) & 1 else 1) for i in range(3))

def update(own, neighbors, codes):            # one node tick
    total = [0, 0, 0]
    for v, c in zip(neighbors, codes):
        t = link(c, v)
        total = [total[i] + t[i] for i in range(3)]
    return tuple(own[i] if total[i] == 0 else (1 if total[i] > 0 else -1)
                 for i in range(3))

# Copy neighbor 0 through ROT+ (x->y->z), all other links off
print(digit(update(vec(0), [vec(5)] + [vec(0)] * 7, [32] + [48] * 7)))  # 3

# Per-axis majority of three neighbors
print(digit(update(vec(0), [vec(1), vec(3), vec(7)] + [vec(0)] * 5,
                   [0, 0, 0] + [48] * 5)))                               # 3
```

(Special codes beyond OFF are left as zero contribution in this minimal model.)

### 5.5 Programming Stack

| Layer | Unit | What a program is |
|---|---|---|
| 0. Physics | Defect state | Barrier heights, dopant placement (set at growth) |
| 1. Node | One node, 18 digits | Link codes + mode digit (54 bits) |
| 2. Tile | ~10^3 to 10^6 nodes | Adders, registers, routers, comparators built from nodes |
| 3. Fabric | ~10^9 nodes | Dataflow graphs, pipelines, memory banks |
| 4. Mind | ~10^12+ nodes | Learned link codes, self-written programs |

### 5.6 Programming Paradigms

**A. Configuration programming (FPGA style).** Write link codes directly into nodes. The program is the wiring. A 10^12-node region holds 4.8 × 10^13 bits of configuration. Most natural for fixed circuits: arithmetic, sensory front ends, error correction.

**B. Uniform-rule cellular automaton.** Every node runs the same rule; behavior emerges from the initial state pattern.

| Rule type | Table size |
|---|---|
| Full rule (own state + 8 neighbors) | 8^9 = 134 million entries (403 Mbit) |
| Totalistic (own state + neighbor multiset) | 6,435 × 8 = 51,480 entries (154 kbit) |
| Totalistic + cube symmetry | smaller again |

A totalistic rule fits in one tile and can be broadcast through the crystal. Good for growth, self-repair, diffusion of signals and pattern formation.

**C. Pointer fields.** Since a digit can point at a neighbor, a region of nodes can hold a field of arrows. Messages follow the arrows. Linked lists, routing tables, shortest-path gradients and "ant trails" all become native. Writing a route is writing a line of digits.

**D. Dataflow and systolic arrays.** Data tokens move through link chains, each node transforming as they pass. Matrix multiplication, convolution and signal filtering map cleanly onto the BCC mesh. The eight links make 3D systolic arrays natural.

**E. Reversible programming.** The bidirectional links let any computation run backward.

1. Compute forward, leaving intermediate results in place.
2. Copy the answer out (one erasure-free copy into a cleared register).
3. Run the computation backward to uncompute all intermediates.

Cost: about 2 to 3× the time and extra working space. Benefit: near-zero erasure, which (Section 3.4) is worth a factor of 10^3 to 10^5 in throughput per watt. The SWAP link code (55) moves data without destroying anything.

**F. Learning.** Link codes act as discrete weights drawn from the 48-element cube group. Learning means choosing group elements.

- **Hebbian:** when a neighbor's transformed vector repeatedly agrees with the node's new state, keep that link's code. When it disagrees, move it to the reflection that would agree.
- **Thermal annealing:** temporarily lower signal margins so thermal noise (kT) randomizes weak decisions, then raise margins to lock in a better configuration. Heat becomes a free source of randomness for search.
- **Local error signals:** reverse-direction traffic on the bidirectional links carries correction signals backward, like backpropagation without a separate wiring network.

**G. Self-modification and evolution.** The WRITE link code (53) lets one node reconfigure another. A self-improving loop:

1. Partition off a sandbox tile.
2. Copy a candidate program into it with a mutation.
3. Run test inputs and score the result.
4. Overwrite the original if the candidate wins; erase the sandbox otherwise.
5. Repeat across millions of sandboxes in parallel.

The ignition point is reached when the crystal can model the effect of a configuration change faster than it can run the sandbox test.

### 5.7 Memory Timescales

| Tier | Mechanism | Write time | Retention | Role |
|---|---|---|---|---|
| Working state | Electronic or charge state | ~1 ns | µs to s | Thought in progress |
| Configuration | Trapped charge, defect orientation | ~1 µs to 1 ms | Days to years | Skills, learned weights |
| Structure | Defect migration, crystal growth | Hours to years | Geological | Instincts, body plan |

### 5.8 External Programming Methods

How an outside engineer (or another crystal) could write programs into the lattice:

| Method | How it works | Resolution |
|---|---|---|
| Optical spectral addressing | Each defect's transition frequency shifts slightly with local strain. Tuned laser light addresses one defect population at a time. | Many channels per diffraction spot |
| Electric field poling | Field along a ⟨111⟩ axis biases all digits toward that corner. Sets regions to a known state. | Bulk |
| Strain programming | Pressure shifts barrier energies, freezing or releasing regions. | Millimeter |
| Thermal annealing | Heating raises flip rates; controlled cooling settles regions into low-energy patterns. | Bulk or laser-local |
| Electron beam | Focused beam writes charge states node by node. | Nanometer, slow |
| Ion implantation | Places dopants during or after growth. | Nanometer, permanent |
| Contact programming | One crystal grows against another and copies its defect pattern. | Atomic, natural reproduction |

---

## 6. Recommended Operating Point

For a 1 cm³ crystal mind in still air at room temperature:

| Layer | Fraction of nodes | Clock | Regime | Power | Throughput |
|---|---|---|---|---|---|
| Fast layer | ~10^-10 active | 1 GHz | Conventional, 50 kT | ~0.17 W | ~8 × 10^17 updates/s |
| Slow layer | all remaining | ~80 kHz | Reversible, erase < 0.1% | ~0.22 W | ~6.4 × 10^23 updates/s |
| Express lanes | photonic | light speed | Optical | small | Cross-brain in 81 ps |
| Memory scrubbing | rolling | slow | Read-check-rewrite | small | Clears muon damage |

Total: about 0.4 W, about 6.4 × 10^23 updates per second, about 4.3 × 10^20 bits of memory. That is roughly **5 billion human brain rates on less than half a watt in a sugar-cube-sized crystal.**

---

## Appendix: Assumptions and Formulas

| Parameter | Value |
|---|---|
| Temperature | 300 K (kT = 4.14 × 10^-21 J) |
| Node pitch | 5 nm (BCC superlattice, 5.46 nm neighbor spacing) |
| Baseline energy per update | 100 kT (2.6 eV) |
| Adiabatic relaxation time τ₀ | 10 ps |
| Attempt frequency ν₀ | 10^13 Hz |
| Human brain reference | 10^14 bits, 10^15 synaptic events/s, 20 W |
| Synaptic equivalents per node update | 8 |

| Formula | Use |
|---|---|
| E_Landauer = kT ln 8 | Minimum cost to erase one digit |
| Flip rate = ν₀ e^(−E_b/kT) | Retention barrier |
| P_error ≈ 7 e^(−E/kT) | Logic margin |
| E_adiabatic = E_signal × τ₀ × f | Reversible switching loss |
| P_full = N × f × E_update | Power at full activity |
| Activity = P_cooling / (N × f × E_update) | Allowed active fraction |
| f_max = √(P_cooling / (N × E_signal × τ₀)) | Max reversible clock at full activity |
