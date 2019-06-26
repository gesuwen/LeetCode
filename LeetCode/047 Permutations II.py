# Backtracking

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# Example:

# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def allPerms(elements):
            if len(elements) < 2:
                yield elements
            else:
                for perm in allPerms(elements[1:]):
                    for i in range(len(perm) + 1):
                        yield perm[:i] + elements[:1] + perm[i:]
        output = []
        for x in allPerms(nums):
            if x not in output:
                output.append(x)
        return output
        