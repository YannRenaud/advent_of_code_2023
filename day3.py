import numpy as np

file = open("input3.txt", "r")
lines = file.readlines()

ll = []
for line in lines:
    line = line.replace('\n', '')
    ll.append(list(line))

def check_close_spec_char(mat, r, c):
    rmin = max(0, r-1)
    rmax = min(r+1, len(mat)-1)
    cmin = max(c-1, 0)
    cmax = min(c+1, len(mat[0])-1)
    print(rmin, rmax, cmin, cmax)
    for i in range(rmin, rmax+1):
        for j in range(cmin, cmax+1):
            print(i, j, mat[i][j])
            if mat[i][j] not in nums and mat[i][j] != '.':
                return True
    return False

nums = [str(n) for n in range(10)]
cur_num = ''
cur_spec = False
cur_sum = 0

for i in range(len(ll)):
    for j in range(len(ll[0])):
        char = ll[i][j]
        if char in nums:
            cur_num += char
            cur_spec = cur_spec or check_close_spec_char(ll, i, j)
        else:
            if cur_num != '':
                # on passe à un point/car spec après un num => fin de la série
                if cur_spec:
                    # on compte le nombre s'il y avait un caractère spec
                    cur_sum += int(cur_num)
            cur_num = ''
            cur_spec = False

cur_sum


## Part two

file = open("input3.txt", "r")
lines = file.readlines()

ll = []
for line in lines:
    line = line.replace('\n', '')
    ll.append(list(line))


def check_close_spec_char_two(mat, r, c):
    rmin = max(0, r-1)
    rmax = min(r+1, len(mat)-1)
    cmin = max(c-1, 0)
    cmax = min(c+1, len(mat[0])-1)
    #print(rmin, rmax, cmin, cmax)
    for i in range(rmin, rmax+1):
        for j in range(cmin, cmax+1):
            #print(f"({i}, {j}) => {mat[i][j]}")
            if mat[i][j] == '*':
                return (True, f"{i}_{j}")
    return (False, "")


nums = [str(n) for n in range(10)]
cur_num = ''
cur_spec = False
post_mat = {}
cur_sum = 0
cur_pos = None
for i in range(len(ll)):
    for j in range(len(ll[0])):
        char = ll[i][j]
        if char in nums:
            cur_num += char
            res, pos = check_close_spec_char_two(ll, i, j)
            #print(res, pos)
            #print('-----------')
            if res:
                cur_pos = pos
        else:
            if cur_num != '':
                #print(f'fin série => {cur_num}')
                # on passe à un point/car spec après un num => fin de la série
                if cur_pos != "":
                    # on note la position pour tout à l'heure
                    print(cur_pos, cur_num)
                    if cur_pos in post_mat.keys():
                        post_mat[cur_pos].append(int(cur_num))
                        #print(f"ajout mat : {post_mat}")
                    else:
                        post_mat[cur_pos] = [int(cur_num)]
                        #print(f"init mat : {post_mat}")
            cur_num = ''
            cur_pos = ''

print(post_mat)

result = 0
for _, val in post_mat.items():
    if len(val) > 1:
        result += np.prod(val)

result