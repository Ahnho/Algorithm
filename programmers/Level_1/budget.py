###########################################
##               예산                     ##
###########################################

def solution(d, budget):
    cnt = 0
    
    for i in sorted(d):
        if i <= budget:
            budget -= i
            cnt += 1
    
    return cnt