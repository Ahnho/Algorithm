###########################################
##        같은 숫자는 싫어                 ##
###########################################

def solution(arr):
    answer = [arr[0]]
    
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer