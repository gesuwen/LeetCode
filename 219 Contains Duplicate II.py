# Array; Hash Table

# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
#
# Example 1:
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numsMap = {}
        for i in range(len(nums)):
            if nums[i] not in numsMap:
                numsMap[nums[i]] = [i]
            else:
                for j in numsMap[nums[i]]:
                    if (i - j) <= k:
                        return True
                numsMap[nums[i]].append(i)
        return False
