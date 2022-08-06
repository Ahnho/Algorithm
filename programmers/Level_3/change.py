###########################################
##            거스름돈                   ##
###########################################

def solution(n, money):
    dp = [1] + [0]*n 
    for m in money : 
        for p in range(m,n+1):
            dp[p] += dp[p-m]
            
    return dp[n] % 1000000007
