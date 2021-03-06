# Array; Two Pointers; Binary Search

# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# Example:
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        numsLen = len(nums)
        output = 2**30
        L = 0
        arrSum = 0
        for i in range(numsLen):
            arrSum += nums[i]
            while arrSum >= s:
                output = min(output, i + 1 - L)
                arrSum -= nums[L]
                L += 1
        if output == 2**30:
            return 0
        return output
    
