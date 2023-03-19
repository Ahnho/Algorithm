import sys

numCase = int(input())
for cnt in range(numCase):
    n,p = map(int, sys.stdin.readline().split())
    cost = list(map(int, sys.stdin.readline().split()))
    cost.sort()
    head,tail = 0,n-1
    for i in range(n-2):
        if head >= tail: 
            break 
        if p == cost[head] + cost[tail]:
            break
        elif p > cost[head] + cost[tail]:
            head += 1
        else :
            tail -= 1
            
    print(cost[head],cost[tail])

