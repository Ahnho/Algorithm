###########################################
##                실패율                  ##
###########################################

import operator

def solution(N, stages):
    answer = {}
    relult = []
    stages = sorted(stages)
    num_stage = len(stages)
    for i in range(1,N+1):
        cnt = 0
        for j in stages : 
            if i == j :
                cnt += 1
        if not num_stage :
            num_stage = 1
        answer[i] = cnt/num_stage
        num_stage -= cnt
        
    answer = sorted(answer.items(), key=operator.itemgetter(1),reverse=True)

    for k in range(len(answer)):
        relult.append(answer[k][0])
    return relult