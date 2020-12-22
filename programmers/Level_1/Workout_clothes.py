###########################################
##                체육복                  ##
###########################################

def solution(n, lost, reserve):
    lli = []
    for k in lost:
        if k in reserve:
            lli.append(k)
    for v in lli:
        lost.remove(v)
        reserve.remove(v)
    
    for i in range(1,n+1):
        if i in lost:
            if i-1 in reserve :
                lost.remove(i)
                reserve.remove(i-1)
            elif i+1 in reserve :
                lost.remove(i)
                reserve.remove(i+1)
                
    return n-len(lost)