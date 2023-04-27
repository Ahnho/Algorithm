n_case = int(input())

for _ in range(n_case):
    q,j,w,l = map(int, input().split())
    home = list(input().split())
    nothome = list(input().split())
    li = []
    teams = []
    for i in range(l):
        lis = []
        lis.append(list(map(int, input().split())))
        teams.append(lis[0][0])
        lis.append(list(input().split()))
        li.append(lis)
    a = []
    b= []
    for k,i in enumerate(li):
        cnt = 0
        for o in range(i[0][1]):
            if i[1][o] in nothome :
                cnt += 1
                break
        if cnt == 0 :
            a.append(k+1)
            b.append(i[0][0])
    ar = []
    for i in range(q):
        if b.count(i+1) == teams.count(i+1):
            ar.append(i+1)
    for i in range(len(a)):
        if not ar :
            break
        elif b[i] == ar[0]:
            ar.pop()
            a.pop(i)
    if not a :
        print(-1)
    else:
        answer = ""
        for i in range(len(a)):
            if i+1 == len(a):
                answer += str(a[i])
            else :
                answer += str(a[i]) + " "
        print(answer)