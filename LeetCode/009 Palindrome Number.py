# Math

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:
#
# Coud you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Solution 1
        #return str(x)[::-1] == str(x)

        # Solution 2 - Without converting the integer to a string
        revertNum = 0
        if (x < 0 or (x % 10 == 0 and x != 0)):
            return False
        while revertNum < x:
            revertNum = int(revertNum * 10 + x % 10)
            x = int(x/10)
        return x == revertNum or x == int(revertNum/10)
