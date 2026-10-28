"""Measure enabled Gecko bytes and repeated C2 hook ownership without writing Dolphin profiles."""
from pathlib import Path
from tools.install_codes import ROOT, gecko_budget, gecko_sizes, parse_sections, validate_selection

SETS = {
    "Stable Netplay": ["COOP-P6", "EXP-16"],
    "DRAFT-01 with debug": ["COOP-P6", "EXP-21", "EXP-22", "DBG-01"],
    "Prep production candidate": ["COOP-P6", "EXP-21", "EXP-25", "EXP-26"],
    "PREP-03 with debug": ["COOP-P6", "EXP-21", "EXP-25", "EXP-26", "DBG-01"],
    "Prep plus in-battle draft": ["COOP-P6", "EXP-21", "EXP-22", "EXP-25", "EXP-26"],
    "DRAFT-02 with debug": ["COOP-P6", "EXP-21", "EXP-23", "DBG-01"],
}


def report(dolphin: Path = ROOT / "Dolphin-x64") -> str:
    source = parse_sections((ROOT / "codes/GFEE01.ini").read_text())
    ids = [l[1:].split()[0] for l in source["Gecko"] if l.startswith("$")]
    handler = dolphin / "Sys/codehandler.bin"
    size = handler.stat().st_size if handler.exists() else 2880
    budget = gecko_budget(dolphin)
    out = ["# Gecko capacity audit", "", "Baseline: 10d2496; measured code definitions in this branch.", "",
           f"Handler: {size} bytes. Installer region: 6144 bytes. Project's conservative enabled-list budget: {budget} bytes.", "",
           "Dolphin tag 2609a GeckoCode.cpp places the GCT header in the final 8 bytes of the handler image. "
           "Its source-derived payload capacity is region − handler − 8 = 3256 bytes for this handler. "
           "The existing project subtracts 16, reserving an additional 8 bytes. This audit retains that conservative limit; "
           "the difference is not a meaningful expansion strategy.", "",
           "Source: https://github.com/dolphin-emu/dolphin/blob/2609a/Source/Core/Core/GeckoCode.cpp#L144-L184", "",
           "Each code line occupies 8 bytes. C2 headers, replayed instructions, padding and branch-back words "
           "are included in the measured sizes. The global header/terminator are reserved once. "
           "AR code storage is separate and is not included in these Gecko totals.", "",
           "| Patch | Bytes | Classification |", "|---|---|---|"]
    for name, count in gecko_sizes(ids):
        category = "debug only" if name.startswith("DBG-") else "aggregate package (contains other listed patches)" if name.startswith("COOP-") else "individual experiment"
        out.append(f"| {name.split()[0]} | {count} | {category} |")
    out += ["", "Do not sum all rows: COOP packages intentionally duplicate their component definitions.", "",
            "| Configuration | Enabled bytes | Remaining conservative bytes | Validation |", "|---|---|---|---|"]
    for label, ids in SETS.items():
        used = sum(n for _, n in gecko_sizes(ids))
        try:
            validate_selection(ids, dolphin)
            status = "fits"
        except ValueError as e:
            status = str(e)
        out.append(f"| {label} | {used} | {budget-used} | {status} |")
    out += ["", "## Enforcement and shared hooks", "",
            "build_ini now rejects over-budget selections, unknown code IDs and duplicate C2 hook writers. "
            "This covers the installer, package contents generation and setup library callers. Setup validates "
            "before --force can remove a profile. The existing installer override remains explicit and unsafe; never distribute its output.", "",
            "Mutually exclusive: EXP-15/16/21; EXP-22/23; aggregate packages with their components or other aggregate versions. "
            "EXP-23 and parked branch EXP-24 also share post-action/phase-advance hooks. "
            "Validation detects C2 writer collisions, not all possible AR/direct-write/adjacent-hook control-flow conflicts. "
            "Manual changes in Dolphin can bypass Python validation. A missing handler uses the documented fallback; "
            "distribution acceptance must measure the actual installed handler.", "",
            "Dolphin skips an oversized code and continues trying later codes. It does not merely truncate the list. "
            "Therefore patch ordering is never a safe workaround.", "",
            "## Optimization recommendation", "",
            "1. Keep production combinations explicit and omit obsolete draft/debug codes where appropriate. "
            "This does not solve chapters without preparations; removing their fallback changes behavior.", "",
            "2. First investigate EXP-21's repeated transfer caves and COOP EXP/result gates. A shared helper "
            "needs position-independent calls, preserved LR/register/CR state, and stable helper lifetime after "
            "Gecko rewrites hooks. Do not infer a usable shared-code address from generated list ordering.", "",
            "3. No assembly shrinking is accepted here without semantic tests plus production Dolphin regression. "
            "The verified work in this milestone improves validation, not gameplay assembly.", "",
            "## Long-term architecture", "",
            "Recommend a reproducible, relocatable payload linked into a deliberately reserved DOL section, "
            "with a small version-checked bootstrap and Gecko retained for experiments. This requires proof "
            "that the section's memory is excluded from arena/heap allocations, survives map/overlay loading, "
            "and is included identically on both Netplay peers. No safe executable payload region has been established.", "",
            "A RAM bootstrap must allocate/reserve memory deterministically before competing allocators, "
            "relocate branch/data references, flush data cache and invalidate instruction cache, and survive "
            "savestate restoration. A patched user-owned main.dol gives more reproducible loading but changes "
            "disc checksums; both peers need the same transformed build. Build only original patch instructions "
            "and hashes, never distribute game assets. Hash the source DOL, toolchain and payload and reject "
            "unexpected hooks. Keep an explicit hook manifest and inverse/rebuild procedure. "
            "A custom Dolphin build is unnecessary unless a measured limitation defeats these options. "
            "No payload proof of concept is attempted without a proven reservation/lifetime model.", ""]
    return "\n".join(out)


if __name__ == "__main__":
    destination = ROOT / "docs/GECKO_AUDIT.md"
    destination.write_text(report(), encoding="utf-8")
    print(f"wrote {destination}")
