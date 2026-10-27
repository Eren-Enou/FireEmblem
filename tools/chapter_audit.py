"""Static co-op compatibility audit of every chapter (read-only on the game image).

For each chapter id N it reads zmap/bmapNN/dispos.cmp (unit placement: force byte +0x61, F-02) and
Scripts/CNN.cmb (event script; the names of the script commands it calls and the PIDs it mentions are
stored as plain strings). It then flags what matters for the two-army system:

  escape        UnitEscape[ByPID] / PlayerEscape*                   -> escape objective; EXP-16 single-unit hand-back (F-40)
  cleanup       AllUnitEscape                                       -> standard chapter-end cleanup; EXP-16 hand-back (F-39)
  transfer      UnitTransferToForce[ByPID]                          -> story moves units between forces
  forced        UnitForcedSally[ByPID] / UnitDontMoveSally[ByPID]   -> fixed line-ups (F-41, F-46)
  sortie        Sally*                                              -> scripted deployment
  join          Join                                                -> recruitment mid-chapter
  phase         BMSetPhase                                          -> scripted phase changes
  partners      force 3 units in the dispos data (native yellow partners, e.g. Lethe in Ch9)
  owned         Player 2 PIDs from tools/owner_code.OWNERS that the chapter deploys or scripts

Static inspection is never proof of compatibility; RUNTIME lists what has actually been played.

Usage: python -m tools.chapter_audit [--out docs/CHAPTER_AUDIT.md]
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from tools.fe9 import dispos, pack
from tools.fe9.disc import DiscReader
from tools.owner_code import OWNERS
from tools.verify_game import DEFAULT_IMAGE

ROOT = Path(__file__).resolve().parents[1]
FLAGS = {
    "escape": ("UnitEscape", "UnitEscapeByPID", "PlayerEscapeCheck", "PlayerEscapeCount"),
    "cleanup": ("AllUnitEscape",),
    "transfer": ("UnitTransferToForce", "UnitTransferToForceByPID"),
    "forced": ("UnitForcedSally", "UnitForcedSallyByPID", "UnitDontMoveSally", "UnitDontMoveSallyByPID"),
    "sortie": ("SallySetByPos", "SallySetByGroup", "SallyAddByPos", "SallyAddByGroup", "SallyGetSurplus"),
    "join": ("Join",),
    "phase": ("BMSetPhase",),
}
# Chapter ids played with the co-op codes, and how (TESTING.md). Prologue = 1, Chapter N = N + 1.
RUNTIME = {
    1: "Prologue played with COOP-P3 (no yellow phase when force 3 is empty, F-37)",
    2: "Ch1 cleared with two armies (EXP-15 v3)",
    3: "Ch2 cleared, yellow Oscar/Boyd automatic (EXP-16)",
    4: "Ch3 cleared, yellow Shinon/Gatrie (EXP-16 run 2)",
    5: "Ch4 cleared, yellow Shinon/Gatrie (EXP-16 run 2)",
    6: "Ch5 cleared with 4 yellow units; suspend/resume; yellow death (EXP-18 session)",
    7: "Ch6 started; yellow death record verified (EXP-19); escape not yet played",
    10: "Ch9 several turns, incl. Netplay NET-01 (native partners Lethe/Mordecai)",
}
WORD = re.compile(rb"[A-Za-z_][A-Za-z0-9_]{2,40}")


def script_words(disc: DiscReader, cid: int) -> set[str]:
    name = f"Scripts/C{cid:02d}.cmb"
    if name not in disc.files():
        return set()
    return {m.group().decode() for m in WORD.finditer(disc.read_file(name))}


def dispos_units(disc: DiscReader, cid: int) -> dict[int, list[str]]:
    name = f"zmap/bmap{cid:02d}/dispos.cmp"
    if name not in disc.files():
        return {}
    files = {e.name: e.data for e in pack.read_pack(disc.read_file(name))}
    data = files.get("dispos_n.bin") or next(iter(files.values()))
    _date, groups = dispos.parse(data)
    out: dict[int, list[str]] = {}
    for g in groups:
        for u in g.units:
            out.setdefault(u.raw[0x61], []).append(u.pid)
    return out


def audit(disc: DiscReader) -> list[dict]:
    owned = {p for p, o in OWNERS.items() if o == 2}
    rows = []
    for cid in range(1, 32):
        words, units = script_words(disc, cid), dispos_units(disc, cid)
        if not words and not units:
            continue
        flags = [f for f, cmds in FLAGS.items() if any(c in words for c in cmds)]
        partners = sorted(set(units.get(3, [])))
        if partners:
            flags.append("partners")
        allies = sorted(set(units.get(0, [])))
        own_here = sorted(owned & (set(allies) | {w for w in words if w.startswith("PID_")}))
        rows.append({
            "cid": cid, "label": "Prologue" if cid == 1 else f"Ch{cid - 1}",
            "allies": allies, "partners": partners, "npcs": sorted(set(units.get(2, []))),
            "enemies": len(units.get(1, [])), "flags": flags, "owned": own_here,
            "transfer_pids": sorted(w for w in words if w.startswith("PID_")) if "transfer" in flags else [],
            "runtime": RUNTIME.get(cid, ""),
        })
    return rows


def needs(row: dict) -> str:
    """A conservative status: what this chapter still needs before it can be called compatible."""
    if row["runtime"]:
        return "runtime verified (partly)" if "not yet" in row["runtime"] or "started" in row["runtime"] else "runtime verified"
    risky = {"transfer", "escape", "partners", "phase"} & set(row["flags"])
    if risky:
        return "needs targeted check: " + ", ".join(sorted(risky))
    return "statically inspected only"


def report(rows: list[dict]) -> str:
    out = ["# Chapter compatibility audit (generated)", "",
           "Generated by `python -m tools.chapter_audit` from the game's own chapter data and event scripts. "
           "Static inspection does not prove compatibility; *runtime verified* means the chapter was played with "
           "the co-op codes (TESTING.md). Flag meanings are in the tool's docstring.", "",
           "| Chapter | id | Status | Flags | Player-2 PIDs involved | Native partners (force 3) | Allies (force 0) | NPCs (force 2) | Enemies |",
           "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        short = lambda pids: ", ".join(p.removeprefix("PID_") for p in pids) or "—"
        out.append(f"| {r['label']} | {r['cid']} | {needs(r)} | {', '.join(r['flags']) or '—'} | {short(r['owned'])} | "
                   f"{short(r['partners'])} | {short(r['allies'])} | {short(r['npcs'])} | {r['enemies']} |")
    out += ["", "## Runtime notes", ""]
    out += [f"- **{r['label']}** (id {r['cid']}): {r['runtime']}" for r in rows if r["runtime"]]
    out += ["", "## Chapters whose scripts transfer units between forces", "",
            "These can move a Player-2 character the table assigns, or a native partner, during the story; each needs a "
            "targeted check of which PIDs are moved and to which force (the PIDs listed are every PID the script mentions).", ""]
    out += [f"- **{r['label']}** (id {r['cid']}): {', '.join(p.removeprefix('PID_') for p in r['transfer_pids'])}"
            for r in rows if r["transfer_pids"]]
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path, default=ROOT / "docs/CHAPTER_AUDIT.md")
    ap.add_argument("--image", type=Path, default=DEFAULT_IMAGE)
    args = ap.parse_args()
    with DiscReader(args.image) as disc:
        rows = audit(disc)
    args.out.write_text(report(rows), encoding="utf-8", newline="\n")
    print(f"wrote {args.out} ({len(rows)} chapters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
