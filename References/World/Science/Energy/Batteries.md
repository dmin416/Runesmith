# Batteries

Chemical cells vs mana stones for invent beats. Stone law: `../../Materials/MonsterCores.md`. Size tables: `ManaStones.md`. Mana joules: `../../../Runes/Energy.md`. Carbon / graphite craft: `../Invent/WritingTools.md`, `../Metallurgy/EarthAlloys.md`. Do not paste Earth brand names into prose unless the story invents them.

## Narrative

Mana stones already win portable energy for most gear. Chemical batteries matter when someone wants **voltage without a stone socket**, Earth-memory demos or gadgets that must not sip mana. Near-reach invents stop around wet and dry zinc cells. Lithium and molten-sodium stay hard prestige.

## Battery: The Concept

A battery stores energy in chemicals and releases it as electricity through a controlled chemical reaction.

- **Two electrodes:** the anode (negative) gives up electrons easily. The cathode (positive) takes them in.
- **Electrolyte:** a material between them that lets charged atoms (ions) travel but blocks electrons.
- **Separator:** keeps the electrodes from touching, which would short the cell.
- **How it works:** electrons cannot cross the electrolyte, so they take the outside path through the circuit to reach the cathode. That flow is the electric current. Ions cross inside the battery at the same time to balance the charge.
- **Voltage:** set by how strongly the two electrode materials differ in their pull on electrons. A larger difference gives higher voltage per cell.
- **Capacity:** set by how much reactive material is in the cell.
- **Rechargeable vs single use:** in rechargeable cells the reaction can be pushed backward by applying outside current. In single-use cells it cannot.
- **Stacking:** cells connected in series add voltage. Cells connected in parallel add capacity.

The simplest classroom example is the lemon or potato battery: two different metals pushed into acidic fruit produce a small measurable voltage.

## Detail

### Stone vs battery (compare only)

Stone law stays in `MonsterCores.md` / size tables in `ManaStones.md`. Compare figure from that law:

```
Wh/kg ≈ 1,050   // any Q; size-only mass
Wh/L  ≈ 2,780
P_sustain (W) ≈ (Input / 60) × 10   // Input from MonsterCores
```

| Need | Prefer |
|---|---|
| Dense reusable mana | Stone (size for tank, Q for recharge) |
| True volts without mana | Voltaic / Daniell / dry cell invent |
| Earth consumer portable | Alkaline → Li-ion ladder (below) |

Common stone still beats commercial cells on Wh/kg by roughly **2×–12×** and matches projected practical Li-air. Loses to gasoline chemical energy and to theoretical Li-air ceilings. No battery matches indefinite ambient recharge.

Rough size checks at Q1 (street pegs from `ManaStones.md`; L bands from `MonsterCores`):

| Band | Cap (mana) | Energy | Mass | Notes |
|---|---|---|---|---|
| Rice | **19** | ~0.05 Wh | ~0.05 g | Street peg |
| Leader | **95** | ~0.26 Wh | ~0.25 g | **5×** rice |
| Marble | **2,145** | ~6 Wh | ~5.7 g | 16 mm street peg |
| Fist | **268,080** | ~745 Wh | ~0.71 kg | 80 mm |

### Caldris invent ceiling

**Near reach:** voltaic pile, Daniell, Leclanché / zinc-carbon wet or dry, simple zinc-air demos if KOH/salts and carbons exist.

**Hard:** NiFe (caustic KOH), any lithium or molten-sodium chemistry (dry rooms, fire). Thermal (pyro) batteries and hot salt rechargeables sit here too.

**Usual power path:** stones and runic reservoirs. Chemical cells are the side door.

### Era ladder (Wh/kg order of magnitude)

| Era | Cell | Wh/kg band | Note |
|---|---|---|---|
| Disputed antiquity | "Baghdad" jar | negligible | May never have been a battery |
| 1800 | Voltaic pile | negligible | First true stack |
| 1836 | Daniell | ~10 | Steady telegraph voltage |
| 1866 | Leclanché | ~20 | Wet MnO₂ |
| 1886 | Zinc-carbon dry | 35–100 | First portable consumer |
| 1901 | Nickel-iron | 30–50 | Abuse-tolerant |
| 1959 | Alkaline | 100–150 | Standard primaries |
| 1970s | Li primary / zinc-air | 280–500 / 300–450 | Long shelf / air cathode |
| 1991+ | Li-ion / LFP | 100–270 / 90–180 | Rechargeables |
| Emerging | Si-anode, solid-state, Li-S | 300–600 practical | Prestige |
| Theory | Li-air | 1,000–3,500+ | Chart top; not a shop build |

