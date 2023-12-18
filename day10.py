
"""
.....
.012.
.1.3.
.234.
.....

0: (1,1)
1: (1,2)
2: (1,3)
3: (2,3)
4: (3,3)
5: (3,2)
6: (2,1)
7: (1,1)
"""

directions = {
    "|": [(-1, 0), (1, 0)], 
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
    ".": [(0, 0), (0, 0)]
}


def move(plateau, i, j, im, jm):
    """ on est en position i, j,
    et on vient de i-1, j-1,
    on retourne la nouvelle position
    """
    # Attention aux out of range si on sort du plateau

    pos = plateau[i][j]
    nextstep = directions[pos][0]
    ip, jp = i + nextstep[0], j + nextstep[1]
    if (ip == im) and (jp == jm):
        nextstep = directions[pos][1]
        ip, jp = i + nextstep[0], j + nextstep[1]

    return ip, jp, i, j


plateau = [[".",".",".",".","."],
           [".","S","-","7","."],
           [".","|",".","|","."],
           [".","L","-","J","."],
           [".",".",".",".","."]]


def get_start(plateau):
    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            if plateau[i][j] == "S":
                return i, j


file = open("input10.txt", "r")
lines = file.readlines()

plateau = []
for l in lines:
    l = l.replace('\n', '')
    plateau.append([c for c in l])

get_start(plateau)

bi, bj = 94, 97
fi, fj = 94, 99
bim, bjm = 94, 98
fim, fjm = 94, 98
keep_going = True
walk = 1
while(keep_going):
    try:
        bi, bj, bim, bjm = move(plateau, bi, bj, bim, bjm)
        fi, fj, fim, fjm = move(plateau, fi, fj, fim, fjm)
        #print(bi, )
        walk += 1
        if (bi == fi) and (bj == fj):
            keep_going = False
    except KeyError:
        print("Fin du parcours")
        keep_going = False

print(walk)


## Part two



file = open("input10_demo.txt", "r")
lines = file.readlines()

plateau = []
for l in lines:
    l = l.replace('\n', '')
    plateau.append([c for c in l])

new_plateau = []
for l in lines:
    l = l.replace('\n', '')
    new_plateau.append([0 for _ in range(len(l))])


get_start(plateau)

bi, bj = 4, 13
fi, fj = 5, 12
bim, bjm = 4, 12
fim, fjm = 4, 12
keep_going = True
walk = 1
new_plateau[bi][bj] = 1
new_plateau[fi][fj] = 1
parcours = [(4, 12)]
while(keep_going):
    try:
        bi, bj, bim, bjm = move(plateau, bi, bj, bim, bjm)
        #fi, fj, fim, fjm = move(plateau, fi, fj, fim, fjm)
        #print(bi, )
        walk += 1
        new_plateau[bi][bj] = 1
        parcours.extend([(bi, bj)])
        #new_plateau[fi][fj] = 1
        #if (bi == fi) and (bj == fj):
        #    keep_going = False
    except KeyError:
        print("Fin du parcours")
        keep_going = False

print(walk)

for l in new_plateau:
    l = [str(c) for c in l]
    print(''.join(l))

def display(p):
    for l in p:
        l = [str(c) for c in l]
        print(''.join(l))


new_plateau = []
for l in lines:
    l = l.replace('\n', '')
    new_plateau.append(['.' for _ in range(len(l))])

###############

cd = 'left'
cds = {
    "J": "up",
    "F": "down",
    "L": "up",
    "7": "left"
}
for i, j in parcours:
    if plateau[i][j] == 'J':
