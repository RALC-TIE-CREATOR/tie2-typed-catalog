# Correr el benchmark con un LLM externo

## Qué necesitas

1. Un LLM con salida JSON fiable: Claude, GPT, Gemini, DeepSeek, Qwen, etc.
2. El archivo `benchmark_340.jsonl` (o los lotes generados).
3. Temperatura 0.
4. Lotes de 10–20 enunciados por mensaje.
5. Guardar cada respuesta como JSON.
6. Ejecutar `python evaluate.py --predictions predictions.jsonl`.

## Opción A — Chat manual

Genera los lotes:

```bash
python make_batches.py
```

Se crean `batches/batch_001.txt` … `batch_034.txt`, cada uno con el prompt y 10 casos. Pega un lote en el chat del LLM, copia su respuesta JSON y guárdala como `responses/batch_001.json`.

Cuando tengas todas:

```bash
python merge_responses.py
python evaluate.py --predictions predictions.jsonl
```

## Opción B — API compatible con OpenAI

Necesitas:

- `base_url` del proveedor;
- `model` exacto;
- API key en una variable de entorno, nunca en el repo.

Ejemplo:

```bash
export LLM_BASE_URL="https://api.example.com/v1"
export LLM_MODEL="model-name"
export LLM_API_KEY="..."
python run_external_api.py --out predictions.jsonl --batch-size 10
```

El script usa `POST {base_url}/chat/completions` con `Authorization: Bearer $LLM_API_KEY`.

## Prompt

El prompt está en `prompt_external.txt`. Las reglas son:

- `valid`, `invalid`, `process`, `candidate`;
- `L ∈ [-3,3]`; `T,R,V,Wb,Gr ∈ {-1,0,1}`;
- sin `T²`, `T⁻²`, `L⁴`, `L⁻⁴`, `R²`, `R⁻²`, `V²`, etc.;
- sin `s²`, `s³`, `√(s²)`;
- sumas con misma dimensión, tipo y clase;
- productos dentro del presupuesto;
- raíces solo de `m²`/`m³`.

## Evaluación

```bash
python evaluate.py --predictions predictions.jsonl
```

Reporta precisión global, por categoría, matriz de confusión, IDs faltantes y extra.

## Advertencia

El benchmark es sintético. Un resultado alto no valida TIE 2; solo mide si el modelo aplica las reglas del catálogo.
