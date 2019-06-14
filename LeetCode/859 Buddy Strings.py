# String

# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
#
#
#
# Example 1:
#
# Input: A = "ab", B = "ba"
# Output: true
# Example 2:
#
# Input: A = "ab", B = "ab"
# Output: false
# Example 3:
#
# Input: A = "aa", B = "aa"
# Output: true
# Example 4:
#
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:
#
# Input: A = "", B = "aa"
# Output: false
#
#
# Note:
#
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): return False
        if len(A) == len(B) == 2 and A[::-1] == B: return True
        if A == B and len(A)>2 and len(A) - len(set(A)) >= 1: return True
        newA, newB = A, B
        i = 0
        while i < len(newA):
            if newA[i] == newB[i]:
                newA = newA[:i] + newA[i+1:]
                newB = newB[:i] + newB[i+1:]
            else:
                i += 1
        if newA[::-1] == newB and len(newA) > 0:
            return True
        return False
