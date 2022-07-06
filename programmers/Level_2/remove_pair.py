##########################################################
##                   짝지어 제거하기           ##
##########################################################


def solution(s):
    if len(s) % 2 == 1: return 0
    stack = []
    
    for i in s:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        elif stack[-1] == i :
            stack.pop()

    return 1 if len(stack) == 0 else 0