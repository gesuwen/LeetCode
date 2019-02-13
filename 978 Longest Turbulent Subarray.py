# Array

# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:
#
# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
# That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
#
# Return the length of a maximum size turbulent subarray of A.
#
#
#
# Example 1:
#
# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
# Example 2:
#
# Input: [4,8,12,16]
# Output: 2
# Example 3:
#
# Input: [100]
# Output: 1
#
#
# Note:
#
# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9

class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(set(A)) < 2:
            return 1
        compareList = []
        maxSize = 1
        for i in range(len(A)-1):
            if A[i+1] > A[i]:
                compareList.append(1)
            elif A[i+1] < A[i]:
                compareList.append(0)
            else:
                compareList.append(-1)
        start = 1
        for i in range(len(compareList) - 1):
            currState = compareList[i]
            if (currState == 1 and compareList[i+1] == 0) or (currState == 0 and compareList[i+1] == 1):
                start += 1
                maxSize = max(maxSize, start)
            else:
                start = 1
        return maxSize + 1
