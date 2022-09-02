##############
#  다리를 지나는 트럭 
# https://programmers.co.kr/learn/courses/30/lessons/42583
##############

def solution(bridge_length, weight, truck_weights):
    time = 0
    tob = [0] * bridge_length
    sm = 0
    
    while tob :
        time += 1
        sm -= tob.pop(0)
        if truck_weights:
            if sm + truck_weights[0] <= weight:
                sm += truck_weights[0]
                tob.append(truck_weights.pop(0))
            else:
                tob.append(0)
    
    return time 
