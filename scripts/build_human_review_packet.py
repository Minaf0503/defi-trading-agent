#!/usr/bin/env python
"""
Phase 5 Week 20: human expert review packet.

Same blind, pairwise design as Week 19's LLM judge (tradingagents/ablation/
llm_judge.py) -- same rubric, same blinding logic -- applied to a real
human reviewer instead of gpt-4o, on a stratified 8-point subsample of the
28-point Week 18 panel (2 points per fixed decision date, randomly selected
within each date so the sample isn't cherry-picked, with a documented seed
so the selection is reproducible). Gives a direct human-vs-LLM-judge
agreement comparison once the reviewer responds, not just an isolated
human opinion.

A/B order uses a DIFFERENT seed than the LLM judge's run, so the human
reviewer's and the LLM judge's orderings are independent -- a coincidental
shared ordering could otherwise make the two judges' answers look more
correlated than they really are.

Outputs two files, deliberately kept separate:
  - experiments/results/human_review_packet.md -- the actual packet to
    send to the reviewer. Contains NO answer key.
  - experiments/results/human_review_answer_key.json -- which response was
    actually which arm, for scoring once the reviewer responds. Not sent
    to the reviewer.
"""

import argparse
import json
import random
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260624, help="Selection + A/B order seed (distinct from the LLM judge's 20260623).")
    parser.add_argument("--panel-dir", default="eval_results/week18_panel")
    parser.add_argument("--total", type=int, default=5, help="Total items, distributed as evenly as possible across the 4 decision dates.")
    return parser.parse_args()


PACKET_HEADER = """# Human Expert Review Packet -- Multi-Agent vs. Single-Agent Trading Decision Reasoning

Thank you for reviewing these. For each item below, you'll see:
- The same three analyst reports (technical, on-chain, tokenomics) that informed both candidate decisions.
- Two candidate decision write-ups, labeled "Response A" and "Response B" -- you are NOT told which system produced which, and you don't need to guess. Please judge only what is written.
- A short rubric to fill in for each item.

**What to judge**: the QUALITY OF REASONING, not which response sounds more confident or decisive. A well-reasoned HOLD that honestly says the evidence is mixed is not worse than a confident BUY that ignores counter-evidence. You do not know (and shouldn't guess at) which decision actually turned out to be profitable -- please don't try to factor in what you think would have happened.

**For each item, please fill in** (1-10 scale unless noted):
- Evidence-grounding A / B: how well does each response cite specific facts from the three reports, vs. vague generalities?
- Logical coherence A / B: does each response's conclusion actually follow from its stated premises?
- Uncertainty engagement A / B: does each response acknowledge counter-evidence/risks, or is it one-sided?
- Overall preference: A, B, or Tie
- Justification: 1-3 sentences

Please fill in your answers inline (replacing the `____` blanks) and send the file back.

---
"""


def render_item(idx, ticker, trade_date, reports, response_a, response_b):
    return f"""
## Item {idx}: {ticker}, decision date {trade_date}

### Technical Analyst Report
{reports.get('technical_report') or '(not available)'}

### On-Chain Analyst Report
{reports.get('onchain_report') or '(not available)'}

### Tokenomics Analyst Report
{reports.get('tokenomics_report') or '(not available)'}

### Response A
{response_a}

### Response B
{response_b}

### Your evaluation
- Evidence-grounding A: ____ / 10
- Evidence-grounding B: ____ / 10
- Logical coherence A: ____ / 10
- Logical coherence B: ____ / 10
- Uncertainty engagement A: ____ / 10
- Uncertainty engagement B: ____ / 10
- Overall preference (A / B / Tie): ____
- Justification: ____

---
"""


def main():
    args = parse_args()
    rng = random.Random(args.seed)

    summary = json.load(open(Path(args.panel_dir) / "_summary.json"))
    by_date = {}
    for d in summary:
        by_date.setdefault(d["trade_date"], []).append(d)
    by_date_by_ticker = {date: {d["ticker"]: d for d in pts} for date, pts in by_date.items()}

    # Stratify by BOTH date and ticker, not date alone -- a per-date-only
    # shuffle can coincidentally repeat the same tickers across dates (seen
    # with seed 20260624: ZEC picked on 3 of 4 dates). Shuffle the ticker
    # list once, then cycle through it across dates so ticker coverage is
    # spread out, while which date pairs with which ticker is still random.
    tickers = sorted({d["ticker"] for d in summary})
    rng.shuffle(tickers)

    dates_sorted = sorted(by_date)
    # Distribute args.total as evenly as possible across dates -- e.g. 5
    # across 4 dates -> [2, 1, 1, 1], assigned round-robin so no single
    # date is arbitrarily favored.
    per_date_counts = [0] * len(dates_sorted)
    for i in range(args.total):
        per_date_counts[i % len(dates_sorted)] += 1

    selected = []
    cursor = 0
    for trade_date, count in zip(dates_sorted, per_date_counts):
        for _ in range(count):
            ticker = tickers[cursor % len(tickers)]
            cursor += 1
            selected.append(by_date_by_ticker[trade_date][ticker])

    print(f"Selected {len(selected)} points (seed={args.seed}, distributed {per_date_counts} across {len(by_date)} dates):")
    for d in selected:
        print(f"  {d['ticker']} {d['trade_date']}")

    packet_sections = [PACKET_HEADER]
    answer_key = []

    for idx, d in enumerate(selected, start=1):
        ticker, trade_date = d["ticker"], d["trade_date"]
        artifact = json.load(open(Path(args.panel_dir) / f"{ticker}_{trade_date}.json"))
        reports = artifact["reports"]
        multi_text = artifact["multi_agent"]["final_trade_decision"] or ""
        single_text = artifact["single_agent"]["full_response"] or ""

        multi_agent_is_a = rng.random() < 0.5
        response_a = multi_text if multi_agent_is_a else single_text
        response_b = single_text if multi_agent_is_a else multi_text

        packet_sections.append(render_item(idx, ticker, trade_date, reports, response_a, response_b))
        answer_key.append({
            "item": idx, "ticker": ticker, "trade_date": trade_date,
            "multi_agent_was_response": "A" if multi_agent_is_a else "B",
            "multi_agent_decision": d["multi_agent"]["decision"],
            "single_agent_decision": d["single_agent"]["decision"],
            "return_30d_pct": d["forward_returns"].get("return_30d_pct"),
        })

    out_dir = Path("experiments/results")
    out_dir.mkdir(parents=True, exist_ok=True)

    packet_path = out_dir / "human_review_packet.md"
    with open(packet_path, "w") as f:
        f.write("\n".join(packet_sections))

    key_path = out_dir / "human_review_answer_key.json"
    with open(key_path, "w") as f:
        json.dump(answer_key, f, indent=2)

    print(f"\nPacket (send to reviewer): {packet_path}")
    print(f"Answer key (keep private, for scoring once the reviewer responds): {key_path}")


if __name__ == "__main__":
    main()
