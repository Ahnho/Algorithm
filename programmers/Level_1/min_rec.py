##############
#  나머지가 1이 되는 수 찾기
##############

def solution(sizes):
    mx = []
    mn = []
    for i in sizes:
        mx.append(max(i))
        mn.append(min(i))
    return max(mx) * max(mn)