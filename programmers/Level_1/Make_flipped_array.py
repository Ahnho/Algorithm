###########################################
##         자연수 뒤집어 배열로 만들기       ##
###########################################

def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n)):
        answer.append(int(n[i]))
 
    return list(reversed(answer))