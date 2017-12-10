instr = """63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24"""

lengths = [ord(x) for x in instr] + [17, 31, 73, 47, 23]

lsize = 256

l = list(range(lsize))

cur_skip = 0
cur_pos = 0

for i in range(64):
    for length in lengths:
        cur_subl = []

        for i in range(length):
            cur_subl.append(l[(i+cur_pos) % len(l)])

        for i in range(length):
            l[(i+cur_pos)%len(l)] = cur_subl[len(cur_subl) - i -1]

        cur_pos = (cur_pos + cur_skip + length) % len(l)
        cur_skip += 1

final = ""

for i in range(16):
    sub = l[i*16:(i+1)*16]

    h = sub[0]
    for c in sub[1:]:
        h = h ^ c
    final += "{:02x}".format(h)

print final





