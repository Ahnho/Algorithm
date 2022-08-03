###########################################
##            숫자 게임                 ##
###########################################

def solution(A, B):
    answer = 0
    A,B = sorted(A)[::-1], sorted(B)[::-1]
    for i in A:
        if i >= B[0]:
            continue
        else:
            answer += 1
            B.pop(0)
    return answer
