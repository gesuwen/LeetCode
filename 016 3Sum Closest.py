# Array; Two pointers

# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float("inf")
        for i in range(len(nums)-2):
            L, R = i+1, len(nums)-1
            while L < R:
                curr = nums[i] + nums[L] + nums[R]
                if curr > target:
                    R -= 1
                elif curr < target:
                    L += 1
                else:
                    return target
                if abs(target-curr) < abs(closest-target):
                    closest = curr
        return closest
