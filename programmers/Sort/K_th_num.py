##############
#  K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748
##############

def solution(array, commands):
    
    answer = []
    for i in range(len(commands)):
        num = array[commands[i][0]-1:commands[i][1]]
        answer.append(sorted(num)[commands[i][2]-1])
    return answer