##############
#  숫자 문자열과 영단어
##############

def solution(s):
    num = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for i,n in enumerate(num):
        s = str(i).join(s.split(n))
            
    return int(s)