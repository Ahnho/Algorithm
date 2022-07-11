##########################################################
##                  구명 보트ㅡ        ##
##########################################################

def solution(people, limit):
    answer = 0
    people = sorted(people)
    h,t = 0, len(people) - 1
    
    while h <= t:
        answer += 1
        if people[h] + people[t] <= limit : 
            h += 1
        t -= 1
            
    return answer