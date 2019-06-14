# Array

# Given an array A of integers, return true if and only if it is a valid mountain array.
#
# Recall that A is a mountain array if and only if:
#
# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[B.length - 1]
#
#
# Example 1:
#
# Input: [2,1]
# Output: false
# Example 2:
#
# Input: [3,5,5]
# Output: false
# Example 3:
#
# Input: [0,3,2,1]
# Output: true
#
#
# Note:
#
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        L, R = 0, len(A)-1
        prevL, prevR = L, R
        while L != R:
            if A[L+1]>A[L]:
                L += 1
            if A[R-1] > A[R]:
                R -= 1
            if L == prevL and R ==prevR:
                return False
            else:
                prevL = L
                prevR = R
        if L == 0 or R == len(A)-1:
            return False
        return True
