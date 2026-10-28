"""Generate bounded event predicates and raw trigger metadata for every campaign script."""
import json
from pathlib import Path
from collections import Counter
from tools.fe9.disc import DiscReader
from tools.fe9.events import functions, instructions
from tools.fe9.event_paths import trace
from tools.chapter_audit import script_strings
from tools.campaign_audit import inventory
from tools.verify_game import DEFAULT_IMAGE

IMPORTANT = {"UnitTransferToForce", "UnitTransferToForceByPID", "UnitEscape", "UnitEscapeByPID",
             "Join", "AllUnitEscape", "BMSetTurn", "BMSetPhase", "Complete18"}


def analyze(disc):
    results, totals = [], Counter()
    for cid in range(1, 32):
        path = f"Scripts/C{cid:02d}.cmb"
        raw = disc.read_file(path)
        scenes = []
        for f in functions(raw):
            totals["functions"] += 1
            totals["instructions"] += len(instructions(raw, f))
            result = trace(raw, f.index, max_states=24, max_steps=1500)
            totals["complete_local_traces" if result["complete_local_trace"] else "incomplete_local_traces"] += 1
            important = [e for e in result["events"] if e["command"] in IMPORTANT or
                         (e["command"] == "set" and any(s in str(e["args"]) for s in ("gf_complete", "gf_gameover")))]
            if important or any(k in f.trigger(raw) for k in ("inferred_turn_trigger", "tile_event")):
                scenes.append({"index": f.index, "name": f.name, "trigger": f.trigger(raw),
                               "complete_local_trace": result["complete_local_trace"],
                               "outcomes": result["outcomes"], "events": important})
        results.append({"id": cid, "script": path, "scenes": scenes})
    return {"limits": {"states": 24, "steps": 1500}, "totals": dict(totals), "chapters": results}


def report(data, titles):
    out = ["# Campaign event predicates", "", "Static local CFG/symbolic analysis. Native calls are opaque; "
           "event registration, scene activation, global effects, world-state feasibility and gameplay are NOT proven. "
           "Infeasible combinations may remain; exact repeated contradictory predicates are pruned. "
           "Incomplete traces may omit later events. Full evidence is in ignored work/event_paths.json.", "",
           "VM format corroboration: https://feuniverse.us/t/fe9-and-fe10-event-script-doc-notes/6143. "
           "Signed operands and interpreter dispatch were independently read from this game's DOL.", "",
           "Totals: " + str(data["totals"]), ""]
    for chapter in data["chapters"]:
        out += [f"## {titles[chapter['id']]} — {chapter['script']}", ""]
        for scene in chapter["scenes"]:
            out += [f"### Scene {scene['index']}: {scene['name']}", "",
                    f"Trigger metadata: `{scene['trigger']}`. Local trace: " +
                    ("all explored local paths returned" if scene["complete_local_trace"] else "INCONCLUSIVE: unsupported operation or exploration bound"), ""]
            grouped = {}
            for e in scene["events"]:
                grouped.setdefault((e["offset"], e["command"]), []).append(e)
            for (offset, name), events in grouped.items():
                # Show one example, never silently imply that it is the only alternative.
                e = events[0]
                fmt = lambda s: str(s).replace("|", " OR ").replace("\n", " ")
                out.append(f"- `0x{offset:X} {name}({', '.join(map(fmt, e['args']))})`: {len(events)} explored alternative(s). "
                           + "Example local guards: " + (" AND ".join(map(fmt, e["conditions"])) or "none in this scene") + ".")
            out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    with DiscReader(DEFAULT_IMAGE) as disc:
        data = analyze(disc)
        titles = {r["internal_id"]: r["title"] for r in inventory(disc)["chapters"]}
    Path("work/event_paths.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    Path("docs/CAMPAIGN_EVENTS.md").write_text(report(data, titles), encoding="utf-8")
    print(data["totals"])
