##############
#  음양 더하기
##############

def solution(absolutes, signs):
    answer = 0
    for a,s in zip(absolutes, signs):
        if s:
            answer += a 
        else :
            answer -= a
    return answer