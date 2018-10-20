# Binary Search Tree

# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
#
# Example:
#
# Input:
#
#    1
#     \
#      3
#     /
#    2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.minDiff = []
        def travel(node):
            if not node:
                return
            self.minDiff.append(node.val)
            L = travel(node.left)
            R = travel(node.right)
        travel(root)
        self.minDiff = sorted(self.minDiff)
        return min(abs(a - b) for a, b in zip(self.minDiff, self.minDiff[1:]))
