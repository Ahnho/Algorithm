##############
#  정수 삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105
##############

def solution(triangle):
    for r in range(len(triangle)):
        triangle[r].append(0)
        triangle[r].insert(0,0)
    for i in range(1,len(triangle)):
        for j in range(1,len(triangle[i])-1):
            triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
        
    return max(triangle[-1])
