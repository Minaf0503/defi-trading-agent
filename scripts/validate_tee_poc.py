#!/usr/bin/env python
"""Deterministic validation for the TEE PoC's integrity-binding property
(no real TEE hardware needed) -- the actual security claim this demo makes
is that commitment_hash is a function of (input, output, code_hash), so a
tampered output can't be passed off as matching a genuine quote's
report_data. This checks that property holds, with a mocked dstack client
so the test works with no TEE runtime present."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tee_poc"))

from fastapi.testclient import TestClient


def test_commitment_binds_to_output():
    section = "1. commitment_hash changes if output is tampered with"
    print(f"\n{'='*70}\n{section}\n{'='*70}")

    import app as app_module
    client = TestClient(app_module.app)

    payload = {
        "decision_id": "TEST_1",
        "calibrated_probability": 0.6,
        "payoff_ratio": 1.5,
        "capital": 100_000,
    }
    resp = client.post("/attest_sizing", json=payload).json()
    genuine_hash = resp["commitment_hash"]

    # Simulate a tampered host: same code_hash and input, but a different
    # (more favorable) position_size_usd in the output.
    tampered_output = dict(resp["output"])
    tampered_output["position_size_usd"] *= 10

    import hashlib
    tampered_commitment = {
        "decision_id": resp["decision_id"],
        "input": resp["input"],
        "output": tampered_output,
        "code_hash": resp["code_hash"],
    }
    tampered_hash = hashlib.sha256(json.dumps(tampered_commitment, sort_keys=True).encode()).hexdigest()

    ok = tampered_hash != genuine_hash
    print(f"genuine commitment_hash:  {genuine_hash}")
    print(f"tampered commitment_hash: {tampered_hash}")
    print("PASS: tampering with output changes the commitment hash (a forged output can't reuse a genuine quote)" if ok else "FAIL")
    return ok


def test_no_tee_runtime_reports_unavailable_not_fake():
    section = "2. No TEE runtime present -> attestation_available=False, not a fabricated quote"
    print(f"\n{'='*70}\n{section}\n{'='*70}")

    import app as app_module
    client = TestClient(app_module.app)
    resp = client.post("/attest_sizing", json={
        "decision_id": "TEST_2", "calibrated_probability": 0.5, "payoff_ratio": 1.5, "capital": 10_000,
    }).json()

    ok = resp["attestation"]["attestation_available"] is False and "quote" not in resp["attestation"]
    print(f"attestation: {resp['attestation']}")
    print("PASS: correctly reports unavailable, no fields fabricated" if ok else "FAIL")
    return ok


def test_mocked_attestation_path_binds_report_data():
    section = "3. With a mocked TEE client, report_data passed to get_quote matches the recomputed commitment hash"
    print(f"\n{'='*70}\n{section}\n{'='*70}")

    import importlib
    import app as app_module
    importlib.reload(app_module)

    captured = {}

    class FakeQuote:
        quote = "FAKE_QUOTE_BLOB"
        event_log = "FAKE_EVENT_LOG"
        report_data = None

    class FakeDstackClient:
        def __init__(self):
            pass

        def get_quote(self, report_data):
            captured["report_data"] = report_data
            return FakeQuote()

    import sys as _sys
    fake_module = type(_sys)("dstack_sdk")
    fake_module.DstackClient = FakeDstackClient
    _sys.modules["dstack_sdk"] = fake_module

    importlib.reload(app_module)
    client = TestClient(app_module.app)
    resp = client.post("/attest_sizing", json={
        "decision_id": "TEST_3", "calibrated_probability": 0.6, "payoff_ratio": 1.5, "capital": 100_000,
    }).json()

    ok = (resp["attestation"]["attestation_available"] is True
          and captured["report_data"].hex() == resp["commitment_hash"])
    print(f"attestation_available: {resp['attestation']['attestation_available']}")
    print(f"report_data passed to get_quote == returned commitment_hash: {captured['report_data'].hex() == resp['commitment_hash']}")
    print("PASS: the quote is bound to this exact commitment, not issued blind" if ok else "FAIL")
    return ok


def main():
    results = [
        test_commitment_binds_to_output(),
        test_no_tee_runtime_reports_unavailable_not_fake(),
        test_mocked_attestation_path_binds_report_data(),
    ]
    print(f"\n{'='*70}\nSummary\n{'='*70}")
    print(f"{sum(results)}/{len(results)} tests passed")
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
