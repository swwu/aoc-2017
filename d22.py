import json
import collections

instr = """.##.#..#...#....###....#.
#.#######.##.##.#.##.##..
.##.#..#.###.#....###..##
......#.#..##.##...#.#.##
.#.##.##.######...##.#..#
###...#..####..######.#..
###....#....#..#####.#.##
..##..#..#.#.#.#....#####
#.#.......##.#....##..#.#
##..#.###.##.####.##...#.
#.####.##.##..##.#.##.##.
###.#..##.##.#.####...#..
######.#...#....#.#...#..
.#.#.###.##.##..#.#....##
#.###..##....###.###..#.#
.#..##.......#..#.##.##.#
..#...####...##.#.##..#.#
..#.##..#..##.###.#####.#
##..##.##....#..###.#.###
.#..######.#.####..#.###.
##...####..##.#.#.#.#.###
#.#....###...##.##..##.#.
..###.#####.####.#.#..#..
..####..#.#....#.###.....
.#......#.#..####.###...."""

infs = {}

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
cdir = UP

lines = instr.split("\n")

cpos = (int(len(lines)/2),
        int(len(lines[0])/2))

for i,line in enumerate(lines):
    for j,c in enumerate(line):
        if c == "#":
            infs[(i,j)] = "I"


infc = 0
for i in range(10000000):
    if cpos in infs:
        st = infs[cpos]
        if st == "I":
            cdir = (cdir + 1) % 4
            infs[cpos] = "F"
        elif st == "W":
            infc += 1
            infs[cpos] = "I"
        elif st == "F":
            cdir = (cdir + 2) % 4
            del infs[cpos]
    else:
        # it's always clean
        cdir = (cdir - 1) % 4
        infs[cpos] = "W"

    i,j = cpos
    if cdir == UP:
        cpos = (i-1, j)
    elif cdir == RIGHT:
        cpos = (i, j+1)
    elif cdir == DOWN:
        cpos = (i+1, j)
    elif cdir == LEFT:
        cpos = (i, j-1)

print infc
