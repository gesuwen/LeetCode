# Hash Table

# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        charMap = collections.Counter(list(s))
        freqList = list(charMap.values())
        maxLen = 0
        singleOdd = 0
        for i in range(len(freqList)):
            if freqList[i] % 2 == 0:
                maxLen += freqList[i]
            else:
                maxLen += (freqList[i] // 2 * 2)
                singleOdd = 1
        maxLen += singleOdd
        return maxLen
