# Binary Search; Dynamic Programming; Greedy

# Given a string s and a string t, check if s is subsequence of t.
#
# You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
#
# Example 1:
# s = "abc", t = "ahbgdc"
#
# Return true.
#
# Example 2:
# s = "axc", t = "ahbgdc"
#
# Return false.
#
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
#
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test cases.

class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Solution 1
        # if len(s) == 0:
        #     return True
        # si, ti = 0, 0
        # tLen, sLen = len(t), len(s)
        # while ti < tLen:
        #     if s[si] == t[ti]:
        #         si += 1
        #     if si == sLen:
        #         return True
        #     ti += 1
        # return False
        # Solution 2
        ind = -1
        for char in s:
            ind = t.find(char, ind + 1)
            if ind == -1:
                return False
        return True
