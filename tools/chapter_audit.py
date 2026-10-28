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
import struct
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


def script_strings(raw: bytes) -> dict[int, str]:
    """The .cmb string pool (little-endian header: +0x24 pool start, +0x28 function table), offset -> text."""
    base, end = struct.unpack_from("<II", raw, 0x24)
    out, o = {}, base
    while o < end:
        e = raw.index(b"\0", o)
        out[o - base] = raw[o:e].decode("latin-1")
        o = e + 1
    return out


def script_transfers(raw: bytes) -> list[tuple[str | None, int | None]]:
    """(PID, force) of every 2-argument UnitTransferToForce[ByPID] call.

    Bytecode seen in the scripts (F-48): 1C xx / 1D hh ll push a pool string, 19 nn pushes a small int,
    38 hh ll nn calls the command named at pool offset hhll with nn arguments. A transfer is therefore
    <push PID> 19 <force> 38 <name> 02; arguments built any other way are reported as None.
    """
    st = script_strings(raw)
    rev = {v: k for k, v in st.items()}
    found = []
    for name in ("UnitTransferToForceByPID", "UnitTransferToForce"):
        if name not in rev:
            continue
        off = rev[name]
        for m in re.finditer(re.escape(bytes([0x38, off >> 8, off & 0xFF, 2])), raw):
            pre = raw[max(0, m.start() - 8):m.start()]
            force = pre[-1] if len(pre) >= 2 and pre[-2] == 0x19 else None
            p = pre[:-2] if force is not None else pre
            pid = None
            if len(p) >= 2 and p[-2] == 0x1C:
                pid = st.get(p[-1])
            elif len(p) >= 3 and p[-3] == 0x1D:
                pid = st.get((p[-2] << 8) | p[-1])
            found.append((pid, force))
    return found


def script_calls(raw: bytes, names: tuple[str, ...]) -> list[tuple[str, list]]:
    """(command, literal args) for every call of the named commands (bytecode as in script_transfers)."""
    st = script_strings(raw)
    rev = {v: k for k, v in st.items()}
    out = []
    for name in names:
        if name not in rev:
            continue
        off = rev[name]
        for m in re.finditer(rb"\x38" + re.escape(bytes([off >> 8, off & 0xFF])) + rb"(.)", raw, re.S):
            n, pre, args, j = m.group(1)[0], raw[max(0, m.start() - 12):m.start()], [], None
            j = len(pre)
            while j > 0 and len(args) < n:
                if j >= 2 and pre[j - 2] == 0x19:
                    args.append(pre[j - 1]); j -= 2
                elif j >= 2 and pre[j - 2] == 0x1C:
                    args.append(st.get(pre[j - 1])); j -= 2
                elif j >= 3 and pre[j - 3] == 0x1D:
                    args.append(st.get((pre[j - 2] << 8) | pre[j - 1])); j -= 3
                else:
                    break
            out.append((name, list(reversed(args)) + [None] * (n - len(args))))
    return out


def sortie_caps(disc: DiscReader, cid: int) -> dict[str, int]:
    """Deployment slots per difficulty file: entries of the chapter's mikata group (F-56).

    SallySetByGroup(bmapNN_mikata_*) (0x8014CF48) resets state+0x544 and stores one (x, y) per group entry at
    state+0x545+2i, so the entry count is the sortie cap. Keys are the dispos file letters (c, h, m, n).
    """
    name = f"zmap/bmap{cid:02d}/dispos.cmp"
    if name not in disc.files():
        return {}
    caps = {}
    for e in pack.read_pack(disc.read_file(name)):
        _date, groups = dispos.parse(e.data)
        for g in groups:
            if re.fullmatch(rf"bmap{cid:02d}_mikata_[chmn]", g.name):
                caps[g.name[-1]] = len(g.units)
    return caps


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
        script = f"Scripts/C{cid:02d}.cmb"
        raw = disc.read_file(script) if script in disc.files() else b""
        transfers = script_transfers(raw) if raw else []
        forced = [a[0] for _n, a in script_calls(raw, ("UnitForcedSallyByPID", "UnitForcedSally"))] if raw else []
        rows.append({
            "cid": cid, "label": "Prologue" if cid == 1 else f"Ch{cid - 1}",
            "allies": allies, "partners": partners, "npcs": sorted(set(units.get(2, []))),
            "enemies": len(units.get(1, [])), "flags": flags, "owned": own_here,
            "transfers": transfers,
            "caps": sortie_caps(disc, cid), "forced": forced,
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
    out += ["", "## Deployment caps and forced units", "",
            "Sortie cap = entries of the chapter's `mikata` group, per difficulty file (F-56): `n`, `h`, `m`, `c`. "
            "Forced = `UnitForcedSally[ByPID]` arguments (`?` = not a literal). **Optional slots** = Normal cap − forced. "
            "Whether a chapter offers a real choice also needs the recruited roster to exceed the cap; that is checked "
            "at runtime (`state+0x544` at the prep screen), not here.", "",
            "| Chapter | id | cap n / h / m / c | Forced | Optional slots (n) |", "|---|---|---|---|---|"]
    for r in rows:
        if not r["caps"] and not r["forced"]:
            continue
        c = r["caps"]
        caps = " / ".join(str(c.get(k, "—")) for k in "nhmc")
        forced = ", ".join((f or "?").removeprefix("PID_") for f in r["forced"]) or "—"
        opt = (c.get("n", 0) - len(set(r["forced"]))) if c.get("n") is not None else "—"
        out.append(f"| {r['label']} | {r['cid']} | {caps} | {forced} | {opt} |")
    out += ["", "## Runtime notes", ""]
    out += [f"- **{r['label']}** (id {r['cid']}): {r['runtime']}" for r in rows if r["runtime"]]
    owned = {p for p, o in OWNERS.items() if o == 2}
    out += ["", "## Force transfers in the event scripts", "",
            "Every `UnitTransferToForce[ByPID]` call as PID → force, decoded from the bytecode (F-48). Force 0 = blue army, "
            "1 = enemy, 2 = green NPC, 3 = yellow partner, 5 = roster, 6 = died list, 7 = away. **Bold** = a Player-2 "
            "character in the current ownership table. `?` = the argument is not a literal.", ""]
    for r in rows:
        if r["transfers"]:
            items = []
            for pid, force in r["transfers"]:
                txt = f"{(pid or '?').removeprefix('PID_')} → {'?' if force is None else force}"
                items.append(f"**{txt}**" if pid in owned else txt)
            out.append(f"- **{r['label']}** (id {r['cid']}): " + ", ".join(items))
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
