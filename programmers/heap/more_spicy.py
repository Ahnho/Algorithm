##############
#  더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626
##############

import heapq as hq 

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)

    while scoville[0] < K :
        if len(scoville) < 2 :
            return -1
        a,b = hq.heappop(scoville),hq.heappop(scoville)
        hq.heappush(scoville, a + b*2)
        answer += 1
        
    return answer 
