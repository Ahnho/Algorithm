###########################################
##            영어 끝말잇기               ##
###########################################

def solution(n, words):
    word = []
    for a,w in enumerate(words): 
        if a == 0:
            word.append(w)
            continue
        if words[a-1][-1] != w[0] or w in word :
            if (a+1) % n == 0 :
                return [n, a//n+1]
            return [(a+1) % n,a//n+1]
        word.append(w)

    return [0,0]
