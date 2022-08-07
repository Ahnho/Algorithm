##############
#  등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898
##############

def solution(m, n, puddles):
    dp = [[0]*(m+1) for i in range(n+1)]
    for p in puddles:
        dp[p[1]][p[0]] = -1
    dp[1][1] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [i,j] == [1,1] :continue
            if dp[i][j] == -1 :
                dp[i][j] = 0
            else: dp[i][j] = dp[i-1][j] + dp[i][j-1] 
    print(dp)
    
    return dp[-1][-1] % 1000000007
