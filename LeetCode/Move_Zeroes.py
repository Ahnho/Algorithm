###################################################################
#  Move Zeroes
###################################################################


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = [i for i in nums]
        for i in range(len(nums)):
            if n[i] == 0:
                nums.append(nums.pop(i-count))
                count += 1
                