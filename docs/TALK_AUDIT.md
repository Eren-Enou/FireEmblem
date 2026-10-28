# Original Talk eligibility audit

Generated with `python -m tools.talk_audit` from the read-only GFEE01 rev0 image. Evidence: RESEARCH.md CAMP-007; signatures pin this chain. STATIC ONLY; Yellow recruitment, event completion, roster retention and Netplay remain NOT TESTED.

| Step | Original behavior | Co-op implication / limit |
|---|---|---|
| Menu callback | Reject context+0x16 bit0 or nonzero context+0x12; collect targets; reject empty list; return 2 if actor+0x1A5 bits4..6 nonzero, otherwise 0 | No force-list or force-ID read in this callback. Context and action-state semantics remain partly unresolved. |
| Target enumeration | Read actor coordinates, four direction bits from a precomputed map halfword, and adjacent occupancy IDs; skip empty slots; dispatch non-null units to callback | No force-list traversal or actor/target force read here. Precomputed mask production is outside this analysis. |
| Target callback | Set context target, query original kind8 matcher, append matching target's x/y/ID to result list | No extra force filter in this callback. |
| Event matcher | Character identity, optional reversal and consumed-key check (CAMP-004) | A static absence of a force restriction is not proof of Yellow menu access or real recruitment. |

The chapter10 Oscar/Kieran conversation is a useful runtime target: Oscar is P2-owned in EXP-16 and the original scene allows reversed participants. A synthetic fixture must retain a living prisoner, an unconsumed key, valid map adjacency and original Talk execution. The scene's force3 transfer alone does not prove permanent recruitment.

## Pinned table links

- Talk availability: `0x80078A24`.
- Adjacent target callback: `0x8002CD70`.

## Direct aligned calls to the kind8 matcher

`0x8002CD90`, `0x800F88B4`, `0x800F8EE4`, `0x801032BC`. Indirect calls and other candidate-generation paths are not excluded.

## Talk availability

Direct calls: `0x80078A64 -> 0x8002B0A4`.

```text
80078A24  9421FFF0  stwu r1, -0x10(r1)
80078A28  7C0802A6  mflr r0
80078A2C  3C60802F  lis r3, -0x7fd1
80078A30  90010014  stw r0, 0x14(r1)
80078A34  3863F4C8  addi r3, r3, -0xb38
80078A38  88030016  lbz r0, 0x16(r3)
80078A3C  540007FF  clrlwi. r0, r0, 0x1f
80078A40  4182000C  beq 0x80078a4c
80078A44  38600003  li r3, 3
80078A48  48000060  b 0x80078aa8
80078A4C  88030012  lbz r0, 0x12(r3)
80078A50  7C000775  extsb. r0, r0
80078A54  4182000C  beq 0x80078a60
80078A58  38600003  li r3, 3
80078A5C  4800004C  b 0x80078aa8
80078A60  80630000  lwz r3, 0(r3)
80078A64  4BFB2641  bl 0x8002b0a4
80078A68  3C60802F  lis r3, -0x7fd1
80078A6C  8003F4E0  lwz r0, -0xb20(r3)
80078A70  2C000000  cmpwi r0, 0
80078A74  4082000C  bne 0x80078a80
80078A78  38600003  li r3, 3
80078A7C  4800002C  b 0x80078aa8
80078A80  3C60802F  lis r3, -0x7fd1
80078A84  38000002  li r0, 2
80078A88  3863F4C8  addi r3, r3, -0xb38
80078A8C  80630000  lwz r3, 0(r3)
80078A90  886301A5  lbz r3, 0x1a5(r3)
80078A94  5464E77E  rlwinm r4, r3, 0x1c, 0x1d, 0x1f
80078A98  7C6400D0  neg r3, r4
80078A9C  7C632378  or r3, r3, r4
80078AA0  7C63FE70  srawi r3, r3, 0x1f
80078AA4  7C031838  and r3, r0, r3
80078AA8  80010014  lwz r0, 0x14(r1)
80078AAC  7C0803A6  mtlr r0
80078AB0  38210010  addi r1, r1, 0x10
80078AB4  4E800020  blr 
```

## Adjacent conversation targets

Direct calls: `0x8002B0E8 -> 0x8002F728`.

