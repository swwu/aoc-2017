import collections
import json

instr = """31/13
34/4
49/49
23/37
47/45
32/4
12/35
37/30
41/48
0/47
32/30
12/5
37/31
7/41
10/28
35/4
28/35
20/29
32/20
31/43
48/14
10/11
27/6
9/24
8/28
45/48
8/1
16/19
45/45
0/4
29/33
2/5
33/9
11/7
32/10
44/1
40/32
2/45
16/16
1/18
38/36
34/24
39/44
32/37
26/46
25/33
9/10
0/29
38/8
33/33
49/19
18/20
49/39
18/39
26/13
19/32"""



ports = collections.defaultdict(set)

for line in instr.split("\n"):
    k,v = (int(x) for x in line.split("/"))
    if v in ports[k] or k in ports[v]:
        print "wtf"
    ports[k].add(v)
    ports[v].add(k)

def check_ports(inp, traversed):
    outs = ports[inp].difference(traversed[inp])

    rets = []
    for out in outs:
        traversed[inp].add(out)
        traversed[out].add(inp)
        weight,length = check_ports(out, traversed)
        rets.append((weight+ inp + out , length+1))
        traversed[out].remove(inp)
        if out in traversed[inp]:
            traversed[inp].remove(out)

    if len(rets) == 0:
        return (0,0)
    else:
        return sorted(rets, key=lambda x: -x[1]*100000 - x[0])[0]

print check_ports(0, collections.defaultdict(set))





