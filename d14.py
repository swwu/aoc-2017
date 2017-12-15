import collections
import json

def knot_hash(instr):

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

    final = []

    for i in range(16):
        sub = l[i*16:(i+1)*16]

        h = sub[0]
        for c in sub[1:]:
            h = h ^ c
        final.append(h)

    return final



def count_bits(n):
    counter = 0
    for v in n:
        for i in range(9):
            if (1 << i) & v > 0:
                counter += 1
    return counter

max_range = 0
def regions_for_line(line):
    global max_range

    l = []
    cur_idx = 0
    for v in line:
        for i in range(7,-1,-1):
            if (1 << i) & v > 0:
                max_range += 1
                l.append(max_range)
            else:
                l.append(0)
            cur_idx += 1

    return l

instr = "xlqgujun"

grid = []
for n in range(128):
    hsh = knot_hash(instr + "-" + str(n))
    cur = regions_for_line(hsh)
    grid.append(cur)

last_uniq_len = 0
while True:
    for i,row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 0: continue
            dj = 0
            for di in [-1,1]:
                if i+di < 0 or i+di >= len(grid) or j+dj < 0 or j+dj >= len(grid):
                    continue
                if cell < grid[i+di][j+dj]:
                    grid[i][j] = grid[i+di][j+dj]
            di = 0
            for dj in [-1,1]:
                if i+di < 0 or i+di >= len(grid) or j+dj < 0 or j+dj >= len(grid):
                    continue
                if cell < grid[i+di][j+dj]:
                    grid[i][j] = grid[i+di][j+dj]
    uniqs = set(it for row in grid for it in row)
    uniq_len = len(uniqs) - 1
    if uniq_len == last_uniq_len:
        # return uniq_len
        break
    last_uniq_len = uniq_len
print uniq_len


