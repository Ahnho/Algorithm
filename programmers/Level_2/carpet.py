##########################################################
##                   카펫          ##
##########################################################

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1,total//2+1):
        if i*(total//i) == total and (i-2)*(total//i-2) == yellow:
            return [total//i,i]
    return answer