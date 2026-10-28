"""Build and verify the shareable Netplay client ZIP for Player 2 (NET-02).

The ZIP is everything a friend needs besides their own Dolphin (already the right version) and their own
game copy. It has no launcher or script: the README says how to start Dolphin with the package's folder.

  FE9-Coop-Client/README.txt               setup, join (Traversal Server room code), controls, checklist, test steps
  FE9-Coop-Client/User/Config/Dolphin.ini  private user folder: cheats on, port 1 = controller, traversal
  FE9-Coop-Client/User/Config/GCPadNew.ini port 1 keyboard layout (the whole keyboard; one player per PC)
  FE9-Coop-Client/User/GameSettings/GFEE01.ini   all code definitions, PACKAGE_CODES enabled
  FE9-Coop-Client/MANIFEST.txt             versions, code fingerprint, SHA-256 of every other file

No game data, save data or memory card is included (verify() enforces an exact file list). The host's
codes are what Netplay actually runs ("Sync AR/Gecko Codes", F-47); the client's copy and the fingerprint
let both players confirm the definitions match before starting; the friend checks the code file's SHA-256
against MANIFEST.txt with Windows' own Get-FileHash.

Code fingerprint: the first 16 hex digits of SHA-256 over the enabled codes of a GameSettings ini, each as
"<kind>:$<name>" followed by its code lines (whitespace-normalised, upper case).

The archive is reproducible: fixed timestamps and order, so the same sources give the same bytes.

Usage: python -m tools.netplay_package                       build dist/FE9-Coop-Client-<fp>.zip and verify it
       python -m tools.netplay_package --verify ZIP          check an existing ZIP
       python -m tools.netplay_package --fingerprint DIR     fingerprint of DIR/GameSettings/GFEE01.ini
                                                             (DIR = a Dolphin user folder, e.g. the host's)
"""

from __future__ import annotations

import argparse
import hashlib
import io
import re
import sys
import zipfile
from pathlib import Path

from tools.install_codes import build_ini, parse_sections
from tools.setup_pads import PORT1_KEYBOARD, set_ini

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "netplay/client"
PACKAGE_CODES = ["COOP-P6", "EXP-16"]
PACKAGE_VERSION = "net02-3"
DOLPHIN_VERSION = "2609a"            # F-47; the version NET-01 ran on
GAME = "GFEE01 rev 0"
# Dolphin's Verify of the project's copy (DolphinTool verify). Informational: other dump formats agree only
# when the disc data is identical, and Netplay's own SHA1 Digest check is the deciding one.
GAME_SHA1 = "a30eca376ab9b2b4dd8b1a9136772a62c0309ace"
TRAVERSAL_SERVER, TRAVERSAL_PORT = "stun.dolphin-emu.org", "6262"   # Dolphin's defaults (strings in Dolphin.exe)
TOP = "FE9-Coop-Client"
FILES = ["README.txt", "User/Config/Dolphin.ini", "User/Config/GCPadNew.ini", "User/GameSettings/GFEE01.ini", "MANIFEST.txt"]
MAX_BYTES = 256 * 1024
# Game/save data, and (since net02-2) no Dolphin binaries or launcher scripts.
FORBIDDEN = re.compile(r"\.(gci|sav|raw|dtm|dol|elf|cmp|iso|ciso|gcm|gcz|rvz|wia|wbfs|nkit|s\d\d"
                       r"|exe|dll|bat|cmd|ps1|vbs|lnk)$", re.I)
_EPOCH = (2026, 1, 1, 0, 0, 0)


def enabled_codes(ini_text: str) -> list[tuple[str, str, list[str]]]:
    """(kind, name, code lines) of every enabled code, in definition order."""
    sec = parse_sections(ini_text)
    out = []
    for kind in ("ActionReplay", "Gecko"):
        on = {l[1:].strip() for l in sec.get(f"{kind}_Enabled", []) if l.startswith("$")}
        cur = None
        for line in sec.get(kind, []):
            if line.startswith("$"):
                cur = (kind, line[1:].strip(), [])
                if cur[1] in on:
                    out.append(cur)
                else:
                    cur = None
            elif cur and not line.startswith("*"):
                cur[2].append(" ".join(line.split()).upper())
    return out


