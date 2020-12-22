###########################################
##             3진법 뒤집기                ##
###########################################

def th(n):
    result = ""
    cnt = 0
    while n >= 3**cnt :
        cnt += 1
    for i in range(cnt-1,-1,-1):
        cnt_2 = 0
        while n >= 3**i:
            n -= 3**i 
            cnt_2 += 1
        result += str(cnt_2)
    return result
        
def solution(n):
    answer = 0
    n_3 = th(n)[::-1]
    
    for i,v in enumerate(n_3):
        answer += int(v) * 3**(len(n_3)-1-i)
    
    return answer