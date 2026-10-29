"""Capture comparable FE9 state evidence, or compare two local/remote snapshots.

Does not drive Dolphin or prove an event happened. Save states must be captured
after the original interaction; record exact configuration/commit with each run.
Usage: python -m tools.campaign_snapshot STATE --ini USER/GameSettings/GFEE01.ini --out work/run.json
       python -m tools.campaign_snapshot --compare work/host.json work/client.json
"""
from __future__ import annotations
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

from tools.inspect_state import STATE, UNITS, load_mem1
from tools.netplay_package import fingerprint, enabled_codes
from tools.verify_game import DEFAULT_IMAGE
from tools.loaded_scripts import inspect as loaded_scripts
from tools.event_state import inspect as event_state, chapter17_request


def configuration_flags(names):
    """Identify active known setup codes; absence never certifies natural history."""
    setup=[name for name in names if name.startswith(("FIXTURE-", "DBG-CAMP-"))
           or name.split()[0] == "EXP-05"]
    return {"debug": any(name.startswith("DBG-") for name in names),
            "synthetic_setup": bool(setup), "setup_codes": setup}


def observe_hooks(mem, dol, text):
    """Compare intended C2 bodies to RAM; mutable cave data may conservatively mismatch."""
    observations=[]
    for kind,name,lines in enabled_codes(text):
        if kind!="Gecko":continue
        pos=0
        while pos<len(lines):
            command,count=(int(w,16) for w in lines[pos].split());pos+=1
            if command>>24 in (0xC0,0xC2):
                payload=[int(w,16) for line in lines[pos:pos+count] for w in line.split()]
                pos+=count
                if command>>24!=0xC2:continue
                hook=0x80000000|(command&0x1FFFFFF)
                original,actual=dol.u32(hook),mem.u32(hook)
                status="original instruction" if actual==original else "unmatched patch"
                if actual!=original and actual>>26==18 and not actual&2:
                    delta=(actual&0x3FFFFFC)-(0x4000000 if actual&0x2000000 else 0)
                    target=hook+delta
                    if 0x80001800<=target<0x80003000:
                        expected=b"".join(w.to_bytes(4,"big") for w in payload[:-1])
                        if mem.read(target,len(expected))==expected:status="intended C2 body matched"
                observations.append({"code":name.split()[0],"hook":hook,"original":original,"actual":actual,"status":status})
    return observations


def capture(path: Path, image: Path, ini: Path, commit: str) -> dict:
    info, mem = load_mem1(path, image)
    units = []
    for i in range(159):
        addr = UNITS + i * 0x280
        char = mem.u32(addr + 0x188)
        if not char:
            continue
        force = mem.u32(addr + 0x190)
        flags = mem.u32(addr + 0x1A0)
        cls = mem.u32(addr + 0x18C)
        units.append({"slot": i + 1, "pid": mem.cstr(mem.u32(char)),
                      "class": mem.cstr(mem.u32(cls)) if cls else None,
                      "force": mem.u8(force + 8) if force else None,
                      "hp": mem.u8(addr + 0x1A8), "level": mem.u8(addr + 0x19A),
                      "exp": mem.u8(addr + 0x19B), "gauge": mem.u8(addr + 0x19C),
                      "xy": [mem.u8(addr + 0x19E), mem.u8(addr + 0x19F)],
                      "inventory_slots_hex": mem.read(addr + 0x1CC, 64).hex(),  # CAMP-005, eight original 8-byte slots
                      "rescue_link": mem.u32(addr + 0x194),
                      "action_state_byte": mem.u8(addr + 0x1A5),  # CAMP-007 original Talk gate
                      "flags": flags, "owned": bool(flags & 0x20000000),
                      "escaped": bool(flags & 0x4000),  # CAMP-001/F-43 original escape flag
                      "owner": 2 if flags & 0x60000000 == 0x60000000 else 1 if flags & 0x20000000 else None,
                      "death_record": bool(flags & 0x8000), "death_chapter": mem.u8(addr + 0x234)})
    text = ini.read_text()
    names = [n for _, n, _ in enabled_codes(text)]
    from tools.fe9.disc import DiscReader
    from tools.fe9.ppc import Dol
    with DiscReader(image) as disc:
        observations=observe_hooks(mem,Dol(disc.read_dol()),text)
    from tools.talk_evidence import capture as talk_fields
    local_talk=None
    if mem.u8(STATE+0x10)==11:
        try:local_talk=talk_fields(mem)
        except ValueError as exc:local_talk={"inconclusive":str(exc),"scope":"Talk fixture fields unavailable"}
    return {"schema": 1, "evidence": {"commit": commit, "state_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
             "dolphin": info.dolphin_version, "codes_fingerprint": fingerprint(text), "codes": names,
             **configuration_flags(names),
             "hooks":observations,
             "intended_c2_verified":bool(observations) and all(o["status"]=="intended C2 body matched" for o in observations),
             "warning": "INI is intended configuration; old savestates may restore different active patches"},
            "game": {"chapter": mem.u8(STATE + 0x10), "phase": mem.u8(STATE + 0x11),
                     "event_flags": event_state(mem),
                     **({'chapter17_request': chapter17_request(mem)} if mem.u8(STATE+0x10)==18 else {}),
                     "battle_stage": {"status": "UNKNOWN",
                         "reason": "chapter/CMB identify container, not a decoded battle-stage discriminator"},
                     "event_scripts": loaded_scripts(mem,mem.u8(STATE + 0x10)),
                     **({"talk_fixture":local_talk} if local_talk is not None else {}),
                     "turn": mem.u16(STATE + 0x12), "control": list(mem.read(STATE + 0x14, 4)), "units": units}}


def differences(a: dict, b: dict) -> list[str]:
    out = []
    for key in ("commit", "dolphin", "codes_fingerprint"):
        if a["evidence"][key] != b["evidence"][key]:
            out.append(f"configuration mismatch: {key}")
    if a["game"] != b["game"]:
        for key in sorted((a['game'].keys() | b['game'].keys()) - {'units'}):
            if key not in a["game"] or key not in b["game"]:
                if key in a["game"] or key in b["game"]:
                    out.append(f"{key}: missing from one snapshot")
                continue
            if a["game"][key] != b["game"][key]:
                out.append(f"{key}: {a['game'][key]} != {b['game'][key]}")
        left = {u["slot"]: u for u in a["game"]["units"]}
        right = {u["slot"]: u for u in b["game"]["units"]}
        for slot in sorted(left.keys() | right.keys()):
            if left.get(slot) != right.get(slot):
                out.append(f"unit slot {slot}: {left.get(slot)} != {right.get(slot)}")
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("state", type=Path, nargs="?")
    p.add_argument("--image", type=Path, default=DEFAULT_IMAGE)
    p.add_argument("--ini", type=Path)
    p.add_argument("--out", type=Path)
    p.add_argument("--compare", type=Path, nargs=2)
    args = p.parse_args()
    if args.compare:
        issues = differences(*(json.loads(f.read_text()) for f in args.compare))
        print("\n".join(issues) if issues else "MATCH: captured fields only, not complete RAM")
        return int(bool(issues))
    if not (args.state and args.ini and args.out):
        p.error("capture requires STATE --ini --out")
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    data = capture(args.state, args.image, args.ini, commit)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(data, indent=2))
    print(f"wrote {args.out}; intended codes {data['evidence']['codes_fingerprint']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
