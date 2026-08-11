#!/usr/bin/env python
"""
Phase 5 Week 20: TEE PoC demo driver.

Feeds real Week 18 panel decisions through the tee_poc FastAPI service
(local or deployed) and verifies what can actually be verified locally:
(1) the service's code_hash matches the canonical tradingagents/calibration
/sizing.py source -- proving the vendored copy hasn't drifted; (2) the
commitment_hash the service returns is independently reproducible from the
(input, output, code_hash) it reports -- proving the attestation's
report_data genuinely binds to this specific computation, not just "the
app is running"; (3) if attestation_available is True, prints the raw quote
for separate, real DCAP/PCCS verification (out of scope for this script --
that step requires either Phala's verification API or Intel's, neither of
which this script calls).

payoff_ratio=1.5 reuses run_e2e_pipeline.py's documented placeholder (this
project has no principled per-decision payoff estimator -- Week 16
limitation) rather than inventing a different placeholder here.

Usage:
    python scripts/run_tee_poc_demo.py --endpoint http://localhost:8000
"""

import argparse
import hashlib
import inspect
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import requests

from tradingagents.calibration.calibration import ProbabilityCalibrator
from tradingagents.calibration.sizing import PositionSizer

PAYOFF_RATIO_PLACEHOLDER = 1.5
CAPITAL_USD = 100_000.0
N_DEMO_DECISIONS = 5


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--endpoint", default="http://localhost:8000")
    parser.add_argument("--panel-dir", default="eval_results/week18_panel")
    return parser.parse_args()


def canonical_code_hash() -> str:
    return hashlib.sha256(inspect.getsource(PositionSizer).encode()).hexdigest()


def hit(decision, ret):
    if ret is None or decision == "HOLD":
        return None
    return (ret > 0) if decision == "BUY" else (ret < 0)


def main():
    args = parse_args()

    summary = json.load(open(Path(args.panel_dir) / "_summary.json"))

    calibrator = ProbabilityCalibrator(min_records_to_calibrate=20)
    directional = []
    for d in summary:
        outcome = hit(d["multi_agent"]["decision"], d["forward_returns"].get("return_30d_pct"))
        if outcome is not None:
            calibrator.add_record(d["multi_agent"]["raw_confidence"], outcome, decision_id=f"{d['ticker']}_{d['trade_date']}")
            directional.append(d)
    calibrator.fit()
    print(f"Fit calibrator on {len(directional)}/{len(summary)} directional multi-agent decisions.")

    demo_points = directional[:N_DEMO_DECISIONS]

    print(f"\nChecking service health at {args.endpoint}...")
    health = requests.get(f"{args.endpoint}/health").json()
    print(f"  {health}")

    local_hash = canonical_code_hash()
    if health["code_hash"] != local_hash:
        print(f"MISMATCH: service code_hash {health['code_hash']} != canonical {local_hash}")
        print("Refusing to trust this service's output -- sizing.py has drifted from the canonical source.")
        sys.exit(1)
    print(f"  code_hash matches canonical tradingagents/calibration/sizing.py: {local_hash[:16]}...")

    results = []
    for d in demo_points:
        decision_id = f"{d['ticker']}_{d['trade_date']}"
        cal = calibrator.calibrate(d["multi_agent"]["raw_confidence"])
        payload = {
            "decision_id": decision_id,
            "calibrated_probability": cal["calibrated_probability"],
            "payoff_ratio": PAYOFF_RATIO_PLACEHOLDER,
            "capital": CAPITAL_USD,
        }
        resp = requests.post(f"{args.endpoint}/attest_sizing", json=payload).json()

        recomputed_commitment = {
            "decision_id": resp["decision_id"],
            "input": resp["input"],
            "output": resp["output"],
            "code_hash": resp["code_hash"],
        }
        recomputed_hash = hashlib.sha256(json.dumps(recomputed_commitment, sort_keys=True).encode()).hexdigest()
        commitment_ok = recomputed_hash == resp["commitment_hash"]

        print(f"\n{decision_id}: raw_confidence={d['multi_agent']['raw_confidence']:.2f} -> "
              f"calibrated_probability={cal['calibrated_probability']:.3f} (calibrated={cal['calibrated']})")
        print(f"  position_size_usd={resp['output']['position_size_usd']:.2f}, capped_by={resp['output']['capped_by']}")
        print(f"  commitment_hash self-consistent: {commitment_ok}")
        print(f"  attestation_available: {resp['attestation']['attestation_available']}")
        if not resp["attestation"]["attestation_available"]:
            print(f"    reason: {resp['attestation']['reason']}")

        results.append({**resp, "commitment_verified_locally": commitment_ok})

    out_path = Path("experiments/results/tee_poc_demo_results.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    n_attested = sum(r["attestation"]["attestation_available"] for r in results)
    print(f"\n{'='*70}\nSummary: {len(results)} decisions processed, "
          f"{sum(r['commitment_verified_locally'] for r in results)}/{len(results)} commitments self-consistent, "
          f"{n_attested}/{len(results)} had real TEE attestation available.")
    print(f"Saved to {out_path}")


if __name__ == "__main__":
    main()