```text
8002B0A4  9421FFE0  stwu r1, -0x20(r1)
8002B0A8  7C0802A6  mflr r0
8002B0AC  3CA08028  lis r5, -0x7fd8
8002B0B0  3C808028  lis r4, -0x7fd8
8002B0B4  90010024  stw r0, 0x24(r1)
8002B0B8  38044E20  addi r0, r4, 0x4e20
8002B0BC  3C80802F  lis r4, -0x7fd1
8002B0C0  38A54D40  addi r5, r5, 0x4d40
8002B0C4  93E1001C  stw r31, 0x1c(r1)
8002B0C8  93C10018  stw r30, 0x18(r1)
8002B0CC  93A10014  stw r29, 0x14(r1)
8002B0D0  93810010  stw r28, 0x10(r1)
8002B0D4  7C7C1B78  mr r28, r3
8002B0D8  90010008  stw r0, 8(r1)
8002B0DC  3804F4E0  addi r0, r4, -0xb20
8002B0E0  7C030378  mr r3, r0
8002B0E4  90A10008  stw r5, 8(r1)
8002B0E8  48004641  bl 0x8002f728
8002B0EC  8BFC019F  lbz r31, 0x19f(r28)
8002B0F0  3C60802D  lis r3, -0x7fd3
8002B0F4  8BDC019E  lbz r30, 0x19e(r28)
8002B0F8  3863A518  addi r3, r3, -0x5ae8
8002B0FC  7FFF0774  extsb r31, r31
8002B100  7FDE0774  extsb r30, r30
8002B104  57FC3032  slwi r28, r31, 6
8002B108  7C1EE214  add r0, r30, r28
8002B10C  5400083C  slwi r0, r0, 1
8002B110  7FA30214  add r29, r3, r0
8002B114  A01D408E  lhz r0, 0x408e(r29)
8002B118  3BBD408E  addi r29, r29, 0x408e
8002B11C  54000739  rlwinm. r0, r0, 0, 0x1c, 0x1c
8002B120  4182005C  beq 0x8002b17c
8002B124  381FFFFF  addi r0, r31, -1
8002B128  7C63F214  add r3, r3, r30
8002B12C  7C000774  extsb r0, r0
8002B130  54003032  slwi r0, r0, 6
8002B134  7C630214  add r3, r3, r0
8002B138  8863000D  lbz r3, 0xd(r3)
8002B13C  28030000  cmplwi r3, 0
8002B140  4182001C  beq 0x8002b15c
8002B144  3803FFFF  addi r0, r3, -1
8002B148  3C60802B  lis r3, -0x7fd5
8002B14C  1C800280  mulli r4, r0, 0x280
8002B150  380314E4  addi r0, r3, 0x14e4
8002B154  7C802214  add r4, r0, r4
8002B158  48000008  b 0x8002b160
8002B15C  38800000  li r4, 0
8002B160  28040000  cmplwi r4, 0
8002B164  41820018  beq 0x8002b17c
8002B168  81810008  lwz r12, 8(r1)
8002B16C  38610008  addi r3, r1, 8
8002B170  818C0008  lwz r12, 8(r12)
8002B174  7D8903A6  mtctr r12
8002B178  4E800421  bctrl 
8002B17C  A01D0000  lhz r0, 0(r29)
8002B180  540007BD  rlwinm. r0, r0, 0, 0x1e, 0x1e
8002B184  41820060  beq 0x8002b1e4
8002B188  381E0001  addi r0, r30, 1
8002B18C  3C60802D  lis r3, -0x7fd3
8002B190  3863A518  addi r3, r3, -0x5ae8
8002B194  7C000774  extsb r0, r0
8002B198  7C030214  add r0, r3, r0
8002B19C  7C60E214  add r3, r0, r28
8002B1A0  8863000D  lbz r3, 0xd(r3)
8002B1A4  28030000  cmplwi r3, 0
8002B1A8  4182001C  beq 0x8002b1c4
8002B1AC  3803FFFF  addi r0, r3, -1
8002B1B0  3C60802B  lis r3, -0x7fd5
8002B1B4  1C800280  mulli r4, r0, 0x280
8002B1B8  380314E4  addi r0, r3, 0x14e4
8002B1BC  7C802214  add r4, r0, r4
8002B1C0  48000008  b 0x8002b1c8
8002B1C4  38800000  li r4, 0
8002B1C8  28040000  cmplwi r4, 0
8002B1CC  41820018  beq 0x8002b1e4
8002B1D0  81810008  lwz r12, 8(r1)
8002B1D4  38610008  addi r3, r1, 8
8002B1D8  818C0008  lwz r12, 8(r12)
8002B1DC  7D8903A6  mtctr r12
8002B1E0  4E800421  bctrl 
8002B1E4  A01D0000  lhz r0, 0(r29)
8002B1E8  5400077B  rlwinm. r0, r0, 0, 0x1d, 0x1d
8002B1EC  41820064  beq 0x8002b250
8002B1F0  381F0001  addi r0, r31, 1
8002B1F4  3C60802D  lis r3, -0x7fd3
8002B1F8  3863A518  addi r3, r3, -0x5ae8
8002B1FC  7C000774  extsb r0, r0
8002B200  7C63F214  add r3, r3, r30
8002B204  54003032  slwi r0, r0, 6
8002B208  7C630214  add r3, r3, r0
8002B20C  8863000D  lbz r3, 0xd(r3)
8002B210  28030000  cmplwi r3, 0
8002B214  4182001C  beq 0x8002b230
8002B218  3803FFFF  addi r0, r3, -1
8002B21C  3C60802B  lis r3, -0x7fd5
8002B220  1C800280  mulli r4, r0, 0x280
8002B224  380314E4  addi r0, r3, 0x14e4
8002B228  7C802214  add r4, r0, r4
8002B22C  48000008  b 0x8002b234
8002B230  38800000  li r4, 0
8002B234  28040000  cmplwi r4, 0
8002B238  41820018  beq 0x8002b250
8002B23C  81810008  lwz r12, 8(r1)
8002B240  38610008  addi r3, r1, 8
8002B244  818C0008  lwz r12, 8(r12)
8002B248  7D8903A6  mtctr r12
8002B24C  4E800421  bctrl 
8002B250  A01D0000  lhz r0, 0(r29)
8002B254  540007FF  clrlwi. r0, r0, 0x1f
8002B258  41820060  beq 0x8002b2b8
8002B25C  381EFFFF  addi r0, r30, -1
8002B260  3C60802D  lis r3, -0x7fd3
8002B264  3863A518  addi r3, r3, -0x5ae8
8002B268  7C000774  extsb r0, r0
8002B26C  7C030214  add r0, r3, r0
8002B270  7C60E214  add r3, r0, r28
8002B274  8863000D  lbz r3, 0xd(r3)
8002B278  28030000  cmplwi r3, 0
8002B27C  4182001C  beq 0x8002b298
8002B280  3803FFFF  addi r0, r3, -1
8002B284  3C60802B  lis r3, -0x7fd5
8002B288  1C800280  mulli r4, r0, 0x280
8002B28C  380314E4  addi r0, r3, 0x14e4
8002B290  7C802214  add r4, r0, r4
8002B294  48000008  b 0x8002b29c
8002B298  38800000  li r4, 0
8002B29C  28040000  cmplwi r4, 0
8002B2A0  41820018  beq 0x8002b2b8
8002B2A4  81810008  lwz r12, 8(r1)
8002B2A8  38610008  addi r3, r1, 8
8002B2AC  818C0008  lwz r12, 8(r12)
8002B2B0  7D8903A6  mtctr r12
8002B2B4  4E800421  bctrl 
8002B2B8  3C60802F  lis r3, -0x7fd1
8002B2BC  38000000  li r0, 0
8002B2C0  3863F4C8  addi r3, r3, -0xb38
8002B2C4  90030004  stw r0, 4(r3)
8002B2C8  83E1001C  lwz r31, 0x1c(r1)
8002B2CC  83C10018  lwz r30, 0x18(r1)
8002B2D0  83A10014  lwz r29, 0x14(r1)
8002B2D4  83810010  lwz r28, 0x10(r1)
8002B2D8  80010024  lwz r0, 0x24(r1)
8002B2DC  7C0803A6  mtlr r0
8002B2E0  38210020  addi r1, r1, 0x20
8002B2E4  4E800020  blr 
```

