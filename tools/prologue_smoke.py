"""Verify captured Prologue Wait smoke evidence; does not drive the UI.

The operator/harness must observe the original Wait action. These assertions
verify the resulting fields, not arbitrary story events or campaign completion.
"""
import argparse
import json
from pathlib import Path


def verify(before, after):
    failures = []
    for name, snapshot in (("before", before), ("after", after)):
        evidence = snapshot["evidence"]
        if not evidence.get("intended_c2_verified"):
            failures.append(f"{name}: intended C2 bodies not verified in RAM")
        if evidence.get("debug"):
            failures.append(f"{name}: debug code enabled")
        if not evidence.get("state_sha256"):
            failures.append(f"{name}: missing state hash")
    for key in ("commit", "dolphin", "codes_fingerprint"):
        if before["evidence"].get(key) != after["evidence"].get(key):
            failures.append(f"configuration mismatch: {key}")
    if before["evidence"].get("state_sha256") == after["evidence"].get("state_sha256"):
        failures.append("before/after state hashes must differ")
    for name, snapshot, phase in (("before", before, 0), ("after", after, 1)):
        game = snapshot["game"]
        if (game["chapter"], game["turn"], game["phase"]) != (1, 1, phase):
            failures.append(f"{name}: expected Prologue turn 1 phase {phase}")
        ike = [u for u in game["units"] if u["pid"] == "PID_IKE"]
        if len(ike) != 1 or any(ike[0][k] != v for k, v in
                               {"force": 0, "hp": 19, "level": 1, "exp": 0, "xy": [3,9]}.items()):
            failures.append(f"{name}: unexpected Ike identity/progression/position")
    return {"status": "FAIL" if failures else "PASS", "failures": failures,
            "scope": "captured original Prologue Wait smoke fields only; UI action observation required",
            "excludes": ["Yellow control", "chapter completion", "story transition", "Netplay"]}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("before", type=Path); p.add_argument("after", type=Path)
    a = p.parse_args()
    result = verify(json.loads(a.before.read_text()), json.loads(a.after.read_text()))
    print(json.dumps(result, indent=2))
    raise SystemExit(result["status"] != "PASS")
