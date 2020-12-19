###########################################
##           정수 내림차순으로 정렬         ##
###########################################


def solution(n):
    answer = ''
    li = []
    for i in str(n):
        li.append(i)
        
    li = sorted(li)
    li.reverse()
    
    for j in li:
        answer += j
    return int(answer) 