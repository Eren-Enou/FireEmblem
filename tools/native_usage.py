"""Cross-reference aligned event calls against recovered native registrations.

Absence means no literal native call in these containers, never proof that an
engine routine is unreachable. Native indirect dispatch and imported helpers
remain outside this analysis. Full registration evidence stays in ignored work/.
"""
from collections import Counter
import json
from pathlib import Path

from tools.fe9.disc import DiscReader
from tools.fe9.events import calls
from tools.fe9.ppc import Dol
from tools.native_registry import registrations
from tools.verify_game import DEFAULT_IMAGE

FOCUS = (
    "PlayerEscapeCount", "PlayerEscapeCheck", "UnitEscape", "AllUnitEscape",
    "DefaultEscapeTalk", "PlayerDeadCheck", "EnemyDeadCheck", "GetDiedPlayerCount",
    "UnitDead", "UnitTransferToForce", "ForceGetCount", "UnitGetByPID", "Join",
    "SallySetByGroup", "UnitForcedSally", "BMSetPhase", "BMSetTurn",
)


def analyze(disc):
    registry = registrations(Dol(disc.read_dol()))
    by_name = {r["name"]: r for r in registry}
    sites = {name: [] for name in by_name}
    unresolved = Counter()
    scripts = sorted(p for p in disc.files() if p.startswith("Scripts/") and p.endswith(".cmb"))
    for path in scripts:
        for call in calls(disc.read_file(path)):
            if call["command"] in sites:
                sites[call["command"]].append({"script": path, "scene": call["function"],
                                               "offset": call["offset"], "args": call["args"]})
            else:
                unresolved[call["command"]] += 1
    return {"scripts": scripts, "registrations": registry, "sites": sites,
            "unresolved_names": dict(sorted(unresolved.items()))}


def render(data):
    sites = data["sites"]
    used = sum(bool(v) for v in sites.values())
    out = ["# Native event-command usage", "",
           f"{len(data['scripts'])} script containers; {len(sites)} literal native registrations; "
           f"{used} native names have aligned reachable local call instructions.", "",
           "This cross-reference excludes string-pool-only mentions. Each call is reachable in its "
           "local scene CFG; scene activation is unproven. Zero calls does not prove engine "
           "unreachability: indirect dispatch, native-to-native calls and imported script helpers "
           "are not resolved. Registration instruction evidence is generated in ignored work/native_usage.json.", "",
           "| Command | Direct script calls | Containers |",
           "|---|---:|---|"]
    for name in FOCUS:
        entries = sites.get(name, [])
        out.append(f"| {name} | {len(entries)} | " +
                   ", ".join(sorted({e["script"].removeprefix("Scripts/") for e in entries})) + " |")
    out += ["", "## Escape and death-check call sites", ""]
    for name in FOCUS[:9]:
        out += [f"### {name}", ""]
        for e in sites.get(name, []):
            out.append(f"- {e['script']} scene {e['scene']}, `0x{e['offset']:X}`, arguments `{e['args']}`.")
        if not sites.get(name):
            out.append("No direct aligned call in the scanned script containers.")
        out.append("")
    out += ["## Unresolved named calls", "",
            "These names lack a recovered literal native registration. They may be imported script "
            "helpers or other resolver entries; they are not assumed missing or unused.", "",
            "| Name | Call sites |", "|---|---:|"]
    out += [f"| {name} | {count} |" for name, count in data["unresolved_names"].items()]
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    with DiscReader(DEFAULT_IMAGE) as disc:
        data = analyze(disc)
    Path("work/native_usage.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
    Path("docs/NATIVE_USAGE.md").write_text(render(data), encoding="utf-8")
    print(f"{len(data['scripts'])} containers, {sum(map(len, data['sites'].values()))} native call sites")
