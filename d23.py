instr = """set b 79
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23"""

#instr = """set b 79
#set c b
#sub c -17000
#set f 1
#set d 2
#set e 2
#set e b
#set z b
#mod z d
#jnz z 2
#set f 0
#set d b
#set g d
#sub g b
#gnz g 5
#jnz f 2
#add h 1
#set g b
#sub g c
#jnz g 2
#jnz 1 3
#sub b -17
#gnz g 3"""

ltrs = set("abcdefghijklmnopqrstuvwxyz")


import json
import collections


lines = instr.split("\n")

send_times = 0

ptr = 0
regs = collections.defaultdict(int)
regs["a"] = 1
buf = []

states = set()

while True:
    if ptr < 0 or ptr >= len(lines):
        break

    print ptr+1,json.dumps(regs)

    toks = lines[ptr].split(" ")
    if ptr > 10:
        exit()

    if len(toks) > 2:
        cmd, reg, amt = toks
        if amt in ltrs:
            amt = regs[amt]
        else:
            amt = int(amt)
    else:
        cmd, reg = toks

    if cmd == "set":
        regs[reg] = amt
    elif cmd == "add":
        regs[reg] += amt
    elif cmd == "sub":
        regs[reg] -= amt
    elif cmd == "mod":
        regs[reg] = regs[reg] % amt
    elif cmd == "mul":
        regs[reg] *= amt
    elif cmd == "gnz":
        if reg in ltrs:
            if regs[reg] != 0:
                ptr = amt
                continue
        else:
            if int(reg) != 0:
                ptr = amt
                continue
    elif cmd == "jnz":
        if reg in ltrs:
            if regs[reg] != 0:
                ptr += amt
                continue
        else:
            if int(reg) != 0:
                ptr += amt
                continue
    else:
        print cmd,reg,amt
        print "wat"

    ptr += 1

print regs["h"]
