###########################################
##         문자열 다루기 기본               ##
###########################################

def solution(s):
    cnt = 0
    if len(s) != 4 and len(s) != 6 :
        return False
    
    for i in s :
        if not 47 < ord(i) < 58 :
            return False
    return True