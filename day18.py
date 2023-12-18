

def get_puz(demo=True):
    puz = []
    if demo:
        file = open("input18_demo.txt")
    else:
        file = open("input18.txt")

    return file.readlines()

puz = get_puz()

def move(d, l, c):
    """
    d : direction
    l : length
    c : current pos
    """
    i, j = c
    if d == 'U':
        i -= l
    if d == 'D':
        i += l
    if d == 'L':
        j -= l
    if d == 'R':
        j += l
    
    return (i, j)

current = (0, 0)
pos = [current]
for p in puz:
    d, l, c = p.split()
    current = move(d, int(l), current)
    pos.extend([current])


def get_max(pos):
    im, jm = 0, 0
    for i, j in pos:
        im = max(im, i)
        jm = max(jm, j)
    
    return (im+1, jm+1)

cmax = get_max(pos)


def build_puz(cmax, pos):
    im, jm = cmax
    puz = []
    for i in range(im):
        for j in range(jm):
            puz[i][j] = "."
    
    for i, j in pos:
        puz[i][j] = "#"
    
    return puz

puz = build_puz(cmax, pos)