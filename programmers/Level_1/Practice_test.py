###########################################
##           모의고사                     ##
###########################################

def solution(answers):
    answer = []
    supo_1 = [1,2,3,4,5] 
    supo_2 = [2,1,2,3,2,4,2,5]
    supo_3 = [3,3,1,1,2,2,4,4,5,5]
    cnts = [0,0,0]

    
    for i,v in enumerate(answers):
        if v == supo_1[i%len(supo_1)]:
            cnts[0] += 1
        if v == supo_2[i%len(supo_2)]:
            cnts[1] += 1
        if v == supo_3[i%len(supo_3)]:
            cnts[2] += 1
    for j,k in enumerate(cnts):
        if k == max(cnts):
            answer.append(j+1)
    return answer