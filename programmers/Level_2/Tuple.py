###################################################################
#  튜플                                                         ###
###################################################################

def solution(s):
    answer = []
    st = ""
    for i in s :
        if 48 <= ord(i) <= 57  or i == ',':
            st += i
    st = st.split(',')
    dic = {}
    for e in set(st):
        dic[e] = st.count(e)
    dic = sorted(dic.items(), key = lambda item: item[1], reverse = True)
    for d 
