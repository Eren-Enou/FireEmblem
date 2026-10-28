"""Build a synthetic Dolphin 2609a GameCube input movie from poll-count steps.

This is test data, never proof of natural campaign progression. One emulated
controller only: poll ordering for multi-controller playback is not implemented.
The output and .sav must be new paths. Copies an existing project fixture and
never changes its payload. State-carried Gecko patches override installed INIs.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import shutil
import struct
from pathlib import Path

BUTTONS = {n: 1 << bit for bit, n in enumerate(("Start", "A", "B", "X", "Y", "Z", "Up", "Down", "Left", "Right", "L", "R"))}


def pad_record(buttons=(), x=128, y=128):
    if any(b not in BUTTONS for b in buttons) or not (0 <= x <= 255 and 0 <= y <= 255):
        raise ValueError("invalid controller command")
    mask = 0x4000
    for b in buttons:
        mask |= BUTTONS[b]
    return struct.pack("<H6B", mask, 255 if "L" in buttons else 0,
                       255 if "R" in buttons else 0, x, y, 128, 128)


def movie(recipe: list[dict], template: bytes | None = None) -> bytes:
    chunks = []
    count = 0
    for step in recipe:
        polls = step["polls"]
        if not isinstance(polls, int) or not 1 <= polls <= 36000:
            raise ValueError("poll count must be 1..36000")
        count += polls
        if count > 120000:
            raise ValueError("movie too large for this test harness")
        chunks.append(pad_record(step.get("buttons", ()), step.get("x", 128), step.get("y", 128)) * polls)
    if not count:
        raise ValueError("empty movie")
    if template is not None and (len(template) != 256 or template[:4] != b"DTM\x1A" or template[4:10] != b"GFEE01"):
        raise ValueError("template must be a GFEE01 Dolphin movie header")
    header = bytearray(template or bytes(256))
    header[:4] = b"DTM\x1A"
    header[4:10] = b"GFEE01"
    header[11] = 1  # pad 1 only
    header[12] = 1  # starts from paired state
    header[152] = 0  # never request memory-card clearing from template settings
    header[155] = 0  # synthetic local movie, not a Netplay recording
    header[161] = 0  # no GBA controller data in this format subset
    header[169:209] = bytes(40)  # no disc-change filename
    struct.pack_into("<QQ", header, 13, count, count)
    header[49:81] = b"Campaign test".ljust(32, b"\0")
    return bytes(header) + b"".join(chunks)


def build(state: Path, recipe: list[dict], output: Path, template: bytes | None = None):
    if not state.is_file():
        raise ValueError("source fixture missing")
    if template is None or len(template)!=256 or template[137]!=1:
        raise ValueError("a validated project DTM settings template is required")
    if output.suffix.lower()!=".dtm":
        raise ValueError("output must use .dtm extension")
    paired = Path(str(output) + ".sav")
    manifest = Path(str(output) + ".json")
    if any(p.exists() for p in (output, paired, manifest)):
        raise ValueError("refusing to replace an existing movie, state or manifest")
    data = movie(recipe, template)
    output.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation prevents accidental overwrite even if another process races.
    with output.open("xb") as stream:
        stream.write(data)
    with paired.open("xb") as stream, state.open("rb") as source:
        shutil.copyfileobj(source, stream)
    with manifest.open("x") as stream:
        stream.write(json.dumps({"classification": "synthetic input over an unchanged copied fixture",
                                   "state_sha256": hashlib.sha256(paired.read_bytes()).hexdigest(),
                                   "movie_sha256": hashlib.sha256(data).hexdigest(), "steps": recipe,
                                   "unit": "controller polls, NOT video frames",
                                   "runtime": "NOT TESTED until executed and inspected"}, indent=2))


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("state", type=Path)
    p.add_argument("recipe", type=Path)
    p.add_argument("output", type=Path)
    p.add_argument("--template", type=Path, required=True, help="existing project DTM; copy settings header only")
    a = p.parse_args()
    build(a.state, json.loads(a.recipe.read_text()), a.output,
          a.template.read_bytes()[:256] if a.template else None)
    print(f"created {a.output} and paired unchanged state")
