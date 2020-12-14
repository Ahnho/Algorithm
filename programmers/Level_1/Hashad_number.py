###########################################
##           하샤드 수                    ##
###########################################

def solution(x):
    a = sum(int(i) for i in str(x))
    if x % a == 0 :
        return True
    return False