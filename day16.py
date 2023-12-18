import sys
from functools import cache

# 👇️ 1000
print(sys.getrecursionlimit())

# 👇️ set recursion limit to 2000
sys.setrecursionlimit(10000)

# 👇️ 2000
print(sys.getrecursionlimit())


def get_puz(demo=True):
    puz = []
    if demo:
        file = open("input16_demo.txt")
    else:
        file = open("input16.txt")
    for line in file:
        puz.append(list(line.replace('\n', '')))

    return puz

puz = get_puz()
puz

position = (0,0)
direction = "r"
size=(len(puz), len(puz[0]))

def change_direction(action, direction):
    if action == "\\":
        if direction == "r":
            return "d"
        if direction == "d":
            return "r"
        if direction == "l":
            return "u"
        if direction == "u":
            return "l"

    if action == "/":
        if direction == "r":
            return "u"
        if direction == "d":
            return "l"
        if direction == "l":
            return "d"
        if direction == "u":
            return "r"

    return 0


def get_next_move(position, direction):
    i, j = position
    if direction == "r":
        j += 1
    if direction == "d":
        i += 1
    if direction == "l":
        j -= 1
    if direction == "u":
        i -= 1
    return (i, j)

# liste des points déjà visités pour éviter les boucles infinies
visited = {}

def get_next(position, direction, puz):
    # Position de départ
    i, j = position

    # Si on sort du plateau, fin
    if i < 0 or i >= len(puz) or j < 0 or j >= len(puz[0]) or (i, j, direction) in visited.keys():
        return
    else:
        action = puz[i][j]
        #print(i, j, action, direction)
        visited[(i, j, direction)] = 1
        if action == "." or (action == "-" and direction in ["l", "r"]) or (action == "|" and direction in ["u", "d"]):
            #print("continuation")
            yield position
            new_pos = get_next_move(position, direction)
            yield from get_next(new_pos, direction, puz)
        if action == "\\":
            #print("mirroring")
            direction = change_direction(action, direction)
            yield position
            new_pos = get_next_move(position, direction)
            yield from get_next(new_pos, direction, puz)
        if action == "/":
            #print("mirroring")
            direction = change_direction(action, direction)
            yield position
            new_pos = get_next_move(position, direction)
            yield from get_next(new_pos, direction, puz)
        if action == "|" and direction in ["l", "r"]:
            #print("spliting pipe")
            yield position
            for d in ["u", "d"]:
                new_pos = get_next_move(position, d)
                yield from get_next(new_pos, d, puz)
        if action == "-" and direction in ["u", "d"]:
            #print("spliting dash")
            yield position
            for d in ["l", "r"]:
                new_pos = get_next_move(position, d)
                yield from get_next(new_pos, d, puz)


puz = get_puz(demo=False)
position = (0,0)
direction = "r"
visited = {}
import datetime as dt
print(dt.datetime.now())
pos = [p for p in get_next(position, direction, puz)]
print(dt.datetime.now())

visited = {}
pos = [p for (_, p) in zip(range(1170), get_next(position, direction, puz))]


for _, pos in zip(range(40), get_next(position, direction, puz)):
    i, j = pos
    new_puz[i][j] = "#"
    display(new_puz)

for i, j in pos:
    puz[i][j] = "#"

display(puz)


score = sum([1 for line in puz for c in line if c == "#"])
print(score)

def display(puz):
    for line in puz:
        print(''.join(line))

## Part two


score = []
for d in range(len(puz)):
    puz = get_puz(demo=False)
    position = (d, 0)
    direction = "r"
    visited = {}
    best = 0
    pos = [p for p in get_next(position, direction, puz)]
    for i, j in pos:
        puz[i][j] = "#"
    score.extend([sum([1 for line in puz for c in line if c == "#"])])
    #print(position, direction)

print(max(score))
8363

score = []
for d in range(len(puz)):
    puz = get_puz(demo=False)
    position = (d, len(puz[0])-1)
    direction = "l"
    visited = {}
    best = 0
    pos = [p for p in get_next(position, direction, puz)]
    for i, j in pos:
        puz[i][j] = "#"
    score.extend([sum([1 for line in puz for c in line if c == "#"])])
    #print(position, direction)

print(max(score))
8451

score = []
for d in range(len(puz[0])):
    puz = get_puz(demo=False)
    position = (0, d)
    direction = "d"
    visited = {}
    best = 0
    pos = [p for p in get_next(position, direction, puz)]
    for i, j in pos:
        puz[i][j] = "#"
    score.extend([sum([1 for line in puz for c in line if c == "#"])])
    #print(position, direction)

print(max(score))
8484

score = []
for d in range(len(puz[0])):
    puz = get_puz(demo=False)
    position = (len(puz) - 1, d)
    direction = "u"
    visited = {}
    best = 0
    pos = [p for p in get_next(position, direction, puz)]
    for i, j in pos:
        puz[i][j] = "#"
    score.extend([sum([1 for line in puz for c in line if c == "#"])])
    #print(position, direction)

print(max(score))
8491