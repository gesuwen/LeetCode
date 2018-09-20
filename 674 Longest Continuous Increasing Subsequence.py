# Array

# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
# Note: Length of the array will not exceed 10,000.
class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1
        output, temp = 0, 0
        for i in range(len(nums)):
            if nums[i-1] >= nums[i]:
                temp = i
            output = max(output, i-temp+1)
        return output

        ## Solution 2
        # if nums == []: return 0
        # maxCount, count = 1, 1
        # i = 0
        # while i < len(nums) - 1:
        #     if nums[i+1] > nums[i]:
        #         count = 2
        #         for j in range(i+1, len(nums)-1):
        #             if nums[j+1] > nums[j]:
        #                 count += 1
        #             else:
        #                 i = j
        #                 break
        #         maxCount = max(maxCount, count);
        #     i += 1
        # return maxCount
