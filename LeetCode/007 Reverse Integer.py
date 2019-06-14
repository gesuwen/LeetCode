# Math

# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNeg = False
        if x < 0:
            isNeg = True
        if isNeg:
            reverseNum = int(str(x)[1:][::-1])
        else:
            reverseNum = int(str(x)[::-1])
        if isNeg:
            reverseNum *= -1
        if reverseNum > (2**31-1) or (reverseNum<-2**31):
            return 0
        return reverseNum
