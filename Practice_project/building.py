# 건물
import sys

numCase = int(input())
for cnt in range(numCase):
    n = int(input())
    g = list(map(int, sys.stdin.readline().split()))
    max = 0
    count =0
    for i in range(n):
        if g[-1-i] > max :
            max = g[-1-i] 
            count += 1
    print(count)
