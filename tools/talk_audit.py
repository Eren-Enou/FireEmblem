"""Read-only original Talk menu chain; static evidence, never runtime acceptance."""
from pathlib import Path
from tools.fe9.disc import DiscReader
from tools.fe9.ppc import Dol, direct_branch_target
from tools.verify_game import DEFAULT_IMAGE


# CAMP-007 in RESEARCH.md. Ends are exclusive and stop before the next function.
ROUTINES = {
    "Talk availability": (0x80078A24, 0x80078AB8),
    "Adjacent conversation targets": (0x8002B0A4, 0x8002B2E8),
    "Conversation target callback": (0x8002CD70, 0x8002CDCC),
}


def analyze(dol):
    result = {}
    for name, (start, end) in ROUTINES.items():
        calls = [(address, direct_branch_target(address, dol.u32(address)))
                 for address in range(start, end, 4)
                 if dol.u32(address) >> 26 == 18 and dol.u32(address) & 1]
        result[name] = {"start": start, "end": end, "calls": calls,
                        "instructions": dol.disasm(start, (end-start)//4)}
    result["matcher_direct_callers"] = dol.direct_callers(0x800BF1E8)
    result["table"] = {"menu_availability": dol.u32(0x80288974),
                       "target_callback": dol.u32(0x80284D48)}
    return result


def report(data):
    out = ["# Original Talk eligibility audit", "",
           "Generated with `python -m tools.talk_audit` from the read-only GFEE01 rev0 image. "
           "Evidence: RESEARCH.md CAMP-007; signatures pin this chain. STATIC ONLY; "
           "Yellow recruitment, event completion, roster retention and Netplay remain NOT TESTED.", "",
           "| Step | Original behavior | Co-op implication / limit |", "|---|---|---|",
           "| Menu callback | Reject context+0x16 bit0 or nonzero context+0x12; collect targets; reject empty list; return 2 if actor+0x1A5 bits4..6 nonzero, otherwise 0 | No force-list or force-ID read in this callback. Context and action-state semantics remain partly unresolved. |",
           "| Target enumeration | Read actor coordinates, four direction bits from a precomputed map halfword, and adjacent occupancy IDs; skip empty slots; dispatch non-null units to callback | No force-list traversal or actor/target force read here. Precomputed mask production is outside this analysis. |",
           "| Target callback | Set context target, query original kind8 matcher, append matching target's x/y/ID to result list | No extra force filter in this callback. |",
           "| Event matcher | Character identity, optional reversal and consumed-key check (CAMP-004) | A static absence of a force restriction is not proof of Yellow menu access or real recruitment. |", "",
           "The chapter10 Oscar/Kieran conversation is a useful runtime target: Oscar is "
           "P2-owned in EXP-16 and the original scene allows reversed participants. A synthetic "
           "fixture must retain a living prisoner, an unconsumed key, valid map adjacency and "
           "original Talk execution. The scene's force3 transfer alone does not prove permanent recruitment.", "",
           "## Pinned table links", "",
           f"- Talk availability: `0x{data['table']['menu_availability']:08X}`.",
           f"- Adjacent target callback: `0x{data['table']['target_callback']:08X}`.", "",
           "## Direct aligned calls to the kind8 matcher", "",
           ", ".join(f"`0x{a:08X}`" for a in data["matcher_direct_callers"]) + ". "
           "Indirect calls and other candidate-generation paths are not excluded.", ""]
    for name in ROUTINES:
        row = data[name]
        out += ["## " + name, "", "Direct calls: " + ", ".join(
            f"`0x{site:08X} -> 0x{target:08X}`" for site, target in row["calls"]) + ".", "",
            "```text", *row["instructions"], "```", ""]
    return "\n".join(out)


if __name__ == "__main__":
    with DiscReader(DEFAULT_IMAGE) as disc:
        result = analyze(Dol(disc.read_dol()))
    Path("docs/TALK_AUDIT.md").write_text(report(result), encoding="utf-8")
    print("generated original Talk chain; runtime NOT TESTED")
