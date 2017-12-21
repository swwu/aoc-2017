import collections
import json

af = 16807
bf = 48271

div = 2147483647

astart = 783
bstart = 325


right16 = 65536

av = astart
bv = bstart

score = 0

for i in xrange(5000000):

    if i % 10000 == 0:
        print(i)


    av = (av * af) % div
    bv = (bv * bf) % div
    while av % 4 != 0:
        av = (av * af) % div
    while bv % 8 != 0:
        bv = (bv * bf) % div


    if av % right16 == bv % right16:
        score += 1

print(score)
