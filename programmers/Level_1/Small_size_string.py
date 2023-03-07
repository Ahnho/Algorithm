def solution(t, p):
    answer = 0
    pn = len(p)
    ip = int(p)
    for i in range(len(t)-pn+1):
        a = int(t[i:i+pn])
        if a <= ip:
            answer += 1
    return answer
