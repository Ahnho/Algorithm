##############
#  폰켓몬
##############

def solution(nums):
    length = len(nums) // 2 
    set_len = len(set(nums))
    return min(length,set_len)