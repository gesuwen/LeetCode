# Number

# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# Example 1:
#
# Input: "A"
# Output: 1
# Example 2:
#
# Input: "AB"
# Output: 28
# Example 3:
#
# Input: "ZY"
# Output: 701
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(len(s)):
            charInd = alpha.index(s[i*-1-1])+1
            output += charInd * (26**(i))
        return(output)
