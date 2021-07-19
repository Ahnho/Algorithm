##############
#  전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577
##############


def solution(phone_book):

    for i in range(len(phone_book)):
        for k in range(i+1,len(phone_book)):
            if (phone_book[i] == (phone_book[k])[0:len(phone_book[i])]) or (phone_book[k] == (phone_book[i])[0:len(phone_book[k])]) :
                return False
    return True