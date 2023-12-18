
import sys
from functools import cache


# 👇️ 1000
print(sys.getrecursionlimit())

# 👇️ set recursion limit to 2000
sys.setrecursionlimit(10000)

def get_puz(demo=True):
    puz = []
    if demo:
        file = open("input17_demo.txt")
    else:
        file = open("input17.txt")
    for line in file:
        puz.append(list(line.replace('\n', '')))

    return puz

puz = get_puz()


opposite_dir = {
    "<": ">",
    ">": "<",
    "v": "^",
    "^": "v"
}


def get_possible_move(pos, direct, st, puz):
    possible = [">", "v", "<", "^"]
    possible.remove(opposite_dir[direct])
    for d in possible:
        i, j = pos
        im, jm = len(puz)-1, len(puz[0])-1
        if d == ">":
            ni = i
            nj = j + 1
        if d == "<":
            ni = i
            nj = j - 1
        if d == "v":
            ni = i + 1
            nj = j
        if d == "^":
            ni = i - 1
            nj = j
        
        if ni < 0 or ni > im or nj < 0 or nj > jm:
            # On sort du plateau
            continue

        if d == direct and st == 2:
            # On ne peut pas continuer tt droit
            continue

        if d == direct:
            # on continue dans la même direction, on incrémente
            st += 1
        else:
            # on change de direction, on reset le compteur
            st = 0
        yield (ni, nj), d, st    


global_path = {}
best_score = 0
@cache
def discover_path(puzzle, position, path, direction, straight, score):
    i, j = position
    score += int(puzzle[i][j])

    step = (i, j, direction)
    if step in global_path.keys() or score >= best_score:
        # on est sur une boucle, on abandonne
        # ou on a déjà dépassé le max score
        pass
    else:
        # on ajoute l'étape en cours
        path = path + (step,)
        global_path[path] = score
        if i == len(puzzle) - 1 and j == len(puzzle[0]) - 1:
            # on est sur la dernière case, c'est fini
            yield score
        else:
            for pos, direct, strai in get_possible_move(position, direction, straight, puzzle):
                yield from discover_path(puzzle, pos, path, direct, strai, score)



pos = (0, 0)
d = ">"
st = 0
score = 0
global_path = {}
path = ((0, 0, d))
best_score = 0
i = 0
j = 0
while(i<len(puz)-1):
    print(i, j)
    best_score += int(puz[i][j])
    i+=1
    print(i, j)
    best_score += int(puz[i][j])
    j+=1
print(i, j)
best_score += int(puz[i][j])

for _ in range(10):
    discover_path(puz, pos, path, d, st, score)

res = [p for (_, p) in zip(range(50), discover_path(puz, pos, path, d, st, score))]

res = [r for r in discover_path(puz, pos, path, d, st, score)]

discover_path(puz, pos, path, d, st, score)

l = list(global_path.keys())
i = 30
k = l[i]
v = global_path[l[i]]

print(k)
print(v)
