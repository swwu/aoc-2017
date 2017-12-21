import collections
import json


instr = open('d19.in').read()

#0 = nothing, 1 = straight only, 2 = can turn

grid = []

startx = 0
starty = 0

lines = instr.split("\n")
startx = list(lines[0]).index("|")

for line in lines:
    newrow = []
    for c in line:
        if c == "|" or c == "-":
            newrow.append(1)
        elif c=="+":
            newrow.append(2)
        elif c == " ":
            newrow.append(0)
        else:
            newrow.append(c)

    grid.append(newrow)

x,y = (startx,starty)
lx,ly = (startx,starty-1)



path = ""
steps = 0
while True:
    nx, ny = None, None

    steps += 1
    v = grid[y][x]

    if v == 1:
        nx = x + (x - lx)
        ny = y + (y - ly)
    if v == 2 or isinstance(v, basestring):
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            if y+dy == ly and x+dx == lx: continue
            if y+dy >= len(grid) or y+dy < 0 or x+dx >= len(grid[y]) or x+dx < 0: continue
            if grid[y+dy][x+dx] != 0:
                nx = x+dx
                ny = y+dy
                break
    if isinstance(v, basestring):
        path += v
        print path
        print steps
    print steps

    lx,ly = x,y
    x,y = nx, ny




    #if isinstance(s, basestring)

