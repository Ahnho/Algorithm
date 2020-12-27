###########################################
##          JadenCase 문자열 만들기        ##
###########################################

def solution(s):
    
    return s.title()

############################################

def solution(s):
    s = s.lower()
    answer = ""
    s_li = s.split(" ")
    for i,v in enumerate(s_li):
        if v == "" :
            answer += " "
        else:
            answer += v[0].upper() + v[1::] 
        if i != len(s_li)-1 and v != "" :
            answer += " "
        if i == len(s_li)-2 and s_li[i+1] == "" :
            return answer
        
    return answer
