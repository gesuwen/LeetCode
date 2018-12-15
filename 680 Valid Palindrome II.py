# String

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L, R = 0, len(s)-1
        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                if s[L+1:R+1] == s[L+1: R+1][::-1] or s[L:R] == s[L:R][::-1]:
                    return True
                else:
                    return False
        return True
