##############
#  부족한 금액 계산하기
##############

def solution(price, money, count):
    total = sum([price*(i+1) for i in range(count)])
    money -= total
    if money >= 0 :
        return 0

    return abs(money)