"""Verify the captured Ch9 native-partner Wait smoke, not campaign completion.

Requires observation of port-2 selection/Wait through Dolphin's original menus.
Only compares exported fields; full RAM/Netplay equivalence is not asserted.
"""
import argparse
import copy
import json
from pathlib import Path


def verify(before, after):
    failures = []
    for label, snapshot in (("before", before), ("after", after)):
        e, game = snapshot["evidence"], snapshot["game"]
        if not e.get("intended_c2_verified") or e.get("debug"):
            failures.append(f"{label}: active non-debug C2 configuration unverified")
        if (game["chapter"],game["phase"],game["turn"],game["control"][3]) != (10,3,1,1):
            failures.append(f"{label}: expected Ch9 turn-1 human Yellow phase")
    for field in ("commit","dolphin","codes_fingerprint"):
        if before["evidence"].get(field) != after["evidence"].get(field):
            failures.append(f"configuration mismatch: {field}")
    hashes = [s["evidence"].get("state_sha256") for s in (before,after)]
    if not all(hashes) or hashes[0] == hashes[1]:
        failures.append("distinct captured state hashes required")
    expected = copy.deepcopy(before["game"])
    partners = {u["pid"]:u for u in expected["units"] if u["force"]==3}
    lethe, mordy = partners.get("PID_LETHE"), partners.get("PID_MORDY")
    if lethe is None or mordy is None:
        failures.append("both original Yellow partners required")
    else:
        if any(u["owned"] or u["owner"] is not None for u in (lethe,mordy)):
            failures.append("native partners must remain unassigned")
        if (lethe["class"],lethe["gauge"],lethe["hp"],lethe["xy"]) != ("JID_CAT/F",20,34,[25,18]):
            failures.append("expected transformed original Lethe")
        if lethe["flags"] & 1 or mordy["flags"] & 1:
            failures.append("partners must not already have acted")
        lethe["flags"] |= 1
    if expected != after["game"]:
        failures.append("expected only Lethe's acted bit to change in captured game fields")
    return {"status":"FAIL" if failures else "PASS","failures":failures,
            "scope":"original Ch9 native-partner Wait fields; observed port-2 UI action required",
            "excludes":["combat EXP","chapter clear","native partner recruitment/cleanup","save/reload","Netplay"]}


if __name__ == "__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("before",type=Path);p.add_argument("after",type=Path)
    a=p.parse_args();result=verify(json.loads(a.before.read_text()),json.loads(a.after.read_text()))
    print(json.dumps(result,indent=2));raise SystemExit(result["status"]!="PASS")
