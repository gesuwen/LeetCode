# Stack

# Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

# Note: n will be less than 15,000.

# Example 1:
# Input: [1, 2, 3, 4]

# Output: False

# Explanation: There is no 132 pattern in the sequence.
# Example 2:
# Input: [3, 1, 4, 2]

# Output: True

# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:
# Input: [-1, 3, 2, 0]

# Output: True

# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        minList = [nums[0]]
        for i in range(1, len(nums)):
            minList.append(min(minList[-1], nums[i]))
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > minList[j]:
                while len(stack) > 0 and stack[-1] <= minList[j]:
                    stack.pop();
                if len(stack) > 0 and stack[-1] < nums[j]:
                    return True;
                stack.append(nums[j]);
        return False