# Two pointers; sort

# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
#
# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def isSubseq(s, substr):
            it = iter(s)
            return all(any(c == ch for c in it) for ch in substr)

        maxLen = 0
        output = ""
        for word in d:
            if isSubseq(s, word) and (len(word) > maxLen or (len(word) == maxLen and word < output)):
                maxLen = len(word)
                output = word
        return output
