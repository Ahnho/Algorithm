###########################################
##            숫자 블록                ##
###########################################


def dg(x):
    result = 1
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0 and x//i <= 10000000:
            result = x//i
            break
    return result

def solution(begin, end):
    answer = []
    if begin == 1:
        answer.append(0)
    else :
        answer.append(dg(begin))
    for i in range(begin+1, end+1):
        answer.append(dg(i))
    return answer
