###########################################
##               다트 게임                 ##
###########################################

def solution(dartResult):
    answer = []
    cnt = -1
    for i,v in enumerate(dartResult):
        if v  == "1" and dartResult[i+1] == "0":
            num = 10
            cnt += 1
        elif v  == "0" and dartResult[i-1] == "1":
            continue
        elif ord(v) > 47 and ord(v) < 58 :
            num = int(v)
            cnt += 1
        elif v == "S":
            answer.append(num**1)
        elif v == "D":
            answer.append(num**2)
        elif v == "T":
            answer.append(num**3)
        elif v == "*" :
            if len(answer) == 1:
                answer[cnt] *= 2
            else:
                answer[cnt-1] *= 2
                answer[cnt] *= 2
        elif v == "#" :
            answer[cnt] *= -1
            
    return sum(answer)