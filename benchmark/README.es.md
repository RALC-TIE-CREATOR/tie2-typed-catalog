# Benchmark — catálogo tipado TIE 2

## Qué es

Un **benchmark sintético de 340 enunciados bilingües** para evaluar si un modelo aplica las reglas de admisibilidad de TIE 2.

No es una validación empírica. Es una prueba controlada de errores de categoría, exponentes prohibidos, procesos y clasificación de candidatos.

## Archivos

- `benchmark_340.jsonl` — un objeto JSON por enunciado.
- `benchmark_340.csv` — los mismos datos en CSV.
- `evaluate.py` — compara un archivo de predicciones con las etiquetas gold.

## Etiquetas

- `valid`: enunciado admisible.
- `invalid`: suma, producto, raíz o unidad prohibida.
- `process`: proceso/relación, no unidad.
- `candidate`: combinación admisible sin nombre ni protocolo; no es predicción.

## Conteo

| Esperado | Nº |
|---|---|
| invalid | 195 |
| valid | 115 |
| candidate | 20 |
| process | 10 |
| **Total** | **340** |

## Evaluar

Crea `predictions.jsonl` con una línea por caso:

```json
{"id":"B-001","label":"invalid"}
```

Luego:

```bash
python benchmark/evaluate.py --predictions predictions.jsonl
```

El evaluador reporta precisión global, precisión por categoría, matriz de confusión, IDs faltantes e IDs extra.

## Advertencias

- Sintético, generado por plantillas; revisión humana pendiente.
- `lean_checkable` marca los casos cuya admisibilidad dimensional se puede verificar directamente; las sumas y los casos de tipo/clase requieren el conjunto completo de reglas.
- No presentar este benchmark como evidencia empírica de TIE 2.