## Conversation target callback

Direct calls: `0x8002CD90 -> 0x800BF1E8`, `0x8002CDB4 -> 0x8002F6E8`.

```text
8002CD70  9421FFF0  stwu r1, -0x10(r1)
8002CD74  7C0802A6  mflr r0
8002CD78  3C60802F  lis r3, -0x7fd1
8002CD7C  90010014  stw r0, 0x14(r1)
8002CD80  3863F4C8  addi r3, r3, -0xb38
8002CD84  93E1000C  stw r31, 0xc(r1)
8002CD88  7C9F2378  mr r31, r4
8002CD8C  93E30004  stw r31, 4(r3)
8002CD90  48092459  bl 0x800bf1e8
8002CD94  5460063F  clrlwi. r0, r3, 0x18
8002CD98  41820020  beq 0x8002cdb8
8002CD9C  3C60802F  lis r3, -0x7fd1
8002CDA0  889F019E  lbz r4, 0x19e(r31)
8002CDA4  88BF019F  lbz r5, 0x19f(r31)
8002CDA8  3863F4E0  addi r3, r3, -0xb20
8002CDAC  88DF0198  lbz r6, 0x198(r31)
8002CDB0  38E00000  li r7, 0
8002CDB4  48002935  bl 0x8002f6e8
8002CDB8  80010014  lwz r0, 0x14(r1)
8002CDBC  83E1000C  lwz r31, 0xc(r1)
8002CDC0  7C0803A6  mtlr r0
8002CDC4  38210010  addi r1, r1, 0x10
8002CDC8  4E800020  blr 
```
