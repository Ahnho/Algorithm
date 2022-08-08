##############
#  가장 긴 팰린드롬
# https://school.programmers.co.kr/learn/courses/30/lessons/12904
##############

def solution(s):
    if s == s[::-1]:
        return len(s) 
    answer = 1
    
    
    for i in range(len(s)):
        for j in range(i+2,len(s)+1):
            pal = s[i:j]
            if len(pal) < answer :
                continue
            if pal == pal[::-1]:
                answer = len(pal)
    
    return answer
