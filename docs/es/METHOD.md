# Método

## 1. Entes y dimensiones

Una cantidad tiene un vector `(L,T,R,V,Wb,Gr)`:

- `L`: exponente de Espacio, `-3..3`.
- `T`: exponente de Tiempo, `-1,0,1`.
- `R`: exponente de Fase, `-1,0,1`.
- `V`, `Wb`, `Gr`: primitivos de Físico, cada uno `-1,0,1`.

## 2. Codificación Lean

`TIE2/Dimensions.lean` define `Dim`, `admissibleB`, `Kind`, `Tensor`, `Status` y `Entry`.

`admissibleB` rechaza `T⁻²`, `T⁻³`, `L⁴`, `R²` y autopotencias de `V`, `Wb`, `Gr`.

## 3. Catálogo

`TIE2/Catalog.lean` contiene `catalog254`, generado desde `data/catalog254.json`.

## 4. Pruebas

`TIE2/Examples.lean` demuestra:

- `catalog254.length = 254`;
- todas las entradas son admisibles;
- `T⁻²`, `L⁴` y `R²` se rechazan.

## 5. Límites

- 254 de 254 entradas codificadas a nivel dimensional.
- R-01–R-12 parcialmente codificadas: la admisibilidad dimensional está en Lean; las reglas de suma/tipo/clase son el siguiente paso.
- Benchmark de 340 enunciados; evaluación pendiente.
