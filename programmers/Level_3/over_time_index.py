###########################################
##            야근 지수                  ##
###########################################

import heapq

def solution(n, works):
    if n > sum(works) : return 0

    works = [-k for k in works]
    heapq.heapify(works)
    
    for j in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)
        
    return sum([w**2 for w in works])
