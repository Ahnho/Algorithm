def solution(s):
    answer = []
    for i,st in enumerate(s):
        a = s[0:i]
        if st in a :
            for i in range(len(a)):
                if a[-1-i] == st :
                    answer.append(i+1)
                    break
        else:
            answer.append(-1)
                    
    return answer
