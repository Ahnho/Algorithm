###########################################
##      문자열 내 마음대로 정렬하기          ##
###########################################

def solution(strings, n):

    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    
    strings = sorted(strings)
    for j in range(len(strings)):
        strings[j] = strings[j][1::]
    return strings