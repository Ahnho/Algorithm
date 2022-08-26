##############
# 키패드 누르기
# https://school.programmers.co.kr/learn/courses/30/lessons/67256
##############

def solution(numbers, hand):
    answer = ''
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    L_position= dic['*']
    R_position = dic['#']
    
    for i in numbers:
        now_position = dic[i]
        if i in [1,4,7] : 
            answer += "L"
            L_position = now_position
        elif i in [3,6,9] : 
            answer += "R"
            R_position = now_position
        else:
            le,ra = 0,0
            for l,r,n in zip(L_position,R_position,now_position) :
                le += abs(l-n)
                ra += abs(r-n)
            if le > ra :
                answer += "R"
                R_position = now_position
            elif ra > le :
                answer += "L"
                L_position = now_position
            else:
                if hand == 'right':
                    answer += "R"
                    R_position = now_position
                else:
                    answer += "L"
                    L_position = now_position
    return answer