### Home-build gist (near-reach)

**Voltaic pile:** Cu / brine cloth / Zn discs stacked. ~0.7–1 V per cell.

**Daniell:** Cu in CuSO₄ outside porous cup; Zn in ZnSO₄ inside. ~1.1 V steady. Gravity cell: dense CuSO₄ bottom, light ZnSO₄ top, no pot.

**Leclanché:** Zn rod + NH₄Cl; porous pot packs MnO₂/graphite around carbon. ~1.5 V, rests to recover.

**Zinc-carbon dry:** Zn cup, paste separator, MnO₂/graphite around carbon, wax seal. ~1.5 V.

**NiFe:** caustic KOH, nickel and iron packed plates. ~1.2 V, decades if you can handle the alkali.

Later Li-ion / solid-state / Li-air stay industrial or lab summaries only until a beat needs process detail. Pull Old file scraps then.

### Pyro battery (thermal battery)

Earth encyclopedia / hard invent. Single-use cell whose electrolyte is a **solid salt at room temperature**. Almost no conduction in storage → **20+ year** shelf with near-zero self-discharge.

**Activation:** Electric igniter or percussion primer fires pyrotechnic heat pellets (usually iron powder + potassium perchlorate) stacked between cells. Heat melts the salt electrolyte (commonly LiCl/KCl, ~**350 °C**). Inert → full power in a fraction of a second to a few seconds.

**Output:** Very high power until the stack cools and the salt refreezes. Run time: seconds to about an hour. Then spent.

**Chemistry:** Modern: Li-Si or Li-Al anode + FeS₂ cathode. Older: Ca / calcium chromate.

**Earth uses:** Missiles, guided munitions, nuke systems, ejection seats, aircraft emergency power, sonobuoys. History: Georg Otto Erb (Germany, WWII; V-weapons); US programs refined after.

**Terra note:** Prestige / invent only. Stones already cover long shelf + dump; a pyro pack is the chemical analog of “wake a dead reserve for one hard burst.”

### Salt battery (loose label)

Several chemistries share the name:

1. **Sodium-nickel chloride (ZEBRA):** Most often sold as “salt battery.” Molten Na anode, NiCl₂ cathode, ceramic β-alumina electrolyte. ~**270–350 °C**. Rechargeable. Grid, telecom backup, some buses.
2. **Sodium-sulfur (NaS):** Hot molten-electrode rechargeable, ~**300–350 °C**. Large grid storage.
3. **Sodium-ion:** Room temperature, like Li-ion but Na ions. Cheap, safer, better in cold; lower Wh/kg than Li-ion.
4. **Saltwater:** Water-based Na salt electrolyte. Non-flammable, non-toxic, low energy density. Stationary only.

### Core difference (thermal vs salt)

| Kind | Heat | Life |
|---|---|---|
| **Thermal / pyro** | Fired once by pyrotechnics | One-shot; seconds to ~1 h; spent |
| **ZEBRA / NaS** | Kept hot continuously | Rechargeable; thousands of cycles |
| **Na-ion / saltwater** | None | Ordinary recharge / stationary |

All of the hot chemistries stay **hard invent** on Caldris. Stones win unless the beat wants volts with no mana socket.

### Rule of thumb

| Job | Pick |
|---|---|
| Spell / rune / train tank | Mana stone |
| Spark gap / telegraph / LED-class invent without mana | Wet/dry Zn cell |
| Abuse-proof shop standby | NiFe if alkali exists |
| Phone/EV Earth parity | Li-ion (invent fiction or import knowledge) |
| Decades shelf, one hard chemical burst | Thermal / pyro battery (hard invent) |
| Hot grid / bus chemical store | ZEBRA / NaS (hard invent) |

## Open

- Converter path: mana → volts (wear on path, not stone cycle fade)
- Full industrial cell recipes if a factory arc needs them
- Pyro pellet / LiCl-KCl shop recipe if a munition or emergency-power beat needs it
