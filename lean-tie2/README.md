# lean-tie2 — prototipo Lean 4

Proyecto mínimo para formalizar las reglas de admisibilidad de TIE 2 y el catálogo de 50 entradas.

## Requisitos

- Lean 4.34.0-rc2 (fijado en `lean-toolchain`)
- Lake

## Compilar

```bash
cd lean-tie2
lake build
```

Resultado esperado:

- `TIE2.Dimensions`, `TIE2.Catalog`, `TIE2.Examples` compilan.
- `catalog50.length = 50`.
- Todas las entradas pasan `admissibleB`.
- `T⁻²`, `L⁴` y `R²` se rechazan.

## Estructura

- `TIE2/Dimensions.lean` — `Dim`, `Kind`, `Tensor`, `Status`, `Entry`, `admissibleB`.
- `TIE2/Catalog.lean` — lista `catalog50` generada desde `catalog50.json`.
- `TIE2/Examples.lean` — pruebas de longitud, admisibilidad y rechazo.
- `TIE2.lean` — importa los módulos.

## Limitaciones

- 50 de 254 entradas.
- R-01–R-12 parcialmente codificadas: la admisibilidad dimensional está; las reglas de suma/tipo/clase se añadirán en la siguiente fase.
- No hay benchmark todavía.
