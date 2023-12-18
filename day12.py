import re
from itertools import product


def get_basic(combo):
    return ".".join(['#'*i for i in combo])


def get_pos_index(basic):
    res = [0]
    res.extend([i.start() for i in re.finditer(pattern='\.', string=basic)])
    res.extend([len(basic)])
    return res


def valide_possibility(basic, combo, idx, origin):
    res = basic
    for i, n in zip(idx[::-1], combo[::-1]):
        res = res[:i] + "." * n + res[i:]
    
    return all([origin[i] == res[i] if origin[i] != "?" else True for i in range(len(res))])


def find_combinations(n, x):
    combinations = []
    
    # Generate combinations of n elements including 0
    for combo in product(range(x+1), repeat=n):
        if sum(combo) == x:
            combinations.append(combo)
    
    return combinations


file = open('2023/input12_demo.txt')
lines = file.readlines()
total = 0
for line in lines:
    line = line.replace('\n', '')

    sequence = line.split(' ')[0]
    sequence = '?'.join([sequence] * 5)

    combo = line.split(' ')[1]
    combo = ','.join([combo] * 5)
    combo = [int(i) for i in combo.split(',')]
    linel = len(sequence)

    basic = get_basic(combo)
    idx = get_pos_index(basic)

    to_fill = len(sequence) - len(basic)
    pos_comb = find_combinations(len(idx), to_fill)

    result = sum([valide_possibility(basic, p, idx, sequence) for p in pos_comb])
    total += result

print(total)


## Part two

global_result = {}
def count_combo(sequence, combo):

    # Si la séquence est vide, on retourne 1 s'il n'y a plus de combo à faire , sinon 0
    if sequence == "":
        return 1 if combo == () else 0

    # Si on a fait tous les combos, on retourne 0 s'il reste des # (on peut remplacer les ? par des . pour la fin de la séquence)
    if combo == ():
        return 0 if "#" in sequence else 1

    mem_key = (sequence, combo)
    if mem_key in global_result.keys():
        return global_result[mem_key]

    result = 0
    if sequence[0] in ".?":
        # si . ou , on skip le caractère et on continue
        result += count_combo(sequence[1:], combo)
    if sequence[0] in "#?":
        # si # ou ?, début d'un nouveau bloc
        # condition1 => la séquence est assez longue pour finir le bloc
        # condition2 => il n'y a pas de . dans les n caractères nécessaires pour faire le bloc
        # condition3 => soit c'est la fini de la séquence soit le caractère juste après le bloc est . ou ? pour être sûr que le bloc est fini
        if combo[0] <= len(sequence) and "." not in sequence[:combo[0]] and (combo[0] == len(sequence) or sequence[combo[0]] != "#"):
            result += count_combo(sequence[combo[0] + 1:], combo[1:])

    global_result[mem_key] = result
    return result


file = open('2023/input12.txt')
lines = file.readlines()
total = 0
for line in lines:
    line = line.replace('\n', '')

    sequence = line.split(' ')[0]
    sequence = '?'.join([sequence] * 5)
    combo = line.split(' ')[1]
    combo = ','.join([combo] * 5)
    combo = tuple([int(i) for i in combo.split(',')])    
    total += count_combo(sequence, combo)

print(total)



len(global_result)
list(global_result.keys())[0:3]

global_result[list(global_result.keys())[0]]

('##?#????.???#??.?##?#????.???#??.?##?#????.???#??.?##?#????.???#??.?##?#???', (1, 7, 1, 1, 7, 1, 1, 7, 1, 1, 7, 1, 1, 7)),
('?##?#????.???#??.?##?#????.???#??.?##?#????.???#??.?##?#????.???#??.?##?#???', (1, 7, 1, 1, 7, 1, 1, 7, 1, 1, 7, 1, 1, 7)), 
('.?##?#????.???#??.?##?#????.???#??.?##?#????.???#??.?##?#????.???#??.?##?#???', (1, 7, 1, 1, 7, 1, 1, 7, 1, 1, 7, 1, 1, 7))



total = 0
for line in open('2023/input12_demo.txt'):
    sequence, combo = line.split()
    combo = tuple(map(int, combo.split(',')))
    total += count_combo(sequence, combo)

print(total)