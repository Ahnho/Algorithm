##########################################################
##                    최댓값과 최솟값                     ##
##########################################################

def solution(s):
    s_li = s.split(" ")
    for i,v in enumerate(s_li):
        s_li[i] = int(v)
    return str(min(s_li)) +" " + str(max(s_li)) 
