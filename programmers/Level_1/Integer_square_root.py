###########################################
##          정수 제곱근 판별               ##
###########################################

from math import sqrt 

def solution(n):
    if sqrt(n) == int(sqrt(n)) :
        return (sqrt(n)+1) ** 2
    return -1