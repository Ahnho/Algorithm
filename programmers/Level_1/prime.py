##############
#  소수 만들기
##############

from itertools import combinations as comb

def is_prime(n):
    for i in range(2,n//2):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    se = list(comb(nums,3))
    for i in se:
        sum_num = i[0] + i[1] + i[2]
        if is_prime(sum_num):
            answer += 1
       

    return answer