#!/usr/bin/env python3
"""Merge external LLM responses into predictions.jsonl."""
import json
from pathlib import Path

base = Path(__file__).resolve().parent
responses = base / "responses"
responses.mkdir(exist_ok=True)

pred = {}
for path in sorted(responses.glob("*.json")):
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = [data]
    for x in data:
        if isinstance(x, dict) and "id" in x and "label" in x:
            pred[str(x["id"])] = str(x["label"])

out = base / "predictions.jsonl"
out.write_text("\n".join(json.dumps({"id": k, "label": v}, ensure_ascii=False) for k, v in sorted(pred.items())) + "\n", encoding="utf-8")
print(f"merged {len(pred)} predictions into {out}")
