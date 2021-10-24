###################################################################
#  Two Sum
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
###################################################################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        
        for i in range(len(nums)):
            for k in range(i+1,len(nums)):
                if target == nums[i]+nums[k]:
                    answer.append(i)
                    answer.append(k)
        return answer