# Hash table

# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
#
# American keyboard (image can be found here: https://leetcode.com/problems/keyboard-row/description/)
#
# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        table = {"qwertyuiop":0, "asdfghjkl":0, "zxcvbnm":0}
        output = []
        for word in words:
            for letter in word.lower():
                for key in table:
                    if letter in key:
                        table[key] += 1
            if sum(x > 0 for x in table.values()) == 1:
                output.append(word)
            table = dict.fromkeys(table, 0)
        return output
