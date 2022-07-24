###########################################
##          점프와 순간 이동              ##
###########################################

# def solution(n):
#     return bin(n).count('1')

def solution(n):
    ans = 0
    while n > 1 :
        ans += n%2
        n = n // 2
    
    return ans+1
