# TIE 2 — Catálogo tipado de cantidades físicas

Prototipo de un **catálogo tipado y verificable por máquina de cantidades físicas**. Formaliza las reglas de admisibilidad de TIE 2 en Lean 4 y ofrece un dataset de 50 entradas extraído de un catálogo combinatorio de 254.

**Estado:** prototipo. 50/254 entradas; la compilación Lean pasa; `T⁻²`, `L⁴` y `R²` se rechazan. No es una teoría física validada.

[English](README.md)

## Por qué

La notación física estándar mezcla cantidades que comparten dimensiones pero no son lo mismo: torque y energía, presión y densidad de energía, frecuencia y velocidad angular. El análisis dimensional no detecta esos errores de categoría.

TIE 2 propone una gramática tipada:

- cuatro entes: Espacio, Tiempo, Fase, Físico;
- reglas R-01–R-12 de admisibilidad;
- un catálogo de 254 combinaciones únicas (35 estándar, 4 etiqueta, 2 puente, 213 candidatos).

Este repositorio prueba si esa gramática puede formalizarse y verificarse.

## Contenido

```
data/                 dataset de 50 entradas (JSON + CSV)
lean-tie2/            proyecto Lean 4
docs/en/              documentación en inglés
docs/es/              documentación en español
```

## Inicio rápido

```bash
cd lean-tie2
lake build
```

Esperado: `TIE2.Dimensions`, `TIE2.Catalog`, `TIE2.Examples` compilan; `catalog50.length = 50`; todas las entradas pasan `admissibleB`; `T⁻²`, `L⁴`, `R²` fallan.

## Dataset

`data/catalog50.json` y `data/catalog50.csv` contienen 50 entradas:

| Bloque | Entradas |
|---|---|
| Unidades de nivel 1 | 16 |
| GET estándar/etiqueta | 14 |
| R5 estándar/puente | 10 |
| Candidatos con Fase (R6–R8) | 10 |

Cada entrada declara: id, nivel, expresión, unidad, vector `L,T,R,V,Wb,Gr`, tipo, clase, estatus, fuente y nota.

## Verificación

- JSON: 50 entradas.
- CSV: 50 filas.
- Lean 4.34.0-rc2: `lake build` — 6 jobs, exit 0.
- Pruebas de rechazo: `T⁻²`, `L⁴`, `R²`.

## AI for Science

Este repositorio respalda una carta de intención para el programa AI for Science de Anthropic: formalizar y verificar un catálogo físico tipado con pruebas Lean asistidas por Claude.

- [Carta en español](docs/es/LOI.md)
- [English LOI](docs/en/LOI.md)

## Lo que no es

- No es una teoría unificada.
- No es una validación empírica.
- No afirma que los 213 candidatos sean predicciones.

## Licencia

- Código: MIT (`LICENSE`).
- Documentación y datos: CC BY 4.0 (`LICENSE-docs.md`).

## Cita

Ver `CITATION.cff`.
