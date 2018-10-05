# Array; Back tracking; Bit Manipulation

# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
from itertools import combinations

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        for i in range(len(nums)+1):
            combList = list(combinations(nums, i))
            for x in combList:
                output.append(list(x))
        return output
