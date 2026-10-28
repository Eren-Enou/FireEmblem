# Staged executable migration research

Research only; stable Gecko gameplay and user images remain unchanged.

## Tools evaluated from their primary documentation

- [GeckoLoader](https://github.com/JoshuaMKW/GeckoLoader) injects a loader/handler
  and larger code storage into DOL builds, with allocation and hook options. It
  can ease transition from existing codes, but still requires FE9-specific hook,
  allocation and lifetime verification. No binaries were installed or executed.
- [DOL C-Kit](https://github.com/Minty-Meeo/dol_c_kit) builds C/C++/assembly via
  devkitPPC, supports DOL injection and an OSArena patcher interface. It requires
  toolchain/dependency setup and game-specific symbols/reservation logic. It is
  a candidate for a maintained compiled payload, not evidence FE9 is supported.
- Direct Python construction is sufficient for a narrow C2 transplant proof.
  Existing owner/draft/prep generators emit PPC words and internal branches;
  those can become payload objects. External relative branches, LR-derived data
  and absolute pointers must be classified before relocation.

## FE9 measurements

GFEE01 rev 0 DOL has 2/7 text slots and 8/11 data slots populated. BSS begins
at 0x802A51C0 with size 0xC7374. Initialized data can lie inside its aggregate
range, so do not treat BSS holes as free executable space. No heap/arena-excluded
payload region has been established. Address ranges and DOL layout are generated
from the hash-anchored header, not a promise that runtime allocations avoid them.

## Small proof completed

`tools/fe9/dol_patch.py` and `tests/test_dol_patch.py` implement a pure offline
transform on a SYNTHETIC DOL. They validate hook bytes, section/BSS overlap,
text-slot availability, alignment, branch range and unsupported external relative
branches; add a text section; and generate a hook and return branch. Source bytes
remain unchanged. No FE9 DOL or disc has been patched or booted by this proof.

This proves format/branch construction only. It deliberately does not claim safe
FE9 allocation, C2 behavioral equivalence or a usable release build.

## Migration gates

1. Export a hook manifest from the existing generators: original instruction,
   injected words, replay position, return target, scratch registers, CR/LR and
   stack behavior, internal data, dependencies and conflicts. Preserve current
   generated INI tests as the reference behavior.
2. Trace FE9's arena/heap initialization and module/map loading. Reserve payload
   memory BEFORE allocator creation; pin the reservation instructions and test
   that later maps, menus, saves and overlays cannot reclaim it. An unused DOL
   slot alone does not reserve RAM.
3. Choose one small independent patch. Build a copied DOL, check source hash and
   original hook, compare its instructions to Gecko and test codes-off/Gecko/
   executable variants on identical disposable fixtures. Do not duplicate hooks
   by leaving the equivalent Gecko enabled.
4. Expand with a pinned compiler/linker and relocation manifest. Check PPC branch
   reach and all embedded data references. Runtime loading needs data-cache
   flush and instruction-cache invalidation; boot-loaded code still needs its
   loader behavior verified rather than assumed from Gecko's cache flushing.
5. Test natural chapter transitions, suspend/fresh reload and fixtures created
   before/after migration. Old savestates restore old RAM/patches and are not
   automatically compatible. Native unit ownership storage must keep its schema.
6. Build identical transformed images on both peers and compare logical game
   digests in Netplay. No host-only allocation or external per-client state may
   affect simulation. Run local-pair and actual two-PC acceptance separately.
7. Distribute original code/patch instructions or a delta with source/result
   hashes, never extracted game files. Rebuild from a verified user-owned image;
   reject unexpected input. Keep reproducible transforms and rollback by rebuild.

Recommendation: retain Gecko during research; migrate proven core behavior to a
reserved compiled payload incrementally. GeckoLoader is a possible bridge, DOL
C-Kit a longer-term build framework. Avoid a custom Dolphin fork. Do not perform
a wholesale migration before campaign/event regression fixtures exist.
