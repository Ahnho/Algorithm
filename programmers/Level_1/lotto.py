##############
#  로또의 최고 순위와 최저 순위
##############

def solution(lottos, win_nums):
    ct = lottos.count(0)
    total_ct = 1
    for i in lottos:
        if i in win_nums:
            total_ct += 1
    if total_ct >= 2:
        total_ct -= 1
    if ct == 6:
        ct -= 1
    answer = [7-total_ct-ct,7-total_ct]
    return answer