def fingerprint(ini_text: str) -> str:
    lines = []
    for kind, name, code in enabled_codes(ini_text):
        lines += [f"{kind}:${name}", *code]
    return hashlib.sha256(("\n".join(lines) + "\n").encode("utf-8")).hexdigest()[:16]


def dolphin_ini() -> str:
    sections = {
        "Analytics": {"Enabled": "False", "PermissionAsked": "True"},
        "Core": {"EnableCheats": "True", "SIDevice0": "6", "SIDevice1": "0", "SIDevice2": "0", "SIDevice3": "0"},
        # Keys reach only the focused game window (the chat box would otherwise move units).
        "Input": {"BackgroundInput": "False"},
        "NetPlay": {"Nickname": "P2-Yellow", "TraversalChoice": "traversal", "TraversalServer": TRAVERSAL_SERVER,
                    "TraversalPort": TRAVERSAL_PORT, "ConnectPort": "2626", "HostPort": "2626"},
    }
    text = ""
    for name, items in sections.items():
        text = set_ini(text, name, items)
    return text


def _crlf(text: str) -> bytes:
    return text.replace("\r\n", "\n").replace("\n", "\r\n").encode("ascii")


def contents() -> dict[str, bytes]:
    codes = build_ini(PACKAGE_CODES, verbose=False)
    fp = fingerprint(codes)
    files = {"User/Config/Dolphin.ini": _crlf(dolphin_ini()),
             "User/Config/GCPadNew.ini": _crlf(set_ini("", "GCPad1", PORT1_KEYBOARD)),
             "User/GameSettings/GFEE01.ini": _crlf(codes)}
    subst = {"PACKAGE_VERSION": PACKAGE_VERSION, "CODES": " + ".join(PACKAGE_CODES), "FINGERPRINT": fp,
             "DOLPHIN_VERSION": DOLPHIN_VERSION, "GAME_SHA1": GAME_SHA1,
             "CODES_SHA256": hashlib.sha256(files["User/GameSettings/GFEE01.ini"]).hexdigest().upper()}
    text = (SOURCE / "README.txt").read_text(encoding="ascii")
    for k, v in subst.items():
        text = text.replace(f"@@{k}@@", v)
    files["README.txt"] = _crlf(text)
    manifest = [f"package_version={PACKAGE_VERSION}", f"codes={' + '.join(PACKAGE_CODES)}",
                f"codes_fingerprint={fp}", f"dolphin_version={DOLPHIN_VERSION}", f"game={GAME}",
                f"game_sha1={GAME_SHA1}", f"traversal_server={TRAVERSAL_SERVER}", f"traversal_port={TRAVERSAL_PORT}", ""]
    manifest += [f"sha256 {hashlib.sha256(files[n]).hexdigest()} {n}" for n in FILES if n in files]
    files["MANIFEST.txt"] = _crlf("\n".join(manifest) + "\n")
    return files


def build(out: Path) -> Path:
    files = contents()
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name in FILES:
            info = zipfile.ZipInfo(f"{TOP}/{name}", _EPOCH)
            info.compress_type, info.external_attr = zipfile.ZIP_DEFLATED, 0o644 << 16
            z.writestr(info, files[name])
        # The private memory card folder exists but stays empty; Netplay supplies the host's save data.
        info = zipfile.ZipInfo(f"{TOP}/User/GC/USA/Card A/", _EPOCH)
        info.external_attr = 0o40755 << 16 | 0x10
        z.writestr(info, b"")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(buf.getvalue())
    return out


