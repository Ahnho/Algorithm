##############
# 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666
##############

def solution(survey, choices):
    answer = ''
    li = [0,0,0,0] 
    su = ['RT','CF','JM','AN']
    for s,c in zip(survey, choices):
        if ord(s[0]) > ord(s[1]):
            c = c-4
        else :
            c = 4-c
        if s == 'RT' or s == 'TR':
            li[0] += c 
        elif s == 'FC' or s == 'CF':
            li[1] += c 
        elif s == 'MJ' or s == 'JM':
            li[2] += c 
        elif s == 'AN' or s == 'NA':
            li[3] += c 
    
    for l,s in zip(li,su):
        if l >= 0 :
            answer += s[0]
        else:
            answer += s[1]
        
    return answer
