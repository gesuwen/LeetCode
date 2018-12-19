# Array

# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# Example 1:
#
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:
#
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        curr, start, end = 0, nums[0], nums[0]
        record = []
        while curr < len(nums)-1:
            if nums[curr+1] != nums[curr] + 1:
                end = nums[curr]
                record.append([start, end])
                start = nums[curr+1]
            curr += 1
        end = nums[curr]
        record.append([start, end])
        output = []
        for x, y in record:
            if x==y:
                output.append(str(x))
            else:
                output.append(str(x)+"->"+str(y))
        return output
