import sys

numCase = int(sys.stdin.readline())
for cnt in range(numCase):
    mat = []
    li = list(map(int, sys.stdin.readline().split()))
    for i in range(li[1]):
        line = list(map(str, sys.stdin.readline()))
        mat.append(line[:-1])
    position = li[2] * 2 -2 
    for k in range(li[1]-1, -1 ,-1):
        if position < li[0]*2-2 and mat[k][position+1] == "+":
            position +=2
        elif position >0 and mat[k][position-1] == "+": 
            position -= 2
    print(position//2 + 1)
