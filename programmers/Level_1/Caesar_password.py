###########################################
##           시저 암호                    ##
###########################################

def solution(s, n):
    answer = ''
    for i in s :
        if ord(i) == 32 :
            answer += " "
        elif ord(i)+n > 122 :
            answer += chr(ord(i)+n-26)
        elif ord(i)+n > 90 and ord(i) <= 90:
            answer += chr(ord(i)+n-26)
        else : 
            answer += chr(ord(i)+n)
        
    return answer