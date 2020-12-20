###########################################
##               소수 찾기                ##
###########################################

def solution(n):
    answer = [1]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if answer[i] :
            for j in range(2*i, n+1, i):
                answer[j] = 0
    return sum(answer)-2