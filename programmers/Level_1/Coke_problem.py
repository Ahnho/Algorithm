def solution(a, b, n):
    answer = 0
    num = 0
    while n >= a : 
        num = n//a * b
        n = num + n%a
        answer += num
      
    return answer
