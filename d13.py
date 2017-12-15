instr = """0: 3
1: 2
2: 4
4: 4
6: 5
8: 6
10: 6
12: 8
14: 6
16: 6
18: 9
20: 8
22: 8
24: 8
26: 12
28: 8
30: 12
32: 12
34: 12
36: 10
38: 14
40: 12
42: 10
44: 8
46: 12
48: 14
50: 12
52: 14
54: 14
56: 14
58: 12
62: 14
64: 12
66: 12
68: 14
70: 14
72: 14
74: 17
76: 14
78: 18
84: 14
90: 20
92: 14"""

t = 0

#instr = """0: 3
#1: 2
#4: 4
#6: 4"""


layers = {}

for l in instr.split("\n"):
    layer, rng = [int(x) for x in l.split(": ")]

    layers[layer] = rng

delay = 1000000
while True:
    sev = 0
    for t in range(delay,delay+94):
        pos = t - delay
        if pos not in layers: continue
        vt = t % (2 * layers[pos] - 2)
        if vt >= layers[pos]:
            vt -= layers[pos]
            vt = layers[pos] - vt - 2
        if vt == 0:
            sev += pos * layers[pos] + 1
    if delay % 10000 == 0:
        print delay
    if sev == 0:
        print delay, sev
        break
    delay += 1




