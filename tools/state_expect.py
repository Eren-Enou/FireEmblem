"""Check explicit fixture preconditions in a captured snapshot, never gameplay.

Unknown keys fail closed. A PASS covers only listed fields, and requires live C2
evidence for this co-op fixture workflow. Use campaign_verify for artifact hashes.
"""
import argparse
import json
from pathlib import Path

TOP = {"description","classification","chapter","phase","turn","control","units",
       "active_player_pids","absent_pids","fingerprint","allow_debug","allow_synthetic"}
UNIT = {"pid","force","class","hp","level","exp","gauge","xy","owned","owner",
        "flags_all","flags_none"}


def verify(snapshot, expected):
    if set(expected)-TOP:
        raise ValueError("unknown fixture expectation keys")
    if type(expected.get("chapter")) is not int or not 1 <= expected["chapter"] <= 31 or not expected.get("units"):
        raise ValueError("fixture expectation requires a campaign chapter and unit preconditions")
    failures=[]
    evidence,game=snapshot["evidence"],snapshot["game"]
    if not evidence.get("intended_c2_verified"):
        failures.append("intended C2 bodies not verified in live RAM")
    if evidence.get("debug") and not expected.get("allow_debug",False):
        failures.append("debug codes not allowed by fixture expectation")
    if evidence.get("synthetic_setup") and not expected.get("allow_synthetic",False):
        failures.append("active synthetic setup codes not allowed by fixture expectation")
    if "fingerprint" in expected and expected["fingerprint"]!=evidence["codes_fingerprint"]:
        failures.append("configuration fingerprint mismatch")
    for key in ("chapter","phase","turn","control"):
        if key in expected and game[key]!=expected[key]:
            failures.append(f"{key}: expected {expected[key]!r}, got {game[key]!r}")
    units=game["units"]
    if "active_player_pids" in expected:
        actual=sorted(u["pid"] for u in units if u["force"] in (0,3))
        if actual!=sorted(expected["active_player_pids"]):
            failures.append("active Blue/Yellow roster differs")
    for pid in expected.get("absent_pids",[]):
        if any(u["pid"]==pid for u in units):
            failures.append(f"{pid}: expected absent")
    for row in expected.get("units",[]):
        if set(row)-UNIT or not row.get("pid"):
            raise ValueError("unknown unit expectation key or missing PID")
        matches=[u for u in units if u["pid"]==row["pid"]]
        if len(matches)!=1:
            failures.append(f"{row['pid']}: expected exactly one record, got {len(matches)}")
            continue
        actual=matches[0]
        for key,value in row.items():
            if key=="flags_all":
                valid=actual["flags"] & value == value
            elif key=="flags_none":
                valid=actual["flags"] & value == 0
            else:
                valid=actual[key]==value
            if not valid:
                failures.append(f"{row['pid']}: {key} expectation differs")
    return {"status":"FAIL" if failures else "PASS","failures":failures,
            "scope":"listed fixture preconditions only; no event/clear/transition claim",
            "classification":expected.get("classification","unspecified")}


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("snapshot",type=Path);p.add_argument("expectation",type=Path)
    a=p.parse_args();result=verify(json.loads(a.snapshot.read_text()),json.loads(a.expectation.read_text()))
    print(json.dumps(result,indent=2));raise SystemExit(result["status"]!="PASS")
