###########################################
##         최대공약수 최소공배수            ##
###########################################

def gcd(n,m):
    if n < m : n,m = m,n
    while m : 
        k = n % m 
        n,m = m,k
    return n

def lcm(n,m):
    return n*m/gcd(n,m)

def solution(n, m):
    return [gcd(n,m),lcd(n,m)]