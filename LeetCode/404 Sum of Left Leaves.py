# Tree

# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def isLeftLeaf(node, outputList):
            if not node:
                return outputList
            elif node.left and (not node.left.left and not node.left.right):
                outputList.append(node.left.val)
            isLeftLeaf(node.left, outputList)
            isLeftLeaf(node.right, outputList)
            return outputList

        outputList = []
        numSum = sum(isLeftLeaf(root, outputList))
        return numSum
