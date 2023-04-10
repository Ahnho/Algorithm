nl = int(input())

for _ in range(nl):
    n, m = map(int,input().split())
    li = list(map(int,input().split()))
    if len(li) % 2 == 1:
        li.append(0)
    li.sort(reverse=True)
    answer = 0 
    nn = len(li)//2
    diff = {}

    for i in range(nn):
        diff[i] = li[i*2] - li[i*2+1]
        # diff[li[i*2] - li[i*2+1]] = [li[i*2] , li[i*2+1]]
    diff = sorted(diff.items(), key=(lambda x:x[1]), reverse=True)

    for k,v in diff :
        if m > 0 :
            answer += li[k*2] 
            m -= 1
        else :
            answer += li[k*2+1]
    print(answer)



    