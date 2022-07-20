###########################################
##            모음 사전                    ##
###########################################


def solution(word):
    answer = 0
    m = 781
    
    for i, n in enumerate(word):
        answer += m * "AEIOU".index(n) + 1 
        m = (m-1)/5

    return answer
