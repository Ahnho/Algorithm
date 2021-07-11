##############
#  기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586
##############

def solution(progresses, speeds):
    Q = []
    answer = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    for i in Q:
        answer.append(i[1])
    return answer