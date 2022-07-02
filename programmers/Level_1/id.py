##############
#  신규 아이디 추천
##############

def solution(new_id):
    answer = ''
    li = "~!@#$%^&*()=+[{]}:?,<>/"
    li.split()
    
    # step 1
    new_id = new_id.lower()
    
    # step 2
    for i in range(len(new_id)):
        if new_id[i] not in li:
            answer += new_id[i]
    
    # step 3 
    while ".." in answer:
        answer = answer.replace('..','.')
    
    # step 4
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and  answer[-1] == '.':
        answer = answer[:-1]
    
    # step 5 
    if len(answer) == 0 or answer == '.':
        answer = "a"
    
    # step 6
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    
    # step 7
    if len(answer) <= 2:
        a = answer[-1]
        while len(answer) < 3 :
            answer += a
        
            
    
    return answer