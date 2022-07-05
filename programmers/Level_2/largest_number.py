##########################################################
##                   가장 큰 수           ##
##########################################################


def solution(numbers):
    answer = '' 
    num2 = [str(n)*3 for n in numbers] 
    num3 = list(enumerate(num2)) 
    num3.sort(key = lambda x:x[1]) 
    
    for index, value in num3: 
        answer = str(numbers[index]) + answer
        
    return str(int(answer))