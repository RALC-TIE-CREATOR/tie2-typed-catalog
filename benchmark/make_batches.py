#!/usr/bin/env python3
"""Create copy-paste batches from the TIE 2 benchmark."""
import json
from pathlib import Path

base = Path(__file__).resolve().parent
rows = [json.loads(l) for l in (base / "benchmark_340.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
prompt = (base / "prompt_external.txt").read_text(encoding="utf-8")
batches = base / "batches"
batches.mkdir(exist_ok=True)

size = 10
for i in range(0, len(rows), size):
    chunk = rows[i:i+size]
    cases = "\n".join(f'{r["id"]} | {r["statement_en"]}' for r in chunk)
    text = prompt.replace("{{CASES}}", cases)
    n = i // size + 1
    (batches / f"batch_{n:03d}.txt").write_text(text, encoding="utf-8")

print(f"wrote {len(rows)} cases in {(len(rows)+size-1)//size} batches to {batches}")
