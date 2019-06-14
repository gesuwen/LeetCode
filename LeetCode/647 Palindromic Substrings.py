# String; Dynamic Programming

# Given a string, your task is to count how many palindromic substrings in this string.
#
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
#
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen = len(s)
        output = 0
        for C in range(2*sLen-1):
            L = C // 2
            R = L + C % 2
            while L >= 0 and R < sLen and s[L] == s[R]:
                output += 1
                L -= 1
                R += 1
        return output
