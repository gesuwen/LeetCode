# Math; Binary Search

# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        leftBound = 1
        rightBound = x
        while leftBound <= rightBound:
            m = (leftBound + rightBound) // 2
            if (m ** 2 < x and (m+1) ** 2 > x) or m ** 2 == x:
                return m
            if m ** 2 < x:
                leftBound = m
            elif m ** 2 > x:
                rightBound = m
        return False
