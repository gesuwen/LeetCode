# Hash Table

# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
#
# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Note: The length of the input array will not exceed 20,000.
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMap = collections.Counter(nums)
        numMapSorted = list(numMap.items())
        numMapSorted.sort(key = operator.itemgetter(0))
        if len(numMapSorted) <= 1:
            return 0
        maxSum = 0
        for i in range(0, len(numMapSorted)-1):
            if numMapSorted[i+1][0] - numMapSorted[i][0] == 1:
                currentSum = numMapSorted[i][1] + numMapSorted[i+1][1]
                if currentSum > maxSum:
                    maxSum = currentSum
        return maxSum
