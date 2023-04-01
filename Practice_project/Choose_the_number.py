import sys
q = int(input())

for _ in range(q):
    n,m = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    li.sort()
    li = li[::-1]
    answer = 1000000001
    for i in range(n-1):
        for j in range(i+1,n):
            num = li[i] - li[j]
            if num == m :
                answer = num 
                break
            elif num >= m and  answer > num :
                answer = num
        if answer == m :
            break

    print(answer)