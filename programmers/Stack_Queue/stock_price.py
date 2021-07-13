##############
#  주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584
##############


from collections import deque

def solution(prices):
    dq = deque(prices) 
    answer = []
    while dq :
        cnt = 0
        ft = dq.popleft()
        for p in dq :
            cnt += 1
            if ft > p:
                break 
        answer.append(cnt)
    return answer