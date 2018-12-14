# Math; Binary Search

# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        elif dividend == 2**31 - 1 and divisor == 1:
            return 2**31 - 1
        neg = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            neg = True
        dividend, divisor = abs(dividend), abs(divisor)
        output = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                multiple <<= 1
                temp <<= 1
            output += multiple
            dividend -= temp
        return -output if neg else output
