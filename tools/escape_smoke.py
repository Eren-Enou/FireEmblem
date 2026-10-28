"""Check the synthetic Ch6 original Yellow Escape evidence, not a chapter clear.

Setup positions were artificial. Escape menu, confirmation and dialogue must be
observed through the original UI. No normal map traversal/combat/save claim.
"""
import argparse
import json
from pathlib import Path


def verify(before,after):
    failures=[]
    expected_codes={"COOP-P6","EXP-16","DBG-CAMP-POS"}
    for label,snapshot in (("before",before),("after",after)):
        e=snapshot["evidence"]
        if not e.get("intended_c2_verified"):
            failures.append(f"{label}: live C2 bodies unverified")
        if {name.split()[0] for name in e["codes"]}!=expected_codes:
            failures.append(f"{label}: wrong synthetic setup code selection")
    for key in ("commit","dolphin","codes_fingerprint"):
        if before["evidence"].get(key)!=after["evidence"].get(key):
            failures.append(f"configuration mismatch: {key}")
    hashes=[s["evidence"].get("state_sha256") for s in (before,after)]
    if not all(hashes) or hashes[0]==hashes[1]:
        failures.append("distinct captured state hashes required")
    games=[s["game"] for s in (before,after)]
    if (games[0]["chapter"],games[0]["phase"],games[0]["turn"])!=(7,3,1):
        failures.append("expected turn1 Yellow pre-Escape state")
    if (games[1]["chapter"],games[1]["phase"],games[1]["turn"])!=(7,0,2):
        failures.append("expected same chapter turn2 Blue post-Escape state")
    oscar=[]
    for label,game in zip(("before","after"),games):
        units=[u for u in game["units"] if u["pid"]=="PID_OSCAR"]
        if len(units)!=1:
            failures.append(f"{label}: exactly one Oscar required")
            continue
        oscar.append(units[0])
        if not any(u["pid"]=="PID_IKE" and u["force"]==0 for u in game["units"]):
            failures.append(f"{label}: Ike must remain on the map")
        if not any(u["pid"]=="PID_EMAKOU" and u["force"]==1 and u["hp"]==32 for u in game["units"]):
            failures.append(f"{label}: synthetic boss must remain alive/enemy")
    if len(oscar)==2:
        a,b=oscar
        if a["force"]!=3 or a["xy"]!=[13,26] or a["flags"]&0x4000:
            failures.append("Oscar pre-Escape faction/position/flag differs")
        if b["force"]!=5 or not b["flags"]&0x4000 or b["death_record"]:
            failures.append("Oscar must be preserved in roster with escaped flag")
        for key in ("slot","class","hp","level","exp","inventory_slots_hex"):
            if a.get(key)!=b.get(key):failures.append(f"Oscar {key} not preserved")
        if len(a.get("inventory_slots_hex",""))!=128:
            failures.append("raw eight-slot inventory evidence required")
    return {"status":"FAIL" if failures else "PASS","failures":failures,
            "classification":"synthetic_original_native_positioning",
            "scope":"original Yellow individual Escape and same-map roster preservation only",
            "excludes":["natural traversal/combat","carried units","Ike-last completion","chapter transition","save/reload","Netplay"]}


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("before",type=Path);p.add_argument("after",type=Path)
    a=p.parse_args();result=verify(json.loads(a.before.read_text()),json.loads(a.after.read_text()))
    print(json.dumps(result,indent=2));raise SystemExit(result["status"]!="PASS")
