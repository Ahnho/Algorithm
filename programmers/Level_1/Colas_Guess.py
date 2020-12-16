    ###########################################
##          콜라스 추측                   ##
###########################################

def solution(num):
    cnt = 0
    while num != 1 :
        if num%2 : 
            num = num*3+1
        else:
            num /= 2
        cnt += 1
        if cnt >= 500:
            return -1

    return cnt 