def verify(path: Path) -> list[str]:
    """Problems found in a client ZIP (empty list = good)."""
    problems = []
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        dirs = [n for n in names if n.endswith("/")]
        files = {n.removeprefix(f"{TOP}/"): z.read(n) for n in names if not n.endswith("/")}
    if set(files) != set(FILES) or len(files) != len(FILES):
        problems.append(f"file list differs: extra {sorted(set(files) - set(FILES))}, missing {sorted(set(FILES) - set(files))}")
    if dirs != [f"{TOP}/User/GC/USA/Card A/"]:
        problems.append(f"unexpected folders {dirs}")
    for n in names:
        if FORBIDDEN.search(n.rstrip("/")) or not n.startswith(f"{TOP}/"):
            problems.append(f"forbidden entry {n}")
    total = sum(len(b) for b in files.values())
    if total > MAX_BYTES:
        problems.append(f"{total} bytes uncompressed (limit {MAX_BYTES})")
    for n, b in files.items():
        if any(c > 0x7E and c not in (0x0D, 0x0A) for c in b) or b"@@" in b:
            problems.append(f"{n}: non-ASCII byte or unfilled placeholder")
        if re.search(rb"[A-Za-z]:\\", b) and n != "README.txt":
            problems.append(f"{n}: contains a local absolute path")
    ini = files.get("User/GameSettings/GFEE01.ini", b"").decode("ascii", "replace")
    want = build_ini(PACKAGE_CODES, verbose=False)
    if fingerprint(ini) != fingerprint(want):
        problems.append(f"code fingerprint {fingerprint(ini)} != {fingerprint(want)} (codes/GFEE01.ini changed? rebuild)")
    names_on = [name for _k, name, _c in enabled_codes(ini)]
    if len(names_on) != len(PACKAGE_CODES) or any(n.startswith("DBG-") for n in names_on):
        problems.append(f"enabled codes {names_on}")
    man = files.get("MANIFEST.txt", b"").decode("ascii", "replace")
    if f"codes_fingerprint={fingerprint(want)}" not in man:
        problems.append("MANIFEST fingerprint does not match the codes")
    for line in man.splitlines():
        if line.startswith("sha256 "):
            _s, digest, n = line.split(" ", 2)
            if n not in files or hashlib.sha256(files[n]).hexdigest() != digest:
                problems.append(f"MANIFEST hash mismatch for {n}")
    if man.count("sha256 ") != len(FILES) - 1:
        problems.append("MANIFEST does not list every file")
    dini = files.get("User/Config/Dolphin.ini", b"").decode("ascii", "replace")
    for need in ("EnableCheats = True", "SIDevice0 = 6", "TraversalChoice = traversal", "BackgroundInput = False"):
        if need not in dini:
            problems.append(f"Dolphin.ini lacks '{need}'")
    if "ISOPath" in dini:
        problems.append("Dolphin.ini carries a game path")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--verify", type=Path, metavar="ZIP")
    ap.add_argument("--fingerprint", type=Path, metavar="USER_DIR")
    args = ap.parse_args()
    if args.fingerprint:
        ini = args.fingerprint / "GameSettings/GFEE01.ini" if args.fingerprint.is_dir() else args.fingerprint
        text = ini.read_text()
        print(fingerprint(text))
        for _k, name, _c in enabled_codes(text):
            print(f"  enabled: {name}")
        expected = fingerprint(build_ini(PACKAGE_CODES, verbose=False))
        print("matches the client package" if fingerprint(text) == expected else f"DIFFERS from the package ({expected})")
        return 0 if fingerprint(text) == expected else 1
    path = args.verify
    if path is None:
        fp = fingerprint(build_ini(PACKAGE_CODES, verbose=False))
        path = build(args.out or ROOT / f"dist/{TOP}-{fp}.zip")
        print(f"built {path} ({path.stat().st_size} bytes), codes {' + '.join(PACKAGE_CODES)}, fingerprint {fp}")
    problems = verify(path)
    for p in problems:
        print(f"PROBLEM: {p}", file=sys.stderr)
    if not problems:
        with zipfile.ZipFile(path) as z:
            for i in z.infolist():
                print(f"  {i.file_size:7d}  {i.filename}")
        print(f"verified: {path} sha256 {hashlib.sha256(path.read_bytes()).hexdigest()}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
