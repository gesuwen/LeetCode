# Array; Backtracking

# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        for i in range(len(nums)+1):
            comb = itertools.combinations(nums, i)
            for x in comb:
                curr = sorted(list(x))
                if curr not in output:
                    output.append(curr)
        return output
        
