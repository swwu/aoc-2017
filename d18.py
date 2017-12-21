import collections
import json


instr = """set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 464
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19"""

lines = instr.split("\n")

ptr = 0

regs0 = collections.defaultdict(int)
regs0["p"] = 0
regs1 = collections.defaultdict(int)
regs1["p"] = 1

freqs = []

ltrs = set("abcdefghijklmnopqrstuvwxyz")

ptr1 = 0
ptr2 = 0

states = [(0, regs0, []), (0, regs1, [])]

send_times = 0

def run_til_recv(pid):
    global send_times

    ptr, regs, buf = states[pid]

    other_pid = 1 if (pid == 0) else 0

    while True:
        toks = lines[ptr].split(" ")

        if ptr < 0 or ptr > len(lines):
            states[pid] = (ptr, regs, buf)
            return

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
        elif cmd == "mul":
            regs[reg] *= amt
        elif cmd == "mod":
            regs[reg] = regs[reg] % amt
        elif cmd == "snd":
            if pid == 1:
                send_times += 1
            if reg in ltrs:
                states[other_pid][2].append(regs[reg])
            else:
                states[other_pid][2].append(int(reg))
        elif cmd == "rcv":
            if len(buf) > 0:
                regs[reg] = buf[0]
                buf = buf[1:]
            else:
                states[pid] = (ptr, regs, buf)
                return
        elif cmd == "jgz":
            if reg in ltrs:
                if regs[reg] > 0:
                    ptr += amt
                    continue
            else:
                if int(reg) > 0:
                    ptr += amt
                    continue
        else:
            print "wat"

        ptr += 1

run_til_recv(0)
if len(states[1][2]) == 0:
    print send_times
    exit()

run_til_recv(1)
while True:
    print send_times

    if len(states[0][2]) == 0:
        break
        print send_times
    run_til_recv(0)
    print send_times

    if len(states[1][2]) == 0:
        break
        print send_times
    run_til_recv(1)







