###########################################
##           괄호 회전하기                  ##
###########################################


def solution(s):
    answer = 0
    temp = list(s)
    for i in range(len(s)):
        stack = []
        for k in temp :
            if len(stack) > 0 :
                if stack[-1] == '[' and k == ']' :
                    stack.pop()
                elif stack[-1] == '(' and k == ')':
                    stack.pop()
                elif stack[-1] == '{' and k == '}':
                    stack.pop()
                else:
                    stack.append(k)
            else:
                stack.append(k)
        if not stack :
            answer += 1
        temp.append(temp.pop(0))
        
    return answer