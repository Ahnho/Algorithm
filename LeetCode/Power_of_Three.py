###################################################################
#  Power of Three
###################################################################

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num = 1
        while n > num :
            num *= 3
        if num == n :
            return True
        return False
            