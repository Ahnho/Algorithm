###########################################
##           멀쩡한 사각형                 ##
###########################################

def gcd(n,m):
    if n < m : n,m = m,n
    while m : 
        k = n % m 
        n,m = m,k
    return n

def solution(w,h):
    return w*h - (w+h-gcd(w,h))