###########################################
##          문자열을 정수로 바꾸기          ##
###########################################


def solution1(s):
    return int(s)


#############################################

def solution2(s):
    answer = 0
    cnt = 0 
    m = 0
    
    if s[0] == "-":
        s = s.replace("-","")
        m = 1
    if s[0] == "+":
        s = s.replace("+","")
    
    for i in s:
        answer += int(i) * 10**(len(s)- 1-cnt)
        cnt += 1
            
    if m :
        return -answer
    return answer