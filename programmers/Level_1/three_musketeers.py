def solution(number):
    answer = 0
    ln = len(number)
    for i in range(ln):
        for j in range(i+1,ln):
            for k in range(j+1,ln):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer
