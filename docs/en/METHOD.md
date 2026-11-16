# Method

## 1. Entities and dimensions

A quantity has a dimension vector `(L,T,R,V,Wb,Gr)`:

- `L`: Space exponent, `-3..3`.
- `T`: Time exponent, `-1,0,1`.
- `R`: Phase exponent, `-1,0,1`.
- `V`, `Wb`, `Gr`: Physical primitives, each `-1,0,1`.

## 2. Lean encoding

`TIE2/Dimensions.lean` defines `Dim`, `admissibleB`, `Kind`, `Tensor`, `Status`, and `Entry`.

`admissibleB` rejects `T⁻²`, `T⁻³`, `L⁴`, `R²`, and self-powers of `V`, `Wb`, `Gr`.

## 3. Catalog

`TIE2/Catalog.lean` contains `catalog254`, generated from `data/catalog254.json`.

## 4. Tests

`TIE2/Examples.lean` proves:

- `catalog254.length = 254`;
- all entries are admissible;
- `T⁻²`, `L⁴`, and `R²` are rejected.

## 5. Limits

- 254 of 254 entries are encoded at the dimensional level.
- R-01–R-12 are partially encoded: dimensional admissibility is in Lean; sum/type/class rules are the next step.
- Benchmark of 340 statements; evaluation pending.
