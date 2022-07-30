###########################################
##              H-Index                   ##
###########################################

def solution(citations):
    answer = sorted(citations)
    answer.reverse()
    for i,v in enumerate(answer):
        if i >= v:
           return v 
    return 0
