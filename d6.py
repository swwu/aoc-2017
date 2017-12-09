import json

instr = """0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11"""


v = [int(x) for x in instr.split()]


seen = {}

seen_str = None

steps = 0

while True:
    cur_str = json.dumps(v)
    if cur_str in seen:
        print(steps - seen[cur_str])
        break
    seen[cur_str] = steps

    # find first max
    maxv = max(v)

    max_idxs = [i for i,j in enumerate(v) if j==maxv]
    max_idx = max_idxs[0]

    n = v[max_idx]
    v[max_idx] = 0

    for i in range(n):
        vi = (max_idx + i+1) % len(v)
        v[vi] += 1
    steps += 1




