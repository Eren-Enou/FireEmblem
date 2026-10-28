"""Bounded symbolic local paths through FE9 event code.

Native functions are opaque expressions. This traces VM branch predicates, not
native side effects, world-state feasibility, event registration or real gameplay.
Unsupported instructions and loop/state bounds are explicit incomplete outcomes.
Opaque query results are distinct per call occurrence; intervening native effects
must not make a later query reuse an earlier symbolic value.
"""
import ast
from tools.fe9.events import functions, instructions
from tools.chapter_audit import script_strings

BIN = {0x22: "+", 0x23: "-", 0x24: "*", 0x25: "/", 0x26: "%", 0x2A: "|", 0x2B: "&",
       0x2C: "^", 0x2D: "<<", 0x2E: ">>", 0x2F: "==", 0x30: "!=", 0x31: "<", 0x32: "<=",
       0x33: ">", 0x34: ">=", 0x35: "string==", 0x36: "string!="}


def integer(value):
    try:
        return int(value, 10)
    except ValueError:
        return None


def binary(left, right, op):
    """Fold only known equality operands; arithmetic/shift edge cases stay opaque."""
    a, b = integer(left), integer(right)
    if op in (0x2F, 0x30) and a is not None and b is not None:
        return str(int((a == b) if op == 0x2F else (a != b)))
    if op in (0x35, 0x36) and left[:1] in ("'", '"') and right[:1] in ("'", '"'):
        try:
            a, b = ast.literal_eval(left), ast.literal_eval(right)
            if isinstance(a, str) and isinstance(b, str):
                return str(int((a == b) if op == 0x35 else (a != b)))
        except (ValueError, SyntaxError):
            pass
    return f"({left} {BIN[op]} {right})"


def trace(raw: bytes, index: int, max_states: int = 128, max_steps: int = 4000) -> dict:
    fs = functions(raw)
    f = fs[index]
    code = {i["offset"]: i for i in instructions(raw, f)}
    strings = script_strings(raw)
    pending = [(f.code, [], {}, [], {})]
    events, outcomes, states, steps = [], [], 0, 0
    while pending and states < max_states and steps < max_steps:
        pc, stack, variables, conditions, visited = pending.pop()
        states += 1
        while pc in code and steps < max_steps:
            steps += 1
            visited[pc] = visited.get(pc, 0) + 1
            if visited[pc] > 2:
                outcomes.append({"status": "INCONCLUSIVE", "reason": "loop bound", "offset": pc})
                break
            i = code[pc]
            op, value, nxt = i["opcode"], i["operand"], i["next"]
            try:
                if op in (0, 0x3F, 0x40):
                    pass
                elif op in (1, 2):
                    stack.append(variables.get(value, f"v{value}"))
                elif op in (7, 8):
                    stack.append(f"&v{value}")
                elif op in (0x19, 0x1A, 0x1B):
                    stack.append(str(value))
                elif op in (0x1C, 0x1D, 0x1E):
                    stack.append(repr(strings.get(value, f"<string@{value}>")))
                elif op == 0x1F:
                    ref = stack[-1]
                    stack.append(variables.get(int(ref[2:]), ref[1:]) if ref.startswith("&v") else f"*({ref})")
                elif op == 0x20:
                    stack.pop()
                elif op == 0x21:
                    val, ref = stack.pop(), stack.pop()
                    if not ref.startswith("&v"):
                        raise ValueError("nonlocal store")
                    variables[int(ref[2:])] = val
                    stack.append(val)
                elif op in BIN:
                    right, left = stack.pop(), stack.pop()
                    stack.append(binary(left, right, op))
                elif op in (0x27, 0x28, 0x29):
                    value = stack.pop()
                    number = integer(value)
                    stack.append(str(int(number == 0)) if op == 0x29 and number is not None else
                                 f"{ {0x27:'-', 0x28:'~', 0x29:'!'}[op]}({value})")
                elif op in (0x37, 0x38):
                    if op == 0x38:
                        name = strings[int.from_bytes(raw[pc + 1:pc + 3], "big")]
                        argc = raw[pc + 3]
                    else:
                        name, argc = f"local_{value}", raw[fs[value].record + 13]
                    args = [stack.pop() for _ in range(argc)][::-1]
                    result = name + "(" + ", ".join(args) + f")@0x{pc:X}#{visited[pc]}"
                    events.append({"offset": pc, "function": index, "command": name, "args": args,
                                   "result": result, "conditions": conditions.copy(), "scope": "local symbolic path only"})
                    # A native may write a passed VM local reference. Preserve
                    # previous samples in predicates but invalidate the local.
                    for arg in args:
                        if arg.startswith("&v") and arg[2:].isdigit():
                            variables[int(arg[2:])] = f"v{arg[2:]}@0x{pc:X}#{visited[pc]}"
                    stack.append(result)
                elif op == 0x39:
                    outcomes.append({"status": "RETURN", "conditions": conditions.copy()})
                    break
                elif op == 0x3A:
                    nxt = i["target"]
                elif 0x3B <= op <= 0x3E:
                    predicate = stack.pop()
                    on_true = op in (0x3B, 0x3C)
                    number = integer(predicate)
                    if number is not None:
                        if (number != 0) == on_true:
                            nxt = i["target"]
                            if op in (0x3C, 0x3E):
                                stack.append("1" if on_true else "0")
                        pc = nxt
                        continue
                    taken_stack = stack.copy()
                    if op in (0x3C, 0x3E):
                        taken_stack.append("1" if on_true else "0")
                    taken_condition = f"{predicate} {'!=' if on_true else '=='} 0"
                    other_condition = f"{predicate} {'==' if on_true else '!='} 0"
                    if other_condition not in conditions and predicate not in ("0" if on_true else "1",):
                        pending.append((i["target"], taken_stack, variables.copy(), conditions + [taken_condition], visited.copy()))
                    if taken_condition in conditions or predicate in ("1" if on_true else "0",):
                        break
                    conditions = conditions + [other_condition]
                elif op == 0x41:
                    for _ in range(value):
                        stack.pop()
                else:
                    raise ValueError(f"unsupported opcode {op:02X}")
            except (IndexError, KeyError, ValueError) as exc:
                outcomes.append({"status": "INCONCLUSIVE", "reason": str(exc), "offset": pc})
                break
            pc = nxt
    if pending or steps >= max_steps:
        outcomes.append({"status": "INCONCLUSIVE", "reason": "state/step bound"})
    unique = {(e["offset"], e["result"], tuple(e["conditions"]), tuple(e["args"])): e for e in events}
    return {"function": index, "events": list(unique.values()), "outcomes": outcomes,
            "states": states, "steps": steps, "complete_local_trace": not any(o["status"] == "INCONCLUSIVE" for o in outcomes)}
