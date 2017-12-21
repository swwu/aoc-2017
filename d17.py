#pt1

import collections


inv = 354

buf = [0]

curpos = 0

for i in range(1,2018):
    curpos = (curpos + inv) % len(buf)
    buf.insert(curpos+1, i)
    curpos = (curpos + 1) % len(buf)



print buf
print buf[(buf.index(2017)+1) % len(buf)]




#pt2


import collections


from linkedlist import LL,Node

inv = 354

curpos = 0
total = 1

for i in xrange(1,50000000):
    curpos = (curpos + inv) % total
    if curpos == 0:
        print i
        print curpos
    curpos += 1
    total += 1
