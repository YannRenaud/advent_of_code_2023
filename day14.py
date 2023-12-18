from functools import cache
import numpy as np

file = open("input14_demo.txt")

puz = np.chararray((10, 10))

for line in file:
    print(line)
    puz.append([c for c in line.replace("\n", "")])
puz

for line in puz:
    print("".join(line))

for j in range(len(puz[0])):
    for i in range(len(puz)-1, -1, -1):
        print(puz[i][j])
    
    break
#OO..#....

[j for j in range(len(puz)-1,-1,-1)]

[puz[i][0] for i in range(10) ]

puz = ['O', 'O', '.', 'O', '.', 'O', '.', '.', '#', '#']
['O', 'O', 'O', '.', '.', 'O', '.', '.', '#', '#']
['O', 'O', 'O', '.', 'O', '.', '.', '.', '#', '#']
['O', 'O', 'O', 'O', '.', '.', '.', '.', '#', '#']

def spin(puz):
    for j in range(len(puz[0])):
        keep_going = True
        while keep_going:
            # print(puz)
            keep_going = False
            dispo = -1
            for i in range(len(puz)):
                if puz[i][j] == '.':
                    dispo = i
                if puz[i][j] == '#':
                    dispo = -1
                if puz[i][j] == 'O':
                    if dispo > -1:
                        keep_going = True
                        puz[i][j] = "."
                        puz[dispo][j] = "O"
                        break

import datetime as dt

print(dt.datetime.now())
spin(puz)
print(dt.datetime.now())

res = 0
for i, m in enumerate(range(len(puz), 0, -1)):
    res += sum([1 for c in puz[i] if c =="O"]) * m

res



### Part two

puz = np.chararray((10, 10))
file = open("input14_demo.txt")

for i, line in enumerate(file):
    puz[i] = [c for c in line.replace("\n", "")]
puz


line = puz[1]
line

@cache
def spin_north(line):
    keep_going = True
    while keep_going:
        keep_going = False
        dispo = -1
        for i in range(len(line)):
            if line[i] == b'.':
                dispo = i
            if line[i] == b'#':
                dispo = -1
            if line[i] == b'O':
                if dispo > -1:
                    keep_going = True
                    line[i] = b"."
                    line[dispo] = b"O"
                    break
    return line

spin_north(line)
@cache
def spin_south(puz):
    for j in range(len(puz[0])):
        keep_going = True
        while keep_going:
            # print(puz)
            keep_going = False
            dispo = -1
            for i in range(len(puz)):
                if puz[i][j] == '.':
                    dispo = i
                if puz[i][j] == '#':
                    dispo = -1
                if puz[i][j] == 'O':
                    if dispo > -1:
                        keep_going = True
                        puz[i][j] = "."
                        puz[dispo][j] = "O"
                        break