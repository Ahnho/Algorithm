###########################################
##            최고의 집합                  ##
###########################################

def solution(n, s):
    if n > s :
        return [-1]
    answer = []
    for i in range(n):
        a = s//n
        s -= a 
        n -= 1
        answer.append(a)
    return answer
