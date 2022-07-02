##########################################################
##                   줄 서는 방법            ##
##########################################################


def fac(n):
    v = 1
    for i in range(1, n+1):
        v *= i
    return v

def solution(n, k):
    answer = []
    li = [i for i in range(1,n+1)]
    
    while li:
        temp = fac(n-1)
        q, r = divmod(k, temp)
        if r == 0:
            q = q-1 
        
        answer.append(li.pop(q))
        
        n -= 1
        k = r
        
    return answer