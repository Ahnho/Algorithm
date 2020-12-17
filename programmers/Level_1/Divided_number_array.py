###########################################
##           나누어 떨어지는 숫자 배열       ##
###########################################


def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0 : 
            answer.append(i)
    if len(answer) == 0 :
        return [-1]
    return sorted(answer)