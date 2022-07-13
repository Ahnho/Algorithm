###########################################
##           다음 큰 숫자                  ##
###########################################


def solution(n):
    answer = n + 1
    bin_n = bin(n).count('1')
            
    while 1:
        if bin(answer).count('1') == bin_n:
            break
        answer += 1
    return answer