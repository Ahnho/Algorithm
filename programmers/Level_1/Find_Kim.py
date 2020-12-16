###########################################
##        서울에서 김서방 찾기              ##
###########################################

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            num = i
            break
    return "김서방은 "+str(num)+"에 있다"