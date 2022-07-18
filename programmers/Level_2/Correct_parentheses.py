###########################################
##            올바른 괄호                  ##
###########################################

def solution(s):
    stack = []
    
    for i in s : 
        if not stack :
            stack.append(i)
            continue
        if i == ')' and stack[-1] == '(':
            stack.pop()
        else :
            stack.append(i)
    if not stack :
        return True
    return False