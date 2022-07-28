###########################################
##            2개 이하로 다른 비트        ##
###########################################

def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            bn = "v0" + bin(num)[2::]
            index = bn.rfind("0")
            bn = bn[:index] + "10" + bn[index+2::]
            answer.append(int(bn[1::],2))
            
    return answer
