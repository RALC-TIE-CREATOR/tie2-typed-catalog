# TIE 2 — Typed Catalog of Physical Quantities

A prototype for a **typed, machine-checkable catalog of physical quantities**. It formalizes the admissibility rules of TIE 2 in Lean 4 and provides the full 254-entry catalog.

**Status:** prototype. 254/254 entries; Lean build passes; `T⁻²`, `L⁴`, and `R²` are rejected. This is not a validated physical theory.

**Repository:** https://github.com/RALC-TIE-CREATOR/tie2-typed-catalog

[Español](README.es.md)

## Why

Standard physics notation conflates quantities that share dimensions but are not the same thing: torque and energy, pressure and energy density, frequency and angular velocity. Dimensional analysis alone does not catch those category errors.

TIE 2 proposes a typed grammar:

- four entities: Space, Time, Phase, Physical;
- rules R-01–R-12 for admissibility;
- a catalog of 254 unique combinations (35 standard, 4 label, 2 bridge, 213 candidates).

This repository tests whether that grammar can be formalized and verified.

## What is here

```
data/                 254-entry dataset (JSON + CSV)
lean-tie2/            Lean 4 project
docs/en/              English documentation
docs/es/              Spanish documentation
```

## Quick start

```bash
cd lean-tie2
lake build
```

Expected: `TIE2.Dimensions`, `TIE2.Catalog`, `TIE2.Examples` compile; `catalog254.length = 254`; all entries pass `admissibleB`; `T⁻²`, `L⁴`, `R²` fail.

## Dataset

`data/catalog254.json` and `data/catalog254.csv` contain 254 entries:

| Block | Entries |
|---|---|
| Level 1 units | 16 |
| R4 GET | 52 |
| R5 S,T,Fi | 60 |
| R6 T,F,Fi | 18 |
| R7 S,F,Fi | 36 |
| R8 S,T,F,Fi | 72 |

Each entry declares: id, level, expression, unit, dimension vector `L,T,R,V,Wb,Gr`, kind, tensor type, status, source, and note.

## Verification

- JSON: 254 entries.
- CSV: 254 rows.
- Lean 4.34.0-rc2: `lake build` — 6 jobs, exit 0.
- Rejection tests: `T⁻²`, `L⁴`, `R²`.

## AI for Science

This repository supports a Letter of Intent for Anthropic's AI for Science program: formalizing and verifying a typed physical catalog with Claude-assisted Lean proofs.

- [English LOI](docs/en/LOI.md)
- [Carta en español](docs/es/LOI.md)

## What this is not

- Not a unified theory.
- Not an empirical validation.
- Not a claim that the 213 candidates are predictions.

## License

- Code: MIT (`LICENSE`).
- Documentation and data: CC BY 4.0 (`LICENSE-docs.md`).

## Citation

See `CITATION.cff`.

