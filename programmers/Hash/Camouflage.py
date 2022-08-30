##############
#  위장
# https://programmers.co.kr/learn/courses/30/lessons/42578
##############

def solution(clothes):
    answer = 1
    ty = [i[1] for i in clothes]
    kind = set(ty) 
    for ch in kind:
        answer *= ty.count(ch)+1
 
    return answer-1
