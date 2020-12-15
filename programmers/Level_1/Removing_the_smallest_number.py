###########################################
##           제일 작은 수 제거하긱          ##
###########################################

def solution(arr):
    answer = arr
    if len(arr) == 1:
        return [-1] 
    
    rm_num = (sorted(arr)[::-1]).pop()
    answer.remove(rm_num)
    return answer