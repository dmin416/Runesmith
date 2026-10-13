# Blood Tech

> Earth craft catalog. Not locked law. Caveman-scale human blood products from a centrifuge, a vacuum chamber, ordinary chemistry, and universal filters. Rows marked **(beyond real filters)** go past real filter technology and stay marked that way. WWI and WWII method names (Rous-Turner, Cohn fractionation, pooled-plasma hepatitis) are Earth history anchors.

Blood color, clot, and animal volume stay in `BloodNotes.md`. Blood restore rates, the Recovery skill, and survivable blood-loss uses stay in `../../../Progression/Attributes.md`, `../../../Progression/SkillsDesign.md`, and `../../../Progression/MultiMechanismResistance.md`. Health points are not blood volume. Ned's daily whole-blood drip stays in `../../../People/NedDesign.md`. Saline here is intravenous fluid. It is not a rune path. Path law stays in `../../../Runes/ManaMaterials.md`. Chamber walls, seals, and pumps stay in `../Metallurgy/SteelVacuumChamber.md` and `../Metallurgy/Vacuum.md`. This file is the blood process those tools can run.

---

## Filtration Capability

The filters can separate almost anything from anything. Some uses match real filter technology. Others go beyond what real filters can do and are marked **(beyond real filters)**.

| Filter type | Removes / separates | Real-world basis |
|---|---|---|
| Sterile filter (0.2 µm) | Bacteria, fungi, parasites | Real |
| Virus nanofilter (15 to 20 nm) | Hepatitis B, hepatitis C, HIV, most other viruses | Real |
| Leukoreduction filter | White blood cells | Real |
| Ultrafilter (about 10 kDa) | Pyrogens and endotoxin | Real |
| Protein-size filters (about 100 to 300 kDa cutoffs) | Splits plasma proteins by size | Real but imprecise |
| Sizing membrane (about 250 nm) | Forces lipid vesicles to a uniform size | Real |
| Chemical-selective filter | Pulls one specific compound out of a mixture | Beyond real filters |
| Antibody-selective filter | Removes only anti-A and anti-B antibodies | Beyond real filters |
| Oxidation-state filter | Removes methemoglobin, keeps working hemoglobin | Beyond real filters |

## Ranking

### 1. Crossmatched fresh whole blood

Still the best option for massive bleeding. Filtration makes it safer and lets it last longer.

**Testing compatibility without antisera:**

- Spin both donor and recipient blood.
- Mix a drop of recipient serum with a drop of donor cells on glass at body temperature. Clumping within a few minutes means reject.
- Run the reverse test as well (donor serum with recipient cells).
- This catches ABO incompatibility and most other major mismatches.
- Serum from known type A and type B people can be kept as permanent typing reagents.

**Anticoagulant (sodium citrate):**

- Make soda ash by burning saltwort or kelp, then leaching and evaporating the ash.
- Neutralize lemon or lime juice with the soda ash. The result is crude sodium citrate.
- **Filter upgrade (beyond real filters):** A chemical-selective filter pulls pure sodium citrate out of the crude mix and leaves behind the other fruit acids and plant residue.
- Sterile-filter the finished solution.
- Target roughly 3.8% strength. Use 1 part citrate to 9 parts blood.
- Adding glucose (grape sugar or crystallized honey glucose) extends cell life. This is essentially WWI Rous-Turner solution. Purify the glucose with the same chemical-selective filter.

**Filter upgrades to the blood itself:**

- **Leukoreduction:** Run the blood through a leukoreduction filter right after collection. This cuts fever reactions, slows cell breakdown during storage and lowers the chance of the recipient developing antibodies.
- **Pathogen screening:** Pass the blood through a filter that holds back bacteria and parasites but lets red cells through. Real filters can't do this cleanly because red cells are about 7 µm across and must squeeze through, so this counts as **beyond real filters**. It removes malaria, syphilis and bacterial contamination.

**Storage:**

- On ice or in a cold spring cave: about 4 to 5 weeks with leukoreduction and purified citrate-glucose.
- At room temperature: a few days.

### 2. Artificial red cells (Nara HbV style)

Filtration moves this from last resort to second place. It is the only product on the list that carries oxygen, needs no typing and stores at room temperature.

**Process:**

