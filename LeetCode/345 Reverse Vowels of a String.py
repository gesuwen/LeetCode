# Two Pointers; string

# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
# Input: "hello"
# Output: "holle"
# Example 2:
#
# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow = 'aeiouAEIOU'
        vowList = []
        splitList = re.split('a|e|i|o|u|A|E|I|O|U',s)
        for i in range(len(s)):
            if s[i] in vow:
                vowList.append(s[i])
        output = splitList[0]
        for j in range(1,len(splitList)):
            output = output + vowList[j*-1] + splitList[j]
        return output
