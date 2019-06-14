# Backtracking

# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        def permutation(nums):
            if len(nums)==1:
                return [nums]
            res = []
            for idx, val in enumerate(nums):
                remain = nums[:idx] + nums[idx+1:]
                res += [[val]+sol for sol in permutation(remain)]
            return res
        return permutation(nums)
