##############
#  H_index
# https://programmers.co.kr/learn/courses/30/lessons/42747
##############

def solution(citations):
    answer = sorted(citations)
    answer.reverse()
    
    for i,v in enumerate(answer):
        if i >= v:
            return i
    return len(answer)