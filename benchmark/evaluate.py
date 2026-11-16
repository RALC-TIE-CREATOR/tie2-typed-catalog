#!/usr/bin/env python3
"""Evaluate predictions against the TIE 2 benchmark."""
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

LABELS = ["valid", "invalid", "process", "candidate"]

def load_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--benchmark", default=str(Path(__file__).with_name("benchmark_340.jsonl")))
    ap.add_argument("--predictions", required=True)
    args = ap.parse_args()

    gold = {r["id"]: r for r in load_jsonl(args.benchmark)}
    pred = {}
    for r in load_jsonl(args.predictions):
        if "id" in r and "label" in r:
            pred[r["id"]] = r["label"]

    missing = sorted(set(gold) - set(pred))
    extra = sorted(set(pred) - set(gold))
    common = [i for i in gold if i in pred]
    correct = sum(1 for i in common if pred[i] == gold[i]["expected"])
    total = len(common)
    acc = correct / total if total else 0.0

    by_cat_total = Counter()
    by_cat_correct = Counter()
    confusion = defaultdict(Counter)
    for i in common:
        cat = gold[i]["category"]
        by_cat_total[cat] += 1
        if pred[i] == gold[i]["expected"]:
            by_cat_correct[cat] += 1
        confusion[gold[i]["expected"]][pred[i]] += 1

    print(f"Overall accuracy: {correct}/{total} = {acc:.3f}")
    print()
    print("Per category:")
    for cat in sorted(by_cat_total):
        c = by_cat_correct[cat]
        n = by_cat_total[cat]
        print(f"  {cat}: {c}/{n} = {c/n:.3f}")
    print()
    print("Confusion matrix (gold -> predicted):")
    for g in LABELS:
        row = confusion.get(g, {})
        if row:
            print(f"  {g}: " + ", ".join(f"{p}={row.get(p,0)}" for p in LABELS))
    print()
    print(f"Missing IDs: {len(missing)}")
    print(f"Extra IDs: {len(extra)}")
    if missing:
        print("  first missing:", ", ".join(missing[:10]))
    if extra:
        print("  first extra:", ", ".join(extra[:10]))

if __name__ == "__main__":
    main()
