###################################################################
#  Intersection of Two Arrays II
###################################################################


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for i in nums2:
            if i in nums1:
                answer.append(i)
                del nums1[nums1.index(i)]
        return answer