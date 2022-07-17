###########################################
##            [1차] 뉴스 클러스터링          ##
###########################################

def inter(a,b):
    sa, sb = set(a) , set(b)
    total = 0
    for i in set(a):
        if i in b:
            total += min(a.count(i), b.count(i))
    return total 

def uni(a,b):
    total = len(a + b)
    li = set(a+b)
    for i in li :
        if i in a and i in b :
            total -= min(a.count(i), b.count(i))
    return total
    

def solution(str1, str2):
    answer = 0
    str1,str2 = str1.lower(), str2.lower()
    arc = [chr(i) for i in range(97,123)]
        
    li_st1 = [] 
    for i in range(0,len(str1)-1):
        a = str1[i:i+2]
        if a[0] in arc and a[1] in arc:
            li_st1.append(a)
        
    li_st2 = [] 
    for i in range(0,len(str2)-1):
        b = str2[i:i+2]
        if b[0] in arc and b[1] in arc:
            li_st2.append(b)
            
    if (not li_st1 and not li_st2) :
        return 65536
    return int((inter(li_st1, li_st2) / uni(li_st1, li_st2))*65536)