1. Lyse expired red cells in distilled water.
2. Spin hard to remove the cell membranes (stroma).
3. Sterile-filter, then virus-nanofilter, the hemoglobin solution.
4. Heat at 60°C for 10 hours to kill any remaining viruses. Protect the hemoglobin from heat damage by bubbling in carbon monoxide first. Wood smoke passed through a chemical-selective filter supplies pure CO.
5. Make a lipid film from egg yolk lecithin plus cholesterol, drying it under vacuum.
6. Rehydrate the film with concentrated hemoglobin.
7. Push the mixture repeatedly through a sizing membrane until the vesicles are about 250 nm. This matches the size used for real HbV.
8. Ultrafilter out any hemoglobin left outside the vesicles. The vesicles are thousands of times larger than free hemoglobin, so this separation works cleanly.
9. Expose the product to bright light under pure oxygen to strip off the carbon monoxide.
10. Run an oxidation-state filter to remove methemoglobin **(beyond real filters)**. Add ascorbic acid from citrus to slow further buildup.
11. Final sterile filtration and pyrogen ultrafiltration.

**Storage:**

- Sealed under vacuum or nitrogen, the vesicles last about 1 to 2 years at room temperature.

**Remaining weaknesses:**

- Real HbV is coated with polyethylene glycol to keep vesicles from clumping and to slow removal by the body. Without that coating, the vesicles circulate for a shorter time and clump more.
- Oxygen affinity can't be tuned the way modern versions are tuned, so oxygen release in tissues is less efficient.
- Use it as a bridge to keep someone alive until real blood arrives, not as a full replacement.

### 3. Freeze-dried universal plasma

1. Centrifuge citrated blood and draw off the plasma.
2. Virus-nanofilter the plasma. This removes the hepatitis risk that plagued WWII pooled plasma and makes large pools safe.
3. **Universal plasma:** Run an antibody-selective filter to remove anti-A and anti-B **(beyond real filters)**. The plasma can then be given to anyone. Without this filter, a 300 kDa size cutoff removes most anti-A and anti-B (which are mostly very large IgM antibodies) but also strips out fibrinogen, the main clotting protein.
4. Freeze it solid. A snow and salt mix reaches about -20°C.
5. Pull a vacuum while keeping the plasma frozen so the ice sublimates.
6. Put a tray of quicklime (burnt limestone) inside the chamber. It absorbs the water vapor and stands in for a cold trap. This also makes up for a weak hand-pumped vacuum.
7. Seal the powder in wax-sealed glass.

**Shelf life:** Years at ambient temperature. Reconstitute with filtered water.

**Uses:** Hemorrhagic shock, burns and clotting failure. No typing is needed.

### 4. Albumin and immune globulin

Filtration replaces most of the difficult Cohn fractionation chemistry.

**Process:**

1. Start with virus-filtered plasma.
2. Run protein-size filters in sequence:
   - About 300 kDa cutoff holds back fibrinogen and IgM.
   - About 100 kDa cutoff holds back IgG (immune globulin).
   - Albumin (about 66 kDa) passes through and is caught on a smaller filter.
3. Without chemical-selective help, the size cuts are messy because the proteins overlap in size. With a chemical-selective filter **(beyond real filters)**, each fraction comes out pure.
4. Use ultrafiltration to concentrate each fraction and swap it into clean saline.
5. Add caprylate to the albumin as a stabilizer. It can be made by saponifying coconut oil or goat milk fat and then purified by filter.
6. Hold the albumin at 60°C for 10 hours as a backup virus kill.

**Products:**

- **Albumin:** A volume expander that stays stable at room temperature for years.
- **Immune globulin (IgG):** Collected from people who survived a disease, it gives temporary protection against that disease. It works against tetanus, rabies, measles and hepatitis A if collected from recovered or immunized donors.
- **Fibrinogen concentrate:** Treats bleeding from clotting failure. Freeze-dry for storage.

### Baseline: IV fluid

- Filtered water with 9 g salt per liter (0.9% saline)
- Pyrogen ultrafiltration replaces distillation.
- Sterile filtration replaces pressure sterilization.
- Purify the salt with a chemical-selective filter to remove magnesium, heavy metals and other contaminants.
- For a Ringer's-type solution, add potash leach for potassium and chalk dissolved in vinegar for calcium. Filter each additive the same way.

## Hardware

**Centrifuge:**

- Hand crank geared about 50:1 gives roughly 3,000 rpm.
- With a 20 cm arm, that produces about 2,000 g, which is enough to pack red cells.

**Filters:**

- Gravity feed works for water and saline.
- Plasma and protein solutions filter faster under pressure from a hand pump or a raised reservoir.
- The vacuum chamber can pull liquid through a filter from the other side.

**Sterilization:**

- Sterile filtration handles most liquids.
- Metal tools and containers still need a sealed bronze or clay pressure vessel at about 121°C, or boiling followed by vacuum sealing.

**Needles and lines:**

- Drawn bronze tubing or quills for needles
- Cleaned animal intestine for tubing
