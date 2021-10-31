###################################################################
#  Merge Sorted Array
###################################################################

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)-m):
            nums1.pop()
        for j in range(len(nums2)-n):
            nums1.pop()
        for k in nums2:
            nums1.append(k)
        nums1.sort()
        
        