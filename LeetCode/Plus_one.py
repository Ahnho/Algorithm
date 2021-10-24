###################################################################
#  Plus_one
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
###################################################################

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = [str(i) for i in digits]
        print(digits_str)
        total = ""
        for k in digits_str:
            total += k
        total = int(total) + 1
        answer = [int(j) for j in str(total)]
        return answer