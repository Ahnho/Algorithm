###########################################
##               2016년                  ##
###########################################

def solution(a, b):
    dow = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    total = 0
    
    for i in range(a):
        total += days[i]
        
    return dow[(total+b) % 7]