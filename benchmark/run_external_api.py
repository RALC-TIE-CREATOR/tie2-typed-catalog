#!/usr/bin/env python3
"""Run the TIE 2 benchmark against an OpenAI-compatible endpoint."""
import argparse
import json
import os
import time
import urllib.request
from pathlib import Path

base_dir = Path(__file__).resolve().parent
rows = [json.loads(l) for l in (base_dir / "benchmark_340.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
system = (base_dir / "prompt_external.txt").read_text(encoding="utf-8").split("Now classify all cases:")[0].strip()

def call(base_url, key, model, batch):
    user = "Classify these cases:\n\n" + "\n".join(f'{r["id"]} | {r["statement_en"]}' for r in batch) + "\n\nReturn the JSON array only."
    body = {
        "model": model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": 0,
        "max_tokens": 4000,
    }
    req = urllib.request.Request(
        base_url.rstrip("/") + "/chat/completions",
        data=json.dumps(body).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    content = (data["choices"][0]["message"].get("content") or "").strip()
    if content.startswith("```"):
        content = content.strip("`")
        if content.startswith("json"):
            content = content[4:].strip()
    parsed = json.loads(content)
    labels = {str(x["id"]): str(x["label"]) for x in parsed if isinstance(x, dict)}
    missing = [r["id"] for r in batch if r["id"] not in labels]
    if missing:
        raise RuntimeError(f"missing ids: {missing[:5]}")
    return [{"id": r["id"], "label": labels[r["id"]]} for r in batch]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default=os.environ.get("LLM_BASE_URL"))
    ap.add_argument("--model", default=os.environ.get("LLM_MODEL"))
    ap.add_argument("--api-key-env", default="LLM_API_KEY")
    ap.add_argument("--out", default=str(base_dir / "predictions.jsonl"))
    ap.add_argument("--batch-size", type=int, default=10)
    args = ap.parse_args()

    key = os.environ.get(args.api_key_env)
    if not args.base_url or not args.model or not key:
        raise SystemExit("Set LLM_BASE_URL, LLM_MODEL, and LLM_API_KEY.")

    out = Path(args.out)
    done = {}
    if out.exists():
        for l in out.read_text(encoding="utf-8").splitlines():
            if l.strip():
                x = json.loads(l)
                done[x["id"]] = x["label"]
    all_preds = [{"id": k, "label": v} for k, v in done.items()]

    for i in range(0, len(rows), args.batch_size):
        batch = [r for r in rows[i:i+args.batch_size] if r["id"] not in done]
        if not batch:
            continue
        for attempt in range(5):
            try:
                preds = call(args.base_url, key, args.model, batch)
                all_preds.extend(preds)
                for x in preds:
                    done[x["id"]] = x["label"]
                out.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in all_preds) + "\n", encoding="utf-8")
                print(f"batch {i//args.batch_size+1} ok ({len(preds)}), total {len(all_preds)}", flush=True)
                break
            except Exception as e:
                print(f"batch {i//args.batch_size+1} attempt {attempt+1}: {e}", flush=True)
                time.sleep(5 * (attempt + 1))
        else:
            print("batch failed; progress saved. Re-run to resume.", flush=True)
            raise SystemExit(2)

    print(f"wrote {out} ({len(all_preds)} predictions)")

if __name__ == "__main__":
    main()
