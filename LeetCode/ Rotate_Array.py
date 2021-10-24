###################################################################
#  Roate_Array
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
###################################################################

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1