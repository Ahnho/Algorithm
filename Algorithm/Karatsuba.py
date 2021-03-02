############################################
##        Karatsuba Multiplication        ##
############################################

# 1. 큰수의 곱에 효과적이다 
# 2. 보통 곱셈은 시간복잡도가 O(n^2) 이지만 Karatsuba는 O(n^1.585) 다
# 3. 제일 빠른 곱셈 알고리즘은 O(nlogn) 속도가 나오는 Havey and vander Oeven 알고리즘 이지만 10^850억 자리부터 적용이 가능하다

import time

def Karatsuba(A,B):
    sA = str(A)
    sB = str(B)
    
    if len(sA) >= len(sB) :
        n,m = len(sB),len(sB)//2 
    else :
        n,m = len(sA),len(sA)//2
    
    a1,a2 = int(sA[:-m]),int(sA[-m::])
    b1,b2 = int(sB[:-m]),int(sB[-m::])
    
    z0 = a1 * b1 
    z1 = a2 * b2
    z2 = (a1+a2) * (b1+b2)
    z3 = z2 - z1 -z0
    
    return 10**n*z0 + 10**m*z3 + z1


## test ## 

print(5678*1234)
print(Karatsuba(5678,1234))
    