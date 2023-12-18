import itertools


file = open("input11.txt", "r")
lines = file.readlines()

lines = [l.replace("\n", "") for l in lines]

univ = []
for line in lines:
    univ.append([l for l in line])


def expand(univ):
    ip = []
    for i in range(len(univ)):
        row = univ[i]
        # print(i, row)
        if all([c == '.' for c in row]):
            ip.append(i)

    jp = []
    for j in range(len(univ[0])):
        col = [univ[i][j] for i in range(len(univ))]
        # print(j, col)
        if all([c == '.' for c in col]):
            # print(j)
            jp.append(j)

    ip.sort(reverse=True)
    for i in ip:
        univ = univ[0: i] + [['.'] * len(univ[0])] + univ[i:]

    jp.sort(reverse=True)
    for i in range(len(univ)):
        for j in jp:
            univ[i] = univ[i][0:j] + ['.'] + univ[i][j:]

    return ip, jp, univ


ip, jp, univ = expand(univ)


display(univ)


def display(univ):
    for l in univ:
        print(''.join(l))


def get_pos(univ):
    count = 1
    res = {}
    for i in range(len(univ)):
        for j in range(len(univ[0])):
            if univ[i][j] == '#':
                res[count] = (i, j)
                count += 1
    
    return res

res = get_pos(univ)

combinations = list(itertools.combinations(list(res.keys()), 2))

def get_distance(posa, posb):
    ia, ja = posa
    ib, jb = posb

    if ia > ib:
        d = ia - ib
    else:
        d = ib-ia

    if ja > jb:
        d += ja - jb
    else:
        d += jb-ja

    return d

s = 0
for a, b in combinations:
    s += get_distance(res[a], res[b])


## Part two


def get_distance_bis(posa, posb, ip, jp, m):
    ia, ja = posa
    ib, jb = posb

    d = 0
    if ia > ib:
        d += ia - ib
        for i in ip:
            if (ib < i) and (i < ia):
                d += m-1
    elif ia < ib:
        d = ib-ia
        for i in ip:
            if (ia < i) and (i < ib):
                d += m-1

    if ja > jb:
        d += ja - jb
        for j in jp:
            if (jb < j) and (j < ja):
                d += m-1
    elif ja > jb:
        d += jb-ja
        for j in jp:
            if (ja < j) and (j < jb):
                d += m-1

    return d

s = 0
for a, b in combinations:
    s += get_distance_bis(res[a], res[b], ip, jp, 1000000)

s

low 545947753755
low 545947207814
high 6......
