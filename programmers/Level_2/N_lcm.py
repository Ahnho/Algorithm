###########################################
##          N개의 최소공배수               ##
###########################################

def gcd(n,m):
    if n < m : n,m = m,n 
    while m : 
        k = n % m 
        n,m = m,k
    return n

def lcm(n,m):
    return n*m/gcd(n,m)

def solution(arr):
    answer = lcm(arr[0],arr[1])
    for i in range(2,len(arr)):
        answer = lcm(answer,arr[i])
    return answer
