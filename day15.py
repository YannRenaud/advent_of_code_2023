
demo = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

file = open("input15.txt")
lines = file.readlines()
line = lines[0]

def get_hash(word, total):
    if word == "":
        return total
    else:
        total += ord(word[0])
        total = total * 17
        total = total % 256
        return get_hash(word[1:], total)


result = 0
for seq in line.split(","):
    result += get_hash(seq, 0)
result