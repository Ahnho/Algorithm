############################################
##              Merge Sort                ##
############################################


# 1. 데이터의 영향을 적게받는다. (데이터와 상관없이 정렬시간은 O(nlog_2 n)으로 동일)
# 2. 레코드를 linked list로 구현하면 링크인덱스만 변경함으로 in place sorting 이 가능해짐 -> 그럴 경우 제일 효과적인 정렬 방법이 된다.
# 3. linked list를 안쓸경우 임시배열을 사용하여야 한다 -> 그럴경우 레코드가 클 경우 레코드의 이동횟수가 많아져 시간이 크게 낭비가 된다 .

def combine(left,right):
    result = []
    
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) :
            if left[0] >= right[0] :
                result.append(right[0])
                right = right[1:]
            else :
                result.append(left[0]) 
                left = left[1:]
        elif len(left) > 0 :
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0 :
            result.append(right[0])
            right = right[1:]
    return result

def Merge_sort(li):
    if len(li) <= 1 : 
        return li
    
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    left = Merge_sort(left)
    right = Merge_sort(right)
    return combine(left,right)

## test 

li = [32,31,41,56,12,67,87,90,231,88,90]
print(Merge_sort(li))
