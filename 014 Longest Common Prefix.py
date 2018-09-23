# String

# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        if len(strs) == 0: return output
        pivotWord = strs[0]
        for charInd in range(len(pivotWord)):
            for word in strs:
                if len(word) < charInd+1 or word[charInd] != pivotWord[charInd]:
                    return output
            output += pivotWord[charInd]
        return output
