# Striog

# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
#
# For example, with A = "abcd" and B = "cdabcdab".
#
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
#
# Note:
# The length of A and B will be between 1 and 10000.
class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # Solution 1
        q = (len(B)-1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1
        # Solution 2
        # concatA = A
        # i = 1
        # while B not in concatA:
        #     concatA += A
        #     i += 1
        #     if i>10000: return -1
        # return i
