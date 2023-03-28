import sys

numCase = int(input())
for cnt in range(numCase):
    n,g = map(int, sys.stdin.readline().split())
    p = 0 
    cnt = 0
    while (p < n):
        if g != p + 2 :
            p += 2 
        elif g == p +1 :
            p += 2
        else:
            p += 1
        cnt += 1
    print(cnt)