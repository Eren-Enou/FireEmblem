"""Campaign evidence inventory, including special maps and separate verification axes.

Run with --out docs/CAMPAIGN_MATRIX.md --json work/campaign_inventory.json.
This generates research leads, not a compatibility certificate. No runtime status
is inferred from passing static tests or from an older release's gameplay report.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict
from pathlib import Path

from tools.chapter_audit import RUNTIME, sortie_caps
from tools.fe9 import dispos, pack
from tools.fe9.disc import DiscReader
from tools.fe9.events import calls, functions, instructions, message_table
from tools.verify_game import DEFAULT_IMAGE

BASELINE = "10d2496 (draft research); stable main 6a81522"
INTEREST = ("Force", "Escape", "Sally", "Join", "Dead", "Die", "Phase", "Turn", "Complete",
            "Dispos", "Chapter", "Talk", "Condition", "MapLoad", "MapChange", "regist")


def inventory(disc: DiscReader) -> dict:
    files = disc.files()
    titles = message_table(disc.read_file("Mess/common.m"))
    scripts = {}
    # Includes C00/global, special scripts, startup and ending; not just C01..31.
    for path in files:
        if path.startswith("Scripts/") and path.endswith(".cmb"):
            raw = disc.read_file(path)
            records = functions(raw)
            scripts[path] = {"functions": len(records), "function_records": [{**asdict(f), "trigger": f.trigger(raw)} for f in records],
                             "instructions": sum(len(instructions(raw, f)) for f in records),
                             "calls": calls(raw)}
    rows = []
    for cid in range(1, 32):
        path = f"Scripts/C{cid:02d}.cmb"
        script_calls = scripts.get(path, {}).get("calls", [])
        maps = []
        for mp in files:
            if re.fullmatch(rf"zmap/bmap{cid:02d}(?:_\d+)?/dispos.cmp", mp):
                groups = []
                for entry in pack.read_pack(disc.read_file(mp)):
                    _, parsed = dispos.parse(entry.data)
                    for group in parsed:
                        groups.append({"variant": entry.name, "group": group.name,
                                       "units": [{"pid": u.pid, "force": u.raw[0x61],
                                                  "xy": list(u.start)} for u in group.units]})
                maps.append({"path": mp, "groups": groups})
        relevant = [c for c in script_calls if any(s in c["command"] for s in INTEREST)]
        rows.append({"internal_id": cid, "title": titles.get(f"MCT{cid:02d}", "UNKNOWN"),
                     "script": path, "maps": maps, "caps": sortie_caps(disc, cid), "events": relevant,
                     "static_research": "inventory complete; conditions/reachability incomplete",
                     "automated": "see run log; never implies gameplay",
                     "runtime_current": "not tested", "cleared_current": "not tested",
                     "transition_current": "not tested", "netplay_current": "not tested",
                     "historical_evidence": RUNTIME.get(cid, "none documented"),
                     "research": {key: "unresolved; candidates below are not reconstructed behavior" for key in (
                         "victory_conditions", "defeat_and_game_over", "initial_simultaneous_factions",
                         "reinforcement_triggers", "available_roster", "forced_optional_restrictions",
                         "recruitment_conditions", "story_transfer_reachability", "objective_interaction",
                         "turn_phase_triggers", "death_requirements", "cleanup_transition_paths",
                         "save_load_interactions", "force_zero_assumptions", "ownership_conflicts")},
                     "unresolved": ["original objective predicates", "script reachability and order",
                                    "available roster vs scripted appearances", "production runtime acceptance"]})
    return {"baseline": BASELINE, "limitations": "group contents are NOT simultaneous deployment; calls are bounded pattern candidates",
            "chapters": rows, "scripts": scripts}


def report(data: dict) -> str:
    out = ["# Campaign compatibility matrix", "", f"Baseline: {data['baseline']}.", "",
           "Generated from the user's GFEE01 rev 0 image. Static inventory and local instruction CFGs cover discovered containers; "
           "event interpretation is incomplete. Every current-configuration gameplay axis remains untested. "
           "Historical reports are retained separately and must not be promoted to current acceptance.", "",
           "| Chapter | ID | Maps | Static research | Automated | Runtime | Cleared | Transition | Netplay |",
           "|---|---|---|---|---|---|---|---|---|"]
    for row in data["chapters"]:
        maps = ", ".join(m["path"].split("/")[1] for m in row["maps"])
        out.append(f"| {row['title']} | {row['internal_id']} | {maps} | inventory; conditions open | see run log | untested | untested | untested | untested |")
    out += ["", "## Multipart and special encounters", "",
            "Internal 18 is Chapter 17, Day Breaks. Both bmap18 and bmap18_3 are inventoried. "
            "The four gameplay stages need separate acceptance: 17-1 untested; 17-2 untested; 17-3 untested; 17-4 untested. "
            "Do not assign stage transitions to SetChapter without tracing C18's local Complete18/BMSetTurn flow.", "",
            "Internal 29 is Ch.27-2, Moment of Fate (separate special encounter), not Chapter 28. "
            "Internal 30 is Chapter 28; internal 31 is Endgame. Names come directly from Mess/common.m MCTxx.", ""]
    for row in data["chapters"]:
        out += [f"## {row['title']} — internal {row['internal_id']}", "",
                f"Historical evidence: {row['historical_evidence']}.", "",
                f"Slot-group counts by file suffix: `{row['caps']}`. These are candidates, not final effective caps.", "",
                "Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):", ""]
        for mp in row["maps"]:
            for g in mp["groups"]:
                if not g["units"]:
                    continue
                forces = {f: sorted(set(u["pid"] for u in g["units"] if u["force"] == f)) for f in range(4)}
                desc = "; ".join(f"F{f}: {', '.join(pids)}" for f, pids in forces.items() if pids)
                if desc:
                    out.append(f"- `{mp['path'].split('/')[1]}/{g['variant']}:{g['group']}`: {desc}")
        out += ["", "Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. "
                "The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.", "",
                "Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. "
                "`?` means computed/unknown. Conditional execution and trigger metadata are unresolved.", "",
                "| Offset | Function | Command | Literal suffix arguments |", "|---|---|---|---|"]
        for c in row["events"]:
            args = ", ".join("?" if a is None else str(a) for a in c["args"])
            out.append(f"| {c['offset']:X} | {c['function']} | {c['command']} | {args.replace('|', '/')} |")
        out += ["", "Open: " + "; ".join(row["unresolved"]) + ".", ""]
    return "\n".join(out) + "\n"


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--image", type=Path, default=DEFAULT_IMAGE)
    p.add_argument("--out", type=Path, default=Path("docs/CAMPAIGN_MATRIX.md"))
    p.add_argument("--json", type=Path, default=Path("work/campaign_inventory.json"))
    args = p.parse_args()
    with DiscReader(args.image) as disc:
        data = inventory(disc)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(report(data), encoding="utf-8")
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"{len(data['chapters'])} chapter IDs; {len(data['scripts'])} scripts; wrote {args.out}")


if __name__ == "__main__":
    main()
