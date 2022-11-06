##############
#  프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587
##############

def solution(priorities, location):
    answer = 0
    Q = [[p,i] for i,p in enumerate(priorities)]
    mx = max(priorities)
    
    while 1 : 
        ft = Q.pop(0)
        ftp = priorities.pop(0)
        if mx == ft[0]:
            answer += 1
            if location == ft[1]:
                break
            mx = max(priorities)
        else:
            Q.append(ft)
            priorities.append(ftp)
        
    
    return answer 
