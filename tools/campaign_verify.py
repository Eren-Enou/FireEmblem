"""Validate and render campaign evidence; never infer gameplay from static checks."""
import argparse
import json
import re
from pathlib import Path

STATUSES={"PASS","FAIL","INCONCLUSIVE","NOT TESTED"}
AXES=("static_cfg","script_model","fixture","event_runtime","chapter_clear","transition","save_reload","netplay_local","netplay_two_pc")
RUNTIME={"fixture","event_runtime","chapter_clear","transition","save_reload","netplay_local","netplay_two_pc"}


def validate(ledger):
    seen=set()
    for row in ledger["chapters"]:
        if row["key"] in seen: raise ValueError("duplicate chapter/stage key")
        seen.add(row["key"])
        for axis in AXES:
            claim=row["checks"][axis]
            if claim["status"] not in STATUSES: raise ValueError("unknown status")
            if claim["status"]=="PASS":
                if not claim.get("evidence"): raise ValueError("PASS requires evidence")
                run=ledger["runs"].get(claim["evidence"])
                if not run: raise ValueError("missing evidence run")
                if axis in RUNTIME:
                    if run["kind"] not in ("dolphin","netplay_local","netplay_two_pc"):
                        raise ValueError("static evidence cannot establish gameplay")
                    if axis.startswith("netplay") and run["kind"]!=axis:
                        raise ValueError("Netplay topology does not match claim")
                    if not all(run.get(k) for k in ("commit","fingerprint","dolphin","fixture_class","artifacts")):
                        raise ValueError("runtime evidence lacks provenance")
                    if axis in ("chapter_clear","transition") and run["fixture_class"]!="naturally_progressed":
                        raise ValueError("synthetic fixture cannot certify natural campaign completion")
                    for artifact in run["artifacts"]:
                        if not isinstance(artifact,dict) or not artifact.get("path") or not re.fullmatch(r"[0-9a-fA-F]{64}",artifact.get("sha256","")):
                            raise ValueError("runtime artifact requires a path and SHA-256")
                    if axis=="netplay_two_pc" and len(set(run.get("machines",[])))<2:
                        raise ValueError("two-PC evidence requires two distinct machine declarations")
    return ledger


def render(ledger):
    validate(ledger)
    out=["# Campaign verification dashboard", "",
         "PASS applies only to the named axis and evidence configuration. Parser/model passes do not imply gameplay. "
         "Old release reports remain in TESTING.md and are not promoted here. A fixture is runnable only after acceptance, "
         "not merely because a file exists. Ch17 stages share a script; stage-specific map assignment is still unresolved.", "",
         "| Chapter/stage | CFG | Script model | Fixture | Original event | Cleared | Transition | Save/reload | Netplay local | Netplay two PCs |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for row in ledger["chapters"]:
        out.append("| "+row["title"]+" | "+" | ".join(row["checks"][a]["status"] for a in AXES)+" |")
    out += ["", "## Evidence runs", ""]
    for key,run in ledger["runs"].items():
        out.append(f"- **{key}**: `{run['kind']}`; {run.get('description','')}")
    out += ["", "## Highest-priority open cases", ""]
    out += ["- "+case for case in ledger["next_cases"]]
    return "\n".join(out)+"\n"


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ledger",type=Path,default=Path("campaign/verification.json"))
    p.add_argument("--out",type=Path,default=Path("docs/VERIFICATION.md"))
    a=p.parse_args();ledger=validate(json.loads(a.ledger.read_text()))
    a.out.write_text(render(ledger),encoding="utf-8")
    print(f"validated {len(ledger['chapters'])} chapter/stage records")
