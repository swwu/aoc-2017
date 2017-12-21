import collections
import json

instr = open('d20.in').read()

points = []

for l in instr.split("\n"):
    if l == "": continue

    p,v,a = l.split(", ")

    pc = [int(x) for x in p[3:-1].split(",")]
    vc = [int(x) for x in v[3:-1].split(",")]
    ac = [int(x) for x in a[3:-1].split(",")]

    print pc,vc,ac
    points.append((pc,vc,ac))



for t in range(1000000):
    min_d = 10000000000000000000000
    min_i = 0

    positions = collections.defaultdict(list)

    for i,(p,v,a) in enumerate(points):
        for j in range(3):
            v[j] += a[j]
        for j in range(3):
            p[j] += v[j]

        key = "".join((str(x) for x in p))

        positions[key].append(i)

        d = sum((abs(x) for x in p))
        if d < min_d:
            min_d = d
            min_i = i

    deleted = set()
    for k,vs in positions.iteritems():
        if len(vs) > 1:
            deleted.update(vs)

    newpoints = []
    for i,p in enumerate(points):
        if i not in deleted:
            newpoints.append(p)

    points = newpoints


    print len(points)


