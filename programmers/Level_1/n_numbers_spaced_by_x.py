###########################################
##      x만큼 간격의 n개의 숫자             ##
###########################################

def solution(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer