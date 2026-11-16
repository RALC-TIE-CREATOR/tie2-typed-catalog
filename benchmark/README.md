# Benchmark — TIE 2 typed catalog

## What it is

A **synthetic benchmark of 340 bilingual statements** for evaluating whether a model can apply the TIE 2 admissibility rules.

It is not an empirical validation. It is a controlled stress test for category errors, forbidden exponents, processes, and candidate classification.

## Files

- `benchmark_340.jsonl` — one JSON object per statement.
- `benchmark_340.csv` — same data in CSV.
- `evaluate.py` — compares a predictions file with the gold labels.

## Labels

- `valid`: admissible statement.
- `invalid`: forbidden sum, product, root, or unit.
- `process`: a process/relation, not a unit.
- `candidate`: admissible combination without standard name or protocol; not a prediction.

## Counts

| Expected | Count |
|---|---|
| invalid | 195 |
| valid | 115 |
| candidate | 20 |
| process | 10 |
| **Total** | **340** |

## Evaluate

Create `predictions.jsonl` with one line per case:

```json
{"id":"B-001","label":"invalid"}
```

Then:

```bash
python benchmark/evaluate.py --predictions predictions.jsonl
```

The evaluator reports overall accuracy, per-category accuracy, confusion matrix, missing IDs, and extra IDs.

For another LLM: see `EXTERNAL_LLM.md`, `prompt_external.txt`, and `make_batches.py`.

## Caveats

- Synthetic, template-generated; human review is pending.
- `lean_checkable` marks cases whose dimensional admissibility can be checked directly; sums and type/class cases require the full rule set.
- Do not present this benchmark as empirical evidence for TIE 2.

