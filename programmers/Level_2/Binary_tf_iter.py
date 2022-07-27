###########################################
##            이진 변환 반복하기            ##
###########################################

def solution(s):
    count, zero_count = 0,0
    while len(s) > 1 :
        sc = s.count("1")
        zero_count += len(s) - sc
        s = bin(sc)[2::]
        count += 1
    return [count,zero_count]
