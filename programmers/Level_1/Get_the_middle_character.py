###########################################
##           가운데 글자 가져오기           ##
###########################################

def solution(s):
    if len(s) % 2 == 1:
        return s[len(s)//2]
    return s[len(s)//2-1] + s[len(s)//2]