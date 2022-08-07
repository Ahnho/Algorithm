##############
#  디스크 컨트롤러 
# https://programmers.co.kr/learn/courses/30/lessons/42627
##############


import heapq

def solution(jobs):
    time,completed,now,start = 0,0,0,-1
    heap = []

    while completed < len(jobs) : 
        for job in jobs:  
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        if len(heap) > 0 :
            currnt = heapq.heappop(heap)
            start = now 
            now += currnt[0]
            time += (now-currnt[1])
            completed += 1
        else : 
            now += 1

    return time//len(jobs)
