# Method

## 1. Entities and dimensions

A quantity has a dimension vector `(L,T,R,V,Wb,Gr)`:

- `L`: Space exponent, `-3..3`.
- `T`: Time exponent, `-1,0,1`.
- `R`: Phase exponent, `-1,0,1`.
- `V`, `Wb`, `Gr`: Physical primitives, each `-1,0,1`.

## 2. Lean encoding

`TIE2/Dimensions.lean` defines `Dim`, `admissibleB`, `Kind`, `Tensor`, `Status`, and `Entry`.

`admissibleB` rejects:

- `T⁻²`, `T⁻³`;
- `L⁴`;
- `R²`;
- any self-power of `V`, `Wb`, `Gr`.

## 3. Catalog

`TIE2/Catalog.lean` contains `catalog50`, generated from `data/catalog50.json`.

## 4. Tests

`TIE2/Examples.lean` proves:

- `catalog50.length = 50`;
- all entries are admissible;
- `T⁻²`, `L⁴`, and `R²` are rejected.

## 5. Limits

- 50 of 254 entries.
- R-01–R-12 partially encoded: dimensional admissibility is in Lean; sum/type/class rules are next.
- No benchmark yet.
