##############
#  베스트앨범
# https://school.programmers.co.kr/learn/courses/30/lessons/42579
##############

def solution(genres, plays):
    answer = []
    pl = {}
    sm = {}
    for i,(g,p) in enumerate(zip(genres, plays)):
        if g in pl:
            pl[g].append((p,i))
        else:
            pl[g] = [(p,i)]
            
    for i in pl:
        total = 0
        for p,d in pl[i]:
            total += p
        sm[total] = i

    for i in range(len(pl)):
        li = sorted(pl[sm[max(sm)]])
        print(li)
        del sm[max(sm)]
        if len(li) == 1:
            answer.append(li[-1][1])
        elif len(li) > 1:
            if li[-1][0] == li[-2][0] :
                if li[-1][1] < li[-2][1] :
                    answer.append(li[-1][1])
                    answer.append(li[-2][1])
                else :
                    answer.append(li[-2][1])
                    answer.append(li[-1][1])
            else:
                answer.append(li[-1][1])
                answer.append(li[-2][1])
    return answer
