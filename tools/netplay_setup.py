"""Create separate Dolphin user folders for a Netplay host and client (Phase 3, NET-01).

Each folder is a complete, private Dolphin user directory, so a Netplay session never touches
Dolphin-x64/User (the user's own memory card, save states and config):

  work/netplay/host/    Player 1, blue. COOP-P3 enabled; its memory card (GC/USA/Card A) is the
                        save data that Netplay sends to the client.
  work/netplay/client/  Player 2, yellow. No codes of its own (the host's codes are synced).

Both get the game folder, Enable Cheats, and a keyboard layout on *their own* port 1. In Netplay each
player's local controller 1 is what the host's pad mapping assigns to a GameCube port, so the client's
local pad 1 uses the port-2 keys (A=M B=N ... stick = numpad 8/5/4/6). Background Input is on, so
two instances on one PC can both read one keyboard (one-PC loopback test).

The host's card starts with the Chapter 9 save (work/saves/netplay_ch9_card/, made by NET-00: a fresh
game with EXP-05, Prologue won, saved when prompted; file 2 = "Ch. 9: Gallia"). Netplay cannot start from
the slot 6 state: Dolphin refuses to load states during Netplay, and a suspend made from that state is
rejected as "not the original Memory Card" (RESEARCH F-31). Title > Restart Chapter > Ch. 9 instead.

Internet session (NET-02): --host-only --traversal makes just the host folder, hosting through Dolphin's
Traversal Server (room code) with Background Input off; Player 2 uses the ZIP from tools/netplay_package.
--card DIR picks the host's memory card files (default: the Chapter 9 card above).

Usage: python -m tools.netplay_setup [--root work/netplay] [--enable CODE ...] [--client-stick numpad|digits] [--force]
       python -m tools.netplay_setup --root work/ch1 --enable COOP-P3 --enable EXP-15   (Chapter 1 test bed)
       python -m tools.netplay_setup --root work/netplay_net --host-only --traversal --card work/saves/net02_card            --enable COOP-P5 --enable EXP-16                                            (NET-02 host)
Launch: Dolphin-x64/Dolphin.exe --user work/netplay/host   (and --user work/netplay/client)
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from tools.install_codes import build_ini
from tools.setup_pads import PORT1_KEYBOARD, _KEYS, keyboard_layout, set_ini

ROOT = Path(__file__).resolve().parents[1]
CH9_CARD = ROOT / "work/saves/netplay_ch9_card"
PORT = 2626
_DIGITS = {"Main Stick/Up": "8", "Main Stick/Down": "5", "Main Stick/Left": "4", "Main Stick/Right": "6"}


def dolphin_ini(games: Path, nickname: str, host: bool, traversal: bool = False) -> str:
    sections = {
        "General": {"ISOPaths": "1", "ISOPath0": str(games)},
        "Analytics": {"Enabled": "False", "PermissionAsked": "True"},
        # The host also has port 2 (numpad layout) so it doubles as a one-window, two-controller test bed.
        "Core": {"EnableCheats": "True", "SIDevice0": "6", "SIDevice1": "6" if host else "0"},
        "Input": {"BackgroundInput": "True"},
        "NetPlay": {"Nickname": nickname, "TraversalChoice": "direct", "Address": "127.0.0.1",
                    "HostPort": str(PORT), "ConnectPort": str(PORT)},
    }
    if traversal:
        # One player per PC: keys only reach the focused game window (typing in the chat moves nothing).
        sections["Input"]["BackgroundInput"] = "False"
        sections["NetPlay"].update({"TraversalChoice": "traversal", "TraversalServer": "stun.dolphin-emu.org",
                                    "TraversalPort": "6262"})
    if host:
        # Start from the host's memory card, and discard what the session writes (first experiments).
        sections["NetPlay"].update({"SyncSaves": "True", "SyncCodes": "True", "WriteSaveData": "False"})
    text = ""
    for name, items in sections.items():
        text = set_ini(text, name, items)
    return text


def make_user(dest: Path, games: Path, nickname: str, pad: dict[str, str], codes: str | None,
              pad2: dict[str, str] | None = None, traversal: bool = False) -> None:
    (dest / "Config").mkdir(parents=True)
    (dest / "Config/Dolphin.ini").write_text(dolphin_ini(games, nickname, codes is not None, traversal))
    pads = set_ini("", "GCPad1", pad)
    if pad2:
        pads = set_ini(pads, "GCPad2", pad2)
    (dest / "Config/GCPadNew.ini").write_text(pads)
    (dest / "GC/USA/Card A").mkdir(parents=True)
    if codes is not None:
        (dest / "GameSettings").mkdir()
        (dest / "GameSettings/GFEE01.ini").write_text(codes)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", type=Path, default=ROOT / "work/netplay")
    ap.add_argument("--dolphin", type=Path, default=ROOT / "Dolphin-x64")
    ap.add_argument("--enable", action="append", default=None, help="host codes (default: COOP-P3)")
    ap.add_argument("--client-stick", choices=["numpad", "digits"], default="numpad",
                    help="client stick keys; 'digits' = top-row 8/5/4/6 for drivers without a keypad")
    ap.add_argument("--force", action="store_true", help="replace existing host/client folders")
    ap.add_argument("--host-only", action="store_true", help="make only the host folder (Player 2 uses the ZIP)")
    ap.add_argument("--traversal", action="store_true", help="host through Dolphin's Traversal Server")
    ap.add_argument("--card", type=Path, default=CH9_CARD, help="folder with the host's .gci card files")
    args = ap.parse_args()

    root = args.root.resolve()
    if (args.dolphin / "User").resolve() in (root, *root.parents) or root == ROOT:
        print("refusing: --root must not be inside Dolphin-x64/User", file=sys.stderr)
        return 1
    host, client = root / "host", root / "client"
    for d in (host,) if args.host_only else (host, client):
        if d.exists():
            if not args.force:
                print(f"{d} exists (use --force to recreate it; its memory card is lost)", file=sys.stderr)
                return 1
            shutil.rmtree(d)

    games = (args.dolphin / "Games").resolve()
    client_keys = {**_KEYS, **(_DIGITS if args.client_stick == "digits" else {})}
    make_user(host, games, "P1-Blue", PORT1_KEYBOARD, build_ini(args.enable or ["COOP-P3"], verbose=False),
              pad2=keyboard_layout(client_keys), traversal=args.traversal)
    if not args.host_only:
        make_user(client, games, "P2-Yellow", keyboard_layout(client_keys), None)
    for gci in sorted(args.card.glob("*.gci")):
        shutil.copy2(gci, host / "GC/USA/Card A" / gci.name)

    exe = (args.dolphin / "Dolphin.exe").resolve()
    print(f"host:   {exe} --user {host}")
    if not args.host_only:
        print(f"client: {exe} --user {client}")
    print(f"host codes: {', '.join(args.enable or ['COOP-P3'])}; "
          f"{'traversal server' if args.traversal else f'port {PORT}'}; client stick = {args.client_stick}")
    if not any(args.card.glob("*.gci")):
        print(f"note: no card in {args.card}; make the Chapter 9 card save first (TESTING.md NET-00)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
