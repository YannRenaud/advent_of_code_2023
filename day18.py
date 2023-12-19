

def get_puz(demo=True):
    puz = []
    if demo:
        file = open("input18_demo.txt")
    else:
        file = open("input18.txt")

    return file.readlines()

puz = get_puz(demo=True)

def move(d, l, c):
    """
    d : direction
    l : length
    c : current pos
    """
    i, j = c
    if d == 'U':
        i -= l
        return i, j

    if d == 'D':
        i += l
        return i, j

    if d == 'L':
        j -= l
        return i, j
    if d == 'R':
        j += l
        return i, j


def get_perimeter(d, l, c):
    """
    d : direction
    l : length
    c : current pos
    """
    i, j = c
    if d == 'U':
        for _ in range(l):
            i -= 1
            yield (i, j)

    if d == 'D':
        for _ in range(l):
            i += 1
            yield (i, j)

    if d == 'L':
        for _ in range(l):
            j -= 1
            yield (i, j)
    if d == 'R':
        for _ in range(l):
            j += 1
            yield (i, j)



current = (0, 0)
perim = [current]
for p in puz:
    d, l, c = p.split()
    for m in get_perimeter(d, int(l), current):
        perim.extend([m])
    current = m


current = (0, 0)
pos = [current]
for p in puz:
    d, l, c = p.split()
    for m in move(d, int(l), current):
        pos.extend([m])
    current = m


current = (0, 0)
pos = [current]
for p in puz:
    d, l, c = p.split()
    m = move(d, int(l), current)
    pos.extend([m])
    current = m



def compute_area(positions):
    res = 0
    copy = positions[::-1]
    for c, p in enumerate(copy[:-1]):
        i, j = p
        ip, jp = positions[c+1]
        res += (i*jp - ip*j)
    return res


def compute_area(positions):
    res = 0
    copy = positions[::-1]
    for c, p in enumerate(copy[:-1]):
        i, j = p
        ip, jp = positions[c+1]
        res += (j+jp) * (i-ip)
    return res / 2


result = compute_area(pos)
result

def get_max(pos):
    im, jm = 0, 0
    for i, j in pos:
        im = max(im, i)
        jm = max(jm, j)
    
    return (im+1, jm+1)

cmax = get_max(pos)


def build_puz(cmax, pos):
    im, jm = cmax
    puz = [["."]*jm for _ in range(im)]

    for i, j in pos:
        puz[i][j] = "#"
    
    return puz

mat = build_puz(cmax, perim)

def display(puz):
    for line in puz:
        print(''.join(line))

display(mat)


def shoelace_formula(x_coords, y_coords):
    # Ensure the number of x and y coordinates are the same
    if len(x_coords) != len(y_coords):
        raise ValueError("The number of x and y coordinates must be the same.")

    # Number of vertices
    n = len(x_coords)

    # Initialize area
    area = 0.0

    # Calculate the area using the Shoelace formula
    for i in range(n - 1):
        area += (x_coords[i] * y_coords[i + 1]) - (x_coords[i + 1] * y_coords[i])

    # Add last term (wrapping around to the first vertex)
    area += (x_coords[n - 1] * y_coords[0]) - (x_coords[0] * y_coords[n - 1])

    # Take the absolute value and divide by 2
    area = abs(area) / 2.0

    return area


# Example coordinates of an irregular polygon
x_coordinates = []
y_coordinates = []
for i, j in pos:
    x_coordinates.append(i)
    y_coordinates.append(j)

# Compute the area using the Shoelace formula
polygon_area = shoelace_formula(x_coordinates, y_coordinates)
print("Area of the irregular polygon:", polygon_area)



def not_in_area(mat):
    res = 0
    for i in range(len(mat)):
        