"""Configure GameCube controller port 2 in the portable Dolphin for two-controller tests (EXP-14).

  --port2 keyboard   port 2 = Standard Controller driven by a second keyboard layout (one-PC testing)
  --port2 device     port 2 = Standard Controller; map your own gamepad in Dolphin > Controllers afterwards
  --port2 none       port 2 = None (Dolphin's default; EXP-14 then falls back to port 1)

Edits Dolphin-x64/User/Config/Dolphin.ini ([Core] SIDevice1) and GCPadNew.ini ([GCPad2]). Both files are
backed up to <name>.bak first. Refuses to run while Dolphin is open, because Dolphin rewrites them on exit.

Usage: python -m tools.setup_pads --port2 keyboard
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SI_NONE, SI_GC_CONTROLLER = 0, 6

# Port 1 (the existing layout) uses X Z C S D Return, arrows, I J K L, Q W, T F G H.
# Port 2 uses keys that port 1 does not. The stick is on the numeric keypad; NUMPAD0..NUMPAD9 are the
# names Dolphin's DInput keyboard backend gives those keys (not the top-row digits "8", "5", ...).
_KEYS = {
    "Buttons/A": "M", "Buttons/B": "N", "Buttons/X": "B", "Buttons/Y": "V", "Buttons/Z": "E",
    "Buttons/Start": "Y",
    "Main Stick/Up": "NUMPAD8", "Main Stick/Down": "NUMPAD5",
    "Main Stick/Left": "NUMPAD4", "Main Stick/Right": "NUMPAD6",
    "Main Stick/Modifier": "RSHIFT",
    "Triggers/L": "O", "Triggers/R": "P",
    "D-Pad/Up": "U", "D-Pad/Down": "J", "D-Pad/Left": "R", "D-Pad/Right": "A",
}
_PORT1_KEYS = {
    "Buttons/A": "X", "Buttons/B": "Z", "Buttons/X": "C", "Buttons/Y": "S", "Buttons/Z": "D",
    "Buttons/Start": "RETURN",
    "Main Stick/Up": "UP", "Main Stick/Down": "DOWN", "Main Stick/Left": "LEFT", "Main Stick/Right": "RIGHT",
    "Main Stick/Modifier": "Shift",
    "C-Stick/Up": "I", "C-Stick/Down": "K", "C-Stick/Left": "J", "C-Stick/Right": "L",
    "Triggers/L": "Q", "Triggers/R": "W",
    "D-Pad/Up": "T", "D-Pad/Down": "G", "D-Pad/Left": "F", "D-Pad/Right": "H",
}
_CALIBRATION = "100.00 141.42 100.00 141.42 100.00 141.42 100.00 141.42"


def keyboard_layout(keys: dict[str, str]) -> dict[str, str]:
    """A [GCPadN] section body for Dolphin's DInput keyboard from {control: key name}."""
    return {"Device": "DInput/0/Keyboard Mouse", **{k: f"`{v}`" for k, v in keys.items()},
            "Main Stick/Calibration": _CALIBRATION}


PORT1_KEYBOARD = keyboard_layout(_PORT1_KEYS)   # Dolphin-x64's existing port 1 layout
PORT2_KEYBOARD = keyboard_layout(_KEYS)


def set_ini(text: str, section: str, items: dict[str, str], replace_section: bool = False) -> str:
    """Set key = value pairs in one [section] of an ini text (creating it if needed)."""
    lines = text.splitlines()
    head = f"[{section}]"
    if head not in lines:
        lines += [head]
    start = lines.index(head) + 1
    end = start
    while end < len(lines) and not lines[end].startswith("["):
        end += 1
    body = [] if replace_section else lines[start:end]
    keys = {k: i for i, k in enumerate(line.split("=")[0].strip() for line in body)}
    for k, v in items.items():
        if k in keys:
            body[keys[k]] = f"{k} = {v}"
        else:
            body.append(f"{k} = {v}")
    return "\n".join(lines[:start] + body + lines[end:]) + "\n"


def dolphin_running() -> bool:
    if sys.platform != "win32":
        return False
    out = subprocess.run(["tasklist", "/FI", "IMAGENAME eq Dolphin.exe"], capture_output=True, text=True).stdout
    return "Dolphin.exe" in out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port2", choices=["keyboard", "device", "none"], required=True)
    ap.add_argument("--dolphin", type=Path, default=ROOT / "Dolphin-x64")
    args = ap.parse_args()
    if dolphin_running():
        print("close Dolphin first (it rewrites its config on exit)", file=sys.stderr)
        return 1
    cfg = args.dolphin / "User" / "Config"
    core, pads = cfg / "Dolphin.ini", cfg / "GCPadNew.ini"
    for f in (core, pads):
        if f.exists():
            shutil.copy2(f, f.with_suffix(".ini.bak"))
    si = SI_NONE if args.port2 == "none" else SI_GC_CONTROLLER
    core.write_text(set_ini(core.read_text() if core.exists() else "", "Core", {"SIDevice1": str(si)}))
    if args.port2 == "keyboard":
        pads.write_text(set_ini(pads.read_text() if pads.exists() else "", "GCPad2", PORT2_KEYBOARD,
                                replace_section=True))
    print(f"port 2 = {args.port2} (SIDevice1 = {si}); backups: *.ini.bak in {cfg}")
    if args.port2 == "keyboard":
        print("port 2 keys: A=M B=N X=B Y=V Z=E Start=Y stick=numpad 8/5/4/6 L=O R=P")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
