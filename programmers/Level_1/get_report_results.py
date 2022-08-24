##############
# 신고 결과 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/92334
##############

def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    ilist = {i : 0 for i in id_list}
    report = list(set(report))
    for r in report:
        ilist[r.split(" ")[1]] += 1
    for w in report:
        li = w.split(" ")
        if ilist[li[1]] >= k :
            answer[id_list.index(li[0])] += 1
            
    return answer
