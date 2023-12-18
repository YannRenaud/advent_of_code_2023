

file = open('input9.txt')
lines = file.readlines()
lines
seq = []
for line in lines:
    line = line.replace('\n', '')
    seq.append([int(i) for i in line.split(' ')])

seq


def getdif(l):
    sl = l
    for i in range(len(l)-1):
        sl = [sl[i+1]-sl[i] for i in range(len(sl)-1)]
        yield sl

def getnext(l):
    for i in range(len(l)-1, 0, -1):
        ad = l[i][-1]
        l[i-1].extend([l[i-1][-1]+ad])
    return l


res = 0
for s in seq:
    sub = []
    sub.append(s)
    for i in getdif(s):
        if all([a == 0 for a in i]):
            break
        sub.append(i)
    s = getnext(sub)[0]
    res += s[-1]

print(res)


## Part two

def getdif(l):
    sl = l
    for i in range(len(l)-1):
        sl = [sl[i+1]-sl[i] for i in range(len(sl)-1)]
        yield sl

def getnext(l):
    for i in range(len(l)-1, 0, -1):
        ad = l[i][-1]
        l[i-1].extend([l[i-1][-1]+ad])
    return l

def revers(l, i):
    sb = l[i][0]
    r = [l[i-1][0]-sb]
    r.extend(l[i-1])
    return r


res = 0
for s in seq:
    sub = []
    sub.append(s)
    for i in getdif(s):
        if all([a == 0 for a in i]):
            break
        sub.append(i)
    
    for i in range(len(sub)-1, 0, -1):
        sub[i-1] = revers(sub, i)
    
    print(sub)
    res += sub[0][0]

print(res)

l = [[10, 13, 16, 21, 30, 45], [3, 3, 5, 9, 15], [0, 2, 4, 6], [2, 2, 2]]


for i in range(len(l)-1, 0, -1):
    l[i-1] = revers(l, i)




def reversbis(l):
    sb = l[i][0]
    r = [l[i-1][0]-sb]
    r.extend(l[i-1])
    return r


