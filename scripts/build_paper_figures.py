#!/usr/bin/env python
"""
Phase 6: real figures for the paper, generated from already-computed result
files -- not illustrative/invented numbers. Each figure's data is printed
alongside the save so it can be spot-checked against the prose in draft.md
before trusting the PDF.

Outputs to writing/papers/overleaf/figures/, sized for a single LNCS column
(~12cm) and using grayscale-safe hatching so they remain legible if printed
in black and white.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

OUT_DIR = Path("writing/papers/overleaf/figures")
OUT_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.size": 9,
    "figure.dpi": 300,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

MULTI_COLOR = "#2c3e50"
SINGLE_COLOR = "#bdc3c7"


def fig_execution_cost_by_size():
    df = pd.read_csv("experiments/results/execution_quality_by_size_bucket.csv")
    tickers = ["ETH", "UNI", "AAVE"]
    sizes = [10000, 100000]

    fig, ax = plt.subplots(figsize=(4.7, 3.0))
    width = 0.35
    x = range(len(tickers))
    for i, size in enumerate(sizes):
        vals = [df[(df.ticker == t) & (df.notional_usd == size)]["mean_diff_pct"].iloc[0] for t in tickers]
        offset = (i - 0.5) * width
        bars = ax.bar([xi + offset for xi in x], vals, width,
                       label=f"${size // 1000}k notional",
                       color=MULTI_COLOR if size == 100000 else SINGLE_COLOR,
                       hatch="//" if size == 100000 else None,
                       edgecolor="black", linewidth=0.5)
        for xi, v in zip(x, vals):
            ax.text(xi + offset, v + 0.03, f"{v:.3f}%" if v < 0.01 else f"{v:.2f}%",
                     ha="center", va="bottom", fontsize=6.5, rotation=0)

    ax.set_xticks(list(x))
    ax.set_xticklabels(tickers)
    ax.set_ylabel("Mean same-tick estimate vs.\nactual fill divergence (%)")
    ax.set_title("Execution cost scales super-linearly with size,\nconcentrated in shallow-liquidity pools", fontsize=8.5)
    ax.legend(frameon=False, fontsize=7.5)
    fig.tight_layout()
    out = OUT_DIR / "fig_execution_cost_by_size.pdf"
    fig.savefig(out)
    plt.close(fig)
    print(f"Saved {out}")
    print(df[["notional_usd", "ticker", "mean_diff_pct"]].to_string(index=False))


def fig_llm_judge_axes():
    df = pd.read_csv("experiments/results/llm_judge_eval.csv")
    axes = ["evidence_grounding", "logical_coherence", "uncertainty_engagement"]
    labels = ["Evidence\ngrounding", "Logical\ncoherence", "Uncertainty\nengagement"]
    multi_means = [df[f"{a}_multi_agent"].mean() for a in axes]
    single_means = [df[f"{a}_single_agent"].mean() for a in axes]

    fig, ax = plt.subplots(figsize=(4.7, 3.0))
    width = 0.35
    x = range(len(axes))
    ax.bar([xi - width / 2 for xi in x], multi_means, width, label="Multi-agent",
           color=MULTI_COLOR, edgecolor="black", linewidth=0.5)
    ax.bar([xi + width / 2 for xi in x], single_means, width, label="Single-agent",
           color=SINGLE_COLOR, hatch="//", edgecolor="black", linewidth=0.5)
    for xi, v in zip(x, multi_means):
        ax.text(xi - width / 2, v + 0.05, f"{v:.2f}", ha="center", va="bottom", fontsize=7)
    for xi, v in zip(x, single_means):
        ax.text(xi + width / 2, v + 0.05, f"{v:.2f}", ha="center", va="bottom", fontsize=7)

    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=7.5)
    ax.set_ylabel("Mean blind-judge score (1--10)")
    ax.set_ylim(0, 10)
    ax.set_title("Blind LLM judge: mixed result, no clean win\nfor either architecture", fontsize=8.5)
    ax.legend(frameon=False, fontsize=7.5, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.0))
    fig.tight_layout()
    out = OUT_DIR / "fig_llm_judge_axes.pdf"
    fig.savefig(out)
    plt.close(fig)
    print(f"Saved {out}")
    for a, m, s in zip(axes, multi_means, single_means):
        print(f"{a}: multi={m:.2f} single={s:.2f}")


def fig_hit_rate_by_date():
    summary = json.load(open("eval_results/week18_panel/_summary.json"))
    rows = []
    for d in summary:
        ma_dec = d["multi_agent"]["decision"]
        ret30 = d["forward_returns"].get("return_30d_pct")
        if ma_dec in ("BUY", "SELL") and ret30 is not None:
            hit = (ma_dec == "BUY" and ret30 > 0) or (ma_dec == "SELL" and ret30 < 0)
            rows.append({"trade_date": d["trade_date"], "hit": hit})
    df = pd.DataFrame(rows)
    agg = df.groupby("trade_date")["hit"].agg(["mean", "count"]).reset_index()
    agg = agg.sort_values("trade_date")

    dates = agg["trade_date"].tolist()
    rates = (agg["mean"] * 100).tolist()
    counts = agg["count"].tolist()
    # both models' self-reported pretraining cutoffs fall inside the panel window
    cutoff_label = ["pre-cutoff", "mixed", "post-cutoff", "post-cutoff"]

    fig, ax = plt.subplots(figsize=(4.7, 3.0))
    colors = [SINGLE_COLOR if c == "pre-cutoff" else ("#7f8c8d" if c == "mixed" else MULTI_COLOR) for c in cutoff_label]
    bars = ax.bar(dates, rates, color=colors, edgecolor="black", linewidth=0.5)
    for xi, (r, n) in enumerate(zip(rates, counts)):
        ax.text(xi, r + 2, f"{r:.0f}%\n(n={n})", ha="center", va="bottom", fontsize=7)
    ax.axhline(50, color="gray", linestyle="--", linewidth=0.7)
    ax.set_ylabel("30-day directional hit rate (%)")
    ax.set_ylim(0, 85)
    ax.set_title("Hit rate drops after both models' self-reported\npretraining cutoffs -- suggestive, not confirmatory (n=6--7/bucket)", fontsize=8)
    plt.setp(ax.get_xticklabels(), rotation=20, ha="right", fontsize=7.5)
    fig.tight_layout()
    out = OUT_DIR / "fig_hit_rate_by_date.pdf"
    fig.savefig(out)
    plt.close(fig)
    print(f"Saved {out}")
    print(agg.to_string(index=False))


if __name__ == "__main__":
    fig_execution_cost_by_size()
    print()
    fig_llm_judge_axes()
    print()
    fig_hit_rate_by_date()
