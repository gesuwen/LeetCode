# Math; Binary search

# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Output: true
# Example 2:
#
# Input: 14
# Output: false
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return True
        elif num < 1: return False
        L, R = 1, num
        while L < R:
            mid = (L+R)//2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num and (mid+1) ** 2 > num:
                return False
            elif mid ** 2 < num:
                L = mid
            else:
                R = mid
