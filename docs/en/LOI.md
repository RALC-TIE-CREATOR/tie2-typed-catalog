# Letter of Intent — Anthropic AI for Science — v2.0

**Date:** 2026-11-16
**Applicant:** Rubén Antonio Lecona Curto (R@LC)
**Institution / PI:** [pending affiliation]
**Program:** Anthropic AI for Science — up to USD 50,000 in Claude credits per project
**Duration:** 6 months
**Title:** *A Typed, Machine-Checkable Catalog of Physical Quantities: Formalizing TIE 2 in Lean 4 with Claude*

---

## 1. Summary

Standard physics notation conflates quantities that share dimensions but are not the same thing: torque and energy, pressure and energy density, frequency and angular velocity. Dimensional algebra does not detect those category errors.

TIE 2 proposes a typed grammar: four entities (Space, Time, Phase, Physical), rules R-01–R-12, and a catalog of **254 unique combinations** (35 standard, 4 label, 2 bridge, 213 candidates).

This project formalizes and verifies that catalog in **Lean 4**, using Claude as a generator, classifier, and counterexample engine. The goal is not to prove a new physical theory. It is to build an **open, typed, machine-checkable artifact** that detects category errors and explores a physical language systematically.

---

## 2. Prototype already built

| Element | Status |
|---|---|
| 254-entry dataset | `catalog254.json` / `catalog254.csv` |
| Lean 4 project | `lean-tie2/` with `lakefile.lean` and `lean-toolchain` |
| Admissibility rules | `L ∈ [-3,3]`; `T,R,V,Wb,Gr ∈ {-1,0,1}` |
| Rejection tests | `T⁻²`, `L⁴`, `R²` → `false` |
| Lean catalog | `catalog254.length = 254`; all entries admissible |
| Build | `lake build` — 6 jobs, exit 0 |

The prototype shows that the grammar is formalizable and that the checker rejects forbidden units.

---

## 3. Research question

> Can a typed proof assistant, assisted by an LLM, formalize and verify a 254-entry physical catalog, detect category errors in standard notation, and produce a reproducible benchmark?

---

## 4. Method

1. **Formalize R-01–R-12** in Lean 4: dimensions, tensor types, classes, domains, processes vs. units.
2. **Encode the 254 entries** as a typed, reproducible dataset.
3. **Use Claude** to draft definitions, type proofs, and counterexamples.
4. **Human review + `lean`** as the final arbiter.
5. **Open benchmark:** given a physical statement, decide whether it is admissible, a process, or an invalid sum.

---

## 5. Deliverables

- Lean 4 library for R-01–R-12.
- Open dataset of 254 entries with dimension, type, class, and status.
- Benchmark of 200–500 valid/invalid statements.
- 8–12 page preprint.
- Reproducible repository with CI.
- Report of detected category errors.

---

## 6. Evaluation

| Metric | Target |
|---|---|
| R-01–R-12 coverage | 100% |
| Entries typed in Lean | 254/254 |
| Type-check rate | ≥ 95% |
| Documented category errors | ≥ 20 |
| Human–Claude agreement on benchmark | ≥ 90% |
| Formalization time reduction | ≥ 30% vs. manual baseline |

---

## 7. Six-month plan

| Month | Milestone |
|---|---|
| 1 | R-01–R-06; 254 entries (already started) |
| 2 | R-07–R-12; type/class rules |
| 3 | Initial benchmark of 200–500 statements |
| 4 | Claude-assisted proofs; expanded benchmark |
| 5 | Preprint and external review |
| 6 | Final repository, CI, and publication submission |

---

## 8. Budget

| Item | Estimate |
|---|---|
| Claude credits | up to USD 50,000 |
| Lean/CI compute | USD 3,000–5,000 |
| Dissemination / preprint | USD 2,000 |
| No salary requested from the program | — |

---

## 9. Why Anthropic

- AI for Science supports high-impact scientific projects with Claude credits; this project uses the model as a formalization engine, not as a text generator.
- The output is an open, verifiable artifact: Lean, dataset, benchmark, and preprint.
- The prototype already exists and builds; technical risk is low.

---

## 10. Risks and mitigation

| Risk | Mitigation |
|---|---|
| The catalog is too broad | 254 entries already encoded; 50-entry subset as regression |
| Claude hallucinates proofs | Lean verifies; human review by sample |
| Lack of affiliation | Seek an academic or nonprofit PI |
| Theory not empirically validated | Presented as formalization, not as confirmed theory |

---

## 11. Affiliation and team

- **PI:** [pending]
- **Institution:** [pending]
- **Collaborators:** [pending]
- **Repository:** https://github.com/RALC-TIE-CREATOR/tie2-typed-catalog

---

## 12. Next step

- Confirm PI/affiliation.
- Publish the Lean repo and dataset.
- Submit the application to AI for Science with this package.

---

## 13. Change log

- **v0.1 (2026-11-16):** initial draft.
- **v1.0 (2026-11-16):** Lean prototype of 50 entries compiled; metrics and six-month plan.
- **v2.0 (2026-11-16):** full 254-entry catalog encoded and compiled; public repository.
