##############
#  약수의 개수와 덧셈
##############

def cnt(n):
    c = 0
    for i in range(1,n+1):
        if n%i == 0:
            c += 1
    return c

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if cnt(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer