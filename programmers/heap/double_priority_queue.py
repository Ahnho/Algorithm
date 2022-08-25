##############
#  이중우선순위큐
# https://programmers.co.kr/learn/courses/30/lessons/42628
##############

import heapq

def solution(operations):
    heap = []
    for i in operations:
        if i[0] == "I":

            heapq.heappush(heap, int(i[2::]))
        else:
            if i == "D 1" and  heap:
                heap.pop(heap.index(heapq.nlargest(1,heap)[0]))
            elif i == "D -1" and  heap:
                heapq.heappop(heap)
    if heap : 
        return [heapq.nlargest(1,heap)[0],heapq.nsmallest(1,heap)[0]]
    return [0,0]
 
