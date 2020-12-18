###########################################
##           비밀 지도                    ##
###########################################

def solution(n, arr1, arr2):
    answer = []
    arr1_li = []
    arr2_li = []
    
    for i in range(n):
        arr1_li.append(str(bin(arr1[i]))[2:])
        arr2_li.append(str(bin(arr2[i]))[2:])
        if len(arr1_li[i]) != n :
            arr1_li[i] = ("0"*(n-len(arr1_li[i]))) + arr1_li[i]
        if len(arr2_li[i]) != n :
            arr2_li[i] = ("0"*(n-len(arr2_li[i]))) + arr2_li[i]

    for j in range(n):
        an = ""
        for k in range(n):
            if arr1_li[j][k] == "0" and arr2_li[j][k] == "0" :
                an += " "
            else :
                an += "#"
        answer.append(an)

    return answer