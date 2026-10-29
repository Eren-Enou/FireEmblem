"""Small FE9 script-only regression VM; never substitutes for Dolphin.

Native calls, timing, scene activation and game memory are supplied by the test.
Unsupported instructions fail closed. Intended for focused original-event tests.
"""
from tools.fe9.events import functions, instructions
from tools.chapter_audit import script_strings


def execute(raw: bytes, index: int, native, max_steps=2000, *, stop_before=(),
            arguments=(), _budget=None, _depth=0):
    """Run a local scene; an explicit native boundary may stop a prefix model.

    A boundary is recorded but never called. Callers must check ``halted_before``
    rather than assuming a returned scene reached the requested boundary.
    """
    fs = functions(raw)
    if _depth >= 32:
        raise ValueError('local call depth exceeded')
    f = fs[index]
    if len(arguments) != raw[f.record+13]:
        raise ValueError('scene argument count differs')
    budget = [max_steps] if _budget is None else _budget
    code = {i["offset"]: i for i in instructions(raw, f)}
    strings, stack, variables, events = script_strings(raw), [], dict(enumerate(arguments)), []
    pc = f.code
    binary = {0x22: lambda a,b:a+b, 0x23:lambda a,b:a-b, 0x24:lambda a,b:a*b,
              0x2F:lambda a,b:int(a==b), 0x30:lambda a,b:int(a!=b),
              0x31:lambda a,b:int(a<b), 0x32:lambda a,b:int(a<=b),
              0x33:lambda a,b:int(a>b), 0x34:lambda a,b:int(a>=b),
              0x2B:lambda a,b:a&b}
    for _ in range(max_steps):
        if budget[0] <= 0:
            raise ValueError('step bound exceeded')
        budget[0] -= 1
        i = code[pc]
        op, val, nxt = i["opcode"], i["operand"], i["next"]
        if op in (0, 0x3F):
            pass
        elif op in (1,2):
            stack.append(variables.get(val,0))
        elif op in (7,8):
            stack.append(("ref",val))
        elif 0x19<=op<=0x1B:
            stack.append(val)
        elif 0x1C<=op<=0x1E:
            stack.append(strings[val])
        elif op==0x1F:
            tag,ref=stack[-1]
            if tag!='ref': raise ValueError('nonlocal dereference')
            stack.append(variables.get(ref,0))
        elif op==0x20:
            stack.pop()
        elif op==0x21:
            value=stack.pop();tag,ref=stack.pop()
            if tag!='ref': raise ValueError('nonlocal store')
            variables[ref]=value;stack.append(value)
        elif op in binary:
            b,a=stack.pop(),stack.pop();stack.append(binary[op](a,b))
        elif op==0x29:
            stack.append(int(not stack.pop()))
        elif op==0x37:
            argc=raw[fs[val].record+13]
            args=[stack.pop() for _ in range(argc)][::-1]
            if any(isinstance(a,tuple) for a in args):
                raise ValueError('cross-frame references unsupported')
            child=execute(raw,val,native,max_steps,stop_before=stop_before,
                          arguments=args,_budget=budget,_depth=_depth+1)
            events.extend(child['events'])
            if 'halted_before' in child:
                return {'events':events,'return':None,'halted_before':child['halted_before']}
            stack.append(child['return'])
        elif op==0x38:
            name=strings[int.from_bytes(raw[pc+1:pc+3],'big')]
            args=[stack.pop() for _ in range(raw[pc+3])][::-1]
            if name in stop_before:
                return {'events':events,'return':None,
                        'halted_before':{'offset':pc,'command':name,'args':args}}
            events.append({'offset':pc,'function':index,'command':name,'args':args})
            stack.append(native(name,args))
        elif op==0x39:
            return {'events':events,'return':stack[-1] if stack else None}
        elif op==0x3A:
            nxt=i['target']
        elif 0x3B<=op<=0x3E:
            test=bool(stack.pop());taken=test if op in (0x3B,0x3C) else not test
            if taken:
                nxt=i['target']
                if op in (0x3C,0x3E):stack.append(int(test))
        elif op==0x41:
            for _ in range(val):stack.pop()
        else:
            raise ValueError(f'unsupported opcode {op:02X}')
        pc=nxt
    raise ValueError('step bound exceeded